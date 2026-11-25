# RQ2 labelling log (Phase 1)

RQ2 is labelling, not coding: each RQ1 key point gets one Extended Swanson category (Swanson 1976; Hindle et al. 2008).
Phase 1: 8 rounds, 400 pairs, 862 key points; 53 key points excluded (48 no author change, 5 no diff), 809 labelled across 347 pairs.

## How labels were assigned

1. Every RQ1 open code has a default category (table below), so the same code gets the same label in every round.
2. Codes marked *check* depend on purpose. For each of those key points the evidence, stated motive and changelog were read (and the diff where needed), and the default was kept or changed.
3. Each change from the default has its reason in `rq2_reason`; defaults say `default for '<code>'`.

## Rules applied

- Corrective needs a shown problem: a fix in the changelog that the diff agrees with, a stated failure (crash, 403s, wrong output), or a change made to address scanner or audit findings (ClawScan, SkillSpector, VirusTotal, registry warnings).
- Security fixes are Corrective. A safeguard with no shown problem is Perfective; one that comes with a new feature is Implementation.
- Docs by purpose: wrong claim corrected = Corrective; docs for a new feature = Implementation; rewording, translation, restructuring = Perfective.
- Tests and eval cases = Perfective. Bundled data updates = Adaptive (Hindle: data).
- Env vars, dependencies or companion skills added for a new feature = Implementation; otherwise Adaptive.
- Changes that follow an upstream service, CLI, platform or host = Adaptive.
- Several key points that make up one fix share its category (e.g. env vars that replace on-disk secrets).

## Poor fits to review (low confidence, 31 key points)

