.. _azure:

Azure (Public)
--------------

Overview
^^^^^^^^
Morpheus offers a complete Integration with Microsoft Azure including the following:

* Virtual Machine Sync, Create, Delete, Manage, RBAC, Tenant Permissions, Policies
* Resource Group Sync, Create, Delete, RBAC, Tenant Permissions
* Network Sync, Create, Delete, RBAC, Tenant Permissions
* Subnet Sync, Create, Delete, RBAC, Tenant Permissions
* Security Group Sync, Create, Delete, Tenant Permissions
* Security Group Rule Sync, Create, Delete, Tenant Permissions
* ARM Blueprints, Spec Templates, Deployment Logs Sync, Git/GitHub Integration
* MSSQL Service Sync, Create, Delete, Manage, RBAC, Tenant Permissions
* AKS Sync, Sync, Create, Delete, Manage, RBAC, Tenant Permissions
* Backup Create, Delete, Manage, RBAC, Policies
* Storage Sync, Create, Delete, Manage, Browse, RBAC, Tenant Permissions, Policies
* Marketplace Sync
* Private Image Sync & Upload
* Azure Marketplace Custom Library Item Support
* Remote Console (SSH & RDP)
* Lifecycle Management
* Availability Set Support
* Scale Set Sync, Create, Assign, Manage, Delete
* Azure Load Balancer Create, Assign, Manage, Delete, RBAC, Tenant Permissions
* Docker (VM) Cluster Sync, Create, Delete, Manage, RBAC, Tenant Permissions
* Kubernetes (VM) Cluster Sync, Create, Delete, Manage, RBAC, Tenant Permissions
* Service Plan Sync, Tenant Permissions, RBAC
* Pricing Sync RBAC, Tenant Permissions, Markup
* Costing Sync, Reporting, Invoicing
* Reservations Sync, Guidance Recommendations
* Azure Stack Support
* Tag Bi-Directional Sync, Creation, Deletion Policy Enforcement
* Cost Estimator
* Azure US Gov Support
* Azure China Support
* Azure Germany Support
* CSP Account Support

Requirements
^^^^^^^^^^^^

Morpheus Azure Integration requires Owner or Contributor access to subscription via App Registration. Adding an Azure Cloud or Clouds to |morpheus| will require the following:

* Azure Subscription ID
* Directory (tenant) ID
* Application (client) ID
* Application (client) Secret
* Application (client) must be Owner or Contributor of Subscription

CSP Accounts require the additional following input:

* CSP Directory (tenant) ID
* CSP Application (client) ID
* CSP Application (client) SECRET (Web App Key)

The |morpheus| appliance requires outbound HTTPS (443) access to the Azure endpoints. Depending on the type of cloud you choose when adding Azure, ensure the proper endpoints are allowed:

  **Global Azure Cloud**
    * https://management.core.windows.net (ServiceManagementUrl)
    * https://management.azure.com (ResourceManagerUrl)
    * https://login.microsoftonline.com (ActiveDirectoryAuthority)
  
  **US Gov Cloud**
    * https://management.core.usgovcloudapi.net (ServiceManagementUrl)
    * https://management.usgovcloudapi.net (ResourceManagerUrl)
    * https://login.microsoftonline.us (ActiveDirectoryAuthority)

  **Germany Cloud**
    * https://management.core.cloudapi.de (ServiceManagementUrl)
    * https://management.microsoftazure.de (ResourceManagerUrl)
    * https://login.microsoftonline.de (ActiveDirectoryAuthority)

  **China Cloud**
    * https://management.core.chinacloudapi.cn (ServiceManagementUrl)
    * https://management.chinacloudapi.cn (ResourceManagerUrl)
    * https://login.chinacloudapi.cn (ActiveDirectoryAuthority)

Credentials & Permissions
^^^^^^^^^^^^^^^^^^^^^^^^^

Morpheus authenticates with Azure via an App Registration with an Owner or Contributor Role on a Subscription. Use the steps below to create and collect the required credentials and assign the required permissions to integrate Azure with |morpheus|.

.. warning:: Using an App Registration (service principal) that has selective resource permissions and is not an Owner or Contributor of the Subscription is not supported and will cause failures/issues. Please confirm the App Registration you use to integrate Azure with Morpheus has Owner or Contributor permissions on the specified Subscription before contacting support.

