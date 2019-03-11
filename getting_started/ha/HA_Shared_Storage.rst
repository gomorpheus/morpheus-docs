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

1. SSH into the Appliance
2. sudo su (or login as root)
3. cd into ```/var/opt/morpheus/```
4. Backup morpheus-ui directory by running the command below.  This will create a new directory in ```/var/opt/morpheus/``` called morpheus-ui-bkp and copy the contents of morpheus-ui into the new directory

 .. code-block:: bash

  cp -r morpheus-ui morpheus-ui-bkp

5. Move morpheus-ui to your shared storage. Example below:

  .. code-block:: bash

   mv morpheus-ui /nfs/appliance-files/

6. Create a symlink in the ```/var/opt/morpheus/``` for morpheus-ui pointing to the shared storage. Example below:

  .. code-block:: bash

   ln -s /nfs-share/appliance-files/morpheus-ui /var/opt/morpheus/morpheus-ui

7. SSH into the second Appliance and then Backup morpheus-ui directory by running

  .. code-block:: bash

    cp -r morpheus-ui morpheus-ui-bkp

8. Create a symlink in the ```/var/opt/morpheus/``` for morpheus-ui pointing to the shared storage on the second appliance. Example below:

  .. code-block:: bash

   ln -s /nfs-share/appliance-files/morpheus-ui /var/opt/morpheus/morpheus-ui



.. TIP:: when adding additional nodes you will only need to run step 7 and 8
