Usage
-----

The `Operations > Costing > Usage` section shows billing information for Instances and hosts that have pricing configured on their Service Plan.

.. IMPORTANT:: Pricing must be enabled in |AdmSetPro| and Service Plans configured with price sets in `|AdmPla|` for pricing to show in the Usage section.

View Usage
^^^^^^^^^^

All Instances are listed by default, with the most recent usage information showing first.

Usage details can be filtered by Cloud and date:

Cloud
  Default view is for all Clouds. Select a Cloud to show Instance and host usage for only one Cloud.
Date
  Default view shows most current Usage. Select the Date filter to scope to a different date range.

API & CLI
^^^^^^^^^

Usage information can also be extracted via the |morpheus| API and CLI, including the ability to extract usage per Tenant.

.. NOTE:: Appropriate Role permissions for `Operations: Usage` are required to view the Usage section.
