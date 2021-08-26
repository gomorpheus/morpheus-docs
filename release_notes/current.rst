.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. WARNING:: OpenStack v2 Identity API has been removed in v5.3.3

.. NOTE:: Items appended with :superscript:`5.2.x` are also included in that version

include:: highlights.rst

New Features
============

:Hosts: - Deleting a Host or VM (Infrastructure > Hosts) with “Remove Associated Instances” marked and “Remove Infrastructure” unmarked is now handled differently. Host records and A records are no longer removed and teardown-phase Tasks are not run. If the Cloud is configured to inventory existing resources, the host or VM will be synced back in as a unmanaged resource on the next cloud sync

:Huawei Cloud: - EIP billing mode changed to bill by traffic rather than bandwidth. Note that this change does not affect OTC Clouds which only bill by traffic

:Library: - Added Ubuntu 20 Layouts for nearly all supported Clouds
          - Added Debian 9 and 10 Layouts for VMware Clouds to the standard Morpheus Library
          - Disabled several deprecated System Instance Types and associated Layouts that are no longer maintained: **Cassandra, Confluence, Devstack, Hadoop, Jboss, Jenkins, Magento, Mongo, Moogsoft, Nexus, Percona, Puppet, RethinkDb, Riak, RiakCs, Stash, Solr, Wordpress, and Zookeeper**. NOTE: this only disables the Instance type from the system seeded library and does not affect user created Insatnce Types or Layouts.

:Network: - Added a Display Name field for networks, this value appears as the network name on the network display page (Infrastructure > Network). For synced networks, the name and display name will initially be identical but users can edit the display name if it makes sense to present a friendlier name to users
          - Added ability to change network during an Instance reconfigure (Select Reconfigure from the Instance Actions menu) for Instances in VMware and OpenStack Clouds. In other Clouds, network is still a read-only field during Instance reconfigure

:UI: - Added more detailed help block text for the Private Key field when storing a new key pair in Morpheus (Infrastructure > Keys & Certs > Key Pairs)

:VMware vCenter: - The UUID for hypervisor hosts synced into vCenter Clouds is now stored to the ``unique_id`` field on hypervisor host ``compute_server`` records
                 - Improved sync performance for VMware Resource Pools and Folders

Fixes
=====

:VMware: - Volumes now update properly when changing Image selection when provisioning the VMWARE Instance Type

|morpheus| API & CLI Improvements
=================================

:Instances: - Calls to the ``instances`` API to GET a specific Instance (at multiple levels including Instance, container details, and server) now include the ``uuid`` property

:NSX-T: - Create, manage, and delete NSX-T segments
        - Manage Group visibility for NSX-T segments
        - Create, manage, and delete Tier 0 and Tier 1 routers
        - Attach and detach Tier 1 routers to Tier 0 routers
        - Retrieve any NSX-T objects which are associated with Tier 0 or Tier 1 routers
        - Create, manage, and delete DNAT and SNAT rules

:Reports: - Fix for display of utilization statistics in some Cloud Usage Reports

Appliance & Agent Updates
=========================

:Appliance: - Tomcat verison update to v9.0.50
            - Java Updated to 8u302-b08

:Agent Packages: - Java Updated to 8u302-b08
