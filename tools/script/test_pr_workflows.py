#!/usr/bin/env python3
"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  narrow contract coverage for the pull-request gate workflows

- Later Extension Points:
    --> Add more text-level workflow contract checks if later D4 gates extend the PR review contract

- Role:
    --> Verifies that the PR workflows keep enforcing the documented reviewer-facing narrative and protected-path posture
    --> Keeps Sprint 0 workflow coverage small by checking the committed workflow text instead of building a custom runner
    --> Must stay focused on merge-gate contract drift, not generic workflow execution

- Exports:
    --> `PullRequestWorkflowContractTests` unittest coverage for D4 PR workflow contracts

- Consumed By:
    --> `python3 -m unittest discover -s tools/script -p 'test_*.py'`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
from __future__ import annotations

# ---------- imports and dependencies ----------

import unittest
from pathlib import Path

# ---------- workflow fixtures ----------

REPO_ROOT = Path(__file__).resolve().parents[2]
DOCS_GUARD_PATH = REPO_ROOT / '.github' / 'workflows' / 'docs-guard.yml'
PROTECTED_PATHS_PATH = REPO_ROOT / '.github' / 'workflows' / 'protected-paths.yml'

# ---------- pull-request workflow contract tests ----------


class PullRequestWorkflowContractTests(unittest.TestCase):
    # Keep the docs guard tied to the reviewer-facing PR sections.
    def test_docs_guard_requires_core_narrative_sections(self) -> None:
        workflow_text = DOCS_GUARD_PATH.read_text(encoding='utf-8')

        self.assertIn('const requiredNarrativeSections = [', workflow_text)
        self.assertIn('"Summary"', workflow_text)
        self.assertIn('"Why this change"', workflow_text)
        self.assertIn('"Files and boundaries"', workflow_text)
        self.assertIn('"Verification"', workflow_text)
        self.assertIn('required PR sections with real reviewer-facing details', workflow_text)

    # Keep docs and ADR enforcement conditional on governed changes only.
    def test_docs_guard_keeps_governed_change_gate_separate(self) -> None:
        workflow_text = DOCS_GUARD_PATH.read_text(encoding='utf-8')

        self.assertIn('if (governedFiles.length === 0) {', workflow_text)
        self.assertIn('fill in the \'Docs and ADR delta\' section', workflow_text)
        self.assertIn('update docs/adr.md for governed repo-control or shared-understanding changes before merge.', workflow_text)

    # Keep every workflow edit inside the protected-path gate.
    def test_protected_paths_covers_all_workflow_files(self) -> None:
        workflow_text = PROTECTED_PATHS_PATH.read_text(encoding='utf-8')

        self.assertIn('["repo-control workflows", /^\\.github\\/workflows\\//]', workflow_text)
        self.assertIn('new Set(', workflow_text)


# ---------- unittest entrypoint ----------


if __name__ == '__main__':
    unittest.main()
