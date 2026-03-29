# 🧾 Architecture Decision Record

## TL;DR

This file is the durable reasoning spine for major Food Run technical and process decisions. It is sorted recency first. Later changes should extend these entries or add a new higher entry instead of scattering rationale across pull requests, chat history, or side-channel docs.

### How To Use This File

- Add new decision entries as the rebuild evolves
- Capture why a choice was made, not just what changed
- Link related repo surfaces and docs when the decision changes shared understanding
- Keep entries sorted newest first
- Keep `## Current Status` to a 5-10 bullet sprint recap instead of a running changelog
- Use 2-5 concrete bullets for every ADR question so benefits, trade-offs, alternatives, and constraints stay explicit
- Keep slices as small as current understanding allows without creating duplicate ADR noise
- Plan out-of-scope human edits separately unless the human explicitly includes them
- One decision per entry — if a deliverable touches multiple distinct surfaces, split into separate entries (e.g., D5 touching Dockerfiles, k8s manifests, health endpoints, and docs should become 4-6 separate ADR entries)

### Decision Entry Template

- ***What was built?***
- ***Why was it chosen?***
- ***What boundaries does it own?***
- ***What breaks if it changes?***
- ***What known edge cases or failure modes matter here?***
- ***Why does this work matter?***
- ***What capability does it unlock?***
- ***Why is the chosen design safer or more scalable?***
- ***What trade-off did the team accept?***

### Current Status

- Sprint 0 established the prototype-preserving rebuild boundary by freezing the old product proof under `legacy-v0/` and clarifying the active v1 tree.
- The active rebuild now has durable homes under `apps/`, `shared/`, `platform/`, `tools/`, `.opencode/`, and `docs/`, so later work can extend permanent surfaces instead of inventing new ones.
- Repo-control governance is now explicit through lane docs, command docs, reusable rules, coordination standards, protected-path handling, and architect-first plus ops-gated execution order.
- CI and PR controls now enforce reviewer narrative, docs and ADR coverage, protected-path acknowledgement, CLA handling, and a central repo verification seam.
- Runtime parity baselines now exist for containers, k3s manifests, health and readiness surfaces, request correlation, observability vocabulary, resilience vocabulary, and edge-policy starter configs.
- The reviewer-visible frontend now lives under `apps/web`, publishes through GitHub Pages, and uses a repo-subpath build plus SPA fallback shell for the public demo URL.
- Sprint 1 now has a durable `docs/design-system/` packet that governs product-surface frontend planning, implementation, and review.
- Repo-control now requires UI and UX work to open the design-system packet, use the frontend skills when available, and route implementation through the `designer` lane by default.
- Frontend quality now has an app-local lint seam, a local-browser Playwright smoke seam, and a dedicated pull-request workflow that keeps those checks separate from deploy automation.
- Governed script seams now live under `tools/scripts/`, while the matching shared repo-control suites and helpers now live together under `shared/testkit/`.
- Sprint 0 delivery now defaults to small Conventional Commit checkpoints, stable scope-based coordination artifacts, and ADR-backed closeout before PR preparation.

---

## Entries

---

### S1-D0 - Treat the design system as the governing packet for frontend work

- ***What was built?***
  - `docs/design-system/` now contains the master brief, reusable design guidance, page packets, implementation playbook, anti-pattern list, and review rubric for the active frontend.
  - `AGENTS.md`, `.opencode/rules/implementation-standards.md`, and the newer repo-control guidance now require UI and UX work to open those design-system documents, use `frontend-first-principles` and `ui-ux-review` when available, and route product-surface implementation through `designer` by default.
- ***Why was it chosen?***
  - The branch had accumulated real product-surface refinement work, but the reasoning for calm hierarchy, surface reduction, honest copy, and review discipline would have stayed fragmented without one governing packet.
  - The repo also needed an explicit rule that UI work is not generic frontend coding, so agent routing and review quality stay aligned with the same source of truth.
- ***What boundaries does it own?***
  - The durable design decision home for product-surface frontend behavior, page-level UX guidance, and UI review standards.
  - The repo-control rule that binds UI planning, implementation, and review to the design-system packet plus the frontend-specialized skills and `designer` lane.
- ***What breaks if it changes?***
  - Frontend work can drift back toward one-off style decisions, duplicate guidance, or agent-specific interpretations that are hard to review and harder to repeat.
  - PM, designer, reviewer, and human operators can also stop sharing the same UI packet, which weakens explainability and increases drift between implementation and critique.
- ***What known edge cases or failure modes matter here?***
  - Runtime skill inventories may lag, so the fallback rule must keep the design-system documents mandatory even when a skill cannot be loaded.
  - Docs-only design-system maintenance is intentionally exempt from forced `designer` delegation so the repo does not over-route pure documentation work.
- ***Why does this work matter?***
  - It turns the new frontend style from a branch-local taste choice into a governed, reusable system that later Sprint 1 work can extend honestly.
  - It also keeps repo-control, design review, and implementation language synchronized instead of scattering UI rules across PR text and chat.
- ***What capability does it unlock?***
  - Later frontend tasks can start from one stable design packet with named page guidance, implementation defaults, and review criteria.
  - UI subagents can now inherit explicit routing expectations instead of guessing whether the work belongs to `developer`, `designer`, or an ad hoc style pass.
- ***Why is the chosen design safer or more scalable?***
  - A central design packet plus repo-control enforcement scales better than repeating visual rules in multiple planning docs or code comments.
  - Binding UI work to specialized skills and the `designer` lane keeps future product-surface changes more reviewable and less likely to blur into generic code churn.
- ***What trade-off did the team accept?***
  - Frontend tasks now carry extra planning and review ceremony because the design-system packet must be opened and cited before product-surface edits land.
  - The repo must keep the design-system documents current or the stronger routing rules will amplify stale guidance rather than useful discipline.

---

### S1-D0 - Reduce shell and page surface density so routed content stays dominant

- ***What was built?***
  - The Sprint 1 frontend and matching page guidance now favor lighter shell framing, calmer navigation chrome, spacing-led route structure, and lighter empty-state treatments instead of stacked boxed panels.
  - `apps/web/src/styles.css`, `apps/web/src/styles/layout.css`, `apps/web/src/styles/pages.css`, route copy updates, and the matching `docs/design-system/pages/*.md` guidance now align the reviewer shell with that reduced-surface direction.
- ***Why was it chosen?***
  - The reviewer-visible shell still carried prototype-era card density that made framing compete with the actual page job, especially on empty states and the routed content region.
  - Sprint 1 needs a frontend that feels calmer and more trustworthy for live-MVP review, so spacing, hierarchy, and copy had to do more work than borders and muted panels.
- ***What boundaries does it own?***
  - The shared shell-versus-page hierarchy for the active reviewer frontend, including how much visual weight the nav, main region, and route empty states are allowed to carry.
  - The page-level design guidance for import, recipes, planner, and shopping surfaces when they need lighter copy and fewer boxed treatments.
