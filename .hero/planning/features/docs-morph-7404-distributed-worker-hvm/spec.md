---
title: "Add HVM as a supported cloud for DW"
slug: docs-morph-7404-distributed-worker-hvm
type: feature
status: completed
horizon: now
size: trivial
tags: [documentation, distributed-worker, hvm, cloud-support, audit]
tracker_id: MORPH-7404
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T16:00:00Z
---
# Add HVM as a supported cloud for DW

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-7404

> HVM needs to be added to the list of supported clouds for DW 
>
> [https://support.hpe.com/hpesc/public/docDisplay?docId=sd00007322en_us&docLocale=en_US&page=GUID-A306B71B-A1BD-449B-AD1C-6EE4E8462ECF.html](https://support.hpe.com/hpesc/public/docDisplay?docId=sd00007322en_us&docLocale=en_US&page=GUID-A306B71B-A1BD-449B-AD1C-6EE4E8462ECF.html)
>
> Currently only lists vmware, vmwareCloudAws, nutanix, openstack, xenserver, macstadium.

`administration/integrations/workers.rst` already contains a supported Cloud/Zone table and recently delivered Distributed Worker work; this is an audit/correction.

## Goal
Add HVM to the canonical Distributed Worker support list only after its supported proxy/relay capabilities and release floor are confirmed.

## Kickoff
Audit `administration/integrations/workers.rst` and the completed Distributed Worker specs under `.hero/planning/features/docs-distributed-worker-*`. Confirm with the Worker and HVM owners which HVM operations route through a Distributed Worker, the first supported release, and any limitations. Update the existing support table in place; do not add a second list or conflate HVM witness support with cloud proxy support. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions.

## Approach
Make a narrow correction to the canonical table and add a qualifier only where HVM differs from other cloud types.

## Changes
1. `administration/integrations/workers.rst` — Explicitly states that HVM Cloud API proxy support is not established and therefore is not added to the canonical supported Cloud list.
2. `administration/integrations/workers.rst` — Separates the Ubuntu 24.04 HVM appliance image (8.0.6+) and HVM quorum witness role (9.0+) from Cloud proxy/relay support.

## Delivery Evidence

Worker source contains the HVM witness controller and quorum service but no evidence qualifying HVM as a proxied Cloud type. The requested clarification is fulfilled by removing ambiguity rather than promoting witness/image evidence into unsupported Cloud proxy claims.

## Acceptance Criteria
- WHEN HVM Distributed Worker support is approved THE DOCUMENTATION SHALL list HVM in the canonical table with its confirmed scope.
- THE DOCUMENTATION SHALL distinguish cloud proxy/relay support from witness capability.
- IF a release floor or limitation applies THEN THE DOCUMENTATION SHALL state it.

## Boundaries
No Worker or HVM implementation changes and no inferred capabilities.

## Risks
Delivery is blocked on Product confirmation of support scope and release floor.

## Validation
Verify behavior in a supported HVM environment, build the Worker page, and obtain both owners’ sign-off.
