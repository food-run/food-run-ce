#!/usr/bin/env python3
"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  focused unit coverage for the release-preparation scaffold and workflow wrapper

- Later Extension Points:
    --> Add later rollout-path coverage here only after Sprint 0 D5 owns real deployment behavior

- Role:
    --> Verifies that the release scaffold stays honest about being prepare-only in Sprint 0
    --> Keeps the manual release workflow bound to the central release script seam
    --> Must stay narrow so the tests do not invent deployment maturity before the platform work exists

- Exports:
    --> `ReleaseScaffoldTests` unittest coverage for `tools/scripts/release.py` and `.github/workflows/cd.yml`

- Consumed By:
    --> `python3 -m unittest discover -s tools/testing -p 'test_*.py'`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
from __future__ import annotations

# ---------- imports and dependencies ----------

import io
from contextlib import redirect_stdout
from pathlib import Path

from shared.testkit import TestCase, load_script

# ---------- module loading ----------

RELEASE_MODULE = load_script('release')
VERIFY_MODULE = load_script('verify')

# ---------- release scaffold tests ----------


class ReleaseScaffoldTests(TestCase):
    def test_prepare_reports_prepared_only_status(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            result = RELEASE_MODULE.print_prepare_summary(ci=False)

        self.assertEqual(result, 0)
        self.assertIn('RELEASE PREP SUMMARY', output.getvalue())
        self.assertIn(RELEASE_MODULE.PREPARED_ONLY_MESSAGE, output.getvalue())

    def test_deploy_action_fails_with_d5_guidance(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            result = RELEASE_MODULE.reject_deploy()

        self.assertEqual(result, 1)
        self.assertIn('Sprint 0 D5', output.getvalue())

    def test_cd_workflow_runs_central_release_script(self) -> None:
        workflow_text = (Path(__file__).resolve().parents[3] / '.github' / 'workflows' / 'cd.yml').read_text(encoding='utf-8')
        self.assertEqual(VERIFY_MODULE.workflow_run_blocks(workflow_text), [RELEASE_MODULE.CENTRAL_RELEASE_COMMAND])

    def test_cd_workflow_is_manual_only(self) -> None:
        workflow_text = (Path(__file__).resolve().parents[3] / '.github' / 'workflows' / 'cd.yml').read_text(encoding='utf-8')
        self.assertIn('workflow_dispatch:', workflow_text)
        self.assertNotIn('push:', workflow_text)
        self.assertNotIn('pull_request:', workflow_text)
