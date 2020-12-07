Servers
-------

Add Storage Server
^^^^^^^^^^^^^^^^^^

Adding 3Par Storage Server
``````````````````````````

#. Select the Infrastructure link in the navigation bar.
#. Select the Storage link in the sub navigation bar.
#. In the SERVERS tab, Click the :guilabel:`+ ADD` button.
#. From the ADD STORAGE SERVER wizard input the following:

   NAME
      Name of the Storage Server in |morpheus|
   TYPE
      Select `3Par`
   URL
     URL Of 3Par Server
     Example : `https://192.168.190.201:8008`
   USERNAME
    Add your administrative user account.
   PASSWORD
    Add your administrative password.

#. Select :guilabel:`SAVE CHANGES`

The 3Par Storage Server will be added and displayed in the Buckets tab. Buckets, Files Shares and Storage Groups will be synced in.

Adding Dell EMC ECS Storage Server
``````````````````````````````````

#. Select the Infrastructure link in the navigation bar.
#. Select the Storage link in the sub navigation bar.
#. In the SERVERS tab, Click the :guilabel:`+ ADD` button.
#. From the ADD STORAGE SERVER wizard input the following:

   NAME
      Name of the Storage Server in |morpheus|
   TYPE
      Select `Dell EMC ECS`
   URL
     URL Of DELL EMC ECS Server
      Example : `https://192.168.190.200:4443`

     .. TIP:: The port 4443 is the api port for ECS api. This may be different depending on your configuration

   USERNAME
    Add your administrative user account.
   PASSWORD
    Add your administrative password.
   S3 SERVICE URL (Optional)
    Add your S3 service url
    Example: http://192.168.190.220:9020

    .. NOTE:: S3 SERVICE URL is not required if you are not planning on using ECS S3.

#. Select :guilabel:`SAVE CHANGES`

The Dell EMC ECS Storage Server will be added and displayed in the Buckets tab. Buckets, Files Shares and Storage Groups will be synced in.

Adding Dell EMC Isilon Storage Server
`````````````````````````````````````

#. Select the Infrastructure link in the navigation bar.
#. Select the Storage link in the sub navigation bar.
#. In the SERVERS tab, Click the :guilabel:`+ ADD` button.
#. From the ADD STORAGE SERVER wizard input the following:

   NAME
      Name of the Storage Server in |morpheus|
   TYPE
      Select `Dell EMC Isilon`
   URL
     URL Of Dell EMC Isilon Server
     Example : `https://192.168.190.202:8080`
   USERNAME
    Add your administrative user account.
   PASSWORD
    Add your administrative password.
   PROVISION USER
    Select Provision User
   PROVISION GROUP
    Select Provision Group
   ROOT PATH
    Enter Root Path
      Example : ``\``

#. Select :guilabel:`SAVE CHANGES`

The Dell EMC Isilon Storage Server will be added and displayed in the Buckets tab. Buckets, Files Shares and Storage Groups will be synced in.
