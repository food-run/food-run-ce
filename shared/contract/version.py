"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  shared contract version surface

- Later Extension Points:
    --> Add reusable contract version markers and compatibility helpers here

- Role:
    --> Holds shared versioning ownership for externally visible contracts
    --> Owns reusable contract-version vocabulary so boundary consumers do not fork version markers
    --> Exists as the single home for shared contract version primitives
    --> Must remain version-focused instead of becoming a changelog or release-notes surface

- Exports:
    --> shared contract version surface

- Consumed By:
    --> local operators and implementers defining shared contract version markers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
