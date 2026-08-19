---
title: "Morpheus Enterprise Software 8.1.0 Release Notes - Updated look"
slug: docs-morph-10132-hpe-branding-release-note
type: feature
status: completed
horizon: now
size: trivial
tags: [documentation, release-notes, branding, 8.1.0]
tracker_id: MORPH-10132
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:10:36Z
---
# Morpheus Enterprise Software 8.1.0 Release Notes - Updated look

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-10132

The 8.1.0 release notes do not mention the changed product look and feel from Morpheus branding to HPE branding.

## Goal
Add a customer-facing 8.1.0 enhancement note explaining the visual branding refresh.

## Kickoff
Deliver `.hero/planning/features/docs-morph-10132-hpe-branding-release-note/spec.md`; update the maintained 8.1.0 release-notes source and use `release_notes/current.rst` for style.

## Approach
Validate approved brand terminology and describe the visible change without implying functional behavior changed.

## Changes
1. Add a MORPH-10132 enhancement entry to a historical 8.1.0 release-note page for the HPE look-and-feel update.
2. State separately that HPE branding is the source-backed current default and avoid implying a functional change.

## Acceptance Criteria
- [x] WHEN users read the 8.1.0 enhancements THE SYSTEM SHALL find MORPH-10132 and a statement that default product branding and visual presentation changed from Morpheus to HPE.
- [x] THE SYSTEM SHALL identify HPE branding as the current default and SHALL NOT characterize the branding update as a functional change.

## Boundaries
No site-wide rebranding or screenshot replacement.

## Risks
Unapproved brand wording could conflict with current HPE naming standards.

## Validation
Build the documentation, inspect the rendered 8.1.0 entry and navigation, and run `make test`.

## Validation Results
- `make html` succeeded; the rendered page and release navigation contain the historical 8.1.0 branding entry.
- `make build` and `make test` forward to nonexistent Sphinx builders in the current Makefile.
- A full Sphinx dummy build succeeded with pre-existing repository warnings and no warning attributed to the historical page.
