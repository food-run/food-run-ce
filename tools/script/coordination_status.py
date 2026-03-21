#!/usr/bin/env python3
"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  coordination cadence verifier and heartbeat reminder runtime

- Later Extension Points:
    --> Add plural active-workstream parsing and per-subagent evidence checks

- Role:
    --> Verifies that the active coordination scope stays fresh in `docs/coordination/`
    --> Generates structured reminder output and draft heartbeat notes before cadence slips
    --> Exists as the single script surface for coordination-status automation in the rebuild
    --> Must remain a thin repo-control runner, not a hidden orchestration layer

- Exports:
    --> `verify` and `remind` command-line entrypoints

- Consumed By:
    --> PM and local operators running coordination checks and reminder commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
from __future__ import annotations

# ---------- imports and dependencies ----------

import argparse
import re
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

# ---------- runtime identity ----------

# Keep all coordination timestamps in one readable format.
TIME_FORMAT = '%Y-%m-%d %H:%M local'
# Parse bold dashboard fields from coordination Markdown.
FIELD_RE = re.compile(r'^- \*\*(.+?):\*\*\s*(.*)$')
# Extract scope IDs from inline code fences.
SCOPE_RE = re.compile(r'`([^`]+)`')
# Match official heartbeat note names by suffix.
OFFICIAL_NOTE_RE = re.compile(r'.+-N(\d+)$')
# Keep the default reporting cadence centralized here.
DEFAULT_MAX_GAP_MINUTES = 6
# Require these structured fields in heartbeat notes.
REQUIRED_HEARTBEAT_FIELDS = (
    'Time',
    'Chat Summary Sent At',
    'What Changed Since Last Check-In',
    'Current Work',
    'Current Paths',
    'Next Check-In Due',
)

# ---------- parsing helpers ----------

# Read simple bullet fields from a coordination file.
def parse_fields(path: Path) -> dict[str, str]:
    # Build a flat field map for later checks.
    fields: dict[str, str] = {}
    # Walk every line in the coordination file.
    for line in path.read_text(encoding='utf-8').splitlines():
        # Match the standard bold bullet format.
        match = FIELD_RE.match(line.strip())
        # Skip lines that are not structured fields.
        if match:
            fields[match.group(1).strip()] = match.group(2).strip()
    # Return the parsed field mapping.
    return fields


# Normalize a scope value into its raw scope ID.
def parse_scope(raw: str) -> str:
    # Prefer the inline-code scope token when present.
    match = SCOPE_RE.search(raw)
    # Fall back to the stripped raw value.
    return match.group(1) if match else raw.strip()


# Parse one coordination timestamp with a helpful label.
def parse_time(raw: str, label: str) -> datetime:
    # Strip whitespace and inline code markers first.
    value = raw.strip().strip('`')
    # Reject empty timestamps with a direct label.
    if not value:
        raise ValueError(f'missing {label}')
    # Parse the canonical coordination time format.
    return datetime.strptime(value, TIME_FORMAT)


# Render timestamps back into the canonical format.
def format_time(value: datetime) -> str:
    # Keep every generated timestamp consistent.
    return value.strftime(TIME_FORMAT)


# Extract the numeric suffix from an official note path.
def note_index(path: Path) -> int:
    # Match only official scope note filenames.
    match = OFFICIAL_NOTE_RE.fullmatch(path.stem)
    # Return a sentinel for non-matching drafts.
    if not match:
        return -1
    # Convert the note suffix into an integer.
    return int(match.group(1))


# Pick the latest official note for one scope.
def latest_note(notes_dir: Path, scope: str) -> Path | None:
    # Keep only official scope notes for this scope.
    candidates = [path for path in notes_dir.glob(f'{scope}-N*.md') if note_index(path) >= 0]
    # Return the newest official note when present.
    return max(candidates, key=note_index) if candidates else None


# Choose the next official note number for one scope.
def next_official_note_number(notes_dir: Path, scope: str) -> int:
    # Read every existing note index for this scope.
    existing = [note_index(path) for path in notes_dir.glob(f'{scope}-N*.md')]
    # Discard drafts and malformed note names.
    official = [index for index in existing if index >= 0]
    # Start at one when no official note exists.
    return (max(official) + 1) if official else 1

# ---------- reminder payloads ----------

