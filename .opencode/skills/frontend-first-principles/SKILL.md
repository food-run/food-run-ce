---
name: frontend-first-principles
description: Design and implement Food Run frontend work from first principles using a refined minimalist system, a playful-comic token language, and production-grade restraint.
---

# Frontend First Principles

## Purpose

Use this skill when designing or implementing Food Run frontend work that should feel calm, polished, playful, trustworthy, and ready for live users.

This skill is for disciplined UI work. It is not for decorative experimentation, trend-chasing, or generic “modern SaaS” output.

## Always Open First

1. `AGENTS.md`
2. `docs/design-system/MASTER.md`
3. The relevant page file in `docs/design-system/pages/`
4. Any supporting file in `docs/design-system/` that directly affects the task
5. Any active planning packet or implementation document for the current scope

## Food Run Design Thesis

Food Run should feel like elegant minimalist execution built on a playful-comic token system.

That means:
- Clean layout
- Strong spacing rhythm
- Careful typography
- Subtle, high-quality interaction states
- Warm personality without childish chaos
- Direct language
- No fake product confidence
- No generic AI styling
- Fewer unnecessary surfaces

## Current Repo Reality

The current reviewer-facing frontend still includes several boxed surface and card-like artifacts from the validated prototype and early reviewer shell.

Use this skill to reduce that carryover deliberately:
- Keep only the surfaces that improve comprehension or scope
- Remove or soften decorative containers
- Prefer spacing, rhythm, and hierarchy over constant borders and filled panels
- Treat card reduction as a design-system alignment task, not merely a cosmetic cleanup

## When to Use This Skill

Use this skill when:
- Creating a new page or section
- Revising an existing page layout
- Improving hierarchy, spacing, typography, or interaction states
- Refining shared styling tokens
- Making a flow easier to scan, understand, or trust
- Adapting the current reviewer shell toward a production MVP surface
- Reducing legacy v0 card artifacts and excessive surface nesting

## Do Not Use This Skill When

Do not use this skill when:
- The task is purely backend
- The task is purely bug triage with no design or UX consequence
- The request is critique-only and does not require implementation
- The work would imply a backend capability that does not exist
- The work would introduce a large new design primitive without a clear need

## Operating Method

### 1) Define the Dominant Job

Restate the page or region’s dominant job in one sentence.

Questions to answer:
- What is the user trying to do here?
- What must they understand before they act?
- What is the primary action?
- What is secondary?
- What can be removed, deferred, collapsed, or softened?

### 2) Reduce Before Styling

Before changing colors, components, or visual polish:
- Remove nonessential surfaces
- Remove duplicated labels
- Remove explanatory text that delays action
- Remove competing calls to action
- Remove false precision or false confidence
- Remove card artifacts that exist only because the old prototype used them

### 3) Preserve the Brand Correctly

Food Run may be playful and comic-leaning, but the implementation must still feel disciplined and production-grade.

Preserve:
- Warmth
- Energy
- Rounded friendliness
- Expressive but readable typography
- Accent-color personality

Avoid:
- Toy-like visual clutter
- Arbitrary motion
- Over-decoration
- Too many loud surfaces
- Inconsistent type sizing
- Novelty that slows comprehension

### 4) Reuse Before Inventing

Prefer:
- Existing shell structure
- Existing tokens
- Existing spacing rhythm
- Existing button and input patterns
- Existing routed-page framing through shared helpers

Do not invent a new shared primitive unless it is meaningfully unique.

A primitive is meaningfully unique only if at least one of the following is true:
- It serves a different user-facing responsibility
- It has a different state model
- It has a different structural role
- It has a different operational constraint
- It has a different interaction pattern

### 5) Reduce Surface Count Deliberately

Food Run’s current reviewer shell has more bordered containers and card-like surfaces than the refined design system should carry into Sprint 1.

Default to:
- Fewer bordered boxes
- Fewer filled panels
- Fewer nested containers
- Fewer “empty-state cards” when a simpler section treatment would work
- Clearer visual grouping through spacing instead of repeated surfaces

A bordered surface should remain only when it clearly improves:
- Scope
- Separation
- Scannability
- Local action clarity
- Trust

### 6) Implement With Restraint

Default to:
- Fewer containers
- Fewer borders
- Fewer colors in one view
- Fewer font sizes
- Stronger spacing relationships
- Cleaner grouping
- More semantic labels
- More obvious primary action

### 7) Protect Scope Honesty

Never style unfinished product behavior as if it is already real.

Examples:
- Do not imply recipe parsing confidence that does not exist
- Do not imply sync or persistence that does not exist
- Do not imply AI reasoning quality that does not exist
- Do not imply planner or shopping intelligence beyond the current logic
- Do not let placeholder states feel more powered than they are

### 8) Verify Before Finishing

Check:
- Hierarchy
- Surface count
- Spacing rhythm
- Typography
- Focus and hover states
- Disabled and loading states, if relevant
- Mobile layout
- Desktop layout
- Trustworthiness of copy
- Consistency with the design-system documents

## Required Output Shape

When using this skill, produce:
1. Dominant job summary
2. Visual direction summary
3. Core hierarchy decisions
4. Surface-reduction decisions
5. Token and styling decisions
6. Files to change
7. Why the result is simpler, clearer, or more trustworthy
8. Risks, follow-ups, or constraints

## Implementation Defaults

- Prefer semantic token edits over one-off overrides
- Prefer updating shared styles only when the pattern is genuinely shared
- Prefer smaller diffs
- Preserve reviewer-shell honesty unless the work is explicitly production-facing
- Keep the code explainable line by line

## Anti-Pattern Reminders

Do not:
- Nest cards inside cards without a strong reason
- Create more than one primary call to action in a local region
- Use decorative icons as substitute hierarchy
- Add large text blocks before the user can act
- Use placeholder text as the only label
- Add gratuitous gradients or AI-style chrome
- Turn a straightforward workflow into a dashboard
- Use playful fonts in ways that reduce legibility
- Keep prototype-era card shells that no longer improve clarity

## Done Criteria

This skill succeeds when the UI is:
- Easier to scan
- Easier to trust
- Easier to act on
- More visually disciplined
- Still recognizably Food Run
- More ready for live users without overstating product maturity
- Less dependent on leftover card artifacts from the prototype