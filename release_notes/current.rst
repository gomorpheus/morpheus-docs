.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

.. IMPORTANT:: Minimum v6.x required to upgrade to v6.0.7+ for environments using embedded RabbitMQ. Environments running 5.5.x or earlier using embedded RabbitMQ must upgrade to v6.0.0 - v6.0.6 prior to upgrading to v6.0.7+
.. IMPORTANT:: v6.0.7+ contains embedded MySQL v8 upgrade. BACKUP YOUR DATABASE PRIOR TO UPGRADE when using embedded MySQL (all-in-one appliances) and upgrading from v6.0.0 - v6.0.6.
.. WARNING:: Rolling upgrades for HA environments using embedded RabbitMQ and/or embedded Elasticsearch services are not supported when upgrading from v6.0.0 - v6.0.6.

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade version: |minUpgradeVer|

.. NOTE:: Items appended with :superscript:`x.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:Security: - Upgraded ``gradle.properties`` to 9.0.83 to mitigate multiple CVEs :superscript:`6.2.6 6.3.3`
            - Upgraded ``netty`` to version 4.1.100.final to mitigate CVE-2023-44487 and CVE-2023-41881 :superscript:`6.2.6 6.3.3`
            - Upgraded ``spring-boot-actuator-autoconfigure`` to 2.7.11 to mitigate CVE-2023-20873 :superscript:`6.2.6 6.3.3`
            - Upgraded ``spring-boot-autoconfigure`` to 2.7.12 to mitigate CVE-2023-20883 :superscript:`6.2.6 6.3.3`
            - Upgraded ``spring-boot`` to version 2.7.18 to mitigate CVE-2023-34055 :superscript:`6.2.6 6.3.3`
            - Upgraded ``spring-expression`` to version 5.3.17 to mitigate CVE-2022-22950 :superscript:`6.2.6 6.3.3`
            - Upgraded ``spring-expression`` to version 5.3.27 to mitigate CVE-2023-20863 and CVE-2023-20861 :superscript:`6.3.3 6.2.6`
            - Upgraded ``spring-security-web`` to 5.7.8 to mitigate CVE-2023-20862 :superscript:`6.2.6 6.3.3`
            - Upgraded ``spring-webmvc`` to version 5.3.30 to mitigate CVE-2023-20860 :superscript:`6.2.6 6.3.3`
            - ``jknack/handlebars.java`` upgraded to version 4.3.1 to mitigate CVE-2022-42889 :superscript:`6.2.6 6.3.3`


Appliance & Agent Updates
=========================

:Appliance: - Upgraded embedded ``erlang`` to version 26.1.2 :superscript:`6.2.6 6.3.3`
:Agent: - |morpheus| Linux Agent updated to v2.5.2 to prevent automation failures when run under specific conditions :superscript:`6.2.6 6.3.3`
:Node Packages: - |morpheus| node and vm-node packages updated to v 3.2.0 with |morpheus| Linux Agent v2.5.2 :superscript:`6.2.6 6.3.3`