- ***What breaks if it changes?***
  - The shell can start visually outranking the routed page again, which makes the frontend feel heavier and less focused than the design system intends.
  - Empty states and secondary guidance can also regress back into card-heavy scaffolding that implies more product completeness than the current app actually has.
- ***What known edge cases or failure modes matter here?***
  - Reducing surfaces too aggressively can weaken grouping or trust if spacing, labels, and interaction states do not compensate.
  - The reviewer shell still needs enough containment and contrast to remain readable in both light and dark themes, so lighter framing cannot become invisible framing.
- ***Why does this work matter?***
  - It makes the active frontend feel more like a coherent workflow product and less like a prototype-era collection of stacked panels.
  - It also keeps Sprint 1 copy and layout honest by letting the real task lead instead of using decorative boxes to simulate structure.
- ***What capability does it unlock?***
  - Later route work can extend one lighter shell language instead of re-deciding whether every page needs its own card wrapper.
  - Reviewers and live users can scan the active page faster because the shell now frames the task instead of competing with it.
- ***Why is the chosen design safer or more scalable?***
  - Shared surface-reduction rules in styles and page docs are easier to maintain than route-by-route visual exceptions.
  - A lighter shell also makes future page additions less likely to inherit unnecessary bordered containers by default.
- ***What trade-off did the team accept?***
  - Some earlier boxed affordances were intentionally removed or softened, so clarity now depends more on strong spacing, copy discipline, and state styling.
  - The team must review future pages more carefully because the design leaves less room for visual noise to hide weak hierarchy.

---

### S1-D0 - Use a compact animated navigation and token set to give the web shell clearer orientation

- ***What was built?***
  - `apps/web/src/components/app.ts` now drives nav state from router activity and hover state, while `apps/web/src/styles/components.css`, `apps/web/src/styles/theme.css`, and `apps/web/src/styles.css` add compact sizing tokens, animated nav emphasis, nav shadow variables, and smoother theme-transition handling.
  - `apps/web/src/components/index.ts` exports the renamed nav template, and the design-system shell guidance now treats the nav rail and routed region contrast as a first-class readability rule.
- ***Why was it chosen?***
  - After the lighter shell pass, the app still needed a stronger orientation cue so route changes feel intentional without reverting to heavy boxed chrome.
  - The nav also needed more polished state behavior and theme transitions so the playful-comic system feels disciplined rather than static or abrupt.
- ***What boundaries does it own?***
  - The shared navigation interaction pattern for the active frontend shell, including active-route emphasis, hover feedback, and the compact token set that supports that pattern.
  - The global styling contract for compact controls, nav movement, and theme-transition behavior that other shared surfaces now inherit.
- ***What breaks if it changes?***
  - Route orientation becomes less obvious, active-page emphasis can drift out of sync with router state, and the nav can fall back into either visually flat or overly heavy behavior.
  - Shared control sizing and theme transitions can also become inconsistent if later changes bypass the compact token layer.
- ***What known edge cases or failure modes matter here?***
  - Hover-driven polish must not become the only orientation cue, so active state and accessible semantics still need to carry the baseline signal.
  - Theme transitions must stay calm and not animate every detail during a mode switch, which is why the shell explicitly suppresses animation noise during theme swapping.
- ***Why does this work matter?***
  - It gives the frontend a more polished and memorable shell without violating the lighter, calmer design direction introduced elsewhere in Sprint 1.
  - It also makes route changes and theme changes feel more deliberate, which improves trust even before deeper product functionality exists.
- ***What capability does it unlock?***
  - Later shell and component work can reuse the compact token vocabulary and animated nav model instead of inventing one-off state treatments.
  - The app can now carry more personality in motion and emphasis while keeping the main page content visually dominant.
- ***Why is the chosen design safer or more scalable?***
  - Centralizing the behavior in shared app-shell and token files keeps the interaction model reviewable in a few stable homes.
  - Using router-derived active state is more durable than manually toggled presentation classes because the navigation signal stays bound to the real route contract.
- ***What trade-off did the team accept?***
  - The shell now carries more motion and token complexity than the earlier static nav, so future edits need stronger discipline to avoid decorative drift.
  - The compact styling direction leaves less margin for oversized labels or controls, so future copy and component work must fit the denser shell deliberately.

---

### S0-D6 - Keep frontend quality app-local while automating lint and smoke checks with installed browsers

- ***What was built?***
  - `apps/web/package.json` now exposes app-local `lint` and `e2e` commands, while `shared/testkit/ui/playwright.config.mjs` resolves an already-installed Chromium or Chrome executable instead of relying on Playwright-managed browser downloads.
  - `.github/workflows/frontend-quality.yml` now runs frontend lint and browser smoke for `apps/web/**` pull requests, and `tools/scripts/hooks.py` installs local `pre-commit` and `pre-push` wrappers for the same bounded checks.
- ***Why was it chosen?***
  - The earlier Playwright slice proved smoke coverage was useful, but it still depended on Playwright-managed browser downloads and manual execution, which made package ownership and operator setup less explicit than the repo standards expect.
  - Keeping frontend quality app-local also avoids broadening the central repo verifier or deploy workflow before the smoke suite has earned that blast radius.
- ***What boundaries does it own?***
  - The active web app's lint contract, local-browser smoke contract, and the thin PR workflow that automates those checks without changing deploy policy.
  - The local hook bootstrap seam that helps contributors run the same bounded frontend checks before commits and pushes leave the machine.
- ***What breaks if it changes?***
  - Contributors can drift back toward Playwright-managed browser downloads, or the smoke suite can stop running against the browser actually available on the operator or CI machine.
  - Frontend regressions can also slip through more easily if lint and smoke automation drift away from the app-local commands they are meant to mirror.
- ***What known edge cases or failure modes matter here?***
  - Local smoke runs now depend on a browser executable already existing, so the config must fail fast with a clear path requirement when neither Chromium nor Chrome is installed.
  - CI browser availability now depends on the workflow's browser-install step rather than Playwright downloads, so workflow drift becomes the main setup failure mode.
- ***Why does this work matter?***
  - It turns frontend lint and smoke coverage into truthful owned quality seams instead of optional local habits.
  - It also keeps browser-install cost and deploy blast radius explicit while the frontend surface is still small.
- ***What capability does it unlock?***
  - Frontend pull requests can now get browser-smoke feedback automatically without waiting for deploy workflows or reintroducing dead Angular test scaffold.
  - Contributors can also install lightweight local hooks that mirror the same lint and smoke commands before code leaves their machine.
- ***Why is the chosen design safer or more scalable?***
  - App-local commands keep ownership simple, while the separate workflow keeps smoke failures from being confused with Pages deployment behavior.
  - Using installed browsers instead of Playwright-managed downloads reduces hidden toolchain behavior and keeps the executable path reviewable in one config file.
