.. _Release Notes:

************************
|morphver| Release Notes
************************

.. No highlights this time, small update
  .. include:: highlights.rst

.. WARNING:: OpenStack v2 Identity API will be deprecated in v5.2.9 and will be removed in v5.3.3

New Features
============

:Huawei Cloud: - EIP billing mode changed to bill by traffic rather than bandwidth. Note that this change does not affect OTC Clouds which only bill by traffic
:Library: - Added Debian 9 and 10 Layouts for VMware Clouds to the standard |morpheus| Library
          - Added Ubuntu 20 Layouts for nearly all supported Clouds
          - Disabled several deprecated System Instance Types and associated Layouts that are no longer maintained: **Cassandra, Confluence, Devstack, Hadoop, Jboss, Jenkins, Magento, Mongo, Moogsoft, Nexus, Percona, Puppet, RethinkDb, Riak, RiakCs, Stash, Solr, Wordpress, and Zookeeper**. Note: this only disables the Instance type from the system seeded library and does not affect user created Insatnce Types or Layouts.
:Network: - Added ability to change network during an Instance reconfigure (Select Reconfigure from the Instance Actions menu) for Instances in VMware and OpenStack Clouds. In other Clouds, network is still a read-only field during Instance reconfigure
          - Added a Display Name field for networks, this value appears as the network name on the network display page (Infrastructure > Network). For synced networks, the name and display name will initially be identical but users can edit the display name if it makes sense to present a friendlier name to users
:Openstack: - OpenStack v2 Identity API will be deprecated in v5.2.9 and will be removed in v5.3.3
:UI: - Added more detailed help block text for the Private Key field when storing a new key pair in |morpheus| (Infrastructure > Keys & Certs > Key Pairs)
     - jQuery version update to v3.6.0
     - Success Message added on save when updating Linux/Windows passwords in User Settings
:VMware vCenter: - The UUID for hypervisor hosts synced into vCenter Clouds is now stored to the ``unique_id`` field on hypervisor host ``compute_server`` records
                 - Improved sync performance for VMware Resource Pools and Folders

|morpheus| API and CLI Improvements
===================================

:Hosts: - Deleting a Host or VM (Infrastructure > Hosts) with "Remove Associated Instances" marked and "Remove Infrastructure" unmarked is now handled differently. Host records and A records are no longer removed and teardown-phase Tasks are not run. If the Cloud is configured to inventory existing resources, the host or VM will be synced back in as a unmanaged resource on the next cloud sync
:Instances: - Calls to the ``instances`` API to GET a specific Instance (at multiple levels including Instance, container details, and server) now include the ``uuid`` property
:NSX-T: - Create, manage, and delete distributed firewall groups and rules
        - Create, manage, and delete DNAT and SNAT rules
        - Create, manage, and delete Tier 0 and Tier 1 routers
        - Manage Group visibility for Tier 0 and Tier 1 routers
        - Attach and detach Tier 1 routers to Tier 0 routers
        - Retrieve any NSX-T objects which are associated with Tier 0 or Tier 1 routers
        - Create, manage, and delete NSX-T segments
        - Manage Group visibility for NSX-T segments

Fixes
=====

:Analytics: - Cloud Costs: Fixed selecting a tag name and value combination in the "more" filters in Cloud Cost Analysis
:Ansible: - Ansible Galaxy: New ``roles`` working folder added, resolves intermittent "galaxy dependent roles can not be found" issue when using git integration source
          - Fixed display of checkbox values for ``USE ANSIBLE GALAXY``, ``ENABLE VERBOSE LOGGING`` and ``USE MORPHEUS AGENT COMMAND BUS`` options in UI. 
          - Fixed Ansible task execution issue caused by special characters in user name
:API: - Tenants: Fixed deletion of Tenants with existing Instances when ``removeResources=on``
      - Tenants: Fixed deletion of Tenants with existing users via API/CLI
:Azure: - ARM Spec Templates: Fixed repo path issue with ARM spec templates stored in a Git repository
        - Fixed ``Actions -> Start/Stop`` for discovered VMs that were converted to managed
