Snapshots
---------

Overview
^^^^^^^^

Snapshots capture the state of a virtual machine's disk(s) at a specific point in time, allowing administrators to quickly revert a VM to a previous state if needed. |morpheus| provides centralized snapshot management across clouds, supporting creation, reversion, and deletion of snapshots.

Snapshots can be managed from the server/instance detail page or from a centralized snapshots view.

Role Requirements
^^^^^^^^^^^^^^^^^

- ``Infrastructure: Compute`` role permission at **Full** level is required to create, revert, or delete snapshots.
- **Read** access allows viewing existing snapshots.

Viewing Snapshots
^^^^^^^^^^^^^^^^^

From a Server:

#. Navigate to the server detail page
#. Select the **SNAPSHOTS** tab

The Snapshots tab displays all snapshots for the server, including:

- **Name** — Snapshot name or description
- **Date Created** — When the snapshot was taken
- **Size** — Disk space consumed by the snapshot
- **Status** — Snapshot state (active, creating, deleting)

Creating a Snapshot
^^^^^^^^^^^^^^^^^^^

#. Navigate to the server or instance detail page
#. Click :guilabel:`ACTIONS`
#. Select **Snapshot**
#. In the snapshot dialog, configure:

   NAME
     A descriptive name for the snapshot.
   DESCRIPTION
     Optional notes about the snapshot's purpose or what state it captures.
   MEMORY
     (Where supported) Include the VM's memory state in the snapshot. This allows reverting to the exact running state.
   QUIESCE
     (Where supported) Quiesce the guest file system before taking the snapshot. This ensures application-consistent data.

#. Click :guilabel:`CREATE`

The snapshot operation runs asynchronously. The new snapshot will appear in the Snapshots tab once complete.

Reverting to a Snapshot
^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to the server's **SNAPSHOTS** tab
#. Click the revert icon next to the desired snapshot
#. Confirm the revert operation

.. WARNING:: Reverting to a snapshot discards all changes made since the snapshot was taken. This includes disk writes, configuration changes, and (if memory was not captured) the running state of applications.

Deleting a Snapshot
^^^^^^^^^^^^^^^^^^^

#. Navigate to the server's **SNAPSHOTS** tab
#. Click the delete icon next to the snapshot
#. Confirm the deletion

Deleting a snapshot consolidates the snapshot data back into the base disk. This frees the space consumed by the snapshot delta.

Deleting All Snapshots
^^^^^^^^^^^^^^^^^^^^^^

To remove all snapshots for a server:

#. Navigate to the server's **SNAPSHOTS** tab
#. Click :guilabel:`DELETE ALL`
#. Confirm the deletion

.. NOTE:: Deleting all snapshots consolidates the entire snapshot chain. This operation may take time for VMs with large or numerous snapshots.

Importing Snapshots
^^^^^^^^^^^^^^^^^^^

|morpheus| can import existing snapshots from the hypervisor:

#. Navigate to the server detail page
#. Click :guilabel:`ACTIONS`
#. Select **Import Snapshot**
#. Select the snapshot to import from the hypervisor
#. Click :guilabel:`IMPORT`

Snapshot Best Practices
^^^^^^^^^^^^^^^^^^^^^^^

- **Keep snapshots short-lived** — Snapshots consume increasing disk space over time as the delta grows. Delete snapshots once they are no longer needed.
- **Don't use as backups** — Snapshots are not a replacement for proper backups. They reside on the same storage as the VM and are lost if the storage fails.
- **Limit chain depth** — Avoid creating deep chains of snapshots (snapshot of a snapshot). Performance degrades with chain depth.
- **Quiesce when possible** — For application consistency, always quiesce the guest file system before snapshotting databases or transactional workloads.
- **Archive snapshots** — Configure the default archive store (``Administration > Settings > Appliance > Archive Store``) if snapshots need to be stored externally.

Supported Cloud Types
^^^^^^^^^^^^^^^^^^^^^

Snapshot support varies by cloud type:

- **VMware vSphere** — Full support including memory snapshots and quiescing
- **Nutanix AHV** — Snapshot support without memory state
- **KVM/MVM** — Snapshot support via libvirt/qemu snapshots
- **Azure** — Managed disk snapshots
- **AWS** — EBS snapshots (volume-level)

.. NOTE:: Some cloud types may not support all snapshot options (e.g., memory snapshots, quiescing). Unavailable options will be hidden or greyed out in the dialog.
