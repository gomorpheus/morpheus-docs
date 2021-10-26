Getting started with |morpheus| and Azure
=========================================

Introduction
------------

This guide is designed to help you get started and quickly get the most out of Morpheus with Microsoft Azure public cloud. By the end, you will integrate your first cloud with |morpheus|, configure networking, prepare and consume images, provision instances, and get started with automation. We will briefly discuss installation and account setup but will provide links to additional resources for those very first steps. For the most part, this guide assumes you are able to get |morpheus| installed and are ready to move forward from that point. There is a lot more to see and do in Morpheus that is beyond the scope of this guide. For more, consult the complete Morpheus documentation or take part in our `Reddit user community forum <https://www.reddit.com/r/morpheusdata/>`_.

Installation & Setup
--------------------

In the simplest configuration, |morpheus| needs one appliance server which will contain all the components necessary to orchestrate virtual machines and containers. Full requirements, including storage and networking considerations, can be found in |morpheus| documentation `here <https://docs.morpheusdata.com/en/latest/getting_started/requirements/requirements.html>`_. In order to provision any new Instances, hosts, or applications (or convert any discovered resources to managed resources) you will need a valid license. If you don't have one, you can request a community edition license for free at `Morpheus Hub <https://www.morpheushub.com>`_. Once obtained, the license can be applied in |AdmSetLic|. For more, take a look at our community edition `welcome package <https://www.morpheusdata.com/community-welcome>`_.

Groups
------

Groups in |morpheus| define which resources a user has access to. Clouds are added to Groups and a user can only access Clouds that are in the Groups to which their roles give them access. More information on |morpheus| Groups is `here <https://docs.morpheusdata.com/en/latest/infrastructure/groups/groups.html#groups>`_. A deep dive into Groups goes beyond the scope of this guide but it's often useful to create a Group that contains all Clouds for testing purposes. We will create that group now so that we can add our first Cloud into this Group in the next section.

Navigate to `Infrastructure > Groups`. Here we will see a list of all configured groups but, of course, this will be empty immediately after installation. Click "+CREATE". Give your group a name, such as "All Clouds". The "CODE" field is used when calling |morpheus| through |morpheus| API or |morpheus| CLI. It's useful in most cases to have an "All Clouds" group for testing purposes so this will likely help you down the road.

Click :guilabel:`SAVE CHANGES`. Your Group is now ready to accept Clouds.

.. image:: /images/azureguideimages/1newGroup.png

Integrating Your First Cloud
----------------------------

Clouds in |morpheus| consist of any consumable endpoint whether that be on-prem, public clouds, or even bare metal. In this guide, we will focus on integrating and working with Microsoft Azure public cloud.

To get started, we will navigate to `Infrastructure > Clouds`. This is the Cloud list page which lists all configured Clouds. It will be empty if you've just completed installation and setup of |morpheus| but soon we will see our integrated Azure cloud here.

Click the "+ADD" button to pop the "CREATE CLOUD" wizard. Select "AZURE (PUBLIC)" and click the "NEXT" button.

On the "CONFIGURE" tab, we're asked to provide Azure-specific details to connect to the cloud. |morpheus| Azure integration requires Owner or Contributor access to subscription via App Registration. Adding an Azure Cloud or Clouds to |morpheus| will require the following:

* Azure Subscription ID
* Directory (tenant) ID
* Application (client) ID
* Application (client) Secret
* Application (client) must be Owner or Contributor of Subscription

CSP Accounts require the additional following input:

* CSP Directory (tenant) ID
* CSP Application (client) ID
* CSP Application (client) SECRET

.. image:: /images/azureguideimages/2createCloud.png

