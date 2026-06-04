.. _llm-integrations:

LLM Integrations
----------------

LLM (Large Language Model) Integrations connect Morpheus to language model providers. These integrations supply the AI reasoning capabilities that power AI Agents. LLM integrations are **added through Administration > Integrations** and appear as a read-only reference under Tools > AI Services > Integrations.

Navigate to :menuselection:`Tools --> AI Services --> Integrations` to view connected LLM providers.

Adding an LLM Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^

LLM integrations are managed from :menuselection:`Administration --> Integrations`:

1. Click :guilabel:`+ ADD`
2. Select an LLM provider type from the integration type list
3. Configure provider-specific settings (API key, endpoint, etc.)
4. Save the integration

After saving, Morpheus automatically discovers available models from the provider and syncs them. These models then appear in the **Model** dropdown when configuring AI Agents.

Supported Providers
^^^^^^^^^^^^^^^^^^^

LLM provider support is plugin-based. The following providers are available:

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

   Additional LLM providers can be added through the Morpheus plugin system as they become available.

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
