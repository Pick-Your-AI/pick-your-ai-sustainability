"""Offline corruption and evolution checks for the current repository format."""
import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validation", ROOT / "scripts/validate_repository.py")
validation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validation)
BASE = {p: json.loads((ROOT / p).read_text(encoding="utf-8")) for p in validation.REQUIRED_FILES}


class RegisterChecks(unittest.TestCase):
    def setUp(self):
        self.documents = copy.deepcopy(BASE)
        self.register = self.documents["data/opportunities.json"]
        self.record = self.register["records"][0]
        self.freshness = self.documents["data/research-freshness.json"]
        self.pipeline = self.documents["data/funding-pipeline.json"]
        self.template = self.documents["templates/opportunity-record.json"]

    def errors(self):
        return validation.validate_registers(self.documents)

    def assertError(self, fragment):
        errors = self.errors()
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_current_registers_and_intentionally_blank_template_pass(self):
        self.assertEqual(self.errors(), [])

    def test_malformed_scores_rejected_by_schema(self):
        for field, value in (("mission_fit", "high"), ("eligibility", 99),
                             ("net_usable_value", -1), ("total", {}), ("total", 101)):
            with self.subTest(field=field, value=value):
                self.record["scoring"][field] = value
                self.assertError(f"[scoring][{field}]")
                self.record["scoring"][field] = None

    def test_uri_and_date_formats_are_actually_checked(self):
        self.record["official_program_url"] = "not a URI"
        self.register["last_verified"] = "2026-02-30"
        self.assertError("[official_program_url]")
        self.assertError("[last_verified]")

    def test_session_local_citation_rejected(self):
        self.record["source_refs"] = ["turn2view0"]
        self.assertError("[source_refs][0]")

    def test_template_required_top_level_and_nested_keys(self):
        del self.template["source_urls"]
        del self.template["scoring"]["total"]
        self.assertError("'source_urls' is a required property")
        self.assertError("'total' is a required property")

    def test_template_rejects_nonblank_invalid_values_and_missing_object_shape(self):
        self.template["scoring"]["total"] = {}
        self.assertError("templates/opportunity-record.json[scoring][total]")
        self.template["scoring"] = None
        self.assertError("None is not of type 'object'")

    def test_template_supports_local_schema_refs_and_still_checks_required_fields(self):
        schema = self.documents["data/opportunities.schema.json"]
        properties = schema["properties"]["records"]["items"]["properties"]
        schema["$defs"] = {"priority": properties["priority"], "scoring": properties["scoring"]}
        properties["priority"] = {"$ref": "#/$defs/priority"}
        properties["scoring"] = {"$ref": "#/$defs/scoring"}
        self.template["priority"] = "P1"
        self.assertEqual(self.errors(), [])
        del self.template["scoring"]["total"]
        self.assertError("'total' is a required property")

    def test_pipeline_false_is_not_the_canonical_numeric_zero(self):
        self.record["score"] = 0
        self.pipeline["records"][0]["score"] = False
        self.assertError("[score]: differs")
        self.pipeline["records"][0]["score"] = 0.0
        self.assertEqual(self.errors(), [])
        self.assertFalse(validation.same_json_value({"values": [0]}, {"values": [False]}))

    def test_completed_template_validates_as_real_record(self):
        schema = self.documents["data/opportunities.schema.json"]["properties"]["records"]["items"]
        for key in schema["required"]:
            self.template[key] = copy.deepcopy(self.record[key])
        self.template.pop("template_only")
        self.assertEqual(validation.schema_errors(self.template, schema, "completed-template"), [])

    def test_distinct_application_endpoint_must_be_tracked(self):
        self.record["official_application_url"] = "https://example.org/new-application"
        self.assertError("missing source/program/application URL")

    def test_legacy_application_url_is_tracked_too(self):
        self.record["application_url"] = "https://example.org/legacy-form"
        self.assertError("missing source/program/application URL")

    def test_url_presence_without_correct_membership_is_not_enough(self):
        url = self.record["official_program_url"]
        row = next(row for row in self.freshness["sources"] if row["url"] == url)
        row["opportunity_ids"].remove(self.record["opportunity_id"])
        self.assertError("missing opportunity membership")

    def test_duplicate_opportunity_and_freshness_url_rejected(self):
        self.register["records"].append(copy.deepcopy(self.record))
        self.freshness["sources"].append(copy.deepcopy(self.freshness["sources"][0]))
        self.assertError("duplicate opportunity_id")
        self.assertError("duplicate url")

    def test_freshness_membership_must_be_well_formed(self):
        row = self.freshness["sources"][0]
        row["opportunity_ids"] = ["UNKNOWN", "UNKNOWN"]
        self.assertError("unknown opportunity UNKNOWN")
        self.assertError("duplicate opportunity membership")
        row["opportunity_ids"] = [{}]
        self.assertError("must be an array of strings")

    def test_declared_counts_must_match_actual_arrays(self):
        for document, field in ((self.register, "records_count"), (self.pipeline, "record_count"),
                                (self.freshness, "records_count"), (self.freshness, "source_count")):
            with self.subTest(field=field):
                old = document[field]
                document[field] = old + 1
                self.assertError(f"[{field}]: expected")
                document[field] = old

    def test_pipeline_membership_must_match_register(self):
        self.pipeline["records"][0]["opportunity_id"] = "UNKNOWN"
        self.assertError("missing opportunity")
        self.assertError("unknown opportunity UNKNOWN")

    def test_every_pipeline_projection_field_detects_drift(self):
        for field in validation.PIPELINE_FIELDS:
            with self.subTest(field=field):
                old = self.pipeline["records"][0].pop(field)
                self.assertError(f"[{field}]: differs")
                self.pipeline["records"][0][field] = old

    def test_legitimate_lifecycle_scores_owners_and_dates_are_not_frozen(self):
        self.record.update(opportunity_stage="Qualified", work_status="Done", score=80,
                           assigned_owner="example-contributor", independent_reviewer="example-reviewer",
                           last_verified="2026-10-20", next_action_date="2026-10-25")
        self.record["scoring"].update(mission_fit=4, total=80)
        self.pipeline["records"][0].update(opportunity_stage="Qualified", research_status="Done", score=80)
        self.assertEqual(self.errors(), [])

    def test_new_opportunity_is_allowed_when_related_registers_are_updated(self):
        record = copy.deepcopy(self.record)
        record["opportunity_id"] = "EXAMPLE-NEW"
        self.register["records"].append(record)
        self.register["records_count"] += 1
        projection = copy.deepcopy(self.pipeline["records"][0])
        projection["opportunity_id"] = record["opportunity_id"]
        self.pipeline["records"].append(projection)
        self.pipeline["record_count"] += 1
        self.freshness["records_count"] += 1
        for source in self.freshness["sources"]:
            if source["url"] in validation.required_urls(record):
                source["opportunity_ids"].append(record["opportunity_id"])
        self.assertEqual(self.errors(), [])

    def test_bad_shapes_report_errors_instead_of_crashing(self):
        for path, field, value in (("data/opportunities.json", "records", {}),
                                  ("data/opportunities.json", "records", [None]),
                                  ("data/funding-pipeline.json", "records", [None]),
                                  ("data/research-freshness.json", "sources", [None])):
            with self.subTest(path=path, field=field):
                documents = copy.deepcopy(BASE)
                documents[path][field] = value
                self.assertTrue(validation.validate_registers(documents))
        self.record["source_urls"] = 3
        self.assertError("[source_urls]")

    def test_missing_or_invalid_required_document_reports_error(self):
        del self.documents["data/opportunities.schema.json"]
        self.assertError("required JSON object is missing or invalid")

    def test_invalid_schema_is_reported(self):
        self.documents["data/opportunities.schema.json"]["type"] = "nonsense"
        self.assertError("invalid schema")

    def test_external_schema_reference_is_refused_without_network(self):
        self.documents["data/opportunities.schema.json"]["$ref"] = "https://example.org/schema.json"
        with patch("socket.socket", side_effect=AssertionError("network attempted")):
            self.assertError("network retrieval disabled")


