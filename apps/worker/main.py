"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  async worker runtime entrypoint

- Later Extension Points:
    --> Compose queue wiring, job registration, and retry startup here

- Role:
    --> Establishes the active background-worker runtime entry point for the rebuild
    --> Owns the startup boundary where queue, jobs, and retry policies will later assemble
    --> Exists as the single executable entry file for governed worker processing flows
    --> Must remain thin: bootstrap and wiring only, not a hidden job-definition layer

- Exports:
    --> worker runtime entry path

- Consumed By:
    --> local operators starting the worker runtime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
