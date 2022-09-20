.. _Release Notes:

*************************
|morphver| Release Notes
*************************

- Compatible Plugin API version: |pluginVer|
- Compatible Morpheus Worker version: |workerVer|

.. important::

   Known issue with embedded Elasticsearch upgrade: When upgrading to v5.4.8, v5.4.9 or v5.5.1, there is a potential issue with embedded Elasticsearch clustering on rolling upgrades and existing data migration for all embedded Elasticsearch architechtures. Release versions with a fix will be posted soon. The issue can be mitigated by running the following after installing/upgrading the v5.4.8, 5.4.9 or 5.5.1 package and PRIOR to running reconfigure. 

   As root, after installing/upgrading the v5.4.8, 5.4.9 or 5.5.1 package and PRIOR to running reconfigure, run the following:

   .. code-block:: bash

     	rm -f /var/opt/morpheus/elasticsearch   
     	mv /var/opt/morpheus/elasticsearch-7.8.1 /var/opt/morpheus/elasticsearch-7.17.5
     	morpheus-ctl reconfigure

.. important::  Security: CVE-2022-35912: Morpheus v5.5.1-2 and v5.4.8-2 are now available in response to CVE-2022-35912, a Grails Framework remote code execution vulnerability. v5.5.1-2 and v5.4.8-2 include the Grails v5.1.9 update that mitigates the vulnerability. At this time, the Grails vulnerability is only confirmed for grails frameworks running on Java 8. Morpheus versions v5.4.4 and higher are on Java 11. Customers on morpheus v5.4.3 or earlier are highly advised to upgrade to at minimum v5.4.4 or higher, and out of an abundance of caution we recommend all customers upgrade to v5.5.1-2 or v5.4.8-2 in the event the vulnerability is found to be exploitable on Java 11.

.. warning:: Morpheus |morphver| requires Morpheus Worker |workerVer|. Please upgrade any existing Morpheus Workers to the |workerVer| Worker package to ensure compatibility with Morpheus |morphver|.

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version

.. .. include:: highlights.rst

Release Dates
  - 5.4.8-1 |releasedate|
  - 5.4.8-2 Jul 20 2022

.. toggle-header:: 
    :header: 5.4.8-2 Updates **Click to Expand/Hide**

     5.4.8-2 contains the following updates not included in 5.4.8-1:

     :Security: - CVE-2022-35912 - Morpheus v5.5.1-2 and v5.4.8-2 include the Grails v5.1.9 update that mitigates the CVE-2022-35912 Grails Framework remote code execution vulnerability. At this time, the  vulnerability is only confirmed for grails frameworks running on Java 8. Morpheus versions v5.4.4 and higher are on Java 11. Customers on morpheus v5.4.3 or earlier are highly advised to upgrade to at minimum v5.4.4 or higher, and out of an abundance of caution we recommend all customers upgrade to v5.5.1-2 or v5.4.8-2 in the event the vulnerability is found to be exploitable on Java 11. :superscript:`5.4.8-2`
     :Azure: - Costing: Fixed Azure costing failing when 429 too many attempts api error is encountered :superscript:`5.5.1-2`
             - Costing: Fixed Azure costing issues related to currency conversion :superscript:`5.5.1-2`
     :Inputs: - Options Types: Fixed export as tag and display value on details not working for catalog items :superscript:`5.5.1-2`
              - Options Types: Improved handling of api option list loading. "No options found" no longer displayed prior to api response, "Failed to load options" now displayed on empty response. :superscript:`5.5.1-2`
     :Openstack: - Reverted 5.4.8-1 update that tied Openstack IP Pool visibility to network visibility :superscript:`5.5.1-2`
     :Plugins: - Update the plugin core to handle the "show on detail" flag in seed. morpheus-plugin-api:0.12.6 :superscript:`5.5.1-2`
     :Security Groups: - Fixed maxSize constraint on security group rule destination causing sync error when destination block contains > 1000 chars :superscript:`5.5.1-2`

|

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