Snapshots
=========

|morpheus| supports point-in-time snapshots of HVM virtual machines for backup, recovery, and testing purposes. The snapshot mechanism varies depending on the underlying storage backend.

Snapshot Consistency Model
--------------------------

HVM snapshots provide different levels of consistency depending on the storage backend and whether the QEMU Guest Agent is available:

**Application-consistent snapshots (QEMU Guest Agent connected):**

When the QEMU Guest Agent is installed and connected, |morpheus| quiesces the guest filesystem before taking the snapshot:

- **Linux guests:** A ``sync`` command flushes pending I/O, then ``fsfreeze`` is applied to freeze all filesystems before the snapshot
- **Windows guests:** The ``fsfreeze`` call triggers **Volume Shadow Copy Service (VSS)** inside the guest via the QEMU Guest Agent, which notifies VSS-aware applications (SQL Server, Exchange, Active Directory, etc.) to flush their buffers and enter a consistent state before the snapshot

This provides **application-consistent** snapshots for both Linux and Windows when the guest agent is available.

**Crash-consistent snapshots (no QEMU Guest Agent):**

When the guest agent is not installed or not responding, snapshots are **crash-consistent** — they capture the disk state at a point in time, equivalent to an unexpected power loss:

- No filesystem freeze or application quiescing is performed
- Modern journaling filesystems (ext4, XFS, NTFS) recover cleanly from crash-consistent state
- Applications with their own write-ahead logs (databases) can also recover, but uncommitted transactions may be lost

.. NOTE:: |morpheus| logs a warning when a snapshot is taken without the guest agent connected, indicating that the snapshot will be crash-consistent only. For production workloads, ensure the QEMU Guest Agent is installed and running to achieve application-consistent snapshots.

No memory state is captured in any snapshot mode — reverting a snapshot requires the VM to be restarted.

Snapshot Types by Storage Backend
----------------------------------

.. list-table::
   :widths: 20 25 55
   :header-rows: 1

   * - Storage Backend
     - Snapshot Type
     - Description
   * - GFS2 / NFS (file-based)
     - External qcow2 overlay
     - Creates a new qcow2 overlay file that captures all writes after the snapshot point. The base image remains unchanged. This is the most common type for HVM clusters.
   * - Ceph RBD
     - RBD snapshot
     - Creates a point-in-time snapshot at the Ceph cluster level.
   * - HPE Alletra MP (array-based)
     - Storage array snapshot
     - Snapshot is created on the HPE Alletra storage array via REST API. The hypervisor is not involved. Provides hardware-accelerated, space-efficient snapshots at the array firmware level.

Taking a Snapshot
-----------------

#. Navigate to the VM detail page
#. Click :guilabel:`Actions` > :guilabel:`Create Snapshot`
#. Enter a name for the snapshot
#. Click :guilabel:`Create`

The Instance action is labeled :guilabel:`Create Snapshot` in current navigation. It appears only for snapshot-capable layouts and users with **Snapshots: Full** permission. See :doc:`/provisioning/instances/managing_instances` for action availability.

For VMs with multiple disks, all disks are snapshotted atomically (when supported by the storage backend). CD-ROM volumes are excluded from snapshots.

How File-Based Snapshots Work (GFS2/NFS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When a snapshot is created on a file-based datastore:

#. If the QEMU Guest Agent is connected:

   - **Linux:** A ``sync`` command flushes pending I/O
   - **Windows:** Sync is skipped (not a Windows command); VSS quiescing is handled by the ``--quiesce`` flag in the next step
   - The snapshot is created with the ``--quiesce`` flag, which triggers filesystem freeze (and VSS on Windows) via the guest agent

#. If the QEMU Guest Agent is not connected:

   - No pre-snapshot flush or freeze is performed
   - A warning is logged indicating the snapshot will be crash-consistent only
   - The snapshot proceeds without quiescing

#. An external qcow2 overlay is created for each disk using an atomic operation
#. The VM continues running — writes go to the new overlay file
#. The original disk image is preserved as read-only at the point-in-time state

The snapshot file is stored alongside the original disk image on the same datastore.

How Array-Based Snapshots Work (HPE Alletra)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When a VM uses storage backed by an HPE Alletra array:

#. |morpheus| calls the Alletra REST API to create a snapshot of the volume set
#. The snapshot is created as a read-only point-in-time copy at the array level
#. No hypervisor-level operation is needed — the VM continues running uninterrupted
#. The array handles space efficiency internally using copy-on-write

Array-based snapshots are recommended for production workloads due to their minimal performance impact and hardware-accelerated operation.

Reverting a Snapshot
--------------------

#. Navigate to the VM detail page
#. Select the **Snapshots** tab
#. Click :guilabel:`Revert` on the desired snapshot

**What happens during revert:**

#. The guest filesystem is frozen (if the QEMU Guest Agent is available)
#. The VM is powered off
#. The disk is rolled back to the snapshot state:

   - **File-based:** The overlay is discarded and the base image becomes active
   - **RBD:** The volume is rolled back to the snapshot point
   - **Alletra:** The array reverts the volume set to the snapshot state

#. The guest filesystem is thawed
#. The VM is restarted

.. WARNING:: Reverting a snapshot discards all changes made since the snapshot was taken. This operation cannot be undone.

Deleting a Snapshot
-------------------

#. Navigate to the VM detail page
#. Select the **Snapshots** tab
#. Click :guilabel:`Delete` on the snapshot to remove

**What happens during deletion:**

- **File-based:** The overlay is committed (merged) back into the base image, then removed. This preserves all changes made since the snapshot while freeing the snapshot overhead.
- **RBD:** The RBD snapshot is deleted.
- **Alletra:** The snapshot set is deleted from the array.

.. NOTE:: For file-based snapshots, deletion involves a block-commit operation that merges the overlay into the base image. This is an I/O-intensive operation and may take time for large disks.

Image Import Behavior
---------------------

Existing snapshots are supported when importing an HVM VM as a Virtual Image. For file-based storage, |morpheus| copies and merges the active qcow2 backing chain into a temporary export disk. This operation does not delete or merge the VM's existing snapshots. Other supported storage backends create a temporary export snapshot using their datastore implementation.

The resulting Virtual Image must contain both ``metadata.json`` and every referenced disk artifact. A metadata-only result is an incomplete import, not evidence that existing snapshots must be deleted. Preserve the source VM and snapshots and see :doc:`/library/virtual_images/virtual_images` for verification and escalation guidance.

Limitations
-----------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Limitation
     - Description
   * - No memory snapshots
     - Only disk state is captured. The VM must be restarted after a revert. Running applications will not resume from their pre-snapshot state.
   * - Guest agent required for app consistency
     - Without the QEMU Guest Agent, snapshots are crash-consistent only. Install and enable the guest agent for application-consistent snapshots with VSS support on Windows.
   * - Mixed storage VMs
     - VMs with disks on different storage backends may have partial snapshots. For example, a VM with one disk on GFS2 and another on Alletra will snapshot each through its respective mechanism.
   * - Concurrent operations
     - A VM cannot be snapshotted while a clone operation is in progress.
   * - RDBM/Raw block devices
     - VMs with raw device block mapping (RDBM) volumes cannot have those volumes snapshotted through the file-based mechanism. Use array-based snapshots for these workloads.