- ***What trade-off did the team accept?***
  - Operators and CI runners now need a browser executable available ahead of the smoke run instead of letting Playwright fetch one automatically.
  - Local hook enforcement still requires an explicit bootstrap step because the repo does not rewrite git config automatically.

---

### S0-D6 - Build the reviewer-visible frontend artifact for the GitHub Pages project path

- ***What was built?***
  - `apps/web/package.json` now exposes `bun run build:pages`, which builds the Angular shell with the `/food-run-ce/` base href and copies `index.html` to `404.html`.
  - `.github/workflows/web-pages.yml`, `docs/architecture.md`, and `docs/operations.md` now point at that Pages-targeted artifact contract instead of a generic production build.
- ***Why was it chosen?***
  - The earlier D6 frontend restore was only partially truthful because a root-based build can look healthy locally while breaking at the real project-page URL.
  - GitHub Pages project hosting also needs an SPA fallback shell for route refreshes, so the branch needed one explicit artifact contract instead of relying on undocumented platform behavior.
- ***What boundaries does it own?***
  - The reviewer-visible static build command, the deployed GitHub Pages artifact shape, and the repo-subpath routing contract for the public demo URL.
  - The documentation boundary that explains GitHub Pages as a static review surface rather than a general frontend deployment target.
- ***What breaks if it changes?***
  - The public demo can load the wrong asset paths or fail on direct navigation to routed pages, which makes the repo look less complete than the governed branch state actually is.
  - Operators and reviewers can also drift back toward a generic `build` command that does not reflect the real Pages environment.
- ***What known edge cases or failure modes matter here?***
  - GitHub Pages project sites serve under a repository subpath, so the base href must stay aligned with `/food-run-ce/` until the hosting model changes.
  - The `404.html` fallback only restores static SPA navigation; it does not imply SSR, backend awareness, or production-grade edge routing.
- ***Why does this work matter?***
  - It turns the public reviewer URL into an honest extension of the active rebuild tree instead of a locally-correct but publicly-broken demo path.
  - It also closes the last visible gap in D6 by making route refreshes behave like the current frontend shell claims they should.
- ***What capability does it unlock?***
  - Reviewers can open the live Pages URL, refresh a routed page, and stay inside the active frontend shell without manual fixes.
  - Later frontend work can extend one truthful reviewer-surface build contract instead of adding platform-specific patches in multiple places.
- ***Why is the chosen design safer or more scalable?***
  - One named build command keeps the project-page behavior reviewable in one home and avoids duplicating base-path logic across workflow YAML and docs.
  - Copying the built shell to `404.html` is a narrow static-hosting adaptation that remains easy to reason about and roll back.
- ***What trade-off did the team accept?***
  - The repo now carries a Pages-specific build variant, so future hosting changes must update that command and the matching docs together.
  - The fallback page is a pragmatic static-hosting compromise rather than a full routing platform.

---

### S0-D6 - Collapse repo-control verification into `shared/testkit/` and simplify script naming

- ***What was built?***
  - Repo-control verification modules moved out of `tools/testing/repo_controls/` into `shared/testkit/` as `verify.py`, `release.py`, `coordination.py`, and `workflows.py`, and the old `tools/testing/` surface was retired.
  - The reviewer-frontend verifier moved into `tools/scripts/frontend.py`, and the coordination runner now lives at `tools/scripts/coordination.py` so folder context carries more of the naming burden.
- ***Why was it chosen?***
  - The master packet already reserved `shared/testkit/` as the long-term home for deterministic shared test support, so keeping a parallel `tools/testing/` tree was drift rather than a real boundary.
  - Explicit module lists in `tools/scripts/verify.py` make the no-prefix naming rule enforceable without relying on `test_*.py` discovery conventions.
- ***What boundaries does it own?***
  - `tools/scripts/` remains the operator-facing runtime home for governed verification commands and helper scripts.
  - `shared/testkit/` now owns both the shared repo-control suites and the reusable test fixtures/helpers those suites depend on.
- ***What breaks if it changes?***
  - Repo verification can silently miss the intended suites if `tools/scripts/verify.py` stops running the explicit `shared.testkit.*` module list.
  - Durable docs and operator commands can drift back toward deleted `tools/testing/` or retired `tools/scripts/coordination_status.py` paths.
- ***What known edge cases or failure modes matter here?***
  - Historical coordination notes may still mention the retired paths; those notes remain archival evidence and do not need mass cleanup.
  - `shared/testkit/` must stay focused on deterministic verification support so the collapse does not turn it into a generic bucket for unrelated utilities.
- ***Why does this work matter?***
  - It removes a duplicate structural story from Sprint 0 and makes the active tree look more like the target repo packet.
  - It also makes naming rules more reviewable by letting folders, not prefixes, carry most of the context.
- ***What capability does it unlock?***
  - Later shared verification work can extend one canonical `shared/testkit/` seam instead of deciding between `shared/` and `tools/testing/` every time.
  - Repo-control automation can keep using semantic filenames even when tests mirror runtime concepts closely.
- ***Why is the chosen design safer or more scalable?***
  - One explicit test-module list in the central verifier is easier to audit than pattern-based filename rules spread across docs and commands.
  - Co-locating shared suites with shared fixtures reduces path drift and avoids a long-lived split between near-identical verification concepts.
- ***What trade-off did the team accept?***
  - The rename touches several durable docs and one repo-control rule because path and naming behavior changed together.
  - The shared testkit surface is slightly broader now, so future reviewers need to keep its ownership line clear.

---

### S0-D6 - Rehome governed script seams under `tools/scripts/` and keep verification coverage aligned

- ***What was built?***
  - The governed repo-control scripts now live under `tools/scripts/`, and the active references in workflows, docs, planning packets, runtime manifests, and helper text were updated to match.
  - Repo-control unit coverage now lives under `shared/testkit/`, where shared fixtures and helper imports can load the governed script home directly.
- ***Why was it chosen?***
  - The branch had already deleted the old `tools/script/` files, so leaving workflows and docs on the retired path would have made the repo-control story broken but still plausible.
  - Collapsing the suites into `shared/testkit/` keeps one clearer ownership boundary between operator-facing scripts and deterministic shared verification support.
- ***What boundaries does it own?***
  - Canonical paths for governed repo-control scripts, the shared repo-control suite home, and the durable references humans and automation use to invoke those surfaces.
  - The documentation boundary that explains where script policy lives versus where tests validate it.
- ***What breaks if it changes?***
  - CI workflows and local operators can call missing files, docs can advertise the wrong commands, and later contributors can recreate duplicate script homes while trying to repair the drift.
  - Verification coverage also becomes harder to trust when tests and helper imports point at an outdated runtime location.
- ***What known edge cases or failure modes matter here?***
  - Historical coordination notes may still mention `tools/script/`; those are archival evidence and do not automatically need mass cleanup.
  - The repo must keep `tools/scripts/` narrow and governed so the rename does not turn into a generic automation dumping ground.
