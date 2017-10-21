SCVMM
=====

Add a SCVMM Cloud
-----------------

#. Navigate to Infrastructure -> Clouds
#. Select `+ CREATE CLOUD`, select SCVMM, and then click Next.
#. Enter the following into the Create Cloud modal:

   Name
    Name of the Cloud in |morpheus| 
   Location
    Description field for adding notes on the cloud, such as location.
   Visibility
    For setting cloud permissions in a multi-tenant environment. Not applicable in single tenant environments.
   SCVMM HOST
    IP or url of SCVMM host
   USERNAME
    SCVMM Username. ex: svc.scvmm
   PASSWORD
    SCVMM User Password
   CLOUD
    Select a Cloud from the available Clouds in SCVMM.
   WORKING PATH
    Path for |morpheus| to write to. ex: ``c:\Cloud``
   DISK PATH
    Path for Virtual Disks. ex: ``c:\VirtualDisks``

#. The Cloud can now be added to a Group or configured with additional Advanced options.

.. .. include:: /integration_guides/advanced_options.rst
