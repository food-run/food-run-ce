"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  public API runtime entrypoint

- Later Extension Points:
    --> Compose routes, middleware, schemas, and startup wiring here

- Role:
    --> Establishes the active request-facing runtime entry point for the rebuild API surface
    --> Owns the startup boundary where route and middleware wiring will later assemble
    --> Exists as the single executable entry file for the governed API runtime
    --> Must remain thin: startup and composition only, not a second home for domain logic

- Exports:
    --> API runtime entry path

- Consumed By:
    --> local operators starting the API runtime
    --> platform/docker/api.Dockerfile
    --> platform/k8s/api.yaml
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
import os

# ---------- runtime identity ----------
SERVICE_NAME = os.environ.get("SERVICE_NAME", "api")
SERVICE_VERSION = os.environ.get("SERVICE_VERSION", "0.0.0-dev")
SERVICE_ENV = os.environ.get("SERVICE_ENV", "local")
RELEASE_ID = os.environ.get("RELEASE_ID", "dev-build")


# ---------- health endpoints ----------
def health():
    """Liveness probe - service is running."""
    return {
        "status": "ok",
        "service": SERVICE_NAME,
    }


def ready():
    """Readiness probe - service is ready to accept traffic."""
    # TODO: Add dependency checks (DB, cache, etc.) before returning ready
    return {
        "status": "ready",
        "service": SERVICE_NAME,
        "environment": SERVICE_ENV,
    }


# ---------- runtime info ----------
def info():
    """Runtime identity endpoint."""
    return {
        "service": SERVICE_NAME,
        "version": SERVICE_VERSION,
        "environment": SERVICE_ENV,
        "release": RELEASE_ID,
    }


# ---------- placeholder app ----------
# TODO: Replace with actual FastAPI/Flask app
# from fastapi import FastAPI
# app = FastAPI()
# app.add_api_route("/health", health)
# app.add_api_route("/ready", ready)
# app.add_api_route("/info", info)

if __name__ == "__main__":
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    host = sys.argv[2] if len(sys.argv) > 2 else "0.0.0.0"
    print(f"Starting {SERVICE_NAME} {SERVICE_VERSION} on {host}:{port}")
    print(f"Environment: {SERVICE_ENV}, Release: {RELEASE_ID}")
    print(f"Health: /health, Readiness: /ready, Info: /info")
    # TODO: Replace with actual server startup
    # uvicorn.run(app, host=host, port=port)