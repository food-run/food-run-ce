# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  API service container surface

- Role:
    --> One container surface for the API runtime
    --> Uses python:3.11-slim per D5 clarification
    --> Entrypoint supports health/readiness via environment and arguments

- Consumed By:
    --> platform/k8s/api.yaml
    --> docker-compose or local dev runs
    --> tools/script/dev.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FROM python:3.11-slim

# ---------- runtime identity ----------
# Passed via docker build --build-arg and docker run -e
ARG SERVICE_NAME=api
ARG SERVICE_VERSION=0.0.0-dev
ARG SERVICE_ENV=local
ARG RELEASE_ID=dev-build

ENV SERVICE_NAME=${SERVICE_NAME}
ENV SERVICE_VERSION=${SERVICE_VERSION}
ENV SERVICE_ENV=${SERVICE_ENV}
ENV RELEASE_ID=${RELEASE_ID}

# ---------- working directory ----------
WORKDIR /app

# ---------- dependencies ----------
# Install dependencies before copying source for better layer caching
COPY apps/api/requirements.txt /app/requirements.txt 2>/dev/null || true
RUN pip install --no-cache-dir -r /app/requirements.txt 2>/dev/null || true

# ---------- source ----------
COPY apps/api/ /app/
COPY apps/domain/ /app/domain/ 2>/dev/null || true

# ---------- health/readiness ----------
# /health - liveness probe
# /ready - readiness probe (depends on dependencies)
EXPOSE 8080

# ---------- entrypoint ----------
# Supports: python -m apps.api.main [ --host 0.0.0.0 --port 8080 ]
CMD ["python", "-m", "apps.api.main"]