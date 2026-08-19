OpenShift Clusters |enterprise-only|
=====================================

.. tier-note:: Enterprise
   :exclude: Essentials, Advanced

   OpenShift cluster integration is an Enterprise-only feature.

Overview
^^^^^^^^

The OpenShift integration adds a new Cluster type, which can be added to |morpheus| from the Clusters list page (:menuselection:`Infrastructure --> Clusters`). Once a pre-existing OpenShift cluster is integrated, |morpheus| can onboard any currently-running virtualized workloads along with the cluster hosts, network objects, storage objects, and virtual images needed to provision additional virtualized workloads.

In addition to a new Cluster type, the OpenShift integration adds a new Instance Type to the provisioning wizard, which is used to provision new Instances to any integrated Clusters.

The OpenShift integration is developed as a standalone plugin for |morpheus| and is not part of the product by default. Information on accessing the plugin and adding it to the |morpheus| appliance is included in a subsequent section.

.. NOTE:: The OpenShift integration with |morpheus| is currently limited to support of virtualized workloads only. There is not currently support for container-based workloads.

Prerequisites
^^^^^^^^^^^^^

- |morpheus| appliance running version 8.0.13 or higher
- At least one pre-existing OpenShift 4.x cluster, which can communicate back to the |morpheus| appliance on the HTTPS port
- Access to a full administrator account for each cluster which will be integrated
- Ability for the |morpheus| appliance to communicate with the OpenShift API on port 6443
- Ability for the |morpheus| appliance to communicate with each provisioned VM on port 22 for SSH and on port 3389 for Windows RDP

Features
^^^^^^^^

- Adds a new Cluster type, which is used to onboard pre-existing OpenShift clusters into |morpheus|
- Enables inventory synchronization for workloads provisioned outside of |morpheus| in the OpenShift console
- Monitor high-level cluster health details such as host numbers, alarms, and high CPU, memory or disk use situations
- Monitor individual host and VM health details such as high CPU, memory, disk use, or network I/O situations
- Onboard network objects, device-agnostic storage objects, and virtual images to enable OpenShift provisioning from the |morpheus| provisioning wizard UI
- Supports IPv4 and IPv6 networking
- Adds new Instance Type to the |morpheus| provisioning wizard for easy provisioning of new OpenShift virtualized workloads
- VM provisioning supports the use of existing templates and service plans
- Interface with Morpheus-type IP Pools or IP Pools sourced from IPAM integrations throughout the lifecycle of OpenShift workloads
- Utilize the |morpheus| automation engine for provisioning and for day two operations across the Instance lifecycle
- Supports |morpheus| labels and tagging features for resource organization
- Provides guest console access into OpenShift-hosted virtual machines

Adding the OpenShift Plugin
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The OpenShift integration is developed as a standalone plugin for |morpheus|, which is not included in the product by default.

#. To download the plugin, navigate to the plugin share site (share.morpheusdata.com) and browse or search for the OpenShift plugin
#. With the plugin downloaded to your workstation, navigate to the plugins list page (|AdmIntPlu|) in |morpheus| UI
#. Click :guilabel:`Add`
#. Browse for the plugin JAR or drag and drop it onto the target
#. Click :guilabel:`Upload`

After a few brief moments, the new plugin will be added. This plugin adds a new Cluster type, which can be added from the Clusters list page (:menuselection:`Infrastructure --> Clusters`) and also adds a new Instance Type which can be provisioned from the Instance provisioning wizard once a compatible cluster is integrated.

Adding OpenShift Clusters
^^^^^^^^^^^^^^^^^^^^^^^^^

.. NOTE:: Adding an OpenShift cluster requires a pre-existing Group and Private Cloud-type Cloud. See Groups and Clouds documentation elsewhere in this user manual for more details on those constructs.

To onboard an OpenShift cluster, begin by collecting an API token and API URL from OpenShift. Bear in mind the integration user with |morpheus| must be a full administrator user.

