Single Node Install on RHEL
^^^^^^^^^^^^^^^^^^^^^^^^^^^

RHEL 7 Installation
```````````````````

To get started installing |morpheus| on RedHat, a few prerequisite items are required.

#. Configure ``firewalld`` to allow access from users on port 443 (Or remove the firewall if not required)
#. Make sure the machine is self resolvable to its own hostname
#. For RHEL 7.x, the optional RPMs repository must be added for the reconfigure to succeed at the end. This is not a requirement for installing on RHEL 8.x, as the optional RPMs repo is now part of the appstream repo that is enabled by default in RHEL 8.x. Consult the RHEL 8.x installation instructions in the next section if needed

   *  **RHEL 7.x Amazon:** ``yum-config-manager --enable rhel-7-server-rhui-optional-rpms``
   *  **RHEL 7.x:** ``yum-config-manager --enable rhel-7-server-optional-rpms``

.. NOTE:: For Amazon users, a Redhat subscription is not required if the appropriate yum REGION repository is added instead as demonstrated above.

Register and Activate the Redhat Server
.......................................

The RedHat Enterprise Linux server needs to be registered and activated with Redhat subscription. The server optional RPMs repo needs to be enabled as well. To check if the server has been activated, run ``subscription-manager version``. Subscription manager will return the version plus the python dependency version.

If the server has not been registered and activated, the ``subscription-manager version`` command will return the message below:

.. code-block:: bash

   sudo subscription-manager version
   server type: This system is currently not registered
   subscription management server: 0.9.51.24.-1
   subscription-manager: 1.10.14-7.el7 python-rhsm: 1.10.12-2.el7

When a server has been registered and activated with Redhat, the subscription manager will return the following message:

.. code-block:: bash

  sudo subscription-manager version
  server type: Red Hat Subscription Management
  subscription management server: 0.9.51.24-1
  subscription-manager: 1.10.14-7.el7 python-rhsm: 1.10.12-2.el7

If the subscription manager returns the message ``This system is currently not registered`` please follow the below steps to register the server.

.. TIP:: To register the server you will need to have ``sudo`` permissions [Member of the Wheel group] or root access to the server. You will also need your Redhat registered email address and password.

To register the server, run ``subscription-manager register``, you should see a return similar to what is shown below:

.. code-block:: bash

  sudo subscription-manager register
  Username: redhat@example.com
  Password: . subscription-manager auto --attach

.. NOTE:: This process can take a minute to complete.

Next, attach a subscription to the system with ``subscription-manager attach --auto`` as shown below:

.. code-block:: bash

  sudo subscription-manager attach --auto

  Installed Product Current Status: Product Name: Red Hat Enterprise Linux
  Server Status: Subscribed

Confirm Optional Repos are Enabled
..................................

To check to see if the RHEL server has the Red Hat Enterprise Linux 7 Server - Optional (RPMs) repo enabled, please run the following command to return the repo status:

.. TIP:: To check the server repos you will need to have sudo permissions (Member of the Wheel group) or root access to the server.

.. code-block:: bash

  sudo yum repolist all | grep "rhel-7-server-optional-rpms" rhel-7-server-optional-rpms/7Server/x86_64 disabled

If the repo status was returned as disabled, you will need to enable the repo using the subscription manager like below:

.. code-block:: bash

  sudo subscription-manager repos --enable rhel-7-server-optional-rpms
  Repository 'rhel-7-server-optional-rpms' is enabled for this system.

The message ``Repo 'rhel-7-server-optional-rpms' is enabled for this system.`` will appear after enabling the repo. This will confirm that the repo has been enabled.

Download and Install the |morpheus| Package
...........................................

Next simply download the relevant ``.rpm`` package for installation. This package can be acquired from morphueshub.com.

.. code-block:: bash

  sudo wget https://downloads.morpheusdata.com/path/to/package.rpm

.. NOTE:: The example command above contains an example download URL. The actual URL for your specific platform and |morpheus| version can be found at morpheushub.com.

Next, we must install the package onto the machine and configure the morpheus services:

.. code-block:: bash

  sudo rpm -i morpheus-appliance_x.x.x-1_amd64.rpm
  sudo morpheus-ctl reconfigure

Once the installation is complete, the web interface will automatically start up. By default it will be resolvable at ``https://your_machine_name`` and in many cases this may not be resolvable from your browser. The URL can be changed by editing ``/etc/morpheus/morpheus.rb`` and changing the value of ``appliance_url``. After this has been changed, simply run:

.. code-block:: bash

  sudo morpheus-ctl reconfigure
  sudo morpheus-ctl stop morpheus-ui
  sudo morpheus-ctl start morpheus-ui

.. NOTE:: The ``morpheus-ui`` can take 2-3 minutes to startup before it becomes available.

There are additional install settings that can be viewed in the :ref:`additional_options` section.

Once the browser is pointed to the appliance for first time, a setup wizard will be presented. Please follow the on screen instructions by creating the master account. From there you will be presented with the license settings page where a license can be applied for use (if a license is required you may request one or purchase one by contacting your sales representative).

More details on setting up infrastructure can be found throughout this guide.

.. TIP:: If any issues occur it may be prudent to check the morpheus log for details at ``/var/log/morpheus/morpheus-ui/current``.

RHEL 8 Installation
```````````````````

