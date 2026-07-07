.. _ai-chatting:

Chatting
--------

The chat interface is a pop-out panel accessible from the lower-right corner of the |morpheus| UI window. Click on the glowing green orb containing the HPE logo to expand the chat interface.

Using the Chat Interface
^^^^^^^^^^^^^^^^^^^^^^^^

Once expanded, the chat interface provides the following features:

- The configured default chat agent will be pre-selected
- Any other configured agents may be selected from the dropdown menu in the upper-left of the chat interface pop-out
- Conversations are maintained within the session
- Tool calls made by the AI are shown with their results
- Write operations require user confirmation before execution

Starting a Conversation
^^^^^^^^^^^^^^^^^^^^^^^

To begin, simply type a message into the input field at the bottom of the chat panel. The selected AI Agent will respond using its configured LLM and any available tools (from MCP Servers or the built-in Morpheus MCP server).

Agent Selection
^^^^^^^^^^^^^^^

The default agent (configured in :ref:`ai-agents`) is automatically selected when the chat interface opens. To use a different agent, select it from the dropdown menu in the upper-left corner of the chat panel. Changing the agent starts a new conversation context.

Tool Calls & Confirmation
^^^^^^^^^^^^^^^^^^^^^^^^^^

When the AI invokes tools to fulfill a request, tool calls and their results are displayed within the conversation. For read operations, results are returned immediately. For write operations (create, modify, delete), the user must confirm the action before it is executed. This provides a safety mechanism against unintended changes.
