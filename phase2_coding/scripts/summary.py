"""Rebuild phase2_summary.md and phase2_spotcheck.csv from phase2_codes.csv (working script)."""
import csv, os, re, random
from collections import Counter, OrderedDict
W = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(W, '..')
rows = list(csv.DictReader(open(os.path.join(P, 'phase2_codes.csv'), encoding='utf-8')))
order = OrderedDict()
for r in rows:
    order.setdefault(r['pair_id'], len(order) + 1)
pairs = OrderedDict()
for r in rows:
    pairs.setdefault(r['pair_id'], []).append(r)

THEMES = OrderedDict([
 ('Upkeep and presentation', ['Documentation content', 'Release status and bookkeeping', 'Description and naming']),
 ('Functional behavior', ['Feature and capability scope', 'Code implementation changes']),
 ('Safety controls and risk communication', ['Agent behavior guardrails', 'Safety and transparency guidance', 'Code-level safety checks', 'Personal data handling']),
 ('Configuration and declared requirements', ['Metadata declarations', 'Credentials and configuration values']),
 ('Dependencies and external reach', ['Installation and dependencies', 'External services and endpoints']),
 ('Package composition', ['Package file housekeeping', 'Testing assets']),
 ('Monetization', ['Payments and monetization']),
])

def first(p): return pairs[p][0]
nac = [p for p in pairs if first(p)['no_author_change'] == 'yes']
du = [p for p in pairs if first(p)['diff_unavailable'] == 'yes']
coded = [p for p in pairs if p not in nac and p not in du]
N = len(coded)
coded_rows = [r for p in coded for r in pairs[p]]
unfit = [r for r in rows if r['subtheme'] == 'UNFIT']
low = [r for r in rows if r['confidence'] == 'low']
partly = [p for p in pairs if first(p)['read_mode'] == 'partly read']
human = [p for p in pairs if first(p)['read_mode'] == 'human']

L = []
A = L.append
A('# Phase 2 coding summary\n')
A('Codebook: `open_coding/themes.md` (frozen). Sample: `coding_rounds/phase2_sheet.csv`. Codes: `phase2_coding/phase2_codes.csv`.\n')
A('This version reflects the full reread of every pair that had been read by scan (batches 1 to 11 of the reread, 272 pairs). See "Reading notes" below.\n')
A('## Counts\n')
A('item | n\n---|---')
A(f'pairs in sheet | {len(pairs)}')
A(f'excluded: no author change | {len(nac)}')
A(f'excluded: diff unavailable | {len(du)}')
A(f'pairs coded (author changes present) | {N}')
A(f'key points, all rows | {len(rows)}')
A(f'key points, coded pairs only | {len(coded_rows)}')
A(f'key points per coded pair (mean) | {len(coded_rows)/N:.2f}')
A(f'UNFIT key points | {len(unfit)}')
A(f'low confidence key points | {len(low)}')
A(f'partly read pairs | {len(partly)}')
A(f'pairs waiting for human coding | {len(human)}\n')
A(f'"Pairs coded" means the {N} pairs left after removing the {len(nac)} no-author-change pairs and the {len(du)} diff-unavailable pairs from the {len(pairs)} in the sheet.\n')
A(f'Pair-level counts below use the coded pairs only. A pair counts for a theme or subtheme if any of its key points has it, so columns sum to more than the pair total.\n')

A('## Pairs per theme and subtheme\n')
A(f'theme / subtheme | pairs | share of {N} | key points | added | removed | modified')
A('---|---|---|---|---|---|---')
def stats(sel):
    ps = {r['pair_id'] for r in coded_rows if sel(r)}
    kp = [r for r in coded_rows if sel(r)]
    d = Counter(r['direction'] for r in kp)
    return len(ps), len(kp), d
for th, subs in THEMES.items():
    n, k, d = stats(lambda r: r['theme'] == th)
    A(f'**{th}** | **{n}** | **{100*n/N:.1f}%** | **{k}** | {d["added"]} | {d["removed"]} | {d["modified"]}')
    for s in subs:
        n, k, d = stats(lambda r, s=s: r['subtheme'] == s)
        A(f'&nbsp;&nbsp;{s} | {n} | {100*n/N:.1f}% | {k} | {d["added"]} | {d["removed"]} | {d["modified"]}')
A('')

