---
title: "Operations > Activity need more detailed information"
slug: docs-morph-6243-operations-activity
type: feature
status: completed
horizon: now
size: small
tags: [documentation, operations, activity, audit]
tracker_id: MORPH-6243
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:31:32Z
---
# Operations > Activity need more detailed information

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-6243

> Has a 1-line description, compared to Enterprise which has information about all the tabs and screenshots

The repository already has substantial Activity and History coverage in `operations/activity.rst`; this work is therefore an audit and correction against the current UI, not a second Activity guide.

## Goal
Ensure the Operations > Activity documentation accurately explains every current tab, control, filter, result field, link behavior, permission dependency, and relevant limitation, with screenshots only where they add durable value.

## Kickoff
Audit the current UI against `operations/activity.rst`, then cross-check permission language in `administration/roles/role_permissions.rst` and audit-log overlap in `administration/logging/audit_logging.rst`. Preserve useful existing coverage and correct gaps rather than adding a parallel page. Obtain current-product UI access and approved screenshots before documenting tabs or labels that cannot be confirmed from the repository. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions.

## Approach
Use `operations/activity.rst` as the canonical page. Compare it with the supported product version and reconcile related pages so navigation and permission terminology agree.

## Changes
1. `operations/activity.rst` — Corrected tabs, event types, filters, scoping, links, History behavior, and permissions from ActivityController.
2. `administration/roles/role_permissions.rst` — Reconciled current Activity filter types and access scoping.
3. `administration/logging/audit_logging.rst` — Linked audit guidance to the canonical Operations Activity page.

## Acceptance Criteria
- WHEN a reader opens the Activity guide THE DOCUMENTATION SHALL explain every product-confirmed current tab and its purpose.
- WHEN a reader needs a specific event THE DOCUMENTATION SHALL explain the verified search, filter, date-range, and navigation controls.
- IF existing text conflicts with the current UI THEN THE DOCUMENTATION SHALL correct it rather than preserve duplicate or stale guidance.
- THE DOCUMENTATION SHALL state the verified role permission required for Activity and History access.

## Boundaries
No product behavior changes, speculative UI labels, comprehensive logging redesign, or unapproved screenshots.

## Risks
Current UI access is required. Delivery is blocked if the current tabs, permissions, or screenshot states cannot be product-confirmed.

## Validation
Build the affected docs, check links and image references, compare each documented control with the current supported UI, and obtain product-owner review.
