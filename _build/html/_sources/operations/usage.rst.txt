Usage
=====

Overview
--------

The `Operations -> Usage` section shows Billing information for Instances and Hosts that have pricing configured on their Service Plan.

.. IMPORTANT:: Pricing must be enabled ins `Administration -> Provisioning` and Service Plans configured with Prices sets in `Administration -> Plans & Pricing` for Pricing to show in the Usage section.

View Usage
----------

All Instances are listed by default, with the most recent usage information showing first.

Usage details can be filtered by Cloud and Date:

Cloud
  Default view is for all Clouds. Select a Cloud to show Instance and Host Usage for only one Cloud.
Date
  Default view shows most current Usage. Select the Date filter to scope to a different date range.

API & CLI
---------

Usage information can also be extracted via the |morpheus| API and CLI, including the ability to extract usage per Tenant.

.. NOTE:: Appropriate Role permissions for `Operations: Usage` are required to view the Usage section.
