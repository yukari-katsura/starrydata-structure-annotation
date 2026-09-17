# Prototypes proposed during annotation

27 proposals, pending review. Each was **already used** -- the process requires proposing before use -- so the question is whether it belongs in the seed taxonomy as written, should be merged into an existing prototype, or should be replaced.

Fill in the `decision` in each block and run `python scripts/apply_proposal_review.py`. Blocks left blank are skipped, so you can review a few at a time.

`accept` folds it into prototypes_seed_v3.json. `merge` rewrites every assignment using it to point at `into` instead. `reject` does the same but flags those assignments for re-annotation.

---

## `ta4site4_chain` — Ta4SiTe4 quasi-1D metal-chain telluride

**Pbam (55)** · chain / low-dimensional · proposed in chunk 7

Primary for **2 host(s)**, 40 samples

- `Si-Ta-Te` (22 samples, high confidence) — Ta4SiTe4 (6); Ta4Si0.995P0.005Te4 (2); Ta4Si0.98P0.02Te4 (2); Ta4Si0.99P0.01Te4 
- `Nb-Si-Te` (18 samples, medium confidence) — Nb3SiTe6 (3); Nb4SiTe4 (3); (Nb0.99Ti0.01)4SiTe4 (1); (Nb0.995Ti0.005)4SiTe4 (1)

> Proposed while annotating chunk 007: the Si-Ta-Te host is entirely Ta4SiTe4 and its P/Mo/Ti/Sb-doped variants (22 samples, 14 compositions) and has no taxonomy entry. MP gives Ta4SiTe4 Pbam (55) mp-28509 (hull 0.000, 2 ICSD refs).

> Needle-like van der Waals crystals with a very large low-temperature power factor; the 10-346 K measured window is the regime the family is studied in.

> The isostructural Nb4SiTe4 appears in the same papers, so the entry is not specific to Ta.

**Distinguished from:**
- `nbse3_chain` — also a quasi-1D transition-metal chalcogenide, but built from MX3 trigonal-prismatic chains; here the chain core is a Ta4 metal cluster column centred by Si and sheathed in Te
- `hms_chimney_ladder` — a commensurate needle-like crystal with discrete covalent chains, not an incommensurate two-subsystem composite
- `chevrel` — Mo6X8 cluster units linked in 3D rather than an infinite one-dimensional metal-chain column

```proposal
id: ta4site4_chain
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `pbpdo2_layered` — PbPdO2

**Imma (74)** · framework oxide · proposed in chunk 5

Primary for **1 host(s)**, 31 samples

- `O-Pb-Pd` (31 samples, high confidence) — PbPdO2 (9); PbPd0.9Co0.1O2 (5); PbPd0.94Li0.06O2 (2); PbPd0.96Li0.04O2 (2); PbPd

> Proposed while annotating chunk 005: the whole O-Pb-Pd host (31 samples, 8 papers) is PbPdO2 with Li, Cu or Co on the Pd site, and it matches no existing prototype.

> Materials Project has PdPbO2 Imma mp-22367 with 4 ICSD references; resolve the structure there in stage 2 rather than from memory.

> A narrow-gap d8 oxide with a metal-insulator transition and large thermopower; Li-for-Pd is the hole-doping variable.

**Distinguished from:**
- `delafossite` — PdCoO2 has triangular nets of two-coordinate Pd between CoO2 layers; PbPdO2 has square-planar PdO4 units in an orthorhombic cell with Pb in a lone-pair site
- `tenorite` — CuO is a binary monoclinic square-planar oxide with no second cation
- `post_perovskite` — not an ABO3 stoichiometry and not built from edge-sharing octahedral layers
- `rutile` — square-planar rather than octahedral coordination of the d8 cation

```proposal
id: pbpdo2_layered
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `yb3rh4sn13_remeika` — Yb3Rh4Sn13 (Remeika 3-4-13 stannide)

**Pm-3n (223)** · cage compound · proposed in chunk 9

Primary for **2 host(s)**, 30 samples

- `La-Rh-Sn` (16 samples, high confidence) — Ca0.2La2.8Rh4Sn13 (13); LaRhSn (3)
- `Ce-Ru-Sn` (14 samples, medium confidence) — CeRuSn3 (4); CeRu4Sn6 (3); CeRuSn2.91 (1); CeRuSn3.03 (1); CeRuSn3.09 (1); CeRuS

> Proposed while annotating chunk 009: Ca0.2La2.8Rh4Sn13 is 13 of 16 samples of the La-Rh-Sn host and the taxonomy has no 3-4-13 entry. MP gives La3Sn13Rh4 Pm-3n mp-30513 with 5 ICSD references.

> These Remeika phases are rattler systems with low lattice thermal conductivity and a structural/superconducting instability, which is what brings them into a thermoelectric dataset.

> Several members show a superlattice distortion below room temperature; the ambient cubic cell is what this entry names.

