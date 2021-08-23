Open Telekom Cloud
------------------

Open Telekom Cloud is an Openstack-based public cloud offering. |morpheus| offers a robust integration into OTC and supports many of its features, including those listed in the next section.

Features
^^^^^^^^

- Virtual machine provisioning
- Backups
- Brownfield VM management and migration
- Hypervisor remote console
- Cloud sync
- Lifecycle management and resizing
- Network security group creation
- Network security group management
- Router and network creation
- Load balancer services
- Docker host management and configuration
- Floating IP assignment
- OBS buckets (create, manage, delete, and discovery)

Add an Open Telekom Cloud
^^^^^^^^^^^^^^^^^^^^^^^^^

Navigate to Infrastructure > Clouds and click :guilabel:`+ ADD`. Scroll to Open Telekom Cloud and click :guilabel:`NEXT`. Complete the ADD CLOUD modal, the remainder of this guide includes descriptions of the fields presented on this modal with advice on formatting needed values and where certain data can be located.

.. include:: /integration_guides/Clouds/base_options.rst

Details
```````

:IDENTITY API URL:  The v2 or v3 identity API URL, such as ``https://iam.eu-de.otc.t-systems.com/v3``
:DOMAIN ID: This pertains to the Openstack v3 API and should be ignored when using v2. Note that this is the Domain ID and not the Domain Name. The Domain ID can be found via the CLI by typing ``openstack domain list``. For default domains, "Default" can be used
:PROJECT: OTC projects are groupings of resources and can include compute resources, storage or networking. Multiple projects may be nested under your account. Select the project to which |morpheus| should onboard from (if desired) and provision
:REGION: Region Selection
:USERNAME: The username for the OTC service account that |morpheus| will use. Ensure this account has sufficient cloud privileges to avoid interruption of work in |morpheus|
:PASSWORD: The password for the above service account
:IMAGE FORMAT: Select QCOW, RAW or VMDK
:IMAGE STORE: Set an OBS bucket as a permanent store location for |morpheus| virtual images. Users are limited to uploading images of 2GB or less in size if an OBS bucket is not specified here
:INVENTORY EXISTING IMAGES: When selected, |morpheus| will automatically onboard existing cloud resources which can be converted to managed Instance if desired. View onboarded cloud resources in the Compute Section (Infrastructure > Compute)
:ENABLE HYPERVISOR CONSOLE: Hypervisor console support for Openstack currently only supports ``novnc``. Be sure the novnc proxy is configured properly in your Openstack environment

Service Endpoints
`````````````````

If needed, update the following service endpoints. A complete listing of OTC API endpoints is `here <https://docs.otc.t-systems.com/endpoint/index.html>`_.

* COMPUTE SERVICE
* IMAGE SERVICE
* STORAGE SERVICE
* NETWORK SERVICE
* LOAD BALANCER SERVICE
* OBJECT STORAGE SERVICE
* SHARED FILE SYSTEM SERVICE

.. include:: /integration_guides/Clouds/openstack/advanced_options.rst

Network and Router Creation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once an Open Telekom Cloud is integrated into |morpheus|, new network creation options become available. When adding a new network (Infrastructure > Networks > Networks Tab), a new type labeled "Open Telekom Private Network" is available when clicking :guilabel:`+ADD`. When the user creates this network construct in |morpheus|, a layer two subnet is created but it's not connected to a Virtual Private Cloud (VPC). This is by design as an Internet-routable network is not always desired. Continue on with this section after creating the network to also create a VPC (router).

Create a network
````````````````

#. Navigate to Infrastructure > Networks
#. Click on the Networks tab
#. Click :guilabel:`+ADD`
#. Select Open Telekom Private Network
#. Complete the modal based on requirements for the new network
#. Click :guilabel:`SAVE CHANGES`

Create a router
```````````````

#. Navigate to Infrastructure > Networks
#. Click on the Routers tab
#. Click :guilabel:`+ADD`
#. Select Open Telekom Router
#. Complete the modal based on requirements for the new router
#. Click :guilabel:`SAVE CHANGES`

When creating a router, it's helpful to note that the External Network is the floating IP network that has been assigned to the OTC project. This network will grant your Instances their routes out to the Internet. The Internal Subnet can be a layer two subnet that you may have created in the previous step. In addition, multiple subnets can be added to the router (VPC) and the IP address on the subnet would be the router's internal IP address.
