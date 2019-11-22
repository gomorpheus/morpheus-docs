Ansible Troubleshooting
========================

When a workflow is executed manually, the Ansible run output is available in the Instance History tab. Select the ``i`` bubble next to the Ansible task to see the output.  You can also see the run output in the ui logs in ``/var/log/morpheus/morpheus-ui/current​`` which can be tailed by running ``morpheus-ctl tail morpheus-ui``.

Verify Ansible is installed on the |morpheus| Appliance.

Ansible should be automatically but certain os's or network conditions can prevent automated install. You can run ``ansible --version`` in the |morpheus|, or in the Ansible integration details page (``Administration -> Integrations -> Select Ansible Integration``, or in the Ansible tab of a group or cloud scoped to Ansible) just run ``--version`` as ansible is already included in the command.

If Ansible is not installed
----------------------------

Follow these instructions to install, or use your preferred installation method

  Ubuntu:

  .. code-block:: bash

      sudo apt-get install software-properties-common
      sudo apt-add-repository ppa:ansible/ansible
      sudo apt-get update
      sudo apt-get install ansible python-requests

  CentOS:

  .. code-block:: bash

      sudo yum install epel-release
      sudo yum install ansible python-requests

  Then create the working Ansible directory for Morpheus:

  .. code-block:: bash

      sudo mkdir /opt/morpheus/.ansible
      sudo chown morpheus-app.morpheus-app /opt/morpheus/.ansible


Validate the git repo is authorizing and the paths are configured correctly.
-----------------------------------------------------------------------------

The public and private ssh keys need to be added to the Morpheus appliance via ``Infrastructure -> Keys & Certs`` and the public key needs to be added to the git repo via user settings. If both are set up right, you will see the playbooks and roles populate in the Ansible Integration details page.

The Git Ref field on playbook tasks is to specify a different git branch than default. It can be left to use the default branch. If your playbooks are in a different branch you can add the brach name in the Git Ref field.

When running a playbook that is in a workflow, the additional playbooks fields do not need to be populated, they are for running a different playbook than the one set in the Ansible task in the Workflow, or using a different Git Ref.

.. NOTE::

  If you are manually running Workflows with Ansible tasks on existing Instances through ``Actions -> Run Workflow​`` and not seeing results, set the Provision Phase on the Ansible task to Provision​ as there may be issues with executing tasks on other phases when executing manually.
