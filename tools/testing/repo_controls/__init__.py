#!/usr/bin/env python3
"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  package marker for repo-control verification suites under tools/testing

- Later Extension Points:
    --> Add repo-control suite helpers here only if several tests need a shared package-level seam

- Role:
    --> Marks the repo-control test folder as an importable unittest-discovery package
    --> Keeps nested verification coverage grouped under one governed ownership boundary
    --> Must stay empty until a real package-level behavior is needed

- Exports:
    --> package marker only

- Consumed By:
    --> `python3 -m unittest discover -s tools/testing -p 'test_*.py'`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
