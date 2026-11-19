# Themes (RQ1 open coding, phase 1 rounds 01-08)

400 pairs, 862 key points, 144 open codes, 16 subthemes (+ "No change" bucket), 7 themes (+ bucket).

Pair counts: a pair counts once per theme/subtheme even if it has several key points there. Direction split counts key points.

## Overview

theme | pairs | key points | per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08)
---|---|---|---
Upkeep and presentation | 203 | 246 | 25 | 25 | 23 | 19 | 30 | 26 | 25 | 30
Package composition | 53 | 73 | 6 | 9 | 6 | 7 | 8 | 5 | 7 | 5
Functional behavior | 111 | 153 | 15 | 15 | 13 | 16 | 10 | 15 | 12 | 15
Dependencies and external reach | 62 | 71 | 12 | 12 | 5 | 4 | 6 | 8 | 7 | 8
Configuration and declared requirements | 115 | 140 | 11 | 16 | 18 | 13 | 15 | 14 | 14 | 14
Safety controls and risk communication | 75 | 111 | 8 | 7 | 9 | 13 | 10 | 7 | 8 | 13
Monetization | 14 | 15 | 3 | 2 | 1 | 1 | 1 | 2 | 4 | 0
No change (bucket) | 53 | 53 | 6 | 3 | 8 | 7 | 4 | 10 | 8 | 7

## Theme: Upkeep and presentation

Changes to how the skill is versioned, described and documented, without changing what it does.

- Pairs: 203 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 25 | 25 | 23 | 19 | 30 | 26 | 25 | 30
- Direction split (key points): added 61, removed 8, modified 177

### Subtheme: Release status and bookkeeping

Changes that only record versions, release notes or lifecycle status.

- Use when: the change only records a version, release note or lifecycle status (e.g. deprecated).
- Don't use when: anything else changed in the same key point; a version pin of a dependency (use Installation and dependencies).
- Pairs: 44 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 5 | 5 | 8 | 3 | 8 | 5 | 6 | 4
- Direction split (key points): added 6, modified 38
- Examples: `sullivangu/eva-ui-skill@1.0.0->1.0.1`, `oomol/oo-callrail@1.0.0->1.0.2`
- Open codes (pairs): version number bump only (27); changelog file updated (11); version field added to metadata (5); deprecation notice added (1)

### Subtheme: Description and naming

How the skill presents and names itself.

- Use when: the skill's name, description, tags or internal identifiers are reworded or renamed.
- Don't use when: the body text of docs changes (Documentation content) or a capability is actually added/removed.
- Pairs: 77 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 13 | 12 | 11 | 4 | 7 | 8 | 9 | 13
- Direction split (key points): added 1, modified 78
- Examples: `xueyetianya/discord-toolkit@2.0.1->3.0.0`, `waydelyle/swarmdock@2.5.3->2.6.0`
- Open codes (pairs): description rewritten (60); names or identifiers renamed (12); tags changed (7)

### Subtheme: Documentation content

Changes to explanatory docs, examples and links with no behavior change.

- Use when: explanatory text, examples, links or layout change and nothing the agent is told to do changes.
- Don't use when: the text changes agent steps (Feature and capability scope) or warns/limits the agent (Agent behavior guardrails).
- Pairs: 111 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 14 | 10 | 9 | 14 | 19 | 15 | 13 | 17
- Direction split (key points): added 54, removed 8, modified 61
- Examples: `13681882136/kami-image-search@1.0.4->1.0.5`, `talkstream/ru-text@1.6.0->1.8.0`
- Open codes (pairs): documentation content expanded (40); formatting-only changes (20); documentation files added (19); documentation condensed (9); doc link or path format changed (7); documentation translated (5); example content changed (4); content moved to reference files (3); example files added (3); tracking parameters added to links (3); capability claims corrected (3); documentation restructured (2); auto-generated content refreshed (2); troubleshooting guidance added (2); example URLs redacted (1)

## Theme: Package composition

Changes to which files ship in the package, including tests.

- Pairs: 53 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 6 | 9 | 6 | 7 | 8 | 5 | 7 | 5
- Direction split (key points): added 19, removed 37, modified 17

### Subtheme: Package file housekeeping

Adding, removing, renaming or swapping files in the package.

