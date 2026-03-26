/*  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  verify the first reviewer-visible frontend smoke paths

- Later Extension Points:
    --> Add deeper route and interaction coverage here once the active shell gains stateful import, recipe, and shopping behavior

- Role:
    --> Exercises the minimal browser checks that prove the active frontend shell renders and routes correctly
    --> Keeps the first Playwright slice narrow by covering one redirect path and one navigation path
    --> Must stay focused on current reviewer-visible behavior instead of inventing page-object layers too early

- Exports:
    --> Playwright smoke tests for the active web shell

- Consumed By:
    --> `apps/web/package.json`
    --> local operators running `bun run e2e`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  */

// ---------- imports and dependencies ----------

import { expect, test } from '@playwright/test';

// ---------- smoke coverage ----------

test('redirects the root route into the import flow', async ({ page }) => {
  await page.goto('/');

  await expect(page).toHaveURL(/\/import$/);
  await expect(page.getByRole('heading', { level: 1, name: /Food Run/i })).toBeVisible();
  await expect(page.getByRole('heading', { level: 2, name: 'Import Recipes' })).toBeVisible();
});

test('navigates from the shared shell to the planner placeholder state', async ({ page }) => {
  await page.goto('/import');

  await page.getByRole('link', { name: 'Planner' }).click();

  await expect(page).toHaveURL(/\/planner$/);
  await expect(page.getByRole('heading', { level: 2, name: 'Planner' })).toBeVisible();
  await expect(page.getByText('No meals planned yet')).toBeVisible();
});
