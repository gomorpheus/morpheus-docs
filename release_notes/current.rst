.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade version: |minUpgradeVer|

.. NOTE:: Items appended with :superscript:`6.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

MVM Virtualization Solution Open Beta
=====================================

MVM is a hypervisor clustering technology utilizing KVM and is now available to all customers through an open beta. MVM has been in closed beta in recent months but is now available to all customers for testing purposes. During the open beta period, customers will be able to provision one MVM cluster with up to three hypervisor hosts. See the `MVM guide <https://docs.morpheusdata.com/en/latest/infrastructure/clusters/clusters.html#mvm-clusters>`_ for complete details on standing up your own cluster. MVM is currently available for testing purposes only, it is **NOT** for production workloads.

.. image:: /images/infrastructure/clusters/mvm/mvmDetail.png


New Features
============

:Catalog: - When configuring Catalog Items to "Allow Quantity," the user may now specify a max quantity to place limits on orders
:Kubernetes: - Added Kubernetes 1.28 and 1.29 for EKS clusters. Versions 1.25 and 1.26 have been disabled
              - Fixed an issue related to HA MKS clusters failing to connect to additional masters following the loss of the first master
:NSX Cloud: - Added NSX Cloud network integrations for association with VMware Clouds or VMware on AWS Clouds
:Nutanix Prism Central: - Calls to the NPC API which are returned with a 409 error "Edit conflict: please retry change." are now retried before reporting as failed in |morpheus| :superscript:`6.2.11`
                  - Options for "UEFI," "SECURE BOOT," "WINDOWS DEFENDER CREDENTIAL GUARD," and "ATTACH VTPM," have been moved from the provisioning wizard to the Virtual Image configuration :superscript:`6.2.11``
:Proxies: - When appliances report telemetry data back to |morpheus| Hub, any configured global proxies are now honored :superscript:`6.2.11`
:Security: - Upgrade Apache Guacamole to 1.5.2 to mitigate CVE-2023-30575 :superscript:`6.2.11``
            - Upgrade ``bcprov-jdk18`` to 1.78 to mitigate CVE-2024-30171 :superscript:`6.2.11`
            - Upgrade ``commons-compress`` to 1.26.0 to mitigate CVE-2024-25710 :superscript:`6.2.11`
            - Upgrade ``h2database`` to 2.2.220 to mitigate CVE-2022-23221 :superscript:`6.2.11`
            - Upgrade ``ion-java`` to 1.10.5 to mitigate CVE-2024-21634 :superscript:`6.2.11``
            - Upgrade ``jsch`` to 0.2.15 to mitigate CVE-2023-48795 :superscript:`6.2.11``
            - Upgrade ``logback-classic`` to 1.2.13 to mitigate CVE-2023-6378 :superscript:`6.2.11`
            - Upgrade ``logback-core`` to version 1.2.13 to mitigate CVE-2023-48795 :superscript:`6.2.11``
            - Upgrade ``mysql-connector-j`` to 8.2.0 to mitigate CVE-2023-22102 :superscript:`6.2.11``
            - Upgrade ``org.apache.sshd`` to 2.12 to mitigate CVE-2023-48795 :superscript:`6.2.11``
            - Upgrade ``rabbitmq-java-client`` to 5.18.0 to mitigate CVE-2023-46120 :superscript:`6.2.11`
            - Upgrade ``spring security core`` to 5.7.12 to mitigate CVE-2024-22257 :superscript:`6.2.11`
            - Upgrade ``spring-amqp`` to 2.4.17 to mitigate CVE-2023-34050 :superscript:`6.2.11`
            - Upgrade ``spring-web`` to 5.3.34 to mitigate CVE-2024-22259 and CVE-2024-22262 :superscript:`6.2.11``
            - Upgrade ``xmlunit-core`` to 2.10.0 to mitigate CVE-2024-31573 :superscript:`6.2.11`
:Zerto: - Added support for Zerto version 10 :superscript:`6.2.11`


Fixes
=====

:API & CLI: - Fixed update requests to the ``storage-bucket`` API failing due to a ``providerType`` property not being passed. This property should not be a requirement :superscript:`6.2.11`
             - Input values configured to not be "EDITABLE" are no longer updated via API request despite returning the correct 400 response :superscript:`6.2.11`
             - The API endpoint for uploading Packages to |morpheus| now works properly :superscript:`6.2.11`
             - When listing Roles via |morpheus| API and filtering to include only Tenant Roles, the response will no longer include the built-in System Admin Role which is not selectable as a Tenant Role :superscript:`6.2.11`
:Ansible Tower: - Fixed Ansible Tower Jobs marked as failed in |morpheus| UI despite showing as successful in Tower :superscript:`6.2.11`
                 - Fixed Ansible Tower Tasks failing as part of Provisioning Workflows associated with Terraform-type Layouts :superscript:`6.2.11`
