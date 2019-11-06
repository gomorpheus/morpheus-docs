Morpheus Agent
===============

The |morpheus| Agent is an important and powerful facet of |morpheus| as a orchestration tool.  Though not required, it is recommended for use as it brings with it a lot of insightful benefits. It's also a key differentiator between Morpheus and some other competing platforms. Not only does it provide statistics of the guest operating system and resource utilization, it also brings along with it monitoring and log aggregation capabilities. After an initial brownfield discovery, users can decide to convert unmanaged virtual machines to managed. Even with the numerous benefits it provides, the |morpheus| Agent is very lightweight and secure.

.. NOTE::
      **The agent is not required** by |morpheus| to become a managed instance.  If you don't have the agent installed we try to aggregate stats but it can vary based on the cloud and can be limited.

The |morpheus| Agent does not open any inbound network ports but rather only opens an outbound connection back to the Morpheus appliance over port 443 (https or wss protocol). This allows for a bidirectional command bus where instructions can be sent to orchestrate a workload without needing access to things like SSH or WinRM. The tool can even be installed at provision time via things like cloud-init, such that the |morpheus| appliance itself doesn't even need direct network access to the VLAN under which the workload resides. By doing this we address many of the network security concerns that arise with regards to the agent while demonstrating its security benefits as well as analytics benefits. We can even use this statistical data at the guest OS level rather than the hypervisor level to provide extremely precise right-sizing recommendations.


Key Agent Features
-------------------
* Provides key enhanced statistics (disc usage, CPU usage, network, disc IO)
* Handles log aggregation
* Provides a command bus to where |morpheus| doesn't need to get credentials to access a box. Can still run workflows if credentials are changed
* SSH agent can be disabled and still get access to the box
* Agent can be installed over Cloud-init, Windows unattend.xml, VMware Tools, SSH, WinRM, Cloudbase-init, or manually.
* Makes a single connect that's persistence over HTTPs web socket and runs as a service
* Health and Monitoring Checks
* Agent buffers and compresses logs and sends them in chunks to minimize packets
* Supports syslog forwarding
* Linux agent can be shrunk and should be less then 0.2% peak
* Accepts commands, can execute commands, write files, and manipulate firewalls
* Agent installation is optional for provisioning and converting Discovered resources to managed

Morpheus Agent OS Support
-------------------------

+--------------------------+--------------+--------------+---------------+---------------------+
| **Name**                 | **Platform** | **Category** | **Bit Count** | **Agent Supported** |
+--------------------------+--------------+--------------+---------------+---------------------+
| centOS                   | linux        | centos       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| centOS 6                 | linux        | centos       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| centOS 6 64-bit          | linux        | centos       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| centOS 64-bit            | linux        | centos       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| centOS 7                 | linux        | centos       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| centOS 7 64-bit          | linux        | centos       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| debian                   | linux        | debian       | 32            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| debian 6                 | linux        | debian       | 32            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| debian 6 64-bit          | linux        | debian       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| debian 64-bit            | linux        | debian       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| debian 7                 | linux        | debian       | 32            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| debian 7 64-bit          | linux        | debian       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| debian 8                 | linux        | debian       | 32            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| debian 8 64-bit          | linux        | debian       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| debian 9.4 64-bit        | linux        | debian       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| fedora                   | linux        | fedora       | 32            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| fedora 64-bit            | linux        | fedora       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| mac os                   | osx          | mac          | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| oracle enterprise        | linux        | oracle       | 32            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| oracle enterprise 64-bit | linux        | oracle       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| oracle linux 64-bit      | linux        | oracle       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| redhat                   | linux        | redhat       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| redhat 6                 | linux        | redhat       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| redhat 6 64-bit          | linux        | redhat       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| redhat 64-bit            | linux        | redhat       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| redhat 7                 | linux        | redhat       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| redhat 7 64-bit          | linux        | redhat       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| ubuntu                   | linux        | ubuntu       | 32            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| ubuntu 12                | linux        | ubuntu       | 32            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| ubuntu 12 64-bit         | linux        | ubuntu       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| ubuntu 13                | linux        | ubuntu       | 32            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| ubuntu 13 64-bit         | linux        | ubuntu       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| ubuntu 14                | linux        | ubuntu       | 32            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| ubuntu 14 64-bit         | linux        | ubuntu       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| ubuntu 15                | linux        | ubuntu       | 32            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| ubuntu 15 64-bit         | linux        | ubuntu       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| ubuntu 16                | linux        | ubuntu       | 32            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| ubuntu 16 64-bit         | linux        | ubuntu       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| ubuntu 18.04             | linux        | ubuntu       | 32            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| ubuntu 18.04 64-bit      | linux        | ubuntu       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| ubuntu 64-bit            | linux        | ubuntu       | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| windows 10               | windows      | windows      | 32            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| windows 10 64-bit        | windows      | windows      | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| windows 7                | windows      | windows      | 32            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| windows 7 64-bit         | windows      | windows      | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| windows 8 64-bit         | windows      | windows      | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| windows server 2008      | windows      | windows      | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| windows server 2008 R2   | windows      | windows      | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| windows server 2012      | windows      | windows      | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| windows server 2016      | windows      | windows      | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+
| windows server 2019      | windows      | windows      | 64            | 1                   |
+--------------------------+--------------+--------------+---------------+---------------------+

