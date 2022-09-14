3-Node HA Upgrade
^^^^^^^^^^^^^^^^^

.. important::

   Known issue with embedded Elasticsearch upgrade: When upgrading to v5.4.8, v5.4.9 or v5.5.1, there is a potential issue with embedded Elasticsearch clustering on rolling upgrades and existing data migration for all embedded Elasticsearch architechtures. Refer to the :ref:`Release Notes` for additional informaiton.

3-Node HA Appliances represent 3 App nodes with local RabbitMQ and Elasticsearch services clustered across the app nodes, and an external Galera/Percona MySQL cluster.

|morpheus| Packages
```````````````````
|morpheus| Release Package urls can be obtained from `https://morpheushub.com <https://morpheushub.com>`_

Refer to :ref:`compatibility` for any 3-node variations using externalized MySQL, Elasticsearch and/or RabbitMQ version requirements.

Upgrade Instructions
````````````````````

.. toctree::
   :maxdepth: 3

   deb.rst
   rpm.rst

.. WARNING:: Upgrades can add additional storage load on database nodes. Please refer to database storage requirements within :ref:`3nodeinstall` before upgrading.
