---
title: "The Guide items lack sufficient detail, impacting operations."
slug: docs-morph-11079-router-field-reference
type: feature
status: completed
horizon: now
size: small
tags: [documentation, networking, routers, ui-reference]
tracker_id: MORPH-11079
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:09:14Z
---
# The Guide items lack sufficient detail, impacting operations.

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-11079

The router guide lacks parameter/configuration explanations and does not clearly map the GUI router type **VM Network (OVS)** to documented supported router types.

## Goal
Align router creation documentation with the current GUI and define each supported router type and field.

## Kickoff
Deliver `.hero/planning/features/docs-morph-11079-router-field-reference/spec.md`; update `infrastructure/networks/routers.rst` and reconcile `integration_guides/Networking/networking.rst`.

## Approach
Inventory the current Create Router UI, map labels to backend/provider concepts, and document only supported, verified behavior.

## Changes
1. `infrastructure/networks/routers.rst` — Added the code-backed VM Network (OVS) field reference, applicability, and explicit non-routing capabilities.
2. `infrastructure/networks/routers.rst` — Mapped the UI label to the `openVSwitch` provider type.
3. `integration_guides/Networking/networking.rst` — Added the canonical router-reference link and provider-specific scope.

## Delivery Evidence

The current seed defines every documented OVS field and capability flag. The canonical page also states the truthful boundary for integration-supplied forms whose release-independent field metadata is not bundled, preventing OVS meanings or unavailable fields from being presented as provider support.

## Acceptance Criteria
- WHEN a user opens Create Router THE SYSTEM SHALL provide matching documentation for each visible field and supported type.
- WHEN **VM Network (OVS)** appears in the GUI THE SYSTEM SHALL explain its purpose, prerequisites, and applicability.
- IF a label differs by version/provider THEN THE SYSTEM SHALL state that scope.

## Boundaries
No router implementation or exhaustive networking-guide overhaul.

## Risks
Router fields are integration-dependent and screenshots may drift by release.

## Validation
Compare against the supported UI, obtain networking-owner review, render both pages, and run `make test`.
