Getting Started
^^^^^^^^^^^^^^^

OpenStack Clouds are very easy to integrate with |morpheus|. First, go to the ``Infrastructure > Clouds`` section and click :guilabel:`+ ADD`. Select OpenStack to begin the integration process, most branded flavors of OpenStack will work with this Cloud selection as well.

.. WARNING:: Support for OpenStack v2 Identity API has been removed in v5.3.3

.. include:: /integration_guides/Clouds/base_options.rst

Details
```````

IDENTITY API URL
  v3 Identity endpoint.
DOMAIN ID
  For `Default` domains, Default can be used. For other domain the Domain ID must be entered, not the Domain Name.
PROJECT
  Target project
USERNAME
  Service Username
PASSWORD
  Service user password
OS VERSION
  Select Openstack Version. |morpheus| supports the latest versions of OpenStack, select the latest version available if your current version is not shown.
IMAGE FORMAT
  Select QCOW2, RAW or VMDK Image Type
LB TYPE
  Select LB Type for Openstack LB syncing and creation
Inventory Existing Instances
  Select for |morpheus| to discover and sync existing VM's
Enable Hypervisor Console
  Hypervisor console support for openstack currently only supports novnc. Be sure the novnc proxy is configured properly in your openstack environment. When disabled |morpheus| will use ssh and rdp for console conneciton (vm/host credentials required)

.. include:: /integration_guides/Clouds/advanced_options.rst

.. NOTE:: v5.3.3 adds openstack project management which requires additional permissions in openstack:

   .. code-block::

      identity:list_domain_roles
      identity:list_projects
      identity:create_project
      identity:update_project
      identity:delete_project
      identity:create_grant
      identity:revoke_grant

Most of the information in the dialog can be acquired from the Openstack dashboard. under ``Project > Access & Security > API Access``. The API URL that is needed is the one tied to `Identity`. The Domain and Project inputs typically correlate to the multitenant domain setup within Openstack (sometimes just left at default) as well as the project name given to instances. |morpheus| allows multiple integrations to the same Openstack cluster to be scoped to various domains and projects as needed.

The remaining options help |morpheus| determine which API capabilities exist in the selected Openstack environment. Hence the need for the Openstack version and image format. If a newer Openstack cluster is being used then exists in the dropdown, simply select the most recent version in the dropdown and this should function sufficiently until the new version is added.

.. TIP:: Some Openstack environments do not support QCOW2 and force RAW image formats (like Metapod). This is due to some network overhead in Ceph created by using QCOW2. |morpheus| keeps two copies of Openstack image templates for this exact purpose.

Saving this cloud integration should perform a verification step and close upon successful completion.

Existing Instances
^^^^^^^^^^^^^^^^^^

|morpheus| provides several features regarding pulling in existing virtual machines and servers in an environment. Most cloud options contain a checkbox titled '*Inventory Existing Instances*'. When this option is selected, all VMs found within the specified scope of the cloud integration will be scanned periodically and Virtual Machines will be synced into |morpheus|.

By default these virtual machines are considered 'unmanaged' and do not appear in the |ProIns| area but rather |InfComVir|. However, a few features are provided with regards to unmanaged instances. They can be assigned to various accounts if using a multitenant master account, however it may be best suited to instead assign the 'Resource Pool' to an account and optionally move all servers with regards to that pool (more on this later).

A server can also be made into a managed server. During this process remote access is requested and an agent install is performed on the guest operating system. This allows for guest operations regarding log acquisition and stats. If the agent install fails, a server will still be marked as managed and an Instance will be created in `Provisioning`, however certain features will not function. This includes stats collection and logs.

Service Ports
^^^^^^^^^^^^^

|morpheus| consumes the following OpenStack service ports by default as part of its cloud integration. If your OpenStack implementation has been configured to use alternate service ports, these can be overwritten in the Cloud configuration under the Service Endpoints section when adding or editing the Cloud integration.

.. image:: /images/integration_guides/clouds/openstack/serviceEndpoints.png
  :width: 50%

Default Service Ports
`````````````````````

