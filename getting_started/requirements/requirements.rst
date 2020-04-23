Requirements
============

|morpheus| is a software based appliance installation capable of orchestrating many clouds and hypervisors. Before an installation is started it is important to understand some of the base requirements.

In the simplest configuration |morpheus| needs one Appliance Server. The Appliance Server, by default, contains all the components necessary to orchestrate both vm's and containers. To get started some base requirements are recommended:

Base Requirements
-----------------

- **Operating System:** Ubuntu 16.04, 18.04 or CentOS/RHEL 7.x
- **Memory:** 16 GB recommended for default installations. 8 GB minimum required with 4 GB+ available storage swap space
- **Storage:** 200 GB storage minimum (see Storage Considerations below)
- **CPU:** 4-core, 1.4 GHz (or better), 64-bit CPU recommended for all-in-one systems. For a distributed-tier installation, it's recommended each tier have 2-core, 1.4 GHz (or better), 64-bit CPU
- Network connectivity from your users to the appliance over TCP 443 (HTTPS)
- Superuser privileges via the sudo command for the user installing the |morpheus| appliance package
- Access to base yum and apt repos
- An appliance license is required for any operations involving provisioning

- Internet Connectivity (optional)
   - To download from |morpheus|' public docker repositories and system Virtual Image catalog
   - Offline installation require installing the offline package in addition to the regular installation package.

.. NOTE:: Access to base yum and apt repos is still required for offline installations.

-  VM and Host Agent Install (optional)
    - Inbound connectivity access from provisioned vm's and container hosts on ports 443 (Agent install and communication) and 80 (Linux Agent installs via yum and apt)
    - An Appliance URL that is accessible/resolvable to all managed hosts. It is necessary for all hosts that are managed by |morpheus| to be able to communicate with the appliance server ip on port 443. This URL is configured under Admin->Settings.

.. NOTE:: Ubuntu 16.10, CentOS/RHEL 8.x and Amazon Linux are not currently supported.

.. NOTE:: Morpheus fully supports running the appliance in a VMware environment and many other virtualized environments, as well as on a physical platform.

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

Logs for services local to the |morpheus| Appliance, such as the Morpheus UI, elasticsearch, rabbitmq, mysql, nginx and guacd are written to ``/var/log/morpheus/``. Current logs are rotated nightly, zipped, and files older than 30 days are automatically removed. Misconfigured services, ports and permissions can cause excessive log file sizes.


Network Connectivity
--------------------

|morpheus| primarily operates via communication with its agent that is installed on all managed vm's or docker hosts. This is a lightweight
agent responsible for aggregating logs and stats and sending them back to the client with minimal network traffic overhead. It also is capable
of processing instructions related to provisioning and deployments instigated by the appliance server.

The |morpheus| Agent exists for both linux and windows based platforms and opens NO ports on the guest operating system. Instead it makes an
outbound SSL (https/wss) connection to the appliance server. This is what is known as the ``appliance url`` during configuration (in
Admin->Settings). When the agent is started it automatically makes this connection and securely authenticates. Therefore, it is necessary for
all vm's and docker based hosts that are managed by morpheus to be able to reach the appliance server ip on port 443.

|morpheus| has numerous methods to execute agent installation, including zero open port methods.

Components
----------

The Appliance Server automatically installs several components for the operation of |morpheus|. This includes:

-  RabbitMQ (Messaging)
-  MySQL (Logistical Data store)
-  Elasticsearch (Logs / Metrics store)
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
   "","WinRM",Windows,Appliance,Node,5985,"| Not required for agent installation in VMware vCenter and vCloud Director type clouds. Otherwise, access from |morpheus| App Nodes to Instance Node on 5985
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
   Remote Console,SSH,Linux,Appliance,Node,22,"ssh enabled on node
   | user/password set on VM or Host in Morpheus "
   " ",RDP,Windows,Appliance,Node,3389,"RDP Enabled on node
   | user/password set on VM or Host in Morpheus"
   " ",Hypervisor Console,All,Appliance,Hypervisor Hosts,443,"
   |  Hypervisor host names resolvable by morpheus appliance"
   "Morpheus Catalog Image Download", ,All,Appliance,AWS S3,443,"Available space at ``/var/opt/morpheus/``"
   "Image Transfer",Stream,All,Appliance,Datastore,443,"Hypervisor Host Names resolvable by Morpheus Appliance"

SELinux
-------

If not required by organizational policy, we recommend setting SELinux to "Permissive" or "Disabled" modes to prevent any unnecessary security-related issues. |morpheus| versions 3.6.0 and higher do support "Enforcing" mode if it is required by your organization due to IT policies. Set the mode appropriately prior to running the |morpheus| installer and it will make the required changes based on your chosen SELinux context.

.. IMPORTANT:: Setting SELinux to "Enforcing" mode requires policies to be configured correctly in order for the |morpheus| appliance to function correctly.

Supported Languages
----------------------------

Morpheus supports a number of different UI languages, including:

  - English
  - German
  - Spanish
  - Chinese (Simplified)

Currently, UI language is not configurable from within Morpheus itself. Changing the language within the application will involve some combination of operating system and web browser language setting changes. Morpheus must also have a translation set for your chosen language to see a change. Depending on the browser and the operating system, you may need to fully close and reopen the web browser or restart the machine completely.

.. NOTE:: Many of Morpheus' language packs are generated by our clients. For that reason, we cannot guarantee accuracy and completeness of the translation. As new UI elements are added, existing language sets may not have immediate updates to keep pace with application changes. If you would like to contribute to a new or existing language pack, contact your account team or Morpheus support. Contributed content would be included with the next application update.
