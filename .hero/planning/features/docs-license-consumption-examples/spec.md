---
title: "License Socket Consumption Examples"
slug: docs-license-consumption-examples
type: feature
status: in-review
size: small
horizon: now
priority: high
tags: [licensing, sockets, hks, vmware, bare-metal]
parent: docs-license-socket-consumption
depends-on: [docs-license-consumption-reference]
created: 2026-07-30
claimed_by: mcp-agent
claimed_at: 2026-07-30T10:03:16-04:00
---

# License Socket Consumption Examples

## Context

Customers need concrete totals for common deployment shapes. The key point is that virtual HKS on VMware must not double dip against sockets already consumed by the VMware hypervisors, while bare-metal HKS worker hosts consume their physical sockets.

## Goal

Add reproducible examples that show how the documented socket rules apply to HKS on VMware, HKS on bare metal, public-cloud VMs, and private-cloud VMs without inventoried hosts.

## Approach

Build each example from the approved reference rules and show the arithmetic. Use exact multiples of 15 for VM-ratio examples until display and rounding behavior for partial groups is confirmed.

## Changes

1. Add a VMware example showing counted ESXi host sockets and zero additional socket usage for virtual HKS control-plane and worker VMs on those hosts.
2. Add a bare-metal HKS example showing each qualifying worker host's physical sockets, including the two-socket fallback only where the product cannot determine the socket count.
3. Add a public-cloud VM example using the 15-VM-per-socket calculation.
4. Add a private-cloud example showing the difference between a Cloud with inventoried hypervisor hosts and one without qualifying hosts.
5. Cross-link examples from the consumption matrix and avoid presenting runtime calculations as contractual advice.

## Acceptance Criteria

- WHEN HKS runs virtually on counted VMware hosts THE DOCUMENTATION SHALL show zero additional sockets for the HKS guest VMs.
- WHEN HKS workers run on bare metal THE DOCUMENTATION SHALL total the workers' physical sockets.
- WHEN 30 public-cloud VMs are managed THE DOCUMENTATION SHALL show two VM-derived sockets.
- WHEN private-cloud hosts are not inventoried THE DOCUMENTATION SHALL show VM-derived socket usage at the documented ratio.
- THE DOCUMENTATION SHALL make each example total reproducible from the reference rules.

## Boundaries

- Do not invent fractional rounding, minimum consumption, pricing, or contract terms.
- Do not duplicate the complete resource matrix from `docs-license-consumption-reference`.

## Risks

- HKS topology labels can obscure which nodes are guest VMs versus qualifying physical worker hosts.
- Examples can become misleading if they omit whether underlying private-cloud hosts are inventoried.

## Validation

- Verify each total against `ApplianceStatsService.getSocketStats()` and existing Spock examples.
- Obtain HKS and Licensing review for the VMware and bare-metal scenarios.
- Run the documentation build and link checks.

## Delivery

- Added reproducible examples for virtual HKS on VMware, bare-metal HKS workers, 30 public Cloud VMs, and 30 private Cloud VMs without qualifying inventoried Hosts.
- Verified all five acceptance criteria against the reference matrix, `ApplianceStatsServiceSpec`, and rendered HTML.
- `python3 -m sphinx -M html . _build` succeeded with the repository's existing warnings.
- HKS and Licensing review remains required before publication.

## Kickoff

Adds worked socket totals for virtual HKS on VMware, bare-metal HKS, and VM-ratio deployments.

**Status:** in-review - examples are implemented and validated; HKS and Licensing approval remains.

**Pick up at:** review the VMware and bare-metal HKS totals, then mark the spec complete if no wording changes are required.

→ `.hero/planning/features/docs-license-consumption-examples/spec.md`

**Files:** `administration/settings/license.rst`, `../morpheus-ui/morpheus-core/src/test/groovy/com/morpheus/ApplianceStatsServiceSpec.groovy`, `../morpheus-ui/morpheus-core/src/test/groovy/com/morpheus/ApplianceLicenseServiceSpec.groovy`
