Getting started with |morpheus| and VMware
==========================================

.. Introduction
.. ^^^^^^^^^^^^

.. This guide is designed to help you get started and quickly get the most out of |morpheus| with VMWare. By the end, you will integrate your first cloud, configure networking, prepare and consume images, provision instances, and get started with automation. We will briefly discuss installation and account setup but will provide links to additional resources for those very first steps. For the most part, this guide assumes you are able to get |morpheus| installed and are ready to move forward from that point. There is a lot more to see and do in |morpheus| that is beyond the scope of this guide. For more, consult the complete |morpheus| documentation or take part in our user community forum.

.. Installation & Setup
.. ^^^^^^^^^^^^^^^^^^^^

.. In the simplest configuration, |morpheus| needs one appliance server which will contain all the components necessary to orchestrate virtual machines and containers. Full requirements, including storage and networking considerations, can be found in |morpheus| documentation `here <https://docs.morpheusdata.com/en/4.1.0/getting_started/requirements/requirements.html#requirements>`_. In order to provision any new instances, hosts, or applications, (or convert any discovered resources to managed resources) you will need a valid license. If you don't have one, you can request a lab license for free at `|morpheus| Hub <https://www.morpheushub.com>`_. Once obtained, the license can be applied in Administration > Settings > LICENSE.
..

Groups
^^^^^^

Groups in |morpheus| define which resources a user has access to. Clouds are added to Groups and a User can only access Clouds in the Groups to which their Role(s) give them access. More information on |morpheus| groups is at :ref:`Groups`. A deep dive into groups goes beyond the scope of this guide but it's often useful to create a group that contains all clouds for testing purposes. We will create that group now so that we can add our first cloud into this group in the next section.

Navigate to ``Infrastructure > Groups``. Here we will see a list of all configured groups but, of course, this will be empty immediately after installation. Click "+CREATE". Give your group a name, such as "All Clouds". The "CODE" field is used when calling |morpheus| through |morpheus| API or |morpheus| CLI. It's useful in most cases to have an "All Clouds" group for testing purposes so this will likely help you down the road.

Configuring Network for Provisioning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When configuring networking, we can set global defaults by going to `Infrastructure > Network > NETWORKS tab`. Here we can add or configure networks from all clouds integrated into |morpheus|. Depending on the number of clouds |morpheus| has ingested, this list may be quite large and may also be paginated across a large number of pages. In such a case, it may be easier to view or configure networks from the specific cloud detail page so that networks from other clouds are not shown.

.. image:: /images/vCenterGuideImages/Network/1networksSection.png
  :width: 80%
  :alt: The list of configured networks
  :align: center

Still in `Infrastructure > Network`, make note of the "INTEGRATIONS" tab. It's here that we can set up any integrations that may be relevant, such as IPAM integrations. Generally speaking, when adding IPAM integrations, we simply need to name our new integration, give the API URL, and provide credentials. There's more information in the `IPAM integration <https://docs.morpheusdata.com/en/4.1.1/integration_guides/integration_guides.html#networking>`_ section of |morpheus| Docs.

.. image:: /images/vCenterGuideImages/Network/2addIPAM.png
  :width: 80%
  :alt: The add IPAM integration dialog box
  :align: center

In `Infrastructure > Networking` we can also set up IP address pools from the IP Pools tab. These pools can be manually defined, known as a |morpheus|-type IP pool, or they can come from any IPAM integrations you've configured. As instances are provisioned, |morpheus| will assign IP addresses from the pool chosen during provisioning. When the instance is later dissolved, |morpheus| will automatically release the IP address to be used by another instance when needed. When adding or editing a network, we can opt to scope the network to one of these configured IP address pools.

.. image:: /images/vCenterGuideImages/Network/3addIPPool.png
  :width: 80%
  :alt: Creating a |morpheus|-type IP pool
  :align: center

Since this guide is focused on working within a VMware cloud that we integrated at the start, we will take a look at our network configurations on the cloud detail page as well. Navigate to `Infrastructure > Clouds > (your VMware cloud) > NETWORKS tab`. Just as with resource pools and data stores, we have the ability to make certain networks inactive in |morpheus|, or scope them to be usable only for certain groups or tenants.

.. image:: /images/vCenterGuideImages/Network/4cloudNetworks.png
  :width: 80%
  :alt: Viewing networks on the cloud detail page
  :align: center

Prepping an Image
^^^^^^^^^^^^^^^^^

As we'll discuss and try out in the next section, |morpheus| comes out of the box with a default set of blueprints that are relevant to many modern deployment scenarios. For the most part, these are base operating system images with a few additional adjustments. However, in many on-premise deployments, there are often custom image and networking requirements. We will work with images included in |morpheus| by default in this guide but it's important to discuss how to prep custom images as well.

**Creating a Windows Image**

