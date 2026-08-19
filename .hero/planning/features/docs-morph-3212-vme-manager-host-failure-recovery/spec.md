---
title: "How to recover the VME Manager when the host it lives on fails"
slug: docs-morph-3212-vme-manager-host-failure-recovery
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, vme, disaster-recovery, manager]
tracker_id: MORPH-3212
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:17:20Z
---
# How to recover the VME Manager when the host it lives on fails

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-3212

Jira description (verbatim):

> Document recovery process for the VME manager when the host it lives on fails

Relevant backup and recovery material exists in `getting_started/guides/backup_restore.rst`, `getting_started/maintenance/db_migration.rst`, and `getting_started/installation/singleNode/hpe_installer.rst`; none should be assumed to define the requested VME host-failure workflow.

## Goal

Document an engineering-approved VME Manager recovery runbook for loss of its host, covering prerequisites, supported recovery sources, identity/network considerations, validation, and escalation.

## Kickoff

Create a validated runbook for recovering VME Manager after its hosting hypervisor fails.

**Status:** planning — backup and installation references exist; supported recovery scenarios and artifacts need confirmation.

**Pick up at:** define failure scenarios and required backups with VME engineering, then exercise the preferred recovery path.

→ `.hero/planning/features/docs-morph-3212-vme-manager-host-failure-recovery/spec.md`

**Files:** `getting_started/guides/backup_restore.rst`, `getting_started/maintenance/db_migration.rst`, `getting_started/installation/singleNode/hpe_installer.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Add a scenario-based recovery section to the canonical backup/restore guide and link installation or migration prerequisites. Separate host failure, surviving Manager disk, and backup-only recovery.

## Changes

1. Update `getting_started/guides/backup_restore.rst` with the approved VME Manager host-failure recovery runbook.
2. Update `getting_started/installation/singleNode/hpe_installer.rst` with prerequisites or a recovery cross-reference where applicable.
3. Update `getting_started/maintenance/db_migration.rst` only if appliance identity/database restoration is part of the approved path.

## Acceptance Criteria

- WHEN the VME Manager host fails THE DOCUMENTATION SHALL help the operator select a supported recovery path based on surviving artifacts.
- THE DOCUMENTATION SHALL include prerequisites, ordered steps, validation, rollback or stop conditions, and escalation criteria.
- IF no viable backup or disk survives THEN THE DOCUMENTATION SHALL clearly state the supported rebuild/escalation path.

## Boundaries

No hypervisor HA design, undocumented database manipulation, or promise of recovery without required backups.

## Risks

- **Blocker:** Jira provides no architecture, backup assumptions, or approved commands.
- Recovery may affect appliance identity, credentials, integrations, and managed-cluster connectivity.

## Validation

Run each documented scenario in a lab, verify cluster management and integrations after recovery, peer-review with support, and run `make build`.
