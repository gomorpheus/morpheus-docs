#!/usr/bin/env python3
"""
Translate a single .po file using stdin/stdout for the translation.

This script is designed to work with AI coding agents (like OpenCode) that can
provide translations inline. It reads a .po file, extracts untranslated entries,
outputs them for translation, and writes the results back.

Usage:
    # Export entries needing translation
    python3 translate_agent.py export locale/es/LC_MESSAGES/getting_started/getting_started.po

    # Import translations back (reads JSON from stdin)
    echo '{"translations": {"1": "texto traducido", ...}}' | \
        python3 translate_agent.py import locale/es/LC_MESSAGES/getting_started/getting_started.po

    # Translate inline (pass translations as argument)
    python3 translate_agent.py apply locale/es/LC_MESSAGES/file.po translations.json
"""

import json
import sys
from pathlib import Path


def parse_po_file(filepath: Path) -> tuple[str, list[dict]]:
    """Parse .po file. Returns (raw_header, entries)."""
    entries = []
    current = {'comments': [], 'msgid': '', 'msgstr': '', 'flags': [], 'references': [], 'msgid_lines': [], 'msgstr_lines': []}
    in_msgid = False
    in_msgstr = False
    header_lines = []
    past_header = False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by double newline to get blocks
    blocks = content.split('\n\n')

    # First block is the header
    header = blocks[0] if blocks else ''

    # Parse remaining blocks
    for block in blocks[1:]:
        if not block.strip():
            continue

        entry = {'comments': [], 'msgid': '', 'msgstr': '', 'flags': [], 'references': []}
        in_msgid = False
        in_msgstr = False

        for line in block.split('\n'):
            if line.startswith('#: '):
                entry['references'].append(line[3:])
            elif line.startswith('#, '):
                entry['flags'].append(line[3:])
            elif line.startswith('#'):
                entry['comments'].append(line)
            elif line.startswith('msgid "'):
                in_msgid = True
                in_msgstr = False
                entry['msgid'] = line[7:-1]
            elif line.startswith('msgstr "'):
                in_msgstr = True
                in_msgid = False
                entry['msgstr'] = line[8:-1]
            elif line.startswith('"') and line.endswith('"'):
                content_str = line[1:-1]
                if in_msgid:
                    entry['msgid'] += content_str
                elif in_msgstr:
                    entry['msgstr'] += content_str

        if entry['msgid']:  # Skip empty entries
            entries.append(entry)

    return header, entries


def write_po_file(filepath: Path, header: str, entries: list[dict]):
    """Write .po file back."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(header)
        f.write('\n\n')

        for entry in entries:
            for comment in entry['comments']:
                f.write(comment + '\n')
            for ref in entry['references']:
                f.write(f'#: {ref}\n')
            for flag in entry['flags']:
                if flag != 'fuzzy':  # Remove fuzzy from translated entries
                    f.write(f'#, {flag}\n')
                elif not entry['msgstr']:  # Keep fuzzy only if still untranslated
                    f.write(f'#, {flag}\n')
            f.write(f'msgid "{entry["msgid"]}"\n')
            f.write(f'msgstr "{entry["msgstr"]}"\n')
            f.write('\n')


def cmd_export(filepath: Path):
    """Export untranslated entries as JSON."""
    header, entries = parse_po_file(filepath)

    untranslated = {}
    for i, entry in enumerate(entries):
        if entry['msgid'] and not entry['msgstr']:
            untranslated[str(i)] = entry['msgid']

    output = {
        'file': str(filepath),
        'total_entries': len(entries),
        'untranslated_count': len(untranslated),
        'entries': untranslated,
    }

    print(json.dumps(output, ensure_ascii=False, indent=2))


def cmd_import(filepath: Path):
    """Import translations from stdin JSON."""
    header, entries = parse_po_file(filepath)

    input_data = json.load(sys.stdin)
    translations = input_data.get('translations', {})

    applied = 0
    for idx_str, translation in translations.items():
        idx = int(idx_str)
        if 0 <= idx < len(entries):
            entries[idx]['msgstr'] = translation
            applied += 1

    write_po_file(filepath, header, entries)
    print(f"Applied {applied} translations to {filepath}", file=sys.stderr)


def cmd_apply(filepath: Path, translations_file: Path):
    """Apply translations from a JSON file."""
    header, entries = parse_po_file(filepath)

    with open(translations_file, 'r', encoding='utf-8') as f:
        translations = json.load(f)

    if 'translations' in translations:
        translations = translations['translations']

    applied = 0
    for idx_str, translation in translations.items():
        idx = int(idx_str)
        if 0 <= idx < len(entries):
            entries[idx]['msgstr'] = translation
            applied += 1

    write_po_file(filepath, header, entries)
    print(f"Applied {applied} translations to {filepath}", file=sys.stderr)


def main():
    if len(sys.argv) < 3:
        print("Usage: translate_agent.py <export|import|apply> <po_file> [translations.json]")
        sys.exit(1)

    action = sys.argv[1]
    filepath = Path(sys.argv[2])

    if not filepath.exists():
        print(f"Error: File not found: {filepath}", file=sys.stderr)
        sys.exit(1)

    if action == 'export':
        cmd_export(filepath)
    elif action == 'import':
        cmd_import(filepath)
    elif action == 'apply':
        if len(sys.argv) < 4:
            print("Usage: translate_agent.py apply <po_file> <translations.json>")
            sys.exit(1)
        cmd_apply(filepath, Path(sys.argv[3]))
    else:
        print(f"Unknown action: {action}")
        sys.exit(1)


if __name__ == '__main__':
    main()
