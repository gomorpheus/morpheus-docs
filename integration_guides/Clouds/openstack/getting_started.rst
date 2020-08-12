
Getting Started
^^^^^^^^^^^^^^^

OpenStack Clouds are very easy to integrate with |morpheus|. First, go to the ``Infrastructure > Clouds`` section and click :guilabel:`+ ADD`. Select OpenStack to begin the integration process, most branded flavors of OpenStack will work with this Cloud selection as well.

.. include:: /integration_guides/Clouds/base_options.rst

Details
```````
IDENTITY API URL
  v2.0 or v3 Identity endpoint.
DOMAIN ID
  For `Default` domains, Default can be used. For other domain the Domain ID must be entered, not the Domain Name.
PROJECT
  Target project
USERNAME
  Service Username
PASSWORD
  Service user password
OS VERSION
  Select Openstack Version.
IMAGE FORMAT
  Select QCOW2, RAW or VMDK Image Type
LB TYPE
  Select LB Type for Openstack LB syncing and creation
 Inventory Existing Instances
  Select for |morpheus| to discover and sync existing VM's
 Enable Hypervisor Console
  Hypervisor console support for openstack currently only supports novnc. Be sure the novnc proxy is configured properly in your openstack environment. When disabled |morpheus| will use ssh and rdp for console conneciton (vm/host credentials required)

.. include:: /integration_guides/Clouds/openstack/advanced_options.rst

.. image:: /images/openstack/add_cloud.png

.. caption="Figure 1: ", title="Add Openstack Cloud form", alt="Add Openstack Cloud form"]

.. NOTE:: The user id used to connect to a project only needs to be a member ('_member_') of the project rather then an Admin.  Admin will work but it exposes some additonal items to the project the Openstack Admin typically does not want portal users to see.

Most of the information in the dialog can be acquired from the Openstack dashboard. under ``Project -> Access & Security -> API Access``. The API Url that is needed is the one tied to `Identity`. The Domain and Project inputs typically correlate to the multitenant domain setup within Openstack (sometimes just left at default) as well as the project name given to instances. |morpheus| allows multiple integrations to the same Openstack cluster to be scoped to domains and projects as needed.

The remaining options help |morpheus| determine what api capabilities exist in the selected Openstack environment. Hence the need for the Openstack version and image format. If a newer Openstack cluster is being used then exists in the dropdown, simply select the most recent version in the dropdown and this should function sufficiently until the new version is added.

.. TIP:: Some Openstack environments do not support QCOW2 and force RAW image formats (like metapod). This is due to some network overhead in Ceph created by using QCOW2. |morpheus| keeps 2 copies of Openstack image templates for this exact purpose.

Saving this cloud integration should perform a verification step and close upon successful completion.

Existing Instances
^^^^^^^^^^^^^^^^^^

|morpheus| provides several features regarding pulling in existing virtual machines and servers in an environment. Most cloud options contain a checkbox titled '*Inventory Existing Instances*'. When this option is selected, all VMs found within the specified scope of the cloud integration will be scanned periodically and Virtual Machines will be synced into |morpheus|.

By default these virtual machines are considered 'unmanaged' and do not appear in the ``Provisioning -> Instances`` area but rather ``Infrastructure -> Hosts -> Virtual Machines``. However, a few features are provided with regards to unmanaged instances. They can be assigned to various accounts if using a multitenant master account, however it may be best suited to instead assign the 'Resource Pool' to an account and optionally move all servers with regards to that pool (more on this later).

A server can also be made into a managed server. During this process remote access is requested and an agent install is performed on the guest operating system. This allows for guest operations regarding log acquisition and stats. If the agent install fails, a server will still be marked as managed and an Instance will be created in `Provisioning`, however certain features will not function. This includes stats collection and logs.

.. NOTE:: All Cloud data is resynchronized on a 5 minute interval. This includes Datastores, Resource Pools, Networks, Blueprints, and Virtual Machines.
