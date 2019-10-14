Upgrading
=========

4.x Upgrade Requirements
------------------------

* Only appliances running Morpheus v3.6.0 or higher can upgrade to 4.x.
* MySQL will be upgraded to 5.7.x on Appliances with MySQL running on the app node (Single Node or "all-in-one" Appliances). Backup your database before running the upgrade.

   .. important:: BACKUP YOUR DATABASE before the upgrade. You can use the appliance backup job in Morpheus, but make sure you download it before you do the upgrade.

* RabbitMQ will be upgrade from 3.4.x to 3.7.x. On 3-Node configurations, the RabbitMQ queues and configuration will be dropped and the cluster will need to be configured and established again.
* Stop all morpheus services, not just the morpheus-ui, before the upgrade. Although the upgrade process will also stop the services, take this step to ensure they are stopped.
* Warnings about missing files during the removal phase are expected and can be ignored.
5. The repo download location has changed to https://downloads.morpheusdata.com from https://downloads.gomorpheus.com so if a customer has an ACL on their firewall or proxy they will need to update the ACL.

When externalizing MySQL, Elasticsearch and/or RabbitMQ services, the following versions are compatible with Morpheus 4.1.0:

+---------------------------------------+----------------------+-----------------------------+
| **Service**                           |**Compatible Branch** | **4.1.0 Installed Version** |
+---------------------------------------+----------------------+-----------------------------+
| MySQL                                 | 5.7                  | 5.7.27                      |
+---------------------------------------+----------------------+-----------------------------+
| Elasticsearch: 5.6 (5.6.16 installed) | 5.6                  | 5.6.16                      |
+---------------------------------------+----------------------+-----------------------------+
| RabbitMQ: 3.7 (3.7.16 installed)      | 3.7                  | 3.7.16                      |
+---------------------------------------+----------------------+-----------------------------+

Single Node Appliance Upgrade
-----------------------------

When upgrading from 3.6.x to 4.0.0 or 4.1.0, the following services will be upgraded on Single Node (all-in-one) Appliances:

- MySQL upgrade to v5.7
- RabbitMQ upgrade to v3.7
- Elasticsearch upgrade to v5.6

Debian / Ubuntu
^^^^^^^^^^^^^^^

To upgrade Morpheus running on Ubuntu/Debian, download and install the new deb package, stop the morpheus-ui, reconfigure and start the morpheus-ui:

.. code-block:: bash

  sudo wget https://packageUrl.morpheus-appliance_x.x.x-x.amd64.deb
  sudo dpkg -i morpheus-appliance_x.x.x-1.amd64.deb
  sudo morpheus-ctl stop
  sudo morpheus-ctl reconfigure
  sudo morpheus-ctl start morpheus-ui

CentOS / RHEL
^^^^^^^^^^^^^

To upgrade Morpheus running on CentOS/RHEL, download and install the new rpm package, stop the morpheus-ui, reconfigure and then start the morpheus-ui:

.. code-block:: bash

  sudo wget https://packageUrl.morpheus-appliance-x.x.x-x.x86_64.rpm
  sudo rpm -Uhv morpheus-appliance-x.x.x-x.x86_64.rpm
  sudo morpheus-ctl stop
  sudo morpheus-ctl reconfigure
  sudo morpheus-ctl start morpheus-ui

3-Node Appliance Upgrade
------------------------

When upgrading a 3-Node appliance from 3.6.x to 4.0.0 or 4.1.0, the following services will be upgraded:

- RabbitMQ upgrade to v3.7
- Elasticsearch upgrade to v5.6

The upgrade process will not upgrade the external MySQL node(s). MySQL v5.7 is required for external databases.

Due to RabbitMQ going from 3.4.x to 3.7.x, which has no direct upgrade path, the RabbitMQ queues and configuration will be dropped, and the cluster will need to be configured and established again. This also ensures new queues are created using our new declaration settings, and removes any old queues not in use anymore.

.. important:: Due to the RabbitMQ upgrade from 3.4.x to 3.7.x, the RabbitMQ queues and configuration will be dropped and the cluster will need to be configured and established again.

1. Stop all Morpheus services via ``morpheus-ctl stop`` on all Nodes
2. Upgrade Node 1, then run a reconfigure on Node 1
3. Upgrade Node 2, then run a reconfigure on Node 2
4. Upgrade Node 3, then run a reconfigure on Node 3
5. Establish the RabbitMQ cluster again using the steps from the 3 Node install guide.
6. Start all services

Other Appliance Configurations Upgrades
---------------------------------------

When upgrading other Appliance Configurations from 3.6.x to 4.0.0 or 4.1.0, only services local to the Morpheus App node(s) will be upgraded. For fully distributed configurations, where MySQL, RabbitMQ and Elasticsearch are external, the upgrade process will not upgrade the external serviced.

When externalizing MySQL, Elasticsearch and/or RabbitMQ services, the following versions are compatible with Morpheus 4.1.0:

+---------------------------------------+----------------------+-----------------------------+
| **Service**                           |**Compatible Branch** | **4.1.0 Installed Version** |
+---------------------------------------+----------------------+-----------------------------+
| MySQL                                 | 5.7                  | 5.7.27                      |
+---------------------------------------+----------------------+-----------------------------+
| Elasticsearch: 5.6 (5.6.16 installed) | 5.6                  | 5.6.16                      |
+---------------------------------------+----------------------+-----------------------------+
| RabbitMQ: 3.7 (3.7.16 installed)      | 3.7                  | 3.7.16                      |
+---------------------------------------+----------------------+-----------------------------+


Fix if Install Hangs
--------------------

Some very old all-in-one appliances may hang during the mysql upgrade process during the 4.0.0 deb or rpm package upgrade.

To resolve, run the following in a separate session while the process is hanging:

#. Create a file ``vi mysqlfix``
#. paste the following:

   .. code-block:: bash

          export PATH=/opt/morpheus/sbin:/opt/morpheus/sbin:/opt/morpheus/embedded/sbin:/opt/morpheus/embedded/bin:$PATH
          MYSQL_ROOT=$(grep root /etc/morpheus/morpheus-secrets.json | awk '{print substr($2,2,length($2)-3)}')
          if [[ -z $MYSQL_ROOT ]]; then
            echo "Failed to lookup the MySQL root password, please enter it when prompted."
          else
            /opt/morpheus/embedded/bin/mysqld_safe --defaults-file=/opt/morpheus/embedded/mysql/my.cnf \
              --log-error=/var/log/morpheus/mysql/mysql_error.log --pid-file=/var/run/morpheus/mysqld/mysqld.pid &
            until [[ -S /var/run/morpheus/mysqld/mysqld.sock ]]; do
              sleep 1
            done
            /opt/morpheus/embedded/bin/mysql_upgrade --defaults-extra-file=/opt/morpheus/embedded/mysql/my.cnf -u root -p${MYSQL_ROOT}
            /opt/morpheus/embedded/bin/mysqladmin --defaults-extra-file=/opt/morpheus/embedded/mysql/my.cnf -u root -p${MYSQL_ROOT} shutdown
            touch /var/opt/morpheus/mysql/.mysql57_table_upgrade_done
          fi

#. Run ``./mysqlfix``

The upgrade will then proceed.


.. include:: ssl-import.rst
.. include:: wars.rst
