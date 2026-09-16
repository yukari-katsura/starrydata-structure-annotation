#!/usr/bin/env python
"""Split mixed host systems into per-composition prototypes by stoichiometry.

A host was flagged `is_mixed` when one label stood over several real structures.
For most of them the composition already decides which: Ca3Co4O9 and Ca3Co2O6
differ by their Co:Ca ratio, FeSi2 and FeSi by Si:Fe, Bi2Te3 and BiTe by Bi:Te.
Those are chemistry inferences, not measurements, so this resolves them from
composition and materials knowledge and records them as such.

IMPORTANT: this does NOT set experimentally_confirmed. These remain candidate
structures. It narrows what still needs a paper; it does not replace one.

Rules are element-ratio thresholds evaluated against the parsed fractional
composition, tried in order, with a fallback. Hosts with no rule keep their host
level assignment and stay flagged.

Output:
    data/annotated/annotations/composition_assignments.parquet
    updates `composition_split_rule` on the ledger records it resolves

Usage:  python scripts/apply_composition_splits.py [--dry-run]
"""

import argparse
import json
import os
import re

import pandas as pd

_P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANN = os.path.join(_P, 'data', 'annotated') + os.sep
LEDGER = ANN + 'annotations/family_assignments.jsonl'
COMPS = ANN + 'input/df_compositions.parquet'
TAX = ANN + 'taxonomy/prototypes_seed_v3.json'
OUT = ANN + 'annotations/composition_assignments.parquet'

# Rare-earth, alkaline-earth and other guests that occupy the skutterudite void.
FILLERS = set('La Ce Pr Nd Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Y Ca Sr Ba In Tl Na K Li U'.split())
ALKALI_AE = set('Li Na K Rb Cs Ca Sr Ba'.split())


def ratio(f, a, b):
    """Atomic ratio a:b, or None when either is absent."""
    if isinstance(a, str):
        a = [a]
    if isinstance(b, str):
        b = [b]
    na = sum(f.get(x, 0.0) for x in a)
    nb = sum(f.get(x, 0.0) for x in b)
    return na / nb if nb > 0 else None


def has(f, els):
    return any(f.get(e, 0.0) > 0 for e in els)


