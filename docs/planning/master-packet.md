# 📦 Food Run Master Packet

## 1. 🧭 Decisive Summary

### 1.1 TL;DR

Food Run is now being executed as a **🤖 AI-native production rebuild** with **📅 live vertical slices**, not as a hidden prototype sequence followed by a later launch.

The repo reality at the end of **📅 Sprint 0** is:

- the **🧼 archived prototype split** is real
- the **🧱 active rebuild tree** is real
- the **📚 docs / 🧾 ADR / planning / coordination spine** is real
- the **🐙 review, protected-path, and merge enforcement** is real
- the **🐝 agentic harness** is real and currently operates with **11 explicit agents**
- the **🖼️ live frontend shell** is real and deployed
- the **🐍 API**, **🧩 domain**, **📦 worker**, and **🤖 agent** runtimes are still mostly seeded seams rather than a completed live product backend

Because of that repo reality, **📅 Sprint 1** is the first true **live MVP productization sprint**.

By the end of **📅 Sprint 1**, the live system must support:

- **🍽️ async recipe import**
- **✅ edit / review / approval where needed**
- **🔑 auth**
- **🏠 tenancy**
- **🧷 sharing**
- **✏️ diet-aware meal plans**
- **🧃 pantry-aware shopping lists**
- **🤖 AI/LLM recommendations**
- **⛓️ LangChain**
- **🧬 LangGraph**
- **🧬 LangSmith**
- enough **🔍 observability**, **🐙 release control**, and **🚨 kill-switch / degraded-mode** posture to support real users during the sprint

This packet is the merged:

- **📚 spec / requirements packet**
- **👤🎯 team lead packet**
- **🧭 architecture alignment packet**
- **🚢 live-production roadmap packet**

### 1.2 Product Goal

The product goal is to deliver a live system where users can move from:

- **🍽️ recipe discovery**
- to **✅ trusted import**
- to **✏️ diet-aware meal planning**
- to **🧃 pantry-aware shopping**
- to **🤖 AI/LLM guidance and recommendations**

without waiting for the end of the roadmap for those flows to exist.

The MVP is not “some AI somewhere.”  
The MVP is the **full meal-planning core loop** operating on a live system with enough runtime and governance maturity to begin taking on real users.

### 1.3 Core User Flow

The decisive user flow for the rebuild is:

1. user submits a recipe URL
2. the system ingests and parses it asynchronously
3. lower-confidence results can be reviewed or edited
4. approved recipe state becomes available in the planning surface
5. the user generates a diet-aware meal plan
6. pantry state is used to generate a consolidated shopping list
7. the system offers grounded **🤖 AI/LLM** recommendations and explanations tied to recipe, pantry, and plan context

This is the product loop that every early architectural choice should serve.

### 1.4 Packet Purpose

This packet defines, in one place:

- current rebuild status
- actual repo baseline
- product and architecture constraints
- workload and storage assumptions
- governance posture
- active/target repo layout
- adapter catalog
- live MVP scope
- sprint ordering
- acceptance criteria
- non-negotiables

It is intentionally **granular**, **operational**, and **DRY**.  
Where deeper treatment already exists or should exist in repo docs, this packet points to those sections rather than repeating them unnecessarily.

### 1.5 Governing Assumptions

The planning assumptions that now govern the rebuild are:

- **📅 Sprint 0** is treated as completed baseline work
- every later **📅 Sprint** is a live vertical slice
- real users may arrive during the roadmap
- production issue discovery is expected during the rebuild
- **🤖 AI/LLM** must appear in the real product path early
- **🔑 Auth + 🏠 tenancy + 🧷 sharing** must be part of **📅 Sprint 1** to avoid schema and contract rewrites immediately after MVP launch
- **🗄️ DB/data** truth remains separate from firehose-scale **📦 Queue/stream**
- **⚡️ shared cache** remains optional acceleration, not correctness dependency
- every meaningful change still requires **📚 docs** and **🧾 ADR** discipline

### 1.6 Sprint 0 Recap

**📅 Sprint 0** should now be described accurately as:

- a completed **governance + coordination + repo-control + deployed frontend-shell baseline**

It completed:

- **🧼 active vs archived boundary**
- **🧱 active rebuild structure**
- **📚 docs / 🧾 ADR / planning / coordination surfaces**
- **🐝 governed agent harness**
- **🐙 merge-readiness and protected-path enforcement**
- **🐳 Docker + ☸️ Kubernetes parity scaffolding**
- **🖼️ live reviewable frontend shell**

It did **not** complete the live backend product loop.

### 1.7 By The End Of Sprint 1

By the end of **📅 Sprint 1**, Food Run should be a true live MVP with:

- real product API
- real domain model
- real async import flow
- real meal-plan and shopping-list generation
- real auth / tenancy / sharing boundaries
- real grounded **🤖 AI/LLM** flows
- real traces and eval visibility
- real operational visibility for live user traffic

### 1.8 High-Level Planning Overview

The revised roadmap is:

- **✅ 📅 Sprint 0** — completed baseline
- **🚀 📅 Sprint 1** — full live MVP sprint with **🔑 Auth + 🏠 tenancy + 🧷 sharing + 🍽️ core loop + 🤖 AI/LLM hardening**
- **📦 📅 Sprint 2** — async/event hardening and importer resilience
- **⚡️ 📅 Sprint 3** — edge/cache/replicas/hot-key optimization
- **🔥 📅 Sprint 4** — resilience, failover, chaos, broader ramp readiness

