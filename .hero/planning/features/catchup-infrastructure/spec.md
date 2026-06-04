---
title: "Catch-Up: Infrastructure"
type: feature
slug: catchup-infrastructure
status: planning
priority: high
horizon: now
parent: docs-catchup-812
---

# Catch-Up: Infrastructure

## Purpose

Sync `infrastructure/` with 8.1.2 portal. Major content area — HVM clusters significantly expanded, Compute section, Boot/PXE, Trust.

## Key Gaps to Investigate

- **Clusters**: HVM Clusters (massive expansion — networking, storage, failover, hardware passthrough, GPU, affinity, vCPU placement), Kubernetes, Docker, EKS, GKE, OpenShift
- **Compute** section: Hosts, Virtual Machines, Containers, Resources, Bare Metal
- **Network**: Floating IPs, Security Groups (new sub-pages?)
- **Trust**: Integrating Hashicorp Vault, Installing External Cypher Appliance, Trust Integrations
- **Boot**: Full PXE/Boot section (Overview, Prerequisites, Troubleshooting, Mapping, Boot Menus, Answer Files, Images)
- **Load Balancers**: Orchestrating Load Balancers

## Acceptance Criteria

- [ ] HVM cluster docs fully expanded to match portal
- [ ] Compute section with all sub-pages present
- [ ] Boot/PXE section added if missing
- [ ] Trust section updated (Vault, external Cypher)
- [ ] All cluster types documented (K8s, Docker, EKS, GKE, OpenShift)
