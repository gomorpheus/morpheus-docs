Nutanix Prism Central
---------------------

|morpheus| offers Nutanix Prism Central Cloud integration support through and official plugin. Adding the plugin to a |morpheus| appliance adds a new Cloud integration type for Nutanix Prism Central. Download the plugin from the |morpheus| `Plugin Exchange <https://share.morpheusdata.com/morpheus-nutanix-prism/about>`_ and upload it to the appliance. Plugins are uploaded at |AdmIntPlu|. See |morpheus| `plugin documentation <https://docs.morpheusdata.com/en/latest/administration/integrations/integrations.html#plugins>`_ for more details on adding plugins.

Features
^^^^^^^^

* Virtual Machine Provisioning
* Backups / Snapshots
* Automatic Cloud sync
* Project scoping
* Brownfield VM management
* Clone VMs to images
* Host monitoring
* Datastore management
* Hypervisor Remote Console
* Lifecycle Management and Resize

Adding a Nutanix Prism Central Cloud
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adding Nutanix Prism Clouds to |morpheus| requires little more than the API URL and valid username and password credentials for a user with sufficient access to the resources that should be utilized by |morpheus|. You'll also need to ensure |morpheus| can reach the NPC appliance at its API URL.

Navigate to |InfClo| and click :guilabel:`+ ADD`. As long as the Nutanix Prism Central plugin have been added to the appliance and this Cloud type isn't disabled in global settings (|AdmSet|), NUTANIX PRISM CENTRAL should be selectable as a Cloud type to add. Select it and click :guilabel:`NEXT`.

.. image:: /images/clouds/npc/pickType.png
  :width: 50%

At minimum, it's required to configure the following to add the new cloud:

- **NAME:** A friendly name for the new NPC Cloud in |morpheus|
- **API URL:** API access URL (ex. https://xx.xx.xx.xx:9440)
- **USERNAME:** Username for a Nutanix Prism Central service account
- **PASSWORD:** The password for the service account

You'll know the API URL and credentials have been entered correctly when the PROJECTS dropdown becomes populated. You may choose to scope Nutanix Prism Central Clouds to a specific project or scope the Cloud to all Projects. Click :guilabel:`NEXT` and select a Group for the Cloud or create a new Group. Click :guilabel:`NEXT` to reach the review screen and then click :guilabel:`COMPLETE`.

.. image:: /images/clouds/npc/configureCloud.png

After completing the wizard, |morpheus| will immediately begin to add the new Cloud and perform the first Cloud sync. Within a short time, existing workloads will be discovered and onboarded into |morpheus| UI (if you've chosen to discover existing workloads). The Cloud is now ready to be used as a provisioning target or for day-two operations.