Create App Registration
```````````````````````

|morpheus| authenticates with Azure via an App Registration with an Owner or Contributor Role on a Subscription. Use the steps below to create and collect the required credentials and assign the required permissions to integrate Azure with |morpheus|.

.. warning:: Using an App Registration (service principal) that has selective resource permissions and is not an Owner or Contributor of the Subscription is not supported and will cause failures/issues. Please confirm the App Registration you use to integrate Azure with |morpheus| has Owner or Contributor permissions on the specified Subscription.

If you do not have an existing Azure Active Directory App Registration, or you wish to use an new one for |morpheus|, you will need to create one using the steps below. If you already have one you wish to use, continue to the next section.

#. Log into the Azure portal
#. Select "Azure Active Directory"
#. Select "App Registrations"
#. Select "New Registration"

   .. image:: /images/clouds/azure/Default_Directory_App_registrations_Microsoft_Azure.png

#. Next, give the app a name, specify Web app / API for the type (default) and enter any URL for the Sign-on URL:
#. Click Create and your new App Registration will be created.

   .. image:: /images/clouds/azure/Register_an_application_Microsoft_Azure.png

Now that we have our App Registration, we will gather the credentials required for the |morpheus| Azure integration in the next section.

Copy Directory (tenant) and Application (client) IDs
````````````````````````````````````````````````````

The App Registration Directory (tenant) and Application (client) ID are required for the |morpheus| Azure integration. Both can be found in the overview section of the App Registration.

#. Go to the Overview section of your App Registration
#. Copy the Directory (tenant) ID
#. Store/Paste for use as the Tenant ID when adding your Azure cloud in |morpheus|
#. Copy the Application (client) ID
#. Store/Paste for use as the Client ID when adding your Azure cloud in |morpheus|

.. image:: /images/clouds/azure/morpheusAppReg_Microsoft_Azure.png

Generate a Client Secret
````````````````````````

While still in your App Registration:

#. Select "Certificates & secrets" in the Manage section
#. Select ``+ New client secret``

   .. image:: /images/clouds/azure/morpheusAppReg_Certificates_secrets_Microsoft_Azure.png

#. The "Add a client secret" modal will come up
#. Add a description to help identify the secret in the future
#. Select an expiration duration
#. Click :guilabel:`Add`

   .. image:: /images/clouds/azure/morpheusAppReg_Certificates_secrets_Add.png

#. Copy the newly-generated client secret value.

   .. IMPORTANT:: Copy the client secret value before continuing as it will not be viewable again later.

   .. image:: /images/clouds/azure/morpheusAppReg_Certificates_secrets_Copy.png

#. Store/Paste client secret for use later when adding your Azure cloud in |morpheus|

You now have three of the four credentials required for |morpheus| Azure cloud integration. The last credential required is the Azure Subscription ID which we will gather in the next section.

Subscription ID
```````````````

To get the Azure Subscription ID:

#. Navigate to the Subscriptions section. The search function can help to locate these sections if they aren't immediately apparent in the UI menu

   .. image:: /images/clouds/azure/azuresubscriptionssearch.png

#. In the Subscriptions section, copy the Subscription ID

   .. image:: /images/clouds/azure/Subscriptions_Microsoft_Azure.png

#. Store/Paste for use as the Subscription ID when adding your Azure cloud in |morpheus|

Make App Registration owner or contributor of Subscription
``````````````````````````````````````````````````````````

The App Registration used needs to be an owner of the Azure Subscription used for the |morpheus| cloud integration. If lesser permissions are given or permissions are assigned at individual resource levels, |morpheus| will not be able to properly inventory existing cloud resources, create resources or remove them.

#. In the Subscriptions section in Azure, select the Subscription
#. In the Subscription pane, select "Access Control (IAM)"
#. Either Click :guilabel`+ Add`, and then "Add Role Assignment" OR simply select "Add a role assignment"

   .. image:: /images/clouds/azure/Azure_subscription_1_Access_control_IAM_Microsoft_Azure.png

#. In the right pane, select "Owner" or "Contributor" Role type
#. Search for the name of the App Registration used for the |morpheus| integration
#. Select the App Registration in the search results
#. Select "Save"

   .. image:: /images/clouds/azure/Add_role_assignment_save.png

You now have the required credentials and permissions to add an Azure Cloud integration into |morpheus|. Continue on with the next sections of this guide to complete the integration from the |morpheus| side.

