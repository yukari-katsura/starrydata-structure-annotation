#!/usr/bin/env python
"""Build the input files for the material-family annotation project.

Stage 1 of the annotation pipeline. Reduces the thermoelectric sample table to
the unit the annotation actually works on -- the *host system*, i.e. the set of
elements left after minor constituents (likely dopants) are split off -- and
writes conversation-sized chunks so the families can be assigned interactively
with Claude Code.

Provenance:
    data/raw/*.csv                  DB snapshot 2026-09-04 02:00:02 JST (renumbered IDs)
      -> scripts/generate_data.py
    data/processed/df_samples.parquet   TE samples (has TE curves, valid composition)
      -> this script
    data/annotated/input/

Input:
    data/processed/df_samples.parquet

Output:
    data/annotated/input/df_compositions.parquet   one row per unique composition
    data/annotated/input/df_host_systems.parquet   one row per host system (annotation unit)
    data/annotated/input/chunks/chunk_NNN.md       coverage-ordered annotation batches
    data/annotated/input/coverage.csv              cumulative sample coverage per chunk

Dependencies:
    pip install pymatgen pandas pyarrow tqdm
"""

import json
import os
import re

import pandas as pd
import tqdm
from pymatgen.core.composition import Composition

# Atomic fraction below which a constituent is treated as a dopant candidate
# rather than part of the host. 0.05 collapses 27k compositions into ~3.6k host
# systems while keeping substitutional solid solutions (e.g. Bi0.5Sb1.5Te3)
# intact as hosts. Recorded per-composition so the threshold can be revisited
# without re-deriving anything.
DOPANT_THRESHOLD = 0.05

# Physically plausible measurement temperatures. Digitised curves contain
# artefacts outside this window, including negative temperatures.
T_FLOOR, T_CEIL = 10.0, 3000.0

# Host systems per conversation chunk.
CHUNK_SIZE = 50

# Examples carried into each chunk.
N_EXAMPLE_COMPS = 6
N_EXAMPLE_TITLES = 3

_PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IN_PATH = os.path.join(_PROJECT_DIR, 'data', 'processed', 'df_samples.parquet')
OUT_DIR = os.path.join(_PROJECT_DIR, 'data', 'annotated', 'input') + os.sep
TAXONOMY = os.path.join(_PROJECT_DIR, 'data', 'annotated', 'taxonomy',
                        'prototypes_seed_v3.json')


# Minority share of a shared sublattice below which a substituent is dilute
# enough that the dominant end member is the sensible host. Above it the
# composition is an alloy in its own right. Asymmetric on purpose: there is no
# upper band around 0.50, because Bi0.5Sb1.5Te3 sits at 0.25 and is universally
# an alloy, not Bi-doped Sb2Te3.
DILUTE_SUBLATTICE = 0.10


def sublattice_share(host_system, host_fracs):
    """Minority share of a shared sublattice, for same-group element pairs.

    The 5 at.% host/dopant split measures against the whole formula, so the
    site occupancy it corresponds to depends on stoichiometry: 5% of an AB
    formula is 10% of either sublattice, but only 8.3% of the anion site in
    A2B3 and 7.5% of the cation site in A2B. This reports the share directly,
    so stage 3 does not have to back it out.

    Returns (x_minor, minor_element, major_element) or (None, None, None).
    """
    from pymatgen.core.periodic_table import Element
    els = host_system.split('-')
    try:
        d = json.loads(host_fracs)
    except Exception:
        return None, None, None
    best = None
    for i, a in enumerate(els):
        for b in els[i + 1:]:
            try:
                if Element(a).group != Element(b).group:
                    continue
            except Exception:
                continue
            fa, fb = d.get(a, 0.0), d.get(b, 0.0)
            if fa + fb <= 0:
                continue
            x = min(fa, fb) / (fa + fb)
            minor, major = (a, b) if fa <= fb else (b, a)
            if best is None or x > best[0]:
                best = (x, minor, major)
    return best if best else (None, None, None)


