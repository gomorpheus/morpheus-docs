Execute Scheduling
------------------

Execute Scheduling creates Schedules for Jobs, including Task, Workflow and Backup Jobs.

Schedules use CRON expressions, such as ``0 23 * * 2`` equalling ``Executes every week on Tuesday at 23:00``. CRON expressions can easily be created by clicking the corresponding translation in the create or edit Execution Schedule modal below the Schedule field and selecting a new value.

Create Execution Schedules
^^^^^^^^^^^^^^^^^^^^^^^^^^

NAME
 Name of the Schedule

 .. note:: When assigning Execution Schedules, the Name will appear in the selection drop-down. Using a name that references the schedule is advised.

DESCRIPTION
 Description of the Execution Schedule for reference in the Execution Schedules list
TIME ZONE
 Time zone for execution
Enabled
 Check to enable the schedule. Uncheck to disable all associated executions.
SCHEDULE
 Enter CRON expression for the Execution Schedule. Example ``0 0 * * *`` equals ``Every day at 00:00`` (default)
SCHEDULE TRANSLATION
 The entered CRON schedule is translated below the SCHEDULE field. Highlighted values can be updated by selecting the value, and relevant options will be presented. The CRON expression will automatically be updated. 
