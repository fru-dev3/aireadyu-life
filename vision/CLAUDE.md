# AI Ready Life: Vision Plugin

## Vault Location

All skills in this plugin read from and write to:

```
~/Documents/AIReadyLife/vault/vision/
```

When running any skill, always use this absolute path as the vault root. Never use relative paths.

## First Time Setup

If `~/Documents/AIReadyLife/vault/vision/` does not exist or is empty:

1. Purchase the **AI Ready Life: Vision Vault** at [frudev.gumroad.com/l/aireadylife-vision](https://frudev.gumroad.com/l/aireadylife-vision)
2. Unzip the download
3. Move the `vision/` folder to `~/Documents/AIReadyLife/vault/`
4. Open `~/Documents/AIReadyLife/vault/vision/config.md` and fill in your details
5. Return here and run any skill — it will find your vault automatically

## Vault Structure

```
~/Documents/AIReadyLife/vault/vision/
├── config.md          — your profile and settings
├── open-loops.md      — active flags and open items
├── 00_current/        — active documents and current state
├── 01_prior/          — prior period records
└── 02_briefs/         — generated briefs and reports
```

## Skills

Skills are located under `vision/skills/` — each skill has its own folder containing a `SKILL.md` file.

## First Run

Before running any skill, check `~/Documents/AIReadyLife/vault/vision/config.md`:

1. **Vault missing** → tell the user to purchase the vault template and link to the Gumroad listing above.
2. **Config filled in** → proceed with the requested skill normally.
3. **Config exists but fields are blank** (values empty after the `:`) → do NOT run the skill. Show the first-run message below instead.

### First-Run Message (show when config is blank)

> **Welcome to AI Ready Life: Vision!**
>
> Your vault is installed at `~/Documents/AIReadyLife/vault/vision/`. Before skills can run, your config and documents need to be in place.
>
> **Step 1 — Complete your config**
> Open `~/Documents/AIReadyLife/vault/vision/config.md` and fill in every field. Leave a field blank rather than guessing — the skills will flag anything that's missing.
>
> **Step 2 — Gather your documents and add them to `00_current/`**
> Here's what this domain needs:
>
- **Annual goals** — 3–5 goals for the year, written as outcomes (not tasks). Include the domain each falls under (career, health, wealth, etc.).
- **Key results or milestones** — for each goal, 2–3 measurable checkpoints that would confirm you're on track.
- **Current progress** — rough assessment of where you are on each goal right now (0–100% or a status note).
- **Life areas to focus on** — from: career, health, wealth, relationships, learning, personal growth, family. Which 2–3 matter most this quarter?
- **Prior year review (optional)** — what you accomplished last year and what carried forward. Helpful context for planning.
>
> **Step 3 — Run your first skill**
> Once config.md is filled in and at least a few documents are in `00_current/`, try: *"quarterly planning"*
>
> You don't need everything perfect to start — add what you have and the skills will tell you what's still missing.
