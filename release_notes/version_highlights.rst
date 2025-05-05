**************************************
|morpheus| |morphAnnualVer| Highlights
**************************************

This section includes feature change highlights and key enhancements for all releases within |morpheus| version 6. Many other features changes and enhancements were added to each of these versions and the release notes page for each individual version can be reviewed for complete details.

7.0.4
=====

:API & CLI: - The Group attribute for Network Pools can now be updated via |morpheus| API and CLI. This functionality is also added to |morpheus| UI in this release
:Catalog: - Catalog item names now truncate after wrapping to a second line rather than at the end of the first line which often cut off too much of longer names
:Docker: - When running a non-Kubernetes Docker image with image tag set to latest, we now force-pull the image to update the Docker host
:Kubernetes: - Added default Kubernetes MKS 1.30 Layouts for all supported Clouds
:Library: - Added or updated Oracle Linux 6, 7, 8 and 9 images for various Cloud types to the default catalog
           - Default Ubuntu 24.04 images have been added for VMware, Azure, AWS, and HVM/KVM Clouds
:Load Balancers: - |morpheus| IP Pools can now be used to auto-assign an IP address for the VIP address field when creating a load balancer Instance
:NSX: - NSX and NSX Cloud now support a configured global proxy
:Network: - Network Domains can now be scoped to a specific Group. Additionally, the "Network: Domains" Role permission now has a Group access level which limits Domain visibility only to those scoped to accessible Groups
           - Network Pools can now be scoped to a specific Group. Additionally, the "Network: IP Pools" Role permission now has a Group access level which limits Network Pool visibility only to those scoped to accessible Groups
:Nutanix Prism Central: - Improved handling of unmanaged VLAN networks. Managed and unmanaged VLANs are no longer synced as the same network type
:Nutanix Prism Element: - References to "Nutanix Prism" integration have been updated to "Nutanix Prism Element" to differentiate from "Nutanix Prism Central"
:vCloud Director: - vCD Clouds can now be authenticated through API tokens in addition to username/password authentication
                  - vCD Clouds will now sync in Plans created in vCD, allow users to select these plans at provision time, and allow access to reconfigure and costing features when custom plans are utilized

7.0.3
=====

:Catalog: - When configuring Catalog Items to "Allow Quantity," the user may now specify a max quantity to place limits on orders
:Kubernetes: - Added Kubernetes 1.28 and 1.29 for EKS clusters. Versions 1.25 and 1.26 have been disabled
              - Fixed an issue related to HA MKS clusters failing to connect to additional masters following the loss of the first master
:NSX: - Deprecates support for NSX v2. General support for NSX v2 ended in 9/2021 and technical guidance ended in 9/2022. Support for integration with |morpheus| will end with the next release (7.0.4)
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

7.0.2
=====

:Administration: - Improved CEF audit logging for situations when a user is being impersonated :superscript:`6.2.10`
:Amazon: - Added support for new reserved keywords in RDS MySQL 3.06.0 :superscript:`6.2.10`
:Budgets: - Budgets now include the option to choose from one of two data forecasting models to estimate out the budget through the end of its configured term
:Clouds: - Added more granular controls around automatic Cloud inventory. Depending on Cloud feature capability, set the default active or inactive state for Plans, Networks, Security Groups, Datastores, Folders, and more
          - Users must now type "DELETE" into a text field to confirm they wish to delete a Cloud which is a safeguard already available on other resources in Morpheus :superscript:`6.2.10`
:Email Notifications: - Added "Email Templates" tab to the global settings section (|AdmSet|). Create new templates to replace the system default templates for notifications such as Instance provisioning completion, password reset, policy warnings, and much more
:Jobs: - Jobs can now be configured to only run on workloads with an on or an off power state (or keep the default behavior of running with any power state)
:License: - Updated wording on the license application page (|AdmSetLic|) to reflect updated licensing policies :superscript:`6.2.10`
:MicrosoftDNS: - Major improvements added to the MicrosoftDNS plugin. See updated MSDNS integration documentation for further details :superscript:`6.2.10`
:Nutanix Prism Central: - Added a "Windows Defender Credential Guard" checkbox when "Secure Boot" is also checked which mirrors functionality available in NPC :superscript:`6.2.10`
                  - Added support for Nutanix Prism Central Projects. Clouds can be scoped to a specific project or Instances can be provisioned to specific projects :superscript:`6.2.10`
