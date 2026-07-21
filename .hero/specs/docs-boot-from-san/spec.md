---
type: feature
status: planning
horizon: someday
tags: [documentation, storage, hvm, field-feedback]
parent: docs-field-feedback-improvements
---

# Boot From SAN

## Objective

Document how to configure and use Boot From SAN with HVM hosts.

## Acceptance Criteria

1. Covers BIOS/UEFI boot configuration for SAN boot
2. Documents FC HBA setup and boot LUN selection
3. Explains LUN masking requirements for boot LUNs
4. Documents the Morpheus provisioning workflow for SAN-booted hosts
5. Includes supported HBA models and firmware requirements

## Changes

- `infrastructure/clusters/hvm/boot_from_san.rst` (new) — Boot From SAN guide
- `infrastructure/clusters/hvm/hvm.rst` — Add to toctree
