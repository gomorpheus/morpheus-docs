.. _requirements:

Requirements
============

|morpheus| is a software-based appliance installation capable of orchestrating many clouds and hypervisors. Before an installation is started it is important to understand some of the base requirements.

In the simplest configuration |morpheus| needs one Appliance Server. The Appliance Server, by default, contains all the components necessary to orchestrate both VMs and containers. To get started some base requirements are recommended:

Base Requirements
-----------------

.. include:: applianceOsTable.rst

- **Memory:** `16 GB recommended <https://support.morpheusdata.com/s/article/How-does-Morpheus-manage-the-memory-it-uses?language=en_US>`_ for default installations. 8 GB minimum required with 4 GB+ available storage swap space
- **Storage:** 200 GB storage minimum (see Storage Considerations below)
- **CPU:** 4-core, 1.4 GHz (or better), 64-bit CPU recommended for all-in-one systems. For a distributed-tier installation, it's recommended each tier have 2-core, 1.4 GHz (or better), 64-bit CPU
- Network connectivity from your users to the appliance over TCP 443 (HTTPS)
- Superuser privileges via the ``sudo`` command for the user installing the |morpheus| appliance package
- |morpheus| service nodes must be configured to use accurate NTP servers. A service node may be an app node, database node, RabbitMQ, or Elasticsearch node (see |morpheus| system architecture details further on in the installation section for more details)
- Required repository access:
    - Prior to installing the |morpheus| Appliance you will need to ensure that the target server or virtual machine has access to the base YUM/DNF or APT repositories
    - A RHEL 8 server requires the ``codeready`` (codeready-builder-for-rhel-8-x86_64-rpms) repository be enabled and accessible
    - A RHEL 7 server requires access to Optional RPMs repo. The repository need to be enabled and accessible
- An appliance license is required for any operations involving provisioning
- Current major web browsers supporting modern standards, such as Google Chrome, Mozilla Firefox, Apple Safari, and Microsoft Edge are supported
- Internet Connectivity (optional)
   - Access to ``https://downloads.morpheusdata.com``, ``https://share.morpheusdata.com``, and ``https://d2u3hdjdxt56gx.cloudfront.net`` (the share.morpheusdata.com cloudfront domain that share package requests will redirect to) over port 443 required on app nodes when reconfiguring to download embedded packages and plugins.
   - Access to ``https://morpheus-images.morpheusdata.com``, ``https://registry.morpheusdata.com``, and ``https://playbooks.morpheusdata.com`` To download |morpheus|' system images and playbooks.
   - Offline installation requires installing the supplemental package in addition to the regular installation package. Local yum/apt repo access still required for offline installations.

.. NOTE:: Access to ``yum`` and ``apt`` repos is still required for offline installations.

-  VM and Host Agent Install (optional)
    - Inbound connectivity access from provisioned VMs and container hosts on port 443 (Agent install and communication). Port 80 may be required for older ``apt`` distros.

    - An Appliance URL that is accessible/resolvable to all managed hosts. It is necessary for all hosts that are managed by |morpheus| to be able to communicate with the appliance server ip on port 443. This URL is configured under |AdmSet|.

Storage Considerations
----------------------

Upon initial installation |morpheus| takes up less than 10 GB of space, however |morpheus| Services, Virtual Images, Backups, Logs, stats, and user-uploaded and imported data require adequate space on the |morpheus| Appliance(s) based on appliance configuration and activity. |morpheus| recommends at least 200 GB as a general figure to start from but storage needs will vary dramatically based on each specific use case. In some cases, significantly more space will be needed.

.. IMPORTANT:: It is the customer's responsibility to ensure adequate storage space per configuration and use case. The appliance should be properly monitored to ensure it does not run low on disk space.

Default Paths
^^^^^^^^^^^^^

``/opt/morpheus``
  Morpheus Application and Services Files
``/var/opt/morpheus``
  User, Application and Services Data, including default config Elasticsearch, RabbitMQ and Database data, default Virtual Image path, and working directory for Backups
``/var/opt/morpheus/morpheus-ui`` (HA Installations Only)
  In an HA Installation, a NFS share is required and mounted to this location.  Virtual Images, Plugins, and other shared files are stored at this path to be accessible for all nodes
