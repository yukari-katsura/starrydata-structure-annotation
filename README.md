# Starrydata structure annotation

Reclassifying the Starrydata thermoelectric dataset by **crystal structure
prototype**, and using that classification to attach Materials Project
structures, identify dopants and compute doping levels.

> **Status: work in progress, and the assignments are model-generated.**
> 100 of 3,648 host systems are annotated, covering 57.8% of samples.
> `experimentally_confirmed` is `false` on every record: the assignments were
> made from composition plus materials knowledge, not read from the papers.
> They are candidate structures, not measured ones. See
> [Limitations](#limitations) before using them.

## What is here

| | |
|---|---|
| `data/annotated/annotations/family_assignments.jsonl` | the annotations — one record per host system |
| `data/annotated/df_annotated_samples.parquet` | 30,068 samples joined to a structure |
| `data/annotated/by_family/` | per-prototype shards |
| `data/annotated/taxonomy/prototypes_seed_v3.json` | 153 structure prototypes |
| `data/annotated/validation/` | held-out curator labels, reference comparison |
| `data/annotated/README.md` | **the detailed methodology** |

## Why

The `MaterialFamily` field in the source dataset mixes three incompatible axes —
chemical class (`Oxide`, `Telluride`), structure prototype (`Half-Heusler`,
`Skutterudite`) and specific compound (`Bi2Te3`, `PbTe`). One material carries
several unrelated labels at once, and you cannot look up a structure or reason
about a dopant site from the word "Telluride".

Once reclassified on a single axis, the scale of that problem is measurable:
**"Oxide" splits across 23 prototypes**, while `rocksalt` gathers **12 different
labels** that all describe the same structure.

## The annotation unit

Each composition is split at 5 at.%: elements at or above are the *host*,
below are *dopant candidates*.

```
Zn0.98Al0.02O   -> host O-Zn      dopant Al
Yb0.2Co4Sb12    -> host Co-Sb     filler Yb  (not a dopant)
Bi0.5Sb1.5Te3   -> host Bi-Sb-Te  solid solution, no dopant
```

27,456 composition strings collapse to 3,648 host systems, and the split
produces the dopant analysis input at the same time. Coverage is steep: 50 host
systems cover 47% of samples.

## Reproducing

```bash
pip install -r requirements.txt

python scripts/merge_taxonomy_v3.py            # build the taxonomy
python scripts/generate_annotation_data.py     # host systems + chunk files
python scripts/build_structure_reference.py    # index ICSD/MP references
python scripts/check_annotations.py            # validate the ledger
python scripts/check_taxonomy_against_refs.py  # taxonomy vs measured structures
python scripts/build_annotated_samples.py      # join down to samples
```

Everything is deterministic and safe to re-run. `data/processed/` ships the two
Starrydata inputs so the pipeline runs without the parent repository.

## Limitations

Read these before treating the output as reference data.

- **Nothing is verified against a paper.** All assignments rest on composition
  and model knowledge. Against ICSD-backed space groups the taxonomy's
  prototype is *present* among measured structures for 82% of testable host
  systems and is the *best-attested* one for 63%; the 55 disagreements are in
  `data/annotated/validation/taxonomy_vs_references.md`.
- **The taxonomy is LLM-generated.** It merges two independently drafted lists,
  but both came from language models, so their agreement is a weak check rather
  than corroboration.
- **13,495 of 30,068 annotated samples need a composition-level split** — they
  sit under a host flagged `is_mixed`, where one label covers several real
  structures (`O-Ti` spans rutile, anatase, Magnéli, corundum and rocksalt).
  `needs_composition_split` marks every one.
- **4,842 samples carry a minor element with no assigned role.**
- **Reference data has holes.** The 2019 Materials Project snapshot contains no
  R-3m Bi2Se3 entry at all, and `e_above_hull` is unusable for layered
  chalcogenides in it — Sb2Te3 R-3m carries 26 ICSD references at hull 1.02.
  Primaries resting on fewer than 5 ICSD references are flagged `low_evidence`.

## Provenance

- **Source data**: Starrydata, DB snapshot 2026-09-04 (renumbered IDs).
- **Structure references**: TEDesignLab and Materials Project — see
  `data/reference/README.md`.
- **Taxonomy lineage**: merges a survey-derived list with the v0.2 ontology in
  `data/lineage/`, itself drafted with ChatGPT. Every prototype records its
  sources in `merged_from`.

## Pre-publication checklist

Not yet resolved; settle these before making the repository public.

- [ ] **TEDesignLab redistribution.** `data/reference/tedesignlab-complete-data.xlsx`
      is tracked but its licence has not been confirmed. Either verify
      redistribution is permitted, or replace it with a download script and a
      checksum.
- [ ] **Starrydata terms.** Confirm that shipping `data/processed/*.parquet`
      is consistent with how the dataset is released.
- [ ] **Copyright holder** in `LICENSE` and `LICENSE-DATA` — currently
      "Starrydata"; set to the intended holder.
- [ ] **Citation.** Add `CITATION.cff` with authors and a DOI.
- [ ] Decide whether partial annotation (57.8%) is the right point to publish,
      or whether to reach a coverage threshold first.

## Licence

Code MIT (`LICENSE`); annotation data CC BY 4.0 (`LICENSE-DATA`). Third-party
data keeps its own terms.
