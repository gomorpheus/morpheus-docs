---
title: "License Socket Consumption Documentation"
slug: docs-license-socket-consumption
type: initiative
status: in-review
size: medium
horizon: now
priority: high
tags: [licensing, sockets, hks, vmware, bare-metal]
child: [docs-license-consumption-reference, docs-license-consumption-examples]
relates-to: [docs-administration-licensing]
created: 2026-07-30
---

# License Socket Consumption Documentation

## Vision

Make the appliance licensing documentation an authoritative, practical reference for what consumes socket capacity and how usage is calculated. Customers should be able to estimate usage for physical hosts, bare-metal HKS, virtual HKS, public-cloud VMs, and private-cloud VMs without assuming that every managed VM consumes an additional socket.

## Goal

Deliver an approved socket-consumption reference and worked examples in the appliance License documentation so customers can calculate expected usage and understand why virtual HKS on VMware is not counted again while bare-metal HKS workers are.

## Approach

Document the source-backed accounting rules first, then derive deployment examples from that reference. Treat product code as the source for runtime behavior and require Product or Licensing review for customer-facing policy and contractual terminology.

## Context

The current appliance license page, `administration/settings/license.rst`, describes legacy workload element and managed RAM licensing but does not explain the standard socket model implemented by the product. This omission produces mixed guidance, particularly for HKS deployments.

The product source establishes these current behaviors:

- Private-cloud physical hypervisors, container hypervisors, and bare-metal hosts consume their reported physical sockets; a host with no reported value defaults to two sockets.
- Duplicate records for the same physical private-cloud host are counted once when they share a unique ID.
- Public-cloud VMs consume socket capacity at 15 VMs per socket.
- Private-cloud VMs use the same 15-VM ratio only when their Cloud has no qualifying inventoried hypervisor or bare-metal host.
- Private-cloud guest VMs do not add socket usage when the underlying hosts are already counted. Therefore, virtual HKS nodes on VMware do not consume additional sockets on top of the VMware hypervisor sockets.
- Bare-metal HKS worker hosts consume physical socket capacity. Controllers, Kubernetes masters, guest VMs, and nested or child host records are excluded from the private-cloud physical-host count.
- HVM-specific socket limits remain distinct in legacy license paths; documentation must label legacy behavior rather than blending it into the current global socket model.

Primary implementation sources:

- `../morpheus-ui/morpheus-core/grails-app/services/com/morpheus/ApplianceLicenseService.groovy`
- `../morpheus-ui/morpheus-core/grails-app/services/com/morpheus/ApplianceStatsService.groovy`
- `../morpheus-ui/morpheus-core/src/test/groovy/com/morpheus/ApplianceLicenseServiceSpec.groovy`
- `../morpheus-ui/morpheus-core/src/test/groovy/com/morpheus/ApplianceStatsServiceSpec.groovy`

## Specs

- [x] `docs-license-consumption-reference` - Reference implemented and awaiting Product or Licensing approval.
- [x] `docs-license-consumption-examples` - Examples implemented and awaiting HKS and Licensing approval.

## Dependencies

- Confirm customer-facing terminology for the current `maxSockets` model and the legacy `maxMvmSockets` model with Product or Licensing before publication.
- Confirm whether fractional VM-derived socket usage is displayed or rounded in supported releases before documenting examples that are not exact multiples of 15.
- The reference rules should land before or with the deployment examples so examples cannot become the only source of licensing policy.

## Acceptance Criteria

- THE DOCUMENTATION SHALL identify each resource category that does and does not consume socket capacity.
- THE DOCUMENTATION SHALL explain physical-host socket counting, the two-socket fallback, and the 15-VM-per-socket calculation.
- WHEN HKS runs as virtual machines on counted VMware hypervisors THE DOCUMENTATION SHALL state that the HKS guest VMs do not consume additional sockets.
- WHEN HKS runs on bare-metal worker hosts THE DOCUMENTATION SHALL explain that the workers consume their physical socket counts.
- THE DOCUMENTATION SHALL distinguish current global socket accounting from legacy workload, RAM, and HVM-specific license limits.
- THE DOCUMENTATION SHALL include worked examples whose totals can be reproduced from the documented rules.
- THE DOCUMENTATION SHALL identify the License page as the source for actual usage and advise customers to contact their account team for contractual entitlement questions.

## Boundaries

- Do not publish prices, contractual terms, or tier entitlements that are not represented by product behavior and approved licensing policy.
- Do not change appliance licensing code or usage calculations as part of this initiative.
- Do not treat software license-key management under `administration/provisioning/licenses.rst` as appliance capacity licensing.
- Do not rewrite the broader three-tier feature matrix tracked by `docs-administration-licensing`.

## Risks

- Source behavior can differ across supported product versions; wording must identify version-specific or legacy paths where applicable.
- "Bare metal consumes a license" is too broad without identifying excluded controllers and Kubernetes masters and the physical socket basis.
- VM-derived usage may be fractional because the implementation divides VM count by 15; examples must not invent rounding behavior.
- Licensing policy may impose contractual rules beyond the runtime enforcement code, so Product or Licensing review is required before publication.

## Validation

- Score and lint the initiative and both child specs with Hero.
- During delivery, trace each documented rule to `ApplianceStatsService` or `ApplianceLicenseService` and their Spock coverage.
- Obtain Product or Licensing approval for policy wording and HKS review for topology examples.
- Run the documentation build and link checks after both children land.

## Progress

Documentation and rendered HTML validation are complete. All acceptance criteria pass; Product or Licensing approval and HKS review remain before publication.

## Kickoff

Clarify appliance socket licensing, especially why virtual HKS on VMware is not charged again while bare-metal HKS workers consume physical sockets.

**Status:** in-review - reference and examples are implemented and validated; policy approval remains.

**Pick up at:** obtain Product or Licensing approval for the resource matrix and HKS review for both topology examples.

→ `.hero/planning/initiatives/docs-license-socket-consumption/spec.md`

**Files:** `administration/settings/license.rst`, `../morpheus-ui/morpheus-core/grails-app/services/com/morpheus/ApplianceStatsService.groovy`, `../morpheus-ui/morpheus-core/grails-app/services/com/morpheus/ApplianceLicenseService.groovy`
