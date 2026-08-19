---
title: "Spelling - Maintaining GFS2 Consistency and High Availability"
slug: docs-morph-7773-gfs2-typos
type: feature
status: completed
horizon: now
size: trivial
tags: [documentation, hvm, gfs2, proofreading]
tracker_id: MORPH-7773
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:30:03Z
---
# Spelling - Maintaining GFS2 Consistency and High Availability

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-7773

> “Depects failures” and “synchnonize" need to be fixed.

The named strings are not present in the current RST corpus, suggesting the issue may already be covered or the source content moved.

## Goal
Confirm whether the two spelling defects remain in the current GFS2 content and correct them at their canonical source without unrelated rewriting.

## Kickoff
Search the current source and generated content for “Depects failures,” “synchnonize,” and the heading “Maintaining GFS2 Consistency and High Availability.” Start with `infrastructure/clusters/hvm/architecture.rst`, `infrastructure/clusters/hvm/storage_operations.rst`, and `infrastructure/clusters/hvm/monitoring.rst`. If neither typo exists, record the issue as already covered after checking the target release branch; do not manufacture a change. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions.

## Approach
Apply a surgical typo correction only where the current canonical source still contains the defects.

## Changes
1. Audit `architecture.rst`, `storage_operations.rst`, and `monitoring.rst` for the named heading and misspellings.
2. Correct only confirmed occurrences in the owning file; otherwise close as already corrected with search evidence.

## Acceptance Criteria
- THE DOCUMENTATION SHALL contain neither “Depects failures” nor “synchnonize” in the applicable GFS2 content.
- IF the defects are absent from the current source THEN THE DELIVERY SHALL record the audit evidence and make no content change.
- THE DOCUMENTATION SHALL preserve the technical meaning of the corrected sentences.

## Boundaries
No broad copyedit or GFS2 behavior changes.

## Risks
The Jira issue may target a different branch or external source. Delivery is blocked only if that target cannot be identified.

## Validation
Search source and built output for both strings, build the affected page if changed, and inspect the rendered sentence.

## Delivery Validation

- Audited `infrastructure/clusters/hvm/architecture.rst`, `storage_operations.rst`, and `monitoring.rst`; neither reported misspelling nor the obsolete heading exists.
- Repository-wide RST search found the strings only in this spec's quoted Jira text, not documentation content.
- Built HVM HTML contains neither misspelling. No content change was manufactured.
