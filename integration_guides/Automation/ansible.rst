Ansible
-------

Overview
^^^^^^^^

|morpheus| supports Ansible for configuration management.  |morpheus| accomplishes this by integrating with an existing repository of playbooks as the master in a master-slave Ansible architecture.

Add Ansible Integration
^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Administration -> Integrations` and select `+ New Integration`
#. Select Integration Type "Ansible"
#. Populate the following fields:

   * Name: Name of the Ansible Integration in |morpheus|
   * Enabled: Enabled by default Ansible Git URL:: https or git url format of the Ansible Git repo to use
   * Keypair: For private Git repos, a keypair must be added to |morpheus| and the public key added to the git account.
   * Playbooks Path: Path of the Playbooks relative to the Git url.
   * Roles Path: Path of the Roles relative to the Git url.
   * Group Variable Path: Path of the Group Variables relative to the Git url.
   * Host Variables Path: Path of the Host Variables relative to the Git url.

#. Save Changes

Once you have completed this section and saved your changes you can set up a Cloud or Group to utilize this integration.

Ansible on Windows
^^^^^^^^^^^^^^^^^^

When executing Ansible playbooks on Windows platforms, a few requirements must be met:

* ``pywinrm`` may need to be installed on the |morpheus| Appliance via ``pip install pywinrm``

* An Ansible Integration must be scoped to a Group or Cloud for Ansible to execute on Windows, as |morpheus| assumes Ansible local when no group or cloud is scoped to Ansible. The playbooks do not need to be executed solely in the Group or Cloud, one just needs to be scoped to an Ansible Integration for Ansible Windows to run properly.

Scope Ansible Integration to a Cloud
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure -> Clouds`
#. Edit the target Cloud
#. Expand the `Advanced Options` section
#. In the `Config Management` dropdown, select the Ansible Integration.
#. Save Changes

Once an Ansible integration is added to a Cloud, a new "ANSIBLE" tab will appear on the Cloud details page, populated with the Ansible integrations Playbook and Roles, as well as an editable Inventory list.

Scope Ansible Integration to a Group
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to `Infrastructure -> Groups`
#. Edit the target Group
#. Expand the `Advanced Options` section
#. In the `Config Management` dropdown, select the Ansible Integration.
#. Save Changes

Once an Ansible integration is added to a Group, a new "ANSIBLE" tab will appear on the Group details page, populated with the Ansible integrations Playbook and Roles, as well as an editable Inventory list.

Provisioning Options
^^^^^^^^^^^^^^^^^^^^

When provisioning Instances into a Cloud or Group with a Ansible Integration added, an `Ansible` section will appear in the Config section of the provisioning wizard. By default, Ansible is enabled, but can be disabled by expanding the `Ansible` section and unchecking `Enable Ansible`.

Ansible Integration Provisioning options:

Enable Ansible
  Select to bootstrap
Ansible Group
  Ansible Inventory Group. Use existing group or enter a new group name to create a new group. Leaving this field blank will place instance in the "unassigned" inventory group.
Playbook
  Playbook(s) to run. The .yml extension is optional.

Running Playbooks
^^^^^^^^^^^^^^^^^

Playbooks can also be ran on all inventory groups, individual groups, or added as a task and ran with workflows.

To run Ansible on all or a single inventory group, in the Ansible tab of the |morpheus| Group page, select the `Actions` dropdown and click `Run`.

In the `Run Ansible` modal, you can then select all or an individual group, and then all or a single Playbook, as well as add custom tags.

Playbook's can also be added as tasks to workflows in the `Provisioning -> Automation` section, and then selected in the Automation pane during provisioning of new instances, when creating app blueprints, or ran on existing instances using the `Actions -> Run Workflow` on the Instance or Host pages.

Using variables
^^^^^^^^^^^^^^^^^

Morpehus variables can be used in playbook. 

Use Case:

  Create a user as instance hostname during provisioning. Below is the playbook. `{{ instance['hostname'] }}` is the format of using Morpheus Variables. Add this playbook to a task and run it as a workflow on the instance.

    .. code-block:: bash

      ---
      - name: Add a user
        hosts: all
        gather_facts: false
        tasks:
          - name: Add User  
            win_user:
              name: "{{ instance['hostname'] }}"
              password: "xxxxxxx"
              state: present

  Create a user with a name which you enter during provisioning using a custom Instance type which has a `Text` Option type that provides a textbox to enter a username. The fieldName of the option type in this case would be `username`. Below is the playbook. `{{ customOptions['username']` will be the format. 

    .. code-block:: bash

      ---
      - name: Add a user
        hosts: all
        gather_facts: false
        tasks:
          - name: Add User  
            win_user:
              name: "{{ customOptions['username'] }}"
              password: "xxxxxxx"
              state: present


Troubleshooting Ansible
^^^^^^^^^^^^^^^^^^^^^^^

* When a workflow is executed manually, the Ansible run output is available in the Instance History tab. Select the ``i`` bubble next to the Ansible task to see the output.  You can also see the run output in the ui logs in /var/log/morpheus/morpheus-ui/current​ which can be tailed by running ``morpheus-ctl tail morpheus-ui``.

* Verify Ansible is installed on the |morpheus| Appliance.

  Ansible should be automatically but certain os's or network conditions can prevent automated install. You can run ``ansible --version`` in the |morpheus appliance|, or in the Ansible integration details page (Administration -> Integrations -> Select Ansible Integration, or in the Ansible tab of a group or cloud scoped to Ansible) just run ``--version`` as ansible is already included in the command.

  If Ansible is not installed, follow these instructions to install, or use your preferred installation method:

  Ubuntu:

  .. code-block:: bash

      sudo apt-get install software-properties-common
      sudo apt-add-repository ppa:ansible/ansible
      sudo apt-get update
      sudo apt-get install ansible

  CentOS:

  .. code-block:: bash

      sudo yum install epel-release
      sudo yum install ansible

  Then create the working Ansible directory for Morpheus:

  .. code-block:: bash

      sudo mkdir /opt/morpheus/.ansible
      sudo chown morpheus-app.morpheus-app /opt/morpheus/.ansible


* Validate the git repo is authorizing and the paths are configured correctly.

  The public and private ssh keys need to be added to the Morpheus appliance via "Infrastructure -> Keys & Certs" and the public key needs to be added to the git repo via user settings. If both are set up right, you will see the playbooks and roles populate in the Ansible Integration details page.

* The Git Ref field on playbook tasks is to specify a different git branch than default. It can be left to use the default branch. If your playbooks are in a different branch you can add the brach name in the Git Ref field.

* When running a playbook that is in a workflow, the additional playbooks fields do not need to be populated, they are for running a different playbook than the one set in the Ansible task in the Workflow, or using a different Git Ref.


* If you are manually running Workflows with Ansible tasks on existing Instances through `Actions -> Run Workflow​` and not seeing results, set the Provision Phase on the Ansible task to Provision​ as there may be issues with executing tasks on other phases when executing manually.
