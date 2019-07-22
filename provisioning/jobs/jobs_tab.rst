Jobs
----

Role Permissions
^^^^^^^^^^^^^^^^

Provisioning: Jobs
  None
    Cannot access ``Provisioning: Jobs : Jobs``
  Read
    Can access ``Provisioning: Jobs: Jobs`` but cannot create, edit or delete Jobs
  Full
    Full permissions to create, edit and delete Jobs

Provisioning: Job Executions
  None
    Cannot access ``Provisioning: Jobs : Job Executions``
  Read
    Can access and view ``Provisioning: Jobs : Job Executions`` including job execution history, status and Job output

Creating Jobs
^^^^^^^^^^^^^

.. note:: Jobs require existing Tasks or Workflows

To create a new job:

#. Navigate to ``Provisioning: Jobs``
#. Select :guilabel:`+ ADD`
#. Enter the following

   NAME
     Name of the ``Job`` in |morpheus|
   JOB TYPE
     Task Job
       Executes selected Task on Job schedule.
     Workflow Job
       Executes seclude Workflow on Job schedule.

#. Select :guilabel:`NEXT`

#. Configure the Job

   Task Jobs
     Job Configuration
       TASK
         Select target Task
       CUSTOM CONFIG
         Specify custom config for task execution (not required)
       Execution Config
         SCHEDULE
           manual
             Job will not be executed on a schedule. Job can be executed fro ``Provisioning: Jobs`` and selecting ``Actions -> Execute``
           Schedules
             Available Execution Schedules will populate.

             .. note:: |morpheus| provides two system default execution schedules, ``Daily at Midnight`` and ``Weekly on Sunday at Midnight``. Additional schedules can be added in ``Provisioning -> Automation -> Execute Scheduling``

         RUN NOW
           Select the checkbox for the job to execute upon save, regardless of ``SCHEDULE`` setting.

    Workflow Jobs
      Job Configuration
        WORKFLOW
          Select target Workflow
        CUSTOM CONFIG
          Specify custom config for Workflow execution (not required)
        Execution Config
          SCHEDULE
            manual
              Job will not be executed on a schedule. Job can be executed fro ``Provisioning: Jobs`` and selecting ``Actions -> Execute``
            Schedules
              Available Execution Schedules will populate.

              .. note:: |morpheus| provides two system default execution schedules, ``Daily at Midnight`` and ``Weekly on Sunday at Midnight``. Additional schedules can be added in ``Provisioning -> Automation -> Execute Scheduling``

          RUN NOW
            Select the checkbox for the job to execute upon save, regardless of ``SCHEDULE`` setting.
