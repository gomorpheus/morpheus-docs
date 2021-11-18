.. _Google Cloud:

Google Cloud Platform (GCP)
---------------------------

Integration Features
^^^^^^^^^^^^^^^^^^^^
* Provisioning Virtual Machines
* Network tagging
* Private and Local Images
* Google VM Snapshots
* Brownfield Inventory
* Costing
* Right-sizing
* Shared Network Support

Requirements for Integration with |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To integrate |morpheus| with Google Cloud Platform, you will need the following. APIs are enabled in "APIs & Services" and must be enabled for all projects or the selected project (depending on your GCP Cloud integration settings):

* The Compute Engine API enabled
* The Cloud Resource Manager API enabled
* The Cloud Billing API
* The Identity and Access Management (IAM) API enabled
* The BigQuery API enabled
* The BigQuery Data Transfer API enabled
* The Kubernetes Engine API enabled (required to provision GKE clusters)
* Credentials for an IAM service account with Owner or Compute Admin role permissions
* The private key and client email for the service account

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

  .. NOTE:: If the button is labeled MANAGE rather than ENABLE, the API is already enabled. When enabling Compute Engine API, you may be prompted to also enable Cloud Billin API. It's also required this API is enabled so go ahead and enable it at this point and you won't have to do so later.

6. Head back to the API library and search for "Cloud Resource Manager API"
7. Select "Cloud Resource Manager API" and click :guilabel:`ENABLE`. It may take a few moments for the API to be fully enabled
8. If you haven't already enabled Cloud Billing API, head back to the API library and search for "Cloud Billing API"
9. Select "Cloud Billing API" and click :guilabel:`ENABLE`. It may take a few moments for the API to be fully enabled

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
#. Click "Manage Keys"

  .. image:: /images/integration_guides/clouds/gcp/6create_key.png

3. On the Keys page, click "Add Key" and then "Create New Key"
4. Select JSON format and click CREATE
5. A JSON-formatted document will be downloaded, this document contains the Project ID, private key, and client email values needed to complete the integration process in the next step

Add a GCP Cloud
^^^^^^^^^^^^^^^

.. Note:: The JSON-formatted document downloaded when creating a key for your service account contains all of the required values for completing the integration. Consult the above section on generating keys if needed.

#. Navigate to Infrastructure > Clouds
#. Select :guilabel:`+ CREATE CLOUD`, select Google Cloud, and then click :guilabel:`NEXT`.
#. Enter the following into the Create Cloud modal:

   .. include:: /integration_guides/Clouds/base_options.rst

   Details
   ```````
   PRIVATE KEY
    The service account private key. Paste in the entire value between (but not including) the quotation marks in your downloaded JSON document, formatted like the following example: ``-----BEGIN PRIVATE KEY-----(your_key)-----END PRIVATE KEY-----``
   CLIENT EMAIL
    The service account client email, ex: `morpheus@morpheus.iam.gserviceaccount.com`
   PROJECT ID
    Projects will auto-populate upon successful entry of the private key and client email. You can opt to scope the GCP integration to a single Project or select "All" to instead select the Project from the Resource Pool dropdown at provision time
   REGION
    Regions will auto-populate upon successful entry of the private key and client email. Select the appropriate region for this Cloud, if applicable. You can also opt to scope the GCP integration to all regions to allow users to select from any region at provision time
   INVENTORY EXISTING INSTANCES
    If checked, existing GCP resources will be inventoried and appear as unmanaged virtual machines in |morpheus|.

   If advanced options are not needed, click :guilabel:`NEXT` to advance to the Group selection page. Otherwise, continue on with this guide and review advanced or provisioning options.

   .. include:: /integration_guides/Clouds/advanced_options.rst

#. After reviewing all options, click :guilabel:`NEXT` to advance to the Group selection page. Following Group selection, click :guilabel:`COMPLETE` to finish the integration process. If you've opted to inventory existing Instances, they will be viewable in |morpheus| shortly. At this point, you are ready to provision new resources in Google Cloud Platform as needed!

.. IMPORTANT:: If you experience difficulties adding a GCP Cloud, review the above guide and ensure you've met all requirements for completing the integration. For example, if the Compute Engine API is not enabled, |morpheus| will not accept credentials entered on the Create Cloud modal. If you repeatedly run into problems completing the integration process, review the above guide in its entirely and double check that each step is completed and your account meets all configuration requirements.

Create a GCP Project
^^^^^^^^^^^^^^^^^^^^

On initial integration, |morpheus| will sync Projects and allow you to scope the integration to a specific Project or to scope the integration to all Projects. As time goes on, additional Projects are continually synced and can be managed from within the Resources tab on the Cloud detail page (Infrastructure > Clouds > Selected GCP Cloud). Within the Resources tab, users can edit some Project settings as well as delete Projects if needed.

To create a new GCP Project:

#. Click :guilabel:`+ ADD RESOURCE POOL`
#. Enter a name value for the new Project
#. Mark the "DEFAULT" box if you'd prefer newly provisioned Instances default to the new Project
#. Enter a Project ID and ensure it meets the listed validation requirements
#. Set a Parent value if the new Project should exist underneath a parent organization
#. Finally, select a billing account
#. Click :guilabel:`SAVE CHANGES`

After a few minutes, the new Project will be ready on the GCP side and |morpheus| will be ready to provision new resources into it.

Enabling Live Costing for GCP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GCP costing is done at the Billing Account level. Each Billing Account can be linked to one or more GCP Projects. All projects which are linked to the Billing Account will have their costing data available to |morpheus| but if the GCP Cloud has been scoped to only one Project, |morpheus| will ingest costing data only for that Project. Users can view the Billing Account linked to a particular project by clicking on the hamburger menu (main menu button in the far upper-left of the console window) and selecting billing. A pop-up window will give users the option to navigate to the Billing Account which is linked to the currently-selected Project.

.. image:: /images/integration_guides/clouds/gcp/costing1.png

Within the Billing Account, Standard Usage Cost must be enabled for |morpheus| to access costing data. From the page for the appropriate Billing Account, click on Billing Export and then click "Edit Settings" under the "Standard usage cost heading". Specify a project and create a dataset or specify an existing one. In doing this, you're specifying a location for the dataset *which will be for the entire billing account and not just for the Project the dataset resides in.*

.. image:: /images/integration_guides/clouds/gcp/costing2.png

With configuration in the GCP console completed, we can now enable cost onboarding from the |morpheus| side. Add or edit an existing GCP Cloud (Infrastructure > Clouds). Within the Advanced Options section, note the COSTING PROJECT and COSTING DATASET fields. When selecting a Project, associated datasets (if any) will automatically be loaded into the dropdown in the next field for selection. Additionally, the COSTING field should be set to "Sync Costing" rather than "Off". Recall from the previous paragraph that this is merely pointing to the Project that houses the appropriate dataset. If your GCP Cloud in |morpheus| is configured for all Projects, all costing data will be consumed for the Projects linked to the associated Billing Account (assuming those Projects have billing enabled). If the GCP Cloud in |morpheus| is scoped to just one Project, only billing data for that Project will be onboarded. For this reason, the selected Costing Project can be (but is not necessarily) the Project to which the |morpheus| Cloud is scoped.

.. image:: /images/integration_guides/clouds/gcp/costing3.png
  :width: 50%

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
