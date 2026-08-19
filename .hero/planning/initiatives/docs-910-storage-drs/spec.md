---
title: "9.1.0 Docs: Storage DRS-Like Functionality"
slug: docs-910-storage-drs
type: initiative
status: completed
horizon: now
tags: [9.1.0, docs]
priority: 2
jira: MORPH-12216
completed_at: 2026-08-19T15:11:11Z
---

# 9.1.0 Docs: Storage DRS-Like Functionality

## Summary

Document HVM Datastore Groups and Storage DRS-like automated storage placement for Morpheus 9.1.0.

## Scope

- Storage DRS configuration and policies
- Automated placement recommendations
- Rebalancing workflows
- Thresholds and tuning options
- HVM-only scope and supported NFS/GFS2 member types

## Acceptance Criteria

1. Document the **Datastore Group** UI name and clarify that it is a logical datastore type specific to HVM clusters.
2. Document eligible NFS and HPE Clustered Datastore members and exclude local, LUN-per-vDisk, nested, inactive, and already-grouped datastores.
3. Document the 70–95% **Space Threshold (%)**, default 85%, and the **Fully Automated** and recommendation-only automation levels.
4. Explain named-group and **Auto - Cluster** provisioning selection without simplifying projected-utilization placement to raw free-space selection.
5. Explain refresh-triggered rebalancing, migration eligibility, consecutive-cycle stabilization, recommendations, and process visibility.
6. Document the current maintenance-status limitation and advise removing a member or disabling provisioning before maintenance.

## Sources

- Jira Epic: MORPH-12216
