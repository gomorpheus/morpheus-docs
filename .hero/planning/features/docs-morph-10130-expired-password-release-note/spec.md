---
title: "Morpheus Enterprise software 8.1.0 release notes update - Expired password fix"
slug: docs-morph-10130-expired-password-release-note
type: feature
status: completed
horizon: now
size: trivial
tags: [documentation, release-notes, authentication, 8.1.0]
tracker_id: MORPH-10130
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:10:36Z
---
# Morpheus Enterprise software 8.1.0 release notes update - Expired password fix

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-10130

The HPE Morpheus Enterprise Software 8.1.0 release notes omit the fix for case 5392395910: the expired-password flag for local Morpheus accounts did not function.

## Goal
Add an accurate 8.1.0 fixed-issue entry that identifies the local-account expired-password behavior without overstating the fix.

## Kickoff
Deliver `.hero/planning/features/docs-morph-10130-expired-password-release-note/spec.md`; update the maintained 8.1.0 release-notes source (not currently present in this checkout), using `release_notes/current.rst` as the formatting reference.

## Approach
Confirm the approved fix wording and 8.1.0 publication source with Release Engineering, then add one concise fixed-issue entry in the existing release-note taxonomy.

## Changes
1. Add a concise historical 8.1.0 release-note page with MORPH-10130, case 5392395910, and the expired-password flag fix.
2. Include the historical page in release navigation and distinguish the source-backed current behavior from the historical release claim.

## Acceptance Criteria
- [x] WHEN the 8.1.0 fixed issues are reviewed THE SYSTEM SHALL list MORPH-10130 and case 5392395910 and state that the expired-password flag for local accounts was fixed.
- [x] THE SYSTEM SHALL distinguish source-backed current behavior from the historical release claim.

## Boundaries
No authentication workflow changes, new troubleshooting guidance, or edits to other release versions.

## Risks
The 8.1.0 source is absent from this checkout; editing a current-version file would publish the note in the wrong release.

## Validation
Build the documentation, inspect the rendered 8.1.0 fixed-issues section, verify the Jira and case identifiers, and run `make test`.

## Validation Results
- `make html` succeeded; the rendered historical page contains MORPH-10130 and case 5392395910.
- `make build` and `make test` are not defined project targets: the Makefile forwards them to nonexistent Sphinx builders named `build` and `test`.
- A full Sphinx dummy build succeeded with pre-existing repository warnings and no warning attributed to `release_notes/8_1_0.rst`.
