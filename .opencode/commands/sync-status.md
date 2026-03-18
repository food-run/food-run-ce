---
description: Summarize live coordination state across tasks, handoffs, notes, and checkpoints
agent: pm
---
# Sync Status Command

## TL;DR

This command summarizes the current live coordination state. It should make active workstreams, blockers, stale notes, and the next recommended action visible at a glance.

## Inputs

- None required

## Execution

Read the latest live coordination files and summarize:

!`find docs/coordination -type f | sort | tail -50`

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
