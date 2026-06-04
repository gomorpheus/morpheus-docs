.. _mcp-servers:

MCP Servers
-----------

MCP (Model Context Protocol) Servers are external tool providers that expose capabilities to AI Agents. When an MCP server is connected, its tools become available for the AI to invoke during conversations — enabling the assistant to interact with external systems, databases, APIs, or custom workflows.

Morpheus includes a **built-in MCP server** that provides tools for managing Morpheus resources (instances, clouds, clusters, networks, etc.). External MCP servers extend this with additional capabilities.

Navigate to :menuselection:`Tools --> AI Services --> MCP Servers` to manage connections.

Adding an MCP Server
^^^^^^^^^^^^^^^^^^^^

Click :guilabel:`+ ADD` to connect a new MCP server.

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Field
     - Description
   * - **Name**
     - A unique display name for the server
   * - **Description**
     - Optional description of what tools this server provides
   * - **Protocol**
     - Transport protocol for communication (see below)
   * - **Service URL**
     - The connection endpoint — a URL for HTTP protocols, or a command path for STDIO
   * - **Credential**
     - Optional authentication credential (API Key, Bearer Token, or Username/Password)
   * - **Arguments**
     - For STDIO protocol only: JSON array of command-line arguments
   * - **Enabled**
     - Toggle to activate or deactivate the server

Protocols
^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Protocol
     - Description
   * - **Streamable HTTP** (recommended)
     - Modern HTTP-based transport with optional SSE streaming. Best for remote/cloud-hosted MCP servers. Uses a single endpoint URL.
   * - **SSE**
     - Legacy HTTP + Server-Sent Events dual-endpoint transport. Supported for backward compatibility with older MCP server implementations.
   * - **STDIO**
     - Local subprocess communication via stdin/stdout. Used for CLI tools or locally-running MCP servers. The Service URL is the command to execute; Arguments provides CLI args as a JSON array.

Tool Discovery
^^^^^^^^^^^^^^

When an MCP server is added or refreshed, Morpheus connects and discovers available tools by calling the server's ``tools/list`` endpoint. Discovered tools are cached and displayed with a tool count on the server listing.

To re-discover tools (e.g., after the server is updated with new capabilities), click the :guilabel:`Refresh` action on the server.

**Status indicators:**

- **OK** — Server is reachable and tools are discovered
- **Error** — Connection failed (check URL, credentials, and network access)
- **Unknown** — Discovery has not been attempted

Built-in Morpheus MCP Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Every Morpheus appliance exposes a built-in MCP server at ``{applianceUrl}/api/mcp``. This server:

- Cannot be deleted or modified
- Provides tools for common Morpheus operations (list instances, check status, run reports, etc.)
- Is automatically included when an AI Agent has **Include Local MCP** enabled
- Respects the user's existing Morpheus role permissions — the AI can only access resources the user can access

Authentication
^^^^^^^^^^^^^^

External MCP servers may require authentication. Supported credential types:

- **API Key** — Sent as a header or query parameter (depending on server implementation)
- **Bearer Token** — Sent as ``Authorization: Bearer <token>`` header
- **Username/Password** — HTTP Basic authentication

Credentials are stored securely and never exposed in the UI after initial configuration.

Example: Connecting a Remote MCP Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To connect a remote MCP server (e.g., a custom tool server for database operations):

1. Click :guilabel:`+ ADD`
2. Set **Name**: "Database Operations"
3. Set **Protocol**: Streamable HTTP
4. Set **Service URL**: ``https://mcp.internal.example.com/tools``
5. Set **Credential**: Select or create a Bearer Token credential
6. Click :guilabel:`SAVE`

After saving, tool discovery runs automatically. Assign the server to an AI Agent to make its tools available during conversations.