The following versions of Windows Server are supported:

- 2008 R2

- 2012

- 2012 R2

- 2016

- 2019

To start, create a new Windows machine in vCenter using a base version of your selected Windows build.

.. NOTE:: It's recommended to make the VMDK drive as small as possible for your purposes as this generally speeds cloning and deploy times. |morpheus| provisioning and post-deploy scripts allow to to expand the drive to any size that you need.

Once the machine is created, ensure VMtools is installed on the operating system. Then, apply all updates and service packs. Next, configure WinRM and open the firewall:

.. code-block:: bash

	winrm quickconfig

.. NOTE:: WinRM configuration is optional if using VMtools RPC mode for agent install and |morpheus| Agent for guest exec.

Next, we'll install .NET 4.5 or higher. Ensure Windows Firewall will allow WinRM connections and shut down the virtual instance. Finally, convert it to a template.

.. NOTE:: |morpheus| will Sysprep images based on the "Force Guest Customizations" flag under VM settings when using DHCP. If this flag is enabled or if using static IP addresses or IP pools when provisioning, ensure a Sysprep has not been performed. In such cases, guest customization will always be performed and a Sysprep will be triggered.

**Creating a CentOS/RHEL Image**

Create a new machine in vCenter and install a base version of your preferred Linux distro.

.. NOTE:: If you are using cloud-init as part of your image, you will need to ensure your virtual machine has a cdrom.

Before installing the operating system, set up a single ext or xfs partition without a swap disk. Next, install the distro applying any updates to the operating system or security updates. Once the operating system is running and updated, install the following:

.. code-block:: bash

	yum install cloud-init
	yum install cloud-utils-growpart
	yum install open-vm-tools
	yum install git
	yum install epel-release

Set selinux to permissive as the enforced setting can cause problems with cloud-init:

.. code-block:: bash

	sudo vi /etc/selinux/config

**Cloud-Init**

We'll get started by installing cloud-init using the following command:

.. code-block:: bash

	yum -y install epel-release
	yum -y install git wget ntp curl cloud-init dracut-modules-growroot
	rpm -qa kernel | sed 's/^kernel-//'  | xargs -I {} dracut -f /boot/initramfs-{}.img {}

.. NOTE:: The above command will install some core dependencies for cloud-init and automation later as you work with your provisioned instances. For example, we install Git here as it is used for Ansible automation. If you had no plans to use Ansible, this installation could be skipped. The dracut-modules-growroot is responsible for resizing the root partition upon initial boot which was potentially adjusted during provisioning.

One key benefit of using cloud-init is that we don't have to lock credentials into the blueprint. We recommend configuring a default cloud-init user that will get created automatically when the VM is booted by cloud-init. We can define that default user in `Administration > Provisioning > Cloud-Init`.

**Network Interfaces**

As of CentOS 7, network interface naming conventions have changed. You can check this by running `ifconfig` and noting that the primary network interface has some value similar to "ens2344". The naming is dynamic and typically set based on hardware ID. We don't want this to fluctuate when provisioning this blueprint in our VMware environments. To accomplish this end, we will rename the interface back to "eth0" using the steps below.

First, adjust the bootloader to disable interface naming:

.. code-block:: bash

	sed -i -e 's/quiet/quiet net.ifnames=0 biosdevname=0/' /etc/default/grub
	grub2-mkconfig -o /boot/grub2/grub.cfg

The next step is to adjust network scripts in CentOS. Start by confiming the presence of a file called `/etc/sysconfig/network-scripts/ifcfg-eth0`. Once confirmed, run the following script:

.. code-block:: bash

	export iface_file=$(basename "$(find /etc/sysconfig/network-scripts/ -name 'ifcfg*' -not -name 'ifcfg-lo' | head -n 1)")
	export iface_name=${iface_file:6}
	echo $iface_file
	echo $iface_name
	sudo mv /etc/sysconfig/network-scripts/$iface_file /etc/sysconfig/network-scripts/ifcfg-eth0
	sudo sed -i -e "s/$iface_name/eth0/" /etc/sysconfig/network-scripts/ifcfg-eth0
	sudo bash -c 'echo NM_CONTROLLED=\"no\" >> /etc/sysconfig/network-scripts/ifcfg-eth0'

This script tries to confirm there is a new `ifcfg-eth0` config created to replace the old config file. Confirm this config exists after running and if not you will have to build your own:

.. code-block:: bash

	TYPE=Ethernet
	DEVICE=eth0
	NAME=eth0
	ONBOOT=yes
	NM_CONTROLLED="no"
	BOOTPROTO="dhcp"
	DEFROUTE=yes

For more on CentOS/RHEL image prep, including additional configurations for specific scenarios, take a look at the `VMware image prep <https://docs.morpheusdata.com/en/4.1.1/integration_guides/Clouds/vmware/vmware_templates.html#gotyas>`_ page in |morpheus| Docs.

