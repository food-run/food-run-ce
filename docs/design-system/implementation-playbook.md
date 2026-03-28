# Implementation Playbook

## Purpose

This file maps design-system decisions to practical repository changes.

Use it to keep implementation work bounded, DRY, and consistent with the repository structure.

## General Workflow

1. Read `AGENTS.md`
2. Read `docs/design-system/MASTER.md`
3. Read the relevant page file in `docs/design-system/pages/`
4. Identify whether the change is:
   - Token-level
   - Shared-style-level
   - Page-level
   - Component-level
5. Prefer the smallest level that solves the problem
6. Verify against `review-rubric.md`

## Change Classification

### Token-Level Change

Use when:
- The system needs a semantic update
- The spacing scale needs adjustment
- Type roles need refinement
- Color roles need tuning
- Shared radius or shadow treatment needs refinement

Typical code impact:
- Theme-level styles
- Token declarations
- Possibly small component ripple effects

### Shared-Style Change

Use when:
- Multiple pages or primitives need the same refinement
- Interaction states are inconsistent
- Button or input behavior needs improvement
- Shell spacing or common layout logic needs adjustment
- Surface density needs reduction across multiple routes

Typical code impact:
- Shared styling files
- Possibly base component structure

### Page-Level Change

Use when:
- One route has a specific hierarchy problem
- One page needs a clearer action structure
- Page-specific spacing or grouping needs refinement
- Current UI problem is local, not systemic
- A page still contains prototype-era card artifacts that should be reduced locally

Typical code impact:
- Page view logic
- Page markup
- Page-specific styles
- Local documentation in `docs/design-system/pages/`

### Component-Level Change

Use when:
- A shared primitive is genuinely missing
- A shared primitive has a repeated usability problem
- Multiple routes depend on the same interaction pattern

Do not create a new component without checking `components.md` first.

## Style-File Decision Guidance

Choose the narrowest correct home.

### Token and theme decisions
Prefer updating the theme or token source.

### Global layout-rhythm decisions
Prefer the shared layout layer.

### Reusable control behavior
Prefer the shared components layer.

### Route-specific hierarchy or composition
Prefer the page layer.

### Surface reduction across repeated page patterns
Prefer the shared pages layer only if the reduction applies consistently across multiple routed surfaces.

## Documentation Update Rules

Update `docs/design-system/` when:
- A new design rule is introduced
- A page override materially changes
- A shared visual principle changes
- A new anti-pattern is discovered
- Review standards evolve
- A card-reduction decision becomes a durable rule instead of a one-off tweak

Do not leave major design reasoning only in implementation comments or pull-request text.

## Implementation Planning Template

Before coding, write:
1. Dominant job
2. Current problem
3. Smallest good fix
4. Impacted files
5. Design-system documents consulted
6. Risk of overreaching scope
7. Verification plan

## Verification Checklist

At minimum verify:
- Primary-action clarity
- Page hierarchy
- Spacing rhythm
- Typography readability
- Focus-visible
- Hover or pressed states where relevant
- Mobile layout
- Dark mode, if applicable
- Scope honesty in copy
- Whether any leftover card artifacts can be removed or softened

## Promotion Rule for Local Patterns

A local fix should remain local unless:
- It appears in multiple places
- It has stable behavior
- Its name can be semantic
- It improves consistency without adding abstraction burden

## Safe Default

When unsure:
- Reduce rather than add
- Reuse rather than invent
- Clarify rather than decorate
- Localize rather than globalize
- Remove a box before adding a new one
- Document the reasoning if the choice could repeat later