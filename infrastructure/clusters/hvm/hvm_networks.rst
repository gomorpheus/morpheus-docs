HVM Networks
^^^^^^^^^^^^

.. versionadded:: 9.0

Overview
````````

The HVM Network Plugin delivers advanced networking capabilities for |morpheus| HVM clusters. It provides a modular, plugin-based network provider that separates networking from the |morpheus| core, enabling independent updates, maintenance, and extensibility without impacting the platform.

The plugin is purpose-built for HVM (KVM-based) clusters and manages the complete lifecycle of virtual networks on cluster hosts. It automates network creation, configuration, and deletion — including Open vSwitch (OVS) bridge-backed port groups, VXLAN overlays, Linux VLAN interfaces, MacVTAP interfaces, and SR-IOV Virtual Function (VF) networks — directly from the |morpheus| user interface.

Key capabilities:

- Create and delete HVM networks of all five types directly from the UI
- Configure Standard Networks in Access, Hybrid, or Trunk-only VLAN modes based on workload requirements
- Trigger trunk VLAN configuration propagation to Aruba CX switches through the Aruba CX Network Plugin (Generic Integration)
- Automatically provision or delete network configurations whenever a host is added to or removed from a cluster
- Detect and repair configuration drift using idempotent synchronization on every refresh cycle
- Discover existing libvirt networks and OVS configurations on hosts

Prerequisites
`````````````

Ensure the following requirements are met before using HVM networks:

General Requirements
~~~~~~~~~~~~~~~~~~~~

- The |morpheus| appliance must run version 9.0.0 or later
- A pre-existing HVM cluster must be available
- All cluster hosts must be reachable from the |morpheus| appliance
- Open vSwitch (OVS) must be installed and running on each host
- Deploy the plugin only on an HVM KVM-based cluster

Standard Network Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- An OVS Bridge Domain virtual switch must exist in the cluster
- The bridge must be backed by a host network interface (for example, ``mgmt`` or ``bond0``)

Aruba CX Integration Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Aruba CX switches must be configured and reachable
- The Aruba CX Network Plugin (Generic Integration) must be installed and configured in |morpheus|

Verifying the Plugin
````````````````````

The HVM networking plugin is pre-installed in |morpheus| and registered automatically during HVM cluster configuration. You do not need to manually install the plugin.

To verify availability:

1. Navigate to :menuselection:`Administration --> Integrations --> Plugins`
2. Confirm that **HVM Networking Plugin** appears in the list with status **Enabled**

.. note::

   If the HVM networking plugin is not listed, upload the plugin JAR manually through :menuselection:`Administration --> Integrations --> Plugins --> + Add Plugin`. The plugin JAR is published at HPE artifactory and is also available in the |morpheus| release bundle.

OVS Bridge Domain Virtual Switches
```````````````````````````````````

Before creating Standard or Overlay networks, ensure that an OVS Bridge Domain virtual switch exists in the cluster. You can either create a new OVS bridge or associate the virtual switch with an existing bridge on the hosts.

An OVS Bridge Domain virtual switch is represented in |morpheus| as a Network Router resource of type ``openVSwitch``. It acts as the underlying virtual switching layer that backs both Standard and Overlay networks, providing the bridge infrastructure required to connect workloads and handle traffic forwarding within the cluster.

.. note::

   Ensure that the Name remains unique within the cluster and does not conflict with any existing OVS bridges on the hosts.

Creating an OVS Bridge Domain Virtual Switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Navigate to :menuselection:`Infrastructure --> Network --> Routers`
2. Select :guilabel:`+ Add` and choose **OVS Bridge Domain**
3. Configure the following:

   - **Name** — A unique name for the virtual switch
   - **Cluster** — Select the target HVM cluster
   - **Bridge Interface** — The host network interface backing the bridge (for example, ``bond0``)

4. Click :guilabel:`Save`

The system creates the OVS bridge on all hosts in the cluster.

Deleting an OVS Bridge Domain Virtual Switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deleting an OVS Bridge Domain virtual switch removes the OVS bridge from all hosts in the cluster, removes the associated libvirt network definitions, and removes all dependent Standard and Overlay network objects from the |morpheus| database.

.. warning::

   The system prevents deletion if any VMs are currently attached to networks that depend on this virtual switch. Ensure that all such networks and VMs are removed or migrated before deleting the virtual switch.

