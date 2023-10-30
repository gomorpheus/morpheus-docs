.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

.. IMPORTANT:: |morpheus| 6.3.0 is the first version to require Plugin API version 1.0.0+. As a result, small changes will need to be made in order to make plugins created by earlier versions of |morpheus| compatible. Please see the related `article in our KnowledgeBase <https://support.morpheusdata.com/s/article/Making-plugins-compatible-with-Morpheus-6-3-0?language=en_US>`_ for full details on updating plugins.
.. IMPORTANT:: |morphver| contains embedded MySQL v8 upgrade when upgrading from  v6.0.0 - v6.0.6 or 6.1.0 - 6.2.1. BACKUP YOUR DATABASE PRIOR TO UPGRADE when using embedded MySQL (all-in-one appliances)
.. IMPORTANT:: Minimum v6.x required to upgrade to |morphver| for environments using embedded RabbitMQ. Environments running 5.5.x or earlier using embedded RabbitMQ must upgrade to v6.0.0 - v6.0.6, or 6.1.0 - 6.2.1 prior to upgrading to |morphver|
.. WARNING:: Rolling upgrades for HA environments using embedded RabbitMQ and/or embedded Elasticsearch services are not supported when upgrading from  v6.0.0 - v6.0.6 or 6.1.0 - 6.2.1

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade version: |minUpgradeVer|

.. NOTE:: Items appended with :superscript:`6.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:Cluster Packages: - Added new UI area (|LibTemClu|) for creating Cluster Packages which can be associated with Cluster Layouts. See the appropriate areas of Morpheus Documentation for more on Cluster Packages and Cluster Layouts
:Currency: - Added support for Mongolian Tugrik (MNT) currency :superscript:`6.0.9 6.2.4`
:Image Builder: - Updated the Image Builder form into a single form rather than a paged wizard. See the Image Builder section of |morpheus| documentation for example scripts and help getting started
:Plugins: - The required Plugin API version is now |pluginVer|. Plugins developed for |morpheus| versions prior to 6.3.0 will need small changes. Please see the KnowledgeBase <https://support.morpheusdata.com/s/article/Making-plugins-compatible-with-Morpheus-6-3-0?language=en_US>`_ article.
:Roles: - Added the ability to specify (per Role) a landing page other than the Dashboard within |morpheus|. For example, a Role could be configured to log into the Instance list page
         - There is now a Feature Permission which determines whether a Role is able to use Task Cancel and Task Retry controls for executions. This also controls access to the Cancel and Retry controls on Tasks within Instance histories
         - There is now a Feature Permission which determines whether a Role may extend expiration or shutdown Policies on workloads. This permission can apply globally or only to workloads the user owns
:VMware: - Added support for versioned templates from VMware Content Library
          - Added the ability to set vApp Property values on VMware Node Types. See `Node Type docs <https://docs.morpheusdata.com/en/6.3.0/library/blueprints/blueprints.html?next=https%3A%2F%2Fdocs.morpheusdata.com%2Fen%2F6.3.0%2Flibrary%2Fblueprints%2Fb>`_ for more


Fixes
=====

:API & CLI: - The return from the ``policies get-type`` CLI call has been updated to return additional information

Appliance Updates
=================

:Embedded Plugins: - BigIp updated to v1.2.0
                   - Bluecat updated to v1.2.0
                   - Efficient IP updated to v1.2.0
                   - Infoblox updated to v1.3.2
                   - Microsoft DNS updated to v2.2.1
                   - Morpheus Home Dashboard updated to v1.1.0
                   - phpIPAM updated to v1.2.1
                   - PowerDNS updated to v1.1.0
                   - Rubrik updated to v1.2.0
                   - SolarWinds updated to v1.1.1