Complete the Add Cloud Process in |morpheus|
````````````````````````````````````````````

If you've followed this guide from the start, you will already have a Cloud integration modal open in |morpheus| UI. If you still need to open that wizard, navigate to Infrastructure > Clouds > :guilabel:`+ ADD` > Azure (Public) and click :guilabel:`NEXT`. Fill in the following fields with the information gathered in the steps above:

- Subscription ID
- Tenant ID
- Client ID
- Client Secret
- Location
- Resource Group
- Inventory Existing Instances
- Inventory Level
- Account Type

Once valid credentials are populated in the appropriate fields, the LOCATION dropdown menu will be populated. Select an available region, this is also a helpful check to ensure you've correctly provided working credentials. In addition, we can scope the cloud integration to all resource groups in the region (All) or can select a specific resource group to limit |morpheus| resource inventorying and creation to just that resource group.

By checking INVENTORY EXISTING INSTANCES, |morpheus| will automatically onboard existing cloud resources which are scoped to the region and resource group indicated. If this box is checked, we will also need to select either basic inventorying, which syncs name, IP addresses, platform types, power status, and sizing data (storage, CPU, and RAM) OR full (API heavy) inventorying which syncs resource utilization metrics (storage, CPU, and RAM) when available in addition to what we get with basic inventorying.

To move on, expand the "Advanced Options" section.

.. NOTE:: CSP accounts will also need to enter CSP TENANT ID, CSP CLIENT ID, and CSP CLIENT SECRET in the Advanced Options section.

Within the "Advanced Options" drawer are additional configurations to consider for your first Cloud. Some of these won't usable until they reference additional configured integrations. Common settings to consider are **DOMAIN**, **STORAGE TYPE**, **APPLIANCE URL** (overrides the |morpheus| URL for external systems), **GUIDANCE** (setting "Manual" will make recommendations for rightsizing), **COSTING**, **DNS INTEGRATION**, **CMDB**, and **AGENT INSTALL MODE**.

Once you're satisfied with your selections, click "NEXT"

We have now arrived at the "GROUP" tab. In this case, we will mark the radio button to "USE EXISTING" Groups if you wish to use the Group we configured earlier. Alternatively, you can create a new one here.

.. image:: /images/azureguideimages/3cloudGroup.png

Once you've selected or created the Group, click "NEXT"

On the final tab of the "CREATE CLOUD" wizard, you'll confirm your selections and click "COMPLETE". The new Cloud is now listed on the Cloud list page. After a short time, |morpheus| will provide summary information and statistics on existing virtual machines, networks, and other resources available in the Cloud.

Viewing Cloud Inventory
^^^^^^^^^^^^^^^^^^^^^^^

Now that we've integrated our first Azure cloud, we can stop for a moment to review what |morpheus| gives us from the Cloud detail page. We can see that |morpheus| gives us estimated costs and cost histories, metrics on used resources, and also lists out resource counts in various categories including container hosts, hypervisors, and virtual machines. We can drill into these categories to see lists of resources in the various categories by clicking on the category tabs. We can link to the detail page for any specific resource by clicking on it from its resource category list.

Configuring Resource Pools
^^^^^^^^^^^^^^^^^^^^^^^^^^

With our Azure Cloud configured, |morpheus| will automatically sync in available resource pools and data stores.

For resource pools, once |morpheus| has had time to ingest them, then will be visible from the cloud detail page. Navigate to `Infrastructure > Clouds > (your Azure cloud) > Resources tab`. In here, we are able to see and control access to the various resource pools that have been configured in Azure. For example, we can restrict access to a specific resource pool within |morpheus| completely by clicking on the "ACTIONS" button, then clicking "Edit". If we unmark the "ACTIVE" button and then click "SAVE CHANGES" we will see that the resource pool is now grayed out in the list. The resources contained in that pool will not be accessible for provisioning within |morpheus| if it is not configured as active.

.. image:: /images/azureguideimages/4resourcePool.png

