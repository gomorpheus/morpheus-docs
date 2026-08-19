---
title: "3-Node HA Transactional Tier Discrepancy Between Docs"
slug: docs-morph-3220-ha-transactional-tier-alignment
type: feature
status: completed
horizon: now
size: small
tags: [documentation, architecture, high-availability, mysql]
tracker_id: MORPH-3220
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:02:52Z
---
# 3-Node HA Transactional Tier Discrepancy Between Docs

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-3220

Jira description (verbatim):

> Looking at our current public docs (and 6.0.0 docs are similar), it has stated:
>
> **3-Node HA (Recommended)**
>
> In this architecture, all tiers are deployed on three machines by HPE Morpheus Enterprise during the installation, with the exception of the Transactional Database Tier. This provides HA not just for the HPE Morpheus Enterprise Application Tier but all underlying tiers that support HPE Morpheus Enterprise. The Transactional Database Tier will remain external, either as a separate cluster or PaaS, following the supported services. An external MySQL cluster must still be set up outside of the HPE Morpheus Enterprise app nodes.
>
> However, a customer is working off a provided Morpheus Reference Architecture 8.0.x pdf and it mentions:
>
> ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=acf17d5f-cf93-463a-a165-daf6177d1983&&collection=&height=1273&occurrenceKey=null&width=1038&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
> All customers I've worked with, we've only pushed for external only and not having the DB co-located on the applications nodes. My opinion is we should align enforce external only, not make it optional as that has been the standard for customer implementations.

The current repository already requires external MySQL for 3-Node HA in `getting_started/installation/distributed/overview.rst` and `getting_started/maintenance/upgrades/3node/overview.rst`.

## Goal

Align all in-repository 3-Node HA architecture statements with the product-approved transactional database topology and explicitly address obsolete external reference material.

## Kickoff

Reconcile 3-Node HA transactional-database guidance with the approved architecture and remove contradictory local wording.

**Status:** planning — current RST says external MySQL; the Jira screenshot and referenced PDF are unavailable.

**Pick up at:** obtain architecture-owner confirmation and the 8.0.x PDF passage before changing authoritative wording.

→ `.hero/planning/features/docs-morph-3220-ha-transactional-tier-alignment/spec.md`

**Files:** `getting_started/installation/distributed/overview.rst`, `getting_started/installation/overview.rst`, `getting_started/maintenance/upgrades/3node/overview.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Use the distributed installation architecture as canonical, then search and align all local 3-Node HA descriptions. Add version context only if architecture owners confirm historical differences.

## Changes

1. `getting_started/installation/distributed/overview.rst` — Made the proven current topology explicit: three application nodes use one external MySQL service.
2. `getting_started/installation/overview.rst` — Aligned installation architecture wording with the canonical external transactional tier.
3. `getting_started/maintenance/upgrades/3node/overview.rst` — Aligned upgrade guidance and warned against co-locating MySQL during upgrade.

## Acceptance Criteria

- THE DOCUMENTATION SHALL state one approved transactional-database topology for current 3-Node HA deployments.
- WHEN older releases differ THE DOCUMENTATION SHALL scope the difference by version and source.
- THE DOCUMENTATION SHALL base the required external transactional tier on the proven appliance 3-node external-DB configuration rather than the reporter's opinion or inaccessible PDF.

## Boundaries

No editing of the external PDF, database deployment tutorial, or architecture product change.

## Risks

- **Blocker:** The Jira image attachment is a non-resolvable blob URL and the cited PDF content is unavailable.
- The reporter's recommendation is not an approved product architecture decision.

## Validation

Obtain architecture sign-off, search for all 3-Node HA transactional-tier statements, run `make build`, and compare rendered pages for identical policy.
