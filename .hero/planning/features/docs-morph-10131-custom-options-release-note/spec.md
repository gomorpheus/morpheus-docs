---
title: "Morpheus Enterprise Software 8.1.0 Release Notes - Custom Options fix"
slug: docs-morph-10131-custom-options-release-note
type: feature
status: completed
horizon: now
size: trivial
tags: [documentation, release-notes, service-catalog, 8.1.0]
tracker_id: MORPH-10131
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:10:36Z
---
# Morpheus Enterprise Software 8.1.0 Release Notes - Custom Options fix

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-10131

The 8.1.0 release notes omit the fix for case 5392804959, where use of `customoption.cloud.split` produced `catalogError`.

## Goal
Record the verified custom-option catalog fix in the 8.1.0 fixed-issues list.

## Kickoff
Deliver `.hero/planning/features/docs-morph-10131-custom-options-release-note/spec.md`; update the maintained 8.1.0 release-notes source, following `release_notes/current.rst` formatting.

## Approach
Obtain approved customer-safe wording from the fix record, preserving the exact expression and case identifier.

## Changes
1. Add MORPH-10131 and case 5392804959 to a historical 8.1.0 release-note page and describe the reported `catalogError` fix involving `customoption.cloud.split`.
2. Attribute the exact behavior to the release record rather than claiming wider Custom Options compatibility.

## Acceptance Criteria
- [x] WHEN users inspect 8.1.0 fixed issues THE SYSTEM SHALL identify MORPH-10131, case 5392804959, and the reported `customoption.cloud.split` catalog fix.
- [x] THE SYSTEM SHALL render the expression as code without altering its spelling and SHALL NOT overclaim broader compatibility.

## Boundaries
No Service Catalog usage tutorial or changes to releases other than 8.1.0.

## Risks
The 8.1.0 source is not present locally; placement requires the maintained publication source.

## Validation
Build the documentation, verify the entry, Jira key, case number, and code markup, and run `make test`.

## Validation Results
- `make html` succeeded; the rendered page contains MORPH-10131, case 5392804959, and code-formatted ``customoption.cloud.split``.
- `make build` and `make test` forward to nonexistent Sphinx builders in the current Makefile.
- A full Sphinx dummy build succeeded with pre-existing repository warnings and no warning attributed to the historical page.
