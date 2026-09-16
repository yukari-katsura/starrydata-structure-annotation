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


def tedl_lookup():
    """(reduced_formula, spacegroup) -> tedl_id, and a formula-only fallback.

    Matching on formula AND space group means the descriptors belong to the
    structure actually assigned. Where only the formula matches, the entry is
    still linked but marked so, because a descriptor computed for a different
    polymorph is a different physical quantity -- LaVO4 appears twice in
    TEDesignLab, at sg 14 and sg 141, with band gaps of 3.50 and 3.15 eV.
    """
    path = ANN + 'input/df_tedl_entries.parquet'
    if not os.path.exists(path):
        return {}, {}, None
    d = pd.read_parquet(path)

    # Starrydata compositions are doped -- Pb0.98Na0.02Te -- while TEDesignLab
    # entries are stoichiometric parents -- PbTe. Exact formula matching links
    # almost nothing, so the link runs through the host system: a doped PbTe
    # sample inherits the descriptors computed for the PbTe parent, which is
    # the physically meaningful association anyway.
    refs = ANN + 'input/df_structure_refs.parquet'
    exact, byhost = {}, {}
    if os.path.exists(refs):
        rf = pd.read_parquet(refs)
        rf = rf[(rf.source == 'tedesignlab') & rf.host_system.notna()]
        icsd_to_id = dict(zip(d.icsd_id, d.tedl_id))
        for r in rf.itertuples():
            tid = icsd_to_id.get(r.icsd_id)
            if not tid:
                continue
            if r.spacegroup_number == r.spacegroup_number:
                exact[(r.host_system, int(r.spacegroup_number))] = tid
            byhost.setdefault(r.host_system, []).append(tid)
    return exact, byhost, d


def main():
    led = load_ledger()
    tedl_exact, tedl_byhost, tedl_tbl = tedl_lookup()
    if tedl_tbl is not None:
        print(f'TEDesignLab feature entries: {len(tedl_tbl)}')
    # Per-composition prototypes from apply_composition_splits.py override the
    # host-level label wherever a mixed host has been split by stoichiometry.
    splits = {}
    sp = ANN + 'annotations/composition_assignments.parquet'
    if os.path.exists(sp):
        d = pd.read_parquet(sp)
        splits = {r.composition: (r.prototype_id, r.confidence, r.matched,
                                  getattr(r, 'assignment_id', None),
                                  getattr(r, 'determined_at', 'composition'))
                  for r in d.itertuples()}
        print(f'Composition-level splits available for {len(splits)} compositions')
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
        split_conf, split_rule, cpa_id, det_at = None, None, None, None
        if r.composition in splits:
            proto, split_conf, split_rule, cpa_id, det_at = splits[r.composition]
        # link to a TEDesignLab feature vector where one exists
        tedl_id, tedl_match = None, None
        sg = first.get('spacegroup_number')
        if sg is not None:
            tedl_id = tedl_exact.get((r.host_system, int(sg)))
            if tedl_id:
                tedl_match = 'host+spacegroup'
        if not tedl_id and r.host_system in tedl_byhost:
            cands = tedl_byhost[r.host_system]
            tedl_id = cands[0]
            tedl_match = ('host only' if len(set(cands)) == 1
                          else f'host only ({len(set(cands))} entries; sg unmatched)')
        rows.append({
            'composition': r.composition,
            'tedl_id': tedl_id,
            'tedl_match': tedl_match,
            'reduced_formula': r.reduced_formula,
            'host_system': r.host_system,
            'prototype_id': proto,
            'prototype_name': tax.get(proto, {}).get('display_name', proto),
            'structural_class': tax.get(proto, {}).get('structural_class'),
            # Lowest-temperature phase: what the sample is at room temperature.
            'spacegroup_number': first.get('spacegroup_number'),
            'mp_id': first.get('mp_id'),
            'confidence': split_conf or rec['confidence'],
            'split_rule': split_rule,
            # which record actually decided this sample's structure
            'assignment_id': cpa_id or rec.get('assignment_id'),
            'host_assignment_id': rec.get('assignment_id'),
            'determined_at': det_at or rec.get('determined_at'),
            # A mixed host carries one label for several real structures, so
            # the composition-level prototype is provisional until split.
            'needs_composition_split': bool(rec.get('is_mixed')) and r.composition not in splits,
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
            'form': getattr(r, 'form', None),
            'chunk': rec.get('chunk'),
        })
    dfc = pd.DataFrame(rows)
    dfc.to_parquet(ANN + 'df_annotated_compositions.parquet', index=False, engine='pyarrow')
    n_t = int(dfc.tedl_id.notna().sum())
    n_ex = int((dfc.tedl_match == 'host+spacegroup').sum())
    print(f'  {n_t} compositions link to a TEDesignLab entry '
          f'({n_ex} on host+spacegroup)')
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
    # the ML-ready subset: samples carrying a computed feature vector
    ml = dfs[dfs.tedl_id.notna()]
    if len(ml):
        mlx = dfs[dfs.tedl_match == 'host+spacegroup']
        ml.to_parquet(ANN + 'df_tedl_linked_samples.parquet', index=False, engine='pyarrow')
        print(f'\n  -> df_tedl_linked_samples.parquet  ({len(ml)} samples, '
              f'{ml.tedl_id.nunique()} distinct TEDesignLab entries)')
        print(f'     of which structure-matched (host+spacegroup): {len(mlx)}')

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
