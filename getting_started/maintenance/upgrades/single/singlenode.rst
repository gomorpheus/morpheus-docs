.. _singleUpgrade:

Single Node/AIO Appliance Upgrades
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. important:: Only appliances running Morpheus |minUpgradeVer| or higher can upgrade to |morphver|. Always backup your database before running any upgrade.

The following covers upgrading Single Node or AIO (All-In-One) Appliance configurations.

Debian / Ubuntu
...............

.. warning:: |morpheus| |morphver| contains new node and VM node packages that require 3.5GB of storage. It is safe to run ``sudo rm -Rf /var/opt/morpheus/package-repos/*`` after |morphver| package installation and before reconfigure to clean old node and vm node packages from the package-repo when room is needed. 

To upgrade Morpheus running on Ubuntu/Debian, download new deb package, stop the morpheus-ui, install the new deb package, then reconfigure.

.. code-block:: bash

  sudo wget https://packageUrl.morpheus-appliance_x.x.x-x_amd64.deb
  sudo morpheus-ctl stop morpheus-ui
  sudo dpkg -i morpheus-appliance_x.x.x-1_amd64.deb
  sudo morpheus-ctl reconfigure

All services will automatically start during the reconfigure process. After the reconfigure has succeeded, tail the ui service to watch ui startup logs with ``morpheus-ctl tail morpheus-ui``.

.. note:: Services will be stopped during package installation and started during the reconfigure process, including the morpheus-ui service. If the reconfigure process is interrupted or fails, the morpheus-ui service may need to be manually started or restarted. In certain situations if another service hangs on starting during reconfigure, run ``systemctl restart morpheus-runsvdir`` then reconfigure and restart ``morpheus-ui`` if successful. 

After the morpheus-ui service finishes loading, the upgrade is complete.

|

CentOS / RHEL / Amazon / SLES
.............................

.. warning:: |morpheus| |morphver| contains new node and VM node packages that require 3.5GB of storage. It is safe to run ``sudo rm -Rf /var/opt/morpheus/package-repos/*`` after |morphver| package installation and before reconfigure to clean old node and vm node packages from the package-repo when room is needed. 

To upgrade Morpheus running on CentOS, RHEL, Amazon or SLES, download and install the new rpm package, stop the morpheus-ui, reconfigure and then start the morpheus-ui:

.. code-block:: bash

  sudo wget https://packageUrl.morpheus-appliance-x.x.x-x.x86_64.rpm
  sudo morpheus-ctl stop morpheus-ui
  sudo rpm -Uhv morpheus-appliance-x.x.x-x.x86_64.rpm
  sudo morpheus-ctl reconfigure

All services will automatically start during the reconfigure process. After the reconfigure has succeeded, tail the ui service to watch ui startup logs with ``morpheus-ctl tail morpheus-ui``.

.. note:: Services will be stopped during package installation and started during the reconfigure process, including the morpheus-ui service. If the reconfigure process is interrupted or fails, the morpheus-ui service may need to be manually started or restarted. In certain situations if another service hangs on starting during reconfigure, run ``systemctl restart morpheus-runsvdir`` then reconfigure and restart ``morpheus-ui`` if successful. 

After the morpheus-ui service finishes loading, the upgrade is complete.

|
|
