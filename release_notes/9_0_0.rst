.. _Release Notes:

**************************************
|morphver| |releasetype| Release Notes
**************************************

- Compatible Plugin API version: |pluginVer|
- Compatible |morpheus| Worker version: |workerVer|
- Minimum upgrade versions: Non-rolling: |minUpgradeVer|, Rolling: |minRollingUpgradeVer|

Release Dates

- |morphver| |releasedate|

.. important:: After upgrading to |morphver|, it is recommended to check for HVM Host agent upgrades as well. To upgrade HVM Host agents, navigate to the detail page for each HVM Host, expand the ACTIONS menu, and click "Upgrade Agent." This process must be undertaken on all HVM Hosts. Alternatively, you may select "Download Agent Script" to download a shell script to handle the upgrade. Connect to the HVM Host over a terminal session and run the downloaded script. The scripts are unique to each HVM Host so you must download all required scripts and run the correct script against the correct HVM Host. Though many do, it is possible that some version upgrade hops will not contain an HVM Host agent upgrade.

|

New Features
============

:Alletra MP Plugin: - For complete update details, see the HPE Storage Integration Pack for VM Essentials Release Notes

:AI and Automation: - Introduced a "Read-only mode" for AI agents and a corresponding RBAC permission that restricts agents to data retrieval only, preventing them from performing any modification or "agentic" actions
                    - Added a new management interface under Tools > AI Services for creating and configuring AI Agents, including model selection and MCP server assignments
                    - Added a management interface for Model Context Protocol (MCP) servers, allowing users to connect external tool providers to AI agents via STDIO or HTTP protocols
                    - Introduced a provider abstraction layer that supports integrating external LLM services like OpenAI and GitHub Copilot for use within the |morpheus| AI framework
                    - Enhanced AI Integration framework for LLM and MCP providers. Endpoints enable execution through Agent Tasks
                    - MCP Server Support for the enablement of AI assistants (including GitHub Copilot CLI and Claude Desktop) through a built-in MCP server exposing the |morpheus| REST API. Supports Streamable HTTP and legacy SSE transports
                    - Private Cloud system initialization wizard to streamline onboarding and provide an extensible plugin-compliant framework

:API & CLI: - Reintroduced and improved API token management with a dedicated API Keys tab in User Settings
            - Support for multiple auth tokens per user, enabling parallel operations across large federated deployments

:Aruba CX: - VLAN IDs specified in trunk ranges are now automatically configured on Aruba CX switches if they do not already exist, simplifying large-scale network provisioning
            - Standard networks now support hybrid and trunk-only modes, allowing multiple tagged VLANs to be carried over a single interface with corresponding automatic switch configuration
            - Security Groups integration for the ArubaCxDss network plugin

:HVM: - |morpheus| |morphver| includes a new cluster layout for HVM Clusters, version 1.3, which succeeds version 1.2. The primary difference in cluster layout 1.3 is the replacement of Pacemaker as the resource manager for GFS2 datastores (now known as HPE Clustered Datastores). Rather than Pacemaker observing the reported state of Corosync and making fencing decisions, the |morpheus| Agent becomes the high-availability control plane, providing even greater reliability for HPE Clustered Datastores in HVM Clusters
      - One-click upgrade to take existing 1.2 HVM Clusters to cluster layout version 1.3. For more information about upgrading HVM Clusters, see Cluster Layout Upgrade in the |morpheus| user manual
      - Added a type-ahead "Search servers" field and a general search field to the Backups History page to allow users to filter backup records by specific virtual machines or servers
      - Users can now modify advanced virtual machine options after deployment, including UEFI/BIOS firmware toggles, Secure Boot, and a new "Boot to BIOS" flag with a configurable timeout for troubleshooting
      - Enhanced the Dynamic Placement system with adjustable aggressiveness profiles (Conservative, Moderate, Aggressive) and migration cooldowns to better balance cluster resources based on memory utilization
      - Automated the injection of VirtIO drivers during bulk migrations from VMware to HVM, eliminating the need for manual driver preparation on Windows virtual machines
      - Stretched Cluster Support spanning multiple logical sites as a single cluster for both uniform and non-uniform configurations. Live Migration is supported for VMs enabled with Secure Boot
      - Guest OS Encryption (vTPM/SecureBoot) automated recovery from backup for VMs using BitLocker/vTPM
      - Memory Overallocation on HVM clusters
      - Support for Two-Node GFS2 clusters using an external quorum witness
      - Shared vDisks to assign vDisks to multiple guest VMs simultaneously
      - Allow VMs to boot via PXE/network boot for customers with established deployment automation workflows
      - Enable BIOS Asset Tag Configuration for VMs at creation and Day 2
      - Support audit logging and traceability in morphd for tracking of user identity for libvirt and virsh actions
      - SR-IOV network type to enable VMs to have direct, near wire-speed access to physical network adapters
      - Trunk VLAN Support for standard networks. Support for multiple VLAN traffic on a single interface (access, hybrid and trunk-only modes)
      - HVM Network Plugin for standard, private, data, and overlay. Enable decoupled networking management through dedicated plugin via the Network Provider framework

:Packaging: - |morpheus| appliance deb/rpm packages contain all files, agents, plugins, and dependencies. Supplemental packages are no longer required for installation or upgrades

:User Interface: - Added React UI for modernized navigation framework and administration

:Supportability: - End-to-end supportability, including support bundle generation, environment telemetry, health metrics, operational runbooks, and RBAC-controlled access
                 - Host Hardware Sensor Metrics Enhancements for improved metrics based on feedback

Fixes
=====

:Platform Updates: - Embedded MySQL updated to 8.4.x LTS; non-embedded support extended to 8.4.x or above

:Agent: - Fixed storage reporting errors on older Linux distributions and systems using btrfs subvolumes that resulted in zero or inflated storage usage values

:API & CLI: - Fixed an issue where the API and CLI did not correctly return all associated resource pools for networks assigned to multiple pools
            - Updated the default API token expiration for system clients (morph-api, morph-cli, and morph-customer) to 30 days to improve security posture

:HVM: - Fixed an issue where virtual machines on a data network with a 9000 MTU could not communicate using jumbo packets until the network interface was manually reset
      - The system now automatically enforces a single active heartbeat datastore per HVM Cluster to prevent failover ambiguity and quorum conflicts
      - Fixed a keyboard mapping issue that prevented the AltGr key from functioning correctly when using the console on HVM-based virtual machines
      - Creating HVM Active/Passive Bond mii-polling-rate, up-delay, and down-delay configurations now applied automatically during provisioning

Appliance & Agent Updates
=========================

:Node Packages: - |morpheus| Node and VM Node packages updated to |nodePackageVer|. Requires 3.5GB of storage for new packages. Run ``sudo rm -Rf /var/opt/morpheus/package-repos/*`` after package installation and before reconfigure to reclaim space from old packages if needed
:Linux Agent: - Updated to |linuxagentver|
:Windows Agent: - |winagentver| (no changes from |previousMorphVer|)
:macOS Agent: - |macagentver| (no changes from |previousMorphVer|)
:MySQL: - Embedded MySQL updated to 8.4.x LTS
:Tomcat: - Updated to |tcver|
:Plugin API: - Updated to |pluginVer|
:Packaging: - Supplemental packages are no longer required. All agents, plugins, and dependencies are included in the main deb/rpm package
