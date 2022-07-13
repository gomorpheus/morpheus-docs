.. _Release Notes:

*************************
|morphver| Release Notes
*************************

- Compatible Plugin API version: |pluginVer|
- Compatible Morpheus Worker version: |workerVer|

.. .. important:: Morpheus Worker v5.4.8 also released. Morpheus v5.4.8 requires Morpheus Worker v5.4.8. Please upgrade any existing Morpheus Workers to the v5.4.8 package.

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version

.. .. include:: highlights.rst

New Features
============

:Blueprints: - Fixed an issue that prevented provisioning some App Blueprints from CloudFormation templates with certain AMI ID parameter formats. :superscript:`5.5.1`
:Clouds: - Updated Cloud logos which were out of date. :superscript:`5.5.1`
:Worker: - Morpheus Worker v5.4.8 release. Note: v5.4.8 Gateway/Worker is the compatible version for Morpheus v5.4.8 Appliances. Previous Gateway/Worker versions must be upgraded to v5.4.8 for compatibility with Morpheus v5.4.8 Appliances.
         - Added support for installing |morpheus| distributed worker on Ubuntu 22.04. :superscript:`5.5.1`
:Plans and Pricing: - Updated Plans list page (Administration > Plans & Pricing > Plans) to include custom view builds (gear icon) to add and remove data fields or sort by custom fields. :superscript:`5.5.1`

Fixes
=====

:API & CLI: - Fixed an issue that could cause port parameters not to be set when specified for Docker-based Node Types in |morpheus| API and CLI. :superscript:`5.5.1`
:Ansible: - Improved handling of validation when Ansible Tasks or Jobs are run against Instances that can no longer be found. :superscript:`5.5.1`
:Archives: - Fixed an issue that could arise when uploading a second file to an Azure backed Archive with the same name as an existing file. :superscript:`5.5.1`
:Azure: - Fixed an issue that could prevent Azure provisioning under specific scenarios if a stored credential set was used to authenticate the Cloud integration. :superscript:`5.5.1`
:Buckets: - There is no longer a pipe character ("|") superimposed over the bucket name on a bucket detail page. :superscript:`5.5.1`
:Costing: - Additional work has been done on Azure costing to add further reduction in duplicated invoice line items. :superscript:`5.5.1`
:Distributed Worker: - Fixed issue with image uploads using morpheus worker hitting Socket Buffer limit.
:Google Cloud (GCP): - Improved plan matching for GCP workloads. Previously, |morpheus| would not set the plan and stats for discovered VMs for a subset of GCP service plans. :superscript:`5.5.1`
:Inputs: - Dependent Inputs are now populated correctly when displayed in App Blueprint deployments. :superscript:`5.5.1`
         - Inputs dependent on other Inputs are now populated correctly when displayed on an Edit Instance dialog. :superscript:`5.5.1`
:Instances: - Fixed an issue that could cause Windows Server 2022 Instances to hang on reconfigure. :superscript:`5.5.1`
:Jobs: - Execution history for Jobs has been improved, previously some executions weren't shown under specific conditions. :superscript:`5.5.1`
:Library: - "Enable Scaling (horizontal)" setting is now honored for specific Layouts even if it is disabled on the Instance Type. :superscript:`5.5.1`
:OpenStack: - Fixed an issue that could cause additional networks to be exposed to the user via the provisioning wizard when their Role restricted Infrastructure: Networks permission to "None". :superscript:`5.5.1`
             - When an Octavia load balancer integration has been removed, |morpheus| now cleans that up rather than continuing to try syncing with the service. :superscript:`5.5.1`
:Option Lists: - |morpheus| API-type Option Lists for Network Security Groups now return the internal database ID for the Security Group as expected. :superscript:`5.5.1`
:Power Scheduling: - Fixed an issue that caused problems provisioning Instances with Power Schedules during a time when the Instance was scheduled to be off. :superscript:`5.5.1`
:Security Groups: - Updated database schema related to a Security Group to prevent specific issues that could arise. :superscript:`5.5.1`
:Terraform: - Terraform Outputs are now updated correctly after applying state changes which update them. :superscript:`5.5.1`
            - When running Terraform commands from the State tab, |morpheus| no longer automatically appends the "-var" option to certain commands where it wasn't needed. :superscript:`5.5.1`
:VMware: - Applying tags and VMware Content Library sync are now working properly when VMware vCenter is accessed behind the |morpheus| Distributed Worker. :superscript:`5.5.1`
:XaaS: - Filtering the Instances list page by Cloud will now also show XaaS Instances which are provisioned to the selected Cloud. :superscript:`5.5.1`
       - The Cloud hyperlink on Instance detail pages for XaaS Instances now links properly to the Cloud the Instance has been provisioned to. :superscript:`5.5.1`
       - The Cloud name now appears on Instance detail pages for XaaS Instances when the user has Infrastructure: Clouds permission set to "None". The name is not hyperlinked in this case due to the user's Role permission. :superscript:`5.5.1`
       - When pricing is correctly configured, price estimates are now shown on detail pages for XaaS Instances. Previously, a "no pricing configured" message was given even if pricing was correctly established. :superscript:`5.5.1`


Appliance & Agent Updates
=========================

:Appliance: - Curl updated to 7.84.0 :superscript:`5.5.1`
            - Elasticsearch upgraded to 7.17.5. :superscript:`5.5.1`
            - Embedded Elasticsearch 'secure_mode' added with TLS & Basic Authentication support. :superscript:`5.5.1`
            - Improved Elasticsearch cleanup job to handle plugin indices.. :superscript:`5.5.1`
            - OpenSSL upgraded to 1.1.1p. :superscript:`5.5.1`
            - Nginx updated to v1.22.0 :superscript:`5.5.1`
            - RabbitMQ and Erlang upgraded to 3.9.20 and 23.3.4.2, respectively. :superscript:`5.5.1`
            - Tomcat upgraded to 9.0.64. :superscript:`5.5.1`
            - Added `bitcan['backup_directory']` and `bitcan['working_directory']` morpheus.rb config options to override default working paths for backups

Morpheus Worker Updates
=======================

:Worker: - Morpheus Worker v5.4.8 released. Morpheus v5.4.8 requires Morpheus Worker v5.4.8. Please upgrade any existing Morpheus Workers to the v5.4.8 package.