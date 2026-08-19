---
title: "Brownfield adoption - How to Comparison"
slug: docs-morph-6004-vmware-vme-comparison
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, vme, vmware, brownfield, adoption]
tracker_id: MORPH-6004
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:12:19Z
---
# Brownfield adoption - How to Comparison

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-6004

Jira description (verbatim):

> This product is heavily marketed to Brownfield users of VMWare. Those Users know how to accomplish specific actions in a VMware environment, but not in ours. A guide showing equivalent steps to accomplish common tasks in VME that they accomplished in VMWare would be helpful. Basically, one page would show how they did something in VMWare, the next page would show how to accomplish the same thing in VME.

Existing VMware and brownfield material includes `integration_guides/Clouds/vmware/vmware.rst`, `getting_started/guides/vmware_guide.rst`, and `provisioning/concepts/concepts.rst`. Jira does not define the comparison task set.

## Goal

Create a task-oriented VMware-to-VME comparison guide for an approved set of common brownfield operations, mapping concepts, navigation, prerequisites, semantic differences, and links to canonical VME procedures.

## Kickoff

Create a focused VMware-to-VME task comparison for brownfield adopters using approved high-value operations.

**Status:** planning — relevant VMware and VME pages exist; the comparison task list needs product approval.

**Pick up at:** agree on 8–12 common operations and map each to current canonical VME documentation before drafting.

→ `.hero/planning/features/docs-morph-6004-vmware-vme-comparison/spec.md`

**Files:** `integration_guides/Clouds/vmware/vmware.rst`, `getting_started/guides/vmware_guide.rst`, `provisioning/concepts/concepts.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Add one concise comparison page organized by user intent, not a page pair per task. Link to canonical procedures and call out where VMware and VME concepts are not equivalent.

## Changes

1. Add `getting_started/guides/vmware_to_vme.rst` with the approved comparison table and task links.
2. Update `getting_started/getting_started.rst` to expose the guide in the existing guides toctree.
3. Add a discoverability link from `integration_guides/Clouds/vmware/vmware.rst`.
4. Link brownfield terminology to `provisioning/concepts/concepts.rst` rather than restating it.

## Acceptance Criteria

- WHEN a VMware administrator looks up an approved common task THE DOCUMENTATION SHALL identify the equivalent VME concept, navigation, prerequisites, and canonical procedure.
- IF no direct equivalent exists THEN THE DOCUMENTATION SHALL explain the semantic difference rather than force a misleading mapping.
- THE DOCUMENTATION SHALL use current VMware terminology and preserve VME as the procedural source of truth.

## Boundaries

No exhaustive VMware manual, feature parity claim, migration-tool procedure, or task set not approved for this first guide.

## Risks

- **Blocker:** Jira does not identify which “common tasks” belong in scope.
- One-to-one mappings can misrepresent lifecycle, inventory, and policy differences.

## Validation

Have VMware and VME SMEs approve the task list and mappings, follow every VME link, run `make build`, and conduct a brownfield-user walkthrough.
