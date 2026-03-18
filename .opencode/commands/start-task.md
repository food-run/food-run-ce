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

## Failure Conditions

- The task is not actually bounded.
- The “what not to touch” boundary is unclear.
- The task cannot start without planning clarification.

## Escalation Rules

Escalate when the task definition is too vague to implement safely.
