Supported PaaS Offerings
````````````````````````

Morpheus has underlying technologies that support the Application Tier, which can be automatically installed and embedded on the applications nodes.  Alternatively, the services can be provided externally and not be embedded.  Many cloud providers
have offerings of these underlying technologies but some are not native or don't provide the performanced needed.  Below is a list of PaaS offerings that have been approved to be used for Morpheus

.. list-table:: PaaS Offering Support
   :widths: auto
   :header-rows: 1

   * - Cloud
     - Messaging (RabbitMQ)
     - Log (Elasticsearch)
     - Database (mySQL)
     - Shared Storage (NFS)
   * - AWS
     - Amazon MQ
     - Amazon OpenSearch
     - Amazon Aurora
     - Elastic File System
   * - GCP
     - N/A
     - N/A
     - mySQL Instance
     - N/A
   * - Azure
     - N/A
     - N/A
     - N/A
     - Storage Account