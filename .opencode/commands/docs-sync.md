---
description: Align README, docs, AGENTS, and process files with the current implementation state
agent: librarian
subtask: true
---
# Docs Sync Command

## TL;DR

This command checks whether durable docs and repo-control docs still match the current implementation state. It should identify what must change now, what should wait, and where terminology drift exists.

## Inputs

- One or more relevant planning files

## Execution

Planning context:

!`cat $ARGUMENTS`

Check:

- `README.md`
- `docs/**`
- `AGENTS.md`
- `.opencode/**`

Report:

- What must change now
- What should wait
- Any terminology drift
- Any false maturity claims
- Any ⚠️ hotspot-file wording concerns

## Failure Conditions

- Docs and implementation materially disagree.
- Terminology drift creates behavior ambiguity.
- The requested docs update would overstate repo maturity.

## Escalation Rules

Escalate when wording changes would affect repo-wide behavior or merge standards.
