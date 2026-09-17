# Material-family annotation

Reclassifying Starrydata's thermoelectric samples by **crystal structure prototype**,
then using that classification to attach Materials Project structures, identify
dopants, and estimate doping levels.

## Why

The existing `MaterialFamily` field in `sample_info` mixes three incompatible axes:

| axis | examples |
|---|---|
| chemical class | `Oxide`, `Telluride`, `Antimonide`, `Chalcogenide` |
| structure prototype | `Half-Heusler`, `Skutterudite`, `Clathrate`, `Zintl` |
| specific compound | `Bi2Te3`, `PbTe`, `ZnO`, `SnSe` |

So one host system carries several unrelated labels at once — `Co-Sb` is recorded
as Skutterudite (984), Antimonide (30) and Heavy-Fermion (13); `Ca-Co-O` as
Cobaltite (646), Oxide (129) and Perovskite (4). The labels are also incomplete:
only 1,825 of 3,648 host systems have one at all.

This project replaces them with a single-axis prototype classification, which is
what the downstream stages actually need — you cannot look up a structure or
reason about a dopant site from "Telluride".

### Taxonomy lineage

`prototypes_seed_v3.json` merges two independently built drafts:

| source | size | contributed |
|---|---|---|
| `prototypes_seed_v2.json` | 135 | breadth — derived by surveying the 700 largest host systems (cuprates, Ruddlesden-Popper, pyrochlore, homologous tetradymites, misfit chalcogenides, borides, heavy-fermion intermetallics) |
| `data/dict/thermoelectric_structure_ontology_v0.2.json` | 51 | assignment epistemics, the field vocabulary, and 13 prototypes v2 missed (inverse/quaternary Heusler, filled skutterudite split, clathrate type VIII, Zintl 3-1-3, Mn5Si3, hollandite, fresnoite, langasite, langatate, a-IGZO, Chevrel, unresolved-crystalline) |

All 51 v0.2 structures are carried into v3; 38 entries merge both lineages, and
each records its sources in `merged_from`. Rebuild with
`python scripts/merge_taxonomy_v3.py`.

**Both lineages are LLM-generated** — v0.2 was drafted in discussion with ChatGPT,
v2 by surveying the data with Claude. Where they agree that is a weak check, not
corroboration: two models drawing on the same conventions can be wrong the same
way. (The separate hand-written family list at `data/dict/material_families.json`
is not an input to this project.)

That is no longer the whole story: `data/reference/` now holds TEDesignLab
(ICSD-backed space groups) and a Materials Project dump, so the taxonomy can be
tested against measured structures rather than only against itself.

```bash
python scripts/build_structure_reference.py     # index references to host systems
python scripts/check_taxonomy_against_refs.py   # test taxonomy space groups
```

### Candidate structure selection

Precedence, highest first:

1. **Thermoelectrics knowledge** decides the prototype. The references supply
   evidence for that judgement; they do not make it.
2. **TEDesignLab** — ICSD-backed and thermoelectric-specific. Where it covers a
   formula, its space group selects *which* Materials Project entry to take,
   rather than the most stable one being taken blindly. 649 formula-polymorph
   candidates across 256 host systems.
3. **Materials Project**, lowest `e_above_hull`, and only for formulas
   TEDesignLab does not cover. 7,853 formulas across 2,447 host systems.

98 TEDesignLab space groups have no Materials Project counterpart for that
formula; they are flagged rather than silently replaced.

### Phases and transitions

A host may need more than one prototype. Transport is measured from a median
302 K to 740 K, and 58% of curves exceed 700 K, so many thermoelectrics
transform *inside* the measured window — SnSe Pnma→Cmcm at ~800 K (where its
record ZT is reported), GeTe R3m→Fm-3m at ~700 K, Cu2Se and Ag2Se turning
superionic near 400 K.

Two independent signals flag this, and chunk files show both:

- 11 prototypes carry `phase_transitions` in the taxonomy; a
  `MEASUREMENT CROSSES A TRANSITION` line appears when a host's own measured
  range spans one.
- 115 formulas across 99 host systems have more than one ICSD polymorph in
  TEDesignLab, each with its own `mp_id` — SnSe resolves to mp-691 (Pnma),
  mp-2168 (Cmcm) and mp-2693 (Fm-3m).

Record these in the ledger's `phases` array with per-phase temperature ranges
and `mp_id`s, not as a single label.

