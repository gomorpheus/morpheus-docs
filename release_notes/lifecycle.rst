Release Lifecycle
=================

This page documents the release cadence, versioning scheme, and support lifecycle for |morpheus| platform components.

Release Cadence
---------------

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Release Type
     - Frequency
     - Description
   * - Major
     - Annual
     - New major version (e.g., 9.0 → 10.0). May include breaking changes, architectural updates, and new platform capabilities. Previous Major enters security/maintenance mode.
   * - Minor
     - Quarterly
     - New features and enhancements within the current Major (e.g., 9.0 → 9.1 → 9.2). Backward compatible within the Major.
   * - Patch
     - Monthly
     - Bug fixes and security updates (e.g., 9.0.0 → 9.0.1 → 9.0.2). No new features.

**Example annual release timeline:**

.. code-block:: text

   9.0.0 → 9.0.1 → 9.0.2 → 9.1.0 → 9.1.1 → 9.1.2 → 9.2.0 → 9.2.1 → 9.2.2 → 10.0.0
   ├── Q1 ──────────────────┤── Q2 ─────────────────┤── Q3 ─────────────────┤── Q4 ──┤

Component Release Schedule
--------------------------

Manager (Morpheus Appliance)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The |morpheus| Manager follows the Major/Minor/Patch cadence described above. All platform features, API changes, and UI updates ship in Manager releases.

HVM OS (Hypervisor Host Operating System)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The HVM OS is released **quarterly** alongside each Minor Manager release. It is a purpose-built operating system for HVM hypervisor hosts based on Ubuntu LTS.

**Currently supported HVM OS versions:**

.. list-table::
   :widths: 20 30 50
   :header-rows: 1

   * - HVM OS
     - Base
     - Notes
   * - 24.04
     - Ubuntu 24.04 LTS
     - Standard HVM host OS for cluster layout 1.3
   * - 26.04
     - Ubuntu 26.04 LTS
     - Required for confidential compute functions. Introduced in |morpheus| 9.1.0.

**HVM OS updates between releases:**

HPE maintains controlled Apt mirrors that deliver quarterly security and kernel updates after internal review. HVM hosts using the standard HVM OS can apply updates using standard ``apt`` procedures:

.. code-block:: bash

   sudo apt update && sudo apt upgrade

Updates available through the HPE Apt mirrors have been validated against the current |morpheus| release. No additional compatibility verification is required when using the official mirrors.

**Compatibility:** HVM OS versions are compatible with Manager releases within the same Major version. For example, HVM OS 24.04 and 26.04 are both compatible with all 9.x Manager releases.

Agent
^^^^^^

The |morpheus| Agent ships with each Manager release and is backward compatible within the same Major version. Agent upgrades are recommended with each Manager upgrade but are not strictly required for patch releases.

To upgrade the Agent on HVM hosts, navigate to the host detail page, expand the ACTIONS menu, and click "Upgrade Agent."

Plugins
^^^^^^^^

Plugins (HPE Alletra Block Storage, Aruba CX, etc.) follow an independent release cycle. Each plugin version declares its compatible Manager version range. Plugin compatibility is documented in the plugin's release notes and on the |morpheus| Plugin Catalog.

Support Lifecycle
-----------------

Active Support (1 Year)
^^^^^^^^^^^^^^^^^^^^^^^^

From the General Availability (GA) date of a Major release, **active support** is provided for **one year**:

- New features delivered in quarterly Minor releases
- Bug fixes delivered in monthly Patch releases
- Security updates delivered in Patch releases
- Full technical support and troubleshooting

Security/Maintenance Mode (1 Year)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When a new Major release ships, the previous Major enters **security/maintenance mode** for **one additional year**:

- Critical security fixes only (no new features or general bug fixes)
- Technical support for existing configurations
- No new Minor releases
- Customers are encouraged to upgrade to the current Major during this period

End of Support
^^^^^^^^^^^^^^^

After the security/maintenance year ends, the release reaches **End of Support**:

- No further patches or security fixes
- Technical support is best-effort only
- Upgrade to a supported Major version is required

**Total lifecycle per Major release: 2 years** (1 year active + 1 year security/maintenance).

.. list-table::
   :widths: 15 20 20 20 25
   :header-rows: 1

   * - Major
     - GA Date
     - Active Support Ends
     - Maintenance Ends
     - Status
   * - 9.0
     - June 2026
     - June 2027
     - June 2028
     - Active
   * - 10.0
     - (projected) 2027
     - 2028
     - 2029
     - Future

Upgrade Policy
--------------

Supported Upgrade Paths
^^^^^^^^^^^^^^^^^^^^^^^^

- **Patch to Patch** (e.g., 9.0.1 → 9.0.2): Always supported, minimal downtime
- **Minor to Minor** (e.g., 9.0.x → 9.1.0): Supported from the latest patch of the previous minor
- **Major to Major** (e.g., 8.x → 9.0): Supported from designated minimum upgrade version (see release notes for each version)
- **Skipping versions:** Skipping Minor releases within a Major is supported (e.g., 9.0.x → 9.2.0). Skipping Major releases is not supported — upgrade to each Major in sequence.

Rolling vs Non-Rolling Upgrades
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 25 35 40
   :header-rows: 1

   * - Upgrade Type
     - Availability
     - Downtime
   * - Rolling (HA)
     - Supported for Patch and some Minor upgrades (see release notes)
     - Near-zero downtime — nodes upgraded sequentially
   * - Non-Rolling
     - Required for Major upgrades and some Minor upgrades
     - Brief downtime — all nodes upgraded simultaneously

HVM Cluster Layout Upgrades
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

HVM cluster layout upgrades (e.g., 1.2 → 1.3) are a **separate operation** from Manager upgrades. A layout upgrade updates the cluster's architecture (quorum system, datastore management, etc.) and is performed via the cluster detail page after the Manager has been upgraded. See :doc:`/infrastructure/clusters/hvm/upgrading` for the detailed procedure.

HVM OS Upgrades
^^^^^^^^^^^^^^^^

HVM host OS upgrades (e.g., 24.04 → 26.04) are performed per-host using the host maintenance workflow:

#. Place the host in maintenance mode (VMs evacuate to other hosts)
#. Perform the OS upgrade
#. Exit maintenance mode

This can be done as a rolling operation across cluster hosts with no VM downtime.
