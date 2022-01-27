.. _Release Notes:

************************
|morphver| Release Notes
************************

Release Date: |releasedate|

.. important:: |morpheus| v5.2.11-2 contains important security updates. v5.2.11-1 is no longer available and it is recommended to update from v5.2.11-1 to v5.2.11-2

.. No highlights this time, small update
  .. include:: highlights.rst

New Features
============

:Dashboard: - Added performance improvements for |morpheus| Dashboard (UI and calls to the Dashboard API) in specific scenarios where |morpheus| is managing a very high number of workloads
:NSX: - Source and destination IP addresses for distributed firewall rules (of any category) are now synced back to |morpheus|
      - Added UI tab for NSX-T Groups (Infrastructure > Networks > Integrations > Selected NSX-T integration > Groups tab) and capabilities for creating an managing Groups from this tab
      - Sync, create and manage NSX-T DHCP servers
      - Added support for configuring DHCP on NSX-T routers. When adding or editing an NSX-T router (Infrastructure > Networks > Routers > Selected NSX-T router > EDIT button), expand the IP address management section and configure DHCP options
      - Sync, create and manage NSX-T DHCP relays
      - Added UI tab for NSX-T DHCP management (Infrastructure > Networks > Integrations > Selected NSX-T integration > DHCP tab)
:SMS: - Twilio SMS Settings added to ``Administration -> Settings -> Provisioning`` for configuring Twilio account for monitoring incident alert SMS notifications
:UI: - After receiving a password reset email and submitting the form to reset the password, the user is redirected to the login screen rather than logged into the product. This ensures two-factor authentication is still honored if set.
     - Errors are now surfaced into the History tab of the Instance detail page if issues occur when taking Snapshots in supported Clouds


Fixes
=====

:Amazon: - Updates made to base Ubuntu 18 image for AWS
:API/CLI: - Message of the Day (MOTD)-type Policies are now returned when issuing GET requests for policies
          - When issuing GET calls for specific Instances, controller information is now populated in the response
:Apps: - Fixed an issue where App Instances would default to one CPU core at provision time rather than the default number of CPU cores indicated on the Blueprint
:Azure Stack: - Removed the ability to select certain unsupported disk types from the provisioning wizard. Selecting these types would cause the provisioning to fail if the user did not know those types were not allowed
:Blueprints: - The expand and contract button for configuration options now works correctly. Previously it defaulted to the expanded state and could not be contracted
:Buckets: - Fixed an issue that could cause non-Amazon S3 buckets to fail on creation when specific string sequences were contained in the endpoint URL
:ESXi: - The number of CPU cores on discovered ESXi VMs is now synced correctly
:Groups: - Fixed an issue where Groups with no assigned Clouds would be able to see managed and discovered VMs in any Cloud
:Guidance: - Corrected an issue that would cause incorrect guidance to be given for Azure Instances
:KVM: - Instance state no longer goes to "unknown" under certain conditions when refreshing a KVM cloud
:Network: - Added validation to API calls to create or edit network proxies to ensure names are unique
          - Corrected an issue where network changes would not be made after reconfiguring from the VM detail page. Reconfiguring from the Instance detail page worked fine
          - Fixed an issue causing network groups not to be handled properly on Instance or VM reconfigure
          - Fixed an issue that caused old IP addresses not to be freed up in some scenarios when a new network and IP pool was selected on Instance reconfigure
          - Fixed an issue that caused Tenant permissions not to be set up properly for subnets in Subtenants
:NSX-T: - Certain errors are no longer surfaced into the logs when NSX-T integrations are refreshed
        - Certain errors are no longer triggered when NSX-T integrations are refreshed
        - Created NSX-T load balancer profiles are now selectable from virtual servers
:Nutanix: - Improved process for cleaning up IP pools when Nutanix clouds are deleted
:OpenStack: - When reconfiguring OpenStack Instances with multiple disks, disks no longer change size without user input in certain scenarios
:Option Lists: - Morpheus user objects and object attributes are now accessible in LDAP-type Option Lists
:Oracle Cloud: - Fixed an issue that could cause Morpheus Agent to not be installed on Windows boxes in Oracle cloud
:Plans & Pricing: - Corrected an issue that caused Plans to appear differently when reconfiguring from the server detail page vs the Instance detail page
                  - Fixed an issue where reconfigure changes were not saved when the only change made was upgrading the plan
:Provisioning: - Fixed issue with $sequence variable reiteration on 35 when using copies and "Reuse Naming Sequence Numbers" is enabled.
:Proxies: - Fixed an issue preventing proxies from being set correctly on SLES and OpenSUSE
:Reports: - Fixed an issue where Reports or Analytics dashboards could show clouds as having more discovered VMs than they would actually show from the Cloud detail page
:Security: - v5.2.11-2 contains important security updates. v5.2.11-1 is no longer available and it is recommended to update from v5.2.11-1 to v5.2.11-2
           - Hid passwords to some Morpheus-owned service accounts (Twilio, Postmark, etc.) which were shared previously in ``application.groovy`` but are no longer needed by customers
           - The Tenant name and database ID are no longer shown in the return payload when sending a POST request to initiate a new user session
:ServiceNow: - Fixed an issue where the workflow indicated on a ServiceNow approval policy would not be honored during App provisioning
             - When exposing a Cloud to a new ServiceNow integration for provisioning which already has a CMDB server association, this association is no longer overwritten to set the new ServiceNow appliance as the Cloud's associated CMDB
:Tags: - Fixed an issue that could cause existing tags to be wiped out when manually adding new tags via the UI after provisioning
:Tasks: - Additional validation added when editing a Task to ensure the Task name is still unique prior to attempting to save changes. This change prevents 500 errors if the Task name has been editing to no longer be unique
        - Fixed an issue causing Ansible Tasks to fail and Morpheus UI to crash if the Ansible integration is connecting to Git over SSH during Task execution
        - Fixed an issue that caused remote-target Tasks to always fail under specific conditions
:vCloud Director: - Certain errors are no longer surfaced into the logs when vCD clouds are refreshed
                  - Fixed an issue where editing Instances in vCD clouds would cause 500 errors (though the changes would be successfully saved)
                  - When reconfiguring vCD Instances with multiple disks, disks no longer change size without user input in certain scenarios
:Veeam: - Disabled Veeam backup integrations will no longer appear as backup targets in Instance and App provisioning wizards
:Virtual Images: - Fixed an issue where Virtual Image conversion processes would consistently fail under certain conditions
:VMware: - Fixed a sporadic issue where automatic downscale features could leave VMs in vCenter despite being removed from Morpheus
         - Fixed an issue that caused Instance snapshots not to be deleted properly
         - Fixed an issue that caused VMware clouds with only discovered VMs and Snapshots to not delete properly
         - Fixed an issue that could cause folder and resource pool selections not to be honored and the VM provisioned into the datacenter root in very specific scenarios
         - Fixed an issue where reconfiguring Instances with many disks could cause the individual disks to report incorrect sizes requiring the user to input them manually prior to executing the reconfigure
:Whitelabel: - Fixed an issue that caused the filename of the primary Tenant logo image to appear in the Subtenant settings are even if the Subtenant had successfully applied their own logo image (which displays correctly)
:XenServer: - Fixed an issue where networks were not changed correctly when reconfiguring Xen Instances to change networks


Appliance & Agent Updates
=========================

:Appliance: - Optimizations added to improve page load times

|
