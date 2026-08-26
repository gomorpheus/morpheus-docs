Cloud Integration Coverage
==========================

Overview
--------

|morpheus| supports over 25 cloud integrations spanning public, private, and hybrid environments. The depth of feature coverage varies by cloud type depending on the maturity of the integration and the capabilities exposed by the underlying platform API.

This page classifies supported clouds into three tiers based on the breadth of |morpheus| management capabilities available, and provides a detailed feature matrix for evaluating cloud-specific functionality.

This feature matrix is not a version certification matrix. Use :ref:`compatibility` for qualified external-product versions. Products and operating models that are absent from both references do not gain a support claim by similarity to a listed hypervisor.

SimpliVity Boundary
-------------------

No SimpliVity-specific Cloud integration or documented eight-node multi-session management contract is included in this documentation. In particular, this guide does not publish supported concurrent-session counts, sequencing, recovery behavior, or an eight-node SVT qualification. Manage the underlying VMware environment only within the documented VMware vCenter integration boundary, and manage SimpliVity-specific lifecycle operations with HPE SimpliVity tools and guidance. Contact HPE for the current interoperability statement before using an eight-node or multi-session design.

.. tip::

   The tier classification reflects |morpheus| integration depth, not the quality of the underlying cloud platform. A Tier 2 cloud may be the ideal choice for your environment depending on your workload requirements.

Cloud Tier Classification
-------------------------

Tier 1 |---| Full Lifecycle Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tier 1 clouds offer the deepest |morpheus| integration with comprehensive lifecycle management across provisioning, networking, security, costing, containers, and governance. These integrations support full CRUD operations on cloud resources, bi-directional synchronization, and advanced features such as Kubernetes orchestration, native load balancing, and multitenancy.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Cloud
     - Key Differentiators
   * - **HVM (HPE VM)**
     - KVM hypervisor management, bridge/VLAN/OVS network CRUD, storage profiles, HA clustering, live migration, brownfield, auto-scaling
   * - **Amazon Web Services (AWS)**
     - VPC/Network CRUD, Security Groups, EKS, ELB/ALB, CloudFormation, Terraform, Route53, IAM, RDS, costing with reservations
   * - **Microsoft Azure (Public)**
     - Network/Subnet CRUD, Security Groups, AKS, ARM Blueprints, Scale Sets, Azure LB, Storage, Marketplace, costing with reservations
   * - **VMware vCenter**
     - Distributed Switches, DRS Clusters, Affinity Groups, NSX/NSX-T integration, image conversion, brownfield migrations, multitenancy

Tier 2 |---| Core Cloud Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tier 2 clouds provide solid provisioning, brownfield discovery, and backup capabilities with partial networking and costing support. Network management may be limited to read-only synchronization or basic operations. These integrations cover the most common day-to-day operations but may lack advanced network lifecycle management, native security groups, or full billing integration.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Cloud
     - Notes
   * - **Google Cloud Platform (GCP)**
     - Provisioning, snapshots, brownfield, costing, right-sizing. Limited network lifecycle management.
   * - **OpenStack**
     - Security groups, floating IPs, network lifecycle, LBaaS, Manila file services, brownfield.
   * - **Nutanix Prism Element**
     - Brownfield, Kubernetes, costing, migrations, auto scaling. Delivered as external plugin.
   * - **Nutanix Prism Central**
     - Project scoping, brownfield, snapshots, cloud sync. Delivered as external plugin.
   * - **Hyper-V**
     - VM provisioning, discovery, Veeam integration. Networks are sync-only (no create/delete). No native security groups.
   * - **SCVMM**
     - Similar to Hyper-V with System Center integration. Veeam backup integration supported. Limited network management.
   * - **VMware vCloud Director (VCD)**
     - vApp support, brownfield, IP pools, multi-NIC, Kubernetes/Docker.
   * - **Open Telekom Cloud (OTC)**
     - OpenStack-based. Security groups, routers, floating IPs, LB, OBS.
   * - **Huawei Cloud**
     - OpenStack-based. Security groups, routers, floating IPs, LB, OBS, SFS.
   * - **Oracle Public Cloud**
     - VM provisioning, brownfield. Limited networking and costing.
   * - **PowerVC**
     - Power Systems provisioning. Security groups, networks, brownfield.
   * - **OLVM (Oracle Linux Virtualization Manager)**
     - VM provisioning, brownfield, snapshots, host monitoring, console.

