"""  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  API middleware registration surface

- Later Extension Points:
    --> Add request context, correlation, and edge-safe middleware wiring here

- Role:
    --> Holds the middleware seam at the public API boundary
    --> Owns request-edge concerns so startup and route files stay narrowly focused
    --> Exists as the single home for API middleware composition
    --> Must remain boundary-focused instead of hiding business rules in transport plumbing

- Exports:
    --> API middleware registration surface
    --> request_id_middleware, get_request_id

- Consumed By:
    --> local operators and implementers defining request-edge middleware
    --> apps/api/main.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  """
import os
import uuid
from typing import Callable


# ---------- request ID middleware ----------
# Per D5 clarification: use X-Request-ID as canonical header
REQUEST_ID_HEADER = "X-Request-ID"


class RequestIDMiddleware:
    """Middleware that ensures X-Request-ID is present on every request.
    
    - Preserves X-Request-ID if already present in incoming request
    - Generates new UUID if missing
    - Makes request ID available via get_request_id()
    """

    def __init__(self, app: Callable):
        self.app = app

    async def __call__(self, scope, receive, send):
        # Extract request ID from headers (case-insensitive)
        headers = dict(scope.get("headers", []))
        request_id = None
        
        for key, value in headers.items():
            if key.lower() == REQUEST_ID_HEADER.lower():
                request_id = value.decode("utf-8") if isinstance(value, bytes) else value
                break
        
        # Generate new request ID if not present
        if not request_id:
            request_id = str(uuid.uuid4())
        
        # Store in scope for access via get_request_id
        scope["request_id"] = request_id
        
        # Add to response headers
        async def send_wrapper(message):
            if message["type"] == "http.response.start":
                message["headers"].append(
                    (REQUEST_ID_HEADER.encode(), request_id.encode())
                )
            await send(message)
        
        await self.app(scope, receive, send_wrapper)


# ---------- request ID accessor ----------
_request_id_context = {}


def set_request_id(request_id: str) -> None:
    """Set request ID in context for current request."""
    _request_id_context["request_id"] = request_id


def get_request_id() -> str:
    """Get request ID from current context.
    
    Returns the X-Request-ID for the current request,
    or empty string if not in request context.
    """
    return _request_id_context.get("request_id", "")


def clear_request_id() -> None:
    """Clear request ID from context after request completes."""
    _request_id_context.pop("request_id", None)


# ---------- placeholder middleware registration ----------
# TODO: Replace with actual middleware composition
# from fastapi import FastAPI
# app = FastAPI()
# app.add_middleware(RequestIDMiddleware)


# ---------- runtime identity for middleware ----------
# Expose runtime identity for logging and traceability
def get_runtime_identity() -> dict:
    """Return runtime identity for current service."""
    return {
        "service_name": os.environ.get("SERVICE_NAME", "api"),
        "service_version": os.environ.get("SERVICE_VERSION", "0.0.0-dev"),
        "service_env": os.environ.get("SERVICE_ENV", "local"),
        "release_id": os.environ.get("RELEASE_ID", "dev-build"),
    }