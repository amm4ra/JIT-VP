# RQ2 labelling log (Phase 2)

Phase 2: 1,300 pairs, 2,776 key points. 136 key points excluded (125 no author change, 11 no diff); 2,640 labelled across 1,164 pairs.
Files are split into 26 batches of 50 pairs (`phase2_batchNN`) in sheet order, plus combined files.

## How labels were assigned

Phase 2 was coded in RQ1 at subtheme level (description, direction, evidence, motive), not with open codes, so defaults are set per subtheme and direction:

| RQ1 subtheme | default |
|---|---|
| Release status and bookkeeping | Non-functional (deprecation: Perfective) |
| Description and naming | Non-functional |
| Documentation content | Perfective (formatting, links, tracking, auto-generated refresh: Non-functional) |
| Testing assets | Perfective |
| Package file housekeeping | Perfective (license, renames: Non-functional; manifests, ignore files: Adaptive) |
| Installation and dependencies | Adaptive |
| Metadata declarations | Adaptive |
| Credentials and configuration values | Adaptive (hardcoded or plaintext secrets and paths removed: Corrective) |
| External services and endpoints | Adaptive (new service called: Implementation; removed: Perfective) |
| Feature and capability scope | Implementation (removed: Perfective) |
| Code implementation changes | Perfective (new function or feature: Implementation) |
| Safety subthemes and Personal data handling | Perfective |
| Payments and monetization | Implementation (prices, promotion, donations: Non-functional; removed: Perfective) |

Then 517 key points (in 293 pairs) whose description, motive or pair changelog mentions a fix, bug, scanner, audit, mismatch, hardcoded value or similar were read one by one, and 294 labels were changed (e.g. to Corrective when a real problem was shown). The same rules as Phase 1 apply (see the Phase 1 log).

## Confidence

- high (617): unambiguous subtheme, or the key point was read and checked.
- medium (1,972): default for a purpose-dependent subtheme that was not read one by one. A spot check of 45 of these found about 4 that a reader could label differently, so treat these as the main thing to review.
- low (51): read and labelled, but none of the five categories fits well (same poor-fit groups as Phase 1: whole-skill template swaps, scanner-driven wording or code changes that fix nothing, secrets or personal data added, safety checks weakened).

## Pairs without a rebuilt diff

8 labelled pairs have no rebuilt diff because their versions were deleted from ClawHub after RQ1 (rows 158, 249, 265, 322, 505, 674, 830, 843). They are labelled from their RQ1 key points (`diff_available = no`).