``/home``
  Morpheus service account home data, such as configuration files
``/var/log``
  Morpheus Service logs
``/tmp``
  Storage for any temp files created by Morpheus or the operating system

.. toggle-header::
    :header: **Storage Calculator**

    .. raw:: html

      <iframe height="333px" width="850" id="storageCalculator" src="../../_static/storageCalculator/index.html" frameborder="0" allowfullscreen></iframe>
|
Images
^^^^^^

Virtual Images can be uploaded to |morpheus| Storage Providers for use across Clouds. By default when no Storage Provider has been added, images will write to ``/var/opt/morpheus/morpheus-ui/vms``. Please ensure adequate space when uploading Images using local file paths.

Backups
^^^^^^^

|morpheus| can offload snapshots when performing backups to local or other Storage Providers. By default when no Storage Provider has been added, backups will write to ``/var/opt/morpheus/bitcan/backups/``. When using none NFS Storage providers, the backup file(s) must be written to ``/var/opt/morpheus/bitcan/working/`` before they can be zipped, sent to the destination Storage provider such as S3, and removed from ``/var/opt/morpheus/bitcan/working/``. Please ensure adequate space in ``/var/opt/morpheus/bitcan/`` when offloading Backups.

.. note:: The backup /working and /backups paths are configurable in morpheus.rb with `bitcan['working_directory'] = '$path'` and `bitcan['backup_directory'] = '/tmp'`

VM Logs and Stats
^^^^^^^^^^^^^^^^^

When using |morpheus| with a locally-installed Elasticsearch configuration, VM, Container, Host and Appliance logs and stats are are stored in Elasticsearch. Please ensure adequate space in ``/var``, specifically ``/var/opt/morpheus/elasticsearch`` in relation to the number of Instances reporting logs, log frequency, and log retention count. With partition space at 85% filled or higher (by default), Elasticsearch will enter an unhealthy state and the |morpheus| appliance will not function properly.

|morpheus| Services Logs
^^^^^^^^^^^^^^^^^^^^^^^^

Logs for services local to the |morpheus| Appliance, such as the Morpheus UI, elasticsearch, rabbitmq, mysql, nginx and guacd are written to ``/var/log/morpheus/``. Current logs are rotated nightly, zipped, and files older than 30 days are automatically removed. Misconfigured services, ports and permissions can cause excessive log file sizes.

Network Connectivity
--------------------

|morpheus| primarily operates via communication with its Agent that is installed on all managed VMs or docker hosts. This is a lightweight agent responsible for aggregating logs and stats and sending them back to the client with minimal network traffic overhead. It also is capable of processing instructions related to provisioning and deployments instigated by the appliance server.

The |morpheus| Agent exists for both Linux and Windows-based platforms and opens NO ports on the guest operating system. Instead it makes an outbound SSL (HTTPS/WSS) connection to the appliance server. This is what is known as the ``appliance url`` during configuration (in |AdmSet|). When the Agent is started it automatically makes this connection and securely authenticates. Therefore, it is necessary for
all VMs and docker based hosts that are managed by |morpheus| to be able to reach the appliance server IP on port 443.

