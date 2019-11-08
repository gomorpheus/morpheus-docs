Morpheus Documentation
======================

What's new in v4.1.0
--------------------

- AWS: Plans: Seeded plans for R5A and T3A AWS Instance Types added
- AWS: RDS: MSSQL Server support added
- AWS: Support added for Static IP Assignment
- Cloud Formation: CF templates can now be provisioned as Instances using Cloud Formation layout types and Spec Templates
- Instances: List View: Actions selection removed when multiple Instances are selected and at least one is in a Read Only Group
- IPAM: ``THROTTLE RATE`` setting added to Infoblox and Bluecat to control API/sync rate.
- Library: Node Types: New Cloud Formation Layout technology Type. Allows CF Spec Templates as Instances
- Library: Spec Templates: New Cloud Formation Spec Template type
- SCVMM : Datastore selection options now filter based on selected resource pool and host
- Usage: createdByUser, createdByUserId, siteId, siteName, siteUUID, siteCode, and metadata [] now returned for /api/billing records. serverUniqueId added for Containers, serverUniqueId added for Servers, zoneCode added for Zones/Clouds. NOTE: These values will only be populated for newly created usage records. Not all record will have values for all fields, such as createdByUser and createdByUserId for discovered servers, site information for non-instance records)
- User Settings: Complex Passwords now required for Linux and Windows users in User Settings. Password must contain at least one uppercase letter, one lowercase letter, a number, and a symbol.
- White Labelling: Sub-tenant notifications branding added

CLI
---
- New format for -S, --sort ORDER Sort Order. DIRECTION may be included as "ORDER [asc|desc]". Example: instances list -S "dateCreated desc"
- New command monitor-alerts. Requires appliance version 4.1.1
- Improved commands monitor-contacts add, monitor-checks, monitor-groups and monitor-apps by adding prompting.
- Improved APIClient so that is easier to use. See APIClient.

Security
--------
- Appliances: Java updated to OpenJDK JRE 8u232
- Node Packages: Java updated to OpenJDK JRE 8u232

System
------
- Added improved handling of messages when database is unreachable to prevent out of memory errors and improve application recovery

Morpheus Hub
------------
- Morpheus Hub Registration and Login added to initial Appliance Setup for licenses. Note the registration and login options will only appear if the Appliance can reach https://morpheushub.com

See :doc:`release_notes/current.rst` for additional information. 

.. toctree::
   :maxdepth: 3
   :caption: Morpheus UI

   getting_started/getting_started
   provisioning/provisioning
   infrastructure/infrastructure
   administration/administration
   monitoring/monitoring
   logs/logs
   backups/backups
   operations/operations
   tools/tools
   integration_guides/integration_guides
   troubleshooting/troubleshooting


.. toctree::
   :maxdepth: 3
   :caption: Morpheus CLI

   cli/install
   cli/walkthrough
   cli/shell
   cli/commands
   cli/changelog

.. toctree::
   :maxdepth: 3
   :caption: Morpheus API

   api/intro
   api/requests

.. toctree::
   :maxdepth: 4
   :caption: Release Notes

   release_notes/current.rst
   release_notes/compatibility.rst
   release_notes/previousReleases.rst


.. |morpheus| replace:: Morpheus