:Oracle Cloud: - Added ``mx-queretaro-1`` region support for Oracle Clouds :superscript:`6.2.10`
:Personas: - Added a new API Persona. This allows service accounts to be configured for API use which have no |morpheus| UI access
:Reports: - For scheduled reports, added a link to include a comma-separated list of email addresses which should be notified each time the report is run
           - Removed the Invoice Details report :superscript:`6.2.10`
           - Updated the Time Series Cost report with improved Group filtering and sort ordering
:Security: - Embedded Apache Tomcat upgraded to 9.0.88 to mitigate CVE-2024-23672 :superscript:`6.2.10`
:Tasks: - For Powershell Tasks, added a Powershell version configuration to run the Task in a specified version of Powershell. The selected version must be installed on the targer for this to function correctly
:Tenants: - The impersonate option for a user with "Password Expired" checked, is no longer active. Previously when click the user would be directed back to the Dashboard page of the |mastertenant| which was confusing :superscript:`6.2.10`
:VMware: - Added SR-IOV network adapter support
:Virtual Images: - In the Locations section of a Virtual Image detail page, the "CLOUD" column has been relabeled to "REFERENCE" as the source can be a Cluster or a Cloud
                  - Virtual Image types are no longer a static list but can be dynamically added to an appliance based on integrated Cloud types


7.0.1
=====

:Clusters: - Added SSH validation to the Add Clusters Wizard. When entering host IP addresses, |morpheus| will validate that it has SSH access to that IP address
            - Removed option to provision KVM and KVM/Docker cluster types. KVM is still supported through onboarding pre-configured brownfield hosts and consuming them as provisioning targets
:DigitalOcean: - Added support for scoping DigitalOcean Clouds to specific VPCs as well as support for discovering existing Droplets and onboarding them as discovered servers
:Identity Sources: - Added an optional configuration to Active Directory Identity Sources which allows users to log in with a UPN credential for subdomain access rather than just a username :superscript:`6.2.9`

7.0.0
=====

:API & CLI: - Added API support for optionally specifying a stack name when provisioning from CloudFormation templates :superscript:`6.2.8`
             - Added API support for specifying an S3 bucket to read CloudFormation templates from during provisioning. This is necessary when provisioning from CF templates greater than 50 KB :superscript:`6.2.8`
:CloudFormation: - Provisioning from CloudFormation templates now includes a "STACK NAME" configuration. By default, this will be the same as the Instance or App name but can be overridden :superscript:`6.2.8`
                  - When provisioning from CloudFormation Spec Templates, added a configuration to specify an S3 bucket to read the Spec Template from. This is required for CF templates greater than 50 KB :superscript:`6.2.8`
:Dashboard: - Added support for Spanish-language localizations for |morpheus| Dashboard :superscript:`6.2.8`
:Identity Sources: - "Post RelayState" field added for For SAML SSO Identity Sources using "Post Binding Mode" for defining RelayState post parameter. :superscript:`6.2.8`
:Import/Export: - Forms can now be used with the import/export feature. Export Forms as code into an integrated Git repository and import them back into any other appliance with the same repository integrated
:Kubernetes: - System Kubernetes 1.29 Layouts added :superscript:`6.2.8`
:Policies: - The Roles and Policies list pages have been updated to give the user control over visible output columns and page size
:Roles: - Added a Cluster Types tab to the Role detail page to control the Cluster types available to the Role
:Security: - Upgraded ``spring-web`` to version 5.3.32 to mitigate CVE-2024-22243 :superscript:`6.2.8`
:Terraform: - For licensing reasons, automated Terraform installs handled by |morpheus| are now capped at version 1.5.5. Other versions may be utilized in |morpheus| through manual installation :superscript:`6.2.8`
:VMware: - When Snapshot names are changed in VMware, the name change is now reflected in |morpheus| following the next Cloud sync :superscript:`6.2.8`


6.3.3
=====

