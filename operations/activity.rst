Activity
========

The Activity section displays a recent activity report for Auditing. |morpheus| defines an activity as any major action performed on an instance or server, such as, but not limited to adding a server, deleting a server, provisioning an instance, deleting an instance, creating a backup, etc… This view can be searched and filtered by type, user, and date range.

Activity
--------

There are 5 types of activities that are displayed in the Activity Reports:

- Provisioning
- Monitoring
- Alert
- Backups
- Logs

**To View a Recent Activity report:**

#. Select the Reports link in the navigation bar.
#. Click the tab Recent Activity.

Recent activity is displayed in order from recent to oldest. This view can be searched and filtered by type, user, and date range.

**Review**

To review the item the activity occurred on, click the name of the activity and it will go to a new page and display that item.

.. NOTE:: Deleted activities are displayed as an alert and do not contain a link to the event item. If the activity is not a deletion event we provide a link on the activity name to go to the item the activity occurred on.

**To Filter:**

#. Click the filter drop down of type of filter you want to apply.
#. Select the appropriate filter.

Usage
-----

Overview
^^^^^^^^

The `Operations -> Usage` section shows Billing information for Instances and Hosts that have pricing configured on their Service Plan.

.. IMPORTANT:: Pricing must be enabled ins `Administration -> Provisioning` and Service Plans configured with Prices sets in `Administration -> Plans & Pricing` for Pricing to show in the Usage section.

View Usage
^^^^^^^^^^

All Instances are listed by default, with the most recent usage information showing first.

Usage details can be filtered by Cloud and Date:

Cloud
  Default view is for all Clouds. Select a Cloud to show Instance and Host Usage for only one Cloud.
Date
  Default view shows most current Usage. Select the Date filter to scope to a different date range.

API & CLI
^^^^^^^^^

Usage information can also be extracted via the |morpheus| API and CLI, including the ability to extract usage per Tenant.

.. NOTE:: Appropriate Role permissions for `Operations: Usage` are required to view the Usage section.

History
-------
