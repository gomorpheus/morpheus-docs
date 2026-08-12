---
title: "Document the overlay option for HVM networks"
slug: docs-morph-3235-hvm-overlay-networks
type: feature
status: completed
horizon: now
size: small
tags: [documentation, hvm, networking, overlay, vxlan]
tracker_id: MORPH-3235
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:17:20Z
---
# Document the overlay option for HVM networks

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-3235

Jira description (verbatim):

> Document the overlay option for HVM networks

Substantial overlay coverage already exists in `infrastructure/clusters/hvm/hvm_networks.rst`, with related cluster fields in `building_clusters.rst` and generic network context in `infrastructure/networks/networks.rst`.

## Goal

Audit and complete HVM overlay network documentation so prerequisites, UI fields, VXLAN behavior, lifecycle, limitations, and verification are accurate and easy to find without duplicating existing content.

## Kickoff

Audit the existing HVM Overlay Network section and close only verified gaps from MORPH-3235.

**Status:** planning — a detailed overlay section already exists, so this may be a validation-and-refinement task.

**Pick up at:** compare current UI and plugin behavior with the existing overlay procedure and record discrepancies.

→ `.hero/planning/features/docs-morph-3235-hvm-overlay-networks/spec.md`

**Files:** `infrastructure/clusters/hvm/hvm_networks.rst`, `infrastructure/clusters/hvm/building_clusters.rst`, `infrastructure/networks/networks.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Preserve `hvm_networks.rst` as canonical. Validate current coverage before adding anything and use cross-references from generic pages.

## Changes

1. Update `infrastructure/clusters/hvm/hvm_networks.rst` only for verified gaps in overlay prerequisites, fields, behavior, lifecycle, or limitations.
2. Align `infrastructure/clusters/hvm/building_clusters.rst` overlay field descriptions with the canonical page.
3. Update `infrastructure/networks/networks.rst` only with a discoverability link if absent.

## Acceptance Criteria

- WHEN a user creates an HVM Overlay Network THE DOCUMENTATION SHALL explain prerequisites, every current field, resulting VXLAN/OVS behavior, and deletion impact.
- THE DOCUMENTATION SHALL identify layout or version constraints confirmed by engineering.
- IF existing coverage already satisfies a criterion THEN delivery SHALL avoid duplicating it.

## Boundaries

No overlay implementation change, general VXLAN design tutorial, or rewrite of unrelated HVM network types.

## Risks

- Current documentation may already satisfy most of Jira, so unsupported expansion would reduce accuracy.
- Plugin behavior can vary by release and layout.

## Validation

Exercise create/use/delete in a supported cluster, compare every field to the UI, run `make build`, and review all cross-references.
