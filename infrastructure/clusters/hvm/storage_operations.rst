Storage Lifecycle
=================

This section covers Day-2 storage operations on an HVM 1.3 cluster, including adding and removing datastores, managing iSCSI targets, and expanding storage capacity.

Adding a New Datastore
-----------------------

New HPE Clustered Datastores (Shared LUNs) can be added to a running cluster without downtime.

Prerequisites
^^^^^^^^^^^^^

- A shared storage LUN is provisioned and accessible to all cluster hosts via iSCSI or Fibre Channel
- The iSCSI target for the LUN has been added to the cluster (see `Adding iSCSI Targets`_ below)
- All hosts can see the block device (verify with ``lsblk`` on each host)

Procedure
^^^^^^^^^

#. Navigate to ``Storage > Datastores``
#. Click :guilabel:`+ Add`
#. Select the HPE Clustered Datastore (GFS2) type
#. Configure the datastore:

   .. list-table::
      :widths: 30 70
      :header-rows: 1

      * - Field
        - Description
      * - Name
        - Descriptive name for the datastore
      * - Cluster
        - Select the target HVM cluster
      * - Block Device
        - The shared block device path (e.g., ``/dev/mapper/mpathX``)
      * - Heartbeat Target
        - Enable if this datastore should be used for heartbeat writes

#. Click :guilabel:`Save`

What Happens Automatically
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When a new HPE Clustered Datastore is created:

#. **GFS2 formatting** — ``mkfs.gfs2`` is run with lock_dlm protocol, 2048 resource groups, and 32 initial journals, with the lock table tied to the cluster
#. **Journal provisioning** — Journals are added (``gfs2_jadd``) if the initial journal count is less than the number of hosts
#. **Mount on all hosts** — The filesystem is mounted on each cluster host. Mount information is persisted to ``/opt/morpheus-node/.mounts``
#. **libvirt storage pool** — A virsh storage pool is created on each host, making the datastore available for VM disk placement
#. **Lock protocol** — The ``lock_dlm`` protocol coordinates file locking across all hosts through the existing DLM infrastructure

Adding iSCSI Targets
---------------------

iSCSI targets provide the block device access that underpins HPE Clustered Datastores.

Procedure
^^^^^^^^^

#. Navigate to ``Infrastructure > Clusters > [Cluster] > Storage > iSCSI``
#. Click :guilabel:`Add`
#. Enter the iSCSI target details:

   .. list-table::
      :widths: 30 70
      :header-rows: 1

      * - Field
        - Description
      * - Target IP
        - IP address of the iSCSI target portal
      * - Target Port
        - Port number (default: 3260)

#. Click :guilabel:`Save`

What Happens Automatically
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When an iSCSI target is added:

#. **Discovery** — ``iscsiadm -m discovery -t st -p "<IP>:<port>"`` is run on all online cluster hosts
#. **Auto-login** — Sessions are configured for automatic startup and all available targets are logged in (``iscsiadm -m node --loginall=automatic``)
#. **Persistence** — Target connections persist across host reboots

.. NOTE:: iSCSI targets are automatically discovered on all hosts in the cluster, not just a single host. This ensures all hosts can access the shared storage simultaneously.

Removing iSCSI Targets
------------------------

.. WARNING:: Before removing an iSCSI target, ensure no datastores are using LUNs from that target. Removing a target with active datastores will cause storage failures.

Procedure
^^^^^^^^^

#. Migrate all VMs off datastores using the target's LUNs
#. Remove the datastore from |morpheus| (see `Removing a Datastore`_ below)
#. Navigate to ``Infrastructure > Clusters > [Cluster] > Storage > iSCSI``
#. Select the target to remove
#. Click :guilabel:`Remove`

What Happens Automatically
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The iSCSI discovery database entry is removed from all online cluster hosts using ``iscsiadm -m discoverydb -t sendtargets -p "<IP>:<port>" -o delete``.

Expanding Storage (New LUNs)
-----------------------------

To add additional capacity to an existing cluster:

#. Provision new LUNs on your storage array
#. Add iSCSI targets (if new portals) as described above
#. Trigger a storage rescan so all hosts discover the new LUN. There are two ways to do this:

   **From the UI:**

   - Navigate to the cluster detail page and click :guilabel:`Actions` > :guilabel:`Rescan Storage` to immediately rescan all hosts

   .. note:: Confirm Rescan Storage button is available in 9.1.0 UI. Update this section when the button ships.

   .. NOTE:: |morpheus| also performs an automatic daily storage rescan during the cluster refresh cycle.

