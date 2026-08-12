---
title: "Need documentation for VME/HVM on how to deploy VMs with Network boot and PXE boot using ISO images"
slug: docs-morph-3202-hvm-pxe-vm-boot
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, hvm, pxe, network-boot, virtual-machines]
tracker_id: MORPH-3202
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:49:50Z
---
# Need documentation for VME/HVM on how to deploy VMs with Network boot and PXE boot using ISO images

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-3202

Jira description (verbatim):

> Need documentation for VME/HVM on how to deploy VMs with Network boot and PXE boot using ISO images

Existing PXE and ISO concepts are covered in `infrastructure/pxeboot/pxeboot.rst`, `library/virtual_images/virtual_images.rst`, and `infrastructure/clusters/hvm/vm_advanced_options.rst`; the exact supported HVM VM workflow remains to be verified.

## Goal

Provide a verified end-to-end HVM VM deployment procedure for ISO and PXE/network boot, including prerequisites, boot ordering, network requirements, and post-install transition.

## Kickoff

Add a verified HVM VM workflow for ISO installation and PXE/network boot without conflating it with bare-metal PXE.

**Status:** planning — related PXE and image references exist; supported UI sequence needs confirmation.

**Pick up at:** validate the HVM provisioning fields, boot order, and network path on a supported cluster.

→ `.hero/planning/features/docs-morph-3202-hvm-pxe-vm-boot/spec.md`

**Files:** `infrastructure/pxeboot/pxeboot.rst`, `library/virtual_images/virtual_images.rst`, `infrastructure/clusters/hvm/vm_advanced_options.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Add HVM-specific VM instructions alongside existing HVM advanced options and cross-link canonical PXE infrastructure and ISO image preparation pages.

## Changes

1. Update `infrastructure/clusters/hvm/vm_advanced_options.rst` with the verified ISO/PXE boot configuration and boot-order lifecycle.
2. Update `infrastructure/pxeboot/pxeboot.rst` with an HVM VM consumer path distinct from bare-metal boot.
3. Update `library/virtual_images/virtual_images.rst` with the applicable ISO configuration and cross-reference.

## Acceptance Criteria

- WHEN an administrator chooses ISO boot THE DOCUMENTATION SHALL identify image settings, VM boot order, installation, and media removal steps.
- WHEN an administrator chooses PXE/network boot THE DOCUMENTATION SHALL identify required PXE infrastructure, VM network reachability, and verified HVM options.
- THE DOCUMENTATION SHALL distinguish VM PXE boot from bare-metal PXE provisioning.
- IF a workflow is unavailable in a supported HVM version THEN THE DOCUMENTATION SHALL state that limitation rather than infer support.

## Boundaries

No PXE server implementation tutorial, operating-system installer walkthrough, or bare-metal workflow rewrite.

## Risks

- **Blocker:** Supported versions and exact UI/boot-order behavior require product validation.
- PXE environment topology and DHCP ownership vary; examples must not prescribe an unverified network architecture.

## Validation

Execute both boot paths in a test cluster, capture field names from the current UI, run `make build`, and verify links and rendered procedure ordering.
