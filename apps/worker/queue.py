"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  worker queue-consumer surface

- Later Extension Points:
    --> Add queue polling, message handling, and worker-consumer wiring here

- Role:
    --> Holds queue-consumer ownership for the worker runtime boundary
    --> Owns async queue wiring so job definitions and retry policy stay narrowly focused
    --> Exists as the single home for worker-side queue consumption behavior
    --> Must remain worker-focused instead of becoming a shared adapter abstraction

- Exports:
    --> worker queue-consumer surface

- Consumed By:
    --> local operators and implementers defining worker queue consumption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
