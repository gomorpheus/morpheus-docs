---
title: "Veeam integration doesn't list SCVMM in available clouds"
slug: docs-morph-11196-veeam-scvmm-support
type: feature
status: completed
horizon: now
size: trivial
tags: [documentation, veeam, scvmm, backups]
tracker_id: MORPH-11196
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:30:46Z
---
# Veeam integration doesn't list SCVMM in available clouds

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-11196

Plugin-source feedback says Veeam supports SCVMM, Hyper-V, vCD, and ESXi, while the guide says to select an existing VMware, Hyper-V, or vCD Cloud.

## Goal
Correct the Veeam cloud-support list to include SCVMM after compatibility confirmation.

## Kickoff
Deliver `.hero/planning/features/docs-morph-11196-veeam-scvmm-support/spec.md`; update `backups/integrations/veeam.rst` and `integration_guides/Backups/veeam.rst`.

## Approach
Confirm SCVMM support against the released plugin and support matrix, then update both duplicate Veeam guide locations consistently.

## Changes
1. `backups/integrations/veeam.rst` — Added proven SCVMM support to every supported/available Cloud statement.
2. `integration_guides/Backups/veeam.rst` — Applied the equivalent SCVMM correction to the duplicate guide.

## Acceptance Criteria
- WHEN users configure Veeam THE SYSTEM SHALL list SCVMM among available Clouds when supported by the released plugin.
- IF support has a plugin or Manager minimum version THEN THE SYSTEM SHALL state it.
- THE SYSTEM SHALL keep both Veeam guide locations consistent.

## Boundaries
No expansion to unverified cloud types or plugin code changes.

## Risks
Source code capability may not equal QA-supported compatibility.

## Validation
Confirm with plugin QA/support matrix, render both pages, search for stale three-cloud lists, and run `make test`.