Often our clients will want to make specific blocks of resources available to their own customers. This can be easily and conveniently controlled through the same "EDIT RESOURCE POOL" dialog box we were just working in. If we expand the "Group Access" drawer, we are able to give or remove access to each pool to any Group we'd like. We can also choose to make some or all of our resource pools available to every Group. Specific resource pools can also be defined as the default for each Group when needed.

.. image:: /images/azureguideimages/5resourcePoolGroup.png

Additionally, we may choose to allow only certain service plans to be provisioned into a specific pool of resources. For example, perhaps a specific cluster is my SQL cluster and only specific services plans should be consumable within it. We can control that through this same dialog box.

Configuring Data Stores
^^^^^^^^^^^^^^^^^^^^^^^

To take a look at data stores, we'll move from the "Resources" tab to the "Data Stores" tab on our Cloud detail page.

|morpheus| gives the user similar control with data stores to what we saw with our resources pools earlier. Just like with resource pools, we can disable access within |morpheus| completely by clicking on "ACTIONS" and then "Edit". If we unmark the "ACTIVE" checkbox and click "SAVE CHANGES", you will see that specific data store has been grayed out.

.. image:: /images/azureguideimages/6dataStore.png

Just like with resource pools, we are also able to scope data stores to specific Groups. This ensures that the members of each Group are only able to consume the data stores they should have access to.

Configuring Network for Provisioning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When configuring networking, we can set global defaults by going to `Infrastructure > Network > NETWORKS tab`. Here we can add or configure networks from all Clouds integrated into |morpheus|. Depending on the number of clouds |morpheus| has ingested, this list may be quite large and may also be paginated across a large number of pages. In such a case, it may be easier to view or configure networks from the specific Cloud detail page so that networks from other Clouds are not shown.

Still in `Infrastructure > Network`, make note of the "INTEGRATIONS" tab. It's here that we can set up any integrations that may be relevant, such as IPAM integrations. Generally speaking, when adding IPAM integrations, we simply need to name our new integration, give the API URL, and provide credentials. There's more information in the `IPAM integration <https://docs.morpheusdata.com/en/latest/integration_guides/integration_guides.html#networking>`_ section of |morpheus| Docs.

In `Infrastructure > Networking` we can also set up IP address pools from the IP Pools tab. These pools can be manually defined, known as a Morpheus-type IP pool, or they can come from any IPAM integrations you've configured. As instances are provisioned, Morpheus will assign IP addresses from the pool chosen during provisioning. When the instance is later dissolved, Morpheus will automatically release the IP address to be used by another instance when needed. When adding or editing a network, we can opt to scope the network to one of these configured IP address pools. Edit an existing network by clicking the pencil icon on the Networks List Page (Infrastructure > Networks > Networks Tab) and fill in the "Network Pool" field to associate the IP Pool with the network.

Since this guide is focused on working within an Azure cloud that we integrated at the start, we will take a look at our network configurations on the cloud detail page as well. Navigate to `Infrastructure > Clouds > (your Azure cloud) > NETWORKS tab`. Just as with resource pools and data stores, we have the ability to make certain networks inactive in |morpheus|, or scope them to be usable only for certain Groups or Tenants.

.. image:: /images/azureguideimages/7cloudNetworks.png

..
  Prepping an Image
  ^^^^^^^^^^^^^^^^^

  As we'll discuss and try out in the next section, |morpheus| comes out of the box with a default set of blueprints that are relevant to many modern deployment scenarios. For the most part, these are base operating system images with a few additional adjustments. We will work with images included in |morpheus| by default in this guide but it's important to discuss how to prep custom images as well.

  **Creating a Windows Image**

  The following versions of Windows Server are supported:

  - 2008 R2

  - 2012

  - 2012 R2

  - 2016

  - 2019

  To start, create a new Windows machine in Azure using a base version of your selected Windows build.

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

  One key benefit of using cloud-init is that we don't have to lock credentials into the blueprint. We recommend configuring a default cloud-init user that will get created automatically when the VM is booted by cloud-init. We can define that default user in `|AdmSetPro| > Cloud-Init`.

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

  For more on CentOS/RHEL image prep, including additional configurations for specific scenarios, take a look at the `VMware image prep <https://docs.morpheusdata.com/en/latest/integration_guides/Clouds/vmware/vmware_templates.html#gotyas>`_ page in |morpheus| Docs.

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

