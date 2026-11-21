# Phase 2 coding summary

Codebook: `open_coding/themes.md` (frozen). Sample: `coding_rounds/phase2_sheet.csv`. Codes: `phase2_coding/phase2_codes.csv`.

This version reflects the full reread of every pair that had been read by scan (batches 1 to 11 of the reread, 272 pairs). See "Reading notes" below.

## Counts

item | n
---|---
pairs in sheet | 1300
excluded: no author change | 125
excluded: diff unavailable | 11
pairs coded (author changes present) | 1164
key points, all rows | 2776
key points, coded pairs only | 2640
key points per coded pair (mean) | 2.27
UNFIT key points | 0
low confidence key points | 3
partly read pairs | 19
pairs waiting for human coding | 0

"Pairs coded" means the 1164 pairs left after removing the 125 no-author-change pairs and the 11 diff-unavailable pairs from the 1300 in the sheet.

Pair-level counts below use the coded pairs only. A pair counts for a theme or subtheme if any of its key points has it, so columns sum to more than the pair total.

## Pairs per theme and subtheme

theme / subtheme | pairs | share of 1164 | key points | added | removed | modified
---|---|---|---|---|---|---
**Upkeep and presentation** | **599** | **51.5%** | **733** | 153 | 23 | 557
&nbsp;&nbsp;Documentation content | 357 | 30.7% | 379 | 139 | 23 | 217
&nbsp;&nbsp;Release status and bookkeeping | 197 | 16.9% | 198 | 10 | 0 | 188
&nbsp;&nbsp;Description and naming | 155 | 13.3% | 156 | 4 | 0 | 152
**Functional behavior** | **395** | **33.9%** | **534** | 288 | 71 | 175
&nbsp;&nbsp;Feature and capability scope | 323 | 27.7% | 408 | 263 | 68 | 77
&nbsp;&nbsp;Code implementation changes | 114 | 9.8% | 126 | 25 | 3 | 98
**Safety controls and risk communication** | **407** | **35.0%** | **543** | 351 | 93 | 99
&nbsp;&nbsp;Agent behavior guardrails | 205 | 17.6% | 223 | 148 | 25 | 50
&nbsp;&nbsp;Safety and transparency guidance | 142 | 12.2% | 148 | 103 | 25 | 20
&nbsp;&nbsp;Code-level safety checks | 99 | 8.5% | 108 | 72 | 16 | 20
&nbsp;&nbsp;Personal data handling | 64 | 5.5% | 64 | 28 | 27 | 9
**Configuration and declared requirements** | **339** | **29.1%** | **383** | 206 | 62 | 115
&nbsp;&nbsp;Metadata declarations | 228 | 19.6% | 232 | 142 | 25 | 65
&nbsp;&nbsp;Credentials and configuration values | 138 | 11.9% | 151 | 64 | 37 | 50
**Dependencies and external reach** | **232** | **19.9%** | **251** | 107 | 40 | 104
&nbsp;&nbsp;Installation and dependencies | 146 | 12.5% | 152 | 68 | 24 | 60
&nbsp;&nbsp;External services and endpoints | 97 | 8.3% | 99 | 39 | 16 | 44
**Package composition** | **134** | **11.5%** | **148** | 61 | 60 | 27
&nbsp;&nbsp;Package file housekeeping | 93 | 8.0% | 94 | 25 | 50 | 19
&nbsp;&nbsp;Testing assets | 54 | 4.6% | 54 | 36 | 10 | 8
**Monetization** | **48** | **4.1%** | **48** | 26 | 3 | 19
&nbsp;&nbsp;Payments and monetization | 48 | 4.1% | 48 | 26 | 3 | 19

## Direction split (key points, coded pairs)

direction | key points | share
---|---|---
added | 1192 | 45.2%
removed | 352 | 13.3%
modified | 1096 | 41.5%

## Flags

changelog_mismatch | all pairs | coded pairs | no author change pairs
---|---|---|---
yes | 77 | 52 | 25
generic | 175 | 114 | 61
no | 1037 | 998 | 39
n/a | 11 | 0 | 0

no_author_change = yes: 125 pairs. diff_unavailable = yes: 11 pairs (rows 570, 577, 595, 736, 839, 900, 1180, 1191, 1202, 1211, 1222).

Empty diff with a specific unmet claim (mismatch yes + no author change): 25 pairs.

