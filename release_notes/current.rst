.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version
.. .. include:: highlights.rst

New Features
============

:API & CLI: - Added API and CLI coverage for configuring DHCP on NSX-T network segments :superscript:`5.4.1`
             - Added API and CLI coverage for configuring DHCP on NSX-T routers :superscript:`5.4.1`
             - Added API coverage for working with NSX-T DHCP static routes :superscript:`5.4.1`
             - Added API endpoints for gathering NSX-T transport zone and edge cluster details :superscript:`5.4.1`
             - Added API endpoints to create and manage NSX-T transport zones :superscript:`5.4.1`
             - Create and manage NSX-T DHCP relays from |morpheus| API and CLI :superscript:`5.4.1`
             - Create and manage NSX-T DHCP servers from |morpheus| API and CLI :superscript:`5.4.1`
             - Get NSX-T Edge Cluster details from |morpheus| API and CLI :superscript:`5.4.0`
             - NSX-T distributed firewall groups and rules can now be created and managed from |morpheus| API and CLI :superscript:`5.4.1`
:Amazon: - Added support for additional regions: ``eu-south-1`` Europe (Milan), ``eu-west-3`` Europe (Paris), and ``me-south-1`` Middle East (Bahrain) :superscript:`5.4.0`
:Clouds: - Scale Priority field removed from the Add/Edit Cloud modal. For Docker provisioning, this field could be used to determine which Cloud would take scale precedence in the Group. This is no longer needed since |morpheus| works with cluster constructs :superscript:`5.4.1`
:Currency: - Added support for new currencies: Jordan Dinar (JD), Saudi Arabia Riyal (SAR), and United Arab Emirates Dirham (AED) :superscript:`5.4.0`
:NSX: - Added the ability to configure DHCP static routes for NSX-T :superscript:`5.4.1`
       - Added the capability to monitor health status of load balancer server pool members :superscript:`5.4.1`
       - Distributed firewalls for NSX-T are now accessible to Subtenants when an NSX-T integration and distributed firewall has been shared from the primary Tenant :superscript:`5.4.1`
       - When creating or editing NSX-V router interfaces (distributed routers or edge gateways), users can now add a secondary IP address, if desired, rather than just a primary :superscript:`5.4.1`
:Oracle Cloud: - Added support for Oracle Public Cloud Dubai region :superscript:`5.4.0`
:UI: - For security purposes, the |morpheus| version number has been removed from the login screen. The version number is still viewable from the footer once the user is logged in :superscript:`5.4.1`


Fixes
=====

:API & CLI: - API calls to GET all Layouts no longer return Layouts to which the user doesn't have access :superscript:`5.4.1`
             - Fixed an intermittent issue that could cause returned Instance lists not to be filtered properly in |morpheus| API :superscript:`5.4.1`
             - Fixed an issue causing NSX-T network router firewall groups and rules creation from Subtenants to fail from |morpheus| API and CLI :superscript:`5.4.1`
             - |morpheus| API access tokens now update with permissions changes in real time. When permissions are updated in |morpheus| UI, the changes will be effective immediately for future calls using the existing token :superscript:`5.4.1`
:Alibaba Cloud: - Alibaba Cloud integrations are updated to honor proxy settings which prevented the ability to create these Clouds in certain environments :superscript:`5.4.1`
:Amazon: - Fixed an issue with Amazon provisioning where, if you stepped through the wizard and selected a Security Group, then went back and chose another AWS Cloud, the Security Group from the first Cloud was still present and could cause provisioning failure :superscript:`5.4.0`
          - |morpheus| now honors VPC-scoping when displaying Security Groups :superscript:`5.4.1`
