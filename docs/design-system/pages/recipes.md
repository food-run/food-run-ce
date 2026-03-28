# Recipes

## Page Role

The Recipes page is a browsing, selection, and management surface for recipe content already in the system or review flow.

## Dominant Job

Scan available recipes and take the next meaningful action with minimal cognitive load.

## Likely Primary Actions

Depending on current implementation scope:
- Open a recipe
- Review ingredients
- Add to Planner
- Manage recipe state

One of these must be made primary in the local context.

## Visual Priorities

1. Page identity
2. Scannable item structure
3. The most useful next action per item
4. Lightweight metadata
5. Secondary tools or filtering, if present

## Layout Guidance

- Optimize for scanability over decoration
- Keep repeated item structures consistent
- Surface the most decision-relevant information first
- Avoid bloated card presentations unless items truly need them

## Surface Guidance

The current shared styles already support `.recipe-list-item` as a surfaced pattern.

That does not mean Recipes should automatically become a wall of cards.

Use boxed recipe items only if they improve:
- Repeated-item scanning
- Clear action grouping
- Local metadata parsing

Prefer lighter treatments if the list reads well without repeated bordered panels.

## Content Guidance

Recipe entries should emphasize:
- Recognizable name
- Meaningful summary information
- The clearest next action

Avoid overwhelming users with low-value metadata upfront.

## Trust Notes

Do not imply:
- Recipe-quality scoring that does not exist
- Ingredient certainty that does not exist
- Planner-integration depth that does not exist

## Empty-State Guidance

If there are no recipes:
- Explain that clearly
- Point back to Import or the next relevant step
- Keep the empty state visually modest

For the current reviewer shell, prefer a lightweight list-empty message over a standalone card unless the extra surface clearly improves scanability.

## Mobile Behavior

On mobile:
- Maintain scanability
- Keep per-item actions clear
- Avoid layouts that require horizontal inspection for basic understanding
- Ensure repeated rows do not become visually noisy

## Banned Clutter

Do not add:
- Excessive badges
- Many equal-priority actions
- Heavy nested cards
- Decorative item chrome
- Long text excerpts that reduce scanability

## Review Questions

1. Can users scan the list quickly?
2. Is the most useful next action obvious?
3. Are repeated items visually calm?
4. Does the page avoid turning recipe management into a dashboard?
5. Are recipe items using the lightest viable surface treatment?
