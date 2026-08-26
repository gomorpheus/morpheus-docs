---
title: "9.1.0 Docs: Support Bundle Generation via UI"
slug: docs-910-support-bundle-ui
type: feature
status: planning
horizon: now
tags: [9.1.0, docs]
priority: 2
jira: MORPH-11382
---

# 9.1.0 Docs: Support Bundle Generation via UI

## Summary

Document the new support bundle generation feature that allows administrators to collect diagnostic logs, health metrics, and telemetry data through the Morpheus UI, with options to download or upload to HPE Support.

## Acceptance Criteria

1. Document how to initiate support bundle generation from the UI (navigation path, permissions required).
2. Document what the bundle contains: logs (check-server, guacd, morpheus-ui, mysql, nginx, opensearch), health summary (CPU, memory, storage, DB, elastic, queue, threads), and configuration stats.
3. Document HPE Support integration: automatic telemetry when call-home is enabled, manual bundle generation when it is not.
4. Document the Alletra MP storage plugin contribution: telemetry collection on configured Alletra storage servers.
5. Document the feature flag gating for safe rollout.
6. Document the station ID reporting for appliance identification.
7. Document size estimation and disk space gating behavior.
8. Note that per-component failure isolation: one array failing does not block the overall bundle.

## Sources

- Jira Epic: MORPH-11382
- Design doc: https://refactored-potato-vm4yzvn.pages.github.io/docs/morpheus/support-bundle.html