1. Navigate to :menuselection:`Infrastructure --> Network --> Routers`
2. Select the OVS Bridge Domain virtual switch to delete
3. Click the delete icon next to the virtual switch name
4. Confirm the deletion when prompted

The system removes the parent libvirt bridge network (the OVS bridge definition) from all hosts in the cluster and deletes all dependent Standard and Overlay network objects.

Network Types
`````````````

HVM clusters support five network types, each designed for specific workload connectivity patterns:

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Network Type
     - Backing Technology
     - Use Case
   * - **Standard**
     - OVS port group on OVS Bridge Domain
     - General VM connectivity with VLAN segmentation
   * - **Overlay**
     - VXLAN tunneling with dedicated OVS bridge per network
     - Tenant isolation without physical VLAN configuration
   * - **Data**
     - Linux VLAN interface mapped to libvirt network
     - High-throughput in-guest storage traffic (iSCSI, NFS)
   * - **Private**
     - MacVTAP-backed libvirt network
     - Direct connectivity to physical network segments
   * - **SR-IOV**
     - SR-IOV Virtual Functions on physical NIC
     - Near-native network performance for demanding workloads

Creating HVM Standard Networks
``````````````````````````````

An HVM Standard Network uses an OVS port group on an existing OVS Bridge Domain virtual switch as its backing. The system determines its VLAN behavior through the **VLAN Trunks** and **Trunk Only** fields, which define whether the network operates in Access, Hybrid, or Trunk-only mode.

.. note::

   A single physical VM NIC (VMNIC) can carry traffic for multiple VLANs in Hybrid and Trunk-only modes, eliminating the need to assign a separate NIC for each VLAN.

1. Navigate to :menuselection:`Infrastructure --> Network --> Networks`
2. Select :guilabel:`+ Add` > **HVM Standard Network**
3. Enter the following details:

   - **Group** — Select the group to which the network belongs
   - **Network Service** — Select the network service
   - **Router** — Select the OVS Bridge Domain virtual switch
   - **Resource Pool** — Select the cluster resource pool
   - **VLAN ID** — The native VLAN ID for the network
   - **VLAN Trunks** — Comma-separated list of trunk VLAN IDs or ranges (for example, ``100,200-210``)
   - **Trunk Only** — Enable to use trunk-only mode (no native VLAN)

4. Click :guilabel:`Save`

VLAN Modes and Traffic Behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Standard Networks support three VLAN modes based on configuration:

**Access Mode (Default)**

The OVS bridge handles VLAN tagging transparently. The VM receives untagged Ethernet frames and remains unaware of VLAN assignments.

- UI fields: VLAN ID = 200, VLAN Trunks = (empty), Trunk Only = off
- Egress (VM → network): The VM sends an untagged frame, and the OVS bridge inserts the VLAN 200 tag before forwarding to the uplink
- Ingress (network → VM): OVS receives a VLAN 200 tagged frame, removes the tag, and delivers an untagged frame to the VM

**Hybrid Mode (Native VLAN + Trunk VLANs)**

The system uses VLAN 0 as an untagged passthrough marker in the port group XML. The untagged traffic uses the native VLAN and trunk VLANs pass through tagged.

- UI fields: VLAN ID = 200, VLAN Trunks = 100,300, Trunk Only = off
- The VM can send/receive both untagged (native VLAN 200) and tagged (VLANs 100, 300) traffic

**Trunk-Only Mode**

All traffic is tagged. No native VLAN is assigned.

- UI fields: VLAN ID = (any), VLAN Trunks = 100,200,300, Trunk Only = on
- The VM must tag all outgoing frames and expects all incoming frames to be tagged

Modifying an HVM Standard Network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can modify the **VLAN Trunks** and **Trunk Only** fields on an existing Standard Network after creation. You cannot modify the VLAN ID, Resource Pool, or Router fields.

1. Navigate to :menuselection:`Infrastructure --> Network --> Networks`
2. Select the Standard Network to modify
3. Click :guilabel:`Edit`
4. Modify the following fields:

   - **VLAN Trunks** — Update the comma-separated list of trunk VLAN IDs or ranges. The system provisions added VLANs on all hosts and removes deleted VLANs unless another network in the same cluster and OVS bridge still uses them.
   - **Trunk Only** — Toggle trunk-only mode on or off. The system removes the native VLAN tag from the OVS port when switching from Hybrid to Trunk-only, and restores the native VLAN tag when switching back.

5. Click :guilabel:`Save Changes`

The plugin updates the port group XML on all hosts in the cluster.

Creating HVM Overlay Networks
`````````````````````````````

