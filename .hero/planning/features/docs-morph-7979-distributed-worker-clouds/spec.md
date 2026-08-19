---
title: "Distribuited Worked Doc update for supported Clouds"
slug: docs-morph-7979-distributed-worker-clouds
type: feature
status: completed
horizon: now
size: small
tags: [documentation, distributed-worker, cloud-support, operating-systems, audit]
tracker_id: MORPH-7979
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T16:00:00Z
---
# Distribuited Worked Doc update for supported Clouds

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-7979

> Regarding to an internal teams chat we should support HVM as Cloud type for our distributed worker. Can this this please added to the doc site? Can you please also check if SCVMM and Hyper-V Cloud types are supported as well and please also check with Ubuntu 24.04 for the distributed worker and update the documentation please?

`administration/integrations/workers.rst` is canonical and already contains a Cloud/Zone table plus package guidance. MORPH-7404 overlaps the HVM correction.

## Goal
Audit and correct Distributed Worker cloud-type and Ubuntu support statements for HVM, SCVMM, Hyper-V, and Ubuntu 24.04 using approved compatibility evidence.

## Kickoff
Audit `administration/integrations/workers.rst`, `release_notes/compatibility_table.rst`, and `release_notes/packages.rst`, plus existing Distributed Worker specs. Obtain a Product/Engineering support decision for HVM, SCVMM, Hyper-V, Ubuntu 24.04, release floors, package versus container differences, and supported Worker functions. Coordinate HVM wording with MORPH-7404 and do not treat an internal chat as authoritative support evidence. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions.

## Approach
Update the existing support table and requirements in place, merging overlap with MORPH-7404 during delivery.

## Changes
1. `administration/integrations/workers.rst` — States that HVM, SCVMM, and Hyper-V Distributed Worker Cloud proxy support is not established and keeps them out of the canonical supported list.
2. `administration/integrations/workers.rst` — States that Ubuntu 24.04 package support is not established and that the Alpine-based container runtime does not prove an Ubuntu host support combination.
3. `release_notes/compatibility_table.rst` and `release_notes/packages.rst` — Audited; neither establishes Worker runtime support, so no misleading cross-product claims were added.

## Delivery Evidence

Available evidence proves an Ubuntu 24.04 HVM appliance image from 8.0.6 and an HVM witness role from 9.0, but neither proves HVM, SCVMM, or Hyper-V Cloud proxy support. Worker container source proves an Alpine-based image, not Ubuntu 24.04 package or host policy.

## Acceptance Criteria
- THE DOCUMENTATION SHALL list HVM, SCVMM, and Hyper-V only with their approved Distributed Worker scope and release floor.
- THE DOCUMENTATION SHALL state whether Ubuntu 24.04 supports package, container, or both deployment methods.
- IF any requested platform remains unconfirmed THEN THE DOCUMENTATION SHALL leave it unlisted and record the blocker.
- THE DOCUMENTATION SHALL not duplicate HVM wording from MORPH-7404.

## Boundaries
No new platform support or inferred equivalence between Hyper-V and SCVMM.

## Risks
Delivery is blocked pending formal support confirmation for all requested platforms and deployment methods.

## Validation
Verify approved configurations, build affected pages, search for conflicting Worker support lists, and obtain Worker owner sign-off.
