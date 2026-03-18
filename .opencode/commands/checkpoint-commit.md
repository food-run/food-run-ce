---
description: Prepare a Conventional Commit from the current checkpoint without pushing
agent: developer
---
# Checkpoint Commit Command

## TL;DR

This command evaluates the current diff for checkpoint readiness. It should propose a Conventional Commit, summarize the checkpoint, and stop before pushing.

## Inputs

- None required

## Execution

Current diff:

!`git diff -- .`

Create:

- A recommended Conventional Commit subject
- An optional commit body
- A short checkpoint summary for `docs/coordination/checkpoints/`
- If the diff is coherent, ask for approval to run `git add` and `git commit`

## Failure Conditions

- The diff is not coherent enough for a useful rollback point.
- The checkpoint mixes unrelated changes.
- Coordination notes are not current enough to support the commit.

## Escalation Rules

Escalate when the right answer is to split the diff before committing.
