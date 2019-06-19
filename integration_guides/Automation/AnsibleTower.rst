Ansible Tower
-------------

Overview
^^^^^^^^

|morpheus| supports Ansible Tower for configuration management.  |morpheus| accomplishes this by integrating with an existing instance running Ansible Tower (AT) 3.3.0-1 and earlier. The username and password required for integration can be a user with admin access or a user with project admin access.
|morpheus| will import the current Inventory, Templates, Hosts, Groups and Projects. In the integration view it will add a Job tab which will have information of all the jobs executed from Morpheus.
Note: It will not import data of the jobs which are not executed from Morpheus.

Add Ansible Tower Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Administration -> Integrations` and select `+ New Integration`
#. Select Integration Type "Ansible Tower"
#. Populate the following fields:

   * Name: Name of the Ansible Tower Integration in |morpheus|
   * Enabled: Enabled by default it is enabled. To disable the integration, uncheck this option and save.
   * Ansible Tower URL: This would be an https or http Ansible tower url.
   * Username: The user morpheus would use to communicate with Ansible Tower.
   * Password: Enter the password. Password is encrypted and saved in DB.
   * API Version: This drop down has one option v2 for now but may have others in future.

#. Save Changes

Once you have completed this section and saved your changes you can set up a Cloud or Group to utilize this integration.

Scope Ansible Tower Integration to a Cloud
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
All instances provisioned in this cloud will have the Ansible Tower config option during provisioning. See below the Provisioning Options for more details about the options.

#. Navigate to `Infrastructure -> Clouds`
#. Edit the target Cloud
#. Expand the `Advanced Options` section
#. In the `Config Management` dropdown, select the Ansible Tower Integration.
#. Save Changes


Scope Ansible Tower Integration to a Group
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
All instances provisioned in this Group will have the Ansible Tower config option during provisioning in any cloud part of the Group. See below the Provisioning Options for more details about the options.

#. Navigate to `Infrastructure -> Groups`
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

Use Case
^^^^^^^^

You have Job template(s) in Ansible Tower to do post build config after the OS is deployed. The playbook with roles and tasks to do post build will add specific users and groups, install required packages, remove packages, disable services, change config for ntp, resolv, hosts etc. You want to add the instance to an existing Group/Inventory in Tower.

You can achieve this by adding the Ansible Tower Integration and then scope it to a Cloud or Group. While provisioning an instance, in the config stage you have the Ansible Tower section with option to select the post build job template, select the Inventory and provide an existing Group Name or if the Group doesn't exist Morpheus will create it and submit for provisioning. 

Morpheus will provision the instance, once it is in the finalize state where the instance has an ip and has completed domain join if required, added user(s) or User Groups if specified then Morpheus will add the instance to the inventory and Group and run the Template which will do all the post build of the server. 

The output of the post build template execution can be see under Instance history.