.. _Deployments:

Deployments
-----------

.. note:: In v5.3.2+, :menuselection:`Provisioning --> Deployments` has been moved to :menuselection:`Provisioning --> Code --> Deployments`

The deployments section provides very useful PaaS like capabilities when it comes to deploying applications into the newly provisioned environment. These can be uploaded directly from the UI, pulled from a build server, pulled from a public or private Git repository or even via the API and the various plugins created, such as Jenkins, and Gradle to support continuous build / integration workflows.

A deployment can be considered a set of versions that relate to a particular project or application being deployed. This allows one to keep track of a history of versions and easily reuse these deployment versions across Instances that may exist in different environments. An example might be to deploy a version from a deployment to a staging Instance and (once approved) also deployed into production.

Role Permissions
^^^^^^^^^^^^^^^^

Access and capabilities for the **Deployments** section is determined by the following role permissions:

Role: Feature Access: ``Provisioning: Code Deployments``
  - None: Cannot access Provisioning: Code Deployments.
  - Read: Can view Code Deployments. Cannot create, delete or edit Code Deployments.
  - Full: Can create, delete and edit Code Deployments.

Getting Started
^^^^^^^^^^^^^^^

Getting started with deployments is easy. They can vary slightly for the application stack being deployed but the simplest phase of a deployment is adding a version and adding the appropriate files to the deployment archive that are needed for the application to run. This could be a single file like a `WAR` file for Tomcat, or it could be hundreds of files for stacks like `Ruby on Rails`.

There are a few ways to create a deployment. The first is to use the :menuselection:`Provisioning --> Code --> Deployments` section of the application to create them. Simply add a new deployment and give it a name representing the application that is being deployed. Once a deployment is created select the deployment to view its versions (which will be empty to start). Next, it is time to add a version.

When adding a version there are several options. There are 3 types represented by the UI. These include File, Fetch, and Git respectively. A File deployment allows the user to simply drag their files into the file explorer presented by the dialog. This file explorer can take single files or entire file trees (If files exist in subfolders then only the Chrome browser is supported due to browser limitations at the time of this writing). This is also the common type that is represented when files are uploaded via the CLI, or available build tool integration plugins. Once the files have completed their upload simply save the version for use.

Git
```

For performing git based deploys |morpheus| supports both public and private repositories. To utilize a private git repository the add version dialog will display a public keypair that can be added to the git service for authentication purposes. Currently this keypair is shared across the account and not specifically scoped to the user so it may be advisable to connect this integration to a deployment account in git. From here either a `ssh` or `https` git url can be entered along with a git branch or tag name. Once the version is saved, this repository will be copied down into the deployment archive for use.

Fetch
`````

Fetch based deployments are pretty straightforward. Simply enter a url to a file representing the deployment. This can be a single file (in which case it will just be added to the deployment archive singularly) or it can be a zip file (which will automatically be expanded into the archive). HTTP Authentication options can also be entered if the url requires some form of basic authentication scheme for access by the appliance.

Configuring Library Items for Deployments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to have the UI tools available to utilize Deployments with a provisioned Instance, the Library items must have certain configurations set. Once configured correctly, any Instance provisioned from the Library item would then have access to any of your Deployments.

First, within the **Instance Type** (|LibBluIns|), ensure the SUPPORT DEPLOYMENTS attribute is marked. This is off by default so it will need to be manually enabled on all relevant Instance Types. Next, you'll want to ensure you have the correct DEPLOY FOLDER configured on **Node Types** (|LibBluNod|). This is the mount point which will be replaced by the contents of your Deployments. Finally, you will want the **Provisioning Workflows** associated with the Library item to have the proper Tasks configured within its Pre-Deploy and/or Deploy phases. Tasks in the Pre-Deploy phase are run as soon as the Deployment is triggered from the UI prior to any other Deploy actions taking place. This could be used, for example, to extract files from the deploy folder and move them to their final destinations before the primary deploy actions take place. Tasks in the Deploy phase are run after the deployment is completed, such as if you wanted to update configuration files or inject connection details from the environment after the completion of the deploy process.

