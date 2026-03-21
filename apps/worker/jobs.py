"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  worker job definition surface

- Later Extension Points:
    --> Add background job handlers and dispatch metadata here

- Role:
    --> Holds job-definition ownership for the worker runtime boundary
    --> Owns async job structure so queue wiring and retry policy stay in their own files
    --> Exists as the single home for worker job definitions
    --> Must remain job-focused instead of turning into a second queue adapter layer

- Exports:
    --> worker job definition surface

- Consumed By:
    --> local operators and implementers defining background job behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
