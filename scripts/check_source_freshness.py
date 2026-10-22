#!/usr/bin/env python3
"""Monitor public source changes without certifying claims or modifying evidence."""
import argparse
from collections import Counter
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
import hashlib
import http.client
import ipaddress
import json
import os
from pathlib import Path
import re
import signal
import socket
import ssl
import time
from urllib.parse import urljoin, urlsplit, urlunsplit
from urllib.robotparser import RobotFileParser
import zipfile

USER_AGENT = 'Pick-Your-AI-Freshness/1.0 (+https://github.com/Pick-Your-AI/pick-your-ai-sustainability)'
MAX_BYTES = 2_000_000
REDIRECTS = {301, 302, 303, 307, 308}


def stamp(value):
    return value.astimezone(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')


def parse_time(value):
    result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if result.tzinfo is None:
        raise ValueError('Check timestamps require an explicit timezone')
    return result.astimezone(timezone.utc)


@contextmanager
def request_deadline(seconds):
    def expired(signum, frame):
        raise TimeoutError('Absolute request deadline exceeded')
    previous = signal.signal(signal.SIGALRM, expired)
    signal.setitimer(signal.ITIMER_REAL, max(0.001, seconds))
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous)


def https_parts(url):
    if not isinstance(url, str) or any(ord(c) <= 32 or ord(c) == 127 for c in url):
        raise ValueError('URL contains whitespace or controls')
    parts = urlsplit(url)
    if (parts.scheme != 'https' or not parts.hostname or parts.username is not None
            or parts.password is not None or parts.port not in (None, 443)):
        raise ValueError('Only public HTTPS URLs without credentials on port 443 are permitted')
    return parts


def public_destination(url):
    parts = https_parts(url)
    addresses = socket.getaddrinfo(parts.hostname, 443, type=socket.SOCK_STREAM)
    if not addresses or any(not ipaddress.ip_address(a[4][0]).is_global or ipaddress.ip_address(a[4][0]).is_multicast for a in addresses):
        raise ValueError('Destination resolves to a non-public address')
    return parts, addresses[0][4][0]


class PublicConnection(http.client.HTTPSConnection):
    def __init__(self, host, address):
        super().__init__(host, timeout=15, context=ssl.create_default_context())
        self.address = address

    def connect(self):
        # Connect to the already validated address; retain hostname for TLS/SNI.
        sock = socket.create_connection((self.address, 443), self.timeout)
        try:
            self.sock = self._context.wrap_socket(sock, server_hostname=self.host)
        except Exception:
            sock.close()
            raise


