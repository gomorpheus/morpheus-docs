---
title: "Update Tenant guide to include Parent Tenant field"
slug: docs-morph-11023-parent-tenant-field
type: feature
status: completed
horizon: now
size: trivial
tags: [documentation, tenants, ui-reference]
tracker_id: MORPH-11023
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:31:32Z
---
# Update Tenant guide to include Parent Tenant field

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-11023

The create-tenant procedure's field list omits the new **Parent Tenant** field, specifically from bullet 4 referenced in the Jira request.

## Goal
Document when and how the Parent Tenant selector is used during tenant creation.

## Kickoff
Deliver `.hero/planning/features/docs-morph-11023-parent-tenant-field/spec.md`; update `administration/tenants/tenants.rst` and reconcile `administration/tenants/configuring_multi_tenancy.rst`.

## Approach
Add the field to the existing create workflow and explain availability, default/root behavior, and hierarchy effect only after UI/product confirmation.

## Changes
1. `administration/tenants/tenants.rst` — Added required Parent Tenant selection, hierarchy result, creation visibility, edit lock, and default-parent behavior.

## Acceptance Criteria
- WHEN an administrator follows tenant creation THE SYSTEM SHALL list and explain the Parent Tenant field.
- IF the selector is conditional on permissions or tenant context THEN THE SYSTEM SHALL state those conditions.
- THE SYSTEM SHALL explain the result of leaving the field unset.

## Boundaries
No redesign of the tenancy guide or undocumented hierarchy behavior.

## Risks
The Jira screenshot is not in the payload; exact options and visibility rules require product verification.

## Validation
Compare against the current UI, render the tenant guide, verify the field order and cross-links, and run `make test`.
