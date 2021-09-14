.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. WARNING:: OpenStack v2 Identity API has been removed in v5.3.3

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version

.. .. include:: highlights.rst

New Features
============

:Amazon: - Added KMS KEY ID field in provisioning Advanced Options sections for specify an AWS KMS key for encrypting EBS Volumes during provisioning when volume encryption is enabled
         - Asia Pacific (Seoul) ap-northeast-2 region added

:Azure: - Select Availability Zones during Instance, App, and Cluster provisioning. Select "Availability Zone" from the "Availability Options" menu and then specify the appropriate Availability Zone from the additional field that appears in the wizard

:Clusters: - Added "Install Docker" checkbox to the Add Hosts wizard. When checked, Docker is installed and when left unchecked, |morpheus| assumes Docker is already installed or will be installed via Workflows or some other means
           - Added "Install Docker" checkbox to the Add Cluster Layout modal. When checked, Docker is installed and when left unchecked, |morpheus| assumes Docker is already installed or will be installed via Workflows or some other means
           - - New Kubernetes Cluster Layouts seeded: ``kubernetes-amazon-eks-1.20, kubernetes-external-1.21, kubernetes-1.20.2-ubuntu-18.04.5-morpheus-amd64, kubernetes-1.20.2-ubuntu-18.04.5-opentelekom-amd64, kubernetes-1.20.2-ubuntu-18.04.5-hyperv-amd64, kubernetes-1.20.2-ubuntu-18.04.5-openstack-amd64, kubernetes-1.20.2-ubuntu-18.04.5-nutanix-amd64, kubernetes-azure-aks-1.19.13, kubernetes-1.20.2-ubuntu-18.04.5-vmware-amd64, kubernetes-1.20.2-ubuntu-18.04.5-amazon-amd64, kubernetes-1.20.2-ubuntu-18.04.5-google-amd64,  kubernetes-google-gke``

:Google: - Added sync for Service Accounts and the ability to select a service account when provisioning Instances, Blueprints and Apps, Clusters and Hosts to Google Clouds. Once the Resource Pool is selected, the available service accounts are synced and the dropdown menu to select them appears
         - When provisioning to the default service account for the selected resource pool, an additional Access Scope option is presented. Users can opt to allow default access or to allow full access to all cloud APIs
         - |morpheus| will now onboard live cost data from GCP, see `GCP integration guide <https://docs.morpheusdata.com/en/5.3.3/integration_guides/Clouds/google/google.html#enabling-live-costing-for-gcp>`_ for configuration details
         - Google Kubernetes Engine (GKE) support added for creating, managing, discovering and provisioning to GKE Kubernetes Clusters.
         - Seoul Region Added

:Hosts: - Deleting a Host or VM (Infrastructure > Hosts) with “Remove Associated Instances” marked and “Remove Infrastructure” unmarked is now handled differently. Host records and A records are no longer removed and teardown-phase Tasks are not run. If the Cloud is configured to inventory existing resources, the host or VM will be synced back in as a unmanaged resource on the next cloud sync :superscript:`5.2.9`

:Huawei Cloud: - EIP billing mode changed to bill by traffic rather than bandwidth. Note that this change does not affect OTC Clouds which only bill by traffic :superscript:`5.2.9`

:Kubernetes: - Deactivated all 1.17 Cluster Layouts (no longer supported by k8s)
             - Google Kubernetes Engine (GKE) support added for creating, managing, discovering and provisioning to GKE Kubernetes Clusters.
             - New Cluster Layouts seeded: ``kubernetes-amazon-eks-1.20, kubernetes-external-1.21, kubernetes-1.20.2-ubuntu-18.04.5-morpheus-amd64, kubernetes-1.20.2-ubuntu-18.04.5-opentelekom-amd64, kubernetes-1.20.2-ubuntu-18.04.5-hyperv-amd64, kubernetes-1.20.2-ubuntu-18.04.5-openstack-amd64, kubernetes-1.20.2-ubuntu-18.04.5-nutanix-amd64, kubernetes-azure-aks-1.19.13, kubernetes-1.20.2-ubuntu-18.04.5-vmware-amd64, kubernetes-1.20.2-ubuntu-18.04.5-amazon-amd64, kubernetes-1.20.2-ubuntu-18.04.5-google-amd64,  kubernetes-google-gke``
             - Added support for either or both token and kubceconfig on external kube clusters

