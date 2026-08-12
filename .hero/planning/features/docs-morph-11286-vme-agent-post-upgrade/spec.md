---
title: "Upgrade Documentation Missing Agent Update Requirement"
slug: docs-morph-11286-vme-agent-post-upgrade
type: feature
status: completed
horizon: now
size: small
tags: [documentation, vme, upgrades, agents, 8.1.1]
tracker_id: MORPH-11286
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:09:14Z
---
# Upgrade Documentation Missing Agent Update Requirement

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-11286

After a VME 8.1.1 Manager upgrade, the UI reports that an additional Agent update is required. The linked upgrade procedure mentions HVM Host Agents but does not identify all post-upgrade Agent dependencies or steps.

## Goal
Make required post-upgrade Agent updates, sequencing, dependencies, and verification explicit for VME 8.1.1.

## Kickoff
Deliver `.hero/planning/features/docs-morph-11286-vme-agent-post-upgrade/spec.md`; update `getting_started/maintenance/upgrading.rst`, the applicable files under `getting_started/maintenance/upgrades/`, and `infrastructure/clusters/hvm/upgrading.rst` where HVM-specific.

## Approach
Obtain the authoritative Agent compatibility/update matrix, separate Manager-level and HVM Host Agent steps, and add a post-upgrade checklist.

## Changes

1. `getting_started/maintenance/upgrading.rst` — Audited; no supplied evidence establishes a generic VME 8.1.1 post-upgrade Agent requirement, so none was added.
2. `getting_started/maintenance/upgrades/` — Audited; topology procedures were not given an unverified generic Agent sequence.
3. `infrastructure/clusters/hvm/upgrading.rst` — Documented the source-proven Agent 3.2.7 minimum, automatic pre-script upgrade, reconnection check, and strict HVM 1.2-to-1.3 scope.

## Delivery Evidence

The HVM update definitions prove `minAgentVersion: 3.2.7` only for the standard and HCI HVM 1.2-to-1.3 transitions. The canonical upgrade page documents that exact sequence and UI verification, and explicitly states that no generic all-Agent VME 8.1.1 requirement is established; unidentified update notices are routed to Support rather than converted into unsupported upgrade promises.

## Acceptance Criteria
- WHEN an operator completes a VME 8.1.1 Manager upgrade THE SYSTEM SHALL identify every Agent type that requires update and the supported sequence.
- WHEN Agent updates complete THE SYSTEM SHALL provide a UI/status verification step.
- IF an Agent update is release-dependent THEN THE SYSTEM SHALL scope the guidance by version.

## Boundaries
No upgrade automation changes or unsupported version matrix.

## Risks
“Agents” is ambiguous; publishing without component ownership confirmation could cause unnecessary upgrades.

## Validation
Release-engineering review, walkthrough on 8.1.1, rendered topology checks, and `make test`.
