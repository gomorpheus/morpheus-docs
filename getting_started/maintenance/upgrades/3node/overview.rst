3-Node HA Upgrade
^^^^^^^^^^^^^^^^^

3-Node HA Appliance represent 3 App nodes with local RabbitMQ and Elasticsearch services clustered across the app nodes, and an external Galera/Percona MySQL cluster.

|morpheus| Packages
```````````````````
|morpheus| Release Package urls can be obtained from `https://morpheushub.com <https://morpheushub.com>`_ 

Refer to :ref:`compatibility` for any 3-node variations using externalized MySQL, Elasticsearch and/or RabbitMQ version requirements.


4.2.x -> |morphver| upgrade 
...........................

Due to Database schema changes in |morphver| it is important to stop the morpheus-ui service on all app nodes prior to upgrade. Failure to do so may result in errors or database corruption.

Upgrade Instructions
````````````````````

.. toctree::
   :maxdepth: 3

   deb.rst
   rpm.rst
