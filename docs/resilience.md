# Resilience Patterns

## TL;DR

S0-D5 establishes baseline resilience vocabulary for the rebuild. This file defines retry, timeout, and fallback patterns that later feature work extends from.

---

## Retry Patterns

### Background Jobs (Worker)

Jobs should implement:

- **Exponential backoff** with jitter
- **Maximum retries** (configurable, default 3)
- **Dead letter** handling after max retries

```python
# Example retry configuration
retry_config = {
    "max_attempts": 3,
    "base_delay": 1,  # seconds
    "max_delay": 30,  # seconds
    "jitter": True,
}
```

### API Calls

Outbound API calls should:

- Timeout after configurable period (default 30s)
- Retry on transient failures (5xx, network errors)
- Not retry on client errors (4xx)
- Propagate context (request ID, service identity)

---

## Timeout Patterns

### Service-to-Service

| Call Type | Timeout | Notes |
|-----------|---------|-------|
| DB queries | 10s | Configurable per query type |
| Cache ops | 2s | Fast-fail for cache |
| External APIs | 30s | Per D5 gateway config |
| Queue ops | 5s | Non-blocking |

### k8s Probe Timeouts

| Probe | Initial Delay | Period | Timeout |
|-------|---------------|--------|---------|
| Liveness | 10s | 15s | 5s |
| Readiness | 5s | 10s | 5s |

---

## Circuit Breaker Pattern

Sprint 0 documents the pattern; implementation comes later.

### States

- **Closed** - Normal operation, requests pass through
- **Open** - Failure threshold exceeded, requests fail fast
- **Half-Open** - Test if service recovered

### Configuration

```yaml
circuit_breaker:
  failure_threshold: 5
  success_threshold: 2
  timeout: 30
```

---

## Graceful Degradation

### Service Dependencies

When a dependency is unavailable:

1. Return cached response if available
2. Return degraded response (e.g., empty list)
3. Return error with clear message

### Health Checks

- `/health` should never fail (liveness)
- `/ready` can fail if dependencies unavailable (readiness)

---

## Related Files

- `platform/edge/limits.yaml` - Request limits
- `platform/edge/gateway.yaml` - Gateway timeout config
- `platform/k8s/*.yaml` - Probe configuration
- `docs/observability.md` - Metrics and logging