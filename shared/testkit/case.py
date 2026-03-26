#!/usr/bin/env python3
"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  shared unittest base case for repo-control and rebuild verification

- Later Extension Points:
    --> Add bounded temp-repo helpers here when more shared suites need the same filesystem setup

- Role:
    --> Owns the common unittest base class used by shared testkit suites
    --> Keeps temp-repo setup and scoped file-writing helpers in one deterministic home
    --> Must stay test-focused instead of becoming a second generic helper bucket

- Exports:
    --> `TestCase` with temp-repo setup and coordination-file helpers

- Consumed By:
    --> shared testkit suites and future shared verification modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """

from __future__ import annotations

# ---------- imports and dependencies ----------

import shutil
import tempfile
import unittest
from pathlib import Path

from .fixtures import make_heartbeat_note
from .helpers import write_file

# ---------- shared unittest case ----------


# Keep every shared suite on the same temp-repo baseline.
class TestCase(unittest.TestCase):
    # Create one isolated temp repo per test method.
    def setUp(self) -> None:
        self.temp_dir = Path(tempfile.mkdtemp())
        self.repo_root = self.temp_dir

    # Remove the temp repo after each test method.
    def tearDown(self) -> None:
        shutil.rmtree(self.temp_dir)

    # Write one active dashboard fixture into the temp repo.
    def write_active_doc(self, content: str) -> None:
        write_file(self.repo_root / 'docs' / 'coordination' / 'active.md', content)

    # Write one stable task packet fixture into the temp repo.
    def write_task_doc(self, scope: str, content: str = '# task\n') -> None:
        write_file(self.repo_root / 'docs' / 'coordination' / 'tasks' / f'{scope}.md', content)

    # Write one official heartbeat note fixture into the temp repo.
    def write_heartbeat_note(self, scope: str, content: str | None = None) -> None:
        write_file(
            self.repo_root / 'docs' / 'coordination' / 'notes' / f'{scope}-N1.md',
            content or make_heartbeat_note(scope),
        )
