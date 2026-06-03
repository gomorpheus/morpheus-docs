---
name: next-merge-recovery
description: How agents detect and self-heal git merge-conflict markers in the projected NEXT files (`.hero/NEXT.md`, `.hero/next/*.md`) without resorting to hand-resolution.
compatibility: opencode
metadata:
  audience: any-agent
  purpose: session-handoff
  applies_when: working in a hero repo where `.hero/NEXT.md` or `.hero/next/*.md` may have unresolved merge markers
---

## What I do

Stop the agent from hand-resolving merge conflicts in projected NEXT
files. These files are graph projections — total-rewrite from local
state every Stop hook. Conflict markers in them are noise to be
regenerated, not a diff to be merged thoughtfully.

When `<<<<<<<` markers appear in any of:

- `.hero/NEXT.md`
- `.hero/next/<user>.md`
- `.hero/next/<user>.local.md`

run `hero next checkpoint` immediately. The command regenerates each
file from the local graph, discarding both sides of the conflict
cleanly.

## Why this matters

`hero next migrate-to-projection` flips `next.projected = true` and
ships a `hero-next` git merge driver registered in `.git/config` by
`hero install`. For clones that have run install, conflicts in these
files never produce markers — the driver regenerates the file on
merge automatically.

For clones that **haven't** run install (fresh checkouts, CI runners,
teammates picking up the repo for the first time), git falls back to
the default merge behavior and writes standard conflict markers. The
next Stop-hook firing of `hero next checkpoint` will catch it and
regenerate, but if an agent gets to the file first and tries to
hand-resolve, the result is wasted effort plus the very brittleness
projection exists to eliminate.

## What to do

**The instant you see `<<<<<<<` in one of those paths:**

```bash
hero next checkpoint
```

That's it. Don't:

- Open the file and pick a side.
- Run `git checkout --ours` / `--theirs`.
- Edit the markers out by hand.
- Try to merge the two halves into a "best of both" version.

The file's content isn't a source of truth — the graph is. Re-deriving
from the graph is faster, deterministic, and the correct semantic
answer.

## Verifying

After `hero next checkpoint`:

```bash
grep -l '<<<<<<<\|=======\|>>>>>>>' .hero/NEXT.md .hero/next/*.md 2>/dev/null
```

Should print nothing. If markers remain, the projection failed (check
the command's stderr) — surface it, don't paper over.

## When this doesn't apply

- **Conflicts in `.hero/specs/*.md` or `.hero/planning/*.md`.** These
  are hand-authored, not projected. Resolve them normally with the
  usual diff-merge tools.
- **Conflicts in `.hero/knowledge/*.md`.** Same — hand-authored.
- **Conflicts in `.hero/QUEUE.md`.** Projected, but covered by its
  own regen path (`hero queue write`). The same principle applies but
  the command differs.
- **`next.projected = false`.** Pre-migration repos still use the
  hand-authored NEXT.md flow. Normal merge resolution applies.

## See also

- `skills/next-handoff-emit/SKILL.md` — the companion skill for
  *writing* projection state during normal work.
- `hero next migrate-to-projection` — one-shot to flip a repo into
  projection mode and capture pre-existing NEXT.md content as graph
  nodes.
- `hero install` — registers the `hero-next` merge driver in
  `.git/config` so future merges resolve without markers in the
  first place.