A('## Direction split (key points, coded pairs)\n')
A('direction | key points | share\n---|---|---')
dc = Counter(r['direction'] for r in coded_rows)
for k in ('added', 'removed', 'modified'):
    A(f'{k} | {dc[k]} | {100*dc[k]/len(coded_rows):.1f}%')
other = {k: v for k, v in dc.items() if k not in ('added', 'removed', 'modified')}
if other: A(f'\nOther direction values: {other}')
A('')

A('## Flags\n')
A('changelog_mismatch | all pairs | coded pairs | no author change pairs\n---|---|---|---')
for v in ('yes', 'generic', 'no', 'n/a'):
    a = sum(1 for p in pairs if first(p)['changelog_mismatch'] == v)
    c = sum(1 for p in coded if first(p)['changelog_mismatch'] == v)
    x = sum(1 for p in nac if first(p)['changelog_mismatch'] == v)
    A(f'{v} | {a} | {c} | {x}')
A('')
A(f'no_author_change = yes: {len(nac)} pairs. diff_unavailable = yes: {len(du)} pairs (rows {", ".join(str(order[p]) for p in du)}).\n')
A(f'Empty diff with a specific unmet claim (mismatch yes + no author change): {sum(1 for p in nac if first(p)["changelog_mismatch"] == "yes")} pairs.\n')
cc = Counter(r['confidence'] for r in rows)
A(f'Confidence (all key points): high {cc["high"]}, medium {cc["medium"]}, low {cc["low"]}\n')

GROUPS = [
 ('Respond to registry scanner or audit findings (incl. reducing false positives)', r'scan|audit|flag|false.positive|virustotal|moderation|security review|review(er)? (warn|finding)|suspicious|可疑|registry (warning|check)|clawhub\'s feedback|skillspector|static.analysis|findings|install.gate'),
 ('Security hardening / prevent harm', r'secur|harm|inject|leak|exploit|vulnerab|malicious|protect|privacy|attack|abuse|ghsa|cve|sandbox|data loss|forg|traversal|safe|unauthori|exfil|username|credential|secret|private key|personal|desensiti|scrub|hardcoded|\beval\b|\bssl\b|phishing|spam|approval|persistence risk|harden|sanitiz|shell history|spending|cryptograph|preflight|network operations|fake content|account names|channel id|api key'),
 ('Fix a defect or improve reliability/compatibility/performance', r'\bfix|bug|error|crash|fail|broken|reliab|compat|perform|faster|speed|timeout|stab|expire|cannot|can\'t|not work|issue|lockout|regress|surprised|wrong|collision|breaks|deprecat|reproducib|restore|revert|rollback|preserv|so openclaw can load|load the correct|version sync|shipped .* inside|reuse|durable|resolve|unwanted activation'),
 ('Registry or metadata compatibility', r'registry|metadata|schema|frontmatter|manifest|clawhub (strip|requir|format)|_meta\.json|listing|published skill'),
 ('Simplify setup or usage', r'simplif|easier|easy|setup|convenien|user experience|\bux\b|one.step|friction|no extra|self.contained|readab|auto.enable|refactor|generic|accessib|bundle|switch default|typescript source|structure|drops the'),
 ('Consistency of formatting', r'format|consisten|style'),
 ('Accurate or honest description', r'accura|honest|mislead|clarif|correct (the )?descr|truthful|align|matches|non.existent|scoped|off.topic|scope helper|real user testing|live account read|figures written|weights from'),
 ('Discoverability and traffic tracking', r'discover|seo|traffic|utm|visib|search rank|attribution|keywords|vector search|embedding search'),
 ('Product or business structure', r'business|pricing|product|monetiz|tier|licen|source.available|intellectual'),
]
mot = OrderedDict()
for p in coded:
    ms = [r['stated_motive'].strip() for r in pairs[p] if r['stated_motive'].strip()]
    if ms: mot[p] = ms
gc = Counter(); others = []
for p, ms in mot.items():
    t = ' '.join(ms).lower(); hit = False
    for g, rx in GROUPS:
        if re.search(rx, t): gc[g] += 1; hit = True
    if not hit: others.append((p, ms[0]))
