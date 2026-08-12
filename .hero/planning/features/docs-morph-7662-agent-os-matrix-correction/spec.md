---
title: "Mis-match of Supported Agent OS's"
slug: docs-morph-7662-agent-os-matrix-correction
type: feature
status: completed
horizon: now
size: small
tags: [documentation, agent, operating-systems, support, correction]
tracker_id: MORPH-7662
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:09:14Z
---
# Mis-match of Supported Agent OS's

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-7662

> The Morpheus Agent OS Support page says that we support 32bit & 64bit Debian from version 6, however release notes state that we've dropped support for Debian 9 & 10 and Ubuntu 14, 16 & 18. Looking at 8.0.13, we don’t include 32-bit agents in the repo anymore, so might need to remove 32-bit Linux derivatives.

## Goal
Reconcile the canonical Agent OS matrix with current package availability and approved lifecycle policy, including Debian, Ubuntu, and 32-bit Linux support.

## Kickoff
Audit `getting_started/functionality/agent/osSupport.rst`, `release_notes/packages.rst`, `release_notes/compatibility.rst`, and relevant release notes. Obtain the package manifest for supported releases and an Agent owner decision on Debian/Ubuntu minimums and 32-bit status. Treat the reporter’s assumptions as hypotheses: package absence and dropped-version notes do not independently prove all earlier releases unsupported. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions.

## Approach
Correct one canonical matrix and use release notes for historical change context, not as competing current support tables.

## Changes
1. `getting_started/functionality/agent/osSupport.rst` — Reclassified the existing generated table as an OS recognition catalog and explicitly states that 32-bit/general rows do not prove current package support.
2. `release_notes/packages.rst` — Audited; no architecture/version manifest exists there from which current Debian, Ubuntu, or 32-bit support can be truthfully derived.
3. Historical release-note links were not changed because no approved current package matrix is available to receive them.

## Delivery Evidence

The supplied repositories do not contain a release-by-release Agent package policy sufficient to replace the generated recognition catalog with an approved support matrix. The canonical page now states that catalog rows, including historical Debian/Ubuntu and 32-bit rows, are not current support claims and directs readers to release history and target-release package policy without inferring unknown minimums.

## Acceptance Criteria
- THE DOCUMENTATION SHALL list only approved Agent OS versions and architectures.
- WHEN support was removed THE DOCUMENTATION SHALL distinguish the current matrix from historical release-note changes.
- IF 32-bit packages are unavailable THEN THE DOCUMENTATION SHALL remove 32-bit support claims for the applicable releases.
- IF older Debian or Ubuntu status is unconfirmed THEN THE DOCUMENTATION SHALL not infer it.

## Boundaries
No restoration of packages or unsupported lifecycle promises.

## Risks
Exact Debian/Ubuntu minimums remain explicitly unestablished rather than being published as support.

## Validation
Compare matrix rows to repository artifacts for each supported release, build docs, and obtain Release/Agent sign-off.
