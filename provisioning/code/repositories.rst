.. _Repositories:

Repositories
------------

The :menuselection:`Provisioning --> Code --> Repositories` section contains the repositories integrated with |morpheus| allowing users to browse repository folders and files, view file contents from any branch, trigger a refresh, and create tasks, scripts and templates directly from the repos.

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
