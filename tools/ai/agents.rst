.. _ai-agents:

AI Agents
---------

AI Agents define the behavior of the AI chat assistant. Each agent ties together a language model, a system prompt, and a set of tool providers (MCP servers). Multiple agents can be configured per account, with one designated as the default.

Navigate to :menuselection:`Tools --> AI Services --> AI Agents` to manage agents.

Creating an AI Agent
^^^^^^^^^^^^^^^^^^^^

Click :guilabel:`+ ADD` to create a new agent.

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Field
     - Description
   * - **Name**
     - A unique display name for the agent (e.g., "Infrastructure Assistant", "Dev Helper")
   * - **Description**
     - The system prompt that seeds the agent's behavior. This instructs the LLM on its role, personality, and constraints. Write clear instructions about what the agent should and should not do.
   * - **LLM Integration**
     - The language model provider to use (configured under Administration > Integrations)
   * - **Model**
     - The specific model from the selected integration (e.g., GPT-4o, Claude 3.5 Sonnet). Models are automatically discovered from the provider.
   * - **Include Local MCP**
     - When enabled (default), the agent has access to built-in Morpheus tools for querying and managing resources. Disable only if the agent should exclusively use external MCP servers.
   * - **Read-Only Tools**
     - When enabled, the agent can only invoke read/GET operations — it cannot create, modify, or delete resources regardless of user permissions.
   * - **Default**
     - Mark as the default agent for the account. Only one agent can be default. The default agent is used when users open the AI chat assistant without selecting a specific agent.
   * - **MCP Servers**
     - Select external MCP Servers to assign to this agent. The agent will have access to all tools provided by assigned servers.
   * - **Enabled**
     - Toggle to activate or deactivate the agent.

System Prompt Best Practices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The **Description** field serves as the system prompt. Effective prompts:

- Define the agent's role clearly (e.g., "You are an infrastructure operations assistant for the IT team")
- Specify constraints (e.g., "Never delete production resources without explicit confirmation")
- Provide context about the environment (e.g., "Our primary cloud is VMware vCenter named 'DC-East'")
- Set the communication style (e.g., "Be concise and technical, avoid unnecessary explanations")

Example::

    You are an infrastructure operations assistant for the Cloud Operations team.
    Our environment consists of VMware vCenter (production) and HVM clusters (dev/staging).
    Always confirm before making changes to production resources.
    Provide concise, actionable responses with relevant resource names and IDs.

Default Agent
^^^^^^^^^^^^^

Only one agent per account can be marked as **Default**. The default agent is used when:

- A user opens the AI chat assistant without specifying an agent
- API calls to ``/api/chat/message`` omit the ``agentId`` parameter

If no default is set, the system uses any enabled agent available to the account.

Agent Capabilities
^^^^^^^^^^^^^^^^^^

What an agent can do depends on:

1. **Include Local MCP** — gives access to built-in Morpheus operations
2. **Assigned MCP Servers** — adds external tool capabilities
3. **Read-Only Tools** setting — restricts to non-destructive operations
4. **User's AI Agentic Tools permission** — ``Read`` limits to read-only; ``Full`` allows writes
5. **Tool confirmation** — write operations require user approval before execution