# Build the next heartbeat draft body for operators.
def heartbeat_stub(draft_path: Path, scope: str, agent: str, action: str, due_time: datetime) -> str:
    # Schedule the following heartbeat from the current due time.
    next_due = due_time + timedelta(minutes=DEFAULT_MAX_GAP_MINUTES)
    # Keep the draft fields aligned with coordination standards.
    body = [
        '# 💠 Heartbeat Draft',
        '',
        f'- **Coordination File:** `{draft_path}`',
        f'- **Scope:** `{scope}`',
        '- **Status:** draft',
        f"- **Agent:** {agent or 'PM'}",
        '- **Files:** fill exact touched files before sending',
        '- **Blockers:** none',
        f"- **Next Step:** {action or 'send the structured chat update and finalize this heartbeat'}",
        '- **Time:** fill at send time',
        '- **Chat Summary Sent At:** fill when the chat update is sent',
        '- **What Changed Since Last Check-In:** fill before sending',
        '- **Current Work:** fill the in-flight work before sending',
        '- **Current Paths:** fill active paths before sending',
        f'- **Next Check-In Due:** {format_time(next_due)}',
        '',
    ]
    # Return the draft as one Markdown string.
    return '\n'.join(body)


# Print the matching chat summary template for humans.
def print_chat_template(scope: str, agent: str, action: str, due_time: datetime) -> None:
    # Schedule the next chat update from this due time.
    next_due = due_time + timedelta(minutes=DEFAULT_MAX_GAP_MINUTES)
    # Keep the chat template field order canonical.
    print('CHAT UPDATE TEMPLATE')
    print(f'- Scope: {scope}')
    print(f"- Agent: {agent or 'PM'}")
    print('- Completed since last report: fill before sending')
    print('- Current in-flight work: fill before sending')
    print('- Blockers: none')
    print(f"- Next step: {action or 'send the next structured heartbeat'}")
    print('- Active paths: fill before sending')
    print(f'- Next expected update: {format_time(next_due)}')

# ---------- verification checks ----------

