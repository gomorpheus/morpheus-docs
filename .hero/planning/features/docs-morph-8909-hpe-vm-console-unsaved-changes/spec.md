---
title: "There Are Unsaved Changes Issues"
slug: docs-morph-8909-hpe-vm-console-unsaved-changes
type: feature
status: completed
horizon: now
size: small
tags: [documentation, hvm, networking, console]
tracker_id: MORPH-8909
jira_status: New
parent: docs-morph-3266-enhancements
relates-to:
  - docs-morph-8908-when-to-use-hpe-vm-console
  - docs-morph-8910-hpe-vm-console-exit-display
created: 2026-08-03
completed_at: 2026-08-03T15:12:19Z
---

# There Are Unsaved Changes Issues

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-8909

Exact Jira description (delivery source requirement):

> In Configuring the HVM Host using the hpe-vm console, if you follow the steps and edit the parameters you can hit ‘Save’ and get the message “Confirm Netplan changes may result in a disconnect. Are you sure you want to continue”. I clicked “Yes”. I clicked “Exit” then I got a popup that said “Confirm There are unsaved changes. Are you sure you want to exit without applying?” You have to hit yes even though the changes are just saved. This happens every time. 

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-8909 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-8909-hpe-vm-console-unsaved-changes/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `getting_started/installation/hvm_host_prep.rst`
- `tools/hvmcli/getting_started.rst`
- `tools/hvmcli/network.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Document the verified save/apply/exit sequence and explain any expected confirmation so users do not discard network changes.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. Update `getting_started/installation/hvm_host_prep.rst` to carry the primary procedure and verified guidance.
2. Update `tools/hvmcli/getting_started.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.
3. Update `tools/hvmcli/network.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-8909
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

- Reproduce on supported versions and determine whether this is a product defect. Do not normalize the reported stale unsaved-changes prompt without verification.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
