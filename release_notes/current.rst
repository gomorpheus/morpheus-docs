.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. NOTE:: Items appended with :superscript:`5.x.x` are also included in that version
.. .. include:: highlights.rst

New Features
============

:API & CLI: - Added API and CLI coverage for configuring DHCP on NSX-T network segments :superscript:`5.2.13`
             - Added API and CLI coverage for configuring DHCP on NSX-T routers :superscript:`5.2.13`
             - Added API coverage for working with NSX-T DHCP static routes :superscript:`5.2.13`
             - Added API endpoints for gathering NSX-T transport zone and edge cluster details :superscript:`5.2.13`
             - Added API endpoints to create and manage NSX-T transport zones :superscript:`5.2.13`
             - Create and manage NSX-T DHCP relays from |morpheus| API and CLI :superscript:`5.2.13`
             - Create and manage NSX-T DHCP servers from |morpheus| API and CLI :superscript:`5.2.13`
             - NSX-T distributed firewall groups and rules can now be created and managed from |morpheus| API and CLI :superscript:`5.2.13`
             - Storage: ``storage-servers`` ``storage-server-types`` & ``storage-volumes`` endpoints added
:Clouds: - Scale Priority field removed from the Add/Edit Cloud modal. For Docker provisioning, this field could be used to determine which Cloud would take scale precedence in the Group. This is no longer needed since |morpheus| works with cluster constructs :superscript:`5.2.13`
:Kubernetes: - AKS: Cluster Scaling functionality added
              - GKE: Cluster Scaling functionality added
:Logs: - New universal React log view component for Instance, App, Server, Cluster, Monitoring > Logs, and Administration > Health > |morpheus| Logs sections.
:NSX: - Added the ability to configure DHCP static routes for NSX-T :superscript:`5.2.13`
       - Added the capability to monitor health status of load balancer server pool members :superscript:`5.2.13`
       - Distributed firewalls for NSX-T are now accessible to Subtenants when an NSX-T integration and distributed firewall has been shared from the primary Tenant :superscript:`5.2.13`
       - When creating or editing NSX-V router interfaces (distributed routers or edge gateways), users can now add a secondary IP address, if desired, rather than just a primary :superscript:`5.2.13`
:OpenStack: - Cinder Volume type selection support for Openstack added
:Plans & Pricing: - Platform Pricing: Distro specific Platform options added to Platform price types: ``Linux Canonical``, ``Linux Centos``, ``Linux Debian``, ``Linux Fedora``, ``Linux OpenSuse``, ``Linux RedHat``, ``Linux Suse``, and ``Linux Xen``
:Plugins: - Invalid jars are now displayed as Invalid in the Plugins directory.
           - Settings added: Ability to edit Plugins and configure standard and custom settings added
:Roles: - Kubernetes: Added new role permission ``Infrastructure: Kubernetes Control`` with ``full`` and ``none`` options to enable more fine grained access to kubernetes control
:Security: - Re-authentication now required when updating user password from User Settings in the UI. The logged in user or impersonated user must now enter the Current Password and then a matching Password/Confirm value to change the password.
:UI: - For security purposes, the |morpheus| version number has been removed from the login screen. The version number is still viewable from the footer once the user is logged in :superscript:`5.2.13`
:VMware: - |morpheus| now extracts ovf details of uploaded virtual images
:vCloud Director: - VCD NSX Integration added (Phase 1)
                  - VCD NSX: Application Port Profiles CRUD added
                  - VCD NSX: Configure DNS on a network: DNS Primary and DNS Secondary values can be specified on a VCD network now
                  - VCD NSX: IP Sets CRUD: Ability to create and managed VCD NSX IP Sets
                  - VCD NSX: NAT Rules: NAT functionality for VCD NSX routers added
                  - VCD NSX: Network CRUD added with ability to create and managed ``VCD Isolated`` and ``VCD Routed`` Networks.
                  - VCD NSX: Security Groups CRUD: Added ability to create and manage VCD NSX Router Firewall Group Security Groups.


