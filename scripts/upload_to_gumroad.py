#!/usr/bin/env python3
"""
AI Ready Life — Gumroad File Uploader
Uploads vault package zip files to Gumroad product listings.

Prerequisites:
  1. Run: python3 scripts/create_gumroad_listings.py   (creates listings)
  2. Run: python3 scripts/build_vault_packages.py       (builds zips)
  3. Add GUMROAD_API_KEY to ~/.ai/env/.env
  4. Run: python3 scripts/upload_to_gumroad.py

GUMROAD_API_KEY setup:
  1. Go to https://app.gumroad.com/settings/advanced
  2. Copy your Access Token
  3. Add to ~/.ai/env/.env: GUMROAD_API_KEY=your_token_here

Usage:
  python3 scripts/upload_to_gumroad.py [domain]   # upload single domain
  python3 scripts/upload_to_gumroad.py             # upload all domains
"""

import os
import sys
import json
import time
import requests
from pathlib import Path


# ── Load API key ────────────────────────────────────────────────────────────
def load_env():
    env_path = Path.home() / ".ai" / "env" / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


load_env()

API_KEY = os.environ.get("GUMROAD_API_KEY", "")
if not API_KEY:
    print("❌  GUMROAD_API_KEY not found.")
    print("   1. Go to: https://app.gumroad.com/settings/advanced")
    print("   2. Copy your Access Token")
    print("   3. Add to ~/.ai/env/.env:  GUMROAD_API_KEY=your_token_here")
    print("   4. Re-run this script")
    sys.exit(1)

API_BASE = "https://api.gumroad.com/v2"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

SCRIPTS_DIR = Path(__file__).parent
DIST_DIR = SCRIPTS_DIR / "dist"
LISTINGS_FILE = SCRIPTS_DIR / "gumroad_listings.json"

DOMAINS = [
    "health",
    "wealth",
    "tax",
    "career",
    "benefits",
    "brand",
    "business",
    "chief",
    "calendar",
    "content",
    "estate",
    "explore",
    "home",
    "insurance",
    "intel",
    "learning",
    "real-estate",
    "records",
    "social",
    "vision",
]


# ── Preflight checks ─────────────────────────────────────────────────────────
def check_prerequisites():
    errors = []

    if not LISTINGS_FILE.exists():
        errors.append(
            f"  - gumroad_listings.json not found at {LISTINGS_FILE}\n"
            "    Run: python3 scripts/create_gumroad_listings.py"
        )

    if not DIST_DIR.exists():
        errors.append(
            f"  - dist/ directory not found at {DIST_DIR}\n"
            "    Run: python3 scripts/build_vault_packages.py"
        )

    if errors:
        print("❌  Prerequisites missing:\n")
        for e in errors:
            print(e)
        sys.exit(1)


# ── Load listings index ──────────────────────────────────────────────────────
def load_listings() -> dict:
    """Load gumroad_listings.json and return domain -> product_id mapping."""
    data = json.loads(LISTINGS_FILE.read_text())
    mapping = {}
    for entry in data:
        domain = entry.get("domain", "")
        product_id = entry.get("product_id", "")
        if domain and product_id:
            mapping[domain] = {
                "product_id": product_id,
                "name": entry.get("name", domain),
            }
    return mapping


# ── Gumroad Files API helpers ────────────────────────────────────────────────
def get_existing_files(product_id: str) -> list:
    """GET /products/{id}/files — return list of file objects."""
    resp = requests.get(
        f"{API_BASE}/products/{product_id}/files",
        headers=HEADERS,
        timeout=15,
    )
    if resp.status_code != 200:
        return []
    data = resp.json()
    if not data.get("success"):
        return []
    return data.get("files", [])


def delete_file(product_id: str, file_id: str) -> bool:
    """DELETE /products/{id}/files/{file_id} — remove existing file."""
    resp = requests.delete(
        f"{API_BASE}/products/{product_id}/files/{file_id}",
        headers=HEADERS,
        timeout=15,
    )
    return resp.status_code in (200, 204)


