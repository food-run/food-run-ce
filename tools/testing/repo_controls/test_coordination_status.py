#!/usr/bin/env python3
"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  focused unit coverage for coordination status parsing and reminder behavior

- Later Extension Points:
    --> Add more fixture helpers here when later coordination packets grow new stable fields

- Role:
    --> Verifies legacy and plural active dashboard parsing without creating a second test harness
    --> Keeps freshness and reminder behavior covered near the shared coordination runtime
    --> Must stay close to `tools/scripts/coordination_status.py` so policy drift remains obvious

- Exports:
    --> `CoordinationStatusTests` unittest coverage for `tools/scripts/coordination_status.py`

- Consumed By:
    --> `python3 -m unittest discover -s tools/testing -p 'test_*.py'`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
from __future__ import annotations

# ---------- imports and dependencies ----------

import io
import sys
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

from shared.testkit import TestCase, load_script, make_active_doc, make_heartbeat_note, write_file

# ---------- module loading ----------

COORDINATION_MODULE = load_script('coordination_status')

# ---------- coordination runtime tests ----------


class CoordinationStatusTests(TestCase):
    def test_parses_legacy_active_scope_as_one_workstream(self) -> None:
        workstreams = COORDINATION_MODULE.parse_active_workstreams(make_active_doc('S0-D4-T4'))
        self.assertEqual(len(workstreams), 1)
        self.assertEqual(COORDINATION_MODULE.parse_scope(workstreams[0]['Scope']), 'S0-D4-T4')

    def test_rejects_ambiguous_mixed_active_shapes(self) -> None:
        active_text = '\n'.join([
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
        ])

        with self.assertRaises(ValueError):
            COORDINATION_MODULE.parse_active_workstreams(active_text)

    def test_latest_note_ignores_drafts(self) -> None:
        notes_dir = self.repo_root / 'docs' / 'coordination' / 'notes'
        write_file(notes_dir / 'S0-D4-T4-N1.md', make_heartbeat_note('S0-D4-T4'))
        write_file(notes_dir / 'S0-D4-T4-N2.draft.md', make_heartbeat_note('S0-D4-T4'))

        latest = COORDINATION_MODULE.latest_note(notes_dir, 'S0-D4-T4')
        self.assertIsNotNone(latest)
        self.assertEqual(latest.name, 'S0-D4-T4-N1.md')

    def test_verify_reports_missing_heartbeat_note(self) -> None:
        self.write_active_doc(make_active_doc('S0-D4-T4'))
        self.write_task_doc('S0-D4-T4')

        output = io.StringIO()
        with redirect_stdout(output):
            result = COORDINATION_MODULE.verify_coordination(self.repo_root, scope_override=None, max_gap_minutes=6)

        self.assertEqual(result, 1)
        self.assertIn('missing heartbeat note for active scope S0-D4-T4', output.getvalue())

    def test_watch_rejects_ci_environment(self) -> None:
        with mock.patch.dict('os.environ', {'CI': 'true'}, clear=False):
            output = io.StringIO()
            with redirect_stdout(output):
                result = COORDINATION_MODULE.watch_coordination(Path('/tmp/food-run-test'))

        self.assertEqual(result, 1)
        self.assertIn('watch is local-only', output.getvalue())

    def test_main_watch_routes_to_default_loop(self) -> None:
        with mock.patch.object(COORDINATION_MODULE, 'remind_coordination', return_value=0) as remind_mock:
            with mock.patch.object(sys, 'argv', ['coordination_status.py', 'watch']):
                result = COORDINATION_MODULE.main()

        self.assertEqual(result, 0)
        _, kwargs = remind_mock.call_args
        self.assertTrue(kwargs['loop'])
        self.assertEqual(kwargs['interval_seconds'], COORDINATION_MODULE.WATCH_INTERVAL_SECONDS)
        self.assertEqual(kwargs['warn_before_minutes'], COORDINATION_MODULE.WATCH_WARN_BEFORE_MINUTES)
        self.assertTrue(kwargs['write_stub'])
