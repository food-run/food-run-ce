"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  domain authorization policy surface

- Later Extension Points:
    --> Add role, scope, and business-owned authorization checks here

- Role:
    --> Holds authorization ownership for the domain truth boundary
    --> Owns policy evaluation so transport middleware and worker entrypoints do not become policy authorities
    --> Exists as the single home for business-owned authorization rules
    --> Must remain policy-focused instead of becoming a generic identity helper bucket

- Exports:
    --> domain authorization policy surface

- Consumed By:
    --> local operators and implementers defining business-owned authorization checks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
