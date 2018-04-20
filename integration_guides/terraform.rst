Terraform
=========

.. IMPORTANT:: In |morpheus| versions 3.3.0 and 3.3.1 VMware cloud types are supported for Terraform App provisioning targets. Additional clouds will be available in later releases.

Requirements
------------

Role Access
^^^^^^^^^^^

* In order to see the Terraform Template type option and create Terraform App Templates in `Provisioning -> Templates`, the Morpheus user must have Role permissions for `Provisioning: Templates - Terraform` set to `Full`.

* In order to provision Terraform Apps in `Provisioning -> Apps`, the Morpheus user must have Role permissions for `Provisioning: Templates - Terraform` set to `Provision` or `Full`.

* Existing Terraform Templates must be added before they can be provisioned from `Provisioning -> Apps`.

* To use .tf files from a Git repo a Git or Github integration needs to be configured in `Administration - Integrations`. If one is not configured .tf or .tf.json files can be manually added to Terraform App Templates.


Terraform Installation
^^^^^^^^^^^^^^^^^^^^^^

|morpheus| will automatically install Terraform locally upon the first Terraform App provision. It is possible on some operating system configurations for the automated terraform to fail, in which case it can be manually installed (run ``terraform --version`` to verify).

To manually install and configure terraform on the Morpheus Appliance:

#. Run the following curl on the |morpheus| Appliance to install Terraform:

   .. code-block:: bash

    curl -k -s "https://applianceServerUrl/api/server-script/terraform-install?local=true" | bash


   .. NOTE:: Replace applianceServerUrl with your |morpheus| appliance url or ip.

#. Create a working directory for Terraform, and change owner to ``morpheus-app``.

   .. code-block:: bash

    sudo mkdir /var/opt/morpheus/morpheus-ui/terraform

    sudo chown morpheus-app.morpheus-app /var/opt/morpheus/morpheus-ui/terraform

   The default location is '``/var/opt/morpheus/morpheus-ui/terraform'`` but can be changed.

#. Add the Terraform working path to ``/opt/morpheus/conf/application.yml``

   .. code-block:: bash

    sudo vi /opt/morpheus/conf/application.yml

   Add the following to the applicaiton.yml config below the repo seciton:

   .. code-block:: bash

    terraform:
        location: '/var/opt/morpheus/morpheus-ui/terraform'

   .. IMPORTANT:: Uses spaces not tabs to indent or ui startup will fail. If you used a different path than the default location, use that path instead.

#. Restart the morpheus-ui to apply the ``application.yml`` config.

   .. code-block:: bash

    sudo morpheus-ctl restart morpheus-ui


Terraform is now installed and configured, and Terraform apps can be provisioned from Morpheus.


Creating Terraform Templates
----------------------------

In order to provision Terraform apps, Terraform App Templates must be created first.

.. IMPORTANT:: In |morpheus| versions 3.3.0 and 3.3.1 VMware cloud types are supported for Terraform App provisioning targets. Additional clouds will be available in later releases.

#. Navigate to `Provisioning -> Templates`
#. Select :guilabel:`+ ADD`
#. Name the Template and select `Terraform` type.

   .. NOTE:: In order to see the Terraform Template type option, the |morpheus| user must have Role permissions for `Provisioning: Templates - Terraform` set to `Full`.

#. Select :guilabel:`NEXT`
#. Configure the following:

   NAME
       Name of the
   DESCRIPTION
       Description for you App Templates shown in the Apps list (optional)
   CATEGORY
       App Category (optional)
   IMAGE
    Add reference image/picture for your App Template (optional)
    CONFIG TYPE
 CONFIG

 1
 ​

 TFVAR SECRET

 OPTIONS
