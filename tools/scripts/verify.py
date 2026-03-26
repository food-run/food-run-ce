#!/usr/bin/env python3
"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  repo verification entrypoint for script and coordination checks

- Later Extension Points:
    --> Add broader repo-control checks as later quality gates become active

- Role:
    --> Runs the bounded verification checks that keep repo-control changes explainable and safe
    --> Verifies script syntax, required script TL;DR headers, stub-only shapes, and coordination cadence from one entrypoint
    --> Exists as the shared verification runner for local checks and CI-safe repo verification
    --> Must remain a thin verifier, not a hidden policy engine with branching workflow logic

- Exports:
    --> `main()` command-line verification entrypoint

- Consumed By:
    --> reviewers, integrators, and local operators running repo verification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """

from __future__ import annotations

# ---------- imports and dependencies ----------

import argparse
import io
import re
import subprocess
import sys
from contextlib import redirect_stdout
from pathlib import Path

# Keep the repo root importable during direct script execution.
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from shared.testkit import TestCase, write_file

# ---------- runtime identity ----------

# Keep required TL;DR markers centralized for every script audit.
TLDR_REQUIRED_MARKERS = (
    'TL;DR  -->',
    '- Later Extension Points:',
    '- Role:',
    '- Exports:',
    '- Consumed By:',
)
# Scan only active rebuild Python script surfaces (exclude node_modules, dist, .angular).
PYTHON_SCRIPT_PATTERNS = (
    'tools/scripts/*.py',
    'apps/agent/*.py',
    'apps/api/*.py',
    'apps/domain/*.py',
    'shared/**/*.py',
)
# Audit script headers across Python and TypeScript entrypoints.
SCRIPT_HEADER_PATTERNS = (
    'tools/scripts/*.py',
    'apps/agent/*.py',
    'apps/api/*.py',
    'apps/domain/*.py',
    'shared/**/*.py',
    'shared/testkit/ui/**/*.ts',
    'shared/testkit/ui/**/*.mjs',
    'apps/web/src/**/*.ts',
    'apps/web/src/**/*.js',
)
# Match canonical Python section headers in implemented files.
PYTHON_SECTION_MARKER_RE = re.compile(r'^# ---------- [a-z0-9][a-z0-9 -]* ----------$', re.MULTILINE)
# Match canonical JavaScript section headers in implemented files.
JS_SECTION_MARKER_RE = re.compile(r'^// ---------- [a-z0-9][a-z0-9 -]* ----------$', re.MULTILINE)
# Permit the minimal syntax keeper in TypeScript stubs.
ALLOWED_TS_STUB_LINES = {'export {}', 'export {};'}
# Match one consumed-by bullet with real detail.
CONSUMED_BY_LINE_RE = re.compile(r'^\s*-->\s+\S.+$', re.MULTILINE)
# Require more than one section in implemented files.
MIN_IMPLEMENTED_SECTION_MARKERS = 2
# Keep the repo verification workflow bound to this entrypoint.
CENTRAL_VERIFY_COMMAND = 'python3 tools/scripts/verify.py --ci'
# Keep the shared testkit suite list stable without filename prefixes.
# Keep script-local unit discovery pointed at the canonical script home.
SCRIPT_TEST_DISCOVERY_START = 'tools/scripts'
# Keep script-local unit discovery narrow to Python script files.
SCRIPT_TEST_DISCOVERY_PATTERN = '*.py'
# Keep the remaining shared testkit workflow suite explicit.
REPO_TEST_MODULES = ('shared.testkit.workflows',)
# Point to the canonical merge-blocking repo verification workflow.
REPO_VERIFY_WORKFLOW_PATH = Path('.github/workflows/repo-verify.yml')

# ---------- subprocess helpers ----------

# Run a child verifier and mirror its output.
def run_script(label: str, command: list[str], cwd: Path) -> int:
    # Announce the verification stage before child logs.
    print(f'==> {label}')
    # Capture text output for readable local and CI logs.
    result = subprocess.run(command, cwd=cwd, text=True, capture_output=True)
    # Preserve child standard output for the calling human.
    if result.stdout:
        print(result.stdout, end='')
    # Preserve child standard error for failure diagnosis.
    if result.stderr:
        print(result.stderr, file=sys.stderr, end='')
    # Return the child exit code unchanged.
    return result.returncode

# ---------- script shape helpers ----------

# Confirm that every required TL;DR marker appears in order.
def has_structured_tldr(text: str) -> bool:
    # Track the prior marker position across the scan.
    previous_index = -1
    # Require the canonical marker order without reordering.
    for marker in TLDR_REQUIRED_MARKERS:
        # Find the next marker after the prior one.
        current_index = text.find(marker, previous_index + 1)
        # Fail when any required marker is missing.
        if current_index == -1:
            return False
        # Advance the scan window to this marker.
        previous_index = current_index
    # Confirm the full ordered marker chain passed.
    return True


# Pick the canonical TL;DR wrapper terminator by language.
def tldr_terminator(path: Path) -> str:
    # Use the JavaScript wrapper for frontend entrypoints.
    if path.suffix in {'.ts', '.js'}:
        return '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  */'
    # Use the Python wrapper for all Python scripts.
    return '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """'


