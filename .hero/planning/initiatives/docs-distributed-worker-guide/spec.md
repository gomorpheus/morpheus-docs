---
title: "Distributed Worker Deployment and Use-Case Documentation"
slug: docs-distributed-worker-guide
type: initiative
status: in-review
size: medium
horizon: now
priority: high
tags: [distributed-worker, console-gateway, vdi, witness, hvm, gfs2, docker]
child: [docs-distributed-worker-capabilities, docs-distributed-worker-deployment, docs-distributed-worker-witness]
relates-to: [catchup-administration, hvm-13-cluster-docs]
created: 2026-07-30
---

# Distributed Worker Deployment and Use-Case Documentation

## Vision

Provide one authoritative guide to the Morpheus Worker runtime: what each registration and key enables, how one runtime can serve multiple roles, how to deploy it from packages or the `morpheusdata/morpheus-worker` container image, and how to configure it as a reachable quorum witness for HVM clusters.

## Goal

Customers can choose and configure the Worker as a Distributed Worker, console gateway, VDI gateway, two-node HPE Shared File System witness, or stretch-cluster witness without conflating the UI objects, API keys, URLs, and network paths required by each role.

## Approach

Consolidate the role model in `administration/integrations/workers.rst`, retain task-specific VDI and HVM procedures in their existing sections, and cross-link them. Ground configuration in `morpheus-worker` runtime properties and `morpheus-ui` registration and quorum code. Treat Docker Hub as a deployment source, but validate examples against the checked-out worker entrypoint before publication.

## Context

Current documentation is fragmented:

- `administration/integrations/workers.rst` documents package installation, cloud proxying, agent relay, and combined Distributed Worker/VDI mode.
- `infrastructure/vdi/gateways.rst` describes VDI gateway routing but does not explain that the same gateway registration can be selected as the appliance Default Console Gateway.
- `tools/vdi_pools.rst` contains older, duplicate package, Docker, and Helm instructions.
- `infrastructure/clusters/hvm/stretch_clusters.rst` identifies a Distributed Worker as the witness but does not explain the Worker URL requirement or two-node GFS2 witness use.
- Docker Hub documents `morpheusdata/morpheus-worker`, `MORPHEUS_KEY`, `MORPHEUS_WORKER_KEY`, `MORPHEUS_URL`, self-signed TLS, and PKCS#12 TLS options.

Source-backed behavior:

- `MORPHEUS_KEY` or package configuration `worker['apikey']` registers VDI/console gateway capability.
- `MORPHEUS_WORKER_KEY` or `worker['worker_key']` registers Distributed Worker capability for cloud/API proxying, agent relay, and witness actions.
- Both keys can be configured on one runtime, enabling combined roles.
- Console sessions use a VDI Gateway selected from network, Cloud, or the appliance `Default Console Gateway`; VDI desktop sessions use the gateway assigned to the VDI Pool.
- A cluster witness is selected from Distributed Worker records. Morpheus derives host quorum `witnessUrl` data from the record's Worker URL (`DistributedWorker.applianceUrl`).
- The worker exposes a witness controller under `/witness`, and cluster Hosts must be able to reach the configured Worker URL for quorum checks.
- For HVM 1.3+, quorum information is activated when the cluster has a GFS2 datastore. Without site groups the worker is used as the two-node GFS2 witness; with site groups it is assigned as `siteWitness` for a stretch cluster.

Primary sources:

- `administration/integrations/workers.rst`
- `infrastructure/vdi/gateways.rst`
- `tools/vdi_pools.rst`
- `infrastructure/clusters/hvm/stretch_clusters.rst`
- `../morpheus-worker/README.md`
- `../morpheus-worker/docker-run-worker.sh`
- `../morpheus-worker/src/main/groovy/com/morpheus/worker/controller/QuorumController.java`
- `../morpheus-ui/morpheus-core/grails-app/services/com/morpheus/StatsService.groovy`
- `../morpheus-ui/morpheus-ui/grails-app/controllers/com/morpheus/TerminalController.groovy`

