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
 Friendly internal name for the Cloud in |morpheus|
CODE
  Short code used for API and variables (optional)
LOCATION
  Can be used to specify the location of the Cloud or add a description. (optional)
VISIBILITY
 Determines Tenant visibility for the Cloud.
   * Private: Access to the Cloud is limited to the assigned Tenant (Master Tenant by default)
   * Public: Access to the Cloud can be configured for Tenants in their Tenant Role permissions
TENANT
  The assigned Tenant when VISIBILITY is set to Private
Enabled
  When unchecked, the cloud will not sync and is not accessible for provisioning actions.
IDENTITY API URL
  The v2 or v3 identity endpoint. See the integration steps above for more detail
DOMAIN ID
  The DOMAIN ID field takes the "Account Name" as shown on the `Basic Information page <https://account-intl.huaweicloud.com/usercenter/?locale=en-us#/userindex/accountInfo>`_ of the account. See the integration steps above for more detail
PROJECT
  The target project name. See the integration steps above for more detail
USERNAME
  The service account username. See the integration steps above for more detail
PASSWORD
  The integration service account password. See the integration steps above for more detail
IMAGE FORMAT
  Select QCOW2, RAW or VMDK image type
Inventory Existing Instances
  Select for |morpheus| to discover and sync existing VMs
Enable Hypervisor Console
  Hypervisor console support for openstack currently only supports novnc. Be sure the novnc proxy is configured properly in your openstack environment.

.. TIP:: When using the RAW image format, you can bypass the image conversion service within the cloud leading to quicker performance. Other image formats are converted to RAW format and back when performing various actions. Using the RAW format from the start will bypass these conversion steps.

Advanced Options
^^^^^^^^^^^^^^^^

BACKUP PROVIDER
  Select Internal Backups (Morpheus) or a Backup Integration
BACKUP TRANSFER STORE
  An OBS bucket for temporary storage and processing of backups
DOMAIN
  Specify a default domain for Instances provisioned to this Cloud
SCALE PRIORITY
  Only affects Docker Provisioning. Specifies the priority with which an Instance will scale into the Cloud. A lower priority number means this cloud integration will take scale precedence over other cloud integrations in the Group
APPLIANCE URL
  Alternate Appliance URL for scenarios when the default Appliance URL (configured in `administration > settings`) is not reachable or resolvable for Instances provisioned in this cloud. The Appliance URL is used for Agent install and reporting
TIME ZONE
  The time zone to be configured on provisioned VMs when necessary
DATACENTER ID
  Used for differentiating pricing among multiple datacenters. Leave blank unless prices are properly configured
NETWORK MODE
  Unmanaged or select Huawei-managed mode. When using Huawei managed network mode, |morpheus| will be able to create subnets, routers, security groups, and load balancers
LOCAL FIREWALL
  On or Off. Set to on in order to manage Host and VM firewall/IP Table rules (linux only)
SECURITY SERVER
  Field present but locked for this cloud integration
TRUST PROVIDER
  Select Internal to use |morpheus|-managed SSH keys and SSL certificates or choose an existing trust provider integration, such as Venafi
STORAGE MODE
  Single Disk, LVM or Clustered
REPLICATION PROVIDER
  Sets the default replication Provider for the Cloud. Select an existing replication provider integration
GUIDANCE
  Enable to collect guidance recommendations from |morpheus| for this cloud
DNS INTEGRATION
  Records for Instances provisioned in this Cloud will be added to selected DNS integration
SERVICE REGISTRY
  Services for Instances provisioned in this Cloud will be added to selected service registry integration
CONFIG MANAGEMENT
  Select a Chef, Salt, Ansible or Puppet integration to be used with this Cloud
CMDB
  Select a pre-existing CMDB integration (such as ServiceNOW) to automatically update when resources are provisioned into this Cloud
AGENT INSTALL MODE
  * SSH / WINRM / Guest Execution: |morpheus| will use SSH or WINRM for Agent install
  * Cloud Init / Unattend (when available): (DEFAULT) |morpheus| will utilize Cloud-Init or Cloudbase-Init for Agent install when provisioning images with Cloud-Init/Cloudbase-Init installed. |morpheus| will fall back on SSH or WINRM if cloud-init is not installed on the provisioned image. Morpheus will also add Agent installation to Windows unattend.xml data when performing guest customizations or utilizing syspreped images
API PROXY
  Field present but locked out for this Cloud integration

Provisioning Options
^^^^^^^^^^^^^^^^^^^^

PROXY
  Set a proxy for inbound communication from Instances to the |morpheus| Appliance. Proxies can be added in the `Infrastructure -> Networks -> Proxies` tab.
Bypass Proxy for Appliance URL
  Enable to bypass proxy settings (if added) for |morpheus| Agent communication to the Appliance URL.
USER DATA (LINUX)
  Add cloud-init user data. |morpheus| 4.1.0 and earlier assumes bash syntax. |morpheus| 4.1.1 and later supports all User Data formats. Refer to https://cloudinit.readthedocs.io/en/latest/topics/format.html for more information.