**Distinguished from:**
- `skutterudite` — a stannide cage of Sn12 icosahedra around the rare earth, not the CoSb3 pnictide framework with an empty icosahedral void at the body centre
- `cecr2al20_cage` — R3T4Sn13 in a cubic Pm-3n cell, not the Fd-3m CeCr2Al20 1-2-20 cage
- `clathrate_i` — a metallic stannide network rather than a covalent group-14 framework obeying a Zintl electron count

```proposal
id: yb3rh4sn13_remeika
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `ba3cu14te12_polytelluride` — Ba3Cu14-d Te12 polytelluride

**space group not given** · Zintl polyanion · proposed in chunk 7

Primary for **1 host(s)**, 22 samples

- `Ba-Cu-Te` (22 samples, medium confidence) — Ba3Cu13.25Te12 (2); BaCu2Te2 (2); Ba3Cu13.5Te12 (1); Ba3Cu13.975Te12 (1); Ba3Cu1

> Proposed while annotating chunk 007: the Ba-Cu-Te host has no taxonomy entry at all and 14 of its 20 compositions are Ba3Cu14-dTe12 with d scanned from 0.025 to 0.825 (Ba3Cu13.175Te12 ... Ba3Cu13.975Te12), from the Chem. Mater. 2006 report of the phase.

> typical_space_group is deliberately null: the structure was not resolved here and must not be filled in from memory. Materials Project has no 3-14-12 entry for this system in the 2019 dump; TEDesignLab's nearest entry is Ba6NaCu3Te14 (193), a different phase.

> The Cu deficiency d is the carrier-concentration variable, not an impurity -- stage 3 should treat it as non-stoichiometry.

**Distinguished from:**
- `cu2se_superionic` — the Cu deficiency sits on partially occupied sites of a rigid Ba-Te framework at fixed Ba:Te, not on a fully mobile Cu sublattice of a binary chalcogenide
- `argyrodite` — no Ag/Cu-rich cubic argyrodite framework; the anion count is fixed at 12 per 3 Ba and the structure is a distinct polytelluride
- `bacu2s2_layered` — the Cu-deficient 3-14-12 phase, not the BaCu2X2 line compound found in the same host

```proposal
id: ba3cu14te12_polytelluride
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `b19prime_martensite` — B19' monoclinic martensite

**P2_1/m (11)** · close-packed intermetallic · proposed in chunk 7

Primary for **1 host(s)**, 21 samples

- `Ni-Ti` (21 samples, medium confidence) — Ti50Ni50 (4); Ti49Ni51 (4); Ni50Ti50 (3); Ti49.3Ni50.7 (2); Ti49.6Ni50.4 (2); Ti

> Proposed while annotating chunk 007: the Ni-Ti host is near-equiatomic TiNi shape-memory alloy measured from 11 to 396 K, which spans the martensitic transformation. The taxonomy only has the B2 parent (b2_cscl), so the low-temperature end of every curve had no prototype.

> The reference evidence favours it: MP TiNi P2_1/m mp-1048 carries 21 ICSD references at hull 0.001, more than any other Ti-Ni entry.

> Ms is strongly composition-dependent -- near 330 K for Ti50Ni50 but suppressed below 200 K for Ni-rich Ti48.4Ni51.6 -- so the transition temperature cannot be a single taxonomy default for the host.

> An R-phase (trigonal, P-3) and a B19 orthorhombic intermediate also occur in this family; they are left out until a paper requires them.

**Distinguished from:**
- `b2_cscl` — the cubic austenite this shears from: B2 is the high-temperature parent of the same composition and B19' the low-temperature martensite, so a measurement spanning Ms crosses both
- `l10_tetragonal` — a tetragonal ordered-fcc martensite (CuAu type); B19' is the monoclinic shear product of an ordered bcc B2 parent
- `cual2_c16` — a distinct tetragonal intermetallic, not a displacive transformation product

```proposal
id: b19prime_martensite
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `prni2al3_ordered_cacu5` — PrNi2Al3 (ordered CaCu5 derivative)

**P6/mmm (191)** · close-packed intermetallic · proposed in chunk 8

Primary for **1 host(s)**, 19 samples

- `Al-Ce-Cu-Ni` (19 samples, medium confidence) — Ce(Ni0.7Cu0.3)2Al3 (11); Ce(Ni0.6Cu0.4)2Al3 (4); Ce(Ni0.8Cu0.2)2Al3 (2); Ce(Ni0.

> Proposed while annotating chunk 008: the whole Al-Ce-Cu-Ni host is Ce(Ni1-xCux)2Al3 (19 samples, 5 compositions) and the taxonomy has the CaCu5 parent but not the ordered ternary RT2Al3 derivative the heavy-fermion 2-3 aluminides adopt.

> Materials Project offers only computed CeAl(CuNi)2 orderings in Cmmm and Amm2 with no ICSD backing, so the space group here comes from the structure literature and must be confirmed in stage 2.

> Cu-for-Ni is the Kondo-lattice tuning variable, not a dopant.

**Distinguished from:**
- `cacu5` — the ternary ordered variant of CaCu5: the transition metal and Al order onto the two distinct Cu sites of the AB5 cell, giving RT2Al3 rather than RB5
- `thcr2si2_122` — hexagonal P6/mmm rather than the body-centred tetragonal BaAl4 derivative -- the Cu-rich RCu2Al3 end is reported as the tetragonal type, which is why this family is not single-structured across x
- `laves_phase` — AB5-derived, not the AB2 tetrahedrally close-packed Laves stacking

```proposal
id: prni2al3_ordered_cacu5
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `tisi2_c54` — TiSi2 (C54)

