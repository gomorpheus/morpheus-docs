.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade version: |minUpgradeVer|

.. NOTE:: Items appended with :superscript:`x.x.x` are also included in that version

.. warning:: Rolling upgrades to |morphver| are not supported and will result in rabbitmq message serialization errors. If one node is upgraded in an HA env prior to the others, existing messages will not be able to be processed by the upgrades node(s).

Release Dates

- |morphver| |releasedate|

New Features
============

:Nutanix Prism Central: - Calls to the NPC API which are returned with a 409 error "Edit conflict: please retry change." are now retried before reporting as failed in |morpheus| :superscript:`7.0.3`
                  - Options for "UEFI," "SECURE BOOT," "WINDOWS DEFENDER CREDENTIAL GUARD," and "ATTACH VTPM," have been moved from the provisioning wizard to the Virtual Image configuration :superscript:`7.0.3`
:Proxies: - When appliances report telemetry data back to |morpheus| Hub, any configured global proxies are now honored :superscript:`7.0.3`
:Security: - Upgraded Apache Guacamole to 1.5.2 to mitigate CVE-2023-30575 :superscript:`7.0.3`
            - Upgraded ``bcprov-jdk18`` to 1.78 to mitigate CVE-2024-30171 :superscript:`7.0.3`
            - Upgraded ``commons-compress`` to 1.26.0 to mitigate CVE-2024-25710 :superscript:`7.0.3`
            - Upgraded ``h2database`` to 2.2.220 to mitigate CVE-2022-23221 :superscript:`7.0.3`
            - Upgraded ``ion-java`` to 1.10.5 to mitigate CVE-2024-21634 :superscript:`7.0.3`
            - Upgraded ``jsch`` to 0.2.15 to mitigate CVE-2023-48795 :superscript:`7.0.3`
            - Upgraded ``logback-classic`` to 1.2.13 to mitigate CVE-2023-6378 :superscript:`7.0.3`
            - Upgraded ``logback-core`` to version 1.2.13 to mitigate CVE-2023-48795 :superscript:`7.0.3`
            - Upgraded ``mysql-connector-j`` to 8.2.0 to mitigate CVE-2023-22102 :superscript:`7.0.3`
            - Upgraded ``org.apache.sshd`` to 2.12 to mitigate CVE-2023-48795 :superscript:`7.0.3`
            - Upgraded ``rabbitmq-java-client`` to 5.18.0 to mitigate CVE-2023-46120 :superscript:`7.0.3`
            - Upgraded ``spring security core`` to 5.7.12 to mitigate CVE-2024-22257 :superscript:`7.0.3`
            - Upgraded ``spring-amqp`` to 2.4.17 to mitigate CVE-2023-34050 :superscript:`7.0.3`
            - Upgraded ``spring-web`` to 5.3.34 to mitigate CVE-2024-22259 and CVE-2024-22262 :superscript:`7.0.3`
            - Upgraded ``xmlunit-core`` to 2.10.0 to mitigate CVE-2024-31573 :superscript:`7.0.3`
:Zerto: - Added support for Zerto version 10 :superscript:`7.0.3`


Fixes
=====

:API & CLI: - Fixed update requests to the ``storage-bucket`` API failing due to a ``providerType`` property not being passed. This property should not be a requirement :superscript:`7.0.3`
             - Input values configured to not be "EDITABLE" are no longer updated via API request despite returning the correct 400 response :superscript:`7.0.3`
             - The API endpoint for uploading Packages to |morpheus| now works properly :superscript:`7.0.3`
             - When listing Roles via |morpheus| API and filtering to include only Tenant Roles, the response will no longer include the built-in System Admin Role which is not selectable as a Tenant Role :superscript:`7.0.3`
:Ansible Tower: - Fixed Ansible Tower Jobs marked as failed in |morpheus| UI despite showing as successful in Tower :superscript:`7.0.3`
                 - Fixed Ansible Tower Tasks failing as part of Provisioning Workflows associated with Terraform-type Layouts :superscript:`7.0.3`
