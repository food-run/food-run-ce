# Components

## Purpose

This file defines the shared component and primitive mindset for Food Run.

The design system should stay lean. Shared primitives should be few, meaningful, and reusable. Do not promote every local pattern into a design-system component.

## Component Philosophy

A shared primitive should exist only when it improves:
- Consistency
- Speed of implementation
- User comprehension
- Maintenance clarity

Do not create shared components only because a pattern appears twice.

## Preferred Shared Primitives

### App shell
Provides stable route framing, navigation context, and page containment.

### Page section
A consistent page-level wrapper for titles, copy, and primary content framing.

### Section header
A reusable way to introduce a content group or action region.

### Primary button
The strongest local action.

### Secondary button
A supporting action that does not compete with the primary action.

### Text input
A clear input control with label, helper, and error support.

### Helper or status block
A small text region for helpful clarification or current state.

### Empty state
A compact structure that explains absence and suggests the next step.

### List item or selection row
A reusable layout for scannable repeated content, where appropriate.

## Component Rules

### One Primitive, One Job

Each shared primitive should have a clearly bounded responsibility.

Avoid Swiss-army components that absorb many unrelated responsibilities.

### Shared Before Local Only When Truly Shared

If a pattern is page-specific, keep it page-specific.

Promote it only when:
- It appears in multiple routes
- It behaves the same way
- It uses the same layout and states
- Sharing it will reduce confusion or drift

### Semantic Naming Only

Use names that describe the primitive’s responsibility, not its appearance alone.

Good direction:
- `PageSection`
- `SectionHeader`
- `PrimaryButton`

Weak direction:
- `BlueCard`
- `FancyPanel`
- `BigCTA`

## Shell Rules

The shell is part of the product experience, not just scaffolding.

It should:
- Keep route transitions coherent
- Preserve spacing rhythm
- Support clear page identity
- Avoid stealing attention from the page’s dominant job

## Surface Rules

Do not turn “card” into the default primitive for every piece of content.

A bordered or filled surface is a valid primitive only if it has a clear job.

Before introducing or keeping a surface wrapper, ask:
- Is this clarifying scope?
- Is this helping a repeated-item pattern?
- Is this improving trust?
- Could spacing do the same job more elegantly?

## Button Rules

Buttons must:
- Have a clear priority model
- Remain readable
- Maintain consistent spacing and state treatment
- Avoid style drift between pages

## Input Rules

Inputs must:
- Have explicit labels
- Support helper and error text cleanly
- Show strong focus feedback
- Preserve readability on mobile and desktop

## Empty-State Rules

A good empty state:
- Explains absence
- Keeps visual weight modest
- Guides the next step
- Does not overuse illustration or decoration

An empty state does not always need a card shell.

## When to Create a New Shared Primitive

Create a new shared primitive only if all are true:
1. The pattern is reusable
2. The behavior is stable
3. The role is clear
4. The name can be semantic
5. It improves consistency more than it increases abstraction cost

## Review Checklist

Before adding or promoting a component, check:
- Is this truly shared?
- Is the name semantic?
- Does it have one job?
- Does it preserve Food Run’s design thesis?
- Could a simpler local pattern work just as well?
- Is the component creating another unnecessary surface?