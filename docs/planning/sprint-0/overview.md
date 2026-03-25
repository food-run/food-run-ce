# 📅 Sprint 0 — 🧼 Repo Reset, 🧱 Foundations, 🛠️ Tooling Baseline, 🐝 Agent Steering, 🧬 LangGraph/LangSmith Spine, 🔍 Observability, 🐙 CI/CD, 📚 Docs Skeleton

**Subtitle:** Freeze the validated prototype, stand up the governed rebuild spine, and make the repo safe for parallel human + agent execution.

## TL;DR

Sprint 0 exists to prevent the rebuild from inheriting prototype coupling, agent drift, and undocumented decisions. Its real output is controlled surface area: one active tree, one preserved legacy tree, one documented ruleset for humans and agents, and one enforced path for reviews, ADR updates, and release safety.

## Table of Contents

- [Why this sprint comes first](#why-this-sprint-comes-first)
- [🎯 Goal](#goal)
- [🪢 Async structure](#async-structure)
- [🌲 Final active tree](#final-active-tree)
- [⚠️ Hotspot files](#hotspot-files)
- [✅ Exit criteria](#exit-criteria)
- [Deliverables](#deliverables)
  - [🌟 S0-D1 — 🧼 Repo Reset + 🧊 Legacy Freeze](#s0-d1-repo-reset-legacy-freeze)
  - [🌟 S0-D2 — 🧱 Active Tree + 🔌 Shared Seams](#s0-d2-active-tree-shared-seams)
  - [🌟 S0-D3 — 🐝 Agent Steering + 📚 Docs Spine](#s0-d3-agent-steering-docs-spine)
  - [🌟 S0-D4 — 🐙 CI/CD + 🛡️ Quality Gates](#s0-d4-ci-cd-quality-gates)
  - [🌟 S0-D5 — 🐳 Docker + ☸️ k3s + 🔍 Observability Baseline](#s0-d5-docker-k3s-observability-baseline)

---

## Why this sprint comes first

Sprint 0 exists to prevent the rebuild from inheriting prototype coupling, agent drift, and undocumented decisions.

The real output of this sprint is not features. It is **controlled surface area**:

- one active tree
- one preserved legacy tree
- one documented ruleset for humans and agents
- one enforced path for reviews, ADR updates, and release safety

If Sprint 0 is weak, every later sprint compounds cognitive debt. If Sprint 0 is strong, later feature sprints can move in parallel without the repo turning into a pile of plausible-but-incompatible patches.

---

## 🎯 Goal

Establish a funding-grade baseline where the team can safely build in parallel across product, event, agent, and operations concerns without mutating the legacy prototype or weakening review quality.

Sprint 0 must leave the repo in a state where:

- the old prototype is preserved as `legacy-v0/`
- the active v1 tree is the only authoritative build path
- OpenCode lane behavior is explicit and permissioned
- docs and ADRs are part of the merge path
- CI/CD, local parity, and observability baselines exist early enough to shape every later sprint

---

## 🪢 Async Structure

### Primary dependency chain

1. **🌟 S0-D1 — 🧼 Repo Reset + 🧊 Legacy Freeze**
   - preserve the validated prototype under `legacy-v0/`
   - remove ambiguity about which paths are active
   - unblock all later work by creating one authoritative root layout
2. **🌟 S0-D2 — 🧱 Active Tree + 🔌 Shared Seams**
   - seed `apps/`, `shared/`, `platform/`, `tools/`, and `docs/`
   - define the permanent homes for contracts, adapters, and test support
   - unblock parallel lane work without path collisions
3. **🌟 S0-D3 — 🐝 Agent Steering + 📚 Docs Spine**
   - define lane rules, protected paths, approval gates, and artifact expectations
   - seed `AGENTS.md`, `opencode.json`, `.opencode/`, and `/docs`
   - unblock safe multi-agent parallelism and ADR-coupled delivery
4. **🌟 S0-D4 — 🐙 CI/CD + 🛡️ Quality Gates**
   - enforce merge safety, docs safety, and approval safety
   - make broken conventions and missing ADR work fail before merge
   - unblock trustworthy parallel contributions
5. **🌟 S0-D5 — 🐳 Docker + ☸️ k3s + 🔍 Observability Baseline**
   - stand up local parity, health/readiness, request IDs, and release markers
   - create the first operational control loop
   - unblock later feature work from drifting away from real deploy and debug conditions

### Parallelism after the chain opens up

Once **S0-D2** lands, the sprint should branch into controlled async lanes:

- **lane A — repo + docs control**
  - `AGENTS.md`
  - `opencode.json`
  - `.opencode/`
  - `/docs`
  - PR template + docs guardrails
- **lane B — app skeletons**
  - `apps/web`
  - `apps/api`
  - `apps/domain`
  - `apps/worker`
  - `apps/agent`
- **lane C — shared seams**
  - `shared/contract`
  - `shared/schema`
  - `shared/adapter`
  - `shared/testkit`
- **lane D — platform spine**
  - `platform/docker`
  - `platform/k8s`
  - `platform/edge`
  - `platform/infra`
- **lane E — tooling + verification**
  - `tools/script`
  - `tools/load`
  - `tools/eval`
  - `tools/chaos`
  - `.github/workflows`

### Owner map

- **👤🎯 Team Lead**
  - owns boundary enforcement
  - reviews `AGENTS.md`, `docs/adr.md`, path sensitivity rules, and Sprint 0 exit criteria
  - approves any ambiguity around active vs. legacy paths
- **👤🎨 FE/Data**
  - owns `apps/web`
  - co-owns `shared/contract`
  - reviews client cache, route structure, and generated-client landing-zone choices
- **👤🧰 BE/API**
  - owns `apps/api` and `apps/domain`
  - co-owns `shared/schema` and `shared/adapter`
  - reviews contract/domain separation and request/write safety seams
- **👤👻 AI/Cloud**
  - owns `apps/agent`
  - co-owns `.opencode/`, `docs/agent.md`, `tools/eval`, and `platform/infra`
  - reviews LangGraph/LangSmith spine placement and artifact/eval storage posture
- **👤🛡️ Platform/QA**
  - owns `.github/workflows`, `platform/docker`, `platform/k8s`, `tools/chaos`, and observability bootstrap files
  - reviews parity, rollout safety, and verification hooks

### Dependency notes

- **S0-D1 blocks everything**
- **S0-D2 blocks meaningful async work**
- **S0-D3 and S0-D4 can run in parallel after S0-D2**
- **S0-D5 should begin after S0-D2, but should not be considered done until S0-D4 gates exist**
- **no later sprint should start until Sprint 0 exit criteria are fully green**

---

## 🌲 Final Active Tree

This is the expected active tree at the end of Sprint 0, with permanent starter files only.

```text
food-run-ce/
├── AGENTS.md
├── README.md
├── CONTRIBUTING.md
├── CLA.md
├── GOVERNANCE.md
├── TRADEMARKS.md
├── LICENSE.md
├── .env.example
├── .gitignore
├── bunfig.toml
├── bun.lock
├── pyproject.toml
├── uv.lock
├── ruff.toml
├── biome.jsonc
├── opencode.json
├── .github/
│   ├── pull_request_template.md
│   └── workflows/
│       ├── ci.yml
│       ├── cd.yml
│       ├── cla_check.yml
│       ├── docs_guard.yml
│       └── protected_paths.yml
├── .opencode/
│   ├── agents/
│   │   ├── pm.md
│   │   ├── scout.md
│   │   ├── planner.md
│   │   ├── architect.md
│   │   ├── developer.md
│   │   ├── designer.md
│   │   ├── reviewer.md
│   │   ├── integrator.md
│   │   ├── ops.md
│   │   └── librarian.md
│   ├── commands/
│   ├── rules/
│   └── skills/
├── apps/
│   ├── web/
│   │   ├── angular.json
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   └── src/
│   │       ├── main.ts
│   │       └── app/
│   ├── api/
│   │   ├── main.py
│   │   ├── routes.py
│   │   ├── middleware.py
│   │   └── schemas.py
│   ├── domain/
│   │   ├── manage.py
│   │   ├── config.py
│   │   ├── models.py
│   │   ├── services.py
│   │   ├── auth.py
│   │   └── migrate/
│   ├── worker/
│   │   ├── main.py
│   │   ├── jobs.py
│   │   ├── queue.py
│   │   └── retry.py
│   └── agent/
│       ├── main.py
│       ├── graph.py
│       ├── evals.py
│       └── store.py
├── shared/
│   ├── contract/
│   │   ├── http.py
│   │   ├── errors.py
│   │   └── version.py
│   ├── schema/
│   │   ├── common.py
│   │   ├── events.py
│   │   └── auth.py
│   ├── adapter/
│   │   ├── ports.py
│   │   ├── factory.py
│   │   ├── cache.py
│   │   ├── queue.py
│   │   └── store.py
│   └── testkit/
│       ├── fixtures.py
│       ├── factory.py
│       └── helpers.py
├── platform/
│   ├── docker/
│   │   ├── web.Dockerfile
│   │   ├── api.Dockerfile
│   │   ├── worker.Dockerfile
│   │   └── agent.Dockerfile
│   ├── k8s/
│   │   ├── web.yaml
│   │   ├── api.yaml
│   │   ├── worker.yaml
│   │   ├── agent.yaml
│   │   └── migrate.yaml
│   ├── edge/
│   │   ├── cache.yaml
│   │   ├── gateway.yaml
│   │   └── limits.yaml
│   └── infra/
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
├── tools/
│   ├── chaos/
│   │   ├── drills.md
│   │   └── checks.py
│   ├── eval/
│   │   ├── cases.py
│   │   └── runner.py
│   ├── load/
│   │   ├── ingest.py
│   │   └── browse.py
│   └── script/
│       ├── dev.py
│       ├── verify.py
│       └── release.py
├── docs/
│   ├── adr.md
│   ├── architecture.md
│   ├── repo.md
│   ├── web.md
│   ├── api.md
│   ├── domain.md
│   ├── worker.md
│   ├── agent.md
│   ├── data.md
│   ├── cache.md
│   ├── edge.md
│   ├── observability.md
│   ├── resilience.md
│   ├── operations.md
│   ├── testing.md
│   └── legacy-v0.md
└── legacy-v0/
    ├── README.md
    ├── client/
    ├── server/
    └── docs/
```

### Tree intent

- `legacy-v0/` preserves the validated prototype
- `apps/` holds deployable units
- `shared/` holds seam-level common contracts and adapters
- `platform/` holds deploy and runtime topology
- `.opencode/` holds agent operating rules, not product docs
- `/docs` holds deep technical docs only

---

## ⚠️ Hotspot files

Sprint 0 hotspot files are the control surfaces that can multiply drift if they are vague, inconsistent, or prematurely overbuilt:

- `AGENTS.md`
- `opencode.json`
- `docs/repo.md`
- `docs/adr.md`
- `.github/pull_request_template.md`
- `.github/workflows/ci.yml`
- `.github/workflows/docs_guard.yml`
- `.github/workflows/protected_paths.yml`
- `apps/api/main.py`
- `shared/adapter/ports.py`

These files need especially careful review because mistakes in them propagate across the entire rebuild.

---

## ✅ Exit Criteria

- **Repo boundary reset is complete**
  - the validated prototype is preserved without remaining ambiguous
  - `legacy-v0/` contains the old `client/`, `server/`, and supporting docs
  - the root README and repo docs explicitly state that `legacy-v0/` is preserved reference material, not the active v1 build path
- **Human + agent governance is active before feature work begins**
  - the lane model is explicit
  - protected-path behavior is enforceable
- **Docs and review discipline are part of the merge path**
  - `/docs/adr.md`, `/docs/architecture.md`, `/docs/repo.md`, and the plane/domain docs exist as permanent technical targets
  - reviewers have a defined checklist for reuse, conventions, dead code, suppressed errors, and “what breaks if this changes”
- **Tooling, parity, and release safety are bootstrapped**
  - Dockerfiles and k3s manifests exist for the initial deployable units and migration flow
  - CI/CD workflows exist for validation, docs safety, protected-path safety, and release scaffolding
  - request IDs, release markers, and the first telemetry conventions are seeded in the active tree

---

## Deliverables

### 🌟 S0-D1 — 🧼 Repo Reset + 🧊 Legacy Freeze

Purpose: freeze the prototype as historical proof, make the active rebuild path unambiguous, and rewrite the repo narrative so humans and agents stop treating the prototype layout as the base to harden.

Primary outputs:

- `legacy-v0/`
- `legacy-v0/README.md`
- `docs/legacy-v0.md`
- `docs/repo.md`
- refactored `README.md`

See: [`d1-repo-reset.md`](./d1-repo-reset.md)

### 🌟 S0-D2 — 🧱 Active Tree + 🔌 Shared Seams

Purpose: create the first permanent active tree so later work has one clear place to land and one shared language for contracts, schemas, adapters, and test support.

Primary outputs:

- `apps/`
- `shared/`
- starter files with permanent TL;DR blocks and section maps
- README updates for active rebuild paths

See: [`d2-active-tree.md`](./d2-active-tree.md)

### 🌟 S0-D3 — 🐝 Agent Steering + 📚 Docs Spine

Purpose: create the operating theory for the repo before parallel work accelerates.

Primary outputs:

- `AGENTS.md`
- `opencode.json`
- `.opencode/agents/`
- `.opencode/commands/`
- `.opencode/rules/`
- `.opencode/skills/`
- `docs/adr.md`
- `docs/architecture.md`
- `docs/agent.md`
- `docs/testing.md`
- `docs/operations.md`

See: [`d3-agent-docs.md`](./d3-agent-docs.md)

### 🌟 S0-D4 — 🐙 CI/CD + 🛡️ Quality Gates

Purpose: turn process agreements into merge-blocking automation that catches drift before it lands on `main`.

Primary outputs:

- `.github/pull_request_template.md`
- `.github/workflows/repo-verify.yml`
- `.github/workflows/cd.yml`
- `.github/workflows/cla-check.yml`
- `.github/workflows/docs-guard.yml`
- `.github/workflows/protected-paths.yml`
- `tools/scripts/verify.py`
- `tools/scripts/release.py`

See: [`d4-quality-gates.md`](./d4-quality-gates.md)

### 🌟 S0-D5 — 🐳 Docker + ☸️ k3s + 🔍 Observability Baseline

Purpose: establish runtime parity and visibility before later sprints add real deploy and scale complexity.

Primary outputs:

- `platform/docker/`
- `platform/k8s/`
- `platform/edge/`
- `tools/scripts/dev.py`
- runtime identity, health, readiness, and release marker surfaces
- `docs/observability.md`
- `docs/resilience.md`

See: [`d5-runtime-parity.md`](./d5-runtime-parity.md)