:Library: - Added Ubuntu 20 Layouts for nearly all supported Clouds :superscript:`5.2.9`
          - Added Debian 9 and 10 Layouts for VMware Clouds to the standard Morpheus Library :superscript:`5.2.9`
          - Added CentOS 8 (7.9, 8.3, 8.4) images for nearly all Cloud types
          - Added Rocky 8 images for VMware, Amazon, Google, Nutanix, OpenStack, DigitalOcean (and more) Cloud types
          - Added OpenSUSE 15 images for all compatible Clouds
          - Added Windows Server 2016 and 2019 images for Azure and Google Clouds
          - Disabled several deprecated System Instance Types and associated Layouts that are no longer maintained: **Cassandra, Confluence, Devstack, Hadoop, Jboss, Jenkins, Magento, Mongo, Moogsoft, Nexus, Percona, Puppet, RethinkDb, Riak, RiakCs, Stash, Solr, Wordpress, and Zookeeper**. NOTE: this only disables the Instance type from the system seeded library and does not affect user created Insatnce Types or Layouts. :superscript:`5.2.9`

:Logs: - Splunk and LogRhythm integrations removed from Administration > Settings > Logs

:Migrations: - Migrations UI (under the Tools menu) is deprecated and removed

:Network: - Added a Display Name field for networks, this value appears as the network name on the network display page (Infrastructure > Network). For synced networks, the name and display name will initially be identical but users can edit the display name if it makes sense to present a friendlier name to users :superscript:`5.2.9`
          - Added ability to change network during an Instance reconfigure (Select Reconfigure from the Instance Actions menu) for Instances in VMware and OpenStack Clouds. In other Clouds, network is still a read-only field during Instance reconfigure :superscript:`5.2.9`

:OpenStack: - Create, modify, and delete OpenStack Projects (Resource Pools) from Cloud detail pages
            - Added option to specify an OpenStack project at provision time through the Resource Pool dropdown menu. This option is available when provisioning Instances, Apps, and Clusters
            - Support for v2 Identity API was deprecated in 5.2.9 and has been dropped for this release

:Packages: - New ``/administration/packages`` component added targeted for uploading future |morpheus| provided mpg's, however users will be able to create, distribute and/or import custom |morpheus| packages. Additional information on creating custom packages will be provided.
           - New Role permission ``Admin: Packages`` (None, Full) added. Allows or disallows access to the Packages tab on the Integrations page (Administration > Integrations)

:Profiles: - New ``Profiles`` component added to Clouds with ``Terraform Profile`` and ``Key/Value Profile`` types. Profiles give users the ability to create custom object associated secrets and metadata that will automatically be mapped during provisioning and automation.
           - Terraform Profiles allow created cloud associated tfvars secrets, allowing tf apps and specs to be provisioned across multiple clouds that required different tfvars.
           - Key/Value Profiles expand provisioning, automation, billing and reporting capabilities by allowing dynamic custom object specific metadata in provisioning and automation mappings using ``<%=cloud.profile.key%>``

:ServiceNow: - Optimized CMDB sync performance to significantly reduce sync times for large cmdb record sets.
             - ServiceNow Multi-Domain (domain separation) Support added. Note: Requires upcoming plugin version

:Terraform: - Added UI feedback and status indication when refreshing Terraform Instance state (:guilabel:`REFRESH STATE` button or "Refresh State" selection from Instance Actions menu)
            - Added support for ``count`` and ``for_each`` loops
            - ``terraform`` command line added to State tabs for executing tf cli commands with execution output
            - Added cloudConfig.agentInstall variable for adding agent install script to tf. Example: ``<%=instance?.cloudConfig?.agentInstall%>`` can be used in userdata section of an aws_instance
            - Custom Options can now be used in tf library configs. For example, option types  can be set on tf layouts or associated Instance Types and <%=customOptions.key%> used tf.

:UI: - Added more detailed help block text for the Private Key field when storing a new key pair in Morpheus (Infrastructure > Keys & Certs > Key Pairs) :superscript:`5.2.9`
     - Execution and history tabs: Execution output is now limited on initial load to 10k characters per event with an option to load the full output for each event
     - Help text added to Add Integration modals warning that HTTP URLs are insecure and not recommended

