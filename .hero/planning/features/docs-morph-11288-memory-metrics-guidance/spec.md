---
title: "Explanation of Memory Metrics, Thresholds, and Operational Guidance"
slug: docs-morph-11288-memory-metrics-guidance
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, health, memory, monitoring, operations]
tracker_id: MORPH-11288
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:31:32Z
---
# Explanation of Memory Metrics, Thresholds, and Operational Guidance

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-11288

Administration > Health exposes System Memory, Used/Free Memory, Morpheus Memory Usage, and application/container limits, but users cannot tell how values relate, why they do not add up, what warnings mean, or which action to take. The report observes Morpheus usage above 60% with an apparent ~7.8 GiB application limit.

## Goal
Provide authoritative definitions, calculations, thresholds, scope, sampling caveats, and action guidance for every displayed memory metric.

## Kickoff
Deliver `.hero/planning/features/docs-morph-11288-memory-metrics-guidance/spec.md`; update `administration/health/health.rst` and reconcile `administration/settings/guidance.rst`.

## Approach
Derive definitions from implementation/observability owners, distinguish host, process/JVM/container, cache, instantaneous, and percentage metrics, then map warning levels to actions.

## Changes
1. `administration/health/health.rst` — Added implementation-derived JVM/system formulas, scopes, relationships, HA context, sampling caveats, ordered thresholds, and operator decisions.
2. `administration/settings/guidance.rst` — Distinguished workload resize Guidance from appliance Health alarms.

## Acceptance Criteria
- WHEN users compare memory values THE SYSTEM SHALL explain why totals may not arithmetically align.
- WHEN a warning appears THE SYSTEM SHALL identify its threshold, evaluated metric, scope, and recommended action.
- THE SYSTEM SHALL distinguish appliance system memory from Morpheus process/application/container memory.
- IF behavior differs in HA or containerized deployments THEN THE SYSTEM SHALL state that context.

## Boundaries
No monitoring implementation or threshold changes.

## Risks
Existing prose may be stale; formulas and defaults must come from the current implementation, not observation alone.

## Validation
Engineering review of every formula/threshold, compare against sample Health output, render tables, and run `make test`.
