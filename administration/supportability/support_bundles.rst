Support Bundles
===============

Support bundles collect diagnostic information from the |morpheus| appliance and managed infrastructure to assist with troubleshooting and support case resolution. Bundles are generated on-demand or automatically and can be downloaded locally or delivered directly to HPE Support.

Navigate to :menuselection:`Administration --> Health --> Support Bundles` to view, generate, download, or delete support bundles.

.. NOTE:: Support bundles are available only to master tenant users with System Admin role. The ``Admin: Support Bundles`` permission gates read and full access.

Generating a Support Bundle
----------------------------

#. Navigate to :menuselection:`Administration --> Health --> Support Bundles`.
#. Click :guilabel:`Generate New Support Bundle`.
#. Enter a :guilabel:`Name` for the bundle.
#. Set the :guilabel:`Log Range Start` and :guilabel:`Log Range End` to define the time window for log collection.
#. In the :guilabel:`Components` section, select one or more categories and content types to include. Resource-backed content types allow selecting specific resources (for example, a specific cloud or storage server).
#. Click :guilabel:`Generate`.

The bundle is created asynchronously. Status progresses from **Pending** through **In Progress** to **Completed** or **Failed**. Large bundles may take several minutes depending on the number of components and log volume. An in-progress bundle can be cancelled from the list page.

Bundle Content Categories
--------------------------

.. list-table::
   :widths: 22 78
   :header-rows: 1

   * - Category
     - Contents
   * - Appliance
     - Application logs (morpheus-ui, check-server, guacd, mysql, nginx, opensearch), appliance configuration (sanitized), health metrics (CPU, memory, storage, database, elastic, queues, threads), system information (OS, kernel, hardware, network)
   * - Clouds
     - Cloud integration diagnostics for selected clouds
   * - Clusters
     - HVM cluster health, host status, quorum state, and cluster-level diagnostics
   * - Networking
     - Network server diagnostics (including Aruba CX switch bundle when configured)
   * - Servers
     - Compute server diagnostics for selected managed servers
   * - Storage
     - Storage server diagnostics. For HPE Alletra MP storage servers: triggers telemetry bundle generation on the array. If call-home is not enabled, downloads the resulting bundle; if call-home is enabled, triggers generation only (data already sent separately)

Each category can expose multiple content types. Resource-backed content types allow selecting specific instances of that resource (for example, a particular storage server or cloud integration). A failure collecting one component does not block the overall bundle.

.. NOTE:: Support bundles never include customer VM data, stored credentials (these are encrypted at rest), or tenant-specific business data. Only infrastructure diagnostic information is collected.

Health Metrics Included
^^^^^^^^^^^^^^^^^^^^^^^^

The health summary collected in the bundle includes:

- **CPU:** Processor count, process uptime, Morpheus CPU usage, system CPU usage, system load average
- **Memory:** Morpheus memory (total, used, free, usage %), system memory, swap
- **Storage:** Filesystem details (used, free, total, percent utilization, mount points)
- **Database (MySQL):** Version, connection statistics, thread statistics, performance metrics (slow queries, temp tables), InnoDB statistics
- **OpenSearch:** Cluster status, node count, shard information, per-node heap/memory/CPU, index health
- **Queues (RabbitMQ):** Queue count, busy/error queues, per-queue message counts
- **Threads:** Total count, busy, running, blocked, per-thread details

This health data is written as a JSON file within the support bundle.

HPE Support Integration
------------------------

Configure HPE Support integration at :menuselection:`Administration --> Settings --> Support`.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Setting
     - Description
   * - Daily Support Bundle
     - When enabled, automatically generates a support bundle once daily and delivers it to HPE Support
   * - Send to HPE
     - When enabled, completed bundles are converted to CMB format and delivered to HPE via the RDA (Remote Data Access) agent
   * - Remote Support Access
     - Enables HPE Support remote access to the appliance for diagnostics (requires Send to HPE enabled)
   * - Default Storage Bucket
     - Select the storage bucket where bundles are archived

The :guilabel:`Appliance Nodes` table on the Support settings page shows each node's hostname, RDA connection status (connected, disconnected, or not configured), and **Station ID**. The Station ID uniquely identifies the appliance to HPE Support.

When **Send to HPE** is enabled:

- Completed bundles are packaged and pushed to the local RDA agent for delivery
- Delivery status is tracked per bundle: In Progress, Delivered, Failed, or Superseded
- The list and detail views show delivery status when HPE delivery is enabled

When **Send to HPE** is disabled, bundles remain on the appliance for manual download and submission to support.

Managing Support Bundles
-------------------------

Previously-generated bundles are listed on the Support Bundles tab with columns for Name, Status, Started At, Completed At, Size, and Log Range. From each bundle's actions:

- **Download** — Download the bundle archive to your local machine
- **Delete** — Remove the bundle from the appliance
- **Cancel** — Stop an in-progress bundle generation

Support bundles are stored on the appliance filesystem. In space-constrained environments, delete old bundles after they have been submitted to support.

API
---

Support bundle operations are available via the REST API:

.. list-table::
   :widths: 15 40 45
   :header-rows: 1

   * - Method
     - Endpoint
     - Description
   * - GET
     - ``/api/support-bundles``
     - List all support bundles
   * - GET
     - ``/api/support-bundles/:id``
     - Show bundle details
   * - POST
     - ``/api/support-bundles``
     - Generate a new support bundle
   * - DELETE
     - ``/api/support-bundles/:id``
     - Delete a bundle
   * - GET
     - ``/api/support-bundles/:id/download``
     - Download the bundle archive
   * - POST
     - ``/api/support-bundles/:id/cancel``
     - Cancel an in-progress bundle

Automated Collection
---------------------

When daily support bundle generation is enabled in Support settings, |morpheus| automatically generates and (if configured) delivers a bundle to HPE Support once per day. This includes standard health metrics, configuration diagnostics, and log data from the configured default time window.

|morpheus| also collects anonymized environment telemetry for proactive support purposes when HPE Support integration is enabled. This telemetry includes:

- Appliance version and license information
- Cluster node counts and high-level resource utilization
- Feature usage statistics (anonymized)

This data does not include any customer content, credentials, or personally identifiable information.