# host -> (rules, fallback). Each rule is (predicate, prototype_id, confidence).
# The comment on each rule is the chemistry it encodes.
RULES = {
    # filler in the icosahedral void makes it a filled skutterudite
    'Co-Sb': ([(lambda f: has(f, FILLERS), 'filled_skutterudite', 'high')],
              ('skutterudite', 'high')),
    'Fe-Sb': ([(lambda f: has(f, FILLERS) or (ratio(f, 'Sb', 'Fe') or 0) > 2.5,
                'filled_skutterudite', 'high')], ('marcasite', 'high')),
    # Ca3Co4O9 (Co/Ca 1.33) misfit vs Ca3Co2O6 (0.67) chain
    'Ca-Co-O': ([(lambda f: (ratio(f, 'Co', 'Ca') or 0) <= 0.85, 'ca3co2o6_chain', 'high'),
                 (lambda f: (ratio(f, 'Co', 'Ca') or 0) >= 1.15, 'misfit_cobaltite', 'high')],
                ('misfit_cobaltite', 'medium')),
    # Bi sits in the rocksalt block of the Bi-based misfits, so Co:Ca runs lower
    # than in Ca3Co4O9 and the Ca-Co-O threshold does not transfer here.
    'Bi-Ca-Co-O': ([], ('misfit_cobaltite', 'high')),
    # A:B > 1 means an extra AO rocksalt layer -- Ruddlesden-Popper
    'O-Sr-Ti': ([(lambda f: (ratio(f, 'Sr', 'Ti') or 0) > 1.15, 'ruddlesden_popper', 'high')],
                ('perovskite', 'high')),
    'Ca-Mn-O': ([(lambda f: (ratio(f, 'Ca', 'Mn') or 0) > 1.15, 'ruddlesden_popper', 'high'),
                 (lambda f: (ratio(f, 'Ca', 'Mn') or 0) < 0.75, 'unresolved_crystalline', 'low')],
                ('perovskite', 'high')),
    'La-Mn-O-Sr': ([(lambda f: (ratio(f, ['La', 'Sr'], 'Mn') or 0) > 1.15,
                     'ruddlesden_popper', 'high')], ('perovskite', 'high')),
    'O-Ru-Sr': ([(lambda f: (ratio(f, 'Sr', 'Ru') or 0) > 1.15, 'ruddlesden_popper', 'high')],
                ('perovskite', 'high')),
    'Cu-La-O': ([(lambda f: (ratio(f, ['La', 'Sr', 'Ba', 'Nd'], 'Cu') or 0) >= 1.5,
                  'ruddlesden_popper', 'high')], ('perovskite', 'medium')),
    'Nd-Ni-O': ([(lambda f: (ratio(f, 'Nd', 'Ni') or 0) >= 1.5, 'ruddlesden_popper', 'high')],
                ('perovskite', 'high')),
    'La-Ni-O': ([(lambda f: (ratio(f, 'La', 'Ni') or 0) >= 1.5, 'ruddlesden_popper', 'high')],
                ('perovskite', 'high')),
    'Fe-O-Sr': ([(lambda f: (ratio(f, 'Sr', 'Fe') or 0) > 1.15, 'ruddlesden_popper', 'high'),
                 (lambda f: (ratio(f, 'O', ['Sr', 'Fe']) or 9) < 1.4, 'brownmillerite', 'medium')],
                ('perovskite', 'high')),
    'Ir-O-Sr': ([(lambda f: (ratio(f, 'Sr', 'Ir') or 0) > 1.15, 'ruddlesden_popper', 'high')],
                ('perovskite', 'medium')),
    'Ba-Fe-O': ([(lambda f: (ratio(f, 'O', ['Ba', 'Fe']) or 9) < 1.4, 'brownmillerite', 'medium')],
                ('perovskite', 'high')),
    'Co-O-Sr': ([(lambda f: (ratio(f, 'Sr', 'Co') or 0) >= 1.15, 'ca3co2o6_chain', 'medium'),
                 (lambda f: (ratio(f, 'O', ['Sr', 'Co']) or 9) < 1.4, 'brownmillerite', 'medium')],
                ('perovskite', 'high')),
    # A2B3 is tetradymite; richer in the metal means a homologue
    'Bi-Te': ([(lambda f: (ratio(f, 'Bi', 'Te') or 0) > 0.75, 'homologous_tetradymite', 'high')],
              ('tetradymite', 'high')),
    'Bi-Se': ([(lambda f: (ratio(f, 'Bi', 'Se') or 0) > 0.75, 'homologous_tetradymite', 'high')],
              ('tetradymite', 'high')),
    'Sb-Zn': ([(lambda f: (ratio(f, 'Zn', 'Sb') or 0) >= 1.15, 'zn4sb3', 'high')],
              ('znsb_cdsb', 'high')),
    'Fe-Si': ([(lambda f: (ratio(f, 'Si', 'Fe') or 0) >= 1.5, 'beta_fesi2', 'high')],
              ('b20_fesi', 'high')),
    'Mn-Si': ([(lambda f: (ratio(f, 'Si', 'Mn') or 0) >= 1.4, 'hms_chimney_ladder', 'high')],
              ('b20_fesi', 'high')),
    'Co-Si': ([(lambda f: (ratio(f, 'Si', 'Co') or 0) >= 1.5, 'beta_fesi2', 'low')],
              ('b20_fesi', 'high')),
    'Ni-Sn-Ti': ([(lambda f: (ratio(f, 'Ni', 'Ti') or 0) >= 1.6, 'full_heusler', 'high')],
                 ('half_heusler', 'high')),
    'Se-Sn': ([(lambda f: (ratio(f, 'Se', 'Sn') or 0) >= 1.6, 'cdi2_1t', 'high')],
              ('layered_ges', 'high')),
    'S-Sn': ([(lambda f: (ratio(f, 'S', 'Sn') or 0) >= 1.6, 'cdi2_1t', 'high')],
             ('layered_ges', 'high')),
    'In-Se': ([(lambda f: (ratio(f, 'In', 'Se') or 0) >= 1.15, 'in4se3', 'high')],
              ('layered_in2se3', 'high')),
    'Fe-O': ([(lambda f: (ratio(f, 'O', 'Fe') or 0) >= 1.45, 'corundum', 'high')],
             ('spinel', 'high')),
    # Ge-rich chalcogenide glass, GST homologue, or plain GeTe
    'Ge-Te': ([(lambda f: (ratio(f, 'Te', 'Ge') or 0) >= 2.0, 'amorphous', 'medium'),
               (lambda f: (ratio(f, 'Sb', 'Ge') or 0) > 0.05, 'gst_homologous', 'high')],
              ('gete_rhombohedral', 'high')),
    'C': ([(lambda f: has(f, ['K', 'Rb', 'Cs']), 'fulleride_a3c60', 'high')],
          ('graphite_layered', 'high')),
    # Ti-O and V-O are oxidation-state series; the O:M ratio names the phase
    'O-Ti': ([(lambda f: (ratio(f, 'O', 'Ti') or 0) <= 1.15, 'rocksalt_oxide', 'high'),
              (lambda f: 1.4 <= (ratio(f, 'O', 'Ti') or 0) <= 1.6, 'corundum', 'high'),
              (lambda f: 1.6 < (ratio(f, 'O', 'Ti') or 0) < 1.9, 'magneli_phase', 'high')],
             ('rutile', 'medium')),
    'O-V': ([(lambda f: has(f, ALKALI_AE), 'vanadium_bronze', 'high'),
             (lambda f: (ratio(f, 'O', 'V') or 0) >= 2.4, 'v2o5_layered', 'high'),
             (lambda f: 1.4 <= (ratio(f, 'O', 'V') or 0) <= 1.6, 'corundum', 'high'),
             (lambda f: 1.6 < (ratio(f, 'O', 'V') or 0) < 1.9, 'magneli_phase', 'high')],
            ('vo2_monoclinic', 'medium')),
    'Mo-O': ([(lambda f: has(f, ALKALI_AE), 'tungsten_bronze', 'high'),
              (lambda f: (ratio(f, 'O', 'Mo') or 0) <= 2.1, 'rutile', 'high')],
             ('magneli_phase', 'medium')),
    # tetrahedrite Cu12Sb4S13 (S/Sb 3.25) vs famatinite Cu3SbS4 (4)
    'Cu-S-Sb': ([(lambda f: (ratio(f, 'S', 'Sb') or 0) >= 3.7, 'famatinite', 'high')],
                ('tetrahedrite', 'high')),
    'Cu-Sb-Se': ([(lambda f: (ratio(f, 'Se', 'Sb') or 0) >= 3.5, 'famatinite', 'high'),
                  (lambda f: (ratio(f, 'Se', 'Sb') or 0) < 2.5, 'unresolved_crystalline', 'low')],
                 ('skinnerite_cu3sbse3', 'high')),
    # Cu5FeS4 bornite is neither chalcopyrite nor tetrahedrite; it has no
    # taxonomy entry, so it is parked rather than mislabelled.
    'Cu-Fe-S': ([(lambda f: (ratio(f, 'Cu', 'Fe') or 0) >= 3.0,
                  'unresolved_crystalline', 'low')], ('chalcopyrite', 'high')),
    'Cu-Fe-O': ([(lambda f: (ratio(f, 'Fe', 'Cu') or 0) >= 1.5, 'spinel', 'high')],
                ('delafossite', 'high')),
    'Cu-O': ([(lambda f: (ratio(f, 'O', 'Cu') or 0) < 0.75, 'cuprite', 'high')],
             ('tenorite', 'high')),
    'Ba-Ga-Sn': ([(lambda f: True, 'clathrate_viii', 'medium')], ('clathrate_viii', 'medium')),
    'Ag-Se': ([(lambda f: True, 'ag2se_naumannite', 'high')], ('ag2se_naumannite', 'high')),
    'Ag-Te': ([(lambda f: True, 'ag2se_naumannite', 'high')], ('ag2se_naumannite', 'high')),
    'Sb-Yb-Zn': ([(lambda f: (ratio(f, 'Yb', 'Zn') or 0) >= 1.5, 'zintl_9_4_9', 'high')],
                 ('caal2si2_zintl', 'high')),
    'Sb-Yb': ([(lambda f: (ratio(f, 'Yb', 'Sb') or 0) >= 1.15, 'yb14mnsb11_zintl', 'medium')],
              ('yb14mnsb11_zintl', 'medium')),
    'Nb-O-Sr': ([(lambda f: (ratio(f, 'Nb', 'Sr') or 0) >= 1.6, 'tungsten_bronze', 'high'),
                 (lambda f: (ratio(f, 'O', ['Sr', 'Nb']) or 0) >= 2.0,
                  'block_shear_niobate', 'medium')], ('perovskite', 'medium')),
    # colusite carries a transition-metal framework site (V/Nb/Ta)
    'Cu-S-Sn': ([(lambda f: has(f, ['V', 'Nb', 'Ta']), 'colusite', 'high')],
                ('cu2gese3', 'high')),
    'Ba-Co-O': ([(lambda f: (ratio(f, 'Co', 'Ba') or 0) >= 3.0,
                  'unresolved_crystalline', 'low')], ('perovskite', 'medium')),
    # ordered-vacancy chalcopyrites run Ga-rich against Cu
    'Cu-Ga-Te': ([(lambda f: (ratio(f, 'Ga', 'Cu') or 0) >= 1.4,
                   'unresolved_crystalline', 'low')], ('chalcopyrite', 'high')),
    # YB66 and the RE-B22C2N frameworks are not the B4C type
    'B': ([(lambda f: has(f, ['Y', 'Yb', 'Er', 'Sm', 'Tb']),
            'unresolved_crystalline', 'low')], ('boron_carbide', 'medium')),
    'B-C': ([(lambda f: has(f, ['Y', 'Yb', 'Er', 'N']),
              'unresolved_crystalline', 'low')], ('boron_carbide', 'high')),
    'Fe-Se': ([(lambda f: (ratio(f, 'Se', 'Fe') or 0) >= 1.6, 'marcasite', 'high')],
              ('fese_pbo', 'medium')),
    'Ce-Cu': ([(lambda f: (ratio(f, 'Cu', 'Ce') or 0) < 4.0, 'unresolved_crystalline', 'low')],
              ('cecu6', 'high')),
}

