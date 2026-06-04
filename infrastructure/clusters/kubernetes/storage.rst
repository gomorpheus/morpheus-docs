.. _k8s-storage:

Kubernetes Storage Management
=============================

Overview
--------

The Storage tab on a Kubernetes Cluster detail page provides management of persistent storage resources within the cluster. |morpheus| syncs and manages StorageClasses, Persistent Volumes (PVs), Persistent Volume Claims (PVCs), ConfigMaps, and Secrets.

Navigate to the Storage tab via ``Infrastructure > Clusters > [cluster name] > Storage``.

.. NOTE:: Storage management requires ``Infrastructure: Clusters > Full`` Role permission.

Storage Classes
---------------

StorageClasses define the types of storage available in the cluster. They map to provisioners (e.g., OpenEBS, Rook/Ceph, AWS EBS, vSphere volumes) and define parameters for dynamically provisioned volumes.

Viewing Storage Classes
^^^^^^^^^^^^^^^^^^^^^^^

The Storage Classes subtab displays all StorageClasses synced from the cluster, including:

- **NAME** — StorageClass name
- **PROVISIONER** — The storage provisioner (e.g., ``kubernetes.io/no-provisioner``, ``openebs.io/local``, ``rook-ceph.rbd.csi.ceph.com``)
- **RECLAIM POLICY** — What happens to PVs when released (``Retain``, ``Delete``, ``Recycle``)
- **VOLUME BINDING MODE** — When volume binding occurs (``Immediate``, ``WaitForFirstConsumer``)
- **DEFAULT** — Whether this is the cluster's default StorageClass

.. IMPORTANT:: When using |morpheus| Kubernetes clusters with OpenEBS, ensure a default StorageClass is available so that Kubernetes specs or Helm templates using a default StorageClass for PVCs can be utilized.

Persistent Volumes (PVs)
------------------------

Persistent Volumes represent physical storage resources in the cluster that have been provisioned by an administrator or dynamically provisioned using a StorageClass.

Viewing Persistent Volumes
^^^^^^^^^^^^^^^^^^^^^^^^^^

The Volumes subtab shows:

- **NAME** — PV name
- **CAPACITY** — Storage size (e.g., ``10Gi``)
- **ACCESS MODES** — ``ReadWriteOnce``, ``ReadOnlyMany``, or ``ReadWriteMany``
- **RECLAIM POLICY** — ``Retain``, ``Delete``, or ``Recycle``
- **STATUS** — ``Available``, ``Bound``, ``Released``, or ``Failed``
- **CLAIM** — The PVC bound to this volume (if any)
- **STORAGE CLASS** — Associated StorageClass
- **NAMESPACE** — Namespace (if applicable)

Creating Persistent Volumes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To create a PV through |morpheus|:

#. Navigate to the Storage tab on the cluster detail page
#. Select the Volumes subtab
#. Click :guilabel:`+ ADD`
#. Configure:

   NAME
     Name for the Persistent Volume
   NAMESPACE
     Target namespace (optional for cluster-scoped PVs)
   STORAGE CLASS
     Select from available StorageClasses
   ACCESS MODE
     Select the access mode:

     - **ReadWriteOnce (RWO)** — Single node read-write
     - **ReadOnlyMany (ROX)** — Multi-node read-only
     - **ReadWriteMany (RWX)** — Multi-node read-write

   CAPACITY
     Storage size (e.g., ``10Gi``, ``100Gi``)

#. Select :guilabel:`SAVE`

Deleting Persistent Volumes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Deleting a PV from |morpheus|:

#. Select the PV from the Volumes list
#. Click :guilabel:`DELETE`
#. Confirm deletion

.. WARNING:: Deleting a PV that is bound to a PVC will first delete the associated claim. Use the ``Orphan`` propagation policy to retain the underlying storage data.

Persistent Volume Claims (PVCs)
-------------------------------

PVCs are requests for storage by a user. They consume PV resources and are namespace-scoped.

Viewing Volume Claims
^^^^^^^^^^^^^^^^^^^^^

The Volume Claims subtab displays:

- **NAME** — Claim name
- **NAMESPACE** — Namespace containing the claim
- **STATUS** — ``Pending``, ``Bound``, or ``Lost``
- **VOLUME** — The PV bound to this claim
- **CAPACITY** — Allocated storage size
- **ACCESS MODES** — Requested access modes
- **STORAGE CLASS** — Requested StorageClass

Creating Volume Claims
^^^^^^^^^^^^^^^^^^^^^^

To create a PVC:

#. Navigate to the Storage tab > Volume Claims subtab
#. Click :guilabel:`+ ADD`
#. Configure:

   NAME
     Claim name
   NAMESPACE
     Target namespace for the claim
   STORAGE CLASS
     Select a StorageClass (or leave blank for default)
   ACCESS MODE
     Requested access mode
   CAPACITY
     Requested storage size

#. Select :guilabel:`SAVE`

|morpheus| creates the PVC in the cluster. If dynamic provisioning is configured for the selected StorageClass, a PV will be automatically created and bound.

Deleting Volume Claims
^^^^^^^^^^^^^^^^^^^^^^

When deleting a PVC from |morpheus|:

- The PVC is removed from the cluster
- Behavior for the associated PV depends on the ``propagationPolicy``:

  - **Foreground** (default) — Both PVC and PV are deleted
  - **Orphan** — Only the PVC is deleted; the PV is retained with a ``Released`` status

ConfigMaps
----------

ConfigMaps store non-confidential configuration data as key-value pairs. They are synced and viewable on the Storage tab.

- View existing ConfigMaps per namespace
- Inspect key-value contents
- Create new ConfigMaps with arbitrary key-value data

Secrets
-------

Secrets store sensitive data such as passwords, tokens, and keys. They are synced from the cluster and displayed (values are masked by default).

- View existing Secrets per namespace
- Secret types include ``Opaque``, ``kubernetes.io/tls``, ``kubernetes.io/dockerconfigjson``, etc.
- Create new Secrets with encoded data

Storage Runtime Options
-----------------------

When provisioning a |morpheus| Kubernetes cluster, the storage runtime is configured via the Cluster Layout:

- **OpenEBS** — Default for many MKS layouts. Provides local and replicated storage.
- **Rook/Ceph** — Available on VMware Fusion and VMware layouts. Provides distributed block storage.
- **None** — External clusters or layouts that rely on cloud-native storage (EBS, Azure Disk, etc.)

The chosen storage runtime determines which StorageClasses are automatically configured on the cluster.
