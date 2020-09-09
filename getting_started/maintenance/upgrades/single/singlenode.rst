Single Node Appliance Upgrade
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following covers upgrading single node (All-In-One) Appliance configurations.

.. important:: Only appliances running Morpheus v3.6.0 or higher can upgrade to 4.x.

3.6.x to |morphver| Upgrade
```````````````````````````

When upgrading from 3.6.x to |morphver|, the following services will be automatically upgraded on Single Node (all-in-one) Appliances:

- MySQL will be upgraded to v5.7. Backup your database before running the upgrade.
- Elasticsearch will be upgraded to v7.4
- RabbitMQ will be upgraded to v3.7.

.. important:: BACKUP YOUR DATABASE before the upgrade. You can use the appliance backup job in Morpheus, but make sure you download it before you do the upgrade.

* Stop all morpheus services, not just the morpheus-ui, before the upgrade. Although the upgrade process will also stop the services, take this step to ensure they are stopped.

* Warnings about missing files during the removal phase are expected and can be ignored.

.. important:: The |morpheus| package repo download location has changed to https://downloads.morpheusdata.com from https://downloads.gomorpheus.com. Update firewall and proxy ACLs when applicable.

|

Debian / Ubuntu
...............

To upgrade Morpheus running on Ubuntu/Debian, download the new deb package, stop morpheus services, install the new deb package, then reconfigure:

.. code-block:: bash

  sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.deb
  sudo morpheus-ctl stop
  sudo dpkg -i morpheus-appliance_x.x.x-1_amd64.deb
  sudo morpheus-ctl reconfigure

.. note:: In 4.x services will be stopped during package installation and started during the reconfigure process, including the |morpheus|-ui service.

All services will automatically start during the reconfigure process. After the reconfigure has succeeded, tail the ui service to watch ui startup logs with ``morpheus-ctl tail morpheus-ui``.

After the morpheus-ui service finishes loading, the upgrade is complete.

|

CentOS / RHEL
.............

To upgrade Morpheus running on CentOS/RHEL, download the new rpm package, stop morpheus services, install the new rpm package, then  reconfigure:

.. code-block:: bash

  sudo wget https://packageUrl.morpheus-appliance-x.x.x-x.x86_64.rpm
  sudo morpheus-ctl stop
  sudo rpm -Uhv morpheus-appliance-x.x.x-x.x86_64.rpm
  sudo morpheus-ctl reconfigure

.. note:: In 4.x services will be stopped during package installation and started during the reconfigure process, including the |morpheus|-ui service.

All services will automatically start during the reconfigure process. After the reconfigure has succeeded, tail the ui service to watch ui startup logs with ``morpheus-ctl tail morpheus-ui``.

After the morpheus-ui service finishes loading, the upgrade is complete.

|
|

4.x to |morphver| Upgrade
`````````````````````````

When upgrading from 4.x to |morphver|, the following services will be automatically upgraded on Single Node (all-in-one) Appliances:

- Elasticsearch upgrade to v7.4

|

Debian / Ubuntu
...............

To upgrade Morpheus running on Ubuntu/Debian, download new deb package, stop the morpheus-ui, install the new deb package, then reconfigure.

.. code-block:: bash

  sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.deb
  sudo morpheus-ctl stop
  sudo dpkg -i morpheus-appliance_x.x.x-1_amd64.deb
  sudo morpheus-ctl reconfigure

.. note:: In 4.x services will be stopped during package installation and started during the reconfigure process, including the |morpheus|-ui service.

All services will automatically start during the reconfigure process. After the reconfigure has succeeded, tail the ui service to watch ui startup logs with ``morpheus-ctl tail morpheus-ui``.

After the morpheus-ui service finishes loading, the upgrade is complete.

|

CentOS / RHEL
.............

To upgrade Morpheus running on CentOS/RHEL, download and install the new rpm package, stop the morpheus-ui, reconfigure and then start the morpheus-ui:

.. code-block:: bash

  sudo wget https://packageUrl.morpheus-appliance-x.x.x-x.x86_64.rpm
  sudo morpheus-ctl stop
  sudo rpm -Uhv morpheus-appliance-x.x.x-x.x86_64.rpm
  sudo morpheus-ctl reconfigure

.. note:: In 4.x services will be stopped during package installation and started during the reconfigure process, including the |morpheus|-ui service.

All services will automatically start during the reconfigure process. After the reconfigure has succeeded, tail the ui service to watch ui startup logs with ``morpheus-ctl tail morpheus-ui``.

After the morpheus-ui service finishes loading, the upgrade is complete.

|
|
