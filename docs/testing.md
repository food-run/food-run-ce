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
- repo verification already runs through `python3 tools/scripts/verify.py`
- `.github/workflows/repo-verify.yml` already enforces that verifier in CI
- `python3 tools/scripts/coordination.py watch` now provides the local-only minute-level reminder loop without expanding the CI verifier contract
- later deliverables should extend this file with deeper runtime, contract, and smoke-specific commands as those layers become real

## Merge Gates

- `tools/scripts/verify.py` is the central repo verification entrypoint for local and CI-safe checks
- `.github/workflows/repo-verify.yml` should stay a thin wrapper that sets up Python, installs Bun, and calls `python3 tools/scripts/verify.py --ci`
- later D4 release scaffolding should stay beside these workflows instead of duplicating their checks in YAML

## Docs and ADR Verification

- `.github/workflows/docs-guard.yml` now treats `Summary`, `Why this change`, `Files and boundaries`, and `Verification` as merge-blocking PR narrative sections for every PR
- `.github/workflows/docs-guard.yml` also checks governed changes for a real `Docs and ADR delta` plus an updated `docs/adr.md`
- meaningful repo-control and shared-understanding changes should keep `docs/adr.md` current before merge-ready status

## Protected-Path Verification

- `.github/workflows/protected-paths.yml` now requires explicit PR acknowledgement when protected paths change, including any `.github/workflows/**` edit and the exact protected-path categories from `AGENTS.md`
- `.github/workflows/cla-check.yml` now skips the CLA phrase gate for repository-owner-authored PRs while keeping the exact phrase requirement for outside contributors
- `shared/testkit/coordination.py` covers coordination parser and reminder-loop behavior for the shared runtime in `tools/scripts/coordination.py`
- `shared/testkit/release.py`, `shared/testkit/verify.py`, and `shared/testkit/workflows.py` keep the governed workflow and script contracts bound to the central script seams without a `tools/testing/` shadow home

## Current Verifier Scope

- Python script syntax across active rebuild script surfaces
- governed TL;DR header and section-comment checks for script files
- shared repo-control suites loaded from explicit `shared.testkit.*` modules instead of `test_*.py` filename discovery
- repo-verification workflow contract checks so CI keeps delegating to the central verifier
- coordination cadence checks outside CI, with an explicit CI-safe skip for local-only coordination artifacts
- reviewer-frontend build verification in `tools/scripts/frontend.py` that checks the GitHub Pages base path and SPA fallback artifact contract

## Release Scaffolding

- `.github/workflows/cd.yml` is now a manual release-preparation workflow, not a deploy pipeline
- `tools/scripts/release.py` owns D4 release-readiness messaging and rejects deploy or publish claims until D5 lands

## Future CI Extensions

- keep release-readiness scaffolding separate from repo verification so rollout logic stays reviewable
