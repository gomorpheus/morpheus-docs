.. _morpheus-mcp-server:

Morpheus MCP Server
-------------------

Every HPE Morpheus Enterprise appliance exposes a built-in MCP (Model Context Protocol) server at ``/api/mcp``. This endpoint allows external AI tools — such as Claude Desktop, VS Code Copilot, cursor, or custom automation scripts — to interact with Morpheus using the same tool-calling interface that powers the built-in AI chat.

The MCP server provides access to the full Morpheus API surface through categorized tools, with dynamic loading to keep initial responses lightweight. All operations respect the authenticated user's existing RBAC permissions.

Endpoint
^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 15 25 60

   * - Method
     - Path
     - Purpose
   * - POST
     - ``/api/mcp``
     - JSON-RPC 2.0 message endpoint (Streamable HTTP transport)
   * - GET
     - ``/api/mcp``
     - SSE stream for server-to-client notifications
   * - DELETE
     - ``/api/mcp``
     - Session termination
   * - GET
     - ``/api/mcp/sse``
     - Legacy SSE transport (for older MCP clients)
   * - POST
     - ``/api/mcp/messages``
     - Legacy SSE message endpoint

The server implements **MCP protocol version 2025-06-18** with Streamable HTTP as the primary transport.

.. important::

   Your Morpheus appliance **must have a valid, signed SSL certificate** configured for external MCP clients to connect. Self-signed or untrusted certificates will cause TLS verification failures in MCP clients (Claude Desktop, VS Code, etc.) that cannot be easily bypassed. See :ref:`SSL Certificates` for configuration details.

Authentication
^^^^^^^^^^^^^^

External clients authenticate using the same mechanisms as the Morpheus REST API:

- **Bearer Token** — ``Authorization: Bearer <your-api-token>`` header (recommended)
- **Access Token** — ``?access_token=<token>`` query parameter
- **Execution Token** — ``Authorization: Execution <token>`` header (for task/job contexts)

All tool executions enforce the authenticated user's role permissions. A user can only access tools and resources their Morpheus role allows.

Connecting External Clients
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Claude Desktop, Cursor, VS Code, or any MCP-compatible client:**

.. code-block:: json

   {
     "mcpServers": {
       "morpheus": {
         "url": "https://your-morpheus-host/api/mcp",
         "headers": {
           "Authorization": "Bearer your-api-token-here"
         }
       }
     }
   }

**Custom scripts (Python, Node, etc.):**

Any HTTP client that supports the MCP Streamable HTTP transport can connect. Send a ``POST`` to ``/api/mcp`` with a JSON-RPC 2.0 ``initialize`` message to start a session, then use the returned ``Mcp-Session-Id`` header on subsequent requests.

Session Management
^^^^^^^^^^^^^^^^^^

- Sessions are created on successful ``initialize`` handshake
- The server returns a ``Mcp-Session-Id`` response header — include this on all subsequent requests
- Sessions expire after **1 hour** of inactivity
- Use ``DELETE /api/mcp`` with the session header to explicitly terminate a session

Dynamic Tool Loading
^^^^^^^^^^^^^^^^^^^^

The MCP server uses **progressive category loading** to keep the initial tool list manageable for LLMs (max 120 tools per response). On first connection, clients see:

**Meta-tools** (always available):

- ``get_tool_details`` — Get detailed documentation for a specific tool
- ``search_external_tools`` — Discover tools from connected external MCP servers
- ``load_external_tools`` — Make discovered external tools callable in the session
- ``get_result_excerpt`` — Retrieve excerpted portions of large results
- ``delegate_to_specialist`` — Route requests to specialist tool categories

**Category loader tools** (one per category):

- ``use_instances_tools`` — Load VM/container instance management tools
- ``use_clouds_tools`` — Load cloud integration tools
- ``use_networks_tools`` — Load network management tools
- ``use_clusters_tools`` — Load cluster management tools
- (and so on for each category)

When an LLM calls a category loader (e.g., ``use_instances_tools``), the tools for that category become visible in subsequent ``tools/list`` calls. The server sends a ``notifications/tools/list_changed`` notification so clients know to re-fetch the tool list.

Tool Categories
^^^^^^^^^^^^^^^

The following 60 tool categories are available (subject to user permissions):

