Oracle VM
---------

Description
^^^^^^^^^^^^^
Oracle VM Server for x86 is the server virtualization offering from Oracle Corporation. Oracle VM Server for x86 incorporates the free and open-source Xen hypervisor technology, supports Windows, Linux, and Solaris guests and includes an integrated Web based management console.


Features
^^^^^^^^^^^^^
* Virtual Machine Provisioning
* Ability to provision by OCID
* Multiple Compartment support and default Compartment selection
* Ability to Reconfigure
* Ability to upload a local image
* Oracle Cloud library nodes
* Support for different storage types





Add a Oracle VM Cloud
^^^^^^^^^^^^^^^^^^^^^^

Name
  Name of the Cloud in |morpheus|
Location
  Description field for adding notes on the cloud, such as location.
Visibility
  For setting cloud permissions in a multi-tenant environment. Not applicable in single tenant environments.
API URL
  Oracle VM API URL. ex: https://10.20.30.40:7002/ovm/core/wsapi/rest
USERNAME
  Oracle VM User
PASSWORD
  Oracle VM User Password
REPOSITORY
  Available repositories will auto-populate upon successful authentication with the above credentials. Select appropriate repository for this Cloud.
SERVER POOL
  Available server pools will auto-populate upon successful authentication with the above credentials. Select appropriate server pool for this Cloud.
Inventory Existing Instances
  If enabled, existing Virtual Machines will be inventoried and appear as unmanaged Virtual Machines in |morpheus| .

The Cloud can now be added to a Group or configured with additional Advanced options.

.. .. include:: /integration_guides/advanced_options.rst