- Use when: files are added, deleted, renamed or swapped as files (manifests, licenses, old copies, configs).
- Don't use when: the deleted file removes a user-facing function (Feature and capability scope: capability removed).
- Pairs: 43 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 5 | 7 | 5 | 4 | 8 | 5 | 4 | 5
- Direction split (key points): added 12, removed 33, modified 15
- Examples: `almiashev/aidex@1.0.4->1.0.5`, `terrycarter1985/financial-report-automator@1.1.1->1.2.0`
- Open codes (pairs): documentation files removed (11); script file removed (8); package manifest added (7); files renamed or moved (7); bundled data file updated (6); config files removed (5); example or template files removed (4); package manifest removed (3); config files added (3); license changed (2); versioned script copies replaced (1); safety manifest file removed (1); license file removed (1); sub-skills consolidated into one SKILL.md (1)

### Subtheme: Testing assets

Tests and eval cases shipped with the skill.

- Use when: tests or eval cases are added, updated or removed.
- Don't use when: a script validates input at runtime (Code-level safety checks).
- Pairs: 13 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 1 | 4 | 1 | 4 | 0 | 0 | 3 | 0
- Direction split (key points): added 7, removed 4, modified 2
- Examples: `rijoyai/necessity-pain-point-selection@0.1.1->0.1.2`, `gilesdawe/tokei-agent@0.3.1->0.3.2`
- Open codes (pairs): tests or eval cases added (9); tests removed (4)

## Theme: Functional behavior

Changes to what the skill does and how its code does it.

- Pairs: 111 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 15 | 15 | 13 | 16 | 10 | 15 | 12 | 15
- Direction split (key points): added 85, removed 20, modified 48

### Subtheme: Feature and capability scope

What the skill can do: functions, flows, modes, interfaces.

- Use when: what the skill can do or the steps the agent follows change (new/removed functions, modes, commands, workflow).
- Don't use when: only the wording of docs changes, or the change is an internal code detail with the same behavior.
- Pairs: 82 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 11 | 9 | 9 | 14 | 5 | 11 | 11 | 12
- Direction split (key points): added 62, removed 11, modified 25
- Examples: `rnwy/rnwy@1.0.6->1.0.7`, `gilesdawe/tokei-agent@0.3.1->0.3.2`
- Open codes (pairs): new capability added (21); workflow instructions expanded (20); new scripts added (15); capability removed (8); CLI commands or arguments changed (7); default or config value changed (6); new API endpoints documented (5); operating modes added (3); workflow instructions reduced (3); default behavior narrowed (3); new sub-skill added (2); prompt templates changed (2); idle session auto-close added (1); automatic message capture added (1); default output verbosity reduced (1)

### Subtheme: Code implementation changes

Changes inside scripts that alter how code runs, not what the skill offers.

- Use when: script internals change: rewrites, fixes, refactors, engines, storage format/location, logging.
- Don't use when: the code change blocks unsafe input/paths/runs (Code-level safety checks).
- Pairs: 39 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 4 | 6 | 4 | 6 | 6 | 6 | 3 | 4
- Direction split (key points): added 23, removed 9, modified 23
- Examples: `ucsdzehualiu/smart-web-search@3.2.0->3.2.1`, `shalinda-j/llmcom-token-optimizer@1.0.0->1.0.1`
- Open codes (pairs): script logic extended (14); main script rewritten (8); bug fix in script logic (7); local logging removed (5); error handling added (4); underlying engine or library replaced (3); rate limiting added (3); script logic removed (2); code refactored without behavior change (2); data storage location changed (2); file write made atomic (2); subprocess call removed (1); data file format changed (1); dependency import changed to lazy loading (1)

## Theme: Dependencies and external reach

Changes to what the skill installs and what it reaches outside itself: network services, and other tools' local files or configs.

- Pairs: 62 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 12 | 12 | 5 | 4 | 6 | 8 | 7 | 8
- Direction split (key points): added 30, removed 13, modified 28

### Subtheme: Installation and dependencies

How the skill and its dependencies get installed, pinned or loaded.

- Use when: install steps, dependency lists, version pins or runtime installs change.
- Don't use when: a new external API is called at runtime (External services and endpoints).
- Pairs: 39 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 5 | 9 | 3 | 1 | 5 | 6 | 4 | 6
- Direction split (key points): added 18, removed 9, modified 20
- Examples: `jjmaxwell4/doorstep@1.0.1->1.0.2`, `waydelyle/swarmdock@2.5.3->2.6.0`
- Open codes (pairs): setup instructions changed (18); dependency version or source changed (11); dependency removed (4); dependency added (4); remote code run via npx (3); dependency version unpinned to latest (3); runtime dependency auto-install added (2); piped shell installer removed (1); runtime dependency auto-install removed (1)

