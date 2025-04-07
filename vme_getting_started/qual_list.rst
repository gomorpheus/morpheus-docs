HPE VM Essentials Software Compatibility Matrix
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section contains the list of hardware that has been tested and confirmed to support HPE VM Essentials Software and HPE VM Essentials clusters at scale. Hardware not included in this list may be compatible but is untested. Using untested hardware may limit the scope of support services available from HPE support teams.

At product launch, compatibility and scale testing has been limited to HPE hardware. As time goes on, third-party hardware will be supported in addition to HPE hardware. This document will be updated over time as new hardware SKUs are tested for compatibility and performance at scale.

.. list-table:: **Server Hardware Support**
  :widths: auto
  :header-rows: 1

  * - Hardware Family
    - Platform Type
    - Hardware SKU
    - Comments
  * - HPE ProLiant
    - Intel 1 RU server
    - HPE ProLiant DL320 Gen 12
    -
  * - HPE ProLiant
    - Intel 1 RU server
    - HPE ProLiant DL360 Gen 10+
    -
  * - HPE ProLiant
    - Intel 1 RU server
    - HPE ProLiant DL360 Gen 11
    -
  * - HPE ProLiant
    - Intel 1 RU server
    - HPE ProLiant DL360 Gen 12
    -
  * - HPE ProLiant
    - AMD 1 RU server
    - HPE ProLiant DL325 Gen 11
    -
  * - HPE ProLiant
    - AMD 1 RU server
    - HPE ProLiant DL365 Gen 11
    -
  * - HPE ProLiant
    - AMD 2 RU server
    - HPE ProLiant DL385 Gen 11
    -
  * - HPE ProLiant
    - AMD 2 RU server
    - HPE ProLiant DL345 Gen 11
    -
  * - HPE ProLiant
    - Intel 2 RU server
    - HPE ProLiant DL340 Gen 12
    -
  * - HPE ProLiant
    - Intel 2 RU server
    - HPE ProLiant DL380 Gen 10+
    -
  * - HPE ProLiant
    - Intel 2 RU server
    - HPE ProLiant DL380 Gen 11
    -
  * - HPE ProLiant
    - Intel 2 RU server
    - HPE ProLiant DL380a Gen 11
    -
  * - HPE ProLiant
    - Intel 2 RU server
    - HPE ProLiant DL380 Gen 12
    -
  * - HPE ProLiant
    - Intel tower server
    - HPE ProLiant ML350 Gen 12
    -
  * - HPE ProLiant
    - Intel single slot blade
    - HPE Synergy 480 Gen 11 (local storage)
    -

.. NOTE:: Currently, only HPE hardware is supported but support for third-party hardware is planned for the future.

.. list-table:: **Storage Hardware Support**
  :widths: auto
  :header-rows: 1

  * - Hardware Family
    - Platform Type
    - Comments
  * - HPE Alletra Storage
    - HPE Alletra 5000 (5010, 5030, 5050) (iSCSI)
    - Update storage hardware to the latest available firmware
  * - HPE Alletra Storage
    - HPE Alletra 6000 (6010, 6030, 6050, 6070, 6090) (iSCSI)
    - Update storage hardware to the latest available firmware
  * - HPE Alletra Storage
    - HPE Alletra Storage MP B10000 (iSCSI, Fibre Channel)
    - Update storage hardware to the latest available firmware

.. NOTE:: For more detail, please visit the `storage matrix <http://www.hpe.com/storage/spock>`_

