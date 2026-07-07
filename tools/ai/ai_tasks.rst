.. _ai-tasks:

AI Tasks
--------

AI Tasks are a Task type in |morpheus| that uses plain-language configuration to perform actions via a configured AI Agent. AI Tasks can:

- Perform singular one-off functions (ad-hoc Task execution)
- Perform repeating functions (configured as recurring Task Jobs)
- Be part of large-scale Workflows (Operational or Provisioning Workflows)

The AI Task type appears in the Task Types list as "AI Task" with the following source options: Local, Repository, URL. The execute target is Local. The role permission required is **Library: Tasks**.

Creating an AI Task
^^^^^^^^^^^^^^^^^^^

Navigate to :menuselection:`Library --> Automation --> Tasks` and click :guilabel:`+ ADD`. Select "AI Task" from the Task Types list.

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Field
     - Description
   * - **Name**
     - Name of the Task
   * - **Code**
     - Unique code name for API, CLI, and variable references
   * - **Agent**
     - Select a pre-existing AI Agent (see :ref:`ai-agents` documentation)
   * - **Inventory**
     - Select an existing Inventory; when bootstrapping an Instance, |morpheus| will add the Instance to the Inventory
   * - **Content**
     - Plain-language prompting for the AI Agent to use in executing the Task

Usage
^^^^^

AI Tasks can be executed in the following ways:

- **Ad-hoc execution** — Run the Task manually from the Tasks list or via API/CLI for one-off operations
- **Recurring Jobs** — Configure the Task as a Job with a schedule for repeating functions
- **Workflows** — Include the Task as a step in Operational or Provisioning Workflows for large-scale automation

The **Content** field is where the plain-language instruction is defined. This prompt is sent to the selected AI Agent, which uses its configured LLM and available tools to carry out the requested action.
