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

## Micro-Commit Rhythm

When executing tasks within a deliverable or task scope:

- create one small, focused commit per file or logical group of files
- keep commits narrow enough to be meaningful rollback points
- use Conventional Commit format with clear English subjects (12-22 words)
- prefer multiple micro-commits over one large checkpoint that mixes unrelated changes
- record commit hashes in the coordination file after each task completes

Example for a deliverable with 4 tasks:

```
T1: 3 micro-commits (one per Dockerfile)
T2: 3 micro-commits (one per manifest file or logical group)
T3: 5 micro-commits (one per runtime file)
T4: 4 micro-commits (edge configs, docs, script)
```

The coordination file should track:
- commit count per task
- commit hash range for each task
- total micro-commits for the deliverable

## Commit Scope Formatting

When writing Conventional Commits, use the first qualifying parent folder as the scope. The scope should be specific enough to identify the affected area but not so granular that it obscures the bigger picture.

### Scope Rules

- **Format:** `type(scope): message` where scope is the first qualifying parent folder
- **Type:** Use standard types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `deploy`, etc.
- **Scope selection:** Choose the first parent folder that provides meaningful context

### Scope Examples

| Change | Correct Scope | Reason |
|--------|---------------|--------|
| Changes to `apps/web/package.json` | `apps-web` | First parent folder `apps` is too broad; `apps/web` is specific |
| Changes to `.github/workflows/cd.yml` | `github` | First parent folder is `.github` |
| Changes to `docs/adr.md` | `docs` | First parent folder is `docs` |
| Changes to `shared/contract/http.py` | `shared` | First parent folder is `shared` |
| Changes to multiple files in `apps/web/src/` | `apps-web` | Still use `apps-web` as the parent |
| Changes spanning `apps/web/` and `.github/` | `repo` | No common parent; use `repo` |

### Multi-Folder Changes

If a change touches files from multiple different parent folders without a clear common ancestor, use `repo` as the scope. Examples include root-level changes, cross-cutting refactors, or coordinated updates to multiple distinct areas.

### Docs Exception

For documentation changes, always use `docs` as the scope regardless of the folder, as per convention.

### Anti-Patterns to Avoid

- Using leaf folders (e.g., `apps-web-src`) instead of parent folders
- Using overly broad scopes like `apps` when the change is specific to `apps/web`
- Using variable names or function names in commit messages
- Creating scopes that don't map to actual folder names in the repo

## Non-Goals

- do not block on routine status updates
- do not wait for the human to ask for progress
- do not rely on chat history alone when `docs/coordination/` should be updated too
