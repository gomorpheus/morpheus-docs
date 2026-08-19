HKS kube-vip
============

HKS can use the product-managed **Kube VIP** load balancer to provide a virtual IP address for a Kubernetes cluster. Kube VIP is available for Kubernetes Cluster layouts using VMware, vCloud Director, Xen, manual, KVM, and standard provision types.

Prerequisites and Configuration
-------------------------------

Select Kube VIP as the cluster load balancer and provide either:

- A **VIP Pool** from which |morpheus| acquires an address. The address must be accessible from every cluster node.
- A **VIP Address** that is unused and routable on the node network.

|morpheus| owns kube-vip configuration. During node configuration, it selects the appropriate master or worker script and writes the generated configuration to the node. Master nodes run kube-vip as a static Pod with leader election. Do not edit the generated ``/etc/kubernetes/manifests/kube-vip.yaml`` file; later |morpheus| operations can replace local changes.

Verification and Troubleshooting
--------------------------------

#. Confirm the cluster load balancer shows Kube VIP and the expected virtual IP.
#. From a system on the node network, verify that the virtual IP is reachable.
#. On each control-plane node, inspect the ``kube-system`` namespace and confirm its ``kube-vip-<node>`` Pod is running.
#. Verify the generated static Pod manifest references the expected image and virtual IP without modifying it.

If the virtual IP is unavailable, verify that it is unused, belongs to a network reachable by all nodes, and is not blocked by network policy or switching configuration. Review the cluster provisioning process output for the Kube VIP node-configuration step. On a multi-control-plane cluster, loss of the leader should cause another kube-vip Pod to acquire leadership; verify the virtual IP remains reachable before returning the cluster to service.
