Terraform
=========

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

|morpheus| will automatically install Terraform locally upon the first Terraform App provision. It is possible on some operating system configurations for the automated terraform to fail, in which case it can be manually installed.

If Terraform on the |morpheus| appliance (again only it does not automatically install )

`/opt/morpheus/conf/application.yml`

terraform:
    location: '/var/opt/morpheus/morpheus-ui/terraform'


mkdir /var/opt/morpheus/morpheus-ui/terraform/

chown morpheus-app.morpheus-app /var/opt/morpheus/morpheus-ui/terraform/
