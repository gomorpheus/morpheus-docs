..
  Groups & Apps
  =============

  One great feature of the monitoring system is the ability to organize checks by groups and apps. This provides a nice convenient way to determine what a customer facing impact might be for a single failure as well as representing redundancy via groupings.

  It is important to note the relationship of apps, groups, and even checks with regards to instances provisioned within |morpheus|. For every `Instance` that is provisioned: A monitoring `Group` is created and a `Check` is added to that group for every `Container` or `Virtual Machine` within that Instance. This makes sense such that as an Instance is scaled out horizontally (containers/VMs added to it) and the monitoring system accurately represents the layers of redundancy. An `App` simply maps to a Provisioning `App` and should be pretty straightforward to understand.

..
  Groups
  ------

  It is also possible to organize custom checks in this hierarchical structure by manually adding or editing a Group or App. Groups can only contain checks and can be edited or created in `Monitoring > Groups`. Besides simply adding and removing checks to a group there are a few other useful options that can be customized in a group.

  Min Checks
    This specifies the minimum number of checks within the group that must be happy to keep the group from becoming unhealthy.
  Max Severity
    The maximum severity incident a failed check may create. This setting overrides a checks Max Severity setting.
  Affects Availability
    Whether or not a failed group impacts system wide availability calculations.

  Some useful information can also be seen on the detail page of a check. For example, the average response time of all checks within the group, or an aggregated check history can be viewed.

..
  Apps
  ----

  Apps are very useful for seeing an aggregation of failures, or impact based on a set of checks and groups. Apps typically correlate to apps created in provisioning but can also be manually created and organized. They can be great for visualizing the customer impact a failure might have or even keeping up on a screen in a NOC. There are a few useful options as well with regards to Apps:

  Max Severity
    The maximum severity incident a failed app may create. This setting overrides check and group Max Severity settings.
  Affects Availability
    Whether or not a failed app impacts system wide availability calculations.
