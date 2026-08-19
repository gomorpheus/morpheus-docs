---
title: "Outline different networking scenarios"
slug: docs-morph-8152-hvm-networking-scenarios
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, hvm, networking, bonds, vlans, lacp]
tracker_id: MORPH-8152
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:49:50Z
---
# Outline different networking scenarios

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-8152

> The documentation example assumes a simple active-backup bond, trunk ports, and host-tagged VLANs. The networking team could provide LACP bonds instead, making the example hard to follow. The request is to outline different networking scenarios because many users do not understand the options.

Current `infrastructure/clusters/hvm/virtual_switches.rst` already covers Active-Backup and LACP/Balance RR, prerequisites, examples, and troubleshooting. This work should turn that coverage into a deployment decision aid and correct gaps.

## Goal
Provide a product-approved decision path for common HVM deployment networking scenarios, mapping switch-port mode, bond mode, VLAN tagging location, interface roles, prerequisites, and validation to the existing procedures.

## Kickoff
Audit `getting_started/installation/hvm_host_prep.rst`, `infrastructure/clusters/hvm/virtual_switches.rst`, `hvm_networks.rst`, and `building_clusters.rst`. Confirm supported combinations and terminology with HVM Networking, especially whether “Balance RR (LACP)” maps exactly to 802.3ad and which access/trunk and tagged/untagged combinations are valid. Coordinate novice-flow changes with MORPH-7934; do not invent topology recipes. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions.

## Approach
Add a scenario selection matrix near installation prerequisites and keep detailed configuration in the existing virtual-switch/network pages.

## Changes
1. Add a scenario decision table and information checklist to `getting_started/installation/hvm_host_prep.rst`.
2. Audit and correct Active-Backup/LACP, access/trunk, and VLAN-tagging procedures in `infrastructure/clusters/hvm/virtual_switches.rst`.
3. Align network-object terminology in `hvm_networks.rst` and deployment cross-links in `building_clusters.rst`.

## Acceptance Criteria
- WHEN a reader selects a networking scenario THE DOCUMENTATION SHALL map supported bond, switch-port, VLAN-tagging, and interface-role choices.
- WHEN LACP is selected THE DOCUMENTATION SHALL state verified host and upstream-switch prerequisites and validation.
- IF a topology is unsupported or unverified THEN THE DOCUMENTATION SHALL not provide a recipe for it.
- THE DOCUMENTATION SHALL distinguish illustrative values from customer-specific network values.
- THE DOCUMENTATION SHALL reuse detailed existing procedures rather than duplicate them.

## Boundaries
No customer network design, switch-vendor configuration guide, or product networking change.

## Risks
Terminology may not match implementation. Delivery is blocked until Networking confirms the supported scenario matrix and LACP semantics.

## Validation
Exercise each approved scenario in a lab, validate host and VM connectivity/failover, build pages, and run novice review with Networking sign-off.