|morpheus| has numerous methods to execute Agent installation, including zero open port methods.

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

   "Agent Communication", "All", "All", "Node", "Appliance", 443, "| DNS Resolution from node to appliance url"
   "Agent Install", "All", "Linux", "Node", "Appliance", 80, "| Used for appliance yum and apt repos"
   " ", "SSH", "Linux", "Appliance", "Node", 22, "| DNS Resolution from node to appliance url
   | Virtual Images configured
   | SSH Enabled on Virtual Image"
   "","WinRM",Windows,Appliance,Node,5985,"| Not required for agent installation in VMware vCenter and vCloud Director type clouds. Otherwise, access from |morpheus| App Nodes to Instance Node on 5985
   | Virtual Images configured
   | WinRM Enabled on Virtual Image(`winrm quickconfig`)"
   " ",Cloud-init,Linux, , , ,"| Cloud-init installed on template/image
   | Cloud-init settings populated in User Settings or in `Administration > Settings > Provisioning`
   | Agent install mode set to Cloud-Init in Cloud Settings"
   " ",Cloudbase-init,Windows, , , ,"| Cloudbase-init installed on template/image
   | Cloud-init settings populated in User Settings or in `Administration > Settings > Provisioning`
   | Agent install mode set to Cloud-Init in Cloud Settings"
   " ",VMtools,All, , , ,"| VMtools installed on template
   | Cloud-init settings populated in Morpheus user settings or in `Administration > Settings > Provisioning` when using Static IP’s
   | Existing User credentials entered on Virtual Image when using DHCP
   | RPC mode set to VMtools in VMware cloud settings."
   "Static IP Assignment & IP Pools",Cloud-Init,All, , , ,"| Network configured in Morpheus (Gateway, Primary and Secondary DNS, CIDR populated, DHCP disabled)
   | Cloud-init/Cloudbase-init installed on template/image
   | Cloud-init settings populated in Morpheus user settings or in `Administration > Settings > Provisioning`"
   " ", "VMware Tools",All, , , ,"| Network configured in Morpheus (Gateway, Primary and Secondary DNS, CIDR populated, DHCP disabled)
   | VMtools installed on Template/Virtual Image"
   Remote Console,SSH,Linux,Appliance,Node,22,"| ssh enabled on node
   | user/password set on VM or Host in Morpheus "
   " ",RDP,Windows,Appliance,Node,3389,"| RDP Enabled on node
   | user/password set on VM or Host in Morpheus"
   " ",Hypervisor Console,All,Appliance,Hypervisor Hosts,443,"|  Hypervisor host names resolvable by morpheus appliance"
   "Morpheus Catalog Image Download", ,All,Appliance,AWS S3,443,"| Available space at ``/var/opt/morpheus/``"
   "Image Transfer",Stream,All,Appliance,Datastore,443,"| Hypervisor Host Names resolvable by Morpheus Appliance"

Communication Data
------------------

The following table contains communication information, including frequency and configurability between |morpheus| and its supported technology integrations.

