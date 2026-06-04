Getting Started
---------------

Setting up AI Services requires three steps: connecting an LLM provider, optionally adding external MCP servers, and configuring an AI Agent.

Prerequisites
^^^^^^^^^^^^^

- An active subscription to a supported LLM provider (OpenAI, Anthropic, Azure OpenAI, Google AI, Ollama, Mistral, etc.)
- API credentials for the LLM provider
- Role permission: **AI Services** set to ``Full``

Quick Setup
^^^^^^^^^^^

**Step 1: Add an LLM Integration**

Navigate to :menuselection:`Administration --> Integrations` and click :guilabel:`+ ADD`. Select an LLM provider type from the available options. Configure the API key and endpoint (provider-specific), then save. Models are automatically discovered from the provider.

See :ref:`LLM Integrations <llm-integrations>` for provider-specific configuration details.

**Step 2: Create an AI Agent**

Navigate to :menuselection:`Tools --> AI Services --> AI Agents` and click :guilabel:`+ ADD`. Configure:

- Select the LLM Integration added in Step 1
- Choose a model (e.g., GPT-4o, Claude 3 Opus)
- Write a system prompt describing the agent's role
- Enable "Include Local MCP" to give the agent access to built-in Morpheus tools
- Mark as **Default** to make this the account-wide assistant

See :ref:`AI Agents <ai-agents>` for full configuration details.

**Step 3: Use the AI chat assistant**

Once an AI Agent is configured and enabled, the AI chat widget becomes available to authenticated users. Click the chat icon to start a conversation.

Example prompts:

- "Show me all instances in the Production group"
- "What's the current CPU usage on my VMware cloud?"
- "Create a new Ubuntu instance on the Dev cluster"
- "List all failed backups from the last 24 hours"

Optional: Add External MCP Servers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To extend the AI's capabilities beyond built-in Morpheus operations, add external MCP servers:

Navigate to :menuselection:`Tools --> AI Services --> MCP Servers` and click :guilabel:`+ ADD`. Configure the server URL, protocol, and credentials.

See :ref:`MCP Servers <mcp-servers>` for details.
