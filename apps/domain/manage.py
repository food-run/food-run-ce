"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  domain management entrypoint

- Later Extension Points:
    --> Add bounded administrative commands and domain runtime wiring here

- Role:
    --> Establishes the managed command entry surface for domain-side administrative work
    --> Owns the bootstrap boundary for future maintenance and management commands
    --> Exists as the single governed script entry for domain management operations
    --> Must remain thin: command assembly only, not a second home for domain rules

- Exports:
    --> domain management entry path

- Consumed By:
    --> local operators running domain management commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
