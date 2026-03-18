---
description: Create a bounded work plan with files, lanes, risks, and verification
agent: planner
subtask: true
---
# Plan Work Command

## TL;DR

This command converts the current planning input into a bounded work packet. It should define exact file touch points, ownership, sequencing, risk, and verification without drifting into implementation.

## Inputs

- One or more relevant planning files

## Execution

Read the current planning files:

!`cat $ARGUMENTS`

Produce:

- Task breakdown
- Exact file touch list
- Owner and reviewer suggestions
- Async-safe split
- ⚠️ Hotspot Files
- Review hotspots
- Verification checklist

## Failure Conditions

- The work cannot be decomposed cleanly.
- The same concept has multiple plausible homes.
- The plan would force unnecessary merge conflicts.

## Escalation Rules

Escalate when safe decomposition requires changing the deliverable scope or when protected paths are unavoidable.