**Distortion series.** Some prototypes change space group without changing
prototype. `reo3_wo3` carries a `distortion_series` field giving WO3's full
sequence -- epsilon (Pc) / delta (P-1) / gamma (P2_1/n) / beta (Pbcn) / alpha
(P4/ncc) / cubic (Pm-3m) -- with transition temperatures, because the cubic
aristotype the entry originally named is essentially never observed below the
melt. The `O-W` host's 49-1100 K window crosses three of those steps. Where a
series exists the chunk file prints it instead of individual transition lines.

Measured ranges are reported as the 5th-95th percentile of curve endpoints, not
the absolute extremes, and the full span is shown alongside when it differs
materially. Absolute extremes are dominated by digitisation artefacts: `Se-Sn`
reported 11-980 K where the robust range is 293-921 K, which would have made
every low-temperature transition look crossed.

**A polymorph list is not a thermal sequence.** TEDesignLab reports the
structures that exist for a formula; it does not say which are reached by
heating. SnSe has three, but only two are thermal phases:

| structure | mp_id | e_above_hull | ICSD refs | role |
|---|---|---:|---:|---|
| Pnma (62) | mp-691 | 0.000 | 32 | ambient phase |
| Cmcm (63) | mp-2168 | 0.011 | 11 | high-T phase, from ~800 K |
| Fm-3m (225) | mp-2693 | 0.004 | 2 | metastable — epitaxial/high-pressure, never on heating |

So SnSe has **one** transition, not two. N thermal phases have N-1 transitions;
`transition_K` on a phase is the temperature at which it becomes the *next* one
and is null on the last. Structures that heating does not produce go in
`other_polymorphs` with an `occurrence` reason, so the two can never be
confused. A worked SnSe record is in `family_assignments.schema.json` under
`examples`.

This is also why the ledger uses an array of objects rather than parallel arrays
of mp_ids, space groups and temperatures: those lists have different lengths —
three structures, two phases, one transition — and would silently desync. Transition temperatures in the taxonomy are
approximate and composition-dependent; `transition_basis` records whether a
value came from the paper or from a default.

Measured ranges are computed from the curve data with a 10–3000 K filter —
about 6% of digitised curves contain points below 10 K, including negative
temperatures, which would otherwise make every range start at zero and hide
which transitions are genuinely crossed.

Current result: across 313 host systems that have both a seed hypothesis and an
ICSD-backed space group, the prototype's space group is **present among the
measured set for 82%**, and is the **best-attested one for 63%**. The 55
disagreements are listed in `validation/taxonomy_vs_references.md` for review.

Read them carefully. A reference describes which phases exist in a chemistry, not
which phase a paper synthesised — `Al-O-Zn` is best attested as ZnAl2O4 spinel
while nearly every sample in that host is Al-doped wurtzite ZnO. Some
disagreements are still real taxonomy weaknesses: `O-W` is listed at the cubic
ReO3 aristotype (221) when monoclinic WO3 (14) carries 22 ICSD references.

v0.2 also corrected two errors in v2: Chevrel had been dropped, and `Ba-Ga-Sn`
was filed under clathrate type I when β-Ba8Ga16Sn30 is type VIII.

**Composition gives a candidate, not a confirmed structure.** v0.2's principle is
carried into v3 and into the ledger schema: `assignment_basis` records how the
call was made and `experimentally_confirmed` is true only when the paper actually
reports the structure. Stage 1 works from composition, so it will almost always
be `false` — confirmation comes later, from the papers.

### The hand labels are held out, not used

The new taxonomy was built from the compositions themselves, by surveying the 700
highest-count host systems. The hand-entered labels were **not** consulted when
choosing prototypes, and the chunk files deliberately do **not** show them.

They are kept in `df_host_systems.parquet` as `holdout_hand_labels`, and the
v0.2 `legacy_label_map` was lifted out of the taxonomy into
`validation/legacy_label_map.json`, for one purpose: once stage 1 is done, they become an independent set to validate the new
classification against — measuring where the two agree, and inspecting every
disagreement. Showing them during annotation would destroy that independence and
anchor the result to the classification being replaced.

## Annotation unit: the host system

Downstream work (structure, dopant, doping level) is a property of the
composition, not of the paper. But 27,456 unique composition strings is too many
to reason about individually, and most differ only by dopant level.

So each composition is split at **5 at.%**: elements at or above that fraction are
the *host*, elements below it are *dopant candidates*.

