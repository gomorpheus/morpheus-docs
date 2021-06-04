.. _Release Notes:

************************
|morphver| Release Notes
************************

.. No highlights this time, small update
  .. include:: highlights.rst

New Features
============

- Keys & Certs: Added support for NSX-T SSL certificate creation (Infrastructure > Keys & Certs > SSL Certificates tab) when an NSX-T integration is present
- VMware vCenter: CPU and memory hot-add settings are now evaluated independently when reconfiguring CPU and memory for vCenter Instances. Previously, these settings were evaluated as a group rather than independently which could cause VMs to be restarted even when they were configured to support hot-add of memory and/or CPU

|morpheus| API Improvements
===========================

- Jobs: Updated Jobs to run against multiple targets in parallel rather than sequentially. Job execution records are added for each target rather than just for the latest target as was the case previously
- Keys & Certs: Added support for NSX-T SSL certificate creation through |morpheus| API when an NSX-T integration is present

Fixes
=====

- Lumen Edge Services: Users can no longer enter negative values in certain fields such as "Copies", "Shutdown Days", and "Expire Days" (and others) where negative values would not make sense when configuring Lumen Edge Services Cloud integrations
- NSX-T: Improvements to NSX-T Load Balancer profile creation functionality

..
  Appliance Updates
  =================
