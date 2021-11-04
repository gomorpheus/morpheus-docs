App Blueprints
--------------

App Blueprints support a vast array of providers and configurations with programmatic markup or Infrastructure as Code capabilities. Blueprints configs can be manually added or scoped to a git repo. |morpheus| blueprints allows for full automation configuration, locked fields, tiered boots, and linked tiers with exported evars. All blueprints have permission settings for controlling group and tenant access.

App Blueprint Types
^^^^^^^^^^^^^^^^^^^

- |morpheus|
- Terraform
- ARM (Azure)
- CloudFormation (AWS)
- Kubernetes
- Helm

.. include:: /library/appBlueprints/blueprints/morpheus.rst
.. include:: /library/appBlueprints/blueprints/terraform.rst
.. include:: /library/appBlueprints/blueprints/arm.rst
.. include:: /library/appBlueprints/blueprints/cloudFormation.rst
.. include:: /library/appBlueprints/blueprints/kubernetes.rst
.. include:: /librar/appBlueprints/blueprints/helm.rst