```
Zn0.98Al0.02O          -> host O-Zn        dopant Al
Pb0.98Na0.02Te         -> host Pb-Te       dopant Na
Bi0.5Sb1.5Te3          -> host Bi-Sb-Te    (no dopant; substitutional solid solution)
Yb0.2Co4Sb12           -> host Co-Sb       filler Yb
```

That collapses 27,456 compositions into **3,648 host systems**, and the split is
itself the input to stage 3. Coverage is steep — the annotation is far smaller
than the row count suggests:

| host systems | share of samples |
|---:|---:|
| 50 (chunk 1) | 47.0% |
| 250 (chunks 1–5) | 71.1% |
| 500 (chunks 1–10) | 80.5% |
| 1000 (chunks 1–20) | ~89% |

The threshold is a default, not a commitment: `dopant_fracs` and `host_fracs` are
stored per composition, so it can be revisited without re-deriving anything.

## Layout

```
data/annotated/
  input/
    df_compositions.parquet     27,456 rows -- one per unique composition string
    df_host_systems.parquet      3,648 rows -- one per host system (the annotation unit)
    coverage.csv                 cumulative sample coverage per chunk
    df_structure_refs.parquet    ICSD/MP reference entries keyed to host systems
    df_host_structures.parquet   per host: space groups by evidence, MP ground states
    chunks/chunk_NNN.md          73 conversation-sized batches, coverage-ordered
  taxonomy/
    prototypes_seed_v3.json      148 prototypes  <- current
    prototypes_seed_v2.json      superseded (135, survey-derived)
    prototypes_seed_v1.json      superseded (68)
    prototypes_proposed.jsonl    new prototypes proposed during annotation, pending review
  validation/
    legacy_label_map.json        curator labels, HELD OUT -- for validating stage 1 only
    taxonomy_vs_references.md    taxonomy space groups vs ICSD/MP evidence
  annotations/
    family_assignments.jsonl     append-only ledger, one record per host system
    family_assignments.schema.json
  by_family/                     stage 2 output: one shard per prototype
```

## Provenance

```
data/raw/*.csv                      DB snapshot 2026-09-04 02:00:02 JST, renumbered IDs
  -> scripts/generate_data.py       dedupe, parse compositions, filter to samples with TE curves
data/processed/df_samples.parquet   52,027 samples / 9,519 papers / 27,456 compositions
  -> scripts/generate_annotation_data.py
data/annotated/input/
```

Regenerate the inputs with:

```bash
python scripts/generate_annotation_data.py
```

It is deterministic and safe to re-run; it rewrites `input/` and leaves
`taxonomy/` and `annotations/` untouched.

## Stages

### Stage 1 — assign a structural prototype to each host system

Done interactively with Claude Code, one chunk at a time. For each host system in
`chunks/chunk_NNN.md`, pick a `prototype_id` from the seed taxonomy or propose a
new one, and append a record to `annotations/family_assignments.jsonl`:

```json
{"host_system":"Co-Sb","prototype_id":"skutterudite","confidence":"high",
 "basis":"CoSb3 and Co4Sb12 dominate; Yb/Ba/In appear only as cage fillers in RxCo4Sb12.",
 "seed_hypothesis_outcome":"refined","assignment_basis":["composition","llm_materials_knowledge"],
 "experimentally_confirmed":false,"is_mixed":true,"alt_prototype_ids":["filled_skutterudite"],
 "chunk":1,"rank":1,"n_samples":1778,
 "annotated_by":"claude-opus-5","annotated_at":"2026-09-16"}
```

Decide from the compositions, the dopant candidates and the paper titles. The
`basis` must not appeal to the hand labels.

A host system that genuinely contains more than one prototype (e.g. `Fe-Si`, which
holds both β-FeSi₂ and B20 FeSi) gets `"is_mixed": true` and
`alt_prototype_ids`, and is split composition-by-composition in stage 2 rather
than forced into one label.

Each chunk entry may carry a **seed hypothesis** — the prototype whose
`example_host_systems` already names that host. It is a hypothesis to confirm
against the compositions, not an answer; record what happened to it in
`seed_hypothesis_outcome`, because rejections and refinements are how the seed
taxonomy earns a v3. Two or more hypotheses on one host means it is genuinely
mixed (`Ca-Co-O` holds both Ca3Co4O9 and Ca3Co2O6) and must be split per
composition. 445 of the 3,648 hosts, covering 75% of samples, carry a hypothesis.

New prototypes go into `taxonomy/prototypes_proposed.jsonl` *before* being used,
and are reviewed and folded into a `v4` seed file before sharding.

After each chunk:

