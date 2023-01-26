.. _3nodeinstall-rhel8:

3-Node HA Install (RHEL/CentOS 8)
-------------------------------

Distributed App Nodes with Externalized DB

.. include:: /installation/app/3-node-ha/assumptions.rst

Database Installation
^^^^^^^^^^^^^^^^^^^^^

Assuming a database has not been provided, this document will include steps from the :ref:`Percona TLS RHEL8` documentation, but other technologies can be chosen from the :ref:`database` documentation.

.. `Database Install Guides </installation/database/database.rst>`_

.. .. include::   /getting_started/installation/distributed/full/perconaTls.rst

.. include:: /installation/app/3-node-ha/app-node-installation-rhel.rst

.. include:: /installation/app/3-node-ha/clustering-rabbitmq.rst

.. include:: /installation/load_balancer/ha_load_balancer.rst

.. include:: /installation/storage/HA_Shared_Storage.rst

.. include:: /installation/app/database-migration.rst

.. include:: /installation/app/recovery.rst