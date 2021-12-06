KVM
---

Overview
^^^^^^^^

|morpheus| KVM is a powerful, cheaper alternative to virtualization compared with other hypervisor offerings. It is also very capable of setting up complex shared storage and multiple networks across many hosts. This guide goes over the process for onboarding brownfield KVM clusters and for provisioning new KVM clusters directly from |morpheus|. When created or onboarded, KVM clusters are associated with the chosen Cloud and can then be selected as provisioning targets using existing Instance types and automation routines. In this example, baremetal KVM hosts are added to a |morpheus|-type Cloud but similar combinations can be made with other Cloud types.

Requirements
````````````

At this time, |morpheus| primarily supports CentOS 7 and Ubuntu-based KVM clusters. When creating KVM clusters directly in |morpheus| these are the two base OS options. It's possible to onboard KVM clusters built on other Linux distributions, such as SUSE Linux but the user would need to ensure the correct packages were installed. The required packages are listed below.

- kvm
- libvirt
- virt-manager
- virt-install
- qemu-kvm-rhev
- genisoimage

Additionally, |morpheus| will attempt to add a new network switch called 'morpheus' and storage pool when onboarding a brownfield KVM host.

When creating new clusters from |morpheus|, users simply provide a basic Ubuntu or CentOS box. |morpheus| takes care of installing the packages listed above as well as |morpheus| Agent if desired.

Creating the Cloud
^^^^^^^^^^^^^^^^^^

|morpheus| doesn't include a KVM-specific Cloud type. Instead, other Cloud types (either pre-existing or newly created) are used and KVM clusters are associated with the Cloud when they are onboarded or created by |morpheus|. For example, a generic |morpheus|-type Cloud could be created to associate with baremetal KVM clusters. Similarly, brownfield VMware KVM hosts could be onboarded into an existing VMware vCenter Cloud. Other combinations are possible as well. In the example in this section, a |morpheus| Cloud will be created and KVM hosts will be associated with it to become |morpheus| provisioning targets.

A |morpheus|-type cloud is a generic Cloud construct that isn't designed to hook into a specific public or private cloud (such as VMware or Amazon AWS). Before onboarding an existing KVM host or creating one via |morpheus| UI tools, create the Cloud:

#. Navigate to |InfClo|
#. Click :guilabel:`+ ADD`
#. Select the |morpheus| Cloud type and click :guilabel:`NEXT`
#. On the Configure tab, provide: A name, Tenant visibility settings, and select "Automatically Power On VMs" if you want |morpheus| to handle the power state of your VMs. Additionally, select "Inventory Existing Instances" if |morpheus| should automatically discover existing VMs on your KVM hosts
#. On the Group tab, create a new Group or associate this Cloud with an existing Group. Click :guilabel:`NEXT`
#. After reviewing your configuration, click :guilabel:`COMPLETE`

.. image:: /images/integrations_guides/clouds/kvm/createCloud.png
  :width: 50%

Onboard an Existing KVM Cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With the Cloud created, we can add existing KVM hosts from the Cloud detail page (|InfClo| > Selected Cloud). From the Hosts tab, open the ADD HYPERVISOR menu and select "Brownfield Libvirt KVM Host".

On the first page of the Create Host modal, enter a name for the onboarded KVM host in |morpheus|. Click :guilabel:`NEXT`. On the following page, enter the IP address for your host in addition to an SSH username and password for the host box. It's recommended that you also copy the revealed SSH public key into your authorized_hosts file. Click :guilabel:`NEXT`.

.. image:: /images/integration_guides/clouds/kvm/onboardHost.png
  :width: 80%

On the Automation tab, select any relevant automation workflows and complete the modal. The new KVM host will now be listed on the host tab along with any other KVM hosts (if any) you may have associated with this Cloud. If the Cloud is configured to automatically onboard existing instances, any VMs you may have running will be automatically discovered by |morpheus| with each Cloud sync (approximately every five minutes by default). For VMs, you will see these listed on the VMs tab of the Cloud detail page and they will also be listed among all other VMs that |morpheus| is aware of on the VMs list page at |InfComVir|.

Create a KVM Cluster
^^^^^^^^^^^^^^^^^^^^

Out of the box, |morpheus| includes layouts for KVM clusters. The default layouts are Ubuntu or CentOS 7-based and include one host. Users can also create their own KVM cluster layouts either from scratch or by cloning a default KVM cluster layout and making changes. Custom cluster layouts can include multiple hosts, if desired. See |morpheus| documentation on `cluster layouts <https://docs.morpheusdata.com/en/latest/library/blueprints/clusterLayouts.html>`_ for more information.

When creating KVM clusters, you'll need the Ubuntu or CentOS 7 box(es) standing but don't need to worry about installing any additional packages on your own. |morpheus| will handle that as part of the cluster creation. Complete the following steps to create a connection into your existing machines, provision a new KVM cluster, and associate it to the KVM Cloud created in an earlier section:

#. Navigate to |InfClu|
#. Click :guilabel:`+ ADD CLUSTER` and select KVM Cluster
#. Choose a Group on the Group tab
#. Select the Cloud created earlier from the Cloud dropdown menu, then provide at least a name for the cluster and a resource name on the Name tab
#. On the Configure tab, set the following options:

    - **LAYOUT:** Select a default KVM cluster layout or a custom layout
    - **SSH HOSTS:** Enter a name for this host and the machine address, click the plus (+) button at the end of the row to add additional hosts to the cluster
    - **SSH PORT:** The port for the SSH connection, typically 22
    - **SSH USERNAME:** The username for an administrator user on the host box(es)
    - **SSH PASSWORD:** The password for the account in the previous field
    - **SSH KEY:** Select a stored SSH keypair from the dropdown menu
    - **LVM ENABLED:** Mark if the destination box has LVM enabled
    - **DATA DEVICE:** If "LVM ENABLED" is marked, this field is available. The indicated logical volume will be added to the logical volume group if it doesn't already exist
    - **SOFTWARE RAID?:** Mark to enable software RAID on the host box
    - **NETWORK INTERFACE:** Select the interface to use for the Open vSwitch Bridge

#. Click :guilabel:`NEXT` to finish configuration, then complete the modal after final review

.. image: /images/integration_guides/clouds/kvm/createCluster.png
  :width: 80%

After adding the new cluster, you will see your newly created hosts listed on the Host Tab of the KVM Cloud detail page (|InfClo| > Selected KVM Cloud).

Provisioning to KVM
^^^^^^^^^^^^^^^^^^^

With the Cloud and hosts available, users can now provision to the KVM host using custom Instance Types and automation routines built in the |morpheus| library. To provision a new Instance, navigate to |ProIns| and click :guilabel:`+ ADD`. Select the Instance Type to provision, and click :guilabel:`NEXT`. Choose a Group that the KVM Cloud lives in and select the Cloud. Provide a name for the new Instance if a naming policy doesn't already give it a name under current configurations. Click :guilabel:`NEXT` to advance to the Configuration tab. The fields here will differ based on the Instance Type and Layout used but in the example case, selections have been made for:

- **Layout:** Single KVM VM
- **Resource Pool:** The selected KVM cluster
- **Volumes:** Configure the needed volumes and the associated datastore for each
- **Networks:** The KVM network the VM(s) should belong to
- **Host:** The selected host the VM(s) should be provisioned onto

Complete the remaining steps to the provisioning wizard and the new KVM Instance will be created.

.. image:: /images/integration_guides/clouds/kvm/provisioning.png
  :width: 50%

.. include:: vlans.rst
