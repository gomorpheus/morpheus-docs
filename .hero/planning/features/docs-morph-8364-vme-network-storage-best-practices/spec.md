---
title: "Improve HPE VME Documentation for Network and Storage Setup – Add Best Practice Guidelines"
slug: docs-morph-8364-vme-network-storage-best-practices
type: feature
status: completed
horizon: now
size: large
tags: [documentation, vme, networking, storage]
tracker_id: MORPH-8364
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:12:41Z
---

# Improve HPE VME Documentation for Network and Storage Setup – Add Best Practice Guidelines

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-8364

Exact Jira description (delivery source requirement):

> Customers have reported that the current documentation for **HPE VME network and storage setup** is vague and assumes prior knowledge of the architecture. Several configuration steps are not explicitly documented, and recommended best practices are missing. As a result, customers are required to make configuration decisions without clear guidance from official documentation.
>
> The current documentation primarily explains the configuration workflow but does not provide sufficient detail on recommended network topology, storage configuration methods, or deployment best practices.

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-8364 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-8364-vme-network-storage-best-practices/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `getting_started/installation/hvm_host_prep.rst`
- `infrastructure/clusters/hvm/hvm_networks.rst`
- `infrastructure/clusters/hvm/virtual_switches.rst`
- `infrastructure/clusters/hvm/storage_operations.rst`
- `infrastructure/clusters/hvm/capacity_planning.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Add an architecture-first best-practices layer to the existing setup procedures: supported topology choices, decision points, prerequisites, cross-links, and verification without duplicating procedures.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. Update `getting_started/installation/hvm_host_prep.rst` to carry the primary procedure and verified guidance.
2. Update `infrastructure/clusters/hvm/hvm_networks.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.
3. Update `infrastructure/clusters/hvm/virtual_switches.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.
4. Update `infrastructure/clusters/hvm/storage_operations.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.
5. Update `infrastructure/clusters/hvm/capacity_planning.rst` to align supporting context, terminology, navigation, and cross-references without duplicating the primary procedure.

## Acceptance Criteria

- WHEN a reader designs HVM network and storage connectivity THE DOCUMENTATION SHALL state the verified prerequisites, design decisions, validation steps, and customer-owned physical infrastructure boundaries.
- IF a reported behavior cannot be reproduced or confirmed THEN THE DOCUMENTATION SHALL omit it or label the supported limitation using approved product wording
- THE DOCUMENTATION SHALL use current repository navigation, terminology, formatting, and cross-references across every changed file
- THE DOCUMENTATION SHALL preserve the Jira-requested correction while avoiding unsupported timing, compatibility, security, or operational guarantees
- WHEN the documentation build and link checks run THE SYSTEM SHALL complete without new warnings or broken internal references caused by these changes

## Boundaries

- Do not change product code, API behavior, UI behavior, or release support policy.
- Do not broaden this issue into a general rewrite of adjacent documentation.
- Do not add inaccessible Jira media to the repository or reconstruct screenshots from descriptions.
- Do not publish commands, defaults, compatibility claims, or destructive operations until an authoritative owner verifies them.

## Risks

- Product and networking/storage SMEs must approve recommendations; the Jira report identifies gaps but supplies no authoritative best-practice matrix.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
