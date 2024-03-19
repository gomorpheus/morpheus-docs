.. _Repositories:

Repositories
------------

The :menuselection:`Provisioning --> Code --> Repositories` section contains the repositories integrated with |morpheus| allowing users to browse repository folders and files, view file contents from any branch, trigger a refresh, and create tasks, scripts and templates directly from the repos. This section also handles Import/Export functionality which allows users to backup |morpheus| items (Tasks, Library Items, etc.) as code in a repository which can also be imported into another appliance, if desired.

- Browse integrated repositories
- View repo files
- Switch branches
- Trigger repo refreshes
- Filter by Integration, Organization or Text search
- Create Custom Views
- Create Tasks from repo files
- Create Spec Templates from repo files

Role Permissions
^^^^^^^^^^^^^^^^

Access and capabilities for the **Repositories** section is determined by the following role permissions:

Role: Feature Access: ``Infrastructure: Groups``
  - None: Cannot access Provisioning: Code section
  - Read or Full: Can access Provisioning: Code section

Role: Feature Access: ``Administration: Users``
  - None: Can view repo list but cannot browse repo folder and file names, select branch, refresh repositories or access/view file contents
  - Read or Full: Can view repo list, browse repo folder and file names, select branch, refresh repositories. Cannot access/view file contents without Read or Full level permission on ``Provisioning: Code Repositories``

Role: Feature Access: ``Provisioning: Code Repositories``
  - None: Cannot access Provisioning: Code Repositories
  - List Files: Can browse repo folder and file names, select branch, refresh Repositories. Cannot access/view file contents
  - Read or Full: Can browse repo folder and file names, select branch, refresh Repositories and access/view file contents

Role: Feature Access: ``Provisioning: Tasks``
  - None: Cannot create Tasks from repo files in repository browser
  - Read or Full: Can create Tasks from repo files in repository browser

Role: Feature Access: ``Provisioning: Library``
  - None: Cannot create Spec Templates from files in repository browser
  - Read or Full: Can create Spec Templates from files in repository browser

List Repositories
^^^^^^^^^^^^^^^^^

#. Select the ``Provisioning`` link in the navigation bar
#. Select the ``Code`` link in the sub-navigation bar
#. Users with sufficient permissions will see a list view of all integrated code repositories
#. Use the Search, Integrations or Organizations filter to filter listed repositories

.. tip:: Select the gear icon |gear| in the top right of the repos list view to create and save custom list views.

Refresh Repository
^^^^^^^^^^^^^^^^^^

#. Select the ``Provisioning`` link in the navigation bar
#. Select the ``Code`` link in the sub-navigation bar
#. Select name of target repository
#. Select :guilabel:`ACTIONS ▿` > ``Refresh``

Browse Repositories
^^^^^^^^^^^^^^^^^^^

#. Select the ``Provisioning`` link in the navigation bar
#. Select the ``Code`` link in the sub-navigation bar
#. Select name of target repository
#. Users with sufficient permissions can browse repo folder and file names, select branches, and refresh repositories. Users can access/view file contents with Read or Full level permission on ``Provisioning: Code Repositories``
#. Select target folder icon to drill into the folder

View Repository File
^^^^^^^^^^^^^^^^^^^^

#. Select the ``Provisioning`` link in the navigation bar
#. Select the ``Code`` link in the sub-navigation bar
#. Select name of target repository
#. Select |info| icon to right of target file name

.. note:: Users can access/view file contents only with Read or Full level permission on ``Provisioning: Code Repositories``. File contents displayed is from last repo sync. Refresh repo to ensure current version for recent commits.

Create Task from Repository File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Select the ``Provisioning`` link in the navigation bar
#. Select the ``Code`` link in the sub-navigation bar
#. Select name of target repository
#. Select gear icon to right of compatible target file name
#. Select target task type from available actions
#. Complete the NEW TASK wizard to create a new Task. The TYPE, SOURCE, REPOSITORY and FILE PATH fields will be automatically configured

.. note:: Shell and Powershell Tasks types can be created from the code repo browser in |morphver|. Ensure file compatibility with target Task type.

.. note:: Users can create tasks from Repositories only with Read or Full level permission on ``Library: Tasks``.

Create Spec Template from Repository File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Select the ``Provisioning`` link in the navigation bar
#. Select the ``Code`` link in the sub-navigation bar
#. Select name of target repository
#. Select gear icon to right of target file name
#. Select target spec template type from available actions
#. Complete the NEW SPEC TEMPLATE wizard to create a new Spec Template. The TYPE, SOURCE, REPOSITORY and FILE PATH fields will be automatically configured

.. note:: Terraform spec template types can be created from the code repo browser in |morphver|. Other spec template types can be created from repo files by changing the TYPE field in the NEW SPEC TEMPLATE wizard.

