Shared Storage
^^^^^^^^^^^^^^

For configurations with 2 or more Applications Nodes, Shared Storage is required between the app nodes. Local Storage File Shares will need to be copied to a shared file system so all assets are available on all App nodes.

Assets
``````
* White label images
* Uploaded virtual images
* Deploy uploads
* Ansible Plays
* Terraform
* Morpheus backups

.. TIP:: Backups, deployments and virtual image storage locations can be overridden within the |morpheus|-ui.  You can find more information on storage here: :ref:`storage`

Moving existing appliance files to shared storage
````````````````````````````````````````````````````````````

Moving the Manager VM between HVM hosts or datastores is a hypervisor VM migration. It does **not** move the appliance files under ``/var/opt/morpheus/morpheus-ui`` to shared application storage. The procedure below concerns appliance files only.

Use a maintenance window. The application is unavailable while all application nodes are stopped. The exact shared-storage type, mount options, copy tool, ownership, and rollback sequence depend on the appliance release and storage platform. HPE does not publish one generic shell sequence for an existing VM Essentials Manager because an incomplete copy or mounting an empty target over the source can make appliance assets unavailable.

#. Confirm why the move is required. A single-node Manager does not gain application availability merely by moving this directory. If the goal is recovery from loss of the HVM host, first use the decision tree in :ref:`vme-manager-host-recovery`.
#. Open an HPE Support case with the Manager version, topology, current filesystem and usage, proposed storage type, mount endpoint and options, and maintenance window. Obtain a release-specific migration and rollback plan before changing the mount.
#. Create and verify all three recovery artifacts described in :doc:`/getting_started/guides/backup_restore`: an appliance database backup, a filesystem-level backup of ``/var/opt/morpheus/morpheus-ui``, and protected copies of appliance configuration and secrets. Keep the backups outside the Manager VM and outside the target being changed.
#. Validate the target from every future application node: capacity, latency, name resolution, permissions, stable boot-time mounting, and the same numeric UID/GID for ``morpheus-app`` and ``morpheus-local``. For NFS, include the ``sync`` requirement below.
#. Stop ``morpheus-ui`` on **every** application node as directed by the approved plan. Verify no node can write to the source before the final copy.
#. Follow the approved copy and mount sequence. Preserve ownership, permissions, links, timestamps, sparse files, and all hidden content. Mount the target at ``/var/opt/morpheus/morpheus-ui``; do not change application paths to point at an arbitrary staging directory.
#. Before startup, have the coordinator compare source and target content and verify ownership from every application node. Do not delete or repurpose the source.
#. Start one application node as directed. Verify the UI, uploaded virtual images, deployment archives, Ansible content, Terraform content, white-label assets, and appliance backup destination. Then start and verify remaining nodes one at a time.
#. Retain the source and verified backups for the rollback period in the approved plan.

Stop and contact HPE Support if the target mounts differently between nodes, UID/GID values differ, the final copy cannot be proven quiescent and complete, startup writes to the old location, or any asset is missing. Roll back by stopping all application nodes and restoring the original mount/source according to the approved plan; do not merge two independently modified copies.

.. important:: NFS mounts require ``sync`` option when using Ansible integration with |morpheus| Agent command bus execution enabled.

.. important:: On each application node, the morpheus-app and morpheus-local user and group uid/gid should be consistent.  If the uid and/or gid are different between nodes, when the permissions are applied during a reconfigure, the permissions can be incorrect for other nodes.  The uid and gid for the users can be seen by executing:  ``sudo cat /etc/passwd`` and ``sudo cat /etc/groups``
