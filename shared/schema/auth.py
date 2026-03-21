"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  shared authorization schema surface

- Later Extension Points:
    --> Add reusable auth-related schema primitives shared across runtime boundaries

- Role:
    --> Holds shared auth vocabulary for transport-safe or reuse-proven schema shapes
    --> Owns reusable auth shape definitions so runtimes do not duplicate the same contract primitives
    --> Exists as the single home for shared authorization-related schema shapes
    --> Must remain shape-focused instead of becoming the home for business authorization policy

- Exports:
    --> shared authorization schema surface

- Consumed By:
    --> local operators and implementers defining shared auth schema primitives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
