.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

.. IMPORTANT:: |morphver| contains embedded MySQL v8 upgrade when upgrading from  v6.0.0 - v6.0.6 or 6.1.0 - 6.2.1. BACKUP YOUR DATABASE PRIOR TO UPGRADE when using embedded MySQL (all-in-one appliances)
.. IMPORTANT:: Minimum v6.x required to upgrade to |morphver| for environments using embedded RabbitMQ. Environments running 5.5.x or earlier using embedded RabbitMQ must upgrade to v6.0.0 - v6.0.6, or 6.1.0 - 6.2.1 prior to upgrading to |morphver|
.. WARNING:: Rolling upgrades for HA environments using embedded RabbitMQ and/or embedded Elasticsearch services are not supported when upgrading from  v6.0.0 - v6.0.6 or 6.1.0 - 6.2.1

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade version: |minUpgradeVer|

.. NOTE:: Items appended with :superscript:`6.x.x` are also included in that version

Release Dates

- |morphver| |releasedate|

New Features
============

:API & CLI: - The Certificates API endpoint now validates the given integration ID and does not create the certificate if an integration with the given ID does not exist :superscript:`6.0.9 6.3.1`
             - ``refId`` and ``refType`` parameters are no longer ignored when |morpheus|-type IP Pool reservations are made over |morpheus| API :superscript:`6.0.9 6.3.1`
:Currency: - Added Malaysian Ringgit (MYR) currency support :superscript:`6.0.9 6.3.1`
            - Added support for Mongolian Tugrik (MNT) currency :superscript:`6.0.9 6.3.0 `
            - Added support for Singapore Dollar (SGD) currency :superscript:`6.0.9 6.3.1`
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


Fixes
=====

:Agent: - Updated public key used by agent installation scripts to prevent downstream warnings or errors in logs :superscript:`6.0.9 6.3.1`
:API & CLI: - |morpheus| is now displaying invalid value or string too long errors for the various BGP neighbor properties when updating a network router's BGP neighbors through the API :superscript:`6.0.9 6.3.1`
:Blueprints: - ARM-type App Blueprints no longer fail on provisioning when they contain array-type parameters with a default value indicated :superscript:`6.0.9 6.3.1`
:Costing: - Fixed an issue that could cause an incorrect price to be displayed if the price was set by a long-running Price phase Task :superscript:`6.0.9 6.3.1`
:Database: - Added an index on the ``process_id`` column in the ``job_execution`` table of the database. This will improve performance for those with very large ``job_execution`` tables :superscript:`6.0.9 6.3.1 `
:Forms: - Fixed the Security Group ID Form variable not resolving in config which caused provisioning failures :superscript:` 6.3.1`
:Inputs: - Typing any value into typeahead-type Inputs which are marked required will no longer satisfy the Input. A valid selection from the dropdown field must be selected :superscript:`6.0.9 6.3.1`
:Installer: - ``sshd-core`` upgraded to 2.10 to mitigate CVE-2023-3588 :superscript:`6.0.9 6.3.1`
:Instances: - For Windows Instances installing |morpheus| Agent via Unattend, |morpheus| will now detect if there is already content in the SetupComplete.cmd script file and ensure the Agent install script is appended in such a way that all scripts will run properly :superscript:`6.0.9 6.3.1`
:Kubernetes: - Fixed failed MKS cluster upgrades from 1.26.x to 1.27.x which were failing due to a removed parameter :superscript:`6.0.9 6.3.1`
:NSX-T: - Fixed a visibility issue that allowed all edge cluster nodes to be visible to all Tenants when the same NSX-T integration was shared with them and individual edge clusters were assigned to each via visibility permissions :superscript:`6.0.9 6.3.1`
         - Increased the network server refresh lock timeout to reduce appliance CPU consumption under certain use cases :superscript:`6.0.9 6.3.1`
:OpenStack: - DNS records are now removed on Instance deletion when setting a floating IP at provision time with a Route53 integration on OpenStack Clouds :superscript:`6.0.9 6.3.1`
:Option Lists: - Added global maximum setting for Option Lists as it was possible to severely reduce appliance performance in some cases with extremely large Option Lists :superscript:` 6.3.1`
                - Updated REST-type Option Lists to no longer ignore the "no proxy" global setting :superscript:`6.0.9 6.3.1`
:Plans and Pricing: - Fixed an issue with custom Service Plans where sometimes the workload size values (CPU, memory, etc.) would only be correct after selecting another Plan, then coming back to reload the original :superscript:`6.0.9 6.3.1`
:Plugins: - Fixed used IPs count (such as on the IP Pools list page) to include reservations made through |morpheus| provisioning or manual assignment in addition to those discovered :superscript:`6.0.9 6.3.1`
:Remedy: - Fixed an issue that prevented loading of COMPANY and APPROVAL USER fields when adding a Remedy integration which made it impossible to create the integration :superscript:`6.0.9 6.3.1`
:SCVMM: - Fixed an SCVMM provisioning issue that would occur when multiple virtual machine paths existed in the SCVMM hosts :superscript:`6.0.9 6.3.1`
:Security: - Fixed an issue that could allow arbitrary code execution against a workload within an Ansible Task execution :superscript:`6.0.9 6.3.1`
            - The returned error message when attempting to edit a Cloud name to a very long string via |morpheus| API has been altered for security reasons :superscript:`6.0.9 6.3.1`
            - The |morpheus| Agent API key is now masked from server and host detail pages for security reasons :superscript:`6.0.9 6.3.1`
:Tasks: - Updated HTTP-type Tasks to no longer ignore the global "no proxy" setting :superscript:`6.0.9 6.3.1`
:Terraform: - Terraform now honors the global "no proxy" setting :superscript:`6.0.9 6.3.1`
:VMware: - Changes made to the disk size on the template in vCenter are now reflected in |morpheus| :superscript:`6.0.9 6.3.1`
          - Converting VMware VMs to managed no longer strips away any tags in VMware :superscript:`6.0.9 6.3.1`
          - |morpheus| now supports VMware tags with "multiple" cardinality :superscript:`6.0.9 6.3.1`
:Workflows: - When running Workflows from the Instance Action menu, it will no longer take multiple clicks on the dropdown menu to display all available Workflows :superscript:`6.0.9 6.3.1`

Embedded Plugins
=========================

:Infoblox: infobox-plugin updated to v1.2.3
