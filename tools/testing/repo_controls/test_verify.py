#!/usr/bin/env python3
"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  narrow unit coverage for the central repo verifier workflow helpers

- Later Extension Points:
    --> Add helper-level verifier tests here when later repo-control checks extend the shared contract

- Role:
    --> Verifies that the repo-verify workflow stays routed through the central verifier
    --> Keeps helper-level coverage near the script boundary without inventing a broad new test structure
    --> Must stay small, explicit, and focused on verifier contract behavior

- Exports:
    --> `WorkflowContractTests` unittest coverage for `tools/scripts/verify.py`

- Consumed By:
    --> `python3 -m unittest discover -s tools/testing -p 'test_*.py'`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
from __future__ import annotations

# ---------- imports and dependencies ----------

import io
from contextlib import redirect_stdout
from pathlib import Path

from shared.testkit import TestCase, load_script, write_file

# ---------- module loading ----------

VERIFY_MODULE = load_script('verify')

# ---------- workflow contract tests ----------


class WorkflowContractTests(TestCase):
    def test_detects_central_verifier_command(self) -> None:
        workflow_text = 'run: python3 tools/scripts/verify.py --ci\n'
        self.assertTrue(VERIFY_MODULE.workflow_runs_central_verifier(workflow_text))

    def test_rejects_missing_central_verifier_command(self) -> None:
        workflow_text = 'run: python3 tools/scripts/other.py --ci\n'
        self.assertFalse(VERIFY_MODULE.workflow_runs_central_verifier(workflow_text))

    def test_rejects_multiline_run_blocks(self) -> None:
        workflow_text = 'run: |\n  python3 tools/scripts/verify.py --ci\n  echo hidden\n'
        self.assertFalse(VERIFY_MODULE.workflow_runs_central_verifier(workflow_text))

    def test_reports_actionable_workflow_contract_failure(self) -> None:
        workflow_path = self.repo_root / '.github' / 'workflows' / 'repo-verify.yml'
        write_file(workflow_path, 'run: python3 tools/scripts/other.py --ci\n')

        output = io.StringIO()
        with redirect_stdout(output):
            result = VERIFY_MODULE.verify_repo_workflow_contract(self.repo_root)

        self.assertEqual(result, 1)
        self.assertIn(str(Path('.github/workflows/repo-verify.yml')), output.getvalue())
        self.assertIn('expected the only shell run step to be', output.getvalue())
