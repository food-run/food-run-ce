---
name: review-rubric
description: Review changes for planning alignment, boundary accuracy, DRYness, explainability, and rollback safety
---
# Review Rubric

## TL;DR

This skill runs the repo’s review standard consistently. It helps catch plausible-but-dangerous output before it becomes mergeable and enforces the `DRYness Gates` section in `.opencode/rules/implementation-standards.md` during closeout.

## What I Do

- Run the repo review questions consistently
- Catch drift, duplication, and boundary collapse
- Check whether new structure is meaningfully unique or should be refactored
- Return approve or reject with concrete reasons
- Highlight protected-path and ⚠️ Hotspot-File concerns
- Check whether covered script files use the required structured TL;DR and section-group comments
- Ignore pre-existing or human-made out-of-scope surfaces unless the current diff broadens into them

## When to Use Me

Use this skill during review, verification, before asking for a checkpoint commit, and before PM calls a goal complete.
