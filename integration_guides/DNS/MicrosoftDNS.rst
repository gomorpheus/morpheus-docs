Microsoft DNS
-------------

Overview
^^^^^^^^

|morpheus| integrates directly with  Microsoft DNS to automatically create DNS entries for Instances provisioned to a configured Cloud or Group. |morpheus| also syncs in Microsoft DNS Domains for easy selection while provisioning, or setting as the default Domain on a Cloud or Network.

Add Microsoft DNS Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. IMPORTANT:: The |morpheus| Microsoft DNS integration works over http/5985.  If you have turned off the http listener on 5985 and only enabled https/5986 it will fail.

Microsoft DNS can be added in the `Administration` or `Infrastructure` sections:

#. In |AdmInt|, select :guilabel:`+ New Integration`
#. In ``Infrastructure > Networks > Services``, select :guilabel:`Add Service`
#. Provide the following:

   TYPE
    Microsoft DNS
   NAME
    Name for the Integration in |morpheus|
   DNS SERVER
    IP or resolvable hostname of DNS server ``morpheus`` will connect to. If using a jump box, specify the IP or resolvable hostname of the jump box here, and the main DNS Server in the COMPUTER NAME field below.
   USERNAME
    DNS provider username
   PASSWORD
    DNS provider user password
   COMPUTER NAME
    If the DNS SERVER specified is not the main DNS server but rather a jump box, enter the Computer Name of the main DNS Server here. If the DNS SERVER specified above is the main DNS server and not a jump box, leave COMPUTER NAME blank.
   CREATE POINTERS
    Enabled to create A records during provisioning

#. Once saved the Integration will be added and visible in both |AdmInt| and ``Infrastructure > Networks > Services``

.. NOTE:: All fields can be edited after saving.

Domains
^^^^^^^

Once the integration is added, Microsoft DNS Domains will sync and listed under ``Infrastructure > Networks > Domains``.

.. NOTE:: Default Domains can be set on Networks and Clouds, and can be selected when provisioning. Additional configuration options are available by editing a domain in `Networks > Domains`

Configuring Microsoft DNS with Clouds and Groups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

DNS Integrations are available in the `DNS Integration` dropdown in Cloud and Group settings. |morpheus| will register Instances with the DNS provider when provisioned into a Cloud or Group with a DNS Integration added.

To take full advantage of the |morpheus| Microsoft DNS integration, a service account in the Admins group is not required. However, an account must have the following minimum access to use all features:

- Read, Create, and Delete rights on objects
- Belongs to the local group ``WinRMRemoteWMIUsers__``
- WinRM Quickconfig must be run on the DNS server
- CIMv2 needs access according to instructions in our `KnowledgeBase <https://support.morpheusdata.com/s/article/How-to-give-C?language=en_US>`_

Add DNS Integration to a Cloud
``````````````````````````````

#. In ``Infrastructure > Clouds`` edit the target Cloud.
#. Expand the `Advanced Options` section.
#. In the `DNS Integration` dropdown, select an available DNS Integration.
#. Save Changes

Add DNS Integration to a Group
``````````````````````````````

#. In ``Infrastructure > Groups`` select the target Group.
#. Select the `Edit` button for the Group
#. Expand the `Advanced Options` section.
#. In the `DNS Integration` dropdown, select an available DNS Integration.
#. Save Changes

.. NOTE:: Instances provisioned into a Cloud or Group with a DNS Integration added will be registered as instancename.domain with the DNS Provider during provisioning, and de-registered at teardown.
