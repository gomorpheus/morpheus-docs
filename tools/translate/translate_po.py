#!/usr/bin/env python3
"""
AI Translation Pipeline for Sphinx .po files.

Translates .po file msgid entries into Spanish using an AI model,
constrained by the official Morpheus UI glossary to ensure terminology consistency.

Usage:
    python3 translate_po.py [options] <po_file_or_directory>

Options:
    --lang LANG         Target language code (default: es)
    --glossary PATH     Path to glossary JSON (default: tools/translate/glossary.json)
    --model MODEL       AI model to use (default: gpt-4o)
    --batch-size N      Number of msgids per API call (default: 20)
    --dry-run           Show what would be translated without calling API
    --resume            Skip already-translated entries (non-empty msgstr)
    --report PATH       Write translation report to file
    --verbose           Show progress details
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Optional


def parse_po_file(filepath: Path) -> list[dict]:
    """Parse a .po file into a list of translation entries."""
    entries = []
    current = {'comments': [], 'msgid': '', 'msgstr': '', 'flags': [], 'references': []}
    in_msgid = False
    in_msgstr = False

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')

            if line.startswith('#: '):
                current['references'].append(line[3:])
            elif line.startswith('#, '):
                current['flags'].append(line[3:])
            elif line.startswith('#'):
                current['comments'].append(line)
            elif line.startswith('msgid "'):
                in_msgid = True
                in_msgstr = False
                current['msgid'] = line[7:-1]  # Strip msgid " ... "
            elif line.startswith('msgstr "'):
                in_msgstr = True
                in_msgid = False
                current['msgstr'] = line[8:-1]  # Strip msgstr " ... "
            elif line.startswith('"') and line.endswith('"'):
                # Continuation line
                content = line[1:-1]
                if in_msgid:
                    current['msgid'] += content
                elif in_msgstr:
                    current['msgstr'] += content
            elif line == '':
                # Empty line = end of entry
                if current['msgid'] or current['msgstr']:
                    entries.append(current)
                current = {'comments': [], 'msgid': '', 'msgstr': '', 'flags': [], 'references': []}
                in_msgid = False
                in_msgstr = False

    # Don't forget last entry
    if current['msgid'] or current['msgstr']:
        entries.append(current)

    return entries


def write_po_file(filepath: Path, entries: list[dict], header: str = ''):
    """Write entries back to a .po file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        if header:
            f.write(header + '\n\n')

        for entry in entries:
            for comment in entry['comments']:
                f.write(comment + '\n')
            for ref in entry['references']:
                f.write(f'#: {ref}\n')
            for flag in entry['flags']:
                f.write(f'#, {flag}\n')

            # Write msgid (handle multiline)
            msgid = entry['msgid']
            f.write(f'msgid "{msgid}"\n')

            # Write msgstr (handle multiline)
            msgstr = entry['msgstr']
            f.write(f'msgstr "{msgstr}"\n')

            f.write('\n')


def extract_po_header(filepath: Path) -> str:
    """Extract the .po file header (everything before the first real entry)."""
    header_lines = []
    with open(filepath, 'r', encoding='utf-8') as f:
        in_header = True
        seen_first_msgid = False
        for line in f:
            line = line.rstrip('\n')
            if line.startswith('msgid "') and not seen_first_msgid:
                seen_first_msgid = True
                header_lines.append(line)
            elif seen_first_msgid and line == '':
                header_lines.append(line)
                break
            elif seen_first_msgid:
                header_lines.append(line)
            else:
                header_lines.append(line)
    return '\n'.join(header_lines)


def should_translate(msgid: str) -> bool:
    """Determine if a msgid should be translated or left as-is."""
    if not msgid:
        return False
    # Skip pure markup/formatting strings
    if re.match(r'^[\s\-=~`\^\.]+$', msgid):
        return False
    # Skip pure code/paths
    if re.match(r'^[/\w\.\-]+\.(sh|py|rb|yml|yaml|json|conf|cfg|ini|log|txt)$', msgid):
        return False
    return True