- ***Why does this work matter?***
  - It keeps the governed automation story executable again after the path migration already started landing on the branch.
  - It also reduces review ambiguity by keeping scripts in one active home and tests in one matching verification home.
- ***What capability does it unlock?***
  - Later repo-control work can extend the renamed script seams and shared suites without repairing stale path drift first.
  - CI and local operators can run the documented commands directly instead of inferring which path is still canonical.
- ***Why is the chosen design safer or more scalable?***
  - Updating the active references together keeps the rename small, deterministic, and easier to audit than carrying a long-lived alias period.
  - Reusing `shared/testkit/` for script loading keeps the test migration DRY while preserving explicit ownership.
- ***What trade-off did the team accept?***
  - The repo had to touch several durable docs and workflow-adjacent surfaces together, so even a narrow path migration carried a non-trivial coordination cost.
  - Historical planning and archive notes may still need selective future cleanup if they are later promoted back into active guidance.

---

### S0-D6 - Upgrade to Angular 21 with TypeScript 6.0 for future TS7 readiness

- ***What was built?***
  - `apps/web` upgraded from Angular 19 to Angular 21.2.5 with TypeScript 6.0.2.
  - Build output changed from `dist/web/` to `dist/` for a flatter directory structure.
- ***Why was it chosen?***
  - Angular 21 requires TypeScript >=5.9.0 and <6.1.0, which aligns with the master packet guidance to adopt TypeScript 6.x in preparation for TypeScript 7 (Go-based).
  - Angular 21 provides significant improvements over Angular 19 including better performance, improved type safety, and newer browser capabilities support.
  - TypeScript 6.0 offers better type inference, stricter checks, and prepares the codebase for TS7 which will use a Go-based compiler for faster builds.
- ***What boundaries does it own?***
  - Frontend dependency versions and TypeScript compatibility constraints.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Downgrading Angular or TypeScript versions outside their compatible ranges will cause build failures.
  - The build output path change means any external references to `dist/web/` need to be updated to `dist/`.
- ***What known edge cases or failure modes matter here?***
  - TypeScript 6.0.x is required for Angular 21. Angular 19 required TypeScript >=5.5.0 and <5.9.0.
  - When TypeScript 7 becomes available, Angular will need to upgrade to a version that supports it before we can adopt TS7.
  - The Angular CLI warnings about invalid workspace extensions (x_tldr, x_runtime_role) are cosmetic and do not affect functionality.
- ***Why does this work matter?***
  - It positions the frontend to adopt TypeScript 7 as soon as Angular supports it, aligning with the master packet roadmap.
  - Angular 21's performance improvements will speed up local development and CI builds.
  - Staying on latest LTS ensures security updates and long-term support from the Angular team.
- ***What capability does it unlock?***
  - Access to TypeScript 6 features including improved type narrowing and template literal types.
  - Future TS7 readiness once Angular adds support for the Go-based compiler.
  - Access to Angular 21's latest features and performance optimizations.
- ***Why is the chosen design safer or more scalable?***
  - Staying on latest Angular LTS ensures security updates and long-term support.
  - The flatter `dist/` structure is simpler and aligns with other Angular projects.
- ***What trade-off did the team accept?***
  - Must monitor Angular's TypeScript version requirements and upgrade Angular before adopting TS7.
  - The upgrade required careful version matching between Angular and TypeScript.
  - Need to update any external references to the old `dist/web/` path.

**Timeline for TS7 readiness:** Monitor Angular releases for TS7 support. Expected: Q4 2026 - Q1 2027 once Angular adds Go-based TypeScript 7 support.

---

### S0-D6 - Restore the reviewer-visible frontend from the active rebuild path

- ***What was built?***
  - `apps/web` now contains a working Angular 21 application that builds to static output in `dist/browser`.
  - `.github/workflows/web-pages.yml` deploys that output to GitHub Pages on push to main.
  - Documentation updated to reflect the honest deployment path.
- ***Why was it chosen?***
  - The repo needed an honest reviewer-visible frontend surface that comes from the active rebuild tree instead of pointing at deprecated legacy output.
  - The previous demo link was stale and did not accurately reflect the current state of the rebuild.
- ***What boundaries does it own?***
  - The frontend deployment path: where the static site comes from, how it builds, and how it publishes.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Reviewers may see stale or misleading demo content, and the public frontend path loses its single source of truth.
  - Any broken references to the old deployment path will cause 404s.
- ***What known edge cases or failure modes matter here?***
  - GitHub Pages is a static surface only — it does not support server-side rendering, API backends, or real-time features.
  - The workflow only triggers on changes to `apps/web/**` or the workflow file itself.
  - Later work that adds real backend services will need separate deployment workflows.
- ***Why does this work matter?***
  - It gives external reviewers, mentors, and funders a truthful live surface that reflects the active rebuild rather than archived prototype output.
  - It enables sprint reviews and demos without manual deployment steps.
- ***What capability does it unlock?***
  - Public demos, sprint reviews, and repo credibility through an honest static frontend that can be iterated in the active tree.
  - Automated deployment on every push to main ensures the demo is always up to date.
- ***Why is the chosen design safer or more scalable?***
  - One frontend source of truth prevents drift between what the repo claims and what reviewers see.
  - The workflow is triggered automatically, reducing human error in deployment.
- ***What trade-off did the team accept?***
  - The static site is intentionally honest about its limitations — it is a reviewer surface, not a production deployment.
  - No server-side rendering means limited functionality compared to a full production app.

---

### S0-D5 - Seed permanent container build surfaces for each deployable runtime

- ***What was built?***
  - `platform/docker/` now contains one permanent Dockerfile each for web, api, worker, and agent runtimes, all using `python:3.11-slim` as the base image.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - Each deployable unit needed one canonical container home before later work started adding inconsistent Dockerfiles or treating containerization as an afterthought.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - Container build surfaces for the web, api, worker, and agent deployable units.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Later work can create duplicate or conflicting Dockerfiles, and local development orchestration loses its canonical build targets.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - The Dockerfiles seed baseline structure only; they intentionally avoid provider-specific production tuning, secrets, or complex entrypoint logic that belongs in later deliverables.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It gives every service one buildable container surface from day one so local development, CI builds, and later deployment work have consistent targets.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - Local containerized development, CI image builds, and local k3s deployment all have stable Dockerfiles to reference.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - One Dockerfile per service prevents build duplication; consistent base images and layer structure make caching predictable.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - The seeded Dockerfiles are intentionally thin baselines rather than production-complete images, so later work must extend them.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D5 - Seed local Kubernetes manifests for each deployable runtime

