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
````````````````

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
````````````````````

PROXY
  Field present but locked for this Cloud inegration
Bypass Proxy for Appliance URL
  Enable to bypass proxy settings (if added) for |morpheus| Agent communication to the Appliance URL. It is currently not possible to set a proxy for Huawei Cloud integrations
USER DATA (LINUX)
  Add cloud-init user data. |morpheus| 4.1.0 and earlier assumes bash syntax. |morpheus| 4.1.1 and later supports all user data formats. Refer to `cloud-init documentation <https://cloudinit.readthedocs.io/en/latest/topics/format.html>`_ for more information

Huawei Scalable File Service (SFS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The |morpheus| integration with Huawei Cloud includes the capability to work with Huawei Scalable File Service (SFS). SFS is shared file storage hosted on Huawei Cloud. By integrating |morpheus| with Huawei Cloud you can discover, create, manage, and delete SFS servers, as well as view and work with the file shares and files contained therein.

SFS Server Discovery and Management
```````````````````````````````````

On integrating Huawei Cloud with |morpheus|, SFS servers and file shares are discovered automatically after a short time. The server(s) can be viewed in Infrastructure > Storage > Servers. By viewing the server detail page and clicking :guilabel:`EDIT`, the storage server can be scoped as needed. Administrators can choose to scope to other Huawei Cloud integrations (if more than one relevant integration currently exists), select from synced availability zones, and scope the storage server to specific Tenants if desired.

.. image:: /images/integration_guides/clouds/huawei/sfs/1editServer.png

Additionally, Huawei SFS servers can be created from the storage server list page (Infrastructure > Storage > Servers) directly in |morpheus|. Click :guilabel:`+ ADD` to begin and set the storage server type value to "Huawei SFS". Just like with existing synced SFS servers, those created from |morpheus| can be scoped as needed.

.. image:: /images/integration_guides/clouds/huawei/sfs/2addServer.png

SFS File Share Discovery and Management
```````````````````````````````````````

Discovered file shares will appear among other file shares synced with |morpheus| in Infrastructure > Storage > File Shares. Depending on the number of cloud integrations in your |morpheus| appliance and the number of cloud integrations available to your user account, this list may be quite large. Using the search bar on this page, we can narrow down the list to file shares displayed to those whose names match the search terms.

.. image:: /images/integration_guides/clouds/huawei/sfs/3shareList.png

We can drill into individual file shares by clicking on their hyperlinked name in the list of all integrated file shares. From the file share detail page, a list of files will appear on the files tab. Begin the process of adding a new file by clicking :guilabel:`+ ADD`. The Access tab on the file shares detail page allows users to view and manage ACL rules.

.. NOTE:: A "Failed to load files from storage provider" is present when the |morpheus| appliance doesn't have access to the file share.

New Huawei SFS file shares can be created directly in |morpheus|. From the file shares list page, get started by clicking :guilabel:`+ ADD`. Select the type "Huawei SFS Share". Set the storage service field to a pre-existing Huawei SFS server. A friendly name for the file share in |morpheus| and selecting from synced availability zones are required fields.

.. image:: /images/integration_guides/clouds/huawei/sfs/4addShare.png

Huawei Object Storage Service (OBS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The |morpheus| integration with Huawei Cloud also supports Object Storage Service (OBS). |morpheus| will automatically onboard existing OBS servers and buckets shortly after completing the cloud integration. Before you can add a new OBS server from |morpheus|, you must know or generate a key and secret value from the Huawei console and must provide a Huawei OBS API endpoint.

Generate a Key and Secret
`````````````````````````

From the Huawei web console, log into the account used to integrate Huawei Cloud with |morpheus|. Hover over your account name in the upper-right corner of the application window and click "My Credentials". Select "Access Keys" from the left-hand sidebar. To create a new key, click :guilabel:`+ Create Access Key`. Complete the two-factor authentication steps in the box that appears.

.. image:: /images/integration_guides/clouds/huawei/obs/1createKey.png

Once the key is generated, download or record the key and store it in a safe location. The key will not be viewable or available for download again after this point.

Create OBS Server in |morpheus|
```````````````````````````````

With the key and secret value in hand from the previous section, navigate to Infrastructure > Storage > Servers. Click :guilabel:`+ ADD`. On changing the server type to Huawei OBS, you will see the fields for the access key and the secret key. OBS API endpoints can be found in `Huawei endpoint documentation <https://developer.huaweicloud.com/en-us/endpoint>`_. Include those three values in the Create Server modal along with a friendly name for use in |morpheus| UI. Just like with SFS objects, we can choose to scope the server to all or specific Tenants at this time.

.. image:: /images/integration_guides/clouds/huawei/obs/2addObsServer.png

Create Huawei OBS Bucket
````````````````````````

With an OBS server onboarded or created in |morpheus|, you're able to create and manage Huawei OBS buckets as needed. To create a new bucket, navigate to Infrastructure > Storage > Buckets. Click :guilabel:`+ ADD` and select "Huawei OBS Bucket". The following fields are required when creating a Huawei OBS bucket:

- **NAME**: A friendly name for use in |morpheus| UI
- **STORAGE SERVICE**: Choose the OBS server to associate the new bucket with
- **BUCKET NAME**: The name of the bucket in Huawei Cloud, this must be unique
- **STORAGE CLASS**: If needed, view the `discussion of storage classes <https://support.huaweicloud.com/en-us/eu-west-0-usermanual-obs/en-us_topic_0050937852.html>`_ in Huawei support documentation
- **BUCKET ACL**: Public Read, Public Read/Write, or Private
- **BUCKET POLICY**: Public Read, Public Read/Write, or Private
- **STORAGE QUOTA**: Set to 0 for no quota

Once finished, click :guilabel:`SAVE CHANGES`

.. image:: /images/integration_guides/clouds/huawei/obs/3createBucket.png
