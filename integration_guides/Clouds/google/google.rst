.. _Google Cloud:

Google Cloud
------------

Requirements
^^^^^^^^^^^^

* IAM Service Account with `Owner` or `Compute Admin` Role permissions
* `project_id`, `private_key` and `client_email` for the Service Account
* `Compute Engine API` enabled in GCP `API's and Services`

.. IMAGE:: /images/integration_guides/clouds/Google-API-Compute.png

Features
^^^^^^^^^
* Provisioning Virtual Machines
* Network tagging
* Private and Local Images
* Google VM Snapshots
* Brownfield Inventory
* Costing
* Right sizing
* Shared Network Support

<<<<<<< HEAD
=======
Requirements for Integration with |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To integrate |morpheus| with Google Cloud Platform, you will need the following:

* The Compute Engine API enabled in GCP "APIs & Services"
* Credentials for an IAM service account with Owner or Compute Admin role permissions
* The Project ID, private key, and client email for the service account

This integration guide goes through the process of configuring your account and obtaining the information necessary to integrate with |morpheus|.

Enabling the Compute Engine API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Log into the Google Cloud Platform web console
#. Hover over the "APIs & Services" menu and click on Dashboard
#. Click :guilabel:`+ ENABLE APIS AND SERVICES`

  .. image:: /images/integration_guides/clouds/gcp/1enable_apis.png

4. In the search bar, search for "Compute Engine API"

  .. image:: /images/integration_guides/clouds/gcp/2search_apis.png

5. Select "Compute Engine API" and click :guilabel:`ENABLE`. It may take a few moments for the API to be fully enabled

.. Note:: If the button is labeled MANAGE rather than ENABLE, the API is already enabled.

Creating a Service Account
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. From the landing page of the GCP web console, hover over the "IAM & Admin" menu and click on "Service Accounts"
#. Click :guilabel:`+ CREATE SERVICE ACCOUNT`

  .. image:: /images/integration_guides/clouds/gcp/3create_service_acct.png

3. Enter at least a name for your new service and click CREATE

  .. image:: /images/integration_guides/clouds/gcp/4config_service_acct.png

4. After creating the service account, you'll be prompted to set a role for the account. In order to fully integrate with |morpheus|, you must use an account in the Owner role or the Compute Admin role
5. Click CONTINUE

  .. image:: /images/integration_guides/clouds/gcp/5service_acct_role.png

6. Following creation of the service account, you'll be taken back to the list of existing service accounts

Generating Keys and Integrating with |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. From the list of service accounts, click the ellipsis button (...)
#. Click "Create Key"

  .. image:: /images/integration_guides/clouds/gcp/6create_key.png

3. Select JSON format and click CREATE
4. A JSON-formatted document will be downloaded, this document contains the Project ID, private key, and client email values needed to complete the integration process in the next step

>>>>>>> f1f4141c... Fix list numbering in GCP integration guide
Add a Google Cloud Cloud
^^^^^^^^^^^^^^^^^^^^^^^^

.. TIP:: All of the required Google Cloud credentials can be found in the .json file created when generating a key for a Google Cloud service account.

#. Navigate to Infrastructure -> Clouds
#. Select :guilabel:`+ CREATE CLOUD`, select Google Cloud, and then click :guilabel:`Next`.
#. Enter the following into the Create Cloud modal:

   Name
    Name of the Cloud in |morpheus|
   Location
    Description field for adding notes on the cloud, such as location.
   Visibility
    For setting cloud permissions in a multi-tenant environment. Not applicable in single tenant environments.
   Project ID
    Google Cloud Project ID
   Private Key
    Service Account Private key, beginning with `-----BEGIN PRIVATE KEY-----\` and ending with `-----END PRIVATE KEY-----`
   Client Email
    Service Account Client Email. ex: `morpheus@morpheus.iam.gserviceaccount.com`
   Region
    Regions will auto-populate upon successful authentication with the above credentials. Select appropriate region for this Cloud.
   Inventory Existing Instances
    If enabled, existing Google Instances will be inventoried and appear as unmanaged Virtual Machines in |morpheus| .

.. NOTE:: |morpheus| scopes clouds to single regions. Multiple clouds can be added for multi-region support, and then optionally added to the same group.

<<<<<<< HEAD
The Cloud can now be added to a Group or configured with additional Advanced options.

.. include:: /integration_guides/Clouds/advanced_options.rst

Finally, add Google Cloud to an existing Group or create a new Group, and you have now integrated |morpheus| with Google Cloud!
=======
If advanced options are not needed, click :guilabel:`NEXT` to advance to the Group selection page. Otherwise, continue on with this guide and review advanced or provisioning options.

.. include:: /integration_guides/Clouds/advanced_options.rst

After reviewing all options, click :guilabel:`NEXT` to advance to the Group selection page. Following Group selection, click :guilabel:`COMPLETE` to finish the integration process. If you've opted to inventory existing Instances, they will be viewable in |morpheus| shortly. At this point, you are ready to provision new resources in Google Cloud Platform as needed!
>>>>>>> f1f4141c... Fix list numbering in GCP integration guide

.. IMPORTANT:: If you experience difficulties adding a GCP Cloud, ensure you have met all the Requirements above, and have logged into Google Cloud and navigated to the Compute Engine sections as it will not be initialized until navigated to upon Google Cloud account creation.

Windows Images
^^^^^^^^^^^^^^

|morpheus| can add custom metatdata that will be injected into the unattend conf by GCP during provisioning. This is required for customizations including setting the Windows Administrator password during provisioning. GCP Windows Images must be syspreped using the ``GCESysprep`` command prior to image creation, and must have platform/os set on the Virtul Image record in |morpheus| after image sync for successful customization and Agent Installation.

GCP Windows Requirements
````````````````````````

- GCP Windows Images must be syspreped using the ``GCESysprep`` command prior to Image creation in GCP. Refer to `Googles "creating-windows-os-image" doc <https://cloud.google.com/compute/docs/instances/windows/creating-windows-os-image>`_.
- Once the Image is synced into Morpheus, the Platform (Windows, Windows 2016 etc) must be set on the |morpheus| Virtual Image record, otherwise linux is assumed and the metadata will not be generated correctly.
- The Global Windows "Administrator" password must be set in |morpheus| under ``/admin/provisioning/settings`` -> Windows Settings -> Administrator Password, or Administrator and password defined on the |morpheus| Virtual Image record.
- Be aware the unattend configuration during startup after sysprep delays causes a reboot and a prolonged finalization process during provisioning, and console/rdp may not be available during this time as windows is configuring.

.. note:: Some Google provided Windows Images have slow startups that cause the Morpheus Agent service to not start within the default 30 second service startup timeframe, including after initial reboot after sysprep/unattend configuration. This can be adjusted by running ``New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\" -Name "ServicesPipeTimeout" -PropertyType DWORD -Value 180000`` in powershell on the Windows Image.

.. important:: Failure to use a GCP Windows Image that has not been sysprepped using ``GCESysprep`` will cause Agent Installation, Automation, and Console issues as |morpheus| will not be able to set user credentials and authenticate.
