App Blueprints
--------------

App Blueprints support a vast array of providers and configurations with programmatic markup or Infrastructure as Code capabilities. Blueprints configs can be manually added or scoped to a git repo. |morpheus| blueprints allows for full automation configuration, locked fields, tiered boots, and linked tiers with exported evars. All blueprints have permission settings for controlling group and tenant access.

App Blueprint Types
 - |morpheus|
 - Terraform
 - ARM (Azure)
 - CloudFormation (AWS)
 - Kubernetes
 - Helm

.. toctree::
      :glob:

      /library/blueprints/appBlueprints/*



.. include:: /library/blueprints/appBlueprints/morpheus.rst
.. include:: /library/blueprints/appBlueprints/terraform.rst
.. include:: /library/blueprints/appBlueprints/arm.rst
.. include:: /library/blueprints/appBlueprints/cloudFormation.rst
.. include:: /library/blueprints/appBlueprints/kubernetes.rst
.. include:: /librar/blueprints/appBlueprints/helm.rst