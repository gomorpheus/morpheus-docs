#!/usr/bin/env python3
"""Merge an agent-translated chunk file back into its original .po file.

Fills EMPTY msgstrs in the original with translations from the chunk.
Already-translated entries in the original are never overwritten.
Uses a lock file so concurrent merges on the same original are safe.

Usage:
    python3 merge_chunk.py <orig.po> <chunk.po>

Prints: applied=N existing=M missed=K
    applied  entries filled in
    existing entries in chunk that were already translated in orig
    missed   chunk translations whose msgid was not found in orig
"""

import fcntl
import os
import sys


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


def escape(s):
    return (s.replace('\\', '\\\\')
             .replace('"', '\\"')
             .replace('\r', '')
             .replace('\n', '\\n')
             .replace('\t', '\\t'))


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
    """Return (msgid_unescaped, msgstr_unescaped, msgstr_start, msgstr_end).

    msgstr_start/msgstr_end are indexes into block_lines of the first/last
    physical line of the msgstr field (-1 if absent).
    """
    msgid = ''
    msgstr = ''
    in_msgid = False
    in_msgstr = False
    ms_start = -1
    ms_end = -1
    for idx, line in enumerate(block_lines):
        if line.startswith('msgid "'):
            in_msgid = True
            in_msgstr = False
            msgid = line[7:-1]
        elif line.startswith('msgstr "'):
            in_msgstr = True
            in_msgid = False
            ms_start = idx
            ms_end = idx
            msgstr = line[8:-1]
        elif line.startswith('"') and line.endswith('"') and len(line) >= 2:
            content = line[1:-1]
            if in_msgid:
                msgid += content
            elif in_msgstr:
                msgstr += content
                ms_end = idx
    return unescape(msgid), unescape(msgstr), ms_start, ms_end


def strip_fuzzy(block_lines):
    out = []
    for line in block_lines:
        if line.startswith('#, '):
            flags = [x.strip() for x in line[3:].split(',')]
            flags = [x for x in flags if x != 'fuzzy']
            if flags:
                out.append('#, ' + ', '.join(flags))
            continue
        out.append(line)
    return out


def main():
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    orig_path, chunk_path = sys.argv[1], sys.argv[2]
    if not os.path.exists(orig_path) or not os.path.exists(chunk_path):
        print('ERROR: file not found', file=sys.stderr)
        return 2

    with open(chunk_path, 'r', encoding='utf-8') as f:
        chunk_lines = f.read().split('\n')
    chunk_blocks = split_blocks(chunk_lines)
    chunk_header = 0
    if not any(l.startswith('msgid ""') for l in chunk_blocks[0][2]):
        matches = [k for k, (_, _, bl) in enumerate(chunk_blocks)
                   if any(l.startswith('msgid ""') for l in bl)]
        chunk_header = matches[0] if matches else -1
    translations = {}
    for k, (_start, _end, bl) in enumerate(chunk_blocks):
        if k == chunk_header:
            continue
        msgid, msgstr, _s, _e = logical(bl)
        if msgid and msgstr:
            translations[msgid] = msgstr

    lock_path = orig_path + '.lock'
    with open(lock_path, 'w') as lock_f:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        with open(orig_path, 'r', encoding='utf-8') as f:
            lines = f.read().split('\n')

        applied = 0
        existing = 0
        missed = 0
        seen = set()
        new_file = []
        prev_end = 0
        all_blocks = split_blocks(lines)
        header_idx = 0
        if not any(l.startswith('msgid ""') for l in all_blocks[0][2]):
            matches = [k for k, (_, _, bl) in enumerate(all_blocks)
                       if any(l.startswith('msgid ""') for l in bl)]
            header_idx = matches[0] if matches else -1
        for bidx, (start, end, bl) in enumerate(all_blocks):
            new_file.extend(lines[prev_end:start])
            if bidx == header_idx:
                new_file.extend(bl)
            else:
                msgid, msgstr, ms_start, ms_end = logical(bl)
                if msgid in translations:
                    seen.add(msgid)
                    if not msgstr:
                        new_block = strip_fuzzy(bl[:ms_start])
                        new_block.append('msgstr "' + escape(translations[msgid]) + '"')
                        new_block.extend(bl[ms_end + 1:])
                        new_file.extend(new_block)
                        applied += 1
                    else:
                        new_file.extend(bl)
                        existing += 1
                else:
                    new_file.extend(bl)
            prev_end = end
        new_file.extend(lines[prev_end:])

        for msgid in translations:
            if msgid not in seen:
                missed += 1

        with open(orig_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_file))

    print(f'applied={applied} existing={existing} missed={missed}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
