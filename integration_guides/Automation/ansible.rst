Ansible
-------

Overview
^^^^^^^^

Ansible is a configuration management engine that is rapidly growing in popularity in the IT and DevOPS community. While it lacks some of the benefits at scale that solutions such as Salt, Chef, or Puppet offer. It is very easy to get started and allows engineers to develop tasks in a simplistic markup language known as YAML.  |morpheus| integrates with an existing repository of playbooks as the master in a master-slave Ansible architecture.

|morpheus| not only supports Ansible but greatly enhances Ansible to do things that it could not do in its native form. For example, Ansible can now be configured to run over the Morpheus agent communication bus. This allows playbooks to be ran against instances where ssh/winrm access may not be feasible due to networking restrictions or other firewall constraints. Instead it can run over the Morpheus |morpheus| which only requires port 443 access back to the |morpheus appliance URL.

This integration supports both Linux based and Windows platforms for playbook execution and can also be configured to query secrets from the Morpheus Cypher services (similar to Vault).

Requirements
^^^^^^^^^^^^^^^
* Minimum Ansible Version Requirement is 2.7.x
* For agentless non commandbus sshpass is required
* For windows non agent command bus pywinrm is required


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

  .. NOTE:: An instance can belong to multiple groups by separating group names with a comma

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
.. NOTE:: This will work on Morpheus Feature release 3.5.3-2 and above. This is not added to LTS release.

Morpehus variables can be used in playbook.

Use Case:

  Create a user as instance hostname during provisioning. Below is the playbook. Add this playbook to a task and run it as a workflow on the instance.

    .. code-block:: bash

      ---
        - name: Add a user
          hosts: all
          gather_facts: false
          tasks:
            - name: Add User
              win_user:
                name: "{{ morpheus['instance']['hostname'] }}"
                password: "xxxxxxx"
                state: present

  .. NOTE:: `{{ morpheus['instance']['hostname'] }}` is the format of using Morpheus Variables


  Create a user with a name which you enter during provisioning using a custom Instance type. This instance type has a `Text` Option type that provides a textbox to enter a username. The fieldName of the option type in this case would be `username`. Below is the playbook.

    .. code-block:: bash

      ---
        - name: Add a user
          hosts: all
          gather_facts: false
          tasks:
            - name: Add User
              win_user:
                name: "{{ morpheus['customOptions']['username'] }}"
                password: "xxxxxxx"
                state: present

  .. NOTE:: `{{ morpheus['customOptions']['username'] }}` will be the format.

Using Secrets
^^^^^^^^^^^^^^^

Another great feature with using Ansible and Morpheus together is the built in support for utilizing some of the services that Morpheus exposes for automation. One of these great services is known as Cypher (please see documentation on Cypher_ for more details). Cypher allows one to store secret data in a highly encrypted way for future retrieval. Referencing keys stored in cypher in your playbooks is a matter of using a built-in lookup plugin for ansible.

  .. code-block:: bash
  
    - name: Add a user
      win_user:
        name: "myusername"
        password: "{{ lookup('cypher','secret=password/myusername') }}"
        state: present


By using the ``{{ lookup('cypher','secret=password/myusername') }}`` syntax. One can grab the value directly out of the key for use. This lookup plugin also supports a few other fancy shortcuts. In this above example the `password/` mountpoint is capable of autogenerating passwords if they have not previously been defined and storing them within cypher for reference later.

Another capability is accessing properties from within a key in cypher. The value of a key can also be a JSON object which can be referenced for properties within. For example:

.. code-block:: bash

  {{ lookup('cypher','secret=secret/myjsonobject:value') }}

This would grab the `value` property off the nested json data stored within the key.

Cypher is very powerful for storing these temporary or permanent secrets that one may need to orchestrate various tasks and workflows within Ansible.


Using Ansible over the Morpheus Agent Command Bus
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In many environments, there may be security restrictions on utilizing SSH or WinRM to run playbooks from an Ansible server on the appliance to a target machine. This could be due to being a customer network (in the environment of an MSP ), or various security restrictions put in place by tighter industries (i.e. Government, Medical, Finance).

Ansible can get one in trouble in a hurry. It is limited in scalability due to its fundamental design decisions that seem to bypass concepts core to all other configuration management frameworks (i.e. SaltStack, Chef, and Puppet). Because of its lack of an agent, the Ansible execution binary itself has to handle all the load and logic of executing playbooks on all the machines in the inventory of an Ansible project. This differs from other tools where the workload is distributed across the agents of each vm. Because of this (reaching out) approach, Ansible is very easy to get started with, but can be quite a bit slower as well as harder to scale up. However, |morpheus| offers some solutions to help mitigate these issues and increase scalability while, at the same time improving security.

How does the Morpheus Agent Command Bus Work? One of the great things about Morpheus is it's Agent Optional approach. This means that this functionality can work without the Agent, however the agent is what adds the security benefits being represented here. When an instance is provisioned (or converted to managed) within |morpheus|, an agent can be installed. This agent opens a secure websocket back to the Morpheus appliance (over port 443). This agent is responsible for sending back logs, guest statistics, and a command bus for automation. Since it is a WebSocket, bidirectional communication is possible over a STOMP communication bus. When this functionality is enabled on an Ansible integration, a `connection_plugin` is registered with Ansible of type `|morpheus|` and `morpheus_win`. These direct bash or powershell commands, in their raw form, from Ansible to run over a |morpheus api|. The Ansible binary sends commands to be executed as an https request over the API utilizing a one time execution lease token that is sent to the Ansible binary. File transfers can also be enacted by this API interface. When morpheus receives these commands, they are sent to the target instances agent to be executed. Once they have completed a response is sent back and updated on the `ExecutionRequest` within Morpheus. Ansible polls for the state and output on these requests and uses those as the response of the execution. This means Ansible needs zero knowledge of a machines target ip address, nor its credentials. These are all stored and safely encrypted within |morpheus|.

It has also been pointed out that this execution bus is dramatically simpler than utilizing `pywinrm` when it comes to orchestrating Windows  as the winrm configurations can be cumbersome to properly setup, especially in tightly secured Enterprise environments.



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