:Azure: - Fixed an issue where servers in multi-node Azure Instances were not deleted (from |morpheus| or Azure) following successful Teardown-phase Tasks :superscript:`7.0.3`
:Clouds: - When Clouds are added in the |mastertenant| and privately assigned to another Tenant, the Cloud detail page from the |mastertenant| now correctly shows total usage (including that of the other Tenant) :superscript:`7.0.3`
:Clusters: - ``NetworkConfig`` data is now available in cloud-init metadata (``/run/cloud-init/instance-data.json``) when provisioning a cluster with a static IP address :superscript:`7.0.3`
:Forms: - Fixed an issue where using Visibility configurations with Disk fields could cause provisioning failure :superscript:`7.0.3`
         - When Catalog Items are configured from Instance Types whose images have multiple disks, the Disks Input on Forms now properly shows multiple disks to configure :superscript:`7.0.3`
:Import/Export: - Fixed Workflow-type Catalog Items not importing successfully into new environments :superscript:`7.0.3`
:Instances: - Fixed an issue where VMs converted to managed Instances updated with custom options would lose those option values following the next Cloud sync :superscript:`7.0.3`
             - Fixed issues converting brownfield VMs to managed Instances when Tag Enforcement Policies with strict enforcement were active :superscript:`7.0.3`
:NSX: - Fixed specific scenarios where networks were not listing properly on the reconfigure modal for Instances :superscript:`7.0.3`
       - For NSX segment creation, a Gateway CIDR configuration is now only required when a Connected Gateway is set :superscript:`7.0.3`
:Network IP Pools: - Host records can no longer be created with duplicate IP addresses when both the compressed and uncompressed form of the address are used :superscript:`7.0.3`
:Plans and Pricing: - Pricing now works correctly when Price Sets are scoped to Resource Pools :superscript:`7.0.3`
:Plugins: - Fixed issues that could arise when deleting Instances which were provisioned using an IP Pool plugin :superscript:`7.0.3`
           - Fixed the "Editable" and "Removable" flags not being present for storage volumes created by plugin :superscript:`7.0.3`
:Policies: - When power schedule policies are configured to allow the schedule to be user editable, the schedule will no longer be reset to the policy value when other edits are made to the Instance :superscript:`7.0.3`
:Security Scans: - Security packages are now properly unzipped and made usable when security packages for SCAP scans are hosted in |morpheus| Archives :superscript:`7.0.3`
:Security: - Fixed a path traversal vulnerability related to Shell Script-type Tasks :superscript:`7.0.3`
            - Fixed an HTML injection vulnerability related to Catalog Item creation :superscript:`7.0.3`
            - Fixed csrf tokens being passed in via the query parameter on execution of a search within various pages :superscript:`7.0.3`
            - Set 644 permissions on the ``morpheus.asc`` file in Agent install for upgraded security :superscript:`7.0.3`
:Terraform: - Fixed Apply State failures on Terraform Apps under specific configurations :superscript:`7.0.3`
:User Settings: - Fixed an issue that would cause a 500 error to be thrown when saving new User Settings failed validation. In those scenarios, a UI warning is now displayed instead :superscript:`7.0.3`
:VMware: - Added an optimization to the reconfigure logic for workloads on VMware Clouds. If a server is resized to change network interface details, any reserved IP address is only released to the IP pool if a new network is selected for the interface
:XaaS: - Tasks can now be run on-demand from the Instance detail page for XaaS Instances. Previously, this did not work and they needed to be run from the Tasks UI instead :superscript:`7.0.3`
:Zerto: - Fixed an issue that prevented adding VMs to an existing replication group :superscript:`7.0.3`
         - Fixed an issue with deleting existing Zerto replication groups :superscript:`7.0.3`
         - Fixed an issue with re-saving Zerto replication groups that were already existing. Additionally added UI support for surfacing any validation errors to the user :superscript:`7.0.3`
         - Synced replication groups (those not created in |morpheus|) are no longer missing key config information in |morpheus| UI :superscript:`7.0.3`


Appliance & Agent Updates
=========================

:Appliance: - Java updated to v11.0.23 :superscript:`7.0.3`
:Agent Packages:  - |morpheus| Linux Agent updated to v2.6.2
                  - Node and VM Node Packages Java updated to v11.0.23 :superscript:`7.0.3`
                  - Node and VM Node Packages updated to v3.2.24 :superscript:`7.0.3`
