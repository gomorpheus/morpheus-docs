---
title: "Two-Node GFS2 Witness Operations and Failure Coverage"
slug: docs-hvm-two-node-gfs2-operations
type: feature
status: completed
size: medium
horizon: now
priority: high
domain: engineering
tags: [hvm, gfs2, two-node, witness, failure, documentation]
parent: docs-hvm-witness-gfs2-quorum
depends-on: [docs-hvm-quorum-topology-model]
relates-to: [docs-distributed-worker-witness]
created: 2026-09-04
completed_at: 2026-09-04T16:34:59Z
---

# Two-Node GFS2 Witness Operations and Failure Coverage

## Context

`two_node_clusters.rst` already has topology, a seven-step deployment list, a 3-of-3 failure matrix, and troubleshooting. Stretch still owns the deeper timed narrative (`failure_scenarios.rst` Scenario 4) and the default “how do I run this” reading. Field feedback is that two-node HPE Clustered Filesystem (GFS2) operators cannot operate from the two-node page with stretch-equivalent confidence.

Source constraints from `../morpheus-ui`:

- Witness is bound on cluster edit via `ComputeClusterService` `opts.serverGroup['witness.id']`.
- Agent quorum members are not sent until `shouldSendQuorumInfo()` is true (layout 1.3+ and a GFS2 datastore). Selecting the Worker before GFS2 is correct; the witness will not appear as a quorum member until GFS2 exists.
- Two-node majority is 2 of 3. One Host plus witness can retain quorum. One Host alone cannot. Both Hosts without the witness retain quorum but lose Host-failure tolerance.
- Heartbeat failure threshold remains 140 seconds (7 missed 20-second writes) per `architecture.rst`. Quorum unreachability remains 60 seconds.

## Goal

Give two-node GFS2 operators stretch-equivalent assignment, Quorum panel validation, timed Host/witness/partition failures, and maintenance rules on the two-node page, without Site Groups or stretch assignment.

## Kickoff

Expands the two-node GFS2 runbook and failure timelines so operators do not need stretch docs to run the cluster.

**Status:** delivering — panel expected values and timed failure scenarios are in; close after audit.

**Pick up at:** `/deliver docs-hvm-witness-discovery-crosslinks` if `workers.rst` still points assignment only at stretch.

→ `.hero/planning/features/docs-hvm-two-node-gfs2-operations/spec.md`

**Files:** `infrastructure/clusters/hvm/two_node_clusters.rst:78`, `infrastructure/clusters/hvm/failure_scenarios.rst:116`
**Skip:** do not send two-node operators through stretch assignment or alphabetical site-winner logic.

## Approach

Keep `two_node_clusters.rst` as the two-node runbook. Expand existing sections rather than creating a new page. Add timed scenarios to `failure_scenarios.rst` so that page is not stretch-only. Link `:ref:`hvm-witness-deployment`` and `:doc:`/administration/integrations/workers`` instead of copying package or container install.

Use |InfClu| for cluster navigation. Do not invent Agent-side two-node fencing details beyond the existing matrix, 60-second unreachability, and 140-second heartbeat threshold.

## Changes

1. Expand `infrastructure/clusters/hvm/two_node_clusters.rst` Deployment and Quorum Validation.
   - Keep the existing order: create two-Host cluster, deploy Worker, validate Host-to-Worker URL, edit cluster and select Witness, add shared storage, create GFS2, then validate the Quorum panel.
   - State the UI path as |InfClu| > cluster > :guilabel:`Edit` > **Witness**. Do not tell operators to choose the witness during initial create even though the create form shows the field (`building_clusters.rst` already says configure after create).
   - Quorum panel expected values after GFS2 exists:
     - Status **ACHIEVED**
     - Nodes configured: 3 (two Hosts plus witness)
     - Both Hosts reachable / online
     - Witness row present and reachable
     - No **Sites** row
     - Host table is a flat list, not grouped by site
     - Designated Coordinator is one of the two Hosts
     - GFS2 lockspaces OK (not WAIT FENCING)
     - Heartbeat target healthy on both Hosts
   - Add an HTTPS check against the generated witness path, using the cluster UUID from the cluster detail page: `https://<Worker URL host>/witness/<cluster UUID>/quorum`. Do not use `--insecure`.