.. note:: Users can create tasks from Repositories only with Read or Full level permission on ``Library: Templates``.

Import and Export
-----------------

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="//www.youtube.com/embed/3JCJUjLuDyQ" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

|

Onboarded Git repositories can be configured as either import or export targets for a |morpheus| appliance. This means that many created |morpheus| constructs, such as Tasks, Library Items, and others, can be backed up to an integrated Git repository as code. This backup can take place on an automatic schedule (syncs every four hours) or can be triggered manually after changes are made. Users can back up all supported constructs within the appliance to a single repository or use Labels to back up only selected items. Exported constructs can also be imported into target appliances. This is useful for sharing items between two |morpheus| environments, such as from a development appliance to a production appliance.

.. NOTE:: The use of this feature requires an integrated Git repository. Please see our `integration guide <https://docs.morpheusdata.com/en/latest/integration_guides/Deployments/deployment.html>`_ for Github or other Git integrations if you've not yet integrated your code repositories. While Morpheus can onboard and work with both public and private code repositories, it is strongly recommended that you use private repositories for exporting your Morpheus constructs as code.

Supported Constructs:

- Tasks
- Workflows
- Spec Templates
- Library Items
- Forms

.. NOTE:: When exporting all supported constructs |morpheus| will export more than just the above types, however, only the above types are exportable as individual resources. This list may expand in the future as additional constructs become supported by future updates.

Role Permissions
^^^^^^^^^^^^^^^^

Access and capabilities for the Import/Export feature set is determined by the following role permissions:

Role: Feature Access: ``Admin: Export/Import``
  - **None:** Cannot access the edit button on the Code List Page (|ProCod|) to set Import/Export settings or see Import/Export actions on the Code Repository Detail Page
  - **Full:** Code repositories can be edited to set Import/Export configurations and Import/Export actions can be viewed and used on Code Repository Detail Pages

Import/Export Settings
^^^^^^^^^^^^^^^^^^^^^^

Code repositories are set to allow import, export or both from the Code Repositories List Page (|ProCod|). Click the edit button (|pencil|) to the right of the selected repository to edit its import/export settings. When editing a code repository for import and export, set the following configurations:

- **ENABLED:** When marked, routine syncs will take place between |morpheus| and this repository. This includes all file syncs and not just actions related to import and export
- **IMPORT/EXPORT:** Set "Auto export all" to automatically export once every four hours, "Manual export" to enable this repository for manual exports on demand, "Manual import" to enable this repository for manual imports on demand, "Import/Export" to enable both manual imports and exports on demand
- **PATH:** The path within the repository where |morpheus| should import from or export to
- **EXPORT LABEL FILTER:** Enter a Label and |morpheus| will export or import only constructs which include the Label into the repository. This must be a single Label, it cannot be a list of multiple Labels

Once you've configured the code repository, click :guilabel:`SAVE CHANGES`

.. NOTE:: Code repositories must have at least one file in them in order to export |morpheus| constructs as code. This can be as simple as a README file, they just cannot be empty.

.. IMAGE:: /images/provisioning/import/editRepo.png
  :width: 50%

Exporting
^^^^^^^^^

After a repository is configured to allow export (see previous section), it may perform periodic automatic refreshes or the user may need to refresh the repository on demand (depending on settings). To manually initiate an export, drill into the Repository Detail page, click :guilabel:`ACTIONS`, and click "Export All Resources".

.. IMAGE:: /images/provisioning/import/exportAll.png

Any new or updated constructs will be refreshed within the repository at the path your repository is configured to export into. Bear in mind that, even if you've configured |morpheus| to export only constructs categorized with a specific Label, any required dependencies would also be exported. For example, if you've labeled a Workflow to be exported, |morpheus| will also export the dependency Tasks so the Workflow will be functional. A similar behavior applies for exported Library Items which may have a number of dependencies. In the screenshot below, files can be seen populating the targeted Github repository.

.. IMAGE:: /images/provisioning/import/githubView.png

|morpheus| items are exported as scribe files. These are HCL-formatted representations of the construct as code. They include static attributes representative of the attributes set on the construct itself or they may use UUIDs to refer to other constructs or integrations. It shouldn't be necessary to view or edit them unless you're curious.

.. IMAGE:: /images/provisioning/import/viewScribe.png
  :width: 50%

Importing
^^^^^^^^^

After |morpheus| constructs have been exported as code, they can be pulled down into other appliances which have the same repositories integrated. Items can be imported ad-hoc from the file browser within a Code Repository Detail page. Click on the gear (|gear|) dropdown to the right of any scribe file that may exist in your repository. For example, in the screenshot below, an individual Task is being imported into the destination appliance.

.. IMAGE:: /images/provisioning/import/importFile.png

