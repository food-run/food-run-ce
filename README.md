# 🛒🏃  Food  Run


*Smart meal prep and grocery planning from the recipes you already love.*


Food Run is a meal planning platform that helps home cooks turn a week’s worth of online recipes into a single, efficient bulk shopping trip. Paste in recipe links, confirm the ingredients, and Food Run will build a consolidated shopping list that respects your pantry, your portions, and your budget. Food Run can also tailor weekly meal plan recommendations for you and your household

> ***Live Demo:***  [https://food-run.github.io/food-run-ce/](https://food-run.github.io/food-run-ce/)


---


## TL;DR

Food Run is being rebuilt from a validated prototype into a multi-surface production system with explicit ownership boundaries, preserved legacy evidence, and durable technical docs that guide later product, platform, and agent work. The archived prototype shows the validated Food Run product loop that existed before the governed rebuild started.

### Quick Navigation

- Technical Docs  →  `docs/`
  - [`docs/repo.md`](docs/repo.md)  →  explains repo layout rules, active versus archived structure, and path ownership
  - [`docs/adr.md`](docs/adr.md)  →  records durable technical and process decisions
  - [`docs/architecture.md`](docs/architecture.md)  →  system design diagrams, architecture breakdowns, and maps the rebuild's runtime and boundary posture
  - [`docs/agent.md`](docs/agent.md)  →  explains governed agent workflow behavior
  - [`docs/testing.md`](docs/testing.md)  →  captures verification posture and testing layers
  - [`docs/operations.md`](docs/operations.md)  →  captures operator-facing runtime and release expectations
- Workflow Coordination
  - Planning Packets  →  `docs/planning/`
  - Live Coordination  →  `docs/coordination/`
  - Legacy Archive Guide  →  [`docs/legacy-v0.md`](docs/legacy-v0.md)
  - Sprint 0 Overview  →  [`docs/planning/sprint-0/overview.md`](docs/planning/sprint-0/overview.md)
- Preserved Prototype Snapshot  →  [`legacy-v0/README.md`](legacy-v0/README.md)
- Repo Operating Contract (Agentic AI Harness)  →  [`AGENTS.md`](AGENTS.md)
  - Agents  →  `.opencode/agents/`
  - Commands  →  `.opencode/commands/`
  - Rules  →  `.opencode/rules/`
  - Skills  →  `.opencode/skills/`

### Tech Stack
- Frontend  →  
- Backend  →  
- Database  →  
- Testing  →  

### Repository Intent

The intent of Food Run CE is to provide a public community edition while preserving clear boundaries around:
- project governance
- contribution review
- release authority
- trademark and brand use
- any separate hosted, commercial, enterprise, support, or partner offerings maintained by the Project Owner

---

## Overview

### Why Food Run?

Most people plan meals in tabs, not systems:

- Five recipes open across three different sites.
- Ingredients scattered across pages with slightly different names or units.
- Forgetting what’s already in the pantry and overbuying.
- Doing mental math for “double this recipe, halve that one” across the whole week.

Food Run aims to be the bridge between **how people actually find recipes** (blogs, TikTok, Instagram, big food sites) and **how they actually shop** (one grocery trip with a clear, realistic list).

### What Food Run Does

Food Run is designed for:

- **Home cooks and students** who batch cook or meal prep.
- **Busy professionals and parents** who want fewer grocery runs and less food waste.
- **Budget-conscious shoppers** who care about planning ahead and using what they already have.

At a high level, Food Run:

- Imports ingredients from recipe URLs.
- Normalizes ingredients into a structured format.
- Lets users confirm and edit those ingredients for accuracy.
- Combines multiple recipes into one consolidated shopping list.
- Adjusts that list based on pantry items the user already has.

### How It Works

1. **Paste recipe links**  →  Users paste one or more recipe URLs from supported sites. Food Run fetches the page content and extracts the recipe metadata and ingredient list.
2. **Confirm ingredients**  →  The app shows a structured ingredient list for each recipe. Users can:

   - Clean up ingredient names (e.g., “onion, chopped” → “yellow onion”).
   - Remove anything that doesn’t belong (pop-ups, odd text).
   - Add or tweak ingredients as needed.
3. **Plan portions**  →  Users choose which recipes they want to cook and how many portions they want for each.The app treats “servings” as a first-class factor when it calculates totals.
4. **Generate the shopping list**  →  Food Run aggregates ingredients across recipes into a single list, combining matching items where possible:

   - “2 cups rice” + “1 cup rice” → “3 cups rice”
   - “onion” appearing in multiple recipes → one line item with a higher quantity
5. **Adjust for pantry items**  →  Users can tell the app what they already have on hand (e.g., “2 cans black beans”, “1 bag of rice”). Food Run subtracts those from the shopping list with a small safety buffer, so users don’t end up short.
6. **Walk away with a clean list**
   The final output is a simple, readable shopping list that can be used on a phone in-store or printed on paper.


---


## Current Status

The repo is in rebuild mode. The validated prototype is preserved under `legacy-v0/`, and Sprint 0 is establishing the governed baseline that later deliverables will extend across the active rebuild tree.

### What This Repo Contains Now

- repo-governance files such as `AGENTS.md`, `opencode.json`, and `.opencode/`
- planning and coordination material under `docs/`
- seeded active rebuild homes under `apps/`, `shared/`, and `tools/`
- contributor and governance documents at the root
- the archived prototype under `legacy-v0/`

### Active Rebuild Path

New implementation work belongs only on the active rebuild surfaces described in `AGENTS.md`: `apps/`, `shared/`, `platform/`, `tools/`, and `docs/`, with repo-control surfaces such as `.opencode/`, `.github/`, `AGENTS.md`, and `opencode.json` remaining active for governance and automation.

The rebuild now includes a governed agent workflow contract in `AGENTS.md`, project-level OpenCode guidance in `opencode.json` and `.opencode/`, and a technical docs spine in `/docs`. Later changes are expected to extend these files instead of creating new side-channel process docs.

The active rebuild tree is now seeded under `apps/`, `shared/`, and `tools/`. Later Sprint 0 deliverables will extend platform parity, CI/CD gates, and runtime observability on top of these permanent homes.

### Repo Layout Direction

- `apps/` holds deployable runtime homes
- `shared/` holds reusable seam vocabulary and deterministic test support
- `tools/` already holds shared repo automation and verification entrypoints
- `platform/` remains a later Sprint 0 layer for runtime parity work

### Next Structural Layers

- later Sprint 0 work will extend platform parity, deepen the existing quality gates, add deeper docs, and seed runtime observability
- future feature work should extend the current committed rebuild structure rather than recreate stale packet-era homes

### Agent-Governed Rebuild

Food Run now uses a governed rebuild workflow. `AGENTS.md` is the always-on operating contract, `opencode.json` defines repo-level OpenCode behavior, and `.opencode/` holds lane docs, commands, rules, and skills that extend the same operating theory.

When planning packets drift from current committed repo reality, the default behavior is to refine the packet to the committed permanent structure rather than recreate older filenames or duplicate control surfaces.


---


## Contributions

Contributions are welcome, but acceptance is at maintainer discretion. Do not extend legacy or prototype-only surfaces with new implementation work unless maintainers explicitly approve it. Changes become mergeable by extending the current committed repo structure, keeping coordination current, and updating the matching durable docs when shared understanding changes. 

In general:
- new work should follow the active rebuild direction, so open the smallest relevant planning packet and `AGENTS.md`
- large architectural changes should be discussed before implementation
- legacy paths should not be extended unless maintainers explicitly approve it

Maintainers may narrow, defer, or reject work that does not align with the current roadmap. Therefore, contributions must:
- prefer reusing current permanent homes over introducing duplicate structures
- update root guidance and technical docs when repo-control behavior changes
- pass the repo verification and review gates before closeout

### Where To Start

Before opening substantial work, review:
- [`LICENSE.md`](LICENSE.md)
- [`CONTRIBUTING.md`](CONTRIBUTING.md)
- [`GOVERNANCE.md`](GOVERNANCE.md)
- [`TRADEMARKS.md`](TRADEMARKS.md)
- [`CLA.md`](CLA.md)
- [`SECURITY.md`](SECURITY.md)
- for more detailed implementation map:
  - [`docs/repo.md`](docs/repo.md)
  - [`AGENTS.md`](AGENTS.md)

### Merge Discipline

- use `.github/pull_request_template.md` and `.opencode/commands/pr-prepare.md` together so the branch summary, verification, docs delta, protected-path notes, and CLA wording stay aligned
- update `docs/adr.md` for meaningful repo-control and shared-understanding changes before treating a branch as PR-ready
- expect merge-gate automation in `.github/workflows/repo-verify.yml`, `.github/workflows/docs-guard.yml`, `.github/workflows/protected-paths.yml`, `.github/workflows/cla-check.yml`, and `.github/workflows/cd.yml` to enforce the documented repo contract

### Protected Paths

- protected surfaces include `.github/workflows/**`, `.opencode/**`, `AGENTS.md`, `opencode.json`, auth/session policy, migrations, tenancy or role enforcement, secrets handling, queue replay controls, and failover controls
- changes on those paths need explicit risk acknowledgement, narrow diffs, and matching durable docs when they alter shared understanding

### CI and Docs Expectations

- keep `tools/script/verify.py`, `tools/script/coordination_status.py`, and `tools/script/release.py` as the central script seams instead of duplicating policy in workflow YAML
- keep `docs/testing.md`, `docs/operations.md`, and `docs/adr.md` aligned with the actual workflow and script behavior
- if a durable doc is missing, stub only that exact permanent file, and only when the expected content is not already sufficiently covered elsewhere
- treat the local `python3 tools/script/coordination_status.py watch` loop as operator-owned coordination support, not as CI-owned automation


---


## License And Project Boundary

Food Run Community Edition (CE) is licensed under the GNU Affero General Public License, version 3 or any later version (AGPLv3-or-later).

See [`LICENSE.md`](LICENSE.md) for the full license text.

### Trademark Boundary

The software license does **not** grant rights to the Food Run name, logos, icons, or other brand assets.

Those rights are governed separately by:
- [`GOVERNANCE.md`](GOVERNANCE.md)
- [`TRADEMARKS.md`](TRADEMARKS.md)
- [`CLA.md`](CLA.md)

If you publish a fork, modified version, or hosted service based on Food Run CE:
- you must comply with the software license
- you must use different branding unless you have written permission
- you must not imply that your version is the official Food Run project

### Security

Please do **not** report vulnerabilities in public issues, pull requests, or discussions. Use the private reporting path described in [`SECURITY.md`](SECURITY.md).

### Commercial boundary

The Project Owner may maintain separate hosted, commercial, enterprise, support, or partner offerings outside the Community Edition.

### Forks and Downstream Use

Forks are allowed under the project’s software license, but forks and hosted derivatives must respect the trademark policy in [`TRADEMARKS.md`](TRADEMARKS.md).

In particular:
- the code license does not grant branding rights
- modified or hosted versions must not present themselves as the official Food Run project without written permission
- forks are encouraged to provide clear factual acknowledgment when referencing the upstream project


---


Last updated: 2026-03-20
