Storage
-------------

When Morpheus is in a High Availability configuration the required Local Storage File Shares will need to be copied to a shared file system so that all nodes within the Morpheus cluster is able to connect to assets.

Assests
^^^^^^^^
* White label images
* Uploaded virtual images
* Deploy uploads
* Ansible Plays
* Terraform
* Morpheus backups.

.. TIP::

    Backup , Deployments and virtual images can be overridden within the Morpheus-UI.  You can find more information on storage here: :ref:`storage`

To copy the ```morpheus-ui``` directory to the shared storage follow the below steps:

#. SSH into the Appliance
#. sudo su (or login as root)
#. cd into ```/var/opt/morpheus/```
#. Backup morpheus-ui directory by running

  .. code-block::

     cp -r morpheus-ui morpheus-ui-bkp

This will create a new directory in ```/var/opt/morpheus/``` called morpheus-ui-bkp and copy the contents of morpheus-ui into the new directory

#. mv morpheus-ui to your shared storage Example:

  .. code-block::

      mv morpheus-ui /nfs/appliance-files/

#. Create a symlink in the ```/var/opt/morpheus/``` for morpheus-ui pointing to the shared storage. Example:

  .. code-block::

       ln -s /nfs-share/appliance-files/morpheus-ui /var/opt/morpheus/morpheus-ui

#. SSH into the second Appliance and then Backup morpheus-ui directory by running

  .. code-block::

      cp -r morpheus-ui morpheus-ui-bkp

#. Create a symlink in the ```/var/opt/morpheus/``` for morpheus-ui pointing to the shared storage. Example:

  .. code-block::
    
     ln -s /nfs-share/appliance-files/morpheus-ui /var/opt/morpheus/morpheus-ui

on the second appliance.

.. TIP:: when adding additional nodes you will only need to run step 7 and 8
