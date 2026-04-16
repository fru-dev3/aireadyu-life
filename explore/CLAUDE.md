# AI Ready Life: Explore Plugin

## Vault Location

All skills in this plugin read from and write to:

```
~/Documents/AIReadyLife/vault/explore/
```

When running any skill, always use this absolute path as the vault root. Never use relative paths.

## First Time Setup

If `~/Documents/AIReadyLife/vault/explore/` does not exist or is empty:

1. Purchase the **AI Ready Life: Explore Vault** at [frudev.gumroad.com/l/aireadylife-explore](https://frudev.gumroad.com/l/aireadylife-explore)
2. Unzip the download
3. Move the `explore/` folder to `~/Documents/AIReadyLife/vault/`
4. Open `~/Documents/AIReadyLife/vault/explore/config.md` and fill in your details
5. Return here and run any skill — it will find your vault automatically

## Vault Structure

```
~/Documents/AIReadyLife/vault/explore/
├── config.md          — your profile and settings
├── open-loops.md      — active flags and open items
├── 00_current/        — active documents and current state
├── 01_prior/          — prior period records
└── 02_briefs/         — generated briefs and reports
```

## Skills

Skills are located under `explore/skills/` — each skill has its own folder containing a `SKILL.md` file.

## First Run

Before running any skill, check `~/Documents/AIReadyLife/vault/explore/config.md`:

1. **Vault missing** → tell the user to purchase the vault template and link to the Gumroad listing above.
2. **Config filled in** → proceed with the requested skill normally.
3. **Config exists but fields are blank** (values empty after the `:`) → do NOT run the skill. Show the first-run message below instead.

### First-Run Message (show when config is blank)

> **Welcome to AI Ready Life: Explore!**
>
> Your vault is installed at `~/Documents/AIReadyLife/vault/explore/`. Before skills can run, your config and documents need to be in place.
>
> **Step 1 — Complete your config**
> Open `~/Documents/AIReadyLife/vault/explore/config.md` and fill in every field. Leave a field blank rather than guessing — the skills will flag anything that's missing.
>
> **Step 2 — Gather your documents and add them to `00_current/`**
> Here's what this domain needs:
>
- **Passport info** — full name as printed, passport number, issue date, and expiration date.
- **Visa info** — any current visas (country, visa type, expiration date). Include ESTA or eTA if applicable.
- **Upcoming trip bookings** — destination, travel dates, flight confirmation numbers, hotel reservations.
- **Loyalty program numbers** — airline frequent flyer numbers and hotel loyalty membership IDs.
- **Travel documents expiring within 12 months** — flag now so you have time to renew.
>
> **Step 3 — Run your first skill**
> Once config.md is filled in and at least a few documents are in `00_current/`, try: *"travel brief"*
>
> You don't need everything perfect to start — add what you have and the skills will tell you what's still missing.
