"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  package marker for the governed tooling tree

- Later Extension Points:
    --> Export exact tooling package seams here only when a stable cross-tool import surface is required

- Role:
    --> Makes `tools/` importable for unittest discovery and script-owned verification coverage
    --> Keeps the tooling tree aligned with the master-packet home without creating a second logic surface
    --> Must stay a thin package marker until broader tooling imports are intentionally designed

- Exports:
    --> package marker only

- Consumed By:
    --> `python3 -m unittest discover -s tools/scripts -p '*.py' -t .`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
