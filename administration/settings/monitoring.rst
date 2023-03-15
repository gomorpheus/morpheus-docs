|morpheus| Monitoring Settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Auto Create Checks
  When enabled a Monitoring Check will automatically be create for Instances and Apps.
Availability Time Frame
  The number of days availability should be calculated for. Changes will not take effect until your checks have passed their check interval.
Availability Precision
  The number of decimal places availability should be displayed in, can be anywhere between 0 and 5. Instance availability is shown on the Instance detail page (and used elsewhere) and refers to the percentage of time the workload is up.
Default Check Interval
  The default interval to use when creating new checks.

.. NOTE:: Monitoring Checks can be manually configured if `Auto Create Checks` is disabled.

.. include:: servicenowmonitoring.rst
.. include:: newrelic.rst
