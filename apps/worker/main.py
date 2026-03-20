"""
TL;DR
Starter surface for the async worker runtime.

Runtime role
- Own future worker startup and queue-processing bootstrap.

Later extension points
- Compose jobs, queue wiring, and retry policy from this module.
"""
