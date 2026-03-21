#!/usr/bin/env python3
"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  focused unit coverage for the D4 release-preparation scaffold and workflow wrapper

- Later Extension Points:
    --> Add D5 deploy-path coverage only after real rollout behavior exists

- Role:
    --> Verifies that the release scaffold stays honest about being prepare-only in D4
    --> Keeps the manual release workflow bound to the central release script seam
    --> Must stay narrow so the tests do not invent deployment maturity before D5

- Exports:
    --> `ReleaseScaffoldTests` unittest coverage for `tools/script/release.py` and `.github/workflows/cd.yml`

- Consumed By:
    --> `python3 -m unittest discover -s tools/script -p 'test_*.py'`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
from __future__ import annotations

# ---------- imports and dependencies ----------

import importlib.util
import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path

# ---------- module loading ----------

# Load the release module directly from its script path.
RELEASE_PATH = Path(__file__).with_name('release.py')
RELEASE_SPEC = importlib.util.spec_from_file_location('food_run_release', RELEASE_PATH)
assert RELEASE_SPEC is not None and RELEASE_SPEC.loader is not None
RELEASE_MODULE = importlib.util.module_from_spec(RELEASE_SPEC)
RELEASE_SPEC.loader.exec_module(RELEASE_MODULE)

# Load the verifier module for workflow run-block parsing reuse.
VERIFY_PATH = Path(__file__).with_name('verify.py')
VERIFY_SPEC = importlib.util.spec_from_file_location('food_run_verify', VERIFY_PATH)
assert VERIFY_SPEC is not None and VERIFY_SPEC.loader is not None
VERIFY_MODULE = importlib.util.module_from_spec(VERIFY_SPEC)
VERIFY_SPEC.loader.exec_module(VERIFY_MODULE)

# ---------- release scaffold tests ----------


class ReleaseScaffoldTests(unittest.TestCase):
    # Keep the prepare path honest and human-readable.
    def test_prepare_reports_prepared_only_status(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            result = RELEASE_MODULE.print_prepare_summary(ci=False)

        self.assertEqual(result, 0)
        self.assertIn('RELEASE PREP SUMMARY', output.getvalue())
        self.assertIn(RELEASE_MODULE.PREPARED_ONLY_MESSAGE, output.getvalue())

    # Reject deploy claims until D5 owns rollout behavior.
    def test_deploy_action_fails_with_d5_guidance(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            result = RELEASE_MODULE.reject_deploy()

        self.assertEqual(result, 1)
        self.assertIn('Sprint 0 D4', output.getvalue())
        self.assertIn('Sprint 0 D5', output.getvalue())

    # Keep the CD workflow bound to one central release command.
    def test_cd_workflow_runs_central_release_script(self) -> None:
        workflow_text = (Path(__file__).resolve().parents[2] / '.github' / 'workflows' / 'cd.yml').read_text(encoding='utf-8')

        self.assertEqual(
            VERIFY_MODULE.workflow_run_blocks(workflow_text),
            [RELEASE_MODULE.CENTRAL_RELEASE_COMMAND],
        )

    # Keep release prep manual-only until D5 owns real rollout behavior.
    def test_cd_workflow_is_manual_only(self) -> None:
        workflow_text = (Path(__file__).resolve().parents[2] / '.github' / 'workflows' / 'cd.yml').read_text(encoding='utf-8')

        self.assertIn('workflow_dispatch:', workflow_text)
        self.assertNotIn('push:', workflow_text)
        self.assertNotIn('pull_request:', workflow_text)