:API & CLI: - Removed API calls and CLI commands related to |morpheus| Dashboard as that is no longer a standardized page and may be replaced by a Dashboard Plugin in some appliances :superscript:`6.2.6`
:Ansible Tower: - Added more descriptive error messages for failed Ansible Tower Tasks, particularly when the Task fails due to being pointed at an incorrect Inventory to make it clearer to the user what has failed :superscript:`6.2.6`
:Apps: - Removed the Tier subtab within the Instances tab of the App detail page :superscript:`6.2.6`
:Plugins: - Nutanix Prism Central plugin leaves beta and enters general availability. See share.morpheusdata.com for more information and release notes specific to this plugin :superscript:`6.2.6`
:Security: - Upgraded ``gradle.properties`` to 9.0.83 to mitigate multiple CVEs :superscript:`6.0.11 6.2.6`
            - Upgraded ``netty`` to version 4.1.100.final to mitigate CVE-2023-44487 and CVE-2023-41881 :superscript:`6.0.11 6.2.6`
            - Upgraded ``spring-boot-actuator-autoconfigure`` to 2.7.11 to mitigate CVE-2023-20873 :superscript:`6.0.11 6.2.6`
            - Upgraded ``spring-boot-autoconfigure`` to 2.7.12 to mitigate CVE-2023-20883 :superscript:`6.0.11 6.2.6`
            - Upgraded ``spring-boot`` to version 2.7.18 to mitigate CVE-2023-34055 :superscript:`6.0.11 6.2.6`
            - Upgraded ``spring-expression`` to version 5.3.17 to mitigate CVE-2022-22950 :superscript:`6.0.11 6.2.6`
            - Upgraded ``spring-expression`` to version 5.3.27 to mitigate CVE-2023-20863 and CVE-2023-20861 :superscript:`6.0.11 6.2.6`
            - Upgraded ``spring-security-web`` to 5.7.8 to mitigate CVE-2023-20862 :superscript:`6.0.11 6.2.6`
            - Upgraded ``spring-webmvc`` to version 5.3.30 to mitigate CVE-2023-20860 :superscript:`6.0.11 6.2.6`
            - Upgraded ``jknack``


6.3.2
=====

:API & CLI: - Added the ability to configure ServiceNow integrations to use table-based CMDB mode rather than the newer IRE via |morpheus| API and CLI. This configuration was added previously to |morpheus| UI :superscript:`6.0.10 6.2.5`
             - Added |morpheus| API and CLI support for Cluster Packages which was added to |morpheus| UI in a previous release
:Clouds: - Changing tabs on the Cloud detail page Containers tab no longer throws an error :superscript:`6.2.5`
:Dashboard: - Added localization to the upgraded dashboard (now a plugin) which was added to the product in 6.0.0 :superscript:`6.0.10 6.2.5`
:Distributed Worker: - When a |morpheus| Distributed Worker is installed and configured with the appliance, |morpheus| Agent communication now go back to the appliance via the Distributed Worker rather than directly to the |morpheus| appliance nodes.  Note: Set cloud appliance url to worker url for agent relay functionality.
:Hyper-V: - Added support for Hyper-V Gen 2 virtual machines :superscript:`6.0.10 6.2.5`
:Kubernetes: - Added Kubernetes sync and comms over Morpheus Agent command bus. Morpheus can now sync and communicate with Kubernetes hosts over the agent for scenerios where Morpheus cannot reach k8s directly. Morpheus Worker v6.3.2 also adds agent relay for k8s hosts that are unable to reach Morpheus appliances directly.
              - Attached Workflows will now apply to Kubernetes Cluster Layouts before the core components are built (kubeadm, kubectl, etc.) such that Workflows can be used to help facilitate installation and configuration of core components
              - The ``default-docker-secret`` value as stored in ``etcd`` for MKS Kubernetes 1.28+ clusters is now encrypted :superscript:`6.0.10 6.2.5`
:NSX-T: - |morpheus| can now authenticate with NSX-T 4.1 as a Project-level user allowing multiple |morpheus| appliances to be mapped to the same NSX server and allowing Project-scoped integrations to be created in |morpheus|
:Network: - Using the search function on the Domains list page now searches on the Domain Name and Description fields in addition to the Domain field that was searched previously :superscript:`6.0.10 6.2.5`
:OpenStack: - When provisioning an Instance, App, or Cluster to an all-Projects OpenStack Cloud, the Security Group dropdown options are being filtered properly to the selected Resource Pool :superscript:`6.0.10 6.2.5`
:Security: - Embedded ``curl`` upgraded to 8.4.0 to mitigate CVEs associated with the prior installed version :superscript:`6.2.5 6.0.10`
            - The first and last names columns on the Users database table are no longer encrypted. This is reverting a recent change that encrypted these values due to some unforeseen downstream issues this caused :superscript:`6.0.10 6.2.5`
            - Upgraded ``netty-all`` to 4.1.77.Final to mitigate CVE-2022-24823 :superscript:`6.0.10 6.2.5`



