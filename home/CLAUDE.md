# AI Ready Life: Home Plugin

## Vault Location

| OS | Vault path |
|----|------------|
| **Mac** | `~/Documents/aireadylife/vault/home/` |
| **Windows** | `%USERPROFILE%\Documents\aireadylife\vault\home\` |

Determine the user's OS from context (file paths they share, or ask if unclear). Use the correct path for their OS. Never use relative paths.

## First Time Setup

If `~/Documents/aireadylife/vault/home/` does not exist or is empty:

1. Purchase the **AI Ready Life: Home Vault** at [frudev.gumroad.com/l/aireadylife-home](https://frudev.gumroad.com/l/aireadylife-home)
2. Unzip the download
3. Move the `home/` folder to `~/Documents/aireadylife/vault/`
4. Open `~/Documents/aireadylife/vault/home/config.md` and fill in your details
5. Return here and run any skill — it will find your vault automatically

## Vault Structure

```
~/Documents/aireadylife/vault/home/
├── config.md          — your profile and settings
├── open-loops.md      — active flags and open items
├── 00_current/        — active documents and current state
├── 01_prior/          — prior period records
└── 02_briefs/         — generated briefs and reports
```

## Skills

Skills are located under `home/skills/` — each skill has its own folder containing a `SKILL.md` file.

## Vault Access

**Mac:** If a file read fails with a permission error, the AI tool needs filesystem access to your Documents folder. Tell the user:
> *Go to **System Settings → Privacy & Security → Full Disk Access**, then add the app you are running this from:*
> - *Claude Code or Codex CLI in a terminal → add **Terminal**, **iTerm**, or **Ghostty** (whichever you use), then restart it.*
> - *Claude Desktop → add **Claude**, then restart it.*

**Windows:** No permission grant needed — terminal apps and Claude Desktop run unrestricted by default.

Do not proceed with the skill until access is confirmed (Mac) or reassure the user that no action is needed (Windows).

## First Run

Before running **any skill or flow** in this domain — including flows called by other skills — read `~/Documents/aireadylife/vault/home/config.md` and check whether the key fields have been filled in (non-blank values after the `:`).

**Rules (follow exactly, no improvisation):**

1. **Vault folder is missing entirely** → output only: *"Your home vault isn't installed. Download it at [frudev.gumroad.com/l/aireadylife-home](https://frudev.gumroad.com/l/aireadylife-home), unzip, and place the `home/` folder at `~/Documents/aireadylife/vault/`."* Stop.

2. **Config fields are blank** (empty after `:`) → output the First-Run Message below verbatim. Stop. Do **not** scaffold files, offer alternatives, or ask questions.

3. **Config is filled in** → proceed with the requested skill normally.

### First-Run Message

> **Welcome to AI Ready Life: Home!**
>
> Your vault is installed at:
> - **Mac:** `~/Documents/aireadylife/vault/home/`
> - **Windows:** `%USERPROFILE%\Documents\aireadylife\vault\home\` Before skills can run, your config and documents need to be in place.
>
> **Step 1 — Complete your config**
> Open `~/Documents/aireadylife/vault/home/config.md` and fill in every field. Leave a field blank rather than guessing — the skills will flag anything that's missing.
>
> **Step 2 — Gather your documents and add them to `00_current/`**
> Here's what this domain needs:
>
- **Home details** — address, purchase price, purchase date, and estimated current value (or lease start date and monthly rent if renting).
- **Open maintenance items** — anything that needs repair, inspection, or replacement. Note the room, issue, priority, and how long it's been open.
- **Seasonal task list** — recurring tasks by season (HVAC filter, gutter cleaning, winterizing, etc.) with when they were last done.
- **Home expense records** — any major repairs, appliance purchases, or improvement costs from the current year.
- **HOA or utility contacts** — HOA management company, property insurance policy number, and utility providers.
>
> **Step 3 — Run your first skill**
> Once config.md is filled in and at least a few documents are in `00_current/`, try: *"home review"*
>
> You don't need everything perfect to start — add what you have and the skills will tell you what's still missing.
>
> **Stop here.** Do not scaffold files, do not offer options, do not ask questions. Wait for the user to complete setup and re-run the skill.

## Skill Index

Skills live in `skills/<skill-name>/SKILL.md`. To run a skill, read its `SKILL.md` and follow the instructions inside. Skills tagged **(renter-only)** auto-skip when `home_type` in config is "own"; **(owner-only)** auto-skip when `home_type` is "rent"; **(pet households)** auto-skip when `pet_count` is 0; **(HOA owners)** auto-skip when `hoa_active` is false.

**Apps (data connectors — fallback when no native MCP connector available):**
- `app-angi` — Contractor listings, ratings, license status, and cost guides on Angi via Playwright.
- `app-thumbtack` — Local pro listings and quote requests on Thumbtack via Playwright.

**Operations (user-facing routines):**
- `op-review-brief` — Home review brief. Default `mode=full` for on-demand status. `mode=weekly` runs the silent-unless-flagged Monday check (replaces deprecated op-weekly-review).
- `op-monthly-sync` — Full monthly home sync on the 1st of each month.
- `op-monthly-synthesis` — Deep monthly home synthesis: re-runs every flow, archives prior month, hands monthly home spend to wealth plugin.
- `op-seasonal-maintenance` — Quarterly seasonal maintenance planner.
- `op-expense-review` — Monthly home expense review.
- `op-meal-grocery-plan` — Weekly meal plan + grocery list aligned to nutrition goals (reads health plugin) and the week's calendar.
- `op-organize-documents` — Indexes lease, insurance, warranties, manuals, HOA docs (renter / owner categories auto-applied) into a searchable document index.
- `op-home-office-audit` — Semi-annual home-office friction audit (lighting, ergonomics, hardware, network, acoustic) feeding flagged items to the maintenance queue.
- `op-emergency-prep-review` — Semi-annual preparedness check: detectors, first aid, water / food, batteries, evacuation plan.
- `op-lease-renewal-review` — **(renter-only)** Triggered 60 days before lease end. Renew-vs-move decision brief with market-rent comparison.
- `op-pet-care-review` — **(pet households)** Monthly pet-care review: vet appointments, vaccinations, meds, supply runway.
- `op-home-improvement-project-log` — **(owner-only)** Per-project record of scope, budget, contractor, permits, payments, photos, warranty, cost-basis tag.
- `op-hoa-tracking` — **(HOA owners)** Tracks dues, special assessments, meeting calendar, and rule changes that affect the user.
- `op-move-planning` — Active-move planner (8 / 4 / 2 / 1 weeks + move-day + first-week checklists). Branches by from-type / to-type (renter / owner).

**Flows (multi-step internals called by ops):**
- `flow-build-expense-summary` — Monthly home expenses by category vs. budget.
- `flow-build-maintenance-schedule` — Complete seasonal maintenance checklist with vendor and cost columns.
- `flow-build-cleaning-routine` — Recurring cleaning cadence (daily / weekly / monthly / quarterly / annual) calibrated to household composition + pets.

**Tasks (atomic operations called by flows / ops):**
- `task-flag-maintenance-item` — Writes a maintenance flag to open-loops and creates an item record.
- `task-log-expense` — Records a home expense (utilities / repairs / supplies / services) with vendor and receipt.
- `task-update-open-loops` — Single write point for `open-loops.md`.
- `task-update-home-inventory` — Annual photo / video walkthrough; writes high-value items to insurance plugin.
- `task-track-utility-usage` — Monthly utility log with YoY usage / amount comparison and spike flags.
- `task-track-mortgage` — **(owner-only)** Monthly mortgage payment log; refi opportunity + PMI removal flags.
- `task-track-property-tax` — **(owner-only)** Property-tax assessment log + payment schedule + appeal-window awareness.
