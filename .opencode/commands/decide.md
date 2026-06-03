---
description: Evaluate an architectural decision with structured analysis and produce a decision spec.
---
**Before creating any file**, check whether the user is working in a sub-folder workspace. If so, preserve that workspace's `subproject:` frontmatter and write the decision under the workspace's `.hero/` root; otherwise write under the project `.hero/` root.

Route this architectural decision to `architecture-reviewer` for structured evaluation.

The reviewer will:
1. Call `hero_anchor` with the decision context to load project mission and tripwires (forbidden options). Eliminate any option that appears in the tripwire list before evaluating — do not present it as an option with caveats.
2. Clarify the decision and its constraints
3. Evaluate the options with tradeoff analysis
4. Consider architectural fit, operational burden, team impact, and reversibility
5. Produce a decision spec with recommendation, rationale, and consequences
6. Save it to `.hero/decisions/{slug}/spec.md`

For decisions that involve a specific technology domain, also involve the relevant architect:
- Existing system concerns → also consult `brownfield-architect`
- New system or subsystem design → also consult `greenfield-architect`

Decision to evaluate: $ARGUMENTS
