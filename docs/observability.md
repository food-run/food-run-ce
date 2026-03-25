# Observability Baseline

## TL;DR

S0-D5 establishes the first observability vocabulary for the rebuild. This file defines the baseline metrics, logging conventions, and runtime identity format that later observability work extends from.

---

## Runtime Identity

All services expose identity via environment variables:

| Variable | Purpose | Example |
|----------|---------|---------|
| `SERVICE_NAME` | Service identifier | `api`, `worker`, `agent` |
| `SERVICE_VERSION` | Version string | `0.0.0-dev`, `1.2.3` |
| `SERVICE_ENV` | Environment | `local`, `staging`, `production` |
| `RELEASE_ID` | Release identifier | `dev-build`, `2026.03.24.1` |
| `COMMIT_SHA` | (optional) Git commit | `abc123f` |

---

## Health Endpoints

| Endpoint | Purpose | Auth Required |
|----------|---------|---------------|
| `/health` | Liveness probe | No |
| `/ready` | Readiness probe | No |
| `/metrics` | Prometheus metrics | No (later) |

- `/health` - Confirms service is running (always returns 200)
- `/ready` - Confirms service dependencies are available (DB, cache, etc.)
- `/metrics` - Reserved for later Prometheus exposure

---

## Metrics Convention

Per D5 clarification, use namespaced Prometheus-style metrics:

### HTTP Metrics

| Metric | Type | Description |
|--------|------|-------------|
| `foodrun_http_requests_total` | Counter | Total HTTP requests |
| `foodrun_http_request_duration_seconds` | Histogram | Request duration |
| `foodrun_http_request_errors_total` | Counter | Total errors |

### Labels

- `service` - SERVICE_NAME
- `route` - Request path pattern
- `method` - HTTP method
- `status_class` - 2xx, 4xx, 5xx

### Example Output

```
foodrun_http_requests_total{service="api",route="/users",method="GET",status_class="2xx"} 1234
foodrun_http_request_duration_seconds{service="api",route="/users",method="GET",status_class="2xx"} 0.045
```

---

## Request Correlation

Use `X-Request-ID` as the canonical request correlation header:

- **Preserve** if present in incoming request
- **Generate** (UUID) if missing
- **Expose** in logs and response headers
- **Forward** through edge/gateway

---

## Logging Convention

Each service should log:

```
[ISO8601 timestamp] [SERVICE_NAME] [X-Request-ID] [LEVEL] message
```

Example:
```
2026-03-24T10:30:00Z api abc-123 INFO incoming request method=GET path=/users
```

---

## Future Extensions

Sprint 0 sets vocabulary only. Later sprints can extend with:

- `foodrun_queue_depth` - Queue depth metrics
- `foodrun_stream_lag` - Stream processing lag
- `foodrun_cache_hit_total` - Cache hit/miss metrics
- `foodrun_release_marker_total` - Release event tracking

---

## Related Files

- `platform/docker/*.Dockerfile` - Container surfaces
- `platform/k8s/*.yaml` - Local cluster manifests
- `platform/edge/*.yaml` - Edge policy vocabulary
- `apps/api/middleware.py` - Request ID middleware
- `docs/resilience.md` - Resilience patterns