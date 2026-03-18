---
description: Split work into async-safe lanes with minimal merge conflicts
agent: planner
subtask: true
---
# Split Work Command

## TL;DR

This command divides the current work into parallel lanes. It should reduce overlap, preserve path ownership, and make handoff points explicit.

## Inputs

- One or more relevant planning files

## Execution

Use this planning input:

!`cat $ARGUMENTS`

Split the work into parallel lanes.

For each lane include:

- Scope
- Touched paths
- Merge-conflict risk
- Dependency order
- Handoff points
- Review hotspots

## Failure Conditions

- The work cannot be split without high path overlap.
- Parallel lanes would collide on protected paths or hotspot files.
- The requested split would create coordination debt instead of speed.

## Escalation Rules

Escalate when the correct answer is sequencing, not parallelism.
