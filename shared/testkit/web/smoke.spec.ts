/*  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  verify the first reviewer-visible frontend smoke paths from the shared testkit home

- Later Extension Points:
    --> Add deeper route and interaction coverage here once the active shell gains stateful import, recipe, and shopping behavior

- Role:
    --> Exercises the minimal browser checks that prove the active frontend shell renders and routes correctly
    --> Keeps the first Playwright slice narrow by covering the shell redirect and the visible navigation paths
    --> Must keep browser-smoke assertions centralized under `shared/testkit/` instead of scattering app tests across runtime folders

- Exports:
    --> Playwright smoke tests for the active web shell

- Consumed By:
    --> `apps/web/package.json`
    --> `.github/workflows/frontend-quality.yml`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  */

// ---------- imports and dependencies ----------

import type { Page } from '@playwright/test';
import { expect, test } from '@playwright/test';

// ---------- shared shell helpers ----------

interface NavigationExpectation {
  linkName: string;
  pathPattern: RegExp;
  headingName: string;
  stateText: string;
}

async function expectShellNavigation(page: Page, expectation: NavigationExpectation) {
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
