.. _JobsJobs:

Jobs
----

.. toggle-header:: :header: Required Role Permissions **Click to Expand/Hide**

    Provisioning: Jobs

    - **None:** Cannot access |ProJob| > Jobs tab
    - **Read:** Can access |ProJob| > Jobs tab but cannot create, edit, or delete Jobs
    - **Full:** Full permissions to create, view, edit, and delete Jobs

    Provisioning: Job Executions

    - **None:** Cannot access |ProJob| > Job Executions tab
    - **Read:** Can access and view |ProJob| > Job Executions tab including job execution history, status, and Job output

|

Creating Jobs
^^^^^^^^^^^^^

.. note:: Jobs require existing Tasks or Workflows. See the appropriate section of |morpheus| docs for more on creating `Tasks <https://docs.morpheusdata.com/en/latest/provisioning/automation/automation.html#tasks>`_ and `Workflows <https://docs.morpheusdata.com/en/latest/provisioning/automation/automation.html#workflows>`_.

To create a new Job:

#. Navigate to |ProJob|
#. Select :guilabel:`+ ADD`
#. Enter the following

   - **NAME:** Name of the Job in |morpheus|
   - **JOB TYPE:** A Task Job will execute a selected Task, a Workflow Job will execute a selected Workflow
   - **ENABLED:** When checked, the Job will run as scheduled

#. Select :guilabel:`NEXT`

#. Configure the Job

   Task Jobs
     **TASK:** Select target Task. If relevant to the Task, Input fields will be presented

     **SCHEDULE:**
         Manual: Job is not scheduled but can be executed from |ProJob| and selecting Actions > Execute

         Date And Time: Job will be executed at one specific point in time and not again (unless rescheduled or executed manually)

         Schedule: Select a configured Execution Schedule. Execution Schedules are created in |LibAutExe|

         .. note:: |morpheus| provides two default execution schedules, ``Daily at Midnight`` and ``Weekly on Sunday at Midnight``. Any additional schedules were created by a User. Additional schedules can be added in |LibAutExe|

      **INCLUDE POWER STATE:** Select All, On, or Off. The default configuration is "All" and indicates the Job will run on all relevant Instances or servers at the proper schedule time. Selecting "On" or "Off" indicates the Job should only run against targets specifically having either an on or off power state

      **CONTEXT TYPE:** Server or Instance

      **CONTEXT SERVER/INSTANCE:** Select the Server or Instance you wish to target with the Job

      **RUN NOW:** When checked, the Job will execute on save regardless of ``SCHEDULE`` setting.

    Workflow Jobs
      **WORKFLOW:** Select target Workflow. If relevant to the Workflow, Input fields will be presented

      **SCHEDULE:**
          Manual: Job is not scheduled but can be executed from |ProJob| and selecting ``Actions > Execute``

          Date And Time: Job will be executed at one specific point in time and not again (unless rescheduled or executed manually)

          Schedule: Select a configured Execution Schedule. Execution Schedules are created in |LibAutExe|

          .. note:: |morpheus| provides two default execution schedules, ``Daily at Midnight`` and ``Weekly on Sunday at Midnight``. Any additional schedules were created by a User. Additional schedules can be added in |LibAutExe|

      **INCLUDE POWER STATE:** Select All, On, or Off. The default configuration is "All" and indicates the Job will run on all relevant Instances or servers at the proper schedule time. Selecting "On" or "Off" indicates the Job should only run against targets specifically having either an on or off power state

      **CONTEXT TYPE:** Server or Instance

      **CONTEXT SERVER/INSTANCE:** Select the Server or Instance you wish to target with the Job

      **RUN NOW:** When checked, the Job will execute on save regardless of ``SCHEDULE`` setting.

#. Select :guilabel:`NEXT`
#. Select :guilabel:`COMPLETE`
