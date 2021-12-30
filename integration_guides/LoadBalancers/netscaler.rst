Citrix NetScaler
----------------

.. image:: /images/infrastructure/lbs/netScaler-logo.png

Add NetScaler Integration
^^^^^^^^^^^^^^^^^^^^^^^^^
To add a NetScaler Load Balancer Integration:

#. Navigate to `Infrastructure > Load Balancers`
#. Select :guilabel:`+ ADD`
#. Select `Citrix NetScaler`
#. Fill in the following:

   GROUP *
    Select the Group the Load Balancer will be available for.
   CLOUD *
    Select the Cloud the Load Balancer will be available for.
   NAME *
    Name of the Load Balancer in |morpheus|.
   DESCRIPTION
    Identifying information displayed on the Load Balancer list page.
   VISIBILITY
    Define Tenant Visibility
      - Public: Available to all Tenants.
      - Private: Only available to specified Tenant.
   Tenant
    If Visibility is set to private, define the Tenant the Load Balancer will be available in.
   API URL  *
    URL of the NetScaler API
      - Example: http://10.30.21.55
   API PORT  *
     NetScaler API port
      - Example: 80
   USERNAME *
     NetScaler service account username
   PASSWORD *
    NetScaler service account password
   VIRTUAL NAME
     Naming Pattern for new NetScaler Virtual Servers
       - If blank, defaults to ``morph_lb_${loadBalancer.id}``
   SERVICE NAME
     Naming Pattern for new NetScaler Services
       - If blank, defaults to ``morph_service_${container.id}``
   SERVER NAME
     Naming Pattern for new NetScaler Servers
       - If blank, defaults to ``morph_server_${server.id}``

Add Load Balancer to Instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Load Balancers can be added to Instances during Provisioning or to existing Instances. For Load Balancer settings to appear during provisioning, or for the scale tab to be available on an Instance, the instances Node Type must have a LB port defined.

.. Note:: For Load Balancer settings to appear during provisioning, or for the scale tab to be available on an Instance, the instances Node Type must have a LB port defined.

Add Load Balancer during Provisioning
`````````````````````````````````````
In the Instance Provisioning wizard, Load Balancers can be configured in the Automation > Load Balancer section.

#. Navigate to |ProIns|.
#. Select :guilabel:`+ ADD`.
#. Select an Instance Type that supports scaling. (ENABLE SCALING (HORIZONTAL) flagged on Instance Type configuration)
#. Proceed with Instance configuration to the Automation section.
#. Fill in the following:

   VIP ADDRESS
    Define IP Address for the Virtual Server
     - Example: 10.30.23.191
   VIP PORT
    Define port for the Virtual Server
     - Example: 80
   VIP HOSTNAME
    Define hostname that will resolve to the VIP IP.
     - Example: jwDemoHaApp59.den.example.com
   VIRTUAL SERVICE NAME
    Define name for the Virtual Service. Defaults to ``${instance.name}``
   BALANCE MODE
    Specify balance mode for the VIP
     - Least Connections
     - Round Robin
   STICKY MODE
    Specify sticky session options for the VIP
     - Source IP
     - Cookie
   SHARED VIP ADDRESS
    Select if VIP is shared, then enter DIRECT VIP ADDRESS
   SSL CERT
    SSL Certificate that will be applied to the VIP.
     - No SSL
     - Select existing Certificate from ``Infrastructure > Keys & Certs`` or from a Trust Provider Integration.
    USE EXTERNAL ADDRESS FOR BACKEND NODES
     - Select if traffic from LB to Backend Nodes needs to be sent to the External Addresses, or leave deselected to use Internal Addresses for Backed Nodes.

#. Optionally configure auto-scaling configuration in the ``Scale`` section
#. Select :guilabel:`NEXT` and provision the Instance.

After all nodes in the Instance are provisioned, the LB configuration will be added to the Instance and Virtual Servers, Services and Servers will be created and configured on the NetScaler. The Load Balancer settings and status will be visible in the Instance details page LOAD BALANCER section, with additional details, links, and configurations options available in the ``SCALE`` tab.
