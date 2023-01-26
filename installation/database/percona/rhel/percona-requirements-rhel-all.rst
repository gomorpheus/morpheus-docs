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
   
Configure SElinux
`````````````````

The `Percona Documentation <https://docs.percona.com/percona-xtradb-cluster/5.7/install/yum.html>`_ recommends setting SELinux from ``enforcing`` to ``permissive`` to eliminate interference.  Run the following to set SELinux to permissive on each database node:
  
  .. code-block:: bash

    [root]# setenforce 0
    [root]# sed -i 's/SELINUX=enforcing/SELINUX=permissive/g' /etc/selinux/config

**(Optional)** If enforcing is required by the organization, SELinux rules can be added to ensure interference is eliminated.  To allow Percona XtraDB Cluster functionality when SELinux is ``Enforcing``, run the following on each database Node:

#. Install SELinux utilities

   .. code-block:: bash

    [root]# yum install -y policycoreutils-python.x86_64

#. Configure Percona ports for SELinux:

   .. code-block:: bash

    [root]# semanage port -m -t mysqld_port_t -p tcp 4444
    [root]# semanage port -m -t mysqld_port_t -p tcp 4567
    [root]# semanage port -a -t mysqld_port_t -p tcp 4568

#. Create the policy file PXC.te

   .. code-block:: bash

    [root]# vi PXC.te
    module PXC 1.0;
    require {
            type unconfined_t;
            type mysqld_t;
            type unconfined_service_t;
            type tmp_t;
            type sysctl_net_t;
            type kernel_t;
            type mysqld_safe_t;
            class process { getattr setpgid };
            class unix_stream_socket connectto;
            class system module_request;
            class file { getattr open read write };
            class dir search;
      }

      #============= mysqld_t ==============

     allow mysqld_t kernel_t:system module_request;
     allow mysqld_t self:process { getattr setpgid };
     allow mysqld_t self:unix_stream_socket connectto;
     allow mysqld_t sysctl_net_t:dir search;
     allow mysqld_t sysctl_net_t:file { getattr open read };
     allow mysqld_t tmp_t:file write;

#. Compile and load the SELinux policy

   .. code-block:: bash

    [root]# checkmodule -M -m -o PXC.mod PXC.te
    [root]# semodule_package -o PXC.pp -m PXC.mod
    [root]# semodule -i PXC.pp