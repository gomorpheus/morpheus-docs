.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. .. NOTE:: This list includes improvements added in 4.2.4 which were not part of the 5.0.0 beta. Users upgrading from 4.x.x may also want to review the `5.0.0 change list <https://docs.morpheusdata.com/en/5.0.0/release_notes/current.html>`_ to get a complete picture of the changes.

.. include:: highlights.rst

All New Features
================

|morpheus| API & CLI Improvements
=================================

Fixes
=====


.. .. note:: :superscript:`+` indicates items also released in v4.2.5

.. new do not remove
Appliance Updates
=================
.. not sure if we should have separate appliance/installer updates, adding here for now 

- Support added for Installing |morpheus| on Ubuntu 20.04
- Java: Openjdk-jre updated to 8u275
- Appliance Logs: Default log rotation added for Nginx and Tomcat logs //add paths & files 
- Installer: ``iptables_bach`` setup bash script moved from /tmp to /opt/morpheus/embedded/bin and renamed to iptables_morpheus.rules. Resolves reconfigure issue for systems with ``noexec`` set on ``/tmp``.


Agent/Node Package Updates
==========================
.. same 

- Java: openjdk and openjdk-jre updated to 8u275
- Node and VM Node package versions updates to 3.1.11  
.. add agent package version vars/list to compatibility? 
