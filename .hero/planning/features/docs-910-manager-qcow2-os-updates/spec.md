---
title: "9.1.0 Docs: Morpheus Manager QCOW2 OS Updates"
slug: docs-910-manager-qcow2-os-updates
type: feature
status: in-review
size: small
horizon: now
priority: 2
tags: [9.1.0, docs, manager, qcow2, ubuntu, apt, air-gap]
parent: docs-910-system-updates
relates-to: [docs-unified-deployment]
created: 2026-08-11
---

# 9.1.0 Docs: Morpheus Manager QCOW2 OS Updates

## Context

The HPE Morpheus Manager Installer deploys an Ubuntu-based QCOW2 appliance without requiring internet access during a local-image deployment. Existing documentation did not explain how to maintain that base OS afterward or how an air-gapped site can supply the required Canonical packages. General offline installation guidance also stated that APT access remains required without describing how to provide it.

## Goal

Document a supportable Manager base-OS maintenance workflow that follows Canonical APT and Landscape practices while requiring HPE to define the validated update content for each Morpheus release.

## Approach

Keep the Morpheus application package upgrade workflow separate from Ubuntu package maintenance. Treat HPE release guidance as the authority for update scope and Canonical documentation as the authority for APT, repository signing, mirroring, snapshots, and air-gap transfer mechanics.

## Changes

1. Add `getting_started/maintenance/manager_os_updates.rst` as the canonical Manager base-OS maintenance guide.
2. Cover connected, restricted-network, and fully disconnected update models.
3. Add preparation, dry-run, maintenance-window, reboot, validation, and recovery steps without inventing an HPE package allowlist.
4. Link the guide from maintenance navigation, application upgrade documentation, offline installation guidance, requirements, and the Manager Installer pages.
5. Clarify that local QCOW2 deployment can be offline while ongoing OS patching still requires an HPE-approved APT source.

## Acceptance Criteria

- THE DOCUMENTATION SHALL distinguish Manager application upgrades from Ubuntu base-OS updates.
- WHEN an operator prepares a Manager OS update THE DOCUMENTATION SHALL require the applicable HPE update guidance and a recoverable backup or snapshot.
- WHILE a Manager cannot reach Canonical repositories THE DOCUMENTATION SHALL provide restricted-network and fully disconnected repository patterns aligned with Canonical Landscape guidance.
- IF HPE has not published validated update inputs THEN THE DOCUMENTATION SHALL direct the operator not to apply an unrestricted Ubuntu upgrade.
- THE DOCUMENTATION SHALL describe post-update health checks and evidence to collect before recovery or support escalation.

## Boundaries

- Do not prescribe an Ubuntu release upgrade such as 22.04 to 24.04.
- Do not claim every package currently available from Canonical is validated by HPE.
- Do not reproduce the complete Landscape installation or repository-management manuals.
- Do not conflate HVM host OS updates with Manager appliance OS updates.

## Risks

- The exact HPE-validated pockets, components, snapshot identifiers, and package restrictions are release inputs and must not be guessed.
- Fully disconnected Landscape refreshes may require transfer of the complete mirrored repository and substantial removable-media capacity.

## Validation

- Build Sphinx and verify all new internal and external links.
- Compare APT commands and Ubuntu 24.04 source-file locations with Canonical documentation.
- Confirm the air-gap models and full-repository transfer limitation match Canonical Landscape guidance.

## Delivery

- Added the canonical Manager base-OS maintenance guide and both Canonical air-gap models.
- Added navigation and cross-references from installation, requirements, offline, and upgrade content.
- Preserved the HPE validation gate instead of recommending arbitrary Canonical updates.

## Verification

- PASS: The guide distinguishes application, base-OS, and Ubuntu release upgrades in its opening section.
- PASS: Preparation requires HPE update guidance and a recoverable appliance and database backup; a VM snapshot is explicitly supplementary.
- PASS: Separate restricted-network and fully disconnected Landscape models are documented, including signing and full-repository transfer constraints.
- PASS: The page prohibits unrestricted APT updates when HPE inputs are unavailable.
- PASS: Post-update service, UI, HVM connectivity, logging, recovery, and escalation checks are documented.
- PASS: A normal Sphinx HTML build completed and rendered `getting_started/maintenance/manager_os_updates.html`. The repository has 1,831 pre-existing warnings; none reference the new page. `make build` remains unusable because the Makefile maps that target to the nonexistent Sphinx builder named `build`.

## Kickoff

Adds connected and air-gapped Ubuntu base-OS update guidance for the Morpheus Manager QCOW2 appliance.

**Status:** in-review - documentation is implemented and built; HPE update inputs need technical approval.

**Pick up at:** review the HPE update manifest requirements and confirm the documented support boundary for 9.1.0.

→ `.hero/planning/features/docs-910-manager-qcow2-os-updates/spec.md`

**Files:** `getting_started/maintenance/manager_os_updates.rst`, `getting_started/additional/offline.rst`, `getting_started/requirements/requirements.rst`
**Skip:** do not document unrestricted Canonical package updates as HPE-supported.
