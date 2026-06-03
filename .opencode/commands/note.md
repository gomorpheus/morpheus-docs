---
description: Capture the current conversation, brainstorm, or thinking as a note in the knowledge base.
---
**Before creating any file**, check whether the user is working in a sub-folder workspace. If so, preserve that workspace's `subproject:` frontmatter and write the note under the workspace's `.hero/` root; otherwise write under the project `.hero/` root.

Save the current conversation as a note in the Hero knowledge base.

Load the `note-capture` skill — it contains the full methodology for how to capture conversations, what to include/exclude, content formatting, and different capture modes.

If the user provides arguments, use them as the topic. If no arguments, ask what to title the note.

Topic to capture: $ARGUMENTS
