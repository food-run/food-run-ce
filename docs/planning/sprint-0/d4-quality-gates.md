# 🌟 S0-D4 — 🐙 CI/CD + 🛡️ Quality Gates

## TL;DR

S0-D4 turns process agreements into enforced repo behavior. It creates the first merge-blocking automation for docs parity, protected paths, review discipline, and release scaffolding so later sprint speed comes from trustworthy automation rather than reviewer guesswork.

## Table of Contents

- [Why this deliverable exists](#why-this-deliverable-exists)
- [👥 Ownership](#ownership)
- [🌿 Branch](#branch)
- [🏷️ Deliverable PR title](#deliverable-pr-title)
- [🎯 Purpose](#purpose)
- [⛓️ Depends on](#depends-on)
- [🚧 Blocks](#blocks)
- [📂 Files touched](#files-touched)
- [🧠 Recommended names](#recommended-names)
- [🧾 Exact TL;DR sections per new or refactored file](#exact-tldr-sections-per-new-or-refactored-file)
- [⚠️ Hotspot files](#hotspot-files)
- [🎟️ Task tickets](#task-tickets)
- [👾 Verification tickets](#verification-tickets)
- [✅ Deliverable verification](#deliverable-verification)
- [🚨 Bad agent output patterns to watch for](#bad-agent-output-patterns-to-watch-for)
- [🧩 Rationale in one sentence](#rationale-in-one-sentence)

---

## Why this deliverable exists

After D3, the repo knows:

- which lanes exist
- which paths are protected
- which docs matter
- which review questions block merge

But none of that matters unless the repo can enforce it.

D4 establishes the first automation spine for:

- PR shape enforcement
- repo verification
- docs parity checks
- protected-path escalation
- release-safety scaffolding

---

## 👥 Ownership

**Owner:** 👤🛡️ Platform/QA  
**Reviewer:** 👤🎯 Team Lead  
**Required consult:** 👤🧰 BE/API, 👤👻 AI/Cloud

---

## 🌿 Branch

` s0/d4-quality-gates `

---

## 🏷️ Deliverable PR title

`ci(repo): enforce protected-path review docs consistency and merge readiness before changes reach main`

---

## 🎯 Purpose

Create the first permanent enforcement layer so later implementation work must satisfy:

- review completeness
- docs/ADR completeness
- protected-path discipline
- verification discipline
- release-safety scaffolding

before it can be merged.

---

## ⛓️ Depends on

- 🌟 S0-D1 — 🧼 Repo Reset + 🧊 Legacy Freeze
- 🌟 S0-D2 — 🧱 Active Tree + 🔌 Shared Seams
- 🌟 S0-D3 — 🐝 Agent Steering + 📚 Docs Spine

---

## 🚧 Blocks

- 🌟 S0-D5 — 🐳 Docker + ☸️ k3s + 🔍 Observability Baseline
- all later feature sprints
- any meaningful protected-path implementation, because the approval and docs gates must exist first

---

## 📂 Files touched

### Workflow and control surfaces to extend or create

- `.github/pull_request_template.md`
- `.github/workflows/repo-verify.yml`
- `.github/workflows/cd.yml`
- `.github/workflows/cla-check.yml`
- `.github/workflows/docs-guard.yml`
- `.github/workflows/protected-paths.yml`

### Permanent script entry points

- `tools/scripts/verify.py`
- `tools/scripts/coordination_status.py`
- `tools/scripts/release.py`

### Repo-control and coordination extensions

- `.opencode/agents/reporter.md`
- `.opencode/commands/start-task.md`
- `.opencode/commands/sync-status.md`
- `docs/templates/coordination/active-template.md`

### Meaningfully refactored docs

- `docs/testing.md`
- `docs/operations.md`
- `README.md`

---

## 🧠 Recommended names

### Workflow names

- `repo verify`
- `cla phrase check`
- `docs guard`
- `protected paths`

### Current committed workflow files

- `.github/workflows/repo-verify.yml`
- `.github/workflows/cd.yml`
- `.github/workflows/cla-check.yml`
- `.github/workflows/docs-guard.yml`
- `.github/workflows/protected-paths.yml`

### Job names

- `verify_repo`
- `verify_docs`
- `verify_paths`
- `verify_pr`
- `prepare_release`
- `check_cla`

### Script names

- `verify.py`
- `release.py`

---

## 🧾 Exact TL;DR sections per new or refactored file

D4 should apply the exact Sprint 0 TL;DR content to:

- `.github/pull_request_template.md`
- `.github/workflows/repo-verify.yml`
- `.github/workflows/cd.yml`
- `.github/workflows/cla-check.yml`
- `.github/workflows/docs-guard.yml`
- `.github/workflows/protected-paths.yml`
- `tools/scripts/verify.py`
- `tools/scripts/release.py`

`docs/testing.md` should gain:

- `## Merge Gates`
- `## Docs and ADR Verification`
- `## Protected-Path Verification`
- `## Future CI Extensions`

`docs/operations.md` should gain:

- `## CI as Operational Control`
- `## Release Marker Discipline`
- `## Rollback-Aware Delivery`
- `## Protected-Path Escalation`

`README.md` should add:

- `## Merge Discipline`
- `## Protected Paths`
- `## CI and Docs Expectations`

---

## ⚠️ Hotspot files

These files define how unsafe or under-documented work gets stopped:

- `.github/pull_request_template.md`
- `.github/workflows/repo-verify.yml`
- `.github/workflows/docs-guard.yml`
- `.github/workflows/protected-paths.yml`
- `tools/scripts/verify.py`
- `tools/scripts/release.py`

---

## 🎟️ Task tickets

### 🎟️ S0-D4-T1 — 🧾 Define the PR contract and merge checklist

**Commit title:**  
`docs(pr): define a pull request contract that forces scope clarity verification notes and docs accountability`

Task focus:

- align `.github/pull_request_template.md` and `.opencode/commands/pr-prepare.md`
- update `CLA.md` and `CONTRIBUTING.md` so the exact confirmation phrase and repository-owner exception are canonical before workflow automation depends on them
- refine this deliverable packet to the current committed workflow filenames before protected workflow edits begin

### 🎟️ S0-D4-T2 — 🧪 Seed the CI verification workflow and repo verification script

**Commit title:**  
`ci(verify): add the first merge-blocking verification workflow and central repo verification entrypoint`

### 🎟️ S0-D4-T3 — 📚 Add docs and protected-path enforcement workflows

**Commit title:**  
`ci(paths): enforce docs parity and escalate risky path changes before they can merge silently`

### 🎟️ S0-D4-T4 — 💠 Support plural active workstreams and verify per-scope coordination evidence

**Commit title:**  
`feat(coordination): support plural active workstreams and verify per-scope reporting evidence with legacy fallback`

Task focus:

- extend `tools/scripts/coordination_status.py` instead of creating a second coordination runtime
- keep `docs/coordination/active.md` backward-compatible while adding plural active-workstream parsing
- add tests for plural-scope parsing, overdue detection, latest-note selection, and per-subagent reporting evidence before any reporter path becomes mandatory

### 🎟️ S0-D4-T5 — 📣 Add the reporter agent contract and scheduled reminder escalation

**Commit title:**  
`chore(opencode): add reporter guidance and scheduled local reminders for overdue coordination scopes`

Task focus:

- add a dedicated `reporter` agent contract whose only job is emitting and normalizing the structured packet used by PM and subagents
- align `.opencode/commands/start-task.md`, `.opencode/commands/sync-status.md`, templates, and coordination rules to the same packet shape
- add local scheduled execution guidance or a lightweight runner so `tools/scripts/coordination_status.py remind` can run every minute and escalate overdue scopes without pretending CI owns local coordination state

### 🎟️ S0-D4-T6 — 🚢 Seed release scaffolding and align testing/operations docs

**Commit title:**  
`ci(release): seed release-readiness scaffolding and document how CI/CD acts as an operational control layer`

---

## 👾 Verification tickets

### 👾 S0-D4-T1-V — 🧠 Verify merge gates reflect the repo’s real review standards

**Commit title:**  
`test(ci): verify the pull request contract and workflow checks match the repo’s documented merge standards`

### 👾 S0-D4-T2-V — 🔍 Verify failure output is actionable instead of noisy

**Commit title:**  
`test(verify): verify workflow and script failures explain what is missing and where the contributor must fix it`

### 👾 S0-D4-T4-V — ⏱️ Verify plural workstream parsing and overdue coordination evidence

**Commit title:**  
`test(coordination): verify plural workstream parsing overdue detection and subagent reporting evidence`

---

## ✅ Deliverable verification

S0-D4 is done only when:

- the PR template forces bounded summary, verification notes, docs/ADR context, and protected-path acknowledgement
- `.github/workflows/repo-verify.yml` and `tools/scripts/verify.py` exist
- docs and protected-path enforcement workflows exist and align with D3 rules
- `tools/scripts/coordination_status.py` supports plural active workstreams with per-scope freshness checks and tests before any reporter path becomes mandatory
- a dedicated `reporter` agent contract and local scheduled reminder path exist without overstating CI or deployment maturity
- a release-preparation workflow plus `tools/scripts/release.py` exist as scaffolds without overclaiming D5 deployment maturity
- automation and documentation tell the same story

---

## 🚨 Bad agent output patterns to watch for

Reject immediately if an agent tries to:

- pack all repo policy into YAML instead of keeping stable logic in scripts and docs
- make CI check only syntax/build status while skipping docs and protected-path concerns
- create vague failure messages like “validation failed”
- redefine protected-path categories differently from D3
- split coordination reporting across multiple runtimes instead of extending `tools/scripts/coordination_status.py`
- make the reporter agent mandatory before tests prove the per-scope evidence model
- commit machine-specific scheduler artifacts instead of a lightweight repo-owned runner or documented local scheduler path
- oversell `cd.yml` as a complete deployment pipeline before D5 exists
- leave `.github/pull_request_template.md` and `.opencode/commands/pr-prepare.md` describing different reviewer contracts
- make CLA automation stricter than the canonical `CLA.md` wording for owner-authored PRs
- turn the PR template into a generic checklist that ignores repo-specific cognitive-debt concerns

---

## 🧩 Rationale in one sentence

S0-D4 is successful when unsafe, under-documented, or high-blast-radius changes fail early and clearly, so later sprint speed comes from trustworthy automation instead of reviewer guesswork.