Fixes
=====

:API & CLI: - AKS clusters can now be provisioned from |morpheus| CLI
             - API calls to GET all Layouts no longer return Layouts to which the user doesn't have access :superscript:`5.2.13`
             - Fixed an intermittent issue that could cause returned Instance lists not to be filtered properly in |morpheus| API :superscript:`5.2.13`
             - Fixed an issue causing NSX-T network router firewall groups and rules creation from Subtenants to fail from |morpheus| API and CLI :superscript:`5.2.13`
             - |morpheus| API access tokens now update with permissions changes in real time. When permissions are updated in |morpheus| UI, the changes will be effective immediately for future calls using the existing token :superscript:`5.2.13`
:Alibaba Cloud: - Alibaba Cloud integrations are updated to honor proxy settings which prevented the ability to create these Clouds in certain environments :superscript:`5.2.13`
:Amazon: - |morpheus| now honors VPC-scoping when displaying Security Groups :superscript:`5.2.13`
:Ansible Galaxy: - Playbooks will no longer continue to run after an Ansible Galaxy command failure
:Azure Stack: - Fixed an issue that caused the Resources Tab on Azure Stack Clouds to get stuck in a loading state leaving the user unable to view the data or work with those constructs :superscript:`5.2.13`
:Azure: - Fixed an issue that caused the personal Windows user account (as stored in |morpheus| user settings) not to be added, even when marking the box to "Create My User" during provisioning
:Backups: - Fixed an issue that could cause the appliance backup time to be set incorrectly when editing an existing appliance backup job :superscript:`5.2.13`
:Domains: - Fixed issue with ``Local Domain`` domain option being selectable when Group Visibility is disabled for that domain.
:ESXi: - Fixed an issue causing connection issues to ESXi hosts when the host contained notes which had double quotes (") in them :superscript:`5.2.13`
:Elasticsearch: - Fixed an issue that could cause |morpheus| not to clean up all ElasticSearch logs which could eventually lead to log sizes becoming very large :superscript:`5.2.13`
:Hosts: - Fixed an issue that could cause server names to become out of sync between |morpheus| and the cloud when the VM/server name was edited in both places at approximately the same time :superscript:`5.2.13`
         - Removed the 'Retry' link from the Hosts and VMs list page (Infrastructure > Compute > Hosts or Virtual Machines) next to red status entries :superscript:`5.2.13`
:Inputs: - Corrected an issue that could cause Typeahead Inputs not to search values correctly when associated with Operational Workflows :superscript:`5.2.13`
          - Custom options (Inputs) always appear in the correct order on Instance Types, previously they could appear out of order if Inputs were added to the Instance Type after it was initially saved :superscript:`5.2.13`
          - Option types containing quotes (") can now be passed into Service Catalog orders without creating errors
:Instances: - Fixed an issue which would cause auto-scaling to attempt to add VMs to Clouds other than the one existing VMs were in, which often would fail :superscript:`5.2.13`
:NSX-T: - Fixed an issue that caused NSX-T network server groups created in a Subtenant not to be visible to Subtenant users :superscript:`5.2.13`
         - Gateway DHCP can now be configured on NSX-T network segments :superscript:`5.2.13`
         - The Subnet DHCP section now expands properly when editing the network from an NSX-T detail page. Previously this section would not expand when clicked on :superscript:`5.2.13`
:NSX: - Creating a NSX-T router group in a Subtenant and referencing it or a group shared from the primary tenant now works properly when creating a load balancer pool :superscript:`5.2.13`
       - Firewall groups in NSX-T routers are now able to reference router groups created in the Subtenant or shared from the primary tenant :superscript:`5.2.13`
       - The modal for editing Edge or DLR routers no longer hangs in a loading state under certain conditions
:Open Telekom Cloud: - Changed the default "Bandwidth" field value to 300 mbps when provisioning to OTC on-prem Clouds and selecting a floating IP. The previous default of 1000 could cause problems if not specifically edited by the user :superscript:`5.2.13`
:OpenStack: - Fixed an issue that could cause Plans not to appear in the provisioning wizard for OpenStack Instances after upgrading |morpheus|
             - Restoring an Instance backup to a new Instance no longer attempts to use the same public IP address which could cause failures when the original IP address was still taken
             - When an OpenStack Cloud is created in the primary Tenant and shared with a Subtenant, Subtenant users can now see the Roles list on the Resource Pools tab
:Option Lists: - Fixed an issue that caused Option Lists from the |morpheus| Plans API not to populate correctly when associated with Service Catalog Blueprints or Workflows (Catalog Instances worked fine) :superscript:`5.2.13`
:Plans & Pricing: - Setting vCPUs to custom and max storage to 0 no longer zeroes out other values on the plan (such as disk sizes and memory amounts) :superscript:`5.2.13`
:Plugins: - Fixed errors that could surface when provisioning from custom Clouds developed using |morpheus| plugin architecture
:Power Schedules: - Fixed an issue that caused Power Schedules not to appear on VMs assigned to Subtenants if the Power Schedule did not also exist in the Subtenant
:PowerShell: - Fixed an issue that could cause PowerShell Tasks executed locally not to return the entire standard output
:Provisioning: - When provisioning a plan that allows for custom root volume sizes, |morpheus| will no longer allow the user to set a root volume smaller than the template. Previously there was a UI warning but the user could still bypass it and the provision would fail
                - When provisioning using stored software licenses (Administration > Settings > Software Licenses), licenses can now be added to unattend.xml even when Sysprep is not enabled on the image.
:Roles: - Fixed an issue causing changes to Group Access permissions (which are saved automatically after each change) not to be retained under certain specific scenarios :superscript:`5.2.13`
:Security: - The username cookie is now cleared on logout :superscript:`5.2.13`
            - When logging out as a Subtenant user, the URL which redirects the user back to the login page no longer includes the Subtenant name and username :superscript:`5.2.13`
:Service Catalog: - Fixed an issue that, in certain scenarios, could cause failed provisioning when lines of Blueprint app spec wrapped onto the next line :superscript:`5.2.13`
:Storage: - Fixed a few minor issues that could cause problems with various CRUD actions related to storage servers :superscript:`5.2.13`
:Tasks: - Fixed an issue that could prevent Python Tasks from retrieving Cypher secrets when more than ten Python Tasks happened to be running simultaneously :superscript:`5.2.13`
:Terraform: - Fixed issue with reading Terraform variables from submodules instead of variables from the working folder's vars. (5.4.0)
             - Multiline string variables are now supported which makes recalling GCP service account credentials from |morpheus| cypher much easier. See |morpheus| Knowledge Base for an example.
             - Removed non-functional state file copy button.
             - Type errors are no longer surfaced when calling Map of List of String type variable
:UI: - Fixed issues related to form rendering and display when editing EKS clusters
      - Puppet Master hostname now appears on the detail page for the Puppet integration. Previously there was a UI space blocked out for the hostname but it was never rendered into the UI :superscript:`5.2.13`
      - The Options dropdown menu on many list pages (such as the Instances list page) no longer clips over other menus and headers when the menu is left open and scrolled up and out of the view window :superscript:`5.2.13`
:Usage: - Fixed an issue that caused component prices not to be displayed in certain scenarios on the Usage tab (Operations > Costing > Usage)
:VMware: - Users can no longer provision a Kubernetes cluster without an IP Pool. This would cause a provisioning failure because no IP addresses would be available for the worker nodes
:vCloud Director: - Fixed issues that could cause power state mismatch between |morpheus| and vCD which could cause inaccuracies in usage stats and billing in |morpheus|
                  - Instance provisioning no longer fails when attempting to provision with hostnames containing trailing hyphens (-). Instead, UI error messages are surfaced and the user can correct the problem before provisioning :superscript:`5.2.13`


Appliance & Agent Updates
=========================

:Appliance: - lvm-attrib-gem updated to to 0.3.9 :superscript:`5.2.13`



.. ..