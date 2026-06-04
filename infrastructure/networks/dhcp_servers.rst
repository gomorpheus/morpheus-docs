.. _dhcp_servers:

DHCP Servers
------------

``Infrastructure > Network > Integrations > (select Network Server) > DHCP``

Overview
^^^^^^^^

The DHCP Servers section provides management of DHCP (Dynamic Host Configuration Protocol) servers within a network integration. DHCP servers automatically assign IP addresses and network configuration parameters to devices on the network. |morpheus| syncs DHCP server configurations from supported network integrations such as VMware NSX-T and allows creation, editing, and deletion of DHCP servers directly from the UI.

.. NOTE:: DHCP server management is available on network server integrations that support this capability (``hasDhcpServers`` flag). Currently, NSX-T is the primary integration supporting DHCP server management.

Viewing DHCP Servers
^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select the desired network server integration (e.g., NSX-T)
#. Click the **DHCP** tab
#. DHCP Servers are displayed in the upper section of the tab

The list view displays DHCP server name, server address, lease time, and status information.

Adding a DHCP Server
^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select the desired network server integration
#. Click the **DHCP** tab
#. Click :guilabel:`+ ADD` in the DHCP Servers section
#. Complete the required fields (fields vary by integration type):

   :Name: A name for the DHCP server in |morpheus|
   :Server Address: The IP address of the DHCP server
   :Lease Time: The duration (in seconds) for IP address leases
   :Edge Cluster: (NSX-T) The edge cluster to associate with this DHCP server
   :Server IP: (NSX-T) The IP address to assign to the server profile

   .. NOTE:: Additional fields may appear based on the network integration type and its configured option types.

#. Click :guilabel:`SAVE`

Editing a DHCP Server
^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select the desired network server integration
#. Click the **DHCP** tab
#. Click the pencil (edit) icon for the target DHCP server
#. Modify the desired fields
#. Click :guilabel:`SAVE`

Deleting a DHCP Server
^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select the desired network server integration
#. Click the **DHCP** tab
#. Click the trash (delete) icon for the target DHCP server
#. Confirm the deletion when prompted

.. WARNING:: Deleting a DHCP server will remove the server from both |morpheus| and the upstream integration. Any clients relying on this server for address assignment will be affected.

API
^^^

DHCP servers are managed through the |morpheus| API at the following endpoints:

- ``GET /api/networks/servers/:serverId/dhcp-servers`` — List DHCP servers
- ``GET /api/networks/servers/:serverId/dhcp-servers/:id`` — Get a specific DHCP server
- ``POST /api/networks/servers/:serverId/dhcp-servers`` — Create a DHCP server
- ``PUT /api/networks/servers/:serverId/dhcp-servers/:id`` — Update a DHCP server
- ``DELETE /api/networks/servers/:serverId/dhcp-servers/:id`` — Delete a DHCP server

Required Role Permissions
^^^^^^^^^^^^^^^^^^^^^^^^^

Access to DHCP server management requires the ``Infrastructure: Network DHCP Server`` permission (``infrastructure-network-dhcp-server``) with ``read`` or ``full`` access.
