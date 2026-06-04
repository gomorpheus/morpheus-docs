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

The following tool categories are available (subject to user permissions):

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Category
     - Description
   * - ``instances``
     - VMs, containers, and managed instances
   * - ``containers``
     - Container management within instances
   * - ``servers``
     - Bare-metal and virtual host servers
   * - ``clouds``
     - Cloud integrations (VMware, AWS, Azure, GCP, etc.)
   * - ``clusters``
     - Kubernetes, Docker Swarm, HVM clusters
   * - ``networks``
     - Networks, routers, firewalls, IP pools, DNS
   * - ``load-balancers``
     - Load balancers, pools, profiles
   * - ``storage``
     - Storage servers, volumes, buckets
   * - ``monitoring``
     - Checks, incidents, alerts
   * - ``logs``
     - Log retrieval and search
   * - ``tasks``
     - Automation tasks
   * - ``jobs``
     - Scheduled and on-demand jobs
   * - ``provisioning``
     - Service plans, virtual images, snapshots
   * - ``library``
     - Instance types, layouts, node types
   * - ``catalog``
     - Self-service catalog items
   * - ``blueprints``
     - App blueprints (ARM, CloudFormation, Terraform, Kubernetes)
   * - ``apps``
     - Multi-tier application deployments
   * - ``admin``
     - Appliance settings, tenants, users
   * - ``roles``
     - RBAC role management
   * - ``security``
     - Security groups, scan results
   * - ``credentials``
     - Credential store management
   * - ``policies``
     - Governance policies
   * - ``backups``
     - Backup jobs and restore operations
   * - ``billing``
     - Usage and billing
   * - ``costing``
     - Invoices, budgets, pricing
   * - ``integrations``
     - Third-party integrations
   * - ``vdi``
     - Virtual Desktop Infrastructure
   * - ``reports``
     - Report generation and retrieval
   * - ``guidance``
     - Optimization recommendations
   * - ``health``
     - Appliance health and diagnostics
   * - ``wiki``
     - Wiki pages
   * - ``search``
     - Global search

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
