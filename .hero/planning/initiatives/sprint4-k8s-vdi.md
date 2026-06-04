---
type: initiative
status: planning
horizon: now
title: "Sprint 4: Kubernetes, Containers & VDI"
tags: [9.0.0, kubernetes, containers, vdi, sprint-4]
priority: 4
---

# Sprint 4: Kubernetes, Containers & VDI

## Priority: HIGH — Key Platform Features with Documentation Gaps

## Scope

### Kubernetes & Containers (Expand/Create)
- **Helm Provisioning** — Helm chart deployment as a provisioning type
- **Helm Upgrade Workflow** — In-place upgrades of deployed Helm apps (`supportsUpgrade`)
- **Kubernetes Storage** — PV/PVC/StorageClass management
- **Kubernetes Registry** — Container registry integration within K8s
- **Kubernetes Jobs** — Job, CronJob, Deploy Job types (3 distinct types)
- **Kubernetes Job Executor** — Running jobs from within Morpheus
- **External Kubernetes** — Importing external clusters vs provisioned
- **Kubernetes Spec Blueprint** — Dedicated blueprint type (no doc page)

### VDI (Expand Existing)
- **VDI Apps** — Application management (distinct from pools)
- **VDI Gateways** — Gateway configuration and management
- **VDI Allocations** — Allocation management

### Cloud Integrations (New Guides)
- **PowerVC** — Full cloud module, no integration guide
- **MVM Cloud** — Full module, no integration guide (distinct from MVM clusters)

## Source Code

- K8s: `HelmProvisionService`, `KubernetesStorageService`, `KubernetesRegistryService`, `KubernetesJobExecutorService`, `ExternalKubernetesHostService`
- VDI: `VdiAppsController`, `VdiGatewaysController`, `VdiAppService`, `VdiGatewayService`
- Clouds: `clouds/powervc/`, `clouds/mvm/`
