---
description: Generate a visual HTML mockup from a spec or free-text description.
---
Route this mockup request to the `ui-designer` agent.

The ui-designer will:
1. Read the spec (if a slug is provided) or parse the free-text description
2. Identify the key screens, components, and interactions needed
3. Generate a self-contained HTML mockup with embedded CSS and inline JS
4. Save it to `.hero/mocks/{slug}/index.html`

If the user provides `--iterate` feedback, read the existing mockup first and modify it based on the feedback rather than regenerating from scratch.

**Output requirements:**
- Single self-contained `index.html` — no external dependencies
- Professional, clean design with modern CSS (flexbox/grid)
- Basic interactivity where appropriate (tabs, modals, dropdowns)
- Responsive layout (works on mobile and desktop)
- HTML comment header with spec slug, date, and description

Load the `html-mockup-generation` skill for detailed design guidance.

Request: $ARGUMENTS
