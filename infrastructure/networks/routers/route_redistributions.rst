.. _route_redistributions:

Route Redistribution
--------------------

``Infrastructure > Network > Routers > (select Router) > Route Redistribution``

Overview
^^^^^^^^

Route redistribution allows routes learned through one routing protocol to be advertised via another. This is essential in environments that run multiple routing protocols (e.g., redistributing static routes or OSPF routes into BGP). |morpheus| supports managing route redistribution configurations on router types that expose this capability.

.. NOTE:: The Route Redistribution tab is available on router types that support redistribution (``hasRouteRedistribution`` flag). NSX Edge Gateways are the primary router type with route redistribution support in |morpheus|.

Viewing Route Redistributions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Routers``
#. Click on the target router to access the detail view
#. Click the **Route Redistribution** tab
#. The list view displays configured redistribution rules with their source protocol, destination, and status

Adding a Route Redistribution Rule
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Routers``
#. Click on the target router to access the detail view
#. Click the **Route Redistribution** tab
#. Click :guilabel:`+ ADD`
#. Complete the configuration fields (fields vary by router type):

   .. NOTE:: The available fields depend on the router type's ``routeRedistributionOptionTypes``. Common fields include source protocol, route map, and metric settings.

#. Click :guilabel:`SAVE`

Editing a Route Redistribution Rule
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Routers``
#. Click on the target router to access the detail view
#. Click the **Route Redistribution** tab
#. Click the pencil (edit) icon for the target redistribution rule
#. Modify the desired fields
#. Click :guilabel:`SAVE`

Deleting a Route Redistribution Rule
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Routers``
#. Click on the target router to access the detail view
#. Click the **Route Redistribution** tab
#. Click the delete icon for the target redistribution rule
#. Confirm the deletion when prompted

.. WARNING:: Removing a route redistribution rule will stop the advertisement of those routes into the target protocol. This may cause reachability issues for networks that depend on the redistributed routes.

Common Redistribution Scenarios
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Scenario
     - Description
   * - Static to BGP
     - Advertise statically configured routes to BGP peers
   * - Connected to OSPF
     - Advertise directly connected networks into OSPF
   * - OSPF to BGP
     - Advertise OSPF-learned routes to external BGP peers
   * - Static to OSPF
     - Include static routes in OSPF link-state advertisements

Required Role Permissions
^^^^^^^^^^^^^^^^^^^^^^^^^

Access to route redistribution management requires the ``Infrastructure: Network Router Redistribution`` permission (``infrastructure-network-router-redistribution``) with ``read`` or ``full`` access.
