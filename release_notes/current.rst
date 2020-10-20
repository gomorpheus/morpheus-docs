.. _Release Notes:

*************************
|morphver| Release Notes
*************************

.. IMPORTANT:: Review :ref:`compatibility` before installing or upgrading |morpheus|

4.2.4 Highlights
================

SCAP Scans Confirm Security Compliance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The SCAP program (Security Content Automation Program) from NIST (National Institute of Standards and Technology) is designed to create an automated and reliable method for setting or verifying security configurations for a system or group of systems. |morpheus| |morphver| adds the ability to call in SCAP security packages and perform SCAP scans using pre-existing scan checklists and security profiles.

- Ensure security compliance of any |morpheus|-managed Instance(s) or server(s)
- Call in existing SCAP packages and checklists from online repositories
- Create Jobs to run SCAP scans against any group of Instances or Servers either on-demand or on recurring schedules
- View complete SCAP evaluation reports on your systems from inside the |morpheus| UI
- `Learn how to run SCAP scans in Morpheus <https://docs.morpheusdata.com/en/4.2.4/provisioning/jobs/jobs.html#creating-and-running-security-scan-jobs>`_

.. image:: /images/provisioning/jobs/security/6server_results.png

ServiceNow Incident Report Improvements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Through its ServiceNow integration, |morpheus| can pass incident data for viewing and handling through the ServiceNow console. In |morpheus| 4.2.4, additional details are passed through to the ServiceNow incident record to directly link back to the specific incident in |morpheus|, as well as provide details on the severity and current resource status.

- Link directly to the matching incident object in |morpheus|
- See incident severity information
- Link directly to the associated Check or Check Group in |morpheus|
- See additional details on the check including its interval, number of failed checks, and whether this incident impacts availability percentage

.. image:: /images/releases/424/servicenow.png

All New Features
----------------

- Amazon: Deploying MySQL or SQL Server with Amazon RDS now automatically creates the corresponding check and Instance status is reported
- Amazon: Routes on AWS routers are now editable (Infrastructure > Network > Selected AWS Network > Routing tab > Pencil icon) in addition to viewing, creating and deleting which could be done previously
- Amazon EKS: Support Added for version 1.7.x

- .. toggle-header:: :header: Azure Public Cloud: **Azure Cloud Integration Improvements**

     - Option to enable Azure Guest OS Diagnostics when provisioning Instance or App
     - Added option to enable Azure Boot Diagnostics when provisioning an Instance or App
     - Set disk encryption (user or platform-managed) and an encryption set (if user-managed) for an Azure Cloud integration (Add/Edit Cloud modal)

- Azure AKS: Support added for version 1.7.11
- Azure Stack: Deploy ARM template Blueprints on Azure Stack Clouds

- .. toggle-header:: :header: KVM: **KVM Improvements**

     - KVM Windows provisioning support added
     - Console access is now available for VMs on the KVM server which were not provisioned by |morpheus|

- OpenStack: Clone updated to work with new OpenStack backup process
- NSX-V: Create and manage DHCP Pools for Edge Gateway routers
- Policies: Load balancer pricing is factored when enforcing budget policies during provisioning and reconfiguration

- .. toggle-header:: :header: Pricing: **Load Balancer Price Tracking**

     - Load balancer support in Price Plans, Price Sets, and Prices (Administration > Plans & Pricing)
     - Load balancer price data sync for Azure and Amazon
     - Automatically apply Price Plans to load balancers based on Plan configuration
     - Usage and Billing data for load balancers

- Provisioning: Set a value to be prepended to all environment variables loaded as part of Instance or App provisioning
- Proxies: Global proxy setting now applies to all |morpheus| functionality, including local integrations such as Ansible and Terraform

- .. toggle-header:: :header: Roles: **Role Permission Changes**

     - Network integration firewall permissions (Infrastructure > Network > Integrations > Selected integration > Firewalls) now have their own setting (Infrastructure: Network Firewalls). Previously they were inherited from the "Network: Integrations" permission

- ServiceNow: "|morpheus| Incident" alerts are now more insightful including links to the related |morpheus| incident or check, severity information, and other details about the failing check
- Security Scanning: Security scan job type added (Provisioning > Jobs) to perform SCAP scans against secure baselines to confirm compliance
- Settings: Cloud refresh interval is now user-configurable, the settings can be changed in Administration > Settings > Appliance (Default: 300 seconds)

- .. toggle-header:: :header: UI: **Interface and Usability Improvements**

     - Icons added for AWS services (such as in Service Catalog), including AWS App Mesh, AWS SQS, and AWS SDB
     - When applying state to Terraform and CloudFormation Apps, a friendly progress bar is displayed to indicate the change
     - Session expiration times can now be configured (Administration > Settings > Appliance), if desired a window can also be displayed at a specified time to warn about the impending logout
     - MySQL tmp file location moved from ``/tmp`` to ``/var/run/morpheus/mysqld``
     - Advanced table view added to Clusters list page (Infrastructure > Clusters) and Load Balancers list page (Infrastructure > Load Balancers)

- Windows: Windows VMs will now auto-expand their root storage partitions to fill drive space, previously this was done manually
- vCloud Director: Create and delete Snapshots in a vCD Cloud

- .. toggle-header:: :header: Veeam: **Backup Jobs can now be deleted**

     - Backup Jobs are deleted from the ACTIONS menu on the Backup Jobs list page (Backups > Jobs)
     - Delete action existed previously but, due to Veeam API limitations, Morpheus could only disable the job
     - Backup job delete is supported only on Veeam version 10

..
  Fixes
  -----


  |morpheus| API Updates
  ======================

  API Enhancements
  ----------------

    - .. toggle-header:: :header: Deployments: **Deployments API/CLI Improvements**

         - Support for adding files to a Deployment version
         - Support for managing Instance deploys (appDeploys). This used to only provide endpoints for a specific instance to deploy and list deploys. Now it has full CRUD, and list shows account wide deploys. See `morpheus deploys`.

  API Fixes
  ---------

    - Billing: Optional parameters added to support pagination of large returns
    - Deployments: The command ``morpheus deploy`` was fixed to correct some unwanted behavior, the ``--help`` flag output was also improved
    - Hosts: Search by tag names and values
    - Instances: Support added for filtering by ``expireDate`` and ``shutdownDate``
    - Instances: Search by tag names and values
    - Search: Global search added similar to the global search bar that has existed in the UI

  |morpheus| CLI Updates
  ======================

  CLI Enhancements
  ----------------


  CLI Fixes
  ---------
