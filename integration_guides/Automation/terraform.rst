Terraform
---------

Requirements
~~~~~~~~~~~~

Role Access
^^^^^^^^^^^

* In order to see the Terraform Blueprint type option and create Terraform App Blueprints in |LibBluApp|, the |morpheus| user must have Role permissions for `Provisioning: Blueprints - Terraform` set to `Full`.

* In order to provision Terraform Apps in |ProApp|, the Morpheus user must have Role permissions for `Provisioning: Blueprints > Terraform` set to `Provision` or `Full`.

* Existing Terraform Blueprints must be added before they can be provisioned from |ProApp|.

Github/Git Repo
^^^^^^^^^^^^^^^

* To use .tf files from a Git repo a Git or Github integration needs to be configured in |AdmInt|. If one is not configured .tf or .tf.json files can be manually added to Terraform App Blueprints.

Supported App Provisioning Targets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* VMware
* Amazon AWS
* Microsoft Azure
* Oracle Cloud

.. NOTE::  Additional clouds will be available in later releases.

Terraform Installation
^^^^^^^^^^^^^^^^^^^^^^

The first time you attempt to provision a Terraform App, you may come across an error indicating that Terraform is not installed:

.. code-block:: bash

  bash: line 1: terraform: command not found

- .. toggle-header:: :header: **Command Not Found Error Screenshot**

    .. image:: /images/integration_guides/automation/terraform/1commandNotFound.png

    |

This likely means you've not yet configured Terraform Settings within |morpheus| global settings. Navigate to |AdmSetPro| and scroll down to the Terraform Settings section. By default, the Terraform Runtime field is set to "Manual". When set this way, |morpheus| will attempt to use Terraform as installed on the appliance box and it may not be currently installed. To have |morpheus| manage the Terraform installation process for you and manage Terraform versioning on a per-App basis, set the Terraform Runtime to "Auto". You should also set the Default Terraform Version field as well. When a version is set on a Terraform Spec Template or Terraform App Blueprint, that version will supersede the default version indicated in global settings.

- .. toggle-header:: :header: **Configured Terraform Runtime Screenshot**

    .. image:: /images/integration_guides/automation/terraform/2configuredTfRuntime.png

    |

.. IMPORTANT:: |morpheus| appliances which do not have access to the Internet will need to leave Terraform Runtime settings on "Manual" and ensure Terraform is installed appropriately on the appliance.

Creating Terraform App Blueprints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to provision Terraform apps, Terraform App Blueprints must be created first.

.. IMPORTANT:: In |morpheus| version 4.2.0, VMware and AWS Cloud types are supported for Terraform App provisioning targets. Additional clouds will be available in later releases.

#. Navigate to |LibBluApp|
#. Select :guilabel:`+ ADD`
#. Name the Blueprint and select `Terraform` type.

   .. NOTE:: In order to see the Terraform Blueprint type option, the |morpheus| user must have Role permissions for `Provisioning: Blueprints - Terraform` set to `Full`.

#. Select :guilabel:`NEXT`
#. Configure the following:

   NAME
       Name of the
   DESCRIPTION
       Description for you App Blueprints shown in the Apps list (optional)
   CATEGORY
       App Category (optional)
   IMAGE
    Add reference image/picture for your App Blueprint (optional)
   CONFIG TYPE (select Terraform, Terraform.json, or Git Repository)
    Terraform (.tf)
     CONFIG
      Paste in the .tf contents in the config section. Variables will be presented as input fields during App provisioning, or auto-populated with matching values if contained in a selected TFVAR Secret file added to the Cypher service.
    Terraform JSON (.tf.json)
      Paste in .tf.json contents in the config section. Variables will be presented as input fields during App provisioning, or auto-populated with matching values if contained in a selected TFVAR Secret file added to the Cypher service.
    Git Repository
      SCM Integration
        Select a Github SCM integration that has been added in `Administration - Integrations`. If using a Git Repository integration from `Administration - Integrations` this filed can be skipped.
      Repository
        Select repository from selected SCM integration, or Git Repository integration from `Administration - Integrations` if no SCM/Github Integration is selected.
      BRANCH OR TAG
        i.e. master (default)
      WORKING PATH
        Enter the repo path for the .tf files (s). ``./`` is default.
      CONFIG
        .tf files found in the working path will populate in the CONFIG section.

        .. NOTE:: If no files are found please ensure your Github or Git integration is configured properly (Private repos need to have a key pair added to |morpheus|, the keypair selected on the integration in |morpheus|, and the keypair's public key added to the GitHub users SSH keys in github or to the git repo).
   TFVAR SECRET
    Select a tfvars secret for .tf variables. Tfvars secrets can be added in |TooCyp| using the tfvars/name mountpoint. This allows sensitive data and passwords to be encrypted and securely used with Terraform Blueprints.
   OPTIONS
    example ``-var 'instanceName=sampleTfApp'``

#. Select :guilabel:`SAVE`

Your Terraform App is ready to be provisioned from |ProApp|.

Cloud Profiles
^^^^^^^^^^^^^^

.. include:: ../../infrastructure/clouds/profiles.rst
  :start-after: .. begin_cloud_profiles
  :end-before: .. end_cloud_profiles

Provisioning Terraform Apps
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. NOTE:: An existing Terraform App Blueprints must be added to |LibBluApp| before it can be provisioned.

.. NOTE:: In order to provision Terraform Apps in |ProApp|, the Morpheus user must have Role permissions for `Provisioning: Blueprints - Terraform` set to `Provision` or `Full`.

#. Navigate to |ProApp|
#. Select :guilabel:`+ ADD`
#. Choose and existing Terraform App Blueprint
#. Select :guilabel:`NEXT`
#. Enter a NAME for the App and select the Group, Default Cloud and Environment (optional)
#. Select :guilabel:`NEXT`
#. Populate any required variables in the `Terraform Variables` section.
   ..TIP:: If the tf CONFIG data needs to be edited, select the `RAW` section, edit, and then select the `BUILDER` section again. The CONFIG changes from the RAW edit will be updated in the CONFIG section.
#. Select :guilabel:`COMPLETE`

The Terraform App will begin to provision.

Once provisioning is completed, note the TERRAFORM tab in the App details page (|ProApp| > select the App). This section contains State and Plan output:

.. image:: /images/apps/terraform/terraform_sample.png
