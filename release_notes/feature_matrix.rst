.. _feature-matrix:

Feature Comparison by License Tier
====================================

|morpheus| is available in three license tiers: **VM Essentials**, **Advanced**, and **Enterprise**. The table below provides a summary of feature availability by tier.

.. NOTE:: Features marked as "Supported" are included in the license tier. Features marked as "Not Supported" are not available at that tier. Contact your HPE representative for full licensing details.

Supported Hypervisors & Private Clouds
---------------------------------------

.. list-table::
   :widths: 40 20 20 20
   :header-rows: 1

   * - Feature
     - VM Essentials
     - Advanced
     - Enterprise
   * - VMware vCenter
     - |yes|
     - |yes|
     - |yes|
   * - HVM (KVM-based)
     - |yes|
     - |yes|
     - |yes|
   * - Standalone ESXi
     - |no|
     - |no|
     - |yes|
   * - Nutanix AHV
     - |no|
     - |no|
     - |yes|
   * - Microsoft Hyper-V / SCVMM
     - |no|
     - |no|
     - |yes|
   * - OpenStack
     - |no|
     - |no|
     - |yes|
   * - Azure Stack
     - |no|
     - |no|
     - |yes|
   * - XenServer
     - |no|
     - |no|
     - |yes|
   * - Oracle VM / OLVM
     - |no|
     - |no|
     - |yes|
   * - Bare Metal
     - |no|
     - |no|
     - |yes|

Public Clouds
--------------

.. list-table::
   :widths: 40 20 20 20
   :header-rows: 1

   * - Feature
     - VM Essentials
     - Advanced
     - Enterprise
   * - Amazon AWS
     - |no|
     - |no|
     - |yes|
   * - Microsoft Azure
     - |no|
     - |no|
     - |yes|
   * - Google Cloud Platform (GCP)
     - |no|
     - |no|
     - |yes|
   * - Oracle Cloud (OCI)
     - |no|
     - |no|
     - |yes|
   * - IBM Cloud
     - |no|
     - |no|
     - |yes|

Automation & Orchestration
---------------------------

.. list-table::
   :widths: 40 20 20 20
   :header-rows: 1

   * - Feature
     - VM Essentials
     - Advanced
     - Enterprise
   * - Bash / Shell Script Tasks
     - |yes|
     - |yes|
     - |yes|
   * - PowerShell Script Tasks
     - |yes|
     - |yes|
     - |yes|
   * - Ansible Integration
     - |no|
     - |yes|
     - |yes|
   * - Terraform (Blueprints/Provider)
     - |no|
     - |no|
     - |yes|
   * - Chef / Puppet
     - |no|
     - |yes|
     - |yes|
   * - Python / Groovy Tasks
     - |no|
     - |yes|
     - |yes|
   * - Workflows
     - |no|
     - |yes|
     - |yes|
   * - Service Catalog
     - |no|
     - |yes|
     - |yes|
   * - Custom Instance Types
     - |no|
     - |yes|
     - |yes|
   * - Application Blueprints
     - |no|
     - |no|
     - |yes|
   * - Cypher (Secrets Management)
     - |yes|
     - |yes|
     - |yes|
   * - REST API / CLI Access
     - |yes|
     - |yes|
     - |yes|

Containers & Kubernetes
------------------------

.. list-table::
   :widths: 40 20 20 20
   :header-rows: 1

   * - Feature
     - VM Essentials
     - Advanced
     - Enterprise
   * - Docker Host Provisioning
     - |yes|
     - |yes|
     - |yes|
   * - HPE Kubernetes Service (HKS) on HVM
     - |no|
     - |yes|
     - |yes|
   * - HKS on VMware
     - |no|
     - |yes|
     - |yes|
   * - HA HKS (requires load balancer)
     - |no|
     - |yes|
     - |yes|
   * - Public K8s (EKS, AKS, GKE)
     - |no|
     - |no|
     - |yes|
   * - External K8s Clusters
     - |no|
     - |no|
     - |yes|
   * - OpenShift Virtualization
     - |no|
     - |no|
     - |yes|