.. list-table::
   :header-rows: 1
   :widths: 20 10 70

   * - Category
     - Tools
     - Description
   * - ``networks``
     - 178
     - Networks, subnets, routers, DNS, DHCP, IP pools, proxies, firewall rules
   * - ``clusters``
     - 115
     - Kubernetes/Docker clusters, namespaces, pods, volumes, services, datastores
   * - ``library``
     - 70
     - Instance type layouts, container types, option types, spec templates, file templates, scripts
   * - ``instances``
     - 61
     - VM and container instances — CRUD, power actions, snapshots, cloning, resize
   * - ``admin``
     - 53
     - Appliance settings, health, ping, setup, tenants, maintenance mode
   * - ``load-balancers``
     - 48
     - Load balancers, virtual servers, pools, profiles, monitors
   * - ``monitoring``
     - 45
     - Monitoring checks, check groups, check apps, incidents, alerts
   * - ``clouds``
     - 44
     - Cloud integrations, cloud datastores, cloud folders, resource pools, security groups
   * - ``servers``
     - 33
     - Bare-metal hosts, hypervisors, managed servers — CRUD and power actions
   * - ``provisioning``
     - 26
     - Provision types, virtual images, pricing/service plans
   * - ``storage``
     - 24
     - Storage servers, storage volumes, storage buckets, file shares
   * - ``deployments``
     - 23
     - App deployments, deployment versions, deployment files
   * - ``backups``
     - 21
     - Backups, backup results, backup restores, backup settings
   * - ``vdi``
     - 20
     - Virtual desktop pools, VDI gateways, VDI allocations
   * - ``catalog``
     - 18
     - Self-service catalog types, catalog orders, cart items, checkout, inventory
   * - ``apps``
     - 17
     - Morpheus apps (multi-tier), app lifecycle, app security groups, wiki
   * - ``roles``
     - 16
     - Roles and role permissions management
   * - ``integrations``
     - 16
     - Third-party integrations (ITSM, IPAM, DNS, CM, etc.)
   * - ``groups``
     - 16
     - Infrastructure groups, group clouds, group wiki
   * - ``tasks``
     - 14
     - Automation tasks — shell scripts, HTTP, Ansible, Puppet, Chef, etc.
   * - ``jobs``
     - 14
     - Scheduled jobs and job executions
   * - ``billing``
     - 14
     - Billing, invoices, invoice line items
   * - ``archives``
     - 14
     - Archive buckets and archive files
   * - ``containers``
     - 12
     - Container/node actions — start, stop, restart, suspend, attach logs
   * - ``credentials``
     - 11
     - Credential store — CRUD for stored credentials
   * - ``security``
     - 10
     - Security scans and security packages
   * - ``user-settings``
     - 9
     - Current user settings and preferences
   * - ``power-schedules``
     - 9
     - Power schedule policies for automated start/stop
   * - ``options``
     - 9
     - Options API for dynamic form lookups (network options, zone options, etc.)
   * - ``guidance``
     - 8
     - Cost and resource optimization recommendations
   * - ``logs``
     - 7
     - Log search and cluster log retrieval
   * - ``image-builds``
     - 7
     - Image build pipelines and image build executions
   * - ``blueprints``
     - 7
     - Blueprints (app templates) CRUD
   * - ``wiki``
     - 6
     - Wiki pages — server, cloud, group, cluster, instance wiki
   * - ``user-sources``
     - 6
     - Identity sources (LDAP, SAML, etc.)
   * - ``reports``
     - 6
     - Report types, report execution and results
   * - ``provisioning-licenses``
     - 6
     - Software license management and license reservations
   * - ``policies``
     - 6
     - Governance policies
   * - ``migrations``
     - 6
     - Hypervisor console/migration tools
   * - ``environments``
     - 6
     - Environment tags (dev, staging, production, etc.)
   * - ``whitelabel-settings``
     - 5
     - Appliance white-labeling / branding
   * - ``user-groups``
     - 5
     - User groups management
   * - ``scale-thresholds``
     - 5
     - Auto-scale threshold definitions
   * - ``resource-pools``
     - 5
     - Resource pool / compute zone management
   * - ``prices``
     - 5
     - Price definitions for billing
   * - ``price-sets``
     - 5
     - Price set groupings
   * - ``preseed-scripts``
     - 5
     - Preseed/unattend scripts for OS automation
   * - ``email-templates``
     - 5
     - Email notification templates
   * - ``clients``
     - 5
     - OAuth client management
   * - ``certificates``
     - 5
     - SSL certificate management
   * - ``budgets``
     - 5
     - Budget definitions and tracking
   * - ``boot-scripts``
     - 5
     - Boot scripts for bare-metal provisioning
   * - ``approvals``
     - 5
     - Approval requests and approval actions
   * - ``license``
     - 4
     - Morpheus license management
   * - ``key-pairs``
     - 4
     - SSH key pair management
   * - ``execution``
     - 3
     - Execution request / remote command execution
   * - ``public-archives``
     - 2
     - Public archive file links
   * - ``forgot``
     - 2
     - Password reset / forgot password
   * - ``search``
     - 1
     - Global search across all resource types
   * - ``costing``
     - \-
     - Invoices, budgets, pricing, and cost management
   * - ``health``
     - \-
     - Appliance health and diagnostics
   * - ``network-pools``
     - \-
     - IPAM — network pools, pool servers, IP addresses

