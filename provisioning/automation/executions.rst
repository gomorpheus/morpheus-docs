Executions
----------

``Automation - Executions`` contains execution status and history from Task and Operational Workflow Executions run from ``Automation - Tasks`` and ``Automation - Workflows``.

.. note:: Tasks and Workflows executed from a Job or from Instance or Host ``Actions`` do not populate in ``Automation -> Executions``, and can be referenced from the History tab on the target resource. All task and Workflow executions can be referenced in ``Operations -> Activity -> History``

Execution results in the ui display:

NAME
 Name of the Task or Workflow Executed
TYPE
 Type of execution (Task or Workflow)
START DATE
 Date and time of execution
ETA/DURATION
 Estimate time of completion for executions in progress, or the total execution time for completed executions.
RESULTS
 Result status of execution (Succeeded, Failed, In-Progress or Pending)
Execution Detail (i)
 Click on the ``i`` to view process output results

 .. note:: Job and automation executions can be expanded to show process details by clicking on the arrow icon immediately to the right of the `NAME` column. 
