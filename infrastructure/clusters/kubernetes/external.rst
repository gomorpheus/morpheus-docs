.. _k8s-external:

External Kubernetes Clusters
============================

Overview
--------

|morpheus| supports two primary modes of Kubernetes cluster management:

- **Provisioned Clusters** — Kubernetes clusters provisioned directly by |morpheus| using MKS (Morpheus Kubernetes Service) layouts
- **External Clusters** — Pre-existing Kubernetes clusters provisioned outside of |morpheus| and imported for management

This guide covers the differences between these approaches, the import process for external clusters, and the feature parity between the two.

Provisioned vs External Clusters
---------------------------------

.. list-table::
   :widths: 30 35 35
   :header-rows: 1

   * - Feature
     - Provisioned (MKS)
     - External
   * - Cluster lifecycle
     - Full (create, scale, upgrade, destroy)
     - Monitor and consume only
   * - Node management
     - Add/remove workers, resize
     - View only
   * - Agent installation
     - Automatic on all nodes
     - Not required
   * - Storage runtime
     - Configured via layout (OpenEBS, Rook)
     - Uses existing storage provisioners
   * - Network runtime
     - Configured via layout (Calico, Weave)
     - Uses existing CNI
   * - Kubernetes version
     - Controlled by layout version
     - Determined by external cluster
   * - Workload deployment
     - Full support
     - Full support
   * - Monitoring
     - Full (nodes + workloads)
     - Workloads + API-level metrics
   * - kubectl access
     - Yes (Control tab)
     - Yes (Control tab)
   * - Namespace management
     - Full CRUD
     - Full CRUD
   * - Helm/Spec deployment
     - Yes
     - Yes
   * - RBAC management
     - Yes
     - Yes (requires sufficient permissions)
   * - Upgrade cluster
     - Yes (via ACTIONS menu)
     - No (managed externally)

Importing an External Cluster
------------------------------

Prerequisites
^^^^^^^^^^^^^

Before importing an external cluster, prepare the following:

1. **Service Account** — Create a service account with cluster-admin privileges:

   .. code-block:: bash

     kubectl create serviceaccount morpheus

2. **Cluster Role Binding** — Bind the service account to cluster-admin:

   .. code-block:: bash

     kubectl create clusterrolebinding morpheus-admin \
       --clusterrole=cluster-admin \
       --serviceaccount=default:morpheus \
       --namespace=default

3. **API URL** — Retrieve the cluster API server URL:

   .. code-block:: bash

     kubectl config view --minify | grep server | cut -f 2- -d ":" | tr -d " "

4. **API Token** — Retrieve the service account token:

   .. code-block:: bash

     SECRET_NAME=$(kubectl get secrets | grep ^morpheus | cut -f1 -d ' ')
     kubectl describe secret $SECRET_NAME | grep -E '^token' | cut -f2 -d':' | tr -d " "

   .. NOTE:: For Kubernetes 1.24+, tokens are no longer auto-created for service accounts. Use ``kubectl create token morpheus`` or create a long-lived token Secret manually.

5. **Kube Config** (alternative) — Export the kubeconfig YAML for the cluster.

Import Process
^^^^^^^^^^^^^^

#. Navigate to ``Infrastructure > Clusters``
#. Select :guilabel:`+ ADD CLUSTER`
#. Choose **External Kubernetes Cluster**
#. Select a Group and click :guilabel:`NEXT`
#. Configure:

   CLOUD
     Select a previously-integrated Cloud (or any Cloud for general association)
   CLUSTER NAME
     Friendly name for the cluster in |morpheus|
   RESOURCE NAME
     Prefix for Kubernetes hosts shown in |morpheus| UI
   LAYOUT
     Select an External Kubernetes layout matching the cluster version
   API URL
     The cluster API server URL (from prerequisites)
   API TOKEN
     The service account token (from prerequisites)
   KUBE CONFIG
     Alternatively, paste the full kubeconfig YAML

#. Complete the wizard

|morpheus| will validate connectivity, sync namespaces, workloads, and storage, and begin ongoing monitoring.

Authentication Methods
^^^^^^^^^^^^^^^^^^^^^^

External clusters support two authentication methods:

- **API Token** — A bearer token from a Kubernetes service account. Simpler but requires manual rotation.
- **Kube Config** — Full kubeconfig YAML supporting certificate-based auth, OIDC, and other authentication providers.

At least one of API Token or Kube Config is required. If both are provided, the API Token takes precedence.

Post-Import Capabilities
-------------------------

Once imported, external clusters support:

- **Workload visibility** — All Pods, Deployments, Services, etc. are synced and viewable
- **Namespace management** — Create, view, and manage namespaces
- **kubectl access** — Execute commands from the Control tab
- **App deployment** — Deploy Helm charts and Kubernetes Spec blueprints
- **Storage management** — View and manage PVs, PVCs, and StorageClasses
- **RBAC** — View and manage roles, role bindings, and service accounts
- **Monitoring** — Events and logs are collected and viewable

Limitations of External Clusters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Cannot add or remove worker nodes through |morpheus|
- Cannot upgrade the Kubernetes version through |morpheus|
- No agent-based host metrics (CPU, memory at the node level)
- Cannot manage the underlying infrastructure (VMs, networks)
- Cluster provisioning logs are not available

Use Cases for External Clusters
--------------------------------

- **OpenShift integration** — Import managed OpenShift clusters for workload deployment
- **EKS/GKE/AKS brought externally** — Import cloud-managed clusters not provisioned through |morpheus|
- **On-premises clusters** — Import clusters built with kubeadm, Rancher, or other tools
- **Development clusters** — Import minikube or kind clusters for testing
- **Multi-cluster management** — Centralize visibility across heterogeneous Kubernetes environments

Troubleshooting
----------------

- **Connection refused:** Verify the API URL is accessible from the |morpheus| appliance over port 6443
- **Unauthorized:** Ensure the API token or kubeconfig credentials are valid and have cluster-admin permissions
- **Partial sync:** Some resources may not appear if the service account lacks list permissions on specific resource types
- **Namespace not visible:** The service account must have cluster-level list permissions (not just namespace-scoped)
