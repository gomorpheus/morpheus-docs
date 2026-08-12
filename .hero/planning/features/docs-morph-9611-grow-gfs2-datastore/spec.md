---
title: "How to grow GFS2 datastore "
slug: docs-morph-9611-grow-gfs2-datastore
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, hvm, gfs2, storage]
tracker_id: MORPH-9611
jira_status: New
parent: docs-morph-3266-enhancements
relates-to:
  - docs-morph-8707-grow-gfs2-datastore
created: 2026-08-03
completed_at: 2026-08-03T15:17:20Z
---

# How to grow GFS2 datastore 

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-9611

Exact Jira description (delivery source requirement):

> We need a doc on how to grow a GFS2 Datastore 

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-9611 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-9611-grow-gfs2-datastore/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `infrastructure/clusters/hvm/storage_operations.rst`
- `infrastructure/clusters/hvm/capacity_planning.rst`
- `infrastructure/clusters/hvm/troubleshooting.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Resolve whether supported releases allow in-place GFS2 datastore growth and document an approved, version-scoped workflow or explicitly retain the add-datastore model.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. Update `infrastructure/clusters/hvm/storage_operations.rst` to carry the primary procedure and verified guidance.
2. Update `infrastructure/clusters/hvm/capacity_planning.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.
3. Update `infrastructure/clusters/hvm/troubleshooting.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-9611
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

- BLOCKED: no runbook is supplied. Resolve duplicate ownership with MORPH-8707 and obtain storage-engineering approval before documenting any destructive or cluster-wide command.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
