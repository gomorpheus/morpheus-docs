---
title: "HVM 1.3 Cluster Layouts Documentation"
slug: hvm-13-cluster-docs
type: initiative
status: delivering
horizon: now
tags: [9.0.0, hvm, clusters, pacemaker-removal]
priority: 1
---

# HVM 1.3 Cluster Layouts Documentation

## Priority: CRITICAL — Major Architecture Change

HVM clusters in Morpheus 9.0 replace Pacemaker with an agent-based quorum system (Corosync + DLM + Morpheus agent QuorumCheckService). GFS2 is renamed to "HPE Clustered Datastore (Shared LUN)". Layout 1.3 diagnostics no longer use `pcs` commands.

## Key Changes from 1.2

- **Pacemaker removed** — replaced by Morpheus agent's own quorum/fencing
- **GFS2 renamed** — now "HPE Clustered Datastore (Shared LUN)" in UI
- **New quorum system** — agent-based with cross-verification, heartbeat failover
- **Stretch cluster support** — multi-site with witness nodes, deterministic arbitration
- **Layout 1.3** — Ubuntu 24.04, no Pacemaker installed on new clusters
- **Diagnostics** — `pcs` commands replaced by `dlm_tool`, `corosync-quorumtool`, agent `/quorum` endpoint

## Scope

### Architecture Overview
- Stack components (Corosync, DLM, Morpheus agent)
- Quorum algorithm (ping, cross-verification, majority)
- Heartbeat failover system
- APD protection
- Designated coordinator election
- Key timing constants

### Building New Clusters
- Prerequisites (Ubuntu 24.04, network, storage)
- Cluster creation wizard workflow
- Automated provisioning phases
- HPE Clustered Datastore (Shared LUN) setup
- Heartbeat datastore configuration
- Health verification

### Stretch Clusters & Witness Nodes
- Witness deployment (Distributed Worker)
- Site group configuration
- Arbitration algorithm (alphabetical, deterministic)
- Vote adjustment on failure/recovery
- Recovery timeline

### Troubleshooting
- Diagnostic commands (replacing pcs)
- UI navigation for cluster health
- Common issues and resolutions
- Agent state files reference
- Emergency procedures

### Failure Scenarios
- Single host failure
- Storage partition (APD)
- Network partition
- Stretch site failure
- Layout 1.2 → 1.3 upgrade path

## Sources

- Confluence: https://hpe.atlassian.net/wiki/spaces/MPS/pages/4981096781
- Word doc: Stretched_Cluster_rev2.0.docx (witness deployment, site groups, quorum verification)
