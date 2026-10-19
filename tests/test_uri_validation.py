"""Offline whole-string URI checks using explicitly synthetic JSON fixtures."""

import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("uri_validation", ROOT / "scripts/validate_repository.py")
validation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validation)
SCHEMA = json.loads((ROOT / "data/opportunities.schema.json").read_text(encoding="utf-8"))
TEMPLATE = json.loads((ROOT / "templates/opportunity-record.json").read_text(encoding="utf-8"))
EXAMPLE = json.loads((ROOT / "templates/examples/opportunity-record.synthetic.json").read_text(encoding="utf-8"))
URI = "https://provider.example.invalid/community-credits"
URI_FIELDS = (
    "official_program_url", "official_application_url", "linked_github_research_issue",
    "source_urls", "source_refs",
)


def documents(record=None):
    """Build one synthetic register with exact pipeline and source membership."""
    record = copy.deepcopy(EXAMPLE if record is None else record)
    identity = record["opportunity_id"]
    urls = sorted(validation.required_urls(record))
    return {
        "data/opportunities.schema.json": copy.deepcopy(SCHEMA),
        "templates/opportunity-record.json": copy.deepcopy(TEMPLATE),
        "data/opportunities.json": {
            "schema_version": "sustainability-opportunity-register/v1",
            "last_verified": "2000-01-01", "records_count": 1, "records": [record],
            "important_limitations": ["Synthetic offline fixture; no source access or acceptance."],
        },
        "data/funding-pipeline.json": {
            "record_count": 1,
            "records": [{"opportunity_id": identity, **{
                target: copy.deepcopy(record.get(canonical))
                for target, canonical in validation.PIPELINE_FIELDS.items()
            }}],
        },
        "data/research-freshness.json": {
            "records_count": 1, "source_count": len(urls),
            "sources": [{"url": url, "opportunity_ids": [identity]} for url in urls],
        },
    }


def set_uri(record, field, value):
    record[field] = [value] if field in ("source_urls", "source_refs") else value


class WholeURIValidationChecks(unittest.TestCase):
    def errors(self, values):
        with patch("socket.socket", side_effect=AssertionError("network attempted")):
            return validation.validate_registers(values)

    def test_supported_uri_syntax_and_encoded_controls_keep_original_spelling(self):
        for value in (URI, URI + "?query=value#fragment", URI + "/%0A%0d%09%20",
                      "http://[2001:db8::1]:8080/path", "urn:example:fixture"):
            with self.subTest(value=value):
                record = copy.deepcopy(EXAMPLE)
                for field in URI_FIELDS:
                    set_uri(record, field, value)
                values = documents(record)
                original = copy.deepcopy(values)
                self.assertEqual(self.errors(values), [])
                self.assertEqual(values, original)

    def test_raw_control_and_whitespace_characters_fail_the_uri_format(self):
        for value in (URI + "\n", URI + "?query=value\n", URI + "#fragment\n",
                      "\n" + URI, URI + "\r\n", URI + "\t", URI + " ",
                      URI + "/line\nbreak", URI + "\n\n", URI + "\x00"):
            with self.subTest(value=value):
                self.assertTrue(validation.schema_errors(
                    value, {"type": "string", "format": "uri"}, "synthetic-uri"))

    def test_nullable_uri_fields_keep_schema_type_rules(self):
        schema = {"type": ["string", "null"], "format": "uri"}
        self.assertEqual(validation.schema_errors(None, schema, "nullable-uri"), [])
        for value in (False, 0, [], {}):
            with self.subTest(value=value):
                self.assertTrue(validation.schema_errors(value, schema, "nullable-uri"))

    def test_each_canonical_uri_field_rejects_a_trailing_lf_with_consistent_projections(self):
        for field in URI_FIELDS:
            with self.subTest(field=field):
                record = copy.deepcopy(EXAMPLE)
                set_uri(record, field, URI + "\n")
                values = documents(record)
                original = copy.deepcopy(values)
                errors = self.errors(values)
                self.assertTrue(any(f"[{field}]" in error and "is not a 'uri'" in error
                                    for error in errors), errors)
                self.assertTrue(all("is not a 'uri'" in error for error in errors), errors)
                self.assertEqual(values, original)

    def test_additional_freshness_endpoint_also_rejects_a_trailing_lf(self):
        values = documents()
        self.assertEqual(self.errors(values), [])
        freshness = values["data/research-freshness.json"]
        freshness["sources"].append({"url": URI + "/intake\n",
                                     "opportunity_ids": [EXAMPLE["opportunity_id"]]})
        freshness["source_count"] += 1
        original = copy.deepcopy(values)
        errors = self.errors(values)
        self.assertEqual(len(errors), 1, errors)
        self.assertIn("freshness.url:", errors[0])
        self.assertIn("is not a 'uri'", errors[0])
        self.assertEqual(values, original)

    def test_filled_template_uris_reject_trailing_lf_while_blank_placeholders_remain_valid(self):
        self.assertEqual(self.errors(documents()), [])
        for field in URI_FIELDS:
            with self.subTest(field=field):
                values = documents()
                set_uri(values["templates/opportunity-record.json"], field, URI + "\n")
                errors = self.errors(values)
                self.assertTrue(any(f"templates/opportunity-record.json[{field}]" in error
                                    and "is not a 'uri'" in error for error in errors), errors)

    def test_real_json_cli_preserves_input_bytes_in_normal_and_optimized_python(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for options in ([], ["-O"]):
                for value, expected in ((URI + "\n", 1), (URI + "/%0A", 0)):
                    with self.subTest(options=options, value=value):
                        record = copy.deepcopy(EXAMPLE)
                        record["official_program_url"] = value
                        values = documents(record)
                        original = {}
                        for relative, document in values.items():
                            path = root / relative
                            path.parent.mkdir(parents=True, exist_ok=True)
                            payload = (json.dumps(document, indent=2) + "\n").encode("utf-8")
                            path.write_bytes(payload)
                            original[relative] = payload
                        result = subprocess.run(
                            [sys.executable, *options, str(ROOT / "scripts/validate_repository.py"),
                             "--root", str(root)], capture_output=True, text=True,
                            check=False, timeout=15,
                        )
                        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
                        self.assertIn("is not a 'uri'" if expected else "PASS:", result.stdout)
                        self.assertNotIn("Traceback", result.stdout + result.stderr)
                        for relative, payload in original.items():
                            self.assertEqual((root / relative).read_bytes(), payload)


if __name__ == "__main__":
    unittest.main()