Common Filter Presets
^^^^^^^^^^^^^^^^^^^^^

Use the ``X-Mcp-Tool-Categories`` header to load only the categories relevant to your use case. The following presets cover common scenarios:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Use Case
     - Categories
   * - VM Operations
     - ``instances,servers,clouds,networks,monitoring``
   * - Kubernetes
     - ``clusters,instances,clouds,networks,storage``
   * - Service Catalog
     - ``catalog,provisioning,library,options``
   * - Networking
     - ``networks,load-balancers,security,certificates``
   * - Cost Management
     - ``billing,budgets,guidance,prices,price-sets``
   * - Automation
     - ``tasks,jobs,execution,power-schedules,scale-thresholds``
   * - Administration
     - ``admin,roles,user-groups,user-sources,user-settings,license``
   * - Provisioning
     - ``instances,clouds,library,options,provisioning,networks,groups,resource-pools``
   * - Full Operations
     - ``instances,servers,clouds,clusters,networks,monitoring,tasks,jobs``

Available Tools
^^^^^^^^^^^^^^^

The MCP server exposes **1112 tools** providing full coverage of the Morpheus REST API. All tool calls execute with the permissions of the authenticated user.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Area
     - Example Tools
   * - Instances
     - ``list_instances``, ``get_instance``, ``create_instance``, ``delete_instance``, ``start_instance``, ``stop_instance``, ``restart_instance``, ``resize_instance``, ``snapshot_instance``, ``clone_instance``
   * - Servers
     - ``list_servers``, ``get_server``, ``create_server``, ``delete_server``, ``start_server``, ``stop_server``, ``resize_server``
   * - Clouds
     - ``list_clouds``, ``get_cloud``, ``create_cloud``, ``delete_cloud``, ``refresh_cloud``
   * - Clusters
     - ``list_clusters``, ``get_cluster``, ``create_cluster``, ``delete_cluster``, ``list_cluster_namespaces``, ``list_cluster_pods``
   * - Networks
     - ``list_networks``, ``get_network``, ``create_network``, ``delete_network``, ``list_subnets``, ``create_subnet``
   * - Monitoring
     - ``list_checks``, ``get_check``, ``create_check``, ``list_incidents``, ``list_alerts``
   * - Automation
     - ``list_tasks``, ``get_task``, ``create_task``, ``execute_task``, ``list_jobs``, ``execute_job``
   * - Catalog
     - ``list_catalog_items``, ``get_catalog_item``, ``create_catalog_order``, ``checkout_catalog``
   * - Admin
     - ``whoami``, ``list_users``, ``get_user``, ``list_accounts``, ``get_appliance_settings``
   * - Search
     - ``search``

Session Customization Headers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Control tool visibility and behavior with request headers on the ``initialize`` call:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Header
     - Description
   * - ``X-Mcp-Tool-Categories``
     - Comma-separated category list. Only specified categories are loaded immediately (bypasses progressive loading). Example: ``instances,clouds,networks``
   * - ``X-Mcp-External-Server-Ids``
     - Comma-separated IDs of external MCP servers to include in this session
   * - ``X-Mcp-Include-Local-Tools``
     - Set to ``false`` to hide all built-in Morpheus tools (only external tools visible)
   * - ``X-Mcp-Read-Only-Tools``
     - Set to ``true`` to restrict to read-only/GET operations only

