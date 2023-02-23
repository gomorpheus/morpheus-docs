Distributed Workers
-------------------

Overview
^^^^^^^^

The |morpheus| distributed worker is installed using the same package as the VDI Gateway worker. Organizations which have already deployed VDI Gateway(s) can use the same worker for both purposes if desired, you'd simply need to update configuration in ``/etc/morpheus/morpheus-worker.rb`` and run a reconfigure. When creating a distributed worker or VDI Gateway object in |morpheus| UI, an API key is generated. Adding one or both types of API keys to the worker configuration file determines if the worker is running in VDI gateway and/or distributed worker mode.

**Supported Cloud Types**

The following Cloud/Zone types support Distributed Workers

- vmware
- vmwareCloudAws
- nutanix
- openstack
- xenserver
- macstadium

Installation
^^^^^^^^^^^^

A distributed worker VM is installed and configured similarly to a |morpheus| appliance via ``rpm`` or ``deb`` package.

.. NOTE:: Package URLs for the distributed worker are available at https://morpheushub.com in the downloads section.

.. NOTE:: The distributed worker requires that the |morpheus| appliance has a trusted SSL certificate.  This can be accomplished by configuring a public trusted SSL certificate on the |morpheus| appliance (or load balancer) or ensure the certificate and chain are added to the Java Keystore of the Distributed Worker, to trust the certificate.

**Requirements**

.. list-table:: **Supported Operating Systems**
   :widths: auto
   :header-rows: 1

   * - OS
     - Version(s)
   * - Amazon Linux
     - 2
   * - CentOS
     - 7.x, 8.x
   * - Debian
     - 10, 11
   * - RHEL
     - 7.x, 8.x
   * - SUSE SLES
     - 12
   * - Ubuntu
     - 18.04, 20.04, 22.04

- **Memory:** 4 GB RAM minimum recommended
- **Storage:** 10 GB storage minimum recommended. Storage is required for installation packages and log files
- **CPU:** 4-core minimum recommended
- Network connectivity **to** the |morpheus| appliance over TCP 443 (HTTPS)
- Superuser privileges via the ``sudo`` command for the user installing the |morpheus| worker package
- Access to base ``yum`` or ``apt`` repos. Access to Optional RPM repos may be required for RPM distros

Download the appropriate package from |morpheus| Hub based on your target Linux distribution and version for installation in a directory of your choosing. The package can be removed after successful installation.

.. code-block:: bash

   wget https://downloads.morpheusdata.com/path/to/morpheus-worker-$version.distro

Validate the package checksum as compared with the values indicated on Hub. For example:

.. code-block:: bash

   sha256sum morpheus-worker-$version.distro

Next, install the package using your selected distribution's package installation command and your preferred options. Example, for RPM:

**rpm**:

.. code-block:: bash

   $ sudo rpm -ihv morpheus-worker-$version.$distro

   Preparing...                          ################################# [100%]
   Updating / installing...
      1:morpheus-worker-x.x.x-1.$distro    ################################# [100%]
   Thank you for installing Morpheus Worker!
   Configure and start the Worker by running the following command:

   sudo morpheus-worker-ctl reconfigure

Configuration
^^^^^^^^^^^^^

With the package installed, we need to add a new distributed worker in |morpheus| UI. Distributed workers are added in |AdmIntDis|. To create one, populate the following fields:

- **NAME:** A name for the distributed worker in |morpheus|
- **DESCRIPTION:** An optional description for the distributed worker
- **PROXY HOSTS:** A comma-delimited list of global proxy hosts, any endpoint listed here will be proxied through the |morpheus| worker. For VMware, you must list the host addresses for any vCenter you wish to proxy through the worker. Xen hosts must be listed here as well. Other Cloud types which are supported by the |morpheus| worker need only have the worker configured on the Edit Cloud modal (|InfClo| > Selected Cloud > Edit button)
- **ENABLED:** When marked, the selected worker is available for use

After clicking :guilabel:`SAVE CHANGES`, an API key is generated and displayed. Make note of this as it will be needed in a later configuration step.

.. image:: /images/worker/createWorker.png

With the worker configured in |morpheus|, the next step is to update supported Cloud integrations which should be proxied through the worker. Select the desired Cloud from the Clouds List Page (|InfClo|) and click :guilabel:`EDIT` from the chosen Cloud's Detail Page. Within the Advanced Options section, choose a configured worker from the DISTRIBUTED WORKER dropdown menu. Click :guilabel:`SAVE CHANGES`.

.. image:: /images/worker/updateCloud.png
  :width: 50%

With the API key in hand and configuration complete in |morpheus| UI, head back to the worker box. Configure the gateway by editing ``/etc/morpheus/morpheus-worker.rb`` and updating the following:

   .. code-block:: rb

       worker_url 'https://gateway_worker_url' # This is the wotker URL the Morpheus appliance can resolve and reach on 443
       worker['appliance_url'] = 'https://morpheus_appliance_url' # The resolvable URL or IP address of Morpheus appliance which the worker can reach on port 443
       worker['apikey'] = 'API KEY FOR THIS GATEWAY' # VDI Gateway API Key generated from Morpheus Appliance VDI Pools > VDI Gateways configuraiton. For worker only mode, a value is still required but can be any value, including the 'API KEY FOR THIS GATEWAY' default template value
       worker['worker_key'] = 'DISTRIBUTED WORKER KEY' # Distributed Worker API Key from Administration > Integrations > Distributed Workers configuration

.. NOTE:: By default the worker_url uses the machine's hostname, ie ``https://your_machine_name``. The default ``worker_url`` value can be changed by editing ``/etc/morpheus/morpheus-worker.rb`` and changing the value of ``worker_url``. Additional appliance configuration options are available below.

After all configuration options have been set, run ``sudo morpheus-worker-ctl reconfigure`` to install and configure the worker, nginx and guacd services:

   .. code-block:: bash

     sudo morpheus-worker-ctl reconfigure

The worker reconfigure process will install and configure the worker, nginx and guacd services and dependencies.

.. TIP:: If the reconfigure process fails due to a missing dependency, add the repo that the missing dependency can be found in and run

.. NOTE:: Configuration options can be updated after the initial reconfigure by editing ``/etc/morpheus/morpheus-worker.rb`` and running ``sudo morpheus-worker-ctl reconfigure`` again.

Once the installation is complete the morpheus worker service will automatically start and open a web socket with the specified |morpheus| appliance. To monitor the startup process, run ``morpheus-worker-ctl tail`` to tail the logs of the worker, nginx and guacd services. Individual services can be tailed by specifying the service, for example ``morpheus-worker-ctl tail worker``
