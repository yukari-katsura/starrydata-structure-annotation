#!/usr/bin/env python
"""Validate the family-annotation ledger and report progress.

Run after each annotation chunk. Checks that every record names a host system
that exists, uses a prototype id that is defined (seed or proposed), and is not
a duplicate -- then reports how much of the TE sample set is annotated so far.

Usage:
    python scripts/check_annotations.py
    python scripts/check_annotations.py --chunk 3     # only report on one chunk

Input:
    data/annotated/input/df_host_systems.parquet
    data/annotated/taxonomy/prototypes_seed_v3.json
    data/annotated/taxonomy/prototypes_proposed.jsonl
    data/annotated/annotations/family_assignments.jsonl
"""

import argparse
import collections
import json
import os
import sys

import pandas as pd

_PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANN_DIR = os.path.join(_PROJECT_DIR, 'data', 'annotated') + os.sep
HOSTS = ANN_DIR + 'input/df_host_systems.parquet'
SEED = ANN_DIR + 'taxonomy/prototypes_seed_v3.json'
PROPOSED = ANN_DIR + 'taxonomy/prototypes_proposed.jsonl'
LEDGER = ANN_DIR + 'annotations/family_assignments.jsonl'

REQUIRED = ('host_system', 'prototype_id', 'confidence', 'basis',
            'annotated_by', 'annotated_at')
CONFIDENCES = ('high', 'medium', 'low')


def read_jsonl(path):
    if not os.path.exists(path):
        return []
    out = []
    with open(path) as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                out.append((i, json.loads(line)))
            except json.JSONDecodeError as e:
                print(f'  ERROR {os.path.basename(path)}:{i}: bad JSON -- {e}')
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--chunk', type=int, help='report on a single chunk only')
    args = ap.parse_args()

    hosts = pd.read_parquet(HOSTS)
    total_samples = hosts.n_samples.sum()
    known_hosts = set(hosts.host_system)

    # --- Taxonomy integrity ------------------------------------------------
    tax = json.load(open(SEED))
    seed = tax['prototypes']
    seed_ids = {p['id'] for p in seed}
    tax_errors = []
    classes = set(tax.get('structural_classes', []))
    for p in seed:
        for k in (p.get('discriminate_from') or {}):
            if k not in seed_ids:
                tax_errors.append(f'prototype "{p["id"]}": discriminate_from '
                                  f'references undefined id "{k}"')
        c = p.get('structural_class')
        if c and c not in classes:
            tax_errors.append(f'prototype "{p["id"]}": unknown structural_class "{c}"')
        for hs in (p.get('example_host_systems') or []):
            if hs not in known_hosts:
                tax_errors.append(f'prototype "{p["id"]}": example_host_system '
                                  f'"{hs}" is not in the input table')
    proposed_ids = {r['id'] for _, r in read_jsonl(PROPOSED) if 'id' in r}
    valid_ids = seed_ids | proposed_ids

    records = read_jsonl(LEDGER)
    errors = []
    seen = {}
    for lineno, r in records:
        for k in REQUIRED:
            if k not in r or r[k] in (None, ''):
                errors.append(f'line {lineno}: missing required field "{k}"')
        h = r.get('host_system')
        if h and h not in known_hosts:
            errors.append(f'line {lineno}: unknown host_system "{h}"')
        if h in seen:
            errors.append(f'line {lineno}: duplicate host_system "{h}" '
                          f'(first at line {seen[h]})')
        elif h:
            seen[h] = lineno
        pid = r.get('prototype_id')
        if pid and pid not in valid_ids:
            errors.append(f'line {lineno}: undefined prototype_id "{pid}" '
                          f'-- add it to prototypes_proposed.jsonl first')
        c = r.get('confidence')
        if c and c not in CONFIDENCES:
            errors.append(f'line {lineno}: confidence "{c}" not in {CONFIDENCES}')

    # Hosts named by more than one prototype are genuinely mixed and must be
    # split per composition in stage 2 -- surfaced here so they are not missed.
    cited = collections.Counter(
        hs for p in seed for hs in (p.get('example_host_systems') or []))
    mixed = sorted(h for h, n in cited.items() if n > 1)
    cov = hosts[hosts.host_system.isin(cited)].n_samples.sum()

    print(f'Taxonomy : {len(seed_ids)} seed + {len(proposed_ids)} proposed '
          f'= {len(valid_ids)} prototype ids')
    if tax_errors:
        print(f'  {len(tax_errors)} taxonomy problem(s):')
        for e in tax_errors:
            print(f'    {e}')
    else:
        print(f'  integrity OK -- {len(cited)} host systems pre-cited as examples, '
              f'covering {cov/total_samples*100:.1f}% of samples')
    print(f'  {len(mixed)} host systems are named by >1 prototype '
          f'(split these per composition): {", ".join(mixed[:6])}'
          + (' ...' if len(mixed) > 6 else ''))
    print(f'Ledger   : {len(records)} records, {len(seen)} distinct host systems')

    if errors:
        print(f'\n{len(errors)} problem(s):')
        for e in errors:
            print(f'  {e}')
    else:
        print('Validation: OK')

    # --- Progress ----------------------------------------------------------
    done = hosts[hosts.host_system.isin(seen)]
    print(f'\nProgress : {len(done)}/{len(hosts)} host systems '
          f'({len(done)/len(hosts)*100:.1f}%), '
          f'{done.n_samples.sum()}/{total_samples} samples '
          f'({done.n_samples.sum()/total_samples*100:.2f}% of the TE set)')

    by_chunk = hosts.assign(done=hosts.host_system.isin(seen)).groupby('chunk')
    pending = [(c, int(g.done.sum()), len(g)) for c, g in by_chunk if not g.done.all()]
    if pending:
        c, d, n = pending[0]
        print(f'Next     : chunk {c:03d} ({d}/{n} done) -- '
              f'data/annotated/input/chunks/chunk_{c:03d}.md')
    else:
        print('Next     : all chunks complete')

    if records:
        # Count distinct host systems, so a duplicated line (already flagged
        # above) does not inflate the tally.
        first = {}
        for _, r in records:
            first.setdefault(r.get('host_system'), r)
        dist = collections.Counter(r.get('prototype_id') for r in first.values())
        conf = collections.Counter(r.get('confidence') for r in first.values())
        print(f'\nConfidence: ' + ', '.join(f'{k}={conf.get(k, 0)}' for k in CONFIDENCES))
        print(f'Top prototypes assigned:')
        for pid, n in dist.most_common(10):
            ns = hosts[hosts.host_system.isin(
                [h for h, r in first.items() if r.get('prototype_id') == pid])].n_samples.sum()
            print(f'  {n:4d} hosts  {ns:6d} samples  {pid}')

        changed = [r for _, r in records if r.get('supersedes_existing')]
        if changed:
            print(f'\nReclassified away from the existing label: {len(changed)} host systems')

    if args.chunk:
        g = hosts[hosts.chunk == args.chunk]
        missing = [h for h in g.host_system if h not in seen]
        print(f'\nChunk {args.chunk:03d}: {len(g)-len(missing)}/{len(g)} annotated')
        if missing:
            print('  missing: ' + ', '.join(missing))

    return 1 if (errors or tax_errors) else 0


if __name__ == '__main__':
    sys.exit(main())
