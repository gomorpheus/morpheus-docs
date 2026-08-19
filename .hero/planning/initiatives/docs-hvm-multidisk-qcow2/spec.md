---
title: "HVM Multi-Disk QCOW2 Virtual Image Documentation"
slug: docs-hvm-multidisk-qcow2
type: initiative
status: in-review
size: small
horizon: now
priority: high
tags: [virtual-images, hvm, kvm, qcow2, multidisk, metadata]
child: [docs-qcow2-multidisk-upload, docs-hvm-qcow2-image-guidance]
relates-to: [docs-virtual-image-options-reference, hvm-13-cluster-docs]
created: 2026-07-30
---

# HVM Multi-Disk QCOW2 Virtual Image Documentation

## Vision

Enable operators to upload a multi-disk QCOW2 image set for HVM/KVM and reliably preserve disk-to-file mapping, capacity, device order, and boot-disk selection using a correctly formatted `metadata.json` manifest.

## Goal

Document the exact files, JSON schema, upload order, Virtual Image settings, and validation steps required to create a usable multi-disk QCOW2 Virtual Image, then surface that procedure from the HVM/KVM documentation where operators look for cluster image requirements.

## Approach

Make `library/virtual_images/virtual_images.rst` the canonical upload procedure because `VirtualImageService` parses the files independent of a specific target Cloud. Add concise HVM/KVM cross-references and target-specific cautions in the HVM cluster and MVM Cloud guides. Coordinate edits to the Library page with the in-flight `docs-virtual-image-options-reference` feature.

## Context

Current documentation lists QCOW2 as a supported upload type but does not explain multi-disk input. HVM documentation only states that QCOW2 and RAW are compatible or walks through ISO-based Windows image preparation.

Source behavior establishes the following workflow:

- A Virtual Image can store multiple uploaded files in its image directory.
- `VirtualImageService.getImageDiskMap()` looks for a file whose name ends with `metadata.json`.
- Without metadata, the service finds one image file and creates a single-disk map, even when multiple QCOW2 files exist.
- Metadata must contain a top-level `disks` array. Disk entries are sorted by `busNumber`, `unitNumber`, then `position`.
- Each disk's `file` value is matched to an uploaded image filename; it may be the full filename or a basename that resolves to the selected image format.
- `capacity` is expressed in bytes and becomes the disk's maximum storage value.
- `guestDeviceName`, `name`, `position`, optional `boot`, `unitNumber`, and optional `storageController` describe the guest disk.
- If no disk has `boot: true`, the first sorted disk becomes the boot disk.
- Uploading `metadata.json` triggers disk-map parsing immediately. Upload all referenced QCOW2 files first and the manifest last so every file can be resolved when volumes are created.
- The create UI supports multiple local file uploads. The normal create-by-URL flow assigns the selected image type as the destination filename, so it should not be documented as a reliable ZIP-bundle workflow without a product change or confirmed alternate UI path.

Primary sources:

- `../morpheus-ui/morpheus-core/grails-app/services/com/morpheus/VirtualImageService.groovy`
- `../morpheus-ui/utils/image-converters/src/main/groovy/com/morpheus/virtualimages/converters/MetadataConverter.groovy`
- `../morpheus-ui/clouds/mvm/src/main/groovy/com/morpheus/compute/KvmComputeUtility.groovy`
- `../morpheus-ui/clouds/mvm/grails-app/services/com/morpheus/provision/KvmProvisionService.groovy`
- `../morpheus-ui/morpheus-ui/grails-app/controllers/com/morpheus/provisioning/VirtualImagesController.groovy`

## Specs

- [x] `docs-qcow2-multidisk-upload` - Implemented and awaiting Virtual Image engineering review.
- [x] `docs-hvm-qcow2-image-guidance` - Implemented and awaiting HVM review.

## Dependencies

- Coordinate `library/virtual_images/virtual_images.rst` changes with `docs-virtual-image-options-reference`, which is actively delivering edits to the same page.
- Confirm whether the product team wants full filenames such as `root.qcow2` or extensionless basenames as the recommended `file` convention; both resolve in current source, but one canonical form should be shown.
- Confirm whether `boot: true` is the supported customer-facing field or whether ordering alone should identify the root disk; current source recognizes `boot` and otherwise selects the first sorted disk.
- Confirm UI terminology and where parsed image volumes are visible in the current 9.1 interface.

## Acceptance Criteria

- THE DOCUMENTATION SHALL state that multi-disk HVM/KVM QCOW2 images require all disk files and a file named `metadata.json`.
- THE DOCUMENTATION SHALL provide a valid manifest example with byte capacities, file mapping, guest device names, positions, names, and boot-disk behavior.
- WHEN users upload files through the UI THE DOCUMENTATION SHALL instruct them to upload all QCOW2 files before `metadata.json`.
- THE DOCUMENTATION SHALL explain how files are matched, how disks are ordered, and what happens when metadata is absent.
- THE DOCUMENTATION SHALL provide post-upload validation that confirms every disk, size, device, and boot disk before provisioning.
- THE HVM cluster and MVM Cloud documentation SHALL link to the canonical procedure and identify multi-disk QCOW2 as supported.
- THE DOCUMENTATION SHALL include troubleshooting for missing files, filename mismatches, byte-size mistakes, malformed JSON, and incorrect boot ordering.

## Boundaries

- Do not change Virtual Image upload or KVM provisioning code.
- Do not document URL ZIP upload as supported through the standard create UI unless end-to-end behavior is confirmed or changed.
- Do not require optional storage-controller metadata for simple VirtIO disk sets.
- Do not duplicate the complete Virtual Image options matrix tracked by `docs-virtual-image-options-reference`.

## Risks

- Uploading the manifest before its disk files can create incomplete cached volumes.
- `capacity` values entered as GiB rather than bytes produce incorrect disk sizing.
- Loose substring filename matching can hide ambiguous naming; examples should use unique, exact filenames.
- The legacy HVM cluster page and newer HVM 1.3 section overlap, so cross-references must avoid creating competing canonical procedures.

## Validation

- Trace every documented manifest field through `VirtualImageService.getImageDiskMap()` and generated metadata in `KvmProvisionService`.
- Validate local multi-file upload behavior through the Virtual Images controller and file explorer.
- Run the Sphinx HTML build and inspect the JSON block, ordered steps, and cross-references.
- Obtain Virtual Image and HVM engineering review before publication.

## Progress

Both documentation children are implemented. The JSON example parses, cross-references resolve, all acceptance criteria pass, and Sphinx builds successfully with existing repository warnings. Virtual Image and HVM engineering review remains before publication.

## Kickoff

Documents the `metadata.json` manifest needed to upload multi-disk QCOW2 images for HVM/KVM.

**Status:** in-review - canonical upload and HVM/KVM discovery guidance is implemented and validated.

**Pick up at:** complete Virtual Image and HVM engineering review, focusing on field terminology and metadata-last recovery guidance.

→ `.hero/planning/initiatives/docs-hvm-multidisk-qcow2/spec.md`

**Files:** `library/virtual_images/virtual_images.rst`, `integration_guides/Clouds/mvm/mvm.rst`, `infrastructure/clusters/mvm.rst`, `../morpheus-ui/morpheus-core/grails-app/services/com/morpheus/VirtualImageService.groovy`
