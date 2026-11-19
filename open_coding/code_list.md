# Code list

144 distinct open codes, 862 key points, 400 pairs.

Counts are number of pairs. Version bumps are only coded when they are the only change.

| open code | definition | first round | pairs |
|---|---|---|---|
| operational rules added | Hard do/don't rules for how the agent produces output or config. | 01 | 9 |
| user confirmation required before actions | Agent told to get explicit user approval before certain actions. | 01 | 8 |
| action risk tags changed | Risk labels on actions (e.g. [write], [destructive]) added or changed in docs. | 03 | 5 |
| irreversible action warning added | Warning that an action cannot be undone added. | 01 | 3 |
| warning notice removed | A caution/status warning removed from docs. | 01 | 2 |
| endpoint use restricted to documented ones | Agent told to only use documented endpoints/paths. | 01 | 1 |
| preflight check steps added | Agent told to run checks before acting. | 01 | 1 |
| read-only default instructed | Agent told to default to read-only operations. | 01 | 1 |
| script writes directive for agent | Code writes instruction text meant for the agent into files it will read. | 04 | 1 |
| user choice prompt added | Agent told to ask the user to pick an option before setup/use. | 01 | 1 |
| script logic extended | New function or logic added inside an existing script. | 02 | 14 |
| main script rewritten | The main script was largely replaced or restructured. | 01 | 8 |
| bug fix in script logic | A specific defect in script logic corrected. | 02 | 7 |
| local logging removed | Code writing local logs/history removed. | 01 | 5 |
| error handling added | try/except or fallback logic added for a failure case. | 01 | 4 |
| rate limiting added | Delays or limits between external calls added in code. | 01 | 3 |
| underlying engine or library replaced | The main library/engine the skill uses swapped for another. | 03 | 3 |
| code refactored without behavior change | Module system or structure changed with same behavior. | 03 | 2 |
| data storage location changed | Where the skill stores state/data on disk changed. | 04 | 2 |
| file write made atomic | File writes changed to temp-file-and-rename. | 01 | 2 |
| script logic removed | Script bodies emptied or reduced to help text; logic left to the agent. | 03 | 2 |
| data file format changed | Format of files the skill reads/writes changed (e.g. md to yaml). | 04 | 1 |
| dependency import changed to lazy loading | Imports moved from module load to call time. | 01 | 1 |
| subprocess call removed | Spawning a child process replaced by in-process call. | 03 | 1 |
| filesystem safety checks added | Code checks against path traversal, symlinks or unsafe file creation added. | 03 | 6 |
| confirmation flag enforced in script | Code refuses to run a risky operation without an explicit flag/argument. | 02 | 5 |
| input validation added | Checks on input type/size/format added in code. | 02 | 4 |
| safety check made optional | A verification/vetting check that was required is now optional or advisory. | 07 | 2 |
| TLS verification enabled | Disabled certificate verification turned back on. | 03 | 1 |
| command allowlist added | Code restricts which subcommands may run via an allowlist. | 08 | 1 |
| download integrity check added | Code verifies a checksum/signature of something it downloads. | 08 | 1 |
| output escaping added | Generated output escaped to prevent injection. | 05 | 1 |
| sensitive content redaction added | Code strips secrets/system prompts before sending content out. | 05 | 1 |
| new env vars introduced | New environment variables read by the skill. | 01 | 11 |
| credential handling instructions changed | Where/how credentials are stored or entered changed in docs. | 02 | 10 |
| hardcoded local paths or addresses removed | Author- or environment-specific absolute paths, IPs or proxies removed. | 01 | 7 |
| env var usage removed | Skill stops reading some environment variables. | 01 | 5 |
| credential marked optional | A credential previously required is now documented as optional. | 01 | 4 |
| API key value shipped in package | A literal API key value placed in code, docs or a shipped file. | 01 | 3 |
| hardcoded local paths or addresses added | Author- or environment-specific absolute paths, IPs or fixed recipient IDs added. | 06 | 3 |
| authentication method changed | Way the skill authenticates to a service changed. | 01 | 2 |
| credential env var renamed | Name of the credential environment variable changed. | 01 | 2 |
| plaintext credential storage removed | Instructions/code writing tokens to plaintext files removed. | 02 | 2 |
| credential made required | A credential previously optional is now required. | 04 | 1 |
| description rewritten | The skill name/description text in frontmatter or header was reworded or replaced. | 01 | 60 |
| names or identifiers renamed | Internal names, markers or references to other skills were renamed. | 01 | 12 |
| tags changed | Tags or keywords in metadata were added, removed or replaced. | 01 | 7 |
| documentation content expanded | New explanatory text, examples, scenarios or reference guidance added to existing docs. | 01 | 40 |
| formatting-only changes | Layout/whitespace/line-wrap/syntax-style changes with no content change. | 01 | 20 |
| documentation files added | New README, reference or other doc files added to the package. | 01 | 19 |
| documentation condensed | Explanatory or reference text removed or shortened. | 01 | 9 |
| doc link or path format changed | Doc links or file references switched between relative paths, variables and absolute URLs. | 01 | 7 |
| documentation translated | Docs translated into another language. | 02 | 5 |
| example content changed | Values or wording inside examples changed. | 01 | 4 |
| capability claims corrected | Docs corrected to state what the skill does and does not actually do. | 01 | 3 |
| content moved to reference files | Content moved out of SKILL.md into separate reference files. | 01 | 3 |
| example files added | New example input/output files added. | 01 | 3 |
| tracking parameters added to links | UTM or referral parameters added to links. | 02 | 3 |
| auto-generated content refreshed | Generated data in docs (counts, link lists) refreshed. | 03 | 2 |
| documentation restructured | Docs reorganised (sections, headings, layout) without new content. | 02 | 2 |
| troubleshooting guidance added | Error handling advice for the agent/user added to docs. | 01 | 2 |
| example URLs redacted | Concrete URLs/hosts in examples replaced by placeholders. | 01 | 1 |
| API endpoint or service URL changed | Base URL, endpoint path or service domain changed. | 01 | 8 |
| external service dependency disclosed | Docs now state which external service the skill relies on or sends data to. | 01 | 5 |
| new external service integrated | Skill now calls a third-party service/API it did not use before. | 01 | 5 |
| external service integration removed | Skill stops calling a third-party service it used before. | 02 | 4 |
| credential read from other app config | Code reads a secret out of another tool's config file. | 07 | 1 |
| external result posting added | Code that sends results to an external endpoint added. | 01 | 1 |
| new capability added | Skill gains a new user-facing function, flow or supported platform. | 01 | 21 |
| workflow instructions expanded | Step-by-step agent workflow made longer or more detailed. | 01 | 20 |
| new scripts added | New executable script files added. | 01 | 15 |
| capability removed | A user-facing function retired or removed. | 02 | 8 |
| CLI commands or arguments changed | Command names or how arguments are passed to a script/CLI changed. | 01 | 7 |
| default or config value changed | A default value in a script or shipped config template changed. | 01 | 6 |
| new API endpoints documented | Additional API endpoints or parameters documented for use. | 01 | 5 |
| default behavior narrowed | Default behavior made narrower/opt-in; extra steps only on request. | 03 | 3 |
| operating modes added | Selectable runtime modes introduced. | 01 | 3 |
| workflow instructions reduced | Steps or behaviors removed from the agent workflow. | 02 | 3 |
| new sub-skill added | A nested skill (its own SKILL.md) added inside the package. | 01 | 2 |
| prompt templates changed | Prompt files the agent follows were reworded. | 04 | 2 |
| automatic message capture added | Code that hooks into the agent to record messages automatically added. | 01 | 1 |
| default output verbosity reduced | Default output made shorter/less detailed. | 01 | 1 |
| idle session auto-close added | Code that closes idle sessions automatically added. | 01 | 1 |
| setup instructions changed | Install/connection/setup steps rewritten or reorganised. | 01 | 18 |
| dependency version or source changed | Install commands pin a dependency version, move the pin, or change where it comes from. | 02 | 11 |
| dependency added | A new dependency (package or other skill) added. | 02 | 4 |
| dependency removed | A dependency removed from requirements/manifest/imports. | 01 | 4 |
| dependency version unpinned to latest | A pinned dependency version replaced by @latest. | 02 | 3 |
| remote code run via npx | Instructions now run remote code via npx/tsx from a URL or registry. | 01 | 3 |
| runtime dependency auto-install added | Skill now installs or fetches a runtime/package on the fly. | 02 | 2 |
| piped shell installer removed | curl|sh style install instructions removed. | 01 | 1 |
| runtime dependency auto-install removed | Code that installed packages at runtime removed. | 01 | 1 |
| requirements declared in metadata | Env vars or binaries the skill needs listed in frontmatter/manifest requires. | 01 | 32 |
| metadata field added | A new non-requirement metadata field added (homepage, endpoints, etc.). | 02 | 19 |
| requirements removed from metadata | Env var or binary requirements dropped from frontmatter/manifest. | 01 | 14 |
| metadata field removed | A non-install frontmatter field removed. | 01 | 8 |
| permissions declared in metadata | Permissions (exec/network/env) declared in metadata. | 01 | 7 |
| frontmatter metadata added | YAML frontmatter block added to SKILL.md where none existed. | 02 | 3 |
| install spec added to metadata | Install entries added to metadata. | 04 | 3 |
| metadata key renamed | A metadata key renamed to match the expected schema. | 02 | 2 |
| frontmatter metadata removed | YAML frontmatter block removed from SKILL.md. | 03 | 1 |
| install spec removed from metadata | Install entries removed from metadata. | 01 | 1 |
| no author change | Diff contains no author-made file changes. | 01 | 48 |
| diff unavailable | No diff could be built (diff_status not ok); coded from changelog only. | 02 | 5 |
| documentation files removed | README, reference or other doc files deleted. | 02 | 11 |
| script file removed | One or more script files deleted from the package. | 02 | 8 |
| files renamed or moved | SKILL.md or other package files renamed or moved to another path. | 02 | 7 |
| package manifest added | A package.json or similar manifest added. | 01 | 7 |
| bundled data file updated | A data file shipped with the skill was changed, added or removed. | 01 | 6 |
| config files removed | Config files (repo, CI or runtime config) deleted. | 01 | 5 |
| example or template files removed | Example, template or sample files deleted from the package. | 01 | 4 |
| config files added | Config or ignore files (e.g. .gitignore, .clawhubignore) added. | 04 | 3 |
| package manifest removed | A package/registry manifest file deleted. | 03 | 3 |
| license changed | License terms replaced. | 03 | 2 |
| license file removed | LICENSE file deleted. | 02 | 1 |
| safety manifest file removed | A file asserting the package is safe (e.g. .clawhubsafe) deleted. | 01 | 1 |
| sub-skills consolidated into one SKILL.md | Many nested skills merged into a single SKILL.md. | 05 | 1 |
| versioned script copies replaced | Old version-named copies of scripts swapped for newer version-named copies. | 01 | 1 |
| pricing changed | Prices of the service changed. | 02 | 5 |
| autonomous payment flow added | Agent told to pay for the service automatically. | 02 | 3 |
| new payment method support added | New currencies, chains or payment protocols supported. | 01 | 3 |
| donation request added | Request for tips/donations added. | 05 | 1 |
| paid feature section removed | Section describing a paid feature removed. | 01 | 1 |
| product promotion added | Promotion of a paid tier, upsell or other products added. | 01 | 1 |
| product promotion removed | Promotion of paid tiers or other products removed. | 03 | 1 |
| data minimization guidance added | Advice to limit personal data in outputs added. | 01 | 3 |
| personal data collection reduced | Skill stops collecting some personal attributes. | 02 | 2 |
| personal data file added | A file containing a real person's personal details added. | 02 | 2 |
| version number bump only | Only the version string changed. | 01 | 27 |
| changelog file updated | A CHANGELOG file in the package got a new entry. | 01 | 11 |
| version field added to metadata | A version field or version line was added where none existed. | 01 | 5 |
| deprecation notice added | Skill marked deprecated and users redirected. | 03 | 1 |
| access scope disclosure expanded | Docs disclose more fully what the skill can access or call. | 01 | 13 |
| safety or privacy claims added | Docs assert protections or that no data leaves the machine. | 03 | 12 |
| credential safety guidance added | Advice on handling credentials safely added. | 01 | 7 |
| least-privilege guidance added | Advice to use minimal scopes/accounts/keys added. | 01 | 5 |
| safety claims or disclosures removed | Statements about safety, or disclosures of behavior, removed. | 04 | 5 |
| binary verification guidance added | Advice to verify downloaded binaries (checksums, official sources) added. | 01 | 2 |
| least-privilege guidance removed | Advice to use minimal scopes/keys removed. | 04 | 2 |
| risk warnings softened | Warnings about data/credential risk reworded to sound less alarming. | 04 | 2 |
| scanner findings response note added | Author note answering registry scanner findings. | 02 | 1 |
| security scan report added | Output of a security scanner shipped in the package as evidence. | 08 | 1 |
| tests or eval cases added | Code tests or eval prompts added or updated. | 01 | 9 |
| tests removed | Test files deleted. | 02 | 4 |

