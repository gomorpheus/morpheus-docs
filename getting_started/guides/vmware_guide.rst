Getting started with Morpheus and VMware
====================================================================

Introduction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Welcome to Morpheus! This guide is designed to help you get started and quickly get the most out of Morpheus with VMWare. By the end, you will integrate your first cloud, configure networking, prepare and consume images, provision instances, and get started with automation. We will briefly discuss installation and account setup but will provide links to additional resources for those very first steps. For the most part, this guide assumes you are able to get Morpheus installed and are ready to move forward from that point. There is a lot more to see and do in Morpheus that is beyond the scope of this guide. For more, consult the complete Morpheus documentation or take part in our user community forum.

Installation & Setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the simplest configuration, Morpheus needs one appliance server which will contain all the components necessary to orchestrate virtual machines and containers. Full requirements, including storage and networking considerations, can be found in Morpheus documentation `here <https://docs.morpheusdata.com/en/4.1.0/getting_started/requirements/requirements.html#requirements>`_. In order to provision any new instances, hosts, or applications, (or convert any discovered resources to managed resources) you will need a valid license. If you don't have one, you can request a lab license for free at `Morpheus Hub <https://www.morpheushub.com>`_. Once obtained, the license can be applied in Administration > Settings > LICENSE.

Groups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Groups in Morpheus define which resources a user has access to. Clouds are added to groups and a user can only access clouds that are in the groups to which their roles give them access. More information on Morpheus groups is `here <https://docs.morpheusdata.com/en/4.1.1/infrastructure/groups/groups.html#groups>`_. A deep dive into groups goes beyond the scope of this guide but it's often useful to create a group that contains all clouds for testing purposes. We will create that group now so that we can add our first cloud into this group in the next section.

Navigate to `Infrastructure > Groups`. Here we will see a list of all configured groups but, of course, this will be empty immediately after installation. Click "+CREATE". Give your group a name, such as "All Clouds". The "CODE" field is used when calling Morpheus through Morpheus API or Morpheus CLI.

Click "SAVE CHANGES". Your group is now ready to accept clouds.

Integrating Your First Cloud
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clouds in Morpheus consist of any consumable endpoint whether that be On-Prem, Public clouds, or even bare metal. In this guide, we will focus on integrating and working with VMWare vCenter.

To get started, we will navigate to `Infrastructure > Clouds`. This is the cloud detail page which lists all configured clouds. It will be empty if you've just completed installation and setup of Morpheus but soon we will see our integrated vCenter cloud here.

Click the "+ADD" button to pop the "CREATE CLOUD" wizard. Select "VMWARE VCENTER" and click the "NEXT" button.

CONFIGURE TAB
----------------------------------------------------------------------

On the "CONFIGURE" tab, we're asked to set the initial connection strings into vSphere. The **API URL** should be in the following format: https://<URL>/sdk. The **USERNAME** should be in user@domain format.

Morpheus allows vCenter clouds to be scoped to the **VDC** and **CLUSTER** or even the specific **RESOURCE POOL** if you choose. Once you've entered your URL and credentials, these dropdown menus will become populated.

The **RPC MODE** setting determines how Morpheus will connect to VMs and make configuration and scripting calls if `Morpheus Agent <https://docs.morpheusdata.com/en/4.1.1/getting_started/agent/morpheus_agent.html#morpheus-agent>`_ is not installed. In a VMware environment we have the additional option to select VMware Tools if WinRM/SSH are not available.

Additionally, we can opt to **INVENTORY EXISTING INSTANCES** to begin polling VMs for statistics and rightsizing recommendations as well as **ENABLE HYPERVISOR CONSOLE** to use native vSphere console with port 443 connectivity between Morpheus and ESXi hosts.

To move on, expand the "Advanced Options" section.

ADVANCED OPTIONS
----------------------------------------------------------------------

Within the "Advanced Options" drawer are additional configurations to consider for your first cloud. Some of these won't usable until they reference additional configured integrations. Common settings to consider are **DOMAIN**, **STORAGE TYPE**, **APPLIANCE URL** (overrides the Morpheus URL for external systems), **GUIDANCE** (setting "Manual" will make recommendations for rightsizing), and **AGENT INSTALL MODE**.

Once you're satisfied with your selections, click "NEXT"

GROUPS
----------------------------------------------------------------------

We have now arrived at the "GROUP" tab. In this case, we will mark the radio button to "USE EXISTING" groups if you wish to use the group we configured earlier.

Once you've selected the group, click "NEXT"

CONCLUDING CLOUD INTEGRATION
----------------------------------------------------------------------

On the final tab of the "CREATE CLOUD" wizard, you'll confirm your selections and click "COMPLETE". The new cloud is now listed on the cloud detail page. After a short time, Morpheus will provide summary information and statistics on existing virtual machines, networks, and other resources available in the cloud.

Viewing Cloud Inventory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configuring Default Data Stores and Resource Pools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configuring Network for Provisioning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Prepping an Image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Provisioning Your First Instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At this point, we are ready to provision our first image. As a first instance, we'll provision an Apache web server to our vCenter cloud.

Navigate to `Provisioning > Instances`. If any instances are currently provisioned, we will see them listed here. To start a new instance we click the "+ADD" button to pop the "CREATE INSTANCE" wizard. We'll scroll down to and select the Apache instance type and click "NEXT".

First, we'll specify the group to provision into which determines the clouds available. If you've followed this guide to this point, you should at least have a group that houses all of your clouds which you can select here. This will allow us to select the vCenter cloud from the "CLOUD" dropdown menu. Provide a unique name to this instance and then click "NEXT"