:vCloud Director: - System administrator account credentials can now be provided to authenticate vCD Cloud integrations in |morpheus|. Previously, only organization administrator credentials could be used. Keep in mind that you will need to set the system administrator account credentials appropriately, for example, to be able to see entities created by the organization administrator
                  - Added the option to specify a catalog to store |morpheus|-provisioned artifacts, previously |morpheus| would always create and use a "morpheus_auto" catalog

:VDI: - VDI pools can now be configured to be "Recyclable". When enabled, the VDI Instance will revert back to a snapshot and become available once again after the user has logged out and the VDI session has expired. This behavior will not apply to VDI pools which are also configured to be persistent because in that configuration the Instance is merely stopped and saved for the user's next session. This feature is currently only available for Cloud types which support snapshot management (VMware, Nutanix, and vCD)
      - Improved image streaming in low bandwidth situations


:VMware vCenter: - Added support for VMware Content Library. |morpheus| automatically on-boards items from your content library and re-syncs them regularly to keep them up to date. Add images from the |morpheus| library to Node Types for use in Layouts and Instance Types
                 - The UUID for hypervisor hosts synced into vCenter Clouds is now stored to the ``unique_id`` field on hypervisor host ``compute_server`` records :superscript:`5.2.9`
                 - Improved sync performance for VMware Resource Pools and Folders :superscript:`5.2.9`

Fixes
=====

:Amazon: - Fixed issue with creating S3 Buckets when using STS Assume Role
:Analytics: - Cloud Costs: Fixed selecting a tag name and value combination in the "more" filters in Cloud Cost Analysis :superscript:`5.2.9`
:Ansible: - Ansible Galaxy: New ``roles`` working folder added, resolves intermittent "galaxy dependent roles can not be found" issue when using git integration source :superscript:`5.2.9`
          - Fixed display of checkbox values for ``USE ANSIBLE GALAXY``, ``ENABLE VERBOSE LOGGING`` and ``USE MORPHEUS AGENT COMMAND BUS`` options in UI.  :superscript:`5.2.9`
          - Fixed Ansible task execution issue caused by special characters in user name :superscript:`5.2.9`
:API: - Currencies: Fixed creating Prices with USN currency via API :superscript:`5.2.9`
      - Tenants: Fixed deletion of Tenants with existing Instances when ``removeResources=on`` :superscript:`5.2.9`
      - Tenants: Fixed deletion of Tenants with existing users via API/CLI :superscript:`5.2.9`
      - Updated response for ``GET ... /api/zones`` when no clouds exist. :superscript:`5.2.10`
:Appliance: - Agent installation: Reconfigure process updated to add ``/var/opt/morpheus/package-repos/yum/el/8.2 -> /var/opt/morpheus/package-repos/yum/el/8`` symlink to handle agent installation requests for centos/rhel configurations version pinned to ``8.2`` :superscript:`5.2.10`
:Automation: - Updated cron syntax validation for schedules & human readable cron string now updates before save
:Azure: - ARM Spec Templates: Fixed repo path issue with ARM spec templates stored in a Git repository :superscript:`5.2.9`
        - Costing: |morpheus| now stores the actual currency and conversion rates during cost syncs to address reporting, budget and analytic values of non-usd actuals when the tenants defined currency does not match actual cost currency :superscript:`5.2.10`
        - Fixed issue with record being association with the deleted record of a re-synced service plan :superscript:`5.2.10`
        - Fixed ``Actions -> Start/Stop`` for discovered VMs that were converted to managed :superscript:`5.2.9`
        - Fixed syncing of private images that do not belong to the scoped region of the cloud (not applicable when cloud is scoped to all regions).
        - Network selection now scoped by region
:Blueprints: - Rapidly activating different Builder, Raw, and Preview tabs in the blueprint wizard no longer causes the active tab content to get stuck. :superscript:`5.2.9`
:Cloning: - Agent Installation: Fixed agent installation issue when Cloning a Windows Instance caused by existing ``C:\installAgent.ps1`` file. :superscript:`5.2.9`
:Clusters: - Docker Clusters: Fixed custom option type issues required flag enforcement and type ahead option type issue when provisioning Docker Clusters :superscript:`5.2.9`
           .. - Fixed 500 error when selecting existing K8s cluster that is associated with a disabled cluster layout
