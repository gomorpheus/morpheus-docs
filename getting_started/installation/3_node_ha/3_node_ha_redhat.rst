3-Node HA Install example
---------------------------------

Distributed App Nodes with Externalized MySQL Database

The most common and recommended HA Morpheus deployment consists of three app nodes using embedded services and an external MySQL DB cluster (minimum of 3 nodes). 

.. IMPORTANT:: HA environments installed without engagement from Morpheus are not eligible for support. The provided configuration serves as a sample only and requirements may vary. Please reach out to your account manager to discuss deploying a HA environment to meet requirements for support.

.. include:: 3_node_ha_assumptions.rst

.. include:: 3_node_ha_paths.rst

.. include:: 3_node_ha_database_requirements.rst

.. include:: /getting_started/installation/database_configure_generic.rst

.. include:: 3_node_ha_app_node.rst

.. include:: 3_node_ha_rabbit.rst

.. include:: 3_node_ha_elastic.rst

.. include:: 3_node_ha_lb.rst 