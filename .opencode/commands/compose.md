---
description: Break a large initiative into sequenced specs with a coordinated delivery plan.
---
Route this initiative to `product-ideator` for scope and sequencing analysis, then to the appropriate delivery lead for spec planning.

Determine whether the initiative is primarily product or platform work:
- Product initiatives, user-facing overhauls, new capability suites → delegate planning to `feature-delivery-lead`
- Migrations, platform transitions, infrastructure overhauls → delegate planning to `platform-delivery-lead`

The workflow:
1. `product-ideator` breaks the initiative into concrete, sequenced work items with dependencies and priorities
2. The delivery lead produces an initiative spec at `.hero/planning/initiatives/{slug}/spec.md` containing:
   - Initiative summary and goals
   - Sequenced work items with dependency ordering
   - Child spec stubs for each work item (ready for individual `/design` passes)
   - Cross-cutting concerns and shared risks
   - Recommended delivery order

Each child spec stub should be actionable as input to `/design` when the team is ready to start that piece.

Initiative to decompose: $ARGUMENTS