.. list-table:: **Independent Software Vendor (ISV) Support**
  :widths: auto
  :header-rows: 1

  * - Partner
    - Product Name
    - Product Version
    - Deployment
    - Validation Type
    - Resources
  * - Veeam
    - Backup and Replication
    - 12.3
    - Agent-based
    - Partner
    - `Technical Brief <https://www.hpe.com/psnow/doc/a50012338enw>`_, Blog (`part 1 <https://community.veeam.com/blogs-and-podcasts-57/navigating-hpe-vm-essentials-part-1-what-is-it-and-how-to-protect-it-with-veeam-9610>`_, `part 2 <https://community.veeam.com/blogs-and-podcasts-57/navigating-hpe-vm-essentials-part-2-exploring-backup-strategies-9611>`_, `part 3 <https://community.veeam.com/blogs-and-podcasts-57/hpe-vme-and-veeam-backup-replication-9863>`_)
  * - Cohesity
    - Data Cloud
    - 7.1.2 and later
    - Agent-based
    - Partner
    -
  * - Cohesity Veritas
    - NetBackup
    - 11
    - Agent-based
    - Partner
    -
  * - Oracle
    - Database
    - 19c
    - Single instance only; Oracle RAC support TBD
    - HPE
    - `Technical Brief <https://www.hpe.com/psnow/doc/a50012368enw>`_, `Blog <https://community.hpe.com/t5/the-cloud-experience-everywhere/reduce-costs-with-hpe-vm-essentials-in-your-oracle-database-on/ba-p/7238767>`_
  * - Microsoft
    - SQL Server
    - SQL Server 2016, 2017, 2019, 2022
    - Single instance with Availability Groups
    - HPE
    - `Technical Brief <https://www.hpe.com/psnow/doc/a50012536enw?jumpid=in_ResourceLibrary>`_, `Blog <https://community.hpe.com/t5/the-cloud-experience-everywhere/sql-server-runs-on-the-new-hpe-vm-essentials/ba-p/7238640>`_
  * - MongoDB
    - Enterprise Advanced
    - 8.0.0
    -
    - HPE
    - `Technical Brief <https://www.hpe.com/psnow/doc/a50012355enw>`_, `Blog <https://community.hpe.com/t5/the-cloud-experience-everywhere/optimize-ai-development-how-hpe-vm-essentials-and-mongodb/ba-p/7235922>`_, `Video <https://youtu.be/UYpOJ6JnuEk>`_
  * - Omnissa
    - Horizon
    - 8.13.1 (Build 11490723527)
    - For test/dev and POC only; not for production environments
    - HPE
    - `Blog <https://community.hpe.com/t5/the-cloud-experience-everywhere/unlock-efficient-vdi-with-hpe-vm-essentials-software-and-omnissa/ba-p/7238879>`_

.. NOTE:: Applications have been validated within the bounds of the supported HPE VM Essentials functionality. Always check the HPE VME feature list to determine whether specific functionality is supported by the HPE VME hypervisor (ex. shared disk access).

Most modern applications like databases were designed with very “loose” dependance on hardware infrastructure. They can typically run on a variety of hypervisors including virtual machines and containers. The respective ISV vendor typically only specifies the supported underlying operating system (Guest OS) but does not require certification of any hypervisor.  However, there can be specific features that a customer deployment of these applications requires at a hypervisor or infrastructure level. For example, a Microsoft SQL Server Failover cluster instance requires a shared disk between multiple SQL Server VMs. Oracle, similarly, requires shared disks for an Oracle Real Application Cluster (RAC) setup.  Therefore, it needs to be always validated whether the specific deployment requires certain features and whether these are supported by HPE VM Essentials in its latest release.

Select ISV applications require “full stack” certifications including OS, hypervisor, compute and storage devices, or even the specific storage connectivity protocol. SAP HANA and related SAP applications are a typical example; so are some Healthcare Electronic Health Record (EDR) applications. If you or your customer plans on running one of these applications, please reach out to your HPE account team.

.. list-table:: **Hypervisor OS Compatibility and Interoperability Matrix**
  :widths: auto
  :header-rows: 1

  * - OS Vendor
    - OS Family
    - Compute Platform
    - Storage Platform
  * - Canonical
    - Ubuntu 22.04 Server
    - x86
    - Alletra; iSCSI

.. list-table:: **Guest OS**
  :widths: auto
  :header-rows: 1

  * - Partner
    - Product Name
    - Product Version
    - Guest OS
    - Validation Type
    - Resources
  * - RHEL
    - RHEL
    - 9.3
    - RHEL 9.3
    - HPE
    -
  * - CentOS
    - CentOS
    - 8
    - CentOS 8
    - HPE
    -
  * - SUSE
    - SUSE Linux Enterprise Server
    - 15-SP6
    - SUSE 15-SP6
    - HPE
    -
  * - Microsoft
    - Windows Server
    - 2022
    - Windows Server 2022
    - HPE
    -

Additional Resources
````````````````````

- Service Pack ProLiant Index Page: `Gen12 SPP <https://support.hpe.com/docs/display/public/a00sppdocen_US/spp/#/index.aspx?version=gen12.2025.01.00.00>`_, `Gen11 SPP <https://support.hpe.com/docs/display/public/a00sppdocen_US/spp/#/index.aspx?version=gen11.2025.01.00.00>`_, `Gen10+/Gen10 SPP <https://support.hpe.com/docs/display/public/a00sppdocen_US/spp/#/index.aspx?version=gen10.2025.01.00.00>`_
- `Spock Storage Configuration Matrix <https://www.hpe.com/storage/spock>`_
- `OS Support Matrix <https://www.hpe.com/us/en/collaterals/collateral.a50010841enw.html>`_
- `HPE Support Center for VME <https://www.hpe.com/support/VME-Docs>`_
