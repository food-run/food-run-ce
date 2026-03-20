---
name: drift-check
description: Detect mismatch between planning docs, AGENTS, repo layout, and actual changes
---
# Drift Check

## TL;DR

This skill compares the current diff and docs against the planning story and `.opencode/rules/master-packet-alignment.md`. It catches terminology drift, structural drift, and false maturity before they spread.

## What I Do

- Compare code, docs, and planning consistency
- Catch terminology drift
- Catch “future state described as current state”
- Flag mismatch between repo-control docs and implementation
- Flag places where repo-control behavior drifted away from master-packet non-negotiables

## When to Use Me

Use this skill before review, docs updates, or PR preparation.