A('## Stated motive groups\n')
A(f'{len(mot)} of {N} coded pairs state a reason. Groups follow the Phase 1 codebook list and are assigned by keyword match on the motive text (keyword lists in `phase2_coding/scripts/summary.py`), so a pair can be in more than one group.\n')
A('motive group | pairs\n---|---')
for g, _ in GROUPS: A(f'{g} | {gc[g]}')
A(f'Other (no group matched) | {len(others)}\n')
if others:
    A('Motives in Other:\n')
    for p, m in others: A(f'- row {order[p]} `{p}`: {m}')
    A('')

A('## UNFIT key points\n')
A('None.\n' if not unfit else '\n'.join(f'- row {order[r["pair_id"]]} `{r["pair_id"]}` kp {r["key_point_no"]}: {r["description"]}. Note: {r["note"]}' for r in unfit) + '\n')
A('## Low confidence key points\n')
A('None.\n' if not low else '\n'.join(f'- row {order[r["pair_id"]]} `{r["pair_id"]}` kp {r["key_point_no"]}: {r["subtheme"]}, "{r["description"]}". Note: {r["note"]}' for r in low) + '\n')

A('## Partly read pairs\n')
A('Rules from CLAUDE.md: (a) single-file rule: one file\'s diff is over 3,000 lines, so its first 1,000 lines plus every SKILL.md and script hunk were read; (b) over-20,000 rule: the pair\'s total diff is over 20,000 lines, so SKILL.md in full, the complete file list, every added or changed script, entry point, manifest and config file, and a sample of the rest were read. Every other pair was read in full.\n')
A('row | pair | rule | what was read\n---|---|---|---')
DS = {}
for d in csv.DictReader(open(os.path.join(P, '..', 'coding_rounds', 'phase2_diffstats.csv'), encoding='utf-8-sig')):
    try: DS[d['pair_id']] = int(float(d['lines_added'] or 0)) + int(float(d['lines_removed'] or 0))
    except ValueError: pass
for p in partly:
    cands = []
    for r in pairs[p]:
        if 'partly read' in r['note']: cands.append(r['note'])
        for m in re.finditer(r'\(partly read[^)]*\)', r['evidence']): cands.append(m.group(0).strip('()'))
        for m in re.finditer(r'(?<!\()partly read:[^)]*$', r['evidence']): cands.append(m.group(0))
    txt = max(cands, key=len) if cands else ''
    tot = DS.get(p, 0)
    rule = f'over 20,000 ({tot:,} lines)' if tot > 20000 else f'single file over 3,000 (pair {tot:,} lines)'
    A(f'{order[p]} | `{p}` | {rule} | {txt.replace("|", "/")}')
A('')

A('## Reading notes\n')
A('- The first coding pass read mid-size pairs (over 250 changed lines) as the first 250 lines plus a scan. All 272 such pairs were reread in 11 batches of up to 25: every pair below the partly read thresholds was read in full, file by file in chunks. `read_mode` is `full` or `partly read` for every pair (`n/a` for the 11 diff-unavailable pairs). No row is left as "needs reread".')
A('- Renamed or moved files that the diff shows as a full delete plus a full add were compared by script; all differing lines and one full copy were read (rows 537, 607, 679, 836, 1159, 1258, 1300).')
A('- Row 827: the scanner snapshot pages inside that diff were left unread on purpose, because they are registry security review text and reading them would break blind coding.')
A('- Row 6 (`batxent/rednote-contacts@1.0.0->1.0.1`) was stopped during the reread at line 1,453; on a later retry it was read in full (all 1,820 lines) and recoded, so `human_coding_list.csv` is now empty.')
A('- Pairs whose codes changed in the reread are listed in `phase2_coding/reread_log.csv` (column `codes_changed`).\n')

open(os.path.join(P, 'phase2_summary.md'), 'w', encoding='utf-8').write('\n'.join(L))

# spotcheck
k = round(0.10 * N)
chosen = set(random.Random(20261031).sample(coded, k))
cols = ['pair_id','key_point_no','description','theme','subtheme','direction','evidence','stated_motive','confidence','changelog_mismatch','no_author_change','diff_unavailable','note','coder_verdict','coder_subtheme','coder_note']
out = []
for p in coded:
    if p in chosen:
        for r in pairs[p]:
            d = {c: r.get(c, '') for c in cols[:13]}
            d.update(coder_verdict='', coder_subtheme='', coder_note='')
            out.append(d)
with open(os.path.join(P, 'phase2_spotcheck.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(out)
print('N', N, 'spotcheck pairs', k, 'rows', len(out), 'partly', len(partly), 'motives', len(mot), 'other', len(others))
