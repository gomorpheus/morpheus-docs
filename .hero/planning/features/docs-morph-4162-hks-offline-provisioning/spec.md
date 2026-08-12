---
title: "HKS offline provisioning - document the process"
slug: docs-morph-4162-hks-offline-provisioning
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, hks, offline, provisioning, kubernetes]
tracker_id: MORPH-4162
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:09:14Z
---
# HKS offline provisioning - document the process

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-4162

Jira description (verbatim):

> HKS offline provisioning - document the process

Existing offline package guidance is in `getting_started/additional/offline.rst`; HKS cluster documentation is under `infrastructure/clusters/` and package concepts in `library/blueprints/clusterLayouts.rst`. No approved HKS offline procedure was supplied.

## Goal

Document a validated HKS offline provisioning workflow covering required artifacts, staging, network/DNS/registry assumptions, configuration, provisioning, verification, upgrades, and troubleshooting.

## Kickoff

Create the supported HKS offline-provisioning runbook using release-approved artifacts and current cluster fields.

**Status:** planning — generic offline guidance exists; HKS artifact inventory and disconnected workflow require engineering input.

**Pick up at:** obtain the supported HKS offline bill of materials and execute provisioning in a truly disconnected test environment.

→ `.hero/planning/features/docs-morph-4162-hks-offline-provisioning/spec.md`

**Files:** `getting_started/additional/offline.rst`, `infrastructure/clusters/clusters.rst`, `library/blueprints/clusterLayouts.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Add an HKS-specific guide under cluster documentation and reference generic appliance offline setup. Use checksums and release-scoped artifact sources; do not invent registry or package names.

## Changes

1. `infrastructure/clusters/hks_offline_provisioning.rst` — Added the code-evidenced image-server provisioning and offline upgrade workflow without inventing release artifact paths.
2. `infrastructure/clusters/clusters.rst` — Added the guide to cluster navigation.
3. `getting_started/additional/offline.rst` — Distinguished appliance offline installation from HKS offline provisioning.
4. `library/blueprints/clusterLayouts.rst` — Audited but unchanged; no additional release-approved artifact prerequisites were available.

## Acceptance Criteria

- WHEN an administrator prepares an offline HKS deployment THE DOCUMENTATION SHALL list every approved artifact, source, version constraint, checksum step, and staging location.
- WHEN provisioning begins THE DOCUMENTATION SHALL cover configuration, execution, verification, and failure diagnostics without external network assumptions.
- IF an artifact or registry path is not release-approved THEN THE DOCUMENTATION SHALL not invent it.

## Boundaries

No air-gapped registry implementation, artifact redistribution policy, HKS product changes, or generic Kubernetes offline guide.

## Risks

- **Blocker:** Jira provides no artifact list, supported versions, or workflow.
- Offline instructions become stale quickly as package sets and image tags change.

## Validation

Provision HKS without internet egress from a clean environment, verify checksums and all pulled artifacts, test failure messages, run `make build`, and secure HKS engineering sign-off.
