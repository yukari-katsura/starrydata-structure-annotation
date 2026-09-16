#!/usr/bin/env python
"""Read the filled-in ```finding``` blocks from needs_review.md into the ledger.

Workflow:
  1. python scripts/build_review_queue.py     -> validation/needs_review.md
  2. read a paper, fill in that host's finding block
  3. python scripts/apply_review_findings.py  -> writes it into the ledger
  4. python scripts/build_review_queue.py     -> regenerate; settled hosts drop out

Blocks still holding their placeholder comments are skipped, so a partly worked
file is fine. Applying a finding sets experimentally_confirmed=true and records
the DOI, which is what moves an assignment from candidate to confirmed.

Usage:
    python scripts/apply_review_findings.py            # apply
    python scripts/apply_review_findings.py --dry-run  # show what would change
"""

import argparse
import json
import os
import re
import shutil
from datetime import date

_P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANN = os.path.join(_P, 'data', 'annotated') + os.sep
REVIEW = ANN + 'validation/needs_review.md'
LEDGER = ANN + 'annotations/family_assignments.jsonl'
TAX = ANN + 'taxonomy/prototypes_seed_v3.json'

VALID_DECISIONS = {'confirm', 'change', 'split', 'unresolved'}


def parse_blocks(text):
    """Pull every ```finding ... ``` block into a dict."""
    out = []
    for body in re.findall(r'```finding\n(.*?)```', text, re.S):
        d, splits = {}, {}
        in_split = False
        for raw in body.splitlines():
            line = raw.rstrip()
            if not line.strip():
                continue
            if in_split and (line.startswith('  ') or line.startswith('\t')):
                t = line.strip()
                if t.startswith('#') or '->' not in t:
                    continue
                comp, proto = [x.strip() for x in t.split('->', 1)]
                if comp and proto:
                    splits[comp] = proto
                continue
            in_split = False
            if ':' not in line:
                continue
            k, v = line.split(':', 1)
            k = k.strip()
            v = v.split('#')[0].strip()          # drop the placeholder comment
            if k == 'split':
                in_split = True
                continue
            if v:
                d[k] = v
        if splits:
            d['split'] = splits
        if d.get('host'):
            out.append(d)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    if not os.path.exists(REVIEW):
        print(f'{REVIEW} not found. Run build_review_queue.py first.')
        return 1

    valid_protos = {p['id'] for p in json.load(open(TAX))['prototypes']}
    records = [json.loads(l) for l in open(LEDGER) if l.strip()]
    by_host = {r['host_system']: r for r in records}

    findings = parse_blocks(open(REVIEW).read())
    applied, skipped, errors = [], [], []

    for f in findings:
        host = f['host']
        dec = f.get('decision')
        # An untouched block has only the host line; that is a skip, not an error.
        if not dec and 'split' not in f:
            skipped.append(host)
            continue
        if host not in by_host:
            errors.append(f'{host}: not in the ledger')
            continue
        if dec and dec not in VALID_DECISIONS:
            errors.append(f'{host}: decision "{dec}" not in {sorted(VALID_DECISIONS)}')
            continue
        r = by_host[host]
        changes = []

        if dec == 'change':
            new = f.get('prototype')
            if not new:
                errors.append(f'{host}: decision=change needs a prototype')
                continue
            if new not in valid_protos:
                errors.append(f'{host}: prototype "{new}" is not in the taxonomy')
                continue
            changes.append(f'prototype {r["prototype_id"]} -> {new}')
            r['prototype_id'] = new

        if f.get('split'):
            bad = [p for p in f['split'].values() if p not in valid_protos]
            if bad:
                errors.append(f'{host}: unknown prototype(s) in split: {bad}')
                continue
            r['composition_split'] = f['split']
            r['is_mixed'] = True
            changes.append(f'split into {len(f["split"])} prototypes')

        if f.get('spacegroup') or f.get('mp_id'):
            phases = r.get('phases') or [{}]
            if f.get('spacegroup'):
                try:
                    phases[0]['spacegroup_number'] = int(f['spacegroup'])
                except ValueError:
                    errors.append(f'{host}: spacegroup "{f["spacegroup"]}" is not a number')
                    continue
            if f.get('mp_id'):
                phases[0]['mp_id'] = f['mp_id']
            phases[0]['confidence'] = 'high'
            r['phases'] = phases
            changes.append('structure fixed from the paper')

        if f.get('transition_K'):
            v = f['transition_K'].strip().lower()
            for ph in r.get('phases') or []:
                if v in ('none', 'no', 'n/a'):
                    ph['transition_K'] = None
                    ph['transition_basis'] = 'paper_evidence'
                elif ph.get('transition_K'):
                    try:
                        ph['transition_K'] = float(v)
                    except ValueError:
                        pass
                    ph['transition_basis'] = 'paper_evidence'
            r['spans_transition'] = v not in ('none', 'no', 'n/a')
            changes.append(f'transition = {v} (from the paper)')

        if dec == 'confirm':
            changes.append('assignment confirmed')
        if dec == 'unresolved':
            r['confidence'] = 'low'
            changes.append('marked unresolved after reading')

        if dec and dec != 'unresolved':
            r['confidence'] = 'high'
            r['experimentally_confirmed'] = True
            ab = set(r.get('assignment_basis') or [])
            ab.add('paper_evidence')
            r['assignment_basis'] = sorted(ab)
        if f.get('evidence'):
            r['evidence'] = f['evidence']
        if f.get('notes'):
            r['review_notes'] = f['notes']
        r['reviewed_by'] = 'user'
        r['reviewed_at'] = date.today().isoformat()
        applied.append((host, changes))

    print(f'{len(findings)} finding blocks in the file')
    print(f'  {len(applied)} filled in, {len(skipped)} left blank, {len(errors)} with problems')
    for h, ch in applied:
        print(f'    {h}: ' + '; '.join(ch))
    for e in errors:
        print(f'    ERROR {e}')

    if errors:
        print('\nNothing written -- fix the problems above and re-run.')
        return 1
    if not applied:
        print('\nNo findings to apply.')
        return 0
    if args.dry_run:
        print('\nDry run: ledger unchanged.')
        return 0

    shutil.copy(LEDGER, LEDGER + '.bak')
    with open(LEDGER, 'w') as fh:
        fh.write('\n'.join(json.dumps(r) for r in records) + '\n')
    print(f'\nWrote {LEDGER} (previous version at {os.path.basename(LEDGER)}.bak)')
    print('Now re-run:  python scripts/build_annotated_samples.py')
    print('             python scripts/build_review_queue.py')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
