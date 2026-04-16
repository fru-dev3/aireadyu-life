# AI Ready Life: Chief Plugin

## Vault Location

All skills in this plugin read from and write to:

```
~/Documents/AIReadyLife/vault/chief/
```

When running any skill, always use this absolute path as the vault root. Never use relative paths.

## First Time Setup

If `~/Documents/AIReadyLife/vault/chief/` does not exist or is empty:

1. Purchase the **AI Ready Life: Chief Vault** at [frudev.gumroad.com/l/aireadylife-chief](https://frudev.gumroad.com/l/aireadylife-chief)
2. Unzip the download
3. Move the `chief/` folder to `~/Documents/AIReadyLife/vault/`
4. Open `~/Documents/AIReadyLife/vault/chief/config.md` and fill in your details
5. Return here and run any skill — it will find your vault automatically

## Vault Structure

```
~/Documents/AIReadyLife/vault/chief/
├── config.md          — your profile and settings
├── open-loops.md      — active flags and open items
├── 00_current/        — active documents and current state
├── 01_prior/          — prior period records
└── 02_briefs/         — generated briefs and reports
```

## Skills

Skills are located under `chief/skills/` — each skill has its own folder containing a `SKILL.md` file.

## First Run

Before running any skill, check `~/Documents/AIReadyLife/vault/chief/config.md`:

1. **Vault missing** → tell the user to purchase the vault template and link to the Gumroad listing above.
2. **Config filled in** → proceed with the requested skill normally.
3. **Config exists but fields are blank** (values empty after the `:`) → do NOT run the skill. Show the first-run message below instead.

### First-Run Message (show when config is blank)

> **Welcome to AI Ready Life: Chief!**
>
> Your vault is installed at `~/Documents/AIReadyLife/vault/chief/`. Before skills can run, your config and documents need to be in place.
>
> **Step 1 — Complete your config**
> Open `~/Documents/AIReadyLife/vault/chief/config.md` and fill in every field. Leave a field blank rather than guessing — the skills will flag anything that's missing.
>
> **Step 2 — Gather your documents and add them to `00_current/`**
> Here's what this domain needs:
>
- **Other domain vaults** — Chief reads across all your installed domains. Set up at least one other domain vault first (health, wealth, or career are good starting points).
- **Priority domains** — note which domains are active so Chief knows where to look for open loops and alerts.
- **Brief schedule preference** — when you want to run your daily brief (morning, evening) and what format you prefer (bullet list vs. narrative).
>
> **Step 3 — Run your first skill**
> Once config.md is filled in and at least a few documents are in `00_current/`, try: *"daily brief"*
>
> You don't need everything perfect to start — add what you have and the skills will tell you what's still missing.
