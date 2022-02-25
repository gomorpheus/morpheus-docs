Health
======

|Morpheus| Health
------------------

.. image:: /images/administration/health/morpheusHealth500.png

The |Morpheus| Health section provides an overview of the health of your |Morpheus| appliance. It includes data on the following:

  - Health Levels
  - CPU
  - Memory
  - Database
  - Elastic
  - Queues

.. NOTE:: An Elasticsearch warning status is typical for single node Appliances due to a single elasticsearch node and default replica count exceeding available nodes.

HEALTH LEVELS include
  - |Morpheus| CPU
  - System CPU
  - |Morpheus| Memory
  - System Memory
  - Used Swap


CPU include
  - Processor Count
  - Process Time
  - Morpheus CPU
  - System CPU
  - System Load

MEMORY includes
  - Morpheus Memory
  - Morpheus Used Memory
  - Morpheus Free Memory
  - Morpheus Memory Usage
  - System Memory
  - System Used Memory
  - System Free Memory
  - System Memory Usage
  - System Swap
  - Free Swap

DATABASE includes
  - Lifetime Connections
  - Aborted Connections
  - Max Used Connections
  - Max Connections
  - Threads Running
  - Threads Connected
  - Slow Queries
  - Temp Tables
  - Key Reads
  - Handler Reads
  - Buffer Pool Free
  - Open Tables
  - Table Scans
  - Full Joins
  - Key Read Requests
  - Key Reads
  - Engine Waits
  - Lock Waits
  - Handler Reads
  - Engine IO Writes
  - Engine IO Reads
  - Engine IO Double Writes
  - Engine Log Writes
  - Engine Memory
  - Dictionary Memory
  - Buffer Pool Size
  - Free Buffers
  - Database Pages
  - Old Pages
  - Dirty Page Percent
  - Max Dirty Pages
  - Pending Reads
  - Insert Rate
  - Update Rate
  - Delete Rate
  - Read Rate
  - Buffer Hit Rate
  - Read Write Ratio
  - Uptime


ELASTIC includes
  - Status
  - Cluster
  - Node Count
  - Data Nodes
  - Shards
  - Primary Shards
  - Relocating Shards
  - Initializing
  - Unassigned
  - Pending Tasks
  - Active Shards

.. NOTE:: Warning status is typical for Elasticsearch

Elastic Nodes include
  - Node
  - Master
  - Location
  - Heap Usage
  - Memory Usage
  - CPU Usage
  - 1M Load
  - 5M Load
  - 15M Load

Elastic Indices include
  - Health
  - Index
  - Status
  - Primary
  - Replicas
  - Doc
  - Count
  - Primary
  - Size
  - Total Size

QUEUES INCLUDE
  - Queue Count
  - Busy Queues
  - Error Queues

|Morpheus| Logs
---------------

The |morpheus| logs section aggregates appliance-specific logs into one list. If needed, users can export the logs by clicking :guilabel:`EXPORT`. This action triggers a download containing the last 10,000 log entries as a ``.log`` file.

.. image:: /images/administration/healthlogs.png
