---
title: "Docs: Multi-session Management (8-node SVT)"
slug: docs-morph-11396-simplivity-multi-session
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, simplivity, multi-session, clusters]
tracker_id: MORPH-11396
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:12:41Z
---
# Docs: Multi-session Management (8-node SVT)

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-11396; source epic: https://hpe.atlassian.net/browse/MORPH-7212

Documentation must cover multi-session management requirements and behavior for eight-node SimpliVity clusters as defined by MORPH-7212. Those details are not included in this Jira payload.

## Goal
Document the verified configuration, lifecycle behavior, limits, and recovery expectations for multi-session management on an eight-node SimpliVity cluster.

## Kickoff
Deliver `.hero/planning/features/docs-morph-11396-simplivity-multi-session/spec.md`; ingest MORPH-7212 requirements, then locate/update the canonical SimpliVity integration source under `integration_guides/`.

## Approach
Treat the epic as authoritative, inventory existing SimpliVity docs before choosing exact files, and separate prerequisites, procedure, observable states, and limitations.

## Changes
1. Extract supported topology, session limits, sequencing, permissions, failure handling, and UI paths from MORPH-7212 acceptance evidence.
2. Locate the canonical SimpliVity guide under `integration_guides/` and add an eight-node multi-session section; update its toctree only if a new page is justified.
3. Add cross-references from relevant cluster lifecycle pages after exact source discovery.

## Acceptance Criteria
- IF no SimpliVity integration or eight-node acceptance evidence is bundled THEN THE DOCUMENTATION SHALL make no multi-session support claim.
- THE DOCUMENTATION SHALL identify VMware vCenter management and SimpliVity lifecycle management as separate integration boundaries.
- THE DOCUMENTATION SHALL direct readers to HPE for the current eight-node and multi-session interoperability statement.

## Boundaries
No SimpliVity implementation changes or support for topologies absent from MORPH-7212.

## Risks
The target file and product contract cannot be finalized from this Jira alone.

## Validation
Epic/engineering review, end-to-end workflow check on an eight-node SVT, build/link validation, and `make test`.
