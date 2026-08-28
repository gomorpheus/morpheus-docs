#!/usr/bin/env python3
"""Build per-agent translation batches (combined chunk + glossary + todo).

For a language, scans all locale .po files for entries with an empty msgstr,
groups them into batches of at most --max-strings entries (entries of the same
file stay contiguous), and writes per batch:

  chunk.po    - combined .po (one header + all entry blocks, raw lines)
  glossary.json - union of glossary terms found in the batch's msgids
  todo.json   - seq -> (original file, msgstr line) mapping + counts
  batch_NNN.json - manifest the agent receives

The agent reads chunk.po + glossary.json, then writes sidecar.tsv with lines:
    <seq>\\t<translation text>
(one line per translated entry; entries intentionally left empty are omitted).
merge_batch.py injects those translations into the original .po files.

Usage:
    python3 build_batches.py --lang fr [--max-strings 800]
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
MAX_GLOSSARY_TERMS = 400


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


def msgstr_line_index(block_lines):
    for idx, line in enumerate(block_lines):
        if line.startswith('msgstr "'):
            return idx
    return -1


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--lang', required=True)
    ap.add_argument('--max-strings', type=int, default=800)
    ap.add_argument('--glossary', default=None)
    args = ap.parse_args()

    here = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.dirname(os.path.dirname(here))
    base = os.path.join(repo, 'locale', args.lang, 'LC_MESSAGES')
    work = os.path.join(repo, 'tools', 'translate', 'work', args.lang)
    batch_dir = os.path.join(work, 'batches')
    os.makedirs(batch_dir, exist_ok=True)
    for fn in os.listdir(batch_dir):
        p = os.path.join(batch_dir, fn)
        if os.path.isfile(p):
            os.remove(p)

    if args.glossary:
        glossary_path = args.glossary
    else:
        glossary_path = os.path.join(here, DEFAULT_GLOSSARIES.get(args.lang, 'glossary.json'))
    with open(glossary_path, 'r', encoding='utf-8') as f:
        glossary = json.load(f)

    skip_path = os.path.join(work, 'skipped.json')
    skipped = {}
    if os.path.exists(skip_path):
        with open(skip_path, 'r', encoding='utf-8') as f:
            skipped = json.load(f)

    # entries: list of dicts in file order
    entries = []
    skipped_excluded = 0
    for root, dirs, fnames in os.walk(base):
        dirs[:] = [d for d in dirs if d not in JUNK_DIRS]
        for fn in sorted(fnames):
            if not fn.endswith('.po'):
                continue
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, repo)
            with open(path, 'r', encoding='utf-8') as f:
                lines = f.read().split('\n')
            blocks = split_blocks(lines)
            if not blocks:
                continue
            for k, (start, end, bl) in enumerate(blocks):
                if k == 0:
                    continue
                msgid, msgstr = logical(bl)
                if msgid and not msgstr:
                    if msgid in skipped:
                        skipped_excluded += 1
                        continue
                    ml = msgstr_line_index(bl)
                    if ml == -1:
                        continue
                    entries.append({
                        'file': rel,
                        'line': start + ml,  # 0-based index in file
                        'msgid': msgid,
                        'block': bl,
                    })

    print(f'lang={args.lang} untranslated_entries={len(entries)}', file=sys.stderr)

    batches = []
    cur = []
    for e in entries:
        cur.append(e)
        if len(cur) >= args.max_strings:
            batches.append(cur)
            cur = []
    if cur:
        batches.append(cur)

    for i, batch in enumerate(batches):
        bdir = os.path.join(batch_dir, f'batch_{i:03d}')
        os.makedirs(bdir, exist_ok=True)
        # header from first file in batch
        first_file = os.path.join(repo, batch[0]['file'])
        with open(first_file, 'r', encoding='utf-8') as f:
            first_lines = f.read().split('\n')
        header_block = split_blocks(first_lines)[0][2]

        chunk_lines = ['\n'.join(header_block)]
        for n, e in enumerate(batch, start=1):
            chunk_lines.append(f'# SEQ: {n}\n' + '\n'.join(e['block']))
        chunk_path = os.path.join(bdir, 'chunk.po')
        with open(chunk_path, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(chunk_lines) + '\n')

        combined = ' '.join(e['msgid'].lower() for e in batch)
        terms = {eng: trans for eng, trans in glossary.items()
                 if len(eng) >= 2 and eng.lower() in combined}
        if len(terms) > MAX_GLOSSARY_TERMS:
            terms = dict(sorted(terms.items(), key=lambda kv: -len(kv[0]))[:MAX_GLOSSARY_TERMS])
        glossary_b = os.path.join(bdir, 'glossary.json')
        with open(glossary_b, 'w', encoding='utf-8') as f:
            json.dump(terms, f, ensure_ascii=False, indent=0)

        for e, n in zip(batch, range(len(batch))):
            e['todo'] = {
                'seq': n + 1,
                'file': e['file'],
                'line': e['line'],
                'msgid_preview': e['msgid'][:100],
            }
        todo_path = os.path.join(bdir, 'todo.json')
        with open(todo_path, 'w', encoding='utf-8') as f:
            json.dump([e['todo'] for e in batch], f, ensure_ascii=False, indent=0)

        manifest = {
            'lang': args.lang,
            'batch': i,
            'count': len(batch),
            'files': sorted({e['file'] for e in batch}),
            'chunk': os.path.relpath(chunk_path, repo),
            'glossary': os.path.relpath(glossary_b, repo),
            'todo': os.path.relpath(todo_path, repo),
            'sidecar': os.path.relpath(os.path.join(bdir, 'sidecar.tsv'), repo),
            'skip': os.path.relpath(os.path.join(bdir, 'skip.tsv'), repo),
        }
        with open(os.path.join(batch_dir, f'batch_{i:03d}.json'), 'w', encoding='utf-8') as f:
            json.dump(manifest, f, ensure_ascii=False, indent=1)

    total = sum(len(b) for b in batches)
    print(f'lang={args.lang} batches={len(batches)} strings={total} '
          f'skipped_excluded={skipped_excluded} '
          f'avg={total // max(1, len(batches))}/batch -> {batch_dir}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
