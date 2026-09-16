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


def reasons_for(rec, ambiguous_hosts):
    """Why this host needs a paper, most blocking first."""
    out = []
    if rec.get('is_mixed'):
        alts = ', '.join(rec.get('alt_prototype_ids') or []) or 'unlisted'
        out.append(f'MIXED — one label covers several structures (also: {alts})')
    if rec['confidence'] in ('low', 'medium'):
        out.append(f'{rec["confidence"]} confidence')
    for ph in rec.get('phases') or []:
        if ph.get('transition_K') and ph.get('transition_basis') == 'taxonomy_default':
            out.append(f'transition at ~{ph["transition_K"]} K is a taxonomy default, '
                       f'not read from a paper')
            break
    if rec['host_system'] in ambiguous_hosts:
        out.append('structure reference cannot separate two polymorphs')
    if rec.get('reference_note'):
        out.append('reference disagreement recorded')
    if rec.get('taxonomy_feedback'):
        out.append('taxonomy issue recorded')
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
                     'chunk': rec.get('chunk'), 'reasons': '; '.join(why)})
        blocks.append((rec.get('n_samples') or 0, rec, why))

    rows = pd.DataFrame(rows).sort_values('n_samples', ascending=False)
    rows.to_parquet(OUT_PQ, index=False, engine='pyarrow')

    blocks.sort(key=lambda t: -t[0])
    lines = [
        '# Annotations that need a paper to settle', '',
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
        for w in why:
            lines.append(f'- {w}')
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
    cnt = collections.Counter(w for _, _, why in blocks for w in
                              [x.split(' —')[0].split(' at ~')[0] for x in why])
    for k, v in cnt.most_common(6):
        print(f'    {v:4d}  {k}')


if __name__ == '__main__':
    main()
