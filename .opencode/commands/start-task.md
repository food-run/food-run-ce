---
description: Start one bounded task and restate exact constraints before work begins
agent: pm
---
# Start Task Command

## TL;DR

This command starts one bounded task. It should restate the exact goal, boundaries, non-goals, and the next expected checkpoint before implementation begins.

## Inputs

- A task identifier or short task scope

## Execution

Task focus:

$ARGUMENTS

Restate:

- Exact objective
- Exact boundaries
- What not to touch
- Active paths
- Protected paths
- ⚠️ Hotspot Files
- Recommended next agent
- Expected checkpoint and commit point
- Expected heartbeat note location in `docs/coordination/notes/`
- Reuse candidates and why any new structure would be meaningfully unique
- Structured 6-minute reporting packet fields for chat and heartbeat notes

Then create or refresh:

- the stable task file in `docs/coordination/tasks/`
- a visible dashboard entry in `docs/coordination/active.md`
- the first expected 6-minute heartbeat target under `docs/coordination/notes/`
- the scoped working branch if it is not already active

Do not start implementation until the `DRYness Gates` section in `.opencode/rules/implementation-standards.md` has a credible pre-implementation answer.
Do not start implementation until `git branch --show-current` matches the intended scoped branch.

## Failure Conditions

- The task is not actually bounded.
- The “what not to touch” boundary is unclear.
- The task cannot start without planning clarification.

## Escalation Rules

Escalate when the task definition is too vague to implement safely.