- ***What was built?***
  - `platform/k8s/` contains one permanent manifest each for web, api, worker, and agent services, plus a migration job manifest for database migrations.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - The rebuild needed one honest local cluster topology before later work started inventing incompatible service definitions or deferring k8s integration until production.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - Local k3s topology surfaces for the web, api, worker, agent, and migrate deployable units.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Later work can create conflicting service definitions, and local development loses its canonical k8s deployment targets.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - The manifests seed baseline structure only with liveness/readiness probes; they intentionally avoid production-specific resource tuning, secrets, or complex rollout policies.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It gives every service one deployable k8s surface so local cluster testing and later production deployment work have consistent manifests.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - Local k3s cluster testing, health-probe integration with orchestrators, and consistent service naming across environments.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - One manifest per service prevents definition duplication; consistent probe paths and labeling make orchestrator behavior predictable.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - The seeded manifests are intentionally thin baselines rather than production-complete configurations, so later work must extend them.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D5 - Seed health, readiness, and request-correlation surfaces in active runtimes

- ***What was built?***
  - `apps/api/main.py`, `apps/worker/main.py`, and `apps/agent/main.py` now expose `/health` and `/ready` endpoints; `apps/api/middleware.py` provides X-Request-ID header correlation.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - The rebuild needed consistent health semantics and request tracing before later work started adding inconsistent probes or debugging without correlation IDs.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - Health/readiness endpoint semantics and request correlation vocabulary across the api, worker, and agent runtimes.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Later work can drift into incompatible health patterns, and debugging distributed requests becomes harder without consistent correlation IDs.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - Workers intentionally only expose `/health` since they have no external dependencies to wait for; the `/ready` endpoint for api depends on DB/cache availability.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It gives every service observable entry points so orchestrators can manage lifecycle properly and debugging can trace requests across services.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - Kubernetes liveness/readiness probes, request tracing across services, and consistent debugging vocabulary.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - Consistent endpoint paths and header names make orchestrator integration predictable and debugging tools work uniformly.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - The seeded endpoints return basic 200 responses; full dependency checking and detailed metrics belong to later deliverables.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D5 - Seed baseline observability vocabulary in durable documentation

- ***What was built?***
  - `docs/observability.md` now defines the baseline metrics vocabulary, runtime identity environment variables, and health endpoint conventions.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - The rebuild needed one shared observability vocabulary before later work started inventing service-specific metric names or inconsistent labeling schemes.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - Metrics naming conventions, runtime identity variables, and health endpoint semantics.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Later work can create inconsistent metric names, and monitoring dashboards become harder to aggregate across services.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - The document seeds baseline vocabulary only; it intentionally avoids implementing actual Prometheus exporters or complex metric collection that belongs in later work.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It gives every service one vocabulary to extend so monitoring, alerting, and debugging share consistent language.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - Consistent Prometheus-style metrics, runtime identity in logs, and unified health probe expectations.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - Shared vocabulary makes dashboard creation predictable and metric queries work across all services uniformly.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - The seeded docs describe vocabulary only; actual metric emission belongs to later implementation work.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D5 - Seed baseline resilience patterns in durable documentation

- ***What was built?***
  - `docs/resilience.md` now defines the baseline retry, timeout, and fallback patterns for background jobs and API calls.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - The rebuild needed one shared resilience vocabulary before later work started implementing inconsistent retry logic or timeout values across services.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - Retry configuration, timeout values, and dead-letter handling conventions.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Later work can create inconsistent retry behavior, making error handling unpredictable across services.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - The document seeds baseline vocabulary only; it intentionally avoids implementing actual retry libraries or circuit breakers that belong in later work.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It gives every service one pattern to extend so error handling, timeouts, and fallback behavior stay consistent.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - Consistent exponential backoff, timeout values, and dead-letter queue expectations.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - Shared patterns make error handling predictable and debugging across services consistent.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - The seeded docs describe patterns only; actual implementation belongs to later feature work.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D5 - Add local development orchestration script for service management

- ***What was built?***
  - `tools/scripts/dev.py` provides local service orchestration including running all services, running individual services, docker compose operations, and health status checks.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - The rebuild needed one obvious entrypoint for local development so team members don't invent different startup scripts or lose track of how to run services together.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - Local development command-line interface for managing the full local stack.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Developers can create ad hoc startup scripts that don't align with container or k8s configurations.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - The script intentionally stays focused on local development only; it does not become a general-purpose operations junk drawer.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It gives every developer one consistent way to start, stop, and check the local stack.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - Quick local iteration, consistent service startup across team members, and health checking during development.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - Single entrypoint prevents script proliferation; consistent flags and commands make onboarding predictable.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - The script covers local development only; production deployment belongs to CI/CD workflows and later platform work.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D5 - Seed edge policy vocabulary for cache, gateway, and request limits

- ***What was built?***
  - `platform/edge/` now defines baseline policy vocabulary including `cache.yaml` (GET/HEAD caching rules, bypass patterns), `gateway.yaml` (header forwarding, timeout defaults), and `limits.yaml` (request size, connection limits, rate placeholders).
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - The rebuild needed one shared edge policy vocabulary before later work started inventing service-specific caching rules or inconsistent timeout values.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - Edge policy vocabulary for caching behavior, gateway forwarding, and request limits.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Later work can create inconsistent caching rules, making behavior unpredictable across environments.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - The configs seed baseline vocabulary only with conservative defaults; they intentionally leave rate limiting disabled and avoid complex routing rules that belong in later work.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It gives every service one vocabulary to extend so edge behavior stays consistent across the platform.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - Consistent caching rules, predictable header forwarding, and baseline limit defaults for local development.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - Shared vocabulary makes edge configuration reviewable in one place; consistent naming prevents fragmentation.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - The seeded configs are intentionally conservative baselines; full edge behavior belongs to later platform work.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D4 - Make the PR narrative and every workflow edit subject to the documented merge gates

- ***What was built?***
  - `.github/workflows/docs-guard.yml` now blocks pull requests that leave `Summary`, `Why this change`, `Files and boundaries`, or `Verification` blank or placeholder-only, and `.github/workflows/protected-paths.yml` now treats any `.github/workflows/**` edit as a protected-path change.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - The earlier D4 slices documented PR-shape enforcement and workflow-path protection, but the actual automation still left those two gaps open, which meant reviewers could trust rules that were not fully enforced.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - The minimum reviewer-facing PR narrative every change must provide, and the protected-path boundary for all workflow automation under `.github/workflows/**`.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Pull requests can slip through with vague review context, workflow changes can avoid the protected-path acknowledgement gate, and the repo's documented merge posture can drift away from reality again.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - The docs gate must still keep `Docs and ADR delta` conditional on governed changes instead of requiring ADR churn for every PR, and the workflow matcher must stay broad enough to catch new workflow files without producing opaque failures.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It closes the last D4 enforcement gap between the documented PR contract and the actual merge-blocking automation.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - Reviewers can rely on every PR carrying a real summary and verification story, and workflow edits now consistently trigger the protected-path review path.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - Extending the existing D4 workflows keeps the logic in the same audited homes, preserves clear failure messages, and automatically covers future workflow files without another policy split.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - More PRs will now fail fast on incomplete narrative or workflow-acknowledgement details, so contributors must keep the template sections and protected-path notes up to date before review.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D4 - Align the OpenCode bash allowlist with the CLI commands the repo actually needs

