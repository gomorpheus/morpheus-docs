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
#. If using existing targets, trigger a rescan:

   .. code-block:: bash

      sudo iscsiadm -m session --rescan

#. Verify the new LUN is visible on all hosts:

   .. code-block:: bash

      sudo multipath -ll

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

#. Navigate to the HVM cluster detail page (|InfClu| > select cluster)
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

#. Navigate to the HVM cluster detail page (|InfClu| > select cluster)
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
