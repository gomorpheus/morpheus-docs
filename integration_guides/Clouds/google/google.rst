Google
-------

Requirements
^^^^^^^^^^^^

* IAM Service Account with `Owner` or `Compute Admin` Role permissions
* `project_id`, `private_key` and `client_email` for the Service Account
* `Compute Engine API` enabled in GCP `API's and Services`

.. IMAGE:: /images/integration_guides/clouds/Google-API-Compute


Features
^^^^^^^^^
* Provisioning Virtual Machines
* Network tagging
* Private and Local Images
* Google VM Snapshots
* Brownfield Inventory
* Costing
* Right sizing

Add a Google Cloud
^^^^^^^^^^^^^^^^^^^

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