At this point, the groundwork is laid and we are ready to attempt our first new provisioning. As a first Instance, we'll provision an Apache web server to our Azure cloud. |morpheus| includes a very robust catalog of pre-configured Instance types. We'll use one of these included catalog items for this guide but you'll likely also need to prep your own custom images and Instance types to make available to your users. Much more on this can be found elsewhere in |morpheus| documentation.

Navigate to `|ProIns|`. If any Instances are currently provisioned, we will see them listed here. To start a new Instance we click :guilabel:`+ ADD` to open the "CREATE INSTANCE" wizard. We'll scroll down to and select the Apache instance type and click "NEXT".

.. image:: /images/azureguideimages/8createInstance.png

First, we'll specify the Group to provision into which determines the Clouds available. If you've followed this guide to this point, you should at least have a Group that houses all of your Clouds which you can select here. This will allow us to select the Azure cloud from the "CLOUD" dropdown menu. Provide a unique name to this instance and then click "NEXT"

From the "CONFIGURE" tab, we're presented with a number of options. The options are cloud and layout-specific, more generalized information on creating Instances and available options is `here <https://docs.morpheusdata.com/en/latest/provisioning/instances/instances.html>`_. For our purposes, we'll select the following options:

- **LAYOUT**: Includes options such as the base OS, custom layouts will also be here when available

- **PLAN**: Select the resource plan for your instance. Some plans have minimum resource limits, |morpheus| will only show plans at or above these limits. User-defined plans can also be created in `|AdmPla|`.

- **VOLUMES**: The minimum disk space is set by the plan, this value may be locked if you've selected a custom plan that defines the volume size

- **NETWORKS**: Select a network

Under the "User Config" drawer, mark the box to "CREATE YOUR USER". Click :guilabel:`NEXT`.

.. image:: /images/azureguideimages/9configureInstance.png

.. NOTE:: "CREATE YOUR USER" will seed a user account into the VM with credentials set in your |morpheus| user account settings. If you've not yet defined these credentials, you can do so by clicking on your username in the upper-right corner of the application window and selecting "USER SETTINGS".

For now, we'll simply click :guilabel:`NEXT` to move through the "AUTOMATION" tab but feel free to stop and take a look at the available selections here. There is more information later in this guide on automation and even more beyond that in the rest of |morpheus| docs.

Review the settings for your first instance and click :guilabel:`COMPLETE`.

We are now dropped back onto the Instances list page. We can see a new entry in the list at this point with a status indicator that the new machine is being launched (rocket icon in the status field). We can double click on the Instance in the list to move to the Instance detail page. For now we will see a progress bar indicating that the Instance is being created and is starting up. The exact amount of time this process will take depends on selections made when provisioning the Instance. Initially, |morpheus| will guess as to how long this will take and the progress bar may not be accurate. Over time, |morpheus| will learn how long these processes take and progress bar accuracy will improve. For more detailed information on the status of various provisioning processes, we can scroll down and select the "HISTORY" tab. The "STATUS" icon will change from the blue rocket to a green play button when the Instance is fully ready. Furthermore, we can click on the hyperlinked IP address in the "VMS" section of this page to view a default page in a web browser to confirm success.

Creating Your First Library Item
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the prior section, we manually provisioned our first Instance. However, |morpheus| allows you to build a catalog of custom provisionable items to simplify and speed provisioning in the future. In this section, we'll build a catalog item and show how that can translate into quick Instance provisioning after configuration.

