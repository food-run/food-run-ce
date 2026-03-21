"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  shared event schema surface

- Later Extension Points:
    --> Add reusable event envelopes and event-shape primitives here

- Role:
    --> Holds shared event vocabulary for async and operational flows
    --> Owns event-shape reuse so runtimes do not fork competing event envelopes
    --> Exists as the single home for shared event schema definitions
    --> Must remain event-focused instead of becoming a worker-only implementation module

- Exports:
    --> shared event schema surface

- Consumed By:
    --> local operators and implementers defining shared event shapes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
