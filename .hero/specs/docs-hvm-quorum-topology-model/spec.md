---
title: "HVM Quorum Topology Model for Two-Node GFS2 and Stretch"
slug: docs-hvm-quorum-topology-model
type: feature
status: completed
size: small
horizon: now
priority: high
domain: engineering
tags: [hvm, quorum, witness, gfs2, stretch-cluster, documentation]
parent: docs-hvm-witness-gfs2-quorum
relates-to: [docs-distributed-worker-witness, hvm-13-cluster-docs]
created: 2026-09-04
completed_at: 2026-09-04T16:34:58Z
---

# HVM Quorum Topology Model for Two-Node GFS2 and Stretch

## Context

Field feedback is that HVM witness and quorum docs still read as stretch-cluster first. `infrastructure/clusters/hvm/architecture.rst` describes majority of same-site peers and never names the two-node GFS2 vote. A two-node page exists, but architecture is the page operators use to interpret Quorum panel numbers.

`../morpheus-ui` already implements two topologies from one cluster Witness field:

- `MvmHostService.shouldSendQuorumInfo()` sends Agent quorum only for layout 1.3+ clusters that have at least one GFS2 datastore.
- `StatsService.sendQuorumDetailsToWorker()` and `sendQuorumDetailsToServer()` append the Distributed Worker as `witnessOnly: true` with `witnessUrl` derived from `DistributedWorker.applianceUrl` plus `witness/<cluster UUID>/`.
- If any Site Group exists (`HostVmGroupType.SITE_GROUP`), the worker is labeled `site: 'siteWitness'`.
- If no Site Groups exist, the worker is labeled `site: null` with the source comment `use this for 2 node gfs2 witness`.
- `_summaryQuorum.gsp` always shows a Witness row when a witness member exists. The Sites row and per-site host tables render only when `quorumStats.sites` is present.

The Manager does not switch topologies by host count. Adding Site Groups to a two-Host cluster changes the payload to stretch `siteWitness` behavior.

## Goal

Publish one source-backed comparison that operators can use to choose, identify, and interpret two-node GFS2 versus stretch quorum without mixing Site Group, `siteWitness`, or same-site peer rules.

## Kickoff

Adds the two-node GFS2 vs stretch quorum comparison to HVM architecture so operators stop reading witness as stretch-only.

**Status:** delivering — architecture table and chooser sentences are in; close after audit.

**Pick up at:** `/deliver docs-hvm-two-node-gfs2-operations` if operations content is not already on `two_node_clusters.rst`.

→ `.hero/planning/features/docs-hvm-quorum-topology-model/spec.md`

**Files:** `infrastructure/clusters/hvm/architecture.rst:47`, `infrastructure/clusters/hvm/hvm.rst:83`
**Skip:** do not copy stretch alphabetical site arbitration onto two-node GFS2.

## Approach

Keep `architecture.rst` as the canonical model. Keep stretch arbitration on `stretch_clusters.rst` and two-node procedures on `two_node_clusters.rst`. Scope the existing same-site peer bullet to stretch. Do not invent two-node cross-verification details that are not in Manager source.

Use customer-facing names in the published table:

- **Two-node GFS2** — two compute Hosts, one Distributed Worker, no Site Groups
- **Stretch** — two Site Groups plus a Distributed Worker labeled `siteWitness`

Do not publish internal field names (`witnessOnly`, `site: null`) in the operator table. Those remain in this spec as source evidence. The published page may mention `siteWitness` because stretch docs already warn operators not to create a group with that name.

## Changes

