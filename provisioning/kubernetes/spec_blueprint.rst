.. _k8s-spec-blueprint:

Kubernetes Spec Blueprint
=========================

Overview
--------

The Kubernetes Spec blueprint type allows deploying raw Kubernetes YAML manifests as |morpheus| Apps. Unlike Helm charts which use templating, Kubernetes Spec blueprints deploy standard Kubernetes resource definitions directly. This is managed by the ``KubernetesAppTemplateService``.

Kubernetes Spec blueprints support:

- Single or multi-document YAML manifests
- Any Kubernetes resource type (Deployments, Services, ConfigMaps, etc.)
- Git repository integration for manifest storage
- Template parameter substitution
- Preview of resources before deployment

Creating a Kubernetes Spec Blueprint
--------------------------------------

#. Navigate to |LibBlu| (Library > Blueprints)
#. Select :guilabel:`+ ADD`
#. Choose **Kubernetes Spec** as the blueprint type
#. Configure:

   NAME
     Friendly name for the blueprint
   DESCRIPTION
     Optional description
   CATEGORY
     Optional category for organization
   SOURCE
     Select the source for the Kubernetes manifests:

     - **Repository** — Git repository containing YAML files
     - **Path** — Subdirectory within the repository containing the manifests
     - **Spec** — Paste YAML directly into the blueprint configuration

   CONFIG TYPE
     Format of the specification: ``yaml`` (default)

#. Select :guilabel:`SAVE`

Manifest Structure
-------------------

Kubernetes Spec blueprints accept standard Kubernetes YAML. Multi-resource manifests are separated by ``---``:

.. code-block:: yaml

   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: nginx-deployment
     labels:
       app: nginx
   spec:
     replicas: 3
     selector:
       matchLabels:
         app: nginx
     template:
       metadata:
         labels:
           app: nginx
       spec:
         containers:
         - name: nginx
           image: nginx:1.21
           ports:
           - containerPort: 80
   ---
   apiVersion: v1
   kind: Service
   metadata:
     name: nginx-service
   spec:
     selector:
       app: nginx
     ports:
     - port: 80
       targetPort: 80
     type: LoadBalancer

Provisioning a Kubernetes Spec App
------------------------------------

#. Navigate to ``Provisioning > Apps``
#. Select :guilabel:`+ ADD`
#. Choose the Kubernetes Spec blueprint
#. Select :guilabel:`NEXT`
#. Configure:

   APP NAME
     Name for the deployed application
   GROUP
     Target Group
   DEFAULT CLOUD
     Cloud containing the target cluster
   RESOURCE POOL
     Kubernetes namespace for deployment

#. Select :guilabel:`NEXT`
#. Configure any template parameters if defined
#. Review the preview showing detected resources
#. Select :guilabel:`COMPLETE`

Resource Mapping
-----------------

When deploying a Kubernetes Spec blueprint, |morpheus| parses the YAML and creates corresponding resource records for each Kubernetes object. This enables:

- Individual resource tracking in the App detail view
- Status monitoring per resource
- Lifecycle management (delete individual resources or the entire App)
- Resource counts and relationship visualization

Supported resource types that are mapped include:

- Deployments
- StatefulSets
- DaemonSets
- Services
- ConfigMaps
- Secrets
- PersistentVolumeClaims
- Ingresses
- Jobs
- CronJobs
- ServiceAccounts
- Roles and RoleBindings

Preview and Validation
-----------------------

Before deployment, |morpheus| provides a preview of the resources that will be created:

- File list from the repository (if using Git source)
- Resource types and names parsed from the YAML
- Namespace assignment validation

This allows operators to verify the deployment before committing.

Git Repository Integration
----------------------------

When using a Git repository as the source:

- |morpheus| clones the repository at deployment time
- The specified path within the repo is scanned for ``.yaml`` and ``.yml`` files
- All YAML files in the path are combined and deployed as a single App
- Changes to the repository require redeployment (not auto-synced)

Managing Deployed Apps
-----------------------

Deployed Kubernetes Spec Apps support:

- **View resources** — See all created Kubernetes objects and their status
- **Delete** — Remove all resources created by the App from the cluster
- **Refresh** — Sync current state from the cluster

Kubernetes Spec vs Helm
------------------------

.. list-table::
   :widths: 30 35 35
   :header-rows: 1

   * - Aspect
     - Kubernetes Spec
     - Helm
   * - Templating
     - None (raw YAML)
     - Full Go template engine
   * - Values/Parameters
     - Limited substitution
     - Full values.yaml support
   * - Versioning
     - Via Git commits
     - Chart versions + release history
   * - Upgrade workflow
     - Redeploy
     - ``helm upgrade`` with history
   * - Rollback
     - Redeploy previous version
     - ``helm rollback`` to revision
   * - Complexity
     - Low — standard YAML
     - Medium — requires chart structure
   * - Dependencies
     - Manual
     - Chart dependencies (subcharts)
   * - Best for
     - Simple deployments, learning
     - Complex apps, repeated deployments

Choose Kubernetes Spec blueprints for straightforward deployments with standard YAML manifests. Use Helm blueprints for applications requiring parameterization, complex dependency management, or upgrade/rollback workflows.
