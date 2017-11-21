Scheduling
==========

Overview
--------

Set weekly schedules for shutdown and startup times for Instances and VM's, apply Power Schedules to Instances pre or post-provisioning, apply Power Schedule policies on Group or Clouds, or use Guidance to automatically recommend and apply optimized Power Schedules.

Create Power Schedule
---------------------

#. Navigate to ``Operations -> Scheduling``
#. Select :guilabel:`+ ADD`
#. Configure the following options:

  NAME
    Name of the Power Schedule
  DESCRIPTION
    Description for the Power Schedule
  TIME ZONE
    Time Zone the Power Schedule times correlate to.
  TYPE
    Power On
      Power Up and then Down at scheduled times
    Power off
      Power Down then Up at scheduled times
    Enabled
      Check for Power Schedule to be Active. Uncheck to disable Power Schedule.
    DAYS
      Slide the start and end time controls for each day to configure each days Schedule. Green sections indicate Power on, red sections indicate Power Off. Time indicated applies to selected Time Zone.

  .. image:: /images/operations/powerSchedule.png

#. Select :guilabel:`SAVE CHANGES`

Add Power Schedule to Instance
------------------------------

#. Navigate to ``Provisioning -> Instances``
#. Select an Instance
#. Select :guilabel:`EDIT`
#. In the POWER SCHEDULE dropdown, select a Power Schedule.
#. Select :guilabel:`SAVE CHANGES`

Add Power Schedule to Virtual Machine
-------------------------------------

#. Navigate to ``Infrastructure -> Hosts -> Virtual Machines``
#. Select a Virtual Machine
#. Select :guilabel:`EDIT`
#. Expand the Advanced Options section
#. In the POWER SCHEDULE dropdown, select a Power Schedule.
#. Select :guilabel:`SAVE CHANGES`