```bash
python scripts/check_annotations.py            # validate + progress
python scripts/check_annotations.py --chunk 3  # one chunk
```

This checks the ledger (every host system exists, every prototype id is defined,
nothing is duplicated, required fields present) *and* the taxonomy itself (every
`discriminate_from` target resolves, every `structural_class` is declared, every
`example_host_systems` key exists in the input table). It exits non-zero on any
problem.

### Stage 2 — shard by prototype, assign Materials Project structures

Once stage 1 covers enough of the set, `by_family/` gets one file per prototype
holding its compositions and dopant candidates. Each shard is then worked through
in its own conversation: resolve the host to a Materials Project entry
(`mp_id`, space group, lattice) via the MP API.

`mp_id` is deliberately `null` everywhere in the seed taxonomy — these must be
resolved by querying Materials Project, never filled in from memory.

Prototypes needing special handling in this stage are flagged in their `notes`
and `confidence_note`: `misfit_cobaltite` and `misfit_layered_chalcogenide`
(incommensurate composites — two subsystems each, no single MP entry),
`hms_chimney_ladder` (incommensurate; only approximants exist in MP),
`quasicrystal_approximant` (no periodic structure — map to an approximant and say
so), `bi_chalcogenide_complex` (every composition is effectively its own
structure), and `amorphous` / `metallic_glass` / `composite_multiphase` (skip).

### TEDesignLab ids: the ML-ready subset

`tedl_id` is kept separate from `mp_id` and `icsd_id` because it answers a
different question. An mp_id points at a *structure*; a tedl_id points at a
computed **feature vector** -- band gap, band and DOS effective masses, valley
degeneracy, lattice thermal conductivity, mobility, the beta quality factor,
bulk modulus, average coordination number and Grueneisen parameter.

```
data/annotated/input/df_tedl_entries.parquet    2,701 entries x 18 features
data/annotated/df_tedl_linked_samples.parquet   10,420 samples carrying one
```

`tedl_id` is `<row>-<compound>-<icsd>`, e.g. `1133-Pb1Te1-648608`, and is the
first column of the table. Each part earns its place: the row number is what you
scroll to in the downloaded spreadsheet, the compound makes the id readable
without a lookup, and the ICSD collection code is what survives the sheet being
re-sorted or re-issued.

`tedl_row` is the 1-based **data** row; `tedl_excel_row` is the number in
Excel's row gutter, which is one higher because row 1 is the header. Both are
kept so neither has to be worked out.

**Why the key uses the ICSD code and not an mp_id.** Materials Project is open
and ICSD is licensed, so an mp_id is the friendlier identifier -- but it cannot
be the key: **356 of 2,701 entries (13%) have no mp_id by any route**, and a key
that is absent for an eighth of the table is not a key. The ICSD code is also
what TEDesignLab itself publishes, so it is the column you can see in the
downloaded file, and collection codes are never reused.

An `mp_id` column is provided instead, for open lookup, with `mp_id_source`
saying how it was obtained:

| source | entries | |
|---|---:|---|
| MP `icsd_ids` cross-reference | 2,268 | Materials Project asserting the link itself |
| formula + space group | 77 | our inference; can pick the wrong polymorph |
| none | 356 | not in the 2019 snapshot |

Note the first route: **MP publishes the ICSD cross-reference**, so an ICSD code
is resolvable without an ICSD licence for 84% of entries. It is a
cross-reference, not a dead end.

Row numbers are only meaningful for the file they came from.
`scripts/fetch_reference_data.py` records the SHA-256 of the copy these outputs
were built from and warns if a fresh download differs -- if it does, re-run
`build_structure_reference.py` before trusting a row number.

Paired columns arrive as "valence,conduction" strings and are split into
separate numeric columns so they can be used as features directly.

**The link runs through the host system, not the composition.** Starrydata
compositions are doped -- `Pb0.98Na0.02Te` -- while TEDesignLab entries are
stoichiometric parents -- `PbTe`. Matching on formula links 65 compositions;
matching through the host links **10,420 samples across 1,997 papers**, and a
doped PbTe sample inheriting the descriptors computed for the PbTe parent is the
physically meaningful association anyway.

`tedl_match` records how good the link is, and this matters for training:

| match | samples | meaning |
|---|---:|---|
| `host+spacegroup` | 7,512 | the descriptors belong to the structure actually assigned |
| `host only` | 2,346 | one entry for the host, space group not confirmed |
| `host only (N entries)` | 562 | several polymorphs; the wrong one may have been taken |

