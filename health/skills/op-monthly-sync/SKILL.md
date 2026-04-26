---
type: op
cadence: monthly
description: >
  Full health data sync on the 1st of each month. Pulls new wearable exports (Oura
  Ring or Apple Health), downloads visit notes and lab results from the configured
  patient app-insurance-portal.portal (MyChart), refreshes the medication list, updates the deductible
  and HSA balance from the insurance log, and organizes all new files in vault. Then
  triggers the Health Review Brief. Triggers: "health monthly sync", "sync health
  data", "refresh health vault", "run my health sync".
---

# health-monthly-sync

**Cadence:** Monthly (1st of month)
**Produces:** Fully refreshed health vault; then triggers `health-review-brief`

## What It Does

The monthly sync is the master operation that keeps the health vault current across all sub-domains. It runs in four sequential phases — wearable, app-insurance-portal.portal, medications, and insurance — then hands off to the review brief for synthesis.

**Phase 1: Wearable Sync.** Calls `health-sync-wearable-data` to ingest any new Oura Ring or Apple Health export files from the configured sync folder. Reports records added, coverage dates, and any gaps.

**Phase 2: Patient Portal Sync.** Using the configured patient app-insurance-portal.portal (MyChart/Epic or equivalent), downloads any new lab results, visit notes (after-visit summaries), upcoming appointment confirmations, and active medication list from the app-insurance-portal.portal. New lab PDFs are placed in `vault/health/00_current/` with standard naming (YYYY-MM-DD_lab_[panel-type].pdf). New visit notes go to `vault/health/00_current/`. If new lab results are found, `health-lab-review` is triggered automatically. This step requires the app-insurance-portal.portal to be configured and accessible — if the session has expired, the user is prompted to re-authenticate.

**Phase 3: Medication List Refresh.** Cross-references the app-insurance-portal.portal's current medication list against the vault's `vault/health/00_current/medications.md`. Flags any discrepancies (medication listed in vault but not on app-insurance-portal.portal active list; medication on app-insurance-portal.portal but not in vault). Does not automatically update the vault list — presents the diff and asks the user to confirm before writing changes.

**Phase 4: Insurance and HSA Update.** Prompts user to confirm current deductible balance and HSA balance if the values haven't been updated within the past 30 days. Updates `vault/health/00_current/deductible-tracker.md` and `vault/health/00_current/hsa-balance.md` with the confirmed values and the date of update.

After all four phases complete, the sync triggers `health-review-brief` to produce the monthly wellness brief from the freshly synchronized vault.

## Configuration

Set in `vault/health/config.md`:
- `wearable_type` — oura | apple_health | both
- `app-insurance-portal.portal_type` — app-mychart.portal | other
- `app-insurance-portal.portal_url` — your specific app-insurance-portal.portal URL (e.g., https://app-mychart.portal.yourhospital.org)
- `app-insurance-portal.portal_username` — login username for the app-insurance-portal.portal

## Calls

- **Flows:** `health-sync-wearable-data`
- **Ops triggered:** `health-lab-review` (if new labs found), `health-review-brief` (on completion)
- **Tasks:** `health-update-open-loops`

## Apps

- `app-oura-ring.api` or `app-apple-health` — wearable data export
- `app-mychart.portal` — patient app-insurance-portal.portal download (headless=False required)

## Vault Output

- `vault/health/00_current/` — updated wearable log
- `vault/health/00_current/` — new lab result files
- `vault/health/00_current/` — new visit notes
- `vault/health/00_current/medications.md` — refreshed after user confirms diff
- `vault/health/00_current/deductible-tracker.md` — updated balance
- `vault/health/00_current/hsa-balance.md` — updated balance
- `vault/health/02_briefs/YYYY-MM-health-brief.md` — monthly review brief (produced by triggered op)

## Vault Paths

- Reads from: `~/Documents/aireadylife/vault/health/00_current/` — active records and current state
- Reads from: `~/Documents/aireadylife/vault/health/01_prior/` — prior period records for trend comparison
- Reads from: `~/Documents/aireadylife/vault/health/02_briefs/` — prior briefs for period-over-period context