2. Expand Failure and Maintenance Behavior on the same page.
   - Keep the existing vote matrix.
   - Add a short timing note: Host unreachability is 60 seconds; VM recovery follows the 140-second heartbeat threshold on the surviving Host while the witness is reachable.
   - Restate maintenance: confirm the other Host and witness are healthy before maintenance mode; never maintain a Host and the witness together; restore all three members before the second Host.

3. Replace `infrastructure/clusters/hvm/failure_scenarios.rst` **Two-Node Cluster Failures** (currently one paragraph) with timed scenarios that match the matrix:
   - One Host down, witness reachable — surviving Host retains 2 of 3; VM recovery after heartbeat threshold.
   - Witness down, both Hosts reachable — cluster retains 2 of 3; no Host may be taken offline until the witness returns.
   - One Host and witness down — remaining Host has 1 of 3 and cannot retain quorum; it fences to protect GFS2.
   - Host-to-Host partition — the Host that can reach the witness can form 2 of 3; the isolated Host cannot. Do not apply stretch alphabetical site-winner logic.
   - Keep the existing pointer into `two_node_clusters` for the full matrix rather than duplicating Worker URL troubleshooting.

4. Add two-node-only troubleshooting on `two_node_clusters.rst`.
   - Worker active but witness missing from the Quorum panel: GFS2 not created yet, or cluster refresh has not sent quorum info.
   - Sites row appearing on a two-node cluster: Site Groups were created; stop and treat as stretch misconfiguration.
   - Do not list stretch **Stretch assignment conflict** / do-not-create-`siteWitness`-group as two-node steps.

5. Add an explicit Site Group warning on the two-node Limitations section: do not create Site Groups on this topology; doing so switches the witness to `siteWitness`. Link `:doc:`host_vm_groups`` only as the place Site Groups are created, not as a required step.

## Acceptance Criteria

- WHEN an operator builds a two-Host GFS2 cluster THE DOCUMENTATION SHALL provide Witness assignment, GFS2 activation, and Quorum panel validation on `two_node_clusters.rst`.
- THE DOCUMENTATION SHALL list expected Quorum panel values including 3 members, witness reachable, and no Sites row.
- THE DOCUMENTATION SHALL include timed failure behavior for Host loss, witness loss, combined loss, and Host-to-Host partition.
- THE DOCUMENTATION SHALL state that two-node GFS2 must not use Site Groups or `siteWitness`.
- THE DOCUMENTATION SHALL keep Agent quorum as the health authority when Corosync reports `Quorate: No`.
- THE TWO-NODE RUNBOOK SHALL NOT require opening `stretch_clusters.rst` for assignment or validation.
- IF stretch alphabetical site-winner logic is described THEN THE DOCUMENTATION SHALL not apply it to two-node partitions.

## Boundaries

- Topology comparison table belongs to `docs-hvm-quorum-topology-model`.
- Retargeting `workers.rst` and HVM landing discovery belongs to `docs-hvm-witness-discovery-crosslinks`.
- Do not rewrite stretch Scenario 4 site failure.
- Do not document NFS-only two-host clusters as GFS2 quorum clusters.
- Do not copy Worker package or `morpheus-worker.rb` snippets onto the two-node page; those stay in `workers.rst`.

## Risks

- Copying stretch T+60s site arbitration onto a two-Host partition would be the original field complaint in reverse.
- Documenting the create-form Witness field as required at create time contradicts both stretch and building-clusters sequencing.
- Heartbeat 140s versus quorum 60s are easy to collapse into one timeout; keep them distinct.

## Validation

- Align 2-of-3 vote counts with `neededForQuorum = (totalNodes / 2) + 1` for three members.
- Confirm GFS2-last activation against `MvmHostService.shouldSendQuorumInfo()`.
- Confirm Witness-on-edit against `ComputeClusterService` `witness.id` binding.
- Confirm no-Sites expected UI against `_summaryQuorum.gsp` `g:if test="${clusterSummary.quorumStats.sites}"`.
- Build `two_node_clusters` and `failure_scenarios` HTML and confirm new headings render.
