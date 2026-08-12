---
title: "Lack of information regarding disk/storage/NIC type selection"
slug: docs-morph-7019-vm-device-types
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, vm, networking, storage, cloud-settings]
tracker_id: MORPH-7019
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T14:31:32Z
---
# Lack of information regarding disk/storage/NIC type selection

## Context
Jira: https://hpe.atlassian.net/browse/MORPH-7019

> Hi team,
>
> A partner asked me how it was possible to change the network interface type in a VM, so I told him that you needed to enable it in the cloud:
>
> ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f072bc4f-c6f7-44ee-8936-c602eb72a4ce&&collection=&height=216&occurrenceKey=null&width=587&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
> After that I looked in the documentation (both VME and Morpheus Enterprise) and it seems that nothing is appearing about it, nothing about Disk/storage/network type.
>
> Could we mention it somewhere please?

## Goal
Explain, for each product-confirmed cloud, how cloud-level enablement controls whether disk, storage, and NIC type selectors appear during VM provisioning or reconfiguration.

## Kickoff
Recover the Jira screenshot or obtain an equivalent current UI capture before delivery. Audit `integration_guides/Clouds/vmware/advanced.rst`, `integration_guides/Clouds/vmware/vmware.rst`, `provisioning/instances/creating_instances.rst`, and `administration/settings/provisioning.rst`. Confirm exact setting names, supported clouds, permissions, and whether each selector applies at create, reconfigure, or both; do not generalize VMware behavior to HVM or other clouds. Record an authoritative source for every factual claim and leave unresolved claims explicitly blocked rather than filling gaps from assumptions.

## Approach
Document enablement at the cloud-specific source and add concise provisioning cross-references. Reuse current content where device-type selection is already mentioned.

## Changes
1. `integration_guides/Clouds/vmware/advanced.rst` — Documented the exact VMware storage/network type enablement settings.
2. `provisioning/instances/creating_instances.rst` — Documented provider-dependent selector visibility and linked VMware configuration.

## Delivery Evidence

Current VMware seed/configuration code proves storage-type selection and core provisioning code consumes network-type selection. The documentation scopes the controls to VMware, explains selector visibility without claiming unsupported reconfigure behavior, and avoids generalizing to other Clouds.

## Acceptance Criteria
- WHEN a supported cloud enables device-type selection THE DOCUMENTATION SHALL identify the exact setting and resulting selectors.
- WHEN a user provisions a VMware VM THE DOCUMENTATION SHALL explain that storage and network type selectors depend on the corresponding Cloud settings and provider-exposed choices.
- THE DOCUMENTATION SHALL state that selector availability can differ during reconfiguration rather than promise unsupported lifecycle behavior.
- IF behavior differs by cloud THEN THE DOCUMENTATION SHALL describe only confirmed cloud-specific behavior.

## Boundaries
No feature enablement, unsupported-cloud claims, or reconstruction of the inaccessible Jira image.

## Risks
The inaccessible Jira image cannot establish behavior; current code supports the documented VMware-only scope. Other Cloud and lifecycle behavior remains intentionally undocumented.

## Validation
Inspect VMware configuration and provisioning code, build affected pages, and check cross-links. A live Cloud is optional future UI regression coverage.
