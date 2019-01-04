Virtualbox
-----------

Overview
^^^^^^^^^
Oracle VM VirtualBox is a free and open-source hosted hypervisor for x86 computers currently being developed by Oracle Corporation. Developed initially by Innotek GmbH, it was acquired by Sun Microsystems in 2008 which was in turn acquired by Oracle in 2010.


Features
^^^^^^^^^
*
*
*


Add a VirtualBox Cloud
^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure -> Clouds``
#. Select :guilabel:`+ CREATE CLOUD`, select Virtual Box, and then click Next.
#. Enter the following into the Create Cloud modal:

   Name
      Name of the Cloud in |morpheus|
   Location
      Description field for adding notes on the cloud, such as location.
   Visibility
      For setting cloud permissions in a multi-tenant environment. Not applicable in single tenant environments.
   VIRTUALBOX HOST
      IP or URL of the VirtualBox Host
   WORKING PATH
      Path |morpheus| will write to. ex: ``~/virtualbox``
   USERNAME
      Host Username
   PASSWORD
      Host Password
   BRIDGE NAME
      Will auto-populate upon successful authentication with the VirtualBox Host (E.X. 'EN0: ETHERNET')
   VBOXMANAGE EXECUTABLE
      Defaults to ``/urs/local/bin/vboxmanage`` if left blank

#. The Cloud can now be added to a Group or configured with additional Advanced options.

.. include:: /integration_guides/Clouds/advanced_options.rst