.. NOTE:: Before starting this process, it's important to decide which virtual image you plan to use. If you're not using a |morpheus|-provided image, you'll want to ensure it's configured. You will not be able to complete this section without selecting an available image. In this example we will use a CentOS image that was previously configured in the |morpheus| library. If you need to configure your own images prior to starting this section, navigate to |LibVir| and click :guilabel:`+ ADD`. A deeper dive into image prep and virtual image configuration goes beyond the scope of this guide.

Provisionable elements in |morpheus| combine a Node Type(s), Layout(s), and an Instance Type. The `Overview section <https://docs.morpheusdata.com/en/latest/provisioning/library/library.html#overview>`_ of |morpheus| docs discusses these objects and how they work together in greater detail. Our first step here will be to create a Node Type which wrap the image itself with additional configuration, templates, and scripts. While not strictly required, creating the Node Type, Instance Type, and then the Layout is often a good workflow for creating Library items. That is the order we will follow in this guide.

Navigate to |LibBluNod| and click :guilabel:`+ ADD`

In this example, I am going to set the following options in the "NEW NODE TYPE" wizard:

- **NAME**: *Example Azure CentOS 7*

- **SHORT NAME**: eac7 (Identifies the Node Type in |morpheus| API/CLI)

- **VERSION**: 7 (Ensures the correct Node Types are used when tying Layouts with multiple images to the same Instance Type)

- **TECHNOLOGY**: Azure

- **VM IMAGE**: Azure-Centos-7

Click :guilabel:`SAVE CHANGES`

.. image:: /images/azureguideimages/10addNodeType.png

With the new Node Type created, we'll now add a new Instance type which will be accessible from the provisioning wizard once created. Move from the "NODE TYPES" tab to the "INSTANCE TYPES" tab and click :guilabel:`+ ADD`.

In the "NEW INSTANCE TYPE" wizard, I'll simply enter a **NAME** and **CODE** value. Click :guilabel:`SAVE CHANGES`. You could also provide a description, icon, and category for easier identification from the provisioning wizard later.

.. image:: /images/azureguideimages/11addInstanceType.png

Now that we've created a new Instance type, access it by clicking on the name in the list of custom Instances you've created. In my case, I've given the name "*Example Azure CentOS 7*".

Once we've opened the new Instance type, by default, we should be on the "LAYOUTS" tab. Click :guilabel:`+ ADD LAYOUT`. I've set the following fields on my example layout:

- **NAME**: *Example Azure CentOS 7*

- **VERSION**: 7 (This is the version number of the layout itself, which is labeled 7 in the example)

- **TECHNOLOGY**: Azure

- **Nodes**: Select the Node Type we created earlier, if desired you can specify multiple nodes

Click :guilabel:`SAVE CHANGES`.

.. image:: /images/azureguideimages/12addLayout.png

At this point we've completed the setup work and can now provision the Instance we've created to our specifications. Navigate to `|ProIns|` and click :guilabel:`+ ADD`. From the search bar we can search for the new Instance type we've created.

.. image:: /images/azureguideimages/13createCustomInstance.png

As before, we can select a Group and Cloud to provision this new Instance. Click :guilabel:`NEXT`. On the "CONFIGURE" tab, make note that the layout and plan are already selected because they were configured as part of creating the new Instance type. Select a network and click :guilabel:`NEXT`. Once again we will also click :guilabel:`NEXT` through the "AUTOMATION" tab. Finally, click :guilabel:`COMPLETE`.

As before when we provisioned a pre-existing Instance from the default catalog, |morpheus| will now begin to spin up the new VM. How long this will take depends on the configuration and environmental factors but |morpheus| will predict how long this process will take and represent that on a progress bar. Over time, |morpheus| begins to learn how long these processes take and becomes more accurate in predicting spin-up time.

Once the provisioning process has completed, open the Instance detail page in |morpheus| and click on the "CONSOLE" tab. You'll be logged in with your user account and are then able to confirm the machine is ready and available, assuming the image and your custom catalog item were configured to seed user accounts and connect back to the |morpheus| appliance.

