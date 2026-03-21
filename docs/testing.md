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

- Sprint 0 has established the need for shared test support in `shared/testkit/`
- later deliverables should extend this file as concrete test commands and gates appear
