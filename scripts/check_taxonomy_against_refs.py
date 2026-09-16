#!/usr/bin/env python
"""Test the seed taxonomy's space groups against ICSD/Materials Project evidence.

The taxonomy was assembled from language-model knowledge. This is the first
check of it against measured structures: for every host system that has both a
seed hypothesis and an ICSD-backed space group, does the prototype's space group
actually appear in what has been measured for that chemistry?

Caveat that limits how hard any single disagreement can be read: the reference
tells you which phases EXIST in a chemical system, not which phase a given paper
synthesised. Al-O-Zn is best attested as ZnAl2O4 spinel (227), while nearly every
Starrydata sample in that host is Al-doped wurtzite ZnO (186). Disagreements are
prompts to review, not proof of error.

Writes data/annotated/validation/taxonomy_vs_references.md

Usage:  python scripts/check_taxonomy_against_refs.py
"""

import json
import os
import re

import pandas as pd

_P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANN = os.path.join(_P, 'data', 'annotated') + os.sep
TAX = ANN + 'taxonomy/prototypes_seed_v3.json'
HS = ANN + 'input/df_host_structures.parquet'
OUT = ANN + 'validation/taxonomy_vs_references.md'


def sg_numbers(text):
    return {int(n) for n in re.findall(r'\((\d{1,3})\)', text or '')}


def observed(text):
    """'204 (17 icsd); 194 (12 icsd)' -> [(204, 17), (194, 12)]"""
    return [(int(a), int(b)) for a, b in re.findall(r'(\d+) \((\d+) icsd\)', text or '')]


def main():
    tax = json.load(open(TAX))['prototypes']
    proto = {p['id']: sg_numbers(p.get('typical_space_group')) for p in tax}
    name = {p['id']: p.get('display_name', p['id']) for p in tax}
    hyp = {}
    for p in tax:
        for h in (p.get('example_host_systems') or []):
            hyp.setdefault(h, []).append(p['id'])

    hs = pd.read_parquet(HS)
    obs = {r.host_system: observed(r.sg_by_icsd)
           for r in hs.itertuples() if isinstance(r.sg_by_icsd, str)}
    samples = dict(zip(hs.host_system, hs.n_samples))

    rows = []
    for host, pids in hyp.items():
        o = obs.get(host)
        if not o:
            continue
        exp = set().union(*[proto[p] for p in pids if proto.get(p)]) or set()
        if not exp:
            continue
        rows.append({
            'host': host, 'prototypes': pids, 'expected': sorted(exp),
            'observed': o, 'n_samples': int(samples.get(host, 0)),
            'present': bool(exp & {sg for sg, _ in o}),
            'best': o[0][0] in exp,
        })
    rows.sort(key=lambda r: -r['n_samples'])
    d = pd.DataFrame(rows)
    n = len(d)

    lines = [
        '# Seed taxonomy vs. measured structures', '',
        f'{n} host systems have both a seed hypothesis and at least one '
        'ICSD-backed space group.', '',
        f'- prototype space group **present** among those measured: '
        f'**{int(d.present.sum())}/{n}** ({d.present.mean() * 100:.0f}%)',
        f'- prototype space group is the **best-attested** one: '
        f'**{int(d.best.sum())}/{n}** ({d.best.mean() * 100:.0f}%)', '',
        'The reference says which phases exist in a chemistry, not which phase a '
        'paper made, so a disagreement is a prompt to review rather than proof of '
        'an error. The Al-O-Zn row below is the clearest example.', '',
        '## Disagreements — prototype space group absent from the measured set', '',
        '| host | samples | prototype | taxonomy SG | measured (by ICSD refs) |',
        '|---|---:|---|---|---|',
    ]
    for r in d[~d.present].itertuples():
        o = ', '.join(f'{sg} ({n_} icsd)' for sg, n_ in r.observed[:4])
        lines.append(f'| `{r.host}` | {r.n_samples} | '
                     f'{", ".join(name[p] for p in r.prototypes)} | '
                     f'{", ".join(str(x) for x in r.expected)} | {o} |')

    lines += ['', '## Present but not best-attested — usually a real polymorph question', '',
              '| host | samples | prototype | taxonomy SG | measured (by ICSD refs) |',
              '|---|---:|---|---|---|']
    for r in d[d.present & ~d.best].head(25).itertuples():
        o = ', '.join(f'{sg} ({n_} icsd)' for sg, n_ in r.observed[:4])
        lines.append(f'| `{r.host}` | {r.n_samples} | '
                     f'{", ".join(name[p] for p in r.prototypes)} | '
                     f'{", ".join(str(x) for x in r.expected)} | {o} |')

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w') as f:
        f.write('\n'.join(lines) + '\n')

    print(f'{n} host systems testable')
    print(f'  prototype SG present      : {int(d.present.sum())}/{n} ({d.present.mean()*100:.0f}%)')
    print(f'  prototype SG best-attested: {int(d.best.sum())}/{n} ({d.best.mean()*100:.0f}%)')
    print(f'  {int((~d.present).sum())} disagreements to review')
    print(f'  -> {OUT}')


if __name__ == '__main__':
    main()
