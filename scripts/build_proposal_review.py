#!/usr/bin/env python
"""List prototypes proposed during annotation, with the context to judge them.

A proposed prototype has been used already -- the process requires proposing
before use -- so review is about whether it should be folded into the seed
taxonomy, merged into an existing entry, or replaced.

Writes data/annotated/taxonomy/proposals_review.md with a fill-in block per
proposal; scripts/apply_proposal_review.py reads them back.

Usage:  python scripts/build_proposal_review.py
"""
import json, os
import pandas as pd

_P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANN = os.path.join(_P, 'data', 'annotated') + os.sep
PROP = ANN + 'taxonomy/prototypes_proposed.jsonl'
SEED = ANN + 'taxonomy/prototypes_seed_v3.json'
LEDGER = ANN + 'annotations/family_assignments.jsonl'
HOSTS = ANN + 'input/df_host_systems.parquet'
OUT = ANN + 'taxonomy/proposals_review.md'


def main():
    props = [json.loads(l) for l in open(PROP) if l.strip()]
    seed = {p['id']: p for p in json.load(open(SEED))['prototypes']}
    recs = [json.loads(l) for l in open(LEDGER) if l.strip()]
    hosts = pd.read_parquet(HOSTS).set_index('host_system')

    used, alt = {}, {}
    for r in recs:
        used.setdefault(r['prototype_id'], []).append(r)
        for a in (r.get('alt_prototype_ids') or []):
            alt.setdefault(a, []).append(r)

    def weight(p):
        return sum(int(hosts.loc[r['host_system'], 'n_samples'])
                   for r in used.get(p['id'], []) if r['host_system'] in hosts.index)

    props.sort(key=weight, reverse=True)
    lines = [
        '# Prototypes proposed during annotation', '',
        f'{len(props)} proposals, pending review. Each was **already used** -- the '
        'process requires proposing before use -- so the question is whether it '
        'belongs in the seed taxonomy as written, should be merged into an '
        'existing prototype, or should be replaced.', '',
        'Fill in the `decision` in each block and run '
        '`python scripts/apply_proposal_review.py`. Blocks left blank are skipped, '
        'so you can review a few at a time.', '',
        '`accept` folds it into prototypes_seed_v3.json. `merge` rewrites every '
        'assignment using it to point at `into` instead. `reject` does the same but '
        'flags those assignments for re-annotation.', '', '---', '']

    for p in props:
        u = used.get(p['id'], [])
        a = alt.get(p['id'], [])
        n = weight(p)
        lines += [f"## `{p['id']}` — {p.get('display_name','')}", '',
                  f"**{p.get('typical_space_group') or 'space group not given'}**"
                  f" · {p.get('structural_class') or 'class not given'}"
                  f" · proposed in chunk {p.get('proposed_from_chunk','?')}", '',
                  f"Primary for **{len(u)} host(s)**, {n} samples"
                  + (f"; listed as an alternative on {len(a)} more" if a else ''), '']
        for r in u:
            ns = int(hosts.loc[r['host_system'], 'n_samples']) if r['host_system'] in hosts.index else 0
            ex = hosts.loc[r['host_system'], 'example_compositions'][:80] if r['host_system'] in hosts.index else ''
            lines += [f"- `{r['host_system']}` ({ns} samples, {r['confidence']} confidence) — {ex}"]
        lines.append('')
        if p.get('notes'):
            for note in (p['notes'] if isinstance(p['notes'], list) else [p['notes']]):
                lines += [f'> {note}', '']
        df = p.get('discriminate_from') or {}
        if df:
            lines.append('**Distinguished from:**')
            for k, v in df.items():
                mark = '' if k in seed or any(x['id'] == k for x in props) else '  ⚠ unknown id'
                lines.append(f'- `{k}`{mark} — {v}')
            lines.append('')
        lines += ['```proposal', f'id: {p["id"]}',
                  'decision:        # accept | merge | reject',
                  'into:            # for merge/reject: the prototype id to use instead',
                  'notes:', '```', '', '---', '']

    with open(OUT, 'w') as f:
        f.write('\n'.join(lines) + '\n')
    print(f'{len(props)} proposals -> {OUT}')
    print(f'  covering {sum(weight(p) for p in props)} samples across '
          f'{sum(len(used.get(p["id"],[])) for p in props)} host systems')


if __name__ == '__main__':
    raise SystemExit(main())
