"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  public API route registration surface

- Later Extension Points:
    --> Add externally visible route groups and registration helpers here

- Role:
    --> Holds the bounded route-map seam for the public API runtime
    --> Owns endpoint registration so transport wiring does not sprawl across startup modules
    --> Exists as the single home for API-facing route composition
    --> Must remain route-focused instead of absorbing request schemas or domain rules

- Exports:
    --> API route registration surface

- Consumed By:
    --> local operators and implementers extending the public API route map
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
