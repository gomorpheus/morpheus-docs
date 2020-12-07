Apps
====

App monitors are very useful for seeing an aggregation of failures or impact based on a set of checks and groups. App monitors typically correlate to Apps provisioned from |morpheus| Blueprints but can also be manually created and organized. They can be great for visualizing the customer impact a failure might have or even keeping up on a screen in a NOC. To create an App monitor:

Name
  A friendly name for the new app monitor in |morpheus|
Description
  An optional description value to identify the app monitor
Max Severity
  The maximum severity incident a failed app may create. This setting overrides check and group max severity settings
Affects Availability
  When checked, this failed app impacts system-wide availability calculations
App Checks
  Use the typeahead field to select as many checks as needed to complete the app monitor. Checks are created in Monitoring > Checks and must exist prior to creating the app monitor