class FilesystemChecks(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        for path, document in BASE.items():
            target = self.root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(json.dumps(document), encoding="utf-8")

    def write(self, path, content="present\n"):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        return target

    def pipeline_score(self, canonical, original_token):
        register = copy.deepcopy(BASE["data/opportunities.json"])
        pipeline = copy.deepcopy(BASE["data/funding-pipeline.json"])
        register["records"][0]["score"] = canonical
        pipeline["records"][0]["score"] = canonical
        self.write("data/opportunities.json", json.dumps(register))
        raw = json.dumps(pipeline).replace(
            '"score": ' + json.dumps(canonical), '"score": ' + original_token, 1)
        return self.write("data/funding-pipeline.json", raw)

    def test_complete_fixture_and_live_checkout_pass_without_network(self):
        with patch("socket.socket", side_effect=AssertionError("network attempted")):
            self.assertEqual(validation.validate_repository(self.root)[0], [])
            self.assertEqual(validation.validate_repository(ROOT)[0], [])

    def test_local_markdown_links_images_references_and_encoded_paths(self):
        self.write("docs/with space (v2).md")
        self.write("assets/plot.png")
        self.write("README.md", '[title](<docs/with space (v2).md> "Title")\n'
                   '[encoded](docs/with%20space%20%28v2%29.md#heading)\n'
                   '[root](/docs/with%20space%20%28v2%29.md?raw=1)\n'
                   '[reference][ref]\n\n[ref]: <docs/with space (v2).md>\n'
                   '![plot](assets/plot.png)\n')
        self.assertEqual(validation.validate_repository(self.root)[0], [])

    def test_missing_inline_image_and_reference_targets_fail(self):
        self.write("README.md", '[missing](missing.md)\n![image](missing.png)\n'
                   '[reference][ref]\n\n[ref]: missing-reference.md\n')
        errors, _ = validation.validate_repository(self.root)
        for name in ("missing.md", "missing.png", "missing-reference.md"):
            self.assertTrue(any(name in error for error in errors), errors)

    def test_code_samples_external_links_and_fragments_are_not_fetched(self):
        self.write("README.md", '`[example](missing.md)`\n\n```md\n[example](missing.md)\n```\n'
                   '[web](https://example.org/no-network)\n[mail](mailto:test@example.org)\n'
                   '[network-relative](//example.org/foo)\n[fragment](#heading)\n')
        with patch("socket.socket", side_effect=AssertionError("network attempted")):
            self.assertEqual(validation.validate_repository(self.root)[0], [])

    def test_local_path_traversal_and_symlink_escape_fail(self):
        self.write("README.md", '[escape](../outside.md)\n[linked](outside.json)\n')
        (self.root / "outside.json").symlink_to(self.root.parent / "outside.json")
        errors, _ = validation.validate_repository(self.root)
        self.assertTrue(any("local link leaves repository" in e for e in errors), errors)
        self.assertTrue(any("source symlink leaves repository" in e for e in errors), errors)

    def test_duplicate_json_keys_nonfinite_numbers_and_invalid_syntax_fail(self):
        for content, expected in (('{"a":1,"a":2}', "duplicate JSON property"),
                                  ('{"a":NaN}', "non-finite JSON number"),
                                  ('{"a":1e400}', "non-finite JSON number"),
                                  ('{"a":', "Expecting value")):
            with self.subTest(content=content):
                self.write("data/broken.json", content)
                errors, _ = validation.validate_repository(self.root)
                self.assertTrue(any(expected in e for e in errors), errors)

    def test_raw_float_tokens_cannot_lose_decimal_or_integral_precision(self):
        for token in ("1.00000000000000001", "9007199254740993.0", "1e23",
                      "1e-999", "-1e-999", "1e-999999999999999999999999"):
            with self.subTest(token=token):
                original = '{"history": [{"amount": ' + token + '}]}'
                target = self.write("data/numeric-input.json", original)
                errors, _ = validation.validate_repository(self.root)
                self.assertTrue(any("data/numeric-input.json: unsupported JSON numeric precision" in e
                                    for e in errors), errors)
                self.assertEqual(target.read_text(encoding="utf-8"), original)

    def test_original_pipeline_numbers_cannot_round_to_the_canonical_score(self):
        for canonical, token in ((1, "1.00000000000000001"), (0, "1e-999")):
            with self.subTest(canonical=canonical, token=token):
                target = self.pipeline_score(canonical, token)
                original = target.read_bytes()
                errors, _ = validation.validate_repository(self.root)
                self.assertTrue(any("data/funding-pipeline.json: unsupported JSON numeric precision" in e
                                    for e in errors), errors)
                self.assertEqual(target.read_bytes(), original)
        self.pipeline_score(1, "1.0000000000000002")
        errors, _ = validation.validate_repository(self.root)
        self.assertTrue(any("[score]: differs" in e for e in errors), errors)

    def test_out_of_range_original_scores_cannot_round_inside_schema_limits(self):
        for boundary, token in ((100, "100.00000000000000001"), (0, "-1e-999")):
            with self.subTest(boundary=boundary, token=token):
                register = copy.deepcopy(BASE["data/opportunities.json"])
                register["records"][0]["scoring"]["total"] = boundary
                raw = json.dumps(register).replace('"total": ' + str(boundary),
                                                   '"total": ' + token, 1)
                target = self.write("data/opportunities.json", raw)
                errors, _ = validation.validate_repository(self.root)
                self.assertTrue(any("data/opportunities.json: unsupported JSON numeric precision" in e
                                    for e in errors), errors)
                self.assertEqual(target.read_text(encoding="utf-8"), raw)

    def test_supported_decimal_spellings_whole_floats_and_signed_zero_still_pass(self):
        self.write("data/numeric-input.json", '{"exact_integer_float": 9007199254740992.0, '
                   '"exact_integral_exponent": 1e22, "subnormal": 5e-324}')
        for canonical, token in ((0.1, "0.10"), (0.1, "1e-1"), (1, "1.000"),
                                 (1, "1e0"), (0, "-0.000e999"), (0, "0e-999"), (100, "1e2")):
            with self.subTest(token=token):
                target = self.pipeline_score(canonical, token)
                original = target.read_bytes()
                self.assertEqual(validation.validate_repository(self.root)[0], [])
                self.assertEqual(target.read_bytes(), original)

    def test_cli_checks_original_numbers_in_normal_and_optimized_python(self):
        for options in ([], ["-O"]):
            for canonical, token, expected in ((1, "1.00000000000000001", 1),
                                                (0, "1e-999", 1), (0.1, "0.10", 0)):
                with self.subTest(options=options, token=token):
                    target = self.pipeline_score(canonical, token)
                    original = target.read_bytes()
                    result = subprocess.run(
                        [sys.executable, *options, str(ROOT / "scripts/validate_repository.py"),
                         "--root", str(self.root)], capture_output=True, text=True, check=False)
                    self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
                    self.assertIn("unsupported JSON numeric precision" if expected else "PASS:", result.stdout)
                    self.assertNotIn("Traceback", result.stdout + result.stderr)
                    self.assertEqual(target.read_bytes(), original)

    def test_symlink_loop_is_reported_without_an_uncaught_exception(self):
        (self.root / "loop.md").symlink_to("loop.md")
        self.write("README.md", "[loop](loop.md)\n")
        errors, _ = validation.validate_repository(self.root)
        self.assertTrue(any("Symlink loop" in error for error in errors), errors)

    def test_dependency_directories_are_excluded(self):
        for directory in validation.EXCLUDED_DIRS:
            self.write(directory + "/broken.json", "not json")
        self.assertEqual(validation.validate_repository(self.root)[0], [])


class WorkflowChecks(unittest.TestCase):
    def test_validation_workflow_is_read_only_and_unfiltered(self):
        # BaseLoader follows YAML scalar spelling, avoiding YAML 1.1's on=true conversion.
        workflow = yaml.load((ROOT / ".github/workflows/validate.yml").read_text(), Loader=yaml.BaseLoader)
        self.assertEqual(set(workflow["on"]), {"pull_request", "push"})
        self.assertEqual(workflow["permissions"], {"contents": "read"})
        self.assertEqual(workflow["on"]["pull_request"], {})
        self.assertEqual(workflow["on"]["push"], {"branches": ["main"]})
        job = workflow["jobs"]["validate"]
        self.assertNotIn("permissions", job)
        self.assertNotIn("environment", job)
        self.assertNotIn("secrets", job)
        actions = [step for step in job["steps"] if "uses" in step]
        self.assertEqual(len(actions), 2)
        for action in actions:
            self.assertRegex(action["uses"], r"^actions/(checkout|setup-python)@[0-9a-f]{40}$")
        self.assertEqual(actions[0]["with"]["persist-credentials"], "false")
        commands = [step["run"] for step in job["steps"] if "run" in step]
        self.assertIn("python -m unittest discover -s tests -v", commands)
        self.assertIn("python scripts/validate_repository.py", commands)
        self.assertFalse(any("--apply" in command or "--check" in command for command in commands))


if __name__ == "__main__":
    unittest.main()