def build_translation_prompt(msgids: list[str], glossary: dict, target_lang: str = 'es') -> str:
    """Build the prompt for the AI model to translate a batch of msgids."""
    # Select relevant glossary terms (terms that appear in any of the msgids)
    combined_text = ' '.join(msgids).lower()
    relevant_terms = {}
    for english, spanish in glossary.items():
        if english.lower() in combined_text:
            relevant_terms[english] = spanish

    # Build the prompt
    prompt = f"""You are a technical documentation translator. Translate the following documentation strings from English to Spanish (es).

RULES:
1. Use these EXACT translations for product terms (from the official Morpheus UI):
"""
    if relevant_terms:
        for eng, spa in sorted(relevant_terms.items()):
            prompt += f"   - \"{eng}\" → \"{spa}\"\n"
    else:
        prompt += "   (no specific terms detected in this batch)\n"

    prompt += """
2. PRESERVE all RST/Markdown markup exactly:
   - :ref:`target` — keep role name and target, translate display text only if explicit
   - :doc:`path` — keep the path unchanged
   - :guilabel:`text` — translate the text inside
   - :menuselection:`A --> B` — translate menu items
   - ``code`` — do NOT translate inline code
   - **bold** and *italic* — translate the text, keep the markup
   - Cross-reference targets like `Section Name`_ — translate display, keep underscore
3. Do NOT translate:
   - Code blocks, CLI commands, file paths, URLs
   - Product name "HPE Morpheus Enterprise" or "Morpheus"
   - API endpoint paths, parameter names, environment variables
   - Version numbers, package names
4. Maintain the same RST/Markdown structure and spacing
5. Return ONLY the translations, one per line, in the same order as the input
6. If a string is pure formatting/markup with no translatable text, return it unchanged

INPUT STRINGS (one per numbered line):
"""
    for i, msgid in enumerate(msgids, 1):
        prompt += f"{i}. {msgid}\n"

    prompt += """
OUTPUT (one translation per numbered line, same order):"""

    return prompt


def translate_batch_openai(prompt: str, model: str = 'gpt-4o') -> list[str]:
    """Call OpenAI API to translate a batch."""
    try:
        import openai
    except ImportError:
        print("Error: openai package not installed. Run: pip3 install openai", file=sys.stderr)
        sys.exit(1)

    client = openai.OpenAI()
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a professional technical translator. Return only the numbered translations, nothing else."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,  # Low temperature for consistency
    )

    result_text = response.choices[0].message.content.strip()
    # Parse numbered lines
    translations = []
    for line in result_text.split('\n'):
        line = line.strip()
        if not line:
            continue
        # Remove numbering prefix (e.g., "1. ", "1) ", "1: ")
        match = re.match(r'^\d+[\.\)\:]\s*(.*)$', line)
        if match:
            translations.append(match.group(1))
        else:
            translations.append(line)

    return translations


