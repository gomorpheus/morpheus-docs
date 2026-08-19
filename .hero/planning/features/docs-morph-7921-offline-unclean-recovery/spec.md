---
title: "Recovery procedure for nodes in “Offline (Unclean)” state"
slug: docs-morph-7921-offline-unclean-recovery
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, hvm, recovery, fencing, troubleshooting]
tracker_id: MORPH-7921
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:49:50Z
---
# Recovery procedure for nodes in “Offline (Unclean)” state

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-7921

> When a node enters an **“Offline (Unclean)”** state in the cluster, there is currently **no documented recovery procedure**. This situation may occur due to **SCSI fencing or other cluster protection mechanisms**. Need documentation describing how to bring a fenced node back into service. Example remediation workflow may include `pcs status` and `pcs resource cleanup` (actual supported commands should be documented and verified).

Existing `infrastructure/clusters/hvm/monitoring.rst` identifies offline/fenced/unclean states, and `troubleshooting.rst` contains GFS2 recovery context. The missing work is a safe, layout-aware procedure.

## Goal
Provide a product-approved diagnosis, isolation, recovery, and validation workflow for Offline (Unclean) HVM nodes without bypassing fencing safety.

## Kickoff
Audit `infrastructure/clusters/hvm/monitoring.rst`, `troubleshooting.rst`, `failure_scenarios.rst`, `architecture.rst`, and `managing_hosts.rst`. Reproduce the state with HVM Engineering for each applicable layout. Confirm which UI indicators and commands are supported; `pcs` may be inappropriate for agent-quorum layouts 1.3/2.0. Require explicit stop/escalation conditions before publishing any cleanup command. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions.

## Approach
Add the recovery procedure to troubleshooting and cross-link monitoring state identification. Branch by cluster layout only where behavior is confirmed.

## Changes
1. Add identification, evidence collection, isolation checks, recovery, and validation to `infrastructure/clusters/hvm/troubleshooting.rst`.
2. Cross-link Offline/Fenced/Unclean indicators in `monitoring.rst` to the procedure.
3. Align causal context in `failure_scenarios.rst` and safety language in `architecture.rst`/`managing_hosts.rst`.

## Acceptance Criteria
- WHEN a node is Offline (Unclean) THE DOCUMENTATION SHALL explain how to identify fencing, resource blockers, and cluster state with approved indicators.
- BEFORE cleanup THE DOCUMENTATION SHALL require verified isolation and root-cause checks.
- IF recovery differs by cluster layout THEN THE DOCUMENTATION SHALL provide distinct, labeled procedures.
- IF safe recovery cannot be established THEN THE DOCUMENTATION SHALL stop and direct the operator to HPE Support.
- WHEN recovery completes THE DOCUMENTATION SHALL verify membership, storage, resources, and cluster health.

## Boundaries
No fencing bypass, speculative `pcs` command, or product recovery automation.

## Risks
Incorrect cleanup can cause split brain or data loss. Delivery is blocked pending HVM Engineering reproduction and command approval.

## Validation
Run the reviewed procedure in disposable affected layouts, capture before/after state, build docs, and secure HVM/Support sign-off.
