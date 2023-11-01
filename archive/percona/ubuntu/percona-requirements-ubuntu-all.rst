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

   .. note:: At the time of this writing, Ubuntu 22.04 is not supported

Percona requires the following TCP ports for the cluster nodes. Please create the appropriate firewall rules on your
Percona nodes.

  - 3306
  - 4444
  - 4567
  - 4568

  .. code-block:: bash

    [root]# ufw allow 3306,4444,4567,4568/tcp
   
Configure AppArmor
``````````````````

Percona recommends completely removing AppArmor, in case a previous AppArmor profile exists.  See the XtraDB documentation at the top of the page for more information.
  
  .. code-block:: bash

    [root]# apt remove apparmor -y

**(Optional)** If AppArmor is required by the organization, profiles can be added to ensure interference is eliminated.  To allow Percona XtraDB Cluster functionality when AppArmor is installed, follow the documentation here:

   `Enabing AppArmor <https://docs.percona.com/percona-xtradb-cluster/8.0/security/apparmor.html#apparmor>`_

