#!/usr/bin/env python3
"""
AI Ready Life — Gumroad Listing Creator
Creates all 20 plugin listings + 2 bundle listings on Gumroad.

Usage:
  python3 scripts/create_gumroad_listings.py

Requirements:
  GUMROAD_API_KEY must be set in ~/.ai/env/.env
  (Get it: https://app.gumroad.com/settings/advanced → Access Token)
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

# ── Product definitions ──────────────────────────────────────────────────────
PLUGINS = [
    # (slug, name, price_cents, tagline, skills_count, tier)
    # $29 plugins
    (
        "aireadylife-ben",
        "AI Ready Life: Ben",
        2900,
        "Chief of Staff — daily briefs across all life domains",
        4,
        "core",
    ),
    (
        "aireadylife-benefits",
        "AI Ready Life: Benefits",
        2900,
        "401k, HSA, coverage, and employer benefits management",
        10,
        "core",
    ),
    (
        "aireadylife-brand",
        "AI Ready Life: Brand",
        2900,
        "Personal brand analytics, mentions, and profile consistency",
        8,
        "core",
    ),
    (
        "aireadylife-business",
        "AI Ready Life: Business",
        2900,
        "LLC/entity revenue, expenses, compliance, and P&L",
        10,
        "core",
    ),
    (
        "aireadylife-calendar",
        "AI Ready Life: Calendar",
        2900,
        "Deadline tracking, focus time, and cross-domain scheduling",
        8,
        "core",
    ),
    (
        "aireadylife-career",
        "AI Ready Life: Career",
        2900,
        "Comp benchmarking, job market, pipeline, and skills gaps",
        10,
        "core",
    ),
    (
        "aireadylife-content",
        "AI Ready Life: Content",
        2900,
        "YouTube, newsletter, Gumroad revenue, and SEO in one view",
        10,
        "core",
    ),
    (
        "aireadylife-estate",
        "AI Ready Life: Estate",
        2900,
        "Rental portfolio — cash flow, maintenance, and tenants",
        13,
        "core",
    ),
    (
        "aireadylife-health",
        "AI Ready Life: Health",
        2900,
        "Labs, wellness, medications, appointments, and HSA",
        11,
        "core",
    ),
    (
        "aireadylife-insurance",
        "AI Ready Life: Insurance",
        2900,
        "All policies, renewals, coverage gaps, and claims",
        9,
        "core",
    ),
    (
        "aireadylife-tax",
        "AI Ready Life: Tax",
        2900,
        "Deadlines, estimates, deductions, entity compliance, filing",
        10,
        "core",
    ),
    (
        "aireadylife-vision",
        "AI Ready Life: Vision",
        2900,
        "Life scorecard, quarterly OKRs, and goal alignment",
        8,
        "core",
    ),
    (
        "aireadylife-wealth",
        "AI Ready Life: Wealth",
        2900,
        "Net worth, investments, cash flow, and estate planning",
        21,
        "core",
    ),
    # $19 plugins
    (
        "aireadylife-explore",
        "AI Ready Life: Explore",
        1900,
        "Trips, passport status, and travel wishlist",
        2,
        "lite",
    ),
    (
        "aireadylife-home",
        "AI Ready Life: Home",
        1900,
        "Home maintenance, expenses, and seasonal tasks",
        3,
        "lite",
    ),
    (
        "aireadylife-intel",
        "AI Ready Life: Intel",
        1900,
        "Daily news briefing filtered to your interests",
        3,
        "lite",
    ),
    (
        "aireadylife-learning",
        "AI Ready Life: Learning",
        1900,
        "Courses, certifications, reading list, and learning goals",
        3,
        "lite",
    ),
    (
        "aireadylife-real-estate",
        "AI Ready Life: Real Estate",
        1900,
        "Market analysis, buy vs. rent, and portfolio strategy",
        3,
        "lite",
    ),
    (
        "aireadylife-records",
        "AI Ready Life: Records",
        1900,
        "Document inventory, expiring IDs, and subscription tracker",
        2,
        "lite",
    ),
    (
        "aireadylife-social",
        "AI Ready Life: Social",
        1900,
        "Birthdays, relationship health, and outreach queue",
        3,
        "lite",
    ),
]

BUNDLES = [
    {
        "slug": "aireadylife-bundle",
        "name": "AI Ready Life: Complete Bundle",
        "price": 19900,  # $199
        "desc": "All 20 AI Ready Life plugins — every domain of your life in one package.",
    },
    {
        "slug": "aireadylife-core-bundle",
        "name": "AI Ready Life: Core Bundle",
        "price": 7900,  # $79
        "desc": "The 4 essential AI Ready Life plugins: Health, Wealth, Tax, and Career.",
    },
]


# ── Description builder ─────────────────────────────────────────────────────
def build_description(slug, name, tagline, skills_count, price_cents):
    domain = slug.replace("aireadylife-", "")
    price = price_cents / 100

    return f"""<p><strong>{tagline}</strong></p>

