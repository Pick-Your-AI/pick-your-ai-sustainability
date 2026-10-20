"""Counterexamples for source identity, population coverage and dashboard meaning.

Small synthetic inputs exercise calculation boundaries without provider access or
old Git history. The dated GitHub audit is tested separately as retained evidence.
"""

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("dashboard", ROOT / "scripts/build_dashboard.py")
DASHBOARD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(DASHBOARD)
REVISION = "1" * 40


def example():
    """Two different programs of one provider; all premises are invented."""
    rows = []
    for identity, name, work, stage in (
        ("EXAMPLE-A", "Alpha", "Done", "Discovered"),
        ("EXAMPLE-B", "Beta", "Ready", "Verified"),
    ):
        rows.append({
            "opportunity_id": identity, "provider": "Example Provider",
            "program_name": name, "program_aliases": [name, "Alias " + name],
            "round": "2026 and 2027 (one program)", "work_status": work,
            "opportunity_stage": stage, "priority": "P2",
            "linked_github_research_issue": "https://github.com/example/repo/issues/1",
            "verified_deadline": None, "deadline_timezone": None,
            "application_gate": "Unknown — no applicant decision",
            "eligibility_status": "Unknown", "current_disposition": "Research only",
            "available_before_incorporation": "Unknown community route",
            "available_through_fiscal_sponsorship": "Unknown host route",
            "available_after_501c3_recognition": "Unknown independent route",
            "assigned_owner": None, "award_evidence": None, "activation_evidence": None,
            "source_urls": ["https://example.test/" + name],
            "review": {"reviewer": None, "reviewed_revision": None, "review_url": None,
                       "decision": "Full research deliverable not accepted"},
        })
    rows[0]["discovery_sources"] = [{"url": "https://example.test/discovery"}]
    projected = [{"opportunity_id": row["opportunity_id"],
                  **{right: row.get(left) for left, right in DASHBOARD.PROJECTION_FIELDS.items()}}
                 for row in rows]
    sources = [
        {"url": "https://example.test/" + name,
         "last_verified": None if name in {"discovery", "form"} else "2020-01-01",
         "opportunity_ids": ["EXAMPLE-A"], "source_roles": ["example"],
         "state": "Not Verified" if name == "form" else "Synthetic observation"}
        for name in ("Alpha", "Beta", "discovery", "form", "redirect", "historical")
    ]
    inputs = {
        DASHBOARD.DATA_PATHS[0]: {"records_count": 2, "records": rows},
        DASHBOARD.DATA_PATHS[1]: {
            "record_count": 2, "records": projected,
            "funding_totals": {"confirmed_awards": None, "cash_received": None,
                               "credits_activated": None, "net_realized_support": None},
            "known_execution_activity": {"applications_submitted": 0,
                                         "scope": "Synthetic bounded execution only"},
        },
        DASHBOARD.DATA_PATHS[2]: {"source_count": 6, "records_count": 2, "sources": sources},
        DASHBOARD.DATA_PATHS[3]: {"actuals": {"cash_balance_cents": None,
                                                    "actual_expenses_cents": None}},
    }
    audit = {
        "schema_version": "sustainability-dashboard-readback/v1",
        "audit_id": "synthetic-boundary-example",
        "audit_path": "data/audits/dashboard-readback-2030-01-01.json",
        "canonical_revision": REVISION,
        "inputs": {path: {"revision": REVISION, "sha256": "0" * 64}
                   for path in DASHBOARD.DATA_PATHS + DASHBOARD.METHOD_PATHS},
        "definitions": [],
        "github": {
            "capture_started_at": "2030-01-01T00:00:00Z",
            "capture_completed_at": "2030-01-01T00:01:00Z",
            "sustainability_issue_pages": [{
                "page": 1, "total_count": 2, "incomplete_results": False,
                "items": [{"id": 100 + number, "number": number,
                           "state": "open" if number == 1 else "closed",
                           "is_pull_request": False,
                           "tracking_key": "E01-01" if number == 1 else "E01-02"}
                          for number in (1, 2)],
            }],
            "repository_open_counts": [
                {"repository": repository, "kind": kind, "total_count": 9,
                 "incomplete_results": False, "returned_items": 1, "error": None,
                 "sample": {"state": "open", "is_pull_request": kind == "pull_request"}}
                for repository in DASHBOARD.REPOSITORIES for kind in ("issue", "pull_request")
            ],
            "project": {"url": "https://github.com/orgs/Pick-Your-AI/projects/7",
                        "item_count": None, "status_counts": None,
                        "request_error": "Synthetic unavailable route"},
        },
    }
    return audit, inputs


class DashboardBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.audit, self.inputs = example()

    def report(self):
        return DASHBOARD.calculate(self.audit, self.inputs)

    def test_two_programs_are_not_aliases_rounds_projections_or_issues(self):
        original = copy.deepcopy((self.audit, self.inputs))
        report = self.report()
        self.assertEqual(report["work"]["program_records"], 2)
        self.assertEqual(report["work"]["by_status"], {"Done": 1, "Ready": 1})
        self.assertEqual(report["opportunity_stages"]["Discovered"], 1)
        self.assertEqual(len(report["work"]["distinct_owning_issue_urls"]), 1)
        self.assertEqual(report["discrepancies"], [])
        self.assertEqual((self.audit, self.inputs), original)

    def test_duplicate_canonical_id_is_rejected(self):
        rows = self.inputs[DASHBOARD.DATA_PATHS[0]]["records"]
        rows.append(copy.deepcopy(rows[0]))
        with self.assertRaisesRegex(DASHBOARD.DashboardError, "duplicate identity"):
            self.report()

    def test_second_round_cannot_create_another_program_count(self):
        rows = self.inputs[DASHBOARD.DATA_PATHS[0]]["records"]
        rows[1].update(provider="  EXAMPLE   PROVIDER ", program_name=" ALPHA ", round="next")
        with self.assertRaisesRegex(DASHBOARD.DashboardError, "Repeated provider/program"):
            self.report()

    def test_missing_or_nontext_program_identity_cannot_be_coerced_into_a_name(self):
        for value in (None, 123, "   "):
            with self.subTest(value=value):
                self.inputs[DASHBOARD.DATA_PATHS[0]]["records"][0]["provider"] = value
                with self.assertRaisesRegex(DASHBOARD.DashboardError, "nonempty strings"):
                    self.report()

    def test_projection_disagreement_remains_visible_without_repair(self):
        projection = self.inputs[DASHBOARD.DATA_PATHS[1]]["records"][0]
        projection["application_gate"] = "A conflicting projection"
        report = self.report()
        self.assertEqual(report["discrepancies"][0]["kind"], "projection_value")
        self.assertEqual(report["discrepancies"][0]["field"], "application_gate")
        self.assertEqual(projection["application_gate"], "A conflicting projection")

    def test_review_negation_and_mechanism_sibling_are_not_acceptance(self):
        row = self.inputs[DASHBOARD.DATA_PATHS[0]]["records"][0]
        row["award_mechanism_review"] = {"reviewer": "Example", "reviewed_revision": REVISION,
                                         "review_url": "https://example.test/review"}
        self.assertFalse(DASHBOARD.complete_review_pointer(row))
        row["review"]["reviewed_revision"] = 123
        self.assertFalse(DASHBOARD.complete_review_pointer(row))
        row["review"].update(reviewer="Example", reviewed_revision=REVISION,
                             review_url="https://example.test/review")
        self.assertTrue(DASHBOARD.complete_review_pointer(row))
        self.assertEqual(row["review"]["decision"], "Full research deliverable not accepted")
        self.assertEqual(self.report()["work"]["complete_review_pointer_count"], 1)

    def test_source_membership_missing_dates_and_claim_validity_are_distinct(self):
        freshness = self.report()["freshness"]
        self.assertEqual(freshness["tracked_urls"], 6)
        self.assertEqual(freshness["referenced_source_or_discovery_urls"], 3)
        self.assertEqual(freshness["tracked_urls_outside_references"], 3)
        self.assertEqual(freshness["without_successful_check_count"], 2)
        self.assertEqual(freshness["recorded_successful_check_dates"], {"2020-01-01": 4})
        self.assertIsNone(freshness["stale_source_count"])

    def test_unknown_financial_populations_do_not_sum_currencies_or_face_values(self):
        rows = self.inputs[DASHBOARD.DATA_PATHS[0]]["records"]
        rows[0].update(currency="USD", benefit_amount_or_capacity=100000,
                       award_evidence={"unqualified_notice": "Example only"})
        rows[1].update(currency="EUR", benefit_amount_or_capacity=50000)
        self.inputs[DASHBOARD.DATA_PATHS[3]]["actuals"]["cash_balance_cents"] = 700
        report = self.report()
        for key in ("cash_received_by_currency", "activated_benefits", "confirmed_awards",
                    "realized_avoided_cost_by_currency", "actual_expenditure_by_currency"):
            self.assertIsNone(report["resources"][key])
        self.assertEqual(report["resources"]["recorded_budget_actuals"]["cash_balance_cents"], 700)
        self.assertEqual(report["resources"]["non_null_award_evidence_ids"], ["EXAMPLE-A"])
        self.assertIsNone(report["obligations"]["confirmed_open_count"])
        self.assertIsNone(report["needs_and_risks"]["funded_coverage"])

    def test_research_assignment_is_not_an_operating_appointment(self):
        self.inputs[DASHBOARD.DATA_PATHS[0]]["records"][0]["assigned_owner"] = "Research only"
        report = self.report()
        self.assertEqual(len(report["work"]["unassigned_research_owner_ids"]), 1)
        self.assertEqual(report["obligations"]["operating_owner"], "Unassigned")
        self.assertIsNone(report["needs_and_risks"]["ownership_continuity"])

    def test_organization_local_deadline_keeps_unknown_utc(self):
        self.inputs[DASHBOARD.DATA_PATHS[0]]["records"][0].update(
            verified_deadline="2030-03-02", deadline_local_time="17:00",
            deadline_timezone="Submitting organization local time; exact zone Unknown",
            deadline_utc=None, deadline_source_url="https://example.test/cutoff")
        deadline = self.report()["deadlines"][0]
        self.assertEqual(deadline["deadline_local_time"], "17:00")
        self.assertIsNone(deadline["deadline_utc"])

    def test_canonical_revision_cannot_mislabel_different_pinned_bytes(self):
        self.audit["inputs"][DASHBOARD.DATA_PATHS[0]]["revision"] = "2" * 40
        with self.assertRaisesRegex(DASHBOARD.DashboardError, "Canonical revision"):
            self.report()

    def test_missing_page_is_unknown_but_explicit_complete_zero_is_zero(self):
        page = self.audit["github"]["sustainability_issue_pages"][0]
        page.update(total_count=0)
        del page["items"]
        self.assertIsNone(self.report()["github"]["issues"]["total"])
        page["items"] = []
        self.assertEqual(self.report()["github"]["issues"]["total"], 0)
        page["error"] = "Response could not be read"
        self.assertIsNone(self.report()["github"]["issues"]["total"])

    def test_truncated_or_inconsistent_pages_cannot_claim_complete_counts(self):
        page = self.audit["github"]["sustainability_issue_pages"][0]
        page["incomplete_results"] = True
        self.assertIsNone(self.report()["github"]["issues"]["total"])
        page.update(incomplete_results=False, total_count=3)
        self.assertIsNone(self.report()["github"]["issues"]["total"])

    def test_duplicate_issue_identity_and_pr_contamination_are_rejected(self):
        page = self.audit["github"]["sustainability_issue_pages"][0]
        page["items"].append(copy.deepcopy(page["items"][0]))
        with self.assertRaisesRegex(DASHBOARD.DashboardError, "repeats issue ID"):
            self.report()
        page["items"].pop()
        page["items"][0]["is_pull_request"] = True
        with self.assertRaisesRegex(DASHBOARD.DashboardError, "PR contaminated"):
            self.report()

    def test_repository_counts_use_typed_total_and_expose_missing_repository(self):
        report = self.report()
        self.assertTrue(all(row["count"] == 9 for row in report["github"]["repositories"]))
        missing = DASHBOARD.REPOSITORIES[0]
        self.audit["github"]["repository_open_counts"] = [
            row for row in self.audit["github"]["repository_open_counts"] if row["repository"] != missing]
        report = self.report()
        absent = [row for row in report["github"]["repositories"] if row["repository"] == missing]
        self.assertEqual(len(absent), 2)
        self.assertTrue(all(row["count"] is None for row in absent))
        self.assertIn("[pick-your-ai-leaderboard]", DASHBOARD.render_markdown(report))

    def test_wrong_typed_sample_is_unknown_and_project_count_cannot_be_invented(self):
        self.audit["github"]["repository_open_counts"][0]["sample"]["is_pull_request"] = True
        self.assertIsNone(self.report()["github"]["repositories"][0]["count"])
        self.audit["github"]["project"]["item_count"] = 0
        with self.assertRaisesRegex(DASHBOARD.DashboardError, "no current Project readback"):
            self.report()

    def test_capture_requires_ordered_explicit_timezones(self):
        self.audit["github"]["capture_completed_at"] = "2029-01-01T00:00:00Z"
        with self.assertRaisesRegex(DASHBOARD.DashboardError, "reversed"):
            self.report()
        self.audit["github"]["capture_completed_at"] = "2030-01-01T00:02:00"
        with self.assertRaisesRegex(DASHBOARD.DashboardError, "explicit timezone"):
            self.report()

    def test_render_preserves_unknown_stage_and_actual_dated_audit_path(self):
        self.inputs[DASHBOARD.DATA_PATHS[0]]["records"][0]["opportunity_stage"] = None
        rendered = DASHBOARD.render_markdown(self.report())
        self.assertIn("| Unknown / not recorded | 1 |", rendered)
        self.assertIn("../data/audits/dashboard-readback-2030-01-01.json", rendered)
        self.assertNotIn(DASHBOARD.DEFAULT_AUDIT, rendered)

    def test_duplicate_json_keys_and_nonfinite_numbers_are_rejected(self):
        for raw in ('{"count":1,"count":2}', '{"number":NaN}', '{"number":1e1000}'):
            with self.subTest(raw=raw), self.assertRaises(DASHBOARD.DashboardError):
                DASHBOARD.strict_json(raw)

    def test_retained_actual_issue_readback_is_72_issues_not_prs_or_programs(self):
        audit = DASHBOARD.strict_json((ROOT / DASHBOARD.DEFAULT_AUDIT).read_bytes())
        discrepancies = []
        github = DASHBOARD.github_metrics(audit["github"], discrepancies)
        self.assertEqual(github["issues"]["total"], 72)
        self.assertEqual(github["issues"]["by_state"], {"closed": 40, "open": 32})
        self.assertEqual(github["issues"]["by_kind"], {"Epic": 9, "Program": 1, "Task": 62})
        self.assertIsNone(github["project"]["item_count"])
        self.assertEqual(discrepancies, [])


