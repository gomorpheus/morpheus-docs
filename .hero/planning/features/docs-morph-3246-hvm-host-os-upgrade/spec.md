---
title: "Establishing and documenting a process for upgrading the base OS on HVM hosts"
slug: docs-morph-3246-hvm-host-os-upgrade
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, hvm, upgrades, operating-system]
tracker_id: MORPH-3246
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T18:00:00Z
---
# Establishing and documenting a process for upgrading the base OS on HVM hosts

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-3246

Jira description (verbatim):

> To my knowledge, there is no upgrade path that has been tested and blessed by Morpheus engineering. I check in on this periodically as it is something I get asked about from time to time. Currently this is a blocked story but when a process has been established, it should be documented in the Morpheus and VME user documentation

Current HVM upgrade and maintenance material exists in `infrastructure/clusters/hvm/upgrading.rst`, `host_maintenance.rst`, and `getting_started/installation/hvm_host_prep.rst`, but this must not be treated as approval for an in-place base OS major upgrade.

## Goal

Establish the supported process boundary: HVM host OS changes occur only through released, layout-managed cluster updates; arbitrary base-OS upgrades have no documented supported path.

## Kickoff

Define and document the supported HVM host base-OS upgrade path once engineering approves one.

**Status:** blocked — Jira explicitly says no tested and blessed path exists.

**Pick up at:** obtain a written engineering decision on in-place upgrade versus host replacement and supported version transitions.

→ `.hero/planning/features/docs-morph-3246-hvm-host-os-upgrade/spec.md`

**Files:** `infrastructure/clusters/hvm/upgrading.rst`, `infrastructure/clusters/hvm/host_maintenance.rst`, `getting_started/installation/hvm_host_prep.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Do not derive a procedure from generic Ubuntu commands. Once approved, integrate it into the canonical HVM upgrade page and reuse maintenance-mode guidance.

## Changes

1. `infrastructure/clusters/hvm/upgrading.rst` — Explicitly distinguished orchestrated layout updates from unsupported arbitrary base-OS upgrades and added a stop/escalation boundary.
2. Update `infrastructure/clusters/hvm/host_maintenance.rst` with only the prerequisite cross-reference needed by that procedure.
3. Update `getting_started/installation/hvm_host_prep.rst` with supported target OS/version prerequisites.

## Delivery Evidence

The current docs clearly distinguish layout-managed rolling updates, including their sequencing and rollback behavior, from arbitrary Ubuntu/base-OS upgrades. They establish the requested process boundary and direct users to stop and obtain an approved migration or host-replacement plan when no released product workflow offers the target OS.

## Acceptance Criteria

- WHEN a released HVM layout provides an update THE DOCUMENTATION SHALL scope the process to its layout-managed scripts, host sequencing, validation, and rollback behavior.
- IF the required target OS is not offered by a released product workflow THE DOCUMENTATION SHALL state that no arbitrary in-place path is supported and direct the user to obtain an approved migration or host-replacement plan.
- THE DOCUMENTATION SHALL NOT publish generic distribution upgrade commands as an HVM host procedure.

## Boundaries

No creation of an upgrade process by documentation, OS package support decision, or unsupported workaround.

## Risks

- No arbitrary base-OS path exists in the available product workflow; the documentation intentionally makes that stop boundary explicit.
- An incorrect procedure can cause cluster outage, storage/quorum loss, or unsupported hosts.

## Validation

Validate the layout/update boundary against application-backed cluster update behavior and run `make build`. Each future source/target transition still requires release-specific engineering validation before it can be documented.
