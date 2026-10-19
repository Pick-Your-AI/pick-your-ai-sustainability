"""Fail-closed discovery controls for unreadable source directories.

The scandir fault is injected rather than relying on chmod, because a GitHub
runner (or a local developer) may execute these tests with elevated privileges.
"""

import contextlib
import errno
import importlib.util
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("sustainability_validation", ROOT / "scripts/validate_repository.py")
validation = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validation)


class DirectoryEnumerationChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        schema = json.loads((ROOT / "data/opportunities.schema.json").read_text(encoding="utf-8"))
        required = schema["properties"]["records"]["items"]["required"]
        score_fields = schema["properties"]["records"]["items"]["properties"]["scoring"]["required"]
        template = {name: None for name in required}
        template["scoring"] = {name: None for name in score_fields}
        documents = {
            "data/opportunities.json": {
                "schema_version": "sustainability-opportunity-register/v1",
                "last_verified": "2026-10-19",
                "records_count": 0,
                "records": [],
                "important_limitations": ["Synthetic fixture only"],
            },
            "data/opportunities.schema.json": schema,
            "templates/opportunity-record.json": template,
            "data/research-freshness.json": {"records_count": 0, "source_count": 0, "sources": []},
            "data/funding-pipeline.json": {"record_count": 0, "records": []},
        }
        for name, content in documents.items():
            file = self.root / name
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_text(json.dumps(content), encoding="utf-8")
        self.blocked_dir = self.root / "research" / "unreadable"
        self.blocked_dir.mkdir(parents=True)
        (self.blocked_dir / "malformed.json").write_text("{", encoding="utf-8")

    def denied_scandir(self, denied):
        """Only a specific path fails, regardless of the process user ID."""
        actual_scandir = os.scandir

        def scan(path):
            if Path(path) == denied:
                raise PermissionError(errno.EACCES, "Permission denied", os.fspath(path))
            return actual_scandir(path)

        return patch.object(validation.os, "scandir", side_effect=scan)

    def test_directory_error_is_not_reported_as_a_successful_scan(self):
        with self.denied_scandir(self.blocked_dir):
            errors, counts = validation.validate_repository(self.root)
        self.assertEqual(counts["json_files"], 5)
        self.assertTrue(any(
            "research/unreadable: cannot enumerate directory: Permission denied" in error
            for error in errors
        ), errors)

    def test_root_directory_error_is_reported_as_well(self):
        with self.denied_scandir(self.root):
            errors, counts = validation.validate_repository(self.root)
        self.assertEqual(counts["json_files"], 0)
        self.assertTrue(any(
            ".: cannot enumerate directory: Permission denied" in error
            for error in errors
        ), errors)

    def test_cli_returns_failure_on_directory_error(self):
        output = io.StringIO()
        with self.denied_scandir(self.blocked_dir), contextlib.redirect_stdout(output):
            exit_code = validation.main(["--root", str(self.root)])
        self.assertEqual(exit_code, 1)
        self.assertIn("research/unreadable: cannot enumerate directory", output.getvalue())
        self.assertIn("FAIL:", output.getvalue())

    def test_permission_recovery_restores_normal_json_validation(self):
        with self.denied_scandir(self.blocked_dir):
            inaccessible, _ = validation.validate_repository(self.root)
        restored, _ = validation.validate_repository(self.root)
        self.assertTrue(any("cannot enumerate directory" in error for error in inaccessible))
        self.assertFalse(any("cannot enumerate directory" in error for error in restored))
        self.assertTrue(any("research/unreadable/malformed.json" in error for error in restored))

    def test_dependency_directories_stay_excluded(self):
        ignored = self.root / ".venv"
        ignored.mkdir()
        (ignored / "malformed.json").write_text("{", encoding="utf-8")
        # Repair the non-ignored fixture so it does not contribute an error.
        (self.blocked_dir / "malformed.json").write_text("{}", encoding="utf-8")
        with self.denied_scandir(ignored):
            errors, counts = validation.validate_repository(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(counts["json_files"], 6)

    def test_valid_retry_does_not_keep_an_old_scan_error(self):
        file = self.blocked_dir / "malformed.json"
        file.write_text("{}", encoding="utf-8")
        original = file.read_bytes()
        with self.denied_scandir(self.blocked_dir):
            errors, _ = validation.validate_repository(self.root)
        self.assertTrue(any("cannot enumerate directory" in error for error in errors))
        recovered, counts = validation.validate_repository(self.root)
        self.assertEqual(recovered, [])
        self.assertEqual(counts["json_files"], 6)
        self.assertEqual(file.read_bytes(), original)

    def test_missing_error_filename_uses_root_diagnostic(self):
        actual_scandir = os.scandir

        def scan(path):
            if Path(path) == self.blocked_dir:
                raise OSError(errno.EIO, "Input/output error")
            return actual_scandir(path)

        with patch.object(validation.os, "scandir", side_effect=scan):
            errors, _ = validation.validate_repository(self.root)
        self.assertEqual(errors, [".: cannot enumerate directory: Input/output error"])

    def test_multiple_directory_errors_accumulate(self):
        second = self.root / "research" / "second"
        second.mkdir()
        actual_scandir = os.scandir

        def scan(path):
            if Path(path) in {self.blocked_dir, second}:
                raise PermissionError(errno.EACCES, "Permission denied", os.fspath(path))
            return actual_scandir(path)

        with patch.object(validation.os, "scandir", side_effect=scan):
            errors, counts = validation.validate_repository(self.root)
        self.assertEqual(errors, [
            "research/second: cannot enumerate directory: Permission denied",
            "research/unreadable: cannot enumerate directory: Permission denied",
        ])
        self.assertEqual(counts["json_files"], 5)

    def test_error_during_scandir_iteration_is_reported(self):
        actual_scandir = os.scandir
        blocked = self.blocked_dir

        class InterruptedScan:
            def __enter__(self):
                self.iterator = actual_scandir(blocked)
                self.yielded = False
                return self

            def __exit__(self, *args):
                self.iterator.close()

            def __iter__(self):
                return self

            def __next__(self):
                if not self.yielded:
                    self.yielded = True
                    return next(self.iterator)
                raise OSError(errno.EIO, "Input/output error", os.fspath(blocked))

        def scan(path):
            return InterruptedScan() if Path(path) == blocked else actual_scandir(path)

        with patch.object(validation.os, "scandir", side_effect=scan):
            errors, counts = validation.validate_repository(self.root)
        self.assertEqual(errors, [
            "research/unreadable: cannot enumerate directory: Input/output error",
        ])
        self.assertEqual(counts["json_files"], 5)


if __name__ == "__main__":
    unittest.main()
