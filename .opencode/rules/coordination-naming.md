# Coordination Naming Rule

## TL;DR

Coordination filenames must be scope-based and stable. Dates may appear inside file contents, but not as the primary identifier in filenames.

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
