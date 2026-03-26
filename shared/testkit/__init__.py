#!/usr/bin/env python3
"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  shared testkit export surface for deterministic Food Run verification support

- Later Extension Points:
    --> Re-export additional exact shared testkit modules here only when they become broadly reused

- Role:
    --> Keeps the shared testkit import surface stable while implementation lives in exact helper modules
    --> Re-exports the shared base case, fixtures, and loader helpers used across repo-control suites
    --> Must stay thin instead of becoming a second implementation home

- Exports:
    --> `TestCase`, fixture builders, and loader helpers from `shared/testkit/`

- Consumed By:
    --> shared testkit suites and future deterministic verification modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """

from __future__ import annotations

# ---------- imports and dependencies ----------

from .case import TestCase
from .fixtures import make_active_doc, make_active_workstream, make_heartbeat_note, make_plural_active_doc
from .helpers import load_module, load_script, write_file

# ---------- shared export surface ----------

__all__ = [
    'TestCase',
    'load_module',
    'load_script',
    'write_file',
    'make_heartbeat_note',
    'make_active_workstream',
    'make_active_doc',
    'make_plural_active_doc',
]
