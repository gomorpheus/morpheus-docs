---
title: "Docs: HVM Cluster 1.3 - Replace Pacemaker with Morpheus Agent"
slug: docs-morph-11393-hvm-agent-ha-control-plane
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, hvm, cluster-layout, high-availability]
tracker_id: MORPH-11393
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:33:01Z
---
# Docs: HVM Cluster 1.3 - Replace Pacemaker with Morpheus Agent

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-11393

The Jira has no description. The repository already documents layout 1.3 replacing Pacemaker with the Morpheus Agent quorum service; this work must verify completeness and consistency rather than invent additional behavior.

## Goal
Audit and complete layout 1.3 HA-control-plane documentation using approved product behavior.

## Kickoff
Deliver `.hero/planning/features/docs-morph-11393-hvm-agent-ha-control-plane/spec.md`; audit `infrastructure/clusters/hvm/architecture.rst`, `upgrading.rst`, `troubleshooting.rst`, `failure_scenarios.rst`, and `release_notes/9_0_0.rst`.

## Approach
Obtain MORPH-11393 acceptance details or owning epic evidence, compare them with existing pages, and make only evidenced gap corrections.

## Changes
1. Audit `infrastructure/clusters/hvm/architecture.rst` and `infrastructure/clusters/hvm/upgrading.rst` for accurate Pacemaker-to-Agent architecture and upgrade behavior.
2. Reconcile operational diagnostics in `infrastructure/clusters/hvm/troubleshooting.rst` and `failure_scenarios.rst` with layout 1.3 Agent quorum behavior.
3. Correct `release_notes/9_0_0.rst` only if approved source evidence identifies an inaccurate or incomplete release statement.

## Acceptance Criteria
- WHEN users read layout 1.3 guidance THE SYSTEM SHALL consistently identify the Morpheus Agent as the HA control plane and distinguish retained Corosync/DLM roles.
- WHEN users troubleshoot layout 1.3 THE SYSTEM SHALL NOT direct them to Pacemaker commands.
- IF no gap is found against approved requirements THEN THE SYSTEM SHALL record the audit evidence rather than fabricate edits.

## Boundaries
No behavior inferred beyond the title and verified source material; legacy layouts remain separate.

## Risks
No Jira description or linked epic is available.

## Validation
Product-owner sign-off, terminology search for contradictory layout 1.3 Pacemaker guidance, build, and `make test`.
