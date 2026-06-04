.. _edge_clusters:

Edge Clusters
-------------

``Infrastructure > Network > Integrations > (select Network Server) > Edge Clusters``

Overview
^^^^^^^^

Edge Clusters group edge transport nodes that provide north-south connectivity between logical networks and the physical infrastructure. In NSX-T environments, edge clusters are collections of edge nodes that host network services such as gateway routers, DHCP servers, and load balancers. |morpheus| syncs edge cluster information from supported network integrations and provides viewing and limited management capabilities.

.. NOTE:: The Edge Clusters tab is available on network server integrations that support this feature (``hasEdgeClusters`` flag). VMware NSX-T is the primary integration that exposes edge clusters.

Viewing Edge Clusters
^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select the desired network server integration (e.g., NSX-T)
#. Click the **Edge Clusters** tab
#. The list view displays edge cluster names, member types, associated cluster profiles, and status information

Use the search bar to filter edge clusters by name or other attributes.

Editing an Edge Cluster
^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Network > Integrations``
#. Select the desired network server integration
#. Click the **Edge Clusters** tab
#. Click the pencil (edit) icon for the target edge cluster
#. Modify the available fields:

   :Name: The display name of the edge cluster
   :Description: (optional) A description for the edge cluster

   .. NOTE:: Additional fields may appear based on the network integration type and its configured option types.

#. Click :guilabel:`SAVE`

Permissions
^^^^^^^^^^^

Edge cluster visibility can be managed through the permissions control:

#. Click the lock icon or **Permissions** action for an edge cluster
#. Configure Group Access and Tenant Permissions as needed
#. Click :guilabel:`SAVE`

.. NOTE:: Edge clusters are typically synced from the upstream integration. Creation and deletion of edge clusters is generally managed from the native integration console (e.g., NSX Manager) rather than from |morpheus|.

Required Role Permissions
^^^^^^^^^^^^^^^^^^^^^^^^^

Access to edge cluster management requires the network server scope permission (``infrastructure-network-integration``) with ``read`` or ``full`` access.
