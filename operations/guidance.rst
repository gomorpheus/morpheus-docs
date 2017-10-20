Guidance
========

Overview
--------

The `Operations -> Guidance` section show recommendations for Resource and Costs Utilization optimization. By analyzing the CPU, RAM, and Storage activity of Instances and Hosts, |morpheus| can recommend actions for Sizing and Power State.

Configuration
-------------

Guidance is configured per Cloud and is set to off by default.

To turn on Guidance for a Cloud:

#. Navigate to `Infrastructure -> Clouds`.
#. Select the Edit icon of the Cloud to configure Guidance for.
#. Expand the `Advanced Options` section in the Edit Cloud modal.
#. In the *Guidance* dropdown, select Manual.
#. Select Save Changes.

Guidance recommendations will begin to appear in the guidance section when generated.

Recommendations
---------------

To view and act on Guidance recommendations, navigate to `Operations -> Guidance`.

The Guidance list contains the following details:

Severity Icon
  Indicates the severity of the recommended action.
Type
  Recommended action Type
Metric
  Guidance Metric used for recommended action.
Action
  Recommended Action for the Instance or Host, such as "Reduce Host memory" or "Shutdown Instance"
RESOURCE
  The Instance or Host targeted
SAVINGS
  Shows projected Monthly Costs savings if recommended action is taken.
DATE
  Date and Time stamp the recommended action was generated.
Information Link
  Click to view details on the recommendation.

.. NOTE:: Guidance Actions are not automatically triggered at this time.

Filters
-------

Search
  Search for Guidance recommendations
Type
  Filter by Sizing or Shutdown Guidance Types.
Severity
  Filter by Guidance Severity of All, Info, Warning, or Critical.
Metric
  Filter by All, Memory, CPU, or Power Guidance Metrics.
