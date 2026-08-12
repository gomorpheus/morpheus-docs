---
title: "Docs: Zerto Support - HVM DR Post GA"
slug: docs-morph-11414-zerto-hvm-dr
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, zerto, hvm, disaster-recovery, 9.0]
tracker_id: MORPH-11414
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:12:41Z
---
# Docs: Zerto Support - HVM DR Post GA

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-11414; source epic: https://hpe.atlassian.net/browse/MORPH-6550

This chore tracks post-GA Zerto disaster-recovery documentation for HVM. The Jira contains no workflows, versions, prerequisites, or limitations.

## Goal
Document released Zerto-on-HVM support end to end using MORPH-6550 acceptance and QA evidence.

## Kickoff
Deliver `.hero/planning/features/docs-morph-11414-zerto-hvm-dr/spec.md`; ingest MORPH-6550, then update `backups/integrations/zerto.rst`, `integration_guides/Backups/zerto.rst`, and compatibility/release-note sources.

## Approach
Confirm supported Zerto/Manager/HVM versions and DR operations before extending existing VMware-centric language.

## Changes
1. Extract HVM prerequisites, supported replication/failover/failback operations, limitations, and tested versions from MORPH-6550.
2. Update `backups/integrations/zerto.rst` and `integration_guides/Backups/zerto.rst` with consistent HVM workflow guidance.
3. Reconcile `release_notes/compatibility_table.rst` and the applicable release note after release scope is confirmed.

## Acceptance Criteria
- IF no HVM/Zerto interoperability and QA evidence is bundled THEN THE DOCUMENTATION SHALL explicitly make no HVM disaster-recovery support claim.
- THE DOCUMENTATION SHALL retain the documented Zerto boundary for compatible Clouds such as VMware vCenter and link the canonical qualified-version matrix.
- THE DOCUMENTATION SHALL identify Zerto infrastructure and recovery-plan operation as governed by Zerto documentation.

## Boundaries
No Zerto product configuration beyond Morpheus integration scope and no unsupported pre-GA behavior.

## Risks
Existing Zerto prose says “such as VMware”; careless edits could imply broad cloud support.

## Validation
Zerto/HVM QA review, workflow exercise, compatibility cross-check, rendered-page build, and `make test`.
