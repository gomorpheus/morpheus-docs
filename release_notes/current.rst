.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. IMPORTANT:: There are a number of important considerations to make before upgrading to |morpheus| version 4.2.0. Please review our KnowledgeBase article on `upgrade considerations <https://support.morpheusdata.com/s/article/What-to-consider-before-upgrading-to-Morpheus-4-2-0?language=en_US>`_ and read the release notes below thoroughly.

New Features
============

UI Design Updates
-----------------

- Theme: New theme and styling for appliances which are not whitelabeled

Network Integration Enhancements
--------------------------------

- NSX-T
- Stealth

Clouds Integration Enhancements
-------------------------------

- Azure: Premium SSD disks can now be selected when provisioning or reconfiguring to add volumes
- Azure: Static IP addresses and IP pools can now be used with subnets, previously subnets defaulted to DHCP
- Azure: Kubernetes AKS version 1.15 replaces 1.13
- Google: Tag compliance policies are now supported for Google clouds, including scanning of existing resources and banner display for non-compliant machines
- Google: Added the ability to set a statically-assigned DHCP addresses when provisioning
- Oracle Cloud:
- SCVMM:
- OpenStack:

Tasks and Workflows
-------------------

- Tasks: For email-type Tasks, added an option to remove the |morpheus| email template and render only email content contained in the "CONTENT" field of the Task
- Tasks: For email-type Tasks, added a Source field to optionally use templates stored in a Git repository or outside URL destination
- Tasks: Git repository integration now supported for Shell, Powershell, and jRuby Task types

Other Enhancements
------------------

- Apps: The App owner can now be edited in Provisioning > Apps > (Selected App) > :guilabel:`EDIT`
- Blueprints: The Blueprint owner can now be edited or removed in Provisioning > Blueprints > :guilabel:`MORE` > Permissions
- Catalog: CentOS catalog items added for SCVMM, Hyper-V, and UpCloud Clouds
- Catalog: Amazon Linux 2 catalog items added
- Convert to Managed: When converting an instance to managed and specifying a Layout tied to custom options (Option Types), the user is prompted with the same options as when provisioning a new Instance with that Layout. If Option Types are configured as required, this validation is also honored when converting to managed
- Convert to Managed: Added the option to apply tags when converting an Instance to managed. Tag policy validation (if applicable) also applies
- Layouts: Layouts can now be scoped to Groups making the list of available Groups at provision time much smaller in appliances that have many
- Licenses: Version column added to the License list view in Administration > Provisioning > Licenses
- Option Lists: Option Lists can now be populated by LDAP queries
- Puppet: |morpheus| integration now supports version 6+
- Roles: Added "Reconfigure Servers" permission (Full or None) to User Roles. When set to None, the user cannot resize or reconfigure from Instance or server detail pages
- Security: Set web security HTTP response headers for enhanced security
- Settings: Added the option to disable SSH password authentication in Administration > Settings > Appliance
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
