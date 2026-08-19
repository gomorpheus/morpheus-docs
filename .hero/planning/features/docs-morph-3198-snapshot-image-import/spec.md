---
title: "snapshot import to image"
slug: docs-morph-3198-snapshot-image-import
type: feature
status: completed
horizon: now
size: small
tags: [documentation, hvm, snapshots, virtual-images]
tracker_id: MORPH-3198
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T18:00:00Z
---
# snapshot import to image

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-3198

Jira description (verbatim):

> Didnt see in the documentation that if you are creating an image from an ISO deployment, if the ISO has a snapshot(specifically for testing before making a template out of it and having to recreate each time), the import of the image only creates the metadata.json, it does not create the qcow2. You have to delete the snapshot in order to fully import to image.

Current related coverage exists in `library/virtual_images/virtual_images.rst`, `infrastructure/clusters/hvm/snapshots.rst`, and `backups/backups_sub.rst` but the Jira-reported HVM import constraint is not yet verified.

## Goal

Document that existing HVM snapshots are supported during Import as Image, explain the temporary export behavior, and show how to identify an incomplete metadata-only result without deleting source snapshots.

## Kickoff

Document the snapshot constraint affecting import of an ISO-installed HVM VM into a Virtual Image.

**Status:** planning — related image and snapshot pages were found; behavior still needs reproduction.

**Pick up at:** reproduce import with and without an active snapshot and record the generated QCOW2 and metadata artifacts.

→ `.hero/planning/features/docs-morph-3198-snapshot-image-import/spec.md`

**Files:** `library/virtual_images/virtual_images.rst`, `infrastructure/clusters/hvm/snapshots.rst`, `backups/backups_sub.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Place the operational warning in the Virtual Images import workflow and link to HVM snapshot lifecycle guidance rather than duplicating snapshot internals.

## Changes

1. `library/virtual_images/virtual_images.rst` — Added a non-destructive HVM image-import preflight, complete-artifact check, and escalation path.
2. `infrastructure/clusters/hvm/snapshots.rst` — Added image-import preflight context without claiming snapshot deletion is a universal remedy.

## Delivery Evidence

`KvmProvisionService.importContainer()` calls `snapshotVm(server, true, true)`, adds each exported disk path and ``metadata.json`` to the Agent upload request, and removes only the temporary export snapshot afterward. `DirDatastoreService.createSnapshot()` explicitly detects an existing qcow2 backing chain and calls `copyAndMergeVolume()` to create a temporary merged export disk. Existing snapshots are therefore supported and do not need to be deleted.

The current code waits for the upload result but marks the Virtual Image Active without checking whether the result is complete. This can expose an incomplete image after a failed or timed-out upload. The documentation now directs users to validate every manifest-referenced disk artifact rather than treating Active status or metadata alone as success.

## Acceptance Criteria

- WHEN a user imports an HVM VM with existing snapshots THE DOCUMENTATION SHALL explain that |morpheus| creates a temporary merged export and does not require deletion of existing snapshots.
- WHEN an import produces metadata without an available disk artifact THE DOCUMENTATION SHALL identify the image as incomplete and provide a source-preserving escalation path.
- THE DOCUMENTATION SHALL state that snapshot deletion is not a required Import as Image step or supported workaround for an incomplete export.

## Boundaries

No changes to import behavior, snapshot implementation, VMware OVF export, or multidisk upload guidance.

## Risks

- The host Agent implementation that packages ``sourceFiles`` is outside `morpheus-ui`, so the exact cause of the reported metadata-only archive is not established.
- The import service can mark a Virtual Image Active after a failed or timed-out upload; artifact verification remains necessary until product code validates upload completion and disk presence.

## Validation

Inspect the HVM snapshot/import implementation, run `make build`, and check the rendered cross-links. A future product reproduction can narrow the affected-version statement but is not required for the source-backed limitation.