### Subtheme: External services and endpoints

Which external services/URLs the skill talks to, or which other tools' local files or configs it reads.

- Use when: which third-party service or URL the skill calls or sends data to changes or is disclosed, or the skill reads another tool's local files or config (e.g. a token from another app's config file).
- Don't use when: the change is how a package is installed from a registry (Installation and dependencies).
- Pairs: 23 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 7 | 3 | 2 | 3 | 1 | 2 | 3 | 2
- Direction split (key points): added 12, removed 4, modified 8
- Examples: `sherrihidalgolt/og-image-skill@1.0.2->2.0.0`, `dylanfeltus/gui-new@1.0.0->1.0.1`
- Open codes (pairs): API endpoint or service URL changed (8); new external service integrated (5); external service dependency disclosed (5); external service integration removed (4); external result posting added (1); credential read from other app config (1)

## Theme: Configuration and declared requirements

Changes to credentials, config values and what the skill declares it needs.

- Pairs: 115 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 11 | 16 | 18 | 13 | 15 | 14 | 14 | 14
- Direction split (key points): added 77, removed 46, modified 17

### Subtheme: Credentials and configuration values

How credentials, env vars and config values are named, sourced, stored or embedded.

- Use when: how keys, env vars, paths or config values are named, sourced, stored, required or hardcoded changes.
- Don't use when: the change only lists requirements in metadata (Metadata declarations).
- Pairs: 46 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 7 | 9 | 4 | 5 | 6 | 7 | 5 | 3
- Direction split (key points): added 19, removed 20, modified 11
- Examples: `jjmaxwell4/doorstep@1.0.1->1.0.2`, `dylanfeltus/gui-new@1.0.0->1.0.1`
- Open codes (pairs): new env vars introduced (11); credential handling instructions changed (10); hardcoded local paths or addresses removed (7); env var usage removed (5); credential marked optional (4); API key value shipped in package (3); hardcoded local paths or addresses added (3); credential env var renamed (2); authentication method changed (2); plaintext credential storage removed (2); credential made required (1)

### Subtheme: Metadata declarations

What the skill declares in frontmatter/manifest about itself and its needs.

- Use when: frontmatter/manifest fields that declare requirements, permissions, install specs or other properties change.
- Don't use when: the description/name text changes (Description and naming).
- Pairs: 80 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 6 | 9 | 15 | 8 | 10 | 9 | 11 | 12
- Direction split (key points): added 58, removed 26, modified 6
- Examples: `jjmaxwell4/doorstep@1.0.1->1.0.2`, `sfkislev/flue@1.0.9->1.0.10`
- Open codes (pairs): requirements declared in metadata (32); metadata field added (19); requirements removed from metadata (14); metadata field removed (8); permissions declared in metadata (7); install spec added to metadata (3); frontmatter metadata added (3); metadata key renamed (2); install spec removed from metadata (1); frontmatter metadata removed (1)

## Theme: Safety controls and risk communication

Changes that constrain the agent or code, or that tell users about risk, access and data.

- Pairs: 75 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 8 | 7 | 9 | 13 | 10 | 7 | 8 | 13
- Direction split (key points): added 92, removed 14, modified 5

### Subtheme: Agent behavior guardrails

Instructions, or code that writes instructions, that constrain or direct what the agent may do or when it must stop/ask.

- Use when: the agent is told to ask, stop, stay read-only, follow hard rules, or actions are labelled by risk.
- Use when: code whose effect is to change what the agent is told to do (e.g. a script that writes a directive into a file the agent reads); classify by effect, not file type.
- Don't use when: the check is enforced in code (Code-level safety checks) or the text is advice to the human user (Safety and transparency guidance).
- Pairs: 24 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 6 | 1 | 2 | 5 | 4 | 1 | 2 | 3
- Direction split (key points): added 27, removed 2, modified 3
- Examples: `jjmaxwell4/doorstep@1.0.1->1.0.2`, `djc00p/rails-ci-fixer@1.1.4->1.2.0`
- Open codes (pairs): operational rules added (9); user confirmation required before actions (8); action risk tags changed (5); irreversible action warning added (3); warning notice removed (2); read-only default instructed (1); endpoint use restricted to documented ones (1); preflight check steps added (1); user choice prompt added (1); script writes directive for agent (1)

