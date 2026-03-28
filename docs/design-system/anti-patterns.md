# Anti-Patterns

## Purpose

This file lists design failures that Food Run should actively avoid.

These are not mild preferences. Treat them as strong warning signs.

## Structure Anti-Patterns

### Card piles
Too many boxed surfaces stacked together.

Why it is bad:
- Adds visual noise
- Weakens hierarchy
- Makes simple workflows feel heavier

### Cards inside cards
Nested panels without a strong structural reason.

Why it is bad:
- Creates fake complexity
- Reduces calmness
- Makes spacing harder to read

### Equal emphasis everywhere
Many regions competing at the same visual weight.

Why it is bad:
- Destroys hierarchy
- Slows comprehension
- Makes the primary task harder to find

### Dashboard-ifying simple flows
Turning a straightforward workflow into a control center.

Why it is bad:
- Adds cognitive load
- Makes the product feel more complicated than it is
- Distracts from the next useful action

### Prototype-surface carryover
Keeping bordered surfaces or card wrappers simply because the older prototype or reviewer shell had them.

Why it is bad:
- Preserves old visual debt
- Blocks the refined design system from taking shape
- Adds weight without adding meaning

## Typography Anti-Patterns

### Too many type sizes
Many sizes that are close together.

Why it is bad:
- Muddies hierarchy
- Makes the page feel accidental

### Playful type without discipline
Using comic-like fonts with weak spacing, weak contrast, or weak role control.

Why it is bad:
- Feels childish
- Harms trust

### Tiny helper text
Making supporting text too small to read comfortably.

Why it is bad:
- Punishes the user for needing help
- Creates false polish

## Color Anti-Patterns

### Accent everywhere
Using accent color on too many elements.

Why it is bad:
- Flattens hierarchy
- Turns the page loud

### Low-contrast muted text
Muted text that is aesthetically soft but functionally weak.

Why it is bad:
- Harms readability
- Is especially bad in dark mode

### Generic AI gradients
Using flashy gradients or generic futuristic styling unrelated to Food Run’s brand.

Why it is bad:
- Looks trend-chasing
- Erases product identity
- Weakens trust

## Interaction Anti-Patterns

### Hover-only affordance
Important cues visible only on hover.

Why it is bad:
- Fails touch users
- Fails keyboard users
- Weakens discoverability

### Unclear disabled states
Unavailable controls that only fade slightly.

Why it is bad:
- Users cannot tell whether a control is broken, inactive, or still clickable

### Decorative motion
Motion with no orientation or feedback function.

Why it is bad:
- Adds noise
- Cheapens the interface

## Content Anti-Patterns

### Vague call-to-action labels
Buttons like:
- Submit
- Continue
- Process
- Confirm

Why it is bad:
- Hides the actual outcome
- Increases hesitation

### Long introductions before action
Large paragraphs before the first useful input or action.

Why it is bad:
- Delays progress
- Increases reading burden
- Often signals weak information design

### Fake confidence language
Text implying the product is more certain or intelligent than it is.

Why it is bad:
- Damages trust
- Creates mismatch between expectation and behavior

### Placeholder as label
Using placeholder text as the only field label.

Why it is bad:
- Harms clarity
- Harms accessibility
- Breaks once the user starts typing

## Product-Truth Anti-Patterns

### Fake progress states
Implying jobs, sync, or processing sophistication that is not real.

### Fake persistence
Designing the UI as if data is safely stored when that is not actually true.

### Fake AI quality
Implying reasoning or automation quality that has not been built.

## Review Trigger Questions

If any of these are true, pause and revise:
- Does the page feel louder after the change?
- Did we add containers instead of fixing hierarchy?
- Did we add style instead of reducing structure?
- Did we make the page seem smarter than it is?
- Did we make the interface more generic?
- Did we reduce Food Run’s playful warmth into sterile modernism?
- Did we keep a card artifact simply because removing it felt risky?