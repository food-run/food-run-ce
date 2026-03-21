#!/usr/bin/env python3
"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  narrow unit coverage for the central repo verifier workflow helpers

- Later Extension Points:
    --> Add helper-level tests here when later verifier slices extend the central workflow contract

- Role:
    --> Verifies that the repo-verify workflow stays routed through the central verifier
    --> Keeps helper-level coverage near the script boundary without inventing a broad new test structure
    --> Must stay small, explicit, and focused on verifier contract behavior

- Exports:
    --> `WorkflowContractTests` unittest coverage for `tools/script/verify.py`

- Consumed By:
    --> `python3 -m unittest discover -s tools/script -p 'test_*.py'`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
from __future__ import annotations

# ---------- imports and dependencies ----------

import importlib.util
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

# ---------- module loading ----------

# Load the verifier module directly from its script path.
VERIFY_PATH = Path(__file__).with_name('verify.py')
VERIFY_SPEC = importlib.util.spec_from_file_location('food_run_verify', VERIFY_PATH)
assert VERIFY_SPEC is not None and VERIFY_SPEC.loader is not None
VERIFY_MODULE = importlib.util.module_from_spec(VERIFY_SPEC)
VERIFY_SPEC.loader.exec_module(VERIFY_MODULE)

# ---------- workflow contract tests ----------


class WorkflowContractTests(unittest.TestCase):
    # Keep a passing sample close to the contract under test.
    def test_detects_central_verifier_command(self) -> None:
        workflow_text = "run: python3 tools/script/verify.py --ci\n"
        self.assertTrue(VERIFY_MODULE.workflow_runs_central_verifier(workflow_text))

    # Reject workflows that drift away from the central verifier.
    def test_rejects_missing_central_verifier_command(self) -> None:
        workflow_text = "run: python3 tools/script/other.py --ci\n"
        self.assertFalse(VERIFY_MODULE.workflow_runs_central_verifier(workflow_text))

    # Reject multiline blocks that can hide extra shell policy.
    def test_rejects_multiline_run_blocks(self) -> None:
        workflow_text = "run: |\n  python3 tools/script/verify.py --ci\n  echo hidden\n"
        self.assertFalse(VERIFY_MODULE.workflow_runs_central_verifier(workflow_text))

    # Ignore comments that mention the command without running it.
    def test_ignores_command_in_comments(self) -> None:
        workflow_text = "# python3 tools/script/verify.py --ci\nrun: python3 tools/script/other.py --ci\n"
        self.assertFalse(VERIFY_MODULE.workflow_runs_central_verifier(workflow_text))

    # Surface actionable failure output for workflow drift.
    def test_reports_actionable_workflow_contract_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            workflow_path = repo_root / '.github' / 'workflows' / 'repo-verify.yml'
            workflow_path.parent.mkdir(parents=True, exist_ok=True)
            workflow_path.write_text('run: python3 tools/script/other.py --ci\n', encoding='utf-8')

            output = io.StringIO()
            with redirect_stdout(output):
                result = VERIFY_MODULE.verify_repo_workflow_contract(repo_root)

        self.assertEqual(result, 1)
        self.assertIn('.github/workflows/repo-verify.yml', output.getvalue())
        self.assertIn('expected the only shell run step to be', output.getvalue())


# ---------- unittest entrypoint ----------


if __name__ == '__main__':
    unittest.main()
