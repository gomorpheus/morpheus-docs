---
title: "Witness Discovery Paths for Two-Node GFS2"
slug: docs-hvm-witness-discovery-crosslinks
type: feature
status: completed
size: small
horizon: now
priority: high
domain: engineering
tags: [hvm, witness, gfs2, navigation, documentation]
parent: docs-hvm-witness-gfs2-quorum
depends-on: [docs-hvm-quorum-topology-model]
relates-to: [docs-distributed-worker-witness, docs-distributed-worker-guide]
created: 2026-09-04
completed_at: 2026-09-04T16:34:59Z
---

# Witness Discovery Paths for Two-Node GFS2

## Context

The two-node page is not the default next step from the pages operators actually open. `administration/integrations/workers.rst` documents both topologies, then sends assignment and quorum validation only to `stretch_clusters` (line 316). `host_vm_groups.rst` documents Site Groups with no stretch-only warning. `troubleshooting.rst` lists Site information as a generic Quorum panel field. Edge-site copy says “two-node or stretch” but links only the Worker install page.

`docs-hvm-quorum-topology-model` owns the architecture comparison and chooser bullets on `hvm.rst`. This spec owns every remaining stretch-default link.

## Goal

Make two-node GFS2 the next step from Worker assignment, Site Groups, troubleshooting, building clusters, and edge-site copy unless the operator has Site Groups.

## Kickoff

Stops generic witness assignment from dumping operators into stretch-cluster docs.

**Status:** delivering — Worker, Site Group, troubleshooting, building-clusters, and edge links are split by topology.

**Pick up at:** HVM engineering review of two-node vote math and Site Group exclusion.

→ `.hero/planning/features/docs-hvm-witness-discovery-crosslinks/spec.md`

**Files:** `administration/integrations/workers.rst:316`, `infrastructure/clusters/hvm/host_vm_groups.rst:53`
**Skip:** do not merge two-node and stretch into one page; do not duplicate Worker install.

## Approach

Split next-step links by topology. Keep Worker URL, TLS, and Host-to-Worker reachability text. Use |AdmIntDis|, |InfClu|, and existing `:doc:` targets. Do not rewrite runbooks owned by the other children.

## Changes

1. Update `administration/integrations/workers.rst` **Witness Configuration**.
   - Keep the sentence that a Distributed Worker can serve two-node GFS2 and stretch.
   - Replace the single next-step sentence currently pointing only at `:doc:`/infrastructure/clusters/hvm/stretch_clusters`` with:
     - Two-Host GFS2, no Site Groups → `:doc:`/infrastructure/clusters/hvm/two_node_clusters``
     - Site Groups / multi-site stretch → `:doc:`/infrastructure/clusters/hvm/stretch_clusters``
   - Optionally retarget the capability-matrix “Assignment and traffic path” cell (line 34) from generic “Select the Worker as the cluster witness” to the same two links. Do not expand that cell into a runbook.

2. Update `infrastructure/clusters/hvm/host_vm_groups.rst` Site Group type.
   - On the **Site Group** bullet under Creating a Host-VM Group, state that Site Groups are for stretch clusters.
   - Add a warning: do not create Site Groups on a two-node GFS2 cluster; adding them switches the Distributed Worker witness to `siteWitness`. Link `:doc:`two_node_clusters`` and `:doc:`stretch_clusters``.
   - Do not document stretch arbitration here.

3. Update `infrastructure/clusters/hvm/troubleshooting.rst` Quick Health Check.
   - Keep Witness status as a common Quorum panel field.
   - Qualify **Site information** as stretch-only (present when Site Groups exist).
   - In the Corosync note that already mentions stretch and two-node GFS2, add links to both runbooks rather than leaving them as unnamed topologies.

4. Tighten remaining entry points without duplicating procedures.
   - `infrastructure/clusters/hvm/building_clusters.rst` Witness field (line 69): change “using the applicable witness procedure” to explicit `:doc:`two_node_clusters`` and `:doc:`stretch_clusters`` links.
   - `getting_started/guides/edge_site_management.rst` HVM quorum witness bullets: keep the Worker install link and add the two HVM runbook links so edge readers are not stuck on `workers.rst`.

5. Do not re-edit `hvm.rst` chooser bullets if `docs-hvm-quorum-topology-model` already added them. If they are missing at delivery time, add the two how-to bullets there as well.

## Acceptance Criteria

- WHEN Worker docs describe cluster witness assignment THE DOCUMENTATION SHALL link two-node GFS2 and stretch as separate next steps.
- THE DOCUMENTATION SHALL NOT use `stretch_clusters` as the default destination for generic “assign a witness” instructions.
- WHEN Site Groups are documented THE DOCUMENTATION SHALL warn that they are stretch-only and change two-node witness classification if added.
- THE TROUBLESHOOTING QUORUM PANEL LIST SHALL mark Sites as stretch-only.
- THE DOCUMENTATION SHALL leave Worker URL, TLS, and Host-to-Worker reachability warnings in place.

## Boundaries

- Architecture comparison table belongs to `docs-hvm-quorum-topology-model`.
- Two-node timed failures and Quorum panel expected values belong to `docs-hvm-two-node-gfs2-operations`.
- Do not duplicate Worker package or container install.
- Do not merge the two runbooks.

## Risks

- Leaving `workers.rst` line 316 unchanged recreates the field complaint after the other children land.
- Edge-site copy that says both topologies but links only Worker install still hides the two-node HVM runbook.
- Over-linking Site Groups from every HVM page will bury affinity/anti-affinity use cases; keep the warning on the Site Group type bullet.

## Validation

- Grep `stretch_clusters`, `siteWitness`, and `witness` in `infrastructure/clusters/hvm`, `administration/integrations/workers.rst`, and `getting_started/guides/edge_site_management.rst`. Every generic assignment sentence must offer both runbooks or a topology chooser.
- Build Sphinx HTML and confirm Worker → two-node and Site Groups → two-node links resolve.
