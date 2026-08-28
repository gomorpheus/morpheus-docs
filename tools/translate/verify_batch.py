#!/usr/bin/env python3
"""Check how many of a batch's todo entries are still empty in the originals.

Usage: python3 verify_batch.py <batch_NNN.json>
Prints remaining=N of M; exits 0 only when the batch is fully processed.
"""

import json
import os
import sys

repo = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    manifest_path = sys.argv[1]
    if not os.path.isabs(manifest_path):
        manifest_path = os.path.join(repo, manifest_path)
    with open(manifest_path, 'r', encoding='utf-8') as f:
        m = json.load(f)
    with open(os.path.join(repo, m['todo']), 'r', encoding='utf-8') as f:
        todo = json.load(f)
    by_file = {}
    for t in todo:
        by_file.setdefault(t['file'], []).append(t['line'])
    remaining = 0
    for fname, idxs in by_file.items():
        with open(os.path.join(repo, fname), 'r', encoding='utf-8') as f:
            lines = f.read().split('\n')
        for i in idxs:
            if i < len(lines) and lines[i] == 'msgstr ""':
                remaining += 1
    print(f'remaining={remaining} of {len(todo)}')
    return 0 if remaining == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
