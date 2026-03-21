"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  shared test factory surface

- Later Extension Points:
    --> Add deterministic object-construction helpers reused across tests

- Role:
    --> Holds shared test-factory ownership for reusable setup construction
    --> Owns object-construction seams so tests do not fork duplicate fixture builders
    --> Exists as the single home for shared deterministic test factories
    --> Must remain test-focused instead of becoming a general-purpose object helper bucket

- Exports:
    --> shared test factory surface

- Consumed By:
    --> local operators and implementers defining shared test factories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
