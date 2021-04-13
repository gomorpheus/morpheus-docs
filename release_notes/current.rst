.. _Release Notes:

************************
|morphver| Release Notes
************************

.. include:: highlights.rst

New Features
============

- NSX-T: Visibility permissions added to NSX-T integrations allowing master tenant administrators to share integrations with subtenants
- NSX-T: Distributed firewalls for NSX-T integrations shared with a subtenant can now be created and managed by subtenant users
- NSX-T: Load balancers and LB virtual servers for NSX-T integrations shared with a subtenant can now be created and managed by subtenant users
- NSX-T: Load balancer rule creation capability added as part of load balancer virtual server creation in |morpheus| UI
- NSX-V: Visibility permissions added to NSX-V integrations allowing master tenant administrators to share integrations with subtenants
- Security: `Two-factor authentication <https://docs.morpheusdata.com/en/5.2.5/administration/user_settings/user_settings.html#factor-authentication>`_ added for |morpheus| local accounts as well as users from Active Directory and LDAP identity sources
- Settings: Add IP addresses or hostnames to approved or denied lists which limits users to only approved sources when creating HTTP Tasks or populating Option Lists through REST calls. Previously, specific hosts could be denied but now administrators can opt to deny all hosts except those which are specifically approved

|morpheus| API Improvements
===========================

- Plans: Remove Service Plans through API (and CLI) as can already be done in |morpheus| UI

Fixes
=====

- App: Fixed error messages that contained database exception response
- Backups: Fixed default schedule displayed on backup screen when no job schedule is configured
- Cloud-init: Fixed multiple Default Gateway flags when creating multiple networks
- Identity Sources: Fixed Get Token API call with custom SSO URL returning 500 instead of 404 if the user do not exists 
- NSX-T: Fixed network delete when network is part of a network group
- Service Catalog: Option Types:  Fixed VISIBILITY FIELD not respecting``matchAll`` logic
- Snapshots: Fixed revert action failing on Brownfield Snapshots when compute_server moved to another tenant
- VMware: Folders: Fixed Group Access -> Default Folder setting only saving for one cloud when multiple VMware Clouds are in the same target Group

.. 

  Agent/Node Package Updates
  ==========================


  Installer Updates
  =================
