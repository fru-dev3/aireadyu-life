# AI Ready Life: Learning Plugin

## Vault Location

All skills in this plugin read from and write to:

```
~/Documents/AIReadyLife/vault/learning/
```

When running any skill, always use this absolute path as the vault root. Never use relative paths.

## First Time Setup

If `~/Documents/AIReadyLife/vault/learning/` does not exist or is empty:

1. Purchase the **AI Ready Life: Learning Vault** at [frudev.gumroad.com/l/aireadylife-learning](https://frudev.gumroad.com/l/aireadylife-learning)
2. Unzip the download
3. Move the `learning/` folder to `~/Documents/AIReadyLife/vault/`
4. Open `~/Documents/AIReadyLife/vault/learning/config.md` and fill in your details
5. Return here and run any skill — it will find your vault automatically

## Vault Structure

```
~/Documents/AIReadyLife/vault/learning/
├── config.md          — your profile and settings
├── open-loops.md      — active flags and open items
├── 00_current/        — active documents and current state
├── 01_prior/          — prior period records
└── 02_briefs/         — generated briefs and reports
```

## Skills

Skills are located under `learning/skills/` — each skill has its own folder containing a `SKILL.md` file.

## First Run

Before running any skill, check `~/Documents/AIReadyLife/vault/learning/config.md`:

1. **Vault missing** → tell the user to purchase the vault template and link to the Gumroad listing above.
2. **Config filled in** → proceed with the requested skill normally.
3. **Config exists but fields are blank** (values empty after the `:`) → do NOT run the skill. Show the first-run message below instead.

### First-Run Message (show when config is blank)

> **Welcome to AI Ready Life: Learning!**
>
> Your vault is installed at `~/Documents/AIReadyLife/vault/learning/`. Before skills can run, your config and documents need to be in place.
>
> **Step 1 — Complete your config**
> Open `~/Documents/AIReadyLife/vault/learning/config.md` and fill in every field. Leave a field blank rather than guessing — the skills will flag anything that's missing.
>
> **Step 2 — Gather your documents and add them to `00_current/`**
> Here's what this domain needs:
>
- **Active courses** — platform (Coursera, Udemy, etc.), course name, enrollment date, and current completion percentage.
- **Books in progress** — title, author, format (physical/Kindle/audio), and current progress (chapter or percentage).
- **Recently completed** — courses or books finished in the past 90 days with key takeaways.
- **Learning goals** — skills you want to develop this year, with target milestones and deadlines.
- **Certifications in progress (optional)** — certification name, exam date, and study schedule.
>
> **Step 3 — Run your first skill**
> Once config.md is filled in and at least a few documents are in `00_current/`, try: *"learning review"*
>
> You don't need everything perfect to start — add what you have and the skills will tell you what's still missing.
