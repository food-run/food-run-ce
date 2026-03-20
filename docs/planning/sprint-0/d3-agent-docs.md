# 🌟 S0-D3 — 🐝 Agent Steering + 📚 Docs Spine

## TL;DR

S0-D3 gives the rebuild its operating theory before parallel work accelerates. It defines how humans and agents are allowed to behave in the repo, where technical reasoning lives, and how lane rules, protected paths, artifacts, and ADR updates become part of normal delivery rather than side-channel process.

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

Once multiple humans and multiple agents are working in parallel, the biggest risk is no longer “we forgot to make a folder.” The real risks become:

- agents editing the wrong paths
- reviewers applying inconsistent standards
- contributors merging code without updating shared understanding
- docs getting treated as after-the-fact cleanup
- architecture decisions living in chat history instead of the repo

D3 must establish two permanent spines:

- **agent steering spine**
  - lane responsibilities
  - protected-path rules
  - approval rules
  - artifact expectations
  - review standards
- **docs spine**
  - ADR source of truth
  - architecture map
  - agent workflow docs
  - testing/verification philosophy
  - repo-level operating guidance

---

## 👥 Ownership

**Owner:** 👤🎯 Team Lead  
**Reviewer:** 👤👻 AI/Cloud  
**Required consult:** 👤🧰 BE/API, 👤🛡️ Platform/QA, 👤🎨 FE/Data

---

## 🌿 Branch

` s0/d3-agent-docs `

---

## 🏷️ Deliverable PR title

`docs(agent): define governed lane rules and seed the ADR and architecture docs that every later change must extend`

---

## 🎯 Purpose

Seed the permanent control documents that later work must follow, so:

- agents have explicit lanes and boundaries
- humans review against one standard
- architecture reasoning has one persistent home
- every future change can update docs and ADRs instead of creating fresh tribal knowledge

---

## ⛓️ Depends on

- 🌟 S0-D1 — 🧼 Repo Reset + 🧊 Legacy Freeze
- 🌟 S0-D2 — 🧱 Active Tree + 🔌 Shared Seams

---

## 🚧 Blocks

- 🌟 S0-D4 — 🐙 CI/CD + 🛡️ Quality Gates
- 🌟 S0-D5 — 🐳 Docker + ☸️ k3s + 🔍 Observability Baseline
- all later sprints, because later work needs lane rules, approval rules, ADR discipline, and architecture documentation entry points

---

## 📂 Files touched

### New root governance file

- `AGENTS.md`

### New project config file

- `opencode.json`

### New `.opencode/` permanent files

- `.opencode/agents/pm.md`
- `.opencode/agents/scout.md`
- `.opencode/agents/planner.md`
- `.opencode/agents/architect.md`
- `.opencode/agents/developer.md`
- `.opencode/agents/designer.md`
- `.opencode/agents/reviewer.md`
- `.opencode/agents/integrator.md`
- `.opencode/agents/ops.md`
- `.opencode/agents/librarian.md`
- `.opencode/commands/plan.md`
- `.opencode/commands/verify.md`
- `.opencode/commands/adr.md`
- `.opencode/rules/paths.md`
- `.opencode/rules/approvals.md`
- `.opencode/rules/reviews.md`
- `.opencode/skills/repo_map.md`
- `.opencode/skills/sprint_flow.md`

### New docs spine files

- `docs/adr.md`
- `docs/architecture.md`
- `docs/agent.md`
- `docs/testing.md`
- `docs/operations.md`

### Meaningfully refactored files

- `README.md`
- `docs/repo.md`

---

## 🧠 Recommended names

### Core repo-control names

- `lane`
- `path_map`
- `approval_gate`
- `review_gate`
- `artifact_set`
- `adr_delta`
- `risk_note`
- `owner_map`

### Lane names

- `scout`
- `planner`
- `coder`
- `reviewer`
- `integrator`

### Path sensitivity terms

- `safe_path`
- `protected_path`
- `human_only`
- `deny_default`
- `escalate_only`

### Artifact terms

- `patch_artifact`
- `plan_artifact`
- `review_artifact`
- `verify_artifact`
- `adr_artifact`

---

## 🧾 Exact TL;DR sections per new or refactored file

D3 should use the exact TL;DR blocks defined in the Sprint 0 packet for:

- `AGENTS.md`
- `opencode.json`
- `.opencode/agents/*.md`
- `.opencode/commands/*.md`
- `.opencode/rules/*.md`
- `.opencode/skills/*.md`
- `docs/adr.md`
- `docs/architecture.md`
- `docs/agent.md`
- `docs/testing.md`
- `docs/operations.md`