That ordering is explained in detail in:
- [9. 📅 Roadmap and Sprint Ordering](#section-9-roadmap-and-sprint-ordering)

---

## Table of Contents

- [1. 🧭 Decisive Summary](#1--decisive-summary)
  - [1.1 TL;DR](#11-tldr)
  - [1.2 Product Goal](#12-product-goal)
  - [1.3 Core User Flow](#13-core-user-flow)
  - [1.4 Packet Purpose](#14-packet-purpose)
  - [1.5 Governing Assumptions](#15-governing-assumptions)
  - [1.6 Sprint 0 Recap](#16-sprint-0-recap)
  - [1.7 By The End Of Sprint 1](#17-by-the-end-of-sprint-1)
  - [1.8 High-Level Planning Overview](#18-high-level-planning-overview)
- [2. 🗺️ Legend and Reading Guide](#2-️-legend-and-reading-guide)
  - [2.1 🗺️ Emoji Legend](#21-️-emoji-legend)
  - [2.2 📖 How to read this packet](#22--how-to-read-this-packet)
- [3. 📌 Packet Intent and Repo-Grounded Baseline](#3--packet-intent-and-repo-grounded-baseline)
  - [3.1 📌 What this packet does](#31--what-this-packet-does)
  - [3.2 🧱 Current rebuild status](#32-️-current-rebuild-status)
  - [3.3 🖼️ What is active versus stubbed at the end of 📅 Sprint 0](#33-️-what-is-active-versus-stubbed-at-the-end-of--sprint-0)
  - [3.4 🧭 Why this revision differs from older planning language](#34--why-this-revision-differs-from-older-planning-language)
- [4. 🎯 Product Model and Delivery Posture](#4--product-model-and-delivery-posture)
  - [4.1 🎯 Live production rebuild goal](#41--live-production-rebuild-goal)
  - [4.2 🤖 What “AI-native” means here](#42--what-ai-native-means-here)
  - [4.3 📅 Vertical-slice delivery rule](#43--vertical-slice-delivery-rule)
  - [4.4 🔍 Live user ramp assumptions](#44--live-user-ramp-assumptions)
- [5. 🏗️ System Shape and Architecture Commitments](#5-️-system-shape-and-architecture-commitments)
  - [5.1 🏗️ Current system shape](#51-️-current-system-shape)
  - [5.2 🧠 Core architecture principles](#52--core-architecture-principles)
  - [5.3 🗄️ Data and storage topology](#53-️-data-and-storage-topology)
  - [5.4 🔁 Request, write, and event strategy](#54--request-write-and-event-strategy)
  - [5.5 📏 Workload, sizing, and five-year scale posture](#55--workload-sizing-and-five-year-scale-posture)
  - [5.6 🔁 Consistency policy](#56--consistency-policy)
  - [5.7 ⚡️ Caching strategy](#57-️-caching-strategy)
- [6. 🐝 Governance, Agentic Harness, and Repo Control](#6--governance-agentic-harness-and-repo-control)
  - [6.1 🔐 Governance model from actual repo docs](#61--governance-model-from-actual-repo-docs)
  - [6.2 🐝 Actual 11-agent harness in the repo](#62--actual-11-agent-harness-in-the-repo)
  - [6.3 🚨 Path control, review, and merge posture](#63--path-control-review-and-merge-posture)
  - [6.4 📚 Docs, coordination, and 🧾 ADR discipline](#64--docs-coordination-and-adr-discipline)
- [7. 🌿 Active / Target Repo Layout](#7--active--target-repo-layout)
  - [7.1 🌿 Layout goals](#71--layout-goals)
  - [7.2 🌿 Active / target layout snapshot](#72--active--target-layout-snapshot)
  - [7.3 Why the layout stays shallow](#73-why-the-layout-stays-shallow)
- [8. 🔌 Adapter Catalog](#8--adapter-catalog)
  - [8.1 Adapter design rule](#81-adapter-design-rule)
  - [8.2 Required ports and adapter surfaces](#82-required-ports-and-adapter-surfaces)
  - [8.3 Default adapters versus later scale adapters](#83-default-adapters-versus-later-scale-adapters)
- [9. 📅 Roadmap and Sprint Ordering](#9--roadmap-and-sprint-ordering)
  - [9.1 ✅ 📅 Sprint 0 — completed baseline](#91---sprint-0--completed-baseline)
  - [9.2 🚀 📅 Sprint 1 — full live MVP sprint](#92---sprint-1--full-live-mvp-sprint)
  - [9.3 📦 📅 Sprint 2 — async/event hardening](#93---sprint-2--asyncevent-hardening)
  - [9.4 ⚡️ 📅 Sprint 3 — edge/cache/replica optimization](#94-️--sprint-3--edgecachereplica-optimization)
  - [9.5 🔥 📅 Sprint 4 — resilience, failover, and broader ramp readiness](#95---sprint-4--resilience-failover-and-broader-ramp-readiness)
- [10. ✅ Acceptance Criteria and Non-Negotiables](#10--acceptance-criteria-and-non-negotiables)
  - [10.1 ✅ End of 📅 Sprint 1 acceptance criteria](#101--end-of--sprint-1-acceptance-criteria)
  - [10.2 ✅ End-of-roadmap acceptance criteria](#102-end-of-roadmap-acceptance-criteria)
  - [10.3 🚨 Non-negotiables](#103--non-negotiables)
- [11. 📎 Appendices and Visuals](#11--appendices-and-visuals)
  - [11.1 Appendix index](#111-appendix-index)

## 11. 📎 Appendices and Visuals

### 11.1 Appendix index

- **Appendix A** — 🌿 Active / target repo layout with comments
- **Appendix B** — 📅 Revised sprint map table
- **Appendix C** — 🍽️ Guaranteed domain acceptance list
- **Appendix D** — ✅ End-of-📅 Sprint 1 acceptance checklist
- **Appendix E** — 🏗️ master macro architecture overview
- **Appendix F** — 🔁 live request / write / async flow
- **Appendix G** — 🍽️🔑🏠🧷🤖 live MVP core-loop diagram
- **Appendix H** — 🔥 degraded-mode and failover posture
- **Appendix I** — 🐝 11-agent governance and delivery flow

---

## 2. 🗺️ Legend and Reading Guide

### 2.1 🗺️ Emoji Legend

#### 2.1.1 👥 People

- 👤🎯 Team Lead — hands-off architecture review, sprint demo review, decision approvals, boundary enforcement
- 👤🎨 FE/Data — Angular UX, generated client usage, cache-first UI, dashboard views, typed frontend integration
- 👤🧰 BE/API — FastAPI contract layer, Django service integration, TDD ownership, contract and integration checks
- 👤👻 AI/Cloud — LangGraph, LangSmith, embeddings, retrieval, provider orchestration, cloud wiring
- 👤🛡️ Platform/QA — Docker, k3s, CI/CD, reliability checks, load validation, rollout safety

#### 2.1.2 📅 Events / Process

- 💠 Standup / async daily update — what changed, what is next, blockers, dependency flags
- 🔶 Contract sync — API schema, generated client, and request/response alignment checkpoint
- 🔐 Merge lock / freeze — branch protection active, risky merges paused
- ✅ QA checkpoint — required checks passed, smoke path confirmed
- 📖 Docs checkpoint — ADR, technical docs, and runbooks updated
- 🎬 Demo checkpoint — scripted rehearsal run before sprint review, visible in sprint review, funding walkthrough, or external stakeholder narrative
- 🚢 Release cut — approved mainline snapshot prepared for deploy
- 🧭 Architecture review — boundary, scale, reliability, and trade-off review with lead

#### 2.1.3 🎟️ Ticket Prefixes / Work Lanes

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
- ✏️ Planning — meal plans, shopping lists, household planning flows
- 🧠 Search/vector — pgvector, retrieval, semantic search, recommendation candidate lookup

#### 2.1.4 ⛳ Markers

- ⚠️ Hotspot — high-churn or high-risk file/path that needs careful review
- 🚨 Alert — security-sensitive, destructive, externally visible, or boundary-breaking change
- 💸 FinOps — anything cost-critical that can spike provider, compute, storage, or CI spend
- 🔥 Chaos Resilience — Ops risks, rollback risk, drift risk, blast radius, failure handling, chaos drills, recovery logic, fallback paths

### 2.2 📖 How to read this packet

#### 2.2.1 What this packet includes

This packet combines:
- product requirements
- architecture commitments
- repo-grounded planning
- governance posture
- roadmap order
- acceptance criteria

#### 2.2.2 What this packet deliberately does not do

This packet does not try to replace:
- deeper implementation docs in `docs/**`
- sprint-specific breakdowns in `docs/planning/**`
- repo-operating rules in `AGENTS.md`
- contribution / governance / trademark / CLA source docs at the repo root

#### 2.2.3 How to use this packet

Use this packet to answer:
- what is already real in the repo?
- what is still stubbed?
- what must **📅 Sprint 1** actually build?
- what assumptions remain fixed across the roadmap?
- what cannot be deferred without breaking the live MVP plan?

---

## 3. 📌 Packet Intent and Repo-Grounded Baseline

### 3.1 📌 What this packet does

#### 3.1.1 Primary function

This packet is the merged source of truth for:
- scope
- architecture
- repo baseline
- planning assumptions
- sprint order
- investor-facing MVP definition

#### 3.1.2 Why this version exists

Older packet language assumed a broader “foundations complete” story than the repo actually shows in the product-runtime layer.

This revision corrects that by distinguishing between:

- **strong governance / docs / harness / repo-control completion**
- versus
- **still-stubbed product runtime and backend execution surfaces**

### 3.2 🧱 Current rebuild status

#### 3.2.1 What is complete at the end of 📅 Sprint 0

The repo shows that **📅 Sprint 0** completed:

- **🧼 archived prototype isolation**
- **🧱 active rebuild structure**
- **📚 technical docs spine**
- **🧾 ADR spine**
- **📚 planning and coordination surfaces**
- **🐝 governed agent harness**
- **🐙 merge-readiness, docs guard, and protected-path enforcement**
- **🐳 Docker + ☸️ Kubernetes parity scaffolding**
- **🖼️ deployed frontend shell**

#### 3.2.2 What is not yet complete at the end of 📅 Sprint 0

The repo also shows that **📅 Sprint 0** did **not** complete:

- live product API
- live domain model
- live async import pipeline
- live shopping-list generation backend
- live recommendation engine
- live **⛓️ LangChain + 🧬 LangGraph + 🧬 LangSmith** runtime integration
- live auth/tenancy/sharing implementation

### 3.3 🖼️ What is active versus stubbed at the end of 📅 Sprint 0

#### 3.3.1 What is active

Active and meaningfully real:
- **🐝 harness**
- **📚 docs / planning / coordination**
- **🐙 repo verification**
- **🖼️ frontend shell**
- **🐳☸️ parity surfaces**
- **🛠️ repo-control scripts**

#### 3.3.2 What is mostly stubbed

Mostly seam-level or ownership-level:
- **🐍 API runtime**
- **🧩 domain runtime**
- **📦 worker runtime**
- **🤖 agent service runtime**

### 3.4 🧭 Why this revision differs from older planning language

The earlier language over-weighted the maturity of the product-runtime surfaces because the repo had already completed a lot of governance and control work.

This revision corrects that by treating **📅 Sprint 1** as:
- the first real productization sprint
- the first real AI-runtime activation sprint
- the first real live MVP sprint

---

## 4. 🎯 Product Model and Delivery Posture

### 4.1 🎯 Live production rebuild goal

#### 4.1.1 Delivery target

The rebuild target is a live production MVP that becomes useful to real users before the roadmap ends.

#### 4.1.2 Why that matters

This means the roadmap is not allowed to postpone:
- user issue discovery
- runtime visibility
- rollback thinking
- kill-switch posture
- operational supportability

until “after launch.”

### 4.2 🤖 What “AI-native” means here

#### 4.2.1 Not a sidecar

“🤖 AI-native” does not mean a later assistant widget or a marketing demo.

#### 4.2.2 Actual meaning in this rebuild

It means the live product loop itself visibly includes:
- **🤖 AI/LLM**
- **🧠 Search/vector**
- **🧬 Graph/Evals**
- grounded import-validation and recommendation logic
- operator-visible traces and evals

### 4.3 📅 Vertical-slice delivery rule

#### 4.3.1 Rule

Every future **📅 Sprint** must leave the live system:
- more useful
- more supportable
- still governable
- still reviewable

#### 4.3.2 Consequence

There are no “throwaway prototype” sprints after **📅 Sprint 0**.

### 4.4 🔍 Live user ramp assumptions

#### 4.4.1 Approved assumption

Investors may begin sending users during **📅 Sprint 1** once **🧃 shopping lists** are operational.

#### 4.4.2 Required consequence

That requires **📅 Sprint 1** to include:
- request IDs
- release markers
- feature flags / kill switches
- import failure visibility
- recommendation-path visibility
- enough operator posture to handle live-user issues during the sprint

---

## 5. 🏗️ System Shape and Architecture Commitments

### 5.1 🏗️ Current system shape

#### 5.1.1 Plane model

The rebuild still uses five conceptual planes:

- **🖼️ experience plane**
- **🐍🧩 product plane**
- **📦 event plane**
- **🐝🤖🧬 agent plane**
- **🔍🐙🔥 operations plane**

#### 5.1.2 Repo-grounded interpretation

At repo reality:
- the **🖼️ experience plane** is the most visibly live
- the **🐝🤖🧬 agent plane** is the most mature in governance/control terms
- the **🐍🧩 product plane** is structurally defined but not fully implemented
- the **📦 event plane** is planned and scaffolded, not yet hard-realized
- the **🔍🐙🔥 operations plane** is stronger in policy/docs than in live product telemetry attachment

### 5.2 🧠 Core architecture principles

#### 5.2.1 🗄️ Truth and scale are separated

- **🗄️ DB/data** truth is durable product state
- **📦 Queue/stream** owns async pressure and replay posture
- raw event volume does not directly rewrite product truth on the hot path

#### 5.2.2 ⚡️ Shared cache is optional acceleration

- local and edge caches can help
- shared cache can help
- correctness must survive without shared cache
- long-tail routes must not inherit unearned caching cost

#### 5.2.3 🔥 Failure is assumed

- parser failures
- queue lag
- fallback usage
- recommendation degradation
- provider degradation
- feature disablement
- partial runtime trouble

All must be considered normal planning cases.

#### 5.2.4 💸 Complexity must keep earning its place

Every new layer must justify:
- runtime value
- product value
- operational value
- cognitive cost
- infra cost

### 5.3 🗄️ Data and storage topology

#### 5.3.1 Durable product truth

**🗄️ DB/data** truth should eventually hold:
- recipe import records
- normalized recipes
- approved recipes
- pantry state
- meal plans
- shopping lists
- recommendation metadata
- prompt/version metadata
- eval metadata
- artifact index
- outbox/idempotency/lock records
- tenancy/auth state once Sprint 1 lands

#### 5.3.2 Artifact and blob surfaces

**☁️ Cloud** or blob-like storage remains for:
- images
- reports
- artifacts
- export bundles
- optional diagnostic outputs

#### 5.3.3 Read-model and projection posture

Read models, projections, and recommendation tables may exist later, but:
- they do not replace truth
- they do not remove the need for domain correctness
- they should be justified route by route

### 5.4 🔁 Request, write, and event strategy

#### 5.4.1 Interactive request strategy

Interactive requests should:
- enter through **🖼️ UI/UX**
- flow through one public contract
- remain observable
- preserve request correlation

#### 5.4.2 Product write strategy

Product writes should:
- validate at the **🐍 FastAPI** boundary
- execute through **🧩 Django** services
- commit durable state
- safely fan out async work after correctness is established

#### 5.4.3 Async/event strategy

The event posture should support:
- import stages
- retries
- replay
- reduction
- async enrichments
- recommendation preparation as needed

### 5.5 📏 Workload, sizing, and five-year scale posture

#### 5.5.1 Interactive request posture

The rebuild still assumes meaningful interactive traffic and later burst pressure.

#### 5.5.2 Product write posture

The live MVP must support meaningful product writes around:
- imports
- approvals
- plans
- lists
- auth/session
- tenancy/sharing state

#### 5.5.3 Raw event posture

The long-range architecture still assumes raw event pressure can outgrow product-truth write capacity, which is why **📦 Queue/stream** remains a first-class design element.

#### 5.5.4 Five-year scale planning rule

The packet still preserves the original large-scale honesty:
- hot truth ≠ firehose sink
- replay and reduction matter
- caches are optional
- scale hardening happens after the first live loop, not before it

### 5.6 🔁 Consistency policy

#### 5.6.1 Stronger consistency areas

These require stronger consistency:
- **🔑 Auth**
- **🏠 tenancy**
- **🧷 sharing / role changes**
- recipe approval
- pantry edits
- meal-plan writes
- shopping-list writes
- outbox / idempotency / lock records

#### 5.6.2 Eventual consistency areas

These can tolerate bounded eventual consistency later:
- some recommendation views
- some dashboards
- some derived projections
- some read-most optimization layers

### 5.7 ⚡️ Caching strategy

#### 5.7.1 Early posture

Early caching should focus on:
- client-side benefit
- edge/read-most benefit
- not overcomplicating Sprint 1

#### 5.7.2 Hard rule

No cache decision should create correctness dependency or schema design assumptions that have to be rewritten immediately after the live MVP lands.

---

## 6. 🐝 Governance, Agentic Harness, and Repo Control

### 6.1 🔐 Governance model from actual repo docs

#### 6.1.1 Project scope

The actual repo governance documents describe Food Run CE as the public Community Edition repository.

#### 6.1.2 Authority structure

The actual repo governance posture is:
- **Project Owner** retains ultimate authority
- **Maintainers** govern day-to-day repository operations
- **Contributors** do not gain roadmap authority by contribution alone

#### 6.1.3 Legal / policy posture

The actual repo docs also define:
- **AGPLv3-or-later** licensing posture in `CONTRIBUTING.md`
- contributor obligations through `CLA.md`
- trademark boundaries through `TRADEMARKS.md`
- governance boundaries through `GOVERNANCE.md`
- security reporting posture through `SECURITY.md`

This packet does not override those files.  
It aligns roadmap and architecture planning to them.

### 6.2 🐝 Actual 11-agent harness in the repo

#### 6.2.1 Repo-grounded agent list

The actual `.opencode/agents/` surface includes 11 agents:

- `pm`
- `reporter`
- `architect`
- `designer`
- `developer`
- `reviewer`
- `integrator`
- `ops`
- `librarian`
- `planner`
- `scout`

#### 6.2.2 Harness interpretation

The real harness is best understood as:

- **🐝 orchestration**
  - `pm`
  - `reporter`

- **🐝 planning / discovery**
  - `scout`
  - `planner`
  - `architect`

- **🐝 implementation**
  - `developer`
  - `designer`

- **🐝 review / closeout / runtime scrutiny**
  - `reviewer`
  - `integrator`
  - `ops`
  - `librarian`

#### 6.2.3 Why this matters to the roadmap

Because the harness is already mature, **📅 Sprint 1** should not spend energy reinventing agent governance.  
It should spend energy attaching that governance to real product and AI runtime work.

### 6.3 🚨 Path control, review, and merge posture

#### 6.3.1 Current reality

The repo already has:
- protected-path enforcement
- docs guards
- repo verification
- PR template discipline
- CLA check
- frontend quality checks

#### 6.3.2 Roadmap implication

This means later sprints should leverage the existing control plane rather than restating it as if it still needs to be invented.

### 6.4 📚 Docs, coordination, and 🧾 ADR discipline

#### 6.4.1 Current reality

The repo already contains:
- `docs/coordination/**`
- `docs/planning/**`
- `docs/adr.md`
- architecture and operations docs
- agent workflow docs

#### 6.4.2 Roadmap implication

The roadmap must treat:
- **📚 docs**
- **🧾 ADR**
- coordination packets
- repo-control docs

as active production surfaces, not side documentation.

---

## 7. 🌿 Active / Target Repo Layout

### 7.1 🌿 Layout goals

The active/target layout should continue to optimize for:
- shallow ownership
- one home per concept
- clear deployable-unit boundaries
- clear seam boundaries
- readable path sensitivity
- compatibility with the existing repo-control surfaces

### 7.2 🌿 Active / target layout snapshot

See:
- **Appendix A** for the detailed tree with purpose comments for every listed file/folder below the root

### 7.3 Why the layout stays shallow

The layout remains intentionally shallow because:
- the harness needs obvious routing
- humans need obvious ownership
- protected-path reasoning should not require archaeology
- schema and contract changes should not splinter into parallel homes

---

## 8. 🔌 Adapter Catalog

### 8.1 Adapter design rule

Adapter seams should remain:
- narrow
- capability-based
- swappable
- explicit
- cheap to reason about
- hard to misuse

### 8.2 Required ports and adapter surfaces

See:
- **Appendix A** for repo placement
- this section for the port list with descriptions

#### 8.2.1 `LLMProvider`
Purpose:
- abstract model invocation for product **🤖 AI/LLM** flows and possibly some governed internal agent/runtime surfaces

#### 8.2.2 `EmbeddingProvider`
Purpose:
- abstract embedding generation for **🧠 Search/vector** and grounded retrieval flows

#### 8.2.3 `VectorStore`
Purpose:
- abstract vector persistence/retrieval for recommendation and retrieval use cases

#### 8.2.4 `LocalCache`
Purpose:
- provide process-local or request-local caching where route-level benefit exists without introducing distributed dependency

#### 8.2.5 `SharedCache`
Purpose:
- provide optional distributed cache behavior when justified by route economics and invalidation ownership

#### 8.2.6 `BlobStore`
Purpose:
- handle binary or artifact-like storage outside product truth tables

#### 8.2.7 `JobQueue`
Purpose:
- enqueue and consume async tasks for imports, enrichments, reductions, and later recommendation preparation

#### 8.2.8 `StreamLog`
Purpose:
- provide append/replay semantics for event-style flows that outgrow simple job semantics

#### 8.2.9 `IdentityProvider`
Purpose:
- abstract login / identity source behavior for **🔑 Auth**

#### 8.2.10 `SessionProvider`
Purpose:
- abstract session or token/session lifecycle behavior independent of the chosen identity source

#### 8.2.11 `MetricSink`
Purpose:
- emit metrics to the chosen observability backend

#### 8.2.12 `TraceSink`
Purpose:
- emit traces and run-level observability data, including AI-workflow trace surfaces where applicable

#### 8.2.13 `LogSink`
Purpose:
- emit structured logs to the chosen logging backend or runtime sink

#### 8.2.14 `FeatureFlagProvider`
Purpose:
- gate risky paths, AI behavior, or rollout decisions without requiring redeploy-first mitigation

#### 8.2.15 `IdempotencyStore`
Purpose:
- preserve idempotent semantics for retries, async work, and protected write flows

#### 8.2.16 `LockStore`
Purpose:
- coordinate critical sections where optimistic concurrency is not sufficient

#### 8.2.17 `RateStore`
Purpose:
- support rate limiting / quota semantics where runtime protection is needed

#### 8.2.18 `SearchStore`
Purpose:
- support non-vector search or indexed lookup capabilities where product flows need them

#### 8.2.19 `Clock`
Purpose:
- centralize time semantics for testing, replay reasoning, and deterministic control

#### 8.2.20 `OutboxStore`
Purpose:
- preserve safe post-commit fan-out semantics from truth mutation into async processing

### 8.3 Default adapters versus later scale adapters

#### 8.3.1 Default adapters

Early adapters should prefer:
- lower cost
- lower complexity
- development speed
- deterministic local behavior where possible

#### 8.3.2 Later scale adapters

Later scale-oriented swaps may include:
- distributed caches
- stronger queue/stream infrastructure
- stronger vector/search infrastructure
- broader edge/CDN infrastructure

But those should not force schema or contract rewrites immediately after **📅 Sprint 1**.

---

## 9. 📅 Roadmap and Sprint Ordering

### 9.1 ✅ 📅 Sprint 0 — completed baseline

#### 9.1.1 What it completed

**📅 Sprint 0** completed:
- repo boundary reset
- active rebuild tree
- docs/ADR/planning/coordination spine
- 11-agent harness and repo-control alignment
- merge/readiness enforcement
- runtime parity scaffolding
- deployed frontend shell

#### 9.1.2 What it intentionally did not complete

It did not complete:
- live MVP backend
- auth / tenancy / sharing
- import pipeline
- meal-plan engine
- shopping-list engine
- recommendation runtime
- LangChain / LangGraph / LangSmith integration

### 9.2 🚀 📅 Sprint 1 — full live MVP sprint

#### 9.2.1 Why this is a full MVP sprint now

Because **🔑 Auth + 🏠 tenancy + 🧷 sharing** need to be part of the MVP to avoid:
- multiple schema versions
- contract rewrites between Sprint 1 and Sprint 2
- recommendation-context redesign immediately after the first live loop

#### 9.2.2 What Sprint 1 must deliver

**📅 Sprint 1** must deliver, on a live system:

- **🐍 FastAPI** runtime activation
- **🧩 Django** domain model activation
- **📦 async import pipeline**
- **🍽️ 6 guaranteed domains**
- **🌐 generic fallback**
- **✅ edit / review / approval path**
- **🔑 auth**
- **🏠 tenancy**
- **🧷 sharing**
- **✏️ diet-aware meal plans**
- **🧃 pantry-aware shopping lists**
- **🤖 AI/LLM recommendations**
- **⛓️ LangChain**
- **🧬 LangGraph**
- **🧬 LangSmith**
- enough **🔍 observability** and **🐙 release control** for real users

#### 9.2.3 Why this is still one sprint in the packet

Because the repo already completed so much control-plane work in **📅 Sprint 0** that the first major remaining step is product-runtime activation, not repo-governance invention.

### 9.3 📦 📅 Sprint 2 — async/event hardening

After the MVP is live, **📅 Sprint 2** should harden:
- import reliability
- retry behavior
- replay posture
- dead-letter semantics
- queue safety
- async reduction and event discipline

### 9.4 ⚡️ 📅 Sprint 3 — edge/cache/replica optimization

After the MVP is live and async/event posture is improved, **📅 Sprint 3** should optimize:
- **🌐 Edge**
- **⚡️ cache strategy**
- replica usage
- hot-key defense
- long-tail route economics

### 9.5 🔥 📅 Sprint 4 — resilience, failover, and broader ramp readiness

Once the live MVP and its supporting runtimes are stable, **📅 Sprint 4** should harden:
- failover posture
- degraded modes
- chaos drills
- broader investor/user ramp readiness

---

## 10. ✅ Acceptance Criteria and Non-Negotiables

### 10.1 ✅ End of 📅 Sprint 1 acceptance criteria

#### 10.1.1 MVP flow acceptance

By end of **📅 Sprint 1**, the live system must:
- accept recipe URLs
- ingest asynchronously
- support the 6 guaranteed domains
- support fallback
- support review/edit/approval where needed
- generate diet-aware meal plans
- generate pantry-aware shopping lists
- provide recommendations

#### 10.1.2 Identity / sharing acceptance

By end of **📅 Sprint 1**, the live system must also include:
- real auth
- tenancy-aware data model
- sharing / household-aware product behavior
- schema and contract choices stable enough to avoid immediate Sprint 2 rewrite

#### 10.1.3 AI and observability acceptance

By end of **📅 Sprint 1**, the live system must visibly use:
- **⛓️ LangChain**
- **🧬 LangGraph**
- **🧬 LangSmith**

And must also support:
- request IDs
- release markers
- import failure visibility
- feature-flag / kill-switch posture
- enough live triage support for investor-sent traffic

### 10.2 ✅ End-of-roadmap acceptance criteria

By the end of the revised roadmap, the system must:
- remain live and supportable
- preserve correctness under broader usage
- harden async/event behavior
- harden scale posture
- harden resilience/failover posture
- preserve governed AI and governed delivery discipline

### 10.3 🚨 Non-negotiables

- **📅 Sprint 0** is treated as completed baseline
- **📅 Sprint 1** is the full live MVP sprint
- **🔑 Auth + 🏠 tenancy + 🧷 sharing** are part of **📅 Sprint 1**
- **🤖 AI/LLM** must appear in the real product path early
- **🗄️ DB/data** truth is not the firehose sink
- **📦 Queue/stream** remains first-class for async scale
- **⚡️ shared cache** remains optional acceleration
- **📚 docs** and **🧾 ADR** updates are part of completion
- protected paths remain gated
- degraded modes must be explicit
- the roadmap remains live-production-first, not prototype-first

## 

### Appendix A — 🌿 Active / target repo layout with comments

```
food-run-ce/
│ 
├── AGENTS.md                              # root operating contract for governed human + 🐝 agent work
├── README.md                              # public project overview, navigation, and high-level live rebuild framing
├── CONTRIBUTING.md                        # contributor workflow, contribution boundaries, and PR expectations
├── CLA.md                                 # contributor license agreement terms for accepted contributions
├── GOVERNANCE.md                          # formal CE governance model: Project Owner, maintainers, decision boundaries
├── TRADEMARKS.md                          # trademark and branding-use boundaries for Food Run CE
├── SECURITY.md                            # security reporting and disclosure posture for the repository
├── LICENSE.md                             # repository license terms
├── NOTICE.md                              # attribution / notice surface where required
├── .env.example                           # canonical environment-variable shape for local/runtime setup
├── .gitignore                             # ignored local/runtime/build artifacts
├── bunfig.toml                            # Bun behavior/config where used in JS/TS workflow
├── bun.lock                               # Bun dependency lockfile
├── pyproject.toml                         # Python project metadata and dependency/tooling configuration
├── uv.lock                                # Python dependency lockfile for reproducible environments
├── ruff.toml                              # Python lint/format rule configuration
├── biome.jsonc                            # JS/TS formatting/lint configuration
├── opencode.json                          # project-level OpenCode entry configuration / default agent routing
│ 
├── .github/
│   ├── pull_request_template.md           # required PR structure for summary, verification, docs, and protected-path visibility
│   └── workflows/
│       ├── repo-verify.yml                # repo-level merge-readiness checks driven by tooling scripts
│       ├── docs-guard.yml                 # docs / 🧾 ADR parity enforcement on qualifying changes
│       ├── protected-paths.yml            # protected-path detection and escalation workflow
│       ├── frontend-quality.yml           # frontend lint / quality / smoke-oriented checks
│       ├── web-pages.yml                  # GitHub Pages deployment workflow for the live web shell
│       ├── cla-check.yml                  # CLA phrase / policy enforcement on PRs
│       └── cd.yml                         # release-prep / post-merge delivery scaffold, not full deploy maturity yet
│ 
├── .opencode/
│   ├── package.json                       # local OpenCode package/runtime metadata for harness support
│   ├── bun.lock                           # lockfile for `.opencode/` package dependencies
│   ├── .gitignore                         # ignore file specific to local harness/package artifacts
│   ├── agents/
│   │   ├── pm.md                          # orchestration hub agent that routes and coordinates scoped work
│   │   ├── reporter.md                    # normalized status / packet / heartbeat emitter for coordination clarity
│   │   ├── architect.md                   # architecture-first planning and invariant-shaping agent before implementation
│   │   ├── designer.md                    # UI/UX implementation-oriented agent for visual and interface work
│   │   ├── developer.md                   # bounded implementation agent for code-bearing changes
│   │   ├── reviewer.md                    # review gate agent for reuse, conventions, and plausible-but-dangerous output
│   │   ├── integrator.md                  # cross-surface fit-check agent for smoke-path and system-level consistency
│   │   ├── ops.md                         # runtime / operational scrutiny agent for blast radius and supportability
│   │   ├── librarian.md                   # durable docs / closeout / knowledge-preservation agent
│   │   ├── planner.md                     # planning decomposition agent for bounded work packets
│   │   └── scout.md                       # discovery / reuse / repo-mapping agent before implementation begins
│   ├── commands/
│   │   ├── kickoff.md                     # work-start ritual and initialization command guidance
│   │   ├── orchestrate.md                 # orchestration command for multi-agent routing and control
│   │   ├── plan-work.md                   # planning command for decomposing scoped work
│   │   ├── split-work.md                  # parallelization guidance for dividing work safely
│   │   ├── start-task.md                  # task-start helper for bounded implementation flow
│   │   ├── checkpoint-commit.md           # small-slice checkpoint commit rhythm guidance
│   │   ├── verify-change.md               # verification command for merge-readiness checks
│   │   ├── docs-sync.md                   # docs synchronization command for keeping repo theory current
│   │   ├── adr-delta.md                   # ADR delta generation/update command
│   │   ├── pr-prepare.md                  # PR-prep command to normalize merge-ready packet content
│   │   ├── close-scope.md                 # scope-closeout command to ensure docs / review / verification completion
│   │   ├── handoff.md                     # coordination handoff command between lanes or humans
│   │   ├── sync-status.md                 # active coordination/status refresh command
│   │   ├── scout.md                       # scout-specific command entry for discovery sweeps
│   │   └── generate.md                    # generation helper for bounded artifact creation
│   ├── rules/
│   │   ├── README.md                      # index/readme for repo-specific harness rules
│   │   ├── implementation-standards.md    # coding, reuse, and implementation boundary standards
│   │   ├── coordination-standards.md      # coordination-state and packet standards for live parallel work
│   │   └── master-packet-alignment.md     # rule for aligning repo behavior to the approved master packet
│   └── skills/
│       ├── active-vs-legacy/         # skill pack for distinguishing archived prototype from active rebuild work
│       ├── async-splitting/          # skill pack for safely parallelizing work across async lanes
│       ├── coordination-handoff/     # skill pack for clean lane-to-lane or human handoffs
│       ├── coordination-state/       # skill pack for maintaining current coordination state and status hygiene
│       ├── docs-and-adr/             # skill pack for docs and ADR updates as part of completion
│       ├── drift-check/              # skill pack for catching repo drift and stale packet assumptions
│       ├── micro-commit-rhythm/      # skill pack for granular commit cadence
│       ├── parallel-lane-policy/     # skill pack for safe multi-lane agent execution
│       ├── planning-reader/          # skill pack for reading current sprint/deliverable docs correctly
│       ├── protected-paths/          # skill pack for path sensitivity and escalation behavior
│       ├── release-safety/           # skill pack for release-aware changes and rollback thinking
│       ├── repo-map/                 # skill pack for active path placement and ownership lookup
│       ├── review-rubric/            # skill pack for review questions and reject conditions
│       ├── scope-router/             # skill pack for routing tasks to the correct lane/surface
│       └── tdd-loop/                 # skill pack for test-first or verify-first execution rhythm
│ 
├── apps/
│   ├── web/
│   │   ├── angular.json              # Angular workspace/build configuration for the live frontend shell
│   │   ├── package.json              # frontend package/runtime manifest
│   │   ├── tsconfig.json             # frontend TypeScript compiler settings
│   │   └── src/                      # live web source root
│   │       ├── main.ts               # frontend bootstrap entrypoint
│   │       └── app/                  # routed UI shell and product-page source surface
│   ├── api/
│   │   ├── main.py                   # public API runtime entry seam
│   │   ├── routes.py                 # public route registry seam
│   │   ├── middleware.py             # request-scoped middleware seam for IDs, envelopes, telemetry hooks
│   │   └── schemas.py                # API request/response schema seam
│   ├── domain/
│   │   ├── manage.py                 # domain-side management entry seam
│   │   ├── config.py                 # domain runtime configuration seam
│   │   ├── models.py                 # durable product-truth model seam
│   │   ├── services.py               # business-rule and transaction service seam
│   │   ├── auth.py                   # domain auth / role / scope seam
│   │   └── migrate/                  # future migration surface for schema evolution
│   ├── worker/
│   │   ├── main.py                   # async worker runtime entry seam
│   │   ├── jobs.py                   # job registration and handler seam
│   │   ├── queue.py                  # queue client / consume / enqueue seam
│   │   └── retry.py                  # retry and poison-handling seam
│   └── agent/
│       ├── main.py                   # product-AI / governed agent runtime entry seam
│       ├── graph.py                  # LangGraph workflow seam
│       ├── evals.py                  # eval runner / scoring seam
│       └── store.py                  # artifact / run / eval persistence seam
│ 
├── shared/
│   ├── contract/
│   │   ├── http.py                   # shared HTTP contract helpers and envelope vocabulary
│   │   ├── errors.py                 # shared public error-shape vocabulary
│   │   └── version.py                # shared version/header vocabulary
│   ├── schema/
│   │   ├── common.py                 # shared non-domain-specific common shapes
│   │   ├── events.py                 # shared event-envelope and event-shape vocabulary
│   │   └── auth.py                   # shared auth / actor / session shape vocabulary
│   ├── adapter/
│   │   ├── ports.py                  # adapter port definitions for swappable dependencies
│   │   ├── factory.py                # adapter selection / assembly helpers
│   │   ├── cache.py                  # cache adapter seam helpers
│   │   ├── queue.py                  # queue/stream adapter seam helpers
│   │   └── store.py                  # blob/artifact/auxiliary storage adapter seam helpers
│   └── testkit/
│       ├── __init__.py               # package initializer for shared test support
│       ├── fixtures.py               # shared deterministic fixture builders
│       ├── factory.py                # reusable test-object factory surface
│       ├── helpers.py                # common test helper utilities
│       ├── case.py                   # shared case-definition helper surface
│       ├── workflows.py              # reusable workflow-oriented test helpers
│       ├── unit/                     # unit-test shared support area
│       ├── integration/              # integration-test shared support area
│       ├── component/                # component/frontend shared support area
│       ├── e2e/                      # end-to-end shared support area
│       └── ui/                       # UI-specific shared testing support
│ 
├── platform/
│   ├── docker/
│   │   ├── web.Dockerfile            # web runtime container packaging surface
│   │   ├── api.Dockerfile            # API runtime container packaging surface
│   │   ├── worker.Dockerfile         # worker runtime container packaging surface
│   │   └── agent.Dockerfile          # agent runtime container packaging surface
│   ├── k8s/
│   │   ├── web.yaml                  # web local-cluster manifest surface
│   │   ├── api.yaml                  # API local-cluster manifest surface
│   │   ├── worker.yaml               # worker local-cluster manifest surface
│   │   ├── agent.yaml                # agent local-cluster manifest surface
│   │   └── migrate.yaml              # one-off migration job manifest surface
│   ├── edge/
│   │   ├── cache.yaml                # edge/cache policy vocabulary surface
│   │   ├── gateway.yaml              # gateway / request-shaping vocabulary surface
│   │   └── limits.yaml               # request-size / burst / safety limit vocabulary surface
│   └── infra/
│       ├── main.tf                   # infra-definition entry surface for future managed resources
│       ├── variables.tf              # infra input variable definitions
│       └── outputs.tf                # infra output surface for later environment wiring
│ 
├── tools/
│   ├── chaos/
│   │   └── checks.py                 # early chaos/resilience helper surface
│   ├── eval/
│   │   └── runner.py                 # eval tooling runner surface
│   ├── load/
│   │   └── ingest.py                 # load tool surface for ingestion/load-oriented checks
│   └── scripts/
│       ├── __init__.py               # package initializer for repo tooling scripts
│       ├── verify.py                 # repo verification / merge-readiness entrypoint
│       ├── release.py                # release-preparation / release-marker helper entrypoint
│       ├── dev.py                    # local runtime / parity helper entrypoint
│       ├── frontend.py               # frontend workflow helper surface
│       ├── coordination.py           # coordination-state / packet helper surface
│       └── hooks.py                  # shared script-hook helper surface
│ 
├── docs/
│   ├── adr.md                        # single evolving architecture decision record
│   ├── architecture.md               # system architecture / diagrams / boundary posture doc
│   ├── repo.md                       # repo layout rules, active-vs-archived guidance, and ownership doc
│   ├── agent.md                      # governed agent workflow and harness explanation
│   ├── testing.md                    # testing + verification posture doc
│   ├── operations.md                 # operator-facing runtime and release expectations doc
│   ├── observability.md              # baseline metrics / logs / traces / release-marker posture doc
│   ├── resilience.md                 # degraded mode / failover / local parity posture doc
│   ├── legacy-v0.md                  # explanation of archived prototype value and extraction rules
│   ├── coordination/                 # live coordination state, handoffs, notes, and checkpoints
│   ├── planning/                     # sprint, deliverable, and packet planning surfaces
│   └── templates/                    # reusable docs/coordination template surface
│ 
└── legacy-v0/
    ├── README.md                     # archived prototype guide and extraction warning surface
    ├── client/                       # preserved prototype frontend implementation
    ├── server/                       # preserved prototype backend implementation
    └── docs/                         # preserved prototype docs/assets
```


### Appendix B — 📅 Revised sprint map table

```
| 📅 Sprint | Title | Primary Goal | Repo-Reality Reason | Live User Posture | Main Outcome |
|---|---|---|---|---|---|
| ✅ 📅 Sprint 0 | 🧼🧱📚🐝🐙🐳☸️🖼️ Completed Baseline | Complete governance, harness, docs, repo control, parity scaffolding, and deployed shell | Already reflected in repo | Live reviewable shell already exists | Strong repo-control baseline, but backend/runtime product loop still mostly stubbed |
| 🚀 📅 Sprint 1 | 🔑🏠🧷🍽️✏️🧃🤖🧬⛓️ Full Live MVP Sprint | Turn seeded seams into a real live MVP with auth, tenancy, sharing, core loop, and AI hardening | Needed because product runtime is still mostly unimplemented | Investors may begin sending users once the shopping-list loop is stable | Live async recipe→plan→list→recommendation MVP with real identity and AI runtime |
| 📦 📅 Sprint 2 | 🗄️📦🧪 Async/Event Hardening | Harden import reliability, replay, retries, poison handling, and importer resilience | MVP will already be live; async runtime needs hardening next | Active production hardening | Stronger queue/event discipline and importer reliability |
| ⚡️ 📅 Sprint 3 | 🌐⚡️🔍🔥 Edge/Cache/Replica Optimization | Optimize latency/cost based on real usage patterns | Better done after live usage reveals route economics | Broader traffic support | Adaptive caching, replica use, hot-key defense, route-level optimization |
| 🔥 📅 Sprint 4 | ☁️🚢🧭 Resilience, Failover, Broader Ramp Readiness | Harden degraded modes, failover, and chaos posture for broader user ramp | Best done after MVP and runtime patterns stabilize | Larger investor/user ramp readiness | Stronger resilience, failover, and operational trust under wider production exposure |
```


### Appendix C — 🍽️ Guaranteed domain acceptance list

```
## 🍽️ Guaranteed Domain Acceptance List

The following domains are guaranteed ingestion targets for the live MVP in **📅 Sprint 1**:

1. `joshuaweissman.com`
2. `simplyrecipes.com`
3. `allrecipes.com`
4. `delish.com`
5. `epicurious.com`
6. `livingchirpy.com`

### 🌐 Generic fallback requirement

In addition to the six guaranteed domains, the live MVP must include a **🌐 generic fallback** ingestion path that supports best-effort extraction for non-guaranteed domains.

### ✅ Acceptance intent for each guaranteed domain

For each guaranteed domain, **📅 Sprint 1** should support:

- **🍽️ async fetch**
- **🍽️ extraction / parse / normalize**
- **✅ review / edit / approval** where needed
- handoff into **✏️ diet-aware planning**
- handoff into **🧃 pantry-aware shopping**
- enough **🔍 observability** to classify and debug failures

### 🚨 Important planning note

These six guaranteed domains are not a side requirement.  
They are a first-class **🍽️ Recipes** reliability workstream in **📅 Sprint 1** because the active repo does not yet contain the new-runtime parser implementations.
```


### Appendix D — ✅ End-of-📅 Sprint 1 acceptance checklist

```
## ✅ End-of-📅 Sprint 1 Acceptance Checklist

### 🔑 Auth / 🏠 Tenancy / 🧷 Sharing
- [ ] Real **🔑 Auth** flow exists
- [ ] Real **🏠 tenancy** model exists in the active runtime
- [ ] Real **🧷 sharing / household-aware** behavior exists where required by MVP flows
- [ ] The schema and contract are stable enough that **📅 Sprint 2** does not need immediate identity-model rewrites

### 🍽️ Recipe Import
- [ ] URL submission works on the live system
- [ ] Import runs asynchronously through the active runtime
- [ ] All 6 guaranteed domains are vetted
- [ ] **🌐 generic fallback** exists
- [ ] Import failures are visible to operators

### ✅ Review / Edit / Approval
- [ ] Lower-confidence or fallback outputs can be reviewed
- [ ] Users or operators can edit where needed
- [ ] Approved recipe state becomes usable by the rest of the MVP loop

### ✏️ Diet-Aware Meal Planning
- [ ] Diet-aware plan generation works from live recipe state
- [ ] Planning logic is wired to the active runtime, not only the frontend shell
- [ ] Plan outputs are visible in the live UI

### 🧃 Pantry-Aware Shopping Lists
- [ ] Pantry-aware shopping list generation works
- [ ] The consolidated list is usable enough for live users
- [ ] Investors can begin sending users once this surface is operationally supportable

### 🤖 AI-Native Runtime
- [ ] **⛓️ LangChain** is used in the live MVP AI stack where it actually reduces integration friction
- [ ] **🧬 LangGraph** orchestrates live product workflows
- [ ] **🧬 LangSmith** traces / eval hooks are visible for the live MVP
- [ ] **🤖 AI/LLM** behavior is in the actual user path, not hidden internally

### 🔍 Production Safety
- [ ] Request IDs exist on MVP core flows
- [ ] **🚢 release markers** exist
- [ ] Import failures, async failures, and recommendation issues are triageable
- [ ] Risky **🤖 AI/LLM** paths can be feature-flagged or disabled
- [ ] The team can support live user issue discovery during the sprint
```


### Appendix E — 🏗️ master macro architecture overview

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ FOOD RUN — 🏗️ MASTER MACRO OVERVIEW                                                          │
│    🖼️ experience is live • 🐝 governance is mature • 📦 event hardening follows MVP         │
│               • 🐍🧩 product runtime is next major activation                                │
└──────────────────────────────────────────────────────────────────────────────────────┘


                            USERS / INVESTORS / REVIEWERS / OPERATORS
                                                │
                                                ▼
┌─────────────────────────────  🖼️ EXPERIENCE PLANE  ────────────────────────────────────┐
│ apps/web live shell -> route surfaces -> real MVP flow host                                   │
│      - current reality: most concretely live user-facing surface in the repo                  │
└───────────────────────────────────────────┬──────────────────────────────────────────┘
                                                │
                                                ▼
┌────────────────────────────────  🐍🧩 PRODUCT PLANE  ─────────────────────────────────┐
│ 🐍 FastAPI seam -> 🧩 Django seam -> 🗄️ durable product truth                                │
│      - current reality: structurally defined, mostly still stubbed                            │
│      - Sprint 1 mission: activate as real live MVP backend                                    │
└───────────────────────────────────────────┬──────────────────────────────────────────┘
                                                │
                                                ▼
┌───────────────────────────────────  📦 EVENT PLANE  ───────────────────────────────────┐
│ async import -> retries -> replay -> reduction -> recommendation preparation                  │
│      - current reality: planned and scaffolded, not yet deeply realized                       │
│      - Sprint 2 mission: harden after live MVP activation                                     │
└───────────────────────────────────────────┬──────────────────────────────────────────┘
                                                │
                                                ▼
┌─────────────────────────────────  🐝🤖🧬 AGENT PLANE  ─────────────────────────────────┐
│ AGENTS.md -> 11-agent harness -> coordination docs -> traces / eval surfaces                   │
│      - current reality: governance and planning maturity are ahead of product-runtime          │
│        maturity                                                                                │
└───────────────────────────────────────────┬───────────────────────────────────────────┘
                                                │
                                                ▼
┌─────────────────────────────── 🔍🐙🔥 OPERATIONS PLANE ─────────────────────────────────┐
│   repo verification  -->  docs guard  -->  protected paths  -->  request IDs / release          │
│   markers / degraded-mode posture                                                               │
│      - current reality: control plane is seeded and partially real; Sprint 1 must attach it     │
│        to live product behavior                                                                 │
└────────────────────────────────────────────────────────────────────────────────────────┘
```


### Appendix F — 🔁 live request / write / async flow 

```
┌─────────────────────────────────────────────────────────────────────────┐
│ FOOD RUN — 🔁 LIVE REQUEST / WRITE / ASYNC FLOW                                │
│   - what the active repo is trying to become by the end of 📅 Sprint 1         │
└─────────────────────────────────────────────────────────────────────────┘


USER ACTION
  │
  ├── 🍽️ submit recipe URL
  ├── ✅ review imported result
  ├── ✏️ generate meal plan
  ├── 🧃 generate shopping list
  └── 🤖 request recommendation
  │
  ▼
🖼️ apps/web
  │
  ├── live routed shell
  ├── request initiation
  └── user-visible states
  │
  ▼
🐍 FastAPI
  │
  ├── request validation
  ├── request id / release context
  ├── 🔑 auth / 🏠 tenancy / 🧷 sharing context
  └── route to domain / async seams
  │
  ▼
🧩 domain services
  │
  ├── durable truth mutation
  ├── approval logic
  ├── planning logic
  ├── shopping-list logic
  └── recommendation entry logic
  │
  ├───  synchronous durable write ────► 🗄️ DB/data truth
  │
  └───  async follow-on work  ────────► 📦 queue / worker jobs
          │
          ▼
          │
          ├── import stages
          ├── retries
          ├── reductions
          └── recommendation preparation
          │
          ▼
          🤖 agent runtime / 🧬 workflow layer
          │
          ├── ⛓️ LangChain helpers
          ├── 🧬 LangGraph orchestration
          └── 🧬 LangSmith traces / eval hooks
```


### Appendix G — 🍽️🔑🏠🧷🤖 live MVP core-loop diagram

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────────┐
│    FOOD RUN — 🍽️🔑🏠🧷🤖 LIVE MVP CORE LOOP                                                                  │
│      - full MVP loop required by the end of 📅 Sprint 1                                                        │
└──────────────────────────────────────────────────────────────────────────────────────────────────────┘


1. 🔑 AUTH + 🏠 TENANCY + 🧷 SHARING CONTEXT
   establish who the user is, which tenant/household scope they act in, and what product state they can affect
        │
        ▼

2. 🍽️ ASYNC RECIPE IMPORT
   user submits URL  -->  system fetches, extracts, parses, normalizes
        │
        ├── 6 guaranteed domains
        └── 🌐 generic fallback
        │
        ▼

3. ✅ REVIEW / EDIT / APPROVAL
   lower-confidence results can be corrected and approved before becoming trusted product state
        │
        ▼

4. ✏️ DIET-AWARE MEAL PLAN
   approved recipes become candidates for plan generation under dietary constraints
        │
        ▼

5. 🧃 PANTRY-AWARE SHOPPING LIST
   pantry state is used to subtract what already exists and build a consolidated list
        │
        ▼

6. 🤖 AI/LLM RECOMMENDATIONS
   recommendations operate on recipe / pantry / plan context
        │
        ├── ⛓️ LangChain integration primitives
        ├── 🧬 LangGraph workflow control
        └── 🧬 LangSmith traces and eval visibility
        │
        ▼

7. 🔍 LIVE SUPPORTABILITY
   request ids, release markers, route visibility, async failure visibility, and feature-flag posture
```


### Appendix H — 🔥 degraded-mode and failover posture

```
┌────────────────────────────────────────────────────────────────────────────────────┐
│ FOOD RUN — 🔥 DEGRADED-MODE AND FAILOVER POSTURE                                           │
│    - early live slices must already know how to behave when parts of the MVP degrade       │
└────────────────────────────────────────────────────────────────────────────────────┘


FAILURE CLASS
  │
  ├── 🍽️ parser failure
  ├── 📦 queue lag or retry storm
  ├── 🤖 provider degradation
  ├── ⚡️ cache miss / cache loss
  ├── 🔑 auth issue
  └── 🧷 sharing / tenant-state inconsistency risk
  │
  ▼
DETECTION
  │
  ├── 🔍 request ids
  ├── route / job visibility
  ├── 🧬 traces
  └── 🚢 release markers
  │
  ▼
MITIGATION
  │
  ├── use fallback path
  ├── disable risky 🤖 AI/LLM path
  ├── surface pending / retry state
  ├── reduce affected feature scope
  └── preserve usable core flow where possible
  │
  ▼
USER-AND-OPERATOR OUTCOME
  │
  ├── clear failure where necessary
  ├── visible degraded mode where acceptable
  ├── triageable runtime behavior
  └── no silent “it probably worked” posture
```


### Appendix I — 🐝 11-agent governance and delivery flow

```
┌─────────────────────────────────────────────────────────────────┐
│ FOOD RUN — 🐝 11-AGENT GOVERNANCE AND DELIVERY FLOW                   │
│    - repo reality at the end of 📅 Sprint 0                           │
└─────────────────────────────────────────────────────────────────┘


ROOT CONTROL
  │
  ├── AGENTS.md
  ├── .opencode/rules/**
  ├── .opencode/commands/**
  ├── .opencode/skills/**
  ├── docs/planning/**
  └── docs/coordination/**
  │
  ▼
ORCHESTRATION
  │
  ├── 🐝 pm
  └── 🐝 reporter
  │
  ▼
DISCOVERY / PLANNING
  │
  ├── 🐝 scout
  ├── 🐝 planner
  └── 🐝 architect
  │
  ▼
IMPLEMENTATION
  │
  ├── 🐝 developer
  └── 🐝 designer
  │
  ▼
REVIEW / FIT / OPS SCRUTINY
  │
  ├── 🐝 reviewer
  ├── 🐝 integrator
  └── 🐝 ops
  │
  ▼
KNOWLEDGE PRESERVATION
  │
  └── 🐝 librarian
  │
  ▼
DURABLE OUTPUTS
  │
  ├── 📚 docs
  ├── 🧾 ADR
  ├── review artifacts
  ├── verify artifacts
  ├── planning packets
  └── coordination packets
```