6.3.1
=====

:API & CLI: - Added the ability to create Catalog Items based on Forms through |morpheus| API and CLI :superscript:`6.2.4`
             - The Certificates API endpoint now validates the given integration ID and does not create the certificate if an integration with the given ID does not exist :superscript:`6.0.9 6.2.4`
             - ``refId`` and ``refType`` parameters are no longer ignored when |morpheus|-type IP Pool reservations are made over |morpheus| API :superscript:`6.0.9 6.2.4`
:Currency: - Added Malaysian Ringgit (MYR) currency support :superscript:`6.0.9 6.2.4`
            - Added support for Singapore Dollar (SGD) currency :superscript:`6.0.9 6.2.4`
:Forms: - Added various fixes and quality of life improvements for Forms feature :superscript:`6.2.4`
:Hyper-V: - Adding a Hyper-V cloud with a WinRM Port value of 5986 rather than the default of 5985 now works properly :superscript:`6.0.9 6.2.4`
:Kubernetes: - Single and HA layouts for Kubernetes version 1.28 clusters added for OpenStack and OpenTelekom Clouds :superscript:`6.0.9 6.2.4`
              - The ``nginx-ingress`` version 1.9.4 package is now being included with Kubernetes 1.26 through 1.28 cluster layouts for all supported operating systems :superscript:`6.0.9 6.2.4`
:NSX-T: - Official support added for NSX-T 4.1 :superscript:`6.0.9 6.2.4`
:Network: - Credential stores can now be used when creating or editing network integrations for NSX and Cisco ACI
:Security: - Bouncycastle upgraded to 1.76 to mitigate CVE-2023-33201 :superscript:`6.0.9 6.2.4`
            - Guava upgraded to 32.0.1 to mitigate CVE-2023-2976 :superscript:`6.0.9 6.2.4`
            - Upgraded cxf-rt-transports-http to 3.4.10 to mitigate CVE-2022-46363 :superscript:`6.0.9 6.2.4`
            - Upgraded to Eclipse.jgit to 6.6.1 to mitigate CVE-2023-4759 :superscript:`6.0.9 6.2.4`
:ServiceNow: - Added the ability to switch back to the older table-based API mode for CMDB sync :superscript:`6.0.9 6.2.4`
:vCloud Director: - Added MKS 1.28 HA layouts for vCD Clouds :superscript:`6.0.9 6.2.4`



6.3.0
=====

:Cluster Packages: - Added new UI area (|LibTemClu|) for creating Cluster Packages which can be associated with Cluster Layouts. See the appropriate areas of Morpheus Documentation for more on Cluster Packages and Cluster Layouts
:Currency: - Added support for Mongolian Tugrik (MNT) currency :superscript:`6.0.9 6.2.4`
:Image Builder: - Updated the Image Builder form into a single form rather than a paged wizard. See the Image Builder section of |morpheus| documentation for example scripts and help getting started
:Plugins: - The required Plugin API version is now |pluginVer|. Plugins developed for |morpheus| versions prior to 6.3.0 will need small changes. Please see https://support.morpheusdata.com/s/article/Making-plugins-compatible-with-Morpheus-6-3-0?language=en_US for more information.
:Roles: - Added the ability to specify (per Role) a landing page other than the Dashboard within |morpheus|. For example, a Role could be configured to log into the Instance list page
         - There is now a Feature Permission which determines whether a Role is able to use Task Cancel and Task Retry controls for executions. This also controls access to the Cancel and Retry controls on Tasks within Instance histories
         - There is now a Feature Permission which determines whether a Role may extend expiration or shutdown Policies on workloads. This permission can apply globally or only to workloads the user owns
:VMware: - Added support for versioned templates from VMware Content Library
          - Added the ability to set vApp Property values on VMware Node Types. See `Node Type docs <https://docs.morpheusdata.com/en/6.3.0/library/blueprints/blueprints.html?next=https%3A%2F%2Fdocs.morpheusdata.com%2Fen%2F6.3.0%2Flibrary%2Fblueprints%2Fb>`_ for more

6.2.11
======

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

6.2.10
======

