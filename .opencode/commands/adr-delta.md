---
description: Draft the reasoning or ADR delta for the current change
agent: librarian
subtask: true
---
# ADR Delta Command

## TL;DR

This command drafts the reasoning delta for the current work. It should answer the full master-packet ADR questions, stay sorted recency first, and be complete before PRs or merge commits are prepared.

## Inputs

- One or more relevant planning files

## Execution

Planning context:

!`cat $ARGUMENTS`

Current diff:

!`git diff -- .`

Draft:

- What was built
- Why it was chosen
- What boundaries it owns
- What breaks if it changes
- Known edge cases or failure modes
- Why this work matters
- What capability it unlocks
- Why the chosen design is safer or more scalable
- What trade-off the team accepted

Also ensure:

- the entry is inserted in recency-first order
- the slice is as small as current understanding allows without creating duplicate ADR noise
- if a deliverable touches multiple distinct surfaces, split into separate ADR entries (e.g., D5 touching Dockerfiles, k8s manifests, health endpoints, and docs should become 4-6 separate entries, not one monolithic entry)
- out-of-scope human edits are planned separately unless the human explicitly includes them

## Failure Conditions

- The reasoning is still unclear.
- The diff is too broad to summarize honestly.
- The change does not yet have stable enough understanding for durable docs.

## Escalation Rules

Escalate when the implementation needs one more review pass before durable reasoning is written.
