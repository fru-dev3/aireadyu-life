<!-- Codex / non-Claude agents: this file mirrors CLAUDE.md so any AGENTS.md-aware agent (Codex CLI, etc.) reads the same instructions. Both files stay in sync. -->

# AI Ready Life: Health Plugin

## Vault Location

| OS | Vault path |
|----|------------|
| **Mac** | `~/Documents/aireadylife/vault/health/` |
| **Windows** | `%USERPROFILE%\Documents\aireadylife\vault\health\` |

Determine the user's OS from context (file paths they share, or ask if unclear). Use the correct path for their OS. Never use relative paths.

## First Time Setup

If `~/Documents/aireadylife/vault/health/` does not exist or is empty:

1. Purchase the **AI Ready Life: Health Vault** at [frudev.gumroad.com/l/aireadylife-health](https://frudev.gumroad.com/l/aireadylife-health)
2. Unzip the download
3. Move the `health/` folder to `~/Documents/aireadylife/vault/`
4. Open `~/Documents/aireadylife/vault/health/config.md` and fill in your details
5. Return here and run any skill — it will find your vault automatically

## Vault Structure

```
~/Documents/aireadylife/vault/health/
├── config.md          — your profile and settings
├── open-loops.md      — active flags and open items
├── 00_current/        — active documents and current state
├── 01_prior/          — prior period records
└── 02_briefs/         — generated briefs and reports
```

## Skills

Skills are located under `health/skills/` — each skill has its own folder containing a `SKILL.md` file.

## Vault Access

**Mac:** If a file read fails with a permission error, Claude Desktop needs filesystem access. Tell the user:
> *Go to **System Settings → Privacy & Security → Full Disk Access**, add **Claude**, then restart Claude Desktop.*

**Windows:** Claude Desktop runs unrestricted — no permission grant needed.

Do not proceed with the skill until access is confirmed (Mac) or reassure the user that no action is needed (Windows).

## First Run

Before running **any skill or flow** in this domain — including flows called by other skills — read `~/Documents/aireadylife/vault/health/config.md` and check whether the key fields have been filled in (non-blank values after the `:`).

**Rules (follow exactly, no improvisation):**

1. **Vault folder is missing entirely** → output only: *"Your health vault isn't installed. Download it at [frudev.gumroad.com/l/aireadylife-health](https://frudev.gumroad.com/l/aireadylife-health), unzip, and place the `health/` folder at `~/Documents/aireadylife/vault/`."* Stop.

2. **Config fields are blank** (empty after `:`) → output the First-Run Message below verbatim. Stop. Do **not** scaffold files, offer alternatives, or ask questions.

3. **Config is filled in** → proceed with the requested skill normally.

### First-Run Message

> **Welcome to AI Ready Life: Health!**
>
> Your vault is installed at:
> - **Mac:** `~/Documents/aireadylife/vault/health/`
> - **Windows:** `%USERPROFILE%\Documents\aireadylife\vault\health\` Before skills can run, your config and documents need to be in place.
>
> **Step 1 — Complete your config**
> Open `~/Documents/aireadylife/vault/health/config.md` and fill in every field. Leave a field blank rather than guessing — the skills will flag anything that's missing.
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
>
> **Stop here.** Do not scaffold files, do not offer options, do not ask questions. Wait for the user to complete setup and re-run the skill.

## Skill Index

Skills live in `skills/<skill-name>/SKILL.md`. To run a skill, read its `SKILL.md` and follow the instructions inside.

**Apps (data connectors — fallback when no native MCP connector available):**
- `app-apple-health` — iPhone HealthKit export (steps, active energy, resting HR, body weight, workouts) via iOS Shortcut → iCloud Drive. Owns dedup/append into `wearable-log.csv`.
- `app-mychart.portal` — Patient portal records (lab results, visit notes, after-visit summaries, upcoming appointments, current med list, immunizations) via Playwright with Chrome cookie authentication.
- `app-oura-ring.api` — Daily sleep, readiness, activity data from Oura Ring API v2 (sleep score, HRV RMSSD, resting HR, readiness, steps, active calories). Owns dedup/append into `wearable-log.csv`.

**Operations (user-facing routines):**
- `op-anomaly-watch` — Weekly wearable anomaly watch (HRV drops, low readiness streaks, RHR elevation).
- `op-appointment-readiness` — Scans appointments in next 7 days, triggers prep brief, verifies in-network status before electives.
- `op-lab-review` — Triggered on new lab results; runs lab summary and flagging.
- `op-medication-review` — Monthly medication review; calls refill-flag task and post-visit reconciliation.
- `op-monthly-sync` — Full monthly sync of wearables, labs, meds, and refresh of all briefs.
- `op-preventive-care-review` — Quarterly preventive-care check.
- `op-review-brief` — Lightweight current-state snapshot (read-only).
- `op-symptom-log-review` — Monthly pattern check on user-maintained symptom log; correlations with sleep/HRV/stress (v2; opt-in).
- `op-vaccination-tracking` — Annual vaccination review against CDC adult schedule; surfaces what's due / overdue.

**Flows (multi-step internals called by ops):**
- `flow-build-hsa-utilization-summary` — Monthly HSA brief: YTD spend, balance, $2k investment threshold, missing-receipt audit.
- `flow-build-lab-summary` — Structured lab summary with biomarker values, reference ranges, trend direction.
- `flow-build-wellness-summary` — Monthly wearable wellness summary (sleep, HRV, RHR, readiness, steps, active energy).
- `flow-eob-reconciliation` — Matches EOBs to provider bills; flags discrepancies, balance billing, surprise OON; tracks deductible/OOP-max progress.
- `flow-fitness-goal-review` — Weight/steps/exercise-minutes/resistance-training vs user-configured goals; streaks and underperformance flags.
- `flow-prep-appointment-brief` — 24h pre-visit packet: last visit, current meds, open lab flags with trends, three prepared questions. PHI-redacted.
- `flow-reconcile-medications-post-visit` — Diffs new visit-note med list against active meds; adds, discontinues, updates dose changes.

**Tasks (atomic operations called by flows / ops):**
- `task-attach-trend-context` — Single primitive: given biomarker + current value, returns prior value, delta, direction (improving/stable/worsening) using reference range polarity.
- `task-flag-out-of-range-value` — Writes structured flag for any lab biomarker outside reference range.
- `task-flag-preventive-care-gap` — Writes flag for any overdue or due-soon preventive-care screening.
- `task-flag-upcoming-refill` — Single refill-flag entry point: scans medications, computes refill dates, writes 30-day reminders.
- `task-prepare-emergency-medical-info` — Generates wallet-card / lock-screen / Apple Medical ID emergency card from severe allergies, active meds, conditions, blood type, insurance, ICE contacts.
- `task-redact-phi-for-brief` — Deterministic PHI scrub run on every brief; replaces identifiers and raw lab numerics with categorical bands.
- `task-track-mental-health` — Mood/stress/sleep-quality logging; rolling baselines, streak detection, optional wearable correlation (opt-in).
- `task-update-allergy-medication-list` — Single source of truth for allergies, adverse reactions, active meds; ER-readable format.
- `task-update-family-medical-history` — Structured first-degree (and known second-degree) family medical history; surfaces risk-relevant patterns to preventive-care.
- `task-update-open-loops` — Single write point for `open-loops.md`.
- `task-update-provider-directory` — Maintains provider directory (PCP, dentist, eye, derm, OB-GYN, mental health, specialists) with in-network status + last-verified date.