class SourceClient:
    def __init__(self, budget_seconds=2100):
        self.deadline = time.monotonic() + budget_seconds
        self.last_request = 0
        self.origin_last = {}
        self.delays = {}
        self.robots = {}
        self.responses = {}

    def request(self, url, headers=None):
        key = (url, tuple(sorted((headers or {}).items())))
        if key in self.responses:
            return self.responses[key]
        with request_deadline(min(30, self.deadline - time.monotonic())):
            parts, address = public_destination(url)
        origin = f'https://{parts.netloc}'
        delay = max(0, 2 - (time.monotonic() - self.last_request),
                    self.delays.get(origin, 2) - (time.monotonic() - self.origin_last.get(origin, 0)))
        if time.monotonic() + delay + 15 >= self.deadline:
            raise TimeoutError('Run budget exhausted')
        time.sleep(delay)
        self.last_request = self.origin_last[origin] = time.monotonic()
        with request_deadline(min(30, self.deadline - time.monotonic())):
            connection = PublicConnection(parts.hostname, address)
            try:
                path = urlunsplit(('', '', parts.path or '/', parts.query, ''))
                request_headers = {'User-Agent': USER_AGENT, 'Accept-Encoding': 'identity'}
                request_headers.update(headers or {})
                connection.request('GET', path, headers=request_headers)
                with connection.getresponse() as response:
                    body = response.read(MAX_BYTES + 1)
                    result = {'status': response.status,
                              'headers': {k.lower(): v for k, v in response.getheaders()},
                              'body': body, 'truncated': len(body) > MAX_BYTES}
            finally:
                connection.close()
        self.responses[key] = result
        return result

    def allowed(self, url):
        parts = urlsplit(url)
        origin = f'{parts.scheme}://{parts.netloc}'
        if origin not in self.robots:
            robots_url = origin + '/robots.txt'
            visited = set()
            for _ in range(6):
                if robots_url in visited:
                    break
                visited.add(robots_url)
                result = self.request(robots_url)
                status = result['status']
                if status in REDIRECTS and result['headers'].get('location'):
                    robots_url = urljoin(robots_url, result['headers']['location'])
                    continue
                if status in (404, 410):
                    self.robots[origin] = True
                elif (status == 200 and not result.get('truncated')
                      and 'text/html' not in result['headers'].get('content-type', '').lower()
                      and not result['body'].lstrip().lower().startswith((b'<html', b'<!doctype'))):
                    parser = RobotFileParser()
                    parser.parse(result['body'].decode('utf-8', errors='replace').splitlines())
                    delay = parser.crawl_delay(USER_AGENT) or 2
                    rate = parser.request_rate(USER_AGENT)
                    if rate and rate.requests:
                        delay = max(delay, rate.seconds / rate.requests)
                    self.delays[origin] = max(2, delay)
                    self.robots[origin] = parser if delay <= 60 else False
                else:
                    self.robots[origin] = False
                break
            self.robots.setdefault(origin, False)
        policy = self.robots[origin]
        return policy if isinstance(policy, bool) else policy.can_fetch(USER_AGENT, url)

    def check(self, url, prior):
        current = url
        chain = []
        try:
            for _ in range(6):
                # Validate before either cache lookup or robots evaluation.
                https_parts(current)
                if not self.allowed(current):
                    return {'outcome': 'access-blocked', 'http_status': None, 'final_url': None,
                            'stopped_at_url': current, 'redirects': chain,
                            'reason': 'Robots denied or unavailable; target not requested'}
                headers = {}
                if prior.get('sha256') and (prior.get('content_final_url') or prior.get('final_url')) == current:
                    for field, header in (('etag', 'If-None-Match'), ('last_modified', 'If-Modified-Since')):
                        value = prior.get(field)
                        if isinstance(value, str) and len(value) <= 1024 and not any(ord(c) < 32 or ord(c) == 127 for c in value):
                            headers[header] = value
                result = self.request(current, headers)
                status = result['status']
                location = result['headers'].get('location')
                if status in REDIRECTS and location:
                    chain.append({'url': current, 'http_status': status, 'location': location})
                    current = urljoin(current, location)
                    continue
                observation = {'http_status': status, 'final_url': current, 'redirects': chain}
                if status == 304 and prior.get('sha256') and (prior.get('content_final_url') or prior.get('final_url')) == current:
                    return {**observation, 'outcome': 'unchanged', 'sha256': prior['sha256'],
                            'etag': prior.get('etag'), 'last_modified': prior.get('last_modified')}
                if status in (401, 403, 429):
                    return {**observation, 'outcome': 'access-blocked'}
                if status in (404, 410):
                    return {**observation, 'outcome': 'dead'}
                if not 200 <= status < 300:
                    return {**observation, 'outcome': 'access-error'}
                if result.get('truncated'):
                    return {**observation, 'outcome': 'partial', 'reason': 'Response exceeds 2 MB; no comparable digest'}
                body = result['body']
                if any(marker in body.lower() for marker in
                       (b'_incapsula_resource', b'cf-chl-', b'just a moment...', b'verify you are human')):
                    return {**observation, 'outcome': 'access-blocked', 'reason': 'Challenge response; no bypass attempted'}
                return {**observation, 'outcome': 'reachable', 'sha256': hashlib.sha256(body).hexdigest(),
                        'bytes': len(body), 'content_type': result['headers'].get('content-type'),
                        'etag': result['headers'].get('etag'),
                        'last_modified': result['headers'].get('last-modified')}
            return {'outcome': 'access-error', 'http_status': None, 'final_url': None,
                    'redirects': chain, 'reason': 'Redirect limit exceeded'}
        except (OSError, ValueError, http.client.HTTPException) as error:
            return {'outcome': 'budget-exhausted' if isinstance(error, TimeoutError) and (str(error) == 'Run budget exhausted' or time.monotonic() >= self.deadline) else 'access-error',
                    'http_status': None, 'final_url': None, 'redirects': chain,
                    'reason': str(error)}


