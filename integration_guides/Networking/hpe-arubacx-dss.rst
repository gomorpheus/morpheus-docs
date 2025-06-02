Aruba CX10000 Integration (ArubaCxDss Network Plugin)
-----------------------------------------------------

Overview
^^^^^^^^
The HPE ANW DSA (HPE Aruba Networking Distributed Service Architecture) plugin, also known as the ArubaCxDss Network Plugin, brings advanced networking features to HPE VME by leveraging Aruba CX10000 switches.
It supports both micro-segmentation and macro-segmentation, integrating seamlessly with HPE and Aruba technologies to improve user experience and operational efficiency.

Implemented as a |morpheus| ``NetworkProvider`` in Groovy, the plugin is purpose-built for the HPE ANW DSS Port Group network type, optimized for HPE VME environments.
It automates the creation and management of networks for HPE ANW DSS Port Groups, connecting servers to Aruba CX10000 switches within a VME cluster.

On each host, the plugin creates Linux bridge interfaces and associates them with VLANs for streamlined network management and configuration.
|morpheus| integrates directly with AFC to automatically create or delete networks for HPE ANW DSS Port Groups as they are added to or removed from a configured cluster.
Adding or removing hosts in the cluster triggers the corresponding network changes in AFC, ensuring that network configurations are always up-to-date.

The plugin also enables the creation of networks with specific VLAN IDs, supporting flexible segmentation and isolation.
When a network is created, the plugin provisions the required VLANs on the Aruba CX10000 switches, ensuring networks are ready for use by instances within the VME cluster.

Additionally, the plugin creates a Libvirt network of type Private.
When an instance is created on the host and associated with this network, a macvtap interface is generated and mapped to the corresponding Linux Interface VLAN ID, ensuring seamless connectivity and isolation.

Features
^^^^^^^^
* Create and delete networks of type ``HPE ANW DSS Port Group`` directly from the integration.
* Automatically create and delete networks in Aruba Fabric Composer (AFC) when hosts are added or removed from the cluster.
* Manage network configurations through seamless integration with Aruba Fabric Composer (AFC).
* Enable both micro-segmentation and macro-segmentation for flexible network isolation.
* View detailed summaries and status of Aruba CX10000 switches.
* Ensure automatic, real-time synchronization of network configurations with Aruba CX10000 switches.

Prerequisites
^^^^^^^^^^^^^
The following requirements must be met to deploy and configure the ArubaCxDss Network plugin on VME.

* Aruba CX10000 series switches - Minimum two switches are required for redundancy.

    - Aruba CX10000 switches are configured.
    - VSX and KeepAlive are configured.
    - Switches are connected to the upstream network.

* HPE VM Cluster is already set up.

    - Ensure all hosts within the cluster are physically connected to the CX10000 switches for optimal network integration and redundancy.

* VME Appliance version 8.0.6 or higher.

    - AFC and PSM are deployed and reachable from VME Manager.

* Aruba Fabric Composer (AFC) version 7.2 or higher, deployed as a VM.

* AMD Pensando PSM (Policy and Services Manager), deployed as a VM.

.. note::
 - Download AFC and PSM from the HPE Networking Support portal: https://networkingsupport.hpe.com/downloads/software/RmlsZTo0YzQ2MzIyYS0xOTU2LTExZjAtYTMzNS0yZmRkN2QyMjdhOTY%3D
 - For more information on deploying AFC and PSM, refer to the official documentation.
 - The AFC and PSM must have network connectivity to the CX1000 switches.
 - Making full use of the |morpheus| Aruba CX10000 integration requires credentials for AFC with API access granted and read/write access to AFC configuration.

Adding `HPE ANW ArubaCX DSS Network` Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Navigate to |Infrastructure->Network->Integrations|
#. Select :guilabel:`+ Add` > Networking > HPE Aruba CX DSS

    .. image:: /images/integration_guides/networking/arubacxdss/1_add_network_integration.png
      :width: 60%

#. Enter the following details in the `Add Network Integration` form:

   NAME
    Name of the integration in |morpheus|
   AFC ADDRESS
    Enter the network address of the AFC
   AFC USERNAME
    Enter the username
   AFC PASSWORD
    Enter the password
   FABRIC NAME
    Enter the Fabric name from the AFC

    .. image:: /images/integration_guides/networking/arubacxdss/2_create_network_integration.png
      :width: 40%

#. Select :guilabel:`Add Network Integration`

Upon add the `ArubaCxDss Network integration` will be created.

.. NOTE:: All fields can be edited after saving.

Create `HPE ANW DSS Port Group` Network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To create an `HPE ANW DSS Port Group` network, follow these steps:

#. Navigate to |Infrastructure->Network->Networks|
#. Select :guilabel:`+ Add Network` > HPE ANW DSS Port Group

   .. image:: /images/integration_guides/networking/arubacxdss/3.1_add_network.png
     :width: 40%

#. Enter the following details in the `Add Network` form:

   .. image:: /images/integration_guides/networking/arubacxdss/3.2_add_network.png
     :width: 40%

#. Save the network by clicking on :guilabel:`Save changes`.

   .. image:: /images/integration_guides/networking/arubacxdss/3.3_add_network.png
     :width: 40%

#. The network will be created and displayed in the list of networks.

   .. image:: /images/integration_guides/networking/arubacxdss/3.4_network_created.png
     :width: 60%

Delete `HPE ANW DSS Port Group` Network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To delete a `HPE ANW DSS Port Group` network, follow these steps:

#. Navigate to |Infrastructure->Network->Networks|
#. Select the network you want to delete from the list.
#. Click on the delete icon (trash can) next to the network name.

   .. image:: /images/integration_guides/networking/arubacxdss/4_delete_network.png
     :width: 60%

View `HPE ANW ArubaCX DSS Network` Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To view the `HPE ANW ArubaCX Network` integration, follow these steps:
 #. Navigate to |Infrastructure->Network->Integrations|
 #. Select the `HPE Aruba CX DSS` integration from the list.

    .. image:: /images/integration_guides/networking/arubacxdss/5.1_list_network_integrations.png
        :width: 60%

    - ``Summary`` - Click on the :guilabel:`Summary` tab to view the summary of the integration.

        .. image:: /images/integration_guides/networking/arubacxdss/5.2_view_integration_summary.png
            :width: 60%

    - ``Switches`` - Click the :guilabel:`Switches` tab to view detailed information about all Aruba CX10000 switches managed by the integration.

        .. image:: /images/integration_guides/networking/arubacxdss/5.3_view_integration_details.png
            :width: 60%

    - ``Networks`` - Click on the :guilabel:`Networks` tab to view the networks associated with the integration.

        .. image:: /images/integration_guides/networking/arubacxdss/5.4_view_integration_networks.png
            :width: 60%