Example: Restricting to Infrastructure Tools Only
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For a client that should only manage infrastructure:

.. code-block:: json

   {
     "mcpServers": {
       "morpheus-infra": {
         "url": "https://your-morpheus-host/api/mcp",
         "headers": {
           "Authorization": "Bearer your-api-token",
           "X-Mcp-Tool-Categories": "instances,clouds,clusters,networks,storage"
         }
       }
     }
   }

Example: Read-Only Monitoring Client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For a monitoring dashboard that should never modify resources:

.. code-block:: json

   {
     "mcpServers": {
       "morpheus-monitor": {
         "url": "https://your-morpheus-host/api/mcp",
         "headers": {
           "Authorization": "Bearer your-api-token",
           "X-Mcp-Tool-Categories": "monitoring,logs,health,reports",
           "X-Mcp-Read-Only-Tools": "true"
         }
       }
     }
   }

Security Considerations
^^^^^^^^^^^^^^^^^^^^^^^

- All tool calls execute with the authenticated user's permissions — the MCP server cannot bypass RBAC
- Write operations in the built-in AI chat require user confirmation; external MCP clients bypass this (the client's LLM handles confirmation)
- Use ``X-Mcp-Read-Only-Tools: true`` for untrusted or automated clients
- API tokens used for MCP should be scoped to the minimum required role
- Sessions are isolated per user — no cross-user data leakage

Exposing to External MCP Clients
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section provides step-by-step instructions for connecting external MCP clients to your Morpheus appliance.

Generate a Morpheus API Token
"""""""""""""""""""""""""""""

To authenticate external MCP clients, you need a Morpheus API token.

**Via the Morpheus UI:**

1. Navigate to **User Settings > API Keys** tab
2. Click **+ADD**
3. Provide a descriptive name (e.g., ``mcp-claude-desktop``)
4. Select the appropriate **Client ID**
5. Click **Save** and copy the generated key

**Via curl:**

.. code-block:: bash

   curl -X POST "https://your-morpheus-host/oauth/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=password&scope=write&client_id=morph-api&username=YOUR_USER&password=YOUR_PASS"

The response contains an ``access_token`` field that you use as your Bearer token.

Configure GitHub Copilot CLI
""""""""""""""""""""""""""""

**Option A: Project-level configuration**

Create or edit ``.github/copilot-mcp.json`` in your project root:

.. code-block:: json

   {
     "mcpServers": {
       "morpheus": {
         "type": "http",
         "url": "https://your-morpheus-host/api/mcp",
         "headers": {
           "Authorization": "Bearer YOUR_API_TOKEN"
         }
       }
     }
   }

**Option B: User-level configuration**

Create or edit ``~/.config/github-copilot/mcp.json``:

.. code-block:: json

   {
     "mcpServers": {
       "morpheus": {
         "type": "http",
         "url": "https://your-morpheus-host/api/mcp",
         "headers": {
           "Authorization": "Bearer YOUR_API_TOKEN"
         }
       }
     }
   }

Configure Claude Desktop
""""""""""""""""""""""""

Edit the Claude Desktop configuration file:

- **macOS:** ``~/Library/Application Support/Claude/claude_desktop_config.json``
- **Windows:** ``%APPDATA%\Claude\claude_desktop_config.json``

.. code-block:: json

   {
     "mcpServers": {
       "morpheus": {
         "type": "http",
         "url": "https://your-morpheus-host/api/mcp",
         "headers": {
           "Authorization": "Bearer YOUR_API_TOKEN"
         }
       }
     }
   }

Configure OpenCode
""""""""""""""""""

**Option A: Manual configuration**

Edit ``opencode.json`` in your project root:

.. code-block:: json

   {
     "mcp": {
       "morpheus": {
         "type": "remote",
         "url": "https://your-morpheus-host/api/mcp",
         "headers": {
           "Authorization": "Bearer YOUR_API_TOKEN"
         }
       }
     }
   }

.. note::

   OpenCode uses ``"type": "remote"`` for HTTP-based MCP servers, rather than ``"type": "http"`` used by other clients.

**Option B: CLI**

Run ``opencode mcp add`` and provide:

- **Name:** ``morpheus``
- **Type:** ``remote``
- **URL:** ``https://your-morpheus-host/api/mcp``
- **Headers:** ``Authorization: Bearer YOUR_API_TOKEN``

Configure Generic MCP Clients
""""""""""""""""""""""""""""""

**Streamable HTTP (recommended):**

Send a ``POST`` request to ``https://your-morpheus-host/api/mcp`` with:

- Header: ``Authorization: Bearer YOUR_API_TOKEN``
- Header: ``Content-Type: application/json``
- Body: JSON-RPC 2.0 messages

**Legacy SSE transport:**

For older MCP clients that require Server-Sent Events:

- **SSE URL:** ``https://your-morpheus-host/api/mcp/sse``
- **Message URL:** ``https://your-morpheus-host/api/mcp/messages``

Both endpoints require the ``Authorization: Bearer YOUR_API_TOKEN`` header.

.. _ssl-certificates:

SSL/TLS Certificates
^^^^^^^^^^^^^^^^^^^^

.. important::

   Most MCP clients require a valid, trusted SSL certificate. Self-signed or untrusted certificates will cause TLS verification failures that cannot be easily bypassed in most MCP client implementations.

Using a Trusted Certificate (Recommended)
""""""""""""""""""""""""""""""""""""""""""

The recommended approach is to configure your Morpheus appliance with a certificate from a trusted Certificate Authority (CA). This ensures all MCP clients can connect without additional configuration.

Self-Signed Certificates
"""""""""""""""""""""""""

If you must use a self-signed certificate, add it to your operating system's trust store:

**macOS:**

.. code-block:: bash

   sudo security add-trusted-cert -d -r trustRoot \
     -k /Library/Keychains/System.keychain /path/to/morpheus-cert.pem

**Linux:**

.. code-block:: bash

   sudo cp /path/to/morpheus-cert.pem /usr/local/share/ca-certificates/morpheus.crt
   sudo update-ca-certificates

**Windows (PowerShell):**

.. code-block:: bash

   Import-Certificate -FilePath "C:\path\to\morpheus-cert.pem" -CertStoreLocation Cert:\LocalMachine\Root

**Node.js-based clients:**

For MCP clients built on Node.js, set the following environment variable:

.. code-block:: bash

   export NODE_EXTRA_CA_CERTS=/path/to/morpheus-cert.pem

Verifying the Connection
^^^^^^^^^^^^^^^^^^^^^^^^

Use the following curl commands to verify your MCP server is accessible and responding correctly.

**Initialize a session:**

.. code-block:: bash

   curl -X POST "https://your-morpheus-host/api/mcp" \
     -H "Authorization: Bearer YOUR_API_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-06-18", "clientInfo": {"name": "curl-test", "version": "1.0"}}}'

