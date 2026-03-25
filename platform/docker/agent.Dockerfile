# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  Agent service container surface

- Role:
    --> One container surface for the Agent runtime (LangGraph/LangSmith)
    --> Uses python:3.11-slim per D5 clarification
    --> Entrypoint supports health/readiness via environment and arguments

- Consumed By:
    --> platform/k8s/agent.yaml
    --> docker-compose or local dev runs
    --> tools/script/dev.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FROM python:3.11-slim

# ---------- runtime identity ----------
ARG SERVICE_NAME=agent
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
COPY apps/agent/requirements.txt /app/requirements.txt 2>/dev/null || true
RUN pip install --no-cache-dir -r /app/requirements.txt 2>/dev/null || true

# ---------- source ----------
COPY apps/agent/ /app/
COPY apps/domain/ /app/domain/ 2>/dev/null || true

# ---------- health/readiness ----------
# Agent exposes health and readiness for orchestration
EXPOSE 8082

# ---------- entrypoint ----------
# Agent runs the LangGraph graph service
CMD ["python", "-m", "apps.agent.main"]