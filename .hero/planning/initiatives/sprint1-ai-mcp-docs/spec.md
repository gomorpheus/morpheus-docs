---
type: initiative
slug: sprint1-ai-mcp-docs
status: completed
horizon: now
title: "Sprint 1: AI/LLM & MCP Documentation (Critical - New Feature)"
tags: [9.0.0, ai, mcp, sprint-1]
priority: 1
---

# Sprint 1: AI/LLM & MCP Documentation

## Priority: CRITICAL — Entirely Undocumented New Feature Surface

The AI/LLM/MCP feature set has zero documentation. This is the highest-priority gap as it represents a major new capability in the product.

## Scope

- **AI Agents** — Configuration and management of AI agents
- **LLM Integrations** — Connecting LLM providers (OpenAI, Azure OpenAI, etc.)
- **AI Services** — AI service configuration and usage
- **MCP Servers** — Model Context Protocol server management
- **AI Chat API** — Using the AI chat endpoint
- **AI Task Type** — The `ai` task type for workflow automation

## Target Audience

IT Operations teams exploring AI-assisted infrastructure management.

## Pages to Create

1. `tools/ai/ai.rst` — AI overview and concepts
2. `tools/ai/agents.rst` — Configuring AI Agents
3. `tools/ai/llm_integrations.rst` — LLM provider setup
4. `tools/ai/mcp_servers.rst` — MCP server configuration
5. `library/automation/tasks/ai_task.rst` — AI task type reference

## Source Code

- `AiAgentsController`, `LlmIntegrationsController`, `AiServicesController`
- `McpServersController`, `AiChatController`
- Task seed: `ai` task type with `aiTaskService`
