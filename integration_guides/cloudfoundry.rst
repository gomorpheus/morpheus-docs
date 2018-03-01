Cloud Foundry
=============

Configuration
-------------

Adding PCF Cloud From `Infrastructure -> Clouds`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

#. Select :guilabel:`NEXT`
   .. include:: advanced_options.rst

#. Select :guilabel:`NEXT`
#. Select an existing or create a new Group to add the Cloud to. The Cloud can be added to additional Groups in a Groups `Clouds` tab.
#. Select :guilabel:`NEXT`
#. Review and then Select :guilabel:`COMPLETE`


Adding PCF Cloud From `Infrastructure -> Groups`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Provisioning
------------

|morpheus| automatically seeds MySQL, Redis and RabbitMQ PCF Instance Types, as well as a generic Cloud Foundry Instance Type that will create a shell app used in conjunction with deployments. PCF Marketplace items can also be easily added to the Provisioning Library in the Cloud detail view Marketplace tab. The Marketplace item will be added to the selected Instance Type and available when selecting the Cloud Foundry Cloud during Instance or App Template creation.

Adding Marketplace Items
^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure -> Clouds` and select your Cloud Foundry Cloud
#. Select the MARKETPLACE tab
#. Select :guilabel:`+ ADD MARKETPLACE ITEM`
#. Select the |morpheus| Instance Type to add the Marketplace Item to.
#. Enter version
#. Search for and select Marketplace Item
#. Select :guilabel:`SAVE CHANGES`

A Node Type and layout will be created in the ``Provisioning -> Library`` section and the layout will be automatically added to the Instance Type selected when adding the Marketplace Item.

Provisioning Instances
^^^^^^^^^^^^^^^^^^^^^^

Seeded and Marketplace Items
............................

|morpheus| automatically seeds MySQL, Redis and RabbitMQ PCF Instance Types, and PCF Marketplace items can also be easily added to the Provisioning Library in the Cloud detail view Marketplace tab. The Marketplace item will be added to the selected Instance Type and available when selecting the Cloud Foundry Cloud during Instance or App Template creation.

#. Navigate to `Provisioning -> Instances` and select an Instance Type with a Cloud Foundry layout (MySQL, Redis and RabbitMQ plus Marketplace additions)
#. Select :guilabel:`NEXT`
#. Select a Group and PCF Cloud
#. Add an Instance Name
#. Optionally select and Environment Tag and/or add a custom Tag
#. Select :guilabel:`NEXT`
#. Select Version and Instance Configuration for a Cloud Foundry layout, ex: `Cloud Foundry MySQL`
#. Select a Plan and available options for the Plan, or use the custom Plan
#. Select a Space to add the Instance to
#. Optionally configure advanced options
#. Select :guilabel:`NEXT`
#. Optionally configure Automation options
#. Select :guilabel:`NEXT`
#. Select :guilabel:`COMPLETE`

.. NOTE:: Compute, Memory, and CPU stats will be pulled, and a Cloud Foundry monitoring health check will be automatically configured for the instance.

Cloud Foundry App Instance Type
...............................

The Cloud Foundry App Instance Type is used in conjunction with deployments. Users do not have to pick deployment when creating a Cloud Foundry App Instance Type, but then Instance will only be a shell of a Cloud Foundry Application.

When using a deployment, |morpheus| will pull down the repo and deploy just like the Cloud Foundry cli, parse the manifest, ignore fields such as memory and disk size which is dictated by the selected plan, and pull down files from path and push to the Instance. Other fields are utilized such as routes, however if services are specified in the manifest, |morpheus| assumes they are already created with matching names. |morpheus| app templates can be created to deploy services used in a manifest, and the service names in the manifest will be overwritten by the Morpheus provisioned service names. Multiple services can be used and wired up by Morpheus.

.. IMPORTANT:: Add Deployments in ``Provisioning -> Deployments`` to be used when provisioning a Cloud Foundry App Instance Type.

Provision a Cloud Foundry App Instance Type

.. NOTE:: Minimal options are outlined below.

#. Navigate to `Provisioning -> Instances` and select the `Cloud Foundry App` Instance Type
#. Select :guilabel:`NEXT`
#. Select a Group and PCF Cloud
#. Add an Instance Name
#. Optionally select and Environment Tag and/or add a custom Tag
#. Select :guilabel:`NEXT`
#. Select a Plan and available options for the Plan, or use the custom Plan
#. Select a Space to add the Instance to
#. Select :guilabel:`NEXT`
#. In the Deployments section, select a Deployment and Version to be deployed. These can be git repos or files added in ``Provisioning -> Deployments``

   .. IMPORTANT:: If services are specified in a git repo manifest, |morpheus| assumes they are already exist in the PCF cloud with matching names.

#. Select :guilabel:`NEXT`
#. Select :guilabel:`COMPLETE`

This will quickly create the Cloud Foundry Application, and then the deployment will follow which may take longer depending on the app configuration. The location will be updated with the route once it is configured.

.. NOTE:: Compute, Memory, and CPU stats will be pulled, and a Cloud Foundry monitoring health check will be automatically configured for the instance.