:Administration: - Improved CEF audit logging for situations when a user is being impersonated :superscript:`7.0.2`
:Amazon: - Added support for new reserved keywords in RDS MySQL 3.06.0 :superscript:`7.0.2`
:Clouds: - Users must now type "DELETE" into a text field to confirm they wish to delete a Cloud which is a safeguard already available on other resources in Morpheus :superscript:`7.0.2`
:License: - Updated wording on the license application page (|AdmSetLic|) to reflect updated licensing policies :superscript:`7.0.2`
:MicrosoftDNS: - Major improvements added to the MicrosoftDNS plugin. See updated MSDNS integration documentation for further details :superscript:`7.0.2`
:Nutanix Prism Central: - Added a "Windows Defender Credential Guard" checkbox when "Secure Boot" is also checked which mirrors functionality available in NPC :superscript:`7.0.2`
                  - Added support for Nutanix Prism Central Projects. Clouds can be scoped to a specific project or Instances can be provisioned to specific projects :superscript:`7.0.2`
:Oracle Cloud: - Added ``mx-queretaro-1`` region support for Oracle Clouds :superscript:`7.0.2`
:Reports: - Removed the Invoice Details report :superscript:`7.0.2`
:Security: - Embedded Apache Tomcat upgraded to 9.0.88 to mitigate CVE-2024-23672 :superscript:`7.0.2`
            - Upgraded ``jose4j`` to 0.9.4 to mitigate CVE-2.23-51775
            - Upgraded ``netty-codec-http`` to 4.1.108.Final to mitigate CVE-2024-29025
:Tenants: - The impersonate option for a user with "Password Expired" checked, is no longer active. Previously when click the user would be directed back to the Dashboard page of the |mastertenant| which was confusing :superscript:`7.0.2`


6.2.9
=====

:Identity Sources: - Added an optional configuration to Active Directory Identity Sources which allows users to log in with a UPN credential for subdomain access rather than just a username :superscript:`7.0.1`

6.2.8
=====

:API & CLI: - Added API support for optionally specifying a stack name when provisioning from CloudFormation templates
             - Added API support for specifying an S3 bucket to read CloudFormation templates from during provisioning. This is necessary when provisioning from CF templates greater than 50 KB
:Agent: - Updated the Windows Agent to send fewer logs :superscript:`7.0.0`
:CloudFormation: - Provisioning from CloudFormation templates now includes a "STACK NAME" configuration. By default, this will be the same as the Instance or App name but can be overridden :superscript:`7.0.0`
                  - When provisioning from CloudFormation Spec Templates, added a configuration to specify an S3 bucket to read the Spec Template from. This is required for CF templates greater than 50 KB :superscript:`7.0.0`
:Dashboard: - Added support for Spanish-language localizations for |morpheus| Dashboard :superscript:`7.0.0`
:Identity Sources: - "Post RelayState" field added for For SAML SSO Identity Sources using "Post Binding Mode" for defining RelayState post parameter. :superscript:`7.0.0`
:Installer: - Added a FIPS-compliant |morpheus| installer for SLES 15 :superscript:`7.0.0`
:Kubernetes: - System Kubernetes 1.29 Layouts added :superscript:`7.0.0`
:Security: - Upgraded ``spring-web`` to version 5.3.32 to mitigate CVE-2024-22243
:Terraform: - For licensing reasons, automated Terraform installs handled by |morpheus| are now capped at version 1.5.5. Other versions may be utilized in |morpheus| through manual installation :superscript:`7.0.0`
:VMware: - When Snapshot names are changed in VMware, the name change is now reflected in |morpheus| following the next Cloud sync :superscript:`7.0.0`


6.2.7
=====

:Dashboard: - The Dashboard plugin has been updated to support German, French, and Italian localizations :superscript:`6.3.4`
:Inputs: - On the Instance detail page under the Runtime tab, the "Option Types" subtab has been relabeled "Inputs" :superscript:`6.3.4`
:Nutanix Prism Central: - Added Terraform support to Nutanix Prism Central plugin :superscript:`6.3.4`
:Security: - Embedded Tomcat upgraded to 9.0.83 to mitigate CVE-2023-46589 :superscript:`6.3.4`
:Veeam: - Added official support for Veeam 12 :superscript:`6.3.4`


6.2.6
=====

