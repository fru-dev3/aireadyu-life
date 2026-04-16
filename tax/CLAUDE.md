# AI Ready Life: Tax Plugin

## Vault Location

All skills in this plugin read from and write to:

```
~/Documents/AIReadyLife/vault/tax/
```

When running any skill, always use this absolute path as the vault root. Never use relative paths.

## First Time Setup

If `~/Documents/AIReadyLife/vault/tax/` does not exist or is empty:

1. Purchase the **AI Ready Life: Tax Vault** at [frudev.gumroad.com/l/aireadylife-tax](https://frudev.gumroad.com/l/aireadylife-tax)
2. Unzip the download
3. Move the `tax/` folder to `~/Documents/AIReadyLife/vault/`
4. Open `~/Documents/AIReadyLife/vault/tax/config.md` and fill in your details
5. Return here and run any skill — it will find your vault automatically

## Vault Structure

```
~/Documents/AIReadyLife/vault/tax/
├── config.md          — your profile and settings
├── open-loops.md      — active flags and open items
├── 00_current/        — active documents and current state
├── 01_prior/          — prior period records
└── 02_briefs/         — generated briefs and reports
```

## Skills

Skills are located under `tax/skills/` — each skill has its own folder containing a `SKILL.md` file.

## First Run

Before running any skill, check `~/Documents/AIReadyLife/vault/tax/config.md`:

1. **Vault missing** → tell the user to purchase the vault template and link to the Gumroad listing above.
2. **Config filled in** → proceed with the requested skill normally.
3. **Config exists but fields are blank** (values empty after the `:`) → do NOT run the skill. Show the first-run message below instead.

### First-Run Message (show when config is blank)

> **Welcome to AI Ready Life: Tax!**
>
> Your vault is installed at `~/Documents/AIReadyLife/vault/tax/`. Before skills can run, your config and documents need to be in place.
>
> **Step 1 — Complete your config**
> Open `~/Documents/AIReadyLife/vault/tax/config.md` and fill in every field. Leave a field blank rather than guessing — the skills will flag anything that's missing.
>
> **Step 2 — Gather your documents and add them to `00_current/`**
> Here's what this domain needs:
>
- **Prior year tax return** — your most recent federal and state return (PDF from your tax software or accountant).
- **W-2 or 1099s** — from all income sources. Download from your employer portal, brokerage, or freelance platforms.
- **HSA contribution statement** — total contributions for the year (from your HSA custodian or W-2 Box 12 code W).
- **Charitable donation receipts** — any letter or receipt for donations over $250.
- **Business expense records** — if self-employed or a freelancer, receipts or summaries by category.
- **Mortgage interest statement (Form 1098)** — from your lender if you own a home.
- **Quarterly estimated payment receipts** — if you pay estimated taxes, your payment confirmations.
>
> **Step 3 — Run your first skill**
> Once config.md is filled in and at least a few documents are in `00_current/`, try: *"tax deadline watch"*
>
> You don't need everything perfect to start — add what you have and the skills will tell you what's still missing.
