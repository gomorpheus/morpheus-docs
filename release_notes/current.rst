.. _Release Notes:

*************************
|morphver| Release Notes
*************************

- Compatible Plugin API version: |pluginVer|
- Compatible Morpheus Worker version: |workerVer|

Release Dates
  - |morphVer|-1 |releasedate|

.. NOTE:: Items appended with :superscript:`6.0.0` are also included in that version

New Features
============

:Catalog: - Self-service catalog Workflows now include the option for Inputs and the addition of a custom config body as Workflows already did in the Standard Persona :superscript:`6.0.0`
:Kubernetes: - Added Kubernetes 1.26 support and added default 1.26 cluster layouts for supported Clouds :superscript:`6.0.1`


Fixes
=====

:API & CLI: - The ``make-managed`` CLI call and underlying API call will now properly set tags on the new managed Instance :superscript:`6.0.1`
             - The ``openapi`` endpoint to |morpheus| API now requires authentication since it returns the current appliance version :superscript:`6.0.0`
:Amazon: - Improved Amazon AWS costing sync to better account for child accounts underneath a management account :superscript:`6.0.1`
:Costing: - Fixed a few issues related to prices vs costs (cost could be higher than price) and improved the accuracy of MTD and projection costs :superscript:`6.0.1`
:Identity Sources: - LDAP identity sources now honor a configured global proxy (if present)
                  - The |morpheus| LDAP integration is now compatible with OpenLDAP :superscript:`6.0.1`
:Inputs: - Fixed an issue that caused reads from multi-select typeahead Inputs to return a list containing a null item at the start :superscript:`6.0.1`
:Morpheus IP Pools: - The MORE pop-out menu on the IP Pools list page (|InfNetIP|) now fully appears without being cut off :superscript:`6.0.0`
:Option Lists: - Using ``zoneId`` to filter |morpheus| API-type Option Lists now works correctly :superscript:`6.0.1`
:Policies: - Adding a network to a Subtenant which would cause it to exceed its network quota Policy now fails with a friendly error message rather than throwing a less helpful 500 (threw a gasket) error :superscript:`6.0.1`
:ServiceNow: - ServiceNow integrations now include an "API Proxy" setting. If configured, ServiceNow integration traffic will be routed through the indicated proxy. If no proxy is configured, ServiceNow traffic will route through a global proxy if one is configured :superscript:`6.0.0`
:Terraform: - Fixed an issue that caused Terraform Instances to be removed from |morpheus| even when the destroy action actually failed which led to orphaned instances left behind in the cloud :superscript:`6.0.1`
             - Fixed an issue that prevented applying state in |morpheus| on Terraform 0.12.31 Apps :superscript:`6.0.1`
             - Improvements added to the HCL parser to account for edge cases that didn't work properly :superscript:`6.0.1`
:UI: - Fixed a UI display issue that could cause the |morpheus| Role names and Active Directory group name fields to overlap each other when adding or editing an Identity Source integration :superscript:`6.0.1`