# Hosts whose alt list was redundant: the competing entries are the same
# prototype, so they were never really mixed.
NOT_ACTUALLY_MIXED = {'Ba-Cu-O-Y'}


# Phrases in the curator's composition_details that name a structure outright.
#
# Each rule is SCOPED to the chemistry it can apply to. Without that scope the
# rule fires on second-phase additives and mislabels the host: a graphene
# composite of SrTiO3 mentions "graphene", a CNT composite of MnSi1.75 mentions
# "nanotube", and matching those as the host structure is nonsense. Scoping is
# what makes this field usable at all.
#
# scope: (host_system or None, reduced_formula or None) -- both must match when set.
DETAIL_RULES = [
    (r'nanocrystalline diamond|\bdiamond\b|\bNDE\b|\bNCD\b|\bUNCD\b',
     'diamond_cubic', 'high', ('C', None)),
    (r'fulleride|\bC60\b|fullerene', 'fulleride_a3c60', 'high', ('C', None)),
    (r'graphene|graphite|nanotube|\bCNT\b|carbon fib|soft carbon|hard carbon|'
     r'rayon-based carbon|carbon black|glassy carbon',
     'graphite_layered', 'high', ('C', None)),
    (r'\banatase\b', 'anatase', 'high', (None, 'TiO2')),
    (r'\brutile\b', 'rutile', 'high', (None, 'TiO2')),
    (r'\bmagnetite\b', 'spinel', 'high', (None, 'Fe3O4')),
    (r'\bmaghemite\b', 'spinel', 'high', (None, 'Fe2O3')),
    (r'\bhematite\b', 'corundum', 'high', (None, 'Fe2O3')),
    (r'\bbornite\b', 'unresolved_crystalline', 'medium', (None, 'Cu5FeS4')),
    (r'\btetrahedrite\b', 'tetrahedrite', 'high', ('Cu-S-Sb', None)),
    (r'quasicrystal|quasi-crystal|icosahedral phase', 'quasicrystal_approximant',
     'high', (None, None)),
]