### Subtheme: Code-level safety checks

Checks added in code that block unsafe input, paths, connections or unconfirmed runs.

- Use when: code now refuses or neutralises unsafe input, paths, connections, output or unconfirmed runs.
- Don't use when: the protection is only stated in docs (Safety and transparency guidance) or only asked of the agent (Agent behavior guardrails).
- Pairs: 18 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 0 | 2 | 3 | 2 | 4 | 2 | 3 | 2
- Direction split (key points): added 20, removed 2
- Examples: `notasign/notasign@1.0.0->1.0.1`, `globalcaos/chatgpt-exporter-ultimate@1.9.1->1.9.2`
- Open codes (pairs): filesystem safety checks added (6); confirmation flag enforced in script (5); input validation added (4); safety check made optional (2); TLS verification enabled (1); sensitive content redaction added (1); output escaping added (1); download integrity check added (1); command allowlist added (1)

### Subtheme: Safety and transparency guidance

Advisory text for users about safe use and what the skill accesses.

- Use when: docs advise users on safe use, disclose access, make or remove safety claims, or soften warnings.
- Don't use when: the text instructs the agent's behavior (Agent behavior guardrails) or is about personal data (Personal data handling).
- Pairs: 40 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 4 | 3 | 5 | 7 | 6 | 3 | 4 | 8
- Direction split (key points): added 41, removed 8, modified 1
- Examples: `0xarkstar/notion-cli-mcp@1.0.0->1.1.0`, `simonvanlaak/kanban-workflow@0.1.9->0.1.10`
- Open codes (pairs): access scope disclosure expanded (13); safety or privacy claims added (12); credential safety guidance added (7); least-privilege guidance added (5); safety claims or disclosures removed (5); binary verification guidance added (2); risk warnings softened (2); least-privilege guidance removed (2); scanner findings response note added (1); security scan report added (1)

### Subtheme: Personal data handling

Personal data shipped, collected or minimised by the skill.

- Use when: personal data is shipped, collected less, or minimisation is advised.
- Don't use when: the data is a credential (Credentials and configuration values).
- Pairs: 6 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 1 | 1 | 1 | 0 | 0 | 1 | 0 | 2
- Direction split (key points): added 4, removed 2, modified 1
- Examples: `byungkyu/firecrawl-api@1.2.0->1.2.1`, `liangmoyuttc/moltoffer-candidate@1.0.2->1.0.3`
- Open codes (pairs): data minimization guidance added (3); personal data file added (2); personal data collection reduced (2)

## Theme: Monetization

Changes to the commercial side: prices, paid features, promotion and payment flows.

- Pairs: 14 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 3 | 2 | 1 | 1 | 1 | 2 | 4 | 0
- Direction split (key points): added 10, removed 2, modified 3

### Subtheme: Payments and monetization

Paid tiers, prices, upsells and payment flows.

- Use when: prices, paid tiers, upsells, donations, payment flows or payment methods change.
- Don't use when: an API key requirement changes without a payment angle (Credentials and configuration values).
- Pairs: 14 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 3 | 2 | 1 | 1 | 1 | 2 | 4 | 0
- Direction split (key points): added 10, removed 2, modified 3
- Examples: `kurosh87/aerobase-travel-flights@3.0.8->3.1.6`, `luiscosio/agentmetal@0.2.0->0.3.0`
- Open codes (pairs): pricing changed (5); autonomous payment flow added (3); new payment method support added (3); product promotion added (1); product promotion removed (1); paid feature section removed (1); donation request added (1)

## Theme: No change (bucket)

Pairs with no author change or no diff. Kept apart from the change themes.

- Pairs: 53 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 6 | 3 | 8 | 7 | 4 | 10 | 8 | 7
- Direction split (key points): n/a 53

### Subtheme: No change

Version published with no author file changes, or no diff available.

- Use when: the pair has no author file changes or no diff.
- Don't use when: any author change exists, even a version bump.
- Pairs: 53 overall; per round (01 | 02 | 03 | 04 | 05 | 06 | 07 | 08): 6 | 3 | 8 | 7 | 4 | 10 | 8 | 7
- Direction split (key points): n/a 53
- Examples: `dlazyai/dlazy-elevenlabs-dialogue@1.3.7->1.3.8`, `wjllance/standx-cli@0.4.7->0.4.8`
- Open codes (pairs): no author change (48); diff unavailable (5)

