Upgrading
==========

|morpheus| provides a very simple and convenient upgrade process. In
most cases it is simply a matter of installing the new package on top of
itself and reconfiguring the services.

.. IMPORTANT:: All services except the morpheus-ui must be running during a reconfigure. The morpheus-ui also must be restarted or stopped and started during an upgrade. Failure to do so will result in errors.

Debian / Ubuntu
---------------

Simply download the latest package or request the latest package from
your account service representative.

Then run the install process as follows:

.. code-block:: bash

  sudo dpkg -i morpheus-appliance_x.x.x-1.amd64.deb
  sudo morpheus-ctl stop morpheus-ui
  sudo morpheus-ctl reconfigure
  sudo morpheus-ctl start morpheus-ui

This typically is enough to complete a full upgrade. Databases will
automatically be migrated upon restart of the application and service
version upgrades will automatically be applied.

CentOS / RHEL
-------------

Yum based package upgrades are a little different. In this case we want
to run a ``rpm -U`` command as the package manager is slightly
different.

.. code-block:: bash

  sudo rpm -Uhv morpheus-appliance-x.x.x-1.x86_64.rpm
  sudo morpheus-ctl stop morpheus-ui
  sudo morpheus-ctl reconfigure
  sudo morpheus-ctl start morpheus-ui

.. TIP:: Sometimes it may be necessary to restart all appliance services on the host. In order to do this simply type ``sudo morpheus-ctl restart``. This will restart ALL services.

.. IMPORTANT If you are upgrading and have modified the java keystore you will have to do the following steps to import trusted certificates to |morpheus|

.. include ssl-import.rst

Morpheus UI war files
---------------------

Pre-release or patched versions of the |morpheus| UI are sometimes provided. To deploy the ui war on a |morpheus| Appliance:

#. Download the war file to the target appliance

   .. code-block:: bash

    wget https://url/war_file

   .. note:: If the war file is provided via a droplr link, ensure a ``+`` is added to end of droplr url or the file will not download

#. Backup current war file

   .. code-block:: bash

    sudo mv /opt/morpheus/lib/morpheus/morpheus-ui.war /opt/morpheus/lib/morpheus/morpheus-ui.bak.`date +"%m-%d-%Y"`

#. Move and rename new war file

   .. code-block:: bash

    sudo mv <file> /opt/morpheus/lib/morpheus/morpheus-ui.war 

#. Ensure war is owned by ``morpheus-app``

   .. code-block:: bash

    sudo chown morpheus-app.morpheus-app /opt/morpheus/lib/morpheus/morpheus-ui.war

#. Restart the |morpheus| UI

   .. code-block:: bash

    sudo morpheus-ctl restart morpheus-ui

The new ui war will load on startup!
