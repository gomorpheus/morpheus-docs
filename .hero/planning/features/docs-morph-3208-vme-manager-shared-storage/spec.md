---
title: "How to migrate VME manager from local storage to shared storage"
slug: docs-morph-3208-vme-manager-shared-storage
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, vme, migration, shared-storage]
tracker_id: MORPH-3208
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:17:20Z
---
# How to migrate VME manager from local storage to shared storage

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-3208

Jira description (verbatim):

> Document how to migrate VME manager from local storage to shared storage. Should be included with the installation guide and also mirrored as a user process guide in that section.

Related storage and installation material exists in `getting_started/installation/distributed/HA_Shared_Storage.rst`, `getting_started/guides/backup_restore.rst`, and `getting_started/installation/3_node_ha/3_node_ha_app_node.rst`.

## Goal

Provide one authoritative, validated procedure for moving VME Manager application data from local to shared storage, surfaced from both installation and user-process navigation without duplicating instructions.

## Kickoff

Document the supported move of VME Manager data from local storage to shared storage with rollback-aware steps.

**Status:** planning — related shared-storage pages exist; VME-specific scope and service sequence require validation.

**Pick up at:** confirm supported source/target layouts, data paths, downtime, ownership, and rollback with VME engineering.

→ `.hero/planning/features/docs-morph-3208-vme-manager-shared-storage/spec.md`

**Files:** `getting_started/installation/distributed/HA_Shared_Storage.rst`, `getting_started/guides/backup_restore.rst`, `getting_started/installation/3_node_ha/3_node_ha_app_node.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Extend the canonical shared-storage page with preflight, backup, service quiescence, copy/mount, permissions, validation, and rollback. Add references rather than mirrored prose.

## Changes

1. Update `getting_started/installation/distributed/HA_Shared_Storage.rst` with the validated local-to-shared migration procedure.
2. Update `getting_started/installation/3_node_ha/3_node_ha_app_node.rst` with an installation-path cross-reference.
3. Update `getting_started/guides/backup_restore.rst` with a user-process cross-reference and backup prerequisite.

## Acceptance Criteria

- WHEN an administrator migrates VME Manager storage THE DOCUMENTATION SHALL provide preflight, backup, service, copy, mount, permission, validation, and rollback steps.
- THE DOCUMENTATION SHALL identify expected downtime and supported shared-storage types.
- THE DOCUMENTATION SHALL maintain a single canonical procedure and use cross-references elsewhere.

## Boundaries

No database migration, VM relocation, storage-array setup, or unsupported zero-downtime promise.

## Risks

- **Blocker:** VME-specific data paths, supported storage, and service sequencing require engineering confirmation.
- Incorrect ownership or incomplete copy can make the Manager unavailable.

## Validation

Execute the procedure in a representative VME environment, test rollback, verify permissions and UI assets, run `make build`, and review both navigation paths.
