#!/usr/bin/env python
"""Check for the external reference datasets and explain how to obtain them.

Neither dataset is redistributed with this repository.

TEDesignLab states citation requirements but no redistribution licence, so the
spreadsheet is not tracked here and has been removed from the git history. The
Materials Project dump is CC BY 4.0 but too large to track usefully.

This script deliberately does NOT download anything. Both sources are fetched by
hand so that whoever runs the pipeline has seen the terms attached to them.

Usage:
    python scripts/fetch_reference_data.py          # report status
    python scripts/fetch_reference_data.py --check  # exit non-zero if missing
"""

import argparse
import hashlib
import os
import sys

_P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF = os.path.join(_P, 'data', 'reference')

SOURCES = [
    {
        'file': 'tedesignlab-complete-data.xlsx',
        'name': 'TEDesignLab',
        'required': True,
        # The copy this project's committed outputs were generated from. A fresh
        # download may legitimately differ if the source sheet has been updated,
        # so a mismatch is a warning, not an error.
        'sha256': '458f95c59fccde1b5fa43c849a11030131f1f677323341e665a49dee27d71e3d',
        'size_hint': '~426 KB, 2,701 rows',
        'url': 'https://www.prashungorai.org/tedesignlab/',
        'steps': [
            'Open https://www.prashungorai.org/tedesignlab/',
            'Follow the "Download Database (CSV)" link, which opens a Google Sheet:',
            '  https://docs.google.com/spreadsheets/d/197XDCG0jPNDocvfdYuODBWW51ftmhMMECRYznQpX3xs/edit',
            'File -> Download -> Microsoft Excel (.xlsx)',
            f'Save it as  data/reference/tedesignlab-complete-data.xlsx',
        ],
        'terms': ('Citation required. The tabulated quantities come from five papers, '
                  'identified per row by the `cite` column; see data/reference/CITATIONS.md. '
                  'No redistribution licence is stated, which is why this file is not '
                  'shipped with the repository.'),
    },
    {
        'file': 'mp_190822.csv',
        'name': 'Materials Project (2019-08-22 dump)',
        'required': False,
        'sha256': None,
        'size_hint': '~35 MB, 119,570 entries',
        'url': 'https://materialsproject.org/',
        'steps': [
            'Obtain a Materials Project snapshot with columns: material_id,',
            '  pretty_formula, elements, nelements, spacegroup, e_above_hull,',
            '  band_gap, icsd_ids',
            'Save it as  data/reference/mp_190822.csv',
            'Newer snapshots work but will shift the numbers in the committed outputs.',
        ],
        'terms': ('CC BY 4.0. Cite Jain et al., APL Materials 1, 011002 (2013). '
                  'Not tracked here because of its size.'),
    },
]


def sha256(path, chunk=1 << 20):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(chunk), b''):
            h.update(b)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true',
                    help='exit non-zero if a required file is missing')
    args = ap.parse_args()

    missing_required = False
    for s in SOURCES:
        path = os.path.join(REF, s['file'])
        tag = 'required' if s['required'] else 'optional'
        if os.path.exists(path):
            note = ''
            if s['sha256']:
                got = sha256(path)
                note = ('  [matches the copy the committed outputs were built from]'
                        if got == s['sha256'] else
                        f'\n    NOTE: sha256 differs from the reference copy.\n'
                        f'      expected {s["sha256"]}\n'
                        f'      found    {got}\n'
                        f'      A newer download is fine, but numbers may shift.')
            print(f'  present  {s["name"]}  ({s["file"]}){note}')
        else:
            print(f'  MISSING  {s["name"]}  ({tag}, {s["size_hint"]})')
            for line in s['steps']:
                print(f'             {line}')
            print(f'             terms: {s["terms"]}')
            if s['required']:
                missing_required = True
        print()

    if missing_required:
        print('At least one required reference dataset is missing.')
        print('build_structure_reference.py cannot run without it.')
        return 1 if args.check else 0
    return 0


if __name__ == '__main__':
    sys.exit(main())