.. list-table:: **Communication Frequency, Ports, and Protocols**
  :widths: auto
  :header-rows: 1

  * - ﻿Source
    - Push/Pull
    - Destination
    - Description
    - Default Interval
    - Configurable Internal
  * - Cloud Foundry App Check
    - Server Pull
    - Cloud Foundry Applications that exist within Morpheus
    - Automatically created during provisioning if using the related system node/container type in order to inspect the running state. May be manually created but must be a machine that exists in Morpheus.
    - 5 Minutes with 30 second recheck on failure.
    - Range of 1 minute to 3 hours of selectable intervals. Additionally, the default interval may be globally altered.
  * - Docker Container Check
    - Server Pull
    - Docker containers that exist within Morpheus
    - If no other check types apply, automatically created during provisioning if using the related system container type, in order to inspect the running state. May be manually created but must be a machine that exists in Morpheus.
    - 5 Minutes with 30 second recheck on failure.
    - Range of 1 minute to 3 hours of selectable intervals. Additionally, the default interval may be globally altered.
  * - Elastic Search Check
    - Server Pull
    - Elastic Search application
    - Automatically created during provisioning if using the related system node/container type in order to inspect the running state. May be manually created but does not need to exist in Morpheus.
    - 5 Minutes with 30 second recheck on failure.
    - Range of 1 minute to 3 hours of selectable intervals. Additionally, the default interval may be globally altered.
  * - Microsoft SQL Server Check
    - Server Pull
    - Microsoft SQL application
    - Automatically created during provisioning if using the related system node/container type in order to inspect the running state. May be manually created but does not need to exist in Morpheus.
    - 5 Minutes with 30 second recheck on failure.
    - Range of 1 minute to 3 hours of selectable intervals. Additionally, the default interval may be globally altered.
  * - Mongo Check
    - Server Pull
    - Mongo DB application
    - Automatically created during provisioning if using the related system node/container type in order to inspect the running state. May be manually created but does not need to exist in Morpheus.
    - 5 Minutes with 30 second recheck on failure.
    - Range of 1 minute to 3 hours of selectable intervals. Additionally, the default interval may be globally altered.
  * - MySQL Check
    - Server Pull
    - MySQL application
    - Automatically created during provisioning if using the related system node/container type in order to inspect the running state. May be manually created but does not need to exist in Morpheus.
    - 5 Minutes with 30 second recheck on failure.
    - Range of 1 minute to 3 hours of selectable intervals. Additionally, the default interval may be globally altered.
  * - Postgres Check
    - Server Pull
    - Postgres application
    - Automatically created during provisioning if using the related system node/container type in order to inspect the running state. May be manually created but does not need to exist in Morpheus.
    - 5 Minutes with 30 second recheck on failure.
    - Range of 1 minute to 3 hours of selectable intervals. Additionally, the default interval may be globally altered.
  * - Push API Check
    - Client Push
    - Morpheus API
    - External system push notifications to Morpheus for the purpose of ensuring the notifications are received.
    - 5 Minutes
    - Range of 1 minute to 3 hours of selectable intervals. Additionally, the default interval may be globally altered.  This is dependent on the external source and triggers an error after two missed intervals.
  * - Rabbit MQ Check
    - Server Pull
    - Rabbit MQ application
    - Automatically created during provisioning if using the related system node/container type in order to inspect the running state. May be manually created but does not need to exist in Morpheus.
    - 5 Minutes with 30 second recheck on failure.
    - Range of 1 minute to 3 hours of selectable intervals. Additionally, the default interval may be globally altered.
  * - Redis Check
    - Server Pull
    - Redis application
    - Automatically created during provisioning if using the related system node/container type in order to inspect the running state. May be manually created but does not need to exist in Morpheus.
    - 5 Minutes with 30 second recheck on failure.
    - Range of 1 minute to 3 hours of selectable intervals. Additionally, the default interval may be globally altered.
  * - Riak Check
    - Server Pull
    - Riak application
    - Automatically created during provisioning if using the related system node/container type in order to inspect the running state. May be manually created but does not need to exist in Morpheus.
    - 5 Minutes with 30 second recheck on failure.
    - Range of 1 minute to 3 hours of selectable intervals. Additionally, the default interval may be globally altered.
  * - SNMP Check
    - Server Pull
    - SNMP
    - Automatically created during provisioning if using the related system node/container type in order to inspect the running state. May be manually created but does not need to exist in Morpheus.
    - 5 Minutes with 30 second recheck on failure.
    - Range of 1 minute to 3 hours of selectable intervals. Additionally, the default interval may be globally altered.
  * - Socket Check
    - Server Pull
    - Web Socket
    - Automatically created during provisioning if using the related system node/container type in order to inspect the running state. May be manually created but does not need to exist in Morpheus.
    - 5 Minutes with 30 second recheck on failure.
    - Range of 1 minute to 3 hours of selectable intervals. Additionally, the default interval may be globally altered.
  * - Virtual Machine Check
    - Server Pull
    - Virtual Machine that exists within Morpheus
    - If no other check types apply, automatically created during provisioning if using the related system node type, in order to inspect the running state. May be manually created.
    - 5 Minutes with 30 second recheck on failure.
    - Range of 1 minute to 3 hours of selectable intervals. Additionally, the default interval may be globally altered.
  * - Web Check
    - Server Pull (GET) or Server Push (POST)
    - Web application
    - Automatically created during provisioning if using the related system node/container type in order to inspect the running state. May be manually created but does not need to exist in Morpheus.
    - 5 Minutes with 30 second recheck on failure.
    - Range of 1 minute to 3 hours of selectable intervals. Additionally, the default interval may be globally altered.
  * - Public Cloud Integration
    - Server Pull
    - Alibaba Cloud
    - Data synchronization
    - 5 Minutes
    - No
  * - Public Cloud Integration
    - Server Pull
    - Amazon AWS
    - Data synchronization
    - 5 Minutes
    - No
  * - Public Cloud Integration
    - Server Pull
    - Amazon AWS GovCloud
    - Data synchronization
    - 5 Minutes
    - No
  * - Public Cloud Integration
    - Server Pull
    - DigitalOcean
    - Data synchronization
    - 5 Minutes
    - No
  * - Public Cloud Integration
    - Server Pull
    - Google Cloud Platform
    - Data synchronization
    - 5 Minutes
    - No
  * - Public Cloud Integration
    - Server Pull
    - Huawei Cloud
    - Data synchronization
    - 5 Minutes
    - No
  * - Public Cloud Integration
    - Server Pull
    - IBM Cloud
    - Data synchronization
    - 5 Minutes
    - No
  * - Public Cloud Integration
    - Server Pull
    - Microsoft Azure
    - Data synchronization
    - 5 Minutes
    - No
  * - Public Cloud Integration
    - Server Pull
    - Open Telekom Cloud
    - Data synchronization
    - 5 Minutes
    - No
  * - Public Cloud Integration
    - Server Pull
    - Oracle Public Cloud
    - Data synchronization
    - 5 Minutes
    - No
  * - Public Cloud Integration
    - Server Pull
    - UpCloud
    - Data synchronization
    - 5 Minutes
    - No
  * - Public Cloud Integration
    - Server Pull
    - VMware on AWS
    - Data synchronization
    - 5 Minutes
    - No
  * - Private Cloud Integration
    - Server Pull
    - Cisco UCS Manager
    - Data synchronization
    - 5 Minutes
    - No
  * - Private Cloud Integration
    - Server Pull
    - Dell EMC
    - Data synchronization
    - 5 Minutes
    - No
  * - Private Cloud Integration
    - Server Pull
    - HPE
    - Data synchronization
    - 5 Minutes
    - No
  * - Private Cloud Integration
    - Server Pull
    - HPE OneView
    - Data synchronization
    - 5 Minutes
    - No
  * - Private Cloud Integration
    - Server Pull
    - KVM
    - Data synchronization
    - 5 Minutes
    - No
  * - Private Cloud Integration
    - Server Pull
    - MacStadium
    - Data synchronization
    - 5 Minutes
    - No
  * - Private Cloud Integration
    - Server Pull
    - Microsoft Azure Stack
    - Data synchronization
    - 5 Minutes
    - No
  * - Private Cloud Integration
    - Server Pull
    - Microsoft Hyper-V
    - Data synchronization
    - 5 Minutes
    - No
  * - Private Cloud Integration
    - Server Pull
    - Microsoft SCVMM
    - Data synchronization
    - 5 Minutes
    - No
  * - Private Cloud Integration
    - Server Pull
    - Nutanix Acropolis
    - Data synchronization
    - 5 Minutes
    - No
  * - Private Cloud Integration
    - Server Pull
    - Openstack
    - Data synchronization
    - 5 Minutes
    - No
  * - Private Cloud Integration
    - Server Pull
    - Oracle VM
    - Data synchronization
    - 5 Minutes
    - No
  * - Private Cloud Integration
    - Server Pull
    - Pivotal Cloud Foundry
    - Data synchronization
    - 5 Minutes
    - No
  * - Private Cloud Integration
    - Server Pull
    - Supermicro
    - Data synchronization
    - 5 Minutes
    - No
  * - Private Cloud Integration
    - Server Pull
    - Vmware vCloud Director
    - Data synchronization
    - 5 Minutes
    - No
  * - Private Cloud Integration
    - Server Pull
    - Vmware ESXi
    - Data synchronization
    - 5 Minutes
    - No
  * - Private Cloud Integration
    - Server Pull
    - VMware Fusion
    - Data synchronization
    - 5 Minutes
    - No
  * - Private Cloud Integration
    - Server Pull
    - VMware vCenter
    - Data synchronization
    - 5 Minutes
    - No
  * - Private Cloud Integration
    - Server Pull
    - Xen Server
    - Data synchronization
    - 5 Minutes
    - No
  * - Automation Integration
    -
    - Ansible
    -
    - N/A
    - No
  * - Automation Integration
    - Server Pull
    - Ansible Tower
    - Data synchronization
    - 10 Minutes
    - No
  * - Automation Integration
    - Server Pull
    - Chef
    - Data synchronization
    - 10 Minutes
    - No
  * - Automation Integration
    - Server Pull
    - Puppet
    - Data synchronization
    - 10 Minutes
    - No
  * - Automation Integration
    -
    - Terraform
    -
    - N/A
    - No
  * - Automation Integration
    - Server Pull
    - vRealize Orchestrator
    - Data synchronization
    - 10 Minutes
    - No
  * - Backup Integration
    - Server Pull
    - Commvault
    - Scheduled backup execution (1 Minute), Backup provider refresh (1 hour)
    - 1 Minute; 1 Hour
    - No
  * - Backup Integration
    - Server Pull
    - Veeam
    - Scheduled backup execution (1 Minute), Backup provider refresh (1 hour)
    - 1 Minute; 1 Hour
    - No
  * - Backup Integration
    - Server Pull
    - Rubrik
    - Scheduled backup execution (1 Minute), Backup provider refresh (1 hour)
    - 1 Minute; 1 Hour
    - No
  * - Backup Integration
    - Server Pull
    - Zerto
    - Scheduled backup execution (1 Minute), Backup provider refresh (1 hour)
    - 1 Minute; 1 Hour
    - No
  * - Backup Integration
    - Server Pull
    - Avamar
    - Scheduled backup execution (1 Minute), Backup provider refresh (1 hour)
    - 1 Minute; 1 Hour
    - No
  * - Build Integration
    - Server Pull
    - Jenkins
    - Data synchronization
    - 10 minutes
    - No
  * - Container Integration
    - Server Pull
    - Docker
    - Data synchronization
    - 5 Minutes
    - No
  * - Container Integration
    -
    - Docker Registry
    - On-demand
    - N/A
    - No
  * - Container Integration
    - Server Pull
    - Kubernetes
    - Data synchronization
    - 5 Minutes
    - No
  * - Deployment Integration
    - Server Pull
    - Git/Github
    - Syncing latest version of Git-tracked repos
    - On-demand when using a file or repository for Morpheus functions
    - No
  * - DNS Integration
    - Server Pull
    - AWS Route53
    - Data synchronization
    - 10 minute
    - No
  * - DNS Integration
    - Server Pull
    - Microsoft DNS
    - Data synchronization
    - 10 minute
    - No
  * - DNS Integration
    - Server Pull
    - PowerDNS
    - Data synchronization
    - 10 minute
    - No
  * - Identity Management Integration
    - Server Pull
    - Microsoft AD
    - User Role and Group Sync
    - N/A, On login
    - No
  * - Identity Management Integration
    - Server Pull
    - OneLogin
    - User Role and Group Sync
    - N/A, On login
    - No
  * - Identity Management Integration
    - Server Pull
    - Okta
    - User Role and Group Sync
    - N/A, On login
    - No
  * - Identity Management Integration
    - Server Pull
    - Jump Cloud
    - User Role and Group Sync
    - N/A, On login
    - No
  * - Identity Management Integration
    - Server Pull
    - LDAP
    - User Role and Group Sync
    - N/A, On login
    - No
  * - Identity Management Integration
    - Server Pull
    - SAML
    - User Role and Group Sync
    - N/A, On login
    - No
  * - IPAM Integration
    - Server Pull
    - Infoblox
    - Refresh network pool servers (1 Hour)
    - 1 Hour
    - Yes (Variable Throttle Rate)
  * - IPAM Integration
    - Server Pull
    - phpIPAM
    - Refresh network pool servers (1 Hour)
    - 1 Hour
    - No
  * - IPAM Integration
    - Server Pull
    - Bluecat
    - Refresh network pool servers (1 Hour)
    - 1 Hour
    - Yes (Variable Throttle Rate)
  * - IPAM Integration
    - Server Pull
    - SolarWinds
    - Refresh network pool servers (1 Hour)
    - 1 Hour
    - No
  * - ITSM Integration
    - Server Pull
    - ServiceNow
    - Approval sync
    - 5 Minutes
    - No
  * - ITSM Integration
    - Server Pull
    - Cherwell
    - Data synchronization
    - 10 Minutes
    - No
  * - ITSM Integration
    - Server Pull
    - Remedy
    - Data synchronization
    - 10 Minutes
    - No
  * - Key & Certificate Integration
    - Server Pull
    - Venafi
    - Certificate and Key Sync
    - 10 Minutes
    - No
  * - Load Balancer Integration
    - Server Pull
    - AzureLB
    - Data synchronization
    - 10 Minutes
    - No
  * - Load Balancer Integration
    - Server Pull
    - F5 BigIP
    - Data synchronization
    - 10 Minutes
    - No
  * - Load Balancer Integration
    - Server Pull
    - Citrix NetScaler
    - Data synchronization
    - 10 Minutes
    - No
  * - Logging Integration
    -
    - Syslog
    - On-demand
    - N/A
    - No
  * - Monitoring Integration
    - Server Pull
    - ServiceNow
    - Data synchronization
    - Depends on check configuration
    - Yes (part of check configuration)
  * - Monitoring Integration
    -
    - AppDynamics
    - On-demand
    - N/A
    - No
  * - Monitoring Integration
    -
    - NewRelic
    - On-demand
    - N/A
    - No
  * - Network Integration
    - Server Pull
    - NSX-T
    - Data synchronization
    - 10 Minutes
    - No
  * - Network Integration
    - Server Pull
    - Cisco ACI
    - Data synchronization
    - 10 Minutes
    - No
  * - Network Integration
    - Server Pull
    - Unisys Stealth
    - Data synchronization
    - 10 Minutes
    - No
  * - Storage Integration
    - Server Pull
    - 3Par
    - Updating storage metadata
    - 10 Minutes
    - No
  * - Storage Integration
    - Server Pull
    - Azure Storage
    - Updating storage metadata
    - 10 Minutes
    - No
  * - Storage Integration
    - Server Pull
    - Dell ECS
    - Updating storage metadata
    - 10 Minutes
    - No
  * - Storage Integration
    - Server Pull
    - Isilon
    - Updating storage metadata
    - 10 Minutes
    - No
  * - Morpheus Agent
    - Agent Pull
    - Application Tier
    - Secure Web Socket
    - Persistent
    - No

