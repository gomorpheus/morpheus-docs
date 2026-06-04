---
description: Generate a visual mockup from a spec or free-text description. Supports HTML (web) and native renderers (SwiftUI, more coming).
---
Route this mockup request to the `ui-designer` agent.

## Renderer Selection

**Do not derive the renderer yourself.** The CLI does it. Run:

```
hero spec mock detect [--renderer=<flag-if-user-passed-one>]
```

Read the single line of JSON it prints. Fields:
- `renderer` — `"html"` or `"swiftui"`. **Use this value verbatim** — pass it to `ui-designer` as the chosen renderer.
- `reason` — one-sentence rationale for the announce step below.
- `signals` — what fired (e.g. `"Package.swift"`, `"MyApp.xcodeproj"`, `"12 .swift files at root"`).
- `toolchain_ok` / `toolchain_path` — whether `swiftc` was found.
- `config_override` — set when `hero.json` `mockups.renderer` won.
- `explicit_flag` — echoed back when the user passed `--renderer=...`.
- `conflict` — non-null when the choice is suspicious (e.g. `--renderer=html` on a Swift project, or `--renderer=swiftui` with no `swiftc`).

If `conflict` is non-null, **halt** — do not proceed to generation. Surface the conflict message to the user and ask them to confirm:

```
Renderer choice conflict.
{conflict message from detect output}
Confirm one:
  [keep flag]    use {explicit_flag} as requested
  [use detected] override my flag and use the auto-detected renderer
```

Only proceed once the user picks.

## Announce step (mandatory, before any generation)

Before delegating to `ui-designer`, emit this one-line announcement as user-visible output:

```
Renderer: {renderer} — reason: {reason} — swiftc: {toolchain_path or "unavailable"}
```

This is the gate that catches wrong picks in-turn — the user sees the choice before any files are written. Skipping it is the bug this command was designed to fix.

For fallback cases (Swift signals present but no `swiftc`), the announce becomes:

```
Renderer: HTML (SwiftUI unavailable — swiftc not found)
```

Tell the ui-designer which renderer to use and which skill to load:
- **HTML:** Load `html-mockup-generation` skill. Output: `.hero/mocks/{slug}/index.html`
- **SwiftUI:** Load `swiftui-mockup-renderer` skill. Output: `.hero/mocks/{slug}/MockView.swift` + `screenshot.png` + `screenshot-dark.png` + `index.html` (viewer)

## Workflow

The ui-designer will:
1. Read the spec (if a slug is provided) or parse the free-text description
2. Identify the key screens, components, and interactions needed
3. Generate the mockup using the selected renderer:
   - **HTML:** Self-contained `index.html` with embedded CSS and JS
   - **SwiftUI:** `MockView.swift` source → compile → capture PNG screenshots (light + dark)
4. Save to `.hero/mocks/{slug}/` (or `.hero/mocks/_adhoc/{summary-slug}/` for free-text)
5. If a spec slug was provided, append (or update on `--iterate`) a `## Mockups` entry in the originating spec at `.hero/planning/features/{slug}/spec.md` or `.hero/planning/bugs/{slug}/spec.md` (or `.hero/specs/{slug}/spec.md` if already archived). Entry format:
   - HTML: `- [{Name}](.hero/mocks/{slug}/index.html) — YYYY-MM-DD — one-line description`
   - SwiftUI: `- [{Name}](.hero/mocks/{slug}/screenshot.png) — YYYY-MM-DD — SwiftUI native render`

If the user provides `--iterate` feedback, read the existing mockup first and modify it based on the feedback rather than regenerating from scratch. On iterate, update the matching `## Mockups` entry's date in place rather than appending a duplicate.

**Output requirements (HTML renderer):**
- Single self-contained `index.html` — no external dependencies
- Professional, clean design with modern CSS (flexbox/grid)
- Basic interactivity where appropriate (tabs, modals, dropdowns)
- Responsive layout (works on mobile and desktop)
- HTML comment header with spec slug, date, and description

**Output requirements (SwiftUI renderer):**
- Single self-contained `MockView.swift` — no SPM dependencies
- Real SwiftUI components, SF Symbols, system colors
- Both light and dark mode screenshots captured
- Viewer `index.html` wrapping the PNGs with light/dark toggle

**Surface outputs — orchestrator responsibility (READ THIS):**

The `ui-designer` runs as a subagent. **The subagent's return value is NOT visible to the user.** When the Agent tool completes, you (the orchestrator running this command) MUST emit a clickable file inventory in your *own* user-facing text response — do not assume the subagent's links reach the user.

To make this reliable, instruct the `ui-designer` (in the prompt you send it) to terminate its return text with a machine-parseable block:

```
<MOCKUP_FILES>
.hero/mocks/{slug}/index.html|Mockup name|primary
.hero/mocks/{slug}/screenshot.png|Screenshot — light|image
.hero/mocks/{slug}/screenshot-dark.png|Screenshot — dark|image
.hero/mocks/{slug}/MockView.swift|SwiftUI source|source
.hero/planning/features/{slug}/spec.md|Spec (Mockups section updated)|spec
</MOCKUP_FILES>
```

Parse that block from the tool result and re-emit it in your final response as a markdown list of clickable links:

```
**Mockups generated:**
- [Mockup name](.hero/mocks/{slug}/index.html) — primary
- [Screenshot — light](.hero/mocks/{slug}/screenshot.png)
- [Screenshot — dark](.hero/mocks/{slug}/screenshot-dark.png)
- [SwiftUI source](.hero/mocks/{slug}/MockView.swift)
- [Spec updated](.hero/planning/features/{slug}/spec.md) — `## Mockups` entry appended
```

If the subagent did not return a `<MOCKUP_FILES>` block, fall back to scanning its response text for `.hero/mocks/...` paths and listing those. Either way, the inventory must appear in YOUR response, not just the subagent's.

**Spec write-back check:** If a spec slug was provided, verify the subagent updated the spec's `## Mockups` section. If the inventory does not include the spec path, read the spec file yourself and append the entry before finishing.

Request: $ARGUMENTS
