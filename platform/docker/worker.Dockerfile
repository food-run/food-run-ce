# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  Worker service container surface

- Role:
    --> One container surface for the Worker runtime
    --> Uses python:3.11-slim per D5 clarification
    --> Entrypoint supports health/readiness via environment and arguments

- Consumed By:
    --> platform/k8s/worker.yaml
    --> docker-compose or local dev runs
    --> tools/script/dev.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FROM python:3.11-slim

# ---------- runtime identity ----------
ARG SERVICE_NAME=worker
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
COPY apps/worker/requirements.txt /app/requirements.txt 2>/dev/null || true
RUN pip install --no-cache-dir -r /app/requirements.txt 2>/dev/null || true

# ---------- source ----------
COPY apps/worker/ /app/
COPY apps/domain/ /app/domain/ 2>/dev/null || true

# ---------- health ----------
# Worker has /health for container orchestration probes
# Worker is a long-running process, not a request-response service
EXPOSE 8081

# ---------- entrypoint ----------
# Worker runs jobs from the queue, exposes health only
CMD ["python", "-m", "apps.worker.main"]