:Azure: - Fixed an issue where servers in multi-node Azure Instances were not deleted (from |morpheus| or Azure) following successful Teardown-phase Tasks :superscript:`6.2.11`
:Clouds: - When Clouds are added in the |mastertenant| and privately assigned to another Tenant, the Cloud detail page from the |mastertenant| now correctly shows total usage (including that of the other Tenant) :superscript:`6.2.11`
:Clusters: - ``NetworkConfig`` data is now available in cloud-init metadata (``/run/cloud-init/instance-data.json``) when provisioning a cluster with a static IP address :superscript:`6.2.11`
:Email Notifications: - Fixed old password warning emails not going out as configured
:Forms: - Default values for hidden Inputs on Forms are now passed properly to the Instance config
         - Fixed an issue where using Visibility configurations with Disk fields could cause provisioning failure :superscript:`6.2.11`
         - Fixed disk sizes updating inconsistently on Form disk Inputs when different Plans were toggled which should have resulted in default disk size changes
         - When Catalog Items are configured from Instance Types whose images have multiple disks, the Disks Input on Forms now properly shows multiple disks to configure :superscript:`6.2.11`
:Import/Export: - Fixed Workflow-type Catalog Items not importing successfully into new environments :superscript:`6.2.11``
:Instances: - Fixed an issue where VMs converted to managed Instances updated with custom options would lose those option values following the next Cloud sync :superscript:`6.2.11`
             - Fixed issues converting brownfield VMs to managed Instances when Tag Enforcement Policies with strict enforcement were active :superscript:`6.2.11`
:Kubernetes: - Fixed an issue where added Kubernetes workers to existing clusters would be on a different Kubernetes point release
:NSX: - Fixed specific scenarios where networks were not listing properly on the reconfigure modal for Instances :superscript:`6.2.11`
       - For NSX segment creation, a Gateway CIDR configuration is now only required when a Connected Gateway is set :superscript:`6.2.11``
:Network IP Pools: - Host records can no longer be created with duplicate IP addresses when both the compressed and uncompressed form of the address are used :superscript:`6.2.11`
:Packages: - Fixed Packages not uploading when items had associated Labels
            - Values associated with a ``description`` key in ``package-manifest.json`` files is now stored in the database and shown in the UI as a description value
            - When uploading an updated package containing a higher version number, the increased version number is now shown in the UI
:Plans and Pricing: - Pricing now works correctly when Price Sets are scoped to Resource Pools :superscript:`6.2.11`
:Plugins: - Fixed issues that could arise when deleting Instances which were provisioned using an IP Pool plugin :superscript:`6.2.11`
           - Fixed the "Editable" and "Removable" flags not being present for storage volumes created by plugin :superscript:`6.2.11`
           - Proxy support added for plugins. Traffic generated by plugins integrated with the |morpheus| appliance is now routed through any configured global proxy
:Policies: - When power schedule policies are configured to allow the schedule to be user editable, the schedule will no longer be reset to the policy value when other edits are made to the Instance :superscript:`6.2.11`
:Security Scans: - Security packages are now properly unzipped and made usable when security packages for SCAP scans are hosted in |morpheus| Archives :superscript:`6.2.11``
:Security: - Fixed a path traversal vulnerability related to Shell Script-type Tasks :superscript:`6.2.11`
            - Fixed an HTML injection vulnerability related to Catalog Item creation :superscript:`6.2.11`
            - Fixed csrf tokens being passed in via the query parameter on execution of a search within various pages :superscript:`6.2.11`
            - Set 644 permissions on the ``morpheus.asc`` file in Agent install for upgraded security :superscript:`6.2.11`
:Terraform: - Fixed Apply State failures on Terraform Apps under specific configurations :superscript:`6.2.11`
:Trust: - OAuth 2.0 credentials can now be stored properly on newly installed environments. This issue did not affect older environments which were upgraded to recent versions, only appliances which were newly installed with recent versions
:User Settings: - Fixed an issue that would cause a 500 error to be thrown when saving new User Settings failed validation. In those scenarios, a UI warning is now displayed instead :superscript:`6.2.11`
                 - Fixed cases where email notifications for updated user settings would state the password was updated successfully even when account information other than the password was updated
:XaaS: - Tasks can now be run on-demand from the Instance detail page for XaaS Instances. Previously, this did not work and they needed to be run from the Tasks UI instead :superscript:`6.2.11`
:Zerto: - Fixed an issue that prevented adding VMs to an existing replication group :superscript:`6.2.11`
         - Fixed an issue with deleting existing Zerto replication groups :superscript:`6.2.11`
         - Fixed an issue with re-saving Zerto replication groups that were already existing. Additionally added UI support for surfacing any validation errors to the user :superscript:`6.2.11`
         - Synced replication groups (those not created in |morpheus|) are no longer missing key config information in |morpheus| UI :superscript:`6.2.11`


Appliance & Agent Updates
=========================

:Appliance: - Java updated to v11.0.23 :superscript:`6.2.11`
:Agent Packages:  - |morpheus| Linux Agent updated to v2.6.2
                  - Node and VM Node Packages Java updated to v11.0.23 :superscript:`6.2.11`
                  - Node and VM Node Packages updated to v3.2.24 :superscript:`6.2.11`
