---
title: "[VME version: 8.1.0]: 'Create Snapshot' Action not documented in 'HPE Morpheus VME' user guide"
slug: docs-morph-9172-instance-create-snapshot-action
type: feature
status: completed
horizon: now
size: small
tags: [documentation, vme, instances, snapshots]
tracker_id: MORPH-9172
jira_status: New
parent: docs-morph-3266-enhancements
relates-to:
  - docs-morph-9171-instance-advanced-options
created: 2026-08-03
completed_at: 2026-08-03T18:00:00Z
---

# [VME version: 8.1.0]: 'Create Snapshot' Action not documented in 'HPE Morpheus VME' user guide

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-9172

Exact Jira description (delivery source requirement):

> **Setup**: PCBE Greenfield VME  
> **Agent Version**: 3.1.3  
> **VME Manager**: 8.1.0  
> **Storage plugin**: 1.9.2
>
> **VME Environment:** [https://10.157.232.173](https://10.157.232.173/)
>
> **Steps to Reproduce:**
>
> 1.Connect to VME and Go to Provisioning → Instances → Select any instance
>
> 2.Click on “Actions” button
>
> 3.Verify the “Create Snapshot” Action item is available
>
> **Expected Result:**
>
> “Create Snapshot” Action item should be available under “Actions” in the HPE Morpheus VME Documentation
>
> **Actual Output:**
>
> “Create Snapshot” Action item is missing in the HPE Morpheus VME Documentation

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-9172 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-9172-instance-create-snapshot-action/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `provisioning/instances/managing_instances.rst`
- `provisioning/instances/instance_details.rst`
- `infrastructure/clusters/hvm/snapshots.rst`
- `administration/roles/role_permissions.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Document the Create Snapshot action from an instance, including prerequisites, permissions, supported storage behavior, and where results are viewed.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. `provisioning/instances/managing_instances.rst` — Documented action visibility, input, process, and result location.
2. `provisioning/instances/instance_details.rst` — Added the action and permission cross-reference.
3. `infrastructure/clusters/hvm/snapshots.rst` — Aligned the current Create Snapshot label and availability.
4. `administration/roles/role_permissions.rst` — Corrected navigation and distinguished Full from Read access.

## Delivery Evidence

Current controller and action code prove snapshot-capable layout, pending-removal, busy-state, and Snapshots: Full gates. This application-backed evidence satisfies the action documentation request while keeping storage behavior provider-scoped.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-9172
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

- Validate 8.1.0 action availability and storage/layout restrictions; the Jira expectation alone is not a support statement.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Review action visibility and permission behavior against current controller code.
2. Review the rendered pages against the Jira request.
3. Run `make build`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