:API & CLI: - Removed API calls and CLI commands related to |morpheus| Dashboard as that is no longer a standardized page and may be replaced by a Dashboard Plugin in some appliances :superscript:`6.3.3`
:Ansible Tower: - Added more descriptive error messages for failed Ansible Tower Tasks, particularly when the Task fails due to being pointed at an incorrect Inventory to make it clearer to the user what has failed :superscript:`6.3.3`
:Apps: - Removed the Tier subtab within the Instances tab of the App detail page :superscript:`6.3.3`
:Plugins: - Nutanix Prism Central plugin leaves beta and enters general availability. See share.morpheusdata.com for more information and release notes specific to this plugin :superscript:`6.3.3`
:Security: - Upgraded ``gradle.properties`` to 9.0.83 to mitigate multiple CVEs :superscript:`6.0.11 6.3.3`
            - Upgraded ``netty`` to version 4.1.100.final to mitigate CVE-2023-44487 and CVE-2023-41881 :superscript:`6.0.11 6.3.3`
            - Upgraded ``spring-boot-actuator-autoconfigure`` to 2.7.11 to mitigate CVE-2023-20873 :superscript:`6.0.11 6.3.3`
            - Upgraded ``spring-boot-autoconfigure`` to 2.7.12 to mitigate CVE-2023-20883 :superscript:`6.0.11 6.3.3`
            - Upgraded ``spring-boot`` to version 2.7.18 to mitigate CVE-2023-34055 :superscript:`6.0.11 6.3.3`
            - Upgraded ``spring-expression`` to version 5.3.17 to mitigate CVE-2022-22950 :superscript:`6.0.11 6.3.3`
            - Upgraded ``spring-expression`` to version 5.3.27 to mitigate CVE-2023-20863 and CVE-2023-20861 :superscript:`6.3.3 6.0.11`
            - Upgraded ``spring-security-web`` to 5.7.8 to mitigate CVE-2023-20862 :superscript:`6.0.11 6.3.3`
            - Upgraded ``spring-webmvc`` to version 5.3.30 to mitigate CVE-2023-20860 :superscript:`6.0.11 6.3.3`
            - Upgraded ``jknack/handlebars.java`` to version 4.3.1 to mitigate CVE-2022-42889 :superscript:`6.0.11 6.3.3`

6.2.5
=====

:API & CLI: - Added the ability to configure ServiceNow integrations to use table-based CMDB mode rather than the newer IRE via |morpheus| API and CLI. This configuration was added previously to |morpheus| UI :superscript:`6.0.10 6.3.2`
:Clouds: - Changing tabs on the Cloud detail page Containers tab no longer throws an error :superscript:`6.3.2`
:Currency: - Added support for Botswanan Pula (BWP) currency :superscript:`6.0.10 6.3.1`
:Dashboard: - Added localization to the upgraded dashboard (now a plugin) which was added to the product in 6.0.0 :superscript:`6.0.10 6.3.2`
:Hyper-V: - Added support for Hyper-V Gen 2 virtual machines :superscript:`6.0.10 6.3.2`
:Kubernetes: - The ``default-docker-secret`` value as stored in ``etcd`` for MKS Kubernetes 1.28+ clusters is now encrypted :superscript:`6.0.10 6.3.2`
:Network: - Using the search function on the Domains list page now searches on the Domain Name and Description fields in addition to the Domain field that was searched previously :superscript:`6.0.10 6.3.2`
:OpenStack: - When provisioning an Instance, App, or Cluster to an all-Projects OpenStack Cloud, the Security Group dropdown options are being filtered properly to the selected Resource Pool :superscript:`6.0.10 6.3.2`
:Security: - Embedded ``curl`` upgraded to 8.4.0 to mitigate CVEs associated with the prior installed version :superscript:`6.3.2 6.0.10`
            - The first and last names columns on the Users database table are no longer encrypted. This is reverting a recent change that encrypted these values due to some unforeseen downstream issues this caused :superscript:`6.0.10 6.3.2`
            - Upgraded ``netty-all`` to 4.1.77.Final to mitigate CVE-2022-24823 :superscript:`6.0.10 6.3.2`


6.2.4
=====

:API & CLI: - Added the ability to create Catalog Items based on Forms through |morpheus| API and CLI :superscript:` 6.3.1`
             - The Certificates API endpoint now validates the given integration ID and does not create the certificate if an integration with the given ID does not exist :superscript:`6.0.9 6.3.1`
             - ``refId`` and ``refType`` parameters are no longer ignored when |morpheus|-type IP Pool reservations are made over |morpheus| API :superscript:`6.0.9 6.3.1`