def translate_batch_anthropic(prompt: str, model: str = 'claude-sonnet-4-20250514') -> list[str]:
    """Call Anthropic API to translate a batch."""
    try:
        import anthropic
    except ImportError:
        print("Error: anthropic package not installed. Run: pip3 install anthropic", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic()
    response = client.messages.create(
        model=model,
        max_tokens=4096,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,
    )

    result_text = response.content[0].text.strip()
    translations = []
    for line in result_text.split('\n'):
        line = line.strip()
        if not line:
            continue
        match = re.match(r'^\d+[\.\)\:]\s*(.*)$', line)
        if match:
            translations.append(match.group(1))
        else:
            translations.append(line)

    return translations


def translate_po_file(
    filepath: Path,
    glossary: dict,
    target_lang: str = 'es',
    model: str = 'gpt-4o',
    batch_size: int = 20,
    resume: bool = True,
    dry_run: bool = False,
    verbose: bool = False,
) -> dict:
    """Translate a single .po file. Returns a report dict."""
    report = {
        'file': str(filepath),
        'total_entries': 0,
        'translated': 0,
        'skipped_existing': 0,
        'skipped_notranslate': 0,
        'errors': [],
    }

    # Read the full file content to preserve header
    raw_content = filepath.read_text(encoding='utf-8')

    # Split header from entries
    # Header is the first msgid/msgstr block (with empty msgid)
    entries = parse_po_file(filepath)
    report['total_entries'] = len(entries)

    # Separate header entry (msgid = "") from content entries
    header_entry = None
    content_entries = []
    for entry in entries:
        if entry['msgid'] == '':
            header_entry = entry
        else:
            content_entries.append(entry)

    # Collect entries needing translation
    to_translate = []
    for entry in content_entries:
        if resume and entry['msgstr']:
            report['skipped_existing'] += 1
            continue
        if not should_translate(entry['msgid']):
            report['skipped_notranslate'] += 1
            continue
        to_translate.append(entry)

    if verbose:
        print(f"  {filepath.name}: {len(to_translate)} entries to translate "
              f"({report['skipped_existing']} existing, {report['skipped_notranslate']} skipped)")

    if dry_run or not to_translate:
        return report

    # Translate in batches
    for i in range(0, len(to_translate), batch_size):
        batch = to_translate[i:i + batch_size]
        msgids = [entry['msgid'] for entry in batch]

        prompt = build_translation_prompt(msgids, glossary, target_lang)

        try:
            if 'claude' in model or 'anthropic' in model:
                translations = translate_batch_anthropic(prompt, model)
            else:
                translations = translate_batch_openai(prompt, model)

            # Apply translations
            for j, entry in enumerate(batch):
                if j < len(translations):
                    entry['msgstr'] = translations[j]
                    report['translated'] += 1
                else:
                    report['errors'].append(f"Missing translation for: {entry['msgid'][:50]}")

        except Exception as e:
            report['errors'].append(f"API error on batch {i//batch_size}: {str(e)}")
            if verbose:
                print(f"  Error: {e}", file=sys.stderr)

        # Rate limiting
        time.sleep(0.5)

    # Remove fuzzy flags from translated entries
    for entry in content_entries:
        if entry['msgstr'] and 'fuzzy' in entry.get('flags', []):
            entry['flags'].remove('fuzzy')

    # Write back
    all_entries = ([header_entry] if header_entry else []) + content_entries
    write_po_file(filepath, all_entries)

    return report


def find_po_files(path: Path, section: Optional[str] = None) -> list[Path]:
    """Find all .po files under a path, optionally filtered by section."""
    if path.is_file() and path.suffix == '.po':
        return [path]

    pattern = '**/*.po'
    if section:
        pattern = f'{section}/**/*.po'

    return sorted(path.glob(pattern))


def main():
    parser = argparse.ArgumentParser(description='Translate .po files using AI')
    parser.add_argument('path', help='Path to .po file or directory containing .po files')
    parser.add_argument('--lang', default='es', help='Target language code (default: es)')
    parser.add_argument('--glossary', default=None, help='Path to glossary JSON')
    parser.add_argument('--model', default='gpt-4o', help='AI model to use (default: gpt-4o)')
    parser.add_argument('--batch-size', type=int, default=20, help='Entries per API call (default: 20)')
    parser.add_argument('--dry-run', action='store_true', help='Show plan without translating')
    parser.add_argument('--resume', action='store_true', default=True, help='Skip already-translated entries')
    parser.add_argument('--no-resume', action='store_false', dest='resume', help='Re-translate all entries')
    parser.add_argument('--report', default=None, help='Write report to file')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show progress')
    parser.add_argument('--section', default=None, help='Only translate a specific section (e.g., getting_started)')

    args = parser.parse_args()

    # Load glossary
    if args.glossary:
        glossary_path = Path(args.glossary)
    else:
        glossary_path = Path(__file__).parent / 'glossary.json'

    if not glossary_path.exists():
        print(f"Error: Glossary not found: {glossary_path}", file=sys.stderr)
        print("Run extract_glossary.py first.", file=sys.stderr)
        sys.exit(1)

    with open(glossary_path, 'r', encoding='utf-8') as f:
        glossary = json.load(f)

    print(f"Loaded glossary: {len(glossary)} terms", file=sys.stderr)

    # Find .po files
    target_path = Path(args.path)
    if not target_path.exists():
        print(f"Error: Path not found: {target_path}", file=sys.stderr)
        sys.exit(1)

    po_files = find_po_files(target_path, args.section)
    print(f"Found {len(po_files)} .po files", file=sys.stderr)

    if args.dry_run:
        print("\n=== DRY RUN ===")
        for f in po_files:
            entries = parse_po_file(f)
            untranslated = sum(1 for e in entries if e['msgid'] and not e['msgstr'] and should_translate(e['msgid']))
            if untranslated > 0:
                print(f"  {f}: {untranslated} entries to translate")
        return

    # Translate
    reports = []
    total_files = len(po_files)
    for idx, po_file in enumerate(po_files, 1):
        if args.verbose:
            print(f"\n[{idx}/{total_files}] {po_file}")

        report = translate_po_file(
            po_file,
            glossary=glossary,
            target_lang=args.lang,
            model=args.model,
            batch_size=args.batch_size,
            resume=args.resume,
            dry_run=args.dry_run,
            verbose=args.verbose,
        )
        reports.append(report)

    # Summary
    total_translated = sum(r['translated'] for r in reports)
    total_errors = sum(len(r['errors']) for r in reports)
    total_skipped = sum(r['skipped_existing'] for r in reports)

    print(f"\n=== Translation Complete ===")
    print(f"Files processed: {len(reports)}")
    print(f"Entries translated: {total_translated}")
    print(f"Entries skipped (existing): {total_skipped}")
    print(f"Errors: {total_errors}")

    # Write report if requested
    if args.report:
        report_path = Path(args.report)
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump({
                'summary': {
                    'files_processed': len(reports),
                    'total_translated': total_translated,
                    'total_skipped_existing': total_skipped,
                    'total_errors': total_errors,
                },
                'files': reports,
            }, f, indent=2, ensure_ascii=False)
        print(f"Report written to: {report_path}")


if __name__ == '__main__':
    main()
