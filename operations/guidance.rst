Guidance
========

Overview
--------

The ``Operations > Guidance`` section shows recommendations for resource and cost optimization. By analyzing the CPU, RAM, and Storage activity of Instances and Hosts, |morpheus| can recommend actions for sizing and power state. Guidance is customizable to show recommendations based on 30, 60, or 90 day periods, this dropdown toggle is visible on the Guidance list page (Operations > Guidance). Guidance thresholds are also customizable, they can be edited in |AdmSetGui|.

Configuration
^^^^^^^^^^^^^^

Guidance is configured per Cloud and is turned off by default.

To turn on |morpheus| Guidance for a Cloud:

#. Navigate to `Infrastructure > Clouds`
#. Click :guilabel:`EDIT`
#. Expand the `Advanced Options` section in the Edit Cloud modal
#. In the *Guidance* dropdown, select Manual
#. Click :guilabel:`SAVE CHANGES`

Guidance recommendations will begin to appear in the guidance section when generated.

Once Guidance has been turned on for a Cloud, |morpheus| will determine if a guidance recommendation should be made once every 30 minutes. In the event that no recommendations can be made, no entry will be added to the list of suggested guidances. As the guidance list continues to grow, sorting and filtering may become necessary to focus on the recommendations that are relevant to the user at the time.

It's important to note that acting on recommendations is entirely manual at this time. In many cases, Morpheus provides one-click action to take the recommended steps but Guidance recommendations cannot be taken automatically. This is a feature that is being explored for a future update but has not been tagged for any specific release version at this time. In addition, it's recommended that |morpheus| Agent be installed to maximize the benefits of Guidance. While Guidance will still work without installing the Agent, the greatly-enhanced statistics provided by the Agent will significantly improve Guidance recommendations.

To see more detail on a Guidance recommendation in your list, click on the (i) button at the far right side of each list row. This will open a detail modal that gives additional information on the Guidance entry. In some cases, such as with sizing and shutdown recommendations, the user can simply click the "EXECUTE" button to take the recommended action as shown below.

.. image:: /images/operations/guidance/sizingexecute.png
  :width: 80%
  :alt: The execute button allows the user to immediately take action on a sizing recommendation
  :align: center

Other types of Guidance recommendations, such as reserve compute recommendations, must be taken in the cloud and Morpheus does not offer the execute button.

.. image:: /images/operations/guidance/reservecompute.png
  :width: 80%
  :alt: The execute button is not present on a reserve compute recommendation
  :align: center

.. NOTE:: The IGNORE button will remove the recommendation from the UI. Subsequent recommendations of the same type will NOT display for the same object (VM, Cloud etc) again unless the original recommendation is resolved.

Recommendations
^^^^^^^^^^^^^^^^^^

To view and act on Guidance recommendations, navigate to `Operations > Guidance`.

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
^^^^^^^^^^

Search
  Search for Guidance recommendations
Type
  Filter by Sizing or Shutdown Guidance Types.
Severity
  Filter by Guidance Severity of All, Info, Warning, or Critical.
Metric
  Filter by All, Memory, CPU, or Power Guidance Metrics.