Key reminders:

- `AGENTS.md` is the top-level operating contract
- `opencode.json` is the root project config, not `.opencode/opencode.json`
- `.opencode/` should hold agents, commands, rules, and skills
- later changes are expected to extend these files rather than creating process side-channels elsewhere

`README.md` should add:

- `## Agent-Governed Rebuild`
- `## Technical Docs`
- `## How Changes Become Mergeable`

with this exact addition:

```md
The rebuild now includes a governed agent workflow contract in `AGENTS.md`, project-level OpenCode guidance in `opencode.json` and `.opencode/`, and a technical docs spine in `/docs`. Later changes are expected to extend these files instead of creating new side-channel process docs.
```

---

## ⚠️ Hotspot files

These files define the operating contract for the entire repo:

- `AGENTS.md`
- `opencode.json`
- `.opencode/rules/paths.md`
- `.opencode/rules/approvals.md`
- `.opencode/rules/reviews.md`
- `docs/adr.md`
- `docs/architecture.md`

---

## 🎟️ Task tickets

### 🎟️ S0-D3-T1 — 🐝 Define the governed lane model and root operating contract

**Commit title:**  
`docs(agent): define lane responsibilities path sensitivity and merge-blocking review rules in the root operating contract`

#### Purpose

Create the top-level operating contract so every human and agent knows the allowed lanes, the protected-path model, and the questions that block merge.

### 🎟️ S0-D3-T2 — 🧭 Seed `.opencode/` with lane, path, and command rules

**Commit title:**  
`docs(agent): seed opencode lane files path rules and reusable commands for planning verification and ADR updates`

#### Purpose

Translate the root operating contract into agent-consumable lane files, rules, and commands so actual agent runs can follow the same structure humans review against.

### 🎟️ S0-D3-T3 — 📚 Seed the technical docs and ADR spine

**Commit title:**  
`docs(adr): seed the architecture record and technical docs that later changes must extend instead of bypass`

#### Purpose

Create the first permanent technical-doc surfaces so later changes update shared theory in place.

### 🎟️ S0-D3-T4 — 🧾 Refactor root guidance so process, structure, and docs point to the same truth

**Commit title:**  
`docs(repo): align the README and repo guide with the new agent contract and technical documentation spine`

#### Purpose

Ensure the root narrative, repo guide, agent rules, and docs spine all tell the same story about how work happens in the rebuild.

---

## 👾 Verification tickets

### 👾 S0-D3-T1-V — 🧠 Verify the lane and approval model is operational, not symbolic

**Commit title:**  
`test(agent): verify the lane model approval rules and review questions are specific enough to guide real work`

#### Verification pass condition

A reviewer can test at least one safe-path scenario and one protected-path scenario and get the same interpretation from `AGENTS.md` and `.opencode/` without ad hoc judgment.

### 👾 S0-D3-T2-V — 📚 Verify the docs spine is extendable and aligned with the repo

**Commit title:**  
`docs(architecture): verify the adr and technical docs are aligned with the active tree and ready for later extension`

#### Verification pass condition

A future Sprint 1 contributor can name one doc they would extend for:

- a contract change
- a domain-rule change
- an agent workflow change
- a release/operations change

without inventing a new side-channel doc.

---

## ✅ Deliverable verification

S0-D3 is done only when:

- `AGENTS.md` exists and defines lanes, path sensitivity, review rules, ADR discipline, and escalation logic
- `opencode.json` exists at the repo root and the `.opencode/` control surface is seeded
- `docs/adr.md`, `docs/architecture.md`, `docs/agent.md`, `docs/testing.md`, and `docs/operations.md` exist
- `README.md`, `docs/repo.md`, `AGENTS.md`, `opencode.json`, and `.opencode/` do not contradict each other

---

## 🚨 Bad agent output patterns to watch for

Reject immediately if an agent tries to:

- write broad motivational language instead of real lane rules
- define protected paths without naming any concrete path classes
- let every lane edit code because “it is more flexible”
- make `AGENTS.md` so long and repetitive that nobody will keep it updated
- duplicate the same rules in many files with slightly different wording
- treat the ADR as a changelog instead of a reasoning record
- write docs that describe future implementation as already complete
- create hidden process docs outside `AGENTS.md`, `opencode.json`, `.opencode/`, or `/docs`

---

## 🧩 Rationale in one sentence

S0-D3 is successful when the rebuild has one shared operating theory for humans and agents, and that theory lives in the repo where later changes must extend it rather than work around it.