* Identity: 5000
* Compute: 8774
* Image: 9292
* Key Manager: 9311
* Network: 9696
* Volume API v3: 8776 v3
* Manila: 8786

OpenStack Scalable File Service (SFS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The |morpheus| integration with Openstack Cloud includes the capability to work with Openstack Scalable File Service (SFS). SFS is shared file storage hosted on Openstack Cloud. By integrating |morpheus| with Openstack you can discover, create, manage, and delete SFS servers, as well as view and work with the file shares and files contained therein.

SFS Server Discovery and Management
```````````````````````````````````

On integrating Openstack Cloud with |morpheus|, SFS servers and file shares are discovered automatically after a short time. The server(s) can be viewed in Infrastructure > Storage > Servers. By viewing the server detail page and clicking :guilabel:`EDIT`, the storage server can be scoped as needed. Administrators can choose to scope to other Openstack Cloud integrations (if more than one relevant integration currently exists), select from synced availability zones, and scope the storage server to specific Tenants if desired.

Additionally, Openstack SFS servers can be created from the storage server list page (Infrastructure > Storage > Servers) directly in |morpheus|. Click :guilabel:`+ADD` to begin and set the storage server type value to "Openstack SFS". Just like with existing synced SFS servers, those created from |morpheus| can be scoped as needed.

.. image:: /images/integration_guides/clouds/openstack/addSfs.png
  :width: 50%

SFS File Share Discovery and Management
```````````````````````````````````````

Discovered file shares will appear among other file shares synced with |morpheus| in Infrastructure > Storage > File Shares. Depending on the number of cloud integrations in your |morpheus| appliance and the number of cloud integrations available to your user account, this list may be quite large. Using the search bar on this page, we can narrow down the list to only file shares whose names match the search terms.

We can drill into individual file shares by clicking on the hyperlinked name in the list of all integrated file shares. From the file share detail page, a list of files will appear on the files tab. Begin the process of adding a new file by clicking :guilabel:`+ADD`. The Access tab on the file shares detail page allows users to view and manage ACL rules.

.. NOTE:: "Failed to load files from storage provider" is present when the |morpheus| appliance doesn't have access to the file share.

New Openstack SFS file shares can also be created directly in |morpheus|. From the file shares list page, get started by clicking :guilabel:`+ADD`. Select the type "Openstack SFS Share". Set the storage service field to a pre-existing Openstack SFS server. Setting a friendly name for the file share in |morpheus| and selecting from synced availability zones is required.

Network and Router Creation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once an OpenStack Cloud is integrated into |morpheus|, new network creation options become available. When adding a new network (Infrastructure > Networks > Networks Tab), a new type labeled "OpenStack Private Network" is available when clicking :guilabel:`+ADD`. When the user creates this network construct in |morpheus|, a layer two subnet is created but it's not connected to a Virtual Private Cloud (VPC). This is by design as an Internet-routable network is not always desired. Continue on with this section after creating the network to also create a VPC (router).

Create a network
````````````````

#. Navigate to Infrastructure > Networks
#. Click on the Networks tab
#. Click :guilabel:`+ADD`
#. Select OpenStack Private Network
#. Complete the modal based on requirements for the new network
#. Click :guilabel:`SAVE CHANGES`

Create a router
```````````````

#. Navigate to Infrastructure > Networks
#. Click on the Routers tab
#. Click :guilabel:`+ADD`
#. Select OpenStack Router
#. Complete the modal based on requirements for the new router
#. Click :guilabel:`SAVE CHANGES`

When creating a router, it's helpful to note that the External Network is the floating IP network that has been assigned to the OpenStack project. This network will grant your Instances their routes out to the Internet. The Internal Subnet can be a layer two subnet that you may have created in the previous step. In addition, multiple subnets can be added to the router (VPC) and the IP address on the subnet would be the router's internal IP address.
