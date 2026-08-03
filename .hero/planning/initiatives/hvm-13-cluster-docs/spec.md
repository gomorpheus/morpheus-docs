---
title: "Unified HVM Cluster Documentation"
slug: hvm-13-cluster-docs
type: initiative
status: delivering
horizon: now
tags: [hvm, clusters, layouts, consolidation]
priority: 1
---

# Unified HVM Cluster Documentation

## Priority: CRITICAL - Consolidate Supported Layouts

Maintain one canonical HVM cluster guide for all supported layouts. Shared workflows must be documented once, with an authoritative support matrix and notices at the procedures that differ by layout.

## Supported Layouts

- **Legacy (1.2 and earlier)** - Ubuntu 22.04, Pacemaker, and Open vSwitch (OVS)
- **1.3** - HVM OS/Ubuntu 24.04, agent-based quorum, and OVS networking
- **2.0** - HVM OS 26.04, agent-based quorum, Virtual Switch networking, and `hvmcli`

## Key Changes from Legacy Layouts

- **Pacemaker removed** — replaced by Morpheus agent's own quorum/fencing
- **GFS2 renamed** — now "HPE Clustered Datastore (Shared LUN)" in UI
- **New quorum system** — agent-based with cross-verification, heartbeat failover
- **Stretch cluster support** — multi-site with witness nodes, deterministic arbitration
- **Layout 1.3** — Ubuntu 24.04, no Pacemaker installed on new clusters
- **Diagnostics** — `pcs` commands replaced by `dlm_tool`, `corosync-quorumtool`, agent `/quorum` endpoint

## Scope

### Documentation Structure
- One HVM cluster landing page and topic tree
- One layout and operating-system support matrix
- Shared architecture, lifecycle, VM, storage, placement, and monitoring procedures
- Scoped notices for layout-specific behavior
- A supported legacy appendix for operations that do not apply to current layouts
- Links to the standalone `hvmcli` command reference rather than duplicated command documentation

### Architecture Overview
- Stack components (Corosync, DLM, Morpheus agent)
- Quorum algorithm (ping, cross-verification, majority)
- Heartbeat failover system
- APD protection
- Designated coordinator election
- Key timing constants

### Building New Clusters
- Prerequisites by layout and HVM OS version
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

### Networking
- OVS workflows for Legacy and layout 1.3
- Virtual Switch workflows for layout 2.0
- Migration considerations between networking models

### Failure Scenarios
- Single host failure
- Storage partition (APD)
- Network partition
- Stretch site failure
- Layout 1.2 → 1.3 upgrade path

## Sources

- Confluence: https://hpe.atlassian.net/wiki/spaces/MPS/pages/4981096781
- Word doc: Stretched_Cluster_rev2.0.docx (witness deployment, site groups, quorum verification)
