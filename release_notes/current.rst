.. _Release Notes:

*************************
|morphver| Release Notes
*************************

- Compatible Plugin API version: |pluginVer|
- Compatible Morpheus Worker version: |workerVer|

.. IMPORTANT:: |morpheus| 5.4.9+ adds the "Provisioning: State" Role permission. This permission determines access to the State tab for Terraform-backed Instances and is set to "None" by default. On upgrade from a version prior to 5.4.9, only System Admin users will be able to see the State tab for these Instances. For other users who should have this access, edit their Roles to include "Provisioning: State" permissions.

.. .. important::  Security: CVE-2022-35912: Morpheus v5.5.1-2 and v5.4.8-2 are now available in response to CVE-2022-35912, a Grails Framework remote code execution vulnerability. v5.5.1-2 and v5.4.8-2 include the Grails v5.1.9 update that mitigates the vulnerability. At this time, the Grails vulnerability is only confirmed for grails frameworks running on Java 8. Morpheus versions v5.4.4 and higher are on Java 11. Customers on morpheus v5.4.3 or earlier are highly advised to upgrade to at minimum v5.4.4 or higher, and out of an abundance of caution we recommend all customers upgrade to v5.5.1-2 or v5.4.8-2 in the event the vulnerability is found to be exploitable on Java 11.

Release Dates
  - |morphVer|-1 |releasedate|

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version

New Features
============

:API & CLI: - Create and manage Scale Thresholds (Library > Automation > Scale Thresholds) from |morpheus| API and CLI. :superscript:`5.5.2`
             - Improved |morpheus| API and CLI response related to networks including the addition of Search Domains when getting Networks and setting/updating Search Domains. :superscript:`5.5.2`
:Oracle Cloud: - Oracle Cloud costing features have migrated from using the Cloud Metered Billing API to using Cost and Usage Report data. :superscript:`5.5.2`
:SAML: - When creating a new SAML integration, the default SAML REQUEST value is now "Self-Signed" and the default SAML RESPONSE value is now "Validate Assertion Signature" to prevent unintentional insecure configuration. :superscript:`5.5.2`
:Security: - xmlrpc-common upgraded to version 3.1.3 (CVE-2019-17570). :superscript:`5.5.2`


Fixes
=====

:API & CLI: - Fixed an issue that could cause provisioning of Azure Marketplace images through |morpheus| API to fail depending on marketplaceOffer syntax used. :superscript:`5.5.2`
             - Fixed an issue with adding Oracle Cloud Instances via |morpheus| CLI which would fail due to a missing Availability Zone prompt. :superscript:`5.5.2`
:Amazon: - Fixed an issue that caused provisioning the |morpheus|-default AWS Ubuntu 22.04 image to fail. :superscript:`5.5.2`
          - When provisioning a Windows Instance to AWS, hostnames longer than 15 characters are now truncated down to 15. This is to resolve an issue preventing backup restoration if the hostname was too long. :superscript:`5.5.2`
:Ansible Tower: - Fixed an issue that caused Ansible Tower sync to break if templates with certain configurations are deleted via |morpheus|. :superscript:`5.5.2`
:Ansible: - Ansible scripts now work when applied against the Instance level, previously these would fail but would be successful when run against the server level. :superscript:`5.5.2`
:Automation Workflows: - Fixed an issue that caused Post Provision-phase to be executed twice on ARM template-based Instances. :superscript:`5.5.2`
:Catalog: - Fixed an issue that could cause a Catalog Item to lose Inputs during ordering if it was built and ordered under specific conditions. :superscript:`5.5.2`
           - Fixed an unintended permissions-related issue that would cause a 500 error when browsing |ProCat| even if the user had required permissions. :superscript:`5.5.2`
           - Hidden-type Inputs are no longer shown on the order review page when checking out selected Service Catalog items. :superscript:`5.5.2`
:Currency: - Currency exchange sync now honors any configured proxies. :superscript:`5.5.2`
:Inputs: - Select List-type Inputs which have dependent refresh based on another Input no longer make the identical refresh call twice. :superscript:`5.5.2`
:Instances: - Fixed an issue that caused Instance counts not to be set correctly on the Instances list page when the user has no Group access. :superscript:`5.5.2`
:Kubernetes: - Plan is now hidden as expected when adding an external Kubernetes cluster from a Subtenant. :superscript:`5.5.2`
:NSX-T: - Fixed a CIDR validation issue on IPv6 networks which caused a number of issues and prevented networks from being saved with changes. :superscript:`5.5.2`
:NetScaler: - When |morpheus| deletes a virtual server from NetScaler, it now also deletes the certificate. :superscript:`5.5.2`
:Network: - Fixed an issue that caused CSV export on several Network list pages (Networks, Network Groups, Domains, etc.) to fail. :superscript:`5.5.2`
:ServiceNow: - |morpheus| now updates the state of created ServiceNow RITMs when a provision approval policy holds up provisioning. After approval or denial, the state will change to "Closed Complete" or "Closed Incomplete". :superscript:`5.5.2`
:Tags: - General validation improvements made to tags, such as setting max tag name lengths based on specific cloud requirements and validating for disallowed characters. :superscript:`5.5.2`
:Terraform: - Fixed an issue that caused Cypher entries at the tfvar mount point not to show up correctly under the Profiles tab for the target Cloud. :superscript:`5.5.2`
             - Improved the handling of adding tags to VMs associated with Terraform Apps as previously the added tags would make the Apps always in a drift state. :superscript:`5.5.2`
             - Removing a Spec Template from a new Terraform App Blueprint draft will no longer close the New App Blueprint modal entirely. :superscript:`5.5.2`
             - 5.4.11-2 fixes 5.4.11-1 issue with existing terraform instances and duplicate files in morpheus-local/repo/local paths after upgrading to 5.4.11-1. :superscript:`5.4.11-2`
:Users: - Fixed an issue that stopped CSV exports of Users and User Group lists from executing correctly. :superscript:`5.5.2`
         - When creating new |morpheus| users, a dash (-) is now counted as a symbol for purposes of password complexity. :superscript:`5.5.2`
:VMware: - VMware Clouds scoped to a specific Resource Pool will now only inventory VMs from that Resource Pool and will only display that Resource Pool in the Resources section. :superscript:`5.5.2`
         - 5.4.11-2 fixes 5.4.11-1 cloud and server status issues for VMware clouds. :superscript:`5.4.11-2`
