Scheduling
==========

Overview
--------

|morpheus| provides scheduling capabilities for various operational tasks, allowing administrators to automate routine activities and manage resource lifecycle timing. Scheduling features are available across several areas of the platform.

Execute Schedules
-----------------

Execute Schedules define time windows during which automated tasks, jobs, and workflows are permitted to run. They act as execution policies that control when automation can execute.

Navigate to |ProAut| > Execute Schedules to manage execute schedule definitions.

Creating an Execute Schedule
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to Provisioning > Automation > Execute Schedules
#. Click :guilabel:`+ ADD`
#. Configure the schedule:

   NAME
     A descriptive name for the execute schedule.

   DESCRIPTION
     Optional description of when and why this schedule is used.

   SCHEDULE TYPE
     The type of schedule definition:

     - **Date and Time** — A specific date/time window
     - **Day of Week** — Recurring on specific days of the week with time windows

   TIME ZONE
     The time zone for the schedule definition.

   ENABLED
     Toggle to enable or disable the schedule.

#. Click :guilabel:`SAVE`

Power Schedules
---------------

Power Schedules automate the start and stop of Instances and Servers based on defined time windows. This is commonly used to shut down non-production environments outside business hours to reduce costs.

Navigate to |ProAut| > Power Schedules to manage power schedule definitions.

Creating a Power Schedule
^^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to Provisioning > Automation > Power Schedules
#. Click :guilabel:`+ ADD`
#. Configure the schedule:

   NAME
     A descriptive name for the power schedule.

   DESCRIPTION
     Optional description.

   SCHEDULE TYPE
     - **Power On** — Start resources during the defined window
     - **Power Off** — Stop resources during the defined window
     - **Custom** — Define specific on/off times

   TIME ZONE
     The time zone for the schedule.

   DAYS
     Select which days of the week the schedule is active.

   START TIME / END TIME
     The time window during which the power action applies.

   ENABLED
     Toggle to enable or disable the schedule.

#. Click :guilabel:`SAVE`

Assigning Power Schedules
^^^^^^^^^^^^^^^^^^^^^^^^^^

Power schedules can be assigned to:

- **Instances** — Via the Instance detail page or during provisioning
- **Servers** — Via the Server detail page

Assigned resources will automatically start or stop according to the schedule definition.

Instance Schedules
------------------

Individual Instances can have schedules assigned for lifecycle management, including:

- **Expiration dates** — Auto-terminate instances after a defined period
- **Shutdown schedules** — Auto-stop instances at specified times
- **Extension requests** — Users can request extensions to scheduled expirations

Instance schedules are configured on the Instance detail page or enforced through policies.

Report Schedules
----------------

Reports can be scheduled for automatic generation on recurring intervals:

#. Navigate to |OpRep|
#. Click :guilabel:`SCHEDULE` next to the desired report type
#. Configure the report parameters and schedule frequency
#. Click :guilabel:`SAVE`

Scheduled reports generate automatically and appear in the report history for the selected report type.

Job Schedules
-------------

Jobs (Provisioning > Jobs) support schedule configuration for recurring execution of tasks and workflows:

- **Manual** — Execute on demand only
- **Date and Time** — Execute once at a specific date/time
- **Schedule** — Execute on a recurring schedule (references Execute Schedules)

Policies and Scheduling
-----------------------

Several policy types leverage scheduling:

- **Power Schedule policies** — Enforce power schedules at the Group or Cloud level
- **Expiration policies** — Set maximum instance lifetimes
- **Shutdown policies** — Enforce automatic shutdowns after defined periods

These are configured under Infrastructure > Groups > Policies or Infrastructure > Clouds > Policies.