#. Verify the new LUN is visible on the cluster's Storage tab
#. Create a new HPE Clustered Datastore using the new block device

.. NOTE:: Each HPE Clustered Datastore (Shared LUN) maps to a single block device. To add capacity, create additional datastores rather than expanding existing GFS2 filesystems.

Removing a Datastore
---------------------

.. WARNING:: All VMs must be migrated off the datastore before removal. Removing a datastore with active VMs will result in data loss.

Procedure
^^^^^^^^^

#. Verify no VMs have disks on the datastore:

   - Navigate to ``Storage > Datastores > [Datastore]``
   - Check the :guilabel:`Virtual Machines` tab

#. Migrate any remaining VMs to another datastore
#. Navigate to ``Storage > Datastores``
#. Select the datastore to remove
#. Click :guilabel:`Remove`

What Happens
^^^^^^^^^^^^

- The GFS2 filesystem is unmounted on all cluster hosts
- The libvirt storage pool is destroyed on all hosts
- Mount information is removed from ``/opt/morpheus-node/.mounts``
- The datastore record is removed from |morpheus|

Heartbeat Datastore Configuration
-----------------------------------

The heartbeat datastore is used for host health detection. Each host writes ``hb.properties`` to the heartbeat datastore every 20 seconds, and the Designated Coordinator monitors these writes to detect host failures.

Changing the Heartbeat Datastore
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Storage > Datastores``
#. Edit the desired datastore's properties
#. Enable the :guilabel:`Heartbeat Target` option
#. Save changes

.. IMPORTANT:: Only one datastore may be configured as the heartbeat target at a time. If multiple datastores are marked as heartbeat targets, |morpheus| will automatically select one (preferring provisioned, non-failing datastores) and clear the heartbeat flag on the others. An alarm is raised when this automatic selection occurs.

Heartbeat Datastore Best Practices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Use a highly reliable datastore as the heartbeat target
- Ensure the heartbeat datastore is accessible from all cluster hosts
- If the heartbeat datastore fails, VM failover detection is impaired until a new heartbeat target is configured
- Monitor the heartbeat datastore's health in the Quorum panel (``Infrastructure > Clusters > [Cluster] > Summary``)

Datastore Health Monitoring
----------------------------

|morpheus| continuously monitors datastore health:

- **Mount status** — Each host's agent reports mount status (MOUNTED, WARNING, FAILED)
- **GFS2 withdrawal** — If the GFS2 filesystem enters a withdrawn state (due to journal errors or storage issues), the datastore location status is updated to ``warning`` or ``failed``
- **virsh pool status** — If a libvirt storage pool is missing on a host, |morpheus| recreates it automatically during the next sync cycle

Datastore Status Indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Status
     - Description
   * - Provisioned
     - Datastore is healthy and operational on all hosts
   * - Warning
     - One or more hosts report mount issues; investigate the affected host(s)
   * - Failed
     - All hosts report mount failures; datastore is not operational
   * - Provisioning
     - Datastore is being created or mounted

For troubleshooting datastore issues, see :doc:`troubleshooting`.

Fibre Channel Configuration
-----------------------------

HVM clusters support Fibre Channel (FC) as a storage transport for HPE Clustered Datastores in addition to iSCSI. FC provides lower latency and higher throughput than iSCSI and is the preferred choice for production workloads.

Host Requirements
^^^^^^^^^^^^^^^^^^

Each HVM host that will access FC storage must have:

- One or more Fibre Channel HBA (Host Bus Adapter) ports connected to the SAN fabric
- Proper zoning configured on the SAN switch to allow the host HBA WWPNs to communicate with the storage array ports
- ``multipathd`` running (installed automatically during HVM cluster provisioning)

FC targets do not need to be manually added in the |morpheus| UI (unlike iSCSI). When a storage plugin provisions a LUN and exports it to the cluster hosts' WWPNs, the hosts automatically discover the new device after a SCSI rescan.

How FC Storage Works with GFS2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. The storage plugin (e.g., HPE Alletra MP) creates a LUN on the array and exports it to a **host-set** containing the FC WWPNs of all cluster hosts
#. A SCSI rescan is triggered on each host to discover the new block device
#. The block device is identified by its **WWN** through multipath — the device path is always ``/dev/mapper/3<volumeWwn>`` (WWN-stable, not positional ``/dev/mapper/mpathX``)
#. GFS2 filesystem is formatted on the device and mounted on all cluster hosts simultaneously
#. The device is registered as a virsh storage pool for VM provisioning

.. IMPORTANT:: Device paths in HVM always use WWN-based multipath names (``/dev/mapper/3<wwn>``), never positional names like ``/dev/mapper/mpathX``. Positional names differ across hosts and would cause mount failures on other cluster members.

