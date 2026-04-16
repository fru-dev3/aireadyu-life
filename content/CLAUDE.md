# AI Ready Life: Content Plugin

## Vault Location

All skills in this plugin read from and write to:

```
~/Documents/AIReadyLife/vault/content/
```

When running any skill, always use this absolute path as the vault root. Never use relative paths.

## First Time Setup

If `~/Documents/AIReadyLife/vault/content/` does not exist or is empty:

1. Purchase the **AI Ready Life: Content Vault** at [frudev.gumroad.com/l/aireadylife-content](https://frudev.gumroad.com/l/aireadylife-content)
2. Unzip the download
3. Move the `content/` folder to `~/Documents/AIReadyLife/vault/`
4. Open `~/Documents/AIReadyLife/vault/content/config.md` and fill in your details
5. Return here and run any skill — it will find your vault automatically

## Vault Structure

```
~/Documents/AIReadyLife/vault/content/
├── config.md          — your profile and settings
├── open-loops.md      — active flags and open items
├── 00_current/        — active documents and current state
├── 01_prior/          — prior period records
└── 02_briefs/         — generated briefs and reports
```

## Skills

Skills are located under `content/skills/` — each skill has its own folder containing a `SKILL.md` file.

## First Run

Before running any skill, check `~/Documents/AIReadyLife/vault/content/config.md`:

1. **Vault missing** → tell the user to purchase the vault template and link to the Gumroad listing above.
2. **Config filled in** → proceed with the requested skill normally.
3. **Config exists but fields are blank** (values empty after the `:`) → do NOT run the skill. Show the first-run message below instead.

### First-Run Message (show when config is blank)

> **Welcome to AI Ready Life: Content!**
>
> Your vault is installed at `~/Documents/AIReadyLife/vault/content/`. Before skills can run, your config and documents need to be in place.
>
> **Step 1 — Complete your config**
> Open `~/Documents/AIReadyLife/vault/content/config.md` and fill in every field. Leave a field blank rather than guessing — the skills will flag anything that's missing.
>
> **Step 2 — Gather your documents and add them to `00_current/`**
> Here's what this domain needs:
>
- **Channel or publication list** — for each platform: name, URL, current subscriber/follower count, and publishing cadence target.
- **Revenue breakdown** — earnings by source (AdSense, sponsorships, affiliate, digital products, newsletter) for the current year.
- **Analytics export** — YouTube Studio CSV, Beehiiv analytics, or Google Analytics for the past 90 days.
- **Content pipeline** — list of posts, videos, or articles in progress, scheduled, or recently published.
- **SEO targets (optional)** — keyword targets or topics you're trying to rank for.
>
> **Step 3 — Run your first skill**
> Once config.md is filled in and at least a few documents are in `00_current/`, try: *"content brief"*
>
> You don't need everything perfect to start — add what you have and the skills will tell you what's still missing.
