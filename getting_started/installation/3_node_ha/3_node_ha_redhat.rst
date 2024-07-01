3-Node HA Install example
---------------------------------

Distributed App Nodes with Externalized MySQL Database

The most common and recommended HA Morpheus deployment consists of 3 app nodes using the embedded services and an external MySQL DB cluster (minimum of 3 nodes). 

.. IMPORTANT:: This is a sample configuration only. Customer configurations and requirements will vary. Please contact your account manager if you wish to deploy a HA environment.

.. include:: 3_node_ha_assumptions.rst

.. include:: 3_node_ha_paths.rst

.. include:: 3_node_ha_database.rst

.. include:: /getting_started/installation/database_configure_generic.rst

.. include:: 3_node_ha_app_node.rst

.. include:: 3_node_ha_rabbit.rst

.. include:: 3_node_ha_elastic.rst
