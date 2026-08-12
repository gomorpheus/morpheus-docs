---
title: "[VME version: 8.1.0]: Jobs, History and Integrations tabs are missing under Backups in HPE Morpheus VME Document"
slug: docs-morph-9169-backups-jobs-history-integrations
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, vme, backups, navigation]
tracker_id: MORPH-9169
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:31:03Z
---

# [VME version: 8.1.0]: Jobs, History and Integrations tabs are missing under Backups in HPE Morpheus VME Document

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-9169

Exact Jira description (delivery source requirement):

> Setup: PCBE Greenfield VME  
> Agent Version: 3.1.3  
> VME Manager: 8.1.0  
> Storage plugin: 1.9.2
>
> The Documentation does not include details about the Jobs, History and Integrations under Backups Menu for the Backup workflow
>
> VME Environment: [https://10.157.232.173](https://10.157.232.173/)
>
> **Steps to Reproduce:**
>
> 1.Connect to VME and Go to 'Backups'
>
> 2.Verify the Jobs, History and Integrations tabs under Backups
>
> **Expected Result:**
>
> "Jobs, History and Integrations tabs" should be available under Backups in HPE Morpheus VME Document
>
> **Actual Output:**
>
> “Jobs, History and Integrations tabs” are missing under Backups in HPE Morpheus VME Documentation

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-9169 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-9169-backups-jobs-history-integrations/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `backups/backups.rst`
- `backups/backups_sub.rst`
- `backups/integrations/integrations.rst`
- `backups/summary.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Document the Jobs, History, and Integrations backup surfaces in the VME navigation, reusing existing backup concepts and version-scoping differences from Enterprise where needed.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. `backups/backups.rst` — Documented Summary, Jobs, Backups, History, and Integrations navigation plus permission-dependent visibility.
2. `backups/backups_sub.rst` — Added Jobs and History task cross-references.
3. `backups/integrations/integrations.rst` — Added the navigation path and Backup Services permission behavior.
4. `backups/summary.rst` — Added navigation and adjacent-view guidance.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-9169
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

- Verify the 8.1.0 UI, role-dependent visibility, and exact History content before adding fields or procedures.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
