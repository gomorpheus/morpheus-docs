Nutanix Prism Element
---------------------

Overview
^^^^^^^^

Nutanix Prism Element simplifies datacenter infrastructure by integrating server and storage resources allowing applications to run at scale. |morpheus| enhances Nutanix resources by allowing efficient and seamless deployment of virtualized or containerized applications, management of existing brownfield resources in Nutanix Clouds, pricing and cost tracking, and monitoring of running workloads.

Features
^^^^^^^^

* Virtual machine provisioning
* Brownfield discovery
* Containers
* Backups / Snapshots
* Datastores
* Kubernetes
* Resources Groups
* Migrations
* |morpheus| costing and pricing
* Auto Scaling
* Load Balancing
* Remote Console for hypervisor hosts and running workloads
* Two-way Cloud sync
* Lifecycle Management and Resize

.. Note:: Prism Central is currently supported and is maintained as a separate, plugin-based Cloud integration. See the `Prism Central plugin page <https://share.morpheusdata.com/plugin/morpheus-nutanix-prism/about>`_ on the |morpheus| plugin share site for additional details and access to the plugin. There is also an `integration guide <https://docs.morpheusdata.com/en/latest/integration_guides/Clouds/prismCentral/prismCentral.html>`_ for that plugin here in |morpheus| UI documentation.

Getting Started
^^^^^^^^^^^^^^^

To get started, first confirm that a few prerequisite steps have been completed. The Nutanix cluster should be provisioned and available on the network. In a typical configuration, Nutanix will be available at the ``https://fqdn:9440`` URL. Have the credentials for an administrator service account available to integrate |morpheus| with the Nutanix cluster. With those prerequisites already completed, you're ready to add a Nutanix Cloud to |morpheus| using the instructions in the next section.

Adding a Nutanix Cloud
^^^^^^^^^^^^^^^^^^^^^^^

To start, navigate to the Cloud list page (|InfClo|) and click :guilabel:`+ ADD`. On the ADD CLOUD modal, you will at least need to provide a NAME for the Cloud in |morpheus| along with the API URL and credentials. Other fields listed here are optional but may be needed for the Cloud to perform as desired in your environment.

- **NAME:** A name for the Nutanix Cloud within |morpheus|
- **CODE:** A unique code for the cloud which is used in |morpheus| API, CLI, and in automation scripts
- **LABELS:** Select or create a new Label to apply to the Cloud. See `Labels documentation <https://docs.morpheusdata.com/en/latest/library/labels.html>`_ for a complete description of the usefulness of Labels
- **LOCATION:** An optional description field for the Cloud to hold location information
- **VISIBILITY:** For multitenant environments, sets the visibility level for Tenants outside of the one the Cloud resources are assigned to
- **TENANT:** If the visibility is set to private, this sets the Tenant the Cloud resources are assigned to
- **ENABLED:** When checked, |morpheus| will perform regular syncs with this Cloud and the Cloud will also be selectable as a provisioning target
- **AUTOMATICALLY POWER ON VMS:** Indicates whether |morpheus| should control the power state for provisioned VMs (not brownfield discovered VMs). If VMs are powered off for an unknown reason (that is, outside of |morpheus|) they will be powered back on. Leave unchecked if you wish to manage workload power state outside of |morpheus|
- **API URL:** The URL for the Nutanix Prism API, typically in a format like ``https://xx.xx.xx.xx:9440``
- **CREDENTIALS:** Choose a pre-stored username/password credential set or enter a username/password set. If entering the credentials locally, you may also choose to securely store the credentials for later use. Depending on selection, additional fields will be added to facilitate that choice
- **API VERSION:** Select the API version supported by your Nutanix environment to ensure |morpheus| is not targeting endpoints which are incompatible with your environment
- **INVENTORY EXISTING INSTANCES:** When checked, |morpheus| will automatically onboard workloads which are already running in the Nutanix environment but which were provisioned outside of |morpheus|. These may be brought under |morpheus| management at a later time, if desired
- **ENABLE HYPERVISOR CONSOLE:** When checked, enables remote console support directly to the hypervisor

In addition to these basic settings, there are also some advanced options. These are similar but not identical for every Cloud type and some of them may not appear for Nutanix Clouds.

- .. toggle-header:: :header: **Advanced Cloud Options**

    .. include:: /integration_guides/Clouds/advanced_options.rst

    |

With the above configurations made, click :guilabel:`NEXT`. Choose to add the Cloud to an existing Group or to create a new Group and click :guilabel:`NEXT` once again. Finally, review the details of the new Cloud on the REVIEW tab and click :guilabel:`COMPLETE` if all looks good. At this point the new Cloud will be added to |morpheus| and the initial Cloud sync will begin. On the Cloud list page (|InfClo|), we will see the Cloud in an "OK" status once it is ready to be consumed in |morpheus| as a provisioning target. Click into the Cloud detail page by clicking on the NAME of the Cloud from the list. Continue on to the next section for an overview of the details available on the Cloud detail.