# Phases distinguishable only by a prefix that the composition string does not
# carry. alpha-Fe2O3 is hematite (corundum) and gamma-Fe2O3 is maghemite
# (spinel) -- same formula, different structure -- so this cannot be decided per
# composition. Where a composition's samples disagree, it is flagged for
# sample-level treatment rather than forced to one answer.
POLYMORPH_PREFIX = {
    'Fe2O3': [(r'(?:^|[^a-z])(?:γ|gamma)\s*-?\s*Fe2O3|maghemite', 'spinel'),
              (r'(?:^|[^a-z])(?:α|alpha)\s*-?\s*Fe2O3|hematite', 'corundum')],
}


def detail_override(texts, host, formula, valid):
    """Return (prototype, confidence, phrase) when the curator names a structure.

    Returns None when the texts disagree, which is itself information: the
    composition covers more than one phase and needs sample-level resolution.
    """
    # same formula, different polymorph named by prefix
    for pat_list in [POLYMORPH_PREFIX.get(formula, [])]:
        found = set()
        phrase = None
        for txt in texts:
            if not isinstance(txt, str):
                continue
            for pat, proto in pat_list:
                m = re.search(pat, txt, re.I)
                if m:
                    found.add(proto)
                    phrase = m.group(0).strip()
        if len(found) == 1:
            p = found.pop()
            return (p, 'high', phrase) if p in valid else None
        if len(found) > 1:
            return ('__AMBIGUOUS__', 'low', 'both polymorph prefixes present')

    for txt in texts:
        if not isinstance(txt, str) or not txt.strip():
            continue
        for pat, proto, conf, (sc_host, sc_form) in DETAIL_RULES:
            if sc_host and host != sc_host:
                continue
            if sc_form and formula != sc_form:
                continue
            m = re.search(pat, txt, re.I)
            if m and proto in valid:
                return proto, conf, m.group(0).strip()
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    valid = {p['id'] for p in json.load(open(TAX))['prototypes']}
    bad = {p for _, (rs, fb) in RULES.items() for p in
           [r[1] for r in rs] + [fb[0]] if p not in valid}
    if bad:
        print(f'ERROR: rules reference prototypes not in the taxonomy: {sorted(bad)}')
        return 1

    records = [json.loads(l) for l in open(LEDGER) if l.strip()]
    by_host = {r['host_system']: r for r in records}
    comp = pd.read_parquet(COMPS)

    # curator free text, keyed by composition; overrides the ratio rules
    det_path = os.path.join(_P, 'data', 'processed', 'df_composition_details.parquet')
    details = {}
    if os.path.exists(det_path):
        dd = pd.read_parquet(det_path)
        for c, t in zip(dd.composition, dd.composition_details):
            details.setdefault(c, []).append(t)
        print(f'curator composition details available for {len(details)} compositions')

    rows, per_host = [], {}
    for r in comp.itertuples():
        rule = RULES.get(r.host_system)
        if rule is None:
            continue
        # The full composition, not just the host: Rb in Rb3C60 is 4.8 at.% and
        # the 5% split strips it, yet it is exactly what makes the compound a
        # fulleride rather than graphite. Element-presence tests must see it.
        try:
            f = json.loads(r.host_fracs) if r.host_fracs else {}
        except Exception:
            f = {}
        try:
            f = dict(f, **(json.loads(r.dopant_fracs) if r.dopant_fracs else {}))
        except Exception:
            pass
        rules, (fb_proto, fb_conf) = rule
        proto, conf, matched = fb_proto, fb_conf, 'fallback'
        for i, (pred, p, c) in enumerate(rules):
            try:
                if pred(f):
                    proto, conf, matched = p, c, f'rule {i + 1}'
                    break
            except Exception:
                continue
        # A structure named in the paper beats a ratio inference.
        phrase = None
        ov = detail_override(details.get(r.composition, []), r.host_system,
                             r.reduced_formula, valid)
        if ov and ov[0] == '__AMBIGUOUS__':
            phrase = ov[2]
            matched = 'detail ambiguous - needs sample-level split'
            conf = 'low'
        elif ov:
            proto, conf, phrase = ov
            matched = 'curator detail'
        rows.append({'composition': r.composition, 'reduced_formula': r.reduced_formula,
                     'host_system': r.host_system, 'prototype_id': proto,
                     'confidence': conf, 'matched': matched,
                     'detail_phrase': phrase, 'n_samples': r.n_samples})
        per_host.setdefault(r.host_system, {}).setdefault(proto, 0)
        per_host[r.host_system][proto] += r.n_samples

    df = pd.DataFrame(rows)
    nd = int((df.matched == 'curator detail').sum())
    print(f'{len(df)} compositions assigned across {df.host_system.nunique()} hosts '
          f'({int(df.n_samples.sum())} samples)')
    print(f'  {nd} of them decided by a structure named in the paper, '
          f'overriding the ratio rule')
    print('\nhosts where the split actually separated something:')
    for host, d in sorted(per_host.items(), key=lambda kv: -sum(kv[1].values())):
        if len(d) > 1:
            parts = ', '.join(f'{k} {v}' for k, v in
                              sorted(d.items(), key=lambda kv: -kv[1]))
            print(f'  {host:14s} {parts}')

    if args.dry_run:
        print('\nDry run: nothing written.')
        return 0

    df.to_parquet(OUT, index=False, engine='pyarrow')
    print(f'\n  -> {OUT}')

    resolved = 0
    for host, d in per_host.items():
        rec = by_host.get(host)
        if not rec:
            continue
        rec['composition_split_rule'] = 'scripts/apply_composition_splits.py'
        rec['composition_split_counts'] = {k: int(v) for k, v in d.items()}
        rec['split_basis'] = 'composition + llm_materials_knowledge (NOT paper evidence)'
        resolved += 1
    for host in NOT_ACTUALLY_MIXED:
        if host in by_host:
            by_host[host]['is_mixed'] = False
            by_host[host]['alt_prototype_ids'] = []
            by_host[host]['split_basis'] = 'alt list was redundant; single prototype'
    with open(LEDGER, 'w') as fh:
        fh.write('\n'.join(json.dumps(r) for r in records) + '\n')
    print(f'  updated {resolved} ledger records (+{len(NOT_ACTUALLY_MIXED)} un-flagged)')
    print('\nThese are composition-based inferences. experimentally_confirmed stays false.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
