---
title: "Distributed Worker Witness Configuration"
slug: docs-distributed-worker-witness
type: feature
status: in-review
size: small
horizon: now
priority: high
tags: [distributed-worker, witness, hvm, gfs2, stretch-cluster]
parent: docs-distributed-worker-guide
depends-on: [docs-distributed-worker-capabilities, docs-distributed-worker-deployment]
relates-to: [hvm-13-cluster-docs]
created: 2026-07-30
claimed_by: mcp-agent
claimed_at: 2026-07-30T11:00:55-04:00
---

# Distributed Worker Witness Configuration

## Context

Stretch-cluster docs state that the witness is a Distributed Worker, but omit the critical Worker URL semantics and the two-node HPE Shared File System/GFS2 use case. A Worker can be connected to the Manager yet fail as a witness when cluster Hosts cannot reach its configured Worker URL.

## Goal

Document a complete, testable witness workflow for two-node GFS2 clusters and stretch clusters, including topology, Worker record configuration, reachable Worker URL, cluster assignment, activation conditions, validation, and failure troubleshooting.

## Approach

Add canonical witness requirements to `administration/integrations/workers.rst` and focused procedures to HVM cluster documentation. Explain that Morpheus builds host quorum `witnessUrl` information from the Distributed Worker record's Worker URL and that every participating Host must resolve, trust, and reach that URL.

## Changes

1. Add a witness role section to `administration/integrations/workers.rst` describing the Distributed Worker key, Worker URL, TLS, and inbound Host connectivity requirements.
2. Update `infrastructure/clusters/hvm/stretch_clusters.rst` with explicit Worker URL configuration, third-site placement, reachability validation, post-deployment witness assignment, and `siteWitness` behavior.
3. Add or update the two-node HPE Shared File System/GFS2 cluster procedure to require a Distributed Worker witness and explain that it is represented without site groups.
4. Explain that HVM 1.3+ sends quorum information when GFS2 shared storage is present, and distinguish this from NFS configurations that do not require cluster-level GFS2 quorum.
5. Add validation for Worker connection, Host DNS and TLS reachability, witness endpoint response, Manager and Worker logs, and the cluster Quorum panel.
6. Add troubleshooting symptoms for missing Worker URL, unreachable URL, certificate trust failure, incorrect witness selection timing, and absent GFS2 quorum activation.

## Acceptance Criteria

- WHEN a Worker is configured as a witness THE DOCUMENTATION SHALL require a Worker URL reachable from all participating cluster Hosts.
- THE DOCUMENTATION SHALL explain that Morpheus derives host `witnessUrl` data from the Distributed Worker record's Worker URL.
- THE DOCUMENTATION SHALL cover witness topology and assignment for both two-node GFS2 and stretch clusters.
- THE DOCUMENTATION SHALL distinguish `siteWitness` behavior from the no-site-group two-node witness.
- THE DOCUMENTATION SHALL state when GFS2 quorum information is activated and distinguish NFS-based behavior.
- THE DOCUMENTATION SHALL provide preflight and post-configuration validation steps that detect DNS, routing, TLS, URL, and worker-connection failures.

## Boundaries

- Do not redesign HVM quorum or duplicate all stretch-cluster operations.
- Do not publish an exact witness endpoint test until URL composition is verified end to end.
- Do not claim a witness is required for NFS-only stretch storage where cluster-level GFS2 quorum is not active.

## Risks

- Manager and Worker source compose witness paths across components; an incorrect example endpoint would create false-negative tests.
- “Worker URL” can be mistaken for the Manager-facing `appliance_url`.
- Existing text says not to select a witness during initial stretch-cluster creation; confirm whether the same sequencing applies to the two-node workflow.

## Validation

- Trace payload generation in `StatsService.sendQuorumDetailsToWorker()` and `sendQuorumDetailsToServer()`.
- Trace Worker handling in `QuorumInfoAction`, `QuorumCheckService`, and `QuorumController`.
- Confirm activation in `MvmHostService.shouldSendQuorumInfo()`.
- Obtain HVM engineering review and run the Sphinx HTML build.

## Delivery

- Documented that the Distributed Worker record's Worker URL is the base used to generate host `witnessUrl` data and must be resolvable, reachable, and trusted by every participating Host.
- Added stretch-cluster third-site setup, post-deployment assignment, `siteWitness` behavior, DNS/TLS preflight, and failure troubleshooting.
- Added two-node HPE Shared File System/GFS2 witness topology and assignment without site groups.
- Documented GFS2 quorum activation for HVM 1.3 or later and retained the existing distinction for NFS-based stretch storage.
- All six acceptance criteria pass against Manager quorum payload generation, Worker quorum handling, HVM activation logic, and rendered HTML. HVM engineering review remains before publication.

## Kickoff

Documents the reachable Worker URL and quorum workflow for two-node GFS2 and stretch-cluster witnesses.

**Status:** in-review - witness procedures and validation are implemented; HVM engineering review remains.

**Pick up at:** validate two-node assignment timing and Worker URL terminology with HVM engineering, then approve for completion.

→ `.hero/planning/features/docs-distributed-worker-witness/spec.md`

**Files:** `administration/integrations/workers.rst`, `infrastructure/clusters/hvm/stretch_clusters.rst`, `../morpheus-ui/morpheus-core/grails-app/services/com/morpheus/StatsService.groovy`, `../morpheus-worker/src/main/groovy/com/morpheus/worker/controller/QuorumController.java`
