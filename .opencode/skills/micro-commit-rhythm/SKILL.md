---
name: micro-commit-rhythm
description: Decide when a change is stable enough for a Conventional Commit checkpoint
---
# Micro-Commit Rhythm

## TL;DR

This skill helps identify useful rollback points and stable commit boundaries. It reduces giant end-of-task commits and improves recoverability.

## What I Do

- Identify useful rollback points
- Draft Conventional Commit messages
- Choose commit scopes using the first qualifying parent surface that preserves enough context for review and history, and fall back to `repo` only when needed
- Recommend splitting a broad diff into smaller checkpoint commits when that avoids an unnecessary `repo` scope
- Discourage giant “everything at once” commits
- Keep checkpoint notes aligned with commit boundaries

## When to Use Me

Use this skill when deciding whether the current diff is ready for a checkpoint commit.
