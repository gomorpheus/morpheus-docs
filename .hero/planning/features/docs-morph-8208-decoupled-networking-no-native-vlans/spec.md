---
title: "Other scenario should be added: Decoupled without Native vLANs"
slug: docs-morph-8208-decoupled-networking-no-native-vlans
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, hvm, networking]
tracker_id: MORPH-8208
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:33:00Z
---

# Other scenario should be added: Decoupled without Native vLANs

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-8208

Exact Jira description (delivery source requirement):

> In our training with Peter around HVM, we saw that there is a possibility to have a Decoupled Networking setup without Native vLANs.  
> It is not part of our documentation at the moment, we only have Decoupled Networking setup with Native vLANs.

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-8208 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-8208-decoupled-networking-no-native-vlans/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `getting_started/installation/hvm_host_prep.rst`
- `infrastructure/clusters/hvm/hvm_networks.rst`
- `infrastructure/clusters/hvm/virtual_switches.rst`
- `tools/hvmcli/network.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Add a distinct, end-to-end decoupled-networking scenario without native VLANs alongside the existing topology guidance, including prerequisites, traffic mapping, and validation.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. Update `getting_started/installation/hvm_host_prep.rst` to carry the primary procedure and verified guidance.
2. Update `infrastructure/clusters/hvm/hvm_networks.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.
3. Update `infrastructure/clusters/hvm/virtual_switches.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.
4. Update `tools/hvmcli/network.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-8208
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

- The Jira issue contains no validated topology, field values, or screenshots; obtain an SME-approved configuration before authoring procedural steps.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
