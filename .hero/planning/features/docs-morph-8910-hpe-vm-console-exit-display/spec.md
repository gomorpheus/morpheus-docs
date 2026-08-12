---
title: "Leaving the hpe-vm console results in a messed up UI"
slug: docs-morph-8910-hpe-vm-console-exit-display
type: feature
status: completed
horizon: now
size: small
tags: [documentation, hvm, console, troubleshooting]
tracker_id: MORPH-8910
jira_status: New
parent: docs-morph-3266-enhancements
relates-to:
  - docs-morph-8908-when-to-use-hpe-vm-console
  - docs-morph-8909-hpe-vm-console-unsaved-changes
created: 2026-08-03
completed_at: 2026-08-03T15:12:19Z
---

# Leaving the hpe-vm console results in a messed up UI

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-8910

Exact Jira description (delivery source requirement):

> When a user exits the hpe-vm console as described in the documentation Configuring the HVM host using hpe-vm console the console remains almost entirely blue and the cursor where you can type is right justified. Please see attached picture. If you type ‘clear’ it goes back to a normal terminal.

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-8910 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-8910-hpe-vm-console-exit-display/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `tools/hvmcli/getting_started.rst`
- `tools/hvmcli/network.rst`
- `infrastructure/clusters/hvm/troubleshooting.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Add a concise, verified terminal-reset recovery note at the console exit point if the behavior remains present in supported versions.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. Update `tools/hvmcli/getting_started.rst` to carry the primary procedure and verified guidance.
2. Update `tools/hvmcli/network.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.
3. Update `infrastructure/clusters/hvm/troubleshooting.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-8910
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

- The attached image is unavailable. Reproduce and confirm whether `clear` is sufficient or whether a terminal reset/product fix is required.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
