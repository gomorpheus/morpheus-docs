---
title: "Add to VME Migration Tool Technical paper to include how to migrate VMs with LVM volumes and source SCSI disk"
slug: docs-morph-3205-vme-lvm-scsi-migration
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, vme, migration, lvm, scsi]
tracker_id: MORPH-3205
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T18:00:00Z
---
# Add to VME Migration Tool Technical paper to include how to migrate VMs with LVM volumes and source SCSI disk

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-3205

Jira description (verbatim):

> Add to VME Migration Tool Technical paper to include how to migrate VMs with LVM volumes and source SCSI disk

Migration coverage exists in `infrastructure/servers/server_migration.rst`, `backups/backups.rst`, and `integration_guides/Clouds/vmware/vmware_templates.rst`, but the requested technical paper or an approved procedure was not provided.

## Goal

Document the implementation-backed migration concepts and requirements for source VMs using LVM volumes and SCSI disks, including controller mapping, limitations, and post-migration checks.

## Kickoff

Add the validated LVM-volume and source-SCSI workflow to VME migration documentation.

**Status:** planning — adjacent migration and image guidance exists; the technical paper and supported procedure are missing.

**Pick up at:** obtain the current VME Migration Tool paper and reproduce the supported LVM/SCSI path.

→ `.hero/planning/features/docs-morph-3205-vme-lvm-scsi-migration/spec.md`

**Files:** `infrastructure/servers/server_migration.rst`, `backups/backups.rst`, `integration_guides/Clouds/vmware/vmware_templates.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Integrate the procedure into the repository's migration page, using the external technical paper only as validated source material. Include disk discovery, conversion prerequisites, and verification without guessing commands.

## Changes

1. `infrastructure/servers/server_migration.rst` — Added source SCSI mapping, LVM prerequisites and limitations, and post-migration checks from current implementation.
2. `backups/backups.rst` — Scoped the deprecated LVM Migration type and linked current migration guidance.
3. Update `integration_guides/Clouds/vmware/vmware_templates.rst` only for confirmed source-disk preparation prerequisites.

## Delivery Evidence

`MigrationPlanService` proves source controller mapping and VirtIO-SCSI selection; deprecated `LvmMigrationService` proves the single-LV, SSH/sudo, snapshot-space, and destination-device requirements. The documentation deliberately describes supported concepts and requirements rather than inventing an operator sequence or generic LVM repair commands.

## Acceptance Criteria

- WHEN a source VM uses LVM on SCSI disks THE DOCUMENTATION SHALL explain implementation-backed controller mapping, prerequisites, and post-migration checks.
- THE DOCUMENTATION SHALL distinguish migration-plan disk conversion from the deprecated single-logical-volume LVM Migration backup type and its limitations.
- THE DOCUMENTATION SHALL not invent commands absent from an approved technical source or successful test.

## Boundaries

No migration-tool code changes, generic Linux LVM tutorial, or unsupported disk conversion workaround.

## Risks

- The referenced technical paper was unavailable, so no prescriptive sequence beyond implementation-backed requirements is published.
- Device naming and bootloader behavior can vary by guest OS and disk controller.

## Validation

Review the documented mappings and requirements against application code and run `make build`. A representative migration remains useful future compatibility validation, not a prerequisite for these source-backed concepts.
