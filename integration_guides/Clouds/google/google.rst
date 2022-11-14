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

.. gcp_guide_start_point

Requirements for Integration with |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To integrate |morpheus| with Google Cloud Platform, you will need the following. APIs are enabled in "APIs & Services" and must be enabled for all projects or the selected project (depending on your GCP Cloud integration settings). The next section contains more detailed steps for enabling API in the GCP web console.

* The Compute Engine API enabled
* The Cloud Resource Manager API enabled
* The Cloud Billing API
* The Identity and Access Management (IAM) API enabled
* The BigQuery API enabled
* The BigQuery Data Transfer API enabled
* The Kubernetes Engine API enabled (required to provision GKE clusters)
* Credentials for an IAM service account with Owner or Compute Admin role permissions
* The private key and client email for the service account

This integration guide goes through the process of configuring your account and obtaining the information necessary to integrate with |morpheus|. Continue to the next section for a detailed look at enabling the APIs mentioned above.

Enabling the Required APIs
^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to take full advantage of the |morpheus| integration with Google Cloud, a number of APIs must be enabled within the GCP web console. It's recommended that you enable all of the APIs listed in the preceding section regardless of the |morpheus| feature set you intend to use. This will ensure you do not run into problems down the road stemming from a lack of access which may take time to diagnose.

Log into the Google Cloud web console and navigate to the APIs and Services page. You may find this in the Quick access area of the welcome page or you can search for it as shown in the screenshot below.

.. image:: /images/integration_guides/clouds/gcp/apis.png

From the APIs and Services page, a list of enabled APIs and some details about your usage are shown. To enable new APIs, click :guilabel:`+ ENABLE APIS & SERVICES` near the top of the window. Now on the API library page, search for the API you wish to enable. Here I've searched for the Kubernetes Engine API.

.. image:: /images/integration_guides/clouds/gcp/apisearch.png

From the search results, click on the API you wish to enable to view its detail page. Click :guilabel:`ENABLE`. Once successfully enabled, the button will change to a :guilabel:`MANAGE` button. It may take a few moments for the API to be fully enabled. You may also be prompted to enable the Cloud Billing API or create an association with a Billing Account when enabling APIs. Go ahead and do so if prompted.

.. image:: /images/integration_guides/clouds/gcp/apienable.png

Repeat this process until all required APIs (listed in the previous section) are enabled.

Creating a Service Account
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. From anywhere in the GCP web console, search for "service accounts" in the global search bar at the top of the window
#. Click on the Service Accounts page (within the IAM & Admin stack)
#. A list of existing service accounts within the selected Project is shown (if any)
#. To create a new one, click :guilabel:`+ CREATE SERVICE ACCOUNT`

  .. image:: /images/integration_guides/clouds/gcp/3create_service_acct.png

3. Enter at least a name for your new service and click CREATE AND CONTINUE

  .. image:: /images/integration_guides/clouds/gcp/4config_service_acct.png

4. After creating the service account, you'll be prompted to set a role for the account. In order to fully integrate with |morpheus|, you must use an account in the Owner role or the Compute Admin role
5. Click CONTINUE

  .. image:: /images/integration_guides/clouds/gcp/5service_acct_role.png

6. Following creation of the service account, you'll be taken back to the list of existing service accounts

Generating Keys and Integrating with |morpheus|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. From the list of service accounts, click the ellipsis button (...) to the right of a selected account
#. Click "Manage Keys"

  .. image:: /images/integration_guides/clouds/gcp/6create_key.png

3. On the Keys page, click "Add Key" and then "Create New Key"
4. Select JSON format and click CREATE
5. A JSON-formatted document will be downloaded, this document contains the Project ID, private key, and client email values needed to complete the integration process in the next step

Add a GCP Cloud
^^^^^^^^^^^^^^^

.. Note:: The JSON-formatted document downloaded when creating a key for your service account contains all of the required values for completing the integration. Consult the above section on generating keys if needed.

#. Navigate to |InfClo|
#. Select :guilabel:`+ CREATE CLOUD`, select Google Cloud, and then click :guilabel:`NEXT`.
#. Enter the following into the Create Cloud modal:

   .. include:: /integration_guides/Clouds/base_options.rst

   **Details**

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

With configuration in the GCP console completed, we can now enable cost onboarding from the |morpheus| side. Add or edit an existing GCP Cloud (|InfClo|). Within the Advanced Options section, note the COSTING PROJECT and COSTING DATASET fields. When selecting a Project, associated datasets (if any) will automatically be loaded into the dropdown in the next field for selection. Additionally, the COSTING field should be set to "Sync Costing" rather than "Off". Recall from the previous paragraph that this is merely pointing to the Project that houses the appropriate dataset. If your GCP Cloud in |morpheus| is configured for all Projects, all costing data will be consumed for the Projects linked to the associated Billing Account (assuming those Projects have billing enabled). If the GCP Cloud in |morpheus| is scoped to just one Project, only billing data for that Project will be onboarded. For this reason, the selected Costing Project can be (but is not necessarily) the Project to which the |morpheus| Cloud is scoped.

.. image:: /images/integration_guides/clouds/gcp/costing3.png
  :width: 50%

.. gcp_guide_stop_point

Windows Images
^^^^^^^^^^^^^^

|morpheus| can add custom metatdata that will be injected into the unattend conf by GCP during provisioning. This is required for customizations including setting the Windows Administrator password during provisioning. GCP Windows Images must be syspreped using the ``GCESysprep`` command prior to image creation, and must have platform/os set on the Virtul Image record in |morpheus| after image sync for successful customization and Agent Installation.

GCP Windows Requirements
````````````````````````

- GCP Windows Images must be syspreped using the ``GCESysprep`` command prior to Image creation in GCP. Refer to `Googles "creating-windows-os-image" doc <https://cloud.google.com/compute/docs/instances/windows/creating-windows-os-image>`_.
- Once the Image is synced into Morpheus, the Platform (Windows, Windows 2016 etc) must be set on the |morpheus| Virtual Image record, otherwise linux is assumed and the metadata will not be generated correctly.
- The Global Windows "Administrator" password must be set in |morpheus| under ``/admin/provisioning/settings`` > Windows Settings > Administrator Password, or Administrator and password defined on the |morpheus| Virtual Image record.
- Be aware the unattend configuration during startup after sysprep delays causes a reboot and a prolonged finalization process during provisioning, and console/rdp may not be available during this time as windows is configuring.

.. note:: Some Google provided Windows Images have slow startups that cause the Morpheus Agent service to not start within the default 30 second service startup timeframe, including after initial reboot after sysprep/unattend configuration. This can be adjusted by running ``New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\" -Name "ServicesPipeTimeout" -PropertyType DWORD -Value 180000`` in powershell on the Windows Image.

.. important:: Failure to use a GCP Windows Image that has not been sysprepped using ``GCESysprep`` will cause Agent Installation, Automation, and Console issues as |morpheus| will not be able to set user credentials and authenticate.
