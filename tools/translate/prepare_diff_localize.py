#!/usr/bin/env python3
"""Prepare incremental Sphinx gettext localization for CI agent workflows.

Runs gettext + sphinx-intl update for one target language, then reports .po files
that still need translation (empty msgstr or fuzzy entries touched by this update).

Usage:
    python3 tools/translate/prepare_diff_localize.py --lang es
    python3 tools/translate/prepare_diff_localize.py --lang fr --check-skip-commit
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

SKIP_COMMIT_PATTERNS = (
    r"\[bulk-i18n\]",
    r"\[skip-localize\]",
    r"chore\(i18n\):\s*bulk",
)

ENGLISH_DOC_SUFFIXES = (".rst", ".md")
ENGLISH_DOC_EXCLUDE_PREFIXES = (
    "locale/",
    "tools/translate/work/",
    "_build/",
    "z_in_progress/",
    ".github/",
    ".hero/",
    ".opencode/",
)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def run(cmd: list[str], cwd: Path) -> None:
    print("+", " ".join(cmd), file=sys.stderr)
    subprocess.run(cmd, cwd=cwd, check=True)


def should_skip_commit_message(message: str) -> bool:
    for pattern in SKIP_COMMIT_PATTERNS:
        if re.search(pattern, message, re.IGNORECASE):
            return True
    return False


def english_docs_in_diff(base: str, head: str, root: Path) -> list[str]:
    out = subprocess.check_output(
        ["git", "diff", "--name-only", f"{base}..{head}"],
        cwd=root,
        text=True,
    )
    changed: list[str] = []
    for line in out.splitlines():
        path = line.strip()
        if not path:
            continue
        if any(path.startswith(prefix) for prefix in ENGLISH_DOC_EXCLUDE_PREFIXES):
            continue
        if Path(path).suffix.lower() in ENGLISH_DOC_SUFFIXES:
            changed.append(path)
    return changed


def parse_po_needing_translation(po_path: Path) -> tuple[int, int]:
    """Return (needs_translation_count, fuzzy_count) for non-header entries."""
    needs = 0
    fuzzy = 0
    in_header = True
    current_flags: list[str] = []
    msgid = ""
    msgstr = ""
    in_msgid = False
    in_msgstr = False

    with po_path.open(encoding="utf-8") as handle:
        for raw in handle:
            line = raw.rstrip("\n")
            if line.startswith("#, "):
                current_flags.extend(part.strip() for part in line[3:].split(","))
            elif line.startswith('msgid "'):
                in_msgid = True
                in_msgstr = False
                msgid = line[7:-1]
            elif line.startswith('msgstr "'):
                in_msgstr = True
                in_msgid = False
                msgstr = line[8:-1]
            elif line.startswith('"') and line.endswith('"'):
                chunk = line[1:-1]
                if in_msgid:
                    msgid += chunk
                elif in_msgstr:
                    msgstr += chunk
            elif line == "":
                if in_header and msgid == "" and msgstr != "":
                    in_header = False
                elif msgid:
                    if "fuzzy" in current_flags:
                        fuzzy += 1
                        needs += 1
                    elif msgstr == "":
                        needs += 1
                current_flags = []
                msgid = ""
                msgstr = ""
                in_msgid = False
                in_msgstr = False

    return needs, fuzzy


def collect_pending_po_files(locale_base: Path) -> list[dict]:
    pending: list[dict] = []
    for po_path in sorted(locale_base.rglob("*.po")):
        needs, fuzzy = parse_po_needing_translation(po_path)
        if needs:
            pending.append(
                {
                    "path": po_path.relative_to(repo_root()).as_posix(),
                    "needs_translation": needs,
                    "fuzzy": fuzzy,
                }
            )
    return pending


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lang", required=True, help="Target locale code (es, fr, de, pt)")
    parser.add_argument("--base-ref", default="HEAD~1", help="Git base ref for English doc diff")
    parser.add_argument("--head-ref", default="HEAD", help="Git head ref for English doc diff")
    parser.add_argument(
        "--commit-message",
        default="",
        help="Commit message to evaluate for bulk-i18n skip markers",
    )
    parser.add_argument(
        "--check-skip-commit",
        action="store_true",
        help="Exit 2 when the commit message marks a manual bulk localization",
    )
    parser.add_argument(
        "--check-english-changes",
        action="store_true",
        help="Exit 3 when no English doc files changed in the diff",
    )
    parser.add_argument(
        "--skip-intl-update",
        action="store_true",
        help="Only scan existing .po files; do not run make gettext / sphinx-intl",
    )
    parser.add_argument(
        "--manifest",
        default="",
        help="Write JSON manifest for the localization agent",
    )
    args = parser.parse_args()

    root = repo_root()
    locale_base = root / "locale" / args.lang / "LC_MESSAGES"
    if not locale_base.is_dir():
        print(f"ERROR: locale directory not found: {locale_base}", file=sys.stderr)
        return 1

    if args.check_skip_commit and args.commit_message:
        if should_skip_commit_message(args.commit_message):
            print("SKIP: bulk localization commit marker detected", file=sys.stderr)
            return 2

    english_changed = english_docs_in_diff(args.base_ref, args.head_ref, root)
    if args.check_english_changes and not english_changed:
        print("SKIP: no English documentation changes in diff", file=sys.stderr)
        return 3

    if not args.skip_intl_update:
        run(["make", "gettext"], cwd=root)
        run(
            [
                "sphinx-intl",
                "update",
                "-p",
                str(root / "_build/gettext"),
                "-l",
                args.lang,
                "-d",
                str(root / "locale"),
            ],
            cwd=root,
        )

    pending = collect_pending_po_files(locale_base)
    glossary_map = {
        "es": "tools/translate/glossary.json",
        "fr": "tools/translate/glossary_fr.json",
        "de": "tools/translate/glossary_de.json",
        "pt": "tools/translate/glossary_pt.json",
    }
    lang_names = {
        "es": "Spanish",
        "fr": "French",
        "de": "German",
        "pt": "Portuguese (Brazil)",
    }

    manifest = {
        "lang": args.lang,
        "lang_name": lang_names[args.lang],
        "glossary": glossary_map[args.lang],
        "english_files_changed": english_changed,
        "pending_files": pending,
        "pending_entry_count": sum(item["needs_translation"] for item in pending),
    }

    if args.manifest:
        manifest_path = Path(args.manifest)
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote manifest: {manifest_path}", file=sys.stderr)
    else:
        print(json.dumps(manifest, indent=2))

    if not pending:
        print("SKIP: no pending translations after intl update", file=sys.stderr)
        return 4

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
