"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  governed agent graph composition surface

- Later Extension Points:
    --> Add graph nodes, transitions, and artifact-aware execution flow here

- Role:
    --> Holds the future workflow-composition seam for governed agent behavior
    --> Owns graph assembly so runtime startup does not become a hidden orchestration layer
    --> Exists as the single home for agent graph structure and execution topology
    --> Must remain graph-focused instead of turning into a grab bag for runtime helpers

- Exports:
    --> agent graph composition surface

- Consumed By:
    --> local operators and implementers extending governed agent graph behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