- ***What was built?***
  - `opencode.json` now explicitly allows `printf *` and the spaced `git log *` matcher that the current repo-control workflows already rely on.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - The shell allowlist had drifted from the real command shapes the governed repo-control flow uses, which could block valid local automation or force awkward command rewrites.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - OpenCode bash-command permissions for low-risk local inspection helpers that PM and repo-control workflows need during governed execution.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Valid local command paths can be denied unexpectedly, and repo-control automation can drift toward less direct shell patterns just to satisfy stale permission rules.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - The allowlist must stay narrow; adding broad shell permissions would weaken guardrails, while overly specific stale patterns would keep breaking legitimate commands.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It keeps the tool policy aligned with the commands the repo actually expects during governed execution.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - PM and related repo-control flows can keep using the expected `git log` and formatting paths without permission mismatches.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - Small, explicit allowlist repairs preserve the deny-by-default posture while reducing avoidable friction in everyday governed workflows.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - The repo must keep reviewing shell-allowlist changes carefully because even tiny permission edits affect operator behavior across the tool surface.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D4 - Rename the root legal files to explicit markdown filenames and repair the repo references

- ***What was built?***
  - The root legal docs now live as `LICENSE.md` and `NOTICE.md`, and the matching repo references in `README.md`, `SECURITY.md`, `GOVERNANCE.md`, `CLA.md`, and planning docs were updated to the new explicit markdown filenames.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - The repo already treats these as markdown documents, so the filename change keeps the root legal surfaces explicit and prevents broken links after the human rename landed.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - Root legal-document naming, the canonical repo references to those files, and the planning-tree examples that describe the committed repo shape.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Root docs and planning material can point at missing files, contributors can miss the canonical legal text, and the repo can drift between actual filenames and documented references.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - The rename must keep every root-policy reference aligned at once; partial link updates would leave the repo in a broken but plausible state.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It keeps the legal boundary readable and prevents contributor-facing docs from pointing at stale filenames after the rename.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - Later legal or governance updates can treat the markdown files as the stable homes without carrying filename ambiguity forward.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - Explicit markdown filenames match the repo’s document surfaces, reduce broken-link risk, and make future doc tooling behavior easier to explain.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - Existing references had to be updated together, so even a small rename carried cross-doc coordination cost.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D4 - Replace the misleading pages deploy stub with honest release-preparation scaffolding

- ***What was built?***
  - `.github/workflows/cd.yml` now runs `tools/scripts/release.py --ci prepare`, `tools/scripts/release.py` emits release-readiness metadata without deploying anything, and the old Pages deploy workflow was retired so D4 no longer implies D5-level delivery maturity.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - The repo needed a visible release-control seam in Sprint 0, but the existing Pages deploy workflow oversold deployment maturity and hid too much behavior in YAML.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - Manual release-preparation control flow, honest release-readiness messaging, and the boundary that D4 prepares releases while D5 will own real rollout behavior.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Reviewers and operators can mistake release scaffolding for a real deployment pipeline, workflow names can promise runtime behavior the repo does not own yet, and future rollout work can lose one obvious place to start from.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - The workflow must stay manual-only, the script must reject deploy requests clearly, and later D5 work must extend this seam instead of reintroducing a second release path.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It gives the repo a truthful release-control checkpoint before runtime parity exists, which keeps CI/CD vocabulary aligned with actual repo maturity.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - Later D5 rollout work can extend one named release seam instead of starting from a misleading Pages deployment stub.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - A thin workflow wrapper plus one script seam keeps release policy explainable, reviewable, and easy to roll back while the platform story is still forming.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - The repo now has a release workflow that intentionally stops short of deployment, so operators must accept a more modest but honest control loop until D5 lands.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D4 - Add a dedicated reporter lane and a local coordination reminder loop

- ***What was built?***
  - `.opencode/agents/reporter.md` now defines a packet-only coordination lane, PM can route packet normalization to it, and `tools/scripts/coordination.py` now exposes a local `watch` runner that reuses the shared reminder runtime every minute instead of creating a second coordination engine.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - D4 needed stronger progress-report automation, but adding another script or machine-specific scheduler artifact would have split coordination logic and made local-only reporting harder to explain and review.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - Reporter-owned packet normalization, the PM handoff boundary for coordination formatting, and the local reminder loop that surfaces overdue scopes while keeping all coordination policy inside `tools/scripts/coordination.py`.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - PM and subagents can drift into competing packet formats, overdue scopes can stop surfacing consistently, and local operators can lose the one obvious entrypoint for recurring coordination checks.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - The reporter lane must stay narrow enough that it never takes PM orchestration ownership, the watch loop must stay honest about being local-only, and overdue output must remain per-scope so one stale workstream does not hide another healthy one.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It turns the coordination packet into a first-class repo-control contract and gives active work a repeatable local reminder loop before more agents or workstreams overlap.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - Later scopes can reuse one normalized reporting lane and one minute-level reminder loop instead of rebuilding coordination format or scheduling behavior ad hoc.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - Reusing the shared coordination runtime keeps policy in one home, reduces drift across PM and subagents, and lets local schedulers call one stable command instead of proliferating wrappers.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - Operators still need to choose how to launch the local reminder loop on their machines, so the repo documents safe entrypoints without pretending a committed machine-specific scheduler file would generalize cleanly.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D4 - Separate docs, protected-path, and CLA gates into explicit pull-request workflows

- ***What was built?***
  - `.github/workflows/docs-guard.yml`, `.github/workflows/protected-paths.yml`, and the updated `.github/workflows/cla-check.yml` now enforce docs and ADR coverage for governed changes, protected-path acknowledgement for high-blast-radius files, and the repository-owner CLA exception already documented in `CLA.md`.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - D4 needed merge-blocking automation for reviewer-visible PR obligations, but folding every rule into `repo-verify.yml` or `tools/scripts/verify.py` would have blurred ownership and made the workflow surface harder to explain.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - Pull-request body contract enforcement for docs and ADR deltas, protected-path acknowledgement across repo-control workflows and the other protected-path categories named in `AGENTS.md`, and CLA phrase handling for outside contributors versus repository-owner-authored PRs.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Governed repo-control changes can land without durable reasoning, protected files can merge without explicit risk acknowledgement, or the CLA gate can block the wrong authors.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - The workflows must use the repo's exact protected-path vocabulary, distinguish repo-control workflows from true release scaffolding, avoid treating `docs/coordination/**` as a merge target, and keep the owner exception narrow enough that outside contributors still need the exact phrase from `CLA.md`.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It turns the PR template obligations into explicit merge gates instead of leaving docs, protected-path notes, and CLA nuance to reviewer memory.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - Later sprint work can rely on clear PR-level guardrails for governed changes before release scaffolding and runtime parity work land.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - Separate workflows keep each gate explainable, reduce policy overlap with the central repo verifier, and make later changes easier to review and roll back.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - The repo now carries more workflow files and PR-body contract logic, so later governance edits must keep the template, docs, and workflow checks aligned.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D4 - Keep repo verification policy in one central script seam