**Fddd (70)** · close-packed intermetallic · proposed in chunk 5

Primary for **1 host(s)**, 18 samples; listed as an alternative on 1 more

- `Al-Ru` (18 samples, high confidence) — RuAl2 (4); Ru0.85Fe0.15Al1.95Si0.05 (1); Ru0.9Fe0.1Al2 (1); Ru0.85Fe0.15Al2 (1);

> Proposed while annotating chunk 005: the Ga-Ru host is roughly half RuGa2 (Ga67Ru33 and its EPMA-averaged neighbours), which Materials Project places at Ga2Ru Fddd mp-1072429 -- the TiSi2 C54 type. The taxonomy has C40 (crsi2_c40) but neither C54 nor C11b.

> Narrow-gap semiconducting intermetallic, studied alongside FeGa3-type RuGa3 in the same papers.

> If accepted, consider adding mosi2_c11b alongside it: Al6Re5Si4 in the Al-Re-Si host is reported as MoSi2-type and currently has no home either.

**Distinguished from:**
- `crsi2_c40` — the hexagonal C40 stacking of the same MX2 layer sequence; C54 is the orthorhombic Fddd variant
- `fega3` — MX2 rather than MX3 -- the Ga-Ru host holds both RuGa2 and RuGa3 and they are different prototypes
- `hms_chimney_ladder` — a simple periodic disilicide-type stacking, not an incommensurate chimney-ladder

```proposal
id: tisi2_c54
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `ni3sn_d019` — Ni3Sn (D0_19)

**P6_3/mmc (194)** · close-packed intermetallic · proposed in chunk 8

Primary for **1 host(s)**, 17 samples; listed as an alternative on 1 more

- `Al-Ce` (17 samples, medium confidence) — CeAl3 (9); CeAl2 (5); Ce3Al (1); Ce0.9La0.1Al3 (1); Ce0.99La0.01Al3 (1)

> Proposed while annotating chunk 008: the Al-La host is mostly LaAl2 but also carries (La,Ce)Al3, and the only AB3 entry in the taxonomy is the cubic L1_2 one. MP places LaAl3 at P6_3/mmc mp-959 with 4 ICSD references, which is the Ni3Sn type, not Pm-3m.

> CeAl3, the archetypal heavy-fermion compound, has the same structure, so this entry will be wanted again.

**Distinguished from:**
- `cu3au_l12` — the cubic ordered-fcc AB3 superstructure; D0_19 is the hexagonal ordered-hcp one, and the light rare-earth trialuminides take the hexagonal form
- `laves_phase` — AB3 not AB2 -- the Al-La host holds LaAl2 (C15) and LaAl3 (D0_19) and they are different prototypes
- `cacu5` — AB3 rather than AB5

```proposal
id: ni3sn_d019
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `banisn3_i4mm` — BaNiSn3 (non-centrosymmetric RTX3)

**I4mm (107)** · close-packed intermetallic · proposed in chunk 9

Primary for **1 host(s)**, 17 samples

