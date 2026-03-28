---
name: ui-ux-review
description: Review Food Run UI and UX for hierarchy, clarity, trust, accessibility, responsiveness, and polished minimalist execution before implementation, release, or demo.
---

# UI/UX Review

## Purpose

Use this skill to critique Food Run interfaces before they ship, before they are demoed, or before implementation work is accepted as complete.

This skill defaults to critique first. Do not rewrite code immediately unless the task explicitly asks for implementation.

## Always Open First

1. `AGENTS.md`
2. `docs/design-system/MASTER.md`
3. The relevant page file in `docs/design-system/pages/`
4. `docs/design-system/review-rubric.md`
5. `docs/design-system/anti-patterns.md`
6. Any supporting design-system file needed for the surface being reviewed

## What This Skill Checks

- Task clarity
- Information hierarchy
- Primary action clarity
- Secondary action restraint
- Spacing and layout rhythm
- Typography discipline
- Trust and scope honesty
- Form usability
- Empty, error, and helper text quality
- Responsive behavior
- Accessibility basics
- Consistency with the design system
- Polish of subtle details
- Reduction of legacy card artifacts where they no longer serve the user

## Core Review Stance

Food Run should not be judged by flashy novelty.

It should be judged by whether it feels:
- Calm
- Obvious
- Trustworthy
- Repeatable
- Polished
- Lightly playful without becoming chaotic

## When to Use This Skill

Use this skill:
- Before implementation
- After implementation
- Before checkpoint commits
- Before pull-request review
- Before demos
- When a surface works technically but still feels noisy, unclear, or immature

## Operating Method

### 1) Identify the Dominant Job

State:
- What the user is trying to do
- What the UI currently emphasizes
- Whether those two things match

### 2) Inspect Hierarchy

Check:
- What draws the eye first
- What the user reads second
- Whether the most important action is visually obvious
- Whether the page has too many competing regions

### 3) Inspect Friction

Check:
- Unnecessary steps
- Vague labels
- Too much text before action
- Unclear system state
- High memory load
- Fragile or hidden affordances

### 4) Inspect Trust

Check:
- Scope honesty
- Precision of claims
- Realism of state labels
- Clarity of limitations
- Whether the copy feels grounded and credible

### 5) Inspect Surface Discipline

Check:
- Whether boxed surfaces are truly needed
- Whether the page is carrying old prototype card habits
- Whether spacing could replace a border or filled panel
- Whether empty states are over-boxed
- Whether repeated bordered containers flatten the hierarchy

### 6) Inspect Polish

Check:
- Spacing consistency
- Optical alignment
- Typography relationships
- State styling
- Contrast and focus treatment
- Mobile and desktop rhythm

## Severity Levels

### Critical
Blocks task success, breaks trust, causes serious confusion, or introduces major accessibility problems.

### Major
Substantially slows comprehension, creates preventable friction, or weakens the page’s primary task.

### Moderate
Noticeably noisy, inconsistent, or under-polished, but still usable.

### Minor
A cosmetic or low-risk polish issue that does not substantially affect success.

## Required Output Shape

1. Overall verdict
2. Dominant job assessment
3. Critical findings
4. Major findings
5. Moderate findings
6. Minor findings
7. Smallest good fixes
8. Optional implementation plan
9. Ship / do not ship yet recommendation

## Browser and Rendered-State Behavior

If rendered inspection is available, also check:
- Hover
- Focus-visible
- Active
- Disabled
- Loading
- Error
- Empty states
- Mobile viewport behavior
- Desktop viewport behavior

If rendered inspection is unavailable, state clearly that the review is code- and static-structure-based.

## Anti-Pattern Reminders

Flag aggressively:
- Card overuse
- Call-to-action overload
- Decorative clutter
- Generic AI SaaS styling
- Unclear status language
- Incomplete-state overclaiming
- Type hierarchy collapse
- Weak contrast
- Hover-only discoverability
- Layouts that rely on guessing instead of guidance

## Done Criteria

This skill succeeds when the review gives:
- Evidence-based critique
- Severity-ranked findings
- Smallest realistic fixes
- Alignment to Food Run’s actual product maturity
- Guidance specific enough to act on without guesswork
- Explicit direction on whether leftover card artifacts should be removed, softened, or kept