---
title: "Docs: Update MySQL support to 8.4.x LTS or greater"
slug: docs-morph-11394-mysql-84-support
type: feature
status: completed
horizon: now
size: small
tags: [documentation, mysql, compatibility, installation]
tracker_id: MORPH-11394
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T18:00:00Z
---
# Docs: Update MySQL support to 8.4.x LTS or greater

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-11394; source epic: https://hpe.atlassian.net/browse/MORPH-7290

The request updates embedded MySQL to 8.4.x LTS and supported non-embedded MySQL to 8.4.x or greater.

## Goal
Align installation, external-service, and compatibility guidance with the released MySQL 8.4 support contract.

## Kickoff
Deliver `.hero/planning/features/docs-morph-11394-mysql-84-support/spec.md`; update `getting_started/external_services/mysql.rst`, `getting_started/installation/database_configure_generic.rst`, and `release_notes/compatibility_table.rst`.

## Approach
Confirm the exact minimum/maximum and “or greater” policy from MORPH-7290 and QA; distinguish embedded package version from external DB compatibility.

## Changes
1. `getting_started/external_services/mysql.rst` — Documented embedded MySQL 8.4.8 and bounded external 8.4 configuration claims by formal release certification.
2. `getting_started/installation/database_configure_generic.rst` and `getting_started/installation/3_node_ha/3_node_ha_database_requirements.rst` — Reconciled external database prerequisites without claiming blanket certification.
3. `release_notes/compatibility_table.rst` and `release_notes/9_0_0.rst` — Recorded embedded 8.4.8 and corrected the previous “or above” wording.

## Delivery Evidence

The appliance source establishes embedded MySQL 8.4.8 in `config/versions.rb` and the SBOM. External MySQL configuration is implemented, but formal certification remains release- and service-variant-specific.

## Acceptance Criteria
- WHEN users select an external MySQL service THE SYSTEM SHALL state that the 8.4 LTS family is configurable while directing users to release-specific formal certification rather than inventing an exact external range.
- WHEN users inspect embedded dependencies THE SYSTEM SHALL state that |morpheus| 9.0.0 ships embedded MySQL 8.4.8.
- IF “or greater” is not an unconditional support policy THEN THE SYSTEM SHALL publish the verified bounded range instead.

## Boundaries
No database migration procedure beyond cross-linking existing guidance.

## Risks
An open-ended “or greater” claim may exceed tested compatibility.

## Validation
Verify release notes and Connector/J application evidence, search for directly affected stale support wording, and run `make build`.
