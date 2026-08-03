.. _vdi-gateways:

VDI Gateways
=============

Overview
--------

VDI Gateways provide a secure connection point between end users and VDI desktop sessions. A gateway acts as a proxy, routing VDI traffic through a controlled network path. This is essential for environments where VDI desktops reside on isolated networks not directly accessible to end users.

VDI Gateways are managed from |TooVDIGat|.

.. NOTE:: VDI Gateways require the ``services-vdi-pools`` Role permission (Read or Full).

Gateway Architecture
--------------------

The VDI Gateway sits between the user's browser and the Guacamole session:

.. code-block:: text

   User Browser → VDI Gateway → Guacamole Server → VDI Desktop (RDP/VNC)

This architecture enables:

- **Network isolation** — VDI desktops can be on a private network inaccessible to users directly
- **Load distribution** — Multiple gateways can distribute connection load
- **Security** — All VDI traffic routes through a controlled proxy with API key authentication
- **Geographic distribution** — Place gateways closer to users for reduced latency

The same VDI Gateway registration can also route Instance and Host consoles. Assign it on a Network or Cloud, or select it as the Default Console Gateway in |AdmSetApp|. VDI desktop routing is separate: assign the gateway to a VDI Pool in |TooVDIPoo|. Both uses authenticate the Worker runtime with the VDI Gateway API key.

The same runtime can additionally act as a Distributed Worker when configured with a Distributed Worker key. See :doc:`/administration/integrations/workers` for the role and key matrix and canonical package and container deployment instructions.

Creating a VDI Gateway
-----------------------

#. Navigate to |TooVDIGat|
#. Click :guilabel:`+ ADD`
#. Configure:

   NAME
     Unique name for the gateway (must be unique per tenant)
   DESCRIPTION
     Optional description of the gateway's purpose or location
   GATEWAY URL
     The URL where the gateway service is accessible (e.g., ``https://vdi-gw.example.com:8443``)

#. Click :guilabel:`SAVE`

Upon creation, |morpheus| generates an **API Key** for the gateway. This key is used by the gateway service to authenticate with the |morpheus| appliance.

.. IMPORTANT:: Copy the API Key immediately after creation. It is used to configure the gateway service and cannot be retrieved later (only regenerated).

Editing a VDI Gateway
----------------------

#. Navigate to |TooVDIGat|
#. Click the gateway name or select the edit action
#. Modify the name, description, or gateway URL
#. Click :guilabel:`SAVE`

.. NOTE:: The API Key cannot be changed through the edit interface. To regenerate a key, delete and recreate the gateway.

Deleting a VDI Gateway
-----------------------

#. Navigate to |TooVDIGat|
#. Select the gateway to delete
#. Click :guilabel:`DELETE`
#. Confirm deletion

.. WARNING:: A gateway cannot be deleted if it is currently assigned to one or more VDI Pools. Remove the gateway assignment from all pools before deleting.

Assigning Gateways to Pools
-----------------------------

VDI Gateways are assigned at the Pool level:

#. Navigate to |TooVDIPoo|
#. Edit or create a VDI Pool
#. In the pool configuration, select the desired **Gateway** from the dropdown
#. Save the pool

When a gateway is assigned to a pool, all user sessions for that pool route through the specified gateway.

Gateway Configuration Fields
------------------------------

.. list-table::
   :widths: 20 50 15 15
   :header-rows: 1

   * - Field
     - Description
     - Required
     - Default
   * - Name
     - Unique identifier for the gateway
     - Yes
     - —
   * - Description
     - Purpose or location note
     - No
     - null
   * - Gateway URL
     - URL of the gateway service endpoint
     - No
     - null
   * - API Key
     - Auto-generated authentication key
     - Auto
     - Generated on save
   * - Enabled
     - Whether the gateway is active
     - No
     - true

Deploying the Gateway Service
------------------------------

The VDI Gateway service is a separate component that must be deployed on a server with network access to both:

- The |morpheus| appliance (for API communication)
- The VDI desktop network (for RDP/VNC proxying)

Configuration requirements:

1. Install the gateway service package
2. Configure the gateway URL to match what was entered in |morpheus|
3. Set the API Key from the |morpheus| gateway configuration
4. Ensure ports are open:

   - Inbound from users (typically 443 or 8443)
   - Outbound to VDI desktops (RDP 3389, VNC 5900+)
   - Outbound to |morpheus| appliance (443)

For current package and `morpheusdata/morpheus-worker <https://hub.docker.com/r/morpheusdata/morpheus-worker>`_ container procedures, TLS options, environment variables, combined-role configuration, logs, and upgrades, see :doc:`/administration/integrations/workers`.

API Reference
--------------

VDI Gateways are manageable via the |morpheus| API:

- ``GET /api/vdi-gateways`` — List all VDI Gateways
- ``GET /api/vdi-gateways/:id`` — Get a specific gateway
- ``POST /api/vdi-gateways`` — Create a gateway
- ``PUT /api/vdi-gateways/:id`` — Update a gateway
- ``DELETE /api/vdi-gateways/:id`` — Delete a gateway

Troubleshooting
----------------

- **Gateway unreachable:** Verify the Gateway URL is accessible from the |morpheus| appliance and from end-user browsers
- **Authentication failed:** Ensure the API Key configured on the gateway service matches the one generated in |morpheus|
- **Cannot delete gateway:** Remove the gateway assignment from all VDI Pools first
- **Sessions not routing through gateway:** Verify the pool has the gateway assigned and that the gateway service is running