1. Update `infrastructure/clusters/hvm/architecture.rst` Quorum Algorithm.
   - After Majority Calculation, add a subsection **Witness topologies** with a comparison table:

     | | Two-node GFS2 | Stretch |
     |---|---|---|
     | Compute Hosts | Two Hosts | Minimum 6 Hosts (3 per site), documented on the stretch page |
     | Site Groups | None | One Site Group per physical site |
     | Witness | One Distributed Worker, quorum-only | One Distributed Worker in a third location, quorum-only |
     | How |morpheus| classifies the witness | No Site Groups present | Site Groups present; worker is assigned as `siteWitness` |
     | Votes | 3 members; majority is 2 | Site-level arbitration described on the stretch page |
     | Quorum panel | Witness row; no Sites row; flat Host table | Witness row; Sites row; Hosts grouped by site |
     | Activation | Layout 1.3 or later and at least one GFS2 datastore | Same GFS2 activation; Site Groups added after cluster create |

   - Change the Peer Communication bullet `Cross-verification: reachability is confirmed by a majority of same-site peers` so it applies to stretch Site Groups only. For two-node GFS2, state that both Hosts ping each other on TCP 7443 and must reach the Worker URL; do not claim same-site cross-verification.
   - Clarify `neededForQuorum = (totalNodes / 2) + 1` counts every Agent quorum member, including the witness on a two-node cluster (2 of 3).
   - State that Corosync `Quorate` is not the Agent quorum decision for layout 1.3 or later. Point to existing notes on `building_clusters.rst` and `troubleshooting.rst` rather than duplicating command blocks.
   - Warn that creating Site Groups on a two-node GFS2 cluster switches the witness classification to stretch `siteWitness`. Link `:doc:`stretch_clusters`` and `:doc:`two_node_clusters``.

2. Add chooser sentences, not procedure, on the topology entry pages.
   - `infrastructure/clusters/hvm/hvm.rst` **How to Use This Guide**: add bullets for two-node GFS2 (`:doc:`two_node_clusters``) and stretch (`:doc:`stretch_clusters``).
   - `infrastructure/clusters/hvm/two_node_clusters.rst` intro: keep the existing “this is not a stretch cluster” limitation and add one sentence pointing to the architecture comparison for vote math and Quorum panel fields.
   - `infrastructure/clusters/hvm/stretch_clusters.rst` intro: keep the existing pointer to `two_node_clusters` and add one sentence that stretch begins when Site Groups exist.

3. Do not retarget `administration/integrations/workers.rst` in this spec. That assignment link is `docs-hvm-witness-discovery-crosslinks`.

## Acceptance Criteria

- THE DOCUMENTATION SHALL describe two-node GFS2 and stretch as distinct witness topologies that share a Distributed Worker and GFS2 activation condition.
- THE DOCUMENTATION SHALL state that two-node GFS2 does not use Site Groups or the `siteWitness` designation.
- THE DOCUMENTATION SHALL state that Agent quorum is sent only for layout 1.3 or later clusters with a GFS2 datastore.
- THE DOCUMENTATION SHALL explain two-node majority as 2 of 3 members, counting the witness.
- THE DOCUMENTATION SHALL identify Witness as a common Quorum panel field and Sites as stretch-only.
- IF two-node same-site cross-verification is not in Manager source THEN THE DOCUMENTATION SHALL not copy that stretch rule onto two-node GFS2.
- WHEN an operator creates Site Groups on a two-node cluster THE DOCUMENTATION SHALL warn that the witness becomes a stretch `siteWitness`.

## Boundaries

- Timed Host/witness failure procedures belong to `docs-hvm-two-node-gfs2-operations`.
- Worker assignment links, landing-page discovery beyond the chooser bullets, and Site Group page warnings belong to `docs-hvm-witness-discovery-crosslinks`.
- Do not duplicate Worker package, container, key, or TLS install.
- Do not document NFS-only clusters as GFS2 quorum clusters.
- Do not claim the product rejects a witness on clusters other than two Hosts; the supported customer topology is two Hosts plus witness, while the code discriminator is Site Group presence.

## Risks

- Publishing `site: null` or `witnessOnly` in customer docs will look like API reference, not operator guidance.
- Leaving the same-site peer bullet unmodified will keep architecture stretch-first.
- Treating any GFS2 cluster with a witness as two-node, including clusters that already have Site Groups, will mix the topologies.

## Validation

- Trace table rows to `StatsService` lines 259–277 and 302–316, `MvmHostService.shouldSendQuorumInfo()`, and `_summaryQuorum.gsp` Witness versus Sites `g:if` blocks.
- Confirm the architecture page does not instruct operators to open stretch docs to interpret a two-node Quorum panel.
- Build Sphinx HTML and check the new table and chooser links resolve.
