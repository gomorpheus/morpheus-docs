---
title: "License Socket Consumption Reference"
slug: docs-license-consumption-reference
type: feature
status: in-review
size: small
horizon: now
priority: high
tags: [licensing, sockets, reference]
parent: docs-license-socket-consumption
relates-to: [docs-administration-licensing]
created: 2026-07-30
claimed_by: mcp-agent
claimed_at: 2026-07-30T10:03:16-04:00
---

# License Socket Consumption Reference

## Context

`administration/settings/license.rst` only describes legacy workload element and managed RAM licensing. The current standard license implementation also measures physical and VM-derived socket usage, but customers do not have a documentation table explaining what is counted.

## Goal

Update the appliance License documentation with an approved reference table that maps managed resource categories to socket consumption and explains how actual usage is calculated and displayed.

## Approach

Use `ApplianceStatsService.getSocketStats()` and the enforcement paths in `ApplianceLicenseService` as the behavioral source, then have Product or Licensing validate customer-facing policy language. Clearly separate appliance capacity licensing from provisioned software license keys.

## Changes

1. Update `administration/settings/license.rst` to describe the current standard socket model alongside clearly labeled legacy license models.
2. Add a resource matrix covering private physical hypervisors, bare-metal and container hypervisor hosts, private guest VMs, public VMs, private VMs without inventoried hosts, HVM hosts, controllers, and Kubernetes masters.
3. Explain that physical hosts use reported socket counts, default to two sockets when unknown, and are deduplicated when the same unique host is inventoried more than once.
4. Explain the 15-VM-per-socket calculation without claiming an unverified rounding rule.
5. Explain where administrators view current limits and usage, and distinguish this page from `administration/provisioning/licenses.rst` software license-key management.

## Acceptance Criteria

- THE DOCUMENTATION SHALL state what consumes physical-host socket capacity and what is excluded.
- THE DOCUMENTATION SHALL state that an unknown qualifying physical host socket count defaults to two.
- THE DOCUMENTATION SHALL state that public VMs and private VMs without qualifying inventoried hosts are calculated at 15 VMs per socket.
- THE DOCUMENTATION SHALL state that private guest VMs are not charged again when their underlying hypervisor hosts are counted.
- THE DOCUMENTATION SHALL label legacy workload, managed RAM, and HVM-specific limits accurately.

## Boundaries

- No pricing, contract interpretation, tier matrix rewrite, or product code change.
- Worked topology examples belong to `docs-license-consumption-examples`.

## Risks

- Product policy may require language that is not inferable from runtime code.
- Supported versions may expose different limit fields or License-page labels.

## Validation

- Compare every matrix row with the source filters in `ApplianceStatsService` and enforcement in `ApplianceLicenseService`.
- Obtain Product or Licensing review.
- Run the documentation build and link checks.

## Delivery

- Updated `administration/settings/license.rst` with the standard socket formula, resource matrix, two-socket fallback, host deduplication, private Cloud double-count protection, License page usage guidance, and legacy-model separation.
- Verified all five acceptance criteria against `ApplianceStatsService.getSocketStats()`, `privateCloudHasHypervisorHosts()`, `ApplianceLicenseService.getCurrentLicenseUsage()`, and the rendered HTML.
- `python3 -m sphinx -M html . _build` succeeded with the repository's existing warnings.
- Product or Licensing review remains required before publication.

## Kickoff

Adds the missing appliance socket-consumption reference to the License page.

**Status:** in-review - documentation and HTML validation are complete; customer-facing policy wording needs Product or Licensing approval.

**Pick up at:** review the socket matrix against approved licensing terminology, then mark the spec complete if no wording changes are required.

→ `.hero/planning/features/docs-license-consumption-reference/spec.md`

**Files:** `administration/settings/license.rst`, `../morpheus-ui/morpheus-core/grails-app/services/com/morpheus/ApplianceStatsService.groovy`, `../morpheus-ui/morpheus-core/grails-app/services/com/morpheus/ApplianceLicenseService.groovy`
