.. _Release Notes:

************************
|morphver| Release Notes
************************

.. include:: highlights.rst

New Features
============

- Network: Change network for Instances and servers via reconfigure. Previously, network details were read-only during a reconfigure
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



.. Below items no longer tagged for 5.2.5
  Agent/Node Package Updates
  ==========================

  - RHEL 8 and CentOS 8 Agent install support added for Instances and Hosts
  - Ubuntu 20 Agent install support added for Hosts

  Installer Updates
  =================

  - Installer now removes old package versions from ``var/opt/morpheus/package-repos`` on reconfigure once they are no longer needed. Previously these could be removed manually to free up space but they were not removed automatically and could take significant space in some scenarios
