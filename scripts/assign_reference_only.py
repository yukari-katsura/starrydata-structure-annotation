#!/usr/bin/env python
"""Attach structure references to hosts without classifying them.

For most of the remaining tail, a prototype assignment is not worth making: 1,685
of the 2,748 unannotated hosts hold a single composition, often a single sample,
with no taxonomy hypothesis and no way to check the answer. A judgement there is
expensive, unverifiable and classifies one measurement.

Attaching an identifier is different work entirely. Either the compound is in
Materials Project and TEDesignLab or it is not; the lookup is mechanical and the
result is checkable. That is worth doing for the whole tail at once.

These records deliberately carry NO prototype_id. They say "here is the
structure entry for this chemistry", not "this is what the sample is" -- the
distinction the rest of the project rests on. They are kept out of the
assignment ledger for the same reason.

Output:
    data/annotated/annotations/reference_only_hosts.parquet

Usage:  python scripts/assign_reference_only.py [--dry-run]
"""
import argparse, json, os
import pandas as pd

_P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANN = os.path.join(_P, 'data', 'annotated') + os.sep
OUT = ANN + 'annotations/reference_only_hosts.parquet'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    hosts = pd.read_parquet(ANN + 'input/df_host_systems.parquet')
    cand = pd.read_parquet(ANN + 'input/df_structure_candidates.parquet')
    refs = pd.read_parquet(ANN + 'input/df_structure_refs.parquet')
    tedl = pd.read_parquet(ANN + 'input/df_tedl_entries.parquet')
    done = {json.loads(l)['host_system']
            for l in open(ANN + 'annotations/family_assignments.jsonl') if l.strip()}

    rest = hosts[~hosts.host_system.isin(done)]
    print(f'{len(rest)} hosts without a family assignment ({rest.n_samples.sum()} samples)')

    # Best reference per host: the primary candidate with the most ICSD support.
    p = cand[cand.is_primary].sort_values(['host_system', 'n_icsd'],
                                          ascending=[True, False])
    best = p.drop_duplicates('host_system').set_index('host_system')

    # TEDesignLab reach, host -> entry, preferring the one whose space group
    # matches the reference we are about to record.
    tr = refs[(refs.source == 'tedesignlab') & refs.host_system.notna()]
    icsd_to_tedl = dict(zip(tedl.icsd_id, tedl.tedl_id))
    tedl_by_host = {}
    for r in tr.itertuples():
        tid = icsd_to_tedl.get(r.icsd_id)
        if tid:
            tedl_by_host.setdefault(r.host_system, []).append((r.spacegroup_number, tid))

    rows = []
    for r in rest.itertuples():
        b = best.loc[r.host_system] if r.host_system in best.index else None
        if b is None:
            continue
        sg = b.spacegroup_number
        tid, tmatch = None, None
        for tsg, t in tedl_by_host.get(r.host_system, []):
            if tsg == sg:
                tid, tmatch = t, 'host+spacegroup'
                break
        if tid is None and tedl_by_host.get(r.host_system):
            tid, tmatch = tedl_by_host[r.host_system][0][1], 'host only'
        rows.append({
            'host_system': r.host_system,
            'rank': r.rank, 'n_samples': r.n_samples,
            'n_compositions': r.n_compositions,
            'reference_formula': b.reduced_formula,
            'spacegroup_number': sg,
            'spacegroup_symbol': b.spacegroup_symbol,
            'mp_id': b.mp_id,
            'n_icsd': b.n_icsd,
            'e_above_hull': b.e_above_hull,
            'tedl_id': tid,
            'tedl_match': tmatch,
            # deliberately absent: prototype_id. This is a reference, not a
            # classification, and must not be read as one.
            'prototype_id': None,
            'record_type': 'reference_only',
            'basis': 'reference lookup through the host system; no structural judgement made',
        })

    df = pd.DataFrame(rows)
    print(f'  {len(df)} hosts get a structure reference '
          f'({df.n_samples.sum()} samples, {df.n_samples.sum()/rest.n_samples.sum()*100:.0f}% of the remainder)')
    print(f'    with an mp_id   : {int(df.mp_id.notna().sum())}')
    print(f'    with a tedl_id  : {int(df.tedl_id.notna().sum())}')
    print(f'    single-composition hosts: {int((df.n_compositions==1).sum())}')
    unmatched = rest[~rest.host_system.isin(df.host_system)]
    print(f'  {len(unmatched)} hosts have no reference at all '
          f'({unmatched.n_samples.sum()} samples) -- nothing to attach')
    if args.dry_run:
        print('\nDry run: nothing written.')
        return 0
    df.to_parquet(OUT, index=False, engine='pyarrow')
    print(f'\n  -> {OUT}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
