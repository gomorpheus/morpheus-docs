#!/usr/bin/env python3
"""Report translation completeness per locale (untranslated msgstr counts).

Usage:
    python3 count_po.py                # all locales
    python3 count_po.py fr de          # specific locales
    python3 count_po.py fr --files     # also list files with remaining work
"""

import argparse
import os
import sys

JUNK_DIRS = ('.hero', '.opencode', 'node_modules')
LOCALES = ['es', 'fr', 'de', 'pt']


def parse_po_file(filepath):
    entries = []
    current = {'msgid': '', 'msgstr': ''}
    in_msgid = False
    in_msgstr = False
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if line.startswith('msgid "'):
                in_msgid = True
                in_msgstr = False
                current['msgid'] = line[7:-1]
            elif line.startswith('msgstr "'):
                in_msgstr = True
                in_msgid = False
                current['msgstr'] = line[8:-1]
            elif line.startswith('"') and line.endswith('"') and len(line) >= 2:
                content = line[1:-1]
                if in_msgid:
                    current['msgid'] += content
                elif in_msgstr:
                    current['msgstr'] += content
            elif line == '':
                if current['msgid'] or current['msgstr']:
                    entries.append(current)
                current = {'msgid': '', 'msgstr': ''}
                in_msgid = False
                in_msgstr = False
    if current['msgid'] or current['msgstr']:
        entries.append(current)
    return entries


def count_locale(base):
    total = 0
    untranslated = 0
    files = 0
    per_file = []
    for root, dirs, fnames in os.walk(base):
        dirs[:] = [d for d in dirs if d not in JUNK_DIRS]
        for fn in sorted(fnames):
            if not fn.endswith('.po'):
                continue
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, base)
            remaining = 0
            for e in parse_po_file(path):
                if not e['msgid']:
                    continue
                total += 1
                if not e['msgstr']:
                    untranslated += 1
                    remaining += 1
            files += 1
            if remaining:
                per_file.append((remaining, rel))
    per_file.sort(reverse=True)
    return total, untranslated, files, per_file


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('langs', nargs='*', default=LOCALES)
    ap.add_argument('--files', action='store_true', help='list files with remaining work')
    ap.add_argument('--top', type=int, default=0, help='show top N files with remaining work')
    args = ap.parse_args()

    repo = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print(f"{'lang':5} {'translated':>10} {'total':>8} {'pct':>6} {'files':>6}")
    for lang in args.langs:
        base = os.path.join(repo, 'locale', lang, 'LC_MESSAGES')
        if not os.path.isdir(base):
            print(f'{lang:5} (missing {base})')
            continue
        total, untranslated, files, per_file = count_locale(base)
        pct = (total - untranslated) / total * 100 if total else 0
        print(f'{lang:5} {total - untranslated:>10} {total:>8} {pct:>5.1f}% {files:>6}')
        if (args.files or args.top) and per_file:
            limit = args.top or len(per_file)
            for remaining, rel in per_file[:limit]:
                print(f'      {remaining:>5}  {rel}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
