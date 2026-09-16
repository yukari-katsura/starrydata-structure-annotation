#!/usr/bin/env python
"""List the annotations that need a paper to settle, with DOI links.

Every assignment so far was made from composition plus materials knowledge, so
`experimentally_confirmed` is false throughout. This ranks the cases where that
matters most and points at the specific papers that would resolve each one.

A host is queued when any of these hold:
  - confidence is low or medium
  - is_mixed: one label covers several real structures
  - a phase transition temperature came from a taxonomy default, not the paper
  - the structure reference could not separate two polymorphs (ambiguous_primary)
  - the record carries a reference_note or taxonomy_feedback

For a mixed host the competing compositions are listed separately, each with the
papers reporting it, so the split can be made by reading rather than guessing.

Output:
    data/annotated/validation/needs_review.md
    data/annotated/validation/needs_review.parquet

Usage:  python scripts/build_review_queue.py [--top N]
"""

import argparse
import json
import os

import pandas as pd

_P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANN = os.path.join(_P, 'data', 'annotated') + os.sep
LEDGER = ANN + 'annotations/family_assignments.jsonl'
SAMPLES = os.path.join(_P, 'data', 'processed', 'df_samples.parquet')
COMPS = ANN + 'input/df_compositions.parquet'
CANDS = ANN + 'input/df_structure_candidates.parquet'
OUT_MD = ANN + 'validation/needs_review.md'
OUT_PQ = ANN + 'validation/needs_review.parquet'


# What to look for in the paper, per flag. Kept next to the flag that raises it
# so the report never says "needs checking" without saying what to check.
WHAT_TO_LOOK_FOR = {
    'mixed': ('Which composition is which structure. Look for the XRD pattern, a stated '
              'space group, or a "single phase" / "second phase" remark. Record a '
              'composition -> prototype mapping; a prefix like "Ca3Co4O9" is enough to '
              'cover every doped variant of it.'),
    'polymorph': ('Which polymorph was actually made. Look for the reported space group '
                  'or lattice parameters in the experimental section. Record the space '
                  'group number, or the mp_id if you have it.'),
    'transition': ('Whether the paper reports a structural transition, and at what '
                   'temperature. Look for DSC, high-temperature XRD, or a kink discussed '
                   'in the text. Record the temperature, or "none" if the paper shows '
                   'the sample staying in one phase across its range.'),
    'confidence': ('Any explicit structure statement -- space group, prototype name, or '
                   'the reference structure the authors index against. Record confirm, '
                   'or the prototype it should be.'),
    'taxonomy': ('Whether the taxonomy entry itself is wrong or incomplete, rather than '
                 'the assignment. Record what should change in the prototype.'),
}


