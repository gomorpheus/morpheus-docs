---
title: "HVM Multi-Disk QCOW2 Image Guidance"
slug: docs-hvm-qcow2-image-guidance
type: feature
status: in-review
size: trivial
horizon: now
priority: high
tags: [hvm, kvm, qcow2, virtual-images]
parent: docs-hvm-multidisk-qcow2
depends-on: [docs-qcow2-multidisk-upload]
relates-to: [hvm-13-cluster-docs]
created: 2026-07-30
claimed_by: mcp-agent
claimed_at: 2026-07-30T17:07:39-04:00
---

# HVM Multi-Disk QCOW2 Image Guidance

## Context

The MVM Cloud guide only states that QCOW2 and RAW are compatible, and the legacy HVM cluster image section focuses on ISO-based Windows preparation. Neither tells HVM/KVM users where to find the multi-disk upload manifest requirements.

## Goal

Make multi-disk QCOW2 support discoverable from both HVM cluster and MVM Cloud documentation without duplicating the canonical manifest procedure.

## Approach

Add concise source-backed notes and links to the canonical Virtual Images subsection. Identify when metadata is required and what operators should check when provisioning sees only one disk or the wrong root disk.

## Changes

1. Add a multi-disk QCOW2 note near image preparation in `infrastructure/clusters/mvm.rst`, linking to the canonical Library procedure.
2. Expand image prerequisites and troubleshooting in `integration_guides/Clouds/mvm/mvm.rst` to state that each disk needs a QCOW2 file and multi-disk sets need `metadata.json`.
3. Use |LibVir| for navigation and avoid reproducing the entire JSON example.
4. Explain that missing or mismatched metadata commonly surfaces as one disk, missing data disks, wrong sizes, or incorrect boot order.

## Acceptance Criteria

- THE HVM CLUSTER DOCUMENTATION SHALL state that multi-disk QCOW2 uploads require `metadata.json` and link to the canonical procedure.
- THE MVM CLOUD DOCUMENTATION SHALL state the same requirement in image prerequisites and troubleshooting.
- THE DOCUMENTATION SHALL explain observable symptoms of a bad or missing manifest.
- THE DOCUMENTATION SHALL avoid duplicating the full schema.

## Boundaries

- Do not rewrite HVM Windows ISO preparation.
- Do not create a second canonical manifest example.

## Risks

- `infrastructure/clusters/mvm.rst` is legacy-oriented; wording must remain applicable to supported HVM/KVM provisioning.

## Validation

- Build Sphinx and verify cross-references resolve.
- Confirm terminology against HVM/KVM provisioning code and current UI labels.

## Delivery

- Added a multi-disk QCOW2 requirement and canonical cross-reference beside HVM cluster image preparation in `infrastructure/clusters/mvm.rst`.
- Added MVM Cloud image prerequisites and troubleshooting for missing metadata, filename mismatches, byte capacities, positions, and boot selection.
- Kept the full schema only in the Virtual Images reference.
- Verified all four acceptance criteria and rendered cross-references with Sphinx.

## Kickoff

Links HVM cluster and MVM Cloud users to the canonical multi-disk QCOW2 manifest procedure.

**Status:** in-review - HVM cluster and MVM Cloud guidance is implemented and validated.

**Pick up at:** review HVM/KVM terminology and approve for completion.

→ `.hero/planning/features/docs-hvm-qcow2-image-guidance/spec.md`

**Files:** `infrastructure/clusters/mvm.rst`, `integration_guides/Clouds/mvm/mvm.rst`, `library/virtual_images/virtual_images.rst`
