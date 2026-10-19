"""Offline checks for the irreversible-choice and idempotence boundaries; no network."""
import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("native", ROOT / "scripts/apply_native_relationships.py")
native = importlib.util.module_from_spec(spec)
spec.loader.exec_module(native)
PLAN = native.load_plan(ROOT / "data/dependencies.json")


class FakeApi:
    def __init__(self):
        self.graph = {item["number"]: {"parent": None, "sub_issues": set(),
                      "blocked_by": set(), "blocking": set()} for item in PLAN["issues"]}
        self.identities = {item["number"]: item for item in PLAN["issues"]}
        self.by_id = {item["id"]: item["number"] for item in PLAN["issues"]}
        self.posts = []

    def get(self, route, allow_missing_parent=False):
        number = int(route.split("/issues/")[1].split("/")[0])
        parent = self.graph[number]["parent"]
        return None if parent is None else self.identities[parent]

    def collection(self, route):
        rest = route.split("/issues/")[1].split("/")
        number, relation = int(rest[0]), rest[-1]
        return [self.identities[other] for other in self.graph[number][relation]]

    def request(self, method, route, payload):
        assert method == "POST"
        self.posts.append((route, copy.deepcopy(payload)))
        number = int(route.split("/issues/")[1].split("/")[0])
        if route.endswith("/sub_issues"):
            assert payload["replace_parent"] is False
            child = self.by_id[payload["sub_issue_id"]]
            assert self.graph[child]["parent"] is None
            self.graph[child]["parent"] = number
            self.graph[number]["sub_issues"].add(child)
            return self.identities[child]
        blocker = self.by_id[payload["issue_id"]]
        self.graph[number]["blocked_by"].add(blocker)
        self.graph[blocker]["blocking"].add(number)
        return self.identities[blocker]


def report():
    return {"mutations": [], "skipped_existing": []}


def valid_context():
    actor = {"login": native.ACTOR, "id": native.ACTOR_ID}
    repo = {"full_name": native.REPOSITORY, "fork": False}
    event = {"action": "synchronize", "number": 73, "repository": repo,
             "sender": actor, "pull_request": {"number": 73, "state": "open", "merged": False,
             "user": actor, "head": {"repo": repo, "ref": native.HEAD_BRANCH, "sha": "a" * 40},
             "base": {"repo": repo, "ref": "main"}}}
    env = {"GITHUB_ACTIONS": "true", "GITHUB_EVENT_NAME": "pull_request",
           "GITHUB_REPOSITORY": native.REPOSITORY, "GITHUB_ACTOR": native.ACTOR,
           "GITHUB_ACTOR_ID": str(native.ACTOR_ID), "GITHUB_TRIGGERING_ACTOR": native.ACTOR}
    return copy.deepcopy(event), env


class SafetyChecks(unittest.TestCase):
    def test_pinned_local_counts(self):
        self.assertEqual([len(PLAN[k]) for k in ("issues", "parent_child", "blocked_by")], [72, 71, 43])

    def test_changed_edge_with_same_counts_is_rejected(self):
        registry = json.loads((ROOT / "data/dependencies.json").read_text())
        registry["parent_child"][0]["parent_issue_number"] = 3
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "registry.json"
            path.write_text(json.dumps(registry))
            with self.assertRaises(native.Refusal):
                native.load_plan(path)

    def test_apply_uses_correct_native_ids_and_is_idempotent(self):
        api = FakeApi()
        expected = native.expected_graph(PLAN)
        before = native.snapshot(api, PLAN, expected)
        first = report()
        native.apply_missing(api, PLAN, expected, before, first)
        self.assertEqual(len(api.posts), 114)
        after = native.snapshot(api, PLAN, expected, require_complete=True)
        self.assertEqual(after, expected)
        second = report()
        native.apply_missing(api, PLAN, expected, after, second)
        self.assertEqual(len(api.posts), 114)
        self.assertEqual(len(second["mutations"]), 0)
        self.assertEqual(len(second["skipped_existing"]), 114)

    def test_unexpected_parent_stops_before_any_write(self):
        api = FakeApi()
        api.graph[2]["parent"] = 3
        api.graph[3]["sub_issues"].add(2)
        with self.assertRaises(native.Refusal):
            native.snapshot(api, PLAN, native.expected_graph(PLAN))
        self.assertEqual(api.posts, [])

    def test_extra_dependency_stops_before_any_write(self):
        api = FakeApi()
        api.graph[1]["blocked_by"].add(2)
        api.graph[2]["blocking"].add(1)
        with self.assertRaises(native.Refusal):
            native.snapshot(api, PLAN, native.expected_graph(PLAN))
        self.assertEqual(api.posts, [])

    def test_raced_parent_is_not_replaced(self):
        api = FakeApi()
        expected = native.expected_graph(PLAN)
        before = native.snapshot(api, PLAN, expected)
        api.graph[2]["parent"] = 3
        with self.assertRaises(native.Refusal):
            native.apply_missing(api, PLAN, expected, before, report())
        self.assertEqual(api.posts, [])

    def test_foreign_or_extra_post_cannot_reach_transport(self):
        api = native.Api("offline-test-placeholder", PLAN)
        with self.assertRaises(native.Refusal):
            api.request("POST", f"{native.PREFIX}/issues/1/sub_issues",
                        {"sub_issue_id": 999, "replace_parent": True})
        with self.assertRaises(native.Refusal):
            api.request("DELETE", f"{native.PREFIX}/issues/1/sub_issue")
        self.assertEqual(api.requests, 0)

    def test_exact_context_and_fork_rejection(self):
        event, env = valid_context()
        self.assertEqual(native.validate_event(event, env), "a" * 40)
        event["pull_request"]["head"]["repo"]["fork"] = True
        with self.assertRaises(native.Refusal):
            native.validate_event(event, env)

    def test_unexpected_rerun_actor_and_pr_are_rejected(self):
        event, env = valid_context()
        env["GITHUB_TRIGGERING_ACTOR"] = "someone-else"
        with self.assertRaises(native.Refusal):
            native.validate_event(event, env)
        event, env = valid_context()
        event["number"] = 74
        with self.assertRaises(native.Refusal):
            native.validate_event(event, env)


if __name__ == "__main__":
    unittest.main()
