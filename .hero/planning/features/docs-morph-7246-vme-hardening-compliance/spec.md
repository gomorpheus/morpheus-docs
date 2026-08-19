---
title: "Platform Hardening with Industry Standards (CIS / STIG) and Integrated Firewall for HPE VM Essentials"
slug: docs-morph-7246-vme-hardening-compliance
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, vme, security, hardening, cis, stig]
tracker_id: MORPH-7246
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:12:41Z
---
# Platform Hardening with Industry Standards (CIS / STIG) and Integrated Firewall for HPE VM Essentials

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-7246

Jira requests CIS/STIG profiles, automated validation and reporting, integrated firewall management, and hardening controls for VME Manager and HVM Hosts. Those are primarily product-feature requests. Existing documentation in `getting_started/installation/hardening.rst` must be audited, but documentation cannot claim unavailable capabilities.

## Goal
Accurately document current, product-confirmed VME Manager and HVM Host hardening capabilities, clearly identify externally managed controls and unsupported compliance claims, and avoid presenting requested future functionality as shipped.

## Kickoff
Audit `getting_started/installation/hardening.rst`, `getting_started/requirements/requirements.rst`, `infrastructure/clusters/hvm/building_clusters.rst`, and `administration/logging/audit_logging.rst`. Obtain Security/Product confirmation for any CIS, STIG, FIPS, Secure Boot, firewall, reporting, API, remediation, or validation claim. If requested dashboards, profiles, scripts, or centralized firewall controls are not shipped, document only current guidance and route feature requests outside this documentation spec. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions.

## Approach
Perform a gap audit against current capabilities. Expand existing security guidance only with approved facts and explicitly separate customer responsibility from platform controls.

## Changes
1. Audit and correct `getting_started/installation/hardening.rst` for current Manager controls and compliance positioning.
2. Add confirmed HVM Host hardening guidance to `infrastructure/clusters/hvm/building_clusters.rst` or cross-link to an approved canonical security page.
3. Align required communications in `getting_started/requirements/requirements.rst` and audit evidence in `administration/logging/audit_logging.rst`.

## Acceptance Criteria
- THE DOCUMENTATION SHALL distinguish documented security capabilities from certification claims and customer-managed CIS, STIG, FIPS, firewall, and compliance controls.
- IF a requested capability is not shipped THEN THE DOCUMENTATION SHALL not describe it as available.
- WHEN hardening guidance changes connectivity THE DOCUMENTATION SHALL identify required communications and rollback considerations.
- IF no approved benchmark/version artifact is bundled THEN THE DOCUMENTATION SHALL make no compliance alignment or certification claim.

## Boundaries
No implementation of dashboards, scripts, APIs, profiles, firewall orchestration, or compliance certification.

## Risks
Security misstatement creates compliance risk. Delivery is blocked pending Security and Product confirmation; Jira’s desired behavior is not evidence of current functionality.

## Validation
Security review every claim, build affected pages, test links, and verify terminology against current release capabilities.