Tier 3 |---| Essential Provisioning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tier 3 clouds support basic virtual machine provisioning and instance discovery. They are suitable for straightforward compute workloads but lack advanced management features such as network CRUD, costing, native security groups, or Kubernetes orchestration.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Cloud
     - Notes
   * - **UpCloud**
     - VM provisioning, cloud-init, backups, periodic sync. No costing, no security groups.
   * - **DigitalOcean**
     - Basic VM provisioning and cloud-init. Delivered as external plugin.
   * - **Alibaba Cloud**
     - Brownfield, security groups, Docker/Kubernetes, tag sync. Limited lifecycle management.
   * - **XCP-ng**
     - VM provisioning, backups. No guest customization, no costing. Delivered as external plugin.
   * - **Oracle VM (OVM)**
     - Basic VM provisioning.
   * - **VMware ESXi (Standalone)**
     - Single-host VM provisioning without vCenter management features.
   * - **MacStadium**
     - macOS VM provisioning on dedicated Mac infrastructure.
   * - **Canonical MaaS**
     - Bare metal provisioning via MaaS.
   * - **Azure Stack**
     - Azure-compatible private cloud. Subset of Azure public capabilities.

.. note::

   Clouds marked "Delivered as external plugin" are installed separately from the |morpheus| appliance. They can be found on the `Morpheus Marketplace <https://share.morpheusdata.com>`_ and installed via |AdmIntPlu|.

Feature Matrix
--------------

The following matrix shows feature availability across all actively supported cloud integrations. Each cell indicates the level of support:

- |checkmark| **Full** |---| Feature is fully supported with create, read, update, and delete operations
- |partial| **Partial** |---| Feature is available but with limited operations (e.g. read-only sync, no CRUD)
- |dash| |---| Feature is not supported for this cloud type

.. note::

   Feature availability may also depend on your |morpheus| license tier (Essentials, Advanced, or Enterprise). See :doc:`/administration/settings/enabled_cloud` for license-based cloud availability.

Provisioning & Lifecycle
^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Cloud", "VM Provision", "Custom Sizing", "Resize", "Clone/Convert", "Auto Scaling", "Migrations"
   :widths: 20, 12, 12, 12, 12, 12, 12

   "AWS", "|checkmark|", "|checkmark|", "|checkmark|", "|partial|", "|checkmark|", "|checkmark|"
   "Azure", "|checkmark|", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|", "|dash|"
   "VMware vCenter", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "HVM", "|checkmark|", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|", "|checkmark|"
   "GCP", "|checkmark|", "|checkmark|", "|dash|", "|dash|", "|dash|", "|dash|"
   "OpenStack", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "Nutanix PE", "|checkmark|", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|", "|checkmark|"
   "Nutanix PC", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|", "|dash|", "|dash|"
   "Hyper-V", "|checkmark|", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|", "|checkmark|"
   "SCVMM", "|checkmark|", "|checkmark|", "|checkmark|", "|dash|", "|dash|", "|dash|"
   "VCD", "|checkmark|", "|checkmark|", "|checkmark|", "|dash|", "|dash|", "|dash|"
   "OTC", "|checkmark|", "|checkmark|", "|checkmark|", "|dash|", "|dash|", "|dash|"
   "Huawei", "|checkmark|", "|checkmark|", "|checkmark|", "|dash|", "|dash|", "|dash|"
   "Oracle Cloud", "|checkmark|", "|checkmark|", "|dash|", "|dash|", "|dash|", "|dash|"
   "PowerVC", "|checkmark|", "|checkmark|", "|checkmark|", "|dash|", "|dash|", "|dash|"
   "OLVM", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|", "|dash|", "|dash|"
   "UpCloud", "|checkmark|", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|", "|checkmark|"
   "DigitalOcean", "|checkmark|", "|partial|", "|partial|", "|dash|", "|dash|", "|dash|"
   "Alibaba", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|", "|dash|", "|dash|"
   "XCP-ng", "|checkmark|", "|checkmark|", "|checkmark|", "|dash|", "|dash|", "|dash|"
   "ESXi", "|checkmark|", "|checkmark|", "|checkmark|", "|dash|", "|dash|", "|dash|"

