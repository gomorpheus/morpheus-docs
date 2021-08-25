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

.. include:: /integration_guides/Clouds/base_options.rst

Details
```````
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
Image Store
  Set an OBS bucket as a permanent store location for |morpheus| virtual images. Users are limited to uploading images of 2GB or less in size if an OBS bucket is not specified here
Inventory Existing Instances
  Select for |morpheus| to discover and sync existing VMs
Enable Hypervisor Console
  Hypervisor console support for openstack currently only supports novnc. Be sure the novnc proxy is configured properly in your openstack environment.

.. TIP:: When using the RAW image format, you can bypass the image conversion service within the cloud leading to quicker performance. Other image formats are converted to RAW format and back when performing various actions. Using the RAW format from the start will bypass these conversion steps.

.. include:: /integration_guides/Clouds/advanced_options.rst

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

Network and Router Creation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once a Huawei Cloud is integrated into |morpheus|, new network creation options become available. When adding a new network (Infrastructure > Networks > Networks Tab), a new type labeled "Huawei Private Network" is available when clicking :guilabel:`+ADD`. When the user creates this network construct in |morpheus|, a layer two subnet is created but it's not connected to a Virtual Private Cloud (VPC). This is by design as an Internet-routable network is not always desired. Continue on with this section after creating the network to also create a VPC (router).

Create a network
````````````````

#. Navigate to Infrastructure > Networks
#. Click on the Networks tab
#. Click :guilabel:`+ADD`
#. Select Huawei Private Network
#. Complete the modal based on requirements for the new network
#. Click :guilabel:`SAVE CHANGES`

Create a router
```````````````

#. Navigate to Infrastructure > Networks
#. Click on the Routers tab
#. Click :guilabel:`+ADD`
#. Select Huawei Router
#. Complete the modal based on requirements for the new router
#. Click :guilabel:`SAVE CHANGES`

When creating a router, it's helpful to note that the External Network is the floating IP network that has been assigned to the Huawei project. This network will grant your Instances their routes out to the Internet. The Internal Subnet can be a layer two subnet that you may have created in the previous step. In addition, multiple subnets can be added to the router (VPC) and the IP address on the subnet would be the router's internal IP address.
