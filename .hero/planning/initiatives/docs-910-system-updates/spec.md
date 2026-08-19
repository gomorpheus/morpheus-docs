---
title: "9.1.0 Docs: Morpheus Core System Update Capabilities"
slug: docs-910-system-updates
type: initiative
status: delivering
size: medium
horizon: now
tags: [9.1.0, docs, manager, updates]
priority: 2
jira: MORPH-4061
child: [docs-910-manager-qcow2-os-updates]
---

# 9.1.0 Docs: Morpheus Core System Update Capabilities

## Vision

Give Morpheus 9.1.0 operators a clear, supportable path for product updates and for operating-system maintenance of the Ubuntu-based Morpheus Manager QCOW2 appliance, including environments that cannot reach Canonical repositories.

## Scope

- System update procedures
- Update channels and scheduling
- Pre-update validation
- Rollback and recovery options
- Connected, restricted-network, and fully disconnected update models
- A clear boundary between Morpheus application upgrades and Manager base-OS updates

## Specs

- [x] `docs-910-manager-qcow2-os-updates` - Document HPE-validated APT maintenance and Canonical-aligned air-gapped repository workflows for the Manager QCOW2 appliance.

## Dependencies

- HPE release guidance must identify the validated Ubuntu series, pockets, components, architectures, and any snapshot identifier or package restrictions for each Manager release.
- Canonical Landscape guidance supplies repository mirroring and transfer mechanics; it does not determine which Ubuntu updates HPE supports on the Manager appliance.

## Acceptance Criteria

- THE DOCUMENTATION SHALL distinguish Morpheus application upgrades from Ubuntu base-OS package maintenance.
- THE DOCUMENTATION SHALL require HPE release guidance before operators apply Ubuntu updates to a Manager appliance.
- THE DOCUMENTATION SHALL cover connected, restricted-network, and fully disconnected repository models.
- THE DOCUMENTATION SHALL include pre-update, update, reboot, validation, and recovery considerations.
- THE DOCUMENTATION SHALL reconcile installation-time offline claims with the repository access required for ongoing maintenance.

## Validation

- Build the Sphinx documentation and confirm the new page and cross-references resolve.
- Review commands and repository terminology against current Canonical Ubuntu Server and Landscape guidance.
- Confirm the guide does not claim that arbitrary Canonical updates are HPE-validated.

## Progress

- The Manager base-OS update and air-gap child documentation is implemented and awaiting technical review of the HPE-approved update inputs.

## Kickoff

Documents supported Ubuntu base-OS maintenance for the Morpheus Manager QCOW2 appliance, including both Canonical air-gap models.

**Status:** delivering - the child guide and cross-references are implemented.

**Pick up at:** obtain technical approval for the HPE update manifest fields, then review the connected and Landscape workflows before completion.

→ `.hero/planning/initiatives/docs-910-system-updates/spec.md`

**Files:** `getting_started/maintenance/manager_os_updates.rst`, `getting_started/additional/offline.rst`, `getting_started/requirements/requirements.rst`
**Skip:** do not replace the HPE validation boundary with an unrestricted `apt upgrade` recommendation.

## Sources

- Jira Epic: MORPH-4061
- Canonical Ubuntu package management: https://documentation.ubuntu.com/server/how-to/software/package-management/
- Canonical Ubuntu snapshot service: https://documentation.ubuntu.com/server/how-to/software/snapshot-service/
- Canonical Landscape air-gapped repository guidance: https://documentation.ubuntu.com/landscape/how-to-guides/repository-mirrors/manage-repositories-in-an-air-gapped-or-offline-environment/