**Creating an Ubuntu Image**

Create a new machine in vCenter and install a base version of your preferred Linux distro.

.. NOTE:: If you are using cloud-init as part of your image, you will need to ensure your virtual machine has a cdrom.

Before installing the operating system, set up a single ext partition without a swap disk. Install the distro and apply any operating system and security updates. Ensure you've set a root password.

Install cloud-init and cloud-utils-growpart:

.. code-block:: bash

	sudo apt install cloud-init
	sudo apt install cloud-utils

Install desired hypervisor drivers, such as Virto or Open-VM Tools

Install Git:

.. code-block:: bash

	sudo apt install git

Since Debian 9 includes network manager, ensure this is disabled. You can do this by editing the configuration file at `/etc/NetworkManager/NetworkManager.conf`. Within that file, update the "managed" flag to false:

.. code-block:: bash

	managed=false

We also recommend setting the network adapter to "eth0". This process is described above in the "Network Interfaces" section of the CentOS image prep guide above.

Provisioning Your First Instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At this point, we are ready to provision our first image. As a first instance, we'll provision an Apache web server to our vCenter cloud.

Navigate to `Provisioning > Instances`. If any instances are currently provisioned, we will see them listed here. To start a new instance we click the "+ADD" button to pop the "CREATE INSTANCE" wizard. We'll scroll down to and select the Apache instance type and click "NEXT".

.. image:: /images/vCenterGuideImages/FirstInstance/1createInstance.png
  :width: 80%
  :alt: Selecting an instance type to provision
  :align: center

First, we'll specify the group to provision into which determines the clouds available. If you've followed this guide to this point, you should at least have a group that houses all of your clouds which you can select here. This will allow us to select the vCenter cloud from the "CLOUD" dropdown menu. Provide a unique name to this instance and then click "NEXT"

From the "CONFIGURE" tab, we're presented with a number of options. The options are cloud and layout-specific, more generalized information on creating instances and available options is `here <https://docs.morpheusdata.com/en/4.1.1/getting_started/agent/morpheus_agent.html#morpheus-agent>`_. For our purposes, we'll select the following options:

- **LAYOUT**: Includes options such as the base OS, custom layouts will also be here when available

- **PLAN**: Select the resource plan for your instance. Some plans have minimum resource limits, |morpheus| will only show plans at or above these limits. User-defined plans can also be created in `Administration > Plans & Pricing`.

- **VOLUMES and DATASTORES**: The minimum disk space is set by the plan, this value may be locked if you've selected a custom plan that defines the volume size

- **NETWORKS**: Select a network, note that IP pools must be linked with the networks defined in VMware in order to assign static IP addresses

Under the "User Config" drawer, mark the box to "CREATE YOUR USER". Click "NEXT".

.. image:: /images/vCenterGuideImages/FirstInstance/2instanceConfigure.png
  :width: 80%
  :alt: The configure tab of the create instance dialog box
  :align: center

.. NOTE:: "CREATE YOUR USER" will seed a user account into the VM with credentials set in your |morpheus| user account settings. If you've not yet defined these credentials, you can do so by clicking on your username in the upper-right corner of the application window and selecting "USER SETTINGS".

For now, we'll simply click "NEXT" to move through the "AUTOMATION" tab but feel free to stop and take a look at the available selections here. There is more information later in this guide on automation and even more beyond that in the rest of |morpheus| docs.

Review the settings for your first instance and click "COMPLETE".

.. image:: /images/vCenterGuideImages/FirstInstance/3completeInstance.png
  :width: 80%
  :alt: Confirming the instance to be provisioned
  :align: center

We are now dropped back onto the instances list page. We can see a new entry in the list at this point with a status indicator that the new machine is being launched (rocket icon in the status field). We can double click on the instance in the list to move to the instance detail page. For now we will see a progress bar indicating that the instance is being created and is starting up. The exact amount of time this process will take depends on your environment and selections made when provisioning the instance. Initially, |morpheus| will guess as to how long this will take and the progress bar may not be accurate. Over time, |morpheus| will learn how long these processes take and progress bar accuracy will improve. For more detailed information on the status of various provisiioning processes, we can scroll down and select the "HISTORY" tab. The "STATUS" icon will change from the blue rocket to a green play button when the instance is fully ready. Furthermore, we can click on the hyperlinked IP address in the "VMS" section of this page to view a default page in a web browser to confirm success.

.. image:: /images/vCenterGuideImages/FirstInstance/4reviewInstance.png
  :width: 80%
  :alt: Monitoring privisioning progress on the instance detail page
  :align: center

