---
title: "SCVMM Sysprep and Unattend.xml Guide"
type: feature
status: planning
---

## Description

SCVMM and Hyper-V customers need specific guidance on creating sysprep'd Windows images and how unattend.xml injection works in their environment. The existing guide at provisioning/windows_cloud_guest_customization.rst is VMware/HVM focused. This spec covers adding SCVMM-specific sysprep workflow documentation including:

- How to prepare a Windows image for SCVMM (sysprep /generalize /shutdown)
- How Morpheus injects unattend.xml for SCVMM VMs (the code shows it uses answer files for non-clone provisioning)
- Limitations: clone operations in SCVMM don't support passing AnswerFile (per source code comment)
- Integration with Morpheus agent installation via unattend.xml
- Domain join via guest customization on SCVMM

## Changes

- `provisioning/windows_cloud_guest_customization.rst` — Add SCVMM-specific sysprep workflow section
- `integration_guides/Clouds/scvmm/scvmm.rst` — Add cross-reference to sysprep guide

## Acceptance Criteria

- SCVMM-specific sysprep workflow is documented in the Windows cloud guest customization guide
- Unattend.xml injection behavior for SCVMM is explained (template-based provisioning vs clones)
- SCVMM page cross-references the sysprep guide
- Clone limitation regarding AnswerFile is noted
