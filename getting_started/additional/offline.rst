.. _offline-installation:

Offline Installations and Upgrades
----------------------------------

For customers that have an appliance behind a firewall/proxy that does not allow downloads from our Amazon download site, you can have the offline package to add the needed packages the standard Morpheus installer would have downloaded.

Offline Installation Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- NTP should be correctly configured and the server is able to connect to the NTP server in the ntp.conf file.
- The OS package repositories should be configured to use local LAN repository servers or the server should be able to receive packages from the configured repositories.
- The standard Morpheus and offline packages must be downloaded from another system and transferred to the Morpheus Appliance server.

.. NOTE:: The offline package is linked 1-to-1 to the appliance release. For example the offline package for 4.0.0-1 should be used with the appliance package 4.0.0-1

Offline Install
^^^^^^^^^^^^^^^

Ubuntu/Debian
^^^^^^^^^^^^^

#. Download both the regular Morpheus Appliance package and the Offline Installer packages on to the appliance server:

   .. code-block:: bash

    wget http://example_url/morpheus-appliance_package_url.deb
    wget http://example_url/morpheus-appliance_package_offline_url.deb

#. Install the appliance package. DO NOT run morpheus-ctl reconfigure yet.

   .. code-block:: bash

    sudo dpkg -i morpheus-appliance_version_amd64.deb

#. Install the offline package using ``dpkg -i morpheus-appliance-offline_2.12.2~rc1-1_all.deb``.

   .. code-block:: bash

    sudo dpkg -i morpheus-appliance-offline_version_all.deb

#. Set the Morpheus UI appliance url (if needed, hostname will be automatically set).

   .. code-block:: bash

    sudo vi /etc/morpheus/morpheus.rb
    edit appliance_url to resolvable url (if not configured correctly by default)

#. Reconfigure the appliance to install required packages

   .. code-block:: bash

    sudo morpheus-ctl reconfigure

The Chef run should complete successfully. There is a small pause when Chef runs the resource remote_file[package_name] action create while Chef verifies the checksum. After the reconfigure is complete, the morpheus-ui will start and be up in a few minutes.

.. NOTE:: Tail the morpheus log file located at /var/log/morpheus/morpheus-ui/current with the command ``morpheus-ctl tail morpheus-ui`` and look for the Morpheus ascii logo to know when the morpheus-ui is up.

CentOS/RHEL
^^^^^^^^^^^

#. Download both the regular Morpheus Appliance package and the Offline Installer packages on to the appliance server:

   .. code-block:: bash

    wget http://example_url/morpheus-appliance_package_url.noarch.rpm
    wget http://example_url/morpheus-appliance_package_offline_url.noarch.rpm

#. Install the appliance package. DO NOT run morpheus-ctl reconfigure yet.

   .. code-block:: bash

    sudo rpm -i morpheus-appliance_version_amd64.rpm

#. Install the offline package using ``rpm -i morpheus-appliance-offline_2.12.2~rc1-1_all.rpm``

   .. code-block:: bash

    sudo rpm -i morpheus-appliance-offline_version_all.rpm

#. Set the Morpheus UI appliance url (if needed, hostname will be automatically set). Edit appliance_url to resolvable url (if not configured correctly by default)

   .. code-block:: bash

    sudo vi /etc/morpheus/morpheus.rb

#. Reconfigure the appliance to install required packages

   .. code-block:: bash

    sudo morpheus-ctl reconfigure

The Chef run should complete successfully. There is a small pause when Chef runs the resource remote_file[package_name] action create while Chef verifies the checksum. After the reconfigure is complete, the morpheus-ui will start and be up in a few minutes.

.. NOTE:: Tail the morpheus-ui log file with ``morpheus-ctl tail morpheus-ui`` and look for the Morpheus ascii logo to know when the morpheus-ui is up.
