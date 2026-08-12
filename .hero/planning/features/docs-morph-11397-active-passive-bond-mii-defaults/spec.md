---
title: "Docs: HVM OS ISO default config to include mii configs for active/passive bonds"
slug: docs-morph-11397-active-passive-bond-mii-defaults
type: feature
status: completed
horizon: now
size: small
tags: [documentation, hvm, networking, bonds, 9.0]
tracker_id: MORPH-11397
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:27:26Z
---
# Docs: HVM OS ISO default config to include mii configs for active/passive bonds

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-11397; source epic: https://hpe.atlassian.net/browse/MORPH-6707

The request concerns HVM OS ISO defaults for MII polling, up-delay, and down-delay on active/passive bonds. MORPH-6707 records that the original 9.0 provisioning fix was reverted and redirected toward CLI work; its final rollout is unconfirmed and no exact values are authoritative.

## Goal
Document the truthful support boundary: automatic MII values are release- and networking-backend-specific, are not guaranteed, and must be inspected and configured explicitly through tooling supported by the installed release.

## Kickoff
Deliver `.hero/planning/features/docs-morph-11397-active-passive-bond-mii-defaults/spec.md`; update `infrastructure/clusters/hvm/virtual_switches.rst`, `getting_started/installation/hvm_host_prep.rst`, and reconcile `release_notes/9_0_0.rst`.

## Approach
Reconcile the reverted 9.0 claim and place release-neutral inspection/configuration guidance in the canonical HVM networking and host-console workflow without inventing values or unsupported commands.

## Changes
1. State in `infrastructure/clusters/hvm/virtual_switches.rst` that automatic Active Backup MII settings are not guaranteed and require release-supported inspection/configuration.
2. Add the same no-assumption boundary to the console/out-of-band host preparation workflow in `getting_started/installation/hvm_host_prep.rst`.
3. Correct the reverted automatic-default claim in `release_notes/9_0_0.rst`.

## Acceptance Criteria
- WHEN an Active Backup bond is provisioned THE DOCUMENTATION SHALL state that automatic MII polling, up-delay, and down-delay defaults are release/backend-specific and not guaranteed.
- WHEN an operator prepares an Active Backup bond for service THE DOCUMENTATION SHALL require inspection and explicit configuration through tooling supported by the installed release.
- IF MORPH-6707 does not confirm rollout or values THEN THE DOCUMENTATION SHALL not invent values, precedence, or unsupported commands.

## Boundaries
No changes to ISO generation or other bond modes.

## Risks
The eventual CLI implementation may expose a more specific supported workflow; this guidance intentionally remains accurate until that rollout is confirmed.

## Validation
Confirm the reverted Jira history, search affected docs for contradictory guarantees or invented values, render pages, and run `make build`.
