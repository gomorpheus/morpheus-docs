Support Bundles
===============

Support bundles collect diagnostic information from the |morpheus| appliance and managed infrastructure to assist with troubleshooting and support case resolution. Bundles are generated on-demand and can be downloaded or sent directly to HPE Support.

Generating a Support Bundle
----------------------------

#. Navigate to |AdmHea|
#. Click :guilabel:`Support Bundle` (or :guilabel:`Actions` > :guilabel:`Generate Support Bundle`)
#. Select the content categories to include
#. Click :guilabel:`Generate`

The bundle is created as a compressed archive and available for download from the Health page.

Bundle Content Categories
--------------------------

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Category
     - Contents
   * - Appliance Logs
     - Application logs, nginx logs, service logs from ``/var/log/morpheus/``
   * - Configuration
     - Appliance configuration (sanitized — credentials are excluded)
   * - Database
     - Schema information and diagnostic queries (no customer data)
   * - Health Metrics
     - CPU, memory, disk, and service health data from the appliance
   * - OpenSearch
     - Index health, cluster state, and statistics
   * - RabbitMQ
     - Queue depths, connection counts, and message rates
   * - System Information
     - OS version, kernel, hardware, network configuration
   * - Cluster Information
     - HVM cluster health, host status, and quorum state (when applicable)
   * - Network Switch
     - Aruba CX switch diagnostics (when Aruba CX integration is configured)

.. NOTE:: Support bundles never include customer VM data, stored credentials (these are encrypted), or tenant-specific business data. Only infrastructure diagnostic information is collected.

Role Requirements
-----------------

- ``Admin: Health`` permission at **Full** access is required to generate and download support bundles
- Read access allows viewing previously-generated bundle metadata but not downloading bundle contents

Managing Support Bundles
-------------------------

Previously-generated bundles are listed on the Health page. From the actions menu on each bundle:

- **Download** — Download the bundle archive to your local machine
- **Delete** — Remove the bundle from the appliance

Support bundles are stored on the appliance filesystem. In space-constrained environments, delete old bundles after they have been submitted to support.

Automated Collection
---------------------

|morpheus| collects anonymized environment telemetry for proactive support purposes. This telemetry includes:

- Appliance version and license information
- Cluster node counts and high-level resource utilization
- Feature usage statistics (anonymized)

This data does not include any customer content, credentials, or personally identifiable information.