Filter to `host+spacegroup` for training. A descriptor computed for a different
polymorph is a different physical quantity -- LaVO4 appears twice, at sg 14 and
sg 141, with band gaps of 3.50 and 3.15 eV.

### CSV export

```bash
python scripts/export_csv.py --both     # -> data/annotated/csv/
```

Four tables are exported: `df_annotated_samples`, `df_annotated_compositions`,
`df_tedl_linked_samples` and `df_tedl_entries` (the TEDesignLab feature table,
0.5 MB, 2,701 x 29). `--flat` applies only to the tables that contain JSON
columns; the entries table has none, so it is written once.

Parquet stays the source of truth -- it preserves dtypes and nulls and is about
a tenth the size. The CSVs are a convenience copy and are gitignored.

`--flat` is usually what a spreadsheet wants: it drops the two JSON columns and
promotes what people actually read out of them -- `phase1_spacegroup`,
`phase1_mp_id`, `phase1_transition_K`, `dopant1_element`, `dopant1_role`,
`dopant1_substitutes_for`, `dopant1_site_fraction`. Note that the flat form
keeps only the first phase and the largest dopant; `n_phases` and `n_dopants`
say when something was left behind, and the full export keeps everything.

### Identifiers, and what a host system is not

**`host_system` is a routing key, not an identity.** The same element set can
hold several structures: `Fe-O` covers spinel Fe3O4 and corundum Fe2O3, `O-Ti`
covers rutile, anatase, corundum, rocksalt and Magneli phases. Keying an
assignment by host alone would claim something the data does not support.

Every assignment therefore carries a stable id and states the level it is
decided at:

| field | meaning |
|---|---|
| `assignment_id` | `HSA-<10 hex>` for host records, `CPA-<10 hex>` for composition records. sha1 of the natural key, so it survives regeneration, re-ranking and threshold changes |
| `determined_at` | `host`, `composition`, or `sample_required` |
| `is_authoritative` | false when a finer-grained record supersedes this one |
| `n_prototypes_below` | how many distinct prototypes the compositions under this host resolve to; >1 means the host label is not a structure |

Current split: **105 hosts decided at host level, 44 at composition level, 1
needing the sample**. By samples: 19,085 / 14,013 / 88.

`df_annotated_samples.parquet` carries `assignment_id` (the record that actually
decided that sample), `host_assignment_id` (its grouping), and `determined_at`,
so a claim about any sample can be traced to the record behind it.

Even composition is not always sufficient. alpha-Fe2O3 is hematite (corundum)
and gamma-Fe2O3 is maghemite (spinel) -- one formula, two structures -- so that
composition reads `sample_required` rather than being forced to an answer.

### Splitting mixed hosts by stoichiometry

47 hosts were flagged `is_mixed` -- one label standing over several real
structures, covering 14,294 samples. Most of them separate on composition alone:
Ca3Co4O9 and Ca3Co2O6 differ by their Co:Ca ratio, FeSi2 and FeSi by Si:Fe,
Bi2Te3 and BiTe by Bi:Te, SrTiO3 and Sr2TiO4 by Sr:Ti.

`scripts/apply_composition_splits.py` encodes those as element-ratio rules and
writes a prototype per composition:

```bash
python scripts/apply_composition_splits.py --dry-run   # see the split first
python scripts/apply_composition_splits.py
python scripts/build_annotated_samples.py              # fold into the sample table
```

This is inference from composition, not measurement, so
`experimentally_confirmed` stays **false** and the basis is recorded as
`composition + llm_materials_knowledge`. It narrows what needs a paper; it does
not replace one.

Result: samples needing a composition-level split fall from 14,294 to 73, and
the family shards go from 56 to 81 -- structures that were previously hidden
inside a mixed host now stand on their own (`ruddlesden_popper` 1,079 samples,
`filled_skutterudite` 669, `magneli_phase`, `brownmillerite`, `corundum`).

Two rules were wrong on the first pass and are worth knowing about. `Bi-Ca-Co-O`
came out backwards because Bi occupies the rocksalt block, so the Co:Ca
threshold calibrated on Ca-Co-O does not transfer. And Cu5FeS4 bornite is
neither chalcopyrite nor tetrahedrite; it has no taxonomy entry and is parked in
`unresolved_crystalline` rather than mislabelled.

### The curator's composition_details

`composition_details` is a top-level column of the raw samples table -- not a
key inside `sample_info`, and not surfaced by the upstream flattening, which is
why it was missed at first. 18,692 samples carry it, and it is transcribed from
the paper, so it outranks an inference from stoichiometry.

