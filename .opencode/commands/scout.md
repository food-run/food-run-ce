---
description: Perform grounded repo discovery against the current planning files
agent: scout
subtask: true
---
# Scout Command

## TL;DR

This command grounds the repo against the current planning packet. It should inspect the current codebase and docs, then return reuse opportunities, inconsistencies, and risk notes with exact path references.

## Inputs

- One or more relevant planning files

## Execution

Use these planning sources:

!`cat $ARGUMENTS`

Ground the repo and report:

- Relevant paths
- Reuse candidates
- ⚠️ Hotspot Files
- Planning inconsistencies
- Risk notes
- Questions that require human clarification

## Failure Conditions

- The repo state cannot be reconciled with the planning files.
- A path is both archived and active-looking.
- The requested work implies unapproved protected-path edits.

## Escalation Rules

Escalate when planning and repo reality diverge or when discovery reveals a protected-path dependency.
