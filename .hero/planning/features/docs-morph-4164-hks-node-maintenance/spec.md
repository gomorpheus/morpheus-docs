---
title: "HKS - document maintenance mode for master and workers"
slug: docs-morph-4164-hks-node-maintenance
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, hks, kubernetes, maintenance]
tracker_id: MORPH-4164
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:31:18Z
---
# HKS - document maintenance mode for master and workers

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-4164

Jira description (verbatim):

> HKS - document maintenance mode for master and workers

Current HVM maintenance guidance in `infrastructure/clusters/hvm/host_maintenance.rst` is not necessarily applicable to HKS. Kubernetes cluster documentation exists in `infrastructure/clusters/kubernetes.rst` and `infrastructure/clusters/clusters.rst`.

## Goal

Document supported HKS maintenance workflows separately for control-plane/master and worker nodes, covering preflight, workload effects, drain/cordon behavior, quorum, execution, return to service, and failure recovery.

## Kickoff

Create HKS-specific maintenance procedures for control-plane and worker nodes without reusing HVM semantics blindly.

**Status:** planning — HVM maintenance is documented; HKS actions and product orchestration require validation.

**Pick up at:** exercise maintenance on representative HKS master and worker nodes and capture workload and quorum behavior.

→ `.hero/planning/features/docs-morph-4164-hks-node-maintenance/spec.md`

**Files:** `infrastructure/clusters/kubernetes.rst`, `infrastructure/clusters/clusters.rst`, `infrastructure/clusters/hvm/host_maintenance.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Add an HKS-specific page with two clear procedures and use upstream Kubernetes terms only where they reflect product behavior. Cross-link but do not duplicate HVM maintenance.

## Changes

1. `infrastructure/clusters/hks_node_maintenance.rst` — Added separate code-evidenced worker and control-plane maintenance workflows.
2. `infrastructure/clusters/clusters.rst` and `infrastructure/clusters/kubernetes.rst` — Linked the HKS maintenance guide.
3. `infrastructure/clusters/hvm/host_maintenance.rst` — Audited but unchanged because the new HKS-specific navigation prevents reuse.

## Acceptance Criteria

- WHEN a worker enters maintenance THE DOCUMENTATION SHALL describe workload evacuation, daemon sets, disruption budgets, validation, and return to service.
- WHEN a master/control-plane node enters maintenance THE DOCUMENTATION SHALL describe quorum and API availability prerequisites and stop conditions.
- IF Morpheus automates cordon or drain THE DOCUMENTATION SHALL distinguish automated from manual actions.

## Boundaries

No generic Kubernetes upgrade guide, HVM maintenance rewrite, or unsupported force-drain recommendation.

## Risks

- **Blocker:** Jira does not specify current UI actions or automation semantics.
- Incorrect control-plane guidance can cause loss of cluster quorum or API availability.

## Validation

Test both procedures with representative workloads and disruption budgets, verify recovery from an interrupted operation, obtain HKS engineering review, and run `make build`.
