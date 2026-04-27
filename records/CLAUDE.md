# AI Ready Life: Records Plugin

## Vault Location

| OS | Vault path |
|----|------------|
| **Mac** | `~/Documents/aireadylife/vault/records/` |
| **Windows** | `%USERPROFILE%\Documents\aireadylife\vault\records\` |

Determine the user's OS from context (file paths they share, or ask if unclear). Use the correct path for their OS. Never use relative paths.

## First Time Setup

If `~/Documents/aireadylife/vault/records/` does not exist or is empty:

1. Purchase the **AI Ready Life: Records Vault** at [frudev.gumroad.com/l/aireadylife-records](https://frudev.gumroad.com/l/aireadylife-records)
2. Unzip the download
3. Move the `records/` folder to `~/Documents/aireadylife/vault/`
4. Open `~/Documents/aireadylife/vault/records/config.md` and fill in your details
5. Return here and run any skill — it will find your vault automatically

## Vault Structure

```
~/Documents/aireadylife/vault/records/
├── config.md          — your profile and settings
├── open-loops.md      — active flags and open items
├── 00_current/        — active documents and current state
├── 01_prior/          — prior period records
└── 02_briefs/         — generated briefs and reports
```

## Skills

Skills are located under `records/skills/` — each skill has its own folder containing a `SKILL.md` file.

## Vault Access

**Mac:** If a file read fails with a permission error, the AI tool needs filesystem access to your Documents folder. Tell the user:
> *Go to **System Settings → Privacy & Security → Full Disk Access**, then add the app you are running this from:*
> - *Claude Code or Codex CLI in a terminal → add **Terminal**, **iTerm**, or **Ghostty** (whichever you use), then restart it.*
> - *Claude Desktop → add **Claude**, then restart it.*

**Windows:** No permission grant needed — terminal apps and Claude Desktop run unrestricted by default.

Do not proceed with the skill until access is confirmed (Mac) or reassure the user that no action is needed (Windows).

## First Run

Before running **any skill or flow** in this domain — including flows called by other skills — read `~/Documents/aireadylife/vault/records/config.md` and check whether the key fields have been filled in (non-blank values after the `:`).

**Rules (follow exactly, no improvisation):**

1. **Vault folder is missing entirely** → output only: *"Your records vault isn't installed. Download it at [frudev.gumroad.com/l/aireadylife-records](https://frudev.gumroad.com/l/aireadylife-records), unzip, and place the `records/` folder at `~/Documents/aireadylife/vault/`."* Stop.

2. **Config fields are blank** (empty after `:`) → output the First-Run Message below verbatim. Stop. Do **not** scaffold files, offer alternatives, or ask questions.

3. **Config is filled in** → proceed with the requested skill normally.

### First-Run Message

> **Welcome to AI Ready Life: Records!**
>
> Your vault is installed at:
> - **Mac:** `~/Documents/aireadylife/vault/records/`
> - **Windows:** `%USERPROFILE%\Documents\aireadylife\vault\records\` Before skills can run, your config and documents need to be in place.
>
> **Step 1 — Complete your config**
> Open `~/Documents/aireadylife/vault/records/config.md` and fill in every field. Leave a field blank rather than guessing — the skills will flag anything that's missing.
>
> **Step 2 — Gather your documents and add them to `00_current/`**
> Here's what this domain needs:
>
- **Identity documents** — passport (number, expiry), driver's license (state, expiry), any government IDs.
- **Active subscriptions** — service name, monthly or annual cost, renewal date, and whether you still use it. Check your credit card statements.
- **Legal documents** — location of your will, power of attorney, healthcare directive, and any trust documents.
- **Insurance policy numbers** — reference numbers for health, auto, home, life, and any other active policies.
- **Key account numbers** — masked last-4 for bank accounts, investment accounts, and tax ID if relevant.
>
> **Step 3 — Run your first skill**
> Once config.md is filled in and at least a few documents are in `00_current/`, try: *"document audit"*
>
> You don't need everything perfect to start — add what you have and the skills will tell you what's still missing.
>
> **Stop here.** Do not scaffold files, do not offer options, do not ask questions. Wait for the user to complete setup and re-run the skill.

## Skill Index

Skills live in `skills/<skill-name>/SKILL.md`. To run a skill, read its `SKILL.md` and follow the instructions inside.

**Apps (data connectors — fallback when no native MCP connector is available):**
- **`app-1password`** — 1Password vault metadata via the local `op` CLI (read-only; never reads passwords).
- **`app-gdrive`** — Google Drive read/write fallback for users without Claude Desktop's native Drive connector.

**Operations (user-facing routines):**
- **`op-document-audit`** — Quarterly document audit. Storage gaps, missing scans, naming-convention lint, retention sweep input.
- **`op-monthly-sync`** — Monthly full records data sync. Refreshes index, subscriptions, renewal calendar, manifests.
- **`op-review-brief`** — Monthly records review brief. Includes the full subscription review (replaces the prior standalone op).
- **`op-digital-legacy-plan`** — Annual survivor packet: account inventory, password-manager unlock plan, legacy-contact verification, key contacts, cleanup checklist.

**Flows (multi-step internals called by ops):**
- **`flow-check-expiring-documents`** — Scans identity and legal documents for expirations within 12 months.
- **`flow-renewal-calendar`** — Cross-category renewal timeline (IDs, vehicles, pro licenses, HOA, insurance, subscriptions).
- **`flow-share-paths-with-agents`** — Emits per-domain JSON manifests (tax, health, insurance, career, vehicle, legacy) consumed by other plugins.

**Tasks (atomic operations called by flows / ops):**
- **`task-log-document`** — Add a new document to the vault with type, holder, dates, issuing authority, physical + digital storage locations.
- **`task-ingest-from-gmail`** — Scan Gmail for receipts, policy docs, account confirmations, IRS letters; surface candidates for `task-log-document`.
- **`task-detect-subscriptions-from-email`** — Parse Gmail recurring-charge receipts; rebuild `subscriptions.md` with the authoritative table.
- **`task-build-vault-index`** — Generate `00_current/INDEX.md` listing every document with category, holder, expiration, storage locations, dependent agents.
- **`task-rename-to-convention`** — Lint and rename files to `YYYY-MM-DD_Source-Type-Description.ext`; user-confirmed execution.
- **`task-apply-retention-policy`** — Annual sweep moving expired / aged documents from `00_current/` to `01_prior/` per category retention rules.
- **`task-build-account-inventory`** — Comprehensive online-account list assembled from password-manager metadata + Gmail confirmations + manual entries.
- **`task-update-vehicle-records`** — Per-vehicle record: registration, title, insurance card, maintenance log, recall status.
- **`task-update-key-contacts`** — User-configurable directory of critical professional contacts (lawyer, accountant, doctor, etc.).
- **`task-verify-backup`** — Monthly check that critical-document backups are current and an offsite legal copy exists.
- **`task-flag-expiring-id`** — Writes an ID expiration flag to `open-loops.md` with renewal action, portal link, cost.
- **`task-track-password-rotation`** *(opt-in)* — Tracks rotation cadence for high-value accounts; flags breach-implicated accounts.
- **`task-update-open-loops`** — Single write-point for `open-loops.md`; resolves completed items.
