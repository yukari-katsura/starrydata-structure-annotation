#!/usr/bin/env python
"""Index external structure references against the annotation's host systems.

Two reference sets are linked to data/annotated/input/df_host_systems.parquet:

  data/reference/tedesignlab-complete-data.xlsx
      2,701 rows / 1,837 compounds, each carrying an ICSD id and an
      experimentally determined space group, plus computed thermoelectric
      quantities (band gap, kL, beta quality factor, effective masses).
      This is the only structure evidence in the project that does not come
      from a language model.

  data/reference/mp_190822.csv
      119,570 Materials Project entries (dump of 2019-08-22) with material_id,
      formula, space group symbol, e_above_hull and ICSD cross-references.
      Lets stage 2 resolve mp_ids offline, without the API.

Output:
    data/annotated/input/df_structure_refs.parquet   one row per reference entry,
        keyed to a host_system where one matches
    data/annotated/input/df_host_structures.parquet  per host system: the space
        groups actually observed, with counts and representative formulas

A reference compound is matched to a host system on its full element set, and
also on the 5 at.% host split, because ordered reference compounds can carry a
minority element that the split would strip (Mn in Yb14MnSb11 is 3.8 at.%).

Dependencies: pip install pymatgen pandas pyarrow openpyxl
"""

import os
import re
import sys

import pandas as pd
from pymatgen.core.composition import Composition

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_annotation_data import DOPANT_THRESHOLD, split_host_dopants  # noqa: E402

_P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF = os.path.join(_P, 'data', 'reference') + os.sep
OUT = os.path.join(_P, 'data', 'annotated', 'input') + os.sep
TEDL = REF + 'tedesignlab-complete-data.xlsx'
MP = REF + 'mp_190822.csv'


def keys_for(formula):
    """Return (reduced_formula, full_element_key, thresholded_host_key).

    Both keys are offered because an ordered reference compound may contain a
    minority element that the 5 at.% split would treat as a dopant.
    """
    try:
        c = Composition(str(formula))
        if len(c) == 0 or c.num_atoms <= 0:
            return None, None, None
    except Exception:
        return None, None, None
    full = '-'.join(sorted(c.as_dict().keys()))
    host, _ = split_host_dopants(c.fractional_composition.as_dict(), DOPANT_THRESHOLD)
    return c.reduced_formula, full, ('-'.join(host) if host else None)


def sg_number(symbol):
    """Space group symbol -> international number, or None."""
    try:
        from pymatgen.symmetry.groups import SpaceGroup
        return int(SpaceGroup(str(symbol)).int_number)
    except Exception:
        return None


def require_references():
    """Neither reference dataset ships with this repository; fail helpfully."""
    missing = [p for p in (TEDL, MP) if not os.path.exists(p)]
    if not missing:
        return
    for p in missing:
        print(f'MISSING: {p}')
    print('\nReference datasets are not redistributed with this repository.')
    print('Run:  python scripts/fetch_reference_data.py')
    print('for the source URLs, the terms attached to each, and where to save them.')
    sys.exit(1)


def tedl_mp_crosswalk(t, mp):
    """Attach an openly-resolvable mp_id to each TEDesignLab entry.

    The key stays ICSD-based: that is the identifier TEDesignLab publishes, it
    is present for all 2,701 entries, and collection codes are never reused. An
    mp_id cannot serve as the key because 13% of entries have none.

    But ICSD is a licensed database, so an mp_id is added for open lookup. Two
    routes, better one first:
      1. Materials Project's own icsd_ids cross-reference (84% of entries).
         This is MP asserting the link, not us inferring it.
      2. reduced formula + space group (a further 3%).
    mp_id_source records which, because route 2 is our inference and can be
    wrong where a formula has several polymorphs.
    """
    import re as _re
    icsd_to_mp, hull = {}, {}
    for r in mp.itertuples():
        hull[r.material_id] = r.e_above_hull
        for n in _re.findall(r'\d+', str(r.icsd_ids)):
            icsd_to_mp.setdefault(int(n), []).append(r.material_id)

    sym_num, by_fs = {}, {}
    for r in mp.itertuples():
        red, _, _ = keys_for(r.pretty_formula)
        if not red:
            continue
        if r.spacegroup not in sym_num:
            sym_num[r.spacegroup] = sg_number(r.spacegroup)
        n = sym_num[r.spacegroup]
        if n is None:
            continue
        k = (red, int(n))
        prev = by_fs.get(k)
        if prev is None or (r.e_above_hull == r.e_above_hull
                            and r.e_above_hull < hull.get(prev, 9e9)):
            by_fs[k] = r.material_id
    return icsd_to_mp, by_fs, hull


