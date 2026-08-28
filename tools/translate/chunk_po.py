#!/usr/bin/env python3
"""Split untranslated .po entries into chunk files for agent translation.

Each chunk file contains the source file's .po header plus a consecutive group
of untranslated entries (raw lines, byte-for-byte). A sidecar glossary file
lists the glossary terms that appear in the chunk's msgids.

Usage:
    python3 chunk_po.py --lang fr
    python3 chunk_po.py --lang es --chunk-size 250 --out tools/translate/work
"""

import argparse
import json
import os
import sys

JUNK_DIRS = ('.hero', '.opencode', 'node_modules')
DEFAULT_GLOSSARIES = {
    'es': 'glossary.json',
    'fr': 'glossary_fr.json',
    'de': 'glossary_de.json',
    'pt': 'glossary_pt.json',
}
MAX_GLOSSARY_TERMS = 500


def unescape(s):
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == '\\' and i + 1 < len(s):
            n = s[i + 1]
            if n in ('n', 't', 'r'):
                out.append({'n': '\n', 't': '\t', 'r': '\r'}[n])
                i += 2
                continue
            if n in ('\\', '"'):
                out.append(n)
                i += 2
                continue
        out.append(c)
        i += 1
    return ''.join(out)


def split_blocks(lines):
    """Return list of (start, end, block_lines) for non-blank line runs."""
    blocks = []
    i = 0
    n = len(lines)
    while i < n:
        if lines[i] == '':
            i += 1
            continue
        j = i
        while j < n and lines[j] != '':
            j += 1
        blocks.append((i, j, lines[i:j]))
        i = j
    return blocks


def logical(block_lines):
    """Return (msgid, msgstr) as unescaped logical strings for an entry block."""
    msgid = ''
    msgstr = ''
    in_msgid = False
    in_msgstr = False
    for line in block_lines:
        if line.startswith('msgid "'):
            in_msgid = True
            in_msgstr = False
            msgid = line[7:-1]
        elif line.startswith('msgstr "'):
            in_msgstr = True
            in_msgid = False
            msgstr = line[8:-1]
        elif line.startswith('"') and line.endswith('"') and len(line) >= 2:
            content = line[1:-1]
            if in_msgid:
                msgid += content
            elif in_msgstr:
                msgstr += content
    return unescape(msgid), unescape(msgstr)


def sanitize(rel):
    return rel.replace('/', '__').removesuffix('.po')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--lang', required=True)
    ap.add_argument('--chunk-size', type=int, default=250)
    ap.add_argument('--out', default=None)
    ap.add_argument('--glossary', default=None)
    args = ap.parse_args()

    here = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.dirname(os.path.dirname(here))
    base = os.path.join(repo, 'locale', args.lang, 'LC_MESSAGES')
    out_dir = args.out or os.path.join(repo, 'tools', 'translate', 'work', args.lang)
    chunk_dir = os.path.join(out_dir, 'chunks')
    os.makedirs(chunk_dir, exist_ok=True)

    if args.glossary:
        glossary_path = args.glossary
    else:
        glossary_path = os.path.join(here, DEFAULT_GLOSSARIES.get(args.lang, 'glossary.json'))
    with open(glossary_path, 'r', encoding='utf-8') as f:
        glossary = json.load(f)

    jobs = []
    files_with_work = 0
    total_entries = 0
    for root, dirs, fnames in os.walk(base):
        dirs[:] = [d for d in dirs if d not in JUNK_DIRS]
        for fn in sorted(fnames):
            if not fn.endswith('.po'):
                continue
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, base)
            with open(path, 'r', encoding='utf-8') as f:
                lines = f.read().split('\n')
            blocks = split_blocks(lines)
            if not blocks:
                continue
            header_idx = 0
            if not any(l.startswith('msgid ""') for l in blocks[0][2]):
                matches = [k for k, (_, _, bl) in enumerate(blocks)
                           if any(l.startswith('msgid ""') for l in bl)]
                if not matches:
                    print(f'WARN: no header in {rel}', file=sys.stderr)
                    continue
                header_idx = matches[0]
            header_block = blocks[header_idx][2]
            untranslated = []
            for k, (start, end, bl) in enumerate(blocks):
                if k == header_idx:
                    continue
                msgid, msgstr = logical(bl)
                if msgid and not msgstr:
                    untranslated.append(bl)
            if not untranslated:
                continue
            files_with_work += 1
            total_entries += len(untranslated)
            for seq, group_start in enumerate(range(0, len(untranslated), args.chunk_size), 1):
                group = untranslated[group_start:group_start + args.chunk_size]
                parts = ['\n'.join(header_block)]
                parts.extend('\n'.join(b) for b in group)
                chunk_rel = f'{sanitize(rel)}__{seq:03d}.po'
                chunk_path = os.path.join(chunk_dir, chunk_rel)
                with open(chunk_path, 'w', encoding='utf-8') as f:
                    f.write('\n\n'.join(parts) + '\n')

                combined = ' '.join(logical(b)[0].lower() for b in group)
                terms = {
                    eng: trans
                    for eng, trans in glossary.items()
                    if len(eng) >= 2 and eng.lower() in combined
                }
                if len(terms) > MAX_GLOSSARY_TERMS:
                    terms = dict(sorted(terms.items(), key=lambda kv: -len(kv[0]))[:MAX_GLOSSARY_TERMS])
                glossary_path_chunk = os.path.join(chunk_dir, chunk_rel[:-3] + '.glossary.json')
                with open(glossary_path_chunk, 'w', encoding='utf-8') as f:
                    json.dump(terms, f, ensure_ascii=False, indent=0)

                jobs.append({
                    'chunk': os.path.relpath(chunk_path, repo),
                    'glossary': os.path.relpath(glossary_path_chunk, repo),
                    'orig': os.path.relpath(path, repo),
                    'file': rel,
                    'count': len(group),
                })

    jobs_path = os.path.join(out_dir, 'jobs.json')
    with open(jobs_path, 'w', encoding='utf-8') as f:
        json.dump(jobs, f, ensure_ascii=False, indent=1)

    print(f'lang={args.lang} files_with_work={files_with_work} '
          f'untranslated_entries={total_entries} chunks={len(jobs)} -> {jobs_path}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
