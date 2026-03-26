"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  shared coordination and repo fixture builders for testkit suites

- Later Extension Points:
    --> Add more reusable fixture builders here when shared suites need richer temp-repo state

- Role:
    --> Owns deterministic fixture strings reused across shared repo-control suites
    --> Keeps coordination packet builders in one place so tests do not fork near-duplicate Markdown fixtures
    --> Must remain fixture-focused instead of becoming a general data-dump module

- Exports:
    --> `make_heartbeat_note`, `make_active_workstream`, `make_active_doc`, and `make_plural_active_doc`

- Consumed By:
    --> shared testkit suites and shared unittest helpers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """

# ---------- heartbeat fixture builders ----------


# Build one canonical heartbeat note fixture.
def make_heartbeat_note(
    scope: str,
    agent: str = 'PM',
    stamp: str = '2026-03-21 11:00 local',
    next_due: str = '2026-03-21 11:06 local',
) -> str:
    return '\n'.join(
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


# ---------- active dashboard fixture builders ----------

# Build one plural-dashboard workstream block.
def make_active_workstream(
    scope: str,
    agent: str = 'PM',
    subagents: str = 'none',
    last_heartbeat: str = '2026-03-21 11:00 local',
    next_heartbeat: str = '2026-03-21 11:06 local',
) -> str:
    return '\n'.join(
        [
            f'### `{scope}`',
            f'- **Scope:** `{scope}`',
            f'- **Current Agent:** {agent}',
            '- **Current Status:** active',
            '- **Active Paths:** tools/scripts/coordination.py',
            f'- **Active Subagents:** {subagents}',
            f'- **Last Heartbeat:** {last_heartbeat}',
            f'- **Next Expected Heartbeat:** {next_heartbeat}',
            '- **Latest Checkpoint:** `docs/coordination/checkpoints/{scope}-C1.md`',
            '- **Blockers:** none',
            '- **Next Recommended Action:** keep working',
        ]
    )


# Build one legacy active dashboard fixture.
def make_active_doc(scope_or_multiple: str = 'S0-D4-T4') -> str:
    parts = [
        '# 💠 Active Coordination Status',
        '',
        '- **Generated At:** 2026-03-21 11:00 local',
        '- **Updated By:** PM',
        f'- **Active Scope:** `{scope_or_multiple}`',
        '- **Current Agent:** PM',
        '- **Current Status:** active',
        '- **Active Paths:** tools/scripts/coordination.py',
        '- **Active Subagents:** none',
        '- **Last Heartbeat:** 2026-03-21 11:00 local',
        '- **Next Expected Heartbeat:** 2026-03-21 11:06 local',
        '- **Latest Checkpoint:** `docs/coordination/checkpoints/{scope_or_multiple}-C1.md`',
        '- **Blockers:** none',
        '- **Next Recommended Action:** keep working',
    ]
    return '\n'.join(parts)


# Build one plural active dashboard fixture.
def make_plural_active_doc(workstreams: list[str]) -> str:
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
    for workstream in workstreams:
        parts.append(make_active_workstream(workstream))
        parts.append('')
    return '\n'.join(parts)
