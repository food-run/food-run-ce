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

import { existsSync } from 'node:fs';
import { defineConfig, devices } from '@playwright/test';

// ---------- local browser resolution ----------

const browserCandidates = [
  process.env.PLAYWRIGHT_BROWSER_PATH,
  '/opt/homebrew/bin/chromium',
  '/Applications/Chromium.app/Contents/MacOS/Chromium',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/usr/bin/chromium',
  '/usr/bin/chromium-browser',
  '/usr/bin/google-chrome',
  '/opt/google/chrome/chrome'
].filter((value): value is string => Boolean(value));

function resolveBrowserExecutable(): string {
  const resolvedPath = browserCandidates.find((candidate) => existsSync(candidate));

  if (resolvedPath) {
    return resolvedPath;
  }

  throw new Error(
    'No local Chromium or Chrome executable was found. Set PLAYWRIGHT_BROWSER_PATH to an installed browser path before running `bun run e2e`.'
  );
}

const browserExecutablePath = resolveBrowserExecutable();

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
      use: {
        ...devices['Desktop Chrome'],
        launchOptions: {
          executablePath: browserExecutablePath
        }
      }
    }
  ],
  webServer: {
    command: 'bunx ng serve --host 127.0.0.1 --port 4200',
    url: 'http://127.0.0.1:4200',
    reuseExistingServer: !process.env.CI,
    timeout: 120000
  }
});
