#!/usr/bin/env python
"""Join the annotation ledger back onto compositions and samples.

The ledger is keyed by host_system, which is a grouping key rather than
something you can query a sample by. This resolves it down:

    family_assignments.jsonl  (host system)
      -> df_compositions      (composition -> host_system)
      -> df_samples           (SID, sample_id -> composition)

and while doing so it applies each host's dopant roles to the actual minor
elements of each composition, which turns a role into a doping level.

Output:
    data/annotated/df_annotated_compositions.parquet
    data/annotated/df_annotated_samples.parquet
    data/annotated/by_family/<prototype_id>.parquet
    data/annotated/validation/holdout_comparison.csv

Usage:  python scripts/build_annotated_samples.py
"""

import json
import os
import re

import pandas as pd

_P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANN = os.path.join(_P, 'data', 'annotated') + os.sep
LEDGER = ANN + 'annotations/family_assignments.jsonl'
TAX = ANN + 'taxonomy/prototypes_seed_v3.json'
COMPS = ANN + 'input/df_compositions.parquet'
SAMPLES = os.path.join(_P, 'data', 'processed', 'df_samples.parquet')


def load_ledger():
    return {r['host_system']: r
            for r in (json.loads(l) for l in open(LEDGER) if l.strip())}


def resolve_dopants(rec, dopant_fracs, host_fracs):
    """Apply a host's dopant roles to one composition's minor elements.

    Returns (list of resolved dopants, list of elements the host has no role for).

    site_fraction is the doping level that actually means something: the
    dopant's share of the sublattice it substitutes into, not of the whole
    formula. Na in Pb0.98Na0.02Te is 1% of the formula but 2% of the cation
    site, and it is the latter that sets the carrier count.
    """
    roles = {d['element']: d for d in rec.get('dopant_roles', [])}
    out, unresolved = [], []
    for el, frac in dopant_fracs.items():
        r = roles.get(el)
        if r is None:
            unresolved.append(el)
            continue
        sub = r.get('substitutes_for')
        site_frac = None
        if sub and host_fracs.get(sub):
            site_frac = round(frac / (frac + host_fracs[sub]), 6)
        out.append({
            'element': el,
            'role': r['role'],
            'substitutes_for': sub,
            'atomic_fraction': round(frac, 6),
            'site_fraction': site_frac,
            'confidence': r.get('confidence'),
        })
    out.sort(key=lambda d: -d['atomic_fraction'])
    return out, unresolved


