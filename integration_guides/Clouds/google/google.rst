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

The Cloud can now be added to a Group or configured with additional Advanced options.

.. include:: /integration_guides/Clouds/advanced_options.rst

Finally, add Google Cloud to an existing Group or create a new Group, and you have now integrated |morpheus| with Google Cloud!

.. IMPORTANT:: If you experience difficulties adding a GCP Cloud, ensure you have met all the Requirements above, and have logged into Google Cloud and navigated to the Compute Engine sections as it will not be initialized until navigated to upon Google Cloud account creation.

Windows Images
^^^^^^^^^^^^^^

|morpheus| can add custom metatdata that will be injected into the unattend conf by GCP during provisioning. This is required for customizations including setting the Windows Administrator password during provisioning. GCP Windows Images must be syspreped using the ``GCESysprep`` command prior to image creation, and must have platform/os set on the Virtul Image record in |morphues| after image sync for successful customization and Agent Installation.

GCP Windows Requirements
````````````````````````

- GCP Windows Images must be syspreped using the ``GCESysprep`` command prior to Image creation in GCP. Refer to `Googles "creating-windows-os-image" doc <https://cloud.google.com/compute/docs/instances/windows/creating-windows-os-image>`_.
- Once the Image is synced into Morpheus, the Platform (Windows, Windows 2016 etc) must be set on the |morphues| Virtual Image record, otherwise linux is assumed and the metadata will not be generated correctly.
- The Global Windows "Administrator" password must be set in |morphues| under ``/admin/provisioning/settings`` -> Windows Settings -> Administrator Password, or Administrator and password defined on the |morpheus| Virtual Image record.
- Be aware the unattend configuration during startup after sysprep delays causes a reboot and a prolonged finalization process during provisioning, and console/rdp may not be available during this time as windows is configuring.

.. note:: Some Google provided Windows Images have slow startups that cause the Morpheus Agent service to not start within the default 30 second service startup timeframe, including after initial reboot after sysprep/unattend configuration. This can be adjusted by running ``New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\" -Name "ServicesPipeTimeout" -PropertyType DWORD -Value 180000`` in powershell on the Windows Image.

.. important:: Failure to use a GCP Windows Image that has not been sysprepped using ``GCESysprep`` will cause Agent Installation, Automation, and Console issues as |morpheus| will not be able to set user credentials and authenticate.