From the "CONFIGURE" tab, we're presented with a number of options. The options are cloud and layout-specific, more generalized information on creating instances and available options is `here <https://docs.morpheusdata.com/en/4.1.1/getting_started/agent/morpheus_agent.html#morpheus-agent>`_. For our purposes, we'll select the following options:

- **LAYOUT**: Includes options such as the base OS, custom layouts will also be here when available

- **PLAN**: Select the resource plan for your instance. Some plans have minimum resource limits, Morpheus will only show plans at or above these limits. User-defined plans can also be created in `Administration > Plans & Pricing`.

- **VOLUMES and DATASTORES**: The minimum disk space is set by the plan, this value may be locked if you've selected a custom plan that defines the volume size

- **NETWORKS**: Select a network, note that IP pools must be linked with the networks defined in VMware in order to assign static IP addresses

Under the "User Config" drawer, mark the box to "CREATE YOUR USER". Click "NEXT".

.. NOTE:: "CREATE YOUR USER" will seed a user account into the VM with credentials set in your Morpheus user account settings. If you've not yet defined these credentials, you can do so by clicking on your username in the upper-right corner of the application window and selecting "USER SETTINGS".

For now, we'll simply click "NEXT" to move through the "AUTOMATION" tab but feel free to stop and take a look at the available selections here. There is more information later in this guide on automation and even more beyond that in the rest of Morpheus docs.

Review the settings for your first instance and click "COMPLETE".

We are now dropped back onto the instances list page. We can see a new entry in the list at this point with a status indicator that the new machine is being launched (rocket icon in the status field). We can double click on the instance in the list to move to the instance detail page. For now we will see a progress bar indicating that the instance is being created and is starting up. The exact amount of time this process will take depends on your environment and selections made when provisioning the instance. Initially, Morpheus will guess as to how long this will take and the progress bar may not be accurate. Over time, Morpheus will learn how long these processes take and progress bar accuracy will improve. For more detailed information on the status of various provisiioning processes, we can scroll down and select the "HISTORY" tab. The "STATUS" icon will change from the blue rocket to a green play button when the instance is fully ready. Furthermore, we can click on the hyperlinked IP address in the "VMS" section of this page to view a default page in a web browser to confirm success.

Creating Your First Library Item
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the prior section, we manually provisioned our first instance. However, Morpheus allows you to build a catalog of custom provisionable items to simplify and speed provisioning in the future. In this section, we'll build a catalog item and show how that can translate into quick instance provisioning after configuration.

.. NOTE:: Before starting this process, it's important to decide which virtual image you plan to use. If you're not using a Morpheus-provided image, you'll want to ensure it's uploaded. You will not be able to complete this section without selecting an available image. In this example we will use Morpheus Redis 3.0 on Ubuntu 14.04.3 v2.

Navigate to `Provisioning > Library > NODE TYPES` and click "+ADD".

.. image:: /images/vCenter Guide Images/NewCatalogItem/1addNode.png

In this example, I am going to set the following options in the "NEW NODE TYPE" wizard:

- **NAME**

- **SHORT NAME**

- **VERSION**: 1 (In this particular case, the version is not important)

- **TECHNOLOGY**: VMware

- **VM IMAGE**: Morpheus Redis 3.0 on Ubuntu 14.04.3 v2

.. NOTE:: Within the "VMware VM Options" section you should add anything that will always be used for this node, regardless of the specific deployment details. This can include LDAP Authentication, bash scripts that should run on installation, among other things.

With the new node created, we'll now add a new instance type which will be accessable from the provisioning wizard once created. Move from the "NODE TYPES" tab to the "INSTANCE TYPES" tab and click "#ADD".

In the "NEW INSTANCE TYPE" wizard, I'll simply enter a **NAME** and **CODE** value. Click "SAVE CHANGES".

Now that we've created a new instance type, access it by clicking on the name in the list of custom instances you've created. In my case, I've given the name "NewInstanceType".

Once we've opened the new instance type, by default, we should be on the "LAYOUTS" tab. Click "+ADD LAYOUT".

I've set the following fields on my example layout:

- **NAME**

- **VERSION**: This is the version number of the layout itself, which is labeled 1.0 in the example

- **TECHNOLOGY**: VMware

- **Nodes**: Select the node we created earlier, if desired you can specify multiple nodes

Click "SAVE CHANGES".

At this point we've completed the setup work and can now provision the instance we've created to our specifications. Navigate to `Provisioning > Instances` and click "+ADD". From the search bar we can search for the new instance type we've created. In the example case, we called it "newinstancetype". Click "NEXT". As before, we can select a group and cloud to provision this new instance. Click "NEXT". On the "CONFIGURE" tab, make note that the layout and plan are already selected because they were configured as part of creating the new instance type. Select a network and click "NEXT". Once again we will also click "NEXT" through the "AUTOMATION" tab. Finally, click "COMPLETE".

As before when we manually provisioned an instance, Morpheus will now begin to spin up the new VM. How long this will take depends on your environment but Morpheus will predict how long this process will take and represent that on a progress bar. Over time, Morpheus begins to learn how long these processes take and becomes more accurate in predicting spin-up time.

Once the privisioning process has completed, open the instance detail page in Morpheus and click on the "CONSOLE" tab. You'll be logged in with your user account and are then able to confirm the machine is ready and available.

Automation and Configuration Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Advanced VMware Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
