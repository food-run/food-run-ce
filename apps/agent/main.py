"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  agent workflow startup and runtime spine

- Later Extension Points:
    --> Compose graph, evaluation, and store wiring

- Role:
    --> Establishes the active runtime entry point for governed agent workflows
    --> Will later coordinate graph execution, artifact creation, eval wiring, approval handoffs, and runtime visibility
    --> Exists as the single executable surface for repo-bound agent operations
    --> Must remain governed and artifact-oriented rather than acting as a hidden autonomous control layer

- Exports:
    --> agent runtime entry

- Consumed By:
    --> local operators starting the agent runtime during governed runs
    --> platform/docker/agent.Dockerfile
    --> platform/k8s/agent.yaml
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
import os

# ---------- runtime identity ----------
SERVICE_NAME = os.environ.get("SERVICE_NAME", "agent")
SERVICE_VERSION = os.environ.get("SERVICE_VERSION", "0.0.0-dev")
SERVICE_ENV = os.environ.get("SERVICE_ENV", "local")
RELEASE_ID = os.environ.get("RELEASE_ID", "dev-build")


# ---------- health endpoints ----------
def health():
    """Liveness probe - agent service is running."""
    return {
        "status": "ok",
        "service": SERVICE_NAME,
    }


def ready():
    """Readiness probe - agent service is ready.
    
    Agent is ready when graph, store, and eval components are initialized.
    """
    # TODO: Add dependency checks (LangSmith connection, store, etc.)
    return {
        "status": "ready",
        "service": SERVICE_NAME,
        "environment": SERVICE_ENV,
    }


def info():
    """Runtime identity endpoint."""
    return {
        "service": SERVICE_NAME,
        "version": SERVICE_VERSION,
        "environment": SERVICE_ENV,
        "release": RELEASE_ID,
    }


# ---------- placeholder agent startup ----------
# TODO: Replace with actual agent startup
# from apps.agent.graph import get_graph
# from apps.agent.store import get_store
# from apps.agent.evals import get_evals
#
# graph = get_graph()
# store = get_store()
# evals = get_evals()

if __name__ == "__main__":
    print(f"Starting {SERVICE_NAME} {SERVICE_VERSION} on port 8082")
    print(f"Environment: {SERVICE_ENV}, Release: {RELEASE_ID}")
    print(f"Health: /health, Readiness: /ready, Info: /info")
    # TODO: Replace with actual agent server startup
    # import uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8082)