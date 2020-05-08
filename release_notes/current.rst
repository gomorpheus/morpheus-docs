.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. IMPORTANT:: There are a number of important considerations to make before upgrading to |morpheus| version 4.2.0. Please review our KnowledgeBase article on `upgrade considerations <https://support.morpheusdata.com/s/article/What-to-consider-before-upgrading-to-Morpheus-4-2-0?language=en_US>`_ and read the release notes below thoroughly.

New Features
============

UI Design Updates
-----------------

Network Integration Enhancements
--------------------------------

- NSX-T
- Stealth

Clouds Integration Enhancements
-------------------------------

- Azure: Premium SSD disks can now be selected when provisioning or reconfiguring to add volumes
- Azure: Static IP addresses and IP pools can now be used with subnets, previously subnets defaulted to DHCP
- Google: Tag compliance policies are now supported for Google clouds, including scanning of existing resources and banner display for non-compliant machines
- Google: Added the ability to set a statically-assigned DHCP addresses when provisioning
- Oracle Cloud:
- SCVMM:
- OpenStack:

Tasks and Workflows
-------------------

- Tasks: For email-type Tasks, added an option to remove the |morpheus| email template and render only email content contained in the "CONTENT" field of the Task
- Tasks: For email-type Tasks, added a Source field to optionally use templates stored in a Git repository or outside URL destination

Other Enhancements
------------------

- Catalog: CentOS catalog items added for SCVMM, Hyper-V, and UpCloud Clouds
- Catalog: Amazon Linux 2 catalog items added
- Licenses: Version column added to the License list view in Administration > Provisioning > Licenses
- Puppet: |morpheus| integration now supports version 6+
- Security: Set web security HTTP response headers for enhanced security
- Users and Roles: Added view accessible from the User list view to see an individual User's effective Role permissions

API Enhancements
================

CLI Updates
===========

Fixes
=====

CVEs Addressed
==============

Services
========
