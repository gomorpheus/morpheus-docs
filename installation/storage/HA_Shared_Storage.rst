Shared Storage
^^^^^^^^^^^^^^

For configurations with 2 or more Applications Nodes, Shared Storage is required between the app nodes. Local Storage File Shares will need to be copied to a shared file system so all assets are available on all App nodes.

Assets
``````
* White label images
* Uploaded virtual images
* Deploy uploads
* Ansible Plays
* Terraform
* Morpheus backups

.. TIP:: Backups, deployments and virtual image storage locations can be overridden within the |morpheus|-ui.  You can find more information on storage here: `Storage Documentation <https://docs.morpheusdata.com/en/latest/integration_guides/storage/storage.html#storage>`_

To copy the ``morpheus-ui`` directory to the shared storage follow the below steps:

1. SSH into the Appliance
2. sudo su (or login as root)
3. cd into ``/var/opt/morpheus/``
4. Backup morpheus-ui directory by running the command below.  This will create a new directory in ``/var/opt/morpheus/`` called morpheus-ui-bkp and copy the contents of morpheus-ui into the new directory

   .. code-block:: bash

    cp -r morpheus-ui morpheus-ui-bkp

5. Move morpheus-ui to your shared storage. Example below:

   .. code-block:: bash

      mv morpheus-ui /nfs/appliance-files/

6. Mount your shared storage volume to ``/var/opt/morpheus/morpheus-ui``. How you mount it is dependent on what kind of storage it is. If you mount the volume after the package install, but before the reconfigure, then you don't need to copy anything to a backup.

7. SSH into the second Appliance and then Backup morpheus-ui directory by running

   .. code-block:: bash

      cp -r morpheus-ui morpheus-ui-bkp

.. TIP:: When adding additional nodes you will only need to run step 6 and 7

.. important:: NFS mounts require ``sync`` option when using Ansible integration with |morpheus| Agent command bus execution enabled.