#. Log into the OpenShift console
#. In the far top-right of the application window, click on the name of the logged in user to expand a small dropdown menu
#. Click "Copy login command"
#. Click "Display Token"
#. On the resulting screen, both the API URL and the API token can be copied. You will need to enter these values directly into the "Add Cluster" modal within |morpheus| in the next step

With the authentication details available, head back to |morpheus| to add a new OpenShift cluster:

#. Navigate to :menuselection:`Infrastructure --> Clusters`
#. Click :guilabel:`+ Add Cluster`
#. Select "RED HAT OPENSHIFT CLUSTER" and click :guilabel:`Next`
#. On the Group tab, select the |morpheus| Group to associate with the cluster and click :guilabel:`Next`
#. On the Name tab, you must at least configure a "Cluster Name" attribute and select a Cloud. The "Cluster Name" is a friendly name to identify the OpenShift cluster in |morpheus|. The Cloud configuration requires you to select a pre-existing Private Cloud-type Cloud. There are optional configurations here as well, such as applying Labels or adding a description
#. On the Configure tab, select the Layout that corresponds closest to the version of OpenShift running on the cluster. Integration with |morpheus| requires OpenShift version 4.x at minimum. On this tab, you'll also enter the API URL and service token collected earlier. If "Inventory Existing Instances" is checked, |morpheus| will automatically onboard any virtualized workloads which are currently running on the cluster and any that are provisioned directly from the OpenShift console in the future. Click :guilabel:`Next`
#. On the Review tab, click :guilabel:`Complete`
#. Within a short time, the new OpenShift cluster will appear on the clusters list page alongside any other cluster that may currently be running

Monitoring the Cluster
^^^^^^^^^^^^^^^^^^^^^^

After onboarding the cluster into |morpheus|, a new Cluster object is added to the Clusters list page. Clicking into the Cluster reveals the Cluster detail page. Note the following subtabs and the cluster details we can monitor in each:

- **Nodes:** Master and worker nodes making up the cluster are shown here. Click into any of them to see a node detail page
- **VMs:** A list of all virtual machines within the scope of the OpenShift cluster are shown. When creating or editing the cluster, an option is given to inventory all existing instances. If selected, all running virtual machines will be onboarded and shown here even if they were provisioned outside of |morpheus|. If this option is not selected, then only the OpenShift virtual machines provisioned through |morpheus| are shown. High level details about each virtual machine are also shown, such as power state and resource usage. Click into any virtual machine to see a detail page with additional options
- **Virtual Images:** A list of virtual images synced to |morpheus| is shown. For provisioning, create an OpenShift VirtualMachine template whose source is an existing PersistentVolumeClaim (PVC). The plugin synchronizes PVC-backed user templates as Virtual Images; the OpenShift default image catalog is not synchronized. Click into a synced image to review its configuration before use

.. IMPORTANT:: Virtual Images used for provisioning OpenShift workloads from |morpheus| must be updated to set appropriate properties prior to use. Edit the Virtual Image to uncheck the "Install Agent?" configuration and check either "Is Cloud Init Enabled?" or "Sysprepped/Generalized Image" depending on the workload-type. Ensure the OpenShift template has VirtIO drivers and QEMU VM agent tools installed. For Windows images, only the "Sysprepped/Generalized Image" option is currently supported. Do not use the Cloudbase-init option until support is added. For Linux-based images, |morpheus| expects standardized NIC names (eth0, eth1, etc) on templates so that cloud-init can reliably apply network configuration. For Windows templates, |morpheus| relies on OpenShift standard interface naming (ex. Ethernet Instance 0) in templates. Currently on Windows Instances, configuration of the first network interface is supported as part of deployment via Sysprep.

- **Networks:** NetworkAttachmentDefinitions (NADs) define virtual network interfaces that can be attached to VMs, acting as network bridges

.. IMPORTANT:: Edit and update synced network objects (OpenShift NADs) in |morpheus| with appropriate IPv4/IPv6 configuration details (DHCP, Gateway, DNS, Subnet, etc.)

