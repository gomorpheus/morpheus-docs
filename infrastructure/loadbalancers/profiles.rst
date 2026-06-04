.. _lb_profiles:

Load Balancer Profiles
----------------------

Overview
^^^^^^^^

Load Balancer Profiles define SSL/TLS and protocol handling configurations that can be applied to virtual servers. Profiles allow you to manage SSL certificate bindings, cipher suites, and protocol settings in a reusable configuration that can be referenced by multiple virtual servers.

Profile management is available for load balancer types that support profile configurations (such as F5 BIG-IP, Avi/NSX ALB, and NSX-T).

Role Requirements
^^^^^^^^^^^^^^^^^

- ``Infrastructure: Load Balancers`` role permission at **Full** level is required to create, edit, or delete profiles.
- ``Infrastructure: Load Balancers`` role permission at **Read** level allows viewing profiles only.

Viewing Profiles
^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Load Balancers``
#. Click the name of a Load Balancer to view its detail page
#. Select the **PROFILES** tab

The Profiles tab lists all profiles configured for the load balancer, including:

- **Name** — Profile name
- **Description** — Profile description
- **Type** — The profile type (e.g., Client SSL, Server SSL, HTTP)
- **Service Type** — The protocol or service the profile applies to

Creating a Profile
^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Load Balancers``
#. Click the name of a Load Balancer
#. Select the **PROFILES** tab
#. Click :guilabel:`+ ADD`
#. Configure the profile fields:

   NAME
     A descriptive name for the profile.
   DESCRIPTION
     Optional description of the profile's purpose.
   SERVICE TYPE
     The type of profile to create. Available options depend on the load balancer type and may include:

     - **Client SSL** — Manages SSL/TLS termination for client-facing connections
     - **Server SSL** — Manages SSL/TLS for backend server connections
     - **HTTP** — HTTP protocol handling options
     - **TCP** — TCP connection management
     - **UDP** — UDP protocol options
     - **Persistence** — Session persistence configuration
     - **Cookie Persistence** — Cookie-based session affinity

   CLIENT SSL CERTIFICATE
     Select one or more client SSL certificates from the certificate store. Certificates must be previously uploaded under ``Infrastructure > Certificates``.
   SERVER SSL CERTIFICATE
     Select one or more server SSL certificates for backend connections.

   .. NOTE:: Additional fields are displayed based on the load balancer type and the selected service type. These are defined by the provider's profile option types.

#. Click :guilabel:`SAVE CHANGES`

Editing a Profile
^^^^^^^^^^^^^^^^^

#. Navigate to the Load Balancer detail page
#. Select the **PROFILES** tab
#. Click the edit icon next to the profile
#. Modify the desired fields
#. Click :guilabel:`SAVE CHANGES`

Deleting a Profile
^^^^^^^^^^^^^^^^^^

#. Navigate to the Load Balancer detail page
#. Select the **PROFILES** tab
#. Click the delete icon next to the profile
#. Confirm the deletion

.. WARNING:: Deleting a profile that is currently assigned to a virtual server may disrupt traffic. Ensure no active virtual servers reference the profile before removing it.

Using Profiles with Virtual Servers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When creating or editing a Virtual Server, profiles can be selected from the **PROFILES** field. Multiple profiles can be applied to a single virtual server. The available profiles are filtered to those belonging to the same load balancer.

See the F5 documentation section for details on how profiles are applied to F5 virtual servers.