NVMe over TCP
--------------

HVM clusters support **NVMe over TCP (NVMe/TCP)** as a storage transport for HPE Clustered Datastores. NVMe/TCP provides significantly lower latency and higher IOPS than iSCSI while using the same standard Ethernet infrastructure — no specialized HBAs or SAN fabric required.

.. NOTE:: NVMe/TCP support was validated in Morpheus 9.0.0 with the removal of Pacemaker. The |morpheus| Agent-based quorum system is fully compatible with NVMe/TCP-backed GFS2 datastores.

Host Requirements
^^^^^^^^^^^^^^^^^^

Each HVM host must have:

- Linux kernel 5.15+ (included in Ubuntu 24.04 used by HVM 1.3 cluster layout)
- The ``nvme-tcp`` kernel module loaded
- The ``nvme-cli`` package installed (for ``nvme connect`` and discovery)
- Network connectivity to the NVMe/TCP target on the configured port (default: 4420)

Connecting NVMe/TCP Targets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

NVMe/TCP targets must be connected on **all cluster hosts** before creating a GFS2 datastore. On each host:

#. Discover available subsystems:

   .. code-block:: bash

      sudo nvme discover -t tcp -a <target-ip> -s <port>

#. Connect to the target subsystem:

   .. code-block:: bash

      sudo nvme connect -t tcp -a <target-ip> -s <port> -n <subsystem-nqn>

#. Verify the NVMe namespace is visible:

   .. code-block:: bash

      sudo nvme list

#. Confirm the block device appears (e.g., ``/dev/nvme0n1``):

   .. code-block:: bash

      lsblk

For **persistent connections** that survive host reboots, create a discovery controller entry or use ``/etc/nvme/discovery.conf``:

.. code-block:: bash

   echo "-t tcp -a <target-ip> -s <port>" | sudo tee -a /etc/nvme/discovery.conf
   sudo systemctl enable --now nvme-connect@.service

.. NOTE:: Unlike iSCSI, NVMe/TCP does not use multipath device-mapper (``/dev/mapper/``). NVMe namespaces appear as ``/dev/nvmeXnY`` devices. For multipath with multiple paths to the same namespace, use the native NVMe multipath (``/sys/module/nvme_core/parameters/multipath`` set to ``Y``), which presents a single ``/dev/nvmeXnY`` device aggregating all paths.

Creating a GFS2 Datastore on NVMe/TCP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once the NVMe namespace is visible on all cluster hosts:

#. Navigate to the cluster detail page > Storage tab
#. Click :guilabel:`+ Add` to create a new HPE Clustered Datastore
#. Select the NVMe block device (e.g., ``/dev/nvme0n1``) as the block device
#. Complete the datastore creation as normal

GFS2 treats the NVMe namespace identically to any other block device — formatting, mounting, and DLM locking work the same as with iSCSI or FC-backed datastores.

Performance Considerations
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - Transport
     - Latency
     - Infrastructure
     - Best For
   * - iSCSI
     - Higher (~100-200μs)
     - Standard Ethernet
     - General workloads, legacy arrays
   * - Fibre Channel
     - Low (~50-100μs)
     - Dedicated SAN fabric + HBAs
     - Enterprise production, existing FC infrastructure
   * - NVMe/TCP
     - Lowest (~30-80μs)
     - Standard Ethernet (25GbE+ recommended)
     - Latency-sensitive workloads, all-flash arrays, new deployments

Pluggable Storage Backend
--------------------------

The HVM storage layer is **pluggable** — storage array management is handled by dedicated plugins rather than being built into the platform. This allows |morpheus| to support different storage backends without modifications to the core cluster code.

HPE Alletra MP Plugin
^^^^^^^^^^^^^^^^^^^^^^

The primary storage plugin for HVM clusters is the **HPE Alletra Block Storage** plugin. This plugin manages the full lifecycle of LUNs on HPE Alletra MP arrays:

- Creates and deletes LUNs (volumes) via Alletra REST APIs
- Exports LUNs to cluster hosts via host-sets (FC WWPNs or iSCSI IQNs)
- Handles LUN discovery, multipath device resolution, and online resize
- Supports snapshots, clones, and synchronous replication (remote copy groups)
- Generates storage-specific support bundle diagnostics

LUN-Per-vDisk Mode
^^^^^^^^^^^^^^^^^^^

In addition to the standard model where VMs store their virtual disks as files on a GFS2 shared filesystem, the Alletra MP plugin supports a **LUN-per-vDisk** mode where each virtual disk is backed by its own dedicated LUN on the storage array.

