-- purpose:
    -- keep a versioned copy of my DB schema with git
    -- create supabase (prod) and local postgres (dev) from the same script 
    -- make new tables from here so both versions are on the same page




-- used to generate UUIDs in postgres / supabase  ;  similar to bcrypt but for DBs
CREATE EXTENSION IF NOT EXISTS "pgcrypto";




-- recipes table  -->  one row per recipe imported or created in Food Run
CREATE TABLE IF NOT EXISTS public.recipes (
    -- primary key  -->  generate a random UUID by default
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),

    -- human-readable recipe name  -->  e.g. "keto chili"
    title text NOT NULL,

    -- original URL where the recipe came from
    source_url text NOT NULL,

    -- how many servings the recipe is written for
    servings integer,

    -- free-form notes  -->  substitutions, tips, etc.
    notes text,

    -- timestamps for tracking when rows were added / updated  -->  default to current time
    created_at timestamptz NOT NULL DEFAULT now(),
    updated_at timestamptz NOT NULL DEFAULT now()
);


-- enforce one recipe per source_url for now  -->  single shared demo user
create unique index if not exists recipes_unique_source_url
    on public.recipes (lower(source_url));




-- ingredients table  -->  global dictionary of ingredients  ;  shared across recipes for aggregation
CREATE TABLE IF NOT EXISTS public.ingredients (
    -- primary key for the ingredient
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),

    -- name of the ingredient  -->  e.g. "yellow onion"
    name text NOT NULL,

    -- optional normalized / lexical name to help with matching later
    canonical_name text,

    -- default unit when not specified  -->  e.g. "count", "pieces", "g", "ml"
    default_unit text,

    created_at timestamptz NOT NULL DEFAULT now()
);


-- normalize by ingredient name (case-insensitive)
create unique index if not exists ingredients_unique_name
    on public.ingredients (lower(name));




-- recipe_ingredients  join table  -->  link recipes to ingredients with per-recipe amounts/units
CREATE TABLE IF NOT EXISTS public.recipe_ingredients (
    -- primary key for this linking row
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),

    -- foreign key to the recipe this ingredient belongs to
    recipe_id uuid NOT NULL REFERENCES public.recipes(id) ON DELETE CASCADE,

    -- foreign key to the shared ingredient record
    ingredient_id uuid NOT NULL REFERENCES public.ingredients(id),

    -- for TS  -->  can be null or decimals (e.g. 0.5, 1.25)
    amount double precision,

    -- normalized unit (e.g. "g", "ml", "cup", "tbsp")  -->  will use for conversions
    unit text,

    -- optional notes about prep  -->  e.g. "finely chopped"
    notes text,

    -- used when wanting to preserve original order
    position integer,

    created_at timestamptz NOT NULL DEFAULT now()
);




-- safe re-runs  -->  ensure all expected columns exist  ;  add any missing columns without touching existing rows

-- recipes  
alter table if exists public.recipes
    add column if not exists title text not null,
    add column if not exists source_url text not null,
    add column if not exists servings integer,
    add column if not exists notes text,
    add column if not exists created_at timestamptz not null default now(),
    add column if not exists updated_at timestamptz not null default now();

-- ingredients  
alter table if exists public.ingredients
    add column if not exists name text not null,
    add column if not exists canonical_name text,
    add column if not exists default_unit text,
    add column if not exists created_at timestamptz not null default now();

-- recipe_ingredients  
alter table if exists public.recipe_ingredients
    add column if not exists recipe_id uuid not null,
    add column if not exists ingredient_id uuid not null,
    add column if not exists amount double precision,
    add column if not exists unit text,
    add column if not exists notes text,
    add column if not exists position integer,
    add column if not exists created_at timestamptz not null default now();





-- indexes  -->  most likely won't need these since my DB is small but it could be great for performance if I did

-- speed up lookups by recipe
CREATE INDEX IF NOT EXISTS idx_recipe_ingredients_recipe_id
    ON public.recipe_ingredients (recipe_id);

-- speed up lookups by ingredient
CREATE INDEX IF NOT EXISTS idx_recipe_ingredients_ingredient_id
    ON public.recipe_ingredients (ingredient_id);




-- turn on RLS  -->  superusers bypass this but anon / authenticated users can't access these tables at all
alter table public.recipes enable row level security;
alter table public.ingredients enable row level security;
alter table public.recipe_ingredients enable row level security;




-- default policies  -->  allow read for everyone, but write only from trusted roles
    -- workaround  -->  create policy only if it doesn't exist

-- Recipes
do $$
begin
    if not exists (
        select 1
        from pg_policies
        where schemaName = 'public'
          and tableName = 'recipes'
          and policyName = 'Public can read recipes'
    ) then
        create policy "Public can read recipes"
            on public.recipes
            for select
            using (true);
    end if;
end $$;

do $$
begin
    if not exists (
        select 1
        from pg_policies
        where schemaName = 'public'
          and tableName = 'recipes'
          and policyName = 'Service role can modify recipes'
    ) then
        create policy "Service role can modify recipes"
            on public.recipes
            for all
            to service_role
            using (true)
            with check (true);
    end if;
end $$;


-- Ingredients
do $$
begin
    if not exists (
        select 1
        from pg_policies
        where schemaName = 'public'
          and tableName = 'ingredients'
          and policyName = 'Public can read ingredients'
    ) then
        create policy "Public can read ingredients"
            on public.ingredients
            for select
            using (true);
    end if;
end $$;

do $$
begin
    if not exists (
        select 1
        from pg_policies
        where schemaName = 'public'
          and tableName = 'ingredients'
          and policyName = 'Service role can modify ingredients'
    ) then
        create policy "Service role can modify ingredients"
            on public.ingredients
            for all
            to service_role
            using (true)
            with check (true);
    end if;
end $$;


-- Recipe ingredients (join table)
do $$
begin
    if not exists (
        select 1
        from pg_policies
        where schemaName = 'public'
          and tableName = 'recipe_ingredients'
          and policyName = 'Public can read recipe_ingredients'
    ) then
        create policy "Public can read recipe_ingredients"
            on public.recipe_ingredients
            for select
            using (true);
    end if;
end $$;

do $$
begin
    if not exists (
        select 1
        from pg_policies
        where schemaName = 'public'
          and tableName = 'recipe_ingredients'
          and policyName = 'Service role can modify recipe_ingredients'
    ) then
        create policy "Service role can modify recipe_ingredients"
            on public.recipe_ingredients
            for all
            to service_role
            using (true)
            with check (true);
    end if;
end $$;

