***************
Getting Started
***************

|firstuse| is a virtualization solution allowing for easy deployment of KVM-based |clusters| with administration made easy through |manager|. Once deployed, take advantage of powerful features including live migration of VMs across cluster hosts with zero downtime, dynamically distribute workloads based on load, automatic failover of workloads following the loss of a host, and a lot more. Provisioning new workloads is also made easy with the |morpheus| image library, automation tools, and powerful provisioning wizard. In addition to |clusters|, |morpheus| also includes a deep integration into VMware vCenter, which also takes advantage of the same powerful provisioning wizard, automation engine, and monitoring capabilities.

This documentation covers the system requirements for |clusters| and a setup guide for installing |manager|. It also includes example use cases for effective implementation of the feature set and in-depth sections for each area of the UI detailing the capabilities of each tool.

Before getting started, it's important to note that administrators have the responsibility to install and configure servers and network equipment in a way that will ensure successful operation of |morpheus|. This includes selecting host servers, storage hardware, and networking hardware that have been certified as compatible with the platform. The |morpheus| section of the `HPE Support Center <https://www.hpe.com/support/VME-Docs>`_ contains a reference architecture document which includes a validated design with specific hardware SKUs. The same section of the HPE Support Center also includes a qualification matrix which lists hardware that has been certified compatible.

Additionally, administrators will be required to perform some setup functions on their own, such as preinstalling Ubuntu 24.04 (or 22.04 though you won't be able to utilize the latest cluster layouts) on host servers, configuring networking for each host, configuring access to external storage at the OS level, and establishing a network topology that ensures acceptable performance. Subsequent sections of this document will outline some effective network designs and some tips for selecting a network design based on available hardware. It will be the responsibility of the administrator to select a network design based on available hardware and to use the Linux command line to establish appropriate network bonds, storage configuration, and access across the cluster.

.. include:: network_considerations.rst

.. include:: installation.rst

.. include:: env_setup.rst

.. include:: qual_list.rst

.. include:: upgrade_to_morpheus.rst
