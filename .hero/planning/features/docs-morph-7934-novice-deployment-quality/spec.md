---
title: "Novice Quality Test"
slug: docs-morph-7934-novice-deployment-quality
type: feature
status: completed
horizon: now
size: large
tags: [documentation, vme, installation, networking, troubleshooting, usability]
tracker_id: MORPH-7934
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:12:19Z
---
# Novice Quality Test

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-7934

The reporter followed the HVM OS installation guide in a lab, found the active-backup/trunk/tagged-VLAN assumptions hard to translate to a different network, experienced very slow steps and a checksum/unknown-error failure at installation step 8, and found no troubleshooting guidance. The Jira description includes environment-specific observations and an external community thread, not confirmed root causes.

## Goal
Make the HVM OS deployment path usable by a novice through explicit assumptions, decision points, expected timing guidance where measurable, and product-approved troubleshooting for checksum and installer failures.

## Kickoff
Audit `getting_started/installation/hvm_host_prep.rst`, `infrastructure/clusters/hvm/building_clusters.rst`, `infrastructure/clusters/hvm/virtual_switches.rst`, and `infrastructure/clusters/hvm/troubleshooting.rst`. Reproduce the documented flow in a controlled supported environment and obtain the reporter’s exact release/media/environment details. Separate documentation ambiguity from lab networking, remote-console performance, media integrity, and product defects; do not present community workarounds as supported. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions.

## Approach
Improve the existing deployment journey with preflight checks, network-scenario links, expected-state checkpoints, and evidence-backed troubleshooting.

## Changes
1. Clarify assumptions and preflight validation in `getting_started/installation/hvm_host_prep.rst`.
2. Add novice-oriented checkpoints and verified expected durations/ranges, if approved, to `infrastructure/clusters/hvm/building_clusters.rst`.
3. Cross-link network choices in `virtual_switches.rst` and add approved checksum/install-failure diagnostics to `troubleshooting.rst`.
4. Coordinate overlapping networking scope with MORPH-8152 rather than duplicating scenario content.

## Acceptance Criteria
- BEFORE installation THE DOCUMENTATION SHALL make topology, bond, switch-port, VLAN, media, and disk assumptions explicit.
- WHEN a reader’s network differs THE DOCUMENTATION SHALL route them to supported scenario guidance rather than imply example values are universal.
- IF checksum or unknown installer errors occur THEN THE DOCUMENTATION SHALL provide approved evidence collection, remediation, and escalation steps.
- IF timing guidance is published THEN THE DOCUMENTATION SHALL state tested conditions and avoid guarantees.
- THE DOCUMENTATION SHALL not publish community disk-wipe advice without Engineering approval.

## Boundaries
No installer performance fix, lab-network redesign, unsupported workaround, or duplication of MORPH-8152.

## Risks
This is `large`. Root causes and expected timings are unconfirmed; delivery is blocked pending reproducible environment details and Installer/Networking review.

## Validation
Run novice usability validation end to end, test failure guidance, build all touched pages, and obtain reviewer and product-owner sign-off.
