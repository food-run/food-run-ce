---
description: Summarize live coordination state across tasks, handoffs, notes, and checkpoints
agent: pm
---
# Sync Status Command

## TL;DR

This command summarizes the current live coordination state. It should make active workstreams, blockers, stale notes, and the next recommended action visible at a glance, and refresh the human-visible coordination dashboard.

## Inputs

- None required

## Execution

Read the latest live coordination files and summarize:

!`find docs/coordination -type f | sort | tail -50`

Then refresh `docs/coordination/active.md` with:

- active scopes
- latest heartbeat time per active scope
- stale workstreams with no heartbeat for more than 8 minutes
- next recommended action

And satisfy `.opencode/rules/progress-reporting.md` with a chat update that includes:

- completed tasks since the last report
- current in-flight work
- blockers
- next expected update time

Return:

- Active workstreams
- Latest checkpoints
- Open blockers
- Stale tasks
- Missing handoffs
- Recommended next action

## Failure Conditions

- Coordination files are too stale to trust.
- Work is active but not tracked.
- The repo state and coordination state disagree materially.

## Escalation Rules

Escalate when coordination drift is blocking safe routing.
