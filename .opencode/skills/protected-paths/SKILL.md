---
name: protected-paths
description: Classify high-blast-radius paths and decide when to escalate instead of editing
---
# Protected Paths

## TL;DR

This skill helps determine whether a path should be treated as protected. It supports deny-or-escalate behavior for high-blast-radius work and keeps the human-only zones from the master packet explicit.

## What I Do

- Identify protected paths
- Recommend deny-or-escalate behavior
- Explain why a path is risky
- Distinguish protected paths from ⚠️ Hotspot Files when both are relevant
- Map risky work back to the human-only zones in the master packet

## When to Use Me

Use this skill before editing auth, migrations, repo-control files, release workflows, or other high-risk surfaces.
