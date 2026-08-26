---
title: "9.1.0 Docs: Agent Log Throttle Settings"
slug: docs-910-agent-log-throttle
type: feature
status: planning
horizon: now
tags: [9.1.0, docs]
priority: 2
jira: MORPH-8559
---

# 9.1.0 Docs: Agent Log Throttle Settings

## Summary

Document the Agent Log Throttle Policy feature under Administration → Settings → Monitoring → Logging (Advanced Options). Includes log rate monitoring, enforcement (disabling logging on offending servers), per-server overrides, auto re-enable, and agent log deduplication.

## Acceptance Criteria

1. Document the global settings: Policy (Off/Monitor/Enforce), Threshold (KB/min, min 100), Window (5-60 min), Auto Re-enable (on/off), Cooldown (≥ window).
2. Document the ceiling calculation: `threshold × window × 1024` bytes per window.
3. Document Monitor mode behavior: alarm raised on Operations → Alarms, logs continue to be stored, alarm auto-cleared after cooldown.
4. Document Enforce mode behavior: logging disabled on server, log batches dropped at WebSocket layer, agent commanded to stop transmitting, manual re-enable required when auto re-enable is off.
5. Document per-server override via Infrastructure → Compute → [Server] → Edit → Log Throttle Policy.
6. Document the API: `GET/PUT /api/log-settings` with fields `logThrottlePolicy`, `logThrottleThreshold`, `logThrottleWindow`, `logThrottleAutoReEnable`, `logThrottleCooldown`.
7. Document the Agent Log Deduplication toggle: suppresses duplicate messages per server within a 30-second window.
8. Document the alarm categories (`log.throttle.monitor`, `log.throttle.enforce`) and the global parameter on `api/health/alarms` for cross-tenant queries.

## Sources

- Jira: MORPH-8559