**List available tools:**

.. code-block:: bash

   curl -X POST "https://your-morpheus-host/api/mcp" \
     -H "Authorization: Bearer YOUR_API_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc": "2.0", "id": 2, "method": "tools/list"}'

**List tools filtered by category:**

.. code-block:: bash

   curl -X POST "https://your-morpheus-host/api/mcp?toolCategories=instances,clouds" \
     -H "Authorization: Bearer YOUR_API_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc": "2.0", "id": 2, "method": "tools/list"}'

**Call a tool:**

.. code-block:: bash

   curl -X POST "https://your-morpheus-host/api/mcp" \
     -H "Authorization: Bearer YOUR_API_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "whoami", "arguments": {}}}'

Example Usage
^^^^^^^^^^^^^

Once an MCP client is configured and connected, you can interact with Morpheus using natural language. Example prompts:

- "List all running instances in my VMware cloud"
- "What's the health status of the appliance?"
- "Show me recent failed provisioning processes"
- "Search for instances named 'web-prod'"
- "Execute task 42 on instance 100"
- "Who am I logged in as?"
- "Create a new Ubuntu instance on my VMware cloud"

Architecture
^^^^^^^^^^^^

The MCP server acts as an API gateway — tool calls are proxied to the existing Morpheus REST API internally using the caller's Bearer token. This means:

- **All existing permissions are enforced** — the MCP layer does not grant any additional access beyond what the user's role allows
- **No new service dependencies** — the MCP layer is thin and stateless, running within the Morpheus appliance itself
- **Full API parity** — every tool maps to a documented REST API endpoint, ensuring consistent behavior between MCP tool calls and direct API usage
