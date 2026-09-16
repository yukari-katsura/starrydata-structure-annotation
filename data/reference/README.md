# External structure references

Two downloaded reference sets, used to check prototype assignments against
measured structures and to resolve database ids offline.

| file | rows | tracked | what it gives |
|---|---:|---|---|
| `tedesignlab-complete-data.xlsx` | 2,701 (1,837 compounds) | yes | ICSD id + experimentally determined space group per compound, plus computed thermoelectric quantities: band gap, κ_L, β quality factor (p,n), effective masses, valley degeneracy, bulk modulus, average coordination number, Grüneisen parameter |
| `mp_190822.csv` | 119,570 | **no** (35 MB, gitignored) | Materials Project dump of 2019-08-22: `material_id`, formula, space group symbol, `e_above_hull`, band gap, ICSD cross-references |

Together they make stage 2 possible without hitting the Materials Project API,
and they are the only evidence in this project that does not come from a
language model.

## Derived index

`python scripts/build_structure_reference.py` links both to the annotation's
host systems and writes:

- `data/annotated/input/df_structure_refs.parquet` — one row per reference entry,
  keyed to a host system where one matches (24,465 rows; 22,623 matched)
- `data/annotated/input/df_host_structures.parquet` — per host system: space
  groups ranked by ICSD evidence, Materials Project ground states with `mp_id`,
  TEDesignLab space groups and transport quantities

2,496 of 3,648 host systems get a structure reference, covering 90.2% of
samples; 1,857 have an experimentally-backed space group (74.3% of samples).

## Two things that will bite you

**Rank by evidence, not by entry count.** The MP dump contains every computed
polymorph, most of them hypothetical and well above the hull. Counting entries
lets those bury the real structure — Pb-S returned no `Fm-3m` at all until the
ranking was changed, because one ground-state entry carrying 33 ICSD references
was outvoted by a handful of one-off computed structures. The index now ranks
space groups by summed ICSD references and reports the lowest-hull entry per
formula separately.

**A reference describes a chemistry, not a sample.** These files say which
phases exist in an element system, not which phase a given paper synthesised.
`Al-O-Zn` is best attested as ZnAl2O4 spinel (227), while nearly every
Starrydata sample in that host is Al-doped wurtzite ZnO (186). Use the space
groups as candidate evidence to weigh against the composition, never as the
answer.
