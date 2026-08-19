---
title: "Remove HVM host from cluster"
slug: docs-morph-7791-hvm-host-removal
type: feature
status: completed
horizon: now
size: small
tags: [documentation, hvm, clusters, hosts, audit]
tracker_id: MORPH-7791
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:49:50Z
---
# Remove HVM host from cluster

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-7791

> Currently, we do not have any public documentation for customers who want to remove a node from an HVM cluster. There is no quick or simple option in the UI to perform this action. At this time, the process appears to require several steps that must be executed directly on the host, if removal is desired.
>
> We should document this procedure. We have seen customers attempt to remove nodes by following unofficial or incomplete steps, which has resulted in multiple issues. Proper documentation would help prevent these problems

Current `infrastructure/clusters/hvm/managing_hosts.rst` already documents a UI-driven removal workflow. This spec audits that newer coverage and corrects any release/layout mismatch rather than reintroducing host-shell instructions.

## Goal
Ensure the canonical HVM host-removal guide accurately describes the supported workflow for each applicable cluster layout, including when UI removal is available and when Support involvement is required.

## Kickoff
Audit `infrastructure/clusters/hvm/managing_hosts.rst` against the supported releases and layouts implicated by Jira. Cross-check `host_maintenance.rst`, `troubleshooting.rst`, and `alarms.rst`. Confirm whether the current UI workflow supersedes the older direct-host process and identify its release floor. Never publish old shell steps merely because Jira says they “appear” necessary. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions.

## Approach
Use the existing host-management page as canonical and add version/layout qualifications based on Engineering evidence.

## Changes
1. Correct `managing_hosts.rst` for supported UI and non-UI paths, prerequisites, consequences, and escalation points.
2. Align `host_maintenance.rst`, `troubleshooting.rst`, and `alarms.rst` with the canonical workflow.
3. Cross-reference MORPH-7772 coverage during delivery to prevent duplicate prose.

## Acceptance Criteria
- WHEN a supported release offers UI host removal THE DOCUMENTATION SHALL give the verified UI procedure and release/layout scope.
- IF a release or failure state requires direct intervention THEN THE DOCUMENTATION SHALL provide only Engineering-approved steps or direct users to Support.
- THE DOCUMENTATION SHALL warn about verified quorum, storage, VM, and network consequences.
- THE DOCUMENTATION SHALL not duplicate the procedure created or audited for MORPH-7772.

## Boundaries
No unsupported host-shell procedure or product feature change.

## Risks
Jira may describe old behavior. Delivery is blocked pending version/layout confirmation and destructive-procedure review.

## Validation
Test each documented path in disposable clusters, verify post-removal health, build docs, and obtain HVM Engineering sign-off.