def upload_file(product_id: str, zip_path: Path) -> dict:
    """POST /products/{id}/files — upload zip as multipart/form-data."""
    with open(zip_path, "rb") as f:
        resp = requests.post(
            f"{API_BASE}/products/{product_id}/files",
            headers=HEADERS,
            files={"file": (zip_path.name, f, "application/zip")},
            timeout=120,  # large files may take a while
        )
    if resp.status_code in (200, 201):
        return resp.json()
    return {"success": False, "message": f"HTTP {resp.status_code}: {resp.text[:200]}"}


# ── Per-domain upload ────────────────────────────────────────────────────────
def upload_domain(domain: str, product_id: str, product_name: str) -> str:
    """
    Upload the vault zip for a domain.
    Returns status: 'uploaded', 'replaced', 'skipped', or 'failed'.
    """
    zip_name = f"aireadylife-{domain}-vault.zip"
    zip_path = DIST_DIR / zip_name

    if not zip_path.exists():
        print(f"  ⚠️   {domain}: {zip_name} not found in dist/ — skipping")
        print(f"       Run: python3 scripts/build_vault_packages.py {domain}")
        return "skipped"

    # Check for existing file with same name and delete it
    existing_files = get_existing_files(product_id)
    replaced = False
    for existing in existing_files:
        if existing.get("name") == zip_name or existing.get("filename") == zip_name:
            file_id = existing.get("id", "")
            if file_id:
                ok = delete_file(product_id, file_id)
                if ok:
                    replaced = True
                else:
                    print(
                        f"  ⚠️   {domain}: could not delete existing file (id={file_id}), uploading anyway"
                    )

    # Upload
    result = upload_file(product_id, zip_path)
    size_kb = zip_path.stat().st_size / 1024

    if result.get("success"):
        action = "REPLACED" if replaced else "UPLOADED"
        print(f"  ✅  {action}  {product_name} ({size_kb:.1f} KB)")
        return "replaced" if replaced else "uploaded"
    else:
        msg = result.get("message", "unknown error")
        print(f"  ❌  FAILED   {product_name} — {msg}")
        return "failed"


# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    check_prerequisites()

    listings = load_listings()

    # Determine which domains to upload
    if len(sys.argv) > 1:
        requested = sys.argv[1:]
        invalid = [d for d in requested if d not in DOMAINS]
        if invalid:
            print(f"❌  Unknown domain(s): {', '.join(invalid)}")
            print(f"   Valid domains: {', '.join(DOMAINS)}")
            sys.exit(1)
        targets = requested
    else:
        targets = DOMAINS

    print(f"📤  Uploading {len(targets)} vault package(s) to Gumroad…\n")

    results = {"uploaded": [], "replaced": [], "skipped": [], "failed": []}

    for domain in targets:
        if domain not in listings:
            print(f"  ⚠️   {domain}: no product_id in gumroad_listings.json — skipping")
            print(f"       Run: python3 scripts/create_gumroad_listings.py")
            results["skipped"].append(domain)
            continue

        entry = listings[domain]
        product_id = entry["product_id"]
        product_name = entry["name"]

        status = upload_domain(domain, product_id, product_name)
        results[status].append(domain)

        # Rate limiting between uploads
        time.sleep(1)

    # Summary
    print(f"\n{'─' * 60}")
    print("SUMMARY")
    print("─" * 60)
    print(f"  Uploaded:  {len(results['uploaded'])}")
    print(f"  Replaced:  {len(results['replaced'])} (existing file removed first)")
    print(f"  Skipped:   {len(results['skipped'])} (no zip or no product_id)")
    print(f"  Failed:    {len(results['failed'])}")

    if results["failed"]:
        print(f"\n  Failed domains: {', '.join(results['failed'])}")
        print("  Check the error messages above for details.")

    total_ok = len(results["uploaded"]) + len(results["replaced"])
    if total_ok > 0:
        print(f"\n  {total_ok} file(s) are now live on Gumroad.")
        print("  Verify at: https://app.gumroad.com/products")


if __name__ == "__main__":
    main()
