"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  shared runtime and filesystem helpers for testkit modules

- Later Extension Points:
    --> Add more deterministic loader and file helpers here when shared suites need them broadly

- Role:
    --> Owns module-loading and file-writing helpers reused across shared testkit modules
    --> Keeps script imports and temp-repo file writes in one deterministic home
    --> Must stay test-focused instead of becoming a generic utility bucket

- Exports:
    --> `load_module`, `load_script`, and `write_file`

- Consumed By:
    --> shared testkit suites and helper modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """

from __future__ import annotations

# ---------- imports and dependencies ----------

import importlib.util
from pathlib import Path

# ---------- shared helper paths ----------

# Keep the governed script home centralized for dynamic loads.
SCRIPTS_PATH = Path(__file__).resolve().parents[2] / 'tools' / 'scripts'

# ---------- loader and file helpers ----------


# Load one Python module from an explicit file path.
def load_module(name: str, module_path: Path):
    spec = importlib.util.spec_from_file_location(name, module_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# Load one governed script module by semantic filename.
def load_script(name: str):
    return load_module(name, SCRIPTS_PATH / f'{name}.py')


# Write one file and create its parent directories first.
def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')
