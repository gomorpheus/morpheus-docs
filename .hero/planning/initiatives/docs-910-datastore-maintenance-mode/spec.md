---
title: "9.1.0 Docs: Datastore Evacuation / Maintenance Mode"
slug: docs-910-datastore-maintenance-mode
type: initiative
status: completed
horizon: now
tags: [9.1.0, docs]
priority: 2
jira: MORPH-12233
completed_at: 2026-08-19T15:30:13Z
---

# 9.1.0 Docs: Datastore Evacuation / Maintenance Mode

## Summary

Document datastore evacuation and maintenance mode functionality for Morpheus 9.1.0.

## Scope

- Entering and exiting datastore maintenance mode
- VM evacuation workflows
- Storage migration during maintenance
- Prerequisites and limitations

## Acceptance Criteria

1. Document the HVM cluster-scoped `Enter Maintenance` and `Leave Maintenance` actions.
2. Explain explicit target selection and automatic destination planning.
3. Document snapshot, powered-off local-storage, capacity, and provider-volume limitations.
4. Explain Entering, Maintenance, Exiting, and Available states and the lack of user-facing cancellation.
5. Distinguish datastore maintenance from Host maintenance and integrate the workflow with datastore removal.
6. Preserve the Datastore Group member-maintenance limitation and required workaround.

## Sources

- Jira Epic: MORPH-12233
