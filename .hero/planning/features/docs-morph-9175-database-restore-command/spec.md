---
title: "VME DB Restore Instructions incorrect + improvement"
slug: docs-morph-9175-database-restore-command
type: feature
status: completed
horizon: now
size: medium
tags: [documentation, database, restore, operations]
tracker_id: MORPH-9175
jira_status: New
parent: docs-morph-3266-enhancements
created: 2026-08-03
completed_at: 2026-08-03T15:02:52Z
---

# VME DB Restore Instructions incorrect + improvement

## Context

Jira: https://hpe.atlassian.net/browse/MORPH-9175

Exact Jira description (delivery source requirement):

> First Issue: existing instructions `[root@app-server~] /opt/morpheus/embedded/mysql/bin/mysql -u morpheus -h 127.0.0.1 morpheus -p < /tmp/morpheus_backup.sql` connect to the morpheus database. As part of the restore, the SQL instructions in the dump-file `/tmp/morpheus_backup.sql` include a “DROP DATABASE” statement:
>
> `--`  
> ``-- Current Database: `morpheus` ``  
> `--`
>
> ``/*!40000 DROP DATABASE IF EXISTS `morpheus`*/;``
>
> If the above restore is performed, the connection will get stuck/hung, as the connection is mapped to the database morpheus, which will then get dropped as one of the first statements.
>
> We suggest to change the documentation to the following statement, without specifying a database in the connection string:`[root@app-server~] /opt/morpheus/embedded/mysql/bin/mysql -u morpheus -h 127.0.0.1 -p < /tmp/morpheus_backup.sql` 
>
> ‌
>
> Second improvement: the existing password retrieval process `cat /etc/morpheus/morpheus-secrets.json | grep morpheus_password` is ambigues in the sense to ensure we capture the correct password. In case the order gets changed between root_password, morpheus_password and ops_passwords; or new credentials are getting introduces, the instruction `<---- this one` might not be correct anymore.
>
> Instead I’m suggesting to use `cat /etc/morpheus/morpheus-secrets.json | jq .mysql.morpheus_password` to ensure we capture the right password.
>
>   
> I classified this as Critical, as we relied on this instructions during an incident and lost critical time for root-cause-analysis.

## Goal

Produce accurate, version-scoped documentation that resolves MORPH-9175 without converting reported observations into unsupported product guarantees. Completion includes SME verification for all behavior not already established by maintained documentation.

## Kickoff

Deliver `.hero/planning/features/docs-morph-9175-database-restore-command/spec.md`. Start by reading the exact Jira description above, then inspect and update only the validated subset of:

- `getting_started/guides/backup_restore.rst`
- `getting_started/maintenance/db_migration.rst`
- `getting_started/additional/encryption.rst`

Do not proceed past any blocker in Risks by guessing; capture the authoritative answer or attachment first.

## Approach

Correct the restore connection so it is not bound to a database the dump drops, replace ambiguous password extraction with an exact-key method, and align duplicate procedures.

Use the existing reStructuredText style, substitutions, navigation markup, admonitions, and single-source cross-linking patterns. Keep claims scoped to verified product versions and personas.

## Changes

1. `getting_started/guides/backup_restore.rst` — Removed the unsupported generic restore command, added exact-key secret lookup, and documented the Support-assisted restore boundary.
2. `getting_started/maintenance/db_migration.rst` — Removed the unsupported generic import command and corrected custom/external database credential guidance.
3. `getting_started/additional/encryption.rst` — Clarified generated embedded MySQL secrets versus external connection configuration.

## Acceptance Criteria

- WHEN a reader follows the affected workflow THE DOCUMENTATION SHALL state the verified prerequisites, decision points, and expected result for MORPH-9175
- IF a reported behavior cannot be reproduced or confirmed THEN THE DOCUMENTATION SHALL omit it or label the supported limitation using approved product wording
- THE DOCUMENTATION SHALL use current repository navigation, terminology, formatting, and cross-references across every changed file
- THE DOCUMENTATION SHALL explain why the database-bound restore command is unsafe, omit an unverified replacement command, and direct readers to a topology-specific supported recovery plan
- WHEN the documentation build and link checks run THE SYSTEM SHALL complete without new warnings or broken internal references caused by these changes

## Boundaries

- Do not change product code, API behavior, UI behavior, or release support policy.
- Do not broaden this issue into a general rewrite of adjacent documentation.
- Do not add inaccessible Jira media to the repository or reconstruct screenshots from descriptions.
- Do not publish commands, defaults, compatibility claims, or destructive operations until an authoritative owner verifies them.

## Risks

- Database engineering must validate commands, jq availability, dump variants, topology/version scope, rollback, and post-restore checks before publication.
- Existing content may span Enterprise and VM Essentials variants; an unscoped edit could create a cross-version contradiction.
- Screenshots and external links may differ from the source tree; validate against a supported environment and maintained destinations.

## Validation

1. Record SME/product-owner evidence for each behavior called out as unverified in Risks.
2. Review the rendered pages against the Jira request and a supported product environment.
3. Run `make build` and `make test`; resolve new warnings, malformed RST, and broken references.
4. Search the repository for superseded wording or navigation and reconcile only directly affected duplicates.
5. Confirm every acceptance criterion against the rendered output and retain evidence for any operational procedure.