Create an App Registration
``````````````````````````

If you do not have an existing Azure Active Directory App Registration, or you wish to use an new one for |morpheus|, you will need to create one.

#. Log into the Azure portal
#. Select "Azure Active Directory"
#. Select "App Registrations"
#. Select "New Registration"

   .. thumbnail:: /images/clouds/azure/Default_Directory_App_registrations_Microsoft_Azure.png



#. Next, give app a name, specify Web app / API for the type (default) and enter any url for the Sign-on URL:
#. Click Create and your new App Registration will be created.

   .. thumbnail:: /images/clouds/azure/Register_an_application_Microsoft_Azure.png


Now that we have (or already had) our App Registration, we will gather the credentials required for the |morpheus| Azure integration.

.. _azure_ids:

Copy Directory (tenant) and Application (client) IDs
````````````````````````````````````````````````````

The App Registration Directory (tenant) and Application (client) ID are required for the |morpheus| Azure integration. Both can be found in the overview section of the App Registration.

#. Go to the Overview section of your App Registration
#. Copy the Directory (tenant) ID
#. Store/Paste for use as the Tenant ID when Adding your Azure cloud in |morpheus|
#. Copy the Application (client) ID
#. Store/Paste for use as the Client ID when Adding your Azure cloud in |morpheus|

   .. thumbnail:: /images/clouds/azure/morpheusAppReg_Microsoft_Azure.png

.. _azure_secret:

Generate a Client Secret
````````````````````````
While still in your App Registration:

#. Select Certificates & secrets in the Manage Section
#. Select ``+ New client secret``

   .. thumbnail:: /images/clouds/azure/morpheusAppReg_Certificates_secrets_Microsoft_Azure.png


#. The "Add a client secret" modal will come up
#. Add a description to help identify the secret in the future
#. Select a duration
#. Select :guilabel:`Add`

   .. thumbnail::  /images/clouds/azure/morpheusAppReg_Certificates_secrets_Add.png


#. Copy the newly generated Client Secret Value. It is important to copy the Client Secret Value now as it will not be displayed/available

   .. IMPORTANT:: Copy the key value before continuing as it will not be displayed/available again.

   .. thumbnail::  /images/clouds/azure/morpheusAppReg_Certificates_secrets_Copy.png

#. Store/Paste for use as the Client Secret when Adding your Azure cloud in |morpheus|

You now have 3 or the 4 credentials required for |morpheus| Azure cloud integration. The last credential required is the Azure Subscription ID.

