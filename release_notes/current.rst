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
- Security: Two-factor authentication added for |morpheus| local accounts
- Settings: Add IP addresses or hostnames to approved or denied lists which limits users to only approved sources when creating HTTP Tasks or populating Option Lists through REST calls. Previously, specific hosts could be denied but now administrators can opt to deny all hosts except those which are specifically approved

|morpheus| API Improvements
===========================



Fixes
=====



Agent/Node Package Updates
==========================

- RHEL 8 and CentOS 8 Agent install support added for Instances and Hosts
- Ubuntu 20 Agent install support added for Hosts
