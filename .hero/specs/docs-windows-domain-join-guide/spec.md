---
type: feature
status: delivering
horizon: now
tags: [documentation, windows, provisioning, field-feedback]
parent: docs-field-feedback-improvements
---

# Windows VM Domain Join Guide

## Objective

Create a guide-style document covering the full workflow for deploying Windows VMs with Active Directory domain join — from image prep through successful domain membership.

## Acceptance Criteria

1. Documents the end-to-end flow: image preparation → VM provisioning → domain join
2. Covers sysprep/unattend configuration for domain join
3. Documents DNS prerequisites (VM must resolve the domain controller)
4. Covers credential handling (domain join service account, where creds are configured in Morpheus)
5. Addresses cloud-init vs sysprep approaches and when to use each
6. Includes troubleshooting for common domain join failures
7. Written as a practical guide with step-by-step instructions

## Changes

- `provisioning/guides/windows_domain_join.rst` (new) — Guide document
- `provisioning/guides/guides.rst` — Add to toctree