Subscription ID
```````````````

To get the Azure Subscription ID:

#. Navigate to the main Subscriptions section. One way is to search for "Subscriptions" and select Subscriptions in the search results

   .. thumbnail:: /images/clouds/azure/azuresubscriptionssearch.png

#. In the main "Subscriptions" section, copy the Subscription ID

   .. thumbnail:: /images/clouds/azure/Subscriptions_Microsoft_Azure.png


#. Store/Paste for use as the Subscription ID when Adding your Azure cloud in |morpheus|

Make App Registration owner or contributor of Subscription
``````````````````````````````````````````````````````````

The App Registration created/used needs to be an owner of the Azure Subscription used for the |morpheus| cloud integration. If lesser permissions are given or permissions are assigned at individual resource levels, |morpheus| will not be able to properly inventory/sync, create and/or remove resources.

#. In the main "Subscriptions" section in Azure, select the Subscription
#. In the Subscription pane, select "Access Control (IAM)"
#. Either Click "+ Add", and the "Add Role Assignment", or simply select "Add a role assignment"

   .. thumbnail:: /images/clouds/azure/Azure_subscription_1_Access_control_IAM_Microsoft_Azure.png


#. In the right pane, select "Owner" or "Contributor" Role type
#. Search for the name of the App Registration used for the |morpheus| integration
#. Select the App Registration in the search results
#. Select "Save"

   .. thumbnail:: /images/clouds/azure/Add_role_assignment_save.png


You now have the required Credentials and permissions to add an Azure Cloud Integration(s) into |morpheus|.

Add an Azure Cloud Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To add a new Azure Cloud integration into |morpheus| using the credentials created/collected from the previous section, perform the following:

#. In |morpheus|, navigate to ``Infrastructure > Clouds`` and select :guilabel:`+ ADD`

   .. image:: /images/clouds/azure/Clouds_Morpheus_Add.png

#. Select "AZURE (PUBLIC)" from the Cloud Types list and click :guilabel:`NEXT`

   .. image:: /images/clouds/azure/Clouds_Morpheus.png


#. Populate the Following

   .. include:: /integration_guides/Clouds/base_options.rst

   **Details**

   CLOUD TYPE
     - Standard (Azure Cloud)
     - US Gov (Azure US Government)
     - German (Azure German Cloud)
     - China (Azure China Cloud)
   SUBSCRIPTION ID
     The target Azure Subscription ID obtained from the previous section
   TENANT ID
     The Directory (tenant) ID obtained from the previous section
   CLIENT ID
     The Application (client) ID obtained from the previous section
   CLIENT SECRET
     The Application (client) Secret obtained from the previous section
   LOCATION
     Once valid credentials are populate above and |morpheus| is able to successfully authenticate with Azure, the available locations/regions will populate.
   RESOURCE GROUP
     - Select "All" to scope the Cloud to all available Resource Groups in the specified location/region.
     - Select a single Resource Group to limit |morpheus| resource creation, selection and discovery to just this Resource Group.
   INVENTORY EXISTING INSTANCES
     Check to enable discovery/inventory of existing VM's in the scoped Region and Resource Group(s)
   INVENTORY LEVEL
     Basic
      |morpheus| will sync information on all resources in the selected Resource Group(s), including Name, IP Addresses, Platform Type, Power Status, and overall resources sizing for Storage, CPU and RAM, every 5 minutes. Inventoried VM's will appear as Unmanaged VM's.
     Full (API Heavy)
      In addition to the information synced from Basic Inventory level, |morpheus| will gather Resource Utilization metrics for Memory, Storage and CPU utilization per VM when available.
     Off
      Existing VM's will not be inventoried
   ACCOUNT TYPE
     Standard, EA or CSP

     .. note:: For CSP Accounts, also enter CSP TENANT ID, CSP CLIENT ID and CSP CLIENT SECRET in the Advanced Options section. In order to enable cost sync for CSP accounts, the "CSP CUSTOMER" checkbox must be marked and "COSTING" should be set to "Costing" rather than "Costing and Reservations".

     For the CSP Client Secret, enter the Web App Key rather than the Native App Key. This should be accessed from the Microsoft Partner Center rather than the Azure web console. If this is not, Plans may sync but Price Sets and Prices would not.

     .. image:: /images/clouds/azure/addAzureCloudMorpheusS1.png

   .. include:: /integration_guides/Clouds/advanced_options.rst

   AZURE COSTING MODE
     Standard, CSP, or Azure Plan

     Example configurations but choose what is applicable to the tenant:

     .. list-table:: **Example Azure Costing Configurations**
        :widths: auto
        :header-rows: 1

        * - Account Type
          - Azure Costing Mode
          - Notes
        * - Standard (Pay as you go)
          - Standard
          - 
        * - EA (Enterprise Agreement)
          - Standard
          - 
        * - CSP (Cloud Solution Provider)
          - CSP
          - CSP Tenant, ID, Client ID, and Client Secret required
        * - CSP (Cloud Solution Provider)
          - Azure Plan (Microsoft Customer Agreement)
          - CSP Tenant, ID, Client ID, and Client Secret required on the primary cloud

#. Once done configuring the Cloud, select :guilabel:`NEXT`. NOTE all specified values except the Subscription ID can be changes after the Cloud is created.

#. Next select an existing Group to add the Azure Cloud to, or create a new Group, then select :guilabel:`NEXT`

   .. image:: /images/clouds/azure/Clouds_MorpheusAddGroup.png


#. Review the configuration and then select :guilabel:`COMPLETE`

   .. image:: /images/clouds/azure/Clouds_MorpheusComplete.png


Your new Azure Cloud integration will be created and begin to sync.

.. note:: The initial sync of an Azure Cloud can take some time due to Marketplace data sync.

.. image:: /images/clouds/azure/Clouds_MorpheusNewCloudAdded.png
