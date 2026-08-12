---
title: "Windows Image ISO Upload Time"
slug: docs-morph-9204-windows-iso-upload-time
type: feature
status: completed
horizon: now
size: small
tags: [documentation, hvm, windows, iso]
tracker_id: MORPH-9204
jira_status: New
parent: docs-morph-3266-enhancements
relates-to:
  - docs-morph-8604-hvm-iso-local-vs-url
  - docs-morph-9134-ubuntu-iso-upload-time
created: 2026-08-03
completed_at: 2026-08-03T15:12:19Z
---

# Windows Image ISO Upload Time

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-9204

Exact Jira description (delivery source requirement):

> When following the documentation for **Configuring Windows Images for Use with HVM Clusters** I downloaded an ISO to my downloads folder and then used the Add File button to browse for it and upload. The file for the Windows server is around 5GB. This took 2 hours to load and I had to make sure to not let the screen time out. This step should recommend another method to upload an ISO that is shorter.

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-9204 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-9204-windows-iso-upload-time/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `library/virtual_images/virtual_images.rst`
- `infrastructure/clusters/hvm/guest_os_notes.rst`
- `getting_started/installation/singleNode/hpe_installer.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Clarify supported Windows ISO upload alternatives, prerequisites, progress monitoring, and session handling without promising a fixed transfer time.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. Update `library/virtual_images/virtual_images.rst` to carry the primary procedure and verified guidance.
2. Update `infrastructure/clusters/hvm/guest_os_notes.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.
3. Update `getting_started/installation/singleNode/hpe_installer.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-9204
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

- The two-hour timing is anecdotal. Validate supported alternate methods, security requirements, and browser/session timeout behavior.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