An HVM Overlay Network uses VXLAN tunneling to provide isolation for east-west VM traffic across hosts. It enables tenant network segmentation without requiring physical VLAN configuration on upstream switches.

The system deploys a dedicated OVS bridge for each overlay network on every host and configures a VXLAN tunnel endpoint on a designated host interface.

.. note::

   The HVM Overlay Network does not use the same OVS Bridge Domain virtual switch as Standard Networks. Instead, the system creates a dedicated OVS bridge for each Overlay Network on every host, ensuring complete isolation from other networks.

1. Navigate to :menuselection:`Infrastructure --> Network --> Networks`
2. Select :guilabel:`+ Add` > **HVM Overlay Network**
3. Enter the following details:

   - **Group** — Select the group
   - **Network Service** — Select the network service
   - **Resource Pool** — Select the cluster resource pool
   - **VNI** — The VXLAN Network Identifier for tunnel isolation
   - **Tunnel Interface** — The host interface used as the VXLAN tunnel endpoint

4. Click :guilabel:`Save`

Creating HVM Data Networks
``````````````````````````

An HVM Data Network creates a Linux VLAN interface on each host and maps it to a libvirt network. It is designed to handle high-throughput in-guest storage traffic, such as iSCSI or NFS. It also supports MTU configuration for jumbo frames.

.. note::

   - You can apply MTU changes only to stopped VMs
   - Ensure to stop and start each VM after changing the MTU
   - Configure the MTU inside the guest VM interface: ``ip link set <iface> mtu 9000``

1. Navigate to :menuselection:`Infrastructure --> Network --> Networks`
2. Select :guilabel:`+ Add` > **HVM Data Network**
3. Enter the following details:

   - **Group** — Select the group
   - **Network Service** — Select the network service
   - **Resource Pool** — Select the cluster resource pool
   - **VLAN ID** — The VLAN for the data network
   - **Host Interface** — The host interface for the VLAN sub-interface
   - **MTU** — Maximum transmission unit (for example, ``9000`` for jumbo frames)

4. Click :guilabel:`Save`

