# Food Run Master Packet

## TL;DR

Food Run is being rebuilt from a validated prototype into a funding-grade, technically documented, end-to-end product that is honest about scale, disciplined about failure, and governable by a small team using multi-agent delivery workflows. The current public repo and demo remain useful evidence of product direction, but they should be preserved as `legacy-v0/` rather than hardened in place.

## Table of Contents

- [0) 📌 Packet Purpose](#0-packet-purpose)
- [1) 🧭 Executive Summary](#1-executive-summary)
- [2) 🧱 Current-State Baseline to Preserve](#2-current-state-baseline-to-preserve)
- [3) 🎯 Product Goal](#3-product-goal)
- [4) 🧠 Core Architecture Principles](#4-core-architecture-principles)
- [5) 📏 Workload Model and Sizing Assumptions](#5-workload-model-and-sizing-assumptions)
- [6) 🏗️ Target System Architecture](#6-target-system-architecture)
- [7) 🗄️ Data and Storage Topology](#7-data-and-storage-topology)
- [8) 🔁 Consistency Policy](#8-consistency-policy)
- [9) ⚡ Caching Strategy](#9-caching-strategy)
- [10) 📦 Async, Queue, and Stream Strategy](#10-async-queue-and-stream-strategy)
- [11) 🤖 Agentic AI Engineering Model](#11-agentic-ai-engineering-model)
- [12) 📚 Documentation Strategy](#12-documentation-strategy)
- [13) 🗂️ Target Repo Layout](#13-target-repo-layout)
- [14) 🔌 Adapter Catalog](#14-adapter-catalog)
- [15) 🔐 Governance, Open Core, and Contribution Model](#15-governance-open-core-and-contribution-model)
- [16) 🧪 Quality Strategy](#16-quality-strategy)
- [17) 🧰 Tooling Strategy](#17-tooling-strategy)
- [18) 🔍 Observability and Operations](#18-observability-and-operations)
- [19) 🔥 Failure Model and Black-Swan Strategy](#19-failure-model-and-black-swan-strategy)
- [20) 👥 Team Operating Model](#20-team-operating-model)
- [21) 📅 Revised Sprint Map](#21-revised-sprint-map)
- [22) ✅ Acceptance Criteria](#22-acceptance-criteria)
- [23) 🚨 Non-Negotiables](#23-non-negotiables)
- [24) Bottom Line](#24-bottom-line)
- [25) **Emoji Legend (Updated, Non-Overlapping, Food Run v1)**](#25-emoji-legend-updated-non-overlapping-food-run-v1)

---


## 0) 📌 Packet Purpose

This packet consolidates the earlier split between the “spec packet” and “team lead packet” into one source of truth for:

- product scope
- technical architecture
- scale posture
- operations posture
- repo structure
- delivery model
- governance rules
- sprint map
- acceptance criteria

This packet is **not** the future repo docs verbatim. It is the planning packet that should drive the repo rebuild, the docs skeleton, the ADR spine, and the sprint breakdowns.

---


## 1) 🧭 Executive Summary

Food Run is being rebuilt from a validated meal-planning prototype into a funding-grade, technically documented, end-to-end product that can evolve toward very large-scale usage and burst-heavy ingestion while remaining operable by a small team.

The rebuild is designed around five planes:

- **experience plane** — buys latency and shields origin
- **product plane** — preserves business truth and invariants
- **event plane** — absorbs burst writes and enables replay
- **agent plane** — accelerates delivery with governed multi-agent workflows
- **operations plane** — makes degradation, release, recovery, and cost visible and controllable

The central architectural choice is:

- **Postgres remains the durable system of record for product truth**
- **raw inbound events do not terminate at Postgres on the hot path**

That decision keeps the scale story honest.

---


## 2) 🧱 Current-State Baseline to Preserve

### 2.1 What the prototype already proves

The current prototype already validates the product loop:

- import recipe URLs
- normalize ingredient data
- let the user confirm or edit ingredients
- combine multiple recipes into one shopping list
- subtract pantry items
- present a usable planning workflow

That core loop is visible in the public README and live demo, and it should be preserved as the product nucleus during the rebuild.

### 2.2 What should not be scaled in place

Treat the current baseline as **legacy-v0**, not as the active v1 source tree, because it currently reflects:

- root `client/`, `server/`, and `docs/`
- React/Vite frontend
- Express server
- npm workflow
- TypeScript 5.9.3
- direct prototype-style coupling between the current UI, server, and build paths

### 2.3 Rebuild stance

- preserve current prototype behavior
- preserve the current repo as a historical artifact
- move active build paths into a new architecture-aligned tree
- make the rebuild look intentional, not accidental

---


## 3) 🎯 Product Goal

### 3.1 Funding-grade v1 goal

Demonstrate a credible, end-to-end product that supports:

- recipe import with review and approval
- recipe versioning and attribution
- pantry-aware meal planning and shopping lists
- household and sharing models
- AI-assisted retrieval, validation, and recommendations
- robust technical documentation
- local-to-cloud parity
- operational controls and observability
- governed agentic delivery workflows

### 3.2 Product thesis

Food Run should become the system that sits between:

- how users actually discover recipes
- how households actually plan meals
- how teams actually shop efficiently
- how modern AI can help without bypassing correctness

---


## 4) 🧠 Core Architecture Principles

### 4.1 Truth and scale are separated

- Postgres stores product truth.
- Stream/log infrastructure absorbs raw high-volume event scale.
- Reducers and projections turn event volume into useful derived state.

### 4.2 Shared cache is optional

- Redis is an accelerator.
- Correctness must survive when Redis is unavailable.
- No critical product invariant may depend on distributed cache availability.

### 4.3 Business rules are centralized

- FastAPI owns the public contract.
- The Django service layer owns business rules.
- The frontend does not own authorization or truth.
- Workers do not silently become domain authority.

### 4.4 AI is governed, not magical

- Every meaningful agent action produces artifacts.
- Protected paths require human approval.
- LangGraph and LangSmith are part of a quality loop, not ornamentation.
- Review is both a correctness gate and a knowledge-transfer gate.

### 4.5 Failure is guaranteed

- degraded modes must be explicit
- stale-read mode, queued-write mode, and read-only mode are designed in advance
- chaos drills are mandatory
- operational runbooks and ADRs are part of the build, not afterthoughts

### 4.6 Complexity must keep earning its place

Every layer has:

- dollar cost
- latency cost
- maintenance cost
- cognitive cost

Nothing stays just because it sounds advanced.

---


## 5) 📏 Workload Model and Sizing Assumptions

These are planning estimates, not measured production numbers.

### 5.1 Traffic classes

#### Interactive user traffic

Plan for:

- **edge/API requests:** `50k–150k RPS steady`
- **edge/API bursts:** `300k–600k RPS burst`
- **origin requests after edge/client offload:** `5k–25k RPS`

#### Product writes

These are correctness-sensitive writes, such as:

- approvals
- pantry changes
- household changes
- meal plan changes
- shopping list changes

Plan for:

- **critical product writes:** `1k–10k writes/sec`

#### Raw event ingest

This is a different class of workload:

- telemetry
- activity streams
- agent run events
- partner/import events
- audit-like append-heavy flows

Plan for:

- **raw inbound event volume:** `0.5M–10M events/sec`

### 5.2 Bandwidth estimate

Assume compressed event payload sizes:

- at **250 B/event**:
  - `0.5M EPS ≈ 1 Gbps`
  - `10M EPS ≈ 20 Gbps`
- at **1 KB/event**:
  - `0.5M EPS ≈ 4 Gbps`
  - `10M EPS ≈ 80 Gbps`

This is before replica traffic, east-west replication, replay traffic, and downstream consumer fan-out.

### 5.3 Five-year storage estimate

If raw events were retained naively for five years:

- at **250 B/event**:
  - roughly **19.7 PB to 394 PB**
- at **1 KB/event**:
  - roughly **78.8 PB to 1.58 EB**

So the production posture must be:

- short hot retention
- compaction
- selective replay windows
- cold archival
- aggressive aggregation
- curated truth in Postgres rather than full firehose retention

### 5.4 Latency budget policy

#### Very low latency targets

- static assets
- edge-cached config
- public read-most views

#### Moderate latency targets

- personalized dashboards
- cached list/detail views
- recommendation retrieval backed by cached or replica-safe reads

#### Strong correctness paths

- approvals
- household role changes
- pantry/plan/list writes
- identity and session mutations

These may accept slightly higher latency because correctness dominates.

---


## 6) 🏗️ Target System Architecture

### 6.1 Plane model

#### Experience plane

Owns:

- Angular SPA
- client cache
- CDN
- edge cache
- edge compute
- WAF
- API gateway
- request shaping

Goal:

- fast paint
- early rejection
- offload of read-most traffic
- cheap latency wins

#### Product plane

Owns:

- FastAPI public contract
- auth/session checks
- request context
- Django service layer
- Postgres primary
- read replicas
- pgvector
- outbox
- idempotency store
- lock store
- local LRU
- optional shared cache

Goal:

- correctness
- business invariants
- durable truth
- safe sync user flows

#### Event plane

Owns:

- ingest edge
- append-only stream/log
- consumer groups
- dedupe
- retry
- replay
- compaction
- reducers
- analytics sinks
- async jobs
- search/vector feeders

Goal:

- burst absorption
- replayability
- async decoupling
- derived-state production

#### Agent plane

Owns:

- OpenCode orchestration
- scout/planner/coder/reviewer/integrator lanes
- LangGraph flows
- LangSmith traces
- eval harness
- artifact lifecycle
- approval checkpoints

Goal:

- governed parallelism
- artifact-backed delivery
- reduced delivery time without reduced maintainability

#### Operations plane

Owns:

- metrics
- traces
- logs
- profilers
- dashboards
- alerting
- mitigations
- release controls
- rollback
- chaos drills
- failover modes
- FinOps loop

Goal:

- visibility
- control
- recovery
- budget discipline

---


## 7) 🗄️ Data and Storage Topology

### 7.1 Durable product truth in Postgres

Postgres stores:

- users
- households
- memberships
- roles
- recipes
- recipe versions
- approvals
- pantry items
- meal plans
- shopping lists
- prompt registry
- eval results
- artifact index
- agent run metadata
- idempotency records
- lock records
- outbox records

### 7.2 Read replicas

Replicas serve routes that can tolerate bounded lag, such as:

- dashboards
- recommendation candidate views
- search-ish reads
- feed-like list reads
- analytics-style views

The primary serves:

- correctness-sensitive reads
- all writes
- recency-sensitive permission and approval checks

### 7.3 pgvector

Use it for:

- semantic retrieval
- recommendation candidates
- recipe similarity
- pantry/recipe proximity
- future retrieval augmentation

### 7.4 Stream/log storage

Use it for:

- raw high-rate event append
- replay windows
- consumer decoupling
- reduction inputs
- append-only operational history where appropriate

### 7.5 Blob store

Use it for:

- images
- generated reports
- archived artifacts
- exported eval bundles
- optional debug snapshots

Never use it as:

- product truth
- authoritative recipe state
- authoritative permissions state

---


## 8) 🔁 Consistency Policy

### 8.1 Stronger consistency required

Use stronger correctness guarantees for:

- approvals
- identity/session mutation
- role changes
- household membership
- pantry edits
- shopping list edits
- meal plan writes
- idempotency completion
- outbox append paired with truth mutation

### 8.2 Eventual consistency acceptable

Allow bounded staleness for:

- recommendation views
- dashboards
- read-most lists
- search results
- read models
- analytics
- cache-backed pages
- some public or semi-public recipe detail pages

### 8.3 Explicit degraded modes

#### Stale-read mode

- stale or replica-backed reads allowed
- freshness hints shown

#### Queued-write mode

- non-critical idempotent writes accepted as pending
- explicit pending acknowledgement required

#### Read-only safety mode

- risky writes blocked
- browsing remains available

#### Partial failover mode

- a secondary region serves traffic
- latency and capacity may degrade
- correctness boundaries remain explicit

---


## 9) ⚡ Caching Strategy

### 9.1 Layered caching

#### Client-side

- route snapshots
- user/household snapshot
- pantry snapshot
- current plan snapshot
- shopping list snapshot
- recommendation snapshot

#### Edge/CDN

- static assets
- safe cacheable GETs
- stale-while-revalidate paths where appropriate

#### Product-side local cache

- per-request memoization
- process-local LRU for hot objects

#### Shared cache

- optional Redis-backed cross-node acceleration
- only where hit rate and saved cost justify it

### 9.2 Adaptive cache rule

A route qualifies for shared caching only if it demonstrates:

- meaningful hit rate
- meaningful saved origin latency
- meaningful saved origin cost
- clear invalidation ownership

### 9.3 Long-tail rule

If 90% of a workload is one-off access:

- do not blindly put shared-cache overhead on all requests
- prefer edge caching, request collapse, local LRU, or direct origin
- remove net-negative caches

### 9.4 Hot-key protections

- request collapsing
- stale-while-revalidate
- per-key concurrency caps
- read-model promotion for repeat hotspots
- emergency edge promotion for safe public objects

---


## 10) 📦 Async, Queue, and Stream Strategy

### 10.1 Product writes versus raw events

#### Product writes

Flow:

- request
- contract validation
- auth/scope
- domain service
- primary DB transaction
- outbox append
- commit
- user response

#### Raw events

Flow:

- ingress edge
- envelope validation
- partitioning
- append-only stream write
- durable append acknowledgement
- async consumer processing

### 10.2 Outbox pattern

Every product mutation with downstream effects writes:

- domain truth
- outbox record
- idempotency completion

in the same transaction.

### 10.3 Consumer responsibilities

Consumer groups handle:

- reducers
- read-model builders
- search/vector refresh
- analytics
- anomaly detection
- archival
- low-priority async enrichments

### 10.4 Replay policy

Replay is used for:

- rebuilding derived state
- recovering from buggy consumers
- rebuilding vector/search structures
- rebuilding dashboards and aggregates

Replay is not used as a casual mechanism to rewrite product truth.

---


## 11) 🤖 Agentic AI Engineering Model

### 11.1 Delivery posture

OpenCode is used as a governed engineering accelerator, not an autonomous repo writer.

OpenCode supports project-level `AGENTS.md`, custom agents in `.opencode/agents/`, reusable commands, reusable skills, and permission controls that can be scoped per agent. That makes it a strong fit for the lane-based workflow below.

### 11.2 Lane model

#### Scout lane

Owns:

- discovery
- reuse search
- hotspot mapping
- dependency tracing
- risk notes

Default mode:

- read-only

#### Planner lane

Owns:

- task decomposition
- file tree impact
- ADR deltas
- recommended names
- verification checklist
- owner/reviewer mapping

#### Coder lane

Owns:

- bounded edits in assigned paths
- tests with implementation
- comment and TL;DR updates
- patch artifact creation

#### Reviewer lane

Owns:

- convention checks
- reuse checks
- dead export checks
- cognitive debt checks
- reject/approve recommendation

Default mode:

- read-only

#### Integrator lane

Owns:

- contract sync
- smoke-path reasoning
- cross-boundary fit
- docs alignment
- integration verification

### 11.3 Human-only zones

Always gated:

- auth/session invariants
- migrations
- role/tenancy enforcement
- secrets handling
- release workflow
- queue replay policy
- failover policy
- destructive infrastructure changes

### 11.4 Mandatory review questions

No merge if the answer to any of these is **no**:

- does it reuse existing patterns where possible?
- does it follow repo conventions?
- can the developer explain every line?
- does the developer understand why this approach was chosen?
- can the developer modify it without re-prompting?
- does the ADR delta explain what was built and what breaks if it changes?

### 11.5 Eval loop

Every meaningful agent run should produce:

- trace
- artifact
- approval status
- reviewer decision
- cost/latency metadata
- rejection/rework data

That data should refine:

- prompts
- permissions
- lane rules
- review heuristics
- `AGENTS.md`

---


## 12) 📚 Documentation Strategy

### 12.1 Doc posture

- one root `README.md`
- deep technical docs in `/docs`
- no generic placeholder docs
- every doc must be a real permanent target file
- ADR is consolidated in one evolving file

### 12.2 Doc set

```text
docs/
├── adr.md
├── architecture.md
├── repo.md
├── web.md
├── api.md
├── domain.md
├── worker.md
├── agent.md
├── data.md
├── cache.md
├── edge.md
├── observability.md
├── resilience.md
├── operations.md
├── testing.md
└── legacy-v0.md
```

### 12.3 ADR rule

Each meaningful change must document:

#### Technical audience

- what was built
- why it was chosen
- what boundaries it owns
- what breaks if a section changes
- known edge cases or failure modes

#### Non-technical audience

- why this work matters
- what capability it unlocks
- why the chosen design is safer or more scalable
- what trade-off the team accepted

The ADR update happens:

- after the code is understood
- before merge
- as part of the same PR flow

---


## 13) 🗂️ Target Repo Layout

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
├── .opencode/
│   ├── agents/
│   ├── commands/
│   ├── rules/
│   └── skills/
├── apps/
│   ├── web/
│   ├── api/
│   ├── domain/
│   ├── worker/
│   └── agent/
├── shared/
│   ├── contract/
│   ├── schema/
│   ├── adapter/
│   └── testkit/
├── platform/
│   ├── docker/
│   ├── k8s/
│   ├── edge/
│   └── infra/
├── tools/
│   ├── chaos/
│   ├── eval/
│   ├── load/
│   └── script/
├── docs/
│   └── ...
└── legacy-v0/
    ├── README.md
    ├── client/
    ├── server/
    └── docs/
```

### 13.1 Layout rules

- prefer deployable-unit boundaries first
- keep nesting shallow
- centralize shared contracts and adapters
- preserve the prototype under `legacy-v0/`
- never duplicate conceptually identical files under different sibling folders unless unavoidable

---


## 14) 🔌 Adapter Catalog

These should sit behind swappable ports where appropriate.

### 14.1 Required ports

- `LLMProvider`
- `EmbeddingProvider`
- `VectorStore`
- `LocalCache`
- `SharedCache`
- `BlobStore`
- `JobQueue`
- `StreamLog`
- `IdentityProvider`
- `SessionProvider`
- `MetricSink`
- `TraceSink`
- `LogSink`
- `FeatureFlagProvider`
- `IdempotencyStore`
- `LockStore`
- `RateStore`
- `SearchStore`
- `Clock`
- `OutboxStore`

### 14.2 Default early adapters

- process-local LRU
- Postgres-backed idempotency
- Postgres-backed outbox
- Postgres-backed locks where acceptable
- local or low-cost embeddings
- lower-cost LLM path by default
- dev/local blob store or S3-compatible path
- local queue or low-cost queue provider for development

### 14.3 Burst/scale adapters

- Redis shared cache
- managed stream/log
- managed queue
- production CDN/edge compute
- managed blob store
- distributed search/vector system if pgvector becomes the bottleneck
- stronger auth/session provider when the business need justifies it

### 14.4 Adapter rule

Keep ports:

- narrow
- capability-based
- hot-path conscious
- startup-selectable where possible

---


## 15) 🔐 Governance, Open Core, and Contribution Model

### 15.1 CE/EE model

#### Community Edition

- public
- GPLv3
- full open-source product foundation
- accepts community PRs
- contains the core planning loop and grounded AI capabilities

#### Enterprise Edition

- private
- proprietary
- reserved for monetization and enterprise extensions
- must never leak into CE

### 15.2 CE guardrails

- CLA required
- trademark policy enforced
- governance at the repo root
- no EE imports or temporary EE code in CE
- CE remains buildable and useful on its own

### 15.3 Extension-points-first rule

If EE needs a capability:

- create a CE extension point
- do not hardwire EE logic into CE
- document the interface boundary
- contract-test the boundary

---


## 16) 🧪 Quality Strategy

### 16.1 Testing stack

- unit tests
- integration tests
- contract tests
- smoke tests
- end-to-end tests
- chaos tests
- load tests
- agent-output verification checks

### 16.2 Verification posture

Code review must catch:

- broken flows nobody can debug
- suppressed errors instead of fixed errors
- phantom code
- repo-convention drift
- plausible-but-wrong logic
- explainability gaps

### 16.3 CI gates

Every merge should require:

- lint/format/type gates
- unit and integration checks
- contract drift check
- dead export / duplicate logic scan
- docs / ADR completeness checks
- smoke validation
- protected-path approval where relevant

---


## 17) 🧰 Tooling Strategy

### 17.1 Runtime/toolchain target

- Bun for the JS/TS package/runtime workflow in the active tree
- TS6 baseline in the active rebuild
- Python environment managed cleanly for the domain/worker/agent stack
- no continued architectural dependence on npm in the active tree

### 17.2 Infrastructure definition posture

Use state-managed declarative infrastructure for:

- network
- DNS
- buckets
- secrets backends
- managed database
- foundational cloud resources

Use more app-oriented manifests/config for:

- deployable topology
- service wiring
- rollout configuration
- local cluster parity

### 17.3 Local parity

Mandatory:

- Docker
- local k3s
- local smoke path
- migration/test parity
- agent workflow parity as much as practical

---


## 18) 🔍 Observability and Operations

### 18.1 Mandatory signals

Track at minimum:

- request latency
- error rate
- queue depth
- stream lag
- replica lag
- cache hit/miss and saved milliseconds
- hot-key concentration
- model/provider cost
- agent run acceptance/rejection
- deployment markers

### 18.2 Alert categories

- SLO burn
- latency regressions
- queue/stream lag
- cache collapse
- replica lag
- provider cost spikes
- route-specific failure spikes
- agent workflow quality regressions

### 18.3 Chaos drills

Mandatory drill catalog includes:

- cache loss
- queue backlog
- consumer failure
- replica lag
- hot-key explosion
- region loss
- throttled failover link
- auth provider slowdown
- blob store outage

---


## 19) 🔥 Failure Model and Black-Swan Strategy

### 19.1 Assumed failures

Assume all of these will happen eventually:

- cache down
- disk pressure
- duplicate events
- replay need
- hot key
- replica lag
- consumer bug
- region loss
- throttled failover
- provider latency spike
- agent workflow producing plausible-but-dangerous output

### 19.2 Black-swan policy

The system must prefer:

- clear degraded experience
- preserved invariants
- explicit user messaging
- bounded write acceptance
- replayable recovery
- documented incident response

over:

- false normality
- silent partial corruption
- hidden stale data
- optimistic unsafe writes

---


## 20) 👥 Team Operating Model

### 20.1 Roles

- 👤🎯 Team Lead
- 👤🎨 FE/Data
- 👤🧰 BE/API
- 👤👻 AI/Cloud
- 👤🛡️ Platform/QA

### 20.2 High-level ownership map

#### 👤🎨 FE/Data

- Angular UX
- client cache
- generated client usage
- dashboard/read-model views
- route usability

#### 👤🧰 BE/API

- FastAPI contract
- Django service boundaries
- TDD ownership
- contract/integration checks
- idempotent write flows

#### 👤👻 AI/Cloud

- LangGraph
- LangSmith
- embeddings
- retrieval
- provider routing
- eval harness
- cloud adapter wiring

#### 👤🛡️ Platform/QA

- Docker
- k3s
- CI/CD
- load validation
- reliability checks
- rollback safety
- chaos drill execution

#### 👤🎯 Team Lead

- architecture review
- boundary enforcement
- sprint demo review
- protected-path approvals
- funding-walkthrough narrative alignment

---


## 21) 📅 Revised Sprint Map

This is the master sprint outline only. The granular breakdown belongs to task-level planning.

### 📅 Sprint 0 — 🧼 Repo Reset, 🧱 Foundations, 🐝 Agent Steering, 📚 Docs Spine

- archive prototype
- establish new active tree
- set style, comment, and governance enforcement
- establish the OpenCode lane model
- local Docker/k3s parity
- docs and ADR spine

### 📅 Sprint 1 — 🐍 Contract Spine, 🧩 Domain Spine, 🔑 Auth Boundaries

- FastAPI public contract
- Django domain authority
- auth/session and tenancy spine
- idempotency/outbox/lock/rate interfaces

### 📅 Sprint 2 — 🌐 Edge, 🚪 Gateway, ⚡ Adaptive Cache, 🔍 Core Observability

- CDN posture
- edge rules
- gateway controls
- local LRU
- optional shared-cache seam
- observability baseline

### 📅 Sprint 3 — 📦 Queue/Stream Spine, 🧱 Async Jobs, 🗄️ Data Safety

- queue/log foundation
- replay/dead-letter posture
- reduction path
- event correctness boundaries

### 📅 Sprint 4 — 🍽️ Recipes, ✏️ Planning, 🧃 Pantry, ✅ Approval Flows

- import/edit/approval
- recipe library
- pantry/plans/lists
- product-core loop

### 📅 Sprint 5 — 🤖 AI Plane, 🧬 LangGraph/LangSmith, 🧠 Search/Vector, 🧪 Evals

- retrieval
- grounding
- prompt/version registry
- eval harness
- governed AI product flows

### 📅 Sprint 6 — ⚡ Scale Layer, 🗄️ Replicas/Shards, 🔥 Hot-Key Defense

- replica policy
- partition strategy
- shard decision framework
- hot-key response model
- burst-mode tuning

### 📅 Sprint 7 — 🔥 Chaos Resilience, ☁️ Multi-Region Recovery, 🚢 Launch Readiness

- black-swan drills
- failover modes
- launch hardening
- runbooks
- funding-demo readiness

---


## 22) ✅ Acceptance Criteria

### 22.1 Product acceptance

Food Run is demo-ready when it can:

- import recipes into editable drafts
- require explicit approval before durable use
- preserve versioning and attribution
- manage pantry state and shopping lists
- support household/shared workflows
- deliver grounded AI-assisted flows
- show a clear durable truth model

### 22.2 Technical acceptance

Food Run is technically credible when it has:

- a clean active repo layout
- real docs and ADR discipline
- governed agent workflows
- observability and alerts
- queue/stream + replay posture
- idempotent write posture
- cache-optional correctness
- local parity and cloud path
- release/rollback safety
- rehearsed degraded modes

### 22.3 Funding-review acceptance

Food Run is diligence-ready when reviewers can see:

- product loop
- scale-posture honesty
- failure-posture honesty
- strong technical judgment
- a clear operating model for a small team
- a clear path from v1 to v2/v3 without redoing the foundation

---


## 23) 🚨 Non-Negotiables

- Postgres is the product truth, not the firehose sink.
- Shared cache is optional.
- Protected paths require explicit human approval.
- Every meaningful change updates ADR context.
- Every meaningful agent run produces artifacts.
- No merge if the developer cannot explain the code.
- No generic placeholder docs.
- No EE leakage into CE.
- No scaling theatrics that the team cannot operate.

---


## 24) Bottom Line

This rebuild is no longer framed as:

- “upgrade the prototype”
- “add a few cloud features”
- “use AI to move faster”

It is framed as:

- **preserve the proven product loop**
- **rebuild around truth, scale, governance, and recovery**
- **use agentic AI as a disciplined force multiplier**
- **show architecture maturity that survives both interviews and diligence**

---


## 25) **Emoji Legend (Updated, Non-Overlapping, Food Run v1)**

### 👥 People (always prefixed with 👤)

- 👤🎯 Team Lead — hands-off architecture review, sprint demo review, decision approvals, boundary enforcement
- 👤🎨 FE/Data — Angular UX, generated client usage, cache-first UI, dashboard views, typed frontend integration
- 👤🧰 BE/API — FastAPI contract layer, Django service integration, TDD ownership, contract and integration checks
- 👤👻 AI/Cloud — LangGraph, LangSmith, embeddings, RAG, provider orchestration, cloud wiring
- 👤🛡️ Platform/QA — Docker, k3s, CI/CD, reliability checks, load validation, rollout safety

### 📅 Events / Process

- 💠 Standup / async daily update — what changed, what is next, blockers, dependency flags; may also label coordination heartbeats and the live active-status view
- 🔶 Contract sync — API schema, generated client, and request/response alignment checkpoint
- 🔐 Merge lock / freeze — branch protection active, risky merges paused
- ✅ QA checkpoint — required checks passed, smoke path confirmed; may also label verified coordination checkpoints
- 🤝 Handoff — ownership transfer between humans or agents with current status, blockers, and next best action
- 📖 Docs checkpoint — ADR, technical docs, and runbooks updated
- 🎬 Demo checkpoint — scripted rehearsal run before sprint review; visible in sprint review, funding walkthrough, or external stakeholder narrative
- 🚢 Release cut — approved mainline snapshot prepared for deploy
- 🧭 Architecture review — boundary, scale, reliability, and trade-off review with the lead

### 🎟️ Ticket Prefixes / Work Lanes

- 🧼 Cleanup / rebuild — refactors, repo reset, drift removal, active path cleanup
- 🧱 Foundations — structure, configuration, shared scaffolding, long-lived patterns
- 🖼️ UI/UX — screens, flows, accessibility, styling, frontend state handling
- 🐍 FastAPI — public REST API, envelopes, middleware, OpenAPI generation
- 🧩 Django — ORM, migrations, admin, domain services, deterministic business rules
- 🔑 Auth — OAuth2, JWT, refresh, roles, scopes, membership rules
- 🗄️ DB/data — Postgres, schema, indexes, partitions, integrity rules, read models
- 🧪 Testing — unit, integration, contract, smoke, E2E, deterministic fixtures
- 🐝 Agentic AI — repo steering, sub-agent roles, OpenCode workflows, human-in-the-loop
- 🧬 Graph/Evals — LangGraph, LangSmith, traces, eval runs, prompt/version tracking
- 🤖 AI/LLM — providers, prompts, embeddings, retrieval, reranking, grounding
- 🐳 Docker — images, compose, local container parity
- ☸️ Kubernetes — k3s manifests, deployments, jobs, local cluster parity
- ☁️ Cloud — Render, Cloud Run, object storage, env wiring, deploy targets
- 🐙 CI/CD — GitHub Actions, PR gates, release pipelines, automation hooks
- 🔍 Observability — metrics, traces, correlation IDs, dashboards, visibility
- ⚡️ Optimization — performance, latency, caching, throughput, cold-start reduction, runtime efficiency, coordination overhead, read/write trade-offs, long-tail
- 📚 Docs — technical docs, runbooks, implementation guidance, diagrams
- 🧾 ADR — architecture decision record updates in the single ADR file
- 👾 Verification — action-by-action review, smoke validation, agent-output review checklist
- 🌐 Edge — CDN, edge compute, cache rules, request shaping, regional routing
- 📦 Queue/stream — job queues, event streams, retries, compaction, replay
- 🛠️ Tooling — scripts, lint config, codegen, local helpers, developer workflow
- 🔒 Security — secrets handling, auth hardening, rate limits, compliance-sensitive work
- 🧃 Pantry — pantry domain flows, stock state, deduction rules
- 🍽️ Recipes — recipe ingestion, parsing, normalization, versioning, attribution
- ✏️ Planning — meal plans, shopping lists, household planning flows; may also label task framing and coordination task packets
- 🧠 Search/vector — pgvector, retrieval, semantic search, recommendation candidate lookup

### ⛳️ Markers

- ⚠️ Hotspot Files — high-churn or high-risk files/paths that need careful review; this marker may appear in repo-control coordination artifacts
- 🚨 Alert — security-sensitive, destructive, externally visible, or boundary-breaking change
- 💸 FinOps — anything cost-critical that can spike provider, compute, storage, or CI spend
- 🔥 Chaos Resilience — ops risks, rollback risk, drift risk, blast radius, failure handling, chaos drills, recovery logic, fallback paths