It is the only field that settles cases no element ratio can:

| composition | what the ratio says | what the curator says |
|---|---|---|
| `C` | carbon | graphite, soft carbon, rayon-based carbon |
| `B0.04C` | boron-doped carbon | boron-doped nanocrystalline diamond (NDE) |
| `Fe2O3` | corundum, from O:Fe | *both* alpha-Fe2O3 and gamma-Fe2O3 appear |

`data/processed/df_composition_details.parquet` ships it, chunk files show the
distribution per host, and `apply_composition_splits.py` uses it to override the
ratio rules.

**Every phrase rule is scoped to a chemistry.** Unscoped, they fire on
second-phase additives and mislabel the host: a graphene composite of SrTiO3
mentions "graphene", a CNT composite of MnSi1.75 mentions "nanotube". An early
version produced 15 such overrides, all wrong. Scoped, it produces 2, both
right.

**Fe2O3 shows the limit of composition-level work.** alpha-Fe2O3 is hematite
(corundum) and gamma-Fe2O3 is maghemite (spinel) -- same formula, different
structure -- so one composition string covers both. Rather than force an answer,
that composition is flagged `detail ambiguous - needs sample-level split`.
Resolving it properly means assigning per sample, not per composition.

### The verification gate

`scripts/verify_assignments.py` exists because of how errors were actually
caught while annotating chunks 1-3: **seven of nine were found because someone
looked at printed output**, not because anything failed. An unattended run does
no looking, so the looking has to be encoded. Run it after any annotation or
rebuild; it exits non-zero on failure.

Three layers:

| layer | what it does | on failure |
|---|---|---|
| **invariants** | valid prototype ids, unique keys and assignment_ids, physically plausible transition temperatures, unique tedl_id | exit 1 |
| **regressions** | pins the specific mistakes already made, so a rebuild cannot reintroduce them | exit 1 |
| **agreement** | checks every assignment against ICSD-backed space groups | reported, not enforced |

The regression layer is the valuable part. Each check is one line now but cost
real effort to find: SnTe returning a metastable zincblende, Sb2Te3 losing to a
hull artefact, Fe3O4 beaten by one ICSD reference, Rb3C60 falling below the 5%
threshold, composite additives relabelling their hosts, the WO3 distortion
series firing on Mo-O.

Agreement is reported rather than enforced because a disagreement can be
correct -- the reference describes a chemistry, the sample is one member of it.
The rate matters more than any single case, and it currently stands at **82%
(95/116 testable)**. `--apply` downgrades disagreeing assignments from high to
medium confidence and records why, so an automated run cannot quietly assert
something the references contradict.

The suite is negative-tested: injecting four of the original bugs makes exactly
those four checks fail.

### Running chunks unattended

```bash
caffeinate -i ./run_chunks.sh 5 10
```

`caffeinate -i` holds an idle-sleep assertion for the script's lifetime and
releases it on exit. Display and disk sleep do not stop computation and are left
alone. On a laptop the lid must stay open; a closed lid sleeps regardless.

**Run it from your own terminal, not from inside a Claude Code session.** A
session that runs this spawns a second Claude which also draws on your quota and
contributes nothing while the subprocess works.

One `claude -p` per chunk rather than one for the whole range, so each chunk is
bounded and a failure stops the loop with everything before it committed. After
each chunk it rebuilds the derived tables, runs the gate, and **stops without
committing if the gate fails**. It commits locally and never pushes.

Four guards, each from something that actually went wrong in a dry run:

| guard | why |
|---|---|
| `< /dev/null` on the `claude -p` call | it otherwise stalls 3s per chunk waiting for stdin that never arrives |
| `--output-format stream-json`, piped through `stream_progress.py` | output is buffered until exit, so a hung chunk and a working one look identical for twenty minutes. The terminal now shows each tool call, each message, the quota reading and a heartbeat when idle |
| ledger must grow by >=40 records | a quota limit, a refusal and a crash all look the same from outside: the ledger did not grow. Without this the loop runs every remaining chunk doing nothing and reports success |
| stop at 85% of the five-hour quota window | `stream-json` reports `rate_limit_event` utilisation per chunk. A chunk takes ~20 minutes, so starting one at 95% means it dies partway rather than not starting |

On a quota stop it exits 0 and prints the resume command, since that is an
orderly end rather than a failure.

### Runs that span days

