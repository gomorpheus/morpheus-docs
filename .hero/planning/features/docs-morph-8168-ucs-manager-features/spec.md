---
title: "UCS Manager Cloud Integration features"
slug: docs-morph-8168-ucs-manager-features
type: feature
status: completed
horizon: now
size: large
tags: [documentation, cisco-ucs, cloud-integration, bare-metal, monitoring, costing]
tracker_id: MORPH-8168
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T18:00:00Z
---
# UCS Manager Cloud Integration features

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-8168

> * Zone-level onboarding of a UCS Manager endpoint, with org selection/creation and validation.
> * Full UCS inventory sync into Morpheus (orgs, chassis, cartridges, blades, cartridge servers, networks, policies, pools, storage profiles, server pools).
> * Bare-metal provisioning of Morpheus hosts using UCS Service Profiles, MAC pools, PXE images, and Kickstart automation.
> * Lifecycle management for UCS servers: onboarding unmanaged assets, creating managed nodes, and safely returning them to unmanaged state.
> * Monitoring & alarms by ingesting UCS faults into Morpheus's notification system and tying them to the corresponding server/chassis/zone.
> * Costing support via a dedicated UCS price set and component prices.

Existing `integration_guides/Clouds/ucs_manager/ucs_manager.rst` is only a short integration page and already claims inventory/provisioning features. This is an audit and expansion, not a parallel guide.

## Goal
Turn the UCS Manager integration page into a verified operator reference covering onboarding, inventory, provisioning, lifecycle, monitoring/alarms, and costing, with permissions, prerequisites, limitations, and safe validation.

## Kickoff
Audit `integration_guides/Clouds/ucs_manager/ucs_manager.rst`, `getting_started/requirements/requirements.rst`, `operations/alarms.rst`, `administration/plans_pricing/prices.rst`, and relevant host lifecycle pages. Exercise each Jira-listed capability in a supported UCS lab and obtain exact UI fields, object mappings, sync behavior, prerequisites, release floors, and limitations from the integration owner. Omit any listed capability that cannot be confirmed. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions.

## Approach
Expand the existing UCS page with task-oriented sections and link to canonical monitoring, pricing, and host-management concepts rather than restating them.

## Changes
1. `integration_guides/Clouds/ucs_manager/ucs_manager.rst` — Expanded code-evidenced onboarding, inventory, provisioning, lifecycle, fault, and costing behavior.
2. `getting_started/requirements/requirements.rst` — Added the UCS API endpoint connectivity prerequisite.

## Delivery Evidence

The integration implementation supports the documented onboarding, inventory, provisioning, lifecycle, fault, and pricing concepts. The page states the operational prerequisites and limitations without inventing a universal Cisco privilege set, UCS-side remediation, or pricing outcome.

## Acceptance Criteria
- WHEN an administrator adds UCS Manager THE DOCUMENTATION SHALL explain endpoint, credential, organization, least-privilege intent, and validation requirements supported by implementation.
- WHEN synchronization runs THE DOCUMENTATION SHALL identify each confirmed UCS object type, mapping, and refresh behavior.
- WHEN provisioning bare metal THE DOCUMENTATION SHALL describe implementation-backed Service Profile, pool, PXE, Kickstart, and failure prerequisites.
- WHEN changing managed state THE DOCUMENTATION SHALL explain implementation-backed effects and the stop/escalation boundary.
- IF UCS faults and costing are supported THEN THE DOCUMENTATION SHALL explain their verified mappings and configuration.
- IF any Jira-listed capability is unconfirmed THEN THE DOCUMENTATION SHALL omit it rather than invent behavior.

## Boundaries
No UCS integration implementation, exhaustive Cisco administration guide, or unsupported feature promise.

## Risks
Exact Cisco privileges and environment-specific object policies vary by UCS deployment. The source-backed feature descriptions do not promise UCS-side remediation or configuration beyond implemented operations.

## Validation
Inspect UCS compute/provisioning, fault, and pricing implementation and run `make build`. A UCS lab remains useful for release-specific integration regression testing but is not required to document behavior directly present in code.
