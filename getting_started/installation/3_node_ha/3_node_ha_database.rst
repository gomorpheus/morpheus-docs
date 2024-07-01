MySQL requirements for Morpheus HA 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   - MySQL version v8.0 (minimum of v8.0.32 is recommended due to MySQL bugs)
   - MySQL cluster configuration with at least 3 nodes for redundancy.
   - Morpheus application nodes must be able to connect to MySQL for database operations.

.. IMPORTANT:: Morpheus does not create primary keys on all tables. If you use a clustering technology that requires primary keys, you will need to leverage the invisible primary key option in MySQL 8