- ***What was built?***
  - `tools/scripts/verify.py`, `.github/workflows/repo-verify.yml`, and `docs/testing.md` were aligned so merge-blocking repo verification stays owned by one central Python entrypoint and the workflow remains a thin CI wrapper around it.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - D4 needs automation that blocks bad changes before merge, but pushing policy logic into YAML would duplicate rules, hide failure reasoning, and make later workflow slices harder to review.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - The shared repo-verification seam for script explainability, central workflow delegation, and CI-safe local-versus-CI behavior.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - The repo-verify workflow can drift into a second policy engine, contributors can get inconsistent failure output, and later D4 workflows can start re-implementing checks in parallel.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - CI checkouts do not include local-only coordination artifacts, so the verifier must keep that case explicit, and the workflow must stay thin enough that docs-guard and protected-path slices can add separate enforcement without overlap.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It keeps D4 automation explainable and preserves one obvious place to extend repo verification as the governed rebuild grows.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - Later workflows can compose around a stable central verifier instead of guessing which checks belong in Python versus YAML.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - A single verifier seam reduces duplicate policy, keeps failure messaging consistent, and lowers the review burden when later quality gates land.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - The repo verifier now owns a clearer contract with CI, so later changes to `.github/workflows/repo-verify.yml` must preserve that thin-wrapper boundary instead of treating the workflow as a general automation scratchpad.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D4 - Standardize the PR review contract and centralize the CLA owner exception

- ***What was built?***
  - The D4 planning packet, `.github/pull_request_template.md`, `.opencode/commands/pr-prepare.md`, `CLA.md`, and `CONTRIBUTING.md` were aligned around one reviewer-facing PR structure, one canonical CLA confirmation phrase, and one documented repository-owner exception for the CLA phrase check.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - The repo already had partial PR and CLA guidance, but the template, PR-prep command, and contributor docs could drift from each other and force workflow automation to guess which wording was canonical.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - Reviewer-facing PR narrative structure, canonical CLA confirmation wording, and the documentation boundary between outside contributors and repository-owner-authored PRs.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - PR preparation can produce the wrong sections, workflow automation can block the wrong authors, and reviewers can lose a stable contract for summary, verification, docs, and protected-path notes.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - Owner-authored PRs need a narrow exception without weakening the CLA requirement for outside contributors, and the PR template plus PR-prep command must stay structurally identical enough to avoid future drift.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It gives the later D4 workflow changes one durable policy source instead of scattering PR and CLA semantics across markdown files, chat, and YAML.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - Later automation can enforce PR structure and CLA rules against a stable documented contract.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - Centralizing the policy details reduces duplicate rule text and makes later workflow or script changes easier to audit for drift.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - The repository now carries a slightly more explicit PR and CLA narrative, which requires future repo-control edits to keep the shared structure in sync.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D3 - Reconcile planning drift to current repo reality

- ***What was built?***
  - A repo-control rule set that treats the committed permanent structure as canonical when older planning packets drift, including updates in `AGENTS.md`, `docs/repo.md`, `README.md`, `.opencode/commands/generate.md`, `.opencode/commands/orchestrate.md`, and `docs/planning/sprint-0/d3-agent-docs.md`.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - The repo had already converged on permanent control surfaces, so recreating packet-era names would have duplicated governance files and pushed agents toward stale targets.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - Planning translation, durable-doc stubbing decisions, and repo-control path selection across the active rebuild surfaces.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Agents can start generating duplicate files, reviving stale packet-era homes, or describing the active tree inaccurately during planning and execution.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - A planning packet can still differ materially from the repo in ways that affect ownership or safety; those cases must escalate instead of being silently normalized.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It keeps the rebuild honest about what is already real in the repo and prevents governance drift from compounding with each later deliverable.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - Safe refinement of planning docs and agent execution without throwing away already-committed permanent structure.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - Reusing the committed structure reduces duplicate homes, review ambiguity, and agent confusion as more lanes work in parallel.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - Older planning language now needs periodic reconciliation instead of being treated as immutable even after the repo evolves.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D3 - Make the implementation workflow architect-first and ops-gated

- ***What was built?***
  - The governed lane order now requires `architect` before `developer` or `designer` on implementation-bearing task scopes, and `ops` after reviewer and integrator but before librarian closeout, PR prep, or merge-ready status.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - Implementation strategy and operational hygiene were too easy to skip when the workflow jumped straight from PM framing into coding or docs closeout.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - Task-scope execution order, TDD and scaffolding handoff expectations, and the operational review gate for implementation-bearing diffs.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Boilerplate can be designed ad hoc inside developer patches, and review can miss reliability, blast-radius, or workflow-hygiene issues such as leaked local runtime artifacts.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - Docs-only tasks can bypass architect and ops, but implementation-bearing tasks cannot; the workflow must keep that distinction explicit.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It turns architecture and operations review from best-effort habits into deterministic gates the human can rely on.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - TDD-shaped implementation handoffs, earlier failure-mode thinking, and consistent ops checks before work is treated as mergeable.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - As more lanes contribute in parallel, explicit sequencing reduces hidden assumptions and catches operational drift before humans clean it up manually.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - The path to merge-ready status becomes slightly longer because implementation-bearing work must clear more explicit gates.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D3 - Consolidate the governed repo-control surface under root and `.opencode/`

- ***What was built?***
  - `AGENTS.md`, `opencode.json`, `.opencode/agents/**`, `.opencode/commands/**`, `.opencode/rules/**`, and `.opencode/skills/**` were established or aligned as the canonical control surface for lane behavior, permissions, routing, and review expectations.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - A governed multi-agent rebuild needs one durable operating contract instead of scattered instructions hidden in chat or one-off notes.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - Repo-level agent permissions, lane responsibilities, orchestration commands, reusable rules, and reusable skills for active rebuild work.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Humans and agents lose a shared source of truth for safe paths, coordination cadence, review gates, and escalation behavior.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - Hotspot-file wording changes act like behavior changes, so small text edits can materially alter how agents execute or escalate work.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It makes the operating theory inspectable, reviewable, and reusable instead of depending on conversational memory.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - Deterministic routing, reusable commands, and permission-aware lane behavior that later sprints can extend safely.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - Centralized repo-control docs reduce rule duplication and help parallel contributors inherit the same behavioral contract.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - The repo now carries heavier governance documentation that must be kept current as behavior evolves.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D3 - Standardize live coordination cadence and stable scope artifacts