Creating Your First Library Item
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the prior section, we manually provisioned our first instance. However, |morpheus| allows you to build a catalog of custom provisionable items to simplify and speed provisioning in the future. In this section, we'll build a catalog item and show how that can translate into quick instance provisioning after configuration.

.. NOTE:: Before starting this process, it's important to decide which virtual image you plan to use. If you're not using a |morpheus|-provided image, you'll want to ensure it's uploaded. You will not be able to complete this section without selecting an available image. In this example we will use |morpheus| Redis 3.0 on Ubuntu 14.04.3 v2.

Navigate to `Provisioning > Library > NODE TYPES` and click "+ADD".

.. image:: /images/vCenterGuideImages/NewCatalogItem/1addNode.png
  :width: 80%
  :alt: Adding a new node type
  :align: center

In this example, I am going to set the following options in the "NEW NODE TYPE" wizard:

- **NAME**

- **SHORT NAME**

- **VERSION**: 1 (In this particular case, the version is not important)

- **TECHNOLOGY**: VMware

- **VM IMAGE**: |morpheus| Redis 3.0 on Ubuntu 14.04.3 v2

.. NOTE:: Within the "VMware VM Options" section you should add anything that will always be used for this node, regardless of the specific deployment details. This can include LDAP Authentication, bash scripts that should run on installation, among other things.

.. image:: /images/vCenterGuideImages/NewCatalogItem/2nodeSettings.png
  :width: 80%
  :alt: Configuring options for the new node
  :align: center

With the new node created, we'll now add a new instance type which will be accessable from the provisioning wizard once created. Move from the "NODE TYPES" tab to the "INSTANCE TYPES" tab and click "+ADD".

.. image:: /images/vCenterGuideImages/NewCatalogItem/3addInstanceType.png
  :width: 80%
  :alt: Adding a new instance type
  :align: center

In the "NEW INSTANCE TYPE" wizard, I'll simply enter a **NAME** and **CODE** value. Click "SAVE CHANGES".

.. image:: /images/vCenterGuideImages/NewCatalogItem/4instanceTypeSettings.png
  :width: 80%
  :alt: Configuring the new instance type
  :align: center

Now that we've created a new instance type, access it by clicking on the name in the list of custom instances you've created. In my case, I've given the name "NewInstanceType".

.. image:: /images/vCenterGuideImages/NewCatalogItem/5openInstanceType.png
  :width: 80%
  :alt: Opening our newly created instance type
  :align: center

Once we've opened the new instance type, by default, we should be on the "LAYOUTS" tab. Click "+ADD LAYOUT".

I've set the following fields on my example layout:

- **NAME**

- **VERSION**: This is the version number of the layout itself, which is labeled 1.0 in the example

- **TECHNOLOGY**: VMware

- **Nodes**: Select the node we created earlier, if desired you can specify multiple nodes

Click "SAVE CHANGES".

.. image:: /images/vCenterGuideImages/NewCatalogItem/6layoutSettings.png
  :width: 80%
  :alt: Configuring the new layout
  :align: center

At this point we've completed the setup work and can now provision the instance we've created to our specifications. Navigate to `Provisioning > Instances` and click "+ADD". From the search bar we can search for the new instance type we've created. In the example case, we called it "newinstancetype". Click "NEXT".

.. image:: /images/vCenterGuideImages/NewCatalogItem/7newInstanceSearch.png
  :width: 80%
  :alt: Searching for our custom instance type
  :align: center

As before, we can select a group and cloud to provision this new instance. Click "NEXT". On the "CONFIGURE" tab, make note that the layout and plan are already selected because they were configured as part of creating the new instance type. Select a network and click "NEXT". Once again we will also click "NEXT" through the "AUTOMATION" tab. Finally, click "COMPLETE".

.. image:: /images/vCenterGuideImages/NewCatalogItem/8newInstanceConfigure.png
  :width: 80%
  :alt: Configuring the newlt created instance
  :align: center

As before when we manually provisioned an instance, |morpheus| will now begin to spin up the new VM. How long this will take depends on your environment but |morpheus| will predict how long this process will take and represent that on a progress bar. Over time, |morpheus| begins to learn how long these processes take and becomes more accurate in predicting spin-up time.

Once the privisioning process has completed, open the instance detail page in |morpheus| and click on the "CONSOLE" tab. You'll be logged in with your user account and are then able to confirm the machine is ready and available.

.. image:: /images/vCenterGuideImages/NewCatalogItem/10newInstanceConsole.png
  :width: 80%
  :alt: Confirming creation of the new instance
  :align: center

Conclusion
^^^^^^^^^^

At this point you should be up and running in |morpheus|, ready to consume VMware. This guide only scratches the surface, there is a lot more to see and do in |morpheus|. Take a look at the rest of `|morpheus| Docs <https://docs.morpheusdata.com/en/4.1.1/index.html>`_ for more information on supported integrations and other things possible.
