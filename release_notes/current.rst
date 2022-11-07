.. _Release Notes:

*************************
|morphver| Release Notes
*************************

- Compatible Plugin API version: |pluginVer|
- Compatible Morpheus Worker version: |workerVer|

.. IMPORTANT:: |morpheus| 5.4.9+ adds the "Provisioning: State" Role permission. This permission determines access to the State tab for Terraform-backed Instances and is set to "None" by default. On upgrade from a version prior to 5.4.9, only System Admin users will be able to see the State tab for these Instances. For other users who should have this access, edit their Roles to include "Provisioning: State" permissions.

.. .. important::  Security: CVE-2022-35912: Morpheus v5.5.1-2 and v5.4.8-2 are now available in response to CVE-2022-35912, a Grails Framework remote code execution vulnerability. v5.5.1-2 and v5.4.8-2 include the Grails v5.1.9 update that mitigates the vulnerability. At this time, the Grails vulnerability is only confirmed for grails frameworks running on Java 8. Morpheus versions v5.4.4 and higher are on Java 11. Customers on morpheus v5.4.3 or earlier are highly advised to upgrade to at minimum v5.4.4 or higher, and out of an abundance of caution we recommend all customers upgrade to v5.5.1-2 or v5.4.8-2 in the event the vulnerability is found to be exploitable on Java 11.

Release Dates
  - |morphVer|-1 |releasedate|

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version

New Features
============



Fixes
=====
