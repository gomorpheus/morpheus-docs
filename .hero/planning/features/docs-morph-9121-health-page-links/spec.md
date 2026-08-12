---
title: "Old links on health page doc "
slug: docs-morph-9121-health-page-links
type: feature
status: completed
horizon: now
size: small
tags: [documentation, health, links]
tracker_id: MORPH-9121
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:12:41Z
---

# Old links on health page doc 

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-9121

Exact Jira description (delivery source requirement):

> Our doc on the health page links to old support and forum pages. These had good/needed info on them. Can this be fixed. 

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-9121 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-9121-health-page-links/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `administration/health/health.rst`
- `operations/activity.rst`
- `troubleshooting/Attaching_Logs.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Replace obsolete support/forum links with maintained destinations or incorporate essential information locally, then check adjacent health-page references.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. Update `administration/health/health.rst` to carry the primary procedure and verified guidance.
2. Update `operations/activity.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.
3. Update `troubleshooting/Attaching_Logs.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.

## Acceptance Criteria

- THE DOCUMENTATION SHALL remove dependencies on retired forum and Knowledge Base pages from the Health workflow.
- WHEN escalation is required THE DOCUMENTATION SHALL link to the maintained HPE Support Center and retain essential diagnostic guidance locally.
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

- Replacement destinations and the content of retired pages are not supplied; obtain approved URLs or archived content before deleting useful guidance.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
