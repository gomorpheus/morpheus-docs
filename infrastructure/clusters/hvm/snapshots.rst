Snapshots
=========

|morpheus| supports point-in-time snapshots of HVM virtual machines for backup, recovery, and testing purposes. The snapshot mechanism varies depending on the underlying storage backend.

Snapshot Consistency Model
--------------------------

HVM snapshots are **crash-consistent** by default — they capture the disk state at a point in time, equivalent to pulling the power and recovering from the resulting state. They are **not** application-consistent:

- A filesystem ``sync`` is issued to Linux guests before the snapshot (to flush pending writes)
- No filesystem freeze (``fsfreeze``) is performed during snapshot creation
- No memory state is captured — reverting a snapshot requires the VM to be restarted
- Windows guests skip the ``sync`` command entirely

.. NOTE:: For application-consistent snapshots (e.g., databases), stop the application or use application-level backup tools before taking the snapshot. The crash-consistent approach is safe for most workloads since modern filesystems (ext4, XFS, NTFS) include journaling that recovers cleanly from crash-consistent state.

For array-based snapshots (HPE Alletra), the storage array provides its own consistency guarantees at the block level.

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
#. Click :guilabel:`Actions` > :guilabel:`Snapshot`
#. Enter a name for the snapshot
#. Click :guilabel:`Create`

For VMs with multiple disks, all disks are snapshotted atomically (when supported by the storage backend). CD-ROM volumes are excluded from snapshots.

How File-Based Snapshots Work (GFS2/NFS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When a snapshot is created on a file-based datastore:

#. A ``sync`` command is issued to the guest (Linux only) to flush pending I/O
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

Limitations
-----------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Limitation
     - Description
   * - No memory snapshots
     - Only disk state is captured. The VM must be restarted after a revert. Running applications will not resume from their pre-snapshot state.
   * - Crash-consistent only
     - No application-level quiescing is performed during snapshot creation. Use application-level tools for database-consistent backups.
   * - Windows guests
     - The ``sync`` flush is skipped for Windows guests. Crash consistency relies on NTFS journal recovery.
   * - Mixed storage VMs
     - VMs with disks on different storage backends may have partial snapshots. For example, a VM with one disk on GFS2 and another on Alletra will snapshot each through its respective mechanism.
   * - Concurrent operations
     - A VM cannot be snapshotted while a clone operation is in progress.
   * - RDBM/Raw block devices
     - VMs with raw device block mapping (RDBM) volumes cannot have those volumes snapshotted through the file-based mechanism. Use array-based snapshots for these workloads.
