# 🌟 S0-D5 — 🐳 Docker + ☸️ k3s + 🔍 Observability Baseline

## TL;DR

S0-D5 establishes the first honest runtime contract for the rebuild. It creates one container surface per deployable unit, one local cluster surface per deployable unit, and one shared baseline for health, readiness, request correlation, runtime identity, and release markers.

## Index

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

<a id="why-this-deliverable-exists"></a>
## Why this deliverable exists

Without D5, the rebuild can still look disciplined in Git and docs while remaining operationally vague. That leads to familiar problems:

- each app grows its own startup assumptions
- containerization is added later and forces structure churn
- health/readiness is retrofitted inconsistently
- observability gets bolted on after routes and jobs already exist
- later deploy work inherits unclear service boundaries
- release debugging starts without request IDs or release markers

D5 creates the first permanent homes for:

- container build surfaces
- local cluster surfaces
- service entry assumptions
- health/readiness semantics
- observability vocabulary
- verification hooks for later load, chaos, and rollout work

---

<a id="ownership"></a>
## 👥 Ownership

**Owner:** 👤🛡️ Platform/QA  
**Reviewer:** 👤👻 AI/Cloud  
**Required consult:** 👤🧰 BE/API, 👤🎨 FE/Data

---

<a id="branch"></a>
## 🌿 Branch

` s0/d5-runtime-parity `

---

<a id="deliverable-pr-title"></a>
## 🏷️ Deliverable PR title

`chore(platform): seed container cluster and telemetry entrypoints so later runtime work grows from one observable parity spine`

---

<a id="purpose"></a>
## 🎯 Purpose

Create the first permanent runtime and observability surfaces so later work can:

- run consistently in local containerized form
- map cleanly onto local k3s topology
- expose health/readiness expectations from day one
- emit request IDs, service identity, and release markers consistently
- extend one shared observability model instead of inventing service-by-service telemetry behavior

---

<a id="depends-on"></a>
## ⛓️ Depends on

- 🌟 S0-D1 — 🧼 Repo Reset + 🧊 Legacy Freeze
- 🌟 S0-D2 — 🧱 Active Tree + 🔌 Shared Seams
- 🌟 S0-D3 — 🐝 Agent Steering + 📚 Docs Spine
- 🌟 S0-D4 — 🐙 CI/CD + 🛡️ Quality Gates

---

<a id="blocks"></a>
## 🚧 Blocks

- Sprint 1 implementation work that needs honest runtime startup assumptions
- later deploy extension work in `.github/workflows/cd.yml`
- later platform work under `platform/edge/` and `platform/infra/`
- later chaos/load work that needs health/readiness and telemetry vocabulary

---

<a id="files-touched"></a>
## 📂 Files touched

### New platform container files

- `platform/docker/web.Dockerfile`
- `platform/docker/api.Dockerfile`
- `platform/docker/worker.Dockerfile`
- `platform/docker/agent.Dockerfile`

### New local cluster files

- `platform/k8s/web.yaml`
- `platform/k8s/api.yaml`
- `platform/k8s/worker.yaml`
- `platform/k8s/agent.yaml`
- `platform/k8s/migrate.yaml`

### New edge/runtime config files

- `platform/edge/cache.yaml`
- `platform/edge/gateway.yaml`
- `platform/edge/limits.yaml`

### New runtime helper scripts

- `tools/script/dev.py`

### Meaningfully refactored app/runtime files

- `apps/api/main.py`
- `apps/api/routes.py`
- `apps/api/middleware.py`
- `apps/worker/main.py`
- `apps/agent/main.py`
- `README.md`
- `docs/operations.md`
- `docs/observability.md`
- `docs/resilience.md`

---

<a id="recommended-names"></a>
## 🧠 Recommended names

### Service names

- `web`
- `api`
- `worker`
- `agent`
- `migrate`

### Runtime names

- `service_name`
- `service_version`
- `service_env`
- `service_region`
- `release_id`
- `request_id`

### Health/readiness route names

- `health`
- `ready`
- `live`

### Metric names

