#!/usr/bin/env python3
"""
Scrape HPE Morpheus documentation from support.hpe.com API.

Usage:
    python3 scrape_hpe_docs.py essentials   # Scrapes VM Essentials (sd00007735en_us)
    python3 scrape_hpe_docs.py enterprise   # Scrapes Enterprise (sd00007732en_us)
    python3 scrape_hpe_docs.py both         # Scrapes both

Output is saved to _scraped/<docId>/ as HTML files with a manifest.json index.
"""

import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path
from html.parser import HTMLParser

DOCS = {
    "essentials": "sd00007735en_us",
    "enterprise": "sd00007732en_us",
}

BASE_API = "https://support.hpe.com/hpesc/public/api/document"
OUTPUT_DIR = Path("_scraped")
DELAY = 0.3  # seconds between requests to be polite


def fetch(url):
    """Fetch URL content as string."""
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8")
    except Exception as e:
        print(f"  ERROR fetching {url}: {e}")
        return None


def get_toc(doc_id):
    """Get table of contents for a document."""
    url = f"{BASE_API}/{doc_id}/toc"
    content = fetch(url)
    if content:
        return json.loads(content)
    return []


def flatten_toc(items, depth=0, parent_path=""):
    """Flatten TOC tree into a list of (topic_name, url, depth, path) tuples."""
    results = []
    for item in items:
        name = item.get("topicName", "Unknown")
        link = item.get("topicLink", "")
        path = f"{parent_path}/{slugify(name)}" if parent_path else slugify(name)
        results.append({
            "name": name,
            "url": link,
            "depth": depth,
            "path": path,
        })
        children = item.get("children")
        if children:
            results.extend(flatten_toc(children, depth + 1, path))
    return results


def slugify(text):
    """Convert text to a filesystem-safe slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text[:80]


def scrape_doc(doc_id, label):
    """Scrape all pages for a document."""
    print(f"\n{'='*60}")
    print(f"Scraping: {label} ({doc_id})")
    print(f"{'='*60}")

    out_dir = OUTPUT_DIR / doc_id
    out_dir.mkdir(parents=True, exist_ok=True)

    # Get TOC
    print("Fetching TOC...")
    toc = get_toc(doc_id)
    if not toc:
        print("ERROR: Could not fetch TOC")
        return

    # Save raw TOC
    with open(out_dir / "toc.json", "w") as f:
        json.dump(toc, f, indent=2)

    # Flatten
    pages = flatten_toc(toc)
    print(f"Found {len(pages)} pages")

    # Scrape each page
    manifest = []
    for i, page in enumerate(pages):
        if not page["url"]:
            manifest.append({**page, "file": None, "status": "no_url"})
            continue

        filename = f"{i:04d}_{page['path'].replace('/', '_')[:100]}.html"
        filepath = out_dir / filename

        # Skip if already scraped
        if filepath.exists():
            print(f"  [{i+1}/{len(pages)}] SKIP (cached): {page['name']}")
            manifest.append({**page, "file": filename, "status": "cached"})
            continue

        print(f"  [{i+1}/{len(pages)}] Fetching: {page['name']}")
        content = fetch(page["url"])

        if content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            manifest.append({**page, "file": filename, "status": "ok"})
        else:
            manifest.append({**page, "file": None, "status": "error"})

        time.sleep(DELAY)

    # Save manifest
    with open(out_dir / "manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)

    ok_count = sum(1 for m in manifest if m["status"] in ("ok", "cached"))
    err_count = sum(1 for m in manifest if m["status"] == "error")
    print(f"\nDone: {ok_count} pages scraped, {err_count} errors")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    target = sys.argv[1].lower()

    if target == "both":
        for label, doc_id in DOCS.items():
            scrape_doc(doc_id, label)
    elif target in DOCS:
        scrape_doc(DOCS[target], target)
    else:
        print(f"Unknown target: {target}")
        print(f"Valid options: {', '.join(DOCS.keys())}, both")
        sys.exit(1)


if __name__ == "__main__":
    main()
