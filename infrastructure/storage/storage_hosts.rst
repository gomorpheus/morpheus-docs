Storage Hosts
-------------

Overview
^^^^^^^^

Storage Hosts represent the physical or virtual hosts that are connected to a Storage Server for the purposes of volume presentation and LUN mapping. When a storage server is integrated into |morpheus| (for example, HPE Alletra MP), the platform automatically syncs and caches the registered hosts and host sets from the storage array.

Storage Hosts are used during datastore creation and volume mapping operations to determine which hosts should have access to a particular storage volume or LUN.

Viewing Storage Hosts
^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Storage``
#. Select the **SERVERS** tab
#. Click the name of a storage server to view its detail page
#. Select the **HOSTS** tab

The Hosts tab displays all hosts registered with the storage server, including:

- **Name** — The host name as reported by the storage array.
- **OS** — The operating system type of the host (where available).
- **WWN/IQN** — Fibre Channel World Wide Names or iSCSI Qualified Names associated with the host.
- **Host Set** — The host group or host set the host belongs to (if applicable).

Host Sets
^^^^^^^^^

Host Sets (also known as Host Groups) are logical groupings of storage hosts that share common volume access. When volumes are mapped to a Host Set, all member hosts gain access to the presented LUN.

Host Sets are synced automatically from the storage array and are used during datastore provisioning to define which group of hosts should see the new volume.

.. NOTE:: Storage Hosts and Host Sets are read-only in |morpheus| and are synced from the external storage server. To add or modify hosts, use the storage array's native management interface.

Sync Behavior
^^^^^^^^^^^^^

When a Storage Server is refreshed (either manually or on schedule), |morpheus| caches:

- **Hosts** — Individual host registrations on the array
- **Host Sets** — Grouped host definitions for multi-host volume access

These cached entries are used by the platform for volume mapping operations and datastore creation workflows.
