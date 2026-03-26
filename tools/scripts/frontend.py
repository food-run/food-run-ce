#!/usr/bin/env python3
"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  verify the reviewer frontend build and GitHub Pages artifact contract

- Later Extension Points:
    --> Add optional browser-smoke hooks here once Sprint 1 owns a stable e2e toolchain

- Role:
    --> Builds the active web app using the same Pages-targeted command used for deployment
    --> Verifies the produced static artifact keeps the reviewer URL path and SPA fallback honest
    --> Keeps Sprint 0 frontend verification deterministic without pretending full browser-matrix maturity exists

- Exports:
    --> CLI entry point for reviewer-frontend verification

- Consumed By:
    --> tools/scripts/verify.py (via --skip-frontend flag)
    --> repo operators running `python3 tools/scripts/frontend.py`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
from __future__ import annotations

# ---------- imports and dependencies ----------

import argparse
import filecmp
import subprocess
import sys
from pathlib import Path

# ---------- runtime identity ----------

REPO_ROOT = Path(__file__).resolve().parents[2]
WEB_DIR = REPO_ROOT / 'apps' / 'web'
PAGES_INDEX_PATH = WEB_DIR / 'dist' / 'browser' / 'index.html'
PAGES_404_PATH = WEB_DIR / 'dist' / 'browser' / '404.html'
PAGES_BASE_HREF = '<base href="/food-run-ce/">'

# ---------- subprocess helpers ----------


def run_command(label: str, command: list[str], cwd: Path) -> int:
    """Run one subprocess and mirror its output."""
    print(f'==> {label}')
    result = subprocess.run(command, cwd=cwd, text=True, capture_output=True)
    if result.stdout:
        print(result.stdout, end='')
    if result.stderr:
        print(result.stderr, file=sys.stderr, end='')
    return result.returncode


# ---------- artifact verification helpers ----------


def install_dependencies() -> int:
    """Install the web app dependencies with the committed lockfile."""
    return run_command('install web dependencies', ['bun', 'install', '--frozen-lockfile'], WEB_DIR)


def build_pages_artifact() -> int:
    """Build the static artifact used for GitHub Pages deployment."""
    return run_command('build reviewer frontend', ['bun', 'run', 'build:pages'], WEB_DIR)


def verify_pages_artifact() -> int:
    """Check the built artifact for the Pages subpath and SPA fallback contract."""
    print('==> verify reviewer frontend artifact')

    failures: list[str] = []
    if not PAGES_INDEX_PATH.is_file():
        failures.append(f'missing built index artifact: {PAGES_INDEX_PATH.relative_to(REPO_ROOT)}')
    if not PAGES_404_PATH.is_file():
        failures.append(f'missing SPA fallback artifact: {PAGES_404_PATH.relative_to(REPO_ROOT)}')

    if failures:
        for failure in failures:
            print(f'FAIL: {failure}')
        return 1

    index_text = PAGES_INDEX_PATH.read_text(encoding='utf-8')
    if PAGES_BASE_HREF not in index_text:
        failures.append(
            f'{PAGES_INDEX_PATH.relative_to(REPO_ROOT)}: expected Pages base href {PAGES_BASE_HREF}'
        )
    if not filecmp.cmp(PAGES_INDEX_PATH, PAGES_404_PATH, shallow=False):
        failures.append(
            f'{PAGES_404_PATH.relative_to(REPO_ROOT)}: expected the SPA fallback to match the built index shell exactly'
        )

    if failures:
        for failure in failures:
            print(f'FAIL: {failure}')
        return 1

    print(f'PASS: {PAGES_INDEX_PATH.relative_to(REPO_ROOT)} keeps the Pages base href')
    print(f'PASS: {PAGES_404_PATH.relative_to(REPO_ROOT)} mirrors the built index shell')
    return 0

# ---------- verification flow ----------


def run_verification(skip_install: bool) -> int:
    """Run the bounded Sprint 0 frontend verification flow."""
    failures = 0
    if not skip_install:
        failures += install_dependencies()
    failures += build_pages_artifact()
    if failures:
        print('FRONTEND VERIFY FAILED')
        return 1

    failures += verify_pages_artifact()
    if failures:
        print('FRONTEND VERIFY FAILED')
        return 1

    print('FRONTEND VERIFY PASSED')
    return 0


# ---------- CLI ----------


def build_parser() -> argparse.ArgumentParser:
    """Build the bounded CLI parser."""
    parser = argparse.ArgumentParser(description='Verify the reviewer frontend build and Pages artifact contract.')
    parser.add_argument('--skip-install', action='store_true', help='Skip `bun install --frozen-lockfile` before the build.')
    return parser


def main() -> int:
    """Run the reviewer frontend verification flow."""
    parser = build_parser()
    args = parser.parse_args()
    return run_verification(skip_install=args.skip_install)


if __name__ == '__main__':
    sys.exit(main())
