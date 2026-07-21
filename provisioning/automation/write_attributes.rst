.. _write_attributes:

Write Attributes Task
=====================

Overview
--------

The Write Attributes Task type writes a JSON payload of key-value pairs to the attributes property of the target resource (Instance, server, or container). This enables passing data between Tasks and Workflow phases, storing computed values for later reference, and building dynamic configuration state during provisioning.

Write Attributes Tasks are particularly useful for:

- Storing values from one Provisioning Workflow phase for use in another phase
- Passing computed configuration between Tasks
- Building dynamic metadata that other Tasks or integrations can reference
- Tagging resources with runtime-determined properties

Creating a Write Attributes Task
----------------------------------

#. Navigate to :menuselection:`Library --> Automation` > Tasks
#. Click :guilabel:`+ ADD`
#. Select **Write Attributes** as the Task Type
#. Configure:

   - **NAME:** Descriptive name for the task
   - **CODE:** Unique code for API, CLI, and variable references
   - **ATTRIBUTES:** JSON payload to write (see formats below)

#. Click :guilabel:`SAVE CHANGES`

JSON Payload Formats
--------------------

Static Key-Value Pairs
^^^^^^^^^^^^^^^^^^^^^^

Write a fixed set of attributes:

.. code-block:: JSON

  {
    "my_key1": "my_value1",
    "my_key2": "my_value2",
    "environment": "production",
    "version": "2.1.0"
  }

Dynamic Values from Prior Task Results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reference outputs from previous Tasks using ``<%= results.taskCode %>`` syntax. The referenced Task must have its **RESULT TYPE** set to "Single Value":

.. code-block:: JSON

  {
    "database_host": "<%=results.discoverDb%>",
    "api_endpoint": "<%=results.resolveEndpoint%>",
    "deployment_id": "<%=results.createDeployment%>"
  }

.. NOTE:: ``taskCode`` refers to the **CODE** field value of the Task whose output you're referencing, not its name.

Dynamic JSON Map from Prior Task
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When a prior Task returns a full JSON object (RESULT TYPE set to "JSON"), pass it through using ``encodeAsJSON()``:

.. code-block:: JSON

  {
    "instances": <%=results.taskCode?.encodeAsJSON()%>
  }

.. IMPORTANT:: The ``encodeAsJSON()`` method is required for proper JSON serialization. Without it, the JSON map may not be stored correctly.

Mixed Static and Dynamic Values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Combine static values with dynamic references:

.. code-block:: JSON

  {
    "app_name": "myapp",
    "build_number": "<%=results.getBuild%>",
    "deployed_by": "<%=instance.createdByUsername%>",
    "deploy_time": "<%=new Date().format('yyyy-MM-dd HH:mm:ss')%>"
  }

Instance Variables
^^^^^^^^^^^^^^^^^^

|morpheus| instance variables can be referenced directly:

.. code-block:: JSON

  {
    "instance_name": "<%=instance.name%>",
    "cloud_name": "<%=zone.name%>",
    "group_name": "<%=instance.group.name%>",
    "ip_address": "<%=container.externalIp%>"
  }

Reading Written Attributes
---------------------------

Attributes written by this Task can be accessed in subsequent Tasks and Workflow phases:

In Scripts (Groovy, Python, etc.)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: groovy

  // Access written attributes
  def myValue = instance.getConfigProperty('my_key1')

In Variable References
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

  <%=instance.metadata.my_key1%>

In Subsequent Write Attributes Tasks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Written attributes accumulate — subsequent Write Attributes Tasks add to or overwrite existing keys without removing unmentioned keys.

Use Cases
---------

**Passing data between Provisioning Workflow phases:**

The Pre-Provision phase discovers infrastructure details, writes them as attributes, and the Provision phase reads them for configuration:

.. code-block:: JSON

  {
    "nfs_mount": "<%=results.discoverNfs%>",
    "subnet_id": "<%=results.selectSubnet%>",
    "security_group": "<%=results.assignSg%>"
  }

**Storing deployment metadata:**

.. code-block:: JSON

  {
    "last_deploy_version": "<%=results.getVersion%>",
    "last_deploy_date": "<%=new Date().format('yyyy-MM-dd')%>",
    "last_deploy_user": "<%=instance.createdByUsername%>"
  }

**Building configuration for downstream automation:**

.. code-block:: JSON

  {
    "monitoring_enabled": "true",
    "alert_channel": "#ops-alerts",
    "backup_schedule": "daily",
    "retention_days": "30"
  }

Best Practices
--------------

#. **Use descriptive key names:** Keys should clearly indicate their purpose (e.g., ``database_connection_string`` not ``val1``)
#. **Keep payloads focused:** Write only the attributes needed; avoid dumping entire result sets
#. **Validate JSON syntax:** Malformed JSON will cause the Task to fail. Use a JSON validator for complex payloads
#. **Handle null results:** When referencing prior Task results that may be null, use Groovy's safe navigation operator:

   .. code-block:: JSON

     {
       "value": "<%=results.myTask ?: 'default_value'%>"
     }

#. **Document attribute contracts:** When multiple Workflow phases depend on written attributes, document which keys are expected and their formats
