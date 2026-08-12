---
title: "Update XCP-ng in support matrix to 8.2.x"
slug: docs-morph-7928-xcp-ng-8-2
type: feature
status: completed
horizon: now
size: trivial
tags: [documentation, xcp-ng, support-matrix, compatibility]
tracker_id: MORPH-7928
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:12:41Z
---
# Update XCP-ng in support matrix to 8.2.x

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-7928

> We’re currently testing XCP against 8.2.1 so the support matrix should reflect that.

XCP-ng appears in `integration_guides/Clouds/cloudCoverage/cloudCoverage.rst`, `integration_guides/Clouds/xen/xen.rst`, and release compatibility pages. “Currently testing” is not equivalent to supported.

## Goal
Update XCP-ng compatibility to the approved 8.2.x/8.2.1 wording only after testing completes and support status is formally approved.

## Kickoff
Audit `release_notes/compatibility_table.rst`, `release_notes/compatibility.rst`, `integration_guides/Clouds/xen/xen.rst`, and `integration_guides/Clouds/cloudCoverage/cloudCoverage.rst`. Obtain completed test evidence and Product/Support approval for the precise published value—8.2.x versus 8.2.1—and applicable Morpheus release. Do not publish an in-progress test as support. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions. Check plugin version and release applicability before editing any table.

## Approach
Correct the canonical compatibility value and align cloud-guide references without duplicating the matrix.

## Changes
1. Update the approved XCP-ng version in `release_notes/compatibility_table.rst` or the confirmed canonical matrix.
2. Align version wording in `integration_guides/Clouds/xen/xen.rst` and links from `release_notes/compatibility.rst`.
3. Audit `cloudCoverage.rst` only for conflicting version claims; preserve feature-coverage scope.

## Acceptance Criteria
- IF XCP-ng 8.2.x testing lacks approval THE DOCUMENTATION SHALL retain the previously published qualified value.
- THE DOCUMENTATION SHALL explicitly state that testing activity is not support certification and that 8.2.x/8.2.1 is not approved by the bundled evidence.
- THE DOCUMENTATION SHALL use consistent qualification wording in the matrix and XCP-ng guide.

## Boundaries
No compatibility certification or inferred wildcard support.

## Risks
Delivery is blocked until testing completes and Product/Support chooses 8.2.x or 8.2.1 wording.

## Validation
Verify approval evidence, search for conflicting XCP-ng versions, build affected pages, and obtain integration owner sign-off.
