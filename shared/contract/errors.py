"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  shared contract error surface

- Later Extension Points:
    --> Add reusable transport-safe error shapes and shared error vocabulary here

- Role:
    --> Holds shared contract-error ownership for public-facing boundaries
    --> Owns reusable error vocabulary so app runtimes do not invent near-duplicate error shapes
    --> Exists as the single home for shared contract error primitives
    --> Must remain contract-focused instead of becoming a dumping ground for app-local failures

- Exports:
    --> shared contract error surface

- Consumed By:
    --> local operators and implementers defining shared contract error vocabulary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
