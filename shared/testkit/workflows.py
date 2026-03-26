#!/usr/bin/env python3
"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  narrow contract coverage for the pull-request gate workflows

- Later Extension Points:
    --> Add more text-level workflow contract checks here when later repo-control gates extend the PR review contract

- Role:
    --> Verifies that the PR workflows keep enforcing the documented reviewer-facing narrative and protected-path posture
    --> Keeps Sprint 0 workflow coverage small by checking committed workflow text instead of building a custom runner
    --> Must stay focused on merge-gate contract drift, not generic workflow execution

- Exports:
    --> `PullRequestWorkflowContractTests` unittest coverage for D4 PR workflow contracts

- Consumed By:
    --> `python3 tools/scripts/verify.py --skip-coordination --skip-frontend`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """

from __future__ import annotations

# ---------- imports and dependencies ----------

from pathlib import Path

from shared.testkit import TestCase

# ---------- workflow fixtures ----------

REPO_ROOT = Path(__file__).resolve().parents[2]
DOCS_GUARD_PATH = REPO_ROOT / '.github' / 'workflows' / 'docs-guard.yml'
PROTECTED_PATHS_PATH = REPO_ROOT / '.github' / 'workflows' / 'protected-paths.yml'

# ---------- pull-request workflow contract tests ----------


class PullRequestWorkflowContractTests(TestCase):
    def test_docs_guard_requires_core_narrative_sections(self) -> None:
        workflow_text = DOCS_GUARD_PATH.read_text(encoding='utf-8')
        self.assertIn('const requiredNarrativeSections = [', workflow_text)
        self.assertIn('"Summary"', workflow_text)
        self.assertIn('"Why this change"', workflow_text)
        self.assertIn('"Files and boundaries"', workflow_text)
        self.assertIn('"Verification"', workflow_text)

    def test_protected_paths_covers_all_workflow_files(self) -> None:
        workflow_text = PROTECTED_PATHS_PATH.read_text(encoding='utf-8')
        self.assertIn('["repo-control workflows", /^\\.github\\/workflows\\//]', workflow_text)
        self.assertIn('new Set(', workflow_text)
