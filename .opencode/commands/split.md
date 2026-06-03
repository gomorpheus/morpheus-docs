---
description: Break a large spec into smaller, independently deliverable child specs.
---
Route this decomposition request to the appropriate delivery lead.

Determine whether this is product feature work or platform/migration work:
- Product features, user-facing enhancements → delegate to `feature-delivery-lead`
- Migrations, refactors, platform changes → delegate to `platform-delivery-lead`

The delivery lead will:
1. Read the parent spec thoroughly
2. Identify natural boundaries for decomposition (by concern, by layer, by user flow, by risk)
3. Create child spec files using the project's spec conventions
4. Each child spec should:
   - Have its own slug (e.g., `{parent}-auth`, `{parent}-api`, `{parent}-ui`)
   - Reference the parent via `relations: [{target: {parent-slug}, kind: parent}]`
   - Be independently deliverable (can be designed, built, and tested on its own)
   - Include its own Goal, Changes, and Acceptance Criteria sections
5. Update the parent spec to:
   - Add a `## Child Specs` section listing all children
   - Add relations: `[{target: {child-slug}, kind: child}]` for each child
   - Optionally note the recommended delivery order and dependencies between children
6. Keep the parent spec as the initiative/umbrella — do NOT delete it

**Decomposition principles:**
- Each child should take no more than 1-2 days to deliver
- Prefer splitting by vertical slice (feature/user flow) over horizontal slice (layer)
- If children have dependencies, note the delivery order
- If a child is still too large, note that it can be split further with another `/split`

Spec to decompose: $ARGUMENTS
