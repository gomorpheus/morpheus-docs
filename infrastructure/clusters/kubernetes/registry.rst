.. _k8s-registry:

Container Registry Integration
===============================

Overview
--------

|morpheus| provides container registry integration within Kubernetes clusters through the ``KubernetesRegistryService``. This allows Kubernetes workloads to pull images from private container registries configured in |morpheus|.

Container registries are managed as Docker Registry integrations and can be associated with Kubernetes clusters to enable authenticated image pulls.

Configuring Registry Integrations
----------------------------------

Adding a Docker Registry
^^^^^^^^^^^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Integrations``
#. Select :guilabel:`+ ADD`
#. Choose **Docker Registry**
#. Configure:

   NAME
     Friendly name for the registry
   REGISTRY URL
     Full URL to the registry (e.g., ``https://registry.example.com``, ``https://ghcr.io``)
   USERNAME
     Registry authentication username
   PASSWORD
     Registry authentication password/token

#. Select :guilabel:`SAVE`

Supported registry types include:

- Docker Hub
- Harbor
- Amazon ECR
- Azure Container Registry (ACR)
- Google Container Registry (GCR) / Artifact Registry
- GitLab Container Registry
- GitHub Container Registry (ghcr.io)
- Self-hosted Docker registries (v2 API)

Associating Registries with Clusters
-------------------------------------

Once a registry integration is configured, it can be used by Kubernetes clusters in two ways:

Image Pull Secrets
^^^^^^^^^^^^^^^^^^

|morpheus| can create Kubernetes ``imagePullSecrets`` in target namespaces to enable pods to authenticate with private registries:

1. The registry credentials are stored as a Kubernetes Secret of type ``kubernetes.io/dockerconfigjson``
2. The secret is referenced in pod specs or service accounts within the namespace
3. |morpheus| manages the lifecycle of these secrets when deploying workloads

Instance Provisioning
^^^^^^^^^^^^^^^^^^^^^

When provisioning container-based Instance Types to a Kubernetes cluster:

- |morpheus| injects the appropriate image pull secret into the pod specification
- The container image reference in the Instance Type configuration determines which registry is used
- Registry credentials are resolved automatically based on the image URL

Service Entry Management
-------------------------

The registry service manages Kubernetes service entries that track deployed services within the cluster:

Viewing Services
^^^^^^^^^^^^^^^^

Navigate to the cluster detail page > Network tab > Services subtab to view all registered services, including:

- Service name
- Namespace
- Service type (ClusterIP, NodePort, LoadBalancer)
- Cluster IP and external IPs
- Port mappings

Deleting Service Entries
^^^^^^^^^^^^^^^^^^^^^^^^

When removing workloads, |morpheus| automatically cleans up associated service entries from both the Kubernetes cluster and the |morpheus| registry.

Working with Private Images
-----------------------------

To deploy workloads using images from a private registry:

#. Ensure the registry is added as an integration in |morpheus|
#. When creating Instance Types or Kubernetes workloads that reference private images, |morpheus| automatically:

   - Creates the required ``imagePullSecret`` in the target namespace
   - Configures the pod spec to reference the secret
   - Handles credential rotation when registry passwords change

#. For Helm charts or raw Kubernetes specs, ensure your manifests reference the image pull secret name that |morpheus| creates, or configure the ``imagePullSecrets`` field in your pod spec/service account

Best Practices
--------------

- **Use dedicated service accounts:** Create service accounts with pre-configured image pull secrets rather than adding secrets to individual pods
- **Scope registries to namespaces:** Limit registry access to specific namespaces where the images are needed
- **Rotate credentials regularly:** When registry credentials are updated in |morpheus|, the corresponding Kubernetes secrets are updated on next sync
- **Use registry mirrors:** For air-gapped environments, configure a local registry mirror and add it as the integration endpoint
