"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  shared adapter assembly surface

- Later Extension Points:
    --> Add adapter selection and construction wiring for reusable runtime dependencies

- Role:
    --> Holds shared adapter-assembly ownership for reusable dependency selection
    --> Owns construction flow so app runtimes do not hand-roll factory logic in multiple places
    --> Exists as the single home for shared adapter assembly and selection seams
    --> Must remain assembly-focused instead of becoming a generic dependency container

- Exports:
    --> shared adapter assembly surface

- Consumed By:
    --> local operators and implementers defining shared adapter selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