## Specs

- [x] `docs-distributed-worker-capabilities` - Implemented and awaiting review.
- [x] `docs-distributed-worker-deployment` - Implemented and awaiting review.
- [x] `docs-distributed-worker-witness` - Implemented and awaiting HVM review.

## Dependencies

- Confirm supported package operating systems and sizing against current release artifacts; existing worker and VDI pages disagree.
- Confirm the supported container tag policy instead of assuming `latest` is appropriate for production.
- Confirm the customer-facing name for “HPE Shared File System” and whether all supported two-node implementations map to GFS2.
- Validate the exact host-to-witness request URL generated from Worker URL before publishing an endpoint test command; source currently spans Manager and Worker URL composition.
- Coordinate witness edits with `hvm-13-cluster-docs` because it owns the broader HVM 1.3 cluster documentation.

## Acceptance Criteria

- THE DOCUMENTATION SHALL distinguish Distributed Worker, console gateway, VDI gateway, and witness roles.
- THE DOCUMENTATION SHALL explain how `worker_key` and gateway `apikey` configuration enable independent or combined roles on one runtime.
- THE DOCUMENTATION SHALL explain where console gateways and VDI Pool gateways are selected and how their traffic paths differ.
- THE DOCUMENTATION SHALL provide current package and `morpheusdata/morpheus-worker` container deployment guidance with required ports, keys, URLs, and TLS choices.
- WHEN a Distributed Worker is selected as an HVM witness THE DOCUMENTATION SHALL require a Worker URL reachable from every participating cluster Host.
- THE DOCUMENTATION SHALL cover both two-node GFS2 witness and stretch-cluster `siteWitness` use cases.
- THE DOCUMENTATION SHALL include role-specific validation and troubleshooting checks.

## Boundaries

- Do not change worker, Manager, agent, quorum, console, or VDI product behavior.
- Do not duplicate the complete HVM stretch-cluster architecture owned by `hvm-13-cluster-docs`.
- Do not publish credentials, sample real keys, unsupported image tags, or unverified firewall ports.
- Do not describe in-development Docker Hub capabilities as generally available.

## Risks

- “Worker URL,” “Appliance URL,” and `DistributedWorker.applianceUrl` are easy to confuse; documentation must identify which component must reach each URL.
- A worker can connect outbound to the Manager while still being unusable as a witness if cluster Hosts cannot reach its Worker URL.
- Combining gateway, proxy, and witness roles changes network exposure and capacity requirements; the guide must avoid implying every combined deployment is operationally desirable.
- Existing VDI content is duplicated and inconsistent, so consolidation must preserve valid task guidance and links.

## Validation

- Trace each role and key to Worker configuration and Manager selection logic.
- Validate witness guidance against Manager quorum payload creation and Worker witness endpoint handling.
- Compare container examples with `docker-run-worker.sh` and the Docker Hub overview.
- Run the Sphinx HTML build and inspect rendered cross-references, tables, and command blocks.
- Obtain HVM, VDI, Security, and Worker engineering review before publication.

## Progress

All three documentation children are implemented and pass source and rendered-HTML validation. HVM, VDI, Security, and Worker engineering review remains before publication.

## Kickoff

Builds one source-backed guide for Worker proxy, console/VDI gateway, container, and HVM witness roles.

**Status:** in-review - capability, deployment, and witness guidance is implemented and validated.

**Pick up at:** complete cross-functional review, focusing on witness assignment timing, supported package platforms, and combined-role security guidance.

→ `.hero/planning/initiatives/docs-distributed-worker-guide/spec.md`

**Files:** `administration/integrations/workers.rst`, `infrastructure/vdi/gateways.rst`, `infrastructure/clusters/hvm/stretch_clusters.rst`, `../morpheus-worker/docker-run-worker.sh`, `../morpheus-ui/morpheus-core/grails-app/services/com/morpheus/StatsService.groovy`
