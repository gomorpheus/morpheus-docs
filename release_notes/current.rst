.. _Release Notes:

************************
|morphver| Release Notes
************************

.. No highlights this time, small update
  .. include:: highlights.rst

New Features
============

- Logging: Added support for custom NGINX log formats by updating ``morpheus.rb`` with a new ``log_format_name`` and ``log_format`` value
- NSX-T: Create and manage NSX-T load balancer profiles (Infrastructure > Load Balancers > Selected Load Balancer > Profiles Tab), previously this tab was read-only
- Software: Patch version numbers are now surfaced on the Software tab of server detail pages (mouse hover over software name) and in Software reports

|morpheus| API Improvements
===========================

- 2FA: Enable, disable and manage two-factor authentication settings with |morpheus| API and CLI
- Integrations: Create and manage integrations between |morpheus| and third-party technologies (including Ansible, ServiceNow, Git, Github, and several more) via |morpheus| API and ClI
- Networking: Add a NIC to existing VMs through |morpheus| API
- NSX-T: Subtenant users can access shared NSX-T integrations and load balancers through |morpheus| API and CLI as they already can through |morpheus| UI
- NSX-V: Router management support added in |morpheus| API and CLI to match functionality currently available in |morpheus| UI

Fixes
=====

- Oracle Cloud: Fixed an issue that prevented Oracle Linux Layouts from being provisioned onto Oracle Clouds in certain scenarios
- UI: Some UI pages have been updated to display data differently when the number of relevant objects is high enough to potentially impact application performance

Appliance Updates
=================


Refer to :ref:`compatibility` for additional details.
