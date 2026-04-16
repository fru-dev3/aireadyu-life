# AI Ready Life: Brand Plugin

## Vault Location

All skills in this plugin read from and write to:

```
~/Documents/AIReadyLife/vault/brand/
```

When running any skill, always use this absolute path as the vault root. Never use relative paths.

## First Time Setup

If `~/Documents/AIReadyLife/vault/brand/` does not exist or is empty:

1. Purchase the **AI Ready Life: Brand Vault** at [frudev.gumroad.com/l/aireadylife-brand](https://frudev.gumroad.com/l/aireadylife-brand)
2. Unzip the download
3. Move the `brand/` folder to `~/Documents/AIReadyLife/vault/`
4. Open `~/Documents/AIReadyLife/vault/brand/config.md` and fill in your details
5. Return here and run any skill — it will find your vault automatically

## Vault Structure

```
~/Documents/AIReadyLife/vault/brand/
├── config.md          — your profile and settings
├── open-loops.md      — active flags and open items
├── 00_current/        — active documents and current state
├── 01_prior/          — prior period records
└── 02_briefs/         — generated briefs and reports
```

## Skills

Skills are located under `brand/skills/` — each skill has its own folder containing a `SKILL.md` file.

## First Run

Before running any skill, check `~/Documents/AIReadyLife/vault/brand/config.md`:

1. **Vault missing** → tell the user to purchase the vault template and link to the Gumroad listing above.
2. **Config filled in** → proceed with the requested skill normally.
3. **Config exists but fields are blank** (values empty after the `:`) → do NOT run the skill. Show the first-run message below instead.

### First-Run Message (show when config is blank)

> **Welcome to AI Ready Life: Brand!**
>
> Your vault is installed at `~/Documents/AIReadyLife/vault/brand/`. Before skills can run, your config and documents need to be in place.
>
> **Step 1 — Complete your config**
> Open `~/Documents/AIReadyLife/vault/brand/config.md` and fill in every field. Leave a field blank rather than guessing — the skills will flag anything that's missing.
>
> **Step 2 — Gather your documents and add them to `00_current/`**
> Here's what this domain needs:
>
- **Platform handles** — your username on LinkedIn, Twitter/X, Instagram, TikTok, YouTube, or wherever you publish. Include the full URL.
- **Follower counts** — current counts per platform. A screenshot or manual note is fine.
- **Recent analytics export (optional)** — LinkedIn Creator Analytics, Twitter Analytics, or YouTube Studio CSV for the past 90 days.
- **Bio copy** — your current bio as it appears on your primary platform. Used for consistency audits.
- **Content cadence goal** — how often you intend to publish per platform (e.g., LinkedIn: 3x/week, newsletter: 2x/month).
>
> **Step 3 — Run your first skill**
> Once config.md is filled in and at least a few documents are in `00_current/`, try: *"brand brief"*
>
> You don't need everything perfect to start — add what you have and the skills will tell you what's still missing.
