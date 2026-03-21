"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  API middleware registration surface

- Later Extension Points:
    --> Add request context, correlation, and edge-safe middleware wiring here

- Role:
    --> Holds the middleware seam at the public API boundary
    --> Owns request-edge concerns so startup and route files stay narrowly focused
    --> Exists as the single home for API middleware composition
    --> Must remain boundary-focused instead of hiding business rules in transport plumbing

- Exports:
    --> API middleware registration surface

- Consumed By:
    --> local operators and implementers defining request-edge middleware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
