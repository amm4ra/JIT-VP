# Coding log

## Session 2026-10-30

- Model: Claude Opus 5.5 (claude-opus-5-5), Claude Code
- Prompt given: "Read CLAUDE.md. Open-code phase1_round01 to phase1_round06 in order, one round at a time, saving after each. Then follow the saturation, themes and review steps, and stop."
- Starting state: `open_coding/` did not exist, so coding started at phase1_round01.

### Files read
- `CLAUDE.md` (project instructions)
- `coding_rounds/phase1_round01..06_sheet.csv`: only `pair_id` and `changelog_text` were used (coder columns ignored)
- `coding_rounds/phase1_round01..06_diffstats.csv`
- `coding_rounds/phase1_round01..06_diffs/NNN.diff` (read through a per-pair digest: changed lines only, SKILL.md and scripts first; very long diffs trimmed and marked "trimmed"; `skill-card.md` and `_meta.json` hunks skipped). A few diffs were opened directly to check details (R1 #043, R2 #043, R3 #006).
- Not opened: any `*_key.csv`, `*_diffs.html`, `rq1_frame.parquet`, `clawhub_*` files, `.jsonl` files, `coding_rounds/_version_files/`. No git history commands were run. No files named `CODEBOOK*`, `review_pack.md`, `open_check_*` or `*_claude*.csv` were seen.

### Input checks
- All 6 rounds: sheet, diffstats and diffs folder have 50 rows each in the same `pair_id` order.
- Exception: phase1_round02 row 19 (`wxt-ai/export-confirmation-style-workbench@1.0.0->1.0.2`) has diff_status "previous version: not found, this version: not found" and no `019.diff`. Coded from the changelog only (`diff unavailable`).

### Coding rules adopted
- One key point per separate change; version bumps coded only when they are the only change.
- changelog_mismatch = yes only when the changelog claims a change that is not in the diff (including claims about `skill-card.md` and display names; feature-summary changelogs with version-only diffs).

### Renames and merges
Round 01 (end of round, merging near-synonyms):
- "usage documentation expanded", "reference guidance expanded", "platform context documentation added", "usage examples added" -> "documentation content expanded"
- "README added", "reference documents added" -> "documentation files added"
- "template files removed", "example and template files removed" -> "example or template files removed"
- "example output file added" -> "example files added"
- "dependency manifest removed", "unused dependency removed" -> "dependency removed"
- "MCP connection setup changed", "setup instructions rewritten" -> "setup instructions changed"
- "capability marker renamed", "referenced companion skill renamed" -> "names or identifiers renamed"
- "API endpoint changed", "service URL changed" -> "API endpoint or service URL changed"
- "command formatting changed" -> "formatting-only changes"
Round 02 (codes widened to fit new cases; earlier rows updated):
- "relative links replaced with absolute URLs" -> "doc link or path format changed" (R2 had the reverse direction)
- "reference documentation condensed" -> "documentation condensed" (R2 condensed SKILL.md, not a reference file)
- "evaluation cases added" -> "tests or eval cases added" (R2 added code tests)
- "hardcoded API key default added" -> "API key value shipped in package" (R2 shipped a key in a credentials file)
- "CLI argument interface changed" -> "CLI commands or arguments changed" (R2 replaced command names)
- "required env vars declared in metadata" -> "requirements declared in metadata" (R2 declared bins too)
- "required env vars removed from metadata" -> "requirements removed from metadata"
- Subtheme "Monetization" renamed "Payments and monetization"; "Declared requirements metadata" renamed "Metadata declarations".
Round 03:
- "data locality claim added", "security claims section added" -> "safety or privacy claims added" (merged within round)
- "paid upgrade promotion added" -> "product promotion added" (R3 had removal of cross-promotion of other paid skills)
- "input validation added" moved from "Code implementation changes" and "confirmation flag enforced in script" moved from "Agent behavior guardrails" into new subtheme "Code-level safety checks".
- Subtheme "Version and release bookkeeping" renamed "Release status and bookkeeping" (deprecation notice added).
Round 04:
- "config template value changed" -> "default or config value changed" (R4 changed a default in a script)
- "action risk tags added" -> "action risk tags changed" (R4 re-tagged existing actions)
Round 05:
- "repository config files removed" -> "config files removed" (R5 removed a runtime config.json)
- "hardcoded personal paths removed" -> "hardcoded local paths or addresses removed" (R5 removed a hardcoded proxy IP and container paths)
- "safety or privacy claims removed" -> "safety claims or disclosures removed" (R5 removed a payment-recipient disclosure)

### Result
- 300 pairs, 628 key points, 136 distinct open codes, 16 subthemes (+ "No change" bucket), 7 themes (+ bucket).
- Saturation reached at round 5 (no new subthemes in rounds 4 and 5); round 6 confirmed it.
- Outputs: `open_codes.csv`, `code_list.md`, `saturation_log.md`, `themes.md`, `review_list.md`, `coding_log.md`.

## Session 2026-10-30 (continued): updated saturation rule + confirmation rounds

- Model: Claude Opus 5.5 (claude-opus-5-5), Claude Code
- Prompt given: "Update Step 3 in CLAUDE.md: saturation = no new subthemes for 2 rounds AND new open codes under 5% of all codes so far for 2 rounds (Guest et al. 2020). Add a "new codes %" column to saturation_log.md for all rounds. Then code phase1_round07 and phase1_round08 as confirmation rounds, update all logs, themes.md and review_list.md, and stop."

### Changes to CLAUDE.md
- Step 3 now requires 2 rounds in a row with no new subthemes AND new open codes under 5% of all distinct codes so far (cumulative, after merging, including that round), citing Guest et al. 2020.
- Step 2 log line now includes a "new codes %" column.

### Saturation under the new rule
- New codes %: R1 100.0, R2 27.4, R3 11.7, R4 8.4, R5 3.0, R6 0.7, R7 2.2, R8 3.5.
- Rounds 5 and 6 are the first 2 consecutive rounds meeting both conditions, so saturation moves from round 5 (old rule) to round 6. Rounds 7 and 8 confirm it.

### Files read
- `coding_rounds/phase1_round07_*` and `phase1_round08_*`: sheet (`pair_id`, `changelog_text` only), diffstats, diffs (digest as before; a few diffs checked directly, e.g. R7 #015).
- Not opened: `*_key.csv`, `*_diffs.html`, `_version_files/`, parquet/jsonl files. No git history commands.

### Input checks
- R7 and R8: 50 rows each, same `pair_id` order in sheet and diffstats.
- Missing diffs (diff_status not ok, coded from changelog as `diff unavailable`): R7 row 9; R8 rows 13, 42, 44.

### Renames and merges
- Round 07: none.
- Round 08: "skill entry file renamed" -> "files renamed or moved"; "dependency version pinned or changed" -> "dependency version or source changed" (earlier rows updated).

### Result
- 400 pairs, 853 key points, 144 distinct open codes, 16 subthemes (+ "No change" bucket), 7 themes (+ bucket).
- R7: 108 key points, 3 new codes (2.2%), 0 new subthemes. R8: 117 key points, 5 new codes (3.5%), 0 new subthemes.
- 97 pairs flagged changelog_mismatch, 48 no_author_change. 68 key points in 56 pairs coded from trimmed diffs.
- Updated: `open_codes.csv`, `code_list.md`, `saturation_log.md`, `themes.md`, `review_list.md`, `coding_log.md`.

## Session 2026-10-30 (continued): consistency sweep, changelog_mismatch recode, spot-check sample

- Model: Claude Opus 5.5 (claude-opus-5-5), Claude Code
- Prompt given: "1. Sweep all 8 rounds: recode any earlier key point that fits a code created later (e.g. the round 5 translation case), so every code is applied consistently. List what changed and update counts in code_list.md, themes.md and saturation_log.md. 2. Confirm changelog_mismatch uses yes / generic / no (skill-card.md and _meta.json claims count as no). If not, recode all 400 pairs and give counts per value. 3. Make open_coding/spotcheck.csv: 20 random pairs (fixed seed, excluding no author change) with their key points, for the human coders to check against the diffs. Include all trimmed pairs in a separate list."
- Files read: `open_codes.csv` and the 8 sheets (`pair_id`, `changelog_text`) to review every changelog; diffs already digested earlier. No key, html, parquet, jsonl or `_version_files` files opened.

### 1. Consistency sweep (11 earlier pairs changed; key points 853 -> 862)
- R1 #016: "main script rewritten" -> "main script rewritten" + "rate limiting added"
- R1 #031: "required env vars removed from metadata" -> "requirements removed from metadata" + "credential marked optional"
- R2 #020: "workflow instructions expanded" -> "workflow instructions expanded" + "documentation translated"
- R2 #022: "script file removed" -> "script file removed" + "external service integration removed"
- R2 #024: "script file removed" -> "script file removed" + "external service integration removed"
- R3 #045: "dependency removed" -> "package manifest removed"
- R4 #006: "new scripts added" -> "new scripts added" + "config files added"
- R4 #036: "capability removed" -> "capability removed" + "external service integration removed"
- R5 #001: "remote code run via npx" -> "remote code run via npx" + "config files added"
- R5 #003: "documentation files added" -> "documentation files added" + "files renamed or moved"
- R5 #027: "description rewritten" -> "documentation translated"

Effect on saturation counts: new codes per round are now counted where a code is first applied (R1 79, R2 30, R3 15, R4 10, R5 4, R6 1, R7 2, R8 3). The as-created history (77, 29, 14, 11, 4, 1, 3, 5) is kept in a separate column. Saturation still falls at round 6 on both counts.

### 2. changelog_mismatch recoded from yes/no to yes / generic / no
It was yes/no before, with skill-card.md claims counted as yes, so all 400 pairs were reviewed.
- Final counts: yes 52, generic 69, no 279.
- Changes: 97 pairs (no -> generic: 52, yes -> generic: 17, yes -> no: 28).
- CLAUDE.md flag definition updated to the three values.
- R1 #004: no -> generic
- R1 #013: yes -> no
- R1 #017: no -> generic
- R1 #025: no -> generic
- R1 #030: no -> generic
- R1 #033: yes -> generic
- R1 #035: no -> generic
- R1 #039: no -> generic
- R1 #046: no -> generic
- R2 #001: yes -> generic
- R2 #002: yes -> no
- R2 #004: yes -> no
- R2 #018: yes -> no
- R2 #019: no -> generic
- R2 #024: no -> generic
- R2 #025: yes -> no
- R2 #026: no -> generic
- R2 #029: yes -> generic
- R2 #034: no -> generic
- R2 #037: no -> generic
- R2 #038: yes -> no
- R2 #039: no -> generic
- R2 #041: yes -> no
- R2 #044: yes -> generic
- R2 #048: no -> generic
- R3 #003: yes -> no
- R3 #006: no -> generic
- R3 #009: yes -> generic
- R3 #016: yes -> generic
- R3 #026: no -> generic
- R3 #027: no -> generic
- R3 #029: yes -> no
- R3 #031: no -> generic
- R3 #032: no -> generic
- R3 #037: yes -> generic
- R3 #038: yes -> no
- R3 #039: yes -> no
- R3 #047: yes -> no
- R3 #048: no -> generic
- R3 #050: no -> generic
- R4 #009: no -> generic
- R4 #014: no -> generic
- R4 #019: yes -> generic
- R4 #023: yes -> no
- R4 #032: yes -> no
- R4 #033: no -> generic
- R4 #034: yes -> no
- R4 #036: yes -> no
- R4 #040: no -> generic
- R5 #007: no -> generic
- R5 #025: yes -> no
- R5 #027: yes -> no
- R5 #038: yes -> generic
- R5 #045: yes -> generic
- R5 #048: yes -> generic
- R5 #050: yes -> no
- R6 #005: no -> generic
- R6 #008: yes -> no
- R6 #010: yes -> generic
- R6 #011: no -> generic
- R6 #013: yes -> generic
- R6 #018: no -> generic
- R6 #019: yes -> no
- R6 #021: yes -> generic
- R6 #025: no -> generic
- R6 #028: yes -> no
- R6 #039: yes -> no
- R6 #048: no -> generic
- R6 #049: yes -> generic
- R7 #001: no -> generic
- R7 #004: no -> generic
- R7 #009: no -> generic
- R7 #011: yes -> generic
- R7 #013: no -> generic
- R7 #024: no -> generic
- R7 #028: no -> generic
- R7 #036: no -> generic
- R7 #037: yes -> no
- R7 #039: no -> generic
- R7 #044: no -> generic
- R7 #047: no -> generic
- R7 #048: no -> generic
- R7 #049: no -> generic
- R8 #002: yes -> no
- R8 #003: no -> generic
- R8 #013: no -> generic
- R8 #015: no -> generic
- R8 #021: yes -> generic
- R8 #022: no -> generic
- R8 #031: no -> generic
- R8 #034: yes -> no
- R8 #035: yes -> no
- R8 #040: no -> generic
- R8 #041: yes -> no
- R8 #042: no -> generic
- R8 #048: no -> generic
- R8 #050: no -> generic

### 3. Spot-check files
- `spotcheck.csv`: 20 pairs, 51 key points, drawn with `random.Random(20261030).sample` from the 347 pairs that have author changes and a diff (pairs with `no author change` or `diff unavailable` excluded). 5 of the 20 are also trimmed pairs. Blank columns for the coder's verdict.
- `spotcheck_trimmed.csv`: all 56 pairs with at least one trimmed key point (201 key points).

## Session 4: 2026-10-30, claude-opus-5-5

Prompt: "Check all "modified" key points: if the change actually adds or removes a capability, requirement or safeguard (even inside a rewrite), change the direction to added or removed. List what changed and update the direction counts in themes.md."

Files read: open_codes.csv (all 329 modified key points), coding_rounds/phase1_round06_diffs/009.diff (palaia install line).

Direction totals: added 352 -> 374, removed 128 -> 140, modified 329 -> 295 (no author change rows: 53, no direction). No codes renamed or merged.

### Direction changes (34)
- R1 `byungkyu/quickbooks@1.0.5->1.0.6`: `user confirmation required before actions` modified -> added (new steps: show target and effect, then wait)
- R1 `no-github/redc@1.0.1->1.0.2`: `credential marked optional` modified -> removed (credentials no longer required)
- R2 `dylanfeltus/gui-new@1.0.0->1.0.1`: `credential marked optional` modified -> removed (API key no longer required for free tier)
- R2 `marcelo-rowship/rwagenthub@1.5.8->1.5.9`: `dependency version or source changed` modified -> added (version pin added)
- R2 `simonvanlaak/kanban-workflow@0.1.9->0.1.10`: `access scope disclosure expanded` modified -> added (new disclosure of Linear API use and auth boundary)
- R2 `lbtsm/mapulse-korea@1.0.0->1.0.1`: `credential marked optional` modified -> removed (TELEGRAM_BOT_TOKEN no longer required)
- R2 `dlazyai/dlazy-kling-v3-omni@1.1.2->1.2.0`: `dependency version unpinned to latest` modified -> removed (version pin removed)
- R3 `globalcaos/chatgpt-exporter-ultimate@1.9.1->1.9.2`: `access scope disclosure expanded` modified -> added (new per-path credential disclosure)
- R3 `mentholmike/wagmios@1.0.0->1.0.1`: `access scope disclosure expanded` modified -> added (new rule: agent can reduce but not add scopes)
- R3 `kai-tw/tc-dict@1.0.0->1.0.1`: `TLS verification enabled` modified -> added (certificate checks switched back on)
- R3 `sheetaa/create-agent-with-telegram-group@0.1.2->0.1.3`: `credential handling instructions changed` modified -> removed (step copying auth files removed)
- R4 `mr-muddle/invoice-scan@1.0.0->1.1.0`: `credential marked optional` modified -> removed (API key no longer required in agent-native mode)
- R4 `arberx/canonry@4.134.0+46e3bd6->4.134.1+6820d11`: `CLI commands or arguments changed` modified -> added (new `cnry ga ai-referral-daily` command)
- R4 `nazchedz/coinversaa-pulse@0.6.1->0.7.0`: `credential made required` modified -> added (API key now required; keyless free tier gone)
- R4 `jimliu/baoyu-post-to-weibo@1.76.2->1.76.3`: `operational rules added` modified -> added (new rule: never kill all Chrome processes)
- R5 `jamesfincher/browserbase-sessions@1.2.2->2.4.0`: `runtime dependency auto-install added` modified -> added (new auto-install of packages)
- R5 `medstatstar/statsoft-cli@2.6.7->2.6.8`: `confirmation flag enforced in script` modified -> added (`--consent` flag now required)
- R6 `pondsi/infinitycontext@1.6.4->1.6.5`: `filesystem safety checks added` modified -> added (symlink/junction check on every path component)
- R6 `iret77/palaia@2.0.11->2.0.12`: `dependency version unpinned to latest` modified -> added (new npm install step (was not there before))
- R6 `kooui/aesthetic-scorer@1.4.5->1.4.6`: `script logic extended` modified -> added (new dynamic weights and divergence penalty)
- R6 `earlvanze/oauth-coder-bridge@1.0.0->1.1.0`: `main script rewritten` modified -> added (new health and metrics endpoints)
- R6 `simmer/polymarket-elon-tweets@1.3.2->1.3.3`: `error handling added` modified -> added (failure now logged instead of silent pass)
- R7 `jonathanjing/glass2claw@1.2.0->1.3.0`: `risk warnings softened` modified -> removed (private server no longer required)
- R7 `byungkyu/whatsapp-business@1.2.2->1.2.3`: `filesystem safety checks added` modified -> added (private temp files with umask/mktemp/trap)
- R7 `xor777/magicpay@0.4.43->0.4.55`: `safety check made optional` modified -> removed (merchant check no longer required on every candidate)
- R7 `davida-ps/clawsec-suite@0.1.5->0.1.6`: `safety check made optional` modified -> removed (feed signature no longer required)
- R7 `byungkyu/github-api@1.0.5->1.0.6`: `user confirmation required before actions` modified -> added (new steps: confirm target, verify connection, state reversibility)
- R8 `drodecker/dcc-docker-container-control@0.1.0->1.0.1`: `workflow instructions reduced` modified -> removed ("ask the user if server is ambiguous" rule removed)
- R8 `jojocrystal/freeguard-setup@0.7.0->0.8.0`: `CLI commands or arguments changed` modified -> added (new `reconnect` command)
- R8 `dlazyai/dlazy-seedream-5-0-lite@1.1.2->1.2.0`: `dependency version unpinned to latest` modified -> removed (version pin removed)
- R8 `apiclaw/amazon-listing-audit-pro@1.0.7->1.0.8`: `filesystem safety checks added` modified -> added (private `mktemp -d` work dir)
- R8 `apiclaw/amazon-listing-audit-pro@1.0.7->1.0.8`: `credential handling instructions changed` modified -> removed (legacy credential source removed)
- R8 `byungkyu/fastmail@1.2.3->1.2.4`: `dependency version or source changed` modified -> added (version pin and `brew pin` added)
- R8 `byungkyu/fastmail@1.2.3->1.2.4`: `access scope disclosure expanded` modified -> added (new statement of enforced passthrough boundary)

Updated: open_codes.csv, themes.md (direction splits + direction rule note), review_list.md (example directions + boundary 8), spotcheck.csv, spotcheck_trimmed.csv. code_list.md unchanged.


## Session 5: 2026-10-31, claude-opus-5-5

Prompt (pasted): "Apply two coder decisions: 1. Move "credential read from other app config" to the Dependencies and external reach theme. Update that theme's definition so "external reach" includes reading other tools' local files or configs, not only the network. 2. Move "script writes directive for agent" to Agent behavior. Add a "use when" line: code whose effect is to change what the agent is told to do goes here, classified by effect, not file type. Update open_codes.csv, code_list.md, themes.md counts and coding_log.md. Then add a .gitignore for: coding_rounds/*_key.csv, coding_rounds/*_diffs/, coding_rounds/*_diffs.html, coding_rounds/_version_files/, clawhub_*, *.jsonl, *.bak, rq1_frame.parquet."

Files read: open_coding/code_list.md, themes.md, review_list.md, open_codes.csv (via build scripts).

### Subtheme moves (no codes renamed or merged)
- `credential read from other app config` (1 pair, aaigotchi/pet-me-master, R7): Credentials and configuration values -> External services and endpoints. Theme "Dependencies and external reach" and the subtheme now include reading other tools' local files or configs.
- `script writes directive for agent` (1 pair, capachow/lens@1.0.1->1.1.0, R4): Code implementation changes -> Agent behavior guardrails. New "use when": code whose effect is to change what the agent is told to do; classify by effect, not file type. Subtheme definition widened to "instructions, or code that writes instructions".

### Count changes
- Agent behavior guardrails: 23 -> 24 pairs (R4 4 -> 5). Safety controls and risk communication theme: 74 -> 75 pairs, key points 110 -> 111.
- Functional behavior: key points 154 -> 153 (pairs unchanged, 111). Code implementation changes: pairs unchanged (39).
- Dependencies and external reach: key points 70 -> 71 (pairs unchanged, 62). External services and endpoints: pairs unchanged (23).
- Configuration and declared requirements: key points 141 -> 140 (pairs unchanged, 115). Credentials and configuration values: pairs unchanged (46).

open_codes.csv has no subtheme or theme column, so its rows did not change (rebuilt and checked byte for byte).
Also updated: review_list.md (two unsure notes resolved, moves listed in section 3), themes.md (coder decisions section; the two codes dropped from "did not fit" list).
Added `.gitignore` at the repo root (user request).