def load_previous(path):
    if path is None or not path.exists():
        return {}
    with zipfile.ZipFile(path) as archive:
        info = archive.getinfo('freshness-report.json')
        if info.file_size > 20_000_000:
            raise ValueError('Previous report exceeds size limit')
        previous = json.loads(archive.read(info))
    if previous.get('schema_version') != 'source-checks/v1':
        raise ValueError('Unknown previous report schema')
    result = {}
    for row in previous['sources']:
        url = row['url']
        if url in result:
            raise ValueError('Duplicate previous source URL')
        if row.get('last_checked_at'):
            parse_time(row['last_checked_at'])
        if row.get('sha256') and not re.fullmatch('[0-9a-f]{64}', row['sha256']):
            raise ValueError('Invalid previous digest')
        result[url] = row
    return result


def build_report(register, previous, now, check, clock=None):
    if register.get('check_policy', {}).get('interval_hours') != 6 or type(register['check_policy']['interval_hours']) is not int:
        raise ValueError('Authorized source-check interval must be six hours')
    sources = register['sources']
    if len({row['url'] for row in sources}) != len(sources) or register['source_count'] != len(sources):
        raise ValueError('Source URLs must be unique and match source_count')
    report = {'schema_version': 'source-checks/v1', 'generated_at': stamp(now),
              'interval_hours': 6, 'mode': 'check' if check else 'plan', 'sources': []}
    for source in sources:
        url = source['url']
        prior = previous.get(url, {})
        last_checked = prior.get('last_checked_at')
        if last_checked:
            last_checked = parse_time(last_checked)
        next_check = last_checked + timedelta(hours=6) if last_checked else now
        row = {'url': url, 'opportunity_ids': source['opportunity_ids'],
               'last_checked_at': stamp(last_checked) if last_checked else None,
               'next_check_at': stamp(next_check), 'outcome': 'pending',
               'claim_verified': False, 'change': 'unknown'}
        if check:
            result = check(url, prior)
            checked_at = clock() if clock else now
            row.update(result)
            if result['outcome'] != 'budget-exhausted':
                row.update(last_checked_at=stamp(checked_at), next_check_at=stamp(checked_at + timedelta(hours=6)))
            if result['outcome'] in ('reachable', 'unchanged'):
                row['change'] = ('baseline_created' if not prior.get('sha256') else
                                 'redirect_changed' if (prior.get('content_final_url') or prior.get('final_url')) and (prior.get('content_final_url') or prior['final_url']) != result.get('final_url') else
                                 'content_changed' if prior['sha256'] != result.get('sha256') else 'unchanged')
                row['content_checked_at'] = stamp(checked_at)
                row['content_final_url'] = result.get('final_url')
            else:
                for key in ('sha256', 'etag', 'last_modified', 'content_checked_at', 'content_final_url'):
                    if key in prior:
                        row[key] = prior[key]
        report['sources'].append(row)
    report['outcomes'] = dict(Counter(row['outcome'] for row in report['sources']))
    report['changes'] = dict(Counter(row['change'] for row in report['sources']))
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--register', type=Path, default=Path('data/research-freshness.json'))
    parser.add_argument('--previous-archive', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--plan', action='store_true', help='Calculate due times without network requests')
    args = parser.parse_args()
    previous = load_previous(args.previous_archive)
    register = json.loads(args.register.read_text())
    client = SourceClient()
    report = build_report(register, previous, datetime.now(timezone.utc), None if args.plan else client.check, clock=lambda: datetime.now(timezone.utc))
    report['revision'] = os.environ.get('GITHUB_SHA')
    report['run_id'] = os.environ.get('GITHUB_RUN_ID')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    summary = ('Source freshness ' + report['mode'] + '\n\n'
               + f'Sources: {len(report["sources"])}; interval: 6 hours (UTC).\n\n'
               + 'Outcomes: ' + json.dumps(report['outcomes']) + '\n\n'
               + 'Changes: ' + json.dumps(report['changes']) + '\n\n'
               + 'Download freshness-report.json for per-source next_check_at and limitations. '
               + 'HTTP success/change detection does not verify cited claims.\n')
    print(summary)
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as stream:
            stream.write(summary)
    return 1 if report['outcomes'].get('budget-exhausted') else 0


if __name__ == '__main__':
    raise SystemExit(main())
