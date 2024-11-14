Execute Scheduling
------------------

Execute Scheduling creates time schedules for automated jobs, such as backups. Backup Jobs are discussed in greater detail in the Backups section and are configured with an execution schedule to coordinate their run times. This section goes through the process of creating and configuring the scheduling object.

Schedules use CRON expressions, such as ``0 23 * * 2`` equalling ``Executes every week on Tuesday at 23:00``. CRON expressions can easily be created by clicking the corresponding translation in the create or edit Execution Schedule modal below the Schedule field and selecting a new value.

.. Note:: Execute Schedules CRON expressions should not include seconds or years. The days of the week should be numbered 1-7, beginning with Monday and ending with Sunday. SUN-SAT notation may also be used. For more on writing CRON expressions, many guides are hosted on the Internet including `this one <https://docs.oracle.com/cd/E12058_01/doc/doc.1014/e12030/cron_expressions.htm>`_. |morpheus| execution schedules support most cron syntax but certain more complex expressions may fail to evaluate and the execute schedule will not save. Additionally, some complex expressions may save and work correctly while the friendly written evaluation below the SCHEDULE field is not interpreted correctly. This is due to an issue with the underlying library used to build this feature and cannot easily be resolved at this time.

Create Execution Schedules
^^^^^^^^^^^^^^^^^^^^^^^^^^

NAME
 Name of the Execution Schedule

 .. Note:: When assigning Execution Schedules, the name value will appear in the selection drop-down. Using a name that makes clear the time interval is often helpful.

DESCRIPTION
 Description of the Execution Schedule for reference in the Execution Schedules list
.. rst-class:: hidden
  VISIBILITY
   |mastertenant| administrators may share Execute Schedules with Subtenants by setting the visibility to Public
TIME ZONE
 The time zone for execution
Enabled
 Check to enable the schedule. Uncheck to disable all associated executions and remove the schedule as an option for Jobs in the future
SCHEDULE
 Enter CRON expression for the Execution Schedule, for example ``0 0 * * *`` equals ``Every day at 00:00``
SCHEDULE TRANSLATION
 The entered CRON schedule is translated below the SCHEDULE field. Highlighted values can be updated by selecting the value, and relevant options will be presented. The CRON expression will automatically be updated
