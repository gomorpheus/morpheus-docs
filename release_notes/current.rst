.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade versions: Rolling: |minRollingUpgradeVer| Non-rolling: |minUpgradeVer|

.. NOTE:: Items appended with :superscript:`7.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

.. _Release Notes:

*************************
|morphver| Release Notes
*************************

New Features
============

:API & CLI: - "Use Agent Communications" can be toggled on Kubernetes clusters via |morpheus| API and CLI as can already be done via UI :superscript:`7.0.10`
            - Added Virtual Image convert functionality to |morpheus| API and CLI :superscript:`7.0.10`
            - Fixed a bug that prevented provisioning new Kubernetes clusters using |morpheus| CLI under certain configurations
:HPE VM: - Added VMDK image support for HPE VM clusters. When provisioning the "HPE VM" Instance Type, VMDK images are now selectable. |morpheus| performs the conversion to QCOW on the fly once the image is selected
:NSX: - Added an "Apply VM tags" checkbox to NSX integrations. VM tags are only applied to VMs in NSX when the box is checked :superscript:`7.0.10`
      - Tags can now be applied to VMs in NSX in addition to the tag functionality for VMs in vCenter which already existed in |morpheus| :superscript:`7.0.10`
:Plugins: - Added generalized improvements to bare metal-type plugins. See the developer documentation for more details :superscript:`7.0.10`


Fixes
=====

:API & CLI: - Fixed a number of issues that prevented the ``clouds add`` CLI command from working properly :superscript:`7.0.10`
             - Provisioning Apps via |morpheus| API now works when only a Group ID is given rather than also requiring a Group name :superscript:`7.0.10`
             - The ``catalog-item-types`` API now has improved error handling when passing invalid parameters :superscript:`7.0.10`
             - The interactive login prompt for |morpheus| CLI no longer fails when a command using the "dry run" switch and requiring authentication is entered
             - Updating the Clouds associated with a Group via |morpheus| API is now working properly :superscript:`7.0.10`
             - When ordering Catalog Items via |morpheus| API, ``customOptions`` which would be populated via select list in the UI are now validated :superscript:`7.0.10`
             - When working with a Cicso ACI integration through |morpheus| API, the option to list Tenants for scoping the integration now correctly lists Tenants :superscript:`7.0.10`
             - |morpheus| API calls to delete volumes associated with Kubernetes clusters now work correctly :superscript:`7.0.10`
:Amazon: - Creating buckets set to all regions and associated actions (creating and deleting files, deleting the bucket, etc) now work correctly :superscript:`7.0.10`
          - When AWS Clouds are scoped to just one region, only buckets from that region are shown in |StoBuc| :superscript:`7.0.10`
:Apps: - Fixed Instances shared across multiple Apps being deleted when one App is deleted if that App is covered by a delete approval Policy :superscript:`7.0.10`
        - For Terraform Apps, the Virtual Machines button under the Instances tab on the App detail page is now working :superscript:`7.0.10`
:Azure: - Availability zones for the Norway East (norwayeast) region are now supported :superscript:`7.0.10`
         - Fixed Azure Instances failing to restore when assigned to an Availability Zone :superscript:`7.0.10`
:Blueprints: - After changing config type from Terraform Specs to Terraform (.tf), the App no longer fails due to duplicate code :superscript:`7.0.10`
:Compute: - The resources list (Infrastructure > Compute > Resources) can now be sorted by the type column properly :superscript:`7.0.10`
:Forms: - Fixed datastores not always loading within Disk-type Inputs on Forms :superscript:`7.0.10`
:Import/Export: - Fixed Catalog Items exporting without any configuration when they were exported by Label :superscript:`7.0.10`
:Instances: - An Instance being suspended is now shown in Instance History :superscript:`7.0.10`
             - The default MySQL Instance Type now shows the correct MySQL version on the Instance detail page following provisioning :superscript:`7.0.10`
:Kubernetes: - Fixed "Run Workload" actions failing when run against External Kubernetes clusters :superscript:`7.0.10`
              - Instances deployed to External Kubernetes clusters no longer go into "Unknown" status after the first Cloud sync and the progress bar on the "Stop Server" action no longer gets stuck :superscript:`7.0.10`
              - When adding external Kubernetes clusters to |morpheus|, control plan nodes are now recognized correctly and not seen as worker nodes :superscript:`7.0.10`
              - Worker node counts are now updated properly when Kubernetes clusters are expanded as a result of auto-scaling :superscript:`7.0.10`
:NSX: - The edit policy modal now loads successfully in |morpheus| if the name of the firewall rule is a number rather than a text string :superscript:`7.0.10`
:Nutanix Prism Central: - Appended the cluster name to datastore options in the provisioning wizard to help the user select compatible cluster and datastore options :superscript:`7.0.10`
:Plugins: - Fixed custom tabs defined by plugin without their own permissions being affected by additional custom tabs which do have defined custom permissions :superscript:`7.0.10`
:Settings: - Updated the input validation on the global "No Proxy" setting to prevent the rejection of some valid inputs :superscript:`7.0.10`
:Tasks: - Fixed an issue where one-off Task runs triggered from an Instance detail page for a Terraform-created Instance would not be run and also would not appear in the Instance History tab :superscript:`7.0.10`
:Workflows: - The platform check ensuring Workflows only run against compatible platforms now works properly when multiple Instances are selected :superscript:`7.0.9 `


Appliance & Agent Updates
=========================

:Appliance: - Appliance Tomcat upgraded to 9.0.98 :superscript:`7.0.10`
:Node Packages: - Updated to v3.2.32 with fix for SLES 15 Morpheus Node package installation dependency error :superscript:`7.0.10`
:Embedded Plugins: - Efficient IP plugin updated to v1.2.6 :superscript:`7.0.10`
                   - Rubrik plugin updated to v2.0.0 :superscript:`7.0.10`
:Tomcat: - Embedded Tomcat updated to v9.0.98 :superscript:`7.0.10`