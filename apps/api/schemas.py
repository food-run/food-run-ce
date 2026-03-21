"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  API schema wiring surface

- Later Extension Points:
    --> Add request and response shapes that reuse shared schema primitives

- Role:
    --> Holds transport-level schema ownership for the public API boundary
    --> Owns API-facing shapes so domain models do not leak straight into request contracts
    --> Exists as the single home for API schema composition and validation wiring
    --> Must remain transport-focused instead of becoming domain authority

- Exports:
    --> API schema wiring surface

- Consumed By:
    --> local operators and implementers defining public API request and response shapes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