- ***What was built?***
  - The coordination system now uses stable scope-based files, a shared six-minute reporting packet, dashboard refresh rules, and reusable templates under `docs/templates/coordination/**` with matching guidance in `.opencode/rules/coordination-standards.md`.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - Parallel human and agent work becomes hard to resume safely when status lives only in chat or in ad hoc filenames.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - Coordination artifact naming, heartbeat cadence, shared status packet fields, and the human-visible active dashboard rules.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Resume and handoff flows become non-deterministic, and later agents must reconstruct state from chat archaeology.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - Coordination files are gitignored live artifacts, so they must stay stable enough to resume work even though they are not durable merge history.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It keeps in-flight work visible and reduces the risk that a later agent or human misses blockers, active paths, or the next checkpoint.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - Reliable resume, handoff, and checkpoint behavior across scoped tasks and deliverables.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - Stable naming and repeated packet fields make coordination machine-readable and human-scannable at the same time.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - Agents must spend time updating coordination artifacts during work instead of treating status as optional overhead.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D3 - Seed the durable docs spine for architecture, agent workflow, testing, operations, and ADRs

- ***What was built?***
  - `docs/architecture.md`, `docs/agent.md`, `docs/testing.md`, `docs/operations.md`, and `docs/adr.md` were created as the permanent technical-doc surfaces that later changes must extend in place.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - Shared theory was going to fragment across PR text and chat unless the rebuild established exact durable homes early.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - Cross-cutting technical explanation, workflow narrative, testing posture, operations posture, and the single consolidated ADR record.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Contributors start inventing side-channel docs, and reviewers lose a stable place to confirm the current architecture and operating theory.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - Stub docs can become misleading if they overclaim current repo maturity, so they must stay thin until later deliverables add concrete runtime detail.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It gives every later change a permanent home for shared understanding instead of making documentation optional cleanup.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - ADR-coupled delivery and durable technical explanation that can keep pace with the rebuild.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - Extending one durable doc spine is easier to review and maintain than chasing many ad hoc notes across the repo.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - Some docs are intentionally skeletal now and need disciplined later extension rather than one-shot completion.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D2 - Seed durable runtime starter files under `apps/`

- ***What was built?***
  - Permanent starter files were seeded for the active runtime homes under `apps/web`, `apps/api`, `apps/domain`, `apps/worker`, and `apps/agent`, with TL;DR headers and narrow boundary narratives.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - The rebuild needed one obvious home for each deployable surface before feature work could begin without path drift.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - Deployable runtime ownership for the experience, contract, domain, worker, and agent surfaces of the active rebuild tree.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Later work can splinter across duplicate app roots or treat the prototype archive as the path of least resistance.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - Stub files must stay TL;DR-only until real implementation lands, otherwise comments and fake boilerplate turn into explainability debt.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It creates real extension points for later sprints instead of leaving ownership implied.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - Safe Sprint 1+ implementation work that can extend existing runtime homes instead of inventing parallel structures.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - Stable starter files reduce future relocation churn and make ownership visible before business logic arrives.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - The repo carries many thin stub files early so later work can grow in place without renaming or moving foundational paths.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D2 - Seed shared seam starter files under `shared/`

- ***What was built?***
  - Permanent starter files were created for shared contracts, schemas, adapters, and deterministic test support under `shared/contract`, `shared/schema`, `shared/adapter`, and `shared/testkit`.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - Cross-cutting concepts needed one shared home before app-local implementations started duplicating schema, adapter, or test vocabulary.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - Shared transport primitives, reusable shape definitions, swappable capability ports, and deterministic support for future verification layers.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Contract and adapter concepts can leak into app-local folders, creating duplicate ownership and harder refactors.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - Shared seams can become junk drawers if later work adds vague helpers instead of capability-based surfaces.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It gives the rebuild one place to centralize concepts that genuinely cross runtime boundaries.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - Reuse-first implementation across apps without forcing every runtime surface to define its own duplicate vocabulary.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - A single shared seam layer makes later contract, adapter, and testing evolution more reviewable and less repetitive.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - Shared surfaces now need stricter review so they stay capability-based instead of becoming generic dumping grounds.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D1 - Freeze the validated prototype under `legacy-v0/`

- ***What was built?***
  - The old runtime tree was relocated under `legacy-v0/` and documented as preserved reference material rather than the active base for the rebuild.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - The prototype had already validated the product loop, but scaling it in place would have carried forward ambiguous ownership and prototype-era coupling.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  -  The archival boundary between historical proof and active rebuild work.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - Contributors can mistake the prototype for the active architecture and keep adding new work to archived paths.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  -  Useful ideas still exist in the archive, but they must be ported deliberately instead of extended in place.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It preserves the evidence of what already worked while clearing the root for a more intentional rebuild.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - Later sprint work can reference the prototype without being trapped by its structure.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - A hard archive boundary prevents legacy coupling from quietly reentering active development.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - Anyone reusing prototype ideas now has to do explicit extraction work instead of shortcutting through the old folders.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.

---

### S0-D1 - Rewrite the repo narrative around active versus archived paths

- ***What was built?***
  - `README.md`, `docs/repo.md`, `docs/legacy-v0.md`, and `legacy-v0/README.md` were rewritten so the root tells a single story about the active rebuild surfaces and the archived prototype.
  - It also established one durable home for this slice so later work can extend it in place instead of recreating the same decision elsewhere.
- ***Why was it chosen?***
  - Moving files alone would not have been enough if the repo narrative still implied that the prototype layout was active.
  - The team needed an explicit Sprint 0 baseline here before parallel work made this surface drift or stay chat-only.
- ***What boundaries does it own?***
  - Contributor guidance, root navigation, path-ownership language, and the shared terminology for archive versus rebuild surfaces.
  - It also names the canonical review seam humans and agents should treat as the stable home for this decision.
- ***What breaks if it changes?***
  - New humans and agents can still infer the wrong build path even if the filesystem technically contains the right folders.
  - Related docs, automation, and later sprint slices would also drift because they already rely on this decision as a stable baseline.
- ***What known edge cases or failure modes matter here?***
  - Narrative docs can drift from repo reality if later structural changes are not reflected in the same durable guidance files.
  - The slice stays intentionally narrow, so broader production hardening and adjacent concerns remain deferred to later deliverables.
- ***Why does this work matter?***
  - It makes path ownership explicit enough that a contributor can choose the right surface without external explanation.
  - It keeps Sprint 0 honest about current repo reality instead of leaving this surface implicit or dependent on chat archaeology.
- ***What capability does it unlock?***
  - Safer onboarding and safer agent planning because the repo tells the truth about where new work belongs.
  - Later changes can now build on one explicit seam instead of inventing competing homes or vocabulary.
- ***Why is the chosen design safer or more scalable?***
  - Shared terminology across root docs reduces ambiguous guidance as more durable docs and active surfaces are added.
  - Keeping the decision explicit also lowers review cost because contributors can reason about one owned surface at a time.
- ***What trade-off did the team accept?***
  - Repo narrative docs now require deliberate upkeep whenever governance or structure changes.
  - The repo now carries more upfront structure and documentation here, so later work must keep the matching surfaces aligned.
