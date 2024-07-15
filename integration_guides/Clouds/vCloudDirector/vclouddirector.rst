vCloud Director
---------------

Features
^^^^^^^^

* Virtual Machine Provisioning
* Backups / Snapshots
* Datastores
* Brownfield VM management and migration
* Periodic Synchronization
* Lifecycle Management and Resize
* IP Pool Support
* Multi-NIC Interfaces
* Kubernetes and Docker
* Proxy Support
* Image Builder
* Monthly estimated pricing and usage tracker
* Custom plan discovery and utilization at provision time

Configuration
^^^^^^^^^^^^^

Add vCD Cloud From `Infrastructure > Clouds`
````````````````````````````````````````````

#. Navigate to ``Infrastructure > Clouds``
#. Select :guilabel:`+ ADD`
#. Select **VCLOUD DIRECTOR** from the Clouds list
#. Select :guilabel:`NEXT`
#. Populate the following:

   .. include:: /integration_guides/Clouds/base_options.rst

   **Details**

   .. NOTE:: Authenticating a new vCD Cloud requires either a username and password combination OR an API token and Tenant. You do not need both despite the fact that all four of those fields are indicated as required fields.

   API URL
     vCloud Director API Url
      Example: ``https://org.vcd.company.com``
   CREDENTIALS
     Authenticating a new vCD Cloud requires either a username and password combination OR an API token and Tenant. These may be locally entered (select Local Credentials), locally entered and stored securely for future use (select "username and password" or "api token, tenant" from within the "New Credentials" section), or a pre-existing credential set may be selected from the |morpheus| secure credential store. Depending on the selection, additional fields will appear (or some may disappear) to facilitate your choice
   USERNAME
     vCD Organization Administrator or System Administrator User

     - User must have an Organizational Administrator or System Administrator Role
     - Username must be in the format of <name>@<org>
     - When using a user with the System Administrator role, give the username in the format of <username>@system. Additionally, ensure this user has permission set correctly, such as to view objects created by the organization administrator if needed. Otherwise, things like catalogs and vApps created by the Organization Administrator might not be visible to |morpheus|
     - In some cases, it may not be advisable to use the system administrator user. This is because some environments will have API access turned off for the system administrator for security reasons as the user would be able to remove key pieces of infrastructure. If your system administrator user does have API access and you understand the risks, you can authenticate |morpheus| with this user

   PASSWORD
    Password for the user indicated above
   API TOKEN
    A generated API token for the service account user
   TENANT
    The Tenant to which the service account user authenticates
   ORG
    Select Organization. Dropdown populates upon successful authorization.
   VDC
    Select VDC. Dropdown populates upon successful authorization.
   API VERSION
    Full version required which much be in the "xx.x" format. When applicable, do not drop a trailing "0" (Ex. ``31.0``). |morpheus| will attempt to discover the API version, which would make this field optional. However, vCD allows disabling of the API versions API. In such an environment, the user would need to specify the API version here
   CATALOG
    Optionally select a vCD catalog to store |morpheus| artifacts or use the default "morpheus_auto" catalog
   Inventory Existing Instances
    If enabled, existing Virtual Machines will be inventoried and appear as unmanaged Virtual Machines in |morpheus|
   Enable Hypervisor Console
    Mark to use VNC hypervisor console for the |morpheus| console rather than the default SSH or RDP connection methods

   .. NOTE: Multiple Organizations/VDC's can be added by creating additional Clouds in |morpheus|. Additionally, websockets need to be enabled on your load balancer when vCD has been deployed in a highly available configuration. The hypervisor console services use websockets. To enable websockets on your load balancer, please consult your load balancer documentation.

   .. include:: /integration_guides/Clouds/advanced_options.rst

#. Select :guilabel:`NEXT`
#. Select an existing or create a new Group to add the Cloud to. The Cloud can be added to additional Groups in a Groups `Clouds` tab.
#. Select :guilabel:`NEXT`
#. Review and then Select :guilabel:`COMPLETE`

.. include:: /integration_guides/Clouds/vCloudDirector/creatingvcloud.rst
​
