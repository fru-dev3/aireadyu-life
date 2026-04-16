# AI Ready Life: Health Plugin

## Vault Location

All skills in this plugin read from and write to:

```
~/Documents/AIReadyLife/vault/health/
```

When running any skill, always use this absolute path as the vault root. Never use relative paths.

## First Time Setup

If `~/Documents/AIReadyLife/vault/health/` does not exist or is empty:

1. Purchase the **AI Ready Life: Health Vault** at [frudev.gumroad.com/l/aireadylife-health](https://frudev.gumroad.com/l/aireadylife-health)
2. Unzip the download
3. Move the `health/` folder to `~/Documents/AIReadyLife/vault/`
4. Open `~/Documents/AIReadyLife/vault/health/config.md` and fill in your details
5. Return here and run any skill — it will find your vault automatically

## Vault Structure

```
~/Documents/AIReadyLife/vault/health/
├── config.md          — your profile and settings
├── open-loops.md      — active flags and open items
├── 00_current/        — active documents and current state
├── 01_prior/          — prior period records
└── 02_briefs/         — generated briefs and reports
```

## Skills

Skills are located under `health/skills/` — each skill has its own folder containing a `SKILL.md` file.

## First Run

Before running any skill, check `~/Documents/AIReadyLife/vault/health/config.md`:

1. **Vault missing** → tell the user to purchase the vault template and link to the Gumroad listing above.
2. **Config filled in** → proceed with the requested skill normally.
3. **Config exists but fields are blank** (values empty after the `:`) → do NOT run the skill. Show the first-run message below instead.

### First-Run Message (show when config is blank)

> **Welcome to AI Ready Life: Health!**
>
> Your vault is installed at `~/Documents/AIReadyLife/vault/health/`. Before skills can run, your config and documents need to be in place.
>
> **Step 1 — Complete your config**
> Open `~/Documents/AIReadyLife/vault/health/config.md` and fill in every field. Leave a field blank rather than guessing — the skills will flag anything that's missing.
>
> **Step 2 — Gather your documents and add them to `00_current/`**
> Here's what this domain needs:
>
- **Lab results** — PDF or text export from MyChart, Quest Diagnostics, LabCorp, or your doctor's portal. Save to `00_current/`.
- **Medication list** — for each prescription: name, dosage, frequency, refill due date, prescribing provider. A text file is fine.
- **Preventive care history** — dates of last physical, dental cleaning, eye exam, and any screenings (mammogram, colonoscopy, etc.).
- **Insurance card** — plan name, member ID, group number, individual deductible, OOP max, primary care copay.
- **Provider contacts** — primary care doctor name, phone, and portal URL. Same for any specialists you see regularly.
- **Wearable data (optional)** — Apple Health export, Oura CSV, or Garmin summary if you track sleep, HRV, or activity.
>
> **Step 3 — Run your first skill**
> Once config.md is filled in and at least a few documents are in `00_current/`, try: *"health brief"*
>
> You don't need everything perfect to start — add what you have and the skills will tell you what's still missing.
