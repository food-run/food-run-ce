#!/usr/bin/env python3
"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  focused unit coverage for plural coordination status parsing and evidence checks

- Later Extension Points:
    --> Add machine-specific scheduler coverage only if the repo later owns those adapters

- Role:
    --> Verifies legacy and plural active dashboard parsing without creating a second test harness
    --> Keeps per-scope freshness and subagent-evidence checks covered before reporter automation becomes mandatory
    --> Must stay close to `tools/script/coordination_status.py` so policy drift is obvious

- Exports:
    --> `CoordinationStatusTests` unittest coverage for `tools/script/coordination_status.py` watch and reminder behavior

- Consumed By:
    --> `python3 -m unittest discover -s tools/script -p 'test_*.py'`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
from __future__ import annotations

# ---------- imports and dependencies ----------

import importlib.util
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

# ---------- module loading ----------

# Load the coordination module directly from its script path.
COORDINATION_PATH = Path(__file__).with_name('coordination_status.py')
COORDINATION_SPEC = importlib.util.spec_from_file_location('food_run_coordination_status', COORDINATION_PATH)
assert COORDINATION_SPEC is not None and COORDINATION_SPEC.loader is not None
COORDINATION_MODULE = importlib.util.module_from_spec(COORDINATION_SPEC)
COORDINATION_SPEC.loader.exec_module(COORDINATION_MODULE)

# ---------- test helpers ----------


# Write one file with parent directories created first.
def write_file(path: Path, content: str) -> None:
    # Keep each fixture write terse and explicit.
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')


# Build a canonical heartbeat note fixture.
def note_body(scope: str, agent: str = 'PM', stamp: str = '2026-03-21 11:00 local', next_due: str = '2026-03-21 11:06 local') -> str:
    # Keep the required fields aligned with the coordination rule.
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


# ---------- coordination runtime tests ----------