def alloy_axes(df_comp, min_comps=4):
    """Detect isoelectronic solid-solution axes inside each host system.

    The 5 at.% host/dopant split uses the whole formula as its denominator, but
    substitution happens on a sublattice. In rocksalt Pb(Se,Te) the anion site
    is only half the atoms, so a 10% anion substitution reads as 5% atomic --
    exactly on the cut. Worse, isoelectronic substitution is a continuum with no
    principled threshold: PbSe0.99Te0.01 is doped PbSe, PbSe0.5Te0.5 is an
    alloy, and PbTe0.9Se0.1 is doped PbTe, yet the last two share a host.

    So rather than move the threshold, report the axis. For each pair of
    same-group elements present in a host, this measures x = A/(A+B) across the
    host's compositions. A wide spread means the host is a solid-solution
    series whose parent compound depends on the composition, not a single
    doped parent.
    """
    from pymatgen.core.periodic_table import Element
    groups = {}

    def group_of(sym):
        if sym not in groups:
            try:
                groups[sym] = Element(sym).group
            except Exception:
                groups[sym] = None
        return groups[sym]

    out = {}
    for host, g in df_comp.groupby('host_system'):
        if len(g) < min_comps:
            continue
        els = host.split('-')
        pairs = [(a, b) for i, a in enumerate(els) for b in els[i + 1:]
                 if group_of(a) is not None and group_of(a) == group_of(b)]
        if not pairs:
            continue
        fr = [json.loads(h) for h in g.host_fracs]
        w = list(g.n_samples)
        best = None
        for a, b in pairs:
            xs, ws = [], []
            for d, n in zip(fr, w):
                fa, fb = d.get(a, 0.0), d.get(b, 0.0)
                if fa + fb > 0:
                    xs.append(fa / (fa + fb))
                    ws.append(n)
            if len(xs) < min_comps:
                continue
            xs_s = sorted(xs)
            lo, hi = xs_s[0], xs_s[-1]
            q1 = xs_s[len(xs_s) // 4]
            q3 = xs_s[(3 * len(xs_s)) // 4]
            spread = q3 - q1
            if best is None or spread > best['spread']:
                best = {'a': a, 'b': b, 'lo': lo, 'hi': hi, 'q1': q1, 'q3': q3,
                        'spread': spread, 'n': len(xs),
                        'med': xs_s[len(xs_s) // 2]}
        if best and best['hi'] - best['lo'] > 0.15:
            # Same group does not guarantee the same site. In oxychalcogenides
            # and oxypnictides (BiCuSeO, LaFeAsO) oxygen sits in its own layer
            # and never substitutes for the heavier chalcogen, so an O-bearing
            # pair is reported but marked as needing confirmation.
            best['same_site_uncertain'] = (
                'O' in (best['a'], best['b']) and {best['a'], best['b']} != {'O', 'S'})
            out[host] = best
    return out


def distortion_series(path=TAXONOMY):
    """prototype id -> its tilt/distortion sequence, where one is recorded.

    These steps sit inside a single prototype and differ only by space group,
    so a host can pass through several of them without changing prototype.
    """
    if not os.path.exists(path):
        return {}
    return {p['id']: p['distortion_series']
            for p in json.load(open(path))['prototypes'] if p.get('distortion_series')}


def phase_transitions(path=TAXONOMY):
    """prototype id -> its transitions, for flagging measurements that cross one."""
    if not os.path.exists(path):
        return {}
    return {p['id']: p['phase_transitions']
            for p in json.load(open(path))['prototypes'] if p.get('phase_transitions')}


def measured_temperature_range(df_parsed):
    """host_system -> (T_min, T_max, n_curves) actually measured.

    Transport here is taken across a wide window, so whether a host's
    measurement crosses a structural transition is a property of the data, not
    something to assume from the prototype.
    """
    path = os.path.join(_PROJECT_DIR, 'data', 'processed', 'df_curves.parquet')
    if not os.path.exists(path):
        return {}
    cur = pd.read_parquet(path, columns=['composition', 'x'])
    cur = cur[cur.x.str.len() > 2]
    lo, hi = {}, {}
    all_lo, all_hi = {}, {}
    n_dropped = 0
    for comp, xs in zip(cur.composition, cur.x):
        try:
            a = [float(v) for v in json.loads(xs) if v is not None]
        except Exception:
            continue
        # Digitised curves carry artefacts: ~6% of them contain points below
        # 10 K, including negative temperatures down to -4 K. Those would make
        # every range start at 0 and hide which transitions are really crossed.
        n = len(a)
        a = [v for v in a if T_FLOOR <= v <= T_CEIL]
        n_dropped += n - len(a)
        if not a:
            continue
        mn, mx = min(a), max(a)
        all_lo.setdefault(comp, []).append(mn)
        all_hi.setdefault(comp, []).append(mx)
        if comp in lo:
            lo[comp] = min(lo[comp], mn)
            hi[comp] = max(hi[comp], mx)
        else:
            lo[comp], hi[comp] = mn, mx
    if n_dropped:
        print(f'    dropped {n_dropped} temperature points outside '
              f'{T_FLOOR:.0f}-{T_CEIL:.0f} K as digitisation artefacts')
    m = df_parsed.set_index('composition')['host_system'].to_dict()
    # Pool every curve endpoint per host, then take the 5th/95th percentile.
    # Absolute min/max are dominated by digitisation artefacts: the O-W host
    # reports 11 K when the median run in the dataset starts near 302 K, which
    # would make a low-temperature transition look crossed when it never was.
    pooled_lo, pooled_hi = {}, {}
    for comp in lo:
        h = m.get(comp)
        if h is None:
            continue
        pooled_lo.setdefault(h, []).extend(all_lo[comp])
        pooled_hi.setdefault(h, []).extend(all_hi[comp])
    out = {}
    for h, los in pooled_lo.items():
        his = pooled_hi[h]
        los, his = sorted(los), sorted(his)
        p5 = los[max(0, int(0.05 * (len(los) - 1)))]
        p95 = his[min(len(his) - 1, int(0.95 * (len(his) - 1)))]
        out[h] = (p5, p95, len(los), min(los), max(his))
    return out


def seed_hypotheses(path=TAXONOMY):
    """Map host_system -> [prototype ids that name it in example_host_systems].

    These are hypotheses to confirm against the compositions, not answers. A
    host named by more than one prototype is genuinely mixed and has to be
    split composition-by-composition.
    """
    out = {}
    if not os.path.exists(path):
        return out
    for p in json.load(open(path))['prototypes']:
        for hs in (p.get('example_host_systems') or []):
            out.setdefault(hs, []).append(p['id'])
    return out


def parse_composition(s):
    """Return (reduced_formula, {element: atomic_fraction}) or (None, None).

    Mirrors generate_data.py: a trailing '_...' suffix is an annotation on the
    composition string, not part of the formula.
    """
    if not isinstance(s, str) or not s.strip():
        return None, None
    t = s.split('_')[0].strip()
    try:
        c = Composition(t)
        if len(c) == 0 or c.num_atoms <= 0:
            return None, None
        return c.reduced_formula, c.fractional_composition.as_dict()
    except Exception:
        return None, None


def split_host_dopants(fracs, threshold=DOPANT_THRESHOLD):
    """Split a fractional composition into host elements and dopant candidates."""
    host = sorted(e for e, f in fracs.items() if f >= threshold)
    dop = sorted(((e, f) for e, f in fracs.items() if f < threshold),
                 key=lambda ef: -ef[1])
    return host, dop


def hand_label(sample_information):
    """Pull the human-entered MaterialFamily out of the flattened sample_information.

    HELD OUT, NOT AN INPUT. These labels mix three axes (chemical class,
    structure prototype, specific compound) and are the thing this project
    replaces. They are carried in the parquet only so the finished
    classification can be validated against them later, and are deliberately
    kept out of the chunk files so they cannot anchor the annotation.
    """
    if not isinstance(sample_information, str) or 'MaterialFamily' not in sample_information:
        return None
    # flatten_dict emits 'Key:category (comment)' segments joined by ' | '.
    m = re.search(r'MaterialFamily\s*:\s*([^|]+)', sample_information)
    if not m:
        return None
    v = re.sub(r'\s*\(.*$', '', m.group(1)).strip()
    return v or None


def main():
    print(f'Reading {IN_PATH} ...')
    df = pd.read_parquet(
        IN_PATH,
        columns=['SID', 'sample_id', 'sample_name', 'composition', 'DOI',
                 'sample_information', 'title', 'year', 'journal_short'],
    )
    print(f'  {len(df)} TE samples, {df.SID.nunique()} papers, '
          f'{df.composition.nunique()} unique composition strings')

    df['holdout_hand_label'] = df['sample_information'].map(hand_label)

    # --- Per-composition parse (once per unique string, not per sample) ------
    print('Parsing compositions ...')
    uniq = sorted(df.composition.dropna().unique())
    parsed = {}
    for s in tqdm.tqdm(uniq):
        formula, fracs = parse_composition(s)
        if formula is None:
            continue
        host, dop = split_host_dopants(fracs)
        if not host:
            continue
        parsed[s] = {
            'reduced_formula': formula,
            'host_system': '-'.join(host),
            'n_host_elements': len(host),
            'dopant_candidates': '-'.join(e for e, _ in dop),
            'dopant_fracs': json.dumps({e: round(f, 5) for e, f in dop}),
            'host_fracs': json.dumps(
                {e: round(f, 5) for e, f in sorted(fracs.items()) if e in set(host)}),
        }
    n_bad = len(uniq) - len(parsed)
    print(f'  parsed {len(parsed)} / {len(uniq)} composition strings '
          f'({n_bad} unparseable, dropped)')

    df_parsed = pd.DataFrame.from_dict(parsed, orient='index')
    df_parsed.index.name = 'composition'
    df_parsed = df_parsed.reset_index()

    # --- Composition-level table -------------------------------------------
    agg = (df.groupby('composition')
             .agg(n_samples=('sample_id', 'size'),
                  n_papers=('SID', 'nunique'),
                  example_sample_name=('sample_name', 'first'),
                  example_SID=('SID', 'first'),
                  example_DOI=('DOI', 'first'),
                  example_title=('title', 'first'),
                  holdout_hand_label=('holdout_hand_label',
                                      lambda s: s.dropna().mode().iat[0]
                                      if s.notna().any() else None))
             .reset_index())

    df_comp = df_parsed.merge(agg, on='composition', how='left')
    shares = [sublattice_share(h, f) for h, f in
              zip(df_comp.host_system, df_comp.host_fracs)]
    df_comp['axis_x_minor'] = [t[0] for t in shares]
    df_comp['axis_minor_el'] = [t[1] for t in shares]
    df_comp['axis_major_el'] = [t[2] for t in shares]
    df_comp['axis_is_dilute'] = df_comp.axis_x_minor.notna() & (
        df_comp.axis_x_minor < DILUTE_SUBLATTICE)
    nb = int(df_comp.axis_is_dilute.sum())
    print(f'  {int(df_comp.axis_x_minor.notna().sum())} compositions sit on a '
          f'same-group substitution axis; {nb} are dilute (<{DILUTE_SUBLATTICE:.0%} '
          f'of the shared site) and are borderline host assignments')
    df_comp = df_comp.sort_values('n_samples', ascending=False, kind='stable')
    os.makedirs(OUT_DIR, exist_ok=True)
    df_comp.to_parquet(OUT_DIR + 'df_compositions.parquet', index=False, engine='pyarrow')
    print(f'  -> {OUT_DIR}df_compositions.parquet  ({len(df_comp)} rows)')

    # --- Host-system table (the annotation unit) ---------------------------
    print('Aggregating host systems ...')
    # Sample-level view, so n_samples/n_papers per host are real counts.
    df_s = df.merge(df_parsed[['composition', 'host_system', 'reduced_formula',
                               'dopant_candidates', 'n_host_elements']],
                    on='composition', how='inner')

    def top_comps(g):
        vc = g.value_counts()
        return '; '.join(f'{c} ({n})' for c, n in vc.head(N_EXAMPLE_COMPS).items())

    def top_dopants(g):
        c = {}
        for s in g.dropna():
            for e in (x for x in s.split('-') if x):
                c[e] = c.get(e, 0) + 1
        return ', '.join(f'{e} ({n})' for e, n in
                         sorted(c.items(), key=lambda kv: -kv[1]))

    def top_families(g):
        vc = g.dropna().value_counts()
        return '; '.join(f'{v} ({n})' for v, n in vc.head(4).items())

    def top_titles(g):
        seen = []
        for t in g.dropna():
            t = str(t).strip().strip('"')
            if t and t not in seen:
                seen.append(t)
            if len(seen) >= N_EXAMPLE_TITLES:
                break
        return ' | '.join(seen)

    df_host = (df_s.groupby('host_system')
                   .agg(n_samples=('sample_id', 'size'),
                        n_papers=('SID', 'nunique'),
                        n_compositions=('composition', 'nunique'),
                        n_host_elements=('n_host_elements', 'first'),
                        example_compositions=('composition', top_comps),
                        dopant_candidates=('dopant_candidates', top_dopants),
                        holdout_hand_labels=('holdout_hand_label', top_families),
                        example_titles=('title', top_titles))
                   .reset_index())

    df_host = df_host.sort_values(['n_samples', 'host_system'],
                                  ascending=[False, True], kind='stable').reset_index(drop=True)
    total = df_host.n_samples.sum()
    df_host['cum_coverage'] = (df_host.n_samples.cumsum() / total).round(5)
    df_host['rank'] = df_host.index + 1
    df_host['chunk'] = (df_host.index // CHUNK_SIZE) + 1

    df_host.to_parquet(OUT_DIR + 'df_host_systems.parquet', index=False, engine='pyarrow')
    print(f'  -> {OUT_DIR}df_host_systems.parquet  ({len(df_host)} rows, '
          f'{df_host.chunk.max()} chunks of {CHUNK_SIZE})')

    # --- Coverage table -----------------------------------------------------
    cov = (df_host.groupby('chunk')
                  .agg(n_hosts=('host_system', 'size'),
                       n_samples=('n_samples', 'sum'),
                       n_compositions=('n_compositions', 'sum'),
                       cum_coverage=('cum_coverage', 'max'))
                  .reset_index())
    cov.to_csv(OUT_DIR + 'coverage.csv', index=False)
    print(f'  -> {OUT_DIR}coverage.csv')

    # --- Conversation chunks ------------------------------------------------
    print('Writing chunks ...')
    hyp = seed_hypotheses()
    trans = phase_transitions()
    distort = distortion_series()
    print('  Computing measured temperature ranges ...')
    trange = measured_temperature_range(df_parsed)
    print('  Detecting isoelectronic solid-solution axes ...')
    axes = alloy_axes(df_comp)
    print(f'    {len(axes)} host systems are solid-solution series')

    # Structure references, if scripts/build_structure_reference.py has run.
    # These are the only non-model evidence available at annotation time.
    struct = {}
    sp = OUT_DIR + 'df_host_structures.parquet'
    if os.path.exists(sp):
        for r in pd.read_parquet(sp).itertuples():
            struct[r.host_system] = r
        print(f'  structure references for {len(struct)} host systems')
    chunk_dir = os.path.join(OUT_DIR, 'chunks') + os.sep
    os.makedirs(chunk_dir, exist_ok=True)
    for old in os.listdir(chunk_dir):
        if old.startswith('chunk_') and old.endswith('.md'):
            os.remove(chunk_dir + old)

    for chunk_id, g in df_host.groupby('chunk'):
        lines = [
            f'# Host systems -- chunk {chunk_id:03d} of {df_host.chunk.max()}',
            '',
            f'Ranks {g["rank"].min()}-{g["rank"].max()} by sample count. '
            f'These {len(g)} host systems cover {g.n_samples.sum()} samples '
            f'({g.n_samples.sum() / total * 100:.2f}% of the TE set); '
            f'cumulative through this chunk: {g.cum_coverage.max() * 100:.2f}%.',
            '',
            'Assign each host system a structural prototype from '
            '`data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new '
            'one in `taxonomy/prototypes_proposed.jsonl` first. Append results '
            'to `data/annotated/annotations/family_assignments.jsonl`.',
            '',
            'The hand-entered MaterialFamily labels are deliberately NOT shown '
            'here -- they are held out in `df_host_systems.parquet` to validate '
            'this classification later. Decide from the compositions.',
            '',
            'A "seed hypothesis" line means the taxonomy already names this host '
            'under that prototype. Confirm it against the compositions rather '
            'than accepting it; two or more listed means the host is mixed and '
            'needs splitting per composition.',
            '',
            'Evidence follows the project precedence. Your judgement about the '
            'thermoelectric chemistry decides the prototype. [ref 1] is '
            'TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. '
            '[ref 2] is Materials Project. Within a formula, polymorphs are ranked '
            'by ICSD reference count and the top one is marked PRIMARY -- not by '
            'e_above_hull, which is unusable for layered chalcogenides in the 2019 '
            'dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting '
            'on fewer than 5 ICSD references is flagged weak; the ambient phase may '
            'simply be absent from the snapshot, as it is for Bi2Se3.',
            '',
            'While you have the host in view, also record what each minor element '
            'DOES, in `dopant_roles` -- the role follows from the prototype and '
            'cannot be judged without it. A median host has 2 such elements. Not '
            'everything listed is a dopant: O, C, N and H are usually milling or '
            'pressing residue, and an element just under 5 at.% may be an alloying '
            'end member rather than dilute doping. The doping LEVEL is computed '
            'later from the parsed fractions -- do not work it out by hand here.',
            '',
            'A polymorph list is NOT a thermal sequence. SnSe has three known '
            'structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is '
            'metastable (2 icsd refs against 32). Put thermally reached phases in '
            '`phases` with their transition temperatures, and everything else in '
            '`other_polymorphs` with an occurrence reason. hull and icsd counts are '
            'shown to help you tell them apart.',
            '',
            'A host may need MORE THAN ONE prototype. Transport is measured across '
            'a wide window and many thermoelectrics transform inside it, so where a '
            '"MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with '
            'its own temperature range in the `phases` field. Transition '
            'temperatures shown are approximate and composition-dependent.',
            '',
            'Both references describe which phases EXIST in a chemistry, not which '
            'phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel '
            '(227) while almost every sample in it is Al-doped wurtzite ZnO (186). '
            'Weigh them against the compositions; do not follow them blindly.',
            '',
        ]
        for _, r in g.iterrows():
            lines.append(f'## {r.host_system}')
            lines.append(f'- rank {r["rank"]} | {r.n_samples} samples | '
                         f'{r.n_papers} papers | {r.n_compositions} compositions')
            lines.append(f'- compositions: {r.example_compositions}')
            if r.dopant_candidates:
                lines.append(f'- dopant candidates (<{DOPANT_THRESHOLD:.0%} at.): '
                             f'{r.dopant_candidates}')
            # Evidence is listed in the project's precedence order: the
            # prototype judgement leads, TEDesignLab is the first data
            # reference, Materials Project fills in only what it lacks.
            h = hyp.get(r.host_system)
            if h:
                lines.append(f'- seed hypothesis (confirm): {", ".join(h)}'
                             + ('  <-- MIXED, split per composition' if len(h) > 1 else ''))
            ax = axes.get(r.host_system)
            if ax:
                lines.append(
                    f'- solid-solution axis: {ax["a"]}/({ax["a"]}+{ax["b"]}) spans '
                    f'{ax["lo"]:.2f}-{ax["hi"]:.2f} (median {ax["med"]:.2f}) over '
                    f'{ax["n"]} compositions')
                if ax.get('same_site_uncertain'):
                    lines.append(
                        '     CHECK: same periodic group, but oxygen often occupies '
                        'its own sublattice (BiCuSeO, LaFeAsO) rather than '
                        'substituting for the heavier chalcogen. Confirm the two '
                        'share a site before treating this as a substitution axis.')
                else:
                    lines.append(
                        '     ISOELECTRONIC SERIES: the parent compound depends on '
                        'the composition, not on this host. Near either end the '
                        'minor element is a dilute substituent; in the middle it is '
                        'a genuine alloy. Record the axis, not one parent -- and '
                        'note the 5% split used the whole formula, not the '
                        'sublattice, so its cut lands at a different level on each '
                        'site.')
            tr = trange.get(r.host_system)
            if tr:
                extra = ''
                if tr[3] < tr[0] - 40 or tr[4] > tr[1] + 40:
                    extra = f'; full span incl. outliers {tr[3]:.0f}-{tr[4]:.0f} K'
                lines.append(f'- measured range: {tr[0]:.0f}-{tr[1]:.0f} K '
                             f'(5th-95th pct of {tr[2]} curves{extra})')
                crossed = []
                for pid in (h or []):
                    if pid in distort:
                        continue  # the series block below says it better
                    for t in trans.get(pid, []):
                        T = t.get('T_K')
                        # compound_specific transitions (e.g. BaTiO3 within the
                        # perovskite family) would otherwise fire on every host
                        # sharing the prototype, most of which never transform.
                        if t.get('compound_specific'):
                            continue
                        if T is not None and tr[0] <= T <= tr[1]:
                            tgt = t.get('to') or 'melt/decomposition'
                            crossed.append(f'{pid} -> {tgt} at ~{T} K ({t["note"]})')
                for c in crossed:
                    lines.append(f'  !! MEASUREMENT CROSSES A TRANSITION: {c}')
                    lines.append('     Record each phase with its own temperature '
                                 'range, not a single prototype.')
                for pid in (h or []):
                    ds = distort.get(pid)
                    if not ds:
                        continue
                    applies = ds.get('applies_to_hosts')
                    if applies and r.host_system not in applies:
                        continue
                    inside = [st for st in ds['steps']
                              if not (st['t_max_K'] is not None and st['t_max_K'] <= tr[0])
                              and not (st['t_min_K'] is not None and st['t_min_K'] >= tr[1])]
                    if len(inside) < 2:
                        continue
                    lines.append(f'  !! DISTORTION SERIES ({ds["compound"]}): the measured '
                                 f'range spans {len(inside)} steps of one prototype --')
                    for st in inside:
                        lo = '' if st['t_min_K'] is None else f'{st["t_min_K"]:.0f}'
                        hi = '' if st['t_max_K'] is None else f'{st["t_max_K"]:.0f}'
                        mp = f' {st["mp_id"]}' if st.get('mp_id') else ''
                        lines.append(f'       {st["label"]:8s} {st["spacegroup_symbol"]} '
                                     f'({st["spacegroup_number"]})  {lo}-{hi} K{mp}')
                    lines.append(f'     {ds["note"]}')
            sr = struct.get(r.host_system)
            if sr is not None:
                t1 = getattr(sr, 'candidates_tedl', None)
                t2 = getattr(sr, 'candidates_mp', None)
                if isinstance(t1, str) and t1:
                    lines.append(f'- [ref 1] TEDesignLab / ICSD: {t1}')
                if isinstance(t2, str) and t2:
                    label = ('[ref 2] MP, ranked by ICSD evidence'
                             if isinstance(t1, str) and t1
                             else '[ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry)')
                    lines.append(f'- {label}: {t2}')
            if r.example_titles:
                lines.append(f'- papers: {r.example_titles}')
            lines.append('')
        with open(f'{chunk_dir}chunk_{chunk_id:03d}.md', 'w') as f:
            f.write('\n'.join(lines))

    print(f'  -> {chunk_dir}chunk_001.md ... chunk_{df_host.chunk.max():03d}.md')
    print('\nDone.')


if __name__ == '__main__':
    main()
