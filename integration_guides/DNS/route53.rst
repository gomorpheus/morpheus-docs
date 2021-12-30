AWS Route53
-----------

Overview
^^^^^^^^

|morpheus| integrates directly with Amazon Route 53 to automatically create DNS entries for Instances provisioned to a configured Cloud or Group. |morpheus| also syncs in Route 53 Domains for easy selection while provisioning, or setting as the default Domain on a Cloud or Network.

Add Route 53 Integration
^^^^^^^^^^^^^^^^^^^^^^^^

Route 53 can be added in the `Administration` or `Infrastructure` sections:

#. In |AdmInt|, select :guilabel:`+ New Integration`
#. In ``Infrastructure > Networks > Services``, select :guilabel:`Add Service`
#. Provide the following:

   TYPE
    Route 53
   NAME
    Name for the Integration in |morpheus|
   REGION
    AWS Region for the Integration
   ACCESS KEY
    AWS User IAM Access Key
   SECRET KEY
    AWS User IAM Secret Key

#. Once saved the Integration will be added and visible in both |AdmInt| and ``Infrastructure > Networks > Services``

.. NOTE:: All fields can be edited after saving.

Domains
^^^^^^^

Once the integration is added, Route 53 Domains will sync and listed under ``Infrastructure > Networks > Domains``.

.. NOTE:: Default Domains can be set on Networks and Clouds, and can be selected when provisioning. Additional configuration options are available by editing a domain in `Networks > Domains`

Configuring Route 53 with Clouds and Groups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

DNS Integrations are available in the `DNS Integration` dropdown in Cloud and Group settings.

|morpheus| will register Instances with the DNS provider when provisioned into a Cloud or Group with a DNS Integration added.

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
