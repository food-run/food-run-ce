---
description: Summarize live coordination state across tasks, handoffs, notes, and checkpoints
agent: pm
---
# Sync Status Command

## TL;DR

This command summarizes the current live coordination state. It should make the active scope or active workstreams, blockers, stale notes, and the next recommended action visible at a glance, and refresh the human-visible coordination dashboard.

## Inputs

- None required

## Execution

Read the latest live coordination files and summarize:

!`find docs/coordination -type f | sort | tail -50`

Then refresh `docs/coordination/active.md` with:

- the active scope when only one scope is live, or the active workstream list when several scopes are live
- the latest heartbeat time for each live scope
- whether each current workstream is stale after more than 6 minutes without a heartbeat
- the next recommended action for each live scope

And satisfy `.opencode/rules/coordination-standards.md` with a chat update that includes:

- scope
- agent or subagent name
- completed tasks since the last report
- current in-flight work
- blockers
- active paths
- next expected update time

Return:

- Active scope or workstreams
- Latest checkpoint
- Open blockers
- Coordination gaps in the active scope or workstreams
- Recommended next action

## Failure Conditions

- Coordination files are too stale to trust.
- Work is active but not tracked.
- The repo state and coordination state disagree materially.

## Escalation Rules

Escalate when coordination drift is blocking safe routing.
