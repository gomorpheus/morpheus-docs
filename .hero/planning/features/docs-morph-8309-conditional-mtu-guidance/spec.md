---
title: "Change the wording for MTU"
slug: docs-morph-8309-conditional-mtu-guidance
type: feature
status: completed
horizon: now
size: small
tags: [documentation, hvm, networking, storage]
tracker_id: MORPH-8309
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:33:00Z
---

# Change the wording for MTU

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-8309

Exact Jira description (delivery source requirement):

> Right now the documentation says “Set the MTU to 9000”.
>
> And then after the picture there is a Note “Most iSCSI storage networks use Jumbo Frames for performance, this configuration needs to be consistent across the network.”
>
> ‌
>
> I think it might be better to specify directly “Set the MTU to 9000 if necessary” or “Set the MTU to 9000 if your hardware allows it”, because I’ve received a lot of questions asking why we needed to set it to 9000, or also some customer/partner automatically setting up to 9000 without thinking if they needed it or not.
>
> Thanks.

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-8309 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-8309-conditional-mtu-guidance/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `infrastructure/clusters/hvm/hvm_networks.rst`
- `infrastructure/clusters/hvm/virtual_switches.rst`
- `getting_started/installation/hvm_host_prep.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Make MTU 9000 conditional on an end-to-end jumbo-frame design and align the instruction, note, examples, and prerequisite language.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. Update `infrastructure/clusters/hvm/hvm_networks.rst` to carry the primary procedure and verified guidance.
2. Update `infrastructure/clusters/hvm/virtual_switches.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.
3. Update `getting_started/installation/hvm_host_prep.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-8309
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

- Verify which page contains the quoted instruction and whether any supported topology mandates MTU 9000 before changing normative wording.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
