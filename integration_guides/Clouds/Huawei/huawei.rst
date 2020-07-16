Huawei Cloud
------------

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
- Huawei OBS buckets (create, manage, delete, and discovery)
- Huawei SFS (create, manage, and delete)

Integrate Huawei Cloud with |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To integrate Huawei Cloud with |morpheus|, we'll gather the following pieces of information:

- Account Name
- Identity (IAM) API URL
- Project
- Username
- Password

Begin by logging into your `Huawei Cloud console <https://console-intl.huaweicloud.com/console>`_. If you're not currently logged in, you will be prompted to do so. Once on the console page, hover over your username in the upper-right corner of the application window and select "My Credentials".

.. image:: /images/integration_guides/clouds/huawei/1credentials.png

From the credentials page, we can gather the Account Name and the Project Name, record them for later when we provide the integration information to |morpheus|.

.. image:: /images/integration_guides/clouds/huawei/2account_project.png

To gather the API endpoint URL, take a look at the complete list of `endpoints <https://developer.huaweicloud.com/en-us/endpoint>`_. If a specific endpoint exists for your region, use it. In any other case use the endpoint for all regions. It will be formatted like this: https://iam.myhuaweicloud.com/v3.

.. image:: /images/integration_guides/clouds/huawei/3identity_api_endpoints.png

With this information gathered, and presuming you know the credentials for the service account you wish to use, we can move back into |morpheus|-UI.

Navigate to Infrastructure > Clouds and click :guilabel:`+ ADD`. Scroll to Huawei Cloud and click :guilabel:`NEXT`. The information we've gathered will be plugged into the CREATE CLOUD modal. The DOMAIN ID field will accept the Account Name field we gathered. Your completed CREATE CLOUD modal will look similar to the one pictured below:

.. image:: /images/integration_guides/clouds/huawei/4add_cloud.png

After clicking :guilabel:`NEXT`, add this new Cloud to a Group or create a new Group. On finalizing the wizard, Huawei Cloud will be integrated into |morpheus| and ready for provisioning. If you opted to inventory existing workloads, those will be onboarded shortly.

Add/Edit Huawei Cloud Modal Fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

NAME
 Internal name for the Cloud in |morpheus|
CODE
  Short code used for api and variables (Optional)
LOCATION
  Can be used to specify the location of the Cloud or add a description. (Optional)
VISIBILITY
 Determines Tenant visibility for the Cloud.
   * Private: Access to the Cloud is limited to the assigned Tenant (Master Tenant by default)
   * Public: Access to the Cloud can be configured for Tenants in their Tenant Role permissions.
TENANT
  Assigned Tenant when VISIBILITY is set to Private.
Enabled
  When unchecked, the cloud will not sync and is not accessible for provisioning actions.
IDENTITY API URL
  v2.0 or v3 Identity endpoint.
DOMAIN ID
  The DOMAIN ID field takes the "Account Name" as shown on the `Basic Information page <https://account-intl.huaweicloud.com/usercenter/?locale=en-us#/userindex/accountInfo>`_ of the account
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
  Select LB Type for Huawei LB syncing and creation
 Inventory Existing Instances
  Select for |morpheus| to discover and sync existing VM's
 Enable Hypervisor Console
  Hypervisor console support for openstack currently only supports novnc. Be sure the novnc proxy is configured properly in your openstack environment.

.. include:: /integration_guides/Clouds/advanced_options.rst