:Code: - Git: Fixed pull issue with some git integrations (ADO) using https basic auth cause by appending ``.git`` to repo url
:Costing: - Fixed inaccuracies on the MTD costing and pricing information getting calculated on server invoice records when ``Sync Costing`` is enabled on Cloud Types that do not have costing integrations
:Google: - Fix duplicate subnet record creation for Shared Networks when cloud scoping is changed between a single region and all regions
:Groups: - ``Infrastructure -> Groups`` Fixed Cloud count hiding after 30 seconds :superscript:`5.2.9`
:Guidance: - CPU Recomendations: Fixed guidance execution defaulting the CPU back to 1 :superscript:`5.2.9`
:Health: - Fixed issue with |morpheus| Appliance logs not displaying in ``Administration -> Health: Logs`` when ``appliance_instance`` id not equal to ``1`` :superscript:`5.2.9`
:Keys & Certs: - Synced keypairs are now filtered from Key Pairs selection list in user settings and admin provisioning settings. Synced Key Pair records do not contain any key data and are not usable for user and global keypairs. :superscript:`5.2.9`
:Image Builder: - Fixed issue with delayed boot command execution during image builds :superscript:`5.2.9`
:Instance: - Tags: Fixed issue with tag sync where adding a new tag post-provision could remove existing tags
:KVM: - Fixed infrastructure deletion of discovered VMs on brownfield KVM clusters :superscript:`5.2.10`
:Library: - Fixed display of sub-tab selection in ``Provisioning -> Library`` UI mobile views :superscript:`5.2.9`
          - Removed some old and unused catalog items from the |morpheus| standard Library :superscript:`5.2.9`
:Localization: - Portuguese: The strings displayed in the Create Cloud dialog are now being displayed properly when selecting Portuguese as the language. Pass in ``?lang=pt_BR`` or ``?lang=pt_PT`` in the url to force the UI to Portuguese Brazil and Portugal, respectively :superscript:`5.2.9`
:Networks:  - Removed deprecated delete option for networks interfaces in Network tab on Instance and Host detail pages. Network interfaces are managed via reconfigure. :superscript:`5.2.9`
:NSX: - Fixed ability to select SERVICE TYPE at the time of NSX-T SSL certificate creation in a Tenant. :superscript:`5.2.9`
      - Fixed members being added to LB pools when adding nodes to an Instance via ``Actions -> Add Node`` :superscript:`5.2.9`
      - Fixed NSX-V VMs added as a part of an app with a load balancer on 1 or more instances being added to pools :superscript:`5.2.10`
      - Fixed ui display issue updating NSX-V Firewall rule priority order after editing rule priority orders :superscript:`5.2.10`
      - Fix visibility of NSX-T Pools created in subtenants on master tenant NSX-T public integrations :superscript:`5.2.10`
:Option Types: Fixed Rest Option Lists Posts filtering out dependent Variables
:Provisioning: - ``Copies`` field now hidden when when a Load Balancer is configured :superscript:`5.2.10`
               - Fixed ``Copies`` field value not applying when using scroll up/down :superscript:`5.2.9`
:Policies: - Delayed Removal: Fixed deleting an unmanaged vm within a Delayed Removal Policy Scope and with "Remove Associated Instances" check causing VM to shut down :superscript:`5.2.9`
           - Fixed Boot order for App tiers not being honored when a provision approval policy is enforced :superscript:`5.2.9`
           - Tag Enforcement: Fixed Tagging Policy not accepting Morpheus Variables as valid input when used in exported option types
:Rubrik: - Backup size now displayed as ``-`` instead of ``0`` when backup size is not available :superscript:`5.2.9`
:Reports: - Fix for display of utilization statistics in some Cloud Usage Reports :superscript:`5.2.9`
:Roles: - Activity: Fixed viewing ``Operations -> Activity`` activity logs requiring ``Operations: Reports`` permissions :superscript:`5.2.9`
        - Datastores: Edit option no longer displayed for Role Permission ``Infrastructure -> Datastores: Read`` :superscript:`5.2.9`
:Security: - Reconfigure and Library XSS vulnerabilities remediated :superscript:`5.2.10`
           - Updated request handling of user scoped policy creation during policy creation :superscript:`5.2.10`
:Tasks: - Chef Bootstrap: Fixed issues where Chef Bootsrap execution would fail with reason "Chef Infra Client cannot execute without accepting the license" :superscript:`5.2.9`
       - Variables: Fixed evaluation of <%=user.username%> variable in task executions :superscript:`5.2.9`
