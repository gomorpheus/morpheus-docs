---
title: "[VME version:8.1.0]:Compute menu is missing under Infrastructure in HPE Morpheus VME Document"
slug: docs-morph-9607-infrastructure-compute-menu
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, vme, infrastructure, compute]
tracker_id: MORPH-9607
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:30:03Z
---

# [VME version:8.1.0]:Compute menu is missing under Infrastructure in HPE Morpheus VME Document

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-9607

Exact Jira description (delivery source requirement):

> Setup: PCBE Greenfield VME  
> Agent Version: 3.1.3  
> VME Manager: 8.1.0  
> Storage plugin: 1.9.2
>
> As per the document “[HPE Morpheus VM Essentials Software | HPE Morpheus VM Essentials Software Documentation v8.1.0](https://support.hpe.com/hpesc/public/docDisplay?docId=sd00007520en_us&page=GUID-498C49E5-5D26-44E1-A2CC-9AAC0813BA93.html)[”](https://support.hpe.com/hpesc/public/docDisplay?docId=sd00007520en_us&page=GUID-FB7D15CC-A606-42DC-9DBF-27778D20282D.html%E2%80%9D)
>
> “Compute menu is missing under Infrastructure in HPE Morpheus VME Document”
>
> The Documentation does not include details about the Compute section
>
> VME Environment: [https://10.157.232.173](https://10.157.232.173/)
>
> **Steps to Reproduce**:
>
> 1.Connect to VME and Go to 'Infrastructure'
>
> 2.Verify the Compute section is available under Infrastructure
>
> **Expected Result**:
>
> "Compute" section should be available under Infrastructure in HPE Morpheus VME Document
>
> **Actual Output**:
>
> “Compute" section are missing under Infrastructure in HPE Morpheus VME Documentation

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-9607 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-9607-infrastructure-compute-menu/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `infrastructure/infrastructure.rst`
- `infrastructure/servers/server_migration.rst`
- `infrastructure/servers/server_devices.rst`
- `administration/roles/role_permissions.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Add an Infrastructure > Compute overview and route readers to its VM/server operations, with VME-specific navigation and permission prerequisites.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. Update `infrastructure/infrastructure.rst` to carry the primary procedure and verified guidance.
2. Update `infrastructure/servers/server_migration.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.
3. Update `infrastructure/servers/server_devices.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.
4. Update `administration/roles/role_permissions.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-9607
- IF a reported behavior cannot be reproduced or confirmed THEN THE DOCUMENTATION SHALL omit it or label the supported limitation using approved product wording
- THE DOCUMENTATION SHALL use current repository navigation, terminology, formatting, and cross-references across every changed file
- THE DOCUMENTATION SHALL preserve the Jira-requested correction while avoiding unsupported timing, compatibility, security, or operational guarantees
- WHEN the documentation build and link checks run THE SYSTEM SHALL complete without new warnings or broken internal references caused by these changes

## Boundaries

- Do not change product code, API behavior, UI behavior, or release support policy.
- Do not broaden this issue into a general rewrite of adjacent documentation.
- Do not add inaccessible Jira media to the repository or reconstruct screenshots from descriptions.
- Do not publish commands, defaults, compatibility claims, or destructive operations until an authoritative owner verifies them.

## Risks

- Verify the 8.1.0 menu structure, child tabs, terminology, and role-dependent visibility before defining scope.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.

## Delivery Validation

- `infrastructure/infrastructure.rst` already includes `compute/compute.rst` in the Infrastructure navigation.
- `infrastructure/compute/compute.rst` already documents `Infrastructure > Compute`, its Hosts, Virtual Machines, Containers, Resources, and Bare Metal tabs, and the expected list-management result.
- `infrastructure/servers/server_migration.rst` and `server_devices.rst` already use the current Compute permission and navigation terminology; `administration/roles/role_permissions.rst` already documents the `Infrastructure: Compute` permission and accessible machine lists.
- `make html` succeeded and rendered the Infrastructure and role pages. No documentation edit was needed to preserve the Jira-requested correction.
