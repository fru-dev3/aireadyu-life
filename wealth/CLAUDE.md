# AI Ready Life: Wealth Plugin

## Vault Location

All skills in this plugin read from and write to:

```
~/Documents/AIReadyLife/vault/wealth/
```

When running any skill, always use this absolute path as the vault root. Never use relative paths.

## First Time Setup

If `~/Documents/AIReadyLife/vault/wealth/` does not exist or is empty:

1. Purchase the **AI Ready Life: Wealth Vault** at [frudev.gumroad.com/l/aireadylife-wealth](https://frudev.gumroad.com/l/aireadylife-wealth)
2. Unzip the download
3. Move the `wealth/` folder to `~/Documents/AIReadyLife/vault/`
4. Open `~/Documents/AIReadyLife/vault/wealth/config.md` and fill in your details
5. Return here and run any skill — it will find your vault automatically

## Vault Structure

```
~/Documents/AIReadyLife/vault/wealth/
├── config.md          — your profile and settings
├── open-loops.md      — active flags and open items
├── 00_current/        — active documents and current state
├── 01_prior/          — prior period records
└── 02_briefs/         — generated briefs and reports
```

## Skills

Skills are located under `wealth/skills/` — each skill has its own folder containing a `SKILL.md` file.

## First Run

Before running any skill, check `~/Documents/AIReadyLife/vault/wealth/config.md`:

1. **Vault missing** → tell the user to purchase the vault template and link to the Gumroad listing above.
2. **Config filled in** → proceed with the requested skill normally.
3. **Config exists but fields are blank** (values empty after the `:`) → do NOT run the skill. Show the first-run message below instead.

### First-Run Message (show when config is blank)

> **Welcome to AI Ready Life: Wealth!**
>
> Your vault is installed at `~/Documents/AIReadyLife/vault/wealth/`. Before skills can run, your config and documents need to be in place.
>
> **Step 1 — Complete your config**
> Open `~/Documents/AIReadyLife/vault/wealth/config.md` and fill in every field. Leave a field blank rather than guessing — the skills will flag anything that's missing.
>
> **Step 2 — Gather your documents and add them to `00_current/`**
> Here's what this domain needs:
>
- **Bank statements** — checking, savings, and high-yield savings accounts. Most recent month. Institution name, account last 4, and current balance.
- **Investment statements** — 401k, Roth IRA, Traditional IRA, brokerage. Most recent. Balance and account type for each.
- **Debt statements** — mortgage, auto loan, student loans, and any credit cards you track. Outstanding balance and interest rate for each.
- **Pay stub** — most recent, to confirm gross income, net pay, and any benefit deductions.
- **Real estate info** — estimated market value and outstanding mortgage balance for any property you own.
>
> **Step 3 — Run your first skill**
> Once config.md is filled in and at least a few documents are in `00_current/`, try: *"net worth review"*
>
> You don't need everything perfect to start — add what you have and the skills will tell you what's still missing.
