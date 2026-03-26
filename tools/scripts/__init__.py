"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  package marker for governed script entrypoints

- Later Extension Points:
    --> Re-export exact script entrypoints here only when a stable package-level import surface is justified

- Role:
    --> Makes `tools/scripts/` importable for unittest discovery after script and test consolidation
    --> Keeps the single-home script layout aligned with the target repo structure in the master packet
    --> Must stay a thin package marker instead of becoming a second script registry

- Exports:
    --> package marker only

- Consumed By:
    --> `python3 -m unittest discover -s tools/scripts -p '*.py' -t .`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
