"""Offline contracts for the deliberately incomplete synthetic intake example.

The fixed unknown/gate assertions apply to this fixture, not to real records.
"""

import copy
import importlib.util
import json
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = "templates/examples/opportunity-record.synthetic.json"
NOTE = "templates/examples/provider-research-worked-example.md"
spec = importlib.util.spec_from_file_location("intake_validation", ROOT / "scripts/validate_repository.py")
validation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validation)


def read_json(path):
    return json.loads(
        (ROOT / path).read_text(encoding="utf-8"),
        object_pairs_hook=validation.no_duplicate_keys,
        parse_constant=validation.no_nonfinite,
        parse_float=validation.finite_float,
    )


class SyntheticIntakeChecks(unittest.TestCase):
    def setUp(self):
        self.record = read_json(EXAMPLE)
        self.template = read_json("templates/opportunity-record.json")
        self.schema = read_json("data/opportunities.schema.json")
        self.item_schema = self.schema["properties"]["records"]["items"]
        self.validator = validation.schema_validator(self.item_schema, self.schema)
        self.note = (ROOT / NOTE).read_text(encoding="utf-8")

    def test_fixture_validates_against_current_record_schema_without_network(self):
        with patch("socket.socket", side_effect=AssertionError("network attempted")):
            self.assertEqual(list(self.validator.iter_errors(self.record)), [])

    def test_schema_required_fields_are_not_relaxed_for_the_fixture(self):
        for key in self.item_schema["required"]:
            with self.subTest(key=key):
                record = copy.deepcopy(self.record)
                del record[key]
                self.assertTrue(list(self.validator.iter_errors(record)))

    def test_schema_rejects_invalid_uri_and_fabricated_score_shapes(self):
        for field, value in (("official_program_url", "not a URI"),
                             ("source_urls", []), ("priority", "Urgent")):
            with self.subTest(field=field):
                record = copy.deepcopy(self.record)
                record[field] = value
                self.assertTrue(list(self.validator.iter_errors(record)))
        for field, value in (("eligibility", 6), ("net_usable_value", "unknown"),
                             ("total", 101)):
            with self.subTest(scoring_field=field):
                record = copy.deepcopy(self.record)
                record["scoring"][field] = value
                self.assertTrue(list(self.validator.iter_errors(record)))

    def test_example_retains_all_template_fields_including_nested_records(self):
        self.assertLessEqual(self.template.keys(), self.record.keys())
        for key in ("scoring", "duplicate_search", "review"):
            with self.subTest(key=key):
                self.assertLessEqual(self.template[key].keys(), self.record[key].keys())

    def test_identity_and_required_placeholders_are_explicitly_synthetic(self):
        self.assertIs(self.record["template_only"], True)
        self.assertIs(self.record["synthetic_example"], True)
        self.assertEqual(self.record["opportunity_id"], "SYNTHETIC-EXAMPLE-CREDITS")
        self.assertEqual(self.record["owning_research_key"], "E00-00")
        self.assertEqual(self.record["priority"], "P2")
        self.assertIsNone(self.record["linked_github_research_issue"])
        self.assertTrue(self.record["example_limitations"])
        self.assertEqual(self.record["source_urls"], [self.record["official_program_url"]])
        self.assertEqual(urlsplit(self.record["official_program_url"]).hostname,
                         "provider.example.invalid")
        self.assertIsNone(self.record["official_application_url"])

    def test_unknown_deadline_value_entity_and_internal_dates_stay_null(self):
        for key in ("verified_deadline", "deadline_timezone", "deadline_source_url",
                    "benefit_amount_or_capacity", "currency", "estimated_usable_value",
                    "valuation_method", "eligibility_jurisdiction", "legal_entity_requirements",
                    "next_action_date", "next_verification_date", "round"):
            with self.subTest(key=key):
                self.assertIsNone(self.record[key])
        for key, value in self.record["scoring"].items():
            with self.subTest(scoring_field=key):
                if key == "justification":
                    self.assertTrue(value)
                else:
                    self.assertIsNone(value)

    def test_all_three_eligibility_routes_remain_independently_unverified(self):
        for key in ("available_before_incorporation", "available_through_fiscal_sponsorship",
                    "available_after_501c3_recognition", "eligibility_status"):
            with self.subTest(key=key):
                self.assertEqual(self.record[key], "Not Verified")
        self.assertEqual(self.record["eligibility_conditions"], [])

    def test_no_source_access_or_duplicate_search_is_invented(self):
        self.assertIsNone(self.record["last_verified"])
        self.assertEqual(self.record["source_review_status"], "Not Verified")
        self.assertEqual(self.record["sources"], [])
        self.assertEqual(self.record["source_refs"], [])
        self.assertEqual(self.record["duplicate_search"], {
            "searched_at": None, "aliases_checked": [], "canonical_match": None,
        })

    def test_owner_reviewer_and_acceptance_are_not_assigned(self):
        self.assertIsNone(self.record["assigned_owner"])
        self.assertIsNone(self.record["independent_reviewer"])
        for key in ("reviewer", "reviewed_revision", "review_url"):
            with self.subTest(key=key):
                self.assertIsNone(self.record["review"][key])
        self.assertEqual(self.record["review"]["decision"], "Not reviewed")
        self.assertTrue(self.record["review"]["limitations"])

    def test_application_award_activation_and_obligations_do_not_advance(self):
        for key, expected in {
            "application_gate": "Not authorized", "application_status": "Unknown",
            "application_outcome": "Unknown", "award_status": "Unknown",
            "activation_status": "Not activated", "work_status": "Backlog",
            "opportunity_stage": "Discovered",
            "reporting_status": "Unknown; no actual offer or terms have been examined.",
        }.items():
            with self.subTest(key=key):
                self.assertEqual(self.record[key], expected)
        for key in ("award_evidence", "activation_evidence"):
            self.assertIsNone(self.record[key])
        for key in ("restrictions_and_obligations", "required_application_evidence",
                    "reporting_obligations"):
            self.assertEqual(self.record[key], [])

    def test_worked_note_matches_identity_and_preserves_unsent_outreach(self):
        for value in (self.record["opportunity_id"], self.record["official_program_url"],
                      self.record["owning_research_key"], "Outreach status: Draft only; not sent.",
                      "Recipient/channel: Unknown.", "Approval record: None."):
            with self.subTest(value=value):
                self.assertIn(value, self.note)
        self.assertTrue(self.record["next_action"])

    def test_synthetic_identity_and_urls_are_absent_from_live_registers(self):
        # Do not freeze real counts, dates or lifecycle states: only exclude this fixture.
        for path in ("data/opportunities.json", "data/funding-pipeline.json",
                     "data/research-freshness.json"):
            text = json.dumps(read_json(path))
            for value in (self.record["opportunity_id"], self.record["owning_research_key"],
                          self.record["official_program_url"], self.record["provider"],
                          self.record["program_name"]):
                with self.subTest(path=path, value=value):
                    self.assertNotIn(value, text)

    def test_full_repository_including_example_passes_offline(self):
        with patch("socket.socket", side_effect=AssertionError("network attempted")):
            errors, _ = validation.validate_repository(ROOT)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
