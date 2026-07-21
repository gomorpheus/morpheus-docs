Windows VM Domain Join
======================

This guide covers the end-to-end workflow for deploying Windows VMs on HVM clusters with automatic Active Directory domain join. The process uses |morpheus| guest customization to join the domain during initial VM provisioning without manual intervention.

Prerequisites
-------------

Before configuring automatic domain join, ensure:

- An Active Directory domain controller is reachable from the provisioned VM's network
- DNS on the target network can resolve the domain name (the VM must be able to find the DC via DNS)
- A **service account** with permissions to join computers to the domain (and optionally create computer objects in a specific OU)
- A Network Domain is configured in |morpheus| (see below)
- The Windows virtual image uses sysprep-based customization

Configuring the Network Domain
-------------------------------

Network Domains in |morpheus| define the Active Directory domain and credentials used for automatic domain join.

#. Navigate to :menuselection:`Infrastructure --> Network --> Domains`
#. Click :guilabel:`+ Add`
#. Configure the domain:

   .. list-table::
      :widths: 25 75
      :header-rows: 1

      * - Field
        - Description
      * - Name
        - Display name for this domain configuration
      * - Domain Name
        - The FQDN of the Active Directory domain (e.g., ``corp.example.com``)
      * - Domain Controller
        - Enable to use this domain for automatic domain join during provisioning
      * - Username
        - Domain join service account in ``DOMAIN\username`` or ``username@domain.com`` format
      * - Password
        - Password for the service account
      * - OU Path
        - (Optional) Distinguished Name of the OU where computer objects are created (e.g., ``OU=Servers,OU=HVM,DC=corp,DC=example,DC=com``)
      * - DC Server
        - (Optional) Specific domain controller hostname or IP. If blank, the VM will locate a DC via DNS SRV records.

#. Click :guilabel:`Save`

Associating Domain with a Network
-----------------------------------

The Network Domain must be associated with the network(s) where Windows VMs will be provisioned:

#. Navigate to :menuselection:`Infrastructure --> Network --> Networks`
#. Edit the target network
#. In the **Domain** field, select the Network Domain configured above
#. Click :guilabel:`Save`

When a VM is provisioned on a network that has a Domain with **Domain Controller** enabled, |morpheus| automatically performs domain join during guest customization.

Windows Image Requirements
---------------------------

The Windows virtual image must support guest customization. Prepare the image using sysprep with **Force Guest Customization** enabled:

#. Prepare the Windows template (install updates, VirtIO drivers, etc.)
#. Run sysprep with ``/generalize /oobe /shutdown``
#. Upload as a Virtual Image in |morpheus|
#. Enable **Is Force Customization** on the Virtual Image settings

Domain Join Trigger
--------------------

Domain join is triggered based on the **Network Domain** selection. The domain can be assigned at multiple levels, with more specific settings taking precedence:

- **At the Cloud level** — A default Network Domain can be set on the Cloud configuration. This applies to all VMs provisioned into that Cloud unless overridden at a more specific level.
- **At the Network level** — A Network Domain can be associated with a specific network. VMs provisioned onto that network inherit the domain assignment.
- **At the VM level during provisioning** — The domain can be explicitly selected or overridden per-VM in the provisioning wizard, regardless of Cloud or Network defaults.

The most specific assignment wins: VM-level overrides Network-level, which overrides Cloud-level.

The domain selection determines which AD domain, credentials, OU, and DC server are used for the join operation.

How Domain Join Works
----------------------

When a Windows VM is provisioned with a Network Domain that has **Domain Controller** enabled:

#. |morpheus| provisions the VM and waits for the guest agent to become responsive
#. The guest customization sets the hostname (from the Instance name)
#. |morpheus| executes a domain join script via the guest agent:

   - Decodes the domain credentials
   - Creates a PSCredential object
   - Runs ``Add-Computer`` with the domain name, credentials, OU path, and optionally a specific DC server
   - Renames the computer to the configured hostname

#. The VM reboots to complete domain join
#. |morpheus| verifies the join was successful

The join operation retries up to 3 times for transient AD errors (replication delays, temporary DC unavailability).

Provisioning a Domain-Joined VM
---------------------------------

#. Navigate to :menuselection:`Provisioning --> Instances` and click :guilabel:`+ Add`
#. Select a Windows Instance Type
#. On the CONFIGURE tab:

   - Select a network that has the domain association
   - The domain join will happen automatically — no additional configuration is needed

#. Complete the provisioning wizard

After provisioning, the VM will appear as a computer object in Active Directory in the configured OU.

Troubleshooting
----------------

Domain Join Fails — "Cannot contact domain controller"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Verify DNS resolution on the VM's network. The VM must resolve the AD domain name to a DC IP.
- If using a specific DC Server in the domain config, ensure the VM can reach that IP on port 389 (LDAP) and 88 (Kerberos).
- Check that no firewall rules block the VM from communicating with the DC.

Domain Join Fails — "Access denied"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Verify the service account credentials in the Network Domain configuration.
- Ensure the service account has "Join computers to the domain" permission.
- If using a specific OU, verify the account has "Create Computer Objects" permission in that OU.

Hostname Not Applied After Join
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In rare cases, the domain join succeeds but the hostname rename does not take effect on the first attempt. |morpheus| will retry ``Rename-Computer`` separately. If the hostname still does not match after provisioning, verify:

- The computer name does not exceed 15 characters (NetBIOS limit)
- No conflicting computer object with the same name exists in AD

VM Joins But Shows "Unknown" in AD Sites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Ensure AD Sites and Services has a subnet entry that covers the VM's IP range
- The VM will be associated with the correct site on next group policy refresh