class DashboardInputPinTests(unittest.TestCase):
    def test_git_inputs_ignore_changed_worktree_and_archive_inputs_must_match(self):
        audit, inputs = example()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "--quiet", str(root)], check=True, capture_output=True)
            pins = {}
            for path in DASHBOARD.DATA_PATHS + DASHBOARD.METHOD_PATHS:
                raw = (json.dumps(inputs[path]) + "\n").encode() if path in inputs else b"Synthetic method only.\n"
                target = root / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(raw)
                pins[path] = {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(),
                              "git_blob": hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()}
            subprocess.run(["git", "add", "."], cwd=root, check=True, capture_output=True)
            subprocess.run(["git", "-c", "user.name=Synthetic test", "-c",
                            "user.email=dashboard@example.invalid", "commit", "--quiet", "-m", "Synthetic pins"],
                           cwd=root, check=True, capture_output=True)
            revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root).decode().strip()
            audit["canonical_revision"] = revision
            audit["inputs"] = {path: {**pin, "revision": revision} for path, pin in pins.items()}
            self.assertEqual(DASHBOARD.load_inputs(audit, root, root), inputs)
            data_path = root / DASHBOARD.DATA_PATHS[0]
            data_path.write_bytes(data_path.read_bytes().replace(b'"Done"', b'"Nope"'))
            self.assertEqual(DASHBOARD.load_inputs(audit, root), inputs)
            with self.assertRaisesRegex(DASHBOARD.DashboardError, "SHA256 differs"):
                DASHBOARD.load_inputs(audit, root, root)
            audit["inputs"][DASHBOARD.METHOD_PATHS[0]]["sha256"] = "0" * 64
            with self.assertRaisesRegex(DASHBOARD.DashboardError, "SHA256 differs"):
                DASHBOARD.load_inputs(audit, root)


if __name__ == "__main__":
    unittest.main()
