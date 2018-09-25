Requirements
============

|morpheus| is a software based appliance installation capable of orchestrating many clouds and hypervisors. Before an installation is
started it is important to understand some of the base requirements.

In the simplest configuration |morpheus| needs one Appliance Server. The Appliance Server, by default, contains all the components
necessary to orchestrate both vm's and containers. To get started some base requirements are recommended:

Base Requirements
-----------------

-  **Operating System:** Ubuntu 14.04 / 16.04 or
   CentOS/RHEL greater than 7.0.
-  **Memory:** 8 GB minimum
-  **Storage:** 100 GB storage minimum
-  Network connectivity from your users to the appliance over TCP 443
   (HTTPS)
-  Inbound connectivity access from provisioned vm's and container hosts
   on ports 443 and 80 (needed for agent communication)
-  Internet Connectivity from Appliance (To download from |morpheus|'
   public docker repositories and virtual image catalog)
-  Superuser privileges via the sudo command for the user installing the
   |morpheus| Appliance package.
-  An Appliance URL that is accessible to all managed hosts. It is
   necessary for all hosts that are managed by |morpheus| to be able to
   communicate with the appliance server ip on port 443. This URL is
   configured under Admin->Settings. |morpheus| also utilizes SSH (Port
   22) and Windows Remote Management (Port 5985) to initialize a server.
-  An Appliance License is required for any operations involving
   provisioning.

.. NOTE:: Ubuntu 16.10 and Amazon Linux are not supported.

.. TIP:: When using AWS for deploying your application we recommend m5.large as a starting point.  For other public clouds please select a comparable instance type.

Storage
-------

|morpheus| needs storage space for a few items. One is for the built-in Elasticsearch store (used for log aggregation and stats collection metrics). |morpheus| also keeps a workspace and local virtual image cache for doing virtual image conversion and blueprint upload. While the permanent store of these can
be offloaded via a Storage Provider some space is still recommended for dealing with non streamable virtual image formats.

In many common scenarios it might be prudent to configure a shared datastore on a storage cluster and mounted to ``/var/opt/morpheus/morpheus-ui``
(this is where all user based data and database data is persisted). There are several folders located within here that can be independently located as desired.

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
