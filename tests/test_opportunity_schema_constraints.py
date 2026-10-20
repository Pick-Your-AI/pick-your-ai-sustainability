"""Residual schema regressions using the existing, merged repository validator."""

import copy
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("residual_validation", ROOT / "scripts/validate_repository.py")
validation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validation)
BASE = {path: json.loads((ROOT / path).read_text()) for path in validation.REQUIRED_FILES}
TEXT_FIELDS = ("provider", "program_name", "available_before_incorporation",
               "available_through_fiscal_sponsorship", "available_after_501c3_recognition",
               "eligibility_status", "application_gate")


class OpportunitySchemaConstraints(unittest.TestCase):
    def setUp(self):
        self.documents = copy.deepcopy(BASE)
        self.register = self.documents["data/opportunities.json"]
        self.record = self.register["records"][0]

    def errors(self):
        with patch("socket.socket", side_effect=AssertionError("Network forbidden")):
            return validation.validate_registers(self.documents)

    def synchronize_projection(self, field, value):
        # An error must come from the canonical field constraint, not projection drift.
        self.record[field] = value
        for target, canonical in validation.PIPELINE_FIELDS.items():
            if canonical == field:
                self.documents["data/funding-pipeline.json"]["records"][0][target] = copy.deepcopy(value)

    def assert_field_error(self, field):
        errors = self.errors()
        location = f"data/opportunities.json[records][0][{field}]"
        self.assertTrue(any(error.startswith(location + ":") for error in errors), errors)
        self.assertFalse(any(": differs from opportunities" in error for error in errors), errors)

    def test_current_records_and_blank_template_remain_valid(self):
        self.assertEqual(self.errors(), [])

    def test_required_descriptive_fields_reject_empty_and_nontext_values(self):
        for field in TEXT_FIELDS:
            for value in ("", None, [], {}, False, 17):
                with self.subTest(field=field, value=value):
                    original = copy.deepcopy(self.documents)
                    self.synchronize_projection(field, value)
                    self.assert_field_error(field)
                    self.documents = original
                    self.register = self.documents["data/opportunities.json"]
                    self.record = self.register["records"][0]

    def test_unknown_text_dispositions_are_preserved_without_new_eligibility_enums(self):
        for field in TEXT_FIELDS:
            self.synchronize_projection(field, "Not Verified")
        self.assertEqual(self.errors(), [])

    def test_per_record_dates_reject_impossible_dates_datetimes_and_wrong_types(self):
        for value in ("2026-02-30", "2026-13-01", "20261019", "2026-10-19T00:00:00Z",
                      "2026-10-19\n", "", 42, False, [], {}):
            with self.subTest(value=value):
                self.record["last_verified"] = value
                self.assert_field_error("last_verified")

    def test_unverified_synthetic_shape_accepts_explicit_null_date(self):
        # Equivalent to PR76's unverified shape, without importing its owned fixture:
        # nonempty synthetic identity, Not Verified route texts, no source-access date.
        self.synchronize_projection("provider", "Synthetic Constraint Test Provider")
        self.synchronize_projection("program_name", "Synthetic Constraint Test Program")
        for field in TEXT_FIELDS[2:-1]:
            self.synchronize_projection(field, "Not Verified")
        self.synchronize_projection("application_gate", "Not authorized")
        self.synchronize_projection("source_review_status", "Synthetic test; no source access claimed")
        self.record["last_verified"] = None
        self.assertEqual(self.errors(), [])
        self.assertIsNone(self.record["last_verified"])
        for valid in ("2024-02-29", "2026-10-19", None):
            self.record["last_verified"] = valid
            self.assertEqual(self.errors(), [])

    def test_legacy_application_endpoint_rejects_nontext_and_empty_values(self):
        for value in (42, False, [], {}, ""):
            with self.subTest(value=value):
                self.record["application_url"] = value
                self.assert_field_error("application_url")

    def test_legacy_application_uri_error_is_direct_even_with_consistent_membership(self):
        value = "this is not a URI"
        self.record["application_url"] = value
        freshness = self.documents["data/research-freshness.json"]
        freshness["sources"].append({"url": value, "opportunity_ids": [self.record["opportunity_id"]]})
        freshness["source_count"] += 1
        self.assert_field_error("application_url")
        self.assertFalse(any("missing source/program/application URL" in error for error in self.errors()))

    def test_legacy_application_null_and_valid_tracked_uri_remain_valid(self):
        self.record["application_url"] = None
        self.assertEqual(self.errors(), [])
        self.record["application_url"] = self.record["official_program_url"]
        self.assertEqual(self.errors(), [])

    def test_delivered_unverified_intake_example_retains_null_date(self):
        example = json.loads((ROOT / "templates/examples/opportunity-record.synthetic.json").read_text())
        item_schema = self.documents["data/opportunities.schema.json"]["properties"]["records"]["items"]
        self.assertIsNone(example["last_verified"])
        self.assertEqual(validation.schema_errors(example, item_schema, "synthetic_example"), [])

    def test_legacy_application_uri_uses_complete_original_string(self):
        # Exercise PR112's complete-match checker through this newly typed alias.
        for value in ("https://example.invalid/\n", "https://example.invalid/\r\n",
                      "https://example.invalid/\t", " https://example.invalid/",
                      "https://example.invalid/ "):
            with self.subTest(value=value):
                original = copy.deepcopy(self.documents)
                self.record["application_url"] = value
                freshness = self.documents["data/research-freshness.json"]
                freshness["sources"].append({"url": value, "opportunity_ids": [self.record["opportunity_id"]]})
                freshness["source_count"] += 1
                self.assert_field_error("application_url")
                self.assertEqual(self.record["application_url"], value)
                self.documents = original
                self.register = self.documents["data/opportunities.json"]
                self.record = self.register["records"][0]

    def test_legacy_application_encoded_newline_is_preserved(self):
        value = "https://example.invalid/%0A"
        self.record["application_url"] = value
        freshness = self.documents["data/research-freshness.json"]
        freshness["sources"].append({"url": value, "opportunity_ids": [self.record["opportunity_id"]]})
        freshness["source_count"] += 1
        self.assertEqual(self.errors(), [])
        self.assertEqual(self.record["application_url"], value)


if __name__ == "__main__":
    unittest.main()
