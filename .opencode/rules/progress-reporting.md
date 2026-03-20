# Progress Reporting Rule

## TL;DR

Active work must stay visible in two places: `docs/coordination/` and the human chat. PM must ensure every active agent and subagent uses the same structured progress packet at least every 6 minutes while work is active. Current automation verifies the active-scope heartbeat and shared coordination evidence; broader plural-workstream enforcement remains follow-up work. Reporting is non-blocking unless a separate approval gate applies. Coordination filenames must follow `.opencode/rules/coordination-naming.md`.

## Applies To

- PM orchestration
- all subagents
- any active task, deliverable, or sprint workstream

## Required Cadence

- Write a non-blocking heartbeat to `docs/coordination/` at least every 6 minutes while work is active.
- Send the human a running chat progress summary at least every 6 minutes while work is active.
- Send the human another chat progress summary whenever a task, subtask, or subagent run completes.

## Structured Progress Packet

Use the same structure in heartbeat notes and in chat updates:

- scope
- agent or subagent name
- completed work since the last report
- current in-flight work
- blockers or `none`
- next step
- active paths
- next expected update time

Heartbeat notes must also include:

- `Time`
- `Chat Summary Sent At`
- `What Changed Since Last Check-In`
- `Current Work`
- `Current Paths`
- `Next Check-In Due`

Subagent runs may share the parent scope note, but they must identify themselves in the `Agent` field and emit their own structured chat completion update. Until plural-workstream automation lands, PM remains responsible for keeping shared coordination evidence current.

## Coordination Artifacts

- Keep the stable task file in `docs/coordination/tasks/` current.
- Refresh `docs/coordination/active.md` so active work is visible at a glance.
- Add stable, scope-prefixed notes in `docs/coordination/notes/` for heartbeats.
- Add checkpoint notes in `docs/coordination/checkpoints/` after meaningful steps.
- Add handoff notes in `docs/coordination/handoffs/` before switching lanes.

## Chat Update Minimum

Each running progress summary should include:

- scope
- agent or subagent name
- completed work since the last report
- current in-flight work
- blockers or "none"
- next step
- active paths
- next expected update time if work is still active

## Non-Goals

- do not block on routine status updates
- do not wait for the human to ask for progress
- do not rely on chat history alone when `docs/coordination/` should be updated too
