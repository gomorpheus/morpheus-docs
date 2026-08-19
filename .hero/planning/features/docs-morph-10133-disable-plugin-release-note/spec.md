---
title: "Morpheus Enterprise Software 8.1.0 Release Notes - Disable Plugin fix"
slug: docs-morph-10133-disable-plugin-release-note
type: feature
status: completed
horizon: now
size: trivial
tags: [documentation, release-notes, plugins, 8.1.0]
tracker_id: MORPH-10133
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:10:36Z
---
# Morpheus Enterprise Software 8.1.0 Release Notes - Disable Plugin fix

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-10133

The 8.1.0 release notes omit case 5401996862 concerning disappearance of the option to disable plugins from both the GUI and API.

## Goal
Document the verified resolution and its GUI/API scope in the 8.1.0 fixed issues.

## Kickoff
Deliver `.hero/planning/features/docs-morph-10133-disable-plugin-release-note/spec.md`; update the maintained 8.1.0 release-notes source, with `release_notes/current.rst` as style reference.

## Approach
Confirm whether the release restored, intentionally removed, or otherwise changed the option before selecting the verb used in the note.

## Changes
1. Add MORPH-10133 and case 5401996862 to a historical 8.1.0 release-note page with careful wording covering the reported GUI and API scope.
2. Identify the current GUI enable/disable control as source-backed while attributing the historical API scope to the case and release input.

## Acceptance Criteria
- [x] WHEN users inspect 8.1.0 fixed issues THE SYSTEM SHALL find MORPH-10133, case 5401996862, and its reported GUI/API scope.
- [x] THE SYSTEM SHALL distinguish source-backed current GUI behavior from the historical API claim supplied by the case and release input.

## Boundaries
No plugin administration procedure or API contract update.

## Risks
The Jira wording describes a symptom, not the confirmed resolution.

## Validation
Build the documentation, verify the Jira key, case, qualified GUI/API wording, and rendered navigation, and run `make test`.

## Validation Results
- `make html` succeeded; the rendered page contains MORPH-10133, case 5401996862, and the qualified GUI/API wording.
- `make build` and `make test` forward to nonexistent Sphinx builders in the current Makefile.
- A full Sphinx dummy build succeeded with pre-existing repository warnings and no warning attributed to the historical page.