<p>AI Ready Life: {domain.title()} is a self-contained AI agent plugin with {skills_count} skills, a pre-built vault schema, and a Node.js MCP server for direct Claude.ai integration.</p>

<h3>What's free (GitHub)</h3>
<ul>
  <li>Agent shells with capabilities defined</li>
  <li>Skill definitions ({skills_count} skills using <code>arlive-</code> prefix)</li>
  <li>Vault schema (domain-organized folder structure)</li>
  <li>Demo vault — synthetic "Alex Rivera" data so you can explore before connecting your own</li>
</ul>

<h3>What you get with this pack (${price:.0f})</h3>
<ul>
  <li>Full agent instructions (100+ lines of domain expertise)</li>
  <li>Onboarding guide for connecting your data sources</li>
  <li>50+ prompts covering every scenario in this domain</li>
  <li>Configuration templates for all supported apps and portals</li>
</ul>

<h3>Install (Paperclip)</h3>
<pre><code>npx companies.sh add fru-dev3/aireadyu-life/{domain} --include plugin,agents,skills</code></pre>

<h3>Install (Claude.ai — MCP)</h3>
<p>Settings → Integrations → Add MCP Server:</p>
<pre><code>npx -y @aireadylife/{domain}-plugin</code></pre>
<p>Demo mode: <code>VAULT_MODE=demo npx -y @aireadylife/{domain}-plugin</code></p>

<h3>Part of AI Ready Life</h3>
<p>AI Ready Life packages your most important life domains as installable AI agent plugins. Install one. Add more as your system grows.</p>
<p>
  <a href="https://aireadyu.dev">aireadyu.dev</a> ·
  <a href="https://youtube.com/@frudev">youtube.com/@frudev</a> ·
  Built by <a href="https://fru.dev">fru.dev</a>
</p>"""


def build_bundle_description(bundle):
    return f"""<p><strong>{bundle['desc']}</strong></p>

<h3>What's included</h3>
{'<p>All 20 plugins: Ben (Chief of Staff), Benefits, Brand, Business, Calendar, Career, Content, Estate, Explore, Health, Home, Insurance, Intel, Learning, Real Estate, Records, Social, Tax, Vision, Wealth.</p>' if 'Complete' in bundle['name'] else '<p>Health, Wealth, Tax, and Career — the 4 most impactful life domains to start with.</p>'}

<h3>What you get</h3>
<ul>
  <li>Full agent instructions for every included plugin</li>
  <li>Onboarding guides for all data sources</li>
  <li>300+ prompts (Complete) or 150+ prompts (Core)</li>
  <li>Configuration templates for all supported apps</li>
</ul>

<h3>Part of AI Ready Life</h3>
<p>
  <a href="https://aireadyu.dev">aireadyu.dev</a> ·
  <a href="https://youtube.com/@frudev">youtube.com/@frudev</a> ·
  Built by <a href="https://fru.dev">fru.dev</a>