def main():
    led = load_ledger()
    tax = {p['id']: p for p in json.load(open(TAX))['prototypes']}
    print(f'Ledger: {len(led)} host systems annotated')

    comp = pd.read_parquet(COMPS)
    comp = comp[comp.host_system.isin(led)].copy()
    print(f'Compositions under an annotated host: {len(comp)} / 27456')

    rows = []
    for r in comp.itertuples():
        rec = led[r.host_system]
        try:
            dop = json.loads(r.dopant_fracs) if r.dopant_fracs else {}
            hf = json.loads(r.host_fracs) if r.host_fracs else {}
        except Exception:
            dop, hf = {}, {}
        resolved, unresolved = resolve_dopants(rec, dop, hf)
        phases = rec.get('phases') or []
        first = phases[0] if phases else {}
        proto = rec['prototype_id']
        rows.append({
            'composition': r.composition,
            'reduced_formula': r.reduced_formula,
            'host_system': r.host_system,
            'prototype_id': proto,
            'prototype_name': tax.get(proto, {}).get('display_name', proto),
            'structural_class': tax.get(proto, {}).get('structural_class'),
            # Lowest-temperature phase: what the sample is at room temperature.
            'spacegroup_number': first.get('spacegroup_number'),
            'mp_id': first.get('mp_id'),
            'confidence': rec['confidence'],
            # A mixed host carries one label for several real structures, so
            # the composition-level prototype is provisional until split.
            'needs_composition_split': bool(rec.get('is_mixed')),
            'alt_prototype_ids': ','.join(rec.get('alt_prototype_ids') or []),
            'spans_transition': bool(rec.get('spans_transition')),
            'n_phases': len(phases),
            'phases_json': json.dumps(phases) if phases else None,
            'n_dopants': len(resolved),
            'dopants_json': json.dumps(resolved) if resolved else None,
            'dopant_elements': ','.join(d['element'] for d in resolved),
            'max_site_fraction': max((d['site_fraction'] for d in resolved
                                      if d['site_fraction'] is not None), default=None),
            'unresolved_dopants': ','.join(unresolved),
            'is_solid_solution': rec.get('solid_solution_axis') is not None,
            'axis_x_minor': r.axis_x_minor,
            'n_samples': r.n_samples,
            'n_papers': r.n_papers,
            'holdout_hand_label': r.holdout_hand_label,
            'chunk': rec.get('chunk'),
        })
    dfc = pd.DataFrame(rows)
    dfc.to_parquet(ANN + 'df_annotated_compositions.parquet', index=False, engine='pyarrow')
    print(f'  -> df_annotated_compositions.parquet  ({len(dfc)} rows)')

    # --- sample level --------------------------------------------------------
    smp = pd.read_parquet(SAMPLES, columns=['SID', 'sample_id', 'sample_name',
                                            'composition', 'DOI', 'title', 'year',
                                            'journal_short'])
    dfs = smp.merge(dfc.drop(columns=['n_samples', 'n_papers']),
                    on='composition', how='inner')
    dfs.to_parquet(ANN + 'df_annotated_samples.parquet', index=False, engine='pyarrow')
    print(f'  -> df_annotated_samples.parquet  ({len(dfs)} rows, '
          f'{dfs.SID.nunique()} papers)')

    # --- per-family shards ---------------------------------------------------
    outdir = ANN + 'by_family' + os.sep
    os.makedirs(outdir, exist_ok=True)
    for f in os.listdir(outdir):
        if f.endswith('.parquet'):
            os.remove(outdir + f)
    for proto, g in dfs.groupby('prototype_id'):
        safe = re.sub(r'[^A-Za-z0-9_.-]', '_', proto)
        g.to_parquet(f'{outdir}{safe}.parquet', index=False, engine='pyarrow')
    print(f'  -> by_family/  ({dfs.prototype_id.nunique()} family shards)')

    # --- what the join bought ------------------------------------------------
    print(f'\nSamples resolved to a structure : {len(dfs)} / 52027 '
          f'({len(dfs)/52027*100:.1f}%)')
    print(f'  with an mp_id                 : {int(dfs.mp_id.notna().sum())}')
    print(f'  needing composition-level split: {int(dfs.needs_composition_split.sum())}')
    print(f'  spanning a phase transition    : {int(dfs.spans_transition.sum())}')
    print(f'  with at least one dopant       : {int((dfs.n_dopants > 0).sum())}')
    unres = dfs[dfs.unresolved_dopants != '']
    print(f'  carrying an unresolved element : {len(unres)}')

    # --- holdout comparison --------------------------------------------------
    v = dfc[dfc.holdout_hand_label.notna()].copy()
    tab = (v.groupby(['prototype_id', 'holdout_hand_label'])['n_samples']
             .sum().reset_index().sort_values('n_samples', ascending=False))
    tab.to_csv(ANN + 'validation/holdout_comparison.csv', index=False)
    print(f'\nHoldout comparison: {len(v)} compositions carry a curator label '
          f'({int(v.n_samples.sum())} samples)')
    print(f'  -> validation/holdout_comparison.csv  ({len(tab)} prototype/label pairs)')
    print('  largest pairings:')
    for r in tab.head(8).itertuples():
        print(f'    {r.n_samples:6d}  {r.prototype_id:22s} <- "{r.holdout_hand_label}"')


if __name__ == '__main__':
    main()