Networking
^^^^^^^^^^

.. csv-table::
   :header: "Cloud", "Network Sync", "Network CRUD", "Security Groups", "IPAM / IP Pools", "Floating/Elastic IPs", "Load Balancers"
   :widths: 20, 12, 12, 12, 12, 12, 12

   "AWS", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "Azure", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|", "N/A", "|checkmark|"
   "VMware vCenter", "|checkmark|", "|partial| :sup:`1`", "|partial| :sup:`2`", "|checkmark|", "N/A", "|dash|"
   "HVM", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|", "N/A", "|dash|"
   "GCP", "|checkmark|", "|dash|", "|dash|", "|checkmark|", "|partial|", "|dash|"
   "OpenStack", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "Nutanix PE", "|checkmark|", "|dash|", "|dash|", "|partial|", "N/A", "|partial|"
   "Nutanix PC", "|checkmark|", "|dash|", "|dash|", "|partial|", "N/A", "|dash|"
   "Hyper-V", "|checkmark|", "|dash|", "|dash|", "|checkmark|", "N/A", "|dash|"
   "SCVMM", "|checkmark|", "|dash|", "|dash|", "|checkmark|", "N/A", "|dash|"
   "VCD", "|checkmark|", "|partial|", "|dash|", "|checkmark|", "N/A", "|dash|"
   "OTC", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "Huawei", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "Oracle Cloud", "|checkmark|", "|dash|", "|dash|", "|dash|", "|partial|", "|dash|"
   "PowerVC", "|checkmark|", "|dash|", "|checkmark|", "|dash|", "N/A", "|dash|"
   "OLVM", "|checkmark|", "|dash|", "|dash|", "|partial|", "N/A", "|dash|"
   "UpCloud", "|checkmark|", "|dash|", "|dash|", "|dash|", "N/A", "|partial|"
   "DigitalOcean", "|checkmark|", "|dash|", "|dash|", "|dash|", "|partial|", "|dash|"
   "Alibaba", "|checkmark|", "|dash|", "|checkmark|", "|dash|", "|partial|", "|dash|"
   "XCP-ng", "|checkmark|", "|dash|", "|dash|", "|partial|", "N/A", "|dash|"
   "ESXi", "|partial|", "|dash|", "|dash|", "|checkmark|", "N/A", "|dash|"

| :sup:`1` Network creation via NSX/NSX-T integration only
| :sup:`2` Security groups via NSX/NSX-T or Cisco ACI integration

Storage & Backups
^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Cloud", "Datastore Sync", "Volume Mgmt", "Snapshots", "Morpheus Backups", "Third-Party Backup"
   :widths: 20, 14, 14, 14, 14, 14

   "AWS", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|", "|dash|"
   "Azure", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|", "|dash|"
   "VMware vCenter", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "HVM", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|", "|dash|"
   "GCP", "|dash|", "|dash|", "|checkmark|", "|partial|", "|dash|"
   "OpenStack", "|dash|", "|checkmark|", "|checkmark|", "|checkmark|", "|dash|"
   "Nutanix PE", "|checkmark|", "|partial|", "|checkmark|", "|checkmark|", "|dash|"
   "Nutanix PC", "|partial|", "|dash|", "|checkmark|", "|checkmark|", "|dash|"
   "Hyper-V", "|dash|", "|dash|", "|checkmark|", "|checkmark|", "|checkmark|"
   "SCVMM", "|dash|", "|dash|", "|checkmark|", "|checkmark|", "|checkmark|"
   "VCD", "|dash|", "|dash|", "|checkmark|", "|checkmark|", "|dash|"
   "OTC", "|dash|", "|checkmark|", "|checkmark|", "|checkmark|", "|dash|"
   "Huawei", "|dash|", "|checkmark|", "|checkmark|", "|checkmark|", "|dash|"
   "Oracle Cloud", "|dash|", "|dash|", "|partial|", "|partial|", "|dash|"
   "PowerVC", "|dash|", "|dash|", "|partial|", "|partial|", "|dash|"
   "OLVM", "|dash|", "|dash|", "|checkmark|", "|checkmark|", "|dash|"
   "UpCloud", "|dash|", "|dash|", "|checkmark|", "|checkmark|", "|dash|"
   "DigitalOcean", "|dash|", "|dash|", "|partial|", "|partial|", "|dash|"
   "Alibaba", "|dash|", "|dash|", "|dash|", "|partial|", "|dash|"
   "XCP-ng", "|dash|", "|dash|", "|checkmark|", "|checkmark|", "|dash|"
   "ESXi", "|dash|", "|dash|", "|partial|", "|partial|", "|dash|"

