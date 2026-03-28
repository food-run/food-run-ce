# Food Run Design System

## Purpose

This folder is the canonical design-system knowledge base for Food Run.

It exists to keep the repository DRY and to make design reasoning reusable across:
- Implementation work
- Reviews
- Demos
- Future sprint planning
- Agent skills
- Human collaboration

The design system should guide both visual decisions and product-surface decisions. It is not just a style guide.

## Design Thesis

Food Run should feel like elegant minimalist execution built on a playful-comic token system.

That means the product should feel:
- Warm
- Clear
- Trustworthy
- Efficient
- Lightly expressive
- Visually disciplined
- Ready for real use

It should not feel:
- Noisy
- Toy-like
- Generic SaaS
- Over-decorated
- Dashboard-heavy
- Overconfident about unfinished features

## Folder Structure

- `MASTER.md`  
  The short, high-signal source of truth. Read this first.

- `principles.md`  
  First-principles workflow for designing or revising a surface.

- `product-lens.md`  
  Food Run-specific UX and trust rules.

- `typography.md`  
  Type-system rules, pairings, scale, and usage guidance.

- `spacing-layout.md`  
  Layout rhythm, grouping, spacing discipline, and surface reduction.

- `color-theme.md`  
  Palette roles, theme behavior, and semantic color rules.

- `interaction-states.md`  
  State design for buttons, inputs, surfaces, and transitions.

- `responsive-accessibility.md`  
  Mobile-first behavior and accessibility expectations.

- `content-voice.md`  
  Writing rules for labels, errors, helper text, and empty states.

- `components.md`  
  Shared primitives and rules for when they should or should not be used.

- `anti-patterns.md`  
  Common design failures to avoid.

- `review-rubric.md`  
  Review framework used by UI and UX audits.

- `implementation-playbook.md`  
  Practical mapping from design decisions to repository changes.

- `pages/*.md`  
  Page-specific overrides. These do not replace the global system.

## How to Use These Documents

### For Implementation

1. Read `MASTER.md`
2. Read the relevant page file in `pages/`
3. Read any supporting global file needed for the task
4. Restate the dominant user job
5. Reduce before styling
6. Implement with restraint
7. Verify against `review-rubric.md`

### For Review

1. Read `MASTER.md`
2. Read the relevant page file
3. Read `review-rubric.md`
4. Read `anti-patterns.md`
5. Audit the page against the system and current product truth

## Master and Page-Override Model

`MASTER.md` is the canonical global source.

A page file may:
- Define the page goal
- Define the primary action
- Define required information
- Define page-specific states or layout behavior
- Define page-specific constraints

A page file may not:
- Restate the full design system
- Silently contradict `MASTER.md`
- Redefine global typography, spacing, color, or component rules without a documented reason

## Scope-Honesty Rule

Food Run surfaces must reflect actual product truth.

Do not design unfinished capabilities as if they already exist.

Examples of prohibited overclaiming:
- Fake confidence scores
- Fake sync states
- Fake background jobs
- Fake AI reasoning quality
- Fake household coordination sophistication

## Surface-Reduction Rule

The current reviewer-facing frontend still carries multiple bordered surface and card patterns from the earlier prototype and reviewer shell.

Sprint 1 should reduce that surface density.

The goal is not to remove every bordered container blindly. The goal is to keep only the surfaces that improve:
- Comprehension
- Scannability
- Scope
- Local action clarity
- Trust

## Sprint 1 Priority

For the deployed MVP with live users, the design system should optimize for:
- Obvious next steps
- Fast scanning
- Trustworthy copy
- Stable responsive behavior
- Strong spacing and typography
- Accessible defaults
- Low-friction correction and recovery
- Fewer unnecessary card-like surfaces

## Maintenance Rules

- Prefer updating this folder over duplicating design logic elsewhere
- Keep the master short and high-signal
- Keep subdocuments focused
- Keep page files local and bounded
- When design reasoning changes, update these documents before or with implementation