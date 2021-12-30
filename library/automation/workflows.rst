Workflows
---------

Workflows are groups of Tasks, which are described in detail in the preceding section. Operational Workflows can be run on-demand against an existing Instance or server from the Actions menu on the Instance or server detail page. Additionally, they can be scheduled to run on a recurring basis through Morpheus Jobs (|ProJob|).

Provisioning Workflows are associated with Instances at provision time (in the Automation tab of the Add Instance wizard) or after provisioning through the Actions menu on the Instance detail page. Provisioning Workflows assign Tasks to various stages of the Instance lifecycle, such as Provision, Post Provision, and Teardown. When the Instance reaches a given stage, the appropriate Tasks are run. Task results and output can be viewed from the History tab of the Instance or server detail page.

Provisioning Workflow Execution Phases
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Phase
    - Description
    - Usage Example
    - Notes
  * - Configuration
    - Tasks are run prior to initial calls to the specified cloud API to initiate provisioning
    - Call to an external platform to dynamically generate a hostname prior to kicking off provisioning
    -
  * - Pre Provision
    - For VMs, Tasks are run after the VM is running and prior to any Tasks in the Provision phase. For containers, Tasks in this phase are run on the Docker host and prior to ``docker run``
    - Prepare a Docker host to run containers
    - Pre Provision can be used for a Blueprint so it is added before a script which is set at the Provision phase executes. Pre Provision for scripts is mainly for Docker as you can execute on the host before the container is running.
  * - Provision
    - Like pre-provision, Tasks for VMs are run after the VM is running. For containers, these Tasks are run on the containers once they are running on the host. For many users, this is the most commonly-used phase.
    - Join the server to a domain
    - Tasks included with in the Provision phase are considered to be vital to the health of the Instance. If a Task in the Provision phase fails, the Workflow will fail and the Instance provisioning will also fail. Tasks not considered to be vital to the existence of the Instance should go in the Post Provision phase where their failure will not constitute failure of the Instance.
  * - Post Provision
    - Tasks are run after the entire provisioning process has completed
    - Disable UAC or Windows Firewall on a Windows box or join Active Directory
    - When adding a node to an Instance, Tasks in this phase will be run on all nodes in the Instance after the new node is provisioned. This is because Post Provision operations may need to affect all nodes, such as when joining a new node to a cluster. Tasks in Pre Provision and Provision phases would only be run on the new node in this scenario.
  * - Start Service
    - Tasks in this phase are intended to start the service associated with the Instance type.
    - Include a script to start the service associated with the Instance (such as MySQL) which will execute when the Start Service action is selected from the Instance detail page
    - Start services is manually run from the Instance detail page and is designed to refer to the service the Instance provides.
  * - Stop Service
    - Tasks in this phase intended to stop the service associated with the Instance type.
    - Include a script to stop the service associated with the Instance (such as MySQL) which will execute when the Stop Service action is selected from the Instance detail page
    - Stop services is manually run from the Instance detail page and is designed to refer to the service the Instance provides.
  * - Pre Deploy
    - Tasks in this phase are run when a new deploy is triggered from the Deploy tab of the Instance detail page, prior to the deploy taking place.
    - Extract files from a deploy folder and move them to their final positions prior to deploy
    - Deployments are manually triggered from the Instance detail page and are designed to refer to deployment of services, like a website or database.
  * - Deploy
    - Tasks in this phase are run when a new deploy is triggered from the Deploy tab of the Instance detail page, after the deploy has completed
    - Update configuration files or inject connection details from the environment at completion of the deploy process
    - Deployments are manually triggered from the Instance detail page and are designed to refer to deployment of services, like a website or database.
  * - Reconfigure
    - Tasks in this phase are run when the reconfigure action is made against an Instance or host
    - Rescan or restart the Instance after a disk is added
    -
  * - Teardown
    - Tasks are run during VM or container destroy
    - Remove Active Directory objects prior to tearing down the Instance
    -
  * - Shutdown
    - Tasks are run immediately before the target is shutdown
    - Send an update on Instance power state to a CMDB
    -
  * - Startup
    - Tasks are run immediately before the target is started
    - Send an update on Instance power state to a CMDB
    -

Add Workflow
^^^^^^^^^^^^

#. Select the Provisioning link in the navigation bar
#. Select Automation from the sub-navigation menu
#. Click the Workflows tab to show the Workflows tab panel
#. Click the :guilabel:`+ Add` dropdown and select a Workflow type (Operational or Provisioning, see the section above for more on Workflow type differences)
#. From the New Workflow Wizard input a name for the workflow
#. Optionally input a description and a target platform
#. Add Tasks and Inputs using the typeahead fields, Tasks must be added to the appropriate phases for Provisioning Workflows
#. If multiple tasks are added to the same execution phase, their execution order can be changed by selecting the grip icon and dragging the task to the desired execution order
#. For multi-Tenant environments, select Public or Private visibility for the Workflow
#. For Operational Workflows, optionally mark "Allow Custom Config" from the Advanced Options section if needed. See the next section for more on this selection
#. Click the :guilabel:`SAVE CHANGES` button to save

.. NOTE:: When setting Workflow visibility to Public in a multi-Tenant environment, Tenants will be able to see the Workflow and also execute it directly from the Workflows list (if it's an Operational Workflow). They will not be able to edit or delete the Workflow.

Allow Custom Config
^^^^^^^^^^^^^^^^^^^

When marked on Operational Workflows, the user is shown a text area for custom configuration at execution time. This could be used to pass extra variables that wouldn't normally be in the script or for specifying extra configuration.

Edit Workflow
^^^^^^^^^^^^^

#. Select the Provisioning link in the navigation bar.
#. Select Automation from the sub-navigation menu.
#. Click the Workflows tab to show the workflows tab panel.
#. Click the Edit icon on the row of the workflow you wish to edit.
#. Modify information as needed.
#. Click the :guilabel:`Save Changes` button to save.

Delete Workflow
^^^^^^^^^^^^^^^

#. Select the Provisioning link in the navigation bar.
#. Select Automation from the sub-navigation menu.
#. Click the Workflows tab to show the workflows tab panel.
#. Click the Delete icon on the row of the workflow you wish to delete.
