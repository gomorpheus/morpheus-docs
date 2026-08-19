---
title: "Maximums Guide for HPE VM Essentials (Hosts, VMs, Clusters, Datastores, Resources)"
slug: docs-morph-7243-vme-maximums-guide
type: feature
status: completed
horizon: now
size: large
tags: [documentation, vme, maximums, scalability, capacity]
tracker_id: MORPH-7243
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:12:41Z
---
# Maximums Guide for HPE VM Essentials (Hosts, VMs, Clusters, Datastores, Resources)

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-7243

> There is currently no consolidated **Maximums Guide** for HPE VM Essentials that defines supported scalability and configuration limits.
>
> Enterprise customers require clear documentation of **platform limits** in order to:
>
> * Design and size environments properly
> * Plan capacity and scalability
> * Validate migration feasibility
> * Avoid unsupported configurations
>
> Without this guide, architecture planning is based on assumptions or trial-and-error testing.  
>   
> Provide an official **HPE VME Maximums Guide** covering at minimum:  
>
> **Host Limits**
>
> * Maximum physical CPUs per host
> * Maximum number of VMs per host
> * Maximum live migrations per host
>
> ‌
>
> ### **Cluster Limits**
>
> * Maximum number of hosts per cluster
> * Maximum number of VMs per cluster
> * Maximum number of datastores per cluster
> * HA / Dynamic Placement limits
>
> ### **VM Limits**
>
> * Maximum vCPUs per VM
> * Maximum memory per VM
> * Maximum number of disks per VM
> * Maximum disk size per virtual disk
> * Maximum total disk capacity per VM
> * Maximum number of vNICs per VM
> * Maximum network throughput (if applicable)
> * Limits for:
>
>     * BIOS vs UEFI
>     * TPM
>     * Nested Virtualization
>     
>
> ### **Storage Limits**
>
> * Maximum datastore size
> * Maximum number of datastores per cluster
> * Maximum disks per datastore
>
> ### **Networking Limits**
>
> * Maximum networks per cluster
> * Maximum vNICs per VM
>
> ### **Migration Limits**
>
> * Maximum VM size for live migration
>
> ### **API & Management Limits**
>
> * Maximum managed hosts per VME Manager
> * Maximum objects supported
> * UI scalability expectations

## Goal
Add a consolidated, versioned VME maximums reference containing only validated limits, with qualifiers and links from existing capacity and installation guidance.

## Kickoff
First obtain the official maximums artifact and named owners for host, cluster, VM, storage, networking, migration, and manager limits. Audit `infrastructure/clusters/hvm/capacity_planning.rst`, `infrastructure/clusters/hvm/vm_compute.rst`, `infrastructure/clusters/hvm/storage_operations.rst`, `infrastructure/clusters/hvm/vm_migration.rst`, and `getting_started/installation/singleNode/hpe_installer.rst`. Never derive supported maxima from UI ranges, defaults, or lab observations. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions. Verify navigation and version scope too.

## Approach
Create one canonical reference only after values are approved, then replace scattered numeric claims with links or aligned values.

## Changes
1. Add `infrastructure/clusters/hvm/maximums.rst` containing versioned tables, definitions, qualifiers, and source ownership for approved limits.
2. Add the page to `infrastructure/clusters/hvm/hvm.rst`.
3. Audit and align numeric claims in `capacity_planning.rst`, `vm_compute.rst`, `storage_operations.rst`, `vm_migration.rst`, and `getting_started/installation/singleNode/hpe_installer.rst`.

## Acceptance Criteria
- THE DOCUMENTATION SHALL provide one canonical, version-scoped VME maximums reference.
- THE DOCUMENTATION SHALL distinguish hard supported limits, tested limits, recommendations, and values that are not applicable.
- IF an official value is unavailable THEN THE DOCUMENTATION SHALL state "Not published; contact HPE" rather than invent a number.
- WHEN another page mentions a maximum THE DOCUMENTATION SHALL align it with or link to the canonical guide.

## Boundaries
No new product limits, sizing calculator, benchmark claims, or unsupported extrapolation.

## Risks
This is `large` and cross-domain. Delivery is blocked until Product/Engineering supplies an approved maximums source for each published value.

## Validation
Require per-domain owner sign-off, compare all repository numeric claims, build tables and links, and verify version qualifiers.
