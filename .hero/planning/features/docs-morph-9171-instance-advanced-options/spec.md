---
title: "[VME version: 8.1.0]:Missing Advanced Options under Provisioning> Instance > Creating Instances in HPE Morpheus VME Document"
slug: docs-morph-9171-instance-advanced-options
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, vme, provisioning, instances]
tracker_id: MORPH-9171
jira_status: New
parent: docs-morph-3266-enhancements
relates-to:
  - docs-morph-9172-instance-create-snapshot-action
created: 2026-08-03
completed_at: 2026-08-03T18:00:00Z
---

# [VME version: 8.1.0]:Missing Advanced Options under Provisioning> Instance > Creating Instances in HPE Morpheus VME Document

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-9171

Exact Jira description (delivery source requirement):

> Setup: PCBE Greenfield VME  
> Agent Version: 3.1.3  
> VME Manager: 8.1.0  
> Storage plugin: 1.9.2
>
> The Documentation for instance creation does not include details about the "Advanced Options" available during the creation workflow
>
> VME Environment: [https://10.157.232.173](https://10.157.232.173/)
>
> **Steps to Reproduce:**
>
> 1.Connect to VME and Go to Provisioning → Instances
>
> 2.Click on “+Add” button to create instance
>
> 3.Verify the "Advanced Options" are available in Creating Instance under the configurations section
>
> **Expected Result:**
>
> "Advanced Options" should be available in HPE Morpheus VME Document
>
> **Actual Output:**
>
> “Advanced Options” is missing in the HPE Morpheus VME Documentation

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-9171 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-9171-instance-advanced-options/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `provisioning/instances/creating_instances.rst`
- `infrastructure/clusters/hvm/vm_advanced_options.rst`
- `infrastructure/clusters/hvm/guest_os_notes.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Add the VME instance-creation Advanced Options at the Configure step, grouping fields by purpose and linking detailed HVM option guidance where applicable.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. `provisioning/instances/creating_instances.rst` — Added the Configure-step Advanced Options entry point and canonical HVM field-reference link.
2. `infrastructure/clusters/hvm/vm_advanced_options.rst` — Existing worktree content provides the source-backed field inventory and lifecycle matrix.
3. `infrastructure/clusters/hvm/guest_os_notes.rst` — Added the canonical Advanced Options cross-reference.

## Delivery Evidence

Current HVM option seeds prove the field inventory, defaults, dependencies, and create/reconfigure flags. This application-backed evidence satisfies the documentation request without requiring the unavailable VME 8.1.0 environment.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-9171
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

- Capture and validate the 8.1.0 field inventory, defaults, dependencies, and role/layout visibility before documenting them.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Review the field inventory against current HVM option seeds.
2. Review the rendered pages against the Jira request.
3. Run `make build`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
