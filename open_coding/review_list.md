# Review list for the human coders

Source: `open_coding/open_codes.csv` (400 pairs, phase1_round01 to phase1_round08). Definitions and "use when / don't use when" lines are in `themes.md`. Pair ids are given as `slug@prev->version`; `kpN` is the key point number in `open_codes.csv`.

## 1. Every subtheme with 3 example key points

### Release status and bookkeeping (theme: Upkeep and presentation)
- `sullivangu/eva-ui-skill@1.0.0->1.0.1` kp1: **version field added to metadata** (added) - SKILL.md: `+version: 1.0.1`, "Current version" line; changelog-claimed VERSION file not in diff
- `oomol/oo-callrail@1.0.0->1.0.2` kp1: **version number bump only** (modified) - SKILL.md: version "1.0.0" -> "1.0.2"; changelog lists features with no matching diff
- `oomol/oo-googleforms@1.0.3->1.0.4` kp1: **version number bump only** (modified) - SKILL.md: version 1.0.3 -> 1.0.4, icon URL case change; changelog lists features with no matching diff

### Description and naming (theme: Upkeep and presentation)
- `xueyetianya/discord-toolkit@2.0.1->3.0.0` kp1: **description rewritten** (modified) - SKILL.md: description replaced with "Powered by BytesAgain"; command list removed
- `waydelyle/swarmdock@2.5.3->2.6.0` kp3: **tags changed** (modified) - SKILL.md: tag `mcp-server` added
- `probebuilders/rydberg-agent-node@2.5.0->2.5.1` kp1: **description rewritten** (modified) - SKILL.md: description reworded "Deploy a ProbeChain Rydberg testnet Agent node with one command..."

### Documentation content (theme: Upkeep and presentation)
- `13681882136/kami-image-search@1.0.4->1.0.5` kp1: **documentation content expanded** (added) - README.md: multi-camera config example and per-device commands
- `talkstream/ru-text@1.6.0->1.8.0` kp1: **doc link or path format changed** (modified) - SKILL.md: `${CLAUDE_PLUGIN_ROOT}/skills/ru-text/references/...` -> `references/...`
- `titus-choi/trunkate-ai@0.16.0->0.17.0` kp1: **formatting-only changes** (modified) - SKILL.md: table separator `|---|` -> `| --- |`

