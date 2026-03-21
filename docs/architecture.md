# Architecture

## TL;DR

This file is the durable architecture map for the active rebuild. It should explain the major runtime surfaces, boundaries, and cross-surface responsibilities as they become real in the repo.

## Scope

- active rebuild surfaces only
- cross-runtime structure and responsibility boundaries
- architecture posture that matches the repo and planning packet

## Expected Growth Areas

- experience, product, event, agent, and operations surfaces
- active tree boundaries under `apps/`, `shared/`, `platform/`, and `tools/`
- long-lived ownership decisions that later implementation should extend

## Current Status

- Sprint 0 has seeded the active tree under `apps/` and `shared/`
- later deliverables should extend this file instead of introducing separate architecture side notes
