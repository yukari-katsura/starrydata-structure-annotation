#!/usr/bin/env python
"""Stamp stable ids on assignments and record what level each is determined at.

host_system is a routing key, not an identity: the same element combination can
hold several structures. Fe-O covers spinel Fe3O4 and corundum Fe2O3; O-Ti
covers rutile, anatase, corundum, rocksalt and Magneli phases. Composition is
usually enough to separate them, but not always -- alpha-Fe2O3 (corundum) and
gamma-Fe2O3 (spinel) share a formula, so only the sample distinguishes them.

So every assignment gets:
  assignment_id          stable, derived from its natural key, not from rank
  determined_at          host | composition | sample_required
  is_authoritative       false when a finer-grained record supersedes it

ids are a sha1 of the natural key, so they survive regeneration, re-ranking and
threshold changes. They change only if the key itself changes, which is the
correct behaviour: a different key is a different thing.

Idempotent. Run after any step that writes assignments.

Usage:  python scripts/add_assignment_ids.py
"""

import hashlib
import json
import os

import pandas as pd

_P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANN = os.path.join(_P, 'data', 'annotated') + os.sep
LEDGER = ANN + 'annotations/family_assignments.jsonl'
COMPA = ANN + 'annotations/composition_assignments.parquet'


def sid(prefix, key):
    return f'{prefix}-{hashlib.sha1(key.encode()).hexdigest()[:10]}'


def main():
    records = [json.loads(l) for l in open(LEDGER) if l.strip()]

    comp_by_host, comp_protos = {}, {}
    if os.path.exists(COMPA):
        d = pd.read_parquet(COMPA)
        for r in d.itertuples():
            comp_by_host.setdefault(r.host_system, []).append(r)
            comp_protos.setdefault(r.host_system, set()).add(r.prototype_id)

    # --- host-level records -------------------------------------------------
    for r in records:
        host = r['host_system']
        r['assignment_id'] = sid('HSA', host)
        protos = comp_protos.get(host, set())
        if len(protos) > 1:
            # the host holds several structures; the composition rows decide
            r['determined_at'] = 'composition'
            r['is_authoritative'] = False
            r['superseded_by'] = 'composition_assignments.parquet'
            r['n_prototypes_below'] = len(protos)
        elif r.get('is_mixed') and not r.get('composition_split_rule'):
            r['determined_at'] = 'sample_required'
            r['is_authoritative'] = False
            r['n_prototypes_below'] = None
        else:
            r['determined_at'] = 'host'
            r['is_authoritative'] = True
            r['n_prototypes_below'] = 1
    with open(LEDGER, 'w') as fh:
        fh.write('\n'.join(json.dumps(r) for r in records) + '\n')

    lv = {}
    for r in records:
        lv[r['determined_at']] = lv.get(r['determined_at'], 0) + 1
    print(f'{len(records)} host-level records stamped')
    for k, v in sorted(lv.items()):
        print(f'  determined_at={k:16s} {v}')

    # --- composition-level records -----------------------------------------
    if not os.path.exists(COMPA):
        print('\nNo composition_assignments.parquet; skipping composition ids.')
        return 0
    d = pd.read_parquet(COMPA)
    d['assignment_id'] = [sid('CPA', c) for c in d.composition]
    d['host_assignment_id'] = [sid('HSA', h) for h in d.host_system]
    # a composition whose curator detail disagreed with itself needs the sample
    amb = d.matched.astype(str).str.contains('ambiguous', na=False)
    d['determined_at'] = ['sample_required' if a else 'composition' for a in amb]
    d['is_authoritative'] = ~amb
    d.to_parquet(COMPA, index=False, engine='pyarrow')
    print(f'\n{len(d)} composition-level records stamped')
    print(f'  determined_at=composition     {int((~amb).sum())}')
    print(f'  determined_at=sample_required {int(amb.sum())}')
    print(f'\n  example: {d.iloc[0].assignment_id} '
          f'({d.iloc[0].composition}) under {d.iloc[0].host_assignment_id}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
