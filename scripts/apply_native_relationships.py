#!/usr/bin/env python3
"""Apply only the pinned sustainability issue hierarchy and hard dependencies.

Default mode validates local intent only. --apply additionally requires the exact
same-repository GitHub Actions pull_request context and its GITHUB_TOKEN. No API
PATCH or DELETE is implemented. Uncertain writes are never retried automatically.
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

REPOSITORY = "Pick-Your-AI/pick-your-ai-sustainability"
ACTOR = "CompleteDotTech"
ACTOR_ID = 5861166
HEAD_BRANCH = "sustainability/program-foundation"
PR_NUMBER = 73
API_VERSION = "2026-03-10"
API_ROOT = "https://api.github.com"
PREFIX = f"/repos/{REPOSITORY}"
PLAN_SHA256 = "87f40e822422cefc52f92c55acd419b1bc5a438055f6b2399273e479ceebbaec"
MAX_REQUESTS = 900
MIN_WRITE_INTERVAL = 1.25
EXPECTED_COUNTS = {"issues": 72, "parent_child": 71, "blocked_by": 43}


class Refusal(RuntimeError):
    """A failed validation stops execution without repairing unrelated state."""


def require(condition, message):
    if not condition:
        raise Refusal(message)


def canonical_bytes(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def load_plan(path):
    registry = json.loads(Path(path).read_text())
    identities = registry["native_issue_id_verification"]["issues"]
    plan = {
        "repository": REPOSITORY,
        "issues": [
            {key: item[key] for key in ("key", "number", "id", "html_url")}
            for item in sorted(identities, key=lambda item: item["number"])
        ],
        "parent_child": sorted([
            [edge["parent_issue_number"], edge["child_issue_number"]]
            for edge in registry["parent_child"]
        ]),
        "blocked_by": sorted([
            [edge["blocked_issue_number"], edge["blocking_issue_number"]]
            for edge in registry["hard_dependencies"]
        ]),
    }
    require(hashlib.sha256(canonical_bytes(plan)).hexdigest() == PLAN_SHA256,
            "Registry identities or graph differ from the pinned 72/71/43 plan")
    require({key: len(plan[key]) for key in EXPECTED_COUNTS} == EXPECTED_COUNTS,
            "Unexpected plan counts")
    by_number = {item["number"]: item for item in plan["issues"]}
    by_key = {item["key"]: item for item in plan["issues"]}
    require(len(by_number) == 72 and len(by_key) == 72, "Duplicate issue identity")
    require(len({item["id"] for item in plan["issues"]}) == 72,
            "Duplicate native numeric issue ID")
    for item in plan["issues"]:
        require(type(item["id"]) is int and item["id"] > 0,
                "Native issue IDs must be positive integers")
        require(item["html_url"] == f"https://github.com/{REPOSITORY}/issues/{item['number']}",
                "A mapped issue URL is outside the authorized repository")
    for family, sides in (("parent_child", ("parent", "child")),
                          ("hard_dependencies", ("blocked", "blocking"))):
        for edge in registry[family]:
            for side in sides:
                item = by_key[edge[f"{side}_key"]]
                require(edge[f"{side}_issue_number"] == item["number"] and
                        edge[f"{side}_issue_id"] == item["id"] and
                        edge[f"{side}_issue_url"] == item["html_url"],
                        "An edge contains inconsistent native issue identity fields")
    for family in ("parent_child", "blocked_by"):
        edges = [tuple(edge) for edge in plan[family]]
        require(len(set(edges)) == len(edges), f"Duplicate {family} edge")
        require(all(a in by_number and b in by_number and a != b for a, b in edges),
                f"Invalid {family} endpoint")
        graph = {number: [] for number in by_number}
        for a, b in edges:
            graph[a].append(b)
        visiting, done = set(), set()

        def visit(number):
            require(number not in visiting, f"Cycle in {family}")
            if number in done:
                return
            visiting.add(number)
            for child in graph[number]:
                visit(child)
            visiting.remove(number)
            done.add(number)

        for number in graph:
            visit(number)
    require({child for _, child in plan["parent_child"]} == set(by_number) - {1},
            "Every issue except PROGRAM must have exactly its declared parent")
    return plan


def validate_event(event, env):
    pr = event.get("pull_request", {})
    head, base = pr.get("head", {}), pr.get("base", {})
    user = pr.get("user", {})
    sender = event.get("sender", {})
    require(env.get("GITHUB_ACTIONS") == "true", "Apply requires GitHub Actions")
    require(env.get("GITHUB_EVENT_NAME") == "pull_request", "Only pull_request is allowed")
    require(env.get("GITHUB_REPOSITORY") == REPOSITORY and
            event.get("repository", {}).get("full_name") == REPOSITORY,
            "Wrong repository")
    require(env.get("GITHUB_ACTOR") == ACTOR and
            str(env.get("GITHUB_ACTOR_ID")) == str(ACTOR_ID) and
            env.get("GITHUB_TRIGGERING_ACTOR") == ACTOR,
            "Unexpected triggering or rerun actor")
    require(sender.get("login") == ACTOR and sender.get("id") == ACTOR_ID,
            "Unexpected event sender")
    require(event.get("action") in {"opened", "synchronize", "reopened", "ready_for_review"},
            "Unexpected pull request activity")
    require(event.get("number") == PR_NUMBER and pr.get("number") == PR_NUMBER and
            pr.get("state") == "open" and not pr.get("merged"),
            "Only the open foundation PR #73 is allowed")
    require(user.get("login") == ACTOR and user.get("id") == ACTOR_ID,
            "Unexpected pull request author")
    require(head.get("repo", {}).get("full_name") == REPOSITORY and
            head.get("repo", {}).get("fork") is False and head.get("ref") == HEAD_BRANCH,
            "The head must be the exact same-repository foundation branch")
    require(base.get("repo", {}).get("full_name") == REPOSITORY and base.get("ref") == "main",
            "Unexpected pull request base")
    sha = head.get("sha", "")
    require(bool(re.fullmatch(r"[0-9a-f]{40}", sha)), "Invalid head commit SHA")
    return sha


class NoRedirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class Api:
    def __init__(self, token, plan):
        require(bool(token), "GITHUB_TOKEN is required for live access")
        self.token = token
        self.plan = plan
        self.ids = {item["number"]: item["id"] for item in plan["issues"]}
        self.allowed_posts = {}
        for parent, child in plan["parent_child"]:
            route = f"{PREFIX}/issues/{parent}/sub_issues"
            self.allowed_posts.setdefault(route, set()).add(canonical_bytes({
                "sub_issue_id": self.ids[child], "replace_parent": False,
            }))
        for blocked, blocking in plan["blocked_by"]:
            route = f"{PREFIX}/issues/{blocked}/dependencies/blocked_by"
            self.allowed_posts.setdefault(route, set()).add(canonical_bytes({"issue_id": self.ids[blocking]}))
        self.opener = urllib.request.build_opener(NoRedirects())
        self.requests = 0
        self.remaining = None
        self.last_write = 0.0
        self.last_link = ""

    def request(self, method, route, payload=None, allow_missing_parent=False):
        require(route.startswith(PREFIX + "/"), "API route is outside the authorized repository")
        if method == "POST":
            require(canonical_bytes(payload) in self.allowed_posts.get(route, set()),
                    "Attempted write is not a pinned relationship")
            pause = MIN_WRITE_INTERVAL - (time.monotonic() - self.last_write)
            if pause > 0:
                time.sleep(pause)
            self.last_write = time.monotonic()
        else:
            require(method == "GET" and payload is None, "Only GET and declared POST are implemented")
        require(self.requests < MAX_REQUESTS, "Per-run API request cap reached")
        require(self.remaining is None or self.remaining > 5,
                "Insufficient rate limit budget; rerun after reset without changing permissions")
        self.requests += 1
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.token}",
            "X-GitHub-Api-Version": API_VERSION,
            "User-Agent": "Pick-Your-AI-native-relationship-setup",
        }
        data = None if payload is None else canonical_bytes(payload)
        if data is not None:
            headers["Content-Type"] = "application/json"
        request = urllib.request.Request(API_ROOT + route, data=data, headers=headers, method=method)
        try:
            with self.opener.open(request, timeout=30) as response:
                if response.headers.get("X-RateLimit-Remaining"):
                    self.remaining = int(response.headers["X-RateLimit-Remaining"])
                self.last_link = response.headers.get("Link", "")
                status = response.status
                result = json.loads(response.read())
        except urllib.error.HTTPError as error:
            if error.headers.get("X-RateLimit-Remaining"):
                self.remaining = int(error.headers["X-RateLimit-Remaining"])
            if allow_missing_parent and method == "GET" and error.code == 404 and route.endswith("/parent"):
                return None
            request_id = error.headers.get("X-GitHub-Request-Id", "unknown")
            retry_after = error.headers.get("Retry-After", "not supplied")
            raise Refusal(f"{method} {route}: HTTP {error.code}; request {request_id}; "
                          f"Retry-After {retry_after}. No automatic write retry or permission change.") from None
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as error:
            raise Refusal(f"{method} {route}: uncertain result ({type(error).__name__}); "
                          "no automatic write retry") from None
        require(status == (201 if method == "POST" else 200),
                f"Unexpected HTTP {status} from {method} {route}")
        return result

    def get(self, route, allow_missing_parent=False):
        return self.request("GET", route, allow_missing_parent=allow_missing_parent)

    def collection(self, route):
        result = []
        separator = "&" if "?" in route else "?"
        next_route = f"{route}{separator}per_page=100"
        for _ in range(5):
            batch = self.get(next_route)
            require(isinstance(batch, list), "Expected a paginated issue array")
            result.extend(batch)
            next_link = re.search(r'<([^>]+)>;\s*rel="next"', self.last_link)
            if not next_link:
                return result
            url = urlsplit(next_link.group(1))
            require(url.scheme == "https" and url.netloc == "api.github.com" and
                    url.path.startswith(PREFIX + "/") and not url.fragment,
                    "Pagination link leaves the authorized GitHub repository")
            next_route = url.path + ("?" + url.query if url.query else "")
        raise Refusal("Collection exceeded the bounded pagination limit")


def verify_head(api, sha):
    ref = api.get(f"{PREFIX}/git/ref/heads/{HEAD_BRANCH}")
    require(ref.get("object", {}).get("sha") == sha, "Foundation branch moved; use its current PR run")
    commit = api.get(f"{PREFIX}/commits/{sha}")
    require(commit.get("sha") == sha and
            (commit.get("author") or {}).get("login") == ACTOR and
            (commit.get("author") or {}).get("id") == ACTOR_ID,
            "Head commit must resolve through GitHub to the authorized author CompleteDotTech")


def expected_graph(plan):
    graph = {item["number"]: {"parent": None, "sub_issues": set(),
             "blocked_by": set(), "blocking": set()} for item in plan["issues"]}
    for parent, child in plan["parent_child"]:
        require(graph[child]["parent"] is None, "Multiple intended parents")
        graph[child]["parent"] = parent
        graph[parent]["sub_issues"].add(child)
    for blocked, blocking in plan["blocked_by"]:
        graph[blocked]["blocked_by"].add(blocking)
        graph[blocking]["blocking"].add(blocked)
    return graph


def verify_identities(api, plan):
    current = {issue["number"]: issue for issue in api.collection(f"{PREFIX}/issues?state=all&sort=created&direction=asc")}
    for item in plan["issues"]:
        issue = current.get(item["number"], {})
        require(not issue.get("pull_request") and issue.get("id") == item["id"] and
                issue.get("html_url") == item["html_url"] and
                f"<!-- sustainability-key: {item['key']} -->" in (issue.get("body") or ""),
                f"Live identity mismatch for {item['key']} #{item['number']}")


def number_from_issue(issue, plan):
    number = issue.get("number")
    identities = {item["number"]: item for item in plan["issues"]}
    expected = identities.get(number)
    require(expected is not None and issue.get("id") == expected["id"] and
            issue.get("html_url") == expected["html_url"],
            "Native relationship refers to an unexpected issue: " + str(issue.get("html_url")))
    return number


def read_set(api, plan, number, relation):
    suffix = "sub_issues" if relation == "sub_issues" else "dependencies/" + relation
    issues = api.collection(f"{PREFIX}/issues/{number}/{suffix}")
    numbers = [number_from_issue(issue, plan) for issue in issues]
    require(len(numbers) == len(set(numbers)), f"Duplicate native relation on #{number}")
    return set(numbers)


def read_parent(api, plan, number):
    parent = api.get(f"{PREFIX}/issues/{number}/parent", allow_missing_parent=True)
    return None if parent is None else number_from_issue(parent, plan)


def snapshot(api, plan, expected, require_complete=False):
    actual = {}
    for number in sorted(expected):
        row = {"parent": read_parent(api, plan, number)}
        for relation in ("sub_issues", "blocked_by", "blocking"):
            row[relation] = read_set(api, plan, number, relation)
        want = expected[number]
        require(row["parent"] is None or row["parent"] == want["parent"],
                f"Unexpected parent on #{number}; no replacement is permitted")
        for relation in ("sub_issues", "blocked_by", "blocking"):
            require(row[relation] <= want[relation],
                    f"Unexpected {relation} edges on #{number}: {sorted(row[relation] - want[relation])}")
        if require_complete:
            require(row == want, f"Incomplete final native readback for #{number}")
        actual[number] = row
    # Reject inconsistent reads before any write. Rerunning starts from a fresh snapshot.
    for number, row in actual.items():
        if row["parent"] is not None:
            require(number in actual[row["parent"]]["sub_issues"], "Parent/sub-issue readback disagreement")
        for child in row["sub_issues"]:
            require(actual[child]["parent"] == number, "Sub-issue/parent readback disagreement")
        for blocker in row["blocked_by"]:
            require(number in actual[blocker]["blocking"], "Blocked-by/blocking readback disagreement")
        for blocked in row["blocking"]:
            require(number in actual[blocked]["blocked_by"], "Blocking/blocked-by readback disagreement")
    return actual


def serializable_graph(graph):
    return {str(number): {key: sorted(value) if isinstance(value, set) else value
                         for key, value in row.items()} for number, row in graph.items()}


def apply_missing(api, plan, expected, before, report):
    by_number = {item["number"]: item for item in plan["issues"]}
    for parent, child in plan["parent_child"]:
        if before[child]["parent"] == parent:
            report["skipped_existing"].append({"kind": "parent_child", "parent": parent, "child": child})
            continue
        current_parent = read_parent(api, plan, child)
        require(current_parent in (None, parent), f"Parent changed on #{child}; refusing to move it")
        if current_parent == parent:
            report["skipped_existing"].append({"kind": "parent_child", "parent": parent, "child": child})
            continue
        operation = {"kind": "parent_child", "parent": parent, "child": child,
                     "payload_id": by_number[child]["id"], "result": "attempting"}
        report["mutations"].append(operation)
        api.request("POST", f"{PREFIX}/issues/{parent}/sub_issues",
                    {"sub_issue_id": by_number[child]["id"], "replace_parent": False})
        operation["result"] = "http_201_pending_final_readback"
    for blocked, blocking in plan["blocked_by"]:
        current = read_set(api, plan, blocked, "blocked_by")
        require(current <= expected[blocked]["blocked_by"],
                f"Unexpected blocker appeared on #{blocked}; refusing further writes")
        if blocking in current:
            report["skipped_existing"].append({"kind": "blocked_by", "blocked": blocked, "blocking": blocking})
            continue
        operation = {"kind": "blocked_by", "blocked": blocked, "blocking": blocking,
                     "payload_id": by_number[blocking]["id"], "result": "attempting"}
        report["mutations"].append(operation)
        api.request("POST", f"{PREFIX}/issues/{blocked}/dependencies/blocked_by",
                    {"issue_id": by_number[blocking]["id"]})
        operation["result"] = "http_201_pending_final_readback"


def save_report(report, path):
    report["finished_at"] = datetime.now(timezone.utc).isoformat()
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(text)
    print(text)
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a") as stream:
            stream.write("## Native sustainability relationships\n\n")
            stream.write(f"Result: **{report['result']}**. Expected: 72 issues, 71 parent links, 43 blocked-by links.\n\n")
            stream.write(f"POST attempts: {len(report['mutations'])}; existing edges skipped: {len(report['skipped_existing'])}.\n\n")
            stream.write("Research status, funding status, labels, issue text, Project fields, and branch review rules are outside this script.\n\n")
            stream.write("<details><summary>Machine-readable execution report</summary>\n\n```json\n")
            stream.write(text + "```\n\n</details>\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", default="data/dependencies.json")
    parser.add_argument("--report", default="native-relationships-report.json")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--check", action="store_true", help="Read-only complete native graph audit")
    args = parser.parse_args()
    report = {"started_at": datetime.now(timezone.utc).isoformat(), "repository": REPOSITORY,
              "plan_sha256": PLAN_SHA256, "expected": EXPECTED_COUNTS, "result": "not_started",
              "mode": "apply" if args.apply else "check" if args.check else "validate_local",
              "mutations": [], "skipped_existing": []}
    api = None
    try:
        plan = load_plan(args.registry)
        report["result"] = "local_plan_validated_no_network_or_mutations"
        if not (args.apply or args.check):
            return 0
        api = Api(os.environ.get("GITHUB_TOKEN"), plan)
        sha = None
        if args.apply:
            event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
            sha = validate_event(event, os.environ)
            report["head_sha"] = sha
            report["pull_request"] = PR_NUMBER
            verify_head(api, sha)
        verify_identities(api, plan)
        require(api.remaining is None or api.remaining >= 330,
                "Insufficient API budget for complete preflight; no mutations attempted")
        expected = expected_graph(plan)
        before = snapshot(api, plan, expected, require_complete=args.check)
        report["before"] = serializable_graph(before)
        if args.apply:
            missing_parents = sum(before[child]["parent"] is None for _, child in plan["parent_child"])
            missing_blocks = sum(blocker not in before[blocked]["blocked_by"] for blocked, blocker in plan["blocked_by"])
            required_remaining = 288 + 2 * missing_parents + missing_blocks + 43 + 25
            require(api.remaining is None or api.remaining >= required_remaining,
                    "Insufficient API budget for writes plus full final readback; no mutations attempted")
            verify_head(api, sha)
            apply_missing(api, plan, expected, before, report)
            after = snapshot(api, plan, expected, require_complete=True)
            report["after"] = serializable_graph(after)
            report["verified_counts"] = {
                "issues": len(after),
                "parent_child": sum(row["parent"] is not None for row in after.values()),
                "blocked_by": sum(len(row["blocked_by"]) for row in after.values()),
                "blocking_reverse": sum(len(row["blocking"]) for row in after.values()),
            }
            for operation in report["mutations"]:
                operation["result"] = "http_201_and_final_native_readback_verified"
            report["result"] = "all_71_parent_and_43_blocked_by_relationships_verified"
        else:
            report["after"] = report["before"]
            report["verified_counts"] = dict(EXPECTED_COUNTS, blocking_reverse=43)
            report["result"] = "all_native_relationships_verified_read_only"
        return 0
    except Exception as error:
        report["result"] = "failed_or_incomplete"
        report["error"] = str(error)
        # A partial run is retained. Do not retry, delete, or replace anything.
        # A subsequent authorized run starts with fresh identities and all native relations.
        return 1
    finally:
        if api is not None:
            report["api_requests"] = api.requests
            report["api_rate_remaining"] = api.remaining
        save_report(report, args.report)


if __name__ == "__main__":
    sys.exit(main())
