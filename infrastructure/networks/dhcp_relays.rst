.. _dhcp_relays:

DHCP Relays
-----------

``Infrastructure > Network > Integrations > (select Network Server) > DHCP``

Overview
^^^^^^^^

DHCP Relays forward DHCP requests from clients on one network segment to a DHCP server on another segment. This eliminates the need for a DHCP server on every subnet while still allowing clients to receive dynamic IP address assignments. |morpheus| supports creating, editing, and deleting DHCP relays within supported network server integrations such as VMware NSX-T.

.. NOTE:: DHCP relay management is available on network server integrations that support this capability (``hasDhcpRelays`` flag).

Viewing DHCP Relays
^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select the desired network server integration (e.g., NSX-T)
#. Click the **DHCP** tab
#. DHCP Relays are displayed in the lower section of the tab, below DHCP Servers

Adding a DHCP Relay
^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select the desired network server integration
#. Click the **DHCP** tab
#. Click :guilabel:`+ ADD` in the DHCP Relays section
#. Complete the required fields (fields vary by integration type):

   :Name: A name for the DHCP relay in |morpheus|
   :Server Addresses: The IP addresses of the DHCP server(s) to relay requests to

   .. NOTE:: Additional fields may appear based on the network integration type and its configured option types.

#. Click :guilabel:`SAVE`

Editing a DHCP Relay
^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select the desired network server integration
#. Click the **DHCP** tab
#. Click the pencil (edit) icon for the target DHCP relay
#. Modify the desired fields
#. Click :guilabel:`SAVE`

Deleting a DHCP Relay
^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select the desired network server integration
#. Click the **DHCP** tab
#. Click the trash (delete) icon for the target DHCP relay
#. Confirm the deletion when prompted

.. WARNING:: Deleting a DHCP relay will remove the relay from both |morpheus| and the upstream integration. Clients on segments served by this relay will lose the ability to obtain DHCP leases.

API
^^^

DHCP relays are managed through the |morpheus| API at the following endpoints:

- ``GET /api/networks/servers/:serverId/dhcp-relays`` — List DHCP relays
- ``GET /api/networks/servers/:serverId/dhcp-relays/:id`` — Get a specific DHCP relay
- ``POST /api/networks/servers/:serverId/dhcp-relays`` — Create a DHCP relay
- ``PUT /api/networks/servers/:serverId/dhcp-relays/:id`` — Update a DHCP relay
- ``DELETE /api/networks/servers/:serverId/dhcp-relays/:id`` — Delete a DHCP relay

Required Role Permissions
^^^^^^^^^^^^^^^^^^^^^^^^^

Access to DHCP relay management requires the ``Infrastructure: Network DHCP Relay`` permission (``infrastructure-network-dhcp-relay``) with ``read`` or ``full`` access.
