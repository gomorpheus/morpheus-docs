Deploying Morpheus with the HPE Installer (Recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The HPE Morpheus Manager Installer is a graphical wizard that deploys Morpheus Enterprise or VM Essentials to an HPE HVM host in minutes. It handles the entire deployment process including image upload, VM creation, network configuration, and post-deployment verification.

The installer is available on the HVM ISO file in two versions:

- **macOS**: ``Morpheus_Manager_Installer-x64-<version>.dmg``
- **Windows**: ``Morpheus_Manager_Installer-x64-<version>.zip``

.. note:: The deployment process typically takes 15–30 minutes depending on image size and network speed. No internet access is required — the installer works entirely over your local network.

Prerequisites and Assumptions
`````````````````````````````

Before using the installer, ensure the following:

- Each HVM host has an IP address, netmask, and gateway already configured
- You have SSH access (port 22) to the target HVM host from your workstation
- You have HTTPS access (port 443) to the HVM host for post-deployment verification
- The SSH user has sudo privileges to run ``virsh``, ``hvmcli``, and manage HVM resources
- You have the HPE VM Essentials QCOW2 image ready (available on the HVM ISO or as an HTTP URL)
- You know the network configuration details (IP address, netmask, gateway, and DNS) for the Morpheus VM

Starting the Installer
``````````````````````

1. Mount or extract the HVM ISO file on your workstation
2. Locate the installer for your platform:

   - **macOS**: Open the ``.dmg`` file and launch the HPE Morpheus Manager Installer application
   - **Windows**: Extract the ``.zip`` file and run the installer executable

3. The installer opens with the **Prerequisites** screen

Step 1: Prerequisites
`````````````````````

The Welcome screen provides an overview of how the deployment works:

1. **Configure** — Enter SSH credentials, network settings, and VM configuration through the wizard
2. **Upload & Deploy** — The installer uploads the QCOW2 image and runs ``hvmcli`` to create and configure the VM
3. **Verify & Access** — Cloud-init configures the VM, and the installer verifies the application is ready

.. image:: /images/getting_started/installation/installer/prerequisites.png
   :alt: HPE Morpheus Installer - Prerequisites screen

Before continuing, confirm each prerequisite in the **Before You Start** checklist:

- **SSH access to the HVM host** — Ensure you can reach the target host over SSH (port 22) from this machine
- **HTTPS access to the HVM host** — The host must be reachable over HTTPS (port 443) for post-deploy verification
- **User has sudo privileges** — The SSH user must have sudo access to run ``virsh``, ``hvmcli``, and manage HVM resources
- **QCOW2 image available** — Have the HPE VM Essentials QCOW2 image ready — either a local file or an HTTP URL
- **Network configuration details** — Know the IP address, netmask, gateway, and DNS for the virtual machine

Once all items are confirmed, click **Next**.

.. image:: /images/getting_started/installation/installer/prerequisites_confirmed.png
   :alt: HPE Morpheus Installer - All prerequisites confirmed

Step 2: SSH Connection
``````````````````````

Configure the SSH connection to the target HVM hypervisor host where the Morpheus VM will be deployed.

.. image:: /images/getting_started/installation/installer/ssh_connection.png
   :alt: HPE Morpheus Installer - SSH Connection screen

- **Host** — The IP address or hostname of the HVM host
- **Port** — SSH port (default: ``22``)
- **Username** — SSH user (e.g., ``ubuntu``)
- **Authentication Method** — Choose between **Password** or **SSH Key** authentication
- **Password** — Enter the password for the SSH user (if using password authentication)

Click **Test Connection** to verify connectivity. The installer will:

1. Establish an SSH connection to the host
2. Verify the host-key fingerprint (you must accept it on first connection)
3. Detect the existing management virtSwitch on the host

.. image:: /images/getting_started/installation/installer/ssh_connection_connected.png
   :alt: HPE Morpheus Installer - SSH connection verified

Once connected and the host identity is verified, click **Next**.

Step 3: VM Network
``````````````````

Configure the static network settings for the Morpheus appliance VM. This is the IP address that will be assigned to the Morpheus VM itself.

.. image:: /images/getting_started/installation/installer/vm_network.png
   :alt: HPE Morpheus Installer - VM Network configuration

- **IP Address** — Static IP address for the Morpheus VM
- **Netmask** — Subnet mask (e.g., ``255.255.252.0``)
- **Gateway** — Default gateway for the VM
- **DNS Servers** — One or more DNS servers (click the **x** to remove entries, or add more as needed)
- **Appliance URL (optional)** — Custom URL for accessing the Morpheus appliance (e.g., ``https://morpheus.example.com``)

Click **Next** to proceed.

Step 4: Host Network
````````````````````

Configure the host management uplink. A management virtSwitch is created on the host before deployment (or reused if one already exists).

.. image:: /images/getting_started/installation/installer/host_network.png
   :alt: HPE Morpheus Installer - Host Network configuration

- **Management virtSwitch** — Displays the detected management virtSwitch (e.g., ``virtSwitch0 already exists on this host and will be reused``)

Optional settings:

- **Use Compute VLAN** — Enable if you want the Morpheus appliance VM to be deployed on a specific VLAN. When a VLAN ID is provided, the Morpheus appliance will be deployed using this VLAN for its network connectivity. When checked:

  - **Compute Interface** — Select the host interface for the compute network bridge
  - **Compute VLAN Tag** — The VLAN ID to use for the Morpheus appliance network

- **Use HTTP Proxy** — Enable if the environment requires an HTTP proxy. When checked:

  - **Proxy URL** — The proxy server URL (e.g., ``http://proxy:8080``)
  - **No Proxy** — Comma-separated list of hosts to bypass the proxy (e.g., ``localhost,127.0.0.1``)

.. image:: /images/getting_started/installation/installer/host_network_options.png
   :alt: HPE Morpheus Installer - Host Network with VLAN and Proxy options

Click **Next** to proceed.

Step 5: VM Configuration
````````````````````````

Configure the Morpheus appliance virtual machine settings.

.. image:: /images/getting_started/installation/installer/vm_configuration.png
   :alt: HPE Morpheus Installer - VM Configuration

**VM Settings:**

- **Hostname** — The hostname for the Morpheus VM (e.g., ``morpheus-app``)
- **VM Size** — Select a VM sizing profile:

  - Small (12 GB RAM, 2 vCPUs)
  - Medium
  - Large

- **QCOW2 Image** — Path to the HPE VM Essentials QCOW2 image. Use the **Browse** button to locate the file on the ISO volume (e.g., ``hpe-vm-essentials-9.0.0-1.qcow2.gz``), or enter an HTTP URL
- **Expected SHA256 Checksum (optional)** — If provided, the local image file's SHA256 will be verified before upload

**Appliance First-Boot Configuration:**

These fields configure the initial setup of the Morpheus appliance after deployment:

- **Appliance Name** — Name of the Morpheus appliance (e.g., ``Morpheus``)
- **Initial Tenant Name** — Name of the initial tenant (e.g., ``Master Tenant``)
- **Admin Username** — Administrator username (e.g., ``admin``)
- **Admin Password** — Password for the administrator account
- **Admin Email** — Email address for the administrator
- **First Name** / **Last Name** — Administrator's name

.. image:: /images/getting_started/installation/installer/qcow2_browse.png
   :alt: HPE Morpheus Installer - Browsing for the QCOW2 image on the ISO

Click **Next** to proceed to the review step.

Step 6: Review & Preflight Check
`````````````````````````````````

The final step before deployment. The installer runs preflight checks to validate your configuration and displays a summary.

.. image:: /images/getting_started/installation/installer/review_preflight.png
   :alt: HPE Morpheus Installer - Review and Preflight Check

**Preflight Checks:**

- SSH connection to host
- ``hvmcli`` present + passwordless sudo
- IP address format valid
- Hostname format valid
- Image path specified
- Management uplink set

All checks must pass (shown in green) before you can deploy. If any check fails, click **Re-run** to retry or go back to correct the configuration.

**Configuration Summary:**

Review the full configuration summary including SSH target, VM IP, netmask/gateway, DNS, hostname, VM size, image path, admin user, management uplink, compute interface, and proxy settings.

When satisfied, click **Deploy** to start the deployment.

Deployment Progress
```````````````````

Once deployment begins, the installer displays a real-time progress view showing each step:

.. image:: /images/getting_started/installation/installer/deploying.png
   :alt: HPE Morpheus Installer - Deployment in progress

The deployment steps include:

1. Preparing host virtSwitch
2. Validating deployment parameters
3. Running pre-flight checks
4. Preparing KVM hypervisor
5. Configuring management network
6. Configuring compute network
7. Creating local storage pool
8. Downloading QCOW2 image
9. Building cloud-init configuration
10. Defining virtual machine
11. Starting virtual machine
12. Waiting for Morpheus services to start
13. Running post-deploy health checks
14. Cleaning up temporary files

A **Cancel Deployment** button is available if you need to abort the process.

Troubleshooting a Failed Deployment
````````````````````````````````````

If the deployment encounters an error, the installer clearly indicates which step failed and provides troubleshooting options.

.. image:: /images/getting_started/installation/installer/deployment_failed.png
   :alt: HPE Morpheus Installer - Deployment Failed

Click **What went wrong** (or **Hide details**) to expand error details showing the specific error message.

.. image:: /images/getting_started/installation/installer/deployment_failed_details.png
   :alt: HPE Morpheus Installer - Deployment failure details

**What to try:**

- Check the deployment logs for more details
- Try restarting the deployment from scratch
- If the issue persists, collect logs and contact support

**Available actions:**

- **View Logs** — Opens the local log directory containing ``main.log`` with detailed deployment trace
- **Export Report** — Exports a deployment report for support purposes
- **Retry Deployment** — Retry the deployment from the beginning
- **Back to Configuration** — Return to the configuration wizard to adjust settings

.. image:: /images/getting_started/installation/installer/view_logs.png
   :alt: HPE Morpheus Installer - Viewing deployment logs

.. tip:: Host-side logs are also available at ``/var/log/hvmcli/`` on the HVM host for additional troubleshooting.