```bash
QUOTA_MODE=wait caffeinate -i ./run_chunks.sh 19 73
```

`QUOTA_MODE=wait` sleeps until the five-hour window resets and carries on,
instead of stopping. Measured rates: **~11 points of the five-hour window per
chunk** (7-8 chunks per window) and **~1 point of the seven-day window per
chunk**. So a full run of the remaining chunks is roughly 7-8 windows, about
40 hours wall clock, of which ~18 hours is actual work.

The seven-day window is never waited on -- it recovers over days, not hours, so
`QUOTA_7D_STOP` (default 0.90) ends the run instead. `MAX_HOURS=36` adds a
wall-clock deadline. Raw streams are gzipped after each chunk; at 5-10 MB each a
55-chunk run would otherwise leave half a gigabyte behind.

Everything else still applies: it commits per chunk, never pushes, and stops
outright on a gate failure or a chunk that does not grow the ledger.

The terminal shows progress as it goes:

```
    0:12  Read     chunk_010.md
    1:03  » Now let me load the taxonomy id list and the schema.
    2:41  Bash     grep -n -A 12 '"id": "alb2"' prototypes_seed_v3.json
    4:15  [quota: five-hour window 29% used]
   18:52  done — 33 tool calls, 8 messages, 18.9 min
```

Under `nohup`, that lands in whatever you redirected to, so
`tail -f queued.out` gives the same view. The raw stream is kept per chunk for
later inspection.

Two things it still cannot do: notice that a whole chunk is subtly wrong in a
way no invariant covers, and verify anything in a host with no structure
reference -- a third of assignments now, rising down the tail.

### Checking an assignment against the paper

Nothing here has been read out of a paper, so `experimentally_confirmed` is
false throughout. `scripts/build_review_queue.py` ranks the cases where that
matters and links the specific papers that would settle each:

```bash
python scripts/build_review_queue.py           # top 40 into validation/needs_review.md
python scripts/build_review_queue.py --top 71  # all of them
```

A host is queued when it is mixed, when confidence is low or medium, when a
transition temperature came from a taxonomy default rather than a paper, when
the structure reference could not separate two polymorphs, or when a reference
or taxonomy disagreement was recorded.

Currently **71 of 150 hosts, covering 19,725 samples**. The dominant reason is
`MIXED` (47 hosts) — one label standing over several real structures. For those
the report lists each competing composition separately with the papers reporting
it, so the split can be made by reading rather than guessing.

Chunk files also carry DOI links directly on the `papers:` line, so the source
is one click away at the moment of assignment.

### Where doping work happens

Split by the kind of work, not by topic. The judgement is per host; the
arithmetic is per composition.

| work | unit | count | where |
|---|---|---:|---|
| What role does element E play in host H? | (host, element) | 4,474 pairs | **stage 1**, with the prototype |
| Which crystallographic site, by Wyckoff label | (host, element) | subset | stage 2, once the structure is resolved |
| What is x in Pb(1-x)Na(x)Te? | composition | 17,313 | stage 3, scripted |
| Nothing — no minor element present | composition | 10,143 (37%) | — |

The role belongs in stage 1 because it *follows from the prototype* and cannot
be judged without it: Yb in `Co-Sb` is a cage filler only once the host is known
to be a skutterudite. A median host has 2 minor elements, so this costs about
two extra calls per host while the chemistry is already in view — against
re-loading every host a second time later.

The level does not belong in a conversation at all. Once the role is fixed, x
comes straight from the parsed fractions already stored per composition.

### Isoelectronic substitution has no threshold

The 5 at.% split has two limits that matter here, and neither is fixed by moving
the number.

**The denominator is the whole formula, but substitution happens on a
sublattice.** In rocksalt Pb(Se,Te) the anion site is only half the atoms, so a
10% anion substitution reads as 5% atomic — exactly on the cut. The same
threshold therefore means a different site occupancy in every structure.

**Isoelectronic substitution is a continuum.** `PbSe0.99Te0.01` is doped PbSe,
`PbSe0.5Te0.5` is an alloy, and `PbTe0.9Se0.1` is doped PbTe — one axis, no
natural boundary. Of the 184 samples in the `Pb-Se-Te` host, 97 sit at 80–95%
Te, i.e. PbTe with a little Se rather than a pseudobinary alloy.