</p>"""


# ── API helpers ──────────────────────────────────────────────────────────────
def create_product(name, description, price_cents, custom_url):
    resp = requests.post(
        f"{API_BASE}/products",
        headers=HEADERS,
        data={
            "name": name,
            "description": description,
            "price": price_cents,
            "url": custom_url,
            "published": "false",  # draft — review before publishing
        },
        timeout=15,
    )
    return resp.json()


def list_existing():
    resp = requests.get(f"{API_BASE}/products", headers=HEADERS, timeout=15)
    data = resp.json()
    if not data.get("success"):
        return {}
    return {
        p["custom_permalink"]: p
        for p in data.get("products", [])
        if p.get("custom_permalink")
    }


# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    print("🔍  Fetching existing Gumroad products…")
    existing = list_existing()
    print(f"    Found {len(existing)} existing products.\n")

    results = []

    # Create plugin listings
    print("📦  Creating plugin listings…")
    for slug, name, price, tagline, skills, tier in PLUGINS:
        domain = slug.replace("aireadylife-", "")
        if slug in existing:
            print(f"    ⏭  SKIP  {name} (already exists)")
            results.append(
                {
                    "name": name,
                    "slug": slug,
                    "status": "existing",
                    "url": f"https://fruverse.gumroad.com/l/{slug}",
                }
            )
            continue

        desc = build_description(slug, name, tagline, skills, price)
        data = create_product(name, desc, price, slug)

        if data.get("success"):
            product = data["product"]
            url = f"https://fruverse.gumroad.com/l/{slug}"
            print(f"    ✅  CREATED  {name}  →  {url}")
            results.append(
                {
                    "name": name,
                    "slug": slug,
                    "status": "created",
                    "price": f"${price/100:.0f}",
                    "url": url,
                }
            )
        else:
            print(f"    ❌  FAILED   {name}  —  {data.get('message', 'unknown error')}")
            results.append(
                {
                    "name": name,
                    "slug": slug,
                    "status": "failed",
                    "error": data.get("message"),
                }
            )
        time.sleep(0.5)  # gentle rate limiting

    # Create bundle listings
    print("\n🎁  Creating bundle listings…")
    for bundle in BUNDLES:
        if bundle["slug"] in existing:
            print(f"    ⏭  SKIP  {bundle['name']} (already exists)")
            results.append(
                {
                    "name": bundle["name"],
                    "slug": bundle["slug"],
                    "status": "existing",
                    "url": f"https://fruverse.gumroad.com/l/{bundle['slug']}",
                }
            )
            continue

        desc = build_bundle_description(bundle)
        data = create_product(bundle["name"], desc, bundle["price"], bundle["slug"])

        if data.get("success"):
            url = f"https://fruverse.gumroad.com/l/{bundle['slug']}"
            print(f"    ✅  CREATED  {bundle['name']}  →  {url}")
            results.append(
                {
                    "name": bundle["name"],
                    "slug": bundle["slug"],
                    "status": "created",
                    "price": f"${bundle['price']/100:.0f}",
                    "url": url,
                }
            )
        else:
            print(
                f"    ❌  FAILED   {bundle['name']}  —  {data.get('message', 'unknown error')}"
            )
        time.sleep(0.5)

    # Summary
    print("\n" + "─" * 60)
    print("SUMMARY")
    print("─" * 60)
    created = [r for r in results if r["status"] == "created"]
    skipped = [r for r in results if r["status"] == "existing"]
    failed = [r for r in results if r["status"] == "failed"]
    print(f"  Created:  {len(created)}")
    print(f"  Skipped:  {len(skipped)} (already existed)")
    print(f"  Failed:   {len(failed)}")

    if created:
        print("\n  New listings (drafts — go publish in Gumroad dashboard):")
        for r in created:
            print(f"    {r['price']:>6}  {r['url']}")

    if failed:
        print("\n  Failed:")
        for r in failed:
            print(f"    {r['name']} — {r.get('error', '?')}")

    # Save results
    out = Path(__file__).parent / "gumroad_listings.json"
    out.write_text(json.dumps(results, indent=2))
    print(f"\n  Full results saved to: scripts/gumroad_listings.json")
    print("\n⚠️   All listings created as DRAFTS.")
    print("    Review at https://app.gumroad.com/products then publish each one.")


if __name__ == "__main__":
    main()