## Stated motives

69 of 400 pairs state a reason. Groups (a pair can be in more than one):

motive group | pairs
---|---
Respond to registry scanner or audit findings (incl. reducing false positives) | 17
Security hardening / prevent harm | 18
Fix a defect or improve reliability/compatibility/performance | 18
Registry or metadata compatibility | 5
Simplify setup or usage | 6
Consistency of formatting | 2
Accurate or honest description | 2
Discoverability and traffic tracking | 2
Product or business structure | 3

## Pair flags

changelog_mismatch: yes = changelog claims a specific change not in the diff; generic = changelog states no checkable change (release labels, auto-sync messages, vague wording, whole-skill feature summaries); no = claims match the diff, or only omit, or only concern skill-card.md/_meta.json.

round | mismatch yes | generic | no | no_author_change = yes
---|---|---|---|---
phase1_round01 | 8 | 8 | 34 | 6
phase1_round02 | 4 | 10 | 36 | 2
phase1_round03 | 6 | 10 | 34 | 8
phase1_round04 | 5 | 5 | 40 | 7
phase1_round05 | 9 | 4 | 37 | 4
phase1_round06 | 9 | 9 | 32 | 10
phase1_round07 | 4 | 13 | 33 | 7
phase1_round08 | 7 | 10 | 33 | 4
total | 52 | 69 | 279 | 48

Empty diff with a specific unmet claim (mismatch yes + no author change): 18 pairs.

## Coder decisions applied (2026-10-31)

- `credential read from other app config` moved from Credentials and configuration values to External services and endpoints (theme Dependencies and external reach). "External reach" now covers reading other tools' local files or configs, not only network calls.
- `script writes directive for agent` moved from Code implementation changes to Agent behavior guardrails. Code whose effect is to change what the agent is told to do is classified by effect, not file type.

## Open codes that did not fit any group well

Every code was placed in a subtheme, but these sit loosely where they are:

- `no author change`, `diff unavailable`: not changes. Kept in a separate "No change" bucket, not a theme.
- `prompt templates changed` (Feature and capability scope): prompt files are neither docs nor code.
- `sub-skills consolidated into one SKILL.md` (Package file housekeeping): a packaging change that also rewrote a lot of content.
- `license changed` (Package file housekeeping): a legal-terms change, not a file move. Only 1 pair.
- `tracking parameters added to links` (Documentation content): has a marketing/attribution purpose that also fits Monetization.
- `donation request added` (Payments and monetization): not a payment for the skill itself.
- `user choice prompt added` (Agent behavior guardrails): asks the user to pick a setup option; it is about UX more than limiting the agent.
- `security scan report added` (Safety and transparency guidance, new in R8): shipped scanner output as evidence; sits between a safety claim and a test asset.
- `safety check made optional` (Code-level safety checks, new in R7): one case is a config flag (signature `required: false`), the other an agent instruction (`check_merchant` optional). Both are loosening of an existing check.

## Subtheme saturation table (from saturation_log.md)

round | pairs coded | key points | new open codes | new codes % | new codes as created | new subthemes | codes renamed or merged | no author change | changelog mismatch (yes / generic / no)
---|---|---|---|---|---|---|---|---|---
phase1_round01 | 50 | 115 | 79 | 100.0% (79/79) | 77 (100.0%) | 13 | 18 merged into 9 | 6 | 8 / 8 / 34
phase1_round02 | 50 | 107 | 30 | 27.5% (30/109) | 29 (27.4%) | 2 (Testing assets; Personal data handling) | 7 renamed (widened); 2 subthemes renamed | 2 | 4 / 10 / 36
phase1_round03 | 50 | 97 | 15 | 12.1% (15/124) | 14 (11.7%) | 1 (Code-level safety checks) | 2 merged into 1; 1 renamed; 2 codes moved to new subtheme; 1 subtheme renamed | 8 | 6 / 10 / 34
phase1_round04 | 50 | 102 | 10 | 7.5% (10/134) | 11 (8.4%) | 0 | 2 renamed (widened) | 7 | 5 / 5 / 40
phase1_round05 | 50 | 112 | 4 | 2.9% (4/138) | 4 (3.0%) | 0 | 3 renamed (widened) | 4 | 9 / 4 / 37
phase1_round06 | 50 | 104 | 1 | 0.7% (1/139) | 1 (0.7%) | 0 | 0 | 10 | 9 / 9 / 32
phase1_round07 | 50 | 108 | 2 | 1.4% (2/141) | 3 (2.2%) | 0 | 0 | 7 | 4 / 13 / 33
phase1_round08 | 50 | 117 | 3 | 2.1% (3/144) | 5 (3.5%) | 0 | 2 renamed (widened) | 4 | 7 / 10 / 33

