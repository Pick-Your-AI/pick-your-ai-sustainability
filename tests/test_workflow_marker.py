"""Run the actual workflow bootstrap offline with a simulated GitHub response."""
import base64
import contextlib
import io
import json
import os
import tempfile
import textwrap
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / '.github/workflows/native-relationships.yml'
BOOTSTRAP = textwrap.dedent(WORKFLOW.read_text().split("python3 - <<'PY'\n", 1)[1]
                           .split('\n          PY', 1)[0])
REPOSITORY = 'Pick-Your-AI/pick-your-ai-sustainability'
SHA = 'a' * 40


class SimulatedGitHub:
    def __init__(self, message):
        self.message = message
        self.urls = []

    def open(self, request, timeout):
        self.urls.append(request.full_url)
        if '/git/ref/' in request.full_url:
            value = {'object': {'sha': SHA}}
        elif '/commits/' in request.full_url:
            value = {'sha': SHA, 'author': {'login': 'CompleteDotTech', 'id': 5861166},
                     'commit': {'message': self.message}}
        elif '/contents/' in request.full_url:
            path = request.full_url.split('/contents/', 1)[1].split('?', 1)[0]
            content = (ROOT / path).read_bytes()
            value = {'type': 'file', 'encoding': 'base64', 'size': len(content),
                     'content': base64.b64encode(content).decode()}
        else:
            raise AssertionError('Unexpected bootstrap URL')
        return io.BytesIO(json.dumps(value).encode())


class MarkerGateChecks(unittest.TestCase):
    def bootstrap(self, message):
        fake = SimulatedGitHub(message)
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            env = {'GITHUB_REPOSITORY': REPOSITORY, 'NATIVE_HEAD_SHA': SHA,
                   'GITHUB_TOKEN': 'offline-simulation',
                   'GITHUB_OUTPUT': str(target / 'outputs'),
                   'GITHUB_STEP_SUMMARY': str(target / 'summary')}
            previous = os.getcwd()
            try:
                os.chdir(directory)
                with patch.dict(os.environ, env), patch('urllib.request.build_opener', return_value=fake), \
                        contextlib.redirect_stdout(io.StringIO()):
                    try:
                        exec(compile(BOOTSTRAP, 'workflow-bootstrap', 'exec'), {})
                    except SystemExit as exit:
                        self.assertEqual(exit.code, 0)
                outputs = (target / 'outputs').read_text()
                downloaded = (target / 'scripts/apply_native_relationships.py').exists()
                summary = (target / 'summary').read_text() if (target / 'summary').exists() else ''
            finally:
                os.chdir(previous)
        return fake.urls, outputs, downloaded, summary

    def test_missing_marker_skips_after_two_identity_reads_before_downloads(self):
        urls, outputs, downloaded, summary = self.bootstrap('docs: record final independent audit')
        self.assertEqual(len(urls), 2)
        self.assertTrue(all('/contents/' not in url for url in urls))
        self.assertEqual(outputs, 'apply_relationships=false\n')
        self.assertFalse(downloaded)
        self.assertIn('skipped', summary)

    def test_verified_marker_allows_pinned_files_and_outputs_true(self):
        urls, outputs, downloaded, _ = self.bootstrap('chore: apply declared graph [native-relationships]')
        self.assertEqual(len(urls), 4)
        self.assertEqual(outputs, 'apply_relationships=true\n')
        self.assertTrue(downloaded)


if __name__ == '__main__':
    unittest.main()
