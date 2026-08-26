Edge Site Management Strategy
==============================

Overview
--------

Large-scale deployments often span multiple geographic regions, data centers, and edge locations. |morpheus| supports a three-tier management architecture that scales from a single appliance to a fully federated multi-region deployment:

.. list-table::
   :widths: 20 30 50
   :header-rows: 1

   * - Tier
     - Component
     - Role
   * - Tier 1 — Federated Management
     - Morpheus Central
     - Single pane of glass across multiple regional |morpheus| Managers. Provides federated visibility, license management, and cross-region coordination.
   * - Tier 2 — Regional Management
     - |morpheus| Manager (Appliance)
     - Full lifecycle management for a region or data center. Handles provisioning, governance, automation, and user access for all clouds and infrastructure within its scope.
   * - Tier 3 — Edge Proxy
     - Distributed Workers
     - Lightweight proxy nodes deployed at edge locations, remote sites, or isolated network segments. Relay Cloud API traffic, Agent communication, console sessions, and quorum witness services back to the regional Manager.

Architecture
------------

.. code-block:: text

                    ┌─────────────────────────┐
                    │    Morpheus Central      │
                    │  (Federated Management)  │
                    └────────┬────────┬────────┘
                             │        │
                ┌────────────┘        └────────────┐
                │                                   │
      ┌─────────▼──────────┐             ┌─────────▼──────────┐
      │  Regional Manager  │             │  Regional Manager  │
      │   (Region A)       │             │   (Region B)       │
      └──┬──────┬──────┬───┘             └──┬──────┬──────┬───┘
         │      │      │                    │      │      │
         ▼      ▼      ▼                    ▼      ▼      ▼
      ┌─────┐┌─────┐┌─────┐             ┌─────┐┌─────┐┌─────┐
      │Edge ││Edge ││Edge │             │Edge ││Edge ││Edge │
      │Wrkr ││Wrkr ││Wrkr │             │Wrkr ││Wrkr ││Wrkr │
      └─────┘└─────┘└─────┘             └─────┘└─────┘└─────┘

Tier 3: Distributed Workers at the Edge
-----------------------------------------

Distributed Workers are the foundation of edge site management. Each Worker is a lightweight service deployed at a remote or edge location that maintains an outbound connection to its regional |morpheus| Manager. Workers proxy:

- **Cloud API traffic** — Communicates with local hypervisors (VMware, HVM, Nutanix, SCVMM, Hyper-V, OpenStack, etc.) on behalf of the regional Manager
- **Agent relay** — Relays |morpheus| Agent traffic from managed VMs back to the Manager
- **Console gateway** — Routes browser-based console sessions to local VMs without requiring direct connectivity from user browsers to the hypervisor network
- **HVM quorum witness** — Provides witness services for two-node or stretch HVM clusters at edge sites

**When to deploy a Worker at an edge site:**

- The regional Manager cannot directly reach the hypervisor management network at the edge location
- Agent traffic from edge VMs cannot route directly to the Manager
- Users need console access to VMs at edge sites without VPN
- Network segmentation or firewall policy requires all traffic to egress through a known endpoint
- HVM clusters at edge sites need a remote quorum witness for availability

**Deployment considerations:**

- Workers require only outbound HTTPS (TCP 443) to the regional Manager
- Multiple Workers can share the same Worker key for HA at a single edge site
- A single Worker can serve multiple roles (cloud proxy, console gateway, witness)
- Separate Workers per role may be preferred for fault isolation or independent scaling

For installation, configuration, and HA deployment details, see :doc:`/administration/integrations/workers`.

Tier 2: Regional Morpheus Managers
-----------------------------------

Each region, data center, or major campus operates its own |morpheus| Manager appliance (or HA appliance cluster). The regional Manager:

- Owns all cloud integrations, groups, and tenants for its scope
- Handles provisioning, automation, governance, and policy enforcement
- Manages its own set of Distributed Workers deployed at edge locations within the region
- Operates independently if connectivity to Morpheus Central is interrupted

**Sizing guidance:**

- A single Manager can manage thousands of VMs across many Distributed Workers
- Deploy additional regional Managers when geographic latency, compliance boundaries, or blast-radius requirements demand independent control planes
- Each Manager maintains its own database, elasticsearch, and RabbitMQ (or HA equivalents)

For appliance installation and HA configuration, see :doc:`/getting_started/ha/ha`.

Tier 1: Morpheus Central (Federated Management)
-------------------------------------------------

Morpheus Central provides a federated management layer that connects multiple regional Managers into a single organizational view:

- **Unified visibility** — View infrastructure, instances, and operations across all registered regions from a single interface
- **License management** — Centralized license allocation and consumption tracking across all Managers
- **Cross-region coordination** — Federated reporting, compliance visibility, and operational awareness

Each regional Manager registers with Morpheus Central via |AdmSet| (Morpheus Central tab). Registration requires outbound HTTPS connectivity from the Manager to the Central service.

.. note::

   Morpheus Central is a federated visibility and coordination layer. Each regional Manager retains full autonomy for provisioning, automation, and day-to-day operations. Central does not replace or override regional Manager functionality.

Deployment Patterns
--------------------

Single Region with Edge Sites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The simplest pattern: one Manager with multiple Workers at remote sites.

- 1 |morpheus| Manager (data center or central office)
- N Distributed Workers (one per edge site or remote network zone)
- Workers proxy cloud and agent traffic from edge hypervisors

Multi-Region with Edge Sites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For organizations spanning multiple geographies:

- 1 Morpheus Central instance
- N |morpheus| Managers (one per region)
- M Distributed Workers per region (at edge locations within each region)

This pattern provides:

- Regional autonomy (each Manager operates independently)
- Edge reach (Workers extend each Manager to remote sites)
- Federated oversight (Central provides cross-region visibility)

Compliance-Driven Segmentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For environments with strict data sovereignty or compliance boundaries:

- Separate Managers per compliance zone (e.g., one for EMEA, one for US)
- Workers within each zone cannot communicate with Managers in other zones
- Central provides visibility across zones without moving workload data across boundaries

Planning Checklist
-------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Question
     - Guidance
   * - How many geographic regions or compliance zones?
     - One Manager per region or zone
   * - How many edge sites per region?
     - One or more Workers per edge site (HA pairs for critical sites)
   * - Do edge sites have HVM clusters?
     - Deploy a Worker with witness capability (separate from cloud proxy if desired)
   * - Do users need console access to edge VMs?
     - Configure Workers as console gateways
   * - Is cross-region visibility required?
     - Deploy Morpheus Central
   * - What is the blast radius tolerance?
     - Separate Managers reduce the impact of a single Manager failure
