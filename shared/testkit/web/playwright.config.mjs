/*  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  configure the shared frontend Playwright smoke suite

- Later Extension Points:
    --> Add built-artifact coverage or additional browser projects here once the frontend shell grows beyond the first smoke path

- Role:
    --> Owns the shared Playwright runtime contract for reviewer-visible frontend smoke coverage
    --> Boots the Angular dev server for browser-smoke coverage without broadening into deploy policy
    --> Must keep the test implementation under `shared/testkit/` while still targeting the active `apps/web` boundary

- Exports:
    --> default Playwright test configuration for the active web smoke suite

- Consumed By:
    --> `apps/web/package.json`
    --> `.github/workflows/frontend-quality.yml`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  */

// ---------- imports and dependencies ----------

import { existsSync } from 'node:fs';
import { createRequire } from 'node:module';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

// ---------- path resolution ----------

const currentFilePath = fileURLToPath(import.meta.url);
const currentDir = dirname(currentFilePath);
const repoRoot = resolve(currentDir, '..', '..', '..');
const webDir = resolve(repoRoot, 'apps', 'web');
const webRequire = createRequire(resolve(webDir, 'package.json'));
const { defineConfig, devices } = webRequire('@playwright/test');

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
].filter((value) => Boolean(value));

function resolveBrowserExecutable() {
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
  testDir: currentDir,
  testMatch: 'smoke.spec.ts',
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
    cwd: webDir,
    url: 'http://127.0.0.1:4200',
    reuseExistingServer: !process.env.CI,
    timeout: 120000
  }
});
