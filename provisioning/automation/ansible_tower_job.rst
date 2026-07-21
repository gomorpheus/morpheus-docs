.. _ansible_tower_job:

Ansible Tower Job Task
======================

Overview
--------

The Ansible Tower Job Task type integrates |morpheus| automation with Ansible Tower (Red Hat Ansible Automation Platform). This Task relays Ansible calls to an Ansible Tower server, executing Job Templates against |morpheus|-managed Instances and infrastructure.

Ansible Tower Jobs are commonly used for:

- Configuration management during Instance provisioning
- Application deployment workflows
- Compliance enforcement and remediation
- Operational automation (patching, updates, health checks)

Prerequisites
-------------

- An active Ansible Tower integration configured in |morpheus| (Administration > Integrations)
- Job Templates configured in Ansible Tower
- Inventories and Groups set up in Ansible Tower
- Network connectivity between |morpheus| and the Ansible Tower server

Configuring an Ansible Tower Integration
------------------------------------------

Before creating Ansible Tower Job Tasks, add the integration:

#. Navigate to Administration > Integrations
#. Click :guilabel:`+ ADD`
#. Select **Ansible Tower** as the integration type
#. Configure:

   - **NAME:** Descriptive name
   - **URL:** Ansible Tower server URL (e.g., ``https://tower.example.com``)
   - **USERNAME:** Tower API username
   - **PASSWORD:** Tower API password or token
   - **API VERSION:** Tower API version

#. Click :guilabel:`SAVE`

Creating an Ansible Tower Job Task
------------------------------------

#. Navigate to :menuselection:`Library --> Automation` > Tasks
#. Click :guilabel:`+ ADD`
#. Select **Ansible Tower Job** as the Task Type
#. Configure the Task:

   - **NAME:** Descriptive name for the Task
   - **CODE:** Unique code for API, CLI, and variable references
   - **TOWER INTEGRATION:** Select the Ansible Tower integration
   - **INVENTORY:** Select an existing Tower Inventory. When bootstrapping an Instance, |morpheus| adds the Instance to this Inventory.
   - **GROUP:** Enter a Group name. When bootstrapping, |morpheus| adds the Instance to this Group. If the Group does not exist in Tower, |morpheus| creates it.
   - **JOB TEMPLATE:** Select the Job Template to execute
   - **SCM OVERRIDE:** (Optional) Specify an SCM branch other than that configured on the Template
   - **EXECUTE MODE:** Select the execution scope:

     - **Limit to Instance:** Template executes only on the provisioned Instance
     - **Limit to Group:** Template executes on all hosts in the Group
     - **Run for All:** Template executes on all hosts in the Inventory
     - **Skip Execution:** Template execution is skipped (Instance is still added to Inventory/Group)

#. Click :guilabel:`SAVE CHANGES`

Execute Modes Explained
------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Mode
     - Behavior
   * - Limit to Instance
     - The Job Template runs with ``--limit`` set to the provisioned Instance hostname. Only the specific Instance is affected.
   * - Limit to Group
     - The Job Template runs with ``--limit`` set to the Group name. All hosts in the Group are affected.
   * - Run for All
     - The Job Template runs against the entire Inventory without limits. All hosts are affected.
   * - Skip Execution
     - The Instance is added to the Inventory and Group but no Job Template is launched. Useful for registration-only scenarios.

Instance Registration
---------------------

When an Ansible Tower Job Task executes during provisioning:

#. |morpheus| adds the Instance to the specified Inventory in Ansible Tower
#. The Instance is added to the specified Group (created if needed)
#. Host variables are set based on Instance metadata (IP address, hostname, etc.)
#. The Job Template is launched according to the Execute Mode

This registration persists in Tower, allowing subsequent Tower operations against the host outside of |morpheus|.

SCM Override
------------

The **SCM OVERRIDE** field allows specifying a different Git branch for the playbook source:

- Override the branch configured on the Tower Project
- Useful for testing playbook changes in development branches
- Format: branch name (e.g., ``develop``, ``feature/new-config``)

Using in Workflows
------------------

Ansible Tower Job Tasks integrate into |morpheus| Workflows:

**Provisioning Workflows:**

- Place in the **Post-Provision** phase for initial configuration
- The Instance is fully provisioned and accessible when the Task executes
- Host is registered in Tower for ongoing management

**Operational Workflows:**

- Execute Tower Job Templates on-demand against existing Instances
- Run from Instance Actions menu or scheduled via Jobs

**Task Results:**

- Tower Job status (success/failure) is relayed back to |morpheus|
- Job output is captured in the |morpheus| execution history
- Workflow continues or halts based on Tower Job exit status

Extra Variables
---------------

Extra variables can be passed to the Job Template through:

- |morpheus| automation variables injected into Tower Job extra_vars
- Custom options passed from the provisioning wizard
- Results from prior Tasks in the Workflow

Troubleshooting
---------------

**Task fails with "Unable to connect to Tower":**

- Verify network connectivity between |morpheus| appliance and Tower server
- Check Tower integration credentials
- Ensure the Tower API URL is correct and accessible

**Instance not appearing in Tower Inventory:**

- Verify the Inventory exists in Tower
- Check Tower user permissions for Inventory management
- Review |morpheus| activity logs for API errors

**Job Template fails:**

- Check the Tower Job details in the Tower UI for specific error output
- Verify the SCM project is synced successfully in Tower
- Ensure the Instance is reachable from Tower for playbook execution
