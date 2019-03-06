Requirements
============

|morpheus| is a software based appliance installation capable of orchestrating many clouds and hypervisors. Before an installation is started it is important to understand some of the base requirements.

In the simplest configuration |morpheus| needs one Appliance Server. The Appliance Server, by default, contains all the components necessary to orchestrate both vm's and containers. To get started some base requirements are recommended:

Base Requirements
-----------------

- **Operating System:** Ubuntu 14.04 /16.04 or CentOS/RHEL greater than 7.0.


- **Memory:** 16 GB recommended for default installations. 8 GB minimum required with 4 GB+ available storage swap space
- **Storage:** 200 GB storage minimum (see Storage Considerations below)
- Network connectivity from your users to the appliance over TCP 443 (HTTPS)
- Superuser privileges via the sudo command for the user installing the |morpheus| Appliance package.
- Access to base yum and apt repos
- An Appliance License is required for any operations involving provisioning.
- Internet Connectivity (optional)
   - To download from |morpheus|' public docker repositories and system Virtual Image catalog
   - Offline installation require installing the offline package in addition to the regular installation package.

   .. NOTE:: Access to base yum and apt repos is still required for offline installations.

-  VM and Host Agent Install (optional)
    - Inbound connectivity access from provisioned vm's and container hosts on ports 443 (Agent install and communication) and 80 (Linux Agent installs via yum and apt)
    - An Appliance URL that is accessible/resolvable to all managed hosts. It is necessary for all hosts that are managed by |morpheus| to be able to communicate with the appliance server ip on port 443. This URL is configured under Admin->Settings.

.. NOTE:: Ubuntu 16.10 and Amazon Linux are not supported.

Storage Considerations
----------------------

Upon initial installation |morpheus| takes up less than 10 GB of space, however Morpheus Services, Virtual Images, Backups, Logs and stats and user uploaded and imported data require adequate space on the Morpheus Appliance(s) per Appliance Configuration and activity.

.. IMPORTANT:: It is the customers responsibility to ensure adequate storage space per configuration and use case.

Default Paths
^^^^^^^^^^^^^

``/opt/morpheus``
  Morpheus Application and Services Files
``/var/opt/morpheus``
  User, Application and Services Data, including default config Elasticsearch, RabbitMQ and Database data, and default Virtual Image path.
``/var/log``
  Morpheus Service logs
``/tmp/morpheus``
  Working directory for Backups

Images
^^^^^^

Virtual Images can be uploaded to |morpheus| Storage Providers for use across Clouds. By default when no Storage Provider has been added, images will write to ``/var/opt/morpheus/morpheus-ui/vms``. Please ensure adequate space when uploading Images using local file paths.

Backups
^^^^^^^

|morpheus| can offload snapshots when performing backups to local or other Storage Providers. By default when no Storage Provider has been added, backups will write to ``/tmp/morpheus/backups/``. When using none NFS Storage providers, the backup file(s) must be written to ``/tmp/morpheus/working/`` before they can be zipped, sent to the destination Storage provider such as S3, and removed from ``/tmp/morpheus/working/``. Please ensure adequate space in ``/tmp/morpheus/`` when offloading Backups.

Migrations
^^^^^^^^^^

When performing a Hypervisor to Hypervisor migration, such as VMware to AWS, Virtual Images are written to local storage before conversion and/or upload to the target hypervisor. Please ensure adequate space in ``/var/opt/morpheus/morpheus-ui/vms`` or other configured local Storage Provider paths when performing Migrations.

VM Logs and Stats
^^^^^^^^^^^^^^^^^

When using a |morpheus| configuration with locally installed ElasticSearch, VM, Container, Host and Appliance logs and stats are are stored in Elasticsearch. Please ensure adequate space in ``/var``, specifically ``/var/opt/morpheus/elasticsearch`` in relation to the number or Instances reporting logs, log frequency, and log retention count.

|morpheus| Services Logs
^^^^^^^^^^^^^^^^^^^^^^^^

Logs for services local to the |morpheus| Appliance, such as the Morpheus ui, elasticsearch, rabbitmq, mysql, nginx and guacd are written to ``/var/log/morpheus/``. Current logs are rotated nightly, zipped, and files older than 30 days are automatically removed. Misconfigured services, ports and permissions can cause excessive log file sizes.


Network Connectivity
--------------------

|morpheus| primarily operates via communication with its agent that is installed on all managed vm's or docker hosts. This is a lightweight
agent responsible for aggregating logs and stats and sending them back to the client with minimal network traffic overhead. It also is capable
of processing instructions related to provisioning and deployments instigated by the appliance server.

