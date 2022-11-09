.. _Release Notes:

*************************
|morphver| Release Notes
*************************

- Compatible Plugin API version: |pluginVer|
- Compatible Morpheus Worker version: |workerVer|

Release Dates
  - |morphVer|-1 |releasedate|

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version
.. .. include:: highlights.rst

New Features
============

:API & CLI: - Added API and CLI coverage for creating and working with Security Scan Jobs which was already possible from |morpheus| UI. :superscript:`5.5.2`
             - Added API and CLI coverage for creating and working with security package templates for security scans which is already possible via |morpheus| UI. :superscript:`5.5.2`
             - Added plugin upload capability for |morpheus| API and CLI. :superscript:`5.5.2`
:Currency: - Add support for Polish Zloty (PLN) currency. :superscript:`5.5.2`
:Jenkins: - The Jenkins integration has been deprecated and removed from the product. A Jenkins Task Plugin has been created for triggering Jenkins jobs. See share.morpheusdata.com for more details on that Plugin. :superscript:`5.5.2`
:Library: - Dark theme versions of Instance Type logos can now be managed via |morpheus| API and CLI. :superscript:`5.5.2`
:Session Manager: Morpheus features a new session manager that was necessary in order to resolve expiring connections from the agents due to a Spring framework update. This new session manager no longer requires Sticky Sessions and they can now be turned off at the load balancer if so desired. However, keeping them on is totally reasonable as well as it reduces overall system load. Rolling restarts no longer kick you out of your session if sticky sessions are off as it distributes your session data across the morpheus nodes in an HA environment. Additionally, overall system load is reduced as a result of the new session manager.
:Terraform: - Added data grouping to the Resource tab of the Detail page for Terraform Apps and Instances to make data more consumable in situations with large numbers of resources. :superscript:`5.5.2`


Fixes
=====

:API & CLI: - API endpoints for adding power schedules to Instances have been updated for intuitiveness and consistency. :superscript:`5.5.2`
             - Fixed an issue causing commands to get a Cloud or list Clouds within Subtenants to return incorrect Group IDs. :superscript:`5.5.2`
             - Fixed an issue that caused "Library Script" and "Library Template" type Tasks created via |morpheus| CLI not to be associated with the script or template resource indicated in the command. :superscript:`5.5.2`
             - Fixed an issue that caused Azure Instance resizing to fail when triggered via |morpheus| API or CLI. :superscript:`5.5.2`
             - Fixed an issue that caused the "providerType" query parameter for the Get All Cluster Types API call not to work properly. :superscript:`5.5.2`
             - The ``networkServer`` property is now being returned at the root of the return payload from calls to the Get All Clouds and Get a Specific Cloud API endpoints. :superscript:`5.5.2`
             - When sourcing an Option List from the |morpheus| Plans API, memory and storage fields now return data properly rather than null values. :superscript:`5.5.2`
:Amazon: - Fixed an issue that caused duplicate backups to occur for AWS Instances when scheduled backups were run. :superscript:`5.5.2`
          - Fixed an issue with Amazon AWS Security Group detail pages that caused the list of Instances associated with the SG to be blank. :superscript:`5.5.2`
:Apps: - Fixed an issue that caused only one Instance within an App to be displayed on the App detail page if the Instance contained many nodes (~25+). :superscript:`5.5.2`
:Azure: - Fixed an issue that caused Azure NSG source ports to be overwritten to the destination port value following Cloud sync. This issue affected only the port shown in |morpheus| UI, it did not actually make that change in the Azure backend. :superscript:`5.5.2`
         - Fixed an issue that could prevent Azure provisioning under specific scenarios if a stored credential set was used to authenticate the Cloud integration. :superscript:`5.5.2`
:Instances: - After renaming an Instance, the old Instance name no longer appears in the History tab of the Instance detail page. It is updated correctly. :superscript:`5.5.2`
             - Fixed an issue that could cause the wrong volume to be resized during reconfigure under specific plan settings. :superscript:`5.5.2`
             - Fixed an issue that prevented Instance detail pages from being opened for brownfield Instances which were converted to managed and in a delayed/pending delete state. :superscript:`5.5.2`
             - Fixed an issue where the listed size of an Instance disk could be incorrect following reconfigure that did not update disk size (though the disk was not actually resized). :superscript:`5.5.2`
:NSX-T: - Fixed an issue that caused creation of new NSX-T IP Pools to fail with errors. :superscript:`5.5.2`
:OpenStack: - Fixed an issue that allowed the root volume to be resized for OpenStack Windows VMs in |morpheus| in some scenarios which shouldn't have been allowed. :superscript:`5.5.2`
             - Fixed an issue that caused OpenStack Clouds scoped to all Projects to sync duplicate Virtual Images. :superscript:`5.5.2`
             - Fixed an issue that caused new OpenStack instance names not to be synced back to |morpheus| when updated on the OpenStack side. :superscript:`5.5.2`
:Terraform: - Fixed an issue that caused Terraform Apps created via imported state not to transition from a "deploying" to "running" state even after they were successfully provisioned. :superscript:`5.5.2`
             - Fixed an issue that led to large Terraform Apps causing the web browser tab to consume large amounts of memory and crash. :superscript:`5.5.2`


Appliance & Agent Updates
=========================

:Guacd: - libssh2 updated to v1.10.0 to address Ubuntu 22.04 ssh issue. Note: Appliances on SLES15 may need openssl-devel manually installed for guacd to succesfully compile.