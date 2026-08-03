Install VME Manager / Worker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The **Install VME Manager** and **Install VME Worker** options deploy a Morpheus appliance VM directly on the HVM host. This is the primary deployment method on HVM OS 24.04.

.. note:: On HVM OS 26.04+, use the :doc:`/getting_started/installation/singleNode/hpe_installer` (GUI) or ``hvmcli deploy`` (CLI) instead.

Installation Fields
```````````````````

When you select **Install VME Manager** or **Install VME Worker**, the following fields are presented:

**Network Configuration:**

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - **IP Address**
     - Static IP address for the Morpheus appliance VM
   * - **Netmask**
     - Subnet mask (e.g., ``255.255.255.0``)
   * - **Gateway**
     - Default gateway for the appliance
   * - **DNS**
     - DNS server address(es)
   * - **Hostname**
     - FQDN for the appliance (e.g., ``morpheus.example.com``)

**Appliance Configuration:**

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - **Appliance URL**
     - The URL where Morpheus will be accessible (e.g., ``https://morpheus.example.com``)
   * - **Admin Username**
     - Administrator username for the appliance
   * - **Admin Password**
     - Administrator password (entered twice for confirmation)
   * - **Image URI**
     - Path or URL to the QCOW2 image (``file://`` for local, ``http://``/``https://`` for remote)
   * - **VM Size**
     - Virtual machine sizing (memory and CPU allocation)
   * - **Management Interface**
     - The host network interface to use for the management bridge

**Compute Network (Optional):**

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - **Compute Interface**
     - Host NIC for the compute network (VM traffic)
   * - **Compute VLAN**
     - VLAN tag for compute network traffic (optional)

**Worker-Only Fields (Install VME Worker):**

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - **Worker URL**
     - The URL where the worker will be accessible
   * - **Worker Key**
     - The distributed worker API key from the Morpheus Manager
   * - **API Key**
     - The API key for worker-to-manager authentication

**Proxy Settings (Optional):**

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - **Proxy**
     - HTTP proxy URL (e.g., ``http://proxy.example.com:8080``)
   * - **No Proxy**
     - Comma-separated list of addresses that bypass the proxy

Deployment Process
``````````````````

Once all fields are validated and you confirm the installation, ``hpe-vm`` performs the following steps:

1. **Prepare KVM** — Configures libvirt, enables nested KVM, and adjusts host settings
2. **Create management bridge** — Builds an OVS bridge and defines the ``Management`` virsh network on the selected interface
3. **Create local storage pool** — Creates a libvirt storage pool if one does not already exist
4. **Configure compute network** (if specified) — Defines the ``Compute`` virsh network with optional VLAN portgroups
5. **Download QCOW2 image** — Downloads or copies the appliance image to ``/var/lib/libvirt/images/``
6. **Build cloud-init ISO** — Generates a cloud-init configuration ISO with network settings, hostname, and appliance credentials
7. **Define virtual machine** — Creates the libvirt VM definition (XML domain)
8. **Start virtual machine** — Boots the VM
9. **Wait for services** — Polls the appliance URL until the Morpheus web application responds
10. **Clean up** — Removes temporary cloud-init artifacts

.. tip:: The deployment typically takes 10–20 minutes depending on image size and host performance.

Validation
``````````

Before installation begins, ``hpe-vm`` validates:

- All required fields are populated
- IP address, netmask, and gateway are valid formats
- URL fields are properly formatted
- Passwords match (entered twice)
- Host has sufficient memory for the selected VM size
- Image file exists (for ``file://`` URIs)
- Management interface exists on the host
- VLAN tag is numeric (1–4094) if specified
- DNS can resolve the hostname (warning if mismatch)

If any validation fails, the installer highlights the problematic field and displays an error message.

Post-Deployment
```````````````

On successful deployment:

- **Manager install**: The console displays the appliance URL. Open it in a browser to complete Morpheus setup.
- **Worker install**: The console reports the worker is deployed and connected to the manager.

If the deployment fails, review the error message displayed in the console. Host-side logs are available at ``/var/log/`` for troubleshooting.