To get started installing |morpheus| on RedHat, a few prerequisite items are required.

#. Configure ``firewalld`` to allow access from users on port 443 (Or remove the firewall if not required)
#. Make sure the machine is self resolvable to its own hostname

Register and Activate the Redhat Server
.......................................

The RedHat Enterprise Linux server needs to be registered and activated with Redhat subscription. The server optional RPMs repo needs to be enabled as well. To check if the server has been activated, run ``subscription-manager version``. Subscription manager will return the version plus the python dependency version.

If the server has not been registered and activated, the ``subscription-manager version`` command will return the message below:

.. code-block:: bash

   sudo subscription-manager version
   server type: This system is currently not registered
   subscription management server: 0.9.51.24.-1
   subscription-manager: 1.10.14-7.el7 python-rhsm: 1.10.12-2.el7

When a server has been registered and activated with Redhat, the subscription manager will return the following message:

.. code-block:: bash

  sudo subscription-manager version
  server type: Red Hat Subscription Management
  subscription management server: 0.9.51.24-1
  subscription-manager: 1.10.14-7.el7 python-rhsm: 1.10.12-2.el7

If the subscription manager returns the message ``This system is currently not registered`` please follow the below steps to register the server.

.. TIP:: To register the server you will need to have ``sudo`` permissions [Member of the Wheel group] or root access to the server. You will also need your Redhat registered email address and password.

To register the server, run ``subscription-manager register``, you should see a return similar to what is shown below:

.. code-block:: bash

  sudo subscription-manager register
  Username: redhat@example.com
  Password: . subscription-manager auto --attach

.. NOTE:: This process can take a minute to complete.

Next, attach a subscription to the system with ``subscription-manager attach --auto`` as shown below:

.. code-block:: bash

  sudo subscription-manager attach --auto

  Installed Product Current Status: Product Name: Red Hat Enterprise Linux
  Server Status: Subscribed

Download and Install the |morpheus| Package
...........................................

Next simply download the relevant ``.rpm`` package for installation. This package can be acquired from morphueshub.com.

.. code-block:: bash

  sudo wget https://downloads.morpheusdata.com/path/to/package.rpm

.. NOTE:: The example command above contains an example download URL. The actual URL for your specific platform and |morpheus| version can be found at morpheushub.com.

Next, we must install the package onto the machine and configure the morpheus services:

.. code-block:: bash

  sudo rpm -i morpheus-appliance_x.x.x-1_amd64.rpm
  sudo morpheus-ctl reconfigure

Once the installation is complete, the web interface will automatically start up. By default it will be resolvable at ``https://your_machine_name`` and in many cases this may not be resolvable from your browser. The URL can be changed by editing ``/etc/morpheus/morpheus.rb`` and changing the value of ``appliance_url``. After this has been changed, simply run:

.. code-block:: bash

  sudo morpheus-ctl reconfigure
  sudo morpheus-ctl stop morpheus-ui
  sudo morpheus-ctl start morpheus-ui

.. NOTE:: The ``morpheus-ui`` can take 2-3 minutes to startup before it becomes available.

There are additional install settings that can be viewed in the :ref:`additional_options` section.

Once the browser is pointed to the appliance for first time, a setup wizard will be presented. Please follow the on screen instructions by creating the master account. From there you will be presented with the license settings page where a license can be applied for use (if a license is required you may request one or purchase one by contacting your sales representative).

More details on setting up infrastructure can be found throughout this guide.

.. TIP:: If any issues occur it may be prudent to check the morpheus log for details at ``/var/log/morpheus/morpheus-ui/current``.