- Whole-skill swaps: a working tool replaced by a static reference tool ("Clean package", BytesAgain template) or scripts emptied. Labelled Perfective.
- Business-driven removals: features moved to a paid skill. Labelled Perfective.
- Promotion, cross-sell and donation requests; price changes. Labelled Non-functional.
- Scanner-driven wording: risk warnings softened or disclosures removed "to avoid false positives". Labelled Perfective, not Corrective, because nothing is fixed.
- Secrets or personal data added (hardcoded API keys, persona files, author's chat IDs or local paths). Labelled Adaptive; none of the five categories describes introducing a problem.
- Checks weakened (signature or merchant check made optional). Labelled Perfective.

## Default category per RQ1 open code

| RQ1 subtheme | open code | default | check | labelled | changed |
|---|---|---|---|---|---|
| Agent behavior guardrails | action risk tags changed | Perfective | yes | 5 | 2 |
| Agent behavior guardrails | endpoint use restricted to documented ones | Perfective | yes | 1 | 0 |
| Agent behavior guardrails | irreversible action warning added | Perfective | yes | 3 | 1 |
| Agent behavior guardrails | operational rules added | Perfective | yes | 9 | 3 |
| Agent behavior guardrails | preflight check steps added | Perfective | yes | 1 | 0 |
| Agent behavior guardrails | read-only default instructed | Perfective | yes | 1 | 0 |
| Agent behavior guardrails | script writes directive for agent | Implementation | yes | 1 | 0 |
| Agent behavior guardrails | user choice prompt added | Perfective | yes | 1 | 0 |
| Agent behavior guardrails | user confirmation required before actions | Perfective | yes | 8 | 1 |
| Agent behavior guardrails | warning notice removed | Perfective | yes | 2 | 1 |
| Code implementation changes | bug fix in script logic | Corrective | no | 7 | 0 |
| Code implementation changes | code refactored without behavior change | Perfective | no | 2 | 0 |
| Code implementation changes | data file format changed | Perfective | no | 1 | 0 |
| Code implementation changes | data storage location changed | Perfective | yes | 2 | 2 |
| Code implementation changes | dependency import changed to lazy loading | Perfective | no | 1 | 0 |
| Code implementation changes | error handling added | Perfective | yes | 4 | 3 |
| Code implementation changes | file write made atomic | Perfective | yes | 2 | 1 |
| Code implementation changes | local logging removed | Perfective | yes | 5 | 0 |
| Code implementation changes | main script rewritten | Perfective | yes | 8 | 6 |
| Code implementation changes | rate limiting added | Perfective | yes | 3 | 2 |
| Code implementation changes | script logic extended | Implementation | yes | 14 | 1 |
| Code implementation changes | script logic removed | Perfective | yes | 2 | 1 |
| Code implementation changes | subprocess call removed | Perfective | yes | 1 | 0 |
| Code implementation changes | underlying engine or library replaced | Adaptive | yes | 3 | 1 |
| Code-level safety checks | TLS verification enabled | Corrective | no | 1 | 0 |
| Code-level safety checks | command allowlist added | Perfective | yes | 1 | 0 |
| Code-level safety checks | confirmation flag enforced in script | Perfective | yes | 5 | 2 |
| Code-level safety checks | download integrity check added | Perfective | yes | 1 | 0 |
| Code-level safety checks | filesystem safety checks added | Perfective | yes | 6 | 3 |
| Code-level safety checks | input validation added | Perfective | yes | 4 | 2 |
| Code-level safety checks | output escaping added | Perfective | yes | 1 | 1 |
| Code-level safety checks | safety check made optional | Perfective | yes | 2 | 2 |
| Code-level safety checks | sensitive content redaction added | Perfective | yes | 1 | 0 |
| Credentials and configuration values | API key value shipped in package | Adaptive | yes | 3 | 3 |
| Credentials and configuration values | authentication method changed | Adaptive | yes | 2 | 0 |
| Credentials and configuration values | credential env var renamed | Non-functional | no | 2 | 0 |
| Credentials and configuration values | credential handling instructions changed | Perfective | yes | 10 | 4 |
| Credentials and configuration values | credential made required | Adaptive | no | 1 | 0 |
| Credentials and configuration values | credential marked optional | Adaptive | no | 4 | 0 |
| Credentials and configuration values | env var usage removed | Perfective | yes | 5 | 1 |
| Credentials and configuration values | hardcoded local paths or addresses added | Adaptive | yes | 3 | 3 |
| Credentials and configuration values | hardcoded local paths or addresses removed | Corrective | yes | 7 | 0 |
| Credentials and configuration values | new env vars introduced | Adaptive | yes | 11 | 6 |
| Credentials and configuration values | plaintext credential storage removed | Corrective | yes | 2 | 0 |
| Description and naming | description rewritten | Non-functional | yes | 60 | 3 |
| Description and naming | names or identifiers renamed | Non-functional | no | 12 | 0 |
| Description and naming | tags changed | Non-functional | no | 7 | 0 |
| Documentation content | auto-generated content refreshed | Non-functional | no | 2 | 0 |
| Documentation content | capability claims corrected | Corrective | no | 3 | 0 |
| Documentation content | content moved to reference files | Perfective | no | 3 | 0 |
| Documentation content | doc link or path format changed | Non-functional | no | 7 | 0 |
| Documentation content | documentation condensed | Perfective | no | 9 | 1 |
| Documentation content | documentation content expanded | Perfective | yes | 40 | 7 |
| Documentation content | documentation files added | Perfective | yes | 19 | 3 |
| Documentation content | documentation restructured | Perfective | no | 2 | 0 |
| Documentation content | documentation translated | Perfective | no | 5 | 0 |
| Documentation content | example URLs redacted | Perfective | yes | 1 | 1 |
| Documentation content | example content changed | Perfective | no | 4 | 0 |
| Documentation content | example files added | Perfective | no | 3 | 0 |
| Documentation content | formatting-only changes | Non-functional | no | 20 | 0 |
| Documentation content | tracking parameters added to links | Non-functional | no | 3 | 0 |
| Documentation content | troubleshooting guidance added | Perfective | no | 2 | 0 |
| External services and endpoints | API endpoint or service URL changed | Adaptive | yes | 8 | 3 |
| External services and endpoints | credential read from other app config | Implementation | yes | 1 | 0 |
| External services and endpoints | external result posting added | Implementation | no | 1 | 0 |
| External services and endpoints | external service dependency disclosed | Perfective | yes | 5 | 0 |
| External services and endpoints | external service integration removed | Perfective | yes | 4 | 1 |
| External services and endpoints | new external service integrated | Implementation | no | 5 | 0 |
| Feature and capability scope | CLI commands or arguments changed | Perfective | yes | 7 | 6 |
| Feature and capability scope | automatic message capture added | Implementation | no | 1 | 0 |
| Feature and capability scope | capability removed | Perfective | yes | 8 | 4 |
| Feature and capability scope | default behavior narrowed | Perfective | yes | 3 | 0 |
| Feature and capability scope | default or config value changed | Perfective | yes | 6 | 1 |
| Feature and capability scope | default output verbosity reduced | Perfective | no | 1 | 0 |
| Feature and capability scope | idle session auto-close added | Implementation | no | 1 | 0 |
| Feature and capability scope | new API endpoints documented | Implementation | no | 5 | 0 |
| Feature and capability scope | new capability added | Implementation | no | 21 | 0 |
| Feature and capability scope | new scripts added | Implementation | yes | 15 | 1 |
| Feature and capability scope | new sub-skill added | Implementation | no | 2 | 0 |
| Feature and capability scope | operating modes added | Implementation | no | 3 | 0 |
| Feature and capability scope | prompt templates changed | Perfective | no | 2 | 0 |
| Feature and capability scope | workflow instructions expanded | Implementation | yes | 20 | 3 |
| Feature and capability scope | workflow instructions reduced | Perfective | yes | 3 | 0 |
| Installation and dependencies | dependency added | Adaptive | yes | 4 | 2 |
| Installation and dependencies | dependency removed | Adaptive | yes | 4 | 2 |
| Installation and dependencies | dependency version or source changed | Adaptive | no | 11 | 0 |
| Installation and dependencies | dependency version unpinned to latest | Adaptive | no | 3 | 0 |
| Installation and dependencies | piped shell installer removed | Perfective | yes | 1 | 1 |
| Installation and dependencies | remote code run via npx | Adaptive | no | 3 | 0 |
| Installation and dependencies | runtime dependency auto-install added | Adaptive | no | 2 | 0 |
| Installation and dependencies | runtime dependency auto-install removed | Adaptive | yes | 1 | 0 |
| Installation and dependencies | setup instructions changed | Adaptive | yes | 18 | 1 |
| Metadata declarations | frontmatter metadata added | Adaptive | no | 3 | 0 |
| Metadata declarations | frontmatter metadata removed | Adaptive | no | 1 | 0 |
| Metadata declarations | install spec added to metadata | Adaptive | no | 3 | 0 |
| Metadata declarations | install spec removed from metadata | Adaptive | no | 1 | 0 |
| Metadata declarations | metadata field added | Adaptive | no | 19 | 1 |
| Metadata declarations | metadata field removed | Adaptive | no | 8 | 1 |
| Metadata declarations | metadata key renamed | Adaptive | no | 2 | 0 |
| Metadata declarations | permissions declared in metadata | Adaptive | yes | 7 | 3 |
| Metadata declarations | requirements declared in metadata | Adaptive | yes | 32 | 10 |
| Metadata declarations | requirements removed from metadata | Adaptive | yes | 14 | 3 |
| Package file housekeeping | bundled data file updated | Adaptive | yes | 6 | 2 |
| Package file housekeeping | config files added | Adaptive | yes | 3 | 0 |
| Package file housekeeping | config files removed | Perfective | no | 5 | 1 |
| Package file housekeeping | documentation files removed | Perfective | no | 11 | 0 |
| Package file housekeeping | example or template files removed | Perfective | no | 4 | 0 |
| Package file housekeeping | files renamed or moved | Non-functional | no | 7 | 0 |
| Package file housekeeping | license changed | Non-functional | no | 2 | 0 |
| Package file housekeeping | license file removed | Non-functional | no | 1 | 0 |
| Package file housekeeping | package manifest added | Adaptive | no | 7 | 0 |
| Package file housekeeping | package manifest removed | Adaptive | no | 3 | 0 |
| Package file housekeeping | safety manifest file removed | Perfective | yes | 1 | 1 |
| Package file housekeeping | script file removed | Perfective | yes | 8 | 1 |
| Package file housekeeping | sub-skills consolidated into one SKILL.md | Perfective | yes | 1 | 1 |
| Package file housekeeping | versioned script copies replaced | Perfective | no | 1 | 0 |
| Payments and monetization | autonomous payment flow added | Implementation | no | 3 | 0 |
| Payments and monetization | donation request added | Implementation | yes | 1 | 1 |
| Payments and monetization | new payment method support added | Implementation | no | 3 | 0 |
| Payments and monetization | paid feature section removed | Perfective | yes | 1 | 0 |
| Payments and monetization | pricing changed | Non-functional | no | 5 | 0 |
| Payments and monetization | product promotion added | Non-functional | yes | 1 | 1 |
| Payments and monetization | product promotion removed | Non-functional | yes | 1 | 1 |
| Personal data handling | data minimization guidance added | Perfective | yes | 3 | 1 |
| Personal data handling | personal data collection reduced | Perfective | yes | 2 | 0 |
| Personal data handling | personal data file added | Adaptive | yes | 2 | 2 |
| Release status and bookkeeping | changelog file updated | Non-functional | no | 11 | 0 |
| Release status and bookkeeping | deprecation notice added | Perfective | yes | 1 | 1 |
| Release status and bookkeeping | version field added to metadata | Non-functional | no | 5 | 0 |
| Release status and bookkeeping | version number bump only | Non-functional | no | 27 | 0 |
| Safety and transparency guidance | access scope disclosure expanded | Perfective | yes | 13 | 5 |
| Safety and transparency guidance | binary verification guidance added | Perfective | yes | 2 | 0 |
| Safety and transparency guidance | credential safety guidance added | Perfective | yes | 7 | 2 |
| Safety and transparency guidance | least-privilege guidance added | Perfective | yes | 5 | 1 |
| Safety and transparency guidance | least-privilege guidance removed | Perfective | yes | 2 | 1 |
| Safety and transparency guidance | risk warnings softened | Perfective | yes | 2 | 1 |
| Safety and transparency guidance | safety claims or disclosures removed | Perfective | yes | 5 | 1 |
| Safety and transparency guidance | safety or privacy claims added | Perfective | yes | 12 | 4 |
| Safety and transparency guidance | scanner findings response note added | Corrective | no | 1 | 0 |
| Safety and transparency guidance | security scan report added | Perfective | yes | 1 | 1 |
| Testing assets | tests or eval cases added | Perfective | no | 9 | 0 |
| Testing assets | tests removed | Perfective | no | 4 | 1 |
