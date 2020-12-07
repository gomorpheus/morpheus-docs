Single Node Appliance Upgrade
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following covers upgrading single node (All-In-One) Appliance configurations.

.. important:: Only appliances running Morpheus v4.2.0 or higher can upgrade to 4.x. Always backup your database before running any upgrade.

4.2.0 to |morphver| Upgrade
```````````````````````````

Debian / Ubuntu
...............

To upgrade Morpheus running on Ubuntu/Debian, download new deb package, stop the morpheus-ui, install the new deb package, then reconfigure.

.. code-block:: bash

  sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.deb
  sudo morpheus-ctl stop morpheus-ui
  sudo dpkg -i morpheus-appliance_x.x.x-1_amd64.deb
  sudo morpheus-ctl reconfigure

.. note:: Services will be stopped during package installation and started during the reconfigure process, including the |morpheus|-ui service.

All services will automatically start during the reconfigure process. After the reconfigure has succeeded, tail the ui service to watch ui startup logs with ``morpheus-ctl tail morpheus-ui``.

After the morpheus-ui service finishes loading, the upgrade is complete.

|

CentOS / RHEL
.............

To upgrade Morpheus running on CentOS/RHEL, download and install the new rpm package, stop the morpheus-ui, reconfigure and then start the morpheus-ui:

.. code-block:: bash

  sudo wget https://packageUrl.morpheus-appliance-x.x.x-x.x86_64.rpm
  sudo morpheus-ctl stop morpheus-ui
  sudo rpm -Uhv morpheus-appliance-x.x.x-x.x86_64.rpm
  sudo morpheus-ctl reconfigure

.. note:: Services will be stopped during package installation and started during the reconfigure process, including the |morpheus|-ui service.

All services will automatically start during the reconfigure process. After the reconfigure has succeeded, tail the ui service to watch ui startup logs with ``morpheus-ctl tail morpheus-ui``.

After the morpheus-ui service finishes loading, the upgrade is complete.

|
|
