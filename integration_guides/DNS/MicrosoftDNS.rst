Microsoft DNS
-------------

Overview
^^^^^^^^

|morpheus| integrates directly with  Microsoft DNS to automatically create DNS entries for Instances provisioned to a configured Cloud or Group. |morpheus| also syncs in Microsoft DNS Domains for easy selection while provisioning, or setting as the default Domain on a Cloud or Network.

Add Microsoft DNS Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Microsoft DNS can be added in the `Administration` or `Infrastructure` sections:

#. In ``Administration -> Integrations``, select :guilabel:`+ New Integration`
#. In ``Infrastructure -> Networks -> Services``, select :guilabel:`Add Service`
#. Provide the following:

   TYPE
    Microsoft DNS
   NAME
    Name for the Integration in |morpheus|
   DNS SERVER
    IP or resolvable hostname of DNS server
   USERNAME
    DNS provider username
   PASSWORD
    DNS provider user password
   ZONE
    (Optional) Enter a dns zone to limit scope
   CREATE POINTERS
    Enabled to create A records during provisioning

#. Once saved the Integration will be added and visible in both ``Administration -> Integrations`` and ``Infrastructure -> Networks -> Services``

.. NOTE:: All fields can be edited after saving.

Domains
^^^^^^^

Once the integration is added, Microsoft DNS Domains will sync and listed under ``Infrastructure -> Networks -> Domains``.

.. NOTE:: Default Domains can be set on Networks and Clouds, and can be selected when provisioning. Additional configuration options are available by editing a domain in `Networks -> Domains`

Configuring Microsoft DNS with Clouds and Groups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

DNS Integrations are available in the `DNS Integration` dropdown in Cloud and Group settings.

|morpheus| will register Instances with the DNS provider when provisioned into a Cloud or Group with a DNS Integration added.

Add DNS Integration to a Cloud
..............................

#. In ``Infrastructure -> Clouds`` edit the target Cloud.
#. Expand the `Advanced Options` section.
#. In the `DNS Integration` dropdown, select an available DNS Integration.
#. Save Changes

Add DNS Integration to a Group
..............................

#. In ``Infrastructure -> Groups`` select the target Group.
#. Select the `Edit` button for the Group
#. Expand the `Advanced Options` section.
#. In the `DNS Integration` dropdown, select an available DNS Integration.
#. Save Changes

.. NOTE:: Instances provisioned into a Cloud or Group with a DNS Integration added will be registered as instancename.domain with the DNS Provider during provisioning, and de-registered at teardown.