# Verify that active coordination evidence stays fresh.
def verify_coordination(repo_root: Path, scope_override: str | None, max_gap_minutes: int) -> int:
    # Resolve the coordination surface paths once.
    coordination_dir = repo_root / 'docs' / 'coordination'
    active_path = coordination_dir / 'active.md'
    notes_dir = coordination_dir / 'notes'
    tasks_dir = coordination_dir / 'tasks'
    # Convert the allowed gap into a timedelta.
    max_gap = timedelta(minutes=max_gap_minutes)
    # Compare evidence against the current local time.
    now = datetime.now()

    # Fail immediately when the dashboard is missing.
    if not active_path.exists():
        print('FAIL: missing docs/coordination/active.md')
        return 1

    # Parse the active dashboard into a field map.
    active_fields = parse_fields(active_path)
    # Allow callers to override the active scope explicitly.
    active_scope_raw = scope_override or active_fields.get('Active Scope', '')
    # Normalize the scope into its raw ID.
    active_scope = parse_scope(active_scope_raw)

    # Treat an empty dashboard scope as idle.
    if not active_scope or active_scope.lower() == 'none':
        print('PASS: no active scope listed in docs/coordination/active.md')
        return 0

    # Collect every coordination problem before failing.
    problems: list[str] = []
    # Track the parsed dashboard heartbeat time for alignment.
    active_last_dt: datetime | None = None

    # The stable task packet remains the resume anchor.
    task_path = tasks_dir / f'{active_scope}.md'
    # Flag missing stable packets as coordination drift.
    if not task_path.exists():
        problems.append(f'missing stable task file: {task_path.relative_to(repo_root)}')

    try:
        # Parse the dashboard heartbeat timestamp first.
        active_last_dt = parse_time(active_fields.get('Last Heartbeat', ''), 'Last Heartbeat')
        # Flag stale dashboard evidence beyond the allowed gap.
        if now - active_last_dt > max_gap:
            problems.append(f'active dashboard heartbeat is older than {max_gap_minutes} minutes')
    except ValueError as exc:
        # Surface parsing failures with the original label.
        problems.append(str(exc))

    try:
        # Parse the dashboard due time next.
        active_next_dt = parse_time(active_fields.get('Next Expected Heartbeat', ''), 'Next Expected Heartbeat')
        # Flag overdue dashboards before reading notes.
        if active_next_dt < now:
            problems.append('next expected heartbeat is already overdue')
    except ValueError as exc:
        # Surface parsing failures with the original label.
        problems.append(str(exc))

    # Load the latest official note for the active scope.
    note_path = latest_note(notes_dir, active_scope)
    # Require at least one official heartbeat note.
    if note_path is None:
        problems.append(f'missing heartbeat note for active scope {active_scope}')
    else:
        # Parse the latest note into flat fields.
        note_fields = parse_fields(note_path)
        # Require every canonical heartbeat field.
        for field in REQUIRED_HEARTBEAT_FIELDS:
            if not note_fields.get(field, '').strip():
                problems.append(f'{note_path.relative_to(repo_root)}: missing {field}')
        try:
            # Parse the note timestamp for freshness checks.
            note_time = parse_time(note_fields.get('Time', ''), 'Heartbeat Time')
            # Flag stale note evidence beyond the allowed gap.
            if now - note_time > max_gap:
                problems.append(
                    f'latest heartbeat note is older than {max_gap_minutes} minutes: {note_path.relative_to(repo_root)}'
                )
            # Keep dashboard and note heartbeat times aligned.
            if active_last_dt is not None and abs(active_last_dt - note_time) > max_gap:
                problems.append('active dashboard last heartbeat does not align with latest heartbeat note')
        except ValueError as exc:
            # Surface note time parsing failures clearly.
            problems.append(f'{note_path.relative_to(repo_root)}: {exc}')

        try:
            # Parse the chat summary timestamp too.
            chat_time = parse_time(note_fields.get('Chat Summary Sent At', ''), 'Chat Summary Sent At')
            # Flag stale chat evidence beyond the allowed gap.
            if now - chat_time > max_gap:
                problems.append(
                    f'chat summary evidence is older than {max_gap_minutes} minutes: {note_path.relative_to(repo_root)}'
                )
        except ValueError as exc:
            # Surface chat time parsing failures clearly.
            problems.append(f'{note_path.relative_to(repo_root)}: {exc}')

        try:
            # Parse the next due time from the note.
            next_due = parse_time(note_fields.get('Next Check-In Due', ''), 'Next Check-In Due')
            # Flag overdue note schedules explicitly.
            if next_due < now:
                problems.append(f'heartbeat note is overdue: {note_path.relative_to(repo_root)}')
        except ValueError as exc:
            # Surface next due parsing failures clearly.
            problems.append(f'{note_path.relative_to(repo_root)}: {exc}')

    # Print every problem together for one repair pass.
    if problems:
        print('FAIL: coordination cadence check failed')
        for problem in problems:
            print(f'- {problem}')
        return 1

    # Confirm the active coordination evidence is healthy.
    print('PASS: coordination cadence check passed')
    print(f'- scope: {active_scope}')
    print(f'- active dashboard: {active_path.relative_to(repo_root)}')
    if note_path is not None:
        print(f'- latest heartbeat: {note_path.relative_to(repo_root)}')
    return 0

# ---------- reminder flow ----------

