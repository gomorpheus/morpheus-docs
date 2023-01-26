Requirements
````````````

**Storage Requirements**

   30 GB storage minimum for each database node. This should be monitored and increased if the |morpheus| database requires more space.

   After database installation ensure that the minimum storage requirement is available for the mysql tmpdir. By default mysql will write temporary files in "/tmp". 
   The mysql tmpdir configuration can be modified using the following steps for each database node:

   #.  Create the new directory.

      .. code-block:: bash

       mkdir /path/to/mysql/tmp/directory
       chown -R mysql:mysql /path/to/mysql/tmp/directory

   #. Edit /etc/my.cnf.

      .. code-block:: bash

       [mysqld]
       tmpdir=/path/to/mysql/tmp/directory


   .. important:: Failing to provide sufficient storage to the mysql tmpdir can result in failed database migrations and |morpheus| upgrades.

Current Operating System (OS) support can be found here:

`XtraDB 5.7 Support <https://www.percona.com/services/policies/percona-software-support-lifecycle#mysql>`_

Percona requires the following TCP ports for the cluster nodes. Please create the appropriate firewall rules on your
Percona nodes.

  - 3306
  - 4444
  - 4567
  - 4568

  .. code-block:: bash

    [root]# firewall-cmd --zone=public --add-port={3306/tcp,4444/tcp,4567/tcp,4568/tcp} --permanent
    [root]# firewall-cmd --reload
