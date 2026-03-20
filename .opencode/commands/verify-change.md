

---
description: Review the current diff against the plan, boundaries, and repo standards
agent: reviewer
subtask: true
---
# Verify Change Command

## TL;DR

This command reviews the current diff against the active planning packet, repo standards, and repo-wide DRYness expectations. It should approve or reject with concrete reasons, not vague impressions.

## Inputs

- One or more relevant planning files

## Execution

Current plan:

!`cat $ARGUMENTS`

Current diff:

!`git diff -- .`

Review for:

- Planning alignment
- Boundary accuracy
- Drift
- Duplication
- Explainability
- Hidden rollback risk
- Protected-path handling
- ⚠️ Hotspot-files handling
- Meaningful uniqueness versus existing repo concepts
- Script TL;DR and section-comment compliance for script-like entry files and automation runners
- Consolidation that should happen now versus later

Return approve or reject with exact reasons, plus:

- what was reused
- what was created
- what was refactored
- what should be consolidated elsewhere outside scope

## Failure Conditions

- The diff and planning packet tell different stories.
- The patch introduces a second home for an existing concept.
- The patch is not meaningfully unique and should have reused or refactored instead.
- Protected or hotspot surfaces changed without appropriate care.

## Escalation Rules

Escalate when rejection implies a planning correction, not just a code correction. Ignore pre-existing or human-made out-of-scope surfaces unless the current diff broadens into them.
