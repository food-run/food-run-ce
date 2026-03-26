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

// ---------- shared shell helpers ----------

interface NavigationExpectation {
  linkName: string;
  pathPattern: RegExp;
  headingName: string;
  stateText: string;
}

async function expectShellNavigation(page: Parameters<typeof test>[0]['page'], expectation: NavigationExpectation) {
  await page.goto('/import');
  await page.getByRole('link', { name: expectation.linkName }).click();

  await expect(page).toHaveURL(expectation.pathPattern);
  await expect(page.getByRole('heading', { level: 2, name: expectation.headingName })).toBeVisible();
  await expect(page.getByText(expectation.stateText)).toBeVisible();
}

// ---------- smoke coverage ----------

test('redirects the root route into the import flow', async ({ page }) => {
  await page.goto('/');

  await expect(page).toHaveURL(/\/import$/);
  await expect(page.getByRole('heading', { level: 1, name: /Food Run/i })).toBeVisible();
  await expect(page.getByRole('heading', { level: 2, name: 'Import Recipes' })).toBeVisible();
});

test('navigates from the shared shell to the planner placeholder state', async ({ page }) => {
  await expectShellNavigation(page, {
    linkName: 'Planner',
    pathPattern: /\/planner$/,
    headingName: 'Planner',
    stateText: 'No meals planned yet'
  });
});

test('navigates from the shared shell to the recipes placeholder state', async ({ page }) => {
  await expectShellNavigation(page, {
    linkName: 'Recipes',
    pathPattern: /\/recipes$/,
    headingName: 'Recipes',
    stateText: 'No recipes yet'
  });
});

test('navigates from the shared shell to the shopping placeholder state', async ({ page }) => {
  await expectShellNavigation(page, {
    linkName: 'Shopping List',
    pathPattern: /\/shopping$/,
    headingName: 'Shopping List',
    stateText: 'No shopping list yet'
  });
});