Creating HVM Private Networks
`````````````````````````````

The HVM Private Network creates a MacVTAP-backed libvirt network on each host. The system creates a VLAN-tagged sub-interface on the selected host interface using the specified VLAN ID. When a VM connects to this network, libvirt automatically creates a macvtap interface on the host, providing direct connectivity to the physical network segment.

1. Navigate to :menuselection:`Infrastructure --> Network --> Networks`
2. Select :guilabel:`+ Add` > **HVM Private Network**
3. Enter the following details:

   - **Group** — Select the group
   - **Network Service** — Select the network service
   - **Resource Pool** — Select the cluster resource pool
   - **VLAN ID** — The VLAN for the private network
   - **Host Interface** — The host interface for the VLAN sub-interface

4. Click :guilabel:`Save`

Creating HVM SR-IOV Networks
````````````````````````````

The HVM SR-IOV Network uses SR-IOV Virtual Functions (VFs) on a physical NIC to deliver near-native network performance. The plugin maps a libvirt hostdev network to a Physical Function (PF), and libvirt manages the assignment of VFs to individual VMs. The NIC hardware performs VLAN Switch Tagging (VST), inserting and removing VLAN tags directly in hardware, making the process transparent to the VM guest OS.

.. note::

   - The system does not support live migration of VMs that use SR-IOV networks
   - Ensure that you enable SR-IOV in the host BIOS/UEFI before configuring SR-IOV networks
   - The plugin automatically detects SR-IOV-capable Physical Functions on each host

.. warning::

   Monitor libvirt behavior after VM clone, backup, or restore because VF tracking can become inconsistent. Restart the ``libvirtd`` daemon if VF tracking issues occur.

Understanding Physical Functions and Virtual Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Physical Function (PF)** — A full-featured PCIe device on a physical network adapter that manages and controls SR-IOV functionality. The host OS discovers and manages the PF like a standard physical NIC. The PF driver controls the hardware, enables SR-IOV, and creates Virtual Functions.
- **Virtual Function (VF)** — A lightweight PCIe function derived from a PF that provides near-native I/O performance to a VM. Each VF operates independently with its own queue and interrupt, allowing direct hardware access without hypervisor overhead.

AppArmor Configuration
~~~~~~~~~~~~~~~~~~~~~~

Configure AppArmor on each host to allow libvirt/QEMU to access VFIO devices for SR-IOV Virtual Functions:

Add the following entry to the local libvirt-qemu AppArmor abstraction file:

.. code-block:: bash

   # File: /etc/apparmor.d/local/abstractions/libvirt-qemu
   # Allow read/write/lock access to all VFIO group devices for SR-IOV VFs
   /dev/vfio/* krw,

Reload AppArmor after making the change:

.. code-block:: bash

   sudo apparmor_parser -r /etc/apparmor.d/abstractions/libvirt-qemu

Host NIC VF Management
~~~~~~~~~~~~~~~~~~~~~~

When you create an SR-IOV network, the plugin automatically performs the following:

1. Discovers all SR-IOV-capable Physical Functions (PFs) on each host by reading ``/sys/class/net/*/device/sriov_totalvfs``
2. If Virtual Functions (VFs) are not enabled, the plugin installs and starts a persistent systemd service on the host. This service writes ``sriov_totalvfs`` to ``sriov_numvfs``, ensuring VFs remain enabled across reboots.
3. Creates and autostarts the libvirt hostdev network on each host
4. All SR-IOV networks that share the same Physical Function (PF) use a single libvirt hostdev pool on each host. The total number of VMs across all networks on that PF is limited by the total number of available VFs.

Creating the SR-IOV Network
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Navigate to :menuselection:`Infrastructure --> Network --> Networks`
2. Select :guilabel:`+ Add` > **HVM SR-IOV Network**
3. Enter the following details:

   - **Group** — Select the group
   - **Network Service** — Select the network service
   - **Resource Pool** — Select the cluster resource pool
   - **Physical Function** — Select the SR-IOV capable NIC (PF)
   - **VLAN ID** — The VLAN for hardware-level VST tagging

4. Click :guilabel:`Save`

Deleting an HVM Network
````````````````````````

Deleting an HVM network removes the network definition from all hosts in the cluster and from the |morpheus| database.

1. Navigate to :menuselection:`Infrastructure --> Network --> Networks`
2. Select the network to delete from the list
3. Click the delete icon next to the network name
4. Confirm the deletion when prompted

The system removes the libvirt network definition and its port group from all hosts in the cluster. For Standard Networks, it removes trunk VLAN IDs automatically along with the port group without requiring separate cleanup. The system also updates the Aruba CX switch configuration for the removed VLAN IDs through the Generic Integration.

Viewing Network Status
``````````````````````

Viewing Networks Managed by the Plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Navigate to :menuselection:`Infrastructure --> Network --> Networks`
2. Filter by **Type** to view networks of each HVM network type:

   - HVM Standard Network
   - HVM Overlay Network
   - HVM Data Network
   - HVM Private Network
   - HVM SR-IOV Network

Viewing OVS Bridge Domain Virtual Switches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Navigate to :menuselection:`Infrastructure --> Network --> Routers`
2. Filter by type **OVS Bridge Domain** to see all virtual switches in the cluster

Viewing Plugin Logs
~~~~~~~~~~~~~~~~~~~

1. Navigate to :menuselection:`Administration --> Health --> Morpheus Logs`
2. Enter ``HvmNetwork`` in the search box to filter by plugin name

Troubleshooting
```````````````

General Troubleshooting
~~~~~~~~~~~~~~~~~~~~~~~

For any issues related to HVM network plugin, view the |morpheus| appliance logs (see `Viewing Plugin Logs`_ above).

New Host Does Not Receive Networks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new host may fail to receive networks if |morpheus| has not completed host discovery or if required interfaces are not yet available for propagation.

|morpheus| must discover the host interfaces before it can propagate network definitions. If bond interface discovery remains incomplete, |morpheus| cannot complete network mapping for the host.

Resolution:

1. Check for pending AddWorker jobs
2. Confirm that |morpheus| has discovered all required bond interfaces on the host
3. Verify that the host inventory reflects the expected network interfaces before propagation begins

If the issue persists:

- Check whether the AddWorker workflow has reached the retry limit
- Review :menuselection:`Infrastructure --> Activity` for error events related to the host
