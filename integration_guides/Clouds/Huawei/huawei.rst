Huawei Cloud
------------

Adding Huawei Cloud
^^^^^^^^^^^^^^^^^^^

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