## Provisional grouping into subthemes

### Release status and bookkeeping (44 pairs, first round 01)
Changes that only record versions, release notes or lifecycle status.

Codes: version number bump only (27); changelog file updated (11); version field added to metadata (5); deprecation notice added (1)

### Description and naming (77 pairs, first round 01)
How the skill presents and names itself.

Codes: description rewritten (60); names or identifiers renamed (12); tags changed (7)

### Documentation content (111 pairs, first round 01)
Changes to explanatory docs, examples and links with no behavior change.

Codes: documentation content expanded (40); formatting-only changes (20); documentation files added (19); documentation condensed (9); doc link or path format changed (7); documentation translated (5); example content changed (4); content moved to reference files (3); example files added (3); tracking parameters added to links (3); capability claims corrected (3); documentation restructured (2); auto-generated content refreshed (2); troubleshooting guidance added (2); example URLs redacted (1)

### Package file housekeeping (43 pairs, first round 01)
Adding, removing, renaming or swapping files in the package.

Codes: documentation files removed (11); script file removed (8); package manifest added (7); files renamed or moved (7); bundled data file updated (6); config files removed (5); example or template files removed (4); package manifest removed (3); config files added (3); license changed (2); versioned script copies replaced (1); safety manifest file removed (1); license file removed (1); sub-skills consolidated into one SKILL.md (1)