In addition to importing one-off items, code repositories may also be configured for import so that many items can be imported at once. The same configurations can be made for import as export, including a specific path within the repository to import from and whether only specific Label groups should be targeted. Triggering a larger scale import for a whole repository is done from the Code Repository Detail Page. Click the :guilabel:`ACTIONS` button and then click "Import All Resources".

.. IMAGE:: /images/provisioning/import/importAll.png

Once the import has been initiated, |morpheus| will check to see if a new item will be created, if an existing item would be updated, if no action could be taken due to a conflict, or if no changes would result. This information is presented to the user who may then decide if the import action should go ahead.

.. IMAGE:: /images/provisioning/import/checkImport.png

.. IMPORTANT:: Care has been taken with |morpheus| Import/Export to ensure that existing work cannot be wiped out by an import action. For example, if a Task with a name identical to a pre-existing Task would try to be imported, |morpheus| will require the naming conflict be resolved before the import can take place. In fact, |morpheus| Import can only create new items or overwrite items created by import. It cannot overwrite anything user-created or anything pre-seeded with the system at install. Additionally, import cannot be scheduled automatically. Users must initiate all imports.

.. IMPORTANT:: Importing resources which rely on existing integrations or sensitive values will require some additional configuration on the destination appliance. For example, importing a Task which references code in a separate repository which is not integrated on the target appliance will be imported with reference to the missing integration. This integration would need to be added before the Task could be used. Another example scenario would be a Task which references a secret value held in |morpheus| Cypher. Once again, the Task would be imported and the required Cypher references would need to be made within the destination appliance before the Task could be used.

Checking Imported Items Prior to Use
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As mentioned in the previous section, not every imported item will immediately be available for use. This is primarily due to the target appliance lacking an integration (for example, an Ansible Tower integration required for an imported Task) or a securely stored secret string (for example, a Task that calls a secret string stored in |morpheus| Cypher). |morpheus| will still import these resources but this section discusses some manual changes that may have to be made to imported items in order for them to be usable.

**Protected Fields and User Credentials**

Protected information and secret values are not exported. When importing any resources which rely on protected information, the user will need to manually update the resource on the target appliance. Examples include anything authenticated using a stored credential set (from the |InfTruCre| section), anything with a password field (such as HTTP Tasks or REST-based Option Lists accessing password-protected information), Chef Task Data Bag Keys, and more. Anything configured with a password or other protected field will need to be edited on the importing appliance and updated to have the protected information needed to function.

**Integrations**

When an imported Task requires an integration that does not exist on the appliance, an integration will be created with the same name. The integration credentials will not be established, nor will any other configuration fields outside of the name. Users will need to update the integration configuration to make it functional in order for the imported Task to function.

**SSH Keys**

SSH Keys are not set on imported resources, such as Tasks configured to be executed on a remote host. Users will need to add a valid key to the importing appliance and update the Task to use that SSH Key.

**Ansible Tower Tasks**

Following import, "Inventory" and "Job Template" fields will need to be configured on Ansible Tower Tasks.

**vRealize Orchestrator Tasks**

Following import, "Inventory" and "Job Template" fields will need to be configured on vRO Tasks.

**Option Lists**

Option lists need to be edited and saved prior to use in order to load any initial data sets that have been configured on the Option List.

**Forms**

Input defaults that are ID-based will require manual correction after import. For example, if you have a Group Input which defaults to ``GroupName:A(ID:2)``, when imported it will still be based off an ID value of 2. It's highly likely that in the importing environment, a different Group will have an ID value of 2. A manual change to the correct ID value is required in the destination environment. Bear in mind that if you re-import a Form, you will also undo any manual changes you've made in the importing environment. Thus, if you update all defaults after importing, and then import once again, these manual default changes will be wiped out.

Additionally, when Forms are using existing Inputs, those Inputs will be exported and imported for use in the destination environment. On import, |morpheus| will add the needed Inputs unless the destination environment already has an Input with the same CODE value. This could give the appearance of creating duplicate Inputs if the destination environment happens to have an Input with the same name but a different code value. Users may wish to rename Inputs in the event they end up with more than one having the same name.

**Tasks**

The user must ensure the presence of any dependency required by a Task. One example would be any Cypher keys being called by the Task. Add any required Cypher entries with identical keys or add compatible Cypher keys and update the Task configuration to utilize the updated Cypher mountpoints. Cypher is just one example, any other dependency required by the Task must be present. |morpheus| does not parse the Task configuration to determine which dependencies are or are not present or required.

**Icons and Images**

Icons which are set up on imported Instance Types will need to be manually uploaded to the appliance after import. They are not brought over as part of the import/export process.

**Virtual Images**

When importing Node Types, the associated Virtual Image is mapped by its "Code" value. It is expected that a Virtual Image with the correct "Code" value already exists on the target appliance. If not, the Node Type will be imported without any Virtual Image attached. The user will then need to edit the Node Type and associate it with a compatible Virtual Image in order to become usable.
