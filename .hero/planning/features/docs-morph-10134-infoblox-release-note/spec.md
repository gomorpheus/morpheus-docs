---
title: "Morpheus Enterprise Software 8.1.0 Release Notes - Infoblox updates"
slug: docs-morph-10134-infoblox-release-note
type: feature
status: completed
horizon: now
size: small
tags: [documentation, release-notes, infoblox, integrations, 8.1.0]
tracker_id: MORPH-10134
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:10:36Z
---
# Morpheus Enterprise Software 8.1.0 Release Notes - Infoblox updates

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-10134

The 8.1.0 release notes need exact Infoblox supported versions (the Jira states plugin 1.5.1 as of 2026-02-24) and a Marketplace reference comparable to Nutanix Prism Central.

## Goal
Make Infoblox compatibility and acquisition information explicit and verifiable in the 8.1.0 notes.

## Kickoff
Deliver `.hero/planning/features/docs-morph-10134-infoblox-release-note/spec.md`; update the maintained 8.1.0 source and verify corresponding rows in `release_notes/compatibility_table.rst`.

## Approach
Confirm plugin version and Manager compatibility from the plugin release artifact/Marketplace before publishing; mirror the Prism Central Marketplace treatment.

## Changes
1. Add MORPH-10134 to a historical 8.1.0 release-note page with plugin version 1.5.1, its supplied update date, and a Plugin Catalog (Marketplace) reference.
2. Qualify the exact version as Jira/release input and explicitly avoid a broad Infoblox or Manager compatibility claim.
3. Replace the broad Infoblox compatibility-table wording with plugin-release-specific guidance and the Marketplace acquisition path.

## Acceptance Criteria
- [x] WHEN users review 8.1.0 integration updates THE SYSTEM SHALL find MORPH-10134 and plugin version 1.5.1 attributed to the Jira/release input dated February 24, 2026.
- [x] WHEN users need the plugin THE SYSTEM SHALL receive an explicit Marketplace/Plugin Catalog reference.
- [x] THE SYSTEM SHALL NOT infer a broad supported Infoblox or Manager version range from the supplied plugin version.

## Boundaries
No Infoblox installation tutorial or unverified compatibility expansion.

## Risks
Plugin and Manager releases have independent lifecycles; stale compatibility claims can mislead upgrades.

## Validation
Build the documentation, inspect the historical page and compatibility table, verify qualified version wording, and run `make test`.

## Validation Results
- `make html` succeeded; the rendered page contains MORPH-10134, plugin version 1.5.1, the supplied date, Marketplace guidance, and the compatibility limitation.
- The compatibility table now defers support to each plugin release instead of claiming all latest versions are supported.
- `make build` and `make test` forward to nonexistent Sphinx builders in the current Makefile; a full Sphinx dummy build succeeded with pre-existing repository warnings.
