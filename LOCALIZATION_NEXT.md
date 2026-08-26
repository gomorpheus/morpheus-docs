# Localization — Next Session Handoff

## Current State (2026-08-26)

| Language | Translated | Total | Coverage |
|----------|-----------|-------|----------|
| Spanish (es) | 37,663 | 44,375 | **84%** |
| Portuguese (pt) | 2,422 | 45,563 | **5%** |
| German (de) | 2,090 | 45,218 | **4%** |
| French (fr) | 2,060 | 45,563 | **4%** |

## What's Been Translated (fr/de/pt)

All 3 new languages have these files completed:
- `administration/settings/settings.po`
- `administration/roles/roles.po`
- `administration/supportability/support_bundles.po`
- `administration/settings/logs.po`
- `administration/logging/log_forwarding.po`
- `infrastructure/storage/storage.po`
- `infrastructure/clusters/hvm/hvm.po`
- `infrastructure/clusters/hvm/virtual_switches.po`
- `infrastructure/clusters/hvm/storage_operations.po`
- `infrastructure/clusters/hvm/nvidia_vgpu.po`
- `infrastructure/clusters/hvm/guest_os_notes.po`
- `infrastructure/clusters/hvm/snapshots.po`
- `infrastructure/clusters/hvm/vm_migration.po`
- `infrastructure/clusters/hvm/vm_placement.po`
- `infrastructure/clusters/hvm/vm_advanced_options.po`
- `infrastructure/clusters/hvm/hvm_networks.po`
- `infrastructure/clusters/hvm/architecture.po`
- `release_notes/9_1_0.po`
- `tools/hpe_vm/install_morpheus.po`
- `getting_started/installation/singleNode/hpe_installer.po`

Spanish also has 5 additional files from earlier in this session.

## Priority Files Remaining (by string count)

### Large files (100+ strings) — use translate_po.py pipeline with API key:
```
1892 infrastructure/compute/compute.po
1858 infrastructure/compute/resourcetypes.po
 817 integration_guides/Clouds/hpe_bare_metal/hpe_bare_metal.po
 654 administration/roles/role_permissions.po
 579 library/automation/automation.po
 484 library/blueprints/blueprints.po
 463 administration/identity_sources/identity_sources.po
 451 infrastructure/loadbalancers/lb.po
 402 library/options/options.po
 364 tools/ai/morpheus_mcp_server.po
 354 library/automation/tasks.po
 339 getting_started/requirements/requirements.po
 310 getting_started/additional/additional_configuration.po
 296 integration_guides/Clouds/hpe_bare_metal/compute_management.po
 290 integration_guides/Clouds/vmware/vmware.po
 275 getting_started/guides/vdi_guide.po
 273 getting_started/functionality/agent/osSupport.po
 272 integration_guides/Clouds/aws/amazon.po
 269 library/blueprints/clusterLayouts.po
 269 getting_started/functionality/communication.po
 263 integration_guides/Clouds/azure/azure.po
 263 getting_started/maintenance/upgrades/overview.po
 253 release_notes/compatibility.po
```

### Medium files (30-100 strings) — agent-translatable:
~40 files per language, ~60 strings each = ~2,400 strings per language

### Small files (<30 strings) — agent-translatable:
~530 files per language, ~15 strings avg = ~7,950 strings per language

## How to Continue

### Option A: API pipeline (fastest, needs key)
```bash
export OPENAI_API_KEY=sk-...
# or
export ANTHROPIC_API_KEY=sk-ant-...

# Translate all remaining strings
python3 tools/translate/translate_po.py locale/fr/LC_MESSAGES --lang fr --glossary tools/translate/glossary_fr.json -v
python3 tools/translate/translate_po.py locale/de/LC_MESSAGES --lang de --glossary tools/translate/glossary_de.json -v
python3 tools/translate/translate_po.py locale/pt/LC_MESSAGES --lang pt --glossary tools/translate/glossary_pt.json -v

# Finish Spanish
python3 tools/translate/translate_po.py locale/es/LC_MESSAGES --glossary tools/translate/glossary.json -v
```

### Option B: Agent sessions (no API key needed)
Use single-file Task agents with the prompt pattern:
```
Translate a Sphinx .po file from English to [LANGUAGE] for Morpheus.
Only translate empty msgstr. Preserve RST markup.
Keep product names untranslated. Keep :guilabel: in English.
Read [FILE], translate all empty msgstr, write back.
```
- Keep files under 80 strings per agent to avoid timeouts
- Run 3 agents in parallel (one per language, same file)

### Option C: Hybrid
Use agents for medium files (30-80 strings), API pipeline for large files (100+).

## Build Commands
```bash
make html-es    # Spanish
make html-fr    # French
make html-de    # German
make html-pt    # Portuguese
make intl-update  # Regenerate .po files from current source
```

## Glossary Files
- `tools/translate/glossary.json` — Spanish (4,438 terms)
- `tools/translate/glossary_fr.json` — French (4,427 terms)
- `tools/translate/glossary_de.json` — German (4,417 terms)
- `tools/translate/glossary_pt.json` — Portuguese (3,490 terms)

## Remotes
- `origin` fetch: `git@github.com:HewlettPackard/morpheus-docs.git` (public)
- `origin` push: `git@github.com-hpe-emu:HPE-EMU/morpheus-docs.git` (private, pre-release)
- `hpe-emu`: same private repo (fetch + push)
