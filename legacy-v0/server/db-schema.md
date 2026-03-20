# food run – db schema (recipes + ingredients)

> source of truth  →  see `server/schema.sql` for the actual sql

## recipes

- `id uuid`
  - primary key, `gen_random_uuid()`
- `title text not null`
  - human-readable recipe name
- `source_url text not null`
  - original recipe link; unique for now ignoring casing (one row per url)
- `servings integer`
  - how many servings the recipe is written for
- `notes text`
  - free-form notes / substitutions / comments
- `created_at timestamptz not null default now()`
- `updated_at timestamptz not null default now()`

indexes:

- `recipes_unique_source_url` on `lower(source_url)`

---

## ingredients

- `id uuid`
  - primary key
- `name text not null`
  - display name, e.g. `"yellow onion"`
- `canonical_name text`
  - optional normalized name for smarter matching later
- `default_unit text`
  - e.g. `"count"`, `"g"`, `"ml"` 
- `created_at timestamptz not null default now()`

indexes:

- `ingredients_unique_name` on `lower(name)`

---

## recipe_ingredients

- `id uuid`
  - primary key
- `recipe_id uuid not null`
  - fk → `public.recipes(id)` with `on delete cascade`
- `ingredient_id uuid not null`
  - fk → `public.ingredients(id)`
- `amount double precision`
  - nullable; supports fractions like `0.5`, `1.25`
- `unit text`
  - normalized unit ( `"g"`, `"cup"`, `"tbsp"`, `"clove"`, etc.)
- `notes text`
  - prep notes per recipe: `"finely chopped"`, `"room temp"`, etc
- `position integer`
  - used to preserve original order
- `created_at timestamptz not null default now()`

indexes:

- `idx_recipe_ingredients_recipe_id`
- `idx_recipe_ingredients_ingredient_id`


---
