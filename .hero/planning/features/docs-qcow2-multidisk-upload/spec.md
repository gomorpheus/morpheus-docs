---
title: "Multi-Disk QCOW2 Virtual Image Upload"
slug: docs-qcow2-multidisk-upload
type: feature
status: in-review
size: small
horizon: now
priority: high
tags: [virtual-images, qcow2, multidisk, metadata]
parent: docs-hvm-multidisk-qcow2
relates-to: [docs-virtual-image-options-reference]
created: 2026-07-30
claimed_by: mcp-agent
claimed_at: 2026-07-30T17:07:39-04:00
---

# Multi-Disk QCOW2 Virtual Image Upload

## Context

The Virtual Images reference lists QCOW2 uploads but does not document how multiple disk files become one image. `VirtualImageService` requires `metadata.json` to map those files; otherwise it falls back to a single-disk image.

## Goal

Add an exact, reproducible UI procedure and manifest reference for uploading a multi-disk QCOW2 Virtual Image.

## Approach

Add a subsection under QCOW2 upload in `library/virtual_images/virtual_images.rst`. Use exact filenames and byte capacities, keep storage-controller fields optional, and explain source-derived defaults rather than exposing internal implementation names unnecessarily.

## Changes

1. Document the required upload set: two or more QCOW2 files plus a root-level file named exactly `metadata.json`.
2. Provide a valid two-disk JSON example, such as:

   ```json
   {
     "disks": [
       {
         "file": "root.qcow2",
         "capacity": 53687091200,
         "guestDeviceName": "vda",
         "position": 0,
         "name": "root",
         "boot": true
       },
       {
         "file": "data.qcow2",
         "capacity": 107374182400,
         "guestDeviceName": "vdb",
         "position": 1,
         "name": "data"
       }
     ]
   }
   ```
3. Define `file`, `capacity`, `guestDeviceName`, `position`, `name`, optional `boot`, `unitNumber`, and optional `storageController`, including byte/GiB conversion examples.
4. Document local UI upload steps using |LibVir|: choose QCOW2, configure image settings, upload every QCOW2 file first, upload `metadata.json` last, wait for completion, and save.
5. Explain matching and ordering: exact unique filenames, sort precedence, explicit boot flag, and first-disk fallback.
6. Add validation and troubleshooting for missing disks, only one parsed disk, incorrect capacity, wrong device order, malformed JSON, and upload sequencing.

## Acceptance Criteria

- THE DOCUMENTATION SHALL include a syntactically valid two-disk `metadata.json` example.
- THE DOCUMENTATION SHALL define required fields and units sufficiently for users to adapt the example.
- WHEN uploading locally THE DOCUMENTATION SHALL instruct users to upload QCOW2 files before the manifest.
- IF metadata is absent THEN THE DOCUMENTATION SHALL explain that the image is treated as a single-disk image.
- THE DOCUMENTATION SHALL explain boot selection and disk sort order.
- THE DOCUMENTATION SHALL include verification and corrective steps for every common manifest failure.

## Boundaries

- No URL ZIP workflow until confirmed end to end.
- No full Virtual Image field rewrite; coordinate adjacent changes with `docs-virtual-image-options-reference`.

## Risks

- The in-flight options-reference feature edits the same file.
- Documenting optional controller objects without a validated example could overcomplicate the basic workflow.

## Validation

- Compare the example and field definitions with `getImageDiskMap()` and KVM-generated metadata.
- Parse the JSON example with a standard JSON parser.
- Run Sphinx and inspect rendered code and tables.

## Delivery

- Added the canonical multi-disk QCOW2 section to `library/virtual_images/virtual_images.rst` with a valid two-disk `metadata.json` example.
- Defined file mapping, byte capacities, guest devices, positions, names, boot behavior, optional controller metadata, and disk sorting.
- Documented the local multi-file upload workflow, including uploading all QCOW2 files before `metadata.json` and validating parsed disks before provisioning.
- Added corrective steps for missing disks, single-disk fallback, malformed JSON, filename mismatches, incorrect byte sizes, device order, and boot selection.
- Parsed the JSON example successfully and verified all six acceptance criteria against `VirtualImageService.getImageDiskMap()` and rendered HTML.

## Kickoff

Adds the missing `metadata.json` schema and upload order for multi-disk QCOW2 Virtual Images.

**Status:** in-review - canonical schema, workflow, and troubleshooting are implemented and validated.

**Pick up at:** review schema terminology with Virtual Image engineering and approve for completion.

→ `.hero/planning/features/docs-qcow2-multidisk-upload/spec.md`

**Files:** `library/virtual_images/virtual_images.rst`, `../morpheus-ui/morpheus-core/grails-app/services/com/morpheus/VirtualImageService.groovy`, `../morpheus-ui/clouds/mvm/grails-app/services/com/morpheus/provision/KvmProvisionService.groovy`
