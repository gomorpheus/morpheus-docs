#!/usr/bin/env python3
"""Inject agent sidecar translations into the original .po files of a batch.

Usage:
    python3 merge_batch.py <batch_NNN.json>

The agent writes sidecar.tsv (path in the manifest) with lines:
    <seq>\\t<translation text>
seq is the entry ordinal in chunk.po (1-based, entries after the header).
Lines are applied to the original file's recorded msgstr line; the line must
still be exactly `msgstr ""`. A `#, fuzzy` flag in the same entry block is
removed. Already-filled lines are reported as conflicts, not overwritten.

Prints one line per original file plus a TOTAL line:
    <file>: applied=N conflict=M
    TOTAL applied=N conflict=M
"""

import fcntl
import json
import os
import sys


def escape(s):
    return (s.replace('\\', '\\\\')
             .replace('"', '\\"')
             .replace('\r', '')
             .replace('\n', '\\n')
             .replace('\t', '\\t'))


def block_range(lines, idx):
    """Return (start, end) 0-based exclusive bounds of the non-blank run containing idx."""
    start = idx
    while start > 0 and lines[start - 1] != '':
        start -= 1
    end = idx
    n = len(lines)
    while end < n and lines[end] != '':
        end += 1
    return start, end


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
        blocks.append(lines[i:j])
        i = j
    return blocks


def logical_msgid(block_lines):
    msgid = ''
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
        elif line.startswith('"') and line.endswith('"') and len(line) >= 2:
            if in_msgid:
                msgid += line[1:-1]
    return unescape(msgid)


def main():
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    here_repo = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    batch_path = sys.argv[1]
    if not os.path.isabs(batch_path):
        batch_path = os.path.join(here_repo, batch_path)
    with open(batch_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    with open(os.path.join(here_repo, manifest['todo']), 'r', encoding='utf-8') as f:
        todo = json.load(f)
    seq_map = {t['seq']: t for t in todo}

    # full msgids per seq come from the chunk (entries in seq order after header)
    seq_msgid = {}
    chunk_lines = open(os.path.join(here_repo, manifest['chunk']), encoding='utf-8').read().split('\n')
    for n, bl in enumerate(split_blocks(chunk_lines)[1:], start=1):
        seq_msgid[n] = logical_msgid(bl)

    # register intentional skips (agent-written skip.tsv: <seq>\t<reason>)
    skip_path = os.path.join(here_repo, manifest.get('skip', '')) if manifest.get('skip') else None
    skipped_path = os.path.join(here_repo, 'tools', 'translate', 'work', manifest['lang'], 'skipped.json')
    skipped = {}
    if os.path.exists(skipped_path):
        with open(skipped_path, 'r', encoding='utf-8') as f:
            skipped = json.load(f)
    skips_registered = 0
    if skip_path and os.path.exists(skip_path):
        with open(skip_path, 'r', encoding='utf-8') as f:
            for raw in f:
                raw = raw.rstrip('\n')
                if not raw:
                    continue
                seq_s, sep, reason = raw.partition('\t')
                if not sep or not seq_s.isdigit():
                    continue
                msgid = seq_msgid.get(int(seq_s))
                if msgid is not None:
                    skipped[msgid] = reason or 'untranslatable'
                    skips_registered += 1
    with open(skipped_path, 'w', encoding='utf-8') as f:
        json.dump(skipped, f, ensure_ascii=False, indent=0)

    sidecar_path = os.path.join(here_repo, manifest['sidecar'])
    translations = {}
    if os.path.exists(sidecar_path):
        with open(sidecar_path, 'r', encoding='utf-8') as f:
            for raw in f:
                raw = raw.rstrip('\n')
                if not raw:
                    continue
                seq_s, sep, text = raw.partition('\t')
                if not sep:
                    print(f'WARN: bad sidecar line skipped: {raw[:60]!r}', file=sys.stderr)
                    continue
                try:
                    seq = int(seq_s)
                except ValueError:
                    print(f'WARN: bad seq skipped: {raw[:60]!r}', file=sys.stderr)
                    continue
                if text:
                    translations[seq] = unescape(text)
    else:
        print('WARN: sidecar not found, nothing to merge', file=sys.stderr)

    # group by original file
    by_file = {}
    for seq, text in translations.items():
        t = seq_map.get(seq)
        if t is None:
            print(f'WARN: seq {seq} not in todo, skipped', file=sys.stderr)
            continue
        by_file.setdefault(t['file'], []).append((t['line'], text))

    total_applied = 0
    total_conflict = 0
    for fname in sorted(by_file):
        fpath = os.path.join(here_repo, fname)
        lock_path = fpath + '.lock'
        with open(lock_path, 'w') as lock_f:
            fcntl.flock(lock_f, fcntl.LOCK_EX)
            with open(fpath, 'r', encoding='utf-8') as f:
                lines = f.read().split('\n')
            applied = 0
            conflict = 0
            drop_flag_lines = set()
            for line_idx, text in by_file[fname]:
                if line_idx >= len(lines):
                    conflict += 1
                    continue
                if lines[line_idx] != 'msgstr ""':
                    conflict += 1
                    continue
                lines[line_idx] = 'msgstr "' + escape(text) + '"'
                start, end = block_range(lines, line_idx)
                for k in range(start, line_idx):
                    if lines[k].startswith('#, ') and 'fuzzy' in lines[k]:
                        flags = [x.strip() for x in lines[k][3:].split(',') if x.strip() != 'fuzzy']
                        if flags:
                            lines[k] = '#, ' + ', '.join(flags)
                        else:
                            drop_flag_lines.add(k)
                applied += 1
            for k in sorted(drop_flag_lines, reverse=True):
                del lines[k]
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
        total_applied += applied
        total_conflict += conflict
        print(f'{fname}: applied={applied} conflict={conflict}')
    print(f'TOTAL applied={total_applied} conflict={total_conflict} skips_registered={skips_registered}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