:Blueprints: - Rapidly activating different Builder, Raw, and Preview tabs in the blueprint wizard no longer causes the active tab content to get stuck.
:Cloning: - Agent Installation: Fixed agent installation issue when Cloning a Windows Instance caused by existing ``C:\installAgent.ps1`` file.
:Clusters: - Docker Clusters: Fixed custom option type issues required flag enforcement and type ahead option type issue when provisioning Docker Clusters
:Currencies: - API: Fixed creating Prices with USN currency via API
:Groups: - ``Infrastructure -> Groups`` Fixed Cloud count hiding after 30 seconds
:Guidance: - CPU Recomendations: Fixed guidance execution defaulting the CPU back to 1
:Health: - Fixed issue with |morpheus| Appliance logs not displaying in ``Administration -> Health: Logs`` when ``appliance_instance`` id not equal to ``1``
:Image Builder: - Fixed issue with delayed boot command execution during image builds
:Keys & Certs: - Synced keypairs are now filtered from Key Pairs selection list in user settings and admin provisioning settings. Synced Key Pair records do not contain any key data and are not usabled for user and global keypairs.
:Library: - Fixed display of sub-tab selection in ``Provisioning -> Library`` UI mobile views
          - Removed some old and unused catalog items from the |morpheus| standard Library
:Localization: - Portuguese: The strings displayed in the Create Cloud dialog are now being displayed properly when selecting Portuguese as the language. Pass in ``?lang=pt_BR`` or ``?lang=pt_PT`` in the url to force the UI to Portuguese Brazil and Portugal, respectively
:Networks:  - Removed deprecated delete option for networks interfaces in Network tab on Instance and Host detail pages. Network interfaces are managed via reconfigure.
:NSX: - Fixed ability to select SERVICE TYPE at the time of NSX-T SSL certificate creation in a Tenant.
      - Fixed members being added to LB pools when adding nodes to an Instance via ``Actions -> Add Node``
:Policies: - Delayed Removal: Fixed deleting an unmanaged vm within a Delayed Removal Policy Scope and with "Remove Associated Instances" check causing VM to shut down
           - Fixed Boot order for App tiers not being honored when a provision approval policy is enforced
:Provisioning: - Fixed ``Copies`` field value not applying when using scroll up/down
:Reports: - Fix for display of utilization statistics in some Cloud Usage Reports
:Roles: - Activity: Fixed viewing ``Operations -> Activity`` activity logs requiring ``Operations: Reports`` permissions
        - Datastores: Edit option no longer displayed for Role Permission ``Infrastructure -> Datastores: Read``
:Rubrik: - Backup size now displayed as ``-`` instead of ``0`` when backup size is not available
:Tasks: - Chef Bootstrap: Fixed issues where Chef Bootsrap execution would fail with reason "Chef Infra Client cannot execute without accepting the license"
        - Variables: Fixed evaluation of <%=user.username%> variable in task executions
:Terraform: - Fixed ``null`` tf variable values redering as ``[object object]`` in UI 
:User Settings: - Success Message added on save when updating Linux/Windows passwords in user settings (Displays for 5s then fades)
:vCD: - Windows User creation is not working for guest customizations
:vCloud Director: - Fixed ``safeComputerName`` issue during Windows Guest Customizations
:VMware: - Optimizations added for Resource Pool and Folder sync. Resolves issue with loading Resource Pools in add cloud wizard in environments with 500+ Resource Pools.
         - Volumes now update properly when changing Image selection when provisioning the VMWARE Instance Type

Appliance & Agent Updates
=========================

:Appliance: - Git: The local code repository path has been moved from ``/var/opt/morpheus/morpheus-ui/repo`` to ``/var/opt/morpheus/morpheus-local/repo`` to reduce potential shared storage issues and performance restrictions. The reconfigure process creates the folders and sets the paths in application.yml, no manual intervention is needed unless symlinks exist on ``/var/opt/morpheus/morpheus-ui/repo/git`` which will need to be removed prior to reconfiguring 5.3.2. The old ``/var/opt/morpheus/morpheus-ui/repo`` path will be automatically deleted in a future release but can be manually recursivly deleted at any time for storage recursively.
            - Java Updated to 8u302-b08
            - Tomcat verison update to v9.0.50
            
:Agent Packages: - Java Updated to 8u302-b08
                 - |morphues| Node and VM Node Packages version update to 3.2.1

