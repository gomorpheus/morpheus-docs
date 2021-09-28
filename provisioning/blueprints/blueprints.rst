Blueprints
==========

Overview
--------

App Blueprints support a vast array of providers and configurations with programmatic markup or Infrastructure as Code capabilities. Blueprints configs can be manually added or scoped to a git repo. |morpheus| blueprints allows for full automation configuration, locked fields, tiered boots, and linked tiers with exported evars. All blueprints have permission settings for controlling group and tenant access.

Blueprint Types
---------------

- |morpheus|
- Terraform
- ARM (Azure)
- CloudFormation (AWS)
- Kubernetes
- Helm

.. include:: /provisioning/blueprints/morpheus.rst
.. include:: /provisioning/blueprints/terraform.rst
.. include:: /provisioning/blueprints/arm.rst
.. include:: /provisioning/blueprints/cloudFormation.rst
.. include:: /provisioning/blueprints/kubernetes.rst
.. include:: /provisioning/blueprints/helm.rst
