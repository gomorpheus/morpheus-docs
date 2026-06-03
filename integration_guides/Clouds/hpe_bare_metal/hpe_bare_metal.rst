HPE Bare Metal (BMaaS)
----------------------

Overview
^^^^^^^^

HPE Bare-Metal-as-a-Service (BMaaS) for |morpheus| Enterprise extends hybrid cloud management capabilities to HPE ProLiant physical servers. This integration allows the |morpheus| platform to discover, provision, and manage these servers as first-class resources. Additionally, HPE BMaaS Cloud integrates HPE ProLiant bare-metal infrastructure into cloud environments to enable cloud-based provisioning and lifecycle management.

HPE BMaaS manages the end-to-end server lifecycle, including hardware discovery, bare-metal provisioning, operating system deployment, monitoring, and metering. The |morpheus| interface centrally orchestrates these tasks. This unified approach enables organizations to manage physical infrastructure, virtual machines, and cloud resources using consistent workflows, policies, and governance controls.

Features
^^^^^^^^

* **Automated Server Discovery** - Automatically imports and discovers HPE ProLiant servers
* **Bare-Metal Provisioning** - Provisions hardware using custom or pre-configured OS images
* **Comprehensive OS Deployment** - Deploys Windows and Linux with unattended installations and customizable boot parameters
* **Lifecycle Management** - Manages firmware and drivers using the HPE Service Pack for ProLiant (SPP)
* **Flexible Networking** - Supports both unmanaged and managed network integrations
* **Metering and Billing** - Maps discovered hardware to service plans to align metering with billing
* **Logical Organization** - Organizes resources into Bare Metal Clouds and Resource Pools to support multi-site environments and scalable infrastructure segmentation

HPE BMaaS improves operational visibility and server lifecycle control. It offers a scalable, automated approach to manage physical infrastructure across both greenfield (new) and brownfield (existing) environments.

.. include:: /integration_guides/Clouds/hpe_bare_metal/adding_integration.rst
.. include:: /integration_guides/Clouds/hpe_bare_metal/creating_cloud.rst
.. include:: /integration_guides/Clouds/hpe_bare_metal/importing_servers.rst
.. include:: /integration_guides/Clouds/hpe_bare_metal/compute_management.rst
.. include:: /integration_guides/Clouds/hpe_bare_metal/firmware_lifecycle.rst
.. include:: /integration_guides/Clouds/hpe_bare_metal/network_management.rst
.. include:: /integration_guides/Clouds/hpe_bare_metal/storage_management.rst
.. include:: /integration_guides/Clouds/hpe_bare_metal/troubleshooting.rst
.. include:: /integration_guides/Clouds/hpe_bare_metal/limitations.rst
