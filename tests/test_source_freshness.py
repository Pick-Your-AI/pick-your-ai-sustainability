"""Offline checks for the bounded public-source monitor."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]


class SourceFreshnessChecks(unittest.TestCase):
    def setUp(self):
        path = ROOT / 'scripts/check_source_freshness.py'
        self.assertTrue(path.exists(), 'The scheduled source checker is not implemented')
        spec = importlib.util.spec_from_file_location('freshness', path)
        self.checker = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.checker)
        self.now = datetime(2026, 12, 31, 22, 30, tzinfo=timezone.utc)
        self.register = {'check_policy': {'interval_hours': 6}, 'source_count': 1,
                         'sources': [{'url': 'https://provider.example/program',
                                      'opportunity_ids': ['EXAMPLE'], 'last_verified': None,
                                      'next_verification_date': None}]}

    def test_first_check_is_due_now_without_inventing_source_access(self):
        report = self.checker.build_report(self.register, {}, self.now, None)
        row = report['sources'][0]
        self.assertEqual(row['next_check_at'], '2026-12-31T22:30:00Z')
        self.assertIsNone(row['last_checked_at'])
        self.assertEqual(row['outcome'], 'pending')

    def test_actual_attempt_calculates_six_hours_across_year_and_preserves_evidence(self):
        original = copy.deepcopy(self.register)
        result = {'outcome': 'reachable', 'http_status': 200,
                  'final_url': 'https://provider.example/program', 'sha256': 'a' * 64}
        report = self.checker.build_report(self.register, {}, self.now, lambda url, prior: result)
        row = report['sources'][0]
        self.assertEqual(row['next_check_at'], '2027-01-01T04:30:00Z')
        self.assertEqual(row['change'], 'baseline_created')
        self.assertEqual(self.register, original)
        self.assertFalse(row['claim_verified'])

    def test_changed_hash_redirect_and_failed_attempt_keep_previous_content_baseline(self):
        url = self.register['sources'][0]['url']
        previous = {url: {'last_checked_at': '2026-12-31T21:00:00Z',
                          'sha256': 'a' * 64, 'final_url': url, 'etag': 'old'}}
        result = {'outcome': 'reachable', 'http_status': 200, 'final_url': url, 'sha256': 'b' * 64}
        row = self.checker.build_report(self.register, previous, self.now, lambda u, p: result)['sources'][0]
        self.assertEqual(row['change'], 'content_changed')
        result = {'outcome': 'access-blocked', 'http_status': 429, 'final_url': url}
        row = self.checker.build_report(self.register, previous, self.now, lambda u, p: result)['sources'][0]
        self.assertEqual(row['sha256'], 'a' * 64)
        self.assertEqual(row['change'], 'unknown')
        self.assertEqual(row['next_check_at'], '2027-01-01T04:30:00Z')
        result = {'outcome': 'reachable', 'http_status': 200,
                  'final_url': 'https://provider.example/new', 'sha256': 'a' * 64}
        row = self.checker.build_report(self.register, previous, self.now, lambda u, p: result)['sources'][0]
        self.assertEqual(row['change'], 'redirect_changed')

    def test_event_run_checks_even_when_not_due_and_new_sources_ignore_other_state(self):
        url = self.register['sources'][0]['url']
        previous = {url: {'last_checked_at': '2026-12-31T22:00:00Z', 'sha256': 'a' * 64}}
        calls = []
        def check(u, prior):
            calls.append(u)
            return {'outcome': 'reachable', 'http_status': 200, 'final_url': u, 'sha256': 'a' * 64}
        row = self.checker.build_report(self.register, previous, self.now, check)['sources'][0]
        self.assertEqual(calls, [url])
        self.assertEqual(row['change'], 'unchanged')

    def test_private_credentials_and_non_https_destinations_rejected_before_connection(self):
        for url in ('http://example.org/', 'https://user:pass@example.org/',
                    'https://127.0.0.1/', 'https://224.0.0.1/', 'https://[::1]/', 'https://169.254.169.254/',
                    'file:///etc/passwd', 'https://example.org:444/', 'https://example.org/\n'):
            with self.subTest(url=url), self.assertRaises(ValueError):
                self.checker.public_destination(url)
        with patch('socket.getaddrinfo', return_value=[(2, 1, 6, '', ('10.0.0.1', 443))]):
            with self.assertRaises(ValueError):
                self.checker.public_destination('https://example.org/')

    def client(self, responses):
        calls = []
        self.enterContext(patch("socket.getaddrinfo", return_value=[(2, 1, 6, "", ("8.8.8.8", 443))]))
        client = self.checker.SourceClient()
        def request(url, headers=None):
            calls.append((url, headers or {}))
            return responses[url]
        client.request = request
        return client, calls

    def test_robots_disallow_prevents_target_request(self):
        client, calls = self.client({'https://provider.example/robots.txt':
                                   {'status': 200, 'headers': {}, 'body': b'User-agent: *\nDisallow: /program'}})
        result = client.check('https://provider.example/program', {})
        self.assertEqual(result['outcome'], 'access-blocked')
        self.assertEqual(len(calls), 1)

    def test_redirect_rechecks_destination_robots_and_never_bypasses_a_block(self):
        client, calls = self.client({
            'https://provider.example/robots.txt': {'status': 404, 'headers': {}, 'body': b''},
            'https://provider.example/program': {'status': 302, 'headers': {'location': 'https://other.example/new'}, 'body': b''},
            'https://other.example/robots.txt': {'status': 403, 'headers': {}, 'body': b''}})
        result = client.check('https://provider.example/program', {})
        self.assertEqual(result['outcome'], 'access-blocked')
        self.assertIsNone(result['final_url'])
        self.assertEqual([x[0] for x in calls], ['https://provider.example/robots.txt',
                                             'https://provider.example/program', 'https://other.example/robots.txt'])

    def test_conditional_304_preserves_digest_and_sends_no_cookies_or_credentials(self):
        url = 'https://provider.example/program'
        client, calls = self.client({
            'https://provider.example/robots.txt': {'status': 404, 'headers': {}, 'body': b''},
            url: {'status': 304, 'headers': {}, 'body': b''}})
        result = client.check(url, {'sha256': 'a' * 64, 'etag': '"v1"', 'final_url': url})
        self.assertEqual(result['sha256'], 'a' * 64)
        self.assertEqual(result['outcome'], 'unchanged')
        self.assertEqual(calls[-1][1], {'If-None-Match': '"v1"'})

    def test_robots_unavailable_dead_and_challenge_are_distinct(self):
        url = 'https://provider.example/program'
        for status, body, expected in ((404, b'gone', 'dead'), (429, b'', 'access-blocked'),
                                       (200, b'<script src="/_Incapsula_Resource"></script>', 'access-blocked'),
                                       (200, b'public source', 'reachable')):
            with self.subTest(status=status, body=body):
                client, _ = self.client({'https://provider.example/robots.txt':
                                        {'status': 404, 'headers': {}, 'body': b''},
                                        url: {'status': status, 'headers': {}, 'body': body}})
                self.assertEqual(client.check(url, {})['outcome'], expected)

    def test_invalid_timestamp_interval_and_duplicate_sources_fail_before_fetch(self):
        for value in ('2026-10-22', '2026-10-22T03:00:00', 'garbage'):
            with self.assertRaises(ValueError):
                self.checker.parse_time(value)
        for interval in (0, True, 5, '6'):
            self.register['check_policy']['interval_hours'] = interval
            with self.assertRaises(ValueError):
                self.checker.build_report(self.register, {}, self.now, None)
        self.register['check_policy']['interval_hours'] = 6
        self.register['sources'] *= 2
        with self.assertRaises(ValueError):
            self.checker.build_report(self.register, {}, self.now, None)

    def test_conditional_responses_with_different_validators_do_not_share_cache(self):
        client = self.checker.SourceClient()
        self.enterContext(patch('socket.getaddrinfo', return_value=[(2, 1, 6, '', ('8.8.8.8', 443))]))
        from unittest.mock import MagicMock
        connection = MagicMock()
        response = connection.getresponse.return_value.__enter__.return_value
        response.status = 304
        response.getheaders.return_value = []
        response.read.return_value = b''
        with patch.object(self.checker, 'PublicConnection', return_value=connection), patch('time.sleep'):
            client.request('https://example.org/', {'If-None-Match': 'v1'})
            client.request('https://example.org/', {'If-None-Match': 'v2'})
        self.assertEqual(connection.request.call_count, 2)

    def test_politeness_wait_does_not_consume_network_deadline(self):
        import signal
        import time
        from unittest.mock import MagicMock
        client = self.checker.SourceClient()
        client.delays['https://example.org'] = 40
        client.origin_last['https://example.org'] = time.monotonic()
        connection = MagicMock()
        response = connection.getresponse.return_value.__enter__.return_value
        response.status = 200
        response.getheaders.return_value = []
        response.read.return_value = b'public'
        timers = []
        def sleep(delay):
            timers.append(signal.getitimer(signal.ITIMER_REAL)[0])
        with patch('socket.getaddrinfo', return_value=[(2, 1, 6, '', ('8.8.8.8', 443))]), \
                patch.object(self.checker, 'PublicConnection', return_value=connection), patch('time.sleep', side_effect=sleep):
            client.request('https://example.org/')
        self.assertEqual(timers, [0.0])

    def test_slow_response_is_interrupted_by_absolute_deadline(self):
        import signal
        import time
        before = signal.getsignal(signal.SIGALRM)
        with self.assertRaises(TimeoutError):
            with self.checker.request_deadline(0.02):
                time.sleep(0.2)
        self.assertEqual(signal.getsignal(signal.SIGALRM), before)

    def test_budget_skips_preserve_due_time_and_actual_completion_sets_timestamp(self):
        url = self.register['sources'][0]['url']
        previous = {url: {'last_checked_at': '2026-12-31T12:00:00Z'}}
        report = self.checker.build_report(self.register, previous, self.now,
                                          lambda u, p: {'outcome': 'budget-exhausted'})
        self.assertEqual(report['sources'][0]['last_checked_at'], '2026-12-31T12:00:00Z')
        self.assertEqual(report['sources'][0]['next_check_at'], '2026-12-31T18:00:00Z')
        completion = datetime(2026, 12, 31, 23, 45, tzinfo=timezone.utc)
        row = self.checker.build_report(self.register, {}, self.now,
                lambda u, p: {'outcome': 'access-error'}, clock=lambda: completion)['sources'][0]
        self.assertEqual(row['last_checked_at'], '2026-12-31T23:45:00Z')
        self.assertEqual(row['next_check_at'], '2027-01-01T05:45:00Z')

    def test_oversize_and_html_robots_do_not_become_content_baselines(self):
        url = 'https://provider.example/program'
        client, _ = self.client({'https://provider.example/robots.txt':
            {'status': 200, 'headers': {'content-type': 'text/html'}, 'body': b'<html>unavailable</html>'}, url: {'status': 200, 'headers': {}, 'body': b'public'}})
        self.assertEqual(client.check(url, {})['outcome'], 'access-blocked')
        client, _ = self.client({'https://provider.example/robots.txt':
            {'status': 404, 'headers': {}, 'body': b''}, url:
            {'status': 200, 'headers': {}, 'body': b'partial', 'truncated': True}})
        result = client.check(url, {})
        self.assertEqual(result['outcome'], 'partial')
        self.assertNotIn('sha256', result)

    def test_plan_cli_writes_all_due_sources_and_never_changes_register_bytes(self):
        import subprocess
        import sys
        with tempfile.TemporaryDirectory() as directory:
            register = Path(directory) / 'register.json'
            report = Path(directory) / 'report.json'
            data = json.dumps(self.register).encode()
            register.write_bytes(data)
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/check_source_freshness.py'),
                                     '--register', str(register), '--output', str(report), '--plan'],
                                    text=True, capture_output=True, check=False)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(register.read_bytes(), data)
            value = json.loads(report.read_text())
            self.assertEqual(value['mode'], 'plan')
            self.assertEqual(len(value['sources']), 1)
            self.assertIsNone(value['sources'][0]['last_checked_at'])
            self.assertEqual(value['sources'][0]['next_check_at'], value['generated_at'])

    def test_previous_artifact_uses_only_fixed_bounded_report_member(self):
        import zipfile
        with tempfile.TemporaryDirectory() as directory:
            archive = Path(directory) / 'previous.zip'
            with zipfile.ZipFile(archive, 'w') as z:
                z.writestr('../escape', 'do not extract')
                z.writestr('freshness-report.json', json.dumps({'schema_version': 'source-checks/v1', 'sources': [
                    {'url': 'https://provider.example/program', 'last_checked_at': '2026-12-31T22:00:00Z', 'sha256': 'a' * 64}]}))
            baseline = self.checker.load_previous(archive)
            self.assertIn('https://provider.example/program', baseline)
            self.assertFalse((Path(directory).parent / 'escape').exists())


class FreshnessWorkflowChecks(unittest.TestCase):
    def test_only_successful_canonical_main_workflow_runs_can_supply_baselines(self):
        import yaml
        import re
        import subprocess
        workflow = yaml.safe_load((ROOT / '.github/workflows/source-freshness.yml').read_text())
        step = next(x for x in workflow['jobs']['freshness']['steps'] if x['name'] == 'Restore latest main-branch check baseline')
        query = re.findall(r"--jq '([^']*)'", step['run'])[0]
        trusted = {'id': 10, 'head_branch': 'main', 'event': 'schedule', 'status': 'completed',
                   'conclusion': 'success', 'head_repository': {'full_name': 'Pick-Your-AI/pick-your-ai-sustainability'}}
        malicious = {**trusted, 'id': 99, 'event': 'pull_request', 'head_repository': {'full_name': 'attacker/fork'}}
        failed = {**trusted, 'id': 98, 'conclusion': 'failure'}
        process = subprocess.run(['jq', '-r', query], input=json.dumps({'workflow_runs': [malicious, failed, trusted]}),
                                 text=True, capture_output=True, check=True)
        self.assertEqual(process.stdout.strip(), '10')

    def test_workflow_is_read_only_and_prs_only_plan_without_live_source_access(self):
        import yaml
        workflow = yaml.safe_load((ROOT / '.github/workflows/source-freshness.yml').read_text())
        events = workflow.get('on', workflow.get(True))
        self.assertEqual(events['schedule'][0]['cron'], '23 */6 * * *')
        self.assertIn('data/**', events['push']['paths'])
        self.assertIn('research/**', events['push']['paths'])
        self.assertNotIn('pull_request_target', events)
        self.assertEqual(workflow['permissions'], {'contents': 'read', 'actions': 'read'})
        steps = workflow['jobs']['freshness']['steps']
        for step in steps:
            if 'uses' in step:
                self.assertRegex(step['uses'], r'^actions/[a-z-]+@[0-9a-f]{40}$')
        live = next(x for x in steps if x['name'] == 'Check public sources and calculate next timestamps')
        self.assertIn("github.event_name != 'pull_request'", live['if'])
        self.assertIn("github.ref == 'refs/heads/main'", live['if'])
        self.assertNotIn('env', live)