# Warn when the next coordination heartbeat is due.
def remind_coordination(
    repo_root: Path,
    loop: bool,
    interval_seconds: int,
    warn_before_minutes: int,
    write_stub: bool,
) -> int:
    # Resolve the live dashboard and notes folder once.
    active_path = repo_root / 'docs' / 'coordination' / 'active.md'
    notes_dir = repo_root / 'docs' / 'coordination' / 'notes'
    # Convert the warning threshold into a timedelta.
    warn_before = timedelta(minutes=warn_before_minutes)

    # Keep looping only when the caller requested it.
    while True:
        try:
            # Return idle when the dashboard is missing locally.
            if not active_path.exists():
                print('IDLE: docs/coordination/active.md not found')
                return 0

            # Parse the active dashboard fields again each cycle.
            active_fields = parse_fields(active_path)
            # Resolve the active scope from the dashboard.
            scope = parse_scope(active_fields.get('Active Scope', ''))
            # Return idle when no active scope is listed.
            if not scope or scope.lower() == 'none':
                print('IDLE: no active scope')
                return 0

            # Parse the next dashboard heartbeat deadline.
            due_time = parse_time(active_fields.get('Next Expected Heartbeat', ''), 'Next Expected Heartbeat')
            # Compare the due time against the current clock.
            now = datetime.now()
            remaining = due_time - now
            # Reuse dashboard ownership fields in reminder output.
            agent = active_fields.get('Current Agent', 'PM')
            action = active_fields.get('Next Recommended Action', 'send the next heartbeat')

            # Print a calm status while the deadline is still distant.
            if remaining > warn_before:
                minutes = int(remaining.total_seconds() // 60)
                seconds = int(remaining.total_seconds() % 60)
                print(f'OK: {scope} heartbeat due in {minutes}m {seconds}s')
            else:
                # Choose the next official note number before drafting.
                next_number = next_official_note_number(notes_dir, scope)
                # Keep reminder drafts separate from official notes.
                draft_path = notes_dir / f'{scope}-N{next_number}.draft.md'
                # Optionally write the draft note once.
                if write_stub and not draft_path.exists():
                    draft_path.write_text(
                        heartbeat_stub(draft_path, scope, agent, action, due_time),
                        encoding='utf-8',
                    )
                    print(f'STUB: created {draft_path.relative_to(repo_root)}')

                # Distinguish early warnings from overdue reminders.
                status = 'DUE' if remaining.total_seconds() <= 0 else 'WARN'
                # Use a human-friendly remaining-time string.
                if remaining.total_seconds() <= 0:
                    remaining_text = 'now'
                else:
                    minutes = int(remaining.total_seconds() // 60)
                    seconds = int(remaining.total_seconds() % 60)
                    remaining_text = f'in {minutes}m {seconds}s'

                # Print the warning summary and next artifacts.
                print(f'{status}: {scope} heartbeat due {remaining_text}')
                print('- active dashboard: docs/coordination/active.md')
                print(f'- draft heartbeat: {draft_path.relative_to(repo_root)}')
                print_chat_template(scope, agent, action, due_time)
                print('- finalize the next official heartbeat note after sending the chat update')

        except ValueError as exc:
            # Surface timestamp parsing failures immediately.
            print(f'FAIL: {exc}')
            return 1

        # Exit after one pass unless loop mode is active.
        if not loop:
            return 0
        # Sleep between reminder cycles in loop mode.
        time.sleep(interval_seconds)

# ---------- command-line bootstrap ----------

# Build the bounded CLI parser for verification and reminders.
def build_parser() -> argparse.ArgumentParser:
    # Keep the root parser description short and direct.
    parser = argparse.ArgumentParser(
        description='Verify coordination cadence and generate structured reminder output.'
    )
    # Split the CLI into explicit subcommands.
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Configure the verification subcommand flags.
    verify_parser = subparsers.add_parser('verify', help='Verify coordination heartbeat freshness.')
    verify_parser.add_argument('--scope', help='Override active scope from docs/coordination/active.md')
    verify_parser.add_argument(
        '--max-gap-minutes',
        type=int,
        default=DEFAULT_MAX_GAP_MINUTES,
        help='Maximum allowed gap between structured progress reports.',
    )

    # Configure the reminder subcommand flags.
    remind_parser = subparsers.add_parser('remind', help='Warn when the next heartbeat is due.')
    remind_parser.add_argument('--loop', action='store_true', help='Keep checking on an interval.')
    remind_parser.add_argument(
        '--interval-seconds',
        type=int,
        default=60,
        help='Loop interval in seconds.',
    )
    remind_parser.add_argument(
        '--warn-before-minutes',
        type=int,
        default=1,
        help='Warn this many minutes before the heartbeat is due.',
    )
    remind_parser.add_argument(
        '--write-stub',
        action='store_true',
        help='Create the next heartbeat draft when warning or overdue.',
    )
    # Return the fully configured parser.
    return parser


# Parse the CLI and run the chosen coordination action.
def main() -> int:
    # Build the bounded parser first.
    parser = build_parser()
    # Parse the current command-line arguments.
    args = parser.parse_args()
    # Resolve the repository root from this script path.
    repo_root = Path(__file__).resolve().parents[2]

    # Route verify requests into the verifier flow.
    if args.command == 'verify':
        return verify_coordination(repo_root, scope_override=args.scope, max_gap_minutes=args.max_gap_minutes)
    # Route remind requests into the reminder flow.
    if args.command == 'remind':
        return remind_coordination(
            repo_root,
            loop=args.loop,
            interval_seconds=args.interval_seconds,
            warn_before_minutes=args.warn_before_minutes,
            write_stub=args.write_stub,
        )
    # Keep unsupported commands impossible in normal use.
    parser.error(f'unsupported command: {args.command}')
    return 2


# Keep the module executable as a direct script.
if __name__ == '__main__':
    # Exit with the selected coordination status code.
    sys.exit(main())
