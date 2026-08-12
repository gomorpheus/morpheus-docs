MySQL requirements for Morpheus HA 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The requirements are as follows:

   - An external MySQL service. The 8.4 LTS family can be configured; confirm the formally certified version and service variant for the installed |morpheus| release.
   - MySQL cluster with at least 3 nodes for redundancy.
   - Morpheus application nodes have connectivity to MySQL cluster.

.. note:: Morpheus does not create primary keys on all tables. If you use a clustering technology that requires primary keys, you will need to leverage the invisible primary key option in MySQL 8
