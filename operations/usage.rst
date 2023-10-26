Usage
-----

The `Operations > Costing > Usage` section shows billing information for Instances and hosts that have pricing configured on their Service Plan.

.. IMPORTANT:: Pricing must be enabled in |AdmSetPro| and Service Plans configured with price sets in |AdmPla| for pricing to show in the Usage section.

View Usage
^^^^^^^^^^

All Instances, discovered resources, virtual images, snapshots are listed by default, with the most recent usage information showing first. When additional details are available, usage records will display a small arrow on the left side of the row. Click this arrow to expand the details for that usage record. Details can include more granular cost breakdowns, such as specific CPU, memory, and/or storage costs for containers (Instances).

Usage records can be filtered by Cloud, type and date:

Cloud
  Default view is for all Clouds. Select a Cloud to show Instance, host and other usage for only one Cloud.
Date
  Default view shows most current Usage. Select the Date filter to scope to a different date range.
Type
  All usage record types are shown by default, select a specific type to filter the list to just one

Example:
  Below is an example of a discovered instance from AWS, which shows different usage periods and the pricing that would be related.  In this case, 
  the compute and storage are used to calculate the Usage Price when the instance is **Running** but only the storage when the instance is **Stopped**:
  
  .. image:: /images/operations/usage_example.png

API & CLI
^^^^^^^^^

Usage information can also be extracted via the |morpheus| API and CLI, including the ability to extract usage per Tenant.

.. NOTE:: Appropriate Role permissions for `Operations: Usage` are required to view the Usage section.