:Currency: - Added Malaysian Ringgit (MYR) currency support :superscript:`6.0.9 6.3.1`
            - Added support for Mongolian Tugrik (MNT) currency :superscript:`6.0.9 6.3.0 `
            - Added support for Singapore Dollar (SGD) currency :superscript:`6.0.9 6.3.1`
:Forms: - Added various fixes and quality of life improvements for Forms feature :superscript:` 6.3.1`
:Hyper-V: - Adding a Hyper-V cloud with a WinRM Port value of 5986 rather than the default of 5985 now works properly :superscript:`6.0.9 6.3.1`
:Kubernetes: - Single and HA layouts for Kubernetes version 1.28 clusters added for OpenStack and OpenTelekom Clouds :superscript:`6.0.9 6.3.1`
              - The ``nginx-ingress`` version 1.9.4 package is now being included with Kubernetes 1.26 through 1.28 cluster layouts for all supported operating systems :superscript:`6.0.9 6.3.1`
:NSX-T: - Official support added for NSX-T 4.1 :superscript:`6.0.9 6.3.1`
:Security: - Bouncycastle upgraded to 1.76 to mitigate CVE-2023-33201 :superscript:`6.0.9 6.3.1`
            - Guava upgraded to 32.0.1 to mitigate CVE-2023-2976 :superscript:`6.0.9 6.3.1`
            - Upgraded cxf-rt-transports-http to 3.4.10 to mitigate CVE-2022-46363 :superscript:`6.0.9 6.3.1`
            - Upgraded to Eclipse.jgit to 6.6.1 to mitigate CVE-2023-4759 :superscript:`6.0.9 6.3.1`
:ServiceNow: - Added the ability to switch back to the older table-based API mode for CMDB sync :superscript:`6.0.9 6.3.1`
:vCloud Director: - Added MKS 1.28 HA layouts for vCD Clouds :superscript:`6.0.9 6.3.1`

6.2.3
=====

:API & CLI: - Added CRUD support for NSX-T network service integrations. Previously it was only possible to list the available network server details. See API documentation for further details :superscript:`6.0.8`
             - Added ``/instances/stats`` endpoint to return summary details related to Instances which may also be filtered to return stats on just specific groupings of Instance. Additional details are available in |morpheus| API documentation :superscript:`6.0.8`
:Identity Sources: - SAML SSO identity sources using HTTP-POST binding are now working as expected when integrated with |morpheus| Tenants :superscript:`6.0.8`
:Kubernetes: - Updated Calico image retrieval to pull from quay.io to avoid customers hitting Docker Hub image pull rate limits :superscript:`6.0.8 6.3.0`
              - Upgrade default Kubernetes Cluster Layouts to version 1.28 :superscript:`6.0.8 6.3.0`
:Plugins: - Improvements added to Task-type Plugins. See Developer Portal documentation for more details :superscript:`6.3.0`
:ServiceNow: - ServiceNow Catalog Items built using Forms can no longer be exposed to an integrated ServiceNow appliance. This is not yet supported but will be in the future :superscript:`6.3.0`

6.2.2
=====

:Catalog: - Added support for saving Catalog items without first passing a check for valid JSON in the config
:Inputs: - Added “REMOVE NO SELECTION” attribute for Select List-based Inputs. This defaults the Input to the first selection in the list rather than to an empty selection
:Layouts: - Added Display Order property for Layouts. Layouts are listed in high-to-low order based on the Display Order in the Layouts dropdown of the provisioning wizard

6.2.1
=====

:Forms: - Additional quality of life features added for Forms
:XaaS: - When Teardown-phase Tasks fail following an attempt to delete an XaaS Instance, the remaining Tasks are stopped which prevents the deletion from taking place. This allows users to correct the failing Tasks and ensure the object is deleted gracefully. Non-XaaS Instances already supported this.

6.2.0
=====

:Import/Export: - Configure code repositories (ex. integrated Github repositories) as import and export targets. Export |morpheus| items as code into repositories and import them into other |morpheus| appliances.
:Workflows: - When running Workflows on-demand against an Instance, users can now select a specific phase of Tasks to be run if a Provisioning Workflow is selected

6.1.2
=====

:Forms: - Added Text Array input type for Forms which allows the user to enter a list of values separated by a delimiter. Once entered, the values are parsed out and may be individually deleted prior to submitting the form
        - Added new ability to filter available Cloud types on Forms. Select a Cloud type from the LIMIT TO CLOUD TYPE dropdown or select FILTER FROM RESOURCE. The option to filter from resource reads the Cloud type from the Catalog Item Instance config