Costing & Governance
^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Cloud", "Metering/Usage", "Price Sync", "Invoicing", "Reservations", "Right-Sizing", "Tag Sync", "Sub-Account Scoping"
   :widths: 16, 11, 11, 11, 11, 11, 11, 11

   "AWS", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark| :sup:`3`", "|checkmark|", "|checkmark|"
   "Azure", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark| :sup:`3`", "|checkmark|", "|checkmark|"
   "VMware vCenter", "|checkmark|", "N/A", "N/A", "N/A", "|checkmark|", "|checkmark|", "|checkmark|"
   "HVM", "|checkmark|", "N/A", "N/A", "N/A", "|checkmark|", "N/A", "|partial|"
   "GCP", "|checkmark|", "|checkmark|", "|partial|", "N/A", "|checkmark| :sup:`3`", "|checkmark|", "|checkmark|"
   "OpenStack", "|checkmark|", "N/A", "N/A", "N/A", "|checkmark|", "N/A", "|checkmark|"
   "Nutanix PE", "|checkmark|", "N/A", "N/A", "N/A", "|checkmark|", "N/A", "|partial|"
   "Nutanix PC", "|checkmark|", "N/A", "N/A", "N/A", "|checkmark|", "N/A", "|checkmark|"
   "Hyper-V", "|checkmark|", "N/A", "N/A", "N/A", "|checkmark|", "N/A", "|dash|"
   "SCVMM", "|checkmark|", "N/A", "N/A", "N/A", "|checkmark|", "N/A", "|dash|"
   "VCD", "|checkmark|", "N/A", "N/A", "N/A", "|checkmark|", "N/A", "|checkmark|"
   "OTC", "|checkmark|", "|partial|", "N/A", "N/A", "|checkmark|", "N/A", "|dash|"
   "Huawei", "|checkmark|", "|partial|", "N/A", "N/A", "|checkmark|", "N/A", "|dash|"
   "Oracle Cloud", "|checkmark|", "N/A", "N/A", "N/A", "|checkmark|", "N/A", "|dash|"
   "PowerVC", "|checkmark|", "N/A", "N/A", "N/A", "|checkmark|", "N/A", "|dash|"
   "OLVM", "|checkmark|", "N/A", "N/A", "N/A", "|checkmark|", "N/A", "|dash|"
   "UpCloud", "|checkmark|", "N/A", "N/A", "N/A", "|checkmark|", "N/A", "|dash|"
   "DigitalOcean", "|checkmark|", "N/A", "N/A", "N/A", "|checkmark|", "N/A", "|dash|"
   "Alibaba", "|checkmark|", "|partial|", "N/A", "N/A", "|checkmark|", "|checkmark|", "|dash|"
   "XCP-ng", "|checkmark|", "N/A", "N/A", "N/A", "|checkmark|", "N/A", "|dash|"
   "ESXi", "|checkmark|", "N/A", "N/A", "N/A", "|checkmark|", "N/A", "|dash|"

| :sup:`3` Includes cloud-native recommendations in addition to |morpheus| guidance

