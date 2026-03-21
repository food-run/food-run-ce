---
description: Prepare a pull request summary, verification notes, and documentation delta summary
agent: pm
---
# PR Prepare Command

## TL;DR

This command prepares the pull request narrative for the current branch. It should summarize the work clearly, name boundaries, and make verification and docs updates visible to reviewers.

## Inputs

- One or more relevant planning files

## Execution

Planning context:

!`cat $ARGUMENTS`

Current branch and diff:

!`git branch --show-current`
!`git diff -- .`

Prepare:

- TL;DR
- Summary
- Why this change
- Files and boundaries
- Verification
- Docs and ADR delta
- Protected-path notes
- ⚠️ Hotspot-files notes if relevant

Before returning:

- confirm every meaningful change has a completed ADR entry
- confirm the ADR file is ordered newest first
- confirm each ADR entry answers the full nine-question master-packet template
- confirm ops review output exists for implementation-bearing changes before calling the branch PR-ready
- call out any intentionally excluded out-of-scope human edits

## Failure Conditions

- The branch contains mixed workstreams.
- Verification notes are too vague.
- The docs delta is unclear or incomplete.
- ADR entries are missing or incomplete for meaningful changes.

## Escalation Rules

Escalate when the branch should be split or reviewed again before PR preparation.
