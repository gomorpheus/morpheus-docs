AI Services
===========

|advanced-plus|

HPE Morpheus Enterprise includes an integrated AI assistant that helps operators manage infrastructure through natural language. The AI Services feature connects large language models (LLMs) to Morpheus capabilities via the Model Context Protocol (MCP), enabling conversational access to provisioning, monitoring, reporting, and infrastructure management.

AI Services is accessed from :menuselection:`Tools --> AI Services` and consists of three components:

- **AI Agents** — Configure the AI assistant's behavior, model selection, and tool access
- **MCP Servers** — Connect external tool providers that extend the AI's capabilities
- **LLM Integrations** — View connected language model providers

.. toctree::
   :maxdepth: 1

   getting_started.rst
   agents.rst
   ai_tasks.rst
   chatting.rst
   mcp_servers.rst
   llm_integrations.rst
   morpheus_mcp_server.rst

How It Works
------------

The AI assistant uses a layered architecture:

#. **Users interact** with the AI chat assistant — a chat interface available to authenticated users
#. **AI Agents** receive messages and route them to a configured **LLM** (language model)
#. The LLM can invoke **tools** exposed by MCP Servers to query or act on Morpheus resources
#. **Responses** are returned with context from the tools used

.. note::

   The built-in Morpheus MCP server provides tools for common operations (listing instances, checking cloud status, querying reports, etc.) without any external configuration.

Security & Permissions
----------------------

AI Services access is controlled by two role permissions:

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Permission
     - Access Levels
     - Description
   * - **AI Services** (``services-ai``)
     - None, Read, Full
     - Controls access to Tools > AI Services configuration. Read = view only; Full = create/edit/delete agents, MCP servers.
   * - **AI Agentic Tools** (``services-ai-agentic``)
     - None, Read, Full
     - Controls tool execution. Read = AI can only use read-only/GET tools; Full = AI can execute write/modify operations.

Additionally, individual AI Agents can be configured with **Read-Only Tools** mode, which restricts that agent to non-destructive operations regardless of the user's permission level.

Tool operations that modify resources (create, delete, reconfigure) require **user confirmation** before execution, providing a safety mechanism against unintended changes.
