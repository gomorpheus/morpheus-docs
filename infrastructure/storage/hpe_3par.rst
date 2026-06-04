HPE 3PAR / Primera Storage
--------------------------

Overview
^^^^^^^^

|morpheus| integrates with HPE 3PAR and Primera storage arrays, providing synchronized visibility into storage groups (CPGs), volumes, hosts, and host sets. Once integrated, |morpheus| can create datastores by mapping volumes to host groups and presenting LUNs automatically.

The integration communicates with the 3PAR Web Services API (WSAPI) over HTTPS.

Prerequisites
^^^^^^^^^^^^^

- HPE 3PAR OS 3.2.1 or later, or HPE Primera OS
- WSAPI service enabled on the array (default port: 8008 for HTTPS)
- An administrative user account with API access
- Network connectivity from the |morpheus| appliance to the 3PAR WSAPI endpoint

Adding an HPE 3PAR Storage Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Storage``
#. Select the **SERVERS** tab
#. Click :guilabel:`+ ADD`
#. From the ADD STORAGE SERVER wizard, fill in the following:

   NAME
     Name of the Storage Server in |morpheus|.
   TYPE
     Select ``3Par``
   URL
     The WSAPI URL of the 3PAR array.
     Example: ``https://192.168.190.201:8008``
   USERNAME
     Administrative user account with API access.
   PASSWORD
     Password for the administrative user.

#. Click :guilabel:`SAVE CHANGES`

Upon successful connection, |morpheus| will sync the following from the array:

- **CPG Groups** — Common Provisioning Groups are displayed under Storage Groups
- **Volumes** — Virtual volumes provisioned on the array
- **Hosts** — Registered hosts with Fibre Channel or iSCSI connectivity
- **Host Sets** — Logical groupings of hosts for shared volume access

Synced Data
^^^^^^^^^^^

CPG Groups
  Common Provisioning Groups define the underlying disk configuration for volumes. CPGs are synced and displayed as Storage Groups.

Volumes
  Virtual volumes on the 3PAR array are synced and visible under the storage server's Volumes tab.

Hosts
  Individual host registrations (with WWN/IQN identifiers) connected to the array.

Host Sets
  Groups of hosts that share volume access, used for LUN presentation.

Creating a Datastore
^^^^^^^^^^^^^^^^^^^^

|morpheus| can create datastores on HPE 3PAR by mapping a volume to a host group (creating a vLUN). To create a datastore:

#. Navigate to the 3PAR storage server detail page
#. Select the **DATASTORES** tab
#. Click :guilabel:`+ ADD`
#. Configure the following fields:

   NAME
     Name for the new datastore.
   STORAGE GROUP
     Select the CPG (Common Provisioning Group) to provision from.
   HOST GROUP
     Select the Host Set to present the volume to.
   VOLUME
     Select or create the volume to map.

   The following options are available when creating a new volume:

   DISK TYPE
     The physical disk type for the volume:

     - **Fibre Channel** — High-performance FC disks
     - **Near Line** — High-capacity NL-SAS disks
     - **SSD** — Solid-state drives for maximum performance

   RAID TYPE
     The RAID level for data protection:

     - **Raid 0** — Striping only (no redundancy)
     - **Raid 1** — Mirroring
     - **Raid 5** — Striping with single parity
     - **Raid 6** — Striping with dual parity

   PROVISIONING TYPE
     How space is allocated on the array:

     - **FULL** — Fully provisioned (thick)
     - **TPVV** — Thin Provisioned Virtual Volume
     - **SNP** — Snapshot space
     - **PEER** — Peer persistence volume

   HA TYPE
     The high-availability layout preference:

     - **PORT** — Distribute across ports
     - **CAGE** — Distribute across drive cages
     - **MAG** — Distribute across magazines

#. Click :guilabel:`SAVE CHANGES`

|morpheus| will create a vLUN (virtual LUN) export on the 3PAR array, mapping the specified volume to the selected host set with auto-LUN assignment.

Refresh and Status
^^^^^^^^^^^^^^^^^^

The 3PAR integration refreshes automatically on a scheduled interval. During a refresh, |morpheus| will:

- Verify API connectivity
- Re-sync CPG groups, volumes, hosts, and host sets
- Update the storage server status indicator

Status indicators:

- **OK** — Connected and syncing normally
- **Error** — Connection failure or invalid credentials
- **Offline** — WSAPI endpoint is not reachable

If an error occurs, a health alarm is raised and displayed on the storage server.

.. NOTE:: The 3PAR integration uses token-based authentication. The API token is obtained at each sync interval and expires automatically.

Troubleshooting
^^^^^^^^^^^^^^^

- **"Error connecting to 3par"** — Verify the WSAPI URL is correct and the port (typically 8008) is accessible from the |morpheus| appliance.
- **"unauthorized - invalid credentials"** — Confirm the username and password have API access on the array.
- **"3par not found - invalid host"** — The WSAPI service may not be running on the target. Verify using ``https://<array-ip>:8008/api/v1/credentials`` in a browser.
