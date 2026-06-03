---
title: "Tier Feature Comparison Matrix: Essentials vs Advanced vs Enterprise"
type: context
status: active
scope: "*"
---

# Tier Feature Comparison Matrix (8.1.2)

## Supported Hypervisors & Private Clouds

| Feature / Integration | VM Essentials | Advanced | Enterprise |
|---|---|---|---|
| VMware vCenter | Supported | Supported | Supported |
| HVM (KVM-based) | Supported | Supported | Supported |
| Standalone ESXi | Not Supported | Not Supported | Supported |
| Nutanix AHV | Not Supported | Not Supported | Supported |
| Microsoft Hyper-V / SCVMM | Not Supported | Not Supported | Supported |
| OpenStack | Not Supported | Not Supported | Supported |
| Nutanix Prism Central | Not Supported | Not Supported | Supported |
| Azure Stack | Not Supported | Not Supported | Supported |
| XenServer | Not Supported | Not Supported | Supported |
| Oracle VM / OLVM | Not Supported | Not Supported | Supported |
| Bare Metal | Not Supported | Not Supported | Supported |

## Supported Public Clouds

| Feature / Integration | VM Essentials | Advanced | Enterprise |
|---|---|---|---|
| Amazon AWS | Not Supported | Not Supported | Supported |
| Microsoft Azure | Not Supported | Not Supported | Supported |
| Google Cloud Platform (GCP) | Not Supported | Not Supported | Supported |
| Alibaba Cloud | Not Supported | Not Supported | Supported |
| Oracle Cloud (OCI) | Not Supported | Not Supported | Supported |
| IBM Cloud | Not Supported | Not Supported | Supported |
| DigitalOcean | Not Supported | Not Supported | Supported |
| UpCloud | Not Supported | Not Supported | Supported |

## Automation & Orchestration (Task Types)

| Task Type / Feature | VM Essentials | Advanced | Enterprise |
|---|---|---|---|
| Bash / Shell Script | Supported | Supported | Supported |
| PowerShell Script | Supported | Supported | Supported |
| Ansible (Direct Integration) | Not Supported | Supported | Supported |
| Terraform (Blueprints/Provider) | Not Supported | Not Supported | Supported |
| Chef / Puppet | Not Supported | Supported | Supported |
| Python / Groovy Tasks | Not Supported | Supported | Supported |
| vRealize Orchestrator (vRO) | Not Supported | Supported | Supported |
| Workflows | Not Supported | Supported | Supported |
| Service Catalogue | Not Supported | Supported | Supported |
| Blueprints – App | Not Supported | Not Supported | Supported |
| Custom Instance Types | Not Supported | Supported | Supported |
| Cypher (Secrets Management) | Supported | Supported | Supported |
| REST API / CLI Access | Supported | Supported | Supported |

## Containers & Kubernetes

| Feature / Integration | VM Essentials | Advanced | Enterprise |
|---|---|---|---|
| Docker Host Provisioning | Supported | Supported | Supported |
| Morpheus Kubernetes (HKS) on Manual | Not Supported | Supported | Supported |
| Morpheus Kubernetes (HKS) on HVM | Not Supported | Supported | Supported |
| Morpheus Kubernetes (HKS) on VMware | Not Supported | Supported | Supported |
| HA HKS (requires LB support) | Not Supported | Supported | Supported |
| Public K8s (EKS, AKS, GKE) | Not Supported | Not Supported | Supported |
| External K8s Clusters | Not Supported | Not Supported | Supported |
| OpenShift Virt. | Not Supported | Not Supported | Supported |

## Software Defined Networking

Note: to be limited by contractual language until technical limits in place.

| Feature | VM Essentials | Advanced | Enterprise |
|---|---|---|---|
| Shared Private Networking (via OVS) — VxLAN, no ingress/egress (manual via dual-homed instance), no CN2 required | Not Supported | Supported | Supported |
| Overlay (via CN2 plugin) | Not Supported | Supported | Supported |
| Routing (via CN2 plugin) | Not Supported | Supported | Supported |
| Load Balancing (via CN2 plugin) | Not Supported | Supported | Supported |
| Security & Micro-Segmentation (via CN2 plugin) | Not Supported | Not Supported* | Supported |
| NAT & VPN / Gateway Services (via CN2 plugin) | Not Supported | Supported | Supported |
| Observability & Support Day2 (via CN2 plugin) | Not Supported | Supported | Supported |

## AI

| Feature | VM Essentials | Advanced | Enterprise |
|---|---|---|---|
| MCP | Supported | Supported | Supported |
| AI Workflow (BYOM) | Not Supported | Supported | Supported |
| AI Appliance Monitoring (BYOM, future feature) | Not Supported | Supported | Supported |
| AI Chat (BYOM) | Not Supported | Not Supported | Supported |
| Proactive Agent (BYOM) | Not Supported | Not Supported | Supported |

## On-Prem Financial Management (FinOps)

| Feature | VM Essentials | Advanced | Enterprise |
|---|---|---|---|
| Cost Visibility | Standard (Resource usage only) | Standard (Resource usage only) | Advanced (Full Cloud Costing) |
| Rightsizing Recommendations | Not Supported | Not Supported | Supported (vCenter/KVM/Public) |
| Invoicing Engine | Not Supported | Not Supported | Supported |
| Budgetary Policies | Not Supported | Not Supported | Dollar-based Budget Enforcement |
| Markup / Price Sets | Basic Plans | Basic Plans | Advanced Tiered Pricing & Markup |
| Guidance / Cloud Optimization | Not Supported | Not Supported | AI-driven Savings Recommendations |

## Multi-Tenancy & MSP Capabilities

| Feature | VM Essentials | Advanced | Enterprise |
|---|---|---|---|
| Single Tenant | Supported | Supported | Supported |
| Sub-Tenant Creation | Not Supported | Not Supported | Full (unlimited isolated tenants) |
| Tenant Roles | Standard RBAC | Standard RBAC | Advanced Multi-Tenant RBAC |
| White Labeling | Not Supported | Not Supported | Advanced (Per-tenant branding/URLs) |
| Tenant-Specific Currencies | Not Supported | Not Supported | Supported |
| Tenant Resource Sharing | Not Supported | Not Supported | Supported |
| Service Provider Features | Not Supported | Not Supported | Supported (MSP specific tools) |

## Platform Features & Governance

| Feature / Integration | VM Essentials | Advanced | Enterprise |
|---|---|---|---|
| Identity Management (AD/LDAP/SAML) | Supported | Supported | Supported |
| RBAC (Role Based Access Control) | Supported | Supported | Supported |
| Personas | Not Supported | Supported | Supported |
| ServiceNow / ITSM Integration | Not Supported | Not Supported | Supported |
| Compliance & Policy Engine | Not Supported | Not Supported | Supported |
| Workload Monitoring/Logging | Not Supported | Supported | Supported |
| Reports and Analytics | Not Supported | Supported | Supported |
| Distributed Worker | Not Supported | Supported | Supported |

## Integrations

Note: not blocked in software, would be restricted by downstream features + contract/support.

| Feature / Integration | VM Essentials | Advanced | Enterprise |
|---|---|---|---|
| Load Balancers | Not Supported | Supported | Supported |
| Backups | Supported | Supported | Supported |
| IPAM | Supported | Supported | Supported |
| ITSM | Not Supported | Not Supported | Supported |
| SCM | Not Supported | Supported | Supported |
| Clouds | Not Supported | Not Supported | Supported |
| Guidance | Not Supported | Not Supported | Supported |
