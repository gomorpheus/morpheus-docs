Task Results
^^^^^^^^^^^^

Overview
`````````
Using Task results, the output from any preceding Tasks within the same Workflow phase is available to be called into additional Tasks. The results are stored on the ``results`` variable. Since results are available to all Tasks, we can use results from any or all prior Tasks so long as they are executed within the same provision phase.

In script type tasks, if a RESULT TYPE is set, |morpheus| will store the output on the ``results`` variable. It's important to understand that the result type indicates the format of the Task output |morpheus| should expect. |morpheus| will parse that output into a Groovy map which can be retrieved and further parsed by resolving the ``results`` variable. If the RESULT TYPE is incorrectly set, |morpheus| may not be able to store the Task results correctly. Jump to the section on `Script Config Examples <https://docs.morpheusdata.com/en/latest/library/automation/tasks/taskResults.html#results-types>`_ to see how script results are processed in various example cases.

Results Types
`````````````

- Single Value
   Entire task output is stored in ``<%=results.taskCode%>`` or ``<%=results["Task Name"]%>`` variable.
- Key/Value pairs
   Expects ``key=value,key=value`` output. Entire task output is available with ``<%=results.taskCode%>`` or ``<%=results["Task Name"]%>`` variable (output inside ``[]``). Individual Values are available with ``<%=results.taskCode.key%>`` variables.
- JSON
   Expects ``key:value,key:value`` json formatted output. Entire task output is available with ``<%=results.taskCode%>`` or ``<%=results["Task Name"]%>`` variable (output inside ``[]``). Individual Values are available with ``<%=results.taskCode.key%>`` variables.

.. important:: The entire output of a script is treated as results, not just the last line. Ensure formatting is correct for the appropriate result type. For example, if Results Type is ``json`` and the output is not fully json compatible, the result would not return properly.

.. important:: Task results are not supported for Library Script task types

Script Config Examples
``````````````````````

:Single Value using Task Code:
  Source Task Config
     - NAME: Var Code (single)
     - CODE: singleExample
     - RESULT TYPE: Single Value
     - SCRIPT: ``echo "string value"``

  Source Task Output: ``string value``

  Results Task Config (using task code in variable)
   - NAME: N/A
   - CODE: N/A
   - RESULT TYPE: N/A
   - SCRIPT: ``echo "single: <%=results.singleExample%>"``

  Results Task Output: ``single: string value``

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
      keyvalExample
    RESULT TYPE
      Key/Value pairs
    SCRIPT
      ``echo "flash=bang,ping=pong"``
  Source Task Output
    ``flash=bang,ping=pong``
  Results Task for all results
    Results Task Script
      ``echo "keyval: <%=results.keyvalExample%>"``
    Results Task Output
      ``keyval: [flash:bang, ping:pong]``
  Results Task for a single value)
    Results Task Script
      ``echo "keyval value: <%=results.keyvalExample.flash%>"``
    Results Task Output
      ``keyval value: bang``

:JSON:
  Source Task Config
    NAME
      Var Code (json)
    CODE
      jsonExample
    RESULT TYPE
      JSON
    SCRIPT
      ``echo "{\"ping\":\"pong\",\"flash\":\"bang\"}"``
  Source Task Output
    ``{"ping":"pong","flash":"bang"}``
  Results Task for all results
    Results Task Script
      ``echo "json: <%=results.jsonExample%>"``
    Results Task Output
      ``json: [ping:pong, flash:bang]``
  Results Task for a single value
    Results Task Script
      ``echo "json value: <%=results.jsonExample.ping%>"``
    Results Task Output
      ``json value: pong``

  :Multiple Task Results:
    Results Task Script
       .. code-block:: bash

          echo "single: <%=results.singleExample%>"
          echo "task name: <%=results["Var Code"]%>"
          echo "keyval: <%=results.keyvalExample%>"
          echo "keyval value: <%=results.keyval.flash%>"
          echo "json: <%=results.jsonExample%>"
          echo "json value: <%=results.jsonExample.ping%>"

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
