#!/usr/bin/env python3
"""
Extract a translation glossary from the Morpheus UI messages_es_ES.properties file.

Parses the Java .properties file and extracts key product terms and their
Spanish translations into a JSON glossary for use by the translation pipeline.
"""

import json
import re
import sys
from pathlib import Path


# Key patterns to extract from the UI properties file.
# These capture the main product navigation terms and concepts.
TERM_PATTERNS = [
    # Top-level navigation
    (r'^gomorpheus\.(provisioning|infrastructure|monitoring|operations|administration|library|backups|tools|security)$', None),
    # Plural forms
    (r'^gomorpheus\.(provisioning|infrastructure|monitoring|operations|administration|library|backups|tools|security)\.plural$', None),
    # Key object types
    (r'^gomorpheus\.label\.(instance|instances|cloud|clouds|group|groups|workflow|workflows|task|tasks|network|networks|backup|backups|integration|integrations|cluster|clusters|server|servers|host|hosts|tenant|tenants|role|roles|user|users|plan|plans|policy|policies|report|reports|job|jobs|execution|executions|environment|environments|check|checks|alert|alerts|contact|contacts|certificate|certificates|credential|credentials|blueprint|blueprints|app|apps|template|templates|script|scripts|image|images|volume|volumes|container|containers|deployment|deployments|router|routers|domain|domains|subnet|subnets|pool|pools|snapshot|snapshots|schedule|schedules)$', None),
    # Navigation sections
    (r'^gomorpheus\.(provisioning|infrastructure|monitoring|operations|administration|library|backups|tools)\.[a-zA-Z]+$', None),
    # Common UI labels
    (r'^gomorpheus\.label\.(name|description|status|type|owner|created|updated|enabled|disabled|active|inactive|actions|settings|details|save|cancel|delete|edit|add|remove|create|clone|copy|refresh|search|filter|apply|execute|run|start|stop|restart|suspend|resume|approve|deny|lock|unlock|import|export|upload|download)$', None),
]


def parse_properties(filepath: Path) -> dict[str, str]:
    """Parse a Java .properties file into a dict."""
    props = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                key, _, value = line.partition('=')
                props[key.strip()] = value.strip()
    return props


def extract_glossary(props: dict[str, str]) -> dict[str, str]:
    """Extract English->Spanish term mappings from parsed properties."""
    # We need the English properties to know the source terms
    glossary = {}

    # Direct term extraction: use the key suffix as English term
    # and the value as Spanish translation
    key_to_english = {
        'gomorpheus.provisioning': 'Provisioning',
        'gomorpheus.infrastructure': 'Infrastructure',
        'gomorpheus.monitoring': 'Monitoring',
        'gomorpheus.operations': 'Operations',
        'gomorpheus.administration': 'Administration',
        'gomorpheus.library': 'Library',
        'gomorpheus.backups': 'Backups',
        'gomorpheus.backup': 'Backup',
        'gomorpheus.tools': 'Tools',
        'gomorpheus.security': 'Security',
    }

    # Extract known mappings
    for key, english in key_to_english.items():
        if key in props:
            glossary[english] = props[key]

    # Extract label terms - the key suffix IS the English term
    label_prefix = 'gomorpheus.label.'
    for key, value in props.items():
        if key.startswith(label_prefix) and value:
            english_term = key[len(label_prefix):]
            # Capitalize first letter to match doc usage
            english_cap = english_term.capitalize()
            if english_cap not in glossary:
                glossary[english_cap] = value

    # Extract section navigation terms
    nav_prefix = 'gomorpheus.infrastructure.'
    for key, value in props.items():
        if key.startswith(nav_prefix) and '.' not in key[len(nav_prefix):] and value:
            english_term = key[len(nav_prefix):].capitalize()
            if english_term not in glossary:
                glossary[english_term] = value

    nav_prefix = 'gomorpheus.provisioning.'
    for key, value in props.items():
        if key.startswith(nav_prefix) and '.' not in key[len(nav_prefix):] and value:
            english_term = key[len(nav_prefix):].capitalize()
            if english_term not in glossary:
                glossary[english_term] = value

    nav_prefix = 'gomorpheus.administration.'
    for key, value in props.items():
        if key.startswith(nav_prefix) and '.' not in key[len(nav_prefix):] and value:
            english_term = key[len(nav_prefix):].capitalize()
            if english_term not in glossary:
                glossary[english_term] = value

    return glossary


def main():
    # Default path to UI i18n file
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    default_props = project_root.parent / 'morpheus-ui' / 'morpheus-ui' / 'grails-app' / 'i18n' / 'messages_es_ES.properties'

    props_path = Path(sys.argv[1]) if len(sys.argv) > 1 else default_props

    if not props_path.exists():
        print(f"Error: Properties file not found: {props_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Parsing: {props_path}", file=sys.stderr)
    props = parse_properties(props_path)
    print(f"Total properties: {len(props)}", file=sys.stderr)

    glossary = extract_glossary(props)
    print(f"Glossary terms extracted: {len(glossary)}", file=sys.stderr)

    # Output glossary as JSON
    output_path = script_dir / 'glossary.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(glossary, f, ensure_ascii=False, indent=2, sort_keys=True)

    print(f"Glossary written to: {output_path}", file=sys.stderr)


if __name__ == '__main__':
    main()
