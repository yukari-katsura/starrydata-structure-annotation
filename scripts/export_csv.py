#!/usr/bin/env python
"""Export the annotation tables as CSV for tools that do not read Parquet.

Parquet stays the source of truth: it preserves dtypes, nulls and nested values,
and is a third the size. CSV is a convenience copy.

Two columns hold JSON (phases_json, dopants_json). --flat drops them and
promotes the fields most people want -- the room-temperature phase and the
principal dopant -- into plain columns, which is usually what a spreadsheet
needs.

Usage:
    python scripts/export_csv.py           # faithful copy, all columns
    python scripts/export_csv.py --flat    # spreadsheet-friendly
    python scripts/export_csv.py --both
"""

import argparse
import json
import os

import pandas as pd

_P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANN = os.path.join(_P, 'data', 'annotated') + os.sep
# (stem, subdirectory it lives in). Tables without JSON columns are exported
# once; --flat is a no-op for them.
TABLES = [('df_annotated_samples', ''),
          ('df_annotated_compositions', ''),
          ('df_tedl_linked_samples', ''),
          ('df_tedl_entries', 'input/')]


def flatten(d):
    """Promote the useful bits of the JSON columns into plain columns."""
    out = d.copy()
    lo_sg, lo_mp, tr = [], [], []
    for s in out.get('phases_json', pd.Series([None] * len(out))):
        try:
            ph = json.loads(s) if isinstance(s, str) else []
        except Exception:
            ph = []
        first = ph[0] if ph else {}
        lo_sg.append(first.get('spacegroup_number'))
        lo_mp.append(first.get('mp_id'))
        tr.append(first.get('transition_K'))
    out['phase1_spacegroup'] = lo_sg
    out['phase1_mp_id'] = lo_mp
    out['phase1_transition_K'] = tr

    el, role, site, frac = [], [], [], []
    for s in out.get('dopants_json', pd.Series([None] * len(out))):
        try:
            dp = json.loads(s) if isinstance(s, str) else []
        except Exception:
            dp = []
        top = dp[0] if dp else {}
        el.append(top.get('element'))
        role.append(top.get('role'))
        site.append(top.get('substitutes_for'))
        frac.append(top.get('site_fraction'))
    out['dopant1_element'] = el
    out['dopant1_role'] = role
    out['dopant1_substitutes_for'] = site
    out['dopant1_site_fraction'] = frac
    return out.drop(columns=[c for c in ('phases_json', 'dopants_json')
                             if c in out.columns])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--flat', action='store_true')
    ap.add_argument('--both', action='store_true')
    args = ap.parse_args()
    modes = ['full', 'flat'] if args.both else (['flat'] if args.flat else ['full'])

    outdir = ANN + 'csv' + os.sep
    os.makedirs(outdir, exist_ok=True)
    for stem, sub in TABLES:
        src = ANN + sub + stem + '.parquet'
        if not os.path.exists(src):
            continue
        d = pd.read_parquet(src)
        has_json = any(c in d.columns for c in ('phases_json', 'dopants_json'))
        # nothing to flatten in a table with no JSON columns
        tbl_modes = modes if has_json else ['full']
        for m in dict.fromkeys(tbl_modes):
            out = flatten(d) if m == 'flat' else d
            name = f'{stem}{"_flat" if m == "flat" else ""}.csv'
            path = outdir + name
            out.to_csv(path, index=False)
            mb = os.path.getsize(path) / 1e6
            pq = os.path.getsize(src) / 1e6
            print(f'  {name:42s} {len(out):6d} rows x {len(out.columns):2d} cols  '
                  f'{mb:5.1f} MB  (parquet {pq:.1f} MB)')
    print(f'\n  -> {outdir}')
    print('  Parquet remains the source of truth; CSV loses dtypes and nulls.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