Monitoring Nutanix Clouds
^^^^^^^^^^^^^^^^^^^^^^^^^

On clicking into the Nutanix Cloud, you'll land on the Summary tab. Here we can see high-level details including cost metrics for the month, general resource utilization information, and information on the number of hosts, workloads, and more that are currently running within the Cloud scope.

.. images:: /images/integration_guides/clouds/nutanix/cloudDetail.png

You'll also notice the Clusters tab. Here you can see and click into any Docker or Kubernetes Clusters which are running on the Nutanix Cloud. |morpheus| will see these clusters as provisioning targets themselves for containerized applications (as opposed to the Cloud itself for virtualized applications). You can also add new Kubernetes or Dockers clusters from this tab. |morpheus| includes built-in Cluster Layouts but custom Cluster Layouts can also be created. There is a guide on creating your own custom Kubernetes Cluster Layouts in the Clusters section of |morpheus| UI documentation.

On the Hosts tab, you'll see all Nutanix hypervisior hosts which are associated with the cluster. Host health metrics are viewable and we can click into individual hosts to see even greater detail on the individual host detail pages.

The VM and Containers tabs show all current VM and container workloads across the cluster. When integrating the Cloud, if you opted to inventory existing workloads, discovered resources will appear here. If not (or if there simply are none), only |morpheus|-provisioned workloads will appear here.

Provisioning New Workloads
^^^^^^^^^^^^^^^^^^^^^^^^^^

With the Cloud integrated, you're already to provision new workloads. |morpheus| comes pre-installed with a number of default library items designed to work with each supported Cloud integration type, including Nutanix. While this guide will not go through the process of using the provisioning wizard (see |ProIns| page to start), you could provision a default workload to test functionality now if desired. Additionally, |morpheus| will sync Virtual Images from Nutanix Clouds (|LibVir|) and custom Library items may be built from these images. See the Library section of |morpheus| documentation for more information on piecing together Instance Types, images, and automation scripts into cohesive and easily-consumed Library items.

Service Plans
^^^^^^^^^^^^^

|morpheus| includes a default set of Service Plans. These Service Plans can be considered akin to AWS Flavors or Openstack Flavors. They provide a means to set predefined tiers on memory, storage, and CPU cores. Price tables can also be applied to these so estimated cost per virtual machine can be tracked as well as pricing for customers. By default, these options are fixed sizes but can be configured for dynamic sizing. A service plan can be configured to allow a custom user entry for memory, storage, or cpu. To configure this, simply edit an existing Service Plan tied to Nutanix or create a new one. These all can be easily managed from the |AdmPla| section.

Docker
^^^^^^

So far, this document has covered how to add the Nutanix cloud integration and has enabled users the ability to provision virtual machine-based Instances. Another great feature provided by |morpheus| out of the box is the ability to use Docker containers and even support multiple containers per Docker host. To do this, a Docker Host must first be provisioned into Nutanix (multiple are needed when dealing with horizontal scaling scenarios). As mentioned previously, these can be viewed or created from the Clusters tab of the Cloud detail page.

To provision a Docker Host, simply navigate to the Cloud detail page or |InfClu| section. From there, click :guilabel:`+ ADD CLUSTER` to add a Nutanix Docker Host. |morpheus| views a Docker host just like any other Hypervisor with the caveat being that it is used for running containerized images instead of virtualized ones. Once a Docker Host is successfully provisioned, a green checkmark will appear to the right of the host marking it as available for use. In the event of a failure, click into the relevant host that failed and an error explaining the failure will be displayed in red at the top. Just like with VMs, |morpheus| includes default containerized items out of the box so provisioning to Docker hosts can be tested even before you've created your own container-based Library items.

Some common error scenarios include network connectivity. For a Docker Host to function properly, it must be able to resolve the |morpheus| appliance URL which can be configured in |AdmSet|. If it is unable to resolve and negotiate with the appliance, then the Agent installation will fail and provisioning instructions will not be able to be issued to the host.

Snapshots
^^^^^^^^^

|morpheus| allows the ability to create a snapshot of a Nutanix Instance.  From the Instance detail page, simply select ``Actions > Create Snapshot`` to begin creation of a new Snapshot. Existing snapshots can be viewed in the ``BACKUPS`` tab on the Instance detail page. Snapshots taken outside |morpheus| will be synced every five minutes (by default). To revert to a previous snapshot, click on the revert icon located on the right side of the Snapshot. Snapshots can be deleted by clicking on the trash can icon.

.. Note:: Access to Snapshots can be limited or removed entirely for specific user roles as needed. To edit a role's Snapshots permissions, go to |AdmRol| > (Your selected role) > Snapshots. Users can be given Full, Read-only, or No access.
