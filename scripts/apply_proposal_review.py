#!/usr/bin/env python
"""Apply the decisions in proposals_review.md.

  accept  fold the proposal into prototypes_seed_v3.json and drop it from the
          pending queue
  merge   rewrite every assignment using it to point at `into` instead
  reject  same as merge, but the affected assignments are flagged for
          re-annotation rather than treated as settled

Blocks with no decision are skipped, so review can be done a few at a time.
Backs up the files it changes.

Usage:  python scripts/apply_proposal_review.py [--dry-run]
"""
import argparse, json, os, re, shutil
from datetime import date

_P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANN = os.path.join(_P, 'data', 'annotated') + os.sep
REVIEW = ANN + 'taxonomy/proposals_review.md'
PROP = ANN + 'taxonomy/prototypes_proposed.jsonl'
SEED = ANN + 'taxonomy/prototypes_seed_v3.json'
LOG = ANN + 'taxonomy/proposals_log.jsonl'
LEDGER = ANN + 'annotations/family_assignments.jsonl'
VALID = {'accept', 'merge', 'reject'}


def parse(text):
    out = []
    for body in re.findall(r'```proposal\n(.*?)```', text, re.S):
        d = {}
        for line in body.splitlines():
            if ':' not in line:
                continue
            k, v = line.split(':', 1)
            v = v.split('#')[0].strip()
            if v:
                d[k.strip()] = v
        if d.get('id') and d.get('decision'):
            out.append(d)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    if not os.path.exists(REVIEW):
        print(f'{REVIEW} not found. Run build_proposal_review.py first.')
        return 1
    props = {json.loads(l)['id']: json.loads(l) for l in open(PROP) if l.strip()}
    seed = json.load(open(SEED))
    seed_ids = {p['id'] for p in seed['prototypes']}
    recs = [json.loads(l) for l in open(LEDGER) if l.strip()]
    decisions = parse(open(REVIEW).read())

    errs, actions = [], []
    for d in decisions:
        pid, dec, into = d['id'], d['decision'], d.get('into')
        if dec not in VALID:
            errs.append(f'{pid}: decision "{dec}" not in {sorted(VALID)}'); continue
        if pid not in props:
            errs.append(f'{pid}: not in the pending queue'); continue
        if dec in ('merge', 'reject'):
            if not into:
                errs.append(f'{pid}: {dec} needs "into"'); continue
            if into not in seed_ids and into not in props:
                errs.append(f'{pid}: target "{into}" is not a known prototype'); continue
        actions.append((pid, dec, into, d.get('notes')))

    for pid, dec, into, notes in actions:
        n = sum(1 for r in recs if r['prototype_id'] == pid
                or pid in (r.get('alt_prototype_ids') or []))
        print(f'  {dec:7s} {pid:26s} affects {n} assignment(s)'
              + (f' -> {into}' if into else ''))
    for e in errs:
        print(f'  ERROR {e}')
    if errs:
        print('\nNothing written -- fix the errors above.'); return 1
    if not actions:
        print('No decisions filled in.'); return 0
    if args.dry_run:
        print('\nDry run: nothing written.'); return 0

    for f in (PROP, SEED, LEDGER):
        shutil.copy(f, f + '.bak')

    logged = []
    for pid, dec, into, notes in actions:
        p = props.pop(pid)
        p.update(status=dec, reviewed_by='user', reviewed_at=date.today().isoformat(),
                 review_notes=notes)
        if dec == 'accept':
            e = {k: v for k, v in p.items() if k not in
                 ('status', 'proposed_by', 'proposed_at', 'proposed_from_chunk',
                  'reviewed_by', 'reviewed_at', 'review_notes')}
            e['merged_from'] = [f'v3 (proposed in chunk {p.get("proposed_from_chunk","?")}, '
                                f'accepted by the user)']
            seed['prototypes'].append(e)
        else:
            p['replaced_by'] = into
            for r in recs:
                if r['prototype_id'] == pid:
                    r['prototype_id'] = into
                    if dec == 'reject':
                        r['confidence'] = 'low'
                        r['needs_reannotation'] = f'proposal {pid} rejected in review'
                r['alt_prototype_ids'] = [into if a == pid else a
                                          for a in (r.get('alt_prototype_ids') or [])]
        logged.append(p)

    with open(PROP, 'w') as f:
        f.write('\n'.join(json.dumps(v) for v in props.values()) + ('\n' if props else ''))
    json.dump(seed, open(SEED, 'w'), indent=1)
    with open(LEDGER, 'w') as f:
        f.write('\n'.join(json.dumps(r) for r in recs) + '\n')
    with open(LOG, 'a') as f:
        for p in logged:
            f.write(json.dumps(p) + '\n')

    print(f'\nApplied {len(actions)}. Seed now {len(seed["prototypes"])} prototypes, '
          f'{len(props)} still pending.')
    print('Re-run: build_proposal_review.py, then verify_assignments.py')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
