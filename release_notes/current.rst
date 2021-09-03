.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. WARNING:: OpenStack v2 Identity API has been removed in v5.3.3

.. NOTE:: Items appended with :superscript:`5.2.9` are also included in that version

.. include:: highlights.rst

New Features
============

:Azure: - Select Availability Zones during Instance, App, and Cluster provisioning. Select "Availability Zone" from the "Availability Options" menu and then specify the appropriate Availability Zone from the additional field that appears in the wizard

:Clusters: - Added "Install Docker" checkbox to the Add Hosts wizard. When checked, Docker is installed and when left unchecked, |morpheus| assumes Docker is already installed or will be installed via Workflows or some other means
           - Added "Install Docker" checkbox to the Add Cluster Layout modal. When checked, Docker is installed and when left unchecked, |morpheus| assumes Docker is already installed or will be installed via Workflows or some other means

:Google: - Added sync for Service Accounts and the ability to select a service account when provisioning Instances, Blueprints and Apps, Clusters and Hosts to Google Clouds. Once the Resource Pool is selected, the available service accounts are synced and the dropdown menu to select them appears
         - When provisioning to the default service account for the selected resource pool, an additional Access Scope option is presented. Users can opt to allow default access or to allow full access to all cloud APIs

:Hosts: - Deleting a Host or VM (Infrastructure > Hosts) with “Remove Associated Instances” marked and “Remove Infrastructure” unmarked is now handled differently. Host records and A records are no longer removed and teardown-phase Tasks are not run. If the Cloud is configured to inventory existing resources, the host or VM will be synced back in as a unmanaged resource on the next cloud sync :superscript:`5.2.9`

:Huawei Cloud: - EIP billing mode changed to bill by traffic rather than bandwidth. Note that this change does not affect OTC Clouds which only bill by traffic :superscript:`5.2.9`

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

:Terraform: - Added UI feedback and status indication when refreshing Terraform Instance state (:guilabel:`REFRESH STATE` button or "Refresh State" selection from Instance Actions menu)

:UI: - Added more detailed help block text for the Private Key field when storing a new key pair in Morpheus (Infrastructure > Keys & Certs > Key Pairs) :superscript:`5.2.9`
     - Help text added to Add Integration modals warning that HTTP URLs are insecure and not recommended

:VDI: - VDI pools can now be configured to be "Recyclable". When enabled, the VDI Instance will revert back to a snapshot and become available once again after the user has logged out and the VDI session has expired. This behavior will not apply to VDI pools which are also configured to be persistent because in that configuration the Instance is merely stopped and saved for the user's next session. This feature is currently only available for Cloud types which support snapshot management (VMware, Nutanix, and vCD)
      - Improved image streaming in low bandwidth situations

:vCD: - System administrator account credentials can now be provided to authenticate vCD Cloud integrations in |morpheus|. Previously, only organization administrator credentials could be used. Keep in mind that you will need to set the system administrator account credentials appropriately, for example, to be able to see entities created by the organization administrator
      - Added the option to specify a catalog to store |morpheus|-provisioned artifacts, previously |morpheus| would always create and use a "morpheus_auto" catalog

:VMware vCenter: - The UUID for hypervisor hosts synced into vCenter Clouds is now stored to the ``unique_id`` field on hypervisor host ``compute_server`` records :superscript:`5.2.9`
                 - Improved sync performance for VMware Resource Pools and Folders :superscript:`5.2.9`
                 - Added support for VMware Content Library. |morpheus| automatically on-boards items from your content library and re-syncs them regularly to keep them up to date. Add images from the |morpheus| library to Node Types for use in Layouts and Instance Types

Fixes
=====

:Terraform: - Fixed an issue where Terraform App and Instance wizard :guilabel:`NEXT` buttons would not deactivate once clicked, allowing multiple submissions for validation. In some scenarios, this could cause the |morpheus| app node to run out of memory

:VMware: - Volumes now update properly when changing Image selection when provisioning the VMWARE Instance Type :superscript:`5.2.9`

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

:Appliance: - Tomcat verison update to v9.0.50 :superscript:`5.2.9`
            - Java Updated to 8u302-b08 :superscript:`5.2.9`

:Agent Packages: - Java Updated to 8u302-b08 :superscript:`5.2.9`