:Terraform: - Fixed UI issue with ``NEXT`` and ``COMPLETE`` buttons becoming active before validation had completed :superscript:`5.2.10`
            - Fixed ``null`` tf variable values redering as ``[object object]`` in UI  :superscript:`5.2.9`
            - Deleting a VM associated with an Instance in Terraform App with ``Remove associated Instances`` enabled, and the associated Instance is the only Instance in the App, no longer deletes the associated App.
            - Added validation for deleting a Terraform app when ``deletion_protection=true`` in Terraform.
            - Fixed ``for_each`` loop value nulled when using tfvars within cypher
            - Fixed issue with resource -> image mapping that caused vm's associated with resources to remain as ``discovered`` server types 
:User Settings: - Success Message added on save when updating Linux/Windows passwords in user settings (Displays for 5s then fades) :superscript:`5.2.9`
:UI: Execution and history tabs: Execution output is now limited on initial load to 10k characters per event with an option to load the full output for each event to address loading of large execution history datasets 
:vCloud Director: - Fixed issue with user-data iso attachment when provisioning cloudbase-init enabled Windows images :superscript:`5.2.10`
                  - Fixed ``safeComputerName`` issue during Windows Guest Customizations :superscript:`5.2.9`
:VMware: - Fixed duplicate filename issue when adding multiple disks during reconfigure :superscript:`5.2.10`
         - Fixed storage volume values not updating on sync when volumes were removed in vCenter but the total number of volumes matches |morpheus| records. :superscript:`5.2.10`
         - Optimizations added for Resource Pool and Folder sync. Resolves issue with loading Resource Pools in add cloud wizard in environments with 500+ Resource Pools. :superscript:`5.2.9`
         - Volumes now update properly when changing Image selection when provisioning the VMWARE Instance Type :superscript:`5.2.9`
         - |morpheus| will no longer append ``localdomain`` to DNS suffix information in unattend customization XML when no domain or default domain are specified.


|morpheus| API & CLI Improvements
=================================

:Instances: - Calls to the ``instances`` API to GET a specific Instance (at multiple levels including Instance, container details, and server) now include the ``uuid`` property :superscript:`5.2.9`
            - Added options to remove expiration, extend expiration, cancel shutdown, extend shutdown, and cancel removal for Instances from API and CLI

:Checks: - The ``apiKey`` is now returned in GET calls for Push API-Type Monitoring Checks

:Cluster Layouts: - Added flag to install Docker when creating Cluster Layouts from API and CLI. When disabled, |morpheus| assumes Docker is already installed or will be installed via Workflows or some other means

:Logs: - Support removed for Splunk and LogRhythm integrations (as has been done in |morpheus| UI)

:NSX-T: - Create, manage, and delete NSX-T segments :superscript:`5.2.9`
        - Manage Group visibility for NSX-T segments :superscript:`5.2.9`
        - Create, manage, and delete Tier 0 and Tier 1 routers :superscript:`5.2.9`
        - Attach and detach Tier 1 routers to Tier 0 routers :superscript:`5.2.9`
        - Retrieve any NSX-T objects which are associated with Tier 0 or Tier 1 routers :superscript:`5.2.9`
        - Create, manage, and delete DNAT and SNAT rules :superscript:`5.2.9`

:Reports: - Fix for display of utilization statistics in some Cloud Usage Reports :superscript:`5.2.9`

:vCD: - Added ability to set the Recyclable attribute on VDI Pools through API and CLI

:Virtual Images: - Added option to remove the virtual image from the cloud (or not) when the image is deleted from |morpheus| through API and CLI

Appliance & Agent Updates
=========================

:Appliance: - Agent installation: Reconfigure process updated to add ``/var/opt/morpheus/package-repos/yum/el/8.2 -> /var/opt/morpheus/package-repos/yum/el/8`` symlink to handle agent installation requests for centOS/rhel configurations version pinned to ``8.2`` :superscript:`5.2.10`
            - Java Updated to 8u302-b08 :superscript:`5.2.9`
            - Tomcat verison update to v9.0.50 :superscript:`5.2.9`
            
:Agent Packages: - Java Updated to 8u302-b08 :superscript:`5.2.9`
                 - |morpheus| Node and VM Node Packages version update to 3.2.1 :superscript:`5.2.9`
