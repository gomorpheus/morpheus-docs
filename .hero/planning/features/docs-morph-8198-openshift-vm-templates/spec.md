---
title: "Update \"Provisioning into OpenShift\" section in OpenShift documentation"
slug: docs-morph-8198-openshift-vm-templates
type: feature
status: completed
horizon: now
size: small
tags: [documentation, openshift, provisioning]
tracker_id: MORPH-8198
jira_status: New
parent: docs-morph-3266-enhancements
relates-to:
  - docs-morph-9280-openshift-nodeselector-provisioning
created: 2026-08-03
completed_at: 2026-08-03T15:17:20Z
---

# Update "Provisioning into OpenShift" section in OpenShift documentation

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-8198

Exact Jira description (delivery source requirement):

> Add the following under the section in the documentation   
> [https://support.hpe.com/hpesc/docDisplay?docId=sd00007322en_us&page=GUID-786D5554-1448-4001-A39C-647F22CA9278.html](https://support.hpe.com/hpesc/docDisplay?docId=sd00007322en_us&page=GUID-786D5554-1448-4001-A39C-647F22CA9278.html)  
> **Provisioning into OpenShift**
>
>  
>
> **Current Text**
>
>  
>
> Image: Select from all synced virtual images. Note that only custom user images are synced from OpenShift, we do not sync from the large library of default images that ship with OpenShift
>
>  
>
> **Change to**
>
>  
>
> Image: Select from all synced virtual images. To provision VMs in OpenShift, you must create virtual machine templates with an existing PVC as the source.   
> Only templates created this way will be synchronized to Morpheus as virtual images. OpenShift's default image catalog is not synchronized.

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-8198 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-8198-openshift-vm-templates/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `infrastructure/clusters/openshift.rst`
- `infrastructure/clusters/kubernetes.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Replace the outdated Image field explanation in Provisioning into OpenShift with the PVC-backed VM-template synchronization requirement, preserving surrounding terminology and navigation.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. Update `infrastructure/clusters/openshift.rst` to carry the primary procedure and verified guidance.
2. Update `infrastructure/clusters/kubernetes.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-8198
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

- Confirm the PVC-backed template requirement and supported OpenShift/plugin versions with the product owner before publishing.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
