#!/usr/bin/env python3
"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  Shared test infrastructure for Food Run

- Later Extension Points:
    --> Add reusable fixture builders here when more repo-control tests share the same setup seams

- Role:
    --> Common test utilities, base classes, and helpers for all tests
    --> Module loading helpers for importing from tools/scripts/
    --> File and fixture helpers

- Exports:
    --> `TestCase` - extended unittest.TestCase with helpers
    --> `load_module()` - dynamic module loader
    --> `write_file()` - file helper with directory creation

- Consumed By:
    --> All test files in tools/testing/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
from __future__ import annotations

# ---------- imports and dependencies ----------

import importlib.util
import tempfile
import unittest
from pathlib import Path

# ---------- module loading ----------

# Path to the scripts directory
SCRIPTS_PATH = Path(__file__).resolve().parents[2] / 'tools' / 'scripts'


def load_module(name: str, module_path: Path):
    """Load a Python module from a file path."""
    spec = importlib.util.spec_from_file_location(name, module_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_script(name: str):
    """Load a script from tools/scripts/ by name (without .py)."""
    return load_module(name, SCRIPTS_PATH / f'{name}.py')


# ---------- test helpers ----------


def write_file(path: Path, content: str) -> None:
    """Write one file with parent directories created first."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')


def make_heartbeat_note(
    scope: str,
    agent: str = 'PM',
    stamp: str = '2026-03-21 11:00 local',
    next_due: str = '2026-03-21 11:06 local',
) -> str:
    """Build a canonical heartbeat note fixture."""
    return "\n".join(
        [
            '# 💠 Heartbeat',
            '',
            f'- **Coordination File:** `docs/coordination/notes/{scope}-N1.md`',
            f'- **Scope:** `{scope}`',
            '- **Status:** active',
            f'- **Agent:** {agent}',
            '- **Files:** docs/coordination/active.md',
            '- **Blockers:** none',
            '- **Next Step:** keep the heartbeat fresh',
            f'- **Time:** {stamp}',
            f'- **Chat Summary Sent At:** {stamp}',
            '- **What Changed Since Last Check-In:** updated the fixture',
            '- **Current Work:** fixture coverage',
            '- **Current Paths:** docs/coordination/active.md',
            f'- **Next Check-In Due:** {next_due}',
            '',
        ]
    )


def make_active_workstream(
    scope: str,
    agent: str = 'PM',
    subagents: str = 'none',
    last_heartbeat: str = '2026-03-21 11:00 local',
    next_heartbeat: str = '2026-03-21 11:06 local',
) -> str:
    """Build a single active workstream section."""
    return "\n".join(
        [
            f'### `{scope}`',
            f'- **Scope:** `{scope}`',
            f'- **Current Agent:** {agent}',
            '- **Current Status:** active',
            '- **Active Paths:** tools/scripts/coordination_status.py',
            f'- **Active Subagents:** {subagents}',
            f'- **Last Heartbeat:** {last_heartbeat}',
            f'- **Next Expected Heartbeat:** {next_heartbeat}',
            '- **Latest Checkpoint:** `docs/coordination/checkpoints/{scope}-C1.md`',
            '- **Blockers:** none',
            '- **Next Recommended Action:** keep working',
        ]
    )


def make_active_doc(scope_or_multiple: str = 'S0-D4-T4') -> str:
    """Build a legacy active.md document with one workstream."""
    parts = [
        '# 💠 Active Coordination Status',
        '',
        '- **Generated At:** 2026-03-21 11:00 local',
        '- **Updated By:** PM',
        f'- **Active Scope:** `{scope_or_multiple}`',
        '- **Current Agent:** PM',
        '- **Current Status:** active',
        '- **Active Paths:** tools/scripts/coordination_status.py',
        '- **Active Subagents:** none',
        '- **Last Heartbeat:** 2026-03-21 11:00 local',
        '- **Next Expected Heartbeat:** 2026-03-21 11:06 local',
        '- **Latest Checkpoint:** `docs/coordination/checkpoints/{scope_or_multiple}-C1.md`',
        '- **Blockers:** none',
        '- **Next Recommended Action:** keep working',
    ]
    return "\n".join(parts)


def make_plural_active_doc(workstreams: list[str]) -> str:
    """Build a plural active.md document with multiple workstreams."""
    parts = [
        '# 💠 Active Coordination Status',
        '',
        '- **Generated At:** 2026-03-21 11:00 local',
        '- **Updated By:** PM',
        '- **Active Scope:** `multiple`',
        '',
        '## Active Workstreams',
        '',
    ]
    for ws in workstreams:
        parts.append(make_active_workstream(ws))
        parts.append('')
    return "\n".join(parts)


# ---------- test base class ----------


class TestCase(unittest.TestCase):
    """Extended TestCase with common helpers."""

    def setUp(self):
        """Create a temp directory for each test."""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.repo_root = self.temp_dir

    def tearDown(self):
        """Clean up temp directory."""
        import shutil

        shutil.rmtree(self.temp_dir)

    def write_active_doc(self, content: str):
        """Write an active.md file."""
        write_file(self.repo_root / 'docs' / 'coordination' / 'active.md', content)

    def write_task_doc(self, scope: str, content: str = '# task\n'):
        """Write a task coordination file."""
        write_file(self.repo_root / 'docs' / 'coordination' / 'tasks' / f'{scope}.md', content)

    def write_heartbeat_note(self, scope: str, content: str | None = None):
        """Write a heartbeat note."""
        if content is None:
            content = make_heartbeat_note(scope)
        write_file(self.repo_root / 'docs' / 'coordination' / 'notes' / f'{scope}-N1.md', content)
