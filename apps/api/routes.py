"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  public API route registration surface

- Later Extension Points:
    --> Add externally visible route groups and registration helpers here

- Role:
    --> Holds the bounded route-map seam for the public API runtime
    --> Owns endpoint registration so transport wiring does not sprawl across startup modules
    --> Exists as the single home for API-facing route composition
    --> Must remain route-focused instead of absorbing request schemas or domain rules

- Exports:
    --> API route registration surface
    --> health_routes, ready_routes

- Consumed By:
    --> local operators and implementers extending the public API route map
    --> apps/api/main.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
# ---------- health routes ----------
# These routes are used by k8s liveness/readiness probes
# and should not require authentication

health_routes = {
    "GET /health": "Liveness probe - service is running",
    "GET /ready": "Readiness probe - service dependencies ready",
}


def register_health_routes(app):
    """Register health and readiness endpoints.
    
    TODO: Replace with actual route registration
    # from apps.api.main import health, ready
    # app.add_route("/health", health)
    # app.add_route("/ready", ready)
    """
    pass


# ---------- placeholder route registration ----------
# TODO: Replace with actual route composition
# from fastapi import FastAPI
# register_health_routes(app)


# ---------- route conventions ----------
# Per D5 clarification:
# - /health - liveness (always available)
# - /ready - readiness (depends on dependencies)
# - /metrics - reserved for later Prometheus exposure
# - /info - runtime identity (optional, non-standard)
#
# All health endpoints should be unauthenticated and
# not require any dependencies to be available.