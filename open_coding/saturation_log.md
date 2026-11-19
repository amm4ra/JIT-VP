# Saturation log

"New" = not present in any earlier round, after merging synonyms. Subtheme counts exclude the "No change" bucket.
"New open codes" and "new codes %" are recomputed after the consistency sweep (later codes applied back to earlier key points): a code counts as new in the first round where it is applied. % = new / all distinct codes so far, including that round.
"New codes as created" is the historical count: when each code was first invented during coding (before the sweep), with its % of codes created so far.
"Changelog mismatch" = yes / generic / no pairs (skill-card.md and _meta.json claims count as no).

Saturation rule (CLAUDE.md Step 3, after Guest et al. 2020): 2 rounds in a row with no new subthemes AND new codes under 5%. Rounds 1-3 are development rounds.

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
