"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  worker retry policy surface

- Later Extension Points:
    --> Add retry windows, backoff rules, and failure classification here

- Role:
    --> Holds retry-policy ownership for asynchronous worker execution
    --> Owns retry semantics so queue consumers and job handlers do not duplicate backoff decisions
    --> Exists as the single home for worker retry and failure-recovery policy
    --> Must remain policy-focused instead of hiding queue wiring or job behavior

- Exports:
    --> worker retry policy surface

- Consumed By:
    --> local operators and implementers defining worker retry behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