- `request_total`
- `request_latency_ms`
- `request_error_total`
- `queue_depth`
- `stream_lag`
- `cache_hit_total`
- `cache_miss_total`
- `release_marker_total`

---

<a id="exact-tldr-sections-per-new-or-refactored-file"></a>
## 🧾 Exact TL;DR sections per new or refactored file

D5 should apply the exact Sprint 0 TL;DR content to:

- `platform/docker/*.Dockerfile`
- `platform/k8s/*.yaml`
- `platform/edge/*.yaml`
- `tools/script/dev.py`

It should also update:

- `apps/api/main.py`
- `apps/api/routes.py`
- `apps/api/middleware.py`
- `apps/worker/main.py`
- `apps/agent/main.py`

with new section groups for:

- health/readiness
- request IDs
- release context
- runtime identity
- telemetry hooks

New docs:

- `docs/observability.md`
- `docs/resilience.md`

Updated docs:

- `docs/operations.md`
- `README.md`

---

<a id="hotspot-files"></a>
## ⚠️ Hotspot files

These files define how runtime parity and observability will evolve later:

- `platform/docker/api.Dockerfile`
- `platform/k8s/api.yaml`
- `apps/api/main.py`
- `apps/api/middleware.py`
- `docs/observability.md`
- `docs/resilience.md`

---

<a id="task-tickets"></a>
## 🎟️ Task tickets

### 🎟️ S0-D5-T1 — 🐳 Seed the container build surfaces for every deployable unit

**Commit title:**  
`chore(platform): create permanent container build files for web api worker and agent runtimes`

### 🎟️ S0-D5-T2 — ☸️ Seed the local cluster parity manifests

**Commit title:**  
`chore(k8s): add stable local cluster manifest homes for web api worker agent and migration execution`

### 🎟️ S0-D5-T3 — 🔍 Seed the runtime identity, health, and request-correlation surfaces

**Commit title:**  
`chore(runtime): add health readiness request id and release marker surfaces to the active runtime entry files`

### 🎟️ S0-D5-T4 — 📚 Seed edge policy vocabulary, local runtime helpers, and observability/resilience docs

**Commit title:**  
`docs(runtime): define edge policy vocabulary local parity helpers and the first observability and resilience docs`

---

<a id="verification-tickets"></a>
## 👾 Verification tickets

### 👾 S0-D5-T1-V — 🧠 Verify parity surfaces map cleanly to the active runtimes

**Commit title:**  
`test(platform): verify each active runtime has exactly one container surface and one local cluster surface`

### 👾 S0-D5-T2-V — 🔍 Verify runtime visibility and docs tell the same operational story

**Commit title:**  
`test(observe): verify runtime identity health visibility and docs language stay aligned across code and docs`

---

<a id="deliverable-verification"></a>
## ✅ Deliverable verification

S0-D5 is done only when:

- `platform/docker/` contains one permanent Dockerfile per deployable runtime
- `platform/k8s/` contains one permanent manifest per deployable runtime plus one migration job surface
- the active runtimes have seeded visibility and health surfaces
- `docs/observability.md` and `docs/resilience.md` exist
- code comments, docs, and root guidance all describe the same D5 scope without pretending full deployment maturity

---

<a id="bad-agent-output-patterns-to-watch-for"></a>
## 🚨 Bad agent output patterns to watch for

Reject immediately if an agent tries to:

- turn Dockerfiles into fully provider-specific production images already
- create multiple manifest variants per runtime before there is real need
- bury health/readiness and request ID behavior in ad hoc files
- write observability docs that sound complete while the code only seeds section groups
- make `dev.py` a generic script junk drawer
- introduce different names for the same concepts across API, worker, and agent runtimes
- bake secrets, deploy policies, or provider-specific rollout logic into D5

---

<a id="rationale-in-one-sentence"></a>
## 🧩 Rationale in one sentence

S0-D5 is successful when the rebuild has one honest runtime packaging, local topology, and baseline visibility model, so later feature work grows from observable parity instead of uninstrumented assumptions.