def build_tedl_entries(t, mp=None):
    """TEDesignLab rows as a feature table, keyed by a stable tedl_id.

    Kept separate from mp_id and icsd_id because it answers a different
    question: an mp_id points at a structure, a tedl_id points at a computed
    thermoelectric feature vector -- band gap, effective masses, valley
    degeneracy, lattice thermal conductivity, mobility, the beta quality
    factor, bulk modulus, coordination number and Grueneisen parameter.

    tedl_id is "<row>-<compound>-<icsd>", e.g. 1-La1O4V1-8294. Each part earns
    its place: the row number is what you scroll to in the downloaded
    spreadsheet, the compound makes the id readable without a lookup, and the
    ICSD collection code is the part that survives the sheet being re-sorted or
    re-issued. row is the 1-based DATA row, so it is Excel row - 1 (row 1 of the
    file is the header).

    Paired columns arrive as "valence,conduction" strings; they are split into
    separate numeric columns so they can be used as features directly.
    """
    PAIRED = {'m*b (vb,cb)': ('mstar_b_vb', 'mstar_b_cb'),
              'Nb (vb,cb)': ('Nb_vb', 'Nb_cb'),
              'mob (h,e)': ('mobility_h', 'mobility_e'),
              'beta (p,n)': ('beta_p', 'beta_n'),
              'm*DOS(vb,cb)': ('mstar_dos_vb', 'mstar_dos_cb')}
    SINGLE = {'Eg (eV)': 'band_gap_eV', 'kL': 'kL_W_mK', 'natoms': 'natoms',
              'density': 'density', 'volume': 'volume', 'bulkmod': 'bulk_modulus',
              'avgcn': 'avg_coordination', 'gamma': 'gruneisen'}

    def num(x):
        try:
            return float(str(x).strip())
        except (TypeError, ValueError):
            return None

    icsd_to_mp, by_fs, hull = ({}, {}, {})
    if mp is not None:
        icsd_to_mp, by_fs, hull = tedl_mp_crosswalk(t, mp)

    rows = []
    for n, r in enumerate(t.itertuples(), start=1):
        d = {'tedl_id': f'{n}-{r.compound}-{int(r.icsd)}',
             'tedl_row': n,
             'tedl_excel_row': n + 1,
             'icsd_id': int(r.icsd),
             'tedl_compound': str(r.compound),
             'spacegroup_number': int(r.sg) if r.sg == r.sg else None,
             'tedl_cite': getattr(r, 'cite', None),
             'tedl_group': getattr(r, 'comment', None)}
        red, _, _ = keys_for(r.compound)
        d['reduced_formula'] = red
        # MP's own cross-reference first; our formula+sg match only as fallback
        cands = icsd_to_mp.get(int(r.icsd))
        if cands:
            d['mp_id'] = sorted(cands, key=lambda m: hull.get(m, 9e9))[0]
            d['mp_id_source'] = 'MP icsd_ids cross-reference'
        elif red and r.sg == r.sg and (red, int(r.sg)) in by_fs:
            d['mp_id'] = by_fs[(red, int(r.sg))]
            d['mp_id_source'] = 'formula+spacegroup match (inferred)'
        else:
            d['mp_id'] = None
            d['mp_id_source'] = None
        row = t.loc[r.Index]
        for col, name in SINGLE.items():
            d[name] = num(row.get(col))
        for col, (a, b) in PAIRED.items():
            v = str(row.get(col, '')).split(',')
            d[a] = num(v[0]) if len(v) > 0 else None
            d[b] = num(v[1]) if len(v) > 1 else None
        rows.append(d)
    df = pd.DataFrame(rows)
    # id first, so it is the leftmost column wherever the table is opened
    return df[['tedl_id'] + [c for c in df.columns if c != 'tedl_id']]