class CoordinationStatusTests(unittest.TestCase):
    # Keep the legacy dashboard shape working as a one-workstream fallback.
    def test_parses_legacy_active_scope_as_one_workstream(self) -> None:
        active_text = "\n".join(
            [
                '# 💠 Active Coordination Status',
                '',
                '- **Generated At:** 2026-03-21 11:00 local',
                '- **Updated By:** PM',
                '- **Active Scope:** `S0-D4-T4`',
                '- **Current Agent:** PM',
                '- **Current Status:** active',
                '- **Active Paths:** tools/script/coordination_status.py',
                '- **Active Subagents:** none',
                '- **Last Heartbeat:** 2026-03-21 11:00 local',
                '- **Next Expected Heartbeat:** 2026-03-21 11:06 local',
                '- **Latest Checkpoint:** `docs/coordination/checkpoints/S0-D4-T4-C1.md`',
                '- **Blockers:** none',
                '- **Next Recommended Action:** keep working',
            ]
        )

        workstreams = COORDINATION_MODULE.parse_active_workstreams(active_text)

        self.assertEqual(len(workstreams), 1)
        self.assertEqual(COORDINATION_MODULE.parse_scope(workstreams[0]['Scope']), 'S0-D4-T4')

    # Parse plural workstreams into independent normalized blocks.
    def test_parses_plural_active_workstreams(self) -> None:
        active_text = "\n".join(
            [
                '# 💠 Active Coordination Status',
                '',
                '- **Generated At:** 2026-03-21 11:00 local',
                '- **Updated By:** PM',
                '- **Active Scope:** `multiple`',
                '',
                '## Active Workstreams',
                '',
                '### `S0-D4-T4`',
                '- **Scope:** `S0-D4-T4`',
                '- **Current Agent:** PM',
                '- **Current Status:** active',
                '- **Active Paths:** tools/script/coordination_status.py',
                '- **Active Subagents:** reporter',
                '- **Last Heartbeat:** 2026-03-21 11:00 local',
                '- **Next Expected Heartbeat:** 2026-03-21 11:06 local',
                '- **Latest Checkpoint:** `docs/coordination/checkpoints/S0-D4-T4-C1.md`',
                '- **Blockers:** none',
                '- **Next Recommended Action:** keep working',
                '',
                '### `S0-D4-T5`',
                '- **Scope:** `S0-D4-T5`',
                '- **Current Agent:** PM',
                '- **Current Status:** active',
                '- **Active Paths:** .opencode/agents/reporter.md',
                '- **Active Subagents:** none',
                '- **Last Heartbeat:** 2026-03-21 11:00 local',
                '- **Next Expected Heartbeat:** 2026-03-21 11:06 local',
                '- **Latest Checkpoint:** `docs/coordination/checkpoints/S0-D4-T5-C1.md`',
                '- **Blockers:** none',
                '- **Next Recommended Action:** keep working',
            ]
        )

        workstreams = COORDINATION_MODULE.parse_active_workstreams(active_text)

        self.assertEqual([COORDINATION_MODULE.parse_scope(item['Scope']) for item in workstreams], ['S0-D4-T4', 'S0-D4-T5'])

    # Reject mixed singular and plural dashboard shapes.
    def test_rejects_ambiguous_mixed_active_shapes(self) -> None:
        active_text = "\n".join(
            [
                '# 💠 Active Coordination Status',
                '',
                '- **Generated At:** 2026-03-21 11:00 local',
                '- **Updated By:** PM',
                '- **Active Scope:** `S0-D4-T4`',
                '',
                '## Active Workstreams',
                '',
                '### `S0-D4-T4`',
                '- **Scope:** `S0-D4-T4`',
            ]
        )

        with self.assertRaises(ValueError):
            COORDINATION_MODULE.parse_active_workstreams(active_text)

    # Prefer official notes and ignore later draft files.
    def test_latest_note_ignores_drafts_and_malformed_suffixes(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            notes_dir = Path(temp_dir)
            write_file(notes_dir / 'S0-D4-T4-N1.md', note_body('S0-D4-T4'))
            write_file(notes_dir / 'S0-D4-T4-N2.draft.md', note_body('S0-D4-T4'))
            write_file(notes_dir / 'S0-D4-T4-Nx.md', note_body('S0-D4-T4'))

            latest = COORDINATION_MODULE.latest_note(notes_dir, 'S0-D4-T4')

        self.assertIsNotNone(latest)
        self.assertEqual(latest.name, 'S0-D4-T4-N1.md')

    # Prefer the newest matching agent note over newer PM notes.
    def test_latest_note_for_agent_prefers_newest_matching_agent(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            notes_dir = Path(temp_dir)
            write_file(notes_dir / 'S0-D4-T4-N1.md', note_body('S0-D4-T4', agent='reporter'))
            write_file(notes_dir / 'S0-D4-T4-N2.md', note_body('S0-D4-T4', agent='PM'))
            write_file(notes_dir / 'S0-D4-T4-N3.md', note_body('S0-D4-T4', agent='reporter'))

            latest = COORDINATION_MODULE.latest_note_for_agent(notes_dir, 'S0-D4-T4', 'reporter')

        self.assertIsNotNone(latest)
        self.assertEqual(latest.name, 'S0-D4-T4-N3.md')

    # Name the overdue scope directly in verification failures.
    def test_verify_reports_overdue_scope_with_scope_name(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            active_text = "\n".join(
                [
                    '# 💠 Active Coordination Status',
                    '',
                    '- **Generated At:** 2026-03-21 11:00 local',
                    '- **Updated By:** PM',
                    '- **Active Scope:** `multiple`',
                    '',
                    '## Active Workstreams',
                    '',
                    '### `S0-D4-T4`',
                    '- **Scope:** `S0-D4-T4`',
                    '- **Current Agent:** PM',
                    '- **Current Status:** active',
                    '- **Active Paths:** tools/script/coordination_status.py',
                    '- **Active Subagents:** none',
                    '- **Last Heartbeat:** 2026-03-21 11:00 local',
                    '- **Next Expected Heartbeat:** 2026-03-21 11:06 local',
                    '- **Latest Checkpoint:** `docs/coordination/checkpoints/S0-D4-T4-C1.md`',
                    '- **Blockers:** none',
                    '- **Next Recommended Action:** keep working',
                ]
            )
            write_file(repo_root / 'docs' / 'coordination' / 'active.md', active_text)
            write_file(repo_root / 'docs' / 'coordination' / 'tasks' / 'S0-D4-T4.md', '# task\n')
            write_file(
                repo_root / 'docs' / 'coordination' / 'notes' / 'S0-D4-T4-N1.md',
                note_body('S0-D4-T4', stamp='2026-03-21 11:00 local', next_due='2026-03-21 11:06 local'),
            )

            output = io.StringIO()
            with redirect_stdout(output):
                result = COORDINATION_MODULE.verify_coordination(repo_root, scope_override=None, max_gap_minutes=6)

        self.assertEqual(result, 1)
        self.assertIn('S0-D4-T4: next expected heartbeat is already overdue', output.getvalue())

    # Require fresh note evidence for every listed subagent.
    def test_verify_requires_subagent_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            active_text = "\n".join(
                [
                    '# 💠 Active Coordination Status',
                    '',
                    '- **Generated At:** 2026-03-21 11:00 local',
                    '- **Updated By:** PM',
                    '- **Active Scope:** `multiple`',
                    '',
                    '## Active Workstreams',
                    '',
                    '### `S0-D4-T4`',
                    '- **Scope:** `S0-D4-T4`',
                    '- **Current Agent:** PM',
                    '- **Current Status:** active',
                    '- **Active Paths:** tools/script/coordination_status.py',
                    '- **Active Subagents:** reporter',
                    '- **Last Heartbeat:** 2099-03-21 11:19 local',
                    '- **Next Expected Heartbeat:** 2099-03-21 11:25 local',
                    '- **Latest Checkpoint:** `docs/coordination/checkpoints/S0-D4-T4-C1.md`',
                    '- **Blockers:** none',
                    '- **Next Recommended Action:** keep working',
                ]
            )
            write_file(repo_root / 'docs' / 'coordination' / 'active.md', active_text)
            write_file(repo_root / 'docs' / 'coordination' / 'tasks' / 'S0-D4-T4.md', '# task\n')
            write_file(
                repo_root / 'docs' / 'coordination' / 'notes' / 'S0-D4-T4-N1.md',
                note_body('S0-D4-T4', stamp='2099-03-21 11:19 local', next_due='2099-03-21 11:25 local'),
            )

            output = io.StringIO()
            with redirect_stdout(output):
                result = COORDINATION_MODULE.verify_coordination(repo_root, scope_override=None, max_gap_minutes=6)

        self.assertEqual(result, 1)
        self.assertIn('missing recent note evidence for subagent reporter', output.getvalue())

    # Accept fresh subagent evidence when the matching note exists.
    def test_verify_accepts_recent_subagent_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            active_text = "\n".join(
                [
                    '# 💠 Active Coordination Status',
                    '',
                    '- **Generated At:** 2026-03-21 11:00 local',
                    '- **Updated By:** PM',
                    '- **Active Scope:** `multiple`',
                    '',
                    '## Active Workstreams',
                    '',
                    '### `S0-D4-T4`',
                    '- **Scope:** `S0-D4-T4`',
                    '- **Current Agent:** PM',
                    '- **Current Status:** active',
                    '- **Active Paths:** tools/script/coordination_status.py',
                    '- **Active Subagents:** reporter',
                    '- **Last Heartbeat:** 2099-03-21 11:19 local',
                    '- **Next Expected Heartbeat:** 2099-03-21 11:25 local',
                    '- **Latest Checkpoint:** `docs/coordination/checkpoints/S0-D4-T4-C1.md`',
                    '- **Blockers:** none',
                    '- **Next Recommended Action:** keep working',
                ]
            )
            write_file(repo_root / 'docs' / 'coordination' / 'active.md', active_text)
            write_file(repo_root / 'docs' / 'coordination' / 'tasks' / 'S0-D4-T4.md', '# task\n')
            write_file(
                repo_root / 'docs' / 'coordination' / 'notes' / 'S0-D4-T4-N1.md',
                note_body('S0-D4-T4', stamp='2099-03-21 11:19 local', next_due='2099-03-21 11:25 local'),
            )
            write_file(
                repo_root / 'docs' / 'coordination' / 'notes' / 'S0-D4-T4-N2.md',
                note_body('S0-D4-T4', agent='reporter', stamp='2099-03-21 11:19 local', next_due='2099-03-21 11:25 local'),
            )

            output = io.StringIO()
            with redirect_stdout(output):
                result = COORDINATION_MODULE.verify_coordination(repo_root, scope_override=None, max_gap_minutes=6)

        self.assertEqual(result, 0)
        self.assertIn('PASS: coordination cadence check passed', output.getvalue())

    # Reject partial subagent notes that omit canonical heartbeat fields.
    def test_verify_rejects_partial_subagent_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            active_text = "\n".join(
                [
                    '# 💠 Active Coordination Status',
                    '',
                    '- **Generated At:** 2026-03-21 11:00 local',
                    '- **Updated By:** PM',
                    '- **Active Scope:** `multiple`',
                    '',
                    '## Active Workstreams',
                    '',
                    '### `S0-D4-T4`',
                    '- **Scope:** `S0-D4-T4`',
                    '- **Current Agent:** PM',
                    '- **Current Status:** active',
                    '- **Active Paths:** tools/script/coordination_status.py',
                    '- **Active Subagents:** reporter',
                    '- **Last Heartbeat:** 2099-03-21 11:19 local',
                    '- **Next Expected Heartbeat:** 2099-03-21 11:25 local',
                    '- **Latest Checkpoint:** `docs/coordination/checkpoints/S0-D4-T4-C1.md`',
                    '- **Blockers:** none',
                    '- **Next Recommended Action:** keep working',
                ]
            )
            write_file(repo_root / 'docs' / 'coordination' / 'active.md', active_text)
            write_file(repo_root / 'docs' / 'coordination' / 'tasks' / 'S0-D4-T4.md', '# task\n')
            write_file(
                repo_root / 'docs' / 'coordination' / 'notes' / 'S0-D4-T4-N1.md',
                note_body('S0-D4-T4', stamp='2099-03-21 11:19 local', next_due='2099-03-21 11:25 local'),
            )
            write_file(
                repo_root / 'docs' / 'coordination' / 'notes' / 'S0-D4-T4-N2.md',
                "\n".join(
                    [
                        '# 💠 Heartbeat',
                        '',
                        '- **Coordination File:** `docs/coordination/notes/S0-D4-T4-N2.md`',
                        '- **Scope:** `S0-D4-T4`',
                        '- **Status:** active',
                        '- **Agent:** reporter',
                        '- **Files:** docs/coordination/active.md',
                        '- **Blockers:** none',
                        '- **Next Step:** keep the heartbeat fresh',
                        '- **Time:** 2099-03-21 11:19 local',
                        '- **Current Work:** partial note',
                        '- **Current Paths:** docs/coordination/active.md',
                        '- **Next Check-In Due:** 2099-03-21 11:25 local',
                        '',
                    ]
                ),
            )

            output = io.StringIO()
            with redirect_stdout(output):
                result = COORDINATION_MODULE.verify_coordination(repo_root, scope_override=None, max_gap_minutes=6)

        self.assertEqual(result, 1)
        self.assertIn('missing Chat Summary Sent At for subagent reporter', output.getvalue())

    # Surface overdue reminders per scope in the reminder flow.
    def test_remind_reports_overdue_scope(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            active_text = "\n".join(
                [
                    '# 💠 Active Coordination Status',
                    '',
                    '- **Generated At:** 2026-03-21 11:00 local',
                    '- **Updated By:** PM',
                    '- **Active Scope:** `multiple`',
                    '',
                    '## Active Workstreams',
                    '',
                    '### `S0-D4-T5`',
                    '- **Scope:** `S0-D4-T5`',
                    '- **Current Agent:** PM',
                    '- **Current Status:** active',
                    '- **Active Paths:** .opencode/agents/reporter.md',
                    '- **Active Subagents:** none',
                    '- **Last Heartbeat:** 2000-03-21 11:00 local',
                    '- **Next Expected Heartbeat:** 2000-03-21 11:01 local',
                    '- **Latest Checkpoint:** `docs/coordination/checkpoints/S0-D4-T5-C1.md`',
                    '- **Blockers:** none',
                    '- **Next Recommended Action:** keep working',
                ]
            )
            write_file(repo_root / 'docs' / 'coordination' / 'active.md', active_text)
            (repo_root / 'docs' / 'coordination' / 'notes').mkdir(parents=True, exist_ok=True)

            output = io.StringIO()
            with redirect_stdout(output):
                result = COORDINATION_MODULE.remind_coordination(
                    repo_root,
                    loop=False,
                    interval_seconds=60,
                    warn_before_minutes=1,
                    write_stub=False,
                )

        self.assertEqual(result, 0)
        self.assertIn('OVERDUE: S0-D4-T5 heartbeat due', output.getvalue())

    # Keep the watch command bound to the shared one-minute reminder loop.
    def test_main_watch_routes_to_default_loop(self) -> None:
        with mock.patch.object(COORDINATION_MODULE, 'remind_coordination', return_value=0) as remind_mock:
            with mock.patch.object(sys, 'argv', ['coordination_status.py', 'watch']):
                result = COORDINATION_MODULE.main()

        self.assertEqual(result, 0)
        self.assertEqual(remind_mock.call_count, 1)
        _, kwargs = remind_mock.call_args
        self.assertTrue(kwargs['loop'])
        self.assertEqual(kwargs['interval_seconds'], COORDINATION_MODULE.WATCH_INTERVAL_SECONDS)
        self.assertEqual(kwargs['warn_before_minutes'], COORDINATION_MODULE.WATCH_WARN_BEFORE_MINUTES)
        self.assertTrue(kwargs['write_stub'])

    # Keep the watch loop explicitly local-only.
    def test_watch_rejects_ci_environment(self) -> None:
        with mock.patch.dict('os.environ', {'CI': 'true'}, clear=False):
            output = io.StringIO()
            with redirect_stdout(output):
                result = COORDINATION_MODULE.watch_coordination(Path('/tmp/food-run-test'))

        self.assertEqual(result, 1)
        self.assertIn('watch is local-only', output.getvalue())
