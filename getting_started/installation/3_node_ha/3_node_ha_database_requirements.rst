MySQL requirements for Morpheus HA 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The requirements are as follows:

   - MySQL version v8.0.x (minimum of v8.0.32)
   - MySQL cluster with at least 3 nodes for redundancy.
   - Morpheus application nodes have connectivity to MySQL cluster.

.. IMPORTANT:: Morpheus does not create primary keys on all tables. If you use a clustering technology that requires primary keys, you will need to leverage the invisible primary key option in MySQL 8