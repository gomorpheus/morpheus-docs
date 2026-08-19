---
title: "Documentation Request: Firewall and Storage - Multipathing Configuration for HVM Clusters"
slug: docs-morph-6012-hvm-firewall-multipathing
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, hvm, firewall, multipath, storage, gfs2]
tracker_id: MORPH-6012
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:49:50Z
---
# Documentation Request: Firewall and Storage - Multipathing Configuration for HVM Clusters

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-6012

Jira description (verbatim):

> **Firewall:**
>
> During hypervisor installation, iptables firewall rules are automatically added at the OS level, even when UFW is enabled. If additional firewall rules are not explicitly configured and UFW is subsequently disabled, clusters using GFS2 Pool Data Stores may start without quorum, potentially resulting in split‑brain conditions following a node reboot.
>
> Please provide documentation or recommended best practices clearly define expected firewall behavior and required rules to ensure cluster quorum and stability for firewall configuration (iptables and/or UFW) for both:
>
> * Vanilla Ubuntu installation
> * HVM Custom ISO–based installations
>
> **Storage:**
>
> For environments using shared storage, such as Fibre Channel (FC)–connected block storage, there is currently no official documentation describing how multipathing should be configured.
>
> Please provide documentation or best practices for multipathing configuration in HVM environments, including supported configurations and recommended OS‑level setup for enterprise shared storage.

Current HVM storage documentation already covers multipath and WWN paths in `storage_operations.rst` and iSCSI constraints in `virtual_switches.rst`; firewall/quorum claims require validation.

## Goal

Publish source-backed HVM multipathing guidance and honestly bound the firewall request: firewall policy and installed rules are host/installer-specific, and manager code does not establish one universal Ubuntu/Custom ISO ruleset or the Jira split-brain outcome.

## Kickoff

Reconcile existing HVM multipath coverage and state the verified ownership boundary for Ubuntu and Custom ISO host firewalls.

**Status:** planning — product source establishes layout 2.0 multipath inspection; it does not establish a universal host firewall contract.

**Pick up at:** verify multipath commands against product source, document the firewall ownership boundary, and build the docs.

→ `.hero/planning/features/docs-morph-6012-hvm-firewall-multipathing/spec.md`

**Files:** `infrastructure/clusters/hvm/storage_operations.rst`, `infrastructure/clusters/hvm/virtual_switches.rst`, `infrastructure/clusters/hvm/troubleshooting.rst`, `getting_started/installation/hvm_host_prep.rst`
**Guardrail:** Verify product behavior; do not turn Jira observations into unsupported documentation claims.

## Approach

Extend canonical storage operations where current multipath coverage lacks read-only preflight detail. In host prep, state that deployed firewall rules must be validated on the actual host and installer release; do not infer ports or failure outcomes from manager code.

## Changes

1. Update `getting_started/installation/hvm_host_prep.rst` with the verified firewall ownership and validation boundary for vanilla Ubuntu and Custom ISO installation.
2. Update `infrastructure/clusters/hvm/storage_operations.rst` with supported FC/iSCSI multipath configuration, verification, and WWN naming where gaps remain.
3. Align `infrastructure/clusters/hvm/virtual_switches.rst` with the canonical multipath procedure.
4. Update `infrastructure/clusters/hvm/troubleshooting.rst` with verified quorum/firewall and multipath diagnostics.

## Acceptance Criteria

- WHEN an HVM host is installed from vanilla Ubuntu or Custom ISO THE DOCUMENTATION SHALL state that firewall behavior and required rules are host/installer-release-specific, are not established by manager code, and must be validated against the deployed host and network policy.
- WHEN FC or iSCSI shared storage is used THE DOCUMENTATION SHALL identify supported multipath setup, stable device naming, health checks, and failure expectations.
- IF the Jira split-brain assertion is not reproduced or approved THEN THE DOCUMENTATION SHALL not state it as a guaranteed outcome.
- THE DOCUMENTATION SHALL preserve existing WWN-based and iSCSI single-NIC guidance unless engineering supersedes it.

## Boundaries

No firewall implementation changes, storage-array vendor setup, unsupported UFW/iptables coexistence recipe, or new support policy.

## Risks

- **Blocker:** Installer firewall behavior, exact ports, and split-brain mechanism require HVM engineering validation.
- Existing multipath documentation may already supersede part of the Jira gap; avoid contradictory duplication.

## Validation

Compare the multipath commands with `HvmcliStorage` and its command-construction tests in product source, confirm no universal firewall or split-brain claim is made, and run `make build`. Host/installer firewall certification remains an installer-release validation responsibility rather than a manager documentation claim.
