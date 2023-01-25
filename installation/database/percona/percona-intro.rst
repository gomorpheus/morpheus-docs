Out of the box |morpheus| uses MySQL but |morpheus| supports any mySQL-compliant database. There are many ways to set up a highly available, MySQL dialect-based database. One which has found favor with many of our customers is Percona's XtraDB Cluster.  Percona's product is based off of Galera's WSREP Clustering, which is also supported.

.. important:: Currently, you must use a v5.7-compatible version of MySQL/Percona. Complete compatibility information is available in the `Compatibility and Breaking Changes <https://docs.morpheusdata.com/en/latest/release_notes/compatibility.html>`_ page. Additional configuration for Percona Clusters with TLS enabled is required. Refer to :ref:`Percona TLS` Configuration in our full HA docs for details.

.. IMPORTANT:: This is a sample configuration only. Customer configurations and requirements will vary.

Additional information can be found below:

`XtraDB 5.7 Installation <https://www.percona.com/doc/percona-xtradb-cluster/5.7/install/yum.html>`_