---
type: initiative
slug: sprint3-storage-lb-infra
status: completed
horizon: now
title: "Sprint 3: Storage, Load Balancers & Infrastructure Operations"
tags: [9.0.0, storage, load-balancers, infrastructure, sprint-3]
priority: 3
---

# Sprint 3: Storage, Load Balancers & Infrastructure Operations

## Priority: HIGH — Core Infrastructure Features Undocumented

## Scope

### Storage (New/Expanded Pages)
- **Share Access Control** — Managing access to file shares
- **Storage Hosts** — Host management under storage servers
- **Storage Namespaces** — Namespace management
- **Storage Groups** — Group management
- **HPE 3PAR/Primera** — Dedicated integration guide (code exists)
- **Volume Resize** — Volume resize and replica activation workflows

### Load Balancers (New Pages)
- **A10 Load Balancer** — Full integration guide
- **Avi (NSX ALB)** — Integration guide
- **KubeVIP** — K8s VIP load balancer
- **LB Profiles** — Profile management
- **LB Scripts** — Script management
- **LB Policies & Rules** — Policy and rule configuration

### Infrastructure Operations (New/Expanded)
- **Server Move/VM Migration** — Move VMs between targets (distinct from bulk migration)
- **Server Placement** — VM placement configuration
- **Server Devices** — Attach/detach/assign devices
- **Compute Chassis** — Chassis management view
- **Host-VM Groups** — Group management on clusters
- **iSCSI Targets** — Target management on clusters
- **Addon Packages** — Install/upgrade/delete lifecycle
- **Cluster Updates** — Execute update workflow
- **Snapshots** — Standalone snapshot management (beyond MVM context)
- **Resource Pool Groups** — Grouping and export

## Source Code

- Storage: `StorageShareAccessController`, `StorageHostsController`, `ThreeParDatastoreService`
- LB: `A10LoadBalancerService`, `AviLoadBalancerService`, `LoadBalancerProfilesController`, `LoadBalancerPoliciesController`
- Infra: `HostVmGroupsController`, `ServerGroupIScsiTargetsController`, `ComputeChassisController`, `AddonPackagesController`