# Slice the file body that appears after the TL;DR.
def script_body_after_tldr(path: Path, text: str) -> str:
    # Split on the canonical wrapper terminator once.
    terminator = tldr_terminator(path)
    # Treat missing wrappers as empty for later failure paths.
    if terminator not in text:
        return ''
    # Return only the executable body region.
    return text.split(terminator, 1)[1]


# Treat empty Python bodies and bare TypeScript exports as stubs.
def is_stub_only_script(path: Path, text: str) -> bool:
    # Normalize away blank lines after the TL;DR.
    meaningful_lines = [line.strip() for line in script_body_after_tldr(path, text).splitlines() if line.strip()]
    # Empty bodies are valid stubs in Python.
    if not meaningful_lines:
        return True
    # Keep the minimal TypeScript syntax keeper allowed.
    if path.suffix in {'.ts', '.js'} and set(meaningful_lines) <= ALLOWED_TS_STUB_LINES:
        return True
    # Everything else counts as real implementation.
    return False


# Count section headers only once real code exists.
def section_marker_count(path: Path, text: str) -> int:
    # Match section syntax by language family.
    marker_re = JS_SECTION_MARKER_RE if path.suffix in {'.ts', '.js'} else PYTHON_SECTION_MARKER_RE
    # Count every canonical section marker in the file.
    return len(marker_re.findall(text))


# Require at least one real consumed-by detail line.
def has_consumed_by_detail(text: str) -> bool:
    # Fail fast when the section is missing.
    if '- Consumed By:' not in text:
        return False
    # Inspect only the consumed-by block content.
    consumed_block = text.split('- Consumed By:', 1)[1]
    # Stop scanning at the TL;DR wrapper edge.
    consumed_block = consumed_block.split('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~', 1)[0]
    # Accept one or more non-empty consumed-by lines.
    return CONSUMED_BY_LINE_RE.search(consumed_block) is not None


# Extract every workflow shell run block in order.
def workflow_run_blocks(text: str) -> list[str]:
    # Split once so indentation-sensitive scanning stays simple.
    lines = text.splitlines()
    # Collect run blocks in encounter order.
    blocks: list[str] = []
    # Track the current line manually across multiline blocks.
    index = 0

    # Walk the workflow text one line at a time.
    while index < len(lines):
        line = lines[index]
        stripped = line.lstrip()
        indent = len(line) - len(stripped)

        # Ignore lines that do not start a run block.
        if not stripped.startswith('run:'):
            index += 1
            continue

        # Capture the inline content after the run key.
        content = stripped[4:].strip()
        # Keep single-line run steps as-is.
        if content and not content.startswith(('|', '>')):
            blocks.append(content)
            index += 1
            continue

        # Collect multiline run blocks until indentation unwinds.
        block_lines: list[str] = []
        index += 1
        while index < len(lines):
            next_line = lines[index]
            next_stripped = next_line.lstrip()
            next_indent = len(next_line) - len(next_stripped)

            # Stop when the multiline block ends.
            if next_stripped and next_indent <= indent:
                break

            # Preserve blank lines inside the run block.
            if not next_stripped:
                block_lines.append('')
                index += 1
                continue

            # Record block lines without their YAML indentation.
            block_lines.append(next_stripped)
            index += 1

        # Keep the reconstructed multiline command block.
        blocks.append('\n'.join(block_lines).rstrip())

    # Return every discovered run block.
    return blocks