AI & Automation Intelligence
-----------------------------

.. list-table::
   :widths: 40 20 20 20
   :header-rows: 1

   * - Feature
     - VM Essentials
     - Advanced
     - Enterprise
   * - MCP Server
     - |yes|
     - |yes|
     - |yes|
   * - AI Workflow (BYOM)
     - |no|
     - |yes|
     - |yes|
   * - AI Appliance Monitoring (BYOM)
     - |no|
     - |yes|
     - |yes|
   * - AI Chat (BYOM)
     - |no|
     - |no|
     - |yes|
   * - Proactive Agent (BYOM)
     - |no|
     - |no|
     - |yes|

Financial Management (FinOps)
------------------------------

.. list-table::
   :widths: 40 20 20 20
   :header-rows: 1

   * - Feature
     - VM Essentials
     - Advanced
     - Enterprise
   * - Cost Visibility
     - Resource usage only
     - Resource usage only
     - Full cloud costing
   * - Rightsizing Recommendations
     - |no|
     - |no|
     - |yes|
   * - Invoicing Engine
     - |no|
     - |no|
     - |yes|
   * - Budgetary Policies
     - |no|
     - |no|
     - |yes|
   * - Markup / Price Sets
     - Basic plans
     - Basic plans
     - Advanced tiered pricing
   * - Guidance / Optimization
     - |no|
     - |no|
     - |yes|

Multi-Tenancy & MSP
---------------------

.. list-table::
   :widths: 40 20 20 20
   :header-rows: 1

   * - Feature
     - VM Essentials
     - Advanced
     - Enterprise
   * - Single Tenant
     - |yes|
     - |yes|
     - |yes|
   * - Sub-Tenant Creation
     - |no|
     - |no|
     - |yes|
   * - White Labeling
     - |no|
     - |no|
     - |yes|
   * - Tenant-Specific Currencies
     - |no|
     - |no|
     - |yes|
   * - Tenant Resource Sharing
     - |no|
     - |no|
     - |yes|
   * - Service Provider Features
     - |no|
     - |no|
     - |yes|

Platform Features & Governance
-------------------------------

.. list-table::
   :widths: 40 20 20 20
   :header-rows: 1

   * - Feature
     - VM Essentials
     - Advanced
     - Enterprise
   * - Identity Management (AD/LDAP/SAML)
     - |yes|
     - |yes|
     - |yes|
   * - RBAC (Role Based Access Control)
     - |yes|
     - |yes|
     - |yes|
   * - Personas
     - |no|
     - |yes|
     - |yes|
   * - ServiceNow / ITSM Integration
     - |no|
     - |no|
     - |yes|
   * - Compliance & Policy Engine
     - |no|
     - |no|
     - |yes|
   * - Workload Monitoring/Logging
     - |no|
     - |yes|
     - |yes|
   * - Reports and Analytics
     - |no|
     - |yes|
     - |yes|
   * - Distributed Worker
     - |no|
     - |yes|
     - |yes|

Integrations
-------------

.. list-table::
   :widths: 40 20 20 20
   :header-rows: 1

   * - Feature
     - VM Essentials
     - Advanced
     - Enterprise
   * - Load Balancers
     - |no|
     - |yes|
     - |yes|
   * - Backups
     - |yes|
     - |yes|
     - |yes|
   * - IPAM
     - |yes|
     - |yes|
     - |yes|
   * - ITSM
     - |no|
     - |no|
     - |yes|
   * - SCM (Source Control)
     - |no|
     - |yes|
     - |yes|
   * - Cloud Integrations
     - |no|
     - |no|
     - |yes|
   * - Guidance
     - |no|
     - |no|
     - |yes|

.. |yes| unicode:: U+2713 .. check mark
.. |no| unicode:: U+2717 .. cross mark