Confidence (all key points): high 2501, medium 272, low 3

## Stated motive groups

222 of 1164 coded pairs state a reason. Groups follow the Phase 1 codebook list and are assigned by keyword match on the motive text (keyword lists in `phase2_coding/scripts/summary.py`), so a pair can be in more than one group.

motive group | pairs
---|---
Respond to registry scanner or audit findings (incl. reducing false positives) | 56
Security hardening / prevent harm | 112
Fix a defect or improve reliability/compatibility/performance | 77
Registry or metadata compatibility | 16
Simplify setup or usage | 15
Consistency of formatting | 4
Accurate or honest description | 17
Discoverability and traffic tracking | 13
Product or business structure | 2
Other (no group matched) | 4

Motives in Other:

- row 133 `tobewin/marketing-plan@1.0.2->1.0.3`: 清理测试文件 (clean up test files)
- row 193 `jenics/baidu-skill-guard@1.0.4->1.0.5`: no upload file
- row 840 `amandiwakar/ai-sentinel@0.1.8->0.2.1`: Disclose channel type
- row 889 `clamepending/videomemory@0.1.6->0.1.7`: Verify the pinned commit

## UNFIT key points

None.

## Low confidence key points

- row 211 `biociao/apm-agent-progressive-memory@1.3.2->1.4.0` kp 2: Agent behavior guardrails, "agent told to report last flush time after loading index". Note: small instruction inside the new layout
- row 235 `redwakame/openclaw-continuity@2.0.4->2.0.5` kp 3: Code implementation changes, "main script changed (not shown)". Note: script content not visible in the diff
- row 587 `voronindenis5/dashboard-generator@1.0.0->1.0.1` kp 1: Package file housekeeping, "examples, references and scripts folders added". Note: folder contents not in the diff

## Partly read pairs

Rules from CLAUDE.md: (a) single-file rule: one file's diff is over 3,000 lines, so its first 1,000 lines plus every SKILL.md and script hunk were read; (b) over-20,000 rule: the pair's total diff is over 20,000 lines, so SKILL.md in full, the complete file list, every added or changed script, entry point, manifest and config file, and a sample of the rest were read. Every other pair was read in full.

