Server Migration
----------------

Overview
^^^^^^^^

|morpheus| supports migrating virtual machines between hosts, clusters, or resource pools within a cloud. The migration (also referred to as VM Move) allows you to relocate a workload to a different compute target without reprovisioning.

Migration is supported for cloud types that provide native VM mobility, such as VMware vSphere (vMotion), Nutanix AHV, and other hypervisor platforms.

Role Requirements
^^^^^^^^^^^^^^^^^

- ``Infrastructure: Compute`` role permission at **Full** level is required to perform migrations.

Migrating a Server
^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Compute > Virtual Machines`` or to the server detail page
#. Select the target server
#. Click :guilabel:`ACTIONS`
#. Select **Migrate**
#. In the migration dialog, configure:

   TARGET HOST
     Select the destination hypervisor host. Available hosts are filtered based on the server's current cloud and compatibility.
   TARGET RESOURCE POOL
     Select the destination resource pool or cluster (if applicable). This may be required for cross-cluster migrations.
   TARGET DATASTORE
     Select the destination datastore for the VM's storage (for storage migrations or combined compute+storage moves).
   PRIORITY
     Migration priority level (where supported by the hypervisor):

     - **Low** — Background migration with minimal impact
     - **Normal** — Standard priority
     - **High** — Prioritized migration

#. Click :guilabel:`EXECUTE`

The migration operation runs asynchronously. Progress can be monitored on the server's History tab.

Migration Types
^^^^^^^^^^^^^^^

Live Migration (vMotion)
  The VM is moved while running, with no downtime. Requires shared storage or storage vMotion capability between source and destination hosts.

Cold Migration
  The VM is powered off, moved to the new location, and optionally powered back on. Used when live migration prerequisites are not met.

Storage Migration
  Only the VM's storage is relocated to a different datastore. The VM remains on the same host.

For HVM/KVM clusters, use :guilabel:`Actions` > :guilabel:`Move` on the Instance or VM detail page to relocate a VM to another host or HVM cluster. Cross-cluster moves map datastores and networks on the destination cluster. This is not a VMware-to-HVM conversion. See :doc:`/infrastructure/clusters/hvm/vm_migration`.

.. NOTE:: Migration availability and options depend on the underlying cloud type and hypervisor capabilities. Not all cloud types support all migration modes.

Monitoring Migration Status
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Migration operations appear in the server's **History** tab with status indicators:

- **Running** — Migration is in progress
- **Complete** — Migration finished successfully
- **Failed** — Migration encountered an error (check event details for the failure reason)

VME Migration: LVM and Source SCSI Disks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before migrating a VM that uses Linux LVM, record the source physical volumes, volume groups, logical volumes, mount points, boot volume, and the controller and unit number for every virtual disk. Confirm that all required source disks are included in the migration plan and mapped to destination datastores with at least the source capacity. The guest must be able to load the destination storage driver and discover every volume required for boot and application data.

The migration planner preserves source controller bus and unit mappings where they are available. When a source VM has any SCSI-backed volume, the HVM destination uses a VirtIO-SCSI controller for the post-conversion disk mapping; otherwise it uses VirtIO Block. Windows migrations that install guest tools boot initially from SATA while VirtIO drivers are registered, then stop the destination VM and move its disks to the selected paravirtual controller. Do not manually change controller mappings while that migration is running.

The legacy **LVM Migration** backup type is a separate, deprecated workflow. Its implementation requires SSH and sudo access to source and destination, ``lvm2`` and ``pv``, an explicitly selected source logical-volume device, enough free space in the source volume group for an LVM snapshot, a writable destination data device, and key-based transfer connectivity from source to destination. It copies a single selected logical-volume snapshot and is not evidence that arbitrary multi-PV, thin-pool, encrypted, clustered, or nested LVM layouts are supported.

After migration, verify that the destination boots from the expected controller, every expected disk is present at the intended bus/unit mapping, all volume groups and logical volumes activate, filesystems mount, and application data is accessible. If discovery does not match the recorded source layout, stop validation and retain the source VM; do not invent device-renaming or bootloader repair steps.
