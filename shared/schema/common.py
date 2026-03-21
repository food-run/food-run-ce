"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  shared common schema surface

- Later Extension Points:
    --> Add reusable schema primitives shared across multiple active runtimes

- Role:
    --> Holds common schema ownership for reusable non-domain-specific shapes
    --> Owns shared shape vocabulary so apps do not duplicate the same primitive structures
    --> Exists as the single home for common shared schema primitives
    --> Must remain primitive-focused instead of becoming a transport or domain junk drawer

- Exports:
    --> shared common schema surface

- Consumed By:
    --> local operators and implementers defining shared schema primitives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
