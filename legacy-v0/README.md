# Food Run Legacy v0

## TL;DR

This folder preserves the validated Food Run prototype exactly so the team can reference what was already proven. It is not the active base for the rebuild, and new implementation work must not extend these paths directly.

## What the Prototype Validated

The prototype proved that Food Run could turn recipe discovery and ingredient cleanup into a practical shopping-list workflow. It established the product value of importing recipes, normalizing ingredients, and consolidating purchasing into one grocery trip.

## Why It Was Archived

The prototype was archived because the repo needed a clean rebuild boundary before deeper product, platform, and agent work could continue. Keeping the prototype active-looking at the root would blur ownership and invite new work into paths that were never designed for long-term maintainability.

## What Is Frozen

This archive preserves the original prototype application layout, root runtime files, and generated static output that previously represented the working demo.

## What Still Works as Reference

Use this snapshot to inspect validated user flows, prior parsing logic, data-shape ideas, and the overall product loop that the rebuild must preserve or intentionally improve.

## What Not to Build On

Do not add new features, restructure the rebuild, or treat these files as the active application baseline. The rebuild belongs in the active surfaces documented by `AGENTS.md` and `docs/repo.md`.

## How to Reuse It Safely

Extract ideas deliberately rather than extending the archived files in place. When something from v0 is worth carrying forward, port it into an active rebuild path with current planning, tests, and documentation.