So the host system is a **routing key, not a parent compound**. Rather than
move the threshold, `generate_annotation_data.py` detects the axis: for every
pair of same-group elements in a host it measures x = A/(A+B) across the host's
compositions and reports the spread. **175 host systems are solid-solution
series** — `Bi-Sb-Te` (Bi/(Bi+Sb) 0.13–0.90 over 537 compositions), `Mg-Si-Sn`,
`Hf-Ni-Sn-Zr`, `Ge-Si`, `Pb-Se-Te` among them. For those, the parent compound is
assigned per composition in stage 3, not per host, and the role is recorded as
`isoelectronic_substitution` with the sublattice fraction rather than as doping.

**Why there is no 50% rule.** An obvious fix is to keep the ternary host only
near 50:50 substitution and otherwise file the composition under its dominant
end member. The dilute half of that is already in effect — for a 1:1 binary,
5% of the formula *is* 10% of the sublattice, which is why `PbSe0.99Te0.01`
already routes to `Pb-Se`. No composition in the dataset has a minority
sublattice share below 0.05; they have all left already.

The 50% half would be a serious error. Minority share of the shared site:

| share of shared site | compositions | samples |
|---|---:|---:|
| < 0.05 | 0 | 0 |
| 0.05 – 0.10 | 229 | 484 |
| 0.10 – 0.20 | 901 | 1,549 |
| 0.20 – 0.35 | 1,892 | 3,274 |
| 0.35 – 0.50 | 1,041 | 1,513 |

A band of x ≥ 0.35 would move 3,022 compositions and 5,307 samples onto dominant
end-member hosts — including **Bi0.5Sb1.5Te3, at x = 0.25 the single most common
composition in the dataset (348 samples)**. It would be refiled as Bi-doped
Sb2Te3, which is not how anyone describes the workhorse p-type alloy. The rule
has to be asymmetric: dilute-on-the-sublattice → dominant host, everything else
→ alloy host, with no upper band.

The threshold is therefore left where it is, and the sublattice share is
recorded instead. `df_compositions.parquet` carries `axis_x_minor`,
`axis_minor_el`, `axis_major_el` and `axis_is_dilute`, so stage 3 works from the
site occupancy directly rather than re-deriving it from the formula. Only **229
compositions** sit in the borderline 0.05–0.10 band, and for structure
assignment even those do not matter — Bi0.5Sb1.5Te3 and Sb2Te3 are both
tetradymite.

Same group does not guarantee the same site: O and Se are both group 16, but in
BiCuSeO oxygen sits in the Bi2O2 layer and never substitutes for Se. Axes
involving oxygen are reported with a `CHECK` marker instead of an assertion.

One consequence for phases: on a solid-solution axis the transition temperature
itself shifts with composition, so a single value cannot cover the whole host.

Note that not every "dopant candidate" is a dopant. The role vocabulary
separates `substitutional`, `interstitial`, `cage_filler`,
`framework_substitution`, `alloying_component` (an end member that happens to
fall below 5 at.%, such as Se in Bi2Te2.85Se0.15), `non_stoichiometry`,
`secondary_phase_or_contaminant`, `processing_residue` (O, C, N and H in
ball-milled or hot-pressed samples are usually this) and `parse_artifact`.

### Stage 3 — doping levels

`dopant_candidates` and `dopant_fracs` are already computed per composition, and
the roles were decided in stage 1. This stage is mechanical: apply the role to
the parsed fractions and emit a doping level per formula unit, flagging for
review only the compositions whose role is `unknown` or whose arithmetic is
ambiguous.

The distinction matters and is prototype-dependent. The taxonomy records these in
each prototype's `notes` so stage 3 does not have to rediscover them:

| case | prototype | what the "dopant" really is |
|---|---|---|
| Yb, Ba, In in CoSb3 | `skutterudite` | cage filler in the icosahedral void |
| O content in YBa2Cu3O6+δ | `ybco_cuprate` | the doping variable itself |
| cation vacancies in La3−xTe4 | `th3p4` | the carrier-concentration knob |
| x in NaxCoO2 | `naxcoo2_layered` | a compositional variable, not a dopant |
| F-for-O in LaFeAsO1−xFx | `zrcusias_1111` | the doping variable |
| Ga/Al/Cu for Ge in Ba8Ga16Ge30 | `clathrate_i` | framework substitution setting electron count |
| N vacancies in TaN0.89 | `rocksalt_nitride_carbide` | non-stoichiometry, not an impurity |
| K-for-Ba in Ba1−xKxFe2As2 | `thcr2si2_122` | the doping variable |

Genuine substitutional dopants (Na in PbTe, Al in ZnO, Nb in SrTiO3) are the
straightforward case.
