KVM
---

Overview
^^^^^^^^

|morpheus| KVM is a powerful, cheaper alternative to virtualization compared with other hypervisor offerings. It is also very capable of setting up complex shared storage and multiple networks across many hosts. This guide goes over the process for onboarding brownfield KVM clusters. When onboarded, KVM clusters are associated with the chosen Cloud and can then be selected as provisioning targets using existing Instance types and automation routines. In this example, baremetal KVM hosts are added to a |morpheus|-type Cloud but similar combinations can be made with other Cloud types.

Requirements
````````````

When onboarding KVM clusters, the user must ensure the correct packages are installed. The required packages are listed below:

- kvm
- libvirt
- virt-manager
- virt-install
- qemu-kvm-rhev
- genisoimage

Additionally, |morpheus| will attempt to add a new network switch called 'morpheus' and storage pool when onboarding a brownfield KVM cluster. |morpheus| detects that virsh is installed and, when present, it will treat it as a brownfield KVM host. Brownfield KVM hosts must have:

- libvirt and virsh installed
- A pool called morpheus-images defined as an image cache and ideally separate from the main datastore
- A pool called morpheus-cloud-init defined which stores small disk images for bootup (this pool can be small)

.. NOTE:: |morpheus| uses a "morpheus-images" pool which is separate from the main datastore. This is a host-local image cache which facilitates faster clone operations. The cache will automatically purge images once the allocation reaches 80% to avoid filling completely. Once it is 80% full, the oldest accessed volumes in the cache will be deleted first until the cache is under 50% full once again.

Creating the Cloud
^^^^^^^^^^^^^^^^^^

|morpheus| doesn't include a KVM-specific Cloud type. Instead, other Cloud types (either pre-existing or newly created) are used and KVM clusters are associated with the Cloud when they are onboarded or created by |morpheus|. For example, a generic |morpheus|-type Cloud could be created to associate with baremetal KVM clusters. Similarly, brownfield VMware KVM hosts could be onboarded into an existing VMware vCenter Cloud. Other combinations are possible as well. In the example in this section, a |morpheus| Cloud will be created and KVM hosts will be associated with it to become |morpheus| provisioning targets.

A |morpheus|-type cloud is a generic Cloud construct that isn't designed to hook into a specific public or private cloud (such as VMware or Amazon AWS). Before onboarding an existing KVM host or creating one via |morpheus| UI tools, create the Cloud:

#. Navigate to |InfClo|
#. Click :guilabel:`+ ADD`
#. Select the |morpheus| Cloud type and click :guilabel:`NEXT`
#. On the Configure tab, provide:

    - **NAME:** A name for the new Cloud
    - **VISIBILITY:** Clouds with Public visibility will be accessible in other Tenants (if your appliance is configured for multitenancy)
    - **Automatically Power On VMs:** Mark this box for |morpheus| to handle the power state of VMs
    - **Inventory Existing Instances:** If marked, |morpheus| will automatically onboard VMs from any KVM hosts associated with this Cloud

#. On the Group tab, create a new Group or associate this Cloud with an existing Group. Click :guilabel:`NEXT`
#. After reviewing your configuration, click :guilabel:`COMPLETE`

.. image:: /images/integration_guides/clouds/kvm/createCloud.png
  :width: 50%

Onboard an Existing KVM Cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With the Cloud created, we can add existing KVM hosts from the Cloud detail page (|InfClo| > Selected Cloud). From the Hosts tab, open the ADD HYPERVISOR menu and select "Brownfield Libvirt KVM Host".

On the first page of the Create Host modal, enter a name for the onboarded KVM host in |morpheus|. Click :guilabel:`NEXT`. On the following page, enter the IP address for your host in addition to an SSH username and password for the host box. It's recommended that you also copy the revealed SSH public key into your authorized_hosts file. Click :guilabel:`NEXT`.

.. image:: /images/integration_guides/clouds/kvm/onboardHost.png
  :width: 80%

On the Automation tab, select any relevant automation workflows and complete the modal. The new KVM host will now be listed on the host tab along with any other KVM hosts (if any) you may have associated with this Cloud. If the Cloud is configured to automatically onboard existing instances, any VMs you may have running will be automatically discovered by |morpheus| with each Cloud sync (approximately every five minutes by default). For VMs, you will see these listed on the VMs tab of the Cloud detail page and they will also be listed among all other VMs that |morpheus| is aware of on the VMs list page at |InfComVir|.

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