Containers & Kubernetes
^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Cloud", "Native K8s (EKS/AKS/GKE)", "Morpheus K8s Clusters", "Docker Hosts", "Brownfield K8s"
   :widths: 20, 18, 18, 14, 14

   "AWS", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "Azure", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "VMware vCenter", "|dash|", "|checkmark|", "|checkmark|", "|checkmark|"
   "HVM", "|dash|", "|checkmark|", "|checkmark|", "|dash|"
   "GCP", "|partial|", "|partial|", "|partial|", "|partial|"
   "OpenStack", "|dash|", "|checkmark|", "|checkmark|", "|dash|"
   "Nutanix PE", "|dash|", "|checkmark|", "|checkmark|", "|dash|"
   "Nutanix PC", "|dash|", "|partial|", "|partial|", "|dash|"
   "Hyper-V", "|dash|", "|dash|", "|checkmark|", "|dash|"
   "SCVMM", "|dash|", "|dash|", "|dash|", "|dash|"
   "VCD", "|dash|", "|checkmark|", "|checkmark|", "|dash|"
   "OTC", "|dash|", "|dash|", "|dash|", "|dash|"
   "Huawei", "|dash|", "|dash|", "|dash|", "|dash|"
   "Oracle Cloud", "|dash|", "|dash|", "|dash|", "|dash|"
   "PowerVC", "|dash|", "|dash|", "|dash|", "|dash|"
   "OLVM", "|dash|", "|dash|", "|dash|", "|dash|"
   "UpCloud", "|dash|", "|dash|", "|checkmark|", "|dash|"
   "DigitalOcean", "|dash|", "|dash|", "|dash|", "|dash|"
   "Alibaba", "|dash|", "|partial|", "|checkmark|", "|dash|"
   "XCP-ng", "|dash|", "|dash|", "|dash|", "|dash|"
   "ESXi", "|dash|", "|dash|", "|dash|", "|dash|"

Brownfield & Synchronization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Cloud", "VM Discovery", "Periodic Sync", "Remote Console", "Inventory Import"
   :widths: 20, 16, 16, 16, 16

   "AWS", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "Azure", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "VMware vCenter", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "HVM", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "GCP", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|"
   "OpenStack", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|"
   "Nutanix PE", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "Nutanix PC", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "Hyper-V", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "SCVMM", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|"
   "VCD", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "OTC", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "Huawei", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "Oracle Cloud", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|"
   "PowerVC", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "OLVM", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "UpCloud", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "DigitalOcean", "|partial|", "|partial|", "|dash|", "|partial|"
   "Alibaba", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|"
   "XCP-ng", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|"
   "ESXi", "|partial|", "|partial|", "|checkmark|", "|partial|"

Guest Customization
^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: "Cloud", "Linux cloud-init", "Windows Sysprep/Unattend", "Force Guest Customization", "Cloudbase-Init"
   :widths: 20, 16, 16, 16, 16

   "AWS", "|checkmark|", "N/A :sup:`4`", "N/A", "|dash|"
   "Azure", "|checkmark|", "N/A :sup:`4`", "N/A", "|dash|"
   "VMware vCenter", "|checkmark|", "|checkmark|", "|checkmark|", "|checkmark|"
   "HVM", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|"
   "GCP", "|checkmark|", "N/A :sup:`4`", "N/A", "|dash|"
   "OpenStack", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|"
   "Nutanix PE", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|"
   "Nutanix PC", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|"
   "Hyper-V", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|"
   "SCVMM", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|"
   "VCD", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|"
   "OTC", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|"
   "Huawei", "|checkmark|", "|checkmark|", "|dash|", "|checkmark|"
   "Oracle Cloud", "|checkmark|", "|dash|", "|dash|", "|dash|"
   "PowerVC", "|checkmark|", "|dash|", "|dash|", "|dash|"
   "OLVM", "|checkmark|", "|dash|", "|dash|", "|dash|"
   "UpCloud", "|checkmark|", "|dash|", "|dash|", "|dash|"
   "DigitalOcean", "|checkmark|", "|dash|", "|dash|", "|dash|"
   "Alibaba", "|checkmark|", "|dash|", "|dash|", "|dash|"
   "XCP-ng", "|checkmark|", "|dash|", "|dash|", "|dash|"
   "ESXi", "|checkmark|", "|partial|", "|dash|", "|dash|"

