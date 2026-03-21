"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  agent evaluation hook surface

- Later Extension Points:
    --> Add governed evaluation cases, fixtures, and runners for agent behavior

- Role:
    --> Holds the bounded evaluation seam for agent-runtime quality checks
    --> Owns the future wiring point for eval scenarios without leaking them into startup code
    --> Exists as the single home for agent-specific evaluation orchestration
    --> Must remain evaluation-focused rather than becoming a second workflow runtime

- Exports:
    --> agent evaluation hook surface

- Consumed By:
    --> local operators extending or running agent evaluation coverage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
