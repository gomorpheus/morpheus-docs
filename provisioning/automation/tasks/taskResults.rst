Task Results
^^^^^^^^^^^^

Overview
`````````
Task Results allow Tasks to use the output from preceding Tasks in the same Workflow phase via results variables.

Results are available for all tasks executed in the same phase in a workflow. For example, instead of using just one Tasks results in another Task, we can use all of the Task Results from the tasks in the same provision phase in a single task inside a workflow.

Configure Tasks
```````````````
In script type tasks, if ``RESULT TYPE`` is set, |morpheus| will store the Task's output as a variable.

Results Types
`````````````

- Single Value
   Entire task output is stored in ``<%=results.taskCode%>`` or ``<%=results["Task Name"]%>`` variable.
- Key/Value pairs
   Expects ``key=value,key=value`` output. Entire task output is available with ``<%=results.taskCode%>`` or ``<%=results["Task Name"]%>`` variable (output inside ``[]``). Individual Values are avilable with ``<%=results.taskCode.key%>`` variables.
- JSON
   Expects ``key:value,key:value`` json formatted output. Entire task output is available with ``<%=results.taskCode%>`` or ``<%=results["Task Name"]%>`` variable (output inside ``[]``). Individual Values are avilable with ``<%=results.taskCode.key%>`` variables.


.. important:: The entire output of a script is treated as results, not just the last line. Ensure formatting is correct for the appropriate result type. For example, if Results Type is ``json`` and the output is not fully json compatible, the result would not return properly.

.. important:: Task results are not supported for Library Script task types

Script Config Examples
````````````````````````

:Single Value using Task Code:
  Source Task Config
    NAME
      Var Code (single)
    CODE
      single
    RESULT TYPE
      Single Value
    SCRIPT
      ``echo "string value"``
  Source Task Output
    ``string value``
  Results Task using task code in variable
    Results Task Script
      ``echo "single: <%=results.single%>"``
    Results Task Output
      ``single: string value``

:Single Value using Task Name:
  Source Task Config
    NAME
      Var Code
    CODE
      none
    RESULT TYPE
      Single Value
    SCRIPT
      ``echo "string value"``
  Source Task Output
    ``string value``
  Results Task using task name in variable
    Results Task Script
      ``echo "task name: <%=results["Var Code"]%>"``
    Results Task Output
      ``task name: test value``


:Key/Value Pairs:
  Source Task Config
    NAME
      Var Code (keyval)
    CODE
      keyval
    RESULT TYPE
      Key/Value pairs
    SCRIPT
      ``echo "flash=bang,ping=pong"``
  Source Task Output
    ``flash=bang,ping=pong``
  Results Task for all results
    Results Task Script
      ``echo "keyval: <%=results.keyval%>"``
    Results Task Output
      ``keyval: [flash:bang, ping:pong]``
  Results Task for a single value)
    Results Task Script
      ``echo "keyval value: <%=results.keyval.flash%>"``
    Results Task Output
      ``keyval value: bang``

:JSON:
  Source Task Config
    NAME
      Var Code (json)
    CODE
      json
    RESULT TYPE
      JSON
    SCRIPT
      ``echo "{\"ping\":\"pong\",\"flash\":\"bang\"}"``
  Source Task Output
    ``{"ping":"pong","flash":"bang"}``
  Results Task for all results
    Results Task Script
      ``echo "json: <%=results.json%>"``
    Results Task Output
      ``json: [ping:pong, flash:bang]``
  Results Task for a single value
    Results Task Script
      ``echo "json value: <%=results.json.ping%>"``
    Results Task Output
      ``json value: pong``

  :Multiple Task Results:
    Results Task Script
       .. code-block:: bash

          echo "single: <%=results.single%>"
          echo "task name: <%=results["Var Code"]%>"
          echo "keyval: <%=results.keyval%>"
          echo "keyval value: <%=results.keyval.flash%>"
          echo "json: <%=results.json%>"
          echo "json value: <%=results.json.ping%>"

    Results Task Output
       .. code-block:: bash

          single: string value
          task name: string value
          keyval: [flash:bang, ping:pong]
          keyval value: bang
          json: [ping:pong, flash:bang]
          json value: pong

Workflow Config
```````````````

Add one or multiple tasks with Results Type configured to a workflow, and the results will be available to all tasks in the same phase of the workflow via the ``<%=results.variables%>`` during the workflow execution.

- Task Results are only available to tasks in the same workflow phase
- Task Results are only available during workflow execution
