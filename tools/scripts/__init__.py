"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  mark the governed script home as an importable Python package

- Later Extension Points:
    --> Add package-level exports here only if the governed script surface truly needs a shared import seam

- Role:
    --> Makes `tools/scripts/` importable for unittest discovery in the central repo verifier
    --> Keeps the script home compatible with the current repo-control verification contract
    --> Must stay a package marker instead of becoming a second home for runtime policy logic

- Exports:
    --> Python package marker for `tools/scripts/`

- Consumed By:
    --> `tools/scripts/verify.py`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