.. important:: Amazon Linux is not supported by the Morpheus Agent

Agent Install
--------------

When provisioning an instance, there are network and configuration requirements to successfully install the morpheus agent. Typically when a VM instance is still in the provisioning phase long after the VM is up, the instance is unable to reach |morpheus|. Alternatively, depending on the agent install mode, |morpheus| may be unable to reach the instance.

The most common reason an agent install fails is the provisioned instance cannot reach the |morpheus| Appliance via the appliance_url set in Admin -> Settings over both 443 and 80. When an instance is provisioned from |morpheus|, it must be able to reach the |morpheus| appliance via the appliance_url or the agent will not be installed.

.. image:: /images/agent-7c9a2.png
    :align: center


In addition to the main appliance_url in Admin -> Settings, additional appliance_urls can be set per cloud in the Advanced options section of the cloud configuration pane when creating or editing a cloud. When this field is populated, it will override the main appliance url for anything provisioned into that cloud.

.. TIP:: The |morpheus| UI current log, located at /var/log/morpheus/morpheus-ui/current, is very helpful when troubleshooting agent installations.

Agent Install Methods
^^^^^^^^^^^^^^^^^^^^^

.. image:: /images/provisioning/agent_ssh.gif
   :height: 500px
   :align: center

The Morpheus Agent can be installed with a variety of automated methods:

- ssh (linux)
- winRM
- VMware Tools
- Cloud-init
- Cloudbase-init
- Windows unattend.xml

Agents can also be manually installed.

For All Agent Install modes
............................

When an instance is provisioned and the agent does not install, verify the following for any agent install mode:

* The |morpheus| appliance_url (Admin -> Settings) is both reachable and resolvable from the provisioned node.
* The appliance_url begins with to https://, not http://.

.. NOTE:: Be sure to use https:// even when using an ip address for the appliance.

* Inbound connectivity access to the |morpheus| Appliance from provisioned VM's and container hosts on port 443 (needed for agent communication)

* Private (non-morpheus provided) VM images/templates must have their credentials entered. These can be entered/edited in the Provisioning > Virtual Images section by clicking the Actions dropdown of an image and selecting Edit.

.. NOTE:: Administrator user is required for Windows agent install.

* The instance does not have an IP address assigned. For scenarios without a dhcp server, static IP information must be entered by selecting the Network Type: Static in the Advanced section during provisioning. IP Pools can also be created in the Infrastructure -> Networks -> IP Pools section and added to the clouds network sections for IPAM.

* DNS is not configured and the node cannot resolve the appliance. If dns cannot be configured, the IP address of the |morpheus| appliance can be used as the main or cloud appliance.

SSH/Winrm
^^^^^^^^^

Linux Agent
............

* Port 22 is open for Linux images, and ssh is enabled
* Credentials have been entered on the image if using custom or synced image. Credentials can be entered on images in the Provisioning -> Virtual Images section.

Windows Agent
..............

* Port 5985 must be open and winRM enabled for Windows images.
* Credentials have been entered on the image if using custom or synced image. Credentials can be entered on images in the Provisioning -> Virtual Images section.

.. NOTE:: Administrator user is required for Windows agent install.

VMware tools (vmtools) rpc mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* VMware tools is installed on the template(s)
* Credentials have been entered on the Image if using uploaded or synced image when Cloud-init or Guest Customizations or Sysprep for Windows are not used. Credentials can be entered on Images in the `Provisioning -> Virtual Images` section.

Cloud-Init agent install mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Cloud-Init is configured in Admin -> Provisioning section
* Provisioned image/blueprint has Cloud-Init (linux) or Cloudbase-Init (windows) installed

.. include:: /troubleshooting/Morpheus_Agent.rst
