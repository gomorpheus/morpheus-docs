---
description: Resume a session — load the focused, ranked context the model needs to be productive from prompt 1. Auto-fire at every fresh session in a hero-aware repo.
---

This is the primary mechanism that makes every prompt smarter. Run
`hero resume` (alias: `hero load`) and read the output **before
doing anything else** — it contains the focused, ranked subgraph
relevant to this session: who you are, what's in flight, what just
changed, dead ends to skip, blockers, and files-nearby context.

**When to use:**

- At the start of every fresh session in a hero-aware repo
- After a long pause (>1 hour) where state may have moved
- After switching branches or pulling
- Whenever you feel like you're missing context
- Whenever the user says "resume", "pick up", "continue", "where
  are we", "catch me up", "what's going on"

**Steps:**

1. Run `hero resume` (or `hero resume --auto` to bias scoring toward
   currently-changed files).
2. Read the entire output. Do not summarize it back to the user — it's
   for you, the agent. Treat it as system context for everything that
   follows in this session.
3. If a section ends with `_…+N more — hero search <topic> to dig
   deeper_`, that's a relief valve. When the user asks something that
   touches that area, run `hero search <topic>` to pull more.
4. If you need to understand WHY something is where it is, run
   `hero why <slug>` to traverse the graph backwards.
5. If the user asks "what's blocked?" or "what should I work on?",
   prefer the resume output's `Blocked on` and `In flight` sections
   over re-deriving from scratch by reading files. For a paste-ready
   list of ready-to-pick-up specs (each with a kickoff prompt), call
   `hero_queue` via MCP or read `.hero/QUEUE.md` directly. The queue
   is the cold-start surface; resume is the warm-context surface —
   they compose.
6. The first item in `In flight` is usually the right next action.
   Propose it directly — don't ask "what should we work on?".

**Why this matters:**

Hero captures every commit, spec, decision, attempt, and cross-repo
dependency over the project's life. The resume output is the
digest — bounded, ranked, fresh — that puts the most-relevant slice
into your context window so the user gets a hot session even on a
cold box. Without it, you're doing the work the digester already
did, slower and less accurately.

**If `hero resume` fails or returns nothing:**

The graph may not be populated yet. Run `hero scan` (or `hero graph
reingest all`) to populate it from the local sources of truth (code,
specs, git log, NEXT.md). Then re-run `hero resume`.

**What to say** (natural-language triggers — agents should auto-route
these to `/resume` without the user having to know the command name):

"resume", "let's resume", "let's continue", "continue", "pick up
where we left off", "where are we", "what's going on", "catch me up",
"load context", "load up", "load me up", "starting fresh", "fresh
session", "hot session", "warm me up", "what should I work on",
"what's the status", "give me the lay of the land".

Also: at the start of any new session in this repo, before
responding to the user's first substantive message, run
`hero resume` unconditionally. It's ≥99% useful and never wrong —
it costs nothing to fire, and it prevents the agent from
re-deriving context the graph already has.
