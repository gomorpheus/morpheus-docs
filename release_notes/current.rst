.. _Release Notes:

*************************
|morphver| Release Notes
*************************

Release Date: |releasedate| v5.2.15-2 Feb 23 2022

.. NOTE:: v5.2.15-2 fixes critical ip addresses issue with jdk11, NSX-V DHCP relay validation error, adds FIPS EL8 Agent Node & VM Node Packages and security updates for embedded Java and Tomcat versions.

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version

.. .. include:: highlights.rst

Fixes
=====

:NSX: - Fixed missing DNS and Gateway fields when creating NSX-T static networks :superscript:`5.4.3`
      - Fixed NSX-V DHCP relay validation error (5.2.15-2)
:Provisioning: - Fixed critical ip addresses issue with jdk11 (5.2.15-2)

Appliance & Agent Updates
=========================

:Appliance: - Java: Embedded Java version updated to v11.0.13 (5.2.15-1), v11.0.14 (5.2.15-2) :superscript:`5.4.3`
            - Mysql: Embedded MySQL version updated to v5.7.37 on standard (non-fips) Appliance packages :superscript:`5.4.3`
            - Tomcat: Updated to v9.0.58 (5.2.15-2)
:Agent: - Added FIPS compliant el8 |morpheus| Agent node & vm-node packages. Compatible with RHEL 8, CentOS 8, and Oracle Linux 8 (5.2.15-2) :superscript:`5.4.3`
        - Agent Node & VM Node Packages: Java: Updated jdk to v11.0.14 (5.2.15-2) :superscript:`5.4.3`
        - |morpheus| Windows Agents updated to v1.8.0, fixes Windows Bare-Metal Servers displaying incorrect core count :superscript:`5.4.3`

.. ..
