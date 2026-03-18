---
name: active-vs-legacy
description: Enforce the rebuild boundary between legacy-v0 reference material and active v1 work
---
# Active vs Legacy

## TL;DR

This skill preserves the rebuild boundary. It keeps `legacy-v0/` as read-most reference material and prevents accidental extension of archived prototype paths.

## What I Do

- Mark `legacy-v0/` as reference-only
- Block accidental implementation in archived paths
- Suggest safe extraction instead of in-place hardening
- Help keep the active rebuild narrative honest

## When to Use Me

Use this skill whenever a request references old prototype code or paths.
