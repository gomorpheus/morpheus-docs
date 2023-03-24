.. _3nodeinstall-rhel8-secure:

(Secure-WIP) 3-Node HA Install (RHEL/CentOS 8)
----------------------------------------------

Distributed App Nodes with Externalized DB

.. error::
    At the time of this writing, RabbitMQ TLS is not a configurable item in |morpheus|, there are not customizable
    settings that allow the configuration to persist with the embedded service.  In this case, RabbitMQ must be installed
    manually, following the steps in the ``RabbitMQ Cluster`` section, as well as the ``Optional TLS`` configuration in it.
    |morpheus| will not install RabbitMQ automatically and will not maintain it, it will be up to the customer to
    maintain/upgrade the service if needed.

.. include:: /installation/app/3-node-ha/assumptions.rst

.. include:: /installation/app/default-locations.rst

.. include:: /installation/database/percona/perconaTls-rhel8.rst

.. include:: /installation/messaging/rhel8.rst

.. include:: /installation/app/3-node-ha/app-node-installation-rhel-secure.rst

.. .. include:: /installation/app/3-node-ha/clustering-rabbitmq.rst

.. include:: /installation/storage/HA_Shared_Storage.rst

.. include:: /installation/app/database-migration.rst

.. include:: /installation/app/recovery.rst