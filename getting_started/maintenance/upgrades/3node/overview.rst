3-Node HA Upgrade
^^^^^^^^^^^^^^^^^

3-Node HA Appliance represent 3 App nodes with local RabbitMQ and Elasticsearch services clustered across the app nodes, and an external Galera/Percona MySQL cluster.

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