### Feature and capability scope (82 pairs, first round 01)
What the skill can do: functions, flows, modes, interfaces.

Codes: new capability added (21); workflow instructions expanded (20); new scripts added (15); capability removed (8); CLI commands or arguments changed (7); default or config value changed (6); new API endpoints documented (5); operating modes added (3); workflow instructions reduced (3); default behavior narrowed (3); new sub-skill added (2); prompt templates changed (2); idle session auto-close added (1); automatic message capture added (1); default output verbosity reduced (1)

### Testing assets (13 pairs, first round 02)
Tests and eval cases shipped with the skill.

Codes: tests or eval cases added (9); tests removed (4)

### Code implementation changes (39 pairs, first round 01)
Changes inside scripts that alter how code runs, not what the skill offers.

Codes: script logic extended (14); main script rewritten (8); bug fix in script logic (7); local logging removed (5); error handling added (4); underlying engine or library replaced (3); rate limiting added (3); script logic removed (2); code refactored without behavior change (2); data storage location changed (2); file write made atomic (2); subprocess call removed (1); data file format changed (1); dependency import changed to lazy loading (1)

### External services and endpoints (23 pairs, first round 01)
Which external services/URLs the skill talks to, or which other tools' local files or configs it reads.

Codes: API endpoint or service URL changed (8); new external service integrated (5); external service dependency disclosed (5); external service integration removed (4); external result posting added (1); credential read from other app config (1)

