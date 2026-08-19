---
title: "Distributed Worker Capability and Registration Model"
slug: docs-distributed-worker-capabilities
type: feature
status: in-review
size: small
horizon: now
priority: high
tags: [distributed-worker, console-gateway, vdi, architecture]
parent: docs-distributed-worker-guide
relates-to: [catchup-administration]
created: 2026-07-30
claimed_by: mcp-agent
claimed_at: 2026-07-30T11:00:55-04:00
---

# Distributed Worker Capability and Registration Model

## Context

The existing worker page says one installation can run as a Distributed Worker and VDI Gateway, but it does not give operators a complete role-to-registration map. Console gateway, VDI Pool gateway, cloud proxy, agent relay, and witness selection are documented on separate pages with inconsistent terminology.

## Goal

Document which Morpheus UI object, key, URL, assignment point, and traffic path apply to each Worker role, including supported combined-role configuration.

## Approach

Add a capability matrix to `administration/integrations/workers.rst` and link task details from the VDI and HVM sections. Describe a console gateway as a VDI Gateway registration used by console routing, not as a third key or runtime mode.

## Changes

1. Update `administration/integrations/workers.rst` with a role matrix for cloud/API proxy, agent relay, console gateway, VDI Pool gateway, and cluster witness.
2. Explain the independent purposes of `worker['worker_key']` and `worker['apikey']`, and that both can be configured on one Worker runtime.
3. Explain console gateway selection precedence from network, Cloud, and appliance Default Console Gateway, and contrast it with VDI Pool gateway assignment.
4. Update `infrastructure/vdi/gateways.rst` and `administration/settings/appliance.rst` cross-references so console and VDI use point to the canonical Worker guide.
5. Identify combined-role network, availability, and sizing considerations without recommending co-location for every environment.

## Acceptance Criteria

- THE DOCUMENTATION SHALL map each Worker role to its UI registration, key, assignment point, and traffic path.
- THE DOCUMENTATION SHALL state that console gateway use relies on a VDI Gateway registration and gateway API key.
- THE DOCUMENTATION SHALL state that Distributed Worker and gateway keys can coexist on one runtime.
- THE DOCUMENTATION SHALL distinguish appliance console routing from VDI Pool gateway routing.
- THE DOCUMENTATION SHALL identify when separate Worker deployments are preferable for security, availability, or capacity isolation.

## Boundaries

- Package and container commands belong to `docs-distributed-worker-deployment`.
- Witness setup details belong to `docs-distributed-worker-witness`.

## Risks

- Existing documentation sometimes uses “VDI Gateway” and “console gateway” interchangeably.
- Gateway selection precedence must match supported Manager behavior across resource types.

## Validation

- Verify key semantics in `WorkerConfig.groovy` and `docker-run-worker.sh`.
- Verify console selection in `TerminalController.groovy` and VDI Pool selection in `VdiPoolService.groovy` and `VdiGatewayService.groovy`.
- Run the documentation build and inspect rendered links.

## Delivery

- Added the Worker capability matrix to `administration/integrations/workers.rst`, mapping cloud/Agent proxy, console gateway, VDI gateway, and witness roles to registrations, keys, assignments, and traffic paths.
- Clarified that console routing uses a VDI Gateway registration, and that `worker_key` and gateway `apikey` can coexist on one runtime.
- Updated `infrastructure/vdi/gateways.rst`, `tools/vdi_pools.rst`, and `administration/settings/appliance.rst` to distinguish Default Console Gateway from VDI Pool assignment and link to the canonical Worker guide.
- All five acceptance criteria pass against `TerminalController`, VDI services, Worker configuration source, and rendered HTML.

## Kickoff

Explains every Worker role and which registration, key, URL, and assignment enables it.

**Status:** in-review - role and registration guidance is implemented and validated.

**Pick up at:** review capability terminology and combined-role operational guidance, then approve for completion.

→ `.hero/planning/features/docs-distributed-worker-capabilities/spec.md`

**Files:** `administration/integrations/workers.rst`, `infrastructure/vdi/gateways.rst`, `administration/settings/appliance.rst`, `../morpheus-ui/morpheus-ui/grails-app/controllers/com/morpheus/TerminalController.groovy`
