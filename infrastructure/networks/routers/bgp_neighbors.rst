.. _bgp_neighbors:

BGP Neighbors
-------------

``Infrastructure > Network > Routers > (select Router) > BGP``

Overview
^^^^^^^^

The BGP (Border Gateway Protocol) tab on a network router provides management of BGP neighbor (peer) configurations. BGP is the primary exterior gateway protocol used for routing between autonomous systems on the Internet and within large enterprise networks. |morpheus| supports configuring BGP neighbors on router types that expose this capability, such as NSX Tier-0 Gateways.

.. NOTE:: The BGP tab is available on router types that support BGP (``hasBgp`` flag). Currently, NSX Tier-0 Gateways are the primary router type with BGP neighbor support in |morpheus|.

Viewing BGP Neighbors
^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Routers``
#. Click on the target router to access the detail view
#. Click the **BGP** tab
#. The list view displays BGP neighbors with their IP address, Remote AS, and status information

Use the search bar to filter neighbors by IP address, remote AS number, or description.

Adding a BGP Neighbor
^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Routers``
#. Click on the target router to access the detail view
#. Click the **BGP** tab
#. Click :guilabel:`+ ADD`
#. Complete the configuration fields:

   :IP Address: The IP address of the BGP neighbor
   :Remote AS: The Autonomous System number of the remote peer
   :Forwarding Address: (optional) The forwarding address for the neighbor
   :Protocol Address: (optional) The protocol address for the neighbor
   :Weight: (optional) The weight value for route preference
   :Keep Alive: (optional) The keepalive interval in seconds (default varies by integration)
   :Hold Down: (optional) The hold-down timer in seconds (typically 3x keepalive)
   :Password: (optional) The MD5 authentication password for the BGP session
   :Route Filtering Type: (optional) The type of route filtering applied (e.g., IP Prefix List)
   :Route Filtering In: (optional) Inbound route filter reference
   :Route Filtering Out: (optional) Outbound route filter reference
   :BFD Enabled: (optional) Enable Bidirectional Forwarding Detection for faster failure detection
   :BFD Interval: (optional) BFD packet transmission interval in milliseconds
   :BFD Multiple: (optional) BFD detection multiplier
   :Allow AS In: (optional) Allow the local AS number in received AS paths
   :Restart Mode: (optional) Graceful restart mode configuration
   :Hop Limit: (optional) Maximum number of hops to the BGP peer (for eBGP multihop)

   .. NOTE:: Additional fields may appear based on the router type and its configured option types.

#. Click :guilabel:`SAVE`

Editing a BGP Neighbor
^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Routers``
#. Click on the target router to access the detail view
#. Click the **BGP** tab
#. Click the pencil (edit) icon for the target BGP neighbor
#. Modify the desired fields
#. Click :guilabel:`SAVE`

Deleting a BGP Neighbor
^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Routers``
#. Click on the target router to access the detail view
#. Click the **BGP** tab
#. Click the delete icon for the target BGP neighbor
#. Confirm the deletion when prompted

.. WARNING:: Removing a BGP neighbor will terminate the BGP session with that peer. This will cause any routes learned from that neighbor to be withdrawn, potentially affecting network connectivity.

BGP Neighbor States
^^^^^^^^^^^^^^^^^^^

BGP neighbors progress through the following states:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - State
     - Description
   * - Idle
     - Initial state; no BGP resources allocated
   * - Connect
     - Waiting for TCP connection to complete
   * - Active
     - Attempting to initiate a TCP connection
   * - OpenSent
     - TCP connection established; OPEN message sent
   * - OpenConfirm
     - OPEN message received and accepted
   * - Established
     - BGP session fully operational; routes being exchanged

Required Role Permissions
^^^^^^^^^^^^^^^^^^^^^^^^^

Access to BGP neighbor management requires the ``Infrastructure: Network Routers`` permission (``infrastructure-routers``) with ``read``, ``full``, or ``group`` access.

API
^^^

BGP neighbors are managed through the |morpheus| API at the following endpoints:

- ``GET /api/networks/routers/:routerId/bgp-neighbors`` — List BGP neighbors
- ``GET /api/networks/routers/:routerId/bgp-neighbors/:id`` — Get a specific BGP neighbor
- ``POST /api/networks/routers/:routerId/bgp-neighbors`` — Create a BGP neighbor
- ``PUT /api/networks/routers/:routerId/bgp-neighbors/:id`` — Update a BGP neighbor
- ``DELETE /api/networks/routers/:routerId/bgp-neighbors/:id`` — Delete a BGP neighbor