Automation and Configuration Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|morpheus| automation is composed of Tasks and Workflows. A Task could be a script added directly, scripts or Blueprints pulled from the |morpheus| Library, playbooks, recipes, or a number of other things. The complete list of Task types can be found in the `Automation section <https://docs.morpheusdata.com/en/latest/provisioning/automation/automation.html#automation>`_ of |morpheus| docs. Tasks can be executed individually but they are often combined into workflows. We can opt to run a workflow at provision time or they can be executed on existing instances through the Actions menu.

In this guide we will set up an Ansible integration, create a Task, add the Task to a Workflow, and run the Workflow against a new and existing Instance. If you've worked through this guide to this point, you should already have an Apache instance running. If you don't yet have that, provision one before continuing with this guide and ensure it's reachable on port 80.

We'll first set up the Ansible integration, you can integrate with the sample repository referenced here or integrate with your own. Go to '|AdmInt|'. Click :guilabel:`+NEW INTEGRATION` and select Ansible from the dropdown menu. Fill in the following details:

- **NAME**

- **ANSIBLE GIT URL**: https://github.com/ncelebic/morpheus/-ansible-example, or enter the URL for your own Ansible git repository

- **PLAYBOOKS PATH**

- **ROLES PATH**

- Mark the box to "USE |morpheus| AGENT COMMAND BUS"

.. NOTE:: If your git repository requires authentication, you should create a keypair and use the following URL format: git@github.com:ncelebic/morpheus/-ansible-example.git.

Click :guilabel:`SAVE CHANGES`. You'll now see our new Ansible integration listed among any other configured integrations. If we click on this new integration to view detail, a green checkmark icon indicates the git repository has been fully synced.

With the Ansible integration set up, we can now create a task that includes our playbook. Go to `|LibAut|`, click :guilabel:`+ ADD`. We'll first set our "TYPE" value to Ansible Playbook so that the correct set of fields appear in the "NEW TASK" wizard. Set the following options:

- **NAME**

- **ANSIBLE REPO**: Here we will choose the Ansible integration that we just created

- **PLAYBOOK**: In our example case, enter 'playbook.yml'

Click "SAVE CHANGES" to save our new task. We can test the new task on our Apache VM now by going to `|ProIns|` and clicking into our VM. From the "ACTIONS" menu select "Run Task". From the "TASK" dropdown menu, select the task we just added and click "EXECUTE".

To see the progress of the task, click on the "HISTORY" tab and click on the (i) button to the right of each entry in the list. In this case, we can also see the results of the task by clicking on the link in the "LOCATION" column of the "VMS" section.

Now that our task is created, we can put it into a workflow. Back in `|LibAut|` we will click on the "WORKFLOWS" tab. Click "+ADD" and select Provisioning Workflow. We'll give the new workflow a name and expand the Post Provision section. As we begin to type in the name of the task we've created, it should appear as a selection. Click "SAVE CHANGES".

Now that we have a Workflow, return to `|ProIns|` and begin to provision another Apache instance. More detailed instructions on provisioning a new Apache instance are included earlier in this guide if needed. Now, when you reach the "AUTOMATION" section of the "CREATE INSTANCE" wizard, we have a workflow to select. From the "WORKFLOW" dropdown menu, select the workflow we just created and complete provisioning of the new instance.

As the instance is provisioning, we can go to the "HISTORY" tab and see |morpheus| executing the tasks that were contained in our workflow.

This is just one example of using |morpheus| to automate the process of configuring an instance to your needs. There are a number of other automation types that can be built into your Workflows as well. For further information, take a look at the `automation integrations <https://docs.morpheusdata.com/en/latest/integration_guides/integration_guides.html#automation>`_ guide in |morpheus| docs.

Conclusion
^^^^^^^^^^

At this point you should be up and running in |morpheus|, ready to consume Azure public cloud. This guide only scratches the surface, there is a lot more to see and do in |morpheus|. Take a look at the rest of `Morpheus Docs <https://docs.morpheusdata.com/en/latest/index.html>`_ for more information on supported integrations and other things possible.