Saturation under the updated rule: rounds 5 and 6 are the first 2 rounds in a row that meet both conditions (0 new subthemes; new codes under 5% on both counts: 2.9%/3.0% and 0.7%/0.7%). Saturation reached at round 6. Round 4 fails the 5% test on both counts (7.5% after sweep, 8.4% as created).
(Under the earlier rule, no new subthemes only, it was reached at round 5.)
Rounds 7 and 8 are confirmation rounds.

Rounds 7 and 8 were coded as confirmation rounds after saturation. Both met the rule again. All new codes in these rounds fit existing subthemes; the 6-theme structure did not change. The consistency sweep moved 3 code first-uses earlier (to rounds 1-2) but did not change where saturation falls.

## Groupings I was unsure about

- **Six themes vs fewer.** "Package composition" and "Monetization" are small. Package composition could merge into Upkeep and presentation; Monetization could merge into Functional behavior. I kept them apart because their codes describe a different kind of change (which files ship; commercial terms).
- **Personal data handling** has only 3 codes and could fold into Safety and transparency guidance. I kept it because one of its codes (`personal data file added`) is not guidance but shipped data.
- **Metadata declarations vs Credentials and configuration values** share the same theme because many declarations are credential env vars. A coder could argue requirements in metadata are "Upkeep".
- **Code-level safety checks** was created in round 3 by moving `input validation added` (from Code implementation changes) and `confirmation flag enforced in script` (from Agent behavior guardrails). It sits in the safety theme, not in Functional behavior.
- **Installation and dependencies** and **External services and endpoints** are grouped as "external reach". `remote code run via npx` could go either way; I kept it under Installation.

- **Loosening vs tightening.** Several safety subthemes now hold both directions (e.g. `least-privilege guidance added/removed`, `safety or privacy claims added` vs `safety claims or disclosures removed`, `safety check made optional`). I kept direction inside the code rather than splitting "weakening" into its own subtheme, because it never formed a large group. Coders may want to test a separate "Safety loosened" subtheme.
- **Direction rule (added in session 4).** `modified` is kept only when a thing is reworded, swapped or retuned. If a change adds or removes a capability, requirement or safeguard, even inside a rewrite, it is `added` or `removed`. 34 key points moved (22 to added, 12 to removed). Kept as `modified`: like-for-like swaps (tool replaced by another tool, auth method A to B, engine replaced), version bumps, reworded descriptions (the real change is coded in its own key point), and narrowed defaults where the behavior is still available on request (`default behavior narrowed`).

## Boundaries that were hard to call

1. **Docs vs behavior for instruction-only skills.** For many skills SKILL.md is the program. I used `workflow instructions expanded/reduced` (Feature scope) when the steps the agent must follow changed, and `documentation content expanded` when only explanation/examples changed. Many key points were close.
2. **Agent guardrail vs user guidance.** "The agent MUST NOT write to ~/.ssh" is a guardrail; "use a least-privilege key" is user guidance. Some sections mix both.
3. **Guardrail in docs vs check in code.** The same idea (ask before overwrite/delete) appears as text (`user confirmation required before actions`) and as code (`confirmation flag enforced in script`). Coded by where it is enforced.
4. **Code fix vs safety check.** `error handling added`, `file write made atomic` and `rate limiting added` were kept in Code implementation changes; only checks that refuse unsafe input/paths/connections/output went to Code-level safety checks.
5. **Script file removed vs capability removed.** If deleting a script removed a user-facing function and the docs said so, I coded `capability removed`; otherwise `script file removed`.
6. **Safety claims vs access disclosure.** `safety or privacy claims added` = an assertion ("no data leaves the machine"); `access scope disclosure expanded` = describing what is accessed. Several new sections did both.
7. **changelog_mismatch.** Coded yes / generic / no (see the Pair flags section). Hardest calls: whole-skill feature summaries (coded generic) and display-name claims with empty diffs (kept yes). Claims about `skill-card.md` / `_meta.json` count as no.
8. **Version bumps.** Coded only when the version string is the only change (`version number bump only`). Version lines that change alongside other edits were not coded as separate key points.