| :sup:`4` Public clouds handle Windows customization via cloud-native userdata/metadata; sysprep is managed by the cloud provider

Understanding the Matrix
-------------------------

Provisioning & Lifecycle
  Covers the ability to create, resize, clone, and migrate virtual machines. Tier 1 clouds support the full range of lifecycle operations. Tier 3 clouds typically support creation and basic resize only.

Networking
  Covers network discovery, CRUD operations (create/update/delete networks and subnets), security group management, IP address management (IPAM), and load balancer integration. This is often the most significant differentiator between tiers. Tier 1 clouds support full network lifecycle; Tier 2 clouds may only sync existing networks; Tier 3 clouds provide basic network selection at provisioning time.

  .. note:: **IPAM / IP Pools** is largely a |morpheus| platform-level capability. When a network has pool assignment enabled, |morpheus| leases an IP from the configured pool and injects it into the guest OS via cloud-init (Linux), sysprep/cloudbase-init (Windows), or VMware/SCVMM guest customization. This means most on-premises clouds (VMware, Hyper-V, SCVMM, KVM/HVM, OpenStack, VCD) support IP pool assignment regardless of whether the underlying hypervisor has native IPAM. The "Floating/Elastic IPs" column refers to cloud-provider-native floating IP concepts (AWS Elastic IP, OpenStack Floating IP, etc.) and is marked N/A for clouds where this concept does not exist.

Storage & Backups
  Covers datastore synchronization, volume management, snapshot support, and backup integrations (both native |morpheus| backups and third-party solutions like Veeam or Commvault).

Costing & Governance
  **Metering/Usage** is a |morpheus| platform capability that tracks resource consumption (CPU, memory, storage) across all synced VMs regardless of cloud type. **Price Sync** and **Invoicing** apply to public clouds where pricing data is available via API. **Reservations** tracks cloud-provider reservation commitments (AWS Reserved Instances, Azure Reservations). **Right-Sizing** recommendations are generated by |morpheus| guidance for all clouds based on usage patterns; public clouds additionally feed cloud-native recommendations. **Tag Sync** is bi-directional tag synchronization with cloud-provider tag/label systems (N/A for platforms without a tag API). **Sub-Account Scoping** refers to the ability to scope a |morpheus| cloud integration to a specific cloud-provider sub-account, project, or subscription (e.g. AWS accounts, Azure subscriptions, GCP projects, OpenStack projects, vCloud Director Orgs).

Containers & Kubernetes
  Covers native managed Kubernetes services (EKS, AKS, GKE), |morpheus|-provisioned Kubernetes clusters, Docker host deployment, and brownfield Kubernetes cluster import.

Brownfield & Synchronization
  Covers the ability to discover and import existing cloud resources, periodic synchronization of cloud state, remote console access, and inventory management.

Guest Customization
  Covers guest OS customization methods supported during provisioning. **Linux cloud-init** injects hostname, network, and user configuration via cloud-init datasources. **Windows Sysprep/Unattend** uses a sysprep'd image with an unattend.xml answer file injected at provisioning time. **Force Guest Customization** is a VMware-specific capability where VMware Tools delivers the customization payload to a running VM without requiring a pre-sysprep'd template. **Cloudbase-Init** is the Windows equivalent of cloud-init, used on platforms that support metadata-driven configuration. See :doc:`/provisioning/windows_cloud_guest_customization` for detailed Windows image preparation guidance.

Plugin-Based Clouds
--------------------

Several cloud integrations are delivered as installable plugins rather than being bundled with the |morpheus| appliance. Plugin-based clouds offer the same management capabilities but are installed separately and may follow an independent release cadence.

Current plugin-based clouds include:

- Nutanix Prism Element
- Nutanix Prism Central
- DigitalOcean
- XCP-ng

Plugins are available on the `Morpheus Marketplace <https://share.morpheusdata.com>`_ and can be installed via |AdmIntPlu|.

.. |partial| unicode:: U+25D0
.. |dash| unicode:: U+2014
.. |---| unicode:: U+2014
