Cloud Foundry
-------------

Configuration
^^^^^^^^^^^^^

Adding PCF Cloud From `Infrastructure -> Clouds`
````````````````````````````````````````````````

#. Navigate to ``Infrastructure -> Clouds``
#. Select :guilabel:`+ ADD`
#. Select **CLOUD FOUNDRY** from the Clouds list
#. Select :guilabel:`NEXT`
#. Populate the following:

   .. include:: /integration_guides/Clouds/base_options.rst

   **Details**

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

   .. include:: /integration_guides/Clouds/advanced_options.rst

#. Select :guilabel:`NEXT`
#. Select an existing or create a new Group to add the Cloud to. The Cloud can be added to additional Groups in a Groups `Clouds` tab.
#. Select :guilabel:`NEXT`
#. Review and then Select :guilabel:`COMPLETE`


Adding PCF Cloud From `Infrastructure -> Groups`
````````````````````````````````````````````````

#. Navigate to ``Infrastructure -> Groups``
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

   .. include:: /integration_guides/Clouds/advanced_options.rst

#. Select :guilabel:`NEXT`
#. Review and then Select :guilabel:`COMPLETE`

Adding Spaces
^^^^^^^^^^^^^
Cloud Foundry Spaces are referred to as Resource Pools in Morpheus.  You can add a new Space by:

#. Navigating to the Cloud and selecting the Resources tab.
#. Then, click :guilabel:‘+ Add Resource’.
#. Give the Resource a Name
#. Expand the Managers, Developers, and Auditors section to add specific Cloud Foundry users to the roles.  When adding a user to these sections, use their Cloud Foundry email addresses.

Provisioning
^^^^^^^^^^^^

|morpheus| automatically seeds MySQL, Redis and RabbitMQ PCF Instance Types, as well as a generic Cloud Foundry Instance Type that will create a shell app used in conjunction with deployments. PCF Marketplace items can also be added to the Provisioning Library in the Cloud detail view Marketplace tab. The Marketplace item will be added to the selected Instance Type and available when selecting the Cloud Foundry Cloud during Instance or App Template creation.

Deployments
^^^^^^^^^^^

The Cloud Foundry App Instance Type is used in conjunction with deployments. Users do not have to pick deployment when creating a Cloud Foundry App Instance Type, but then Instance will only be a shell of a Cloud Foundry Application.

A deployment in Morpheus can either point to a git hub repository or contain the actual manifest.yml and associated artifacts required for a Cloud Foundry deployment.  During the deployment, Morpheus will gather up the files required.  Therefore, if the deployment points to a git hub repository, Morpheus will fetch the files from git hub.  Once the files are obtained, Morpheus will deploy the artifacts in a similar fashion to the Cloud Foundry cli.  This includes parsing the manifest to obtain the parameters to create or update the Cloud Foundry application.  Morpheus will ignore certain fields such as memory and disk size because they are dictated by the selected plan.  Other fields are utilized such as routes.  After parsing the manifest.yml file (including overwriting certain fields), Morpheus is ready to update or create the App in Cloud Foundry.

After the App is configured, the artifacts references in the Morpheus deployment are uploaded to Cloud Foundry for the App.  Note that when paths are referenced in the manifest.yml file, the paths continue to be relative to the manifest.  So, a jar file under build/libs would need to be found under the build/libs directory.

If Cloud Foundry services are specified in the manifest, they must already exist within Cloud Foundry.  Morpheus App templates can be utilized to wire up Cloud Foundry services created by Morpheus.  In this case, Morpheus will add all of the included service names defined in the App template to the manifest.yml services section.  Therefore, multiple services can be used and wired up by Morpheus.”

Example
^^^^^^^

To better understand how Morpheus parses the manifest.yml file, lets take a closer look at the Cloud Foundry 'spring-music' project.  The project can be found here (https://github.com/cloudfoundry-samples/spring-music).

The project contains the required manifest.yml file as well as the source code and build.gradle file to define how the project is to be built.  After downloading the project to your local machine, build the project to generate the jar.

Now, let's take a look at the manifest.yml file:

.. code-block:: bash

    ---
    applications:
    - name: spring-music
      memory: 1G
      random-route: true
      path: build/libs/spring-music.jar


Using the Cloud Foundry docs (https://docs.cloudfoundry.org/devguide/deploy-apps/manifest.html), we can gain a better understanding of how this file is utilized by Cloud Foundry.

- The ``-name`` parameter defines the name that will be given to the application in Cloud Foundry.  Morpheus will overwrite this value with the name given to the Instance being created in Morpheus.

- The ``-memory`` parameter (as well as the disk_quota parameter if specified) will be overwritten by Morpheus based on the plan specified for the Instance.

- The ``-path`` parameter defines, where relative to the manifest.yml file, your Cloud Foundry application can be found.

- The ``-random-route parameter``, as well as all other parameters described in the Cloud Foundry documentation will simply be passed through to Cloud Foundry.


Adding Marketplace Items
^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure -> Clouds`` and select your Cloud Foundry Cloud
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
````````````````````````````

|morpheus| automatically seeds MySQL, Redis and RabbitMQ PCF Instance Types, and PCF Marketplace items can also be easily added to the Provisioning Library in the Cloud detail view Marketplace tab. The Marketplace item will be added to the selected Instance Type and available when selecting the Cloud Foundry Cloud during Instance or App Template creation.

#. Navigate to ```Provisioning -> Instances`` and select an Instance Type with a Cloud Foundry layout (MySQL, Redis and RabbitMQ plus Marketplace additions)
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
```````````````````````````````

.. IMPORTANT:: Add Deployments in ``Provisioning -> Deployments`` to be used when provisioning a Cloud Foundry App Instance Type.

.. NOTE:: Minimal options are outlined below.

#. Navigate to ```Provisioning -> Instances`` and select the `Cloud Foundry App` Instance Type
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