# Confirm the workflow still delegates to the central verifier.
def workflow_runs_central_verifier(text: str) -> bool:
    # Accept only one exact single-line verifier command.
    return workflow_run_blocks(text) == [CENTRAL_VERIFY_COMMAND]


# Enforce the canonical Python wrapper position.
def has_canonical_python_wrapper(text: str) -> bool:
    # Allow an initial shebang before the wrapper.
    if text.startswith('#!'):
        newline_index = text.find('\n')
        # Reject one-line shebang files with no wrapper.
        if newline_index == -1:
            return False
        # Resume checking after the shebang line.
        text = text[newline_index + 1 :]
    # Require the canonical opening wrapper immediately next.
    return text.startswith('"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# ---------- verification checks ----------

# Compile every Python script without emitting cache files.
def verify_script_syntax(repo_root: Path) -> int:
    # Announce the syntax verification stage.
    print('==> python script syntax')
    # Collect compile failures for one combined report.
    failures: list[str] = []
    # Avoid double-checking overlapping glob matches.
    seen: set[Path] = set()
    # Walk each active Python script pattern.
    for pattern in PYTHON_SCRIPT_PATTERNS:
        # Keep output order stable across runs.
        for path in sorted(repo_root.glob(pattern)):
            # Skip duplicate matches and directories.
            if path in seen or not path.is_file():
                continue
            # Record the path before compiling.
            seen.add(path)
            try:
                # Read the source without importing the module.
                source = path.read_text(encoding='utf-8')
                # Compile in memory so no cache files leak.
                compile(source, str(path), 'exec')
                # Report each passing file explicitly.
                print(f'PASS: {path.relative_to(repo_root)}')
            except SyntaxError as exc:
                # Store detailed failures for the summary block.
                failures.append(f'{path.relative_to(repo_root)}: {exc.msg} (line {exc.lineno})')
    # Print failures together after the scan finishes.
    if failures:
        for failure in failures:
            print(f'FAIL: {failure}')
        return 1
    # Return success when every file compiles.
    return 0


# Verify TL;DR wrappers, stub rules, and section headers.
def verify_script_tldrs(repo_root: Path) -> int:
    # Announce the explainability verification stage.
    print('==> script explainability headers')
    # Collect failures for one readable summary.
    failures: list[str] = []
    # Avoid duplicate checks across overlapping globs.
    seen: set[Path] = set()
    # Walk every governed script header target.
    for pattern in SCRIPT_HEADER_PATTERNS:
        # Keep output ordering stable across runs.
        for path in sorted(repo_root.glob(pattern)):
            # Skip duplicate matches and non-files.
            if path in seen or not path.is_file():
                continue
            # Record the file before validating it.
            seen.add(path)
            # Read the full file for body-shape checks.
            text = path.read_text(encoding='utf-8')
            # Limit header scans to the early file window.
            header_window = text[:1600]
            # Require the full TL;DR marker set.
            if not has_structured_tldr(header_window):
                failures.append(
                    f'{path.relative_to(repo_root)}: missing structured TL;DR header required by .opencode/rules/implementation-standards.md'
                )
                continue
            # Keep Python wrappers in the canonical opening position.
            if path.suffix == '.py' and not has_canonical_python_wrapper(header_window):
                failures.append(
                    f'{path.relative_to(repo_root)}: python TL;DR header must use the canonical wrapper immediately after the optional shebang'
                )
                continue
            # Keep TypeScript and JavaScript wrappers canonical too.
            if path.suffix in {'.ts', '.js'} and not header_window.startswith('/*  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'):
                failures.append(f'{path.relative_to(repo_root)}: script TL;DR header must use the canonical wrapper')
                continue
            # Keep consumed-by detail present and reviewable.
            if not has_consumed_by_detail(header_window):
                failures.append(
                    f'{path.relative_to(repo_root)}: Consumed By must include at least one non-empty detail line'
                )
                continue
            # Allow true stubs to stop after the TL;DR.
            if is_stub_only_script(path, text):
                print(f'PASS: {path.relative_to(repo_root)}')
                continue
            # Require multiple section headers once implementation exists.
            if section_marker_count(path, text) < MIN_IMPLEMENTED_SECTION_MARKERS:
                failures.append(
                    f'{path.relative_to(repo_root)}: implemented files need at least {MIN_IMPLEMENTED_SECTION_MARKERS} section-group comments required by .opencode/rules/implementation-standards.md'
                )
                continue
            # Report the file once every explainability rule passes.
            print(f'PASS: {path.relative_to(repo_root)}')
    # Print failures together after the scan finishes.
    if failures:
        for failure in failures:
            print(f'FAIL: {failure}')
        return 1
    # Return success when every file passes.
    return 0


# Run the shared repo-control suites from their canonical module list.
def verify_repo_test_modules(repo_root: Path) -> int:
    # Discover script-owned unit coverage from the canonical script home.
    failures = run_script(
        'tools/scripts unittest discovery',
        [
            sys.executable,
            '-m',
            'unittest',
            'discover',
            '-s',
            SCRIPT_TEST_DISCOVERY_START,
            '-p',
            SCRIPT_TEST_DISCOVERY_PATTERN,
            '-t',
            '.',
        ],
        repo_root,
    )
    # Run the remaining shared workflow suite from its stable module home.
    failures += run_script(
        'shared testkit workflow suite',
        [sys.executable, '-m', 'unittest', *REPO_TEST_MODULES],
        repo_root,
    )
    return failures


# Keep the merge-blocking workflow thin and script-driven.
def verify_repo_workflow_contract(repo_root: Path) -> int:
    # Announce the workflow-boundary verification stage.
    print('==> repo verification workflow contract')
    # Resolve the canonical workflow path from the repo root.
    workflow_path = repo_root / REPO_VERIFY_WORKFLOW_PATH
    # Fail clearly when the workflow is missing.
    if not workflow_path.is_file():
        print(f'FAIL: {REPO_VERIFY_WORKFLOW_PATH}: missing repo verification workflow')
        return 1

    # Read the workflow once for all contract checks.
    workflow_text = workflow_path.read_text(encoding='utf-8')
    # Collect workflow contract failures together.
    failures: list[str] = []

    # Inspect every shell run block in the workflow.
    run_blocks = workflow_run_blocks(workflow_text)

    # Keep YAML orchestration thin instead of encoding policy there.
    if len(run_blocks) != 1:
        failures.append(
            f'{REPO_VERIFY_WORKFLOW_PATH}: expected exactly 1 shell run step so policy stays in tools/scripts/verify.py, found {len(run_blocks)}'
        )

    # Reject multiline shell blocks that could hide extra logic.
    if any('\n' in block for block in run_blocks):
        failures.append(
            f"{REPO_VERIFY_WORKFLOW_PATH}: expected a single-line run command '{CENTRAL_VERIFY_COMMAND}', not a multiline shell block"
        )

    # Require the workflow to call the central verifier entrypoint exactly.
    if run_blocks != [CENTRAL_VERIFY_COMMAND]:
        failures.append(
            f"{REPO_VERIFY_WORKFLOW_PATH}: expected the only shell run step to be '{CENTRAL_VERIFY_COMMAND}'"
        )

    # Report every contract failure together.
    if failures:
        for failure in failures:
            print(f'FAIL: {failure}')
        return 1

    # Confirm the workflow contract passed.
    print(f'PASS: {REPO_VERIFY_WORKFLOW_PATH}')
    return 0


# Run coordination freshness checks unless explicitly skipped.
def verify_coordination(repo_root: Path, ci: bool, skip_coordination: bool) -> int:
    # Resolve the local-only coordination dashboard path.
    active_path = repo_root / 'docs' / 'coordination' / 'active.md'
    # Skip cadence checks when the caller asked.
    if skip_coordination:
        print('==> coordination cadence')
        print('SKIP: coordination check disabled by flag')
        return 0
    # Skip local-only coordination in CI checkouts.
    if ci and not active_path.exists():
        print('==> coordination cadence')
        print('SKIP: docs/coordination/active.md is local-only and not available in CI checkout')
        return 0
    # Delegate coordination policy to its dedicated script.
    return run_script(
        'coordination cadence',
        [sys.executable, 'tools/scripts/coordination.py', 'verify'],
        repo_root,
    )

# ---------- command-line bootstrap ----------

# Parse flags and run the bounded verification stages.
def main() -> int:
    # Keep the CLI description short and operator-friendly.
    parser = argparse.ArgumentParser(description='Run repo verification checks.')
    # Let CI suppress local-only coordination requirements.
    parser.add_argument('--ci', action='store_true', help='Use CI-safe behavior for local-only artifacts.')
    # Allow local users to skip cadence checks deliberately.
    parser.add_argument('--skip-coordination', action='store_true', help='Skip coordination cadence checks.')
    # Allow skipping reviewer-frontend verification for non-frontend changes.
    parser.add_argument('--skip-frontend', action='store_true', help='Skip reviewer-frontend verification.')
    # Parse the incoming command-line flags.
    args = parser.parse_args()

    # Resolve the repository root from this script location.
    repo_root = Path(__file__).resolve().parents[2]
    # Aggregate failures without hiding later check results.
    failures = 0
    # Compile Python scripts before higher-level policy checks.
    failures += verify_script_syntax(repo_root)
    # Check script explainability against repo policy.
    failures += verify_script_tldrs(repo_root)
    # Run the shared repo-control suites from their canonical modules.
    failures += verify_repo_test_modules(repo_root)
    # Keep the CI workflow routed through this verifier.
    failures += verify_repo_workflow_contract(repo_root)
    # Check coordination freshness unless the caller skipped it.
    failures += verify_coordination(repo_root, ci=args.ci, skip_coordination=args.skip_coordination)
    # Run reviewer-frontend verification unless skipped.
    if not args.skip_frontend:
        failures += run_script(
            'reviewer frontend',
            [sys.executable, 'tools/scripts/frontend.py'],
            repo_root,
        )

    # Fail the run when any stage reported issues.
    if failures:
        print('VERIFY FAILED')
        return 1

    # Report success once every stage passed.
    print('VERIFY PASSED')
    return 0


# ---------- test coverage ----------


# Keep verifier helper coverage beside the single verifier runtime.
class WorkflowContractTests(TestCase):
    # Accept the one canonical central verifier command.
    def test_detects_central_verifier_command(self) -> None:
        workflow_text = 'run: python3 tools/scripts/verify.py --ci\n'
        self.assertTrue(workflow_runs_central_verifier(workflow_text))

    # Reject workflows that bypass the central verifier entrypoint.
    def test_rejects_missing_central_verifier_command(self) -> None:
        workflow_text = 'run: python3 tools/scripts/other.py --ci\n'
        self.assertFalse(workflow_runs_central_verifier(workflow_text))

    # Reject multiline shell blocks that can hide extra policy.
    def test_rejects_multiline_run_blocks(self) -> None:
        workflow_text = 'run: |\n  python3 tools/scripts/verify.py --ci\n  echo hidden\n'
        self.assertFalse(workflow_runs_central_verifier(workflow_text))

    # Keep workflow failures actionable and path-specific.
    def test_reports_actionable_workflow_contract_failure(self) -> None:
        workflow_path = self.repo_root / '.github' / 'workflows' / 'repo-verify.yml'
        write_file(workflow_path, 'run: python3 tools/scripts/other.py --ci\n')

        output = io.StringIO()
        with redirect_stdout(output):
            result = verify_repo_workflow_contract(self.repo_root)

        self.assertEqual(result, 1)
        self.assertIn(str(Path('.github/workflows/repo-verify.yml')), output.getvalue())
        self.assertIn('expected the only shell run step to be', output.getvalue())


# Keep the module executable as a direct script.
if __name__ == '__main__':
    # Exit with the verifier status code.
    sys.exit(main())