def main():
    require_references()
    hosts = pd.read_parquet(OUT + 'df_host_systems.parquet')
    known = set(hosts.host_system)
    rows = []

    # --- TEDesignLab ------------------------------------------------------
    print(f'Reading {TEDL} ...')
    t = pd.read_excel(TEDL)
    print(f'  {len(t)} rows, {t.compound.nunique()} distinct compounds')
    for _, r in t.iterrows():
        red, full, host = keys_for(r['compound'])
        if red is None:
            continue
        rows.append({
            'source': 'tedesignlab',
            'entry_id': f"icsd-{int(r['icsd'])}" if pd.notna(r['icsd']) else None,
            'icsd_id': int(r['icsd']) if pd.notna(r['icsd']) else None,
            'mp_id': None,
            'formula_raw': str(r['compound']),
            'reduced_formula': red,
            'element_key': full,
            'host_key': host,
            'spacegroup_number': int(r['sg']) if pd.notna(r['sg']) else None,
            'spacegroup_symbol': None,
            'e_above_hull': None,
            'band_gap': r.get('Eg (eV)'),
            'kL': r.get('kL'),
            'beta_pn': r.get('beta (p,n)'),
            # Which TEDesignLab paper produced this row; see
            # data/reference/CITATIONS.md for the marker -> reference mapping.
            'tedl_cite': r.get('cite'),
            'n_icsd': 1,
            'is_experimental': True,
            'group': r.get('comment'),
        })

    # --- Materials Project ------------------------------------------------
    print(f'Reading {MP} ...')
    m = pd.read_csv(MP, usecols=['material_id', 'pretty_formula', 'elements',
                                 'nelements', 'spacegroup', 'e_above_hull',
                                 'band_gap', 'icsd_ids'], low_memory=False)
    print(f'  {len(m)} entries')
    # built here rather than with the TEDesignLab read: the crosswalk needs the
    # Materials Project table, which is loaded above.
    tedl = build_tedl_entries(t, m)
    tedl.to_parquet(OUT + 'df_tedl_entries.parquet', index=False, engine='pyarrow')
    n_mp = int(tedl.mp_id.notna().sum())
    print(f'  -> {OUT}df_tedl_entries.parquet  ({len(tedl)} entries, '
          f'{len(tedl.columns)} columns, {tedl.reduced_formula.nunique()} formulas)')
    print(f'     {n_mp} carry an mp_id ({n_mp/len(tedl)*100:.0f}%); '
          f'{len(tedl)-n_mp} have none by any route')

    sym_cache = {}
    for _, r in m.iterrows():
        red, full, host = keys_for(r['pretty_formula'])
        if red is None:
            continue
        # Only keep entries that can attach to a host system we care about;
        # the full dump is 119k rows and most of it is irrelevant here.
        if full not in known and host not in known:
            continue
        sym = r['spacegroup']
        if sym not in sym_cache:
            sym_cache[sym] = sg_number(sym)
        icsd = r['icsd_ids']
        n_icsd = 0
        if isinstance(icsd, str):
            n_icsd = len(re.findall(r'\d+', icsd))
        rows.append({
            'source': 'materials_project',
            'entry_id': r['material_id'],
            'icsd_id': None,
            'mp_id': r['material_id'],
            'formula_raw': str(r['pretty_formula']),
            'reduced_formula': red,
            'element_key': full,
            'host_key': host,
            'spacegroup_number': sym_cache[sym],
            'spacegroup_symbol': sym,
            'e_above_hull': r['e_above_hull'],
            'band_gap': r['band_gap'],
            'kL': None,
            'beta_pn': None,
            'tedl_cite': None,
            'n_icsd': n_icsd,
            'is_experimental': n_icsd > 0,
            'group': None,
        })

    df = pd.DataFrame(rows)
    # Attach to a host system: prefer the full element set, fall back to the split.
    df['host_system'] = df.apply(
        lambda r: r['element_key'] if r['element_key'] in known
        else (r['host_key'] if r['host_key'] in known else None), axis=1)
    df.to_parquet(OUT + 'df_structure_refs.parquet', index=False, engine='pyarrow')

    matched = df[df.host_system.notna()]
    print(f'\n  -> {OUT}df_structure_refs.parquet  ({len(df)} rows, '
          f'{len(matched)} attached to a host system)')
    for src, g in df.groupby('source'):
        mg = g[g.host_system.notna()]
        print(f'     {src:18s} {len(g):6d} entries, {mg.host_system.nunique():5d} host systems matched')

    # --- Per-host summary --------------------------------------------------
    # The MP dump contains every computed polymorph, most of them hypothetical
    # and high above the hull. Summarising by raw count lets those bury the real
    # structure (1,276 Mg-O entries at P4/mmm outvoting rocksalt MgO), so
    # experimentally-backed entries are summarised separately and first.
    HULL_TOL = 0.05  # eV/atom

    def sg_summary(g):
        vc = g.dropna().astype(int).value_counts()
        return '; '.join(f'{int(s)} ({n})' for s, n in vc.head(5).items())

    def formula_summary(g):
        seen = []
        for f in g:
            if f not in seen:
                seen.append(f)
            if len(seen) >= 5:
                break
        return '; '.join(seen)

    exp = matched[matched.is_experimental]
    stable = matched[(matched.source == 'materials_project')
                     & (matched.e_above_hull <= HULL_TOL)]

    def sg_by_evidence(g):
        """Space groups ranked by how often they have actually been measured.

        Counting MP entries instead would let a handful of hypothetical
        polymorphs outvote the ground state: PbS has one Fm-3m entry carrying
        33 ICSD references and several one-off computed structures.
        """
        w = g.groupby('spacegroup_number')['n_icsd'].sum().sort_values(ascending=False)
        return '; '.join(f'{int(k)} ({int(v)} icsd)' for k, v in w.head(5).items() if k == k)

    def ground_states(g):
        """Lowest-hull entry for each of the best-attested formulas."""
        out = []
        # Ties are common -- most formulas have zero ICSD references -- and a
        # groupby's order for tied values is not stable across pandas versions.
        # Break ties on the formula name so the output is reproducible whatever
        # interpreter builds it.
        _s = g.groupby('reduced_formula')['n_icsd'].sum().reset_index()
        order = (_s.sort_values(['n_icsd', 'reduced_formula'],
                                ascending=[False, True])['reduced_formula'].tolist())
        for f in list(order)[:4]:
            sub = g[g.reduced_formula == f].sort_values('e_above_hull', na_position='last')
            if sub.empty:
                continue
            r = sub.iloc[0]
            sg = f'{r.spacegroup_symbol} ({int(r.spacegroup_number)})' if r.spacegroup_number == r.spacegroup_number else str(r.spacegroup_symbol)
            out.append(f'{f} {sg} {r.mp_id or ""}'.strip())
        return '; '.join(out)

    # ------------------------------------------------------------------
    # Candidate structure selection, in the project's precedence order:
    #   1. the LLM's thermoelectric judgement  (made at annotation time,
    #      not here -- this table only supplies evidence for it)
    #   2. TEDesignLab: ICSD-backed and thermoelectric-specific
    #   3. Materials Project, most stable by e_above_hull, and ONLY for
    #      formulas TEDesignLab does not cover
    #
    # TEDesignLab carries a space group but no mp_id, and stage 2 needs a
    # structure file. So where TEDesignLab has the formula, its space group is
    # used to pick WHICH Materials Project entry to take, rather than taking
    # the most stable one blindly. A formula TEDesignLab covers whose space
    # group has no Materials Project counterpart is flagged, not silently
    # replaced -- that disagreement is worth seeing.
    # ------------------------------------------------------------------
    print('\nSelecting candidate structures ...')
    mpe = matched[matched.source == 'materials_project']
    tdl = matched[matched.source == 'tedesignlab']
    mp_by_formula = {f: g for f, g in mpe.groupby('reduced_formula')}
    tdl_by_formula = {f: g for f, g in tdl.groupby('reduced_formula')}

    cands = []
    for host, g in matched.groupby('host_system'):
        # Ties are common -- most formulas have zero ICSD references -- and a
        # groupby's order for tied values is not stable across pandas versions.
        # Break ties on the formula name so the output is reproducible whatever
        # interpreter builds it.
        _s = g.groupby('reduced_formula')['n_icsd'].sum().reset_index()
        order = (_s.sort_values(['n_icsd', 'reduced_formula'],
                                ascending=[False, True])['reduced_formula'].tolist())
        for formula in list(order)[:6]:
            t = tdl_by_formula.get(formula)
            m = mp_by_formula.get(formula)

            # Build one candidate per space group, merging both sources.
            # TEDesignLab supplies the polymorph list and the thermoelectric
            # properties; Materials Project supplies mp_id, hull and ICSD
            # counts. Neither source alone can say which polymorph is the
            # ambient phase, so they are pooled and ranked afterwards.
            by_sg = {}
            if t is not None:
                for sg in sorted({int(v) for v in t.spacegroup_number.dropna()}):
                    tt = t[t.spacegroup_number == sg].iloc[0]
                    by_sg[sg] = {'spacegroup_number': sg, 'in_tedesignlab': True,
                                 'band_gap': tt.band_gap, 'kL': tt.kL,
                                 'beta_pn': tt.beta_pn,
                                 'tedl_cite': getattr(tt, 'tedl_cite', None),
                                 'mp_id': None,
                                 'spacegroup_symbol': None, 'e_above_hull': None,
                                 'n_icsd': 0}
            if m is not None:
                for r in m.itertuples():
                    if r.spacegroup_number != r.spacegroup_number:
                        continue
                    sg = int(r.spacegroup_number)
                    e = by_sg.setdefault(sg, {'spacegroup_number': sg,
                                              'in_tedesignlab': False,
                                              'band_gap': r.band_gap, 'kL': None,
                                              'beta_pn': None, 'n_icsd': 0})
                    # keep the lowest-hull MP entry at this space group
                    if e.get('mp_id') is None or (
                            r.e_above_hull == r.e_above_hull
                            and (e.get('e_above_hull') is None
                                 or r.e_above_hull < e['e_above_hull'])):
                        e['mp_id'] = r.mp_id
                        e['spacegroup_symbol'] = r.spacegroup_symbol
                        e['e_above_hull'] = r.e_above_hull
                    e['n_icsd'] = max(e['n_icsd'], int(r.n_icsd))
            if not by_sg:
                continue

            # Rank by measured evidence first. e_above_hull cannot lead: the
            # 2019 dump has no van der Waals correction, so layered
            # chalcogenides are badly penalised -- Sb2Te3 R-3m carries 26 ICSD
            # references at hull 1.017. ICSD count is what distinguishes the
            # ambient phase from a metastable or hypothetical one.
            # Two-stage rule. ICSD count identifies which polymorphs are real,
            # but it cannot rank among them: MP cross-links one ICSD collection
            # to several entries, so Fe3O4 reads 101/100/100/100 and magnetite
            # (Fd-3m, hull 0) loses to a Pbcm entry by a single reference. So
            # take everything within 20% of the best-attested count as tied on
            # evidence, then let hull decide inside that set.
            def _hull(e):
                return e['e_above_hull'] if e['e_above_hull'] is not None else 9e9
            top_icsd = max(e['n_icsd'] for e in by_sg.values())
            well_attested = [e for e in by_sg.values()
                             if top_icsd > 0 and e['n_icsd'] >= 0.8 * top_icsd]
            ranked = (sorted(well_attested, key=_hull)
                      + sorted([e for e in by_sg.values() if e not in well_attested],
                               key=lambda e: (-e['n_icsd'], _hull(e))))
            primary = ranked[0]
            for i, e in enumerate(ranked):
                tier = ('tedesignlab' if e['in_tedesignlab'] else 'materials_project')
                row = {'host_system': host, 'reduced_formula': formula,
                       'tier': tier,
                       'source': ('TEDesignLab (ICSD)' if e['in_tedesignlab']
                                  else 'Materials Project'),
                       'is_primary': i == 0, 'n_polymorphs': len(ranked)}
                row.update({k: v for k, v in e.items() if k != 'in_tedesignlab'})
                if i == 0 and not e['in_tedesignlab'] and t is not None:
                    row['tier1_demoted'] = (
                        f'TEDesignLab lists this formula but not sg {e["spacegroup_number"]}, '
                        f'which carries {e["n_icsd"]} ICSD references -- more than any '
                        f'polymorph it does list. Falling through to Materials Project.')
                if e['in_tedesignlab'] and e['mp_id'] is None:
                    row['mp_match'] = 'no MP entry at this space group'
                if i == 0 and len(ranked) > 1:
                    # A tie on ICSD evidence broken by a hull margin smaller than
                    # the accuracy of the calculation is not a real decision.
                    # SrSi2 has two polymorphs at 5 ICSD references each,
                    # separated by 3 meV/atom, and the ambient chiral phase is
                    # the one that loses.
                    nxt = ranked[1]
                    if (nxt['n_icsd'] >= 0.8 * e['n_icsd']
                            and e['e_above_hull'] is not None
                            and nxt['e_above_hull'] is not None
                            and abs(nxt['e_above_hull'] - e['e_above_hull']) < 0.01):
                        row['ambiguous_primary'] = (
                            f'sg {nxt["spacegroup_number"]} ({nxt["mp_id"]}) is within '
                            f'10 meV/atom on a comparable ICSD count; the ranking cannot '
                            f'separate them. Decide from the chemistry.')
                if i == 0 and e['n_icsd'] < 5:
                    # Thin experimental support for the phase we are calling
                    # primary. Sometimes the ambient structure is simply absent
                    # from the 2019 dump: it holds no R-3m Bi2Se3 at all, only
                    # Pnma, so ranking cannot recover the tetradymite.
                    row['low_evidence'] = (
                        f'Primary chosen on only {e["n_icsd"]} ICSD reference(s). '
                        f'The ambient phase may be missing from this snapshot -- '
                        f'do not trust this over your own knowledge of the chemistry.')
                cands.append(row)

    cand = pd.DataFrame(cands)
    cand.to_parquet(OUT + 'df_structure_candidates.parquet', index=False, engine='pyarrow')
    n_t = int((cand.tier == 'tedesignlab').sum())
    n_m = int((cand.tier == 'materials_project').sum())
    dem = cand[cand.get('tier1_demoted').notna()] if 'tier1_demoted' in cand else cand.iloc[0:0]
    print(f'  -> {OUT}df_structure_candidates.parquet  ({len(cand)} formula candidates)')
    print(f'     tier 1  TEDesignLab      {n_t:5d} formulas, '
          f'{cand[cand.tier=="tedesignlab"].host_system.nunique()} host systems')
    print(f'     tier 2  Materials Project {n_m:5d} formulas, '
          f'{cand[cand.tier=="materials_project"].host_system.nunique()} host systems')
    print(f'     {len(dem)} formulas where the ICSD-primary phase is one '
          f'TEDesignLab does not list (tier-1 fall-through)')
    if 'low_evidence' in cand:
        le = cand[cand.low_evidence.notna()]
        print(f'     {len(le)} primaries rest on fewer than 5 ICSD references '
              f'(flagged as weak evidence)')

    def cand_summary(g):
        """Render candidates with the evidence needed to tell a thermally
        accessible phase from a metastable one.

        A polymorph list is not a thermal sequence: SnSe has three known
        structures but only Pnma -> Cmcm happens on heating. Hull distance and
        ICSD reference count are what separate them -- rocksalt SnSe carries 2
        ICSD references against 32 for Pnma -- so both are shown here rather
        than left for the annotator to look up.
        """
        out = []
        g = g.sort_values(['is_primary', 'n_icsd'], ascending=[False, False])
        for r in g.itertuples():
            sg = f'{int(r.spacegroup_number)}' if r.spacegroup_number == r.spacegroup_number else '?'
            sym = f' {r.spacegroup_symbol}' if isinstance(r.spacegroup_symbol, str) else ''
            mp = f' {r.mp_id}' if isinstance(r.mp_id, str) else ''
            ev = []
            if r.e_above_hull == r.e_above_hull and r.e_above_hull is not None:
                ev.append(f'hull={r.e_above_hull:.3f}')
            if getattr(r, 'n_icsd', None) == getattr(r, 'n_icsd', None) and getattr(r, 'n_icsd', 0):
                ev.append(f'icsd={int(r.n_icsd)}')
            if getattr(r, 'is_primary', False):
                ev.append('PRIMARY')
            if isinstance(getattr(r, 'ambiguous_primary', None), str):
                ev.append('AMBIGUOUS')
            tail = f' [{", ".join(ev)}]' if ev else ''
            out.append(f'{r.reduced_formula}{sym} ({sg}){mp}{tail}')
        return '; '.join(out[:5])

    c1 = (cand[cand.tier == 'tedesignlab'].groupby('host_system')
          .apply(cand_summary).rename('candidates_tedl').reset_index())
    c2 = (cand[cand.tier == 'materials_project'].groupby('host_system')
          .apply(cand_summary).rename('candidates_mp').reset_index())

    summ = (matched.groupby('host_system')
                   .agg(n_refs=('entry_id', 'size'),
                        n_tedesignlab=('source', lambda s: int((s == 'tedesignlab').sum())),
                        n_mp=('source', lambda s: int((s == 'materials_project').sum())),
                        ref_formulas=('reduced_formula', formula_summary))
                   .reset_index())
    e = (exp.groupby('host_system')
            .agg(n_experimental=('entry_id', 'size'),
                 spacegroups_exp=('spacegroup_number', sg_summary)).reset_index())
    ev = exp.groupby('host_system').apply(sg_by_evidence).rename('sg_by_icsd').reset_index()
    gs = (matched[matched.source == 'materials_project']
          .groupby('host_system').apply(ground_states).rename('ground_states').reset_index())
    td = (matched[matched.source == 'tedesignlab'].groupby('host_system')
          .agg(tedl_spacegroups=('spacegroup_number', sg_summary),
               tedl_beta=('beta_pn', lambda s: '; '.join(str(x) for x in s.dropna().head(3))),
               tedl_kL=('kL', lambda s: '; '.join(f'{x:.1f}' for x in s.dropna().head(3)))).reset_index())
    st = (stable.groupby('host_system')
               .agg(n_mp_stable=('entry_id', 'size'),
                    spacegroups_stable=('spacegroup_number', sg_summary)).reset_index())
    for extra in (e, ev, gs, td, st, c1, c2):
        summ = summ.merge(extra, on='host_system', how='left')
    # Best available evidence, in descending order of trust.
    summ['spacegroups_best'] = (summ.tedl_spacegroups
                                .fillna(summ.sg_by_icsd)
                                .fillna(summ.spacegroups_stable))

    summ = hosts[['host_system', 'rank', 'n_samples', 'chunk']].merge(
        summ, on='host_system', how='left')
    summ.to_parquet(OUT + 'df_host_structures.parquet', index=False, engine='pyarrow')

    have = summ[summ.n_refs.notna()]
    print(f'  -> {OUT}df_host_structures.parquet')
    print(f'\nCoverage: {len(have)}/{len(hosts)} host systems have a structure reference '
          f'({have.n_samples.sum()/hosts.n_samples.sum()*100:.1f}% of samples)')
    for n in (50, 200, 500, 1000):
        t = summ.head(n)
        c = int(t.n_refs.notna().sum())
        print(f'  top {n:4d} hosts: {c}/{n} ({c/n*100:.0f}%)')
    tedl_hosts = matched[matched.source == 'tedesignlab'].host_system.nunique()
    n_exp = int(summ.n_experimental.notna().sum())
    print(f'\nTEDesignLab (ICSD-backed space groups) reaches {tedl_hosts} host systems.')
    print(f'Experimentally-backed space groups available for {n_exp} host systems '
          f'({summ[summ.n_experimental.notna()].n_samples.sum()/hosts.n_samples.sum()*100:.1f}% of samples).')


if __name__ == '__main__':
    main()