row | pair | rule | what was read
---|---|---|---
48 | `yun520-1/heartflow-skill@2.6.4->2.9.2` | over 20,000 (162,007 lines) | partly read: SKILL.md, file list, bin/, plugins/, scripts/, manifests read in full; 106 changed src/ scripts read as headers plus changed lines touching processes, files, network, env, eval; deleted files and docs/ sampled by name and size
132 | `virtualstechteam/virtuals-protocol-acp@1.0.0->1.0.1` | single file over 3,000 (pair 9,200 lines) | partly read: package-lock.json diff 3,361 lines, first 1,000 lines read; all other files read in full
180 | `zack-dev-cm/openclaw-agent-chinese-laoshi@1.0.10->1.0.11` | over 20,000 (24,315 lines) | partly read: very large pair, 24,315 lines; read SKILL.md, file list, all docs in full; 51 data JSON/MD files sampled and pattern-scanned, no URLs or commands
205 | `vannelier/deep-validator@2.0.15->2.0.16` | single file over 3,000 (pair 9,423 lines) | partly read: app/services/disposable_domains.txt diff 5,359 lines, first 1,000 lines read; all other deleted files read in full
272 | `shaike1/openclaw-skill-red-alert@1.0.1->1.1.0` | over 20,000 (20,793 lines) | partly read: very large pair, 20,793 lines; read SKILL.md, README, install.sh and oref_native.py in full, file list of ~170 deleted files
341 | `lkocaj/leadflow@1.0.2->1.0.3` | over 20,000 (20,705 lines) | partly read: very large pair; file list, README, changelog read; src pattern-scanned for endpoints, exec, env
351 | `p-diogo/totalreclaw@3.3.12-rc.23->3.3.12` | over 20,000 (122,094 lines) | partly read: very large pair, 122,094 lines; file list, SKILL.md, package.json, skill.json, tsconfig read; moved files compared line by line by script; new files pattern-scanned
433 | `nexecuteinc/cmdbcompass@1.0.3->1.0.4` | over 20,000 (81,268 lines) | partly read: very large pair; SKILL.md, file list, manifests and scripts/ read; rest pattern-scanned for secrets and endpoints
514 | `fanyadan/super-router@0.1.2->0.1.3` | single file over 3,000 (pair 6,622 lines) | partly read: router.py diff 3,531 lines, first 1,000 lines read; all other files (SKILL.md, README.md, references, render script, template, tests) read in full
626 | `alightttt/play-chess@1.0.13->1.0.14` | single file over 3,000 (pair 2,820 lines) | partly read: SKILL.md diff 3,047 lines; first 1,000 lines and every SKILL.md hunk read
664 | `mustbesimo/cinematic-scroll@2.5.5->2.6.9` | over 20,000 (22,173 lines) | partly read (very-large rule, 22,173 lines): SKILL.md, manifest, file list and all tools/ read; examples (~30 folders) and images sampled
721 | `cindulasai/clawshorts@1.0.0->1.0.1` | over 20,000 (44,322 lines) | partly read (very-large rule, 44,322 lines): SKILL.md, file list and all scripts/ and src/ hunks read; deleted folders sampled
762 | `dobrinalexandru/dual-memory@1.0.2->1.0.4` | single file over 3,000 (pair 7,781 lines) | partly read: package-lock.json diff is 7778 lines, first 1000 lines read (all entries resolve to registry.npmjs.org); composite-search-manager.ts read in full
789 | `matthiasbeckmann987-spec/beckmann-knowledge-graph@1.4.0->2.0.0` | single file over 3,000 (pair 9,739 lines) | partly read: "graph old.json" diff is 8526 lines (new file, copy of the v1.4 graph), first 1000 lines read; SKILL.md, graph.json (1509 lines: new game theory and cognitive bias entities, German `connection_to_base_graph` fields dropped), package.json and Readme.md read in full
820 | `vieiradiego/openclaw-aws-sre-report@1.0.0->1.0.1` | single file over 3,000 (pair 5,791 lines) | partly read: package-lock.json diff is 5523 lines (deleted), first 1000 lines read (all entries resolve to registry.npmjs.org); jest.config.js, tests/reporter.test.ts, tsconfig.json read in full
891 | `cchacons/openjobs@3.12.0->1.5.0` | single file over 3,000 (pair 3,948 lines) | partly read: SKILL.md diff is 3,127 lines; read its first 1,000 lines and every added line (all 466 additions), skipping only removed lines after line 1,000; HEARTBEAT.md and both scripts read in full
1018 | `apiclaw/amazon-opportunity-discoverer@1.0.1->1.0.4` | single file over 3,000 (pair 5,618 lines) | partly read: zoodata.py diff 3,165 lines; instead of a sample, the deleted scripts/apiclaw.py (2,348 lines) was compared to the added zoodata.py by script and every differing line (1,186 diff lines) was read; SKILL.md, README.md and references/reference.md read in full
1164 | `bruce-shi/massive-skill@1.0.2->1.0.3` | over 20,000 (20,932 lines) | partly read: over-20,000 rule; SKILL.md read in full, full file list, all eight references diffs read (only command-prefix changes), deleted cli.js sampled (lines 1-35, ~10,000, end with main/help)
1213 | `autogame-17/capability-evolver@1.53.2->1.88.4` | over 20,000 (68,042 lines) | partly read: total diff 68,042 changed lines over 327 files; SKILL.md, file list, package.json, index.js, README.md and every readable script read in full; tests, i18n and CSS tables, README translations sampled; obfuscated one-line files not readable

## Reading notes

- The first coding pass read mid-size pairs (over 250 changed lines) as the first 250 lines plus a scan. All 272 such pairs were reread in 11 batches of up to 25: every pair below the partly read thresholds was read in full, file by file in chunks. `read_mode` is `full` or `partly read` for every pair (`n/a` for the 11 diff-unavailable pairs). No row is left as "needs reread".
- Renamed or moved files that the diff shows as a full delete plus a full add were compared by script; all differing lines and one full copy were read (rows 537, 607, 679, 836, 1159, 1258, 1300).
- Row 827: the scanner snapshot pages inside that diff were left unread on purpose, because they are registry security review text and reading them would break blind coding.
- Row 6 (`batxent/rednote-contacts@1.0.0->1.0.1`) was stopped during the reread at line 1,453; on a later retry it was read in full (all 1,820 lines) and recoded, so `human_coding_list.csv` is now empty.
- Pairs whose codes changed in the reread are listed in `phase2_coding/reread_log.csv` (column `codes_changed`).
