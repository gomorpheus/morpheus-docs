---
title: "Need doc on how to remove hosts from HVM cluster"
slug: docs-morph-7772-remove-hvm-host
type: feature
status: completed
horizon: now
size: small
tags: [documentation, hvm, clusters, hosts, audit]
tracker_id: MORPH-7772
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:49:50Z
---
# Need doc on how to remove hosts from HVM cluster

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-7772

> We have a doc on how to add hosts ... but none that go over how to remove a host.

The repository now contains a detailed removal procedure in `infrastructure/clusters/hvm/managing_hosts.rst`. This issue is therefore an audit, correction, and discoverability task rather than new duplicate content.

## Goal
Verify the existing HVM host-removal procedure against the current product, correct gaps, and make it discoverable from host-addition, maintenance, alarm, and troubleshooting paths.

## Kickoff
Audit `infrastructure/clusters/hvm/managing_hosts.rst` against a current supported cluster layout and UI. Cross-check `infrastructure/clusters/hvm/host_maintenance.rst`, `infrastructure/clusters/hvm/alarms.rst`, `infrastructure/clusters/hvm/troubleshooting.rst`, and the HVM toctree in `infrastructure/clusters/hvm/hvm.rst`. Preserve the existing procedure; do not add direct-host commands unless HVM Engineering explicitly approves them. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions. Validate both healthy and failed-host paths.

## Approach
Treat `managing_hosts.rst` as canonical, validate clean and failed-host paths, and add targeted cross-links.

## Changes
1. Audit and correct removal prerequisites, UI steps, evacuation, quorum, datastore, and post-removal checks in `managing_hosts.rst`.
2. Add relevant cross-links from `host_maintenance.rst`, `alarms.rst`, and `troubleshooting.rst`.
3. Verify `hvm.rst` navigation makes host management discoverable.

## Acceptance Criteria
- WHEN a user removes a healthy HVM host THE DOCUMENTATION SHALL provide the verified supported procedure and preflight checks.
- WHEN a host is failed or unreachable THE DOCUMENTATION SHALL provide the separately approved path or direct the user to Support.
- THE DOCUMENTATION SHALL explain verified VM, quorum, datastore, and network consequences.
- IF existing instructions are already correct THEN THE DOCUMENTATION SHALL retain them and improve discoverability rather than duplicate them.

## Boundaries
No unsupported shell workaround or product workflow change.

## Risks
Destructive guidance can cause outage or data loss. Delivery is blocked until HVM Engineering validates both healthy and failed-host paths.

## Validation
Exercise approved paths in a disposable cluster, verify resulting cluster health and resources, build docs, and obtain HVM owner sign-off.
