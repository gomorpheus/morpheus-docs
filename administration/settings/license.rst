Overview
^^^^^^^^

|morpheus| requires a valid license for provisioning new Instances, Apps and Hosts, and converting existing Instances and Hosts to managed. Licenses can be applied and updated in this section, and the current license status can be checked.

The limits shown on the License page depend on the applied license. Current standard licenses can include a socket limit. Older licenses can instead use workload element (WLE), managed RAM, storage, Host, or HVM-specific limits. The rules in `Socket Consumption`_ describe the current standard socket limit; they do not replace the terms of the applicable license agreement.

.. NOTE:: The appliance License page controls the |morpheus| product license and capacity limits. It is different from the :ref:`provisioning_licenses` section, which stores third-party software license keys for application to provisioned Instances.

Current Licenses and Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^

If a License Key has already been applied, the License page shows the installed license, its effective dates, and each limit encoded in the license. When multiple compatible licenses are installed, the page also shows the effective stacked license.

Tenant Name
  Company name the License was generated for.
Start Date
  Date and time the current License started.
End Date
  Date and time the current License expires.
Usage
  Used and available capacity for the limits encoded in the License. For a standard socket license, expand the Sockets usage details to view Host Sockets, Private Cloud VM Sockets, and Public Cloud VM Sockets.

The License page is the source for the appliance's calculated usage. Contact your account team if the displayed limits differ from your license agreement or if you need help interpreting contractual entitlements.

.. NOTE:: Once a current License expires or reaches a hard limit, users can no longer provision resources governed by that limit or convert additional resources to managed. |morpheus| otherwise continues to function.

Socket Consumption
^^^^^^^^^^^^^^^^^^

For a current standard socket license, total socket usage is the sum of:

* Physical sockets on qualifying private Cloud Hosts
* VM-derived sockets for public Cloud VMs
* VM-derived sockets for private Cloud VMs only when their Cloud has no qualifying inventoried Host

The VM-derived rate is 15 VMs per socket. The appliance can calculate fractional usage when the VM count is not an exact multiple of 15; use the value shown on the License page rather than estimating how a fraction is displayed.

.. list-table:: Socket consumption by resource type
   :widths: 30 20 50
   :header-rows: 1

   * - Resource
     - Socket consumption
     - Calculation
   * - Physical hypervisor, container hypervisor, or bare metal Host in a private Cloud
     - Yes
     - Uses the Host's reported physical socket count. If no socket count is reported, the Host consumes two sockets.
   * - Duplicate inventory record for the same physical private Cloud Host
     - No additional sockets
     - Records that share the same unique Host identifier are counted once.
   * - Guest VM in a private Cloud with qualifying inventoried Hosts
     - No additional sockets
     - The underlying Hosts already consume their physical sockets, so their guest VMs are not counted again.
   * - VM in a private Cloud without qualifying inventoried Hosts
     - Yes
     - The appliance divides the number of VMs by 15 to calculate VM-derived sockets.
   * - VM in a public Cloud
     - Yes
     - The appliance divides the number of VMs by 15 to calculate VM-derived sockets.
   * - Virtual HKS control plane or worker node on VMware
     - No additional sockets
     - When the VMware Hosts are inventoried and counted, the HKS nodes are guest VMs and do not consume sockets again.
   * - Bare metal HKS worker Host
     - Yes
     - Uses the worker Host's reported physical sockets, or two sockets when no value is reported.
   * - Controller, Kubernetes master, guest Host, or nested child Host record
     - No physical Host sockets
     - These records are excluded from the qualifying private Cloud Host count. Their underlying physical Hosts can still consume sockets.

This accounting prevents double counting in a private Cloud. For example, virtual HKS nodes running on VMware do not consume an HKS socket allocation in addition to the physical sockets already consumed by the VMware Hosts.

Socket Consumption Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Virtual HKS on VMware
  A VMware Cloud contains three inventoried Hosts with two physical sockets each. The Hosts consume six sockets total. An HKS cluster runs three control plane VMs and six worker VMs on those Hosts. The nine HKS guest VMs consume zero additional sockets, so total socket usage remains six.

Bare Metal HKS
  An HKS cluster contains four qualifying bare metal worker Hosts with two physical sockets each. The workers consume eight sockets total. Kubernetes master records are excluded from the physical Host count. If a qualifying worker does not report its socket count, |morpheus| counts two sockets for that worker.

Public Cloud VMs
  Thirty VMs in a public Cloud consume two VM-derived sockets: ``30 / 15 = 2``.

Private Cloud VMs without inventoried Hosts
  Thirty VMs in a private Cloud with no qualifying inventoried hypervisor or bare metal Hosts consume two VM-derived sockets: ``30 / 15 = 2``. If qualifying Hosts are later inventoried for that Cloud, their physical sockets are counted and their guest VMs are no longer counted separately.

Legacy License Limits
^^^^^^^^^^^^^^^^^^^^^

Older licenses can use a different limit model. Depending on the applied License, the License page can show workload elements, managed RAM, storage, Hosts, or a separate HVM socket limit instead of the current standard socket limit. Do not combine limits from different models when estimating usage. The values and usage shown on the License page identify the model active on the appliance.

For information about WLE-based licensing, see the `Workload Element Knowledge Base article <https://support.morpheusdata.com/s/article/What-is-a-Workload-Element-or-WE-for-purposes-of-Morpheus-licensing?language=en_US>`_.

Upgrade License Key
^^^^^^^^^^^^^^^^^^^

To add a new or update an existing License:

#. Copy the License Key into the License Key field
#. Click `UPDATE`

If valid, the new License will be applied.

Request new License
^^^^^^^^^^^^^^^^^^^

Licenses can be requested at https://app.morpheushub.com or by contacting your account team.