The |morpheus| Agent exists for both linux and windows based platforms and opens NO ports on the guest operating system. Instead it makes an
outbound SSL (https/wss) connection to the appliance server. This is what is known as the ``appliance url`` during configuration (in
Admin->Settings). When the agent is started it automatically makes this connection and securely authenticates. Therefore, it is necessary for
all vm's and docker based hosts that are managed by morpheus to be able to reach the appliance server ip on port 443.

|morpheus| also utilizes SSH (Port 22) and Windows Remote Management (Port 5985) to initialize a server. This includes sending remote command
instructions to install the agent. It is actually possible for |morpheus| to operate without agent connectivity (though stats and logs
will not function) and utilize SSH/WinRM to perform operations. Once the agent is installed and connections are established SSH/WinRM
communication will stop. This is why an outbound requirement exists for the appliance server to be able to utilize port 22 and 5985.

.. NOTE:: In newer versions of morpheus this outbound connectivity is not mandatory. The agent can be installed by hand or via Guest Process API's on cloud integrations like VMware.

Components
----------

The Appliance Server automatically installs several components for the operation of |morpheus|. This includes:

-  RabbitMQ (Messaging)
-  MySQL (Logistical Data store)
-  Elasticsearch (Logs / Metrics store)
-  Redis (Cache store)
-  Tomcat (|morpheus| Application)
-  Nginx (Web frontend)
-  Guacamole (Remote console service for clientless remote console)
-  Check Server (Monitoring Agent for custom checks added via UI)

All of these are installed in an isolated way using chef zero to ``/opt/morpheus``. It is also important to note these services can be
offloaded to separate servers or clusters as desired. For details check the installation section and high availability.

Common Ports & Requirements
----------------------------

The following chart is useful for troubleshooting Agent install, Static IP assignment, Remote Console connectivity, and Image transfers.

.. csv-table:: Common Ports & Requirements
   :header: "Feature", "Method",  "OS", "Source", "Destination", "Port", "Requirement"
   :widths: 35, 25, 15, 15, 15, 10, 100

   "Agent Communication", "All", "All", "Node", "Appliance", 443, "DNS Resolution from node to appliance url"
   "Agent Install", "All", "Linux", "Node", "Appliance", 80, "Used for appliance yum and apt repos"
   " ", "SSH", "Linux", "Appliance", "Node", 22, "| DNS Resolution from node to appliance url
   | Virtual Images configured
   | SSH Enabled on Virtual Image"
   "","WinRM",Windows,Appliance,Node,5985,"| DNS Resolution from node to appliance url
   | Virtual Images configured
   | WinRM Enabled on Virtual Image(`winrm quickconfig`)"
   " ",Cloud-init,Linux, , , ,"| Cloud-init installed on template/image
   | Cloud-init settings populated in User Settings or in `Admin –> Provisioning`
   | Agent install mode set to Cloud-Init in Cloud Settings"
   " ",Cloudbase-init,Windows, , , ,"| Cloudbase-init installed on template/image
   | Cloud-init settings populated in User Settings or in `Admin –> Provisioning`
   | Agent install mode set to Cloud-Init in Cloud Settings"
   " ",VMtools,All, , , ,"| VMtools installed on template
   | Cloud-init settings populated in Morpheus user settings or in `Administration –> Provisioning` when using Static IP’s
   | Existing User credentials entered on Virtual Image when using DHCP
   | RPC mode set to VMtools in VMware cloud settings."
   "Static IP Assignment & IP Pools",Cloud-Init,All, , , ,"| Network configured in Morpheus (Gateway, Primary and Secondary DNS, CIDR populated, DHCP disabled)
   | Cloud-init/Cloudbase-init installed on template/image
   | Cloud-init settings populated in Morpheus user settings or in `Administration –> Provisioning`"
   " ", "VMware Tools",All, , , ,"| Network configured in Morpheus (Gateway, Primary and Secondary DNS, CIDR populated, DHCP disabled)
   | VMtools installed on Template/Virtual Image"
   Remote Console,SSH,Linux,Applaince,Node,22,"| ssh enabled on node
   | user/password set on VM or Host in Morpheus "
   " ",RDP,Windows,Appliance,Node,3389,"| RDP Enabled on node
   | user/password set on VM or Host in Morpheus"
   " ",Hypervisor Console,All,Appliance,ESXi Host,5900-6000+,"| GBB server opened on all ESXii host firewalls
   | *Port range req's vary per env
   | ESXi host names resolvable by morpheus appliance"
   "Morpheus Catalog Image Download", ,All,Appliance,AWS S3,443,"Available space at ``/var/opt/morpheus/``"
   "Image Transfer",Stream,All,Appliance,Datastore,443,"Hypervisor Host Names resolvable by Morpheus Appliance"
