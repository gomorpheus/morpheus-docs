HKS Offline Provisioning and Upgrades
=====================================

HKS layouts that advertise offline support can use a configured image server instead of public image and package sources. This is separate from installing the |morpheus| appliance with its supplemental package; see :ref:`offline-installation` for appliance installation.

Preparation
-----------

#. Select an HKS Cluster Layout that supports offline provisioning and the required Kubernetes version. |morpheus| rejects offline mode for layouts that do not advertise offline support.
#. Obtain the release-approved offline manifest for the selected |morpheus| and HKS layout release. The required artifact categories are the node OS image or template, HKS layout/package metadata, Kubernetes and node-component packages, container-runtime packages, CNI/CSI and other cluster add-on images, Kubernetes control-plane and pause images, and any Agent packages used by the layout.
#. Stage every item from that manifest on the release-approved image server, registry, OS package repository, or |morpheus| image location named by the manifest. Use only the versions, registry/repository paths, and checksums supplied for that release. A universal bill of materials is not bundled with this guide and must not be inferred from another release.
#. Ensure every control-plane and worker node can resolve and reach the image server and the |morpheus| appliance. Configure local DNS, NTP, OS package repositories, and any registry credentials before provisioning.
#. Validate each downloaded artifact against its published checksum before importing it. Do not substitute a similarly named upstream artifact.
#. Record the manifest version, source URL, expected checksum, calculated checksum, and final staging location for every artifact. Do not begin provisioning while an item is missing, has no release-approved checksum, or does not match its checksum.

Provisioning
------------

#. Start the Kubernetes Cluster wizard and select a layout that supports offline provisioning.
#. In the advanced repository settings, select the cluster repository credentials and enable **Image Server**.
#. Complete the normal HKS network, node, and layout settings, then provision the cluster.
#. Follow the cluster process output. Confirm that package and image requests resolve to the staged repository and that no node requires internet egress.
#. When provisioning completes, confirm every node is Ready, system Pods are running, and the configured Kubernetes version matches the layout.

Offline Upgrades
----------------

Offline clusters use the versions available from enabled compatible layouts and run dedicated offline control-plane and worker upgrade scripts. Upgrades proceed one minor version at a time. Before starting, stage and verify the target release artifacts on the same image server, confirm the target layout is enabled, and ensure the repository remains reachable from every node.

During an upgrade, |morpheus| cordons nodes, upgrades control-plane nodes before workers, and returns successful nodes to service. Review :doc:`hks_node_maintenance` before upgrading. Afterward, confirm all nodes are Ready and report the target version.

Troubleshooting
---------------

- If offline mode is rejected, verify the selected layout supports offline provisioning.
- If no upgrade version appears, verify an enabled compatible layout exists for the next supported version and that its artifacts are staged.
- If registry validation fails, verify the image-server URL, credentials, certificate trust, DNS, and node-to-server network path.
- If package installation fails, verify the release-specific Debian repository URL and package versions on the image server.
- Use cluster History and process output to identify the node and artifact that failed. Do not temporarily enable internet access as a substitute for correcting an incomplete offline artifact set.
