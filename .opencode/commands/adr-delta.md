---
description: Draft the reasoning or ADR delta for the current change
agent: librarian
subtask: true
---
# ADR Delta Command

## TL;DR

This command drafts the reasoning delta for the current work. It should explain what changed, why it was chosen, what it owns, and what breaks if it changes.

## Inputs

- One or more relevant planning files

## Execution

Planning context:

!`cat $ARGUMENTS`

Current diff:

!`git diff -- .`

Draft:

- What changed
- Why it was chosen
- What it owns
- What breaks if it changes
- Why it matters technically
- Why it matters non-technically

## Failure Conditions

- The reasoning is still unclear.
- The diff is too broad to summarize honestly.
- The change does not yet have stable enough understanding for durable docs.

## Escalation Rules

Escalate when the implementation needs one more review pass before durable reasoning is written.