.. TIP:: IP Pools can be associated with the network definitions synced from OpenShift. These can be Morpheus-type IP Pools created within the |morpheus| UI or can be IP Pools sourced from IPAM integrations. If IP Pools are used, |morpheus| can manage IP addresses across the Instance lifecycle (claim a free address at provision time, release an address at teardown, etc).

Provisioning into OpenShift
^^^^^^^^^^^^^^^^^^^^^^^^^^^

In addition to adding a new cluster type (as covered in the previous sections), the |morpheus| OpenShift plugin also adds the "OpenShift" Instance Type to the provisioning wizard. Through this, new virtualized Instances can be provisioned to the OpenShift cluster. Use the following steps to provision a new virtual machine into the cluster.

#. Navigate to :menuselection:`Provisioning --> Instances`
#. Click :guilabel:`+ ADD`
#. Select OPENSHIFT and click :guilabel:`NEXT`
#. On the Group tab, select a Group and Cloud. These selections will be filtered to include only Groups which can access Clouds that contain OpenShift clusters
#. Still on the Group tab, provide a Name for the new Instance and click :guilabel:`NEXT`
#. On the Configure tab, set the following configurations:

   - **Layout:** The "Openshift VM" Layout is included by default. Additional Layouts can be created within the Blueprints section (|LibBluLay|) by selecting the "Openshift" Layout technology and associating the Layout with the "Openshift" Instance Type. See the Blueprints section of this user manual for more information on building Library items
   - **Plan:** Plans of various sizes and levels of customizability can be created in |AdmPla|. By default, a single Plan specifying 2 CPU cores and 4 GB memory is seeded when adding the plugin
   - **Resource Pool:** Select the desired OpenShift cluster
   - **Volumes:** Select the proper number and size volumes
   - **Networks:** Networks correspond to NetworkAttachedDefinitions (NADs) in OpenShift. This list includes all NADs and names them by "<namespace>/<NAD name>" to make it easier to select a network within the intended namespace (Project). Users may select multiple NADs while provisioning but they must be from the same namespace

   .. IMPORTANT:: The first network interface chosen as part of Instance deployment will be treated as the primary interface and is expected to be reachable from the |morpheus| appliance.

   - **Image:** Select from the synchronized Virtual Images. To provision an OpenShift VM, first create a VirtualMachine template in OpenShift whose source is an existing PVC. The plugin synchronizes templates created this way; it does not synchronize the OpenShift default image catalog
   - **Project:** Select the proper namespace. Bear in mind it's currently up to the user to select a valid namespace based on the network selected. If you choose an invalid namespace for the chosen network, provisioning will fail. In the future, this select list may provide automatic filtering to prevent invalid configuration but, for now, the user must make a valid selection

   .. important:: Template scheduling and image synchronization behavior is supplied by the installed OpenShift plugin and can vary by plugin/OpenShift version. Validate the template against the compatibility information shipped with that plugin. If the template includes ``nodeSelector`` labels, OpenShift considers only matching nodes during VM scheduling. Every NAD/network selected in |morpheus| must be available, with compatible attachment configuration, on **all** nodes eligible under that selector. A selector that matches no ready node, or a network absent from any eligible node, can cause provisioning or scheduling to fail. Verify the selector, node labels, NAD namespace, and network availability in OpenShift before retrying; do not remove placement constraints merely to bypass the error.

#. Still on the Configure tab, other configurations common to many Instance Types can also be made. When finished, click :guilabel:`NEXT`
#. On the Automation tab, choose to run automation Tasks or associate Workflows with the new Instance. Other common automation configurations can also be made, such as scale or backup configurations. Click :guilabel:`NEXT`
#. On the Review tab, click :guilabel:`COMPLETE`

The new OpenShift VM will soon be running based on the configurations given. Its status can be monitored from the OpenShift cluster detail page discussed in the previous section or from the Instances list page.

.. NOTE:: Instance/VM console access is only supported if the VM is available on the network and reachable by |morpheus| over the SSH port for Linux or the RDP port for Windows.
