.. _conditional_workflows:

Conditional Workflow Tasks
==========================

Overview
--------

Conditional Workflow Tasks provide branching logic within |morpheus| Workflows. A Conditional Workflow Task evaluates a JavaScript expression and, based on the result, executes one of two Operational Workflows — enabling dynamic, decision-based automation chains.

This task type is found in :menuselection:`Library --> Automation` (Library > Automation > Tasks) with the type **Conditional Workflow**.

How It Works
------------

The Conditional Workflow Task operates on a simple if/else model:

#. A JavaScript expression is evaluated
#. If the expression resolves to ``true``, the **If Workflow** is executed
#. If the expression resolves to ``false``, the **Else Workflow** is executed
#. The parent Workflow continues after the conditional branch completes

.. code-block:: text

   Parent Workflow
   ├── Task 1
   ├── Conditional Workflow Task
   │   ├── [true]  → If Operational Workflow
   │   └── [false] → Else Operational Workflow
   └── Task 3 (continues after conditional)

Creating a Conditional Workflow Task
-------------------------------------

#. Navigate to :menuselection:`Library --> Automation` > Tasks
#. Click :guilabel:`+ ADD`
#. Select **Conditional Workflow** as the Task Type
#. Configure the Task:

   - **NAME:** Descriptive name for the conditional task
   - **CODE:** Unique code for API, CLI, and variable references
   - **LABELS:** Comma-separated labels for organization
   - **CONDITIONAL (JS):** JavaScript expression that evaluates to ``true`` or ``false``
   - **IF OPERATIONAL WORKFLOW:** The Workflow to execute when the condition is true
   - **ELSE OPERATIONAL WORKFLOW:** The Workflow to execute when the condition is false

#. Click :guilabel:`SAVE CHANGES`

JavaScript Conditional Syntax
------------------------------

The **CONDITIONAL (JS)** field accepts JavaScript expressions. The expression must resolve to a truthy or falsy value.

Simple Comparisons
^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

   // Check instance type
   "<%= instance.instanceTypeName %>" === "nginx"

   // Check cloud type
   "<%= zone.zoneType.code %>" === "vmware"

   // Numeric comparison
   parseInt("<%= instance.maxMemory %>") > 1073741824

Variable References
^^^^^^^^^^^^^^^^^^^

|morpheus| variables can be injected into the JavaScript expression using ``<%= %>`` syntax:

.. code-block:: javascript

   // Check custom option value
   "<%= customOptions.environment %>" === "production"

   // Check instance status
   "<%= instance.status %>" === "running"

   // Check group membership
   "<%= instance.group.name %>" === "Web Tier"

Using Task Results
^^^^^^^^^^^^^^^^^^

Results from prior Tasks in the Workflow can be referenced:

.. code-block:: javascript

   // Check result from a previous task (by task code)
   "<%= results.healthCheck %>" === "healthy"

   // Boolean from prior task
   "<%= results.validationTask %>" === "true"

   // Check if result contains a value
   "<%= results.checkStatus %>".indexOf("SUCCESS") >= 0

Complex Conditions
^^^^^^^^^^^^^^^^^^

Multiple conditions can be combined:

.. code-block:: javascript

   // AND condition
   "<%= customOptions.tier %>" === "web" && "<%= zone.name %>" === "Production"

   // OR condition
   "<%= instance.plan.name %>".indexOf("large") >= 0 || parseInt("<%= instance.maxCores %>") > 4

   // Negation
   "<%= instance.status %>" !== "suspended"

Result Propagation
------------------

When a Conditional Workflow Task executes a sub-workflow:

- **Task Results:** Results from Tasks within the If/Else workflow are accessible to subsequent Tasks in the parent Workflow via ``results.taskCode``
- **Error Handling:** If a Task within the sub-workflow fails:

  - If **Continue on Error** is set on the conditional task, the parent Workflow continues
  - If not set, the parent Workflow fails

- **Output:** The conditional task itself does not produce a result value; results come from the individual Tasks within the executed sub-workflow

Best Practices
--------------

#. **Keep conditions simple:** Complex logic should be in a preceding Script Task that outputs a simple value for the conditional to evaluate
#. **Use task codes:** Reference prior task results by code rather than name for stability
#. **Test both branches:** Ensure both the If and Else workflows handle their scenarios completely
#. **Handle null values:** Wrap variable references in null checks when values may not be present:

   .. code-block:: javascript

      ("<%= customOptions.skipDeploy %>" || "false") === "true"

#. **Use RESULT TYPE wisely:** When chaining tasks before a conditional, set appropriate result types (Single Value, JSON) so values are accessible

Examples
--------

**Route deployment by environment:**

.. code-block:: javascript

   "<%= customOptions.targetEnv %>" === "production"

- If true → Production Deployment Workflow (with approvals, blue-green, etc.)
- If false → Development Deployment Workflow (direct deploy)

**Conditional backup before update:**

.. code-block:: javascript

   "<%= customOptions.skipBackup %>" !== "true"

- If true → Pre-Update Backup Workflow
- If false → Skip backup (empty workflow or no-op)

**Scale decision based on metrics:**

.. code-block:: javascript

   parseInt("<%= results.checkMetrics %>") > 80

- If true → Scale Out Workflow
- If false → Normal Operation Workflow (no-op)