### Code-level safety checks (18 pairs, first round 03)
Checks added in code that block unsafe input, paths, connections or unconfirmed runs.

Codes: filesystem safety checks added (6); confirmation flag enforced in script (5); input validation added (4); safety check made optional (2); TLS verification enabled (1); sensitive content redaction added (1); output escaping added (1); download integrity check added (1); command allowlist added (1)

### Credentials and configuration values (46 pairs, first round 01)
How credentials, env vars and config values are named, sourced, stored or embedded.

Codes: new env vars introduced (11); credential handling instructions changed (10); hardcoded local paths or addresses removed (7); env var usage removed (5); credential marked optional (4); API key value shipped in package (3); hardcoded local paths or addresses added (3); credential env var renamed (2); authentication method changed (2); plaintext credential storage removed (2); credential made required (1)

### Metadata declarations (80 pairs, first round 01)
What the skill declares in frontmatter/manifest about itself and its needs.

Codes: requirements declared in metadata (32); metadata field added (19); requirements removed from metadata (14); metadata field removed (8); permissions declared in metadata (7); install spec added to metadata (3); frontmatter metadata added (3); metadata key renamed (2); install spec removed from metadata (1); frontmatter metadata removed (1)

### Installation and dependencies (39 pairs, first round 01)
How the skill and its dependencies get installed, pinned or loaded.

Codes: setup instructions changed (18); dependency version or source changed (11); dependency removed (4); dependency added (4); remote code run via npx (3); dependency version unpinned to latest (3); runtime dependency auto-install added (2); piped shell installer removed (1); runtime dependency auto-install removed (1)

### Agent behavior guardrails (24 pairs, first round 01)
Instructions, or code that writes instructions, that constrain or direct what the agent may do or when it must stop/ask.

Codes: operational rules added (9); user confirmation required before actions (8); action risk tags changed (5); irreversible action warning added (3); warning notice removed (2); read-only default instructed (1); endpoint use restricted to documented ones (1); preflight check steps added (1); user choice prompt added (1); script writes directive for agent (1)

### Safety and transparency guidance (40 pairs, first round 01)
Advisory text for users about safe use and what the skill accesses.

Codes: access scope disclosure expanded (13); safety or privacy claims added (12); credential safety guidance added (7); least-privilege guidance added (5); safety claims or disclosures removed (5); binary verification guidance added (2); risk warnings softened (2); least-privilege guidance removed (2); scanner findings response note added (1); security scan report added (1)

### Personal data handling (6 pairs, first round 02)
Personal data shipped, collected or minimised by the skill.

Codes: data minimization guidance added (3); personal data file added (2); personal data collection reduced (2)

### Payments and monetization (14 pairs, first round 01)
Paid tiers, prices, upsells and payment flows.

Codes: pricing changed (5); autonomous payment flow added (3); new payment method support added (3); product promotion added (1); product promotion removed (1); paid feature section removed (1); donation request added (1)

### No change (53 pairs, first round 01)
Version published with no author file changes, or no diff available.

Codes: no author change (48); diff unavailable (5)

## Renames and merges

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