def reasons_for(rec, ambiguous_hosts):
    """Why this host needs a paper, most blocking first. Returns (text, kind)."""
    # A host that has been read and settled must leave the queue, or the list
    # never shrinks and the workflow has no end state.
    if rec.get('experimentally_confirmed') and rec.get('confidence') != 'low':
        if not (rec.get('is_mixed') and not
                (rec.get('composition_split') or rec.get('composition_split_rule'))):
            return []

    out = []
    if rec.get('is_mixed') and not (rec.get('composition_split')
                                    or rec.get('composition_split_rule')):
        alts = ', '.join(rec.get('alt_prototype_ids') or []) or 'unlisted'
        out.append((f'MIXED — one label covers several structures (also: {alts})', 'mixed'))
    if rec['confidence'] in ('low', 'medium'):
        out.append((f'{rec["confidence"]} confidence', 'confidence'))
    for ph in rec.get('phases') or []:
        if ph.get('transition_K') and ph.get('transition_basis') == 'taxonomy_default':
            out.append((f'transition at ~{ph["transition_K"]} K is a taxonomy default, '
                        f'not read from a paper', 'transition'))
            break
    if rec['host_system'] in ambiguous_hosts:
        out.append(('structure reference cannot separate two polymorphs', 'polymorph'))
    if rec.get('reference_note'):
        out.append(('reference disagreement recorded', 'polymorph'))
    if rec.get('taxonomy_feedback'):
        out.append(('taxonomy issue recorded', 'taxonomy'))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--top', type=int, default=40,
                    help='how many hosts to write into the markdown report')
    args = ap.parse_args()

    led = [json.loads(l) for l in open(LEDGER) if l.strip()]
    comp = pd.read_parquet(COMPS)
    smp = pd.read_parquet(SAMPLES, columns=['SID', 'composition', 'DOI', 'title', 'year'])

    amb = set()
    if os.path.exists(CANDS):
        c = pd.read_parquet(CANDS)
        if 'ambiguous_primary' in c:
            amb = set(c[c.ambiguous_primary.notna()].host_system)

    # papers per composition, ordered by how much of it they carry
    smp = smp[smp.composition.notna()]
    per_comp = (smp.groupby(['composition', 'DOI'])
                   .agg(n=('SID', 'size'), title=('title', 'first'), year=('year', 'first'))
                   .reset_index().sort_values('n', ascending=False))

    rows, blocks = [], []
    for rec in led:
        why = reasons_for(rec, amb)
        if not why:
            continue
        host = rec['host_system']
        rows.append({'host_system': host, 'prototype_id': rec['prototype_id'],
                     'confidence': rec['confidence'], 'n_samples': rec.get('n_samples'),
                     'chunk': rec.get('chunk'),
                     'reasons': '; '.join(w for w, _ in why)})
        blocks.append((rec.get('n_samples') or 0, rec, why))

    rows = pd.DataFrame(rows).sort_values('n_samples', ascending=False)
    rows.to_parquet(OUT_PQ, index=False, engine='pyarrow')

    blocks.sort(key=lambda t: -t[0])
    lines = [
        '# Annotations that need a paper to settle', '',
        '**How to use this file.** Each entry says what is uncertain, what to look for '
        'in the paper, and links the papers reporting the compositions in question. '
        'Fill in the ```finding``` block at the end of an entry and run '
        '`python scripts/apply_review_findings.py` to write it into the ledger. '
        'Entries you skip are left alone, so you can work through this a few at a '
        'time. Nothing is overwritten without a decision.', '',
        f'{len(blocks)} of {len(led)} annotated host systems, '
        f'{int(rows.n_samples.sum())} samples. Ordered by sample count, so working '
        'top-down resolves the most data per paper read.', '',
        'Every assignment here was made from composition and materials knowledge; '
        'none has been read out of a paper. The links below go to the specific '
        'papers reporting the compositions in question.', '',
        '---', '',
    ]
    for _, rec, why in blocks[:args.top]:
        host = rec['host_system']
        lines.append(f'## {host} — {rec.get("n_samples")} samples, chunk {rec.get("chunk")}')
        lines.append('')
        lines.append(f'**Assigned** `{rec["prototype_id"]}` ({rec["confidence"]} confidence)')
        lines.append('')
        lines.append('**Needs checking because:**')
        for w, _ in why:
            lines.append(f'- {w}')
        lines.append('')
        seen_kinds = []
        for _, k in why:
            if k not in seen_kinds:
                seen_kinds.append(k)
        lines.append('**What to look for:**')
        for k in seen_kinds:
            lines.append(f'- {WHAT_TO_LOOK_FOR[k]}')
        lines.append('')
        if rec.get('basis'):
            lines.append(f'> {rec["basis"]}')
            lines.append('')

        # the compositions actually in dispute
        hc = comp[comp.host_system == host].nlargest(4, 'n_samples')
        for r in hc.itertuples():
            papers = per_comp[per_comp.composition == r.composition].head(3)
            if papers.empty:
                continue
            lines.append(f'**`{r.composition}`** — {r.n_samples} samples, {r.n_papers} papers')
            for pr in papers.itertuples():
                t = str(pr.title).strip().strip('"') if isinstance(pr.title, str) else ''
                t = (t[:95] + '...') if len(t) > 98 else t
                # year arrives as a string and is sometimes blank
                yr = ''
                try:
                    yr = f' ({int(float(pr.year))})' if str(pr.year).strip() else ''
                except (TypeError, ValueError):
                    yr = ''
                lines.append(f'- [{t or pr.DOI}](https://doi.org/{pr.DOI}){yr} — {pr.n} samples')
            lines.append('')
        # Fill-in block. Parsed by scripts/apply_review_findings.py, so leave the
        # fences and keys intact and delete the block entirely if you skip a host.
        lines.append('**Your finding** — fill in, then run '
                     '`python scripts/apply_review_findings.py`:')
        lines.append('')
        lines.append('```finding')
        lines.append(f'host: {host}')
        lines.append('decision:        # confirm | change | split | unresolved')
        lines.append('prototype:       # for change: the prototype id it should be')
        if rec.get('is_mixed'):
            lines.append('split:           # for split: one "composition -> prototype_id" per line')
            lines.append('  # Ca3Co4O9 -> misfit_cobaltite')
            lines.append('  # Ca3Co2O6 -> ca3co2o6_chain')
        if any(k == 'polymorph' for _, k in why):
            lines.append('spacegroup:      # number the paper reports, e.g. 212')
            lines.append('mp_id:           # if you have it')
        if any(k == 'transition' for _, k in why):
            lines.append('transition_K:    # temperature, or "none"')
        lines.append('evidence:        # DOI you read this from')
        lines.append('notes:')
        lines.append('```')
        lines.append('')
        lines.append('---')
        lines.append('')

    if len(blocks) > args.top:
        lines.append(f'*{len(blocks) - args.top} further hosts are in '
                     f'`needs_review.parquet`; re-run with `--top` to include them.*')

    os.makedirs(os.path.dirname(OUT_MD), exist_ok=True)
    with open(OUT_MD, 'w') as f:
        f.write('\n'.join(lines) + '\n')

    print(f'{len(blocks)} / {len(led)} host systems need a paper '
          f'({int(rows.n_samples.sum())} samples)')
    print(f'  -> {OUT_MD}  (top {min(args.top, len(blocks))} written)')
    print(f'  -> {OUT_PQ}')
    print('\n  most common reasons:')
    import collections
    cnt = collections.Counter(w.split(' —')[0].split(' at ~')[0]
                              for _, _, why in blocks for w, _ in why)
    for k, v in cnt.most_common(6):
        print(f'    {v:4d}  {k}')


if __name__ == '__main__':
    main()
