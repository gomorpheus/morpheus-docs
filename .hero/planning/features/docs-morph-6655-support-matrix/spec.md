---
title: "For 8.1, add support matrix (formerly a kb) to the docs"
slug: docs-morph-6655-support-matrix
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, support-matrix, compatibility, release-notes]
tracker_id: MORPH-6655
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:12:41Z
---
# For 8.1, add support matrix (formerly a kb) to the docs

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-6655

> No description was provided in Jira.

Compatibility data already exists in `release_notes/compatibility.rst`, `release_notes/compatibility_table.rst`, and `integration_guides/Clouds/cloudCoverage/cloudCoverage.rst`. This work must determine whether the former knowledge-base matrix is already represented and correct it in place where possible.

## Goal
Provide one discoverable, product-approved support matrix for the applicable 8.1 documentation set, with an explicit scope and authoritative source for every support claim.

## Kickoff
Start with `release_notes/compatibility.rst`, `release_notes/compatibility_table.rst`, and `integration_guides/Clouds/cloudCoverage/cloudCoverage.rst`; also inspect their toctree owners before choosing the canonical location. Obtain the former KB content or URL and an approved 8.1 support data source first. Treat existing tables as candidates for consolidation, not as permission to infer missing support values. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions.

## Approach
Inventory existing matrices, map the former KB’s scope to the repository, designate one canonical table, and link to it from overlapping pages.

## Changes
1. Audit `release_notes/compatibility.rst` and `release_notes/compatibility_table.rst` against the approved former-KB source.
2. Audit overlap with `integration_guides/Clouds/cloudCoverage/cloudCoverage.rst`; consolidate or cross-link rather than repeat values.
3. Update the owning release-notes toctree only if the canonical matrix is not already discoverable.

## Acceptance Criteria
- WHEN a reader looks for support information THE DOCUMENTATION SHALL identify the release compatibility table as the canonical integration-version matrix.
- THE DOCUMENTATION SHALL distinguish platform compatibility from cloud feature coverage.
- IF a support value lacks an approved source THEN THE DOCUMENTATION SHALL omit it or explicitly state that it is not qualified and direct the reader to HPE Support.
- THE DOCUMENTATION SHALL not maintain conflicting duplicate matrices.

## Boundaries
No invented versions, retroactive promises, or changes to product support policy.

## Risks
Delivery is blocked until the former KB artifact and product-approved 8.1 values are supplied; Jira contains neither.

## Validation
Verify every cell against the approved source, build the release notes, check table rendering and links, and secure support/product sign-off.
