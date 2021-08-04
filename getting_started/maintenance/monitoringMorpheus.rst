Monitoring Morpheus 
-------------------

When configuring monitoring for |morpheus|, the following should be taken into consideration. Please note additional data points my need to be monitored per customer configuration and usage. 

|morpheus| provided Health Data 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|morpheus| provides status and data for all critical system services, including morpheus-ui, mysql, elasticsearch and rabbitmq services, in the Health section/endpoint. The |morpheus| system **Health** page is accessible via the ui at ``/administration/health``, the API at ``/api/health`` and the CLI with ``morpheus health``. External monitoring tools can utilize the morpheus api to check status and data values for system and morpheus-ui memory and cpu data as well as local and external services, pending sufficient permissions for external services. 

.. note:: Some metrics may not be able to be gathered when using external services due to permission restrictions, such as mysql statistics when using Amazon RDS.

	
File System 
^^^^^^^^^^^

- Overall filesystem space
  - The following filesystems are written to by |morpheus| and should be monitored to ensure none become full.
    - ``/``
    - ``var`` 
    - ``opt`` 
    - ``etc`` 
    - ``tmp`` 
  
- ``/var``
  
  The default locations for critical service data paths are located in /var, including morpheus-ui, elasticsearch, mysql and rabbitmq data. Elasticsearch and RabbitMQ have default disk space thresholds that can cause service disruption when reached.

  - Warning: <80%
  - Critical <95% 
  
    When ``/var`` has <95% free space available (or 95% or greater used), Elasticsearch will by default enforce read-only (cluster.routing.allocation.disk.watermark.flood_stage) preventing any writes as well as causing rabbitmq messages to become backlogged, eventually leading to memory issues and possible morpheus-ui shutdown.
      
Memory
^^^^^^

When monitoring memory usage, it is important to monitor actual usage rather than memory allocated for java processes. Basic memory statistics will only include allocated memory for |morpheus| and |elasticsearch| processes, not the actual usage.

.. important:: 80% of system memory by default will always be allocated to java heap. If elasticsearch is local then 35% of total system memory is allocated to morpheus-ui heap and 45% to elasticsearch heap. If elasticsearch is external, then 80% of total system memory is allocated to morpheus-ui heap. This means basic memory stats will always show system memory utilization at or above 80% regardless of actual memory usage. 

morpheus-ui memory
^^^^^^^^^^^^^^^^^^

Various services and tools provide jvm statics such as jvmtop and jstat. The |morpheus| api also provides morpheus-ui memory utilization in addition to overall system memory data. 

The |morpheus| api ``/api/health`` response contains multiple memory data points, including: 

- **health.memory.memoryPercent** Percent of allocated memory used by |morpheus-ui| process. This is the stat that should be monitored.
- **health.memory.systemMemoryPercent** Percent of overall memory used for the system. (This includes memory allocated to the JVM and can be misleading).

The Health service will return a WARNING status and status message 'heavy memory usage, consider increasing morpheus memory' when **health.memory.memoryPercent** is greater than 95%.

.. important:: The Health service will return a WARNING status when **health.memory.memoryPercent** is greater than 95%.


morpheus-ui service
^^^^^^^^^^^^^^^^^^^

The best way to monitor the status of the ``morpheus-ui`` service is by utilizing the ``/ping`` endpoint on application nodes. This ensure the app is up and running. Monitoring the status of the ``morpheus-ui`` process/pid, or any other process, only informs if the process itself is running, not that the actual service successfully started and is running.

- ``https://appliance_url/ping`` returns **MORPHEUS PING** only when |morpheus| is up and running. 

Checks monitoring morpheus availability should fail when ``https://appliance_url/ping`` does not return **MORPHEUS PING**

``https://appliance_node_ip/ping`` should be used by load balancer monitors/checks for HA configurations to monitor the status of morpheus on each app node.

elasticsearch
^^^^^^^^^^^^^

Health 

Disk 

- Warning: <80%
- Critical <95% 

  When ``/var`` has <95% free space available (or 95% or greater used), Elasticsearch will by default enforce read-only (cluster.routing.allocation.disk.watermark.flood_stage) preventing any writes as well as causing rabbitmq messages to become backlogged, eventually leading to memory issues and possible morpheus-ui shutdown.
  
  
mysql 
^^^^^

Health 

Connections 

"maxConnections": 151,
"maxUsedConnections": 93,
"usedConnections": 27,
"abortedConnections": 0,

rabbitmq
^^^^^^^^

Health 

Messages 

Cluster Status 

rtn.queueList?.each { row ->
  if(row.count > 1000) {
    row.status = 'error'
    rtn.errorQueues << row
  } else if(row.count > 10) {
    row.status = 'warning'
    rtn.busyQueues << row

|