- `Ce-Rh-Si` (17 samples, medium confidence) — CeRhSi3 (8); Ce3RhSi3 (5); CeRh1.9Ni0.1Si2 (1); CeRh1.8Ni0.2Si2 (1); CeRh2Si2 (1

> Proposed while annotating chunk 009: CeRhSi3 is 8 of 17 samples of the Ce-Rh-Si host and is not a 122. The taxonomy carries thcr2si2_122 for the centrosymmetric parent but nothing for the non-centrosymmetric RTX3 derivative.

> No reference entry is offered for CeRhSi3 itself -- the chunk file lists the 122 and several other Ce-Rh-Si stoichiometries -- so the space group comes from the structure literature and must be confirmed in stage 2.

> The family recurs: CeIrSi3, CeCoGe3 and CeRhGe3 share it and all appear in the heavy-fermion thermopower literature.

**Distinguished from:**
- `thcr2si2_122` — the centrosymmetric I4/mmm BaAl4 derivative at RT2X2 stoichiometry; BaNiSn3 is the RTX3 ordering of the same BaAl4 parent, in which T and X order along c and inversion symmetry is lost -- which is the defining feature of these compounds
- `alb2` — a tetragonal BaAl4-derived stacking, not the hexagonal honeycomb layer of the AlB2 family
- `laves_phase` — RTX3 rather than the AB2 tetrahedrally close-packed Laves stacking

```proposal
id: banisn3_i4mm
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `thortveitite_re2si2o7` — Thortveitite rare-earth disilicate

**C2/m (12), beta polymorph** · framework oxide · proposed in chunk 9

Primary for **1 host(s)**, 16 samples

- `O-Si-Y` (16 samples, medium confidence) — Y2Si2O7 (11); Y2SiO5 (5)

> Proposed while annotating chunk 009: Y2Si2O7 is 11 of 16 samples of the O-Si-Y host, measured as an environmental barrier coating, and the taxonomy carries no rare-earth disilicate.

> TEDesignLab marks Y2Si2O7 C2/m mp-5652 AMBIGUOUS at 2 ICSD references against P2_1/c mp-7999 with 2. The disilicates have at least five polymorphs whose stability fields lie inside the coating processing range, so the polymorph has to come from the paper rather than from composition.

> The whole RE2Si2O7 series behaves the same way, so this entry should recur down the tail.

**Distinguished from:**
- `x2_re2sio5_monosilicate` — corner-shared Si2O7 dimers with a bridging oxygen; the monosilicate has isolated SiO4 tetrahedra and a free oxygen bound only to rare-earth cations
- `fresnoite` — Ba2TiSi2O8 also contains Si2O7 dimers, but they sit in a polar layered titanosilicate framework rather than the thortveitite arrangement
- `garnet` — a different silicate framework of isolated tetrahedra in a cubic cell

```proposal
id: thortveitite_re2si2o7
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `zrbesi_ordered_alb2` — ZrBeSi (ordered AlB2 / Ni2In derivative)

**P6_3/mmc (194)** · Zintl polyanion · proposed in chunk 10

Primary for **1 host(s)**, 15 samples

- `Ag-Ca-Ce-Sb` (15 samples, medium confidence) — Ca0.84Ce0.16Ag0.85Sb (2); CaCeAgSb (1); Ca0.84Ce0.16Ag0.86Sb (1); Ca0.84Ce0.16Ag

> Proposed while annotating chunk 010: the whole Ag-Ca-Ce-Sb host is Ca1-xCexAg1-ySb (15 samples, 14 compositions) and the taxonomy has the binary AlB2 parent but no ordered ternary ABX derivative.

> The chunk file offers NO reference line at all for this host -- neither TEDesignLab nor Materials Project -- so the space group comes from the structure literature on the isostructural CaAgAs / CaAgP nodal-line semimetals and must be confirmed in stage 2.

> Ag vacancies (y up to about 0.15 in these samples) sit on the honeycomb site and are the carrier-concentration variable, which is what the Chem. Mater. paper on defect chemistry of this system is about.

**Distinguished from:**
- `alb2` — the ternary ordered derivative of AlB2: the honeycomb layer carries two alternating species (Ag and Sb) so the cell doubles along c and the formula is ABX rather than AB2
- `caal2si2_zintl` — planar honeycomb nets with the large cation between them, not the CaAl2Si2 slab of edge-sharing tetrahedra -- both are ABX-type Zintl phases and they are the usual pair to separate
- `crb_feb_chain` — hexagonal layered, not the orthorhombic CrB zigzag chain that other equiatomic ABX compounds adopt
- `half_heusler` — hexagonal ordered AlB2 rather than the cubic MgAgAs ordering of the same 1:1:1 stoichiometry

```proposal
id: zrbesi_ordered_alb2
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `sr4fe6o13_intergrowth` — Sr4Fe6O13 perovskite / iron-oxide intergrowth

**Iba2 (45), incommensurately modulated -- to be confirmed** · perovskite-derived · proposed in chunk 10

Primary for **1 host(s)**, 15 samples

- `Ca-Fe-O-Sr` (15 samples, medium confidence) — Sr1.2Ca2.8Fe6O13 (3); Sr2.4Ca1.6Fe6O13 (2); Sr0.4Ca0.6FeO3 (1); Sr2Ca2Fe6O13 (1)

> Proposed while annotating chunk 010: the Ca-Fe-O-Sr host is almost entirely Sr4-xCaxFe6O13 (12 compositions), and its single paper is titled for the crystal chemistry of the intergrowth. The taxonomy has brownmillerite, perovskite and Ruddlesden-Popper but nothing at A4Fe6O13.

> Every Materials Project entry offered for this chemistry is a computed P1 / Pm / Cmmm ordering with no ICSD reference, so mp_id is left null rather than guessed.

> The FeO2+x sheet is incommensurately modulated against the perovskite blocks, so a single space group is an approximation; stage 2 should expect a superspace description.

**Distinguished from:**
- `brownmillerite` — Ca2Fe2O5 removes one oxygen row from every perovskite layer of a single structure type, giving alternating octahedra and tetrahedra; the 4-6-13 phase intergrows perovskite blocks with a chemically distinct five-coordinate FeO2+x sheet
- `ruddlesden_popper` — the block between the perovskite slabs is an iron-oxide sheet, not a rock-salt AO layer, and the cell is orthorhombic rather than body-centred tetragonal
- `perovskite` — a two-component intergrowth, not a single corner-sharing octahedral network -- the A:B ratio is 4:6, not 1:1

```proposal
id: sr4fe6o13_intergrowth
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `pbfcl_matlockite` — PbFCl (matlockite) tetragonal MXY

**P4/nmm (129)** · layered van der Waals · proposed in chunk 10

Primary for **1 host(s)**, 14 samples

- `As-Se-U` (14 samples, high confidence) — UAsSe (2); UAs0.979Se1.021 (2); UAs0.926Se1.074 (2); UAs0.982Se1.018 (2); UAs0.9

> Proposed while annotating chunk 010: the whole As-Se-U host is UAs1-xSe1+x (14 samples), which MP gives as UAsSe P4/nmm mp-22595 at hull 0.000 with 4 ICSD references. The taxonomy has the filled ZrCuSiAs derivative but not the parent PbFCl type.

> The As:Se ratio is scanned from 0.926 to 1.021 across the samples, so the anion off-stoichiometry is the carrier-concentration variable rather than an impurity; both elements are host elements, so nothing appears in dopant_roles.

> The same type carries the UXY uranium pnictide-chalcogenide series (UAsS, UPSe, USbTe), all Kondo ferromagnets that appear in the low-temperature thermopower literature.

**Distinguished from:**
- `zrcusias_1111` — ZrCuSiAs is the FILLED PbFCl type -- a fourth site inserted into the layer stack gives ABXO with two chemically distinct anion layers. UAsSe has only three sites, the pnictogen square net taking the halide position of PbFCl
- `fese_pbo` — anti-PbO is a binary two-site MX layer; PbFCl stacks two different anion sheets around the cation layer
- `bis2_layered` — the BiS2 family is a 1111-derived oxychalcogenide with a separate REO block, not a three-element MXY stack

```proposal
id: pbfcl_matlockite
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `hocoga5_115` — HoCoGa5 (115)

**P4/mmm (123)** · close-packed intermetallic · proposed in chunk 10

Primary for **1 host(s)**, 14 samples

- `Ce-In-Ir-Rh` (14 samples, high confidence) — CeRh0.58Ir0.42In5 (14)

> Proposed while annotating chunk 010: the whole Ce-In-Ir-Rh host is the single composition CeRh0.58Ir0.42In5 (14 samples), and the taxonomy has no 115 entry despite this being one of the most-studied heavy-fermion families.

> No reference line at all is offered for this host, so mp_id is left null and the space group comes from the structure literature.

> Rh and Ir sit on the same transition-metal site and are isoelectronic; the paper scans that ratio to tune between conventional and unconventional quantum criticality, so it is a tuning axis rather than doping. The automatic solid-solution detector did not flag it because both are minority constituents of the formula.

**Distinguished from:**
- `thcr2si2_122` — both are tetragonal RTX intermetallics, but 115 is a primitive P4/mmm stack alternating one RIn3 layer with one TIn2 layer, not the body-centred BaAl4 derivative at RT2X2
- `cu3au_l12` — the RIn3 block on its own is the cubic L1_2 structure; the 115 intergrows it with a transition-metal layer, which is what makes the family quasi-two-dimensional
- `banisn3_i4mm` — a different BaAl4-derived RTX3 ordering, centrosymmetric P4/mmm here against non-centrosymmetric I4mm there
- `cecu6` — an orthorhombic heavy-fermion structure with no layered RIn3 block

```proposal
id: hocoga5_115
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `bii3_layered_trihalide` — BiI3 / CrCl3-type layered trihalide

**C2/m (12) at room temperature, R-3 (148) below about 150 K** · layered van der Waals · proposed in chunk 10

Primary for **1 host(s)**, 14 samples

- `Cl-Ru` (14 samples, medium confidence) — RuCl3 (14)

> Proposed while annotating chunk 010: the whole Cl-Ru host is alpha-RuCl3 (14 samples, 12 of them single crystals), the Kitaev quantum magnet, and the taxonomy has no layered trihalide entry.

> The reference disagrees with the structure literature: MP gives RuCl3 P6_3/mcm mp-22850 with 5 ICSD references, which is the idealised high-symmetry cell. alpha-RuCl3 is monoclinic C2/m at room temperature and converts to rhombohedral R-3 near 150 K, so the mp_id points at an aristotype rather than at either observed phase.

> The layer stacking is what the magnetism is sensitive to, so stage 2 should resolve the polytype rather than take a single entry.

**Distinguished from:**
- `cdi2_1t` — the same sheet of edge-sharing octahedra, but one third of the metal sites is vacant and the vacancies order into a honeycomb, giving MX3 rather than MX2
- `mos2_2h` — octahedral rather than trigonal-prismatic metal coordination, and a vacancy-ordered honeycomb metal net
- `stibnite` — a three-dimensional ribbon structure, not a stack of neutral van der Waals sheets
- `graphite_layered` — the honeycomb here is a metal net inside a halide sandwich, not a single atomic layer

```proposal
id: bii3_layered_trihalide
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `hexaferrite` — Hexagonal ferrite (magnetoplumbite block family)

**P6_3/mmc (194) for M-type, R-3m (166) for Y-type** · framework oxide · proposed in chunk 5

Primary for **0 host(s)**, 0 samples; listed as an alternative on 1 more


> Proposed while annotating chunk 005: Ba2Co2Fe12-2x(Ti,Mn)xO22 in the Ba-Co-Fe-O host is a Y-type hexaferrite and has no taxonomy entry; the rest of that host is BCFZY perovskite.

> BaFe12O19 also appears as a deliberate nanoinclusion additive in the Ce-Co-Fe-Sb skutterudite host, where it is a second phase rather than the host structure.

> Me is the divalent transition metal (Co, Zn, Ni, Mg); Ti/Mn substitution on the Fe sublattice is the usual carrier and anisotropy control.

**Distinguished from:**
- `spinel` — built from spinel S blocks but interleaved with R (or T) blocks containing the large Ba/Sr cation in a close-packed oxygen layer -- the cell is hexagonal and far longer than Fd-3m spinel
- `perovskite` — no corner-sharing BO6 network; the Ba-Co-Fe-O host holds both a cubic perovskite and a Y-type hexaferrite
- `magneli_phase` — block stacking of two structure types, not crystallographic shear of one

```proposal
id: hexaferrite
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `cu2v2o7_pyrovanadate` — M2V2O7 pyrovanadate (thortveitite-derived)

**C2/c (15) ziesite; Fdd2 (43) blossite** · framework oxide · proposed in chunk 7

Primary for **0 host(s)**, 0 samples; listed as an alternative on 1 more


> Proposed while annotating chunk 007: the Cu-O-V host is roughly two thirds beta'-Cu2.2V4O11 bronze but also holds Cu2V2O7 and the Zn-substituted (Zn,Cu)2V2O7 series (4 compositions), which the bronze entry explicitly does not cover. MP gives V2Cu2O7 C2/c mp-607934 (hull 0.002, 3 ICSD refs).

> Zn2V2O7 and Cu2V2O7 are isostructural at room temperature, so the Zn0.25Cu1.75V2O7 -> Zn0.5Cu1.5V2O7 series stays in one prototype.

> Cu2V2O7 has a blossite (Fdd2) / ziesite (C2/c) transition near 985 K, above the measured window for this host.

**Distinguished from:**
- `vanadium_bronze` — a stoichiometric divanadate built from corner-sharing V2O7 groups with V5+ only -- not a mixed-valence AxV2O5 / AxV4O11 bronze with an intercalated cation
- `v2o5_layered` — discrete V2O7 dimers bridged by the M cation, not V2O5 sheets
- `spinel` — M:V = 1:1 with V in tetrahedral V2O7 units, not an AB2O4 close-packed oxide

```proposal
id: cu2v2o7_pyrovanadate
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `metavanadate_chain` — AVO3 metavanadate chain

**C2/c (15)** · chain / low-dimensional · proposed in chunk 7

Primary for **0 host(s)**, 0 samples; listed as an alternative on 1 more


> Proposed while annotating chunk 007: the Li-O-V host holds LiV2O4 (spinel, 10 samples) and LiVO3 plus Cr-doped and (K,Li)VO3 variants (5 compositions), and the taxonomy's vanadium_bronze entry covers neither of the latter -- it is defined as AxV2O5/V4O11 with an intercalated cation.

> MP gives LiVO3 C2/c mp-19440 (hull 0.000, 2 ICSD refs) and NaVO3 C2/c mp-19083 (5 ICSD refs).

> The ferroelectric KVO3/CsVO3 metavanadates studied in the same papers belong here too, so this entry is likely to be needed again further down the tail.

**Distinguished from:**
- `vanadium_bronze` — a stoichiometric V5+ chain compound with the alkali as a charge-balancing cation, not a mixed-valence AxV2O5 bronze where x is the carrier-concentration variable
- `perovskite` — AVO3 here is a chain metavanadate with an alkali A cation and low-coordinate V, not an ABO3 corner-sharing octahedral network
- `spinel` — LiV2O4 in the same host is the heavy-fermion spinel; LiVO3 is this chain phase -- split by the Li:V ratio

```proposal
id: metavanadate_chain
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `bacu2s2_layered` — BaCu2S2-type ACu2X2

**Pnma (62)** · Zintl polyanion · proposed in chunk 7

Primary for **0 host(s)**, 0 samples; listed as an alternative on 2 more


> Proposed while annotating chunk 007: the Ba-Cu-Te host holds BaCu2Te2 alongside Ba3Cu14-dTe12 and neither has a taxonomy entry. MP gives Ba(CuTe)2 Pnma (62) mp-30133 (hull 0.014, 1 ICSD ref), which is the alpha-BaCu2S2 type.

> Only one ICSD reference backs the MP entry, so the Pnma assignment is a candidate: the alpha/beta (Pnma / I4/mmm) choice in this family is synthesis-dependent and should be confirmed from the paper in stage 2.

**Distinguished from:**
- `thcr2si2_122` — beta-BaCu2S2 is the I4/mmm ThCr2Si2-type variant of the same formula; the alpha form assigned here is the orthorhombic Pnma one with puckered CuX layers
- `fese_pbo` — anti-PbO CuX layers of edge-sharing tetrahedra exist in both, but here they are separated by a large alkaline-earth cation at ACu2X2 rather than forming a binary
- `ba3cu14te12_polytelluride` — the 1:2:2 line compound, not the Cu-deficient 3-14-12 polytelluride in the same host

```proposal
id: bacu2s2_layered
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `th7fe3` — Th7Fe3 (hexagonal R7T3)

**P6_3mc (186)** · close-packed intermetallic · proposed in chunk 8

Primary for **0 host(s)**, 0 samples; listed as an alternative on 1 more


> Proposed while annotating chunk 008: (Ce0.9La0.1)7Ni3 sits in the Ce-La-Ni host, one of whose papers is titled for the heavy-fermion compound Ce7Ni3, and the taxonomy has no R7T3 entry.

> No Materials Project entry is offered for the composition in the chunk file, so mp_id is left null rather than guessed.

> The same structure carries La7Ni3 and the rest of the R7T3 rare-earth series, so the entry is likely to be needed again down the tail.

**Distinguished from:**
- `crb_feb_chain` — the equiatomic CeNi in the same host is the CrB-type chain structure; R7T3 is a distinct rare-earth-rich hexagonal phase
- `laves_phase` — R7T3 rather than AB2 -- CeNi2 in the same host is the C15 Laves phase
- `cacu5` — rare-earth-rich rather than transition-metal-rich, and P6_3mc rather than P6/mmm

```proposal
id: th7fe3
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `nb3site6_layered` — Nb3SiTe6 layered ternary telluride

**Pmmn (59), to be confirmed** · layered van der Waals · proposed in chunk 8

Primary for **0 host(s)**, 0 samples; listed as an alternative on 1 more


> Proposed while annotating chunk 008: the Nb-Si-Te host holds both Nb4SiTe4 (covered by ta4site4_chain, proposed in chunk 007) and Nb3SiTe6, which has no entry. Nb3SiTe6 is the few-layer van der Waals semimetal of the Phys. Rev. Materials paper in that host.

> The space group is from the structure literature, not from a reference line -- the chunk file offers only Nb2SiTe4 entries for this chemistry -- so it must be checked in stage 2.

**Distinguished from:**
- `ta4site4_chain` — the other silicide telluride of the same chemistry: M4SiTe4 is a quasi-one-dimensional needle of Si-centred metal-chain columns, while M3SiTe6 is a van der Waals layer
- `mos2_2h` — a ternary slab with Si inside it, not a binary MX2 sandwich
- `misfit_layered_chalcogenide` — a single commensurate ternary layer, not two incommensurate subsystems

```proposal
id: nb3site6_layered
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `defect_chalcopyrite_ovc` — Ordered-vacancy compound (defect chalcopyrite)

**P-42m (111) and related tetragonal variants** · tetrahedral diamond-like · proposed in chunk 8

Primary for **0 host(s)**, 0 samples; listed as an alternative on 3 more


> Proposed while annotating chunk 008: AgIn5Se8 is the single largest composition of the Ag-In-Se host (5 samples) and is not chalcopyrite -- TEDesignLab gives In5AgSe8 at space group 111 while AgInSe2 is I-42d (122).

> These ordered-vacancy compounds are the n-type members of the I-III-VI2 family and the vacancy ordering is what suppresses their lattice thermal conductivity, so separating them matters for stages 2 and 3.

> The references disagree on the symmetry: MP gives In5AgSe8 C2 (5) mp-1224092 at hull 0.003 against TEDesignLab space group 111. Resolve from the paper.

**Distinguished from:**
- `chalcopyrite` — ABX2 with every cation site filled; the OVCs are III-rich derivatives in which an ordered fraction of the A sites is vacant
- `sphalerite` — vacancy and cation ordering lowers the symmetry and multiplies the cell
- `stannite_kesterite` — ordering of two different cations rather than of cations and vacancies

```proposal
id: defect_chalcopyrite_ovc
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `conductive_mof_2d` — 2D conductive coordination framework

**P6/mmm (191), eclipsed stacking** · molecular / organic · proposed in chunk 8

Primary for **0 host(s)**, 0 samples; listed as an alternative on 1 more


> Proposed while annotating chunk 008: one composition of the C-H-N host is the HITP ligand C18H12N6 with Ni -- Ni3(HITP)2, the archetypal electrically conductive 2D MOF -- while the rest of the host is polyaniline. organic_polymer does not describe a coordination framework.

> Only one sample carries it here, so this is a placeholder for a family that recurs in the organic and hybrid thermoelectric literature rather than a load-bearing entry.

**Distinguished from:**
- `organic_polymer` — a crystalline metal-organic framework of pi-d conjugated sheets with a defined unit cell, not a chain polymer such as polyaniline or PEDOT
- `graphite_layered` — the conducting sheet is a metal-ligand network with large hexagonal pores, not a carbon honeycomb

```proposal
id: conductive_mof_2d
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `zrnial_fe2p` — ZrNiAl (Fe2P-derived equiatomic RTX)

**P-62m (189)** · close-packed intermetallic · proposed in chunk 9

Primary for **0 host(s)**, 0 samples; listed as an alternative on 2 more


> Proposed while annotating chunk 009: LaRhSn is 3 of 16 samples of the La-Rh-Sn host, alongside the 3-4-13 Remeika phase, and the taxonomy has no Fe2P/ZrNiAl entry.

> The Ce-Cu-In host in the same chunk shows the same structure type at CeInCu P-62m mp-20665 with 4 ICSD references, so the entry is wanted twice already.

> CeRhSn, the valence-fluctuating compound named in the papers of this host, is the same type.

**Distinguished from:**
- `half_heusler` — the other common equiatomic RTX structure: half-Heusler is the cubic F-43m MgAgAs ordering, while ZrNiAl is the hexagonal ordered Fe2P type
- `crb_feb_chain` — a three-dimensional hexagonal network, not the orthorhombic CrB chain structure that other equiatomic compounds adopt
- `mgagsb_alpha` — a rare-earth transition-metal main-group intermetallic, not the half-Heusler-derived alpha-MgAgSb ordering

```proposal
id: zrnial_fe2p
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `x2_re2sio5_monosilicate` — X2-type rare-earth monosilicate

**C2/c (15), X2 polymorph** · framework oxide · proposed in chunk 9

Primary for **0 host(s)**, 0 samples; listed as an alternative on 1 more


> Proposed while annotating chunk 009: Y2SiO5 is 5 of 16 samples of the O-Si-Y host and is a different structure from the Y2Si2O7 that makes up the rest. MP gives Y2SiO5 C2/c mp-3520 with 4 ICSD references.

> The X1 (P2_1/c) and X2 (C2/c) polymorphs are selected by rare-earth size and processing temperature, and Y sits near that boundary, so the polymorph needs the paper.

> Kept separate from thortveitite_re2si2o7 so disilicate and monosilicate coatings are never averaged together in stage 2.

**Distinguished from:**
- `thortveitite_re2si2o7` — isolated SiO4 tetrahedra plus an oxo-centred OY4 unit, against the corner-shared Si2O7 dimers of the disilicate -- and the Si:RE ratio differs, which is how the O-Si-Y host splits
- `garnet` — monoclinic with two inequivalent rare-earth sites, not the cubic garnet framework

```proposal
id: x2_re2sio5_monosilicate
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `co2al5_d811` — Co2Al5 (D8_11)

**P6_3/mmc (194)** · close-packed intermetallic · proposed in chunk 10

Primary for **0 host(s)**, 0 samples; listed as an alternative on 1 more


> Proposed while annotating chunk 010: 3 of 14 samples of the Al-Co host are Al5Co2 and its Fe-substituted variants, which MP gives as Al5Co2 P6_3/mmc mp-196 at hull 0.000 with 3 ICSD references. The rest of the host is Al13Co4 and decagonal Al-Co-Ni, which quasicrystal_approximant covers.

> Co2Al5 is one of the complex metallic alloys studied for a pseudogap at the Fermi level, so it recurs in the Al-transition-metal thermoelectric literature alongside Al13TM4.

**Distinguished from:**
- `quasicrystal_approximant` — a small commensurate hexagonal cell, not a decagonal quasicrystal or one of its large-cell approximants -- the Al-Co host holds both and they must not be merged
- `nias` — derived from the B8 family by ordered site filling, but at A5B2 rather than AB, so the metal sublattice is only partly occupied
- `b2_cscl` — AlCo is the cubic B2 phase of the same binary and a different prototype
- `laves_phase` — A5B2 rather than the AB2 tetrahedrally close-packed stacking

```proposal
id: co2al5_d811
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

## `ceru4sn6_tetragonal` — CeRu4Sn6

**I-42m (121)** · cage compound · proposed in chunk 10

Primary for **0 host(s)**, 0 samples; listed as an alternative on 1 more


> Proposed while annotating chunk 010: CeRu4Sn6 is 3 of 14 samples of the Ce-Ru-Sn host and has no taxonomy entry. MP gives Ce(Sn3Ru2)2 I-42m mp-20752 at hull 0.000 with 1 ICSD reference.

> It is the anisotropic Kondo insulator of the first paper of that host, with a hybridisation gap that closes strongly anisotropically -- which is why the thermopower is measured along different axes.

> Only one ICSD reference backs the MP entry, so the space group is a candidate and stage 2 should confirm it from the paper.

**Distinguished from:**
- `skutterudite` — RT4X12 with an icosahedral void at the body centre of a cubic Im-3 cell; CeRu4Sn6 is RT4X6 in a body-centred TETRAGONAL cell and the rare earth is a framework constituent, not a filler
- `yb3rh4sn13_remeika` — the other Ce-Ru-Sn phase in the same host: cubic Pm-3n at R3T4Sn13, which is how the host splits
- `filled_skutterudite` — not a filled variant of anything -- the 1-4-6 framework is its own type
- `cecr2al20_cage` — a cubic Fd-3m 1-2-20 cage rather than the tetragonal 1-4-6 network

```proposal
id: ceru4sn6_tetragonal
decision:        # accept | merge | reject
into:            # for merge/reject: the prototype id to use instead
notes:
```

---

