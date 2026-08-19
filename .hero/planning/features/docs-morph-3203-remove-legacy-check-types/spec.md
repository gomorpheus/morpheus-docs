---
title: "From comms data table, remove some check types that relate to old Instance Types we no longer ship"
slug: docs-morph-3203-remove-legacy-check-types
type: feature
status: completed
horizon: now
size: small
tags: [documentation, communication, monitoring, cleanup]
tracker_id: MORPH-3203
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:12:41Z
---
# From comms data table, remove some check types that relate to old Instance Types we no longer ship

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-3203

Jira description (verbatim):

> [https://support.hpe.com/hpesc/public/docDisplay?docId=sd00007079en_us&page=GUID-2EC9F4F8-8A77-4259-958F-7DC5EE782A2E.html](https://support.hpe.com/hpesc/public/docDisplay?docId=sd00007079en_us&page=GUID-2EC9F4F8-8A77-4259-958F-7DC5EE782A2E.html)

The current communications tables are maintained in `getting_started/functionality/communication.rst`, with related check-type descriptions in `monitoring/checks.rst`. Jira does not identify which rows are obsolete.

## Goal

Remove only product-confirmed legacy check types from the communications table and keep remaining monitoring and requirements references consistent.

## Kickoff

Remove obsolete communication-table check types only after obtaining the authoritative list from product engineering.

**Status:** planning — the local communication and monitoring tables are known, but Jira does not name rows.

**Pick up at:** compare the linked published table with current product check types and secure an approved removal list.

→ `.hero/planning/features/docs-morph-3203-remove-legacy-check-types/spec.md`

**Files:** `getting_started/functionality/communication.rst`, `monitoring/checks.rst`, `getting_started/requirements/requirements.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Treat this as a surgical table cleanup. Use a product-owned list as the source of truth and search all documentation for each removed type before editing.

## Changes

1. Update `getting_started/functionality/communication.rst` to remove the approved legacy check-type rows.
2. Update `monitoring/checks.rst` and `getting_started/requirements/requirements.rst` only where the same retired types remain referenced.

## Acceptance Criteria

- THE DOCUMENTATION SHALL identify the communication table as communication-category guidance, not an inventory of shipped Instance Types or automatically created checks.
- IF a check type cannot be demonstrated absent from shipped seeds/code or an approved product list THEN THE DOCUMENTATION SHALL retain its communication row.
- THE DOCUMENTATION SHALL direct readers to verify check availability in the current release before deployment planning.

## Boundaries

No product removal, monitoring redesign, broad table reformatting, or removal based solely on age.

## Risks

- **Blocker:** Jira and its linked page do not identify the check types to remove.
- Removing a still-supported row could cause deployment firewall misconfiguration.

## Validation

Obtain product sign-off on a before/after row list, search for every removed name, run `make build`, and review the rendered table alignment.
