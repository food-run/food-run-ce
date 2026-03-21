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

## Merge Gates

- `tools/script/verify.py` is the central repo verification entrypoint for local and CI-safe checks
- `.github/workflows/repo-verify.yml` should stay a thin wrapper that sets up Python and calls `python3 tools/script/verify.py --ci`
- later D4 workflows should add docs parity, protected-path, and release scaffolding beside the central verifier instead of duplicating its checks in YAML

## Current Verifier Scope

- Python script syntax across active rebuild script surfaces
- governed TL;DR header and section-comment checks for script files
- repo-verification workflow contract checks so CI keeps delegating to the central verifier
- coordination cadence checks outside CI, with an explicit CI-safe skip for local-only coordination artifacts

## Future CI Extensions

- add docs and ADR parity checks in a dedicated docs-guard workflow
- add protected-path escalation checks in a dedicated protected-paths workflow
- keep release-readiness scaffolding separate from repo verification so rollout logic stays reviewable
