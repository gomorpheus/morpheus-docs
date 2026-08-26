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

Creating Linked Clone Images
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

VMware and HVM/KVM snapshots can be registered as linked clone Virtual Images. A linked clone uses the selected snapshot as a shared backing disk instead of copying the complete source disk. This reduces provisioning time and initial storage consumption, but creates a dependency on the source VM and snapshot.

Prepare the guest before taking the snapshot. Otherwise, every VM provisioned from the linked clone can inherit the source hostname, machine identity, SSH host keys, network rules, or Windows system identity. Complete the guest preparation steps below before creating the snapshot.

#. Prepare and shut down the source VM.
#. On the Instance detail page, select :guilabel:`Actions` > :guilabel:`Create Snapshot`.
#. Enter a recognizable name and create the snapshot.
#. Select the Instance :guilabel:`Backups` tab.
#. Locate the completed snapshot, select :guilabel:`More`, and then select :guilabel:`Create Linked Clone`.
#. Confirm the operation.
#. Navigate to :menuselection:`Library --> Virtual Images` and open the Virtual Image whose name matches the snapshot.
#. Verify its operating system, guest customization, cloud-init or Sysprep, agent, credentials, and tenant permissions before using it in an Instance Type or provisioning workflow.

The :guilabel:`Create Linked Clone` action appears only for supported provision types and users with **Snapshots: Linked Clone** permission set to **Full**. Creating it registers a Virtual Image record; it does not create a VM. VMs are created when that Virtual Image is selected during provisioning.

**Guest Preparation**

Complete application installation, patching, and configuration before generalizing the guest. Do not start the source VM again between generalization and snapshot creation.

**Windows**

Use Sysprep to remove the source system identity and start OOBE on the first boot of each provisioned VM:

.. code-block:: powershell

   & "$env:SystemRoot\System32\Sysprep\sysprep.exe" /generalize /oobe /shutdown

After Sysprep shuts down the VM, leave it powered off and create the snapshot. On the resulting Virtual Image, enable **Sysprep**. For platform-specific customization behavior, including VMware **Force Guest Customization**, see :doc:`/provisioning/windows_cloud_guest_customization`.

**Linux**

For a cloud-init-enabled Linux guest, clear instance state and identifiers before shutdown. The exact files vary by distribution; the following is appropriate for current Ubuntu images:

.. code-block:: bash

   sudo cloud-init clean --logs --machine-id
   sudo rm -f /etc/ssh/ssh_host_*
   sudo rm -f /etc/udev/rules.d/70-persistent-net.rules
   sudo truncate -s 0 /etc/machine-id
   sudo poweroff

If ``/var/lib/dbus/machine-id`` is a regular file rather than a symbolic link to ``/etc/machine-id``, remove or empty it according to the distribution's image-preparation guidance. Remove only persistent udev rules created for the source VM; do not remove distribution-supplied rules. Verify that cloud-init is installed and enabled, then leave **Cloud Init Enabled** selected on the resulting Virtual Image.

**Dependencies and Limitations**

- Do not treat a linked clone as an independent image. The source VM and selected snapshot remain part of its backing chain.
- Do not delete the backing snapshot or source VM while linked-clone VMs depend on them. HVM blocks these operations when it detects active dependents.
- VMware linked clone images are primarily intended for rapid provisioning such as VDI pools and cannot be resized.
- HVM linked clones require a file-based datastore and QCOW2 disks. LUN-per-vDisk storage, including HPE Alletra datastore types, does not support linked clones.
- HVM linked clones on local storage are pinned to the source hypervisor. Host migration is not supported. HVM storage migration is not supported because the overlay depends on the original snapshot backing file.
- Shared HVM storage avoids local-host pinning, but the backing snapshot must remain available in its original datastore.
- Changes made to the source VM after the snapshot are not included. To publish an updated image, prepare the source again, create a new snapshot, and create a new linked clone Virtual Image.
- Snapshot chains add storage and performance dependencies. Keep chains shallow and monitor the source datastore's capacity and health.

**API**

Create a linked clone Virtual Image via the API:

- ``PUT /api/instances/{instanceId}/linked-clone/{snapshotId}``
- ``PUT /api/servers/{serverId}/linked-clone/{snapshotId}``

These endpoints register the snapshot as a linked clone Virtual Image. Provisioning a VM from the image then creates the thin overlay automatically.

Snapshot Best Practices
^^^^^^^^^^^^^^^^^^^^^^^

- **Keep snapshots short-lived** — Snapshots consume increasing disk space over time as the delta grows. Delete snapshots once they are no longer needed.
- **Don't use as backups** — Snapshots are not a replacement for proper backups. They reside on the same storage as the VM and are lost if the storage fails.
- **Limit chain depth** — Avoid creating deep chains of snapshots (snapshot of a snapshot). Performance degrades with chain depth.
- **Quiesce when possible** — For application consistency, always quiesce the guest file system before snapshotting databases or transactional workloads.
- **Archive snapshots** — Configure the default archive store (``Administration > Settings > Appliance > Archive Store``) if snapshots need to be stored externally.

Supported Cloud Types
^^^^^^^^^^^^^^^^^^^^^

Snapshot support is available on more cloud types than linked clone Virtual Image creation. Linked clone creation is supported only for VMware vSphere and HVM/KVM.

.. list-table::
   :widths: 25 50 25
   :header-rows: 1

   * - Cloud Type
     - Snapshot Support
     - Linked Clone Virtual Images
   * - VMware vSphere
     - Full support including memory snapshots and quiescing
     - **Supported**
   * - HVM/KVM
     - Libvirt/QEMU snapshots
     - **Supported on file-based datastores with QCOW2 disks only**; not supported on LUN-per-vDisk storage such as HPE Alletra
   * - Nutanix AHV
     - Snapshots without memory state
     - Not supported
   * - Azure
     - Managed disk snapshots
     - Not supported
   * - AWS
     - EBS snapshots at the volume level
     - Not supported

.. NOTE:: Some cloud types may not support all snapshot options (e.g., memory snapshots, quiescing). Unavailable options will be hidden or greyed out in the dialog.