Deploying to an Instance
^^^^^^^^^^^^^^^^^^^^^^^^

Now that the Deployment object and Library items are configured, it is easy to push that deployment out to any Instance provisioned within |morpheus| by navigating to the specific Instance that it needs deployed to. On the Instance detail page there is a tab called `Runtime` and within it another tab labeled `Deploy`. From here simply add a deploy. The dialog will ask firstly from which deployment the deploy is from (or allow you to create a new one on the spot), and secondly which version to deploy (also with the option to add one on the fly). The next step of the wizard will display any configuration options that might be specific to the Instance type being deployed to (i.e. `CATALINA_OPTS` for Tomcat or `Java Command` for java) as well as the file explorer and deployment type selections for review (or use when creating a new version on the fly). Fill in the required items then simply hit complete. The deploy will now be asynchronously sent off to all of the virtual machines or containers within the Instance in a rolling restart and the deployment status will be represented.

.. TIP:: When deploying to an Instance, the custom configuration options that were entered during the previous deployment are automatically carried forward allowing one to edit them or leave them as is.

Rolling Backwards and Forwards
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Because of the tracked history of deployments kept within |morpheus|, the deploy tab of Instance detail makes it easy to choose a previously run deployment and jump back to it in the event of a failed deployment. The history will automatically be updated and the configuration, as well as data from the previous deployment state of the Instance will be restored.

Offloading Storage
^^^^^^^^^^^^^^^^^^

Since a full history of the backup builds are kept in |morpheus|, as the appliance grows it becomes necessary to change where these are stored. On a fresh install these are stored on the local appliance in ``/var/opt/morpheus`` or wherever the master account may have changed the configuration to point to. It is also possible to adjust the deployment archive store by creating a `Storage Provider` tied to an S3 compatible object store, Openstack Swift object store, or any other type of mountpoint provided. This option can be adjusted in |AdmSetPro| once a storage provider is created within the account.

Add Deployment
^^^^^^^^^^^^^^

#. Select the ``Provisioning`` link in the navigation bar.
#. Select the ``Code`` link in the sub-navigation bar.
#. Select the ``Deployments`` tab.
#. Click the :guilabel:`+ Add` button.
#. Enter a Name for the deployment and a description (optional)
#. Click the :guilabel:`Save Changes` button to save.

Add Version
^^^^^^^^^^^

#. Select the ``Provisioning`` link in the navigation bar.
#. Select the ``Code`` link in the sub-navigation bar.
#. Select the ``Deployments`` tab.
#. Click the Name of the deployment you would like to add a version to.
#. Click the :guilabel:`Add Version` button.
#. From the Add Version Wizard select the deployment type.
#. Input the Version of the deployment.
#. Depending on the type of deployment selected perform one of the following:

    Files
      Drag files into the file explorer presented by the dialog. This file explorer can take single files or entire file trees.
    Fetch
      Enter a url to a file representing the deployment.
    Git
      The add version dialog will display a public key pair that can be added to the git service for authentication purposes. Either a ssh or https git url can be entered along with a git branch or tag name.

#. Click the :guilabel:`Save Changes` button to save.

Edit Deployment
^^^^^^^^^^^^^^^

#. Select the ``Provisioning`` link in the navigation bar.
#. Select the ``Code`` link in the sub-navigation bar.
#. Select the ``Deployments`` tab.
#. Click the |pencil| icon on the row of the deployment you wish to edit, or click the Name of the deployment and then the :guilabel:`Edit` button from the deployment detail page.
#. Modify information as needed
#. Click the :guilabel:`Save Changes` button to save.

Delete Deployment
^^^^^^^^^^^^^^^^^

#. Select the ``Provisioning`` link in the navigation bar.
#. Select the ``Code`` link in the sub-navigation bar.
#. Select the ``Deployments`` tab.
#. Click the |trash| icon on the row of the deployment you wish to delete, or click the Name of the deployment and then the :redguilabel:`DELETE` button.
