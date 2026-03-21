# Testing

## TL;DR

This file is the durable testing and verification guide for the rebuild. It should explain how unit, integration, contract, smoke, and agent-output checks work as the system grows.

## Scope

- verification posture across runtime surfaces
- required test layers and when they apply
- how review, smoke checks, and quality gates fit together

## Expected Test Layers

- unit tests
- integration tests
- contract tests
- smoke validation
- agent-output verification

## Current Status

- Sprint 0 has established shared test support in `shared/testkit/`
- repo verification already runs through `python3 tools/script/verify.py`
- `.github/workflows/repo-verify.yml` already enforces that verifier in CI
- later deliverables should extend this file with deeper runtime, contract, and smoke-specific commands as those layers become real
