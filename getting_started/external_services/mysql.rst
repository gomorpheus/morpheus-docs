.. _external-mysql:

MySQL
-----

MySQL is the transactional database for |morpheus|, storing all operational data including Instances, users, tenants, policies, automation configurations, and billing records. This page covers preparing an external MySQL service for use with |morpheus|.

.. note::

   For HVM deployments and all-in-one installations, MySQL is embedded and requires no configuration. This page is only relevant when running MySQL externally for HA, managed database services, or organizational requirements.

Supported Versions
^^^^^^^^^^^^^^^^^^

- **MySQL 8.0.x** (embedded default: |mysqlver|)
- **MySQL 8.4.x LTS** (supported for external clusters in |morphver|+)
- **MySQL 8.0.x FIPS** (|mysqlverfips|)

.. important::

   |morpheus| requires the ``utf8mb4`` character set and ``utf8mb4_general_ci`` collation. Ensure your external MySQL instance is configured accordingly.

When to Externalize
^^^^^^^^^^^^^^^^^^^

Consider running MySQL externally when:

- You need **high availability** with multi-master replication or InnoDB Cluster
- You want to use a **managed database service** (e.g., Amazon RDS, Azure Database for MySQL, Google Cloud SQL)
- Your organization requires databases to be **managed by a dedicated DBA team**
- You need **cross-region replication** for disaster recovery
- The appliance's all-in-one footprint is constrained and you want to offload database I/O

Preparing the External Database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Perform the following on your external MySQL host or cluster to prepare it for |morpheus|.

**Step 1 — Create the database**

.. code-block:: sql

   CREATE DATABASE morpheus CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

**Step 2 — Create the Morpheus database user**

This user will be used by |morpheus| application nodes to authenticate with MySQL:

.. code-block:: sql

   CREATE USER 'morpheus'@'%' IDENTIFIED BY '<secure-password>';

**Step 3 — Grant permissions**

.. code-block:: sql

   GRANT ALL PRIVILEGES ON morpheus.* TO 'morpheus'@'%' WITH GRANT OPTION;
   GRANT SELECT, PROCESS, SHOW DATABASES, RELOAD ON *.* TO 'morpheus'@'%';
   FLUSH PRIVILEGES;

.. tip::

   Replace ``'%'`` with specific appliance node IPs for tighter security (e.g., ``'morpheus'@'10.0.0.%'``).

MySQL HA / InnoDB Cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^

For high availability, MySQL can be configured in a clustered topology. Common approaches:

**InnoDB Cluster (Recommended)**

InnoDB Cluster provides built-in high availability using Group Replication with automatic failover:

- Minimum 3 nodes for quorum-based failover
- Supports single-primary (one writer) or multi-primary (multiple writers) mode
- Single-primary mode is recommended for |morpheus| to avoid write conflicts
- Use MySQL Router as a connection proxy between |morpheus| and the cluster for automatic failover routing

**Multi-Master Replication**

Traditional MySQL replication with multiple writable masters:

- Can be configured with no replication delay within the same region
- Allow some replication delay for cross-region replicas
- Increases risk of job overlap between regions, though concurrent operations typically self-correct

**Managed Services**

Cloud-managed MySQL services (RDS, Azure Database, Cloud SQL) handle replication, failover, and backups automatically. Ensure:

- The service supports MySQL 8.0+ or 8.4.x
- ``utf8mb4`` character set is available
- The |morpheus| appliance nodes can reach the service endpoint on port 3306
- The service allows the ``GRANT`` permissions listed above

Network Requirements
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 20 20 10 20

   * - Description
     - Source
     - Destination
     - Port
     - Protocol
   * - |morpheus| application connection
     - |morpheus| appliance
     - MySQL host(s)
     - 3306
     - TCP
   * - InnoDB Cluster Group Replication
     - MySQL node
     - MySQL node
     - 33061
     - TCP
   * - MySQL Router (if used)
     - |morpheus| appliance
     - MySQL Router
     - 6446 (RW), 6447 (RO)
     - TCP

TLS Connections
^^^^^^^^^^^^^^^

To connect to an external MySQL instance over TLS, configure the MySQL server with a valid certificate and enable TLS on the |morpheus| side via ``morpheus.rb``. Consult the MySQL documentation for server-side TLS setup.

|morpheus| will use TLS when the external MySQL server requires it — no additional ``morpheus.rb`` settings are needed beyond the host/user/password configuration if the MySQL server enforces TLS for all connections.

Database Sizing
^^^^^^^^^^^^^^^

MySQL storage requirements grow with:

- Number of managed Instances and hosts
- Billing and usage record retention
- Audit log history
- Backup metadata

For most environments, start with **50 GB** of database storage and monitor growth. Large environments (10,000+ managed resources) may require 200 GB+ and should consider dedicated I/O-optimized storage.

Refer to :doc:`Capacity and Planning </getting_started/requirements/capacity_planning>` for general sizing guidance.

Backup Considerations
^^^^^^^^^^^^^^^^^^^^^

.. important::

   Always backup the MySQL database before performing |morpheus| upgrades. The database can be restored if an upgrade needs to be rolled back.

For external databases:

- Configure automated backups through your MySQL HA solution or managed service
- Test restore procedures regularly
- For ``mysqldump``-based backups, use ``--single-transaction`` to avoid locking tables
- Retain at least one backup from before each |morpheus| upgrade
