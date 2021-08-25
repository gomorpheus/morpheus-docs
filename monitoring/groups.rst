Monitoring Groups
=================

Group monitors can only contain checks and can be edited or created in `Monitoring > Groups`. Besides simply adding and removing checks to a group there are a few other useful options that can be customized in a group:

Name
  A friendly name for the group monitor in |morpheus|
Min Checks
  This specifies the minimum number of checks within the group that must be happy to keep the group from becoming unhealthy
Max Severity
  The maximum severity incident a failed check may create. This setting overrides a check's max severity setting
Affects Availability
  If checked, a failing group monitor impacts system-wide availability calculations
Checks
  Use the typeahead field to select pre-existing checks for the group monitor. If check(s) need to be created, this can be done in Monitoring > Checks

.. NOTE:: Some useful information can also be seen on the detail page of a check. For example, the average response time of all checks within the group, or an aggregated check history can be viewed.
