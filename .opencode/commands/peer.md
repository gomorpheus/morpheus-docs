---
description: Cross-repo peering — ask a sibling Hero a question, have it design a spec, or hand off work. Routes to `hero peer call` / `hero handoff` / `hero peer list` / `hero peer show` with trail discipline.
---
Front door for cross-repo peering operations. Picks the right interaction
mode (advisory, spec-out, handoff, list, show) from the user's intent and
runs the appropriate CLI command with the trail-discipline flags filled
in.

Before doing anything, **load `skills/cross-repo-peering/SKILL.md`** —
the skill carries the decision tree, the prompt-composition rules, and
the anti-patterns. Don't try to compose a peer call without it.

**Steps:**

1. Run `hero peer list` first to confirm peers are registered. If empty,
   tell the user to register first with
   `hero admin repos add <alias> <path>` and stop. Don't try to invoke
   a peer call against an unregistered alias.

2. Parse the user's intent into one of five sub-actions:

   | Intent signal | Sub-action |
   |---|---|
   | "ask <peer>", "check with <peer>", "what's <peer>'s X" | advisory peer call |
   | "have <peer> design", "let <peer> handle the design of" | spec-out peer call |
   | "hand off to <peer>", "drop on <peer>'s queue", "transfer to <peer>" | async handoff |
   | "pick up", "accept", "peer finished" | handoff accept |
   | "list peers", "what peers", "show <peer>", "what does <peer> expose" | discovery (list / show) |

   If two sub-actions are plausible (common between advisory and spec-out;
   common between handoff and spec-out), ask one focused clarifying
   question. Don't guess.

3. **For advisory peer calls** (`--mode=advisory`):

   - Identify the active spec from the session context. If there is one,
     attach it: `--related-spec <slug>`.
   - Draft a `--reason` string from the session context (one sentence,
     why this call is happening now). Show it to the user inline before
     dispatching.
   - **Compose the peer-call prompt as a focused brief**, not a paraphrase.
     Name the specific artifact, field, or constraint. Read the skill's
     "Composing a good peer-call prompt" section.
   - Default budgets (20 turns / 50,000 tokens) are usually fine; only
     override if the user asks or the prompt is genuinely huge.

   Example output to the user before dispatching:

   > Calling `hero-cloud` (advisory mode). Reason: "Need to know the
   > error envelope shape before changing the renderer in this session."
   > Prompt: "What's the current shape of the `errors` array in the
   > `/v1/order` POST response? Any deprecations in flight?"
   > Related spec: `order-failure-error-display`.
   >
   > Run this? [y/n]

4. **For spec-out peer calls** (`--mode=spec-out`):

   - Same trail discipline (`--related-spec`, `--reason`).
   - **Shape the prompt as a `/design` kickoff** — name the work, list
     constraints, list out-of-scope, list acceptance shape. The peer's
     `/design` flow runs on this verbatim.
   - Default budget is larger (50 turns / 150,000 tokens). Don't override
     unless the spec is genuinely heavyweight.
   - Confirm with the user before dispatching — spec-out writes a spec on
     the peer's side.

5. **For async handoff**:

   - Pre-condition: there must be a local spec to hand off. If the user
     hasn't named one and the session has an active spec, suggest that
     one. If neither, ask which spec to hand off.
   - The handoff scaffolds a spec on the peer's side based on the local
     spec's frontmatter + body. The receiver's title and type can be
     overridden with `--title` / `--type` if the peer's conventions want
     a different shape.
   - Run: `hero handoff <local-slug> <peer-alias> --reason "<why>" --type <type>`.
   - After the handoff returns, surface to the user:
     - The receiver-side slug (may differ from local if there was a
       collision — Hero appends `-2`, `-3`, etc.).
     - The trail entry was written.
     - The local spec's status moved to `handed_off`.
     - The peer's side now owns the next move.

6. **For handoff accept** (when a `handed_back` spec needs picking up):

   - Run `hero handoff accept <slug>`.
   - Prompt the user to pick the next status (usually verify the symptom
     on the originator's side, then mark complete).

7. **For discovery** (list / show):

   - `hero peer list` for the table view.
   - `hero peer show <alias>` for one peer's manifest contents and
     in-flight handoffs.
   - These are read-only; no confirmation needed.

8. **Always surface the result to the user**, not the raw command output.

   - For advisory: summarize the findings (headline + 2-3 actionable
     bullets). Quote excerpts; don't dump the full peer envelope.
   - For spec-out: confirm the peer-side slug was created and that the
     local spec moved to `awaiting_peer`.
   - For handoff: confirm the peer-side slug and the trail.
   - For list/show: render the table or detail block plainly.

9. **Trail discipline checks** — before reporting "done":

   - Did `hero handoff status` show the new entry?
   - Is the active spec's frontmatter updated (`status:`, trail block)?
   - Did the peer's events log get the corresponding event? (You can
     check `cat ../<peer-alias>/.hero/events.log | tail -5` if curious.)

**Common patterns** (these should fire from natural language, not just
slash invocation):

- "Ask hero-cloud about X" → advisory call
- "Have hero-code design the migration story" → spec-out
- "Hand off the tracker-fronting spec to hero-cloud" → async handoff
- "What peers do we have" → list
- "What does hero-cloud expose" → show

**What NOT to do:**

- Don't invoke a peer call to answer a question you can answer locally
  (`hero search`, reading the workspace, etc.). Peer calls cost a
  subagent spawn.
- Don't paraphrase the user's words verbatim as the peer-call prompt.
  Compose a structured brief.
- Don't skip `--related-spec` when one exists in session context.
- Don't run `--mode=full` — full-delivery peer call is v2+; not
  available in v1. If the user asks, explain and offer spec-out as the
  closest available option.

**What to say:** "ask peer", "ask hero-code about", "check with sibling",
"have hero-cloud design", "hand off to", "drop on peer's queue",
"transfer to", "list peers", "what peers do we have", "what does peer
expose", "pick up the handoff".
