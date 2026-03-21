# Coordination Standards

## TL;DR

Coordination work must use stable scope-based filenames and a visible structured reporting cadence. Keep active work visible in `docs/coordination/` and in chat, use the canonical artifact names for every scope, and refresh the shared progress packet at least every 6 minutes while work is active.

## Applies To

- PM orchestration
- all subagents
- any active task, deliverable, sprint, or ad hoc workstream

## Scope IDs

Use one of these scope forms:

- sprint: `S<number>`
- deliverable: `S<number>-D<number>`
- task: `S<number>-D<number>-T<number>`
- ad hoc workstream: `X-<slug>`
- ad hoc child task: `X-<slug>-T<number>`

`<slug>` must be a short, stable kebab-case identifier for the workstream, such as `repo-control`, `auth-audit`, or `parser-spike`.

## Canonical Filenames

Use these exact patterns:

- stable task packet: `docs/coordination/tasks/<scope>.md`
- heartbeat note: `docs/coordination/notes/<scope>-N<number>.md`
- checkpoint note: `docs/coordination/checkpoints/<scope>-C<number>.md`
- handoff note: `docs/coordination/handoffs/<scope>-H<number>.md`
- active dashboard: `docs/coordination/active.md`

Examples:

- `docs/coordination/tasks/S0-D1.md`
- `docs/coordination/tasks/X-repo-control.md`
- `docs/coordination/notes/S0-D1-N1.md`
- `docs/coordination/checkpoints/X-repo-control-C1.md`
- `docs/coordination/handoffs/X-repo-control-H1.md`

## Naming Rules

- prefer the stable task packet first
- increment `N`, `C`, and `H` within the same scope instead of creating date-based filenames
- use dates and times inside the file body when needed
- do not create timestamp-only coordination filenames
- do not rename an active scope unless the scope itself changed materially

## Lookup Rules

When resuming work for a scope, look in this order:

1. exact stable task packet
2. parent stable task packet
3. newest matching scoped artifact with the same `<scope>` prefix
4. create the stable task packet if none exist

## Required Cadence

- write a non-blocking heartbeat to `docs/coordination/` at least every 6 minutes while work is active
- send the human a running chat progress summary at least every 6 minutes while work is active
- send the human another chat progress summary whenever a task, subtask, or subagent run completes

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

When PM routes reporting work to `reporter`, that lane must emit the exact same packet shape instead of inventing a parallel format.

Heartbeat notes must also include:

- `Time`
- `Chat Summary Sent At`
- `What Changed Since Last Check-In`
- `Current Work`
- `Current Paths`
- `Next Check-In Due`

Subagent runs may share the parent scope note, but they must identify themselves in the `Agent` field and emit their own structured chat completion update. PM remains responsible for keeping shared coordination evidence current, including plural active-workstream dashboards when more than one scope is live.

## Coordination Artifacts

- keep the stable task file in `docs/coordination/tasks/` current
- refresh `docs/coordination/active.md` so active work is visible at a glance
- add stable, scope-prefixed notes in `docs/coordination/notes/` for heartbeats
- add checkpoint notes in `docs/coordination/checkpoints/` after meaningful steps
- add handoff notes in `docs/coordination/handoffs/` before switching lanes

When more than one scope is active, `docs/coordination/active.md` may use an `## Active Workstreams` section with one `###` block per live scope. Each block must include:

- `Scope`
- `Current Agent`
- `Current Status`
- `Active Paths`
- `Active Subagents`
- `Last Heartbeat`
- `Next Expected Heartbeat`
- `Latest Checkpoint`
- `Blockers`
- `Next Recommended Action`

Use a comma-separated list or `none` for `Active Subagents`.

The legacy single-scope top-level `Active Scope` shape remains valid when only one scope is active.

## Chat Update Minimum

Each running progress summary should include:

- scope
- agent or subagent name
- completed work since the last report
- current in-flight work
- blockers or `none`
- next step
- active paths
- next expected update time if work is still active

## Non-Goals

- do not block on routine status updates
- do not wait for the human to ask for progress
- do not rely on chat history alone when `docs/coordination/` should be updated too