### Package file housekeeping (theme: Package composition)
- `almiashev/aidex@1.0.4->1.0.5` kp1: **bundled data file updated** (modified) - scripts/data/tokens.json (+694/-8): new token entries (trimmed)
- `terrycarter1985/financial-report-automator@1.1.1->1.2.0` kp2: **script file removed** (removed) - scripts/publish_report.py deleted (Feishu wiki publisher with app_id/app_secret)
- `oomol/oo-deepseek@1.0.0->1.0.1` kp1: **documentation files removed** (removed) - actions/*.md (4 files) deleted; descriptions inlined in SKILL.md

### Testing assets (theme: Package composition)
- `rijoyai/necessity-pain-point-selection@0.1.1->0.1.2` kp4: **tests or eval cases added** (added) - evals/evals.json (+26)
- `gilesdawe/tokei-agent@0.3.1->0.3.2` kp2: **tests or eval cases added** (added) - src/__tests__/commands.test.ts, mcp.test.ts: referrals:top tests
- `stephenredmond-straiteis/edge-tts-voice-system@2.0.0->2.1.0` kp4: **tests or eval cases added** (modified) - scripts/test_skill.py: checks edge-tts instead of piper

### Feature and capability scope (theme: Functional behavior)
- `rnwy/rnwy@1.0.6->1.0.7` kp1: **new capability added** (added) - SKILL.md: "Flow 8: Marketplace (ERC-8183 Jobs)" post/find/hire jobs (trimmed)
- `gilesdawe/tokei-agent@0.3.1->0.3.2` kp1: **new capability added** (added) - src/index.ts, src/mcp.ts: `referrals:top` CLI command and MCP tool (trimmed)
- `mcdoolz/openclaw-sulcus-skill@1.3.0->1.4.0` kp1: **capability removed** (removed) - SKILL.md: "Cloud Sync (Optional — Paid Add-on)" section and `webhook` action removed

### Code implementation changes (theme: Functional behavior)
- `ucsdzehualiu/smart-web-search@3.2.0->3.2.1` kp1: **dependency import changed to lazy loading** (modified) - scripts/search.js: static `import { chromium }` replaced by `await import('playwright')` in getBrowser()
- `shalinda-j/llmcom-token-optimizer@1.0.0->1.0.1` kp2: **main script rewritten** (modified) - optimizer.py (+262/-355): classifier/router replaced by LLMCOM converter (trimmed)
- `ericlooi504/ericlooi504-seo-audit@1.0.0->1.0.1` kp1: **script logic removed** (removed) - scripts/audit.py (-195), check.py (-81), report.py (-99): logic replaced by HELP text only

### Installation and dependencies (theme: Dependencies and external reach)
- `jjmaxwell4/doorstep@1.0.1->1.0.2` kp1: **setup instructions changed** (modified) - SKILL.md: hosted URL `https://trydoorstep.app/mcp` replaced by npx bridge as default; HTTP kept as alternative
- `waydelyle/swarmdock@2.5.3->2.6.0` kp1: **remote code run via npx** (added) - SKILL.md: "MCP server: `npx -y swarmdock-mcp`" recommended for MCP clients
- `claytantor/katbot-trading@0.1.4->0.1.5` kp1: **setup instructions changed** (modified) - SKILL.md: `uv pip install` -> `pip install`

### External services and endpoints (theme: Dependencies and external reach)
- `sherrihidalgolt/og-image-skill@1.0.2->2.0.0` kp1: **external service dependency disclosed** (added) - README.md: "Powered by the Neta AI image generation API"; requires a Neta API token
- `dylanfeltus/gui-new@1.0.0->1.0.1` kp1: **external service dependency disclosed** (added) - SKILL.md: "## Security Note: This skill sends HTML content to https://gui.new, a third-party hosted service... Do not send sensitive"
- `luduoxin/ai-leaderboard@1.2.0->1.3.0` kp2: **API endpoint or service URL changed** (modified) - SKILL.md: web_fetch of openrouter.ai pages -> `https://openrouter.ai/api/v1/models` via script

### Credentials and configuration values (theme: Configuration and declared requirements)
- `jjmaxwell4/doorstep@1.0.1->1.0.2` kp3: **authentication method changed** (modified) - SKILL.md: browser login replaced by DOORSTEP_API_KEY for default option
- `dylanfeltus/gui-new@1.0.0->1.0.1` kp2: **credential marked optional** (removed) - SKILL.md: "Pro API Key (optional)... No API key is needed for free tier"
- `fudanjx/notebooklm-pdf-cleaner@1.0.0->1.0.1` kp2: **hardcoded local paths or addresses removed** (removed) - SKILL.md: machine-specific paths replaced with portable skill paths (trimmed)

### Metadata declarations (theme: Configuration and declared requirements)
- `jjmaxwell4/doorstep@1.0.1->1.0.2` kp4: **requirements declared in metadata** (added) - SKILL.md + claw.json: `requires.env: DOORSTEP_API_KEY`, bins: node, primaryEnv
- `sfkislev/flue@1.0.9->1.0.10` kp1: **frontmatter metadata added** (added) - SKILL.md: new YAML front matter with name and description
- `xueyetianya/slack-automator@2.3.7->2.0.0` kp1: **metadata field added** (added) - SKILL.md: `homepage:` and `source:` added; changelog-claimed description and security fix not in diff

### Agent behavior guardrails (theme: Safety controls and risk communication)
- `jjmaxwell4/doorstep@1.0.1->1.0.2` kp5: **user choice prompt added** (added) - SKILL.md: "Before first use, ask the user how they want to connect"
- `djc00p/rails-ci-fixer@1.1.4->1.2.0` kp1: **user confirmation required before actions** (added) - SKILL.md: "NEVER auto-commit without human approval — pause and present changes"
- `oomol/oo-deepseek@1.0.0->1.0.1` kp2: **action risk tags changed** (added) - SKILL.md: actions carry `[write]` or `[destructive]` tags

### Code-level safety checks (theme: Safety controls and risk communication)
- `notasign/notasign@1.0.0->1.0.1` kp2: **input validation added** (added) - scripts/send_envelope.ts: SUPPORTED_FILE_EXTENSIONS set and MAX_FILE_SIZE_BYTES 100MB (trimmed)
- `globalcaos/chatgpt-exporter-ultimate@1.9.1->1.9.2` kp1: **filesystem safety checks added** (added) - SKILL.md/scripts/export-conversations.ts: O_CREAT/O_EXCL, O_NOFOLLOW, symlink/hard link refusal (trimmed)
- `crawlora-org/nike-research@1.0.10->1.0.11` kp1: **input validation added** (added) - scripts/crawlora.sh: reject `@` in query args

### Safety and transparency guidance (theme: Safety controls and risk communication)
- `0xarkstar/notion-cli-mcp@1.0.0->1.1.0` kp3: **least-privilege guidance added** (added) - SKILL.md: "Use the least-privilege scopes the workflow actually needs"; checksums referenced
- `simonvanlaak/kanban-workflow@0.1.9->0.1.10` kp1: **access scope disclosure expanded** (added) - SKILL.md/README: wrapper "calls Linear GraphQL over HTTPS using LINEAR_API_KEY"; ARCH_REVIEW auth boundary text
- `globalcaos/chatgpt-exporter-ultimate@1.9.1->1.9.2` kp4: **access scope disclosure expanded** (added) - SKILL.md: "Every claim is now scoped to the path that does it"; bookmarklet "CREDENTIALS: cookie only"

### Personal data handling (theme: Safety controls and risk communication)
- `byungkyu/firecrawl-api@1.2.0->1.2.1` kp3: **data minimization guidance added** (added) - SKILL.md: "Responses can carry personal data... extract just the fields"
- `liangmoyuttc/moltoffer-candidate@1.0.2->1.0.3` kp2: **personal data file added** (added) - persona.md: candidate name, email, phone number
- `sora-mury/openclaw-memory-kit@0.2.0->0.2.1` kp3: **data minimization guidance added** (added) - SKILL.md: "Never copy the source user's raw env file, live app IDs... private LAN addresses... Use placeholders only"

### Payments and monetization (theme: Monetization)
- `kurosh87/aerobase-travel-flights@3.0.8->3.1.6` kp1: **product promotion added** (added) - SKILL.md: "Pro Superpowers... Download Pro skills at https://aerobase.app/..."
- `luiscosio/agentmetal@0.2.0->0.3.0` kp1: **pricing changed** (modified) - SKILL.md: nano $0.40 -> $1.20/h, small $0.80 -> $2.20, medium $1.60 -> $4.20
- `nollio/normieclaw-dashboard-builder@1.0.0->1.0.2` kp2: **product promotion removed** (removed) - SKILL.md: list of other paid skills (Expense Report Pro, Budget Buddy Pro...) removed

### No change (theme: No change (bucket))
- `dlazyai/dlazy-elevenlabs-dialogue@1.3.7->1.3.8` kp1: **no author change** (n/a) - no files changed; changelog claims display name restored
- `wjllance/standx-cli@0.4.7->0.4.8` kp1: **no author change** (n/a) - no files changed; changelog claims display name fix
- `chrischall/ofw-fpx@2.13.0->2.14.0` kp1: **no author change** (n/a) - no files changed; changelog claims skill-card.md removed


## 2. Key points I was unsure about

### Coding of specific key points
- `utkarshthedev/lg-thinq-universal@0.1.2->0.1.3` (R1): only the "Sanitize ... for security" comments were removed; the sanitising code stayed. Not coded as a removal. The hardcoded API key default is coded `API key value shipped in package`.
- `xueyetianya/discord-toolkit@2.0.1->3.0.0` (R1) and `bytesagain-lab/arbitrage-finder@2.0.1->3.0.0` (R2): scripts rewritten into a generic "reference tool". Coded `main script rewritten` + `description rewritten`; could also be `capability removed`.
- `raydoomed/daily-introspection@1.0.2->1.0.3` (R2): changelog says "no changes" but a new function was added. Coded `script logic extended`, changelog_mismatch = no.
- `wxt-ai/export-confirmation-style-workbench@1.0.0->1.0.2` (R2): no diff (both versions not found). Coded `diff unavailable` from the changelog only.
- `liangmoyuttc/moltoffer-candidate@1.0.2->1.0.3` (R2): a credentials file with a real-looking API key and a persona file with a name, email and phone were added. Coded neutrally as `API key value shipped in package` and `personal data file added`.
- `waldyrious/workflowy@1.0.5->1.0.6` (R3): changelog says the "openclaw" metadata section was removed; the diff looks like reformatting only. Coded changelog_mismatch = no; may be "yes".
- `halfmoon82/brand-marketing-workflow@3.0.0->3.0.1` (R4): SKILL.md now says it is "documentation-only... contains no executable code" while 40+ code files were added. Coded `safety or privacy claims added` next to `new scripts added`.
- `capachow/lens@1.0.1->1.1.0` (R4): bootstrap.js writes a "CRITICAL INSTRUCTION ... you MUST read" block into YAML the agent reads. New code `script writes directive for agent`; coder decision (2026-10-31): placed in Agent behavior guardrails, classified by effect, not file type.
- `isdyh01/shortapi-ai-video-generation@1.0.1->1.0.2` (R4): the new Security & Privacy section was trimmed in my view; coded `access scope disclosure expanded`.
- `dlazyai/dlazy-wan2-6-r2v@1.0.3->1.0.4` (R4): `risk warnings softened` is an interpretive code (plaintext wording and "data leaves your machine" removed). Author's own motive: reduce false-positive scanner alerts.
- `jamesfincher/browserbase-sessions@1.2.2->2.4.0` (R5): install logic now uses break-system-packages outside a venv. Coded `runtime dependency auto-install added` (modified).
- `icepopma/linkedin-post-generator@1.0.6->1.0.7` (R5): merchant key moved from SKILL.md into a code default and the "payments go to the publisher" note removed. Coded `API key value shipped in package` + `safety claims or disclosures removed`.
- `medstatstar/statsoft-cli@2.6.7->2.6.8` (R5): removal of a trust-and-safety table row and a remote-run example coded as `documentation condensed`; could be `safety claims or disclosures removed`.
- `hmyaoyuan/anima@1.0.2->1.1.0` (R6): new debug script with an author path and a fixed Feishu recipient ID; coded `hardcoded local paths or addresses added`. Temp files committed coded as `bundled data file updated`.
- `kooui/aesthetic-scorer@1.4.5->1.4.6` (R6): scoring formula change coded `script logic extended` (modified); there is no code for "algorithm changed".
- `earlvanze/oauth-coder-bridge@1.0.0->1.1.0` (R6): large rewrite, trimmed. The default bind host 127.0.0.1 and the `/home/umbrel/...` default path were not coded because the old values were not visible.

### changelog_mismatch judgement calls (recoded to yes / generic / no)
Rule: **yes** = the changelog claims a specific change that is not in the diff; **generic** = the changelog states no checkable change (release labels such as "Release v1.9.16", auto-sync/publish messages, vague wording such as "Clean package" or "Quality upgrade", and whole-skill feature summaries); **no** = the claims match the diff, or the changelog only omits changes, or the only unmet claims are about `skill-card.md` / `_meta.json`. Totals: yes 52, generic 69, no 279. Every change from the earlier yes/no coding is listed in `coding_log.md`.
- **Feature summaries coded generic.** The `oomol/oo-*` changelogs (e.g. `oomol/oo-tinybird` R1, `oomol/oo-callrail` R2, `oomol/oo-deepseek` R3, `oomol/oo-taxjar` R4, `oomol/oo-brevo` R5, `oomol/oo-crisp` R6, `oomol/oo-opsgenie` R7, `oomol/oo-paymo` R8) describe the whole skill, not the version. They are now generic whether the diff is a version bump or a doc edit. Before, the version-only ones were "yes". This is the biggest judgement call.
- **skill-card.md / _meta.json claims now "no"** (27 pairs carried such a note, e.g. `fulcra/fulcra-dashboard` R1, `chrischall/ofw-fpx` R3, `chrischall/zola-mcp` R6). If a pair also claimed something else that was missing (e.g. `zmtucker/drivethru-operations` R8: "SKILL.md updated for clarity" but only the version line changed), it stayed "yes". `sahilaujla/alchemy-official` R3 ("Re-publish with clean metadata") was treated as a `_meta.json` claim and coded "no".
- **Display-name claims stay "yes"** (`dlazyai/*` pairs, `wjllance/standx-cli`, `mozz0/josh-learns`, `northcap-group/crypto-drt-scalping`). They are specific, and they are not about skill-card.md or _meta.json. If your coders think the display name lives only in the registry, recode them to "no".
- **Vague changelogs:** "Quality upgrade", "Final Quality & Bilingual Polishing", "yaml-fix+quality", "Clean package (with matching SKILL.md)", "Sync local updates", "test", "probe", "retry-fix-token", "Daily auto-update", "例行版本更新", "Re-publish with latest changes", "Initial release", "Publish ... v1.0.2", "Protocol standardization enhancements", "Batch: pricing through feedback" are all generic.
- **Diff unavailable:** the 5 pairs without a diff are generic when the changelog is an auto-sync message, and "no" for `viratkumar123/model-troubleshooter` R8 (a specific claim that cannot be checked). Coders may prefer a separate "not checkable" value.
- **"No changes" auto-summaries** that sit next to real changes (e.g. `raydoomed/daily-introspection` R2, `mineru-extract/mineru-document-extractor` R8) stay "no": they omit, they do not claim a missing change.

### Key points coded from trimmed diffs (see count in coding_log.md)
The diff was very long and only SKILL.md and changed scripts were read closely. These carry "(trimmed)" in `evidence`. Pairs: see `open_codes.csv` (filter `evidence` for "trimmed"). The largest were `rokkiezeng/mamp-memory` (R1), `senazeng/prism-gen-demo` (R2), `halfmoon82/brand-marketing-workflow` (R4), `vince-winkintel/gitlab-cli-skills` (R5) and `silbosu/vdoob` (R6).

### Rounds 7 and 8 (confirmation rounds)
- `aaigotchi/pet-me-master@2.0.2->2.1.0` (R7): script greps a Telegram bot token out of `~/.openclaw/openclaw.json` and sends to a fixed chat ID. New code `credential read from other app config` plus `hardcoded local paths or addresses added`. Coder decision (2026-10-31): code moved to External services and endpoints (theme Dependencies and external reach).
- `jonathanjing/glass2claw@1.2.0->1.3.0` (R7): mandatory "Least Privilege" and "Private Discord Server" rules softened to a recommendation. Coded `least-privilege guidance removed` + `risk warnings softened`; changelog calls it "streamlined".
- `xor777/magicpay@0.4.43->0.4.55` (R7) and `davida-ps/clawsec-suite@0.1.5->0.1.6` (R7): coded `safety check made optional` (merchant check now advisory; feed signature `required: false`). The magicpay diff is mostly trimmed.
- `googlarz/proactive-claw` appears twice: R7 (1.2.16->1.2.17) removed install/daemon disclosures from the description (`safety claims or disclosures removed`), R8 (1.2.17->1.2.18) put them back (`access scope disclosure expanded`).
- `drodecker/dcc-docker-container-control@0.1.0->1.0.1` (R8): the controller script was renamed to `.txt` and the "ask the user if the server is ambiguous" rule dropped. Coded `files renamed or moved` + `workflow instructions reduced`; the dropped rule could be read as a guardrail removal.
- `officialdelta/gmail-secretary@1.0.9->1.0.10` (R8): voice reference refreshed with real email excerpts naming a person and their school. Coded `personal data file added` (modified).
- `kaicianflone/consensus-publish-guard@1.1.8->1.1.9` (R8): a dependency switched to a local `file:../` path; coded under the widened `dependency version or source changed`.
- `mineru-extract/mineru-document-extractor@0.1.19->0.1.20` (R8): changelog says "no changes", but the metadata line with the privacy note and `allowed-tools` was removed. Coded `safety claims or disclosures removed` + `permissions declared in metadata` (removed); changelog_mismatch = no (omission, not a false claim).
- `deciqai/herzberg-two-factor@1.0.2->1.0.3` (R8): the changed footer line was cut off in my view; coded `doc link or path format changed` from the changelog's description.
- New codes in R7-R8 kept as separate codes (all inside existing subthemes): `credential read from other app config`, `documentation translated`, `safety check made optional`, `security scan report added`, `external service integration removed`, `download integrity check added`, `command allowlist added`, `config files added`.
- `documentation translated` was introduced in R7. Earlier translation cases (e.g. `openlark/xhs-suggest-keywords` R5) were coded as `description rewritten` / `workflow instructions expanded` and were not recoded.

## 3. Every rename and merge

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
Round 07: no renames or merges.
Round 08:
- "skill entry file renamed" -> "files renamed or moved" (R8 moved scripts and renamed sub-skill folders)
- "dependency version pinned or changed" -> "dependency version or source changed" (R8 switched a dependency from a registry version to a local path)

Consistency sweep (after round 08: codes created later applied to earlier key points):
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

### Subtheme moves (coder decisions, 2026-10-31)
- `credential read from other app config`: Credentials and configuration values -> External services and endpoints (theme Dependencies and external reach). External reach now includes reading other tools' local files or configs.
- `script writes directive for agent`: Code implementation changes -> Agent behavior guardrails. Classified by effect (changes what the agent is told to do), not file type.

## 4. Hardest boundaries

1. **Documentation content vs Feature and capability scope.** For instruction-only skills, SKILL.md is the behavior. Rule used: if the steps the agent must follow change, it is Feature scope (`workflow instructions expanded/reduced`); if only explanation or examples change, it is Documentation content.
2. **Agent behavior guardrails vs Safety and transparency guidance.** Rule used: text that tells the agent what it may or must do is a guardrail; advice to the human (least privilege, verify binaries) or disclosure is guidance.
3. **Agent behavior guardrails vs Code-level safety checks.** The same intent (confirm before a risky action) is coded by where it is enforced: in text (`user confirmation required before actions`) or in code (`confirmation flag enforced in script`).
4. **Code implementation changes vs Code-level safety checks.** Error handling, atomic writes and rate limiting stayed in Code implementation; only refusals of unsafe input, paths, TLS, unconfirmed runs, secrets in output, and unescaped output went to safety checks.
5. **Credentials and configuration values vs Metadata declarations.** Declaring an env var in frontmatter is Metadata; changing how the key is read, stored, required or hardcoded is Credentials.
6. **Package file housekeeping vs Feature scope.** Deleting a script is housekeeping unless it removed a user-facing function the docs mention (`capability removed`).
7. **changelog_mismatch yes vs generic** for whole-skill feature summaries and for display-name claims (see section 2).
8. **modified vs added/removed.** A rewrite that also adds or removes a capability, requirement or safeguard is coded `added` or `removed` (e.g. `credential marked optional` = removed, `safety check made optional` = removed, new health endpoints inside `main script rewritten` = added). Like-for-like swaps stay `modified`. Hardest calls: BytesAgain script swaps (kept modified, the lost functions are coded separately), `default behavior narrowed` (kept modified), `risk warnings softened` (only the mandatory-to-recommended case moved to removed).
