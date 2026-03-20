---
description: Close out a task, deliverable, or sprint by updating stable coordination state, unresolved items, and the next recommended scope
agent: pm
---
# Close Scope Command

## TL;DR

This command closes a scope cleanly. It updates the stable coordination file, records what is done, records what remains unresolved, and names the next recommended scope.

## Inputs

- `$1` = scope ID

## Scope

Close scope: `$1`

## Required Skills

Load:

- `scope-router`
- `coordination-state`
- `drift-check`

## Execution

Do all of the following:

1. Load the stable coordination file for the scope.
2. Determine whether the scope is:
   - complete
   - blocked
   - review-rejected
   - waiting for human approval
3. Update the coordination file with:
   - final status
   - completed child scopes
   - unresolved issues
   - next recommended scope
4. Run a repo-wide DRYness review for the affected concept areas before calling the scope complete.
5. Record:
   - what was reused
   - what was created
   - what was refactored
   - what should be consolidated elsewhere outside scope
6. Refresh `docs/coordination/active.md` so closed scopes disappear from the active dashboard and blocked scopes remain visible.
7. If durable docs changed, call out the docs delta.
8. If the scope is complete, mark it complete explicitly and stop.
9. If the scope is blocked, state the blocker explicitly and stop.

## Stable Coordination Rule

Always write to the stable scope file:

- `docs/coordination/tasks/Sx.md`
- `docs/coordination/tasks/Sx-Dy.md`
- `docs/coordination/tasks/Sx-Dy-Tz.md`

For ad hoc work, also use:

- `docs/coordination/tasks/X-slug.md`
- `docs/coordination/tasks/X-slug-Tn.md`

If scoped artifacts exist but the stable scope file does not, fold the valid current state into the stable scope file first.

## Stop Conditions

Stop if:

- the scope cannot be closed honestly because review or integration is incomplete
- the current coordination state is conflicting or stale
- the next scope is outside the requested parent scope
- a human decision is required before closure

## Output Contract

Return:

- Scope
- Final status
- Stable coordination file updated
- DRYness review status
- What was completed
- What was reused, created, refactored, and deferred for later consolidation
- What remains unresolved
- Next recommended scope
- Human decisions needed
