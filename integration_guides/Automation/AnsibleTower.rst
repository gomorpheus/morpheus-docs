Ansible Tower
-------------

Overview
^^^^^^^^

|morpheus| supports Ansible Tower for configuration management.  |morpheus| accomplishes this by integrating with an existing instance running Ansible Tower (AT) 3.3.0-1 and earlier. The username and password required for integration can be a user with admin access or a user with project admin access

|morpheus| will import the current Inventory, Templates, Hosts, Groups and Projects. In the integration view it will add a Job tab which will have information of all the jobs executed from Morpheus.

.. Note:: This integration will not import data of the jobs which are not executed from |morpheus|.

Add Ansible Tower Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `|AdmInt|` and select :guilabel:`+ New Integration`
#. Select Integration Type "Ansible Tower"
#. Populate the following fields:

   * Name: Name of the Ansible Tower Integration in |morpheus|
   * Enabled: To disable the integration, uncheck this option
   * Ansible Tower URL: An HTTPS or HTTP Ansible Tower URL
   * Username: The user |morpheus| would use to communicate with Ansible Tower
   * Password: Enter the password. Password is encrypted and saved in DB
   * API Version: This drop down has one option (``v2``) for now but may have others in future

#. Save Changes

Once you have completed this section and saved your changes you can set up a Cloud or Group to utilize this integration.

Scope Ansible Tower Integration to a Cloud
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
All instances provisioned in this cloud will have the Ansible Tower config option during provisioning. See below the Provisioning Options for more details about the options.

#. Navigate to `Infrastructure > Clouds`
#. Edit the target Cloud
#. Expand the `Advanced Options` section
#. In the `Config Management` dropdown, select the Ansible Tower Integration.
#. Save Changes


Scope Ansible Tower Integration to a Group
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
All instances provisioned in this Group will have the Ansible Tower config option during provisioning in any cloud part of the Group. See below the Provisioning Options for more details about the options.

#. Navigate to `Infrastructure > Groups`
#. Edit the target Group
#. Expand the `Advanced Options` section
#. In the `Config Management` dropdown, select the Ansible Tower Integration.
#. Save Changes

Provisioning Options
^^^^^^^^^^^^^^^^^^^^

When provisioning Instances into a Cloud or Group with a Ansible Tower Integration added, an `Ansible Tower` section will appear in the Config section of the provisioning wizard. By default, Ansible Tower is enabled, but can be disabled by expanding the `Ansible Tower` section and unchecking `Enable Ansible Tower`.

Ansible Integration Provisioning options:

Enable Ansible Tower
  Select to bootstrap
Inventory
  A list of Inventory available in Ansible Tower will appear in the drop down. Select an existing inventory. The instance will be added to the inventory selected.
Ansible Group
  Enter the name of an existing Group in the inventory selected above.
Template
  Select an existing template or select the option 'Create New Template'. If 'Create New Template' is selected below fields will appear and are mandatory
    Template Name
      Enter the template name
    Project
      Select an existing project from the drop down options
    Playbook
      Select a playbook from the dropdown to be associated with the template. Note: |morpheus| doesn't store a local copy of the playbooks visible in Ansible Tower. SCM or local path for playbooks should be maintained in Ansible Tower.
Execute Mode
  Select one of the options from the dropdown
    Limit to instance
      This will execute the template on the instance provisioned.
    Limit to Group
      This will execute the template on all hosts attached to the group entered in the 'Ansible Group' field.
    Run for all
      This will execute the template on all hosts in the inventory
    Skip execution
      This will skip the execution of the template on the instance provisioned.

Scoping Ansible Tower Jobs to Tenant-Default Inventories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Users in the Primary Tenant have an additional Inventory execution option when creating Ansible Tower Job-type Tasks. When making a selection in the Inventory field, "Use Tenant Default" may be selected rather than a specific Inventory. This is because Ansible Tower Jobs created in the Primary Tenant may be shared publicly to other Tenants through public Workflows or when associated with public Library items.

.. image:: /images/integration_guides/automation/ansibleTower/ansibleTowerInventory.png
  :width: 50%

When this option is selected and the Task is run in a Subtenant, it will automatically be run against the default Inventory which is configured for the Subtenant. The next section includes steps for associating Tenants and default Inventories.

.. IMPORTANT:: An Ansible Tower Job configured to run against a Tenant-default Inventory will fail when run by a user whose Tenant does not have a default Inventory set.

Setting Default Inventories for Tenants
```````````````````````````````````````

When creating or editing Ansible Tower integrations, navigate to the Inventory tab to view all Inventories synced from the selected integration. Click "Permissions" inside the "MORE" action menu at the end of a row for the selected Invetory. Within the PERMISSIONS modal, there is a single typeahead field where a Tenant can be selected. Once the Tenant is selected, click :guilabel:`SAVE CHANGES`. Now back on the Inventory list view, you'll see the default Tenant which is associated with each Inventory.

.. NOTE:: Tenants may only be associated with one Inventory, though an Inventory can have multiple Tenant associations. If a Tenant is selected to be associated with a new Inventory, its association with a previous Inventory will automatically be removed.

.. image:: /images/integration_guides/automation/ansibleTower/inventoryList.png
  :width: 50%

Passing extra_vars to Ansible Tower Job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When provisioning or when running Ansible Tower Jobs as |morpheus| Tasks, you may pass the ``extra_vars`` stack to the Tower Job. First, ensure the Job Template has extra variables "Prompt on Launch" enabled as shown below:

.. image:: /images/automation/towerExtraVars.png

The sample Playbook below is associated with the Tower Job Template.

.. code-block:: bash

  ---
  - hosts: all
  vars:
    Opensource_Team: "Customer"
  tasks:
  - name: Print Hello World
    debug:
      msg:
      - "Hello World {{ Opensource_Team }}. Here are Morpheus extra_vars: {{ morpheus }}"

After executing the Tower Job, we can see the variable stack surfaced into the results as defined in the Playbook:

.. image:: /images/automation/towerResults.png

Use Case
^^^^^^^^

You have Job template(s) in Ansible Tower to do post build config after the OS is deployed. The playbook with roles and tasks to do post build will add specific users and groups, install required packages, remove packages, disable services, change config for ntp, resolv, hosts etc. You want to add the instance to an existing Group/Inventory in Tower.

You can achieve this by adding the Ansible Tower Integration and then scope it to a Cloud or Group. While provisioning an instance, in the config stage you have the Ansible Tower section with option to select the post build job template, select the Inventory and provide an existing Group Name or if the Group doesn't exist Morpheus will create it and submit for provisioning.

Morpheus will provision the instance, once it is in the finalize state where the instance has an ip and has completed domain join if required, added user(s) or User Groups if specified then Morpheus will add the instance to the inventory and Group and run the Template which will do all the post build of the server.

The output of the post build template execution can be see under Instance history.