SELinux
-------

If not required by organizational policy, we recommend setting SELinux to "Permissive" or "Disabled" modes to prevent any unnecessary security-related issues. |morpheus| versions 3.6.0 and higher do support "Enforcing" mode if it is required by your organization due to IT policies. Set the mode appropriately prior to running the |morpheus| installer and it will make the required changes based on your chosen SELinux context.

.. IMPORTANT:: Setting SELinux to "Enforcing" mode requires policies to be configured correctly in order for the |morpheus| appliance to function correctly.

Supported Locales
-------------------

Morpheus supports a number of different UI locales, including:

  - English
  - French
  - German
  - Spanish
  - Chinese (Simplified)
  - Portuguese (Brazil)
  - Korean
  - Italian

The full list of supported locales can be viewed within the Morpheus UI via the "Default Appliance Locale" select list within Administration Settings.

Switching Locales
^^^^^^^^^^^^^^^^^

The language of text in the Morpheus UI can be changed by telling the Morpheus server which locale to use. A Locale is made up of a language code and a country code. For example "en_US" is the code for US English, whilst "en_GB" is the code for British English. When using the Morpheus UI software through a client, the Morpheus UI software server will send the UI text back to the client using the appropriate static Language Pack. All translations returned via Morpheus Internationalization have been made and approved prior to the Morpheus UI version release.

