.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. NOTE:: Features appended with :superscript:`5.2.4` or :superscript:`5.2.5` debuted previously in the 5.2.x LTS version

.. include:: highlights.rst

New Features
============
- GCP: 
- Library: Canonical MaaS and Lumen Edge are now selectable as technology types for Library items such as Layouts and Node Types :superscript:`5.2.4`
- NSX-T: Visibility permissions added to NSX-T integrations allowing master tenant administrators to share integrations with subtenants :superscript:`5.2.5`
- NSX-T: Distributed firewalls for NSX-T integrations shared with a subtenant can now be created and managed by subtenant users :superscript:`5.2.5`
- NSX-T: Load balancers and LB virtual servers for NSX-T integrations shared with a subtenant can now be created and managed by subtenant users :superscript:`5.2.5`
- NSX-T: Load balancer rule creation capability added as part of load balancer virtual server creation in Morpheus UI :superscript:`5.2.5`
- NSX-V: Visibility permissions added to NSX-T integrations allowing master tenant administrators to share integrations with subtenants :superscript:`5.2.5`
- NSX-V: Configure DHCP and DHCP log levels on Edge Gateways :superscript:`5.2.4`
- NSX-V: Create and manage DHCP Pools for Edge Gateways :superscript:`5.2.4`
- NSX-V: Create and manage DHCP Relay for Edge Gateways and Logical Routers :superscript:`5.2.4`
- NSX-V: Create and manage DHCP Bindings for Edge Gateways :superscript:`5.2.4`
- Security: Two-factor authentication added for Morpheus local users as well as users from Active Directory and LDAP identity sources :superscript:`5.2.5`
- Settings: Add IP addresses or hostnames to approved or denied lists which limits users to only approved sources when creating HTTP Tasks or populating Option Lists through REST calls. Previously, specific hosts could be denied but now administrators can opt to deny all hosts except those which are specifically approved :superscript:`5.2.5`

Fixes
=====

Appliance Updates
=================


|morpheus| API & CLI Improvements
=================================
- Billing: The ``billing`` API endpoint now returns ``resourcePoolId`` and ``resourcePoolName`` :superscript:`5.2.4`
- Clouds: ``scalePriority`` is now handled properly for get, add and update requests to the ``clouds`` API :superscript:`5.2.4`

Enhancements
------------


Fixes
-----


Agent/Node Package Updates
==========================
