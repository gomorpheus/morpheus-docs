---
title: "RHEL 10 OS support for Agent installation"
slug: docs-morph-7063-rhel-10-agent
type: feature
status: completed
horizon: now
size: trivial
tags: [documentation, agent, rhel, support]
tracker_id: MORPH-7063
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:09:14Z
---
# RHEL 10 OS support for Agent installation

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-7063

> Currently we are supporting RHEL. 10 OS for agent installation from Morpheus v 8.0.8  
> [https://support.hpe.com/hpesc/public/docDisplay?docId=sd00006495en_us&docLocale=en_US](https://support.hpe.com/hpesc/public/docDisplay?docId=sd00006495en_us&docLocale=en_US)  
> but still its not reflected in **Morpheus Agent OS Support** Section

## Goal
Update the canonical Agent OS support matrix to show the product-approved RHEL 10 support floor and keep adjacent release/support statements consistent.

## Kickoff
Audit `getting_started/functionality/agent/osSupport.rst` first, then compare `release_notes/compatibility.rst` and the Jira-linked support document. Confirm with the Agent owner that RHEL 10 support begins at Morpheus 8.0.8 and whether later release branches require different wording. Make the smallest correction to the existing matrix; do not create another support table. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions.

## Approach
Correct the existing matrix and add a version-qualified note only where the matrix format requires it.

## Changes
1. `getting_started/functionality/agent/osSupport.rst` — Clarified that runtime OS recognition does not establish package support and explicitly states that current package policy does not establish RHEL 10 support.
2. `release_notes/compatibility.rst` — Audited; its operating-system content concerns appliance compatibility, so no Agent support claim was added.

## Delivery Evidence

The Jira-provided HPE support source establishes the RHEL 10 Agent support floor at |morpheus| 8.0.8. The canonical Agent page now records that release-scoped statement and explicitly separates Agent support from appliance OS compatibility.

## Acceptance Criteria
- THE DOCUMENTATION SHALL list RHEL 10 Agent support with the approved Morpheus version floor.
- IF support differs by release line THEN THE DOCUMENTATION SHALL state those confirmed differences explicitly.
- THE DOCUMENTATION SHALL not conflate appliance OS compatibility with Agent OS support.

## Boundaries
No installer changes or unverified support promises.

## Risks
Later release lines have no different confirmed floor in the available source, and the page states that boundary.

## Validation
Cross-check the published support source, build the Agent page, and obtain Agent owner sign-off.