**Use cases:**

- Raw Device Mapping (RDM) workloads requiring direct block device access
- High-performance VMs that need dedicated I/O paths without filesystem overhead
- Applications that require consistent low-latency storage (databases, real-time analytics)

**How it works:**

- When a VM disk is created with the Alletra storage provider selected, the plugin provisions an individual LUN on the array
- The LUN is exported to **all hosts in the cluster** (not just the host currently running the VM) to support live migration and failover
- The block device is attached directly to the VM via its WWN-based multipath path

**Performance limits and considerations:**

.. WARNING:: Limit LUN-per-vDisk usage to approximately **800 vDisks per cluster**. Beyond this threshold, multipath management overhead saturates and storage performance degrades significantly. This limit applies to the total number of LUN-per-vDisk volumes across the entire cluster, regardless of cluster size.

- Because LUNs are exported to all hosts for failover support, the per-cluster limit is independent of the number of hosts — adding more hosts does not increase the maximum
- Use LUN-per-vDisk selectively for workloads that genuinely require it, not as a default for all VMs
- Standard GFS2-backed datastores are recommended for the majority of workloads and have no practical per-cluster vDisk limit
- Monitor the storage array's host-set export count and multipath device count on each host

.. list-table::
   :widths: 30 35 35
   :header-rows: 1

   * - Storage Mode
     - Best For
     - Considerations
   * - GFS2 Shared Datastore
     - General workloads, templates, most VMs
     - No per-vDisk limit, shared filesystem overhead, standard performance
   * - LUN-per-vDisk (Alletra)
     - RDM, high-performance VMs, dedicated I/O
     - ~800 vDisk cluster limit, higher array management overhead, direct block performance

Raw Device Block Mapping (RDBM)
-------------------------------

Raw Device Block Mapping (RDBM) allows attaching a raw host block device directly to an HVM virtual machine without an intermediate virtual disk file or clustered filesystem layer. This is analogous to VMware's Raw Device Mapping (RDM) feature and is ideal for performance-sensitive workloads, direct SCSI passthrough, or cluster applications requiring shared storage access.

When an RDBM volume is attached, the system creates a ``<disk type="block" device="disk">`` entry in the VM's libvirt configuration, with the host device path as the source.

Prerequisites
^^^^^^^^^^^^^

- The raw block device must be visible on the HVM host
- The device must not be part of an existing datastore or clustered filesystem
- A stable device path is recommended (e.g., ``/dev/disk/by-id/wwn-0x...``)
Attaching an RDBM Volume
^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to the HVM cluster detail page (:menuselection:`Infrastructure --> Clusters` > select cluster)
#. Select the **Storage Volumes** tab
#. Locate the raw block device volume to attach
#. Click :guilabel:`Attach` on the volume row
#. Select the target VM from the prompt
#. Confirm the attachment

   .. NOTE:: Volumes that are already backing a Datastore are excluded from the available list.

Hot-attach is supported for running VMs without requiring a reboot.

Detaching an RDBM Volume
^^^^^^^^^^^^^^^^^^^^^^^^^

RDBM volumes can be detached from a VM in two ways:

**From the Cluster Storage Volumes tab:**

#. Navigate to the HVM cluster detail page (:menuselection:`Infrastructure --> Clusters` > select cluster)
#. Select the **Storage Volumes** tab
#. Locate the attached RDBM volume
#. Click :guilabel:`Detach` on the volume row
#. Confirm the detachment

**From the VM Reconfigure action:**

#. Navigate to the VM detail page
#. Click the :guilabel:`Actions` dropdown and select :guilabel:`Reconfigure`
#. Remove the RDBM volume from the disk configuration
#. Save the reconfiguration

Hot-detach is supported for running VMs without requiring a reboot.

Limitations
^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Limitation
     - Description
   * - Host Pinning
     - VMs with RDBM volumes are pinned to the current host. Dynamic Placement will not migrate these VMs.
   * - No Cross-Host Migration
     - Even if the same SAN LUN is visible on multiple hosts, RDBM VMs cannot be live migrated in this release.
   * - Maintenance Mode
     - RDBM VMs are skipped during host maintenance mode evacuation with a warning. They must be manually shut down or moved.
   * - Move Operations Blocked
     - Placement move and manage operations are blocked for VMs with RDBM volumes, returning a clear error message.

.. NOTE:: Volumes with ``diskType=block`` that **do** have a Datastore association (such as Alletra shared LUNs) remain moveable and are not subject to these limitations. Only raw block devices without a Datastore association are treated as pinned RDBM volumes.
