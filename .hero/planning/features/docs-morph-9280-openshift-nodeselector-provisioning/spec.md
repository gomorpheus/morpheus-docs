---
title: "Openshift documentation for VM Provisioning using nodeSelector"
slug: docs-morph-9280-openshift-nodeselector-provisioning
type: feature
status: completed
horizon: now
size: small
tags: [documentation, openshift, provisioning, networking]
tracker_id: MORPH-9280
jira_status: New
parent: docs-morph-3266-enhancements
relates-to:
  - docs-morph-8198-openshift-vm-templates
created: 2026-08-03
completed_at: 2026-08-03T15:17:20Z
---

# Openshift documentation for VM Provisioning using nodeSelector

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-9280

Exact Jira description (delivery source requirement):

> Add the below under the section **Provisioning into OpenShift**  
> as a note.  
> ”Node selector labels included in VM templates are used during VM provisioning; only nodes that match these labels will be considered for deployment. Ensure that any network selected during VM provisioning is available on all matching nodes. Failure to do so may result in provisioning errors.”

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-9280 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-9280-openshift-nodeselector-provisioning/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `infrastructure/clusters/openshift.rst`
- `infrastructure/clusters/kubernetes.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Add a version-appropriate note explaining nodeSelector scheduling and the requirement that selected networks be available to every eligible node.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. Update `infrastructure/clusters/openshift.rst` to carry the primary procedure and verified guidance.
2. Update `infrastructure/clusters/kubernetes.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-9280
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

- Verify plugin behavior, supported selector forms, and failure symptoms with the OpenShift integration owner before publishing the supplied note as normative guidance.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
