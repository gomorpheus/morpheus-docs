---
title: "Documentation Update Request — Docker Host Disk Prerequisite"
slug: docs-morph-7251-docker-host-disks
type: feature
status: completed
horizon: now
size: small
tags: [documentation, docker, clusters, storage, prerequisites]
tracker_id: MORPH-7251
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T18:00:00Z
---
# Documentation Update Request — Docker Host Disk Prerequisite

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-7251

> When deploying a Docker cluster in Morpheus, Docker hosts require two disks: one for the operating system and one dedicated disk for Docker data storage.
>
> This requirement applies both when creating new Docker hosts from Morpheus and adding an existing VM as a Docker host. If only a single disk is present or selected, the deployment may fail. Currently, this prerequisite is not documented.

## Goal
State the product-confirmed disk prerequisite before every supported Docker-host onboarding path and explain how users verify the OS and Docker-data disks before deployment.

## Kickoff
Audit `infrastructure/clusters/docker.rst`, `integration_guides/Clouds/vmware/docker.rst`, `integration_guides/Clouds/openstack/docker.rst`, and `infrastructure/hosts/hosts.rst`. Confirm with the Containers owner whether two disks are mandatory for every current layout and cloud, what minimum properties apply to the data disk, and how imported hosts are validated. Do not convert the Jira report into a universal requirement without that confirmation. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions.

## Approach
Put the canonical prerequisite in the Docker cluster page and add concise cloud-guide cross-references.

## Changes
1. `infrastructure/clusters/docker.rst` — Corrected the Jira premise: a data volume is configurable but a dedicated second disk is not universal.
2. `integration_guides/Clouds/vmware/docker.rst` and `integration_guides/Clouds/openstack/docker.rst` — Added layout-scoped volume guidance.
3. `infrastructure/hosts/hosts.rst` — Audited but unchanged because imported-host disk validation was not proven.

## Delivery Evidence

Current layouts expose configurable volume definitions but do not impose a universal second-disk prerequisite. The documentation explicitly corrects the Jira premise and scopes volume configuration to the selected layout and Cloud without inventing one-disk failure behavior.

## Acceptance Criteria
- WHEN a user provisions a Docker host THE DOCUMENTATION SHALL state that volume requirements come from the selected layout, Cloud, and storage design.
- THE DOCUMENTATION SHALL explicitly correct the claim that every Docker host requires a dedicated second disk.
- THE DOCUMENTATION SHALL NOT claim a one-disk failure or existing-host disk validation behavior that is not present in implementation evidence.

## Boundaries
No Docker layout change, storage automation, or unsupported sizing values.

## Risks
The universal second-disk premise is contradicted by current layout behavior. Existing-host validation remains outside the published claim because no implementation evidence established it.

## Validation
Inspect Docker layout volume definitions and run `make build`. Live new-host and existing-host runs are optional future provider-specific validation.