6.1.1
=====

:Amazon: - Added ability to scope Amazon AWS Clouds to all regions
:Instances: - Both the Name and Display Name property for Instances can now be edited. Previously, only the Display Name could be edited

6.1.0
=====

:Forms: - Added a Form builder tool to aid in creating robust order Forms for Catalog Items

6.0.10
======

:Distributed Worker: - Updated Distributed Worker such that all |morpheus| Agent communications can be routed to the |morpheus| appliance via the Worker

6.0.9
=====

:NSX: Official support added for NSX 4.1
:ServiceNow: Added the ability to switch back to the older table-based API mode for CMDB sync

6.0.8
=====

:Kubernetes: - Upgrade default Kubernetes Cluster Layouts to version 1.28

6.0.7
=====

:Layouts: - Added Display Order property for Layouts. Layouts are listed in high-to-low order based on the Display Order in the Layouts dropdown of the provisioning wizard

6.0.6
=====

:Costing: - The date filter on the Invoices list page now defaults to the last three months to ensure quicker page loads

6.0.5
=====

:Clouds: - IBM PowerVC Cloud support is now officially added. This Cloud type has existed in prior versions but is officially out of Alpha state with 6.0.5
:Kubernetes: - Added Kubernetes 1.25, 1.26 and 1.27 layouts for vCloud Director
             - Added default Kubernetes 1.25, 1.26, and 1.27 layouts for Google Cloud Platform
:Workflows: - When running a Workflow on demand against an Instance, users can now select a phase of Tasks to run when a Provisioning Workflow is selected

6.0.4
=====

:Workflows: - Added Scale Down phase for Provisioning Workflows. Tasks in this phase are run on nodes being deleted when Instances are scaled down (horizontally). This phase is invoked during both manual and automatic scale down events

6.0.3
=====

:Instances: - Instances now have a Name and Display Name field when editing. Previously editing the Name only updated the Display Name database property which created confusion when duplicate name warnings were received in future provisioning
:Logs: - Morpheus Agent logs can now be disabled on a per-server basis in additional to the global enable/disable setting which is already in the product

6.0.2
=====

:Plans & Pricing: - Added the ability to set a cores per socket range on VMware-type Service Plans
:Policies: - Added Max VM Snapshot Policies to allow users to limit the number of stored snapshots per VM which allows greater control over storage
           - Max Policies (Max Cores, Storage, and Memory) now include the option to include or exclude container resources in the Policy
:ServiceNow: - Refactored API calls to ServiceNow which provide integration functionality within Morpheus. This results in greater fault prevention and some performance improvements

6.0.1
=====

:Labels: - Run Tasks, Operational Workflows, or Jobs against a group of Workloads (Instances or servers) with a commomn Label
:Kubernetes: - Added Kubernetes 1.26 support
:Oracle Cloud: - Added two-way tag sync for Oracle Cloud workloads, similar to tag sync capability with other public Clouds
:Policies: - Added Workflow execution approval Policies. When Operational Workflows are executed
:Workflows: - Added Workflow stop capability, such as if you realize a long-running Task will fail and do not wish to wait out the expected failure

6.0.0
=====

:Dashboard: - The main |morpheus| Dashboard landing page (|OpeDas|) has been completely redesigned
:Instances: - Instance detail pages now include a Resources tab which shows VMs, containers, Apps, and other constructs which may be associated with the Instance. Previously this information was on the main detail page, not inside its own tab
            - The Instance detail page header has been redesigned to move more of the most important information to the top of the page
            - The Instance detail page headers has been redesigned to move more of the most important information to the top of the page
            - The Instance detail page now includes a costing tab. This tab pulls and aggregates Instance and host invoices, pricing history charts, pricing trends, and lists associated metered prices
            - The Instances detail page now includes a Summary tab which holds information that was previously in the Info section of the page and was always present (regardless of which subtab the user was looking at)
            - The Instances detail page now includes a monitoring tab which holds memory, storage, CPU, disk I/O and network stats. This information can be shown over a maximum of 90 days depending on your appliance stats retainment setting
:Policies: - Many Policy types can now be scoped to Service Plans
:Workflows: - Nested Workflows have been added. Create modular Workflow pieces to build out larger Workflows
            - Retry failed Workflows from the point where the first Task failed