**Via Locale Settings in the Morpheus UI:**
An application wide default locale can be configured within the Master Tenant under Administration -> Settings -> Default Appliance Locale. An individual Morpheus user can configure a preferred locale within their user settings. Using a locale setting is the preferred method for switching the Morpheus UI language.

**Via the Accept-Language HTTP header:**
The Accept-Language request HTTP header advertises which languages the client is able to understand, and which locale variant is preferred. Most browsers will by default send a “Accept-Language” HTTP header when visiting websites. The value of Accept-Language will match the configured preference of the browser’s user language/locale settings. The Morpheus UI will automatically detect the Accept-Language header and return the UI text from the corresponding Language Pack where possible. If there is no matching Language Pack the English US language pack is displayed in the UI. If an application locale or user locale setting has been configured in the Morpheus UI, then this will override the user’s browser preferences.

**Via the “lang” query parameter:**
Morpheus has the capability to switch locales by passing a parameter called “lang” to the Morpheus UI request. For example, “operations/dashboard?lang=de” will switch the locale preference to German. Morpheus will automatically switch the user’s locale and store it in a cookie so subsequent requests will have the new header. If a user is unauthenticated then the user’s locale will be reset. To switch a locale back to English pass “?lang=en” as a query parameterin the Morpheus UI request.

.. NOTE:: Many of Morpheus' language packs are generated by our clients. For that reason, we cannot guarantee accuracy and completeness of the translation. As new UI elements are added, existing language sets may not have immediate updates to keep pace with application changes. If you would like to contribute to a new or existing language pack, contact your account team or Morpheus support. Contributed content will be included within the next application version.
