.. _llm-integrations:

LLM Integrations
----------------

LLM (Large Language Model) Integrations connect Morpheus to language model providers. These integrations supply the AI reasoning capabilities that power AI Agents.

Navigate to :menuselection:`Tools --> AI Services --> Integrations` to manage connected LLM providers.

Adding an LLM Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^

LLM integrations are managed from :menuselection:`Tools --> AI Services --> Integrations`:

1. Navigate to :menuselection:`Tools --> AI Services --> Integrations`
2. Click :guilabel:`+ New Integration`
3. From the :guilabel:`New Integration` dropdown, select a type

   .. note::

      Currently, all integration types consume the same configuration fields.

4. Configure the following fields:

   - :guilabel:`NAME` — A descriptive name for this integration
   - :guilabel:`ENABLED` — Check to activate the integration
   - :guilabel:`API ENDPOINT` — The URL for the provider's API endpoint
   - :guilabel:`CREDENTIALS` — Select **Local Credentials** to paste an API key directly, or select from the secure credential store (e.g., Cypher)

5. Save the integration

After saving, Morpheus automatically discovers available models from the provider and syncs them. These models then appear in the **Model** dropdown when configuring AI Agents.

Supported Providers
^^^^^^^^^^^^^^^^^^^

Morpheus ships with provider integrations pre-installed but more will be added over time. Additionally, new AI integrations can be added to the platform by users through custom plugin development.

The following providers are currently available:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Provider
     - Notes
   * - **GitHub Copilot**
     - GitHub Copilot integration. Requires GitHub Copilot subscription and authentication token.
   * - **Ollama (Local)**
     - Self-hosted open-source models (Llama, Mistral, DeepSeek, etc.). Requires Ollama server URL. No API key needed for local instances.
   * - **OpenAI-Compatible (Local)**
     - Any local LLM server that exposes an OpenAI-compatible API (e.g., LM Studio, vLLM, LocalAI). Configure with the local server endpoint URL.

.. note::

   Additional LLM providers can be added through the Morpheus plugin system. See the developer documentation for guidance on creating custom AI integration plugins.

Model Properties
^^^^^^^^^^^^^^^^

Discovered models include metadata to help select the appropriate model for your use case:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Property
     - Description
   * - **Context Window**
     - Maximum number of tokens the model can process in a single conversation (input + output)
   * - **Max Output Tokens**
     - Maximum tokens the model can generate in a single response
   * - **Speed Score**
     - Relative speed rating for response generation
   * - **Quality Score**
     - Relative quality/capability rating
   * - **Cost Score**
     - Relative cost per request/token

Usage Tracking
^^^^^^^^^^^^^^

LLM integrations track token and request usage:

- **Token Usage** — Total tokens consumed, remaining quota, and reset period
- **Request Usage** — Total requests made, remaining quota, and reset period

These metrics help monitor API consumption and manage costs. Usage data is visible on the integration detail page.

Choosing a Model
^^^^^^^^^^^^^^^^

When selecting a model for an AI Agent, consider:

- **Context window** — Larger windows allow longer conversations and more tool results. Models with 128K+ context windows are recommended for complex infrastructure queries.
- **Tool calling support** — Ensure the model supports function/tool calling (most modern models do). This is required for MCP tool invocation.
- **Speed vs. quality** — Faster models (GPT-4o-mini, Claude 3 Haiku) are better for frequent, simple queries. Higher-quality models (GPT-4o, Claude 3 Opus) are better for complex reasoning and multi-step operations.
- **Cost** — High-throughput environments with many users should consider cost per token carefully.
