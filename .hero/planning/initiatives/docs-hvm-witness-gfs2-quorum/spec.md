---
title: "HVM Witness and Quorum Docs for Two-Node GFS2"
slug: docs-hvm-witness-gfs2-quorum
type: initiative
status: in-review
size: medium
horizon: now
priority: high
tags: [hvm, witness, quorum, gfs2, two-node, stretch-cluster, documentation]
child:
  - docs-hvm-quorum-topology-model
  - docs-hvm-two-node-gfs2-operations
  - docs-hvm-witness-discovery-crosslinks
relates-to: [docs-distributed-worker-guide, docs-distributed-worker-witness, hvm-13-cluster-docs]
domain: engineering
created: 2026-09-04
---

# HVM Witness and Quorum Docs for Two-Node GFS2

## Vision

Make HVM witness and quorum documentation equally operational for two-node HPE Clustered Filesystem (GFS2) clusters and multi-site stretch clusters, matching the two assignment paths already implemented in `morpheus-ui`.

## Goal

Operators deploying a two-Host GFS2 cluster with a Distributed Worker witness can follow HVM architecture, assignment, validation, failure, and troubleshooting guidance without being routed into stretch-cluster site groups, `siteWitness`, or third-site arbitration.

## Context

Field feedback is that witness and quorum docs still read as stretch-cluster first. A dedicated two-node page exists (`infrastructure/clusters/hvm/two_node_clusters.rst`), but the surrounding HVM and Worker narrative still treats stretch as the canonical witness workflow.

`../morpheus-ui` implements both topologies from one cluster Witness field:

- Quorum is sent only when the cluster is layout 1.3+ and has at least one GFS2 datastore (`MvmHostService.shouldSendQuorumInfo()`).
- `StatsService.sendQuorumDetailsToWorker()` / `sendQuorumDetailsToServer()` add the Distributed Worker as `witnessOnly: true`.
- If site groups exist, the worker is labeled `site: 'siteWitness'` (stretch).
- If no site groups exist, the worker is labeled `site: null` with the source comment `use this for 2 node gfs2 witness`.
- The Quorum panel always shows a witness member when present (`_summaryQuorum.gsp`); site names are stretch-only.

Current documentation gaps that produce the stretch-first reading:

- `administration/integrations/workers.rst` documents both topologies, then sends assignment and quorum validation only to `stretch_clusters`.
- `infrastructure/clusters/hvm/architecture.rst` describes same-site peer cross-verification and does not mention the two-node `site: null` vote.
- `stretch_clusters.rst` owns the detailed witness install, assignment timing, and troubleshooting; `two_node_clusters.rst` is shorter and is not the default discovery path.
- `failure_scenarios.rst` gives stretch site failure a full timeline and reduces two-node failures to a paragraph that points elsewhere.
- `host_vm_groups.rst` documents Site Groups without stating they are stretch-only and must not be created for two-node GFS2.

`docs-distributed-worker-witness` already added the two-node page and Worker URL semantics. This initiative does not redo Worker package or container install. It rebalances HVM quorum documentation so two-node GFS2 is a first-class topology, not an appendix to stretch.

## Specs

- [x] `docs-hvm-quorum-topology-model` - Architecture comparison, scoped same-site language, chooser sentences.
- [x] `docs-hvm-two-node-gfs2-operations` - Two-node Quorum panel expected values and timed failure scenarios.
- [x] `docs-hvm-witness-discovery-crosslinks` - Worker, Site Group, troubleshooting, building-clusters, and edge links split by topology.

## Dependencies

- `docs-hvm-quorum-topology-model` must land first. The other children reuse its topology names and must not invent a third witness model.
- `docs-distributed-worker-witness` remains the Worker URL / TLS / inbound Host path source. Link it; do not duplicate package or container install.
- Confirm with HVM engineering any two-node claims not established by `StatsService`, `MvmHostService`, or the Quorum panel: Corosync `Quorate: No` as expected, heartbeat-target requirement, and whether two Hosts plus witness is the only supported no-site-group GFS2 shape.
- `../morpheus-ui` is the implementation source of truth. Do not infer stretch behavior onto two-node clusters, or the reverse.

## Acceptance Criteria

- THE DOCUMENTATION SHALL present two-node GFS2 witness and stretch `siteWitness` as peer topologies that share a Distributed Worker and GFS2 activation condition.
- THE DOCUMENTATION SHALL state that two-node GFS2 does not use site groups or the `siteWitness` designation.
- WHEN an operator assigns a cluster Witness THE DOCUMENTATION SHALL provide a two-node GFS2 assignment and validation path that does not require opening stretch-cluster procedures.
- THE DOCUMENTATION SHALL describe two-node Host, witness, and partition failures with the same operational specificity as stretch site failure.
- THE DOCUMENTATION SHALL distinguish Agent quorum from Corosync `Quorate` for both topologies.
- IF a two-node behavior cannot be verified in `../morpheus-ui` THEN THE DOCUMENTATION SHALL not copy stretch arbitration, vote adjustment, or Site Group rules onto it.

## Boundaries

- Do not change product quorum, fencing, or Worker behavior.
- Do not rewrite Distributed Worker package, container, key, or TLS install owned by `docs-distributed-worker-guide`.
- Do not merge two-node and stretch into one undifferentiated witness page.
- Do not document NFS-only clusters as requiring a GFS2 quorum witness.
- Do not treat three-node single-site GFS2 without a witness as unsupported; the two-node page is additive.

## Risks

- Stretch language (`same-site peers`, `siteWitness`, third site, alphabetical site arbitration) is easy to leave in architecture and troubleshooting even after the two-node page exists.
- `workers.rst` currently funnels all assignment/validation to stretch; leaving that link will recreate the field complaint.
- Creating Site Groups on a two-node cluster would switch the payload to `siteWitness` and change arbitration; docs must warn against that.
- Worker URL versus appliance URL confusion remains; keep the existing Host-to-Worker reachability warning.

## Validation

- Trace two-node versus stretch payload construction in `StatsService.sendQuorumDetailsToWorker()` and `sendQuorumDetailsToServer()`.
- Confirm GFS2 activation in `MvmHostService.shouldSendQuorumInfo()` and Quorum panel rendering in `_summaryQuorum.gsp`.
- Audit every `stretch_clusters` cross-reference from Worker, architecture, building, failure, troubleshooting, edge, and Host-VM Groups pages.
- Build Sphinx HTML and confirm two-node pages are reachable from HVM landing, Worker witness, and building-clusters paths.
- Obtain HVM engineering review of two-node vote math, failure matrix, and Site Group exclusion.

## Progress

- All three children implemented 2026-09-04.
- `workers.rst` assignment no longer points only at stretch.
- Architecture compares two-node GFS2 and stretch; same-site peer language is stretch-only.
- Two-node runbook has panel expected values and timed Host/witness/partition failures.
- HVM engineering review of vote math and Site Group exclusion remains before publication.

## Kickoff

Rebalance HVM witness/quorum docs so two-node GFS2 is a first-class topology, not a stretch-cluster footnote.

**Status:** delivering — docs are in; HVM review remains.

**Pick up at:** HVM engineering review, then commit if requested.

→ `.hero/planning/initiatives/docs-hvm-witness-gfs2-quorum/spec.md`

**Files:** `infrastructure/clusters/hvm/architecture.rst`, `infrastructure/clusters/hvm/two_node_clusters.rst`, `administration/integrations/workers.rst`
**Skip:** do not redo Worker package/container install; do not copy stretch site arbitration onto two-node GFS2.