:Ansible: - Fixed an issue causing Ansible Tasks to fail due to Ansible Galaxy install issues :superscript:`5.4.0`
:Azure Stack: - Fixed an issue that caused the Resources Tab on Azure Stack Clouds to get stuck in a loading state leaving the user unable to view the data or work with those constructs :superscript:`5.4.1`
:Backups: - Fixed an issue that could cause the appliance backup time to be set incorrectly when editing an existing appliance backup job :superscript:`5.4.1`
:Catalog: - Fixed an issue where the Catalog could become inaccessible for a user after adding an item to the cart which contained an Option List with invalid data :superscript:`5.4.0`
:Clusters: - Docker Cluster provisioning now respects custom ranges on Plans when CUSTOMIZE EXTRA VOLUMES and ADD VOLUMES is enabled on the plan :superscript:`5.4.0`
:ESXi: - Fixed an issue causing connection issues to ESXi hosts when the host contained notes which had double quotes (") in them :superscript:`5.4.1`
:Elasticsearch: - Fixed an issue that could cause |morpheus| not to clean up all ElasticSearch logs which could eventually lead to log sizes becoming very large :superscript:`5.4.1`
:Guidance: - Users with ``Guidance -> Full`` but ``Read`` Group permissions are no longer able to perform full actions in Guidance against resources in that Group :superscript:`5.4.0`
:Hosts: - Fixed an issue that could cause server names to become out of sync between |morpheus| and the cloud when the VM/server name was edited in both places at approximately the same time :superscript:`5.4.1`
         - Removed the 'Retry' link from the Hosts and VMs list page (Infrastructure > Compute > Hosts or Virtual Machines) next to red status entries :superscript:`5.4.1`
:Identity Sources: - Fixed issue with customSSO API 500 response for multiple customsso user token requests :superscript:`5.4.0`
:Inputs: - Corrected an issue that could cause Typeahead Inputs not to search values correctly when associated with Operational Workflows :superscript:`5.4.1`
          - Custom options (Inputs) always appear in the correct order on Instance Types, previously they could appear out of order if Inputs were added to the Instance Type after it was initially saved :superscript:`5.4.1`
:Instances: - Fixed an issue which would cause auto-scaling to attempt to add VMs to Clouds other than the one existing VMs were in, which often would fail :superscript:`5.4.1`
             - Startup and shutdown entries no longer show in the History tab of the Instance Detail page if there are no Tasks associated with those phases of the Instance Provisioning Workflow :superscript:`5.4.0`
:Library: - DOCKER COMMAND EXTRA field added to Docker Node Types to add arbitrary docker command line args :superscript:`5.4.0`
:Load Balancers: - Improved UI error messages when load balancer virtual server creation fails :superscript:`5.4.0`
:Logs: - Added optimizations for Agent logs to improve performance and scalability :superscript:`5.4.0`
:NSX-T: - Cleaned up Gateway Interface sync errors which would appear in logs on NSX-T integration sync :superscript:`5.4.0`
         - Fixed an issue that caused IP Management Settings on an NSX-T router not to be set properly on the |morpheus| side compared to what was in NSX-T :superscript:`5.4.0`
         - Fixed an issue that caused NSX-T network server groups created in a Subtenant not to be visible to Subtenant users :superscript:`5.4.1`
         - Gateway DHCP can now be configured on NSX-T network segments :superscript:`5.4.1`
         - NSX-T load balancer virtual server creation no longer gives the option for generating a self-signed server. This change was made to prevent confusion as NSX-T LB virtual servers cannot use self-signed certificates :superscript:`5.4.0`
         - Subtenant users can now select an NSX-T integration shared from the Primary Tenant for purposes of creating SSL certificates :superscript:`5.4.0`
         - The Subnet DHCP section now expands properly when editing the network from an NSX-T detail page. Previously this section would not expand when clicked on :superscript:`5.4.1`
:NSX-V: - Fixed an issue that caused errors to be thrown when attempting to edit locked NSX-V distributed firewall rules :superscript:`5.4.0`
:NSX: - Creating a NSX-T router group in a Subtenant and referencing it or a group shared from the primary tenant now works properly when creating a load balancer pool :superscript:`5.4.1`
       - Firewall groups in NSX-T routers are now able to reference router groups created in the Subtenant or shared from the primary tenant :superscript:`5.4.1`
:Open Telekom Cloud: - Changed the default "Bandwidth" field value to 300 mbps when provisioning to OTC on-prem Clouds and selecting a floating IP. The previous default of 1000 could cause problems if not specifically edited by the user :superscript:`5.4.1`
:Option Lists: - Fixed an issue that caused Option Lists from the |morpheus| Plans API not to populate correctly when associated with Service Catalog Blueprints or Workflows (Catalog Instances worked fine) :superscript:`5.4.1`
:Plans & Pricing: - Setting vCPUs to custom and max storage to 0 no longer zeroes out other values on the plan (such as disk sizes and memory amounts) :superscript:`5.4.1`
:Provisioning: - When provisioning into a network with a |morpheus| IP Pool and selecting a static IP, the IP is no longer automatically assigned to the first range in the pool, which could cause errors when the address was outside that range :superscript:`5.4.0`
:Remedy: - Fixed a number of issues with the Remedy integration to improve the user experience :superscript:`5.4.0`
:Roles: - Fixed an issue causing changes to Group Access permissions (which are saved automatically after each change) not to be retained under certain specific scenarios :superscript:`5.4.1`
:SCVMM: - Fixed an issue where Instances provisioned to SCVMM Clouds from Subtenants would not correctly receive static IP addresses as selected during provisioning :superscript:`5.4.0`
:Security Scans: - Windows SCAP scans can now utilize XML files in addition to ZIP files :superscript:`5.4.0`
:Security: - The username cookie is now cleared on logout :superscript:`5.4.1`
            - When creating new Apps, certain detailed MySQL exceptions are no longer surfaced into the UI. Instead, a more generic error message is surfaced directing the user to check logs for the complete exception :superscript:`5.4.0`
            - When logging out as a Subtenant user, the URL which redirects the user back to the login page no longer includes the Subtenant name and username :superscript:`5.4.1`
:Service Catalog: - Fixed an issue that, in certain scenarios, could cause failed provisioning when lines of Blueprint app spec wrapped onto the next line :superscript:`5.4.1`
:ServiceNow: - Fixed an issue that caused Inputs not to be updated on Instance Types exposed to ServiceNow integrations after the Inputs were edited in the Instance Type in |morpheus|
:Storage: - Fixed a few minor issues that could cause problems with various CRUD actions related to storage servers :superscript:`5.4.1`
:Tasks: - Fixed an issue that could prevent Python Tasks from retrieving Cypher secrets when more than ten Python Tasks happened to be running simultaneously :superscript:`5.4.1`
:UI: - Fixed presentation issues with some automated email, including inactive user warning email, old password warning email, disabling inactive user email, and login attempts with locked email warnings :superscript:`5.4.0`
      - Puppet Master hostname now appears on the detail page for the Puppet integration. Previously there was a UI space blocked out for the hostname but it was never rendered into the UI :superscript:`5.4.1`
      - The Options dropdown menu on many list pages (such as the Instances list page) no longer clips over other menus and headers when the menu is left open and scrolled up and out of the view window :superscript:`5.4.1`
:Users: - Fixed an issue that could cause 500 errors and failure when editing a User synced from an identity source integration to have a Linux password of insufficient complexity :superscript:`5.4.0`
:Whitelabel: - The opacity slider in the whitelabel color picker (Administration > Settings > Whitelabel) now works correctly :superscript:`5.4.0`
:vCloud Director: - Instance provisioning no longer fails when attempting to provision with hostnames containing trailing hyphens (-). Instead, UI error messages are surfaced and the user can correct the problem before provisioning :superscript:`5.4.1`


Appliance & Agent Updates
=========================

:Appliance: - MacOS Node package jre version updated to 8u312-b07 :superscript:`5.4.0`
             - lvm-attrib-gem updated to to 0.3.9 :superscript:`5.4.1`



.. ..