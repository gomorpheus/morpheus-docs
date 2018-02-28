Cloud Foundry
=============

Overview
--------

Creating a Cloud Foundry Cloud
------------------------------

From `Infrastructure -> Clouds`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure -> Clouds`
#. Select :guilabel:`+ ADD`
#. Select **CLOUD FOUNDRY** from the Clouds list
#. Select :guilabel:`NEXT`
#. Populate the following:

   Name
    Name of the Cloud in |morpheus|
   Location
    Description field for adding notes on the cloud, such as location.
   Visibility
    For setting cloud permissions in a multi-tenant environment. Not applicable in single tenant environments.
   API URL
     Cloud Foundry API Url
   CLIENT ID
     Typically ``cf``
   CLIENT SECRET
     Typically blank
   USERNAME
     Enter Username. If using an API Key, enter ``apikey`` for username, and the API Key as the password.
   PASSWORD
    Enter Password. If using an API Key, the API Key as the password.
   ORGANIZATION
    Select Organization. Dropdown populates upon successful authorization.

   .. include:: advanced_options.rst

#. Select :guilabel:`NEXT`
#. Select an existing or create a new Group to add the Cloud to. The Cloud can be added to additional Groups in a Groups `Clouds` tab.
#. Select :guilabel:`NEXT`
#. Review and then Select :guilabel:`COMPLETE`


From `Infrastructure -> Groups`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure -> Groups`
#. Select a Group
#. Select the `CLOUDS` tab
#. Scroll down to CLOUD FOUNDRY and select :guilabel:`+ ADD`
#. Populate the following:

   Name
    Name of the Cloud in |morpheus|
   Location
    Description field for adding notes on the cloud, such as location.
   Visibility
    For setting cloud permissions in a multi-tenant environment. Not applicable in single tenant environments.
   TENANT
    Select a Tenant if Visibility is set to Private to assign to Cloud to that Tenant. Multiple Tenants can be added by editing the cloud after creation.
   API URL
     Cloud Foundry API Url. Example ``https://api.cf.morpheusdata.com``
   CLIENT ID
     Typically ``cf``
   CLIENT SECRET
     Typically blank
   USERNAME
     Enter Username. If using an API Key, enter ``apikey`` for username, and the API Key as the password.
   PASSWORD
    Enter Password. If using an API Key, the API Key as the password.
   ORGANIZATION
    Select Organization. Dropdown populates upon successful authorization.

   .. include:: advanced_options.rst

#. Select :guilabel:`NEXT`
#. Review and then Select :guilabel:`COMPLETE`
