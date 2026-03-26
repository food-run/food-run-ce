/*  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  configure the app-local Playwright smoke suite

- Later Extension Points:
    --> Add built-artifact coverage or additional browser projects here once the frontend shell grows beyond the first smoke path

- Role:
    --> Owns the Playwright runtime contract for the active web app
    --> Boots the Angular dev server for browser-smoke coverage without broadening into CI or deploy policy
    --> Must stay app-local so browser tooling does not leak into unrelated repo surfaces

- Exports:
    --> default Playwright test configuration

- Consumed By:
    --> `apps/web/package.json`
    --> local operators running `bun run e2e`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  */

// ---------- imports and dependencies ----------

import { defineConfig, devices } from '@playwright/test';

// ---------- test runner configuration ----------

export default defineConfig({
  testDir: './e2e',
  fullyParallel: true,
  forbidOnly: Boolean(process.env.CI),
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'list',
  use: {
    baseURL: 'http://127.0.0.1:4200',
    trace: 'on-first-retry'
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] }
    }
  ],
  webServer: {
    command: 'bunx ng serve --host 127.0.0.1 --port 4200',
    url: 'http://127.0.0.1:4200',
    reuseExistingServer: !process.env.CI,
    timeout: 120000
  }
});
