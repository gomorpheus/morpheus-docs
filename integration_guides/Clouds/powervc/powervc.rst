PowerVC
-------

Overview
^^^^^^^^

IBM PowerVC (Power Virtualization Center) is a cloud management solution for IBM Power Systems based on OpenStack. |morpheus| integrates with PowerVC using its OpenStack-compatible APIs, providing full virtual machine lifecycle management for Power architecture workloads (AIX, IBM i, Linux on Power).

Features
^^^^^^^^

- Virtual Machine provisioning on IBM Power Systems
- Security Group management
- Network lifecycle management
- Brownfield VM discovery and import
- Resource pool (Host Group) visibility
- Native plan (flavor) discovery
- Console access (VNC)

Prerequisites
^^^^^^^^^^^^^

- PowerVC 1.4+ deployed and operational
- Identity API (Keystone) endpoint accessible from the |morpheus| appliance over HTTPS (port 5000)
- A PowerVC user account with sufficient privileges for the target project(s)
- Network connectivity from |morpheus| to the PowerVC management interfaces

Adding a PowerVC Cloud
^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Clouds``
#. Select :guilabel:`+ ADD`
#. Choose **PowerVC** from the cloud type list
#. Configure the following:

   **Connection Settings**

   IDENTITY API URL
     The Keystone identity endpoint URL for PowerVC (e.g., ``https://powervc-host:5000``)
   CREDENTIAL
     Select a stored credential or provide local credentials:

     - **Username** — PowerVC user with API access
     - **Password** — PowerVC user password

   PROJECT
     Select one or more projects (tenants) to scope the integration. Select "All" to discover resources across all accessible projects. This field uses typeahead and queries projects from the PowerVC endpoint using the provided credentials.

   **Discovery Options**

   INVENTORY EXISTING INSTANCES
     Enable to import existing VMs from PowerVC into |morpheus| as managed or unmanaged instances
   ENABLE HYPERVISOR CONSOLE
     Enable VNC console access to VMs through the |morpheus| UI

#. Expand **Advanced Options** for additional settings (API timeout, proxy, etc.)
#. Select :guilabel:`NEXT` and complete the wizard

.. TIP:: PowerVC uses the same Keystone identity API as OpenStack. The Identity API URL should point to the Keystone v3 endpoint (typically port 5000).

Cloud Detail Tabs
^^^^^^^^^^^^^^^^^^

Once added, the PowerVC cloud detail page provides:

- **VMs** — All discovered and provisioned virtual machines
- **Hosts** — Power Systems hypervisor hosts
- **Networks** — VLAN and virtual networks configured in PowerVC
- **Security Groups** — Security group rules
- **Resource Pools** — Host Groups configured in PowerVC (provisioning requires a resource pool selection)

Provisioning to PowerVC
^^^^^^^^^^^^^^^^^^^^^^^^^

When provisioning to a PowerVC cloud:

#. Select a PowerVC cloud as the target
#. Choose from discovered native plans (flavors) or custom service plans
#. Select a network (PowerVC VLAN)
#. Select a resource pool (Host Group)
#. Choose a virtual image compatible with Power architecture

.. NOTE:: PowerVC uses the ``powervc`` provision type internally. Instance Type Layouts targeting PowerVC must use this provision type.

Server Types
^^^^^^^^^^^^^

PowerVC supports the following server types in |morpheus|:

- **powervcLinux** — Linux on Power managed instances
- **powervcWindows** — Windows on Power managed instances (rare)
- **powervcVm** — Generic PowerVC VM (Linux)
- **powervcWindowsVm** — Generic PowerVC VM (Windows)

Network Configuration
^^^^^^^^^^^^^^^^^^^^^^

PowerVC networks are synced as VLAN network types (``powervcVlan``). Networks are managed through the integrated network server which supports:

- Viewing available networks
- Assigning networks to instances during provisioning
- Network router management

Differences from Standard OpenStack
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While PowerVC is built on OpenStack, several differences exist:

.. list-table::
   :widths: 30 35 35
   :header-rows: 1

   * - Feature
     - OpenStack
     - PowerVC
   * - Architecture
     - x86_64
     - ppc64le (Power)
   * - Compute service
     - Nova
     - Nova (Power-optimized)
   * - Image format
     - QCOW2, RAW
     - OVA, disk image
   * - Disk mode options
     - Local, Ceph
     - SAN-backed storage
   * - Costing
     - Available
     - Not available
   * - Functions/Jobs
     - Available
     - Not available
   * - Bare Metal
     - Ironic
     - Not available
   * - Distributed Worker
     - Supported
     - Supported

Troubleshooting
^^^^^^^^^^^^^^^^

- **Cannot connect:** Verify the Identity API URL includes the protocol (``https://``) and correct port (5000). Ensure TLS certificates are valid or trusted.
- **No projects found:** Check that the user credentials have access to at least one project in PowerVC.
- **No images available:** Power architecture images must be uploaded to PowerVC separately. Standard x86 images are not compatible.
- **Provisioning fails:** Verify resource pool (Host Group) has available capacity and the selected network is properly configured in PowerVC.
