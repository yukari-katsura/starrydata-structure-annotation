# Prototypes proposed during annotation

75 proposals, pending review. Each was **already used** -- the process requires proposing before use -- so the question is whether it belongs in the seed taxonomy as written, should be merged into an existing prototype, or should be replaced.

Fill in the `decision` in each block and run `python scripts/apply_proposal_review.py`. Blocks left blank are skipped, so you can review a few at a time.

`accept` folds it into prototypes_seed_v3.json. `merge` rewrites every assignment using it to point at `into` instead. `reject` does the same but flags those assignments for re-annotation.

---

## `yb3rh4sn13_remeika` — Yb3Rh4Sn13 (Remeika 3-4-13 stannide)

**Pm-3n (223)** · cage compound · proposed in chunk 9

Primary for **5 host(s)**, 64 samples

- `La-Rh-Sn` (16 samples, high confidence) — Ca0.2La2.8Rh4Sn13 (13); LaRhSn (3)
- `Ce-Ru-Sn` (14 samples, medium confidence) — CeRuSn3 (4); CeRu4Sn6 (3); CeRuSn2.91 (1); CeRuSn3.03 (1); CeRuSn3.09 (1); CeRuS
- `Ca-Rh-Sn` (13 samples, high confidence) — Ca2.8La0.2Rh4Sn13 (13)
- `Ca-La-Rh-Sn` (12 samples, high confidence) — Ca1.5La1.5Rh4Sn13 (12)
- `Ge-Ir-Lu` (9 samples, high confidence) — Lu3Ir4Ge13 (8); (Yb0.3Lu0.7)3Ir4Ge13 (1)

> Proposed while annotating chunk 009: Ca0.2La2.8Rh4Sn13 is 13 of 16 samples of the La-Rh-Sn host and the taxonomy has no 3-4-13 entry. MP gives La3Sn13Rh4 Pm-3n mp-30513 with 5 ICSD references.

> These Remeika phases are rattler systems with low lattice thermal conductivity and a structural/superconducting instability, which is what brings them into a thermoelectric dataset.

> Several members show a superlattice distortion below room temperature; the ambient cubic cell is what this entry names.

**Distinguished from:**
- `skutterudite` — a stannide cage of Sn12 icosahedra around the rare earth, not the CoSb3 pnictide framework with an empty icosahedral void at the body centre
- `cecr2al20_cage` — R3T4Sn13 in a cubic Pm-3n cell, not the Fd-3m CeCr2Al20 1-2-20 cage
- `clathrate_i` — a metallic stannide network rather than a covalent group-14 framework obeying a Zintl electron count

```proposal
id: yb3rh4sn13_remeika
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `zrbesi_ordered_alb2` — ZrBeSi (ordered AlB2 / Ni2In derivative)

**P6_3/mmc (194)** · Zintl polyanion · proposed in chunk 10

Primary for **3 host(s)**, 32 samples

- `Ag-Ca-Ce-Sb` (15 samples, medium confidence) — Ca0.84Ce0.16Ag0.85Sb (2); CaCeAgSb (1); Ca0.84Ce0.16Ag0.86Sb (1); Ca0.84Ce0.16Ag
- `Ag-Ba-Sb` (9 samples, high confidence) — BaAgSb (2); Ba0.99AgSb (1); Ba0.97AgSb (1); Ba0.97Eu0.1AgSb (1); Ba0.98AgSb (1);
- `Ag-Ca-Sb-Zn` (8 samples, medium confidence) — CaZn0.35Ag0.3Sb (1); CaZn0.25Ag0.5Sb (1); CaZn0.4Ag0.18Sb (1); CaZn0.4Ag0.14Sb (

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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `hocoga5_115` — HoCoGa5 (115)

**P4/mmm (123)** · close-packed intermetallic · proposed in chunk 10

Primary for **3 host(s)**, 32 samples

- `Ce-In-Ir-Rh` (14 samples, high confidence) — CeRh0.58Ir0.42In5 (14)
- `Ga-Rh-U` (10 samples, high confidence) — URh0.97Pd0.03Ga5 (8); URhGa5 (2)
- `Ce-Co-In` (8 samples, high confidence) — CeCoIn5 (8)

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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `hexagonal_perovskite_polytype` — Hexagonal perovskite polytype (face-sharing ABO3)

**C2/c (15) for monoclinic 9R BaIrO3; R-3m (166) for ideal 9R; P6_3/mmc (194) for 2H and 4H** · perovskite-derived · proposed in chunk 12

Primary for **3 host(s)**, 28 samples; listed as an alternative on 1 more

- `Ba-Ir-O` (11 samples, medium confidence) — BaIrO3 (9); Ba2IrO4 (1); Ba2Ir3O9 (1)
- `Ba-Mn-O` (10 samples, medium confidence) — Ba0.98La0.02MnO3 (5); Ba3Mn2O8 (2); (La0.67Ba0.33MnO3)0.17(BaMnO3)0.83 (1); (La0
- `Cr-Ge-La` (7 samples, high confidence) — LaCrGe3 (7)

> Proposed while annotating chunk 012: BaIrO3 is 9 of the 11 samples of the Ba-Ir-O host and the taxonomy has no hexagonal-polytype entry, only the cubic perovskite and the post-perovskite.

> The reference disagrees with the structure literature and should not be followed here: Materials Project ranks BaIrO3 Pm-3m mp-5660 PRIMARY on 3 ICSD references at hull 0.141, which is the cubic aristotype. BaIrO3 at ambient conditions is the monoclinically distorted 9R polytype, so the entry names a cell the compound does not adopt -- the same failure mode as the cubic ReO3 aristotype standing in for monoclinic WO3.

> Which polytype forms (2H, 4H, 6H, 9R) depends on the B cation and on synthesis pressure, so stage 2 must take it from the paper rather than from the formula.

**Distinguished from:**
- `perovskite` — the cubic aristotype is built entirely of corner-sharing octahedra. A large A cation forces hexagonal close packing of the AO3 layers, so some octahedra share faces and condense into dimers or trimers -- BaIrO3 is a 9R stack of face-sharing Ir3O12 trimers and is not a corner-sharing network at all
- `post_perovskite` — edge-sharing layers under pressure, not face-sharing oligomers driven by the tolerance factor
- `ca3co2o6_chain` — the extreme of the same series -- infinite face-sharing chains at A3B2O6 with alternating octahedra and trigonal prisms, rather than finite oligomers at ABO3
- `ruddlesden_popper` — Ba2IrO4 in the same host is the n = 1 Ruddlesden-Popper phase; the A:B ratio is how the host splits

```proposal
id: hexagonal_perovskite_polytype
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `ni3sn_d019` — Ni3Sn (D0_19)

**P6_3/mmc (194)** · close-packed intermetallic · proposed in chunk 8

Primary for **2 host(s)**, 26 samples; listed as an alternative on 1 more

- `Al-Ce` (17 samples, medium confidence) — CeAl3 (9); CeAl2 (5); Ce3Al (1); Ce0.9La0.1Al3 (1); Ce0.99La0.01Al3 (1)
- `Al-Ce-Nd` (9 samples, medium confidence) — (Ce0.9Nd0.1)3Al (1); (Ce0.4Nd0.6)3Al (1); (Ce0.3Nd0.7)3Al (1); (Ce0.2Nd0.8)3Al (

> Proposed while annotating chunk 008: the Al-La host is mostly LaAl2 but also carries (La,Ce)Al3, and the only AB3 entry in the taxonomy is the cubic L1_2 one. MP places LaAl3 at P6_3/mmc mp-959 with 4 ICSD references, which is the Ni3Sn type, not Pm-3m.

> CeAl3, the archetypal heavy-fermion compound, has the same structure, so this entry will be wanted again.

**Distinguished from:**
- `cu3au_l12` — the cubic ordered-fcc AB3 superstructure; D0_19 is the hexagonal ordered-hcp one, and the light rare-earth trialuminides take the hexagonal form
- `laves_phase` — AB3 not AB2 -- the Al-La host holds LaAl2 (C15) and LaAl3 (D0_19) and they are different prototypes
- `cacu5` — AB3 rather than AB5

```proposal
id: ni3sn_d019
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `blue_bronze_a03moo3` — Blue bronze A0.3MoO3

**C2/m (12)** · framework oxide · proposed in chunk 11

Primary for **2 host(s)**, 22 samples

- `Mo-O-Rb` (14 samples, high confidence) — Rb0.3MoO3 (10); Rb1.5Mo8O16 (1); Rb0.3Mo0.999W0.001O3 (1); Rb0.3Mo0.997W0.003O3 
- `K-Mo-O` (8 samples, high confidence) — K0.3MoO3 (3); K0.24Tl0.06MoO3 (2); K0.3Mo0.96W0.04O3 (2); Tl0.06K0.24MoO3 (1)

> Proposed while annotating chunk 011: Rb0.3MoO3 and its W-substituted variants are 13 of the 14 samples of the Mo-O-Rb host. The seed taxonomy files that host under tungsten_bronze, whose entry names Sr0.5Ba0.5Nb2O6 and the cubic AxWO3 bronze as its prototypes; the molybdenum blue bronze is neither of those.

> The charge-density-wave transition at about 180 K is what the transport papers measure, and the measured window of 18-290 K spans it. It is a Peierls transition with a lattice superstructure rather than a change of structure type, so it is not recorded as a phase change.

> Materials Project offers nothing at A0.3MoO3 for this chemistry -- every entry ranked for the host is a molybdate or a computed Rb-Mo-O ordering with a single ICSD reference -- so mp_id is left null rather than guessed.

**Distinguished from:**
- `tungsten_bronze` — the seed entry this refines. The tetragonal tungsten bronze is a three-dimensional P4bm framework of corner-sharing octahedra with the alkali in pentagonal and square tunnels; blue bronze is monoclinic C2/m, built from slabs ten octahedra wide that share edges within the slab and corners between them, with alkali layers in between, and it conducts along one direction only
- `hollandite` — the other compound of this same host, A1.5Mo8O16, which has genuine 2x2 octahedral tunnels and a three-dimensional framework
- `reo3_wo3` — a fully stoichiometric corner-sharing MO3 network with no alkali guest at all
- `vanadium_bronze` — the same bronze principle applied to the V2O5 host lattice, a different framework

```proposal
id: blue_bronze_a03moo3
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `b19prime_martensite` — B19' monoclinic martensite

**P2_1/m (11)** · close-packed intermetallic · proposed in chunk 7

Primary for **1 host(s)**, 21 samples; listed as an alternative on 1 more

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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `zrnial_fe2p` — ZrNiAl (Fe2P-derived equiatomic RTX)

**P-62m (189)** · close-packed intermetallic · proposed in chunk 9

Primary for **2 host(s)**, 20 samples; listed as an alternative on 3 more

- `Ce-Rh-Sn` (12 samples, high confidence) — CeRhSn (5); CeRh0.95Ni0.05Sn (1); CeRh0.9Ni0.1Sn (1); CeRh0.95Co0.05Sn (1); CeRh
- `Al-Co-U` (8 samples, high confidence) — UCoAl (8)

> Proposed while annotating chunk 009: LaRhSn is 3 of 16 samples of the La-Rh-Sn host, alongside the 3-4-13 Remeika phase, and the taxonomy has no Fe2P/ZrNiAl entry.

> The Ce-Cu-In host in the same chunk shows the same structure type at CeInCu P-62m mp-20665 with 4 ICSD references, so the entry is wanted twice already.

> CeRhSn, the valence-fluctuating compound named in the papers of this host, is the same type.

**Distinguished from:**
- `half_heusler` — the other common equiatomic RTX structure: half-Heusler is the cubic F-43m MgAgAs ordering, while ZrNiAl is the hexagonal ordered Fe2P type
- `crb_feb_chain` — a three-dimensional hexagonal network, not the orthorhombic CrB chain structure that other equiatomic compounds adopt
- `mgagsb_alpha` — a rare-earth transition-metal main-group intermetallic, not the half-Heusler-derived alpha-MgAgSb ordering

```proposal
id: zrnial_fe2p
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `prni2al3_ordered_cacu5` — PrNi2Al3 (ordered CaCu5 derivative)

**P6/mmm (191)** · close-packed intermetallic · proposed in chunk 8

Primary for **1 host(s)**, 19 samples; listed as an alternative on 1 more

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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `bacu2s2_layered` — BaCu2S2-type ACu2X2

**Pnma (62)** · Zintl polyanion · proposed in chunk 7

Primary for **2 host(s)**, 18 samples; listed as an alternative on 2 more

- `Ba-Cu-Se` (9 samples, medium confidence) — Ba1Cu2Se3 (1); Ba0.99Na0.01Cu2Se2 (1); Ba0.985Na0.015Cu2Se2 (1); Ba0.975Na0.025C
- `Ba-Sb-Zn` (9 samples, medium confidence) — BaZn2Sb2 (4); Ba(Zn0.998Ag0.002)2Sb2 (1); Ba(Zn0.996Ag0.004)2Sb2 (1); Ba(Zn0.992

> Proposed while annotating chunk 007: the Ba-Cu-Te host holds BaCu2Te2 alongside Ba3Cu14-dTe12 and neither has a taxonomy entry. MP gives Ba(CuTe)2 Pnma (62) mp-30133 (hull 0.014, 1 ICSD ref), which is the alpha-BaCu2S2 type.

> Only one ICSD reference backs the MP entry, so the Pnma assignment is a candidate: the alpha/beta (Pnma / I4/mmm) choice in this family is synthesis-dependent and should be confirmed from the paper in stage 2.

**Distinguished from:**
- `thcr2si2_122` — beta-BaCu2S2 is the I4/mmm ThCr2Si2-type variant of the same formula; the alpha form assigned here is the orthorhombic Pnma one with puckered CuX layers
- `fese_pbo` — anti-PbO CuX layers of edge-sharing tetrahedra exist in both, but here they are separated by a large alkaline-earth cation at ACu2X2 rather than forming a binary
- `ba3cu14te12_polytelluride` — the 1:2:2 line compound, not the Cu-deficient 3-14-12 polytelluride in the same host

```proposal
id: bacu2s2_layered
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `osge2_monoclinic` — OsGe2-type monoclinic MX2 semimetal

**C2/m (12)** · close-packed intermetallic · proposed in chunk 14

Primary for **2 host(s)**, 18 samples

- `Nb-Sb` (10 samples, high confidence) — NbSb2 (8); (Zn0.005Nb0.995)4Sb3 (1); (Zn0.01Nb0.99)4Sb3 (1)
- `Sb-Ta` (8 samples, high confidence) — TaSb2 (8)

> Proposed while annotating chunk 014: the Nb-Sb host is 8 of 10 samples NbSb2, and the seed taxonomy names that host under marcasite. Materials Project gives NbSb2 at C2/m (12) mp-1969 with 5 ICSD references at hull 0.000 and lists no Pnnm polymorph at all, which agrees with the literature on NbSb2 and TaSb2 as OsGe2-type semimetals. The marcasite hypothesis is rejected rather than refined.

> The family is of interest beyond thermoelectrics for its extremely large magnetoresistance, so the group Nb/Ta-Sb/As is likely to recur further down the tail.

> mp_id is recorded as a candidate from the chunk reference line only; stage 2 should confirm it by query rather than trusting this entry.

**Distinguished from:**
- `marcasite` — the taxonomy files NbSb2 under marcasite, but marcasite is orthorhombic Pnnm with a single edge-sharing octahedral chain direction. NbSb2 and TaSb2 are monoclinic C2/m with pairs of edge-sharing MSb6 octahedra and an Sb-Sb bond pattern that marcasite does not have; the two are different structure types at the same MX2 stoichiometry
- `pyrite` — cubic Pa-3 with isolated X2 dumbbells and no octahedral chains
- `ir3ge7` — the other Nb/Ta-pnictide-adjacent cubic framework, at a different stoichiometry
- `fega3` — a tetragonal MX3 framework, not MX2

```proposal
id: osge2_monoclinic
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `banisn3_i4mm` — BaNiSn3 (non-centrosymmetric RTX3)

**I4mm (107)** · close-packed intermetallic · proposed in chunk 9

Primary for **1 host(s)**, 17 samples; listed as an alternative on 2 more

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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `b19_orthorhombic_martensite` — B19 orthorhombic martensite

**Pmma (51)** · close-packed intermetallic · proposed in chunk 11

Primary for **1 host(s)**, 14 samples

- `Cu-Ni-Ti` (14 samples, medium confidence) — Ti50Ni45Cu5 (2); Ti50Ni42.5Cu7.5 (2); Ti50Ni25Cu25 (2); Ti50Ni20Cu30 (2); Ti50Ni

> Proposed while annotating chunk 011: the Cu-Ni-Ti host is Ti50Ni50-xCux with x from 5 to 30 at.%, measured from 12 to 386 K, which spans the martensitic transformation. Chunk 007 proposed b19prime_martensite for binary Ni-Ti and deliberately left B19 out until a paper required it; this host is that paper.

> The Cu content selects the product: below about 7.5 at.% Cu the transformation is B2 to B19-prime, above about 10 at.% it is B2 to B19 and the monoclinic shear does not occur, and in between both appear in sequence. So the low-temperature prototype of this host is composition-dependent and stage 2 must split it on the Cu fraction.

> Materials Project offers only off-stoichiometry Ti-Cu-Ni ternaries for this host -- TiCuNi2 Pmmn, Ti8Cu3Ni, TiCuNi I4mm -- and none of them is the pseudobinary TiNi phase these samples actually are, so mp_id is left null.

**Distinguished from:**
- `b19prime_martensite` — the monoclinic shear of this same orthorhombic cell. Binary TiNi transforms B2 to B19-prime directly, but substituting more than about 10 at.% Cu for Ni stops the shear and leaves the orthorhombic B19 as the final product, so the two are selected by composition within one host
- `b2_cscl` — the cubic austenite parent both martensites shear from, and the phase above the transformation in every one of these samples
- `l10_tetragonal` — a tetragonal ordered-fcc martensite of the CuAu type, not an orthorhombic shear product of an ordered bcc parent

```proposal
id: b19_orthorhombic_martensite
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `thmn12_tetragonal` — ThMn12 (D2_b)

**I4/mmm (139)** · close-packed intermetallic · proposed in chunk 11

Primary for **2 host(s)**, 14 samples; listed as an alternative on 1 more

- `Al-Mn-Y` (7 samples, high confidence) — YMn3Al9 (1); YMn3.5Al7.5 (1); YMn4Al8 (1); YMn5.3Al6.7 (1); YMn6.5Al5.5 (1); YMn
- `Be-Ti` (7 samples, high confidence) — TiBe12 (7)

> Proposed while annotating chunk 011: CeCu4Al8 is 1 of the 13 samples of the Al-Ce-Cu host and is a different compound from the CeCu4Al that makes up the other 12. The taxonomy has no 1-12 entry.

> Materials Project ranks Ce(Al2Cu)4 I4/mmm mp-20003 first for that host at hull 0.000 with 3 ICSD references. Reduced, that formula is CeCu4Al8 -- so the best reference evidence for the host describes the one-sample minority compound and not the majority one.

> The RT4Al8 series is a large family of Kondo lattice and spin-glass intermetallics, so this entry should recur down the tail.

**Distinguished from:**
- `thcr2si2_122` — both are body-centred tetragonal I4/mmm rare-earth intermetallics, but ThMn12 puts twelve framework atoms per rare earth on three distinct sites, rather than the BaAl4-derived RT2X2 layer stack
- `cacu5` — ThMn12 is derived from CaCu5 by replacing every second rare earth with a dumbbell of framework atoms. That is exactly how CeCu4Al and CeCu4Al8 relate inside the Al-Ce-Cu host, which is why the pair has to be told apart
- `cecr2al20_cage` — a cubic Fd-3m 1-2-20 cage, not the tetragonal 1-12 framework
- `laves_phase` — 1:12 rather than the AB2 tetrahedrally close-packed stacking

```proposal
id: thmn12_tetragonal
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `al2fe3si3_tau2` — Al2Fe3Si3 (tau2 phase)

**P-1 (2) in Materials Project, monoclinic P2_1/c (14) in the thermoelectric literature -- unresolved** · close-packed intermetallic · proposed in chunk 11

Primary for **1 host(s)**, 13 samples

- `Al-Fe-Si` (13 samples, medium confidence) — Al25.7Fe37.1Si37.1 (4); Al27.4Fe36.5Si36.1 (1); Al25.5Fe36.5Si38 (1); Al25.3Fe36

> Proposed while annotating chunk 011: 12 of the 13 samples of the Al-Fe-Si host sit within about a percent of Al25.7Fe37.1Si37.1, which normalises to Al2Fe3Si3, and the seed taxonomy files the whole host under quasicrystal_approximant. The aluminium content is far too low for an Al-Fe-Si Mackay approximant, so the seed entry covers at most the one paper that is about one.

> The space group is not settled by the references: Materials Project gives Al2(FeSi)3 P-1 mp-29110 at hull 0.000 with 2 ICSD references, while the thermoelectric papers on the compound describe it as monoclinic. Both settings are recorded here and stage 2 must take one from the paper rather than from the database.

> It is a narrow-gap semiconducting intermetallic whose conduction type is set by the Al:Si ratio, which is the variable the 2018 paper scans -- so the small composition spread across these samples is the experiment, not scatter.

**Distinguished from:**
- `quasicrystal_approximant` — the seed entry for this host. The Mackay-type 1/1 cubic approximant of Al-Fe-Si sits near Al70Fe15Si15 with a cell of well over a hundred atoms; the tau2 phase is at Al26Fe37Si37, a small low-symmetry cell, and is an ordinary intermetallic with no icosahedral local order
- `beta_fesi2` — the other narrow-gap iron silicide thermoelectric, orthorhombic Cmca FeSi2, with no aluminium in the framework
- `b20_fesi` — cubic P2_13 FeSi, a binary with a chiral structure
- `crsi2_c40` — a hexagonal binary disilicide

```proposal
id: al2fe3si3_tau2
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `beta_sn_a5` — beta-Sn (A5, white tin)

**I4_1/amd (141)** · close-packed intermetallic · proposed in chunk 11

Primary for **1 host(s)**, 13 samples

- `Sn` (13 samples, high confidence) — Sn (8); Sb0.0000007Sn (1); Sb0.000007Sn (1); Sb0.0000003Sn (1); Sb0.000002Sn (1)

> Proposed while annotating chunk 011: the whole Sn host is elemental tin and its ppm-level Sb dopings, 13 samples measured from 10 to 434 K, and one of its three papers is explicitly on beta-tin thin films. The taxonomy has diamond_cubic for the grey-tin form and solid_solution_alloy for the close-packed elemental metals, but nothing for A5.

> Materials Project ranks Sn I4_1/amd mp-84 first for this host with 39 ICSD references at hull 0.040, against diamond-cubic Sn Fd-3m mp-117 at hull 0.000 with 5. The hull ordering is the reverse of what is observed at room temperature, which is the usual signature of a ground state that is thermodynamically correct and kinetically inaccessible.

> beta-Sn recurs as the high-pressure phase of Si and Ge, so the entry is wanted beyond this one host.

**Distinguished from:**
- `diamond_cubic` — alpha-Sn, grey tin, is the diamond-cubic form and is the equilibrium phase BELOW 286 K. beta-Sn is the metallic body-centred tetragonal form, and it is what every sample in this host actually is, because the transformation to grey tin is so sluggish that it does not nucleate on the timescale of a transport measurement
- `solid_solution_alloy` — the A1, A2 and A3 close-packed elemental metals; white tin is a distinct six-coordinate tetragonal type and a semimetal rather than a simple metal
- `a7_rhombohedral` — the A7 distortion of As, Sb and Bi, a different elemental type
- `trigonal_te` — the chain structure of elemental Te and Se

```proposal
id: beta_sn_a5
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `ga2te3_defect_zincblende` — Ga2Te3 vacancy-ordered defect zincblende

**Cc (9) when the vacancies order, F-43m (216) when they do not** · tetrahedral diamond-like · proposed in chunk 11

Primary for **1 host(s)**, 13 samples; listed as an alternative on 1 more

- `Ga-Te` (13 samples, medium confidence) — Ga1.9Cu0.05Sb0.1Te2.95 (4); Ga2Te3 (4); Ga20Te80 (1); GaTe (1); Ga2Cu0.05Sb0.05T

> Proposed while annotating chunk 011: 10 of the 13 samples of the Ga-Te host are Ga2Te3 and its Cu- and Sb-substituted variants, and one of the papers is titled for the engineered cation vacancy plane that reduces the lattice thermal conductivity. The taxonomy has sphalerite but nothing for the vacancy-ordered III2VI3 derivative.

> The two references disagree about this compound. Materials Project ranks Ga2Te3 R-3m mp-1070116 PRIMARY at hull 0.332 on a single ICSD reference, while the hull-zero entry for the same formula is Ga2Te3 Cc mp-38970 with no ICSD count shown; TEDesignLab has no Ga2Te3 entry at all and offers Ga2Te5 and GaTe instead. The ICSD-count ranking therefore promotes a high-hull rhombohedral cell over the monoclinic one, and stage 2 should take Cc unless a paper says otherwise.

> GaTe, the other compound of that host, is a monoclinic layered semiconductor and is NOT this type, so the host has to be split.

**Distinguished from:**
- `sphalerite` — the parent structure, with every cation site filled. In Ga2Te3 one third of the cation sites is vacant, and the vacancies order onto planes -- which is what collapses the lattice thermal conductivity and is the whole point of the compound
- `defect_chalcopyrite_ovc` — the ordered-vacancy compounds of the chalcopyrite family, CuIn3Se5 and relatives: quaternary-derived and tetragonal. Ga2Te3 is a binary III2VI3 with a monoclinic vacancy ordering of the cubic parent
- `layered_in2se3` — In2Se3 has the same M2X3 stoichiometry but is built from layers with mixed tetrahedral and octahedral coordination, not a vacancy-ordered zincblende network
- `stannite_kesterite` — cation-ordered diamond-like derivatives with full site occupancy

```proposal
id: ga2te3_defect_zincblende
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `kagome_staircase_m3v2o8` — M3V2O8 kagome staircase

**Cmca / Cmce (64)** · framework oxide · proposed in chunk 12

Primary for **1 host(s)**, 12 samples

- `Co-O-V` (12 samples, high confidence) — Co3V2O8 (11); CoV2O4 (1)

> Proposed while annotating chunk 012: Co3V2O8 is 11 of the 12 samples of the Co-O-V host -- all single crystals, and the second paper is titled for the antiferromagnetic insulator Co3V2O8 -- while the seed taxonomy files the whole host under spinel. Only the remaining CoV2O4 sample is a spinel.

> Materials Project offers no Co3V2O8 entry at all for this host; the closest evidence for the family is Mn3V2O8 Cmce mp-19692 at hull 0.000 in the Mn-O-V host of the same chunk, which is this structure type. mp_id is therefore left null.

> The geometric frustration of the buckled kagome layer is what these crystals are grown to study, so the entry will recur wherever Ni3V2O8 and Co3V2O8 appear.

**Distinguished from:**
- `spinel` — the seed entry for this host, and CoV2O4 in the same host genuinely is one. M3V2O8 has the cation ratio inverted -- three divalent ions per two V5+ -- and the M2+ octahedra form buckled kagome staircase layers linked by isolated V5+O4 tetrahedra, an orthorhombic cell rather than a cubic AB2O4 close-packed network
- `cu2v2o7_pyrovanadate` — isolated VO4 tetrahedra at M:V = 3:2, not corner-shared V2O7 dimers at 1:1
- `v2o5_layered` — a vanadate of a second cation, not a V2O5 sheet
- `vanadium_bronze` — stoichiometric with V5+ only, no intercalated cation and no mixed valence

```proposal
id: kagome_staircase_m3v2o8
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `li2mo3_honeycomb` — Li2MO3 honeycomb-ordered layered oxide

**C2/m (12)** · rocksalt-derived · proposed in chunk 12

Primary for **1 host(s)**, 12 samples

- `Li-O-Ru` (12 samples, medium confidence) — Li2RuO3 (3); Li2Ru0.95Ti0.05O3 (2); Li2Ru0.9Ti0.1O3 (2); Li2Ru0.9Ir0.1O3 (1); Li

> Proposed while annotating chunk 012: the whole Li-O-Ru host is Li2RuO3 with Ti or Ir on the Ru site, and the taxonomy has the O3 parent but nothing for the honeycomb-ordered Li2MO3 family. Materials Project gives Li2RuO3 C2/m mp-4630 at hull 0.000 with 3 ICSD references, and Li2MnO3 C2/m mp-18988 with 5 appears in the Li-Mn-O host of the same chunk, so the family is already wanted twice.

> Li2RuO3 dimerises below about 540 K: the Ru honeycomb forms Ru-Ru singlet pairs and the symmetry drops from C2/m to P2_1/m. That is a distortion of this prototype rather than a change of type, so both ends are recorded here as one entry with two space groups.

> The family is the parent of the Li-rich layered cathodes and of the Kitaev candidate Li2IrO3, so it should recur down the tail.

**Distinguished from:**
- `alpha_nafeo2_layered` — the O3 parent this derives from. Here one third of the transition-metal layer is Li, and the Li and M order into a honeycomb, which triples the in-plane cell and lowers the symmetry from R-3m to C2/m -- so it is a superstructure of alpha-NaFeO2, not the same cell
- `naxcoo2_layered` — octahedral rather than prismatic alkali coordination, and a fixed alkali content rather than a variable x
- `spinel` — LiMn2O4 in the neighbouring Li-Mn-O host is the spinel at a different Li:M ratio; that ratio is how such hosts split
- `delafossite` — no linear O-M-O dumbbells

```proposal
id: li2mo3_honeycomb
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `mnsb2se4_type` — MnSb2Se4-type ternary chalcogenide

**C2/m (12), to be confirmed** · chain / low-dimensional · proposed in chunk 12

Primary for **1 host(s)**, 12 samples

- `Fe-Sb-Se` (12 samples, medium confidence) — FeSb2Se4 (2); FeSb1.85Sn0.15Se4 (1); FeSb1.9Sn0.1Se4 (1); FeSb1.8Sn0.2Se4 (1); F

> Proposed while annotating chunk 012: the whole Fe-Sb-Se host is FeSb2Se4 with Sn or In substitution (12 samples, 11 compositions), and the taxonomy has no MSb2X4 entry.

> The space group comes from the structure literature on the isostructural MnSb2Se4, not from a reference line: the only Materials Project entry offered for this host is FeSbSe P2_1/c mp-1103256, a different stoichiometry, so mp_id is left null and C2/m must be confirmed in stage 2.

> These are ferromagnetic semiconductors rather than conventional thermoelectrics, and the two papers in the host are about placing Sn and In on specific sites of this framework, so the site assignment matters for stage 3.

**Distinguished from:**
- `stibnite` — Sb2Se3 is the binary ribbon structure; here MSe6 octahedral chains are built into the framework and the M:Sb ratio is fixed at 1:2
- `bi_chalcogenide_complex` — a bismuth-free ternary line compound of a divalent transition metal, not one of the large-cell alkali bismuth chalcogenides
- `marcasite` — FeSb2 is the binary marcasite; adding Se changes both the stoichiometry and the connectivity
- `nias` — octahedral M coordination in both, but here the octahedra form chains inside an Sb-Se framework rather than a binary close-packed net

```proposal
id: mnsb2se4_type
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `scrh3si7_type` — ScRh3Si7 (RT3X7)

**R-3c (167), to be confirmed** · close-packed intermetallic · proposed in chunk 12

Primary for **1 host(s)**, 12 samples

- `Rh-Si-Yb` (12 samples, medium confidence) — YbRh3Si7 (7); YbRh2Si2 (3); Yb0.98La0.02Rh2Si2 (1); Yb(Rh0.94Ir0.06)2Si2 (1)

> Proposed while annotating chunk 012: YbRh3Si7 is 7 of the 12 samples of the Rh-Si-Yb host -- the low-carrier-density Kondo lattice of the Phys. Rev. X paper -- and the taxonomy has no RT3X7 entry. The other 5 samples are YbRh2Si2.

> The only Materials Project entry offered for this host is Yb(SiRh)2 I4/mmm mp-10626, which is the 122; nothing is offered at 1-3-7, so mp_id is left null and the space group comes from the structure literature on the ScRh3Si7 type. Confirm it in stage 2.

> The rare earth sits in a large, weakly bonded site, which is why these compounds are studied for low carrier density and heavy-fermion behaviour rather than as conventional thermoelectrics.

**Distinguished from:**
- `thcr2si2_122` — YbRh2Si2 in the same host is the body-centred tetragonal BaAl4 derivative at RT2X2; the 1-3-7 phase is rhombohedral and rare-earth-dilute, and the stoichiometry is how the host splits
- `yb3rh4sn13_remeika` — also a cage-like rare-earth-dilute stannide or silicide, but cubic Pm-3n at R3T4X13
- `cecu6` — an orthorhombic heavy-fermion structure with a very different framework

```proposal
id: scrh3si7_type
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `mo9se11_cluster` — AgxMo9Se11 (Mo9 bioctahedral cluster compound)

**space group not given** · cluster compound · proposed in chunk 12

Primary for **1 host(s)**, 11 samples

- `Ag-Mo-Se` (11 samples, medium confidence) — Ag3.4Mo9Se11 (2); Ag3.8Mo9Se11 (2); Ag3.5Mo9Se11 (1); Ag3.7Mo9Se11 (1); Ag3.9Mo9

> Proposed while annotating chunk 012: the whole Ag-Mo-Se host is AgxMo9Se11 with x scanned from 3.4 to 3.9 (11 samples), which is the composition range of the first paper, and the taxonomy has only the Mo6X8 Chevrel entry.

> typical_space_group is deliberately null: neither reference covers the compound. TEDesignLab offers Ag(MoSe)3 P6_3/m mp-1105028, which is the AgMo3Se3 chain phase, and Materials Project offers Ag(Mo3Se4)2 R-3 mp-1103642, which is the AgMo6Se8 Chevrel phase. Both are different compounds of the same chemistry, so mp_id is left null and the cell must be resolved in stage 2 rather than taken from either.

> The silver content x is the carrier-concentration variable and the Ag ions sit in partially occupied channel sites between the clusters, which is also what makes the lattice thermal conductivity low.

**Distinguished from:**
- `chevrel` — the parent family, built from single Mo6X8 octahedral clusters. Here two Mo6 octahedra share a face to give a bioctahedral Mo9 cluster sheathed by eleven Se, so the cluster nuclearity and the anion count both differ -- and the two occur side by side in the same chemistry, AgMo6Se8 against Ag3.8Mo9Se11
- `tl2mo3se3_chain` — the infinite-chain member of the same reduced-molybdenum-selenide series, where the Mo6 octahedra condense without limit rather than stopping at two
- `ir3ge7` — a binary cluster framework with no intercalated cation

```proposal
id: mo9se11_cluster
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `tl2mo3se3_chain` — Tl2Mo3Se3-type quasi-1D cluster chain

**P6_3/m (176)** · chain / low-dimensional · proposed in chunk 12

Primary for **1 host(s)**, 11 samples

- `As-Cs-Mo` (11 samples, high confidence) — Cs2Mo3As3 (11)

> Proposed while annotating chunk 012: the whole As-Cs-Mo host is Cs2Mo3As3 (11 samples), the quasi-one-dimensional superconductor of its single paper, and the taxonomy has no entry for the condensed-cluster chain family.

> No reference line is offered for this host, so mp_id is left null. The space group is the one reported across the A2Mo3X3 family, and it is corroborated from a neighbouring host in the same chunk: TEDesignLab gives the isostructural AgMo3Se3 at P6_3/m mp-1105028.

> The measured window here is 10-13 K for most curves, so these samples are low-temperature superconductivity measurements rather than thermoelectric characterisation.

**Distinguished from:**
- `chevrel` — the same Mo6 octahedra, but here they condense by sharing opposite faces into infinite [Mo3X3] chains rather than staying as discrete Mo6X8 units, and conduction is one-dimensional along those chains
- `mo9se11_cluster` — the finite two-octahedron member of the same condensation series; this entry is the infinite limit
- `nbse3_chain` — a trigonal-prismatic MX3 chain of a single metal atom per repeat, not a condensed metal-cluster column
- `ta4site4_chain` — a Si-centred Ta4 chain in an orthorhombic cell, not a hexagonal Mo3X3 column

```proposal
id: tl2mo3se3_chain
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `beta_ga2o3` — beta-Ga2O3 (monoclinic gallia)

**C2/m (12)** · framework oxide · proposed in chunk 13

Primary for **1 host(s)**, 11 samples

- `Ga-O` (11 samples, high confidence) — (Ti)0.00182(Ga2O3)0.99818 (1); Ga2O3 (1); (Al0.1Ga0.9)2O3 (1); Sn0.0008Ga2O3 (1)

> Proposed while annotating chunk 013: the Ga-O host is beta-Ga2O3 in 10 of its 11 samples and the taxonomy carries corundum, bixbyite and amorphous_igzo but no entry for monoclinic gallia, which is the ultra-wide-bandgap semiconductor these papers are about.

> TEDesignLab ranks Ga2O3 C2/m (12) mp-886 first with 5 ICSD references at hull 0.000, against R-3c (167) mp-1243 with 4 references at hull 0.029, so the reference agrees that the monoclinic form is the ground state. mp_id is left null here and resolved in stage 2.

> The half-tetrahedral, half-octahedral gallium arrangement is what gives the strongly anisotropic thermal conductivity these measurements report, so it is a structural distinction with a transport consequence rather than a bookkeeping one.

**Distinguished from:**
- `corundum` — alpha-Ga2O3 is the corundum polymorph of the same formula, all-octahedral in R-3c, and is only reachable epitaxially or under pressure. The beta form puts half the gallium on tetrahedral sites in a monoclinic cell and is the thermodynamic ground state, so for gallia the corundum entry is the metastable one -- the reverse of the usual sesquioxide situation
- `bixbyite` — the C-type sesquioxide of In2O3 and Y2O3 is cubic Ia-3 with all-octahedral cations and a different oxygen vacancy pattern
- `reo3_wo3` — a corner-sharing MO3 octahedral network at a different cation-to-oxygen ratio, with a distortion series rather than two distinct polymorphs
- `amorphous_igzo` — the amorphous oxide-semiconductor phase that the same Ga-In-Zn-O chemistries form when deposited cold

```proposal
id: beta_ga2o3
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `co2_dry_ice_pa3` — Dry-ice-type molecular cryocrystal (Pa-3)

**Pa-3 (205)** · molecular / organic · proposed in chunk 13

Primary for **1 host(s)**, 11 samples

- `N-O` (11 samples, high confidence) — N2O (11)

> Proposed while annotating chunk 013: the N-O host is solid N2O measured from 10 to 139 K in two cryocrystal thermal-conductivity papers, and the taxonomy has no entry for a molecular cryocrystal at all.

> N2O is isostructural with CO2 dry ice: cubic Pa-3, four linear molecules per cell, with the N-N-O molecules head-to-tail disordered because the two ends are nearly indistinguishable to the lattice. That residual orientational disorder is itself the phonon scattering mechanism the second paper measures.

> Neither reference covers it. The Materials Project list for the N-O chemistry is all NOx oxides -- NO, N2O3, NO2, NO6, N4O9 -- at large positive hull, and none of them is N2O, so mp_id is null and must be resolved in stage 2 rather than taken from that list.

**Distinguished from:**
- `organic_polymer` — a covalently bonded macromolecule or a semicrystalline polymer film, not discrete small molecules held only by van der Waals forces
- `amorphous` — the cryocrystal is fully crystalline; what is disordered in N2O is the head-to-tail orientation of the molecules on their sites, not the lattice
- `rocksalt` — the molecular centres do sit on an fcc lattice, but the repeat unit is a whole linear molecule with orientational freedom rather than a spherical ion, and the space group drops to Pa-3 as a result
- `graphite_layered` — the other van der Waals molecular solid in the taxonomy, but built from extended sheets rather than isolated molecules

```proposal
id: co2_dry_ice_pa3
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `zrc_al3c2_homologous` — (MC)nAl3C2 layered aluminium carbide homologous series

**P6_3mc (186)** · layered van der Waals · proposed in chunk 13

Primary for **1 host(s)**, 10 samples

- `Al-C-Zr` (10 samples, high confidence) — Zr2Al3C4 (2); Zr2Al3.56Si0.44C5 (2); Zr3Al3C5 (2); (ZrC)3Al3C2 (1); Zr3Al3.56Si0

> Proposed while annotating chunk 013: the Al-C-Zr host is entirely Zr2Al3C4 and Zr3Al3C5, which the curator writes in the revealing form (ZrC)2Al3C2 and (ZrC)3Al3C2, and both of its papers are titled for a new layered ternary carbide. The taxonomy has no entry for the family.

> typical_space_group is given as P6_3mc (186), the setting reported for Zr2Al3C4 and Zr3Al3C5 in the synthesis papers. Materials Project disagrees: it lists Zr2Al3C4 at P-3m1 (164) mp-1215737 but at hull 0.225 with no ICSD backing, so that is a computed cell rather than counter-evidence. The space group should be confirmed in stage 2 and mp_id is left null.

> Related to but distinct from the MAX phases. Materials Project offers Zr2AlC P6_3/mmc mp-3886 for this chemistry, which is the 211 MAX phase -- one Al layer between two ZrC slabs, no Al3C2 block, and a different carbon count. The two must not be merged.

**Distinguished from:**
- `rocksalt_nitride_carbide` — binary ZrC itself, which is the rocksalt slab that this series interleaves; the homologue index n counts how many ZrC layers sit between two Al3C2 blocks, so pure ZrC is the n = infinity limit
- `graphite_layered` — the layers here are covalently bonded carbide slabs stacked with Al-C bonds between them, not van der Waals sheets
- `alb2` — a simple hexagonal AlB2 stack of one metal and one honeycomb layer, with no rocksalt block and no homologous index
- `sic_polytype` — a single tetrahedral network whose polytypes differ only in stacking sequence, not a two-block intergrowth of different chemistries
- `boron_carbide` — an icosahedral cluster framework, not a layered intergrowth

```proposal
id: zrc_al3c2_homologous
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `cr2si2te6_layered` — Cr2Si2Te6-type M2Si2Te6 layered telluride

**R-3 (148)** · layered van der Waals · proposed in chunk 14

Primary for **1 host(s)**, 10 samples

- `Sb-Si-Te` (10 samples, medium confidence) — Sb2Si2Te6 (3); Sb2Si2Te6.93 (3); Sb2Si2Te6.43 (2); Sb2Si2Te7.5 (2)

> Proposed while annotating chunk 014: the whole Sb-Si-Te host is Sb2Si2Te6 and its Te-rich variants, from one paper on cellular nanostructured Sb2Si2Te6 as a high-performance thermoelectric. Neither reference covers the host, so no space group is quoted from evidence here -- R-3 (148) is the setting reported for the Cr2Si2Te6 family and should be confirmed in stage 2.

> In Sb2Si2Te6 the trivalent cation site is only two-thirds occupied relative to Cr2Si2Te6, so vacancy ordering on the M sublattice is part of the structure rather than a defect; the compositions written Sb2Si2Te6.43 and Sb2Si2Te7.5 are excess-Te variants of the same phase and should not be read as a separate prototype.

> mp_id left null.

**Distinguished from:**
- `cdi2_1t` — the parent CdI2 sheet is a single MX2 layer of edge-sharing octahedra; here one third of the octahedral metal sites is occupied by an Si-Si dimer standing perpendicular to the layer, which triples the in-plane cell and lowers the symmetry to R-3
- `tetradymite` — a quintuple-layer Te-M-Te-M-Te block with no second cation and no homonuclear dimer
- `cu2gese3` — also a ternary tetrelide chalcogenide, but a three-dimensional diamond-like network rather than a van der Waals stack
- `mos2_2h` — trigonal-prismatic coordination and a binary sheet

```proposal
id: cr2si2te6_layered
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `ypd2si_ordered_cementite` — YPd2Si (ordered Fe3C cementite) RT2X

**Pnma (62)** · close-packed intermetallic · proposed in chunk 14

Primary for **1 host(s)**, 10 samples

- `Ce-Ga-Pd` (10 samples, low confidence) — CePd2Ga (4); CePdGa (2); CePd0.4Ga3.6 (1); CePd0.8Ga3.2 (1); CePd0.5Ga3.5 (1); C

> Proposed while annotating chunk 014: CePd2Ga is the largest single composition in the Ce-Ga-Pd host and Materials Project gives CeGaPd2 at Pnma (62) mp-639863, hull 0.000, with 3 ICSD references -- the best-attested entry in that host. Filing it under full_heusler on the strength of the AB2C formula would have been wrong.

> Fe3C ordering and Co2Si ordering both give Pnma and both occur in rare-earth intermetallics; they are kept as separate prototypes because the coordination polyhedra differ, but stage 2 should check which one an individual compound actually takes.

> mp_id is a candidate from the chunk reference line, not a confirmed query.

**Distinguished from:**
- `tinisi_co2si` — the equiatomic RTX member of the same orthorhombic Pnma family; here the transition metal count is doubled and the packing is the ordered cementite one, not the ordered Co2Si one
- `full_heusler` — cubic Fm-3m L2_1 at the same RT2X stoichiometry -- the competing ordering, and the one an AB2C formula would suggest by default. CePd2Ga is not cubic
- `laves_phase` — AB2 with no third element
- `thcr2si2_122` — tetragonal RT2X2, twice the X content

```proposal
id: ypd2si_ordered_cementite
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `ybfe2al10_cage` — YbFe2Al10-type RT2Al10 cage intermetallic

**Cmcm (63)** · cage compound · proposed in chunk 14

Primary for **1 host(s)**, 9 samples

- `Al-Ce-Ru` (9 samples, high confidence) — CeRu2Al10 (5); Ce0.95Y0.05Ru2Al10 (1); Ce0.9Y0.1Ru2Al10 (1); Ce0.95La0.05Ru2Al10

> Proposed while annotating chunk 014: the Al-Ce-Ru host is entirely CeRu2Al10 with light Y and La substitution for Ce, and its papers are on the anisotropic transport and the unusual 27 K ordering of CeRu2Al10. The taxonomy has no entry for the 1-2-10 family.

> CeRu2Al10 and CeOs2Al10 are the cases where a Kondo semiconductor orders magnetically at an anomalously high temperature, so this prototype will keep company with the heavy-fermion entries rather than with the cage thermoelectrics.

> mp_id is taken from the chunk reference line -- Ce(Al5Ru)2 Cmcm mp-31364, hull 0.000, 2 ICSD references, which is the same compound written with a different formula normalisation. Confirm in stage 2.

**Distinguished from:**
- `cecr2al20_cage` — the other rare-earth-in-an-aluminium-cage family, but cubic Fd-3m at AB2C20 with a Frank-Kasper CN16 cage; this one is orthorhombic Cmcm at AB2C10 and the cage is a 20-vertex Al polyhedron elongated along the orthorhombic axis, which is what makes the transport strongly anisotropic
- `thcr2si2_122` — also an R-T-Al ternary with a tetragonal body-centred cell, but at RT2X2 with slab stacking rather than a cage framework
- `laves_phase` — AB2 close packing with no third element and no guest site
- `clathrate_i` — a genuine host-guest clathrate with tetrahedral framework bonding; the cage here is metallic and the guest is not rattling in a covalent cage

```proposal
id: ybfe2al10_cage
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `alb12_icosahedral` — alpha-AlB12 icosahedral aluminium boride

**P4_12_12 (92)** · cluster compound · proposed in chunk 14

Primary for **1 host(s)**, 9 samples

- `Al-B` (9 samples, medium confidence) — AlB12 (5); Y0.62Al1.24B14 (1); Y0.62Al1.55B14 (1); Y0.62Al1.86B14 (1); AlB2 (1)

> Proposed while annotating chunk 014: 5 of 9 samples in the Al-B host are AlB12, and the seed hypothesis boron_carbide covers only the B4C rhombohedral type. AlB12 belongs to the same icosahedral-boron structural class but is a different framework, so the hypothesis is refined rather than accepted.

> Materials Project prints only AlB2 P6/mmm mp-944 for this host; neither reference covers AlB12, so the space group here is from the literature on alpha-AlB12 and not from evidence in this dataset. mp_id left null.

> The Al occupancy is variable and the composition is often written AlB12 regardless, so stage 3 should not read an Al deficit as doping.

**Distinguished from:**
- `boron_carbide` — the taxonomy entry the Al-B host was seeded to. B4C is rhombohedral R-3m with B12 icosahedra at the cell corners and a three-atom C-B-C chain along the long diagonal. AlB12 has no inter-icosahedral chain: it is a tetragonal framework of B12 and B19 units with aluminium in framework channels, and the Al site is only partly occupied
- `alb2` — the other Al-B phase entirely -- a simple hexagonal stack of Al layers and flat boron honeycombs, metallic, with no icosahedra at all
- `ub12_boride` — cubic UB12 built from B12 cuboctahedra, not icosahedra, with the metal on an ordered fcc site
- `mgalb14_boride` — the other icosahedral aluminium boride here, orthorhombic Imma with two metal sites and bridging boron between icosahedra

```proposal
id: alb12_icosahedral
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `alpha_ga_a11` — alpha-Ga (A11)

**Cmce (64)** · close-packed intermetallic · proposed in chunk 15

Primary for **1 host(s)**, 9 samples

- `Ga` (9 samples, medium confidence) — Ga (6); Ga0.999In0.001 (1); Ga0.9995In0.0005 (1); Ga0.9999In0.0001 (1)

> Proposed while annotating chunk 015: the Ga host is elemental gallium and the taxonomy has no entry for the A11 structure. solid_solution_alloy is the elemental-metal bucket but is defined as Cu/W/Mg packings, which alpha-Ga is not.

> Gallium melts at 303 K, so in this dataset the crystal structure covers only the very bottom of the measured window; see liquid_metal for the rest.

**Distinguished from:**
- `solid_solution_alloy` — not one of the three simple close-packed elemental metal structures: alpha-Ga is orthorhombic with a covalent Ga-Ga dimer, which is why it melts at 303 K and expands on freezing
- `beta_sn_a5` — the other low-symmetry group-13/14 elemental metal structure, tetragonal I4_1/amd rather than orthorhombic Cmce
- `a7_rhombohedral` — the As/Sb/Bi puckered-layer elemental structure, not the Ga dimer packing

```proposal
id: alpha_ga_a11
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `liquid_metal` — liquid metal / molten alloy

**space group not given** · disordered / non-crystalline · proposed in chunk 15

Primary for **1 host(s)**, 9 samples; listed as an alternative on 1 more

- `Ga-Zn` (9 samples, high confidence) — Ga0.7Zn0.3 (1); Ga0.4Zn0.6 (1); Ga0.9Zn0.1 (1); Ga0.6Zn0.4 (1); Ga0.8Zn0.2 (1); 

> Proposed while annotating chunk 015 for two hosts whose papers are explicitly on melts: Ga (measured 302-1053 K, melting point 303 K) and Ga-Zn (measured 561-1077 K, titled Electronic transport properties of liquid Ga-Zn alloys).

> Like amorphous and metallic_glass this is a bucket rather than a structure prototype: stage 2 has nothing to resolve and should skip it. It is kept separate from amorphous because the physics differs -- these are equilibrium liquids, not quenched glasses, and the relevant reference data is a structure factor rather than a space group.

> Recording it as a phase above the melting point lets an elemental host keep its crystal prototype at the low-temperature end instead of being forced to choose.

**Distinguished from:**
- `amorphous` — a quenched glass held below its glass transition, whereas this is an equilibrium melt above the liquidus and has no solid structure to resolve at all
- `metallic_glass` — same distinction: a glass is a frozen liquid, this is the liquid
- `solid_solution_alloy` — a crystalline substitutional solid solution; here the constituents need not even be miscible as solids, as Ga and Zn are not

```proposal
id: liquid_metal
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `zn5sb4in2_ternary` — Zn5Sb4In2-delta ternary zinc antimonide

**P2_12_12_1 (19)** · close-packed intermetallic · proposed in chunk 15

Primary for **1 host(s)**, 9 samples

- `In-Sb-Zn` (9 samples, medium confidence) — Zn5Sb4In1.85 (4); (ZnSb)60(InSb)40 (1); (ZnSb)50(InSb)50 (1); (ZnSb)80(InSb)20 (

> Proposed while annotating chunk 015: two of the three papers on the In-Sb-Zn host are on Zn5Sb4In2-delta, one of them titled Zn5Sb4In2-delta - a Ternary Derivative of Thermoelectric Zinc Antimonides, and neither zn4sb3 nor znsb_cdsb describes it.

> The delta in Zn5Sb4In2-delta is a vacancy on the In site and is the carrier-concentration knob, not a dopant level.

**Distinguished from:**
- `zn4sb3` — described in the literature as a ternary derivative of the zinc antimonides, but it is an ordered orthorhombic structure with its own In site rather than the rhombohedral R-3c beta-Zn4Sb3 with disordered Zn interstitials
- `znsb_cdsb` — not the binary CdSb-type ZnSb, which coexists with it in this host as a separate phase
- `sphalerite` — InSb is the zincblende binary in the same chemistry and is a distinct second phase, not this ternary

```proposal
id: zn5sb4in2_ternary
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `re6ch15_cluster` — Re6(Se,Te)15 octahedral cluster chalcogenide

**Pbca (61)** · cluster compound · proposed in chunk 15

Primary for **1 host(s)**, 9 samples

- `Re-Se-Te` (9 samples, low confidence) — Re6Se2.4Te12.6 (1); Re6Ga0.5Se2.4Te12.6 (1); Re6Ga0.5Se4.5Te10.5 (1); Re6GaSe4.5

> Proposed while annotating chunk 015: the whole Re-Se-Te host is one paper on Re6GaxSeyTe15-y and no seed prototype covers a Re6 cluster chalcogenide.

> LOW CONFIDENCE ON THE DETAIL. The Re6 octahedral cluster core is well established across this chemistry, and the reference gives Pbca for Re6Te7Se8, but the arrangement of the seven chalcogen atoms beyond the Re6Ch8 core is taken from the general behaviour of the family and not from a structure report. Review this entry against the literature before folding it into v4.

> Ga in Re6GaxSeyTe15-y is most likely a cation between the cluster units rather than a substituent inside them; that too should be confirmed.

**Distinguished from:**
- `chevrel` — both are octahedral metal-cluster chalcogenides, but the Chevrel phase is rhombohedral R-3 with a Mo6X8 core and intercalated cations, whereas this is orthorhombic Pbca with a Re6 core and far more chalcogen per cluster, the excess sitting in bridging units between clusters
- `mo9se11_cluster` — the condensed bi-octahedral Mo9 cluster, not an isolated Re6 octahedron
- `ir3ge7` — a cubic metal-metalloid framework rather than discrete clusters

```proposal
id: re6ch15_cluster
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `d022_al3ti` — Al3Ti (D0_22)

**I4/mmm (139)** · close-packed intermetallic · proposed in chunk 16

Primary for **1 host(s)**, 8 samples; listed as an alternative on 1 more

- `Al-V` (8 samples, medium confidence) — V3Al (1); PrV2Al20 (1); LaV2Al20 (1); Al3V (1); Al3V0.95Ti0.05 (1); Al3V0.9Ti0.1

> Proposed while annotating chunk 016: Al3V and its Ti-substituted variants are 3 of the 8 samples of the Al-V host, and Ni3V is one end of the Ni3V-Ni3Al pseudo-binary in the Al-Ni-V host. The taxonomy has the cubic L1_2 A3B ordering but nothing tetragonal.

> Al3V is a pseudogap intermetallic, which is why it appears in a thermoelectric set at all; one of the Al-V papers is titled for the lattice thermal conductivity of pseudogap intermetallic compounds.

> Ti substitutes for V on the same site in Al3V0.9Ti0.1 because Al3Ti is the type compound, so the whole Al3(V,Ti) join stays in this entry.

**Distinguished from:**
- `cu3au_l12` — the cubic A3B ordering of the fcc lattice. D0_22 is its tetragonal variant, with an antiphase shift every two cells along c, and the two are exactly the pair that Ni3Al and Ni3V separate into in a Ni3V-Ni3Al pseudo-binary
- `l10_tetragonal` — an AB ordering of the fcc lattice, not A3B
- `full_heusler` — an X2YZ ordering of the bcc lattice at a different stoichiometry; Al3V is not a Heusler despite sitting in an Al-V chunk next to Fe2VAl
- `a15_cr3si` — the other A3B intermetallic in this chemistry, cubic Pm-3n with orthogonal B chains, which is what V3Al adopts while Al3V takes D0_22

```proposal
id: d022_al3ti
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `hg_tl_1212_cuprate` — ABa2Ca(n-1)CunO(2n+2+d) single-reservoir cuprate (A = Hg, Tl)

**P4/mmm (123)** · perovskite-derived · proposed in chunk 16

Primary for **1 host(s)**, 8 samples; listed as an alternative on 1 more

- `Ba-Ca-Cu-Hg-O` (8 samples, high confidence) — HgBa2Ca2Cu3O8 (5); Hg0.82Re0.18Ba2Ca2Cu3O8 (3)

> Proposed while annotating chunk 016: the whole Ba-Ca-Cu-Hg-O host is HgBa2Ca2Cu3O8 and 3 of the 8 samples of Ba-Ca-Cu-O-Tl are TlBa2Ca2Cu3O9. The taxonomy carries 123, BSCCO, infinite-layer, chain and ruthenocuprate entries but nothing for the mercury and thallium single-reservoir families, which are the highest-Tc cuprates known.

> Hg and Tl are grouped because the single A-O sheet plays the same structural and doping role in both; if a reviewer prefers them separate, the split is by the A cation and nothing else changes.

> The oxygen excess d in the reservoir layer is the doping variable, exactly as 6+d is for 123, and Re substitution for Hg is used to stabilise the phase rather than to dope it.

**Distinguished from:**
- `tl_2212_cuprate` — the same homologous CuO2 stacking but with a rock-salt DOUBLE A-O layer between the BaO layers, which doubles the c axis and makes the cell body centred. The single-layer members stay primitive P4/mmm
- `ybco_cuprate` — the charge reservoir is a single A-O sheet with partial oxygen occupancy, not a CuO chain, so there is no orthorhombic chain ordering and no Cu in the reservoir
- `bscco_cuprate` — also a double reservoir layer, and additionally incommensurately modulated, which these are not
- `infinite_layer_cuprate` — no charge reservoir block at all

```proposal
id: hg_tl_1212_cuprate
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `tl_2212_cuprate` — Tl2Ba2Ca(n-1)CunO(2n+4) double-reservoir cuprate

**I4/mmm (139)** · perovskite-derived · proposed in chunk 16

Primary for **1 host(s)**, 8 samples

- `Ba-Ca-Cu-O-Tl` (8 samples, high confidence) — TlBa2Ca2Cu3O9 (3); Tl2Ba2Ca2Cu3O10 (3); Tl2Ba2CaCu2O8 (2)

> Proposed while annotating chunk 016: 5 of the 8 samples of the Ba-Ca-Cu-O-Tl host are Tl2Ba2Ca2Cu3O10 and Tl2Ba2CaCu2O8.

> This entry is structurally the tetragonal unmodulated analogue of bscco_cuprate. It is kept separate rather than folded into it because the incommensurate modulation of BSCCO is a defining feature of that entry and is absent here; a reviewer could reasonably merge them, and this note is the record of that choice.

**Distinguished from:**
- `hg_tl_1212_cuprate` — one A-O sheet instead of two: TlBa2Ca2Cu3O9 and Tl2Ba2Ca2Cu3O10 carry the same three CuO2 planes but differ in the reservoir, and they are the pair that has to be separated inside the Ba-Ca-Cu-O-Tl host
- `bscco_cuprate` — the same double rock-salt reservoir aristotype, but the bismuth members are incommensurately modulated and orthorhombically distorted while the thallium members remain tetragonal I4/mmm
- `ybco_cuprate` — a CuO chain reservoir rather than a rock-salt Tl-O double layer

```proposal
id: tl_2212_cuprate
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `ybco124_double_chain` — YBa2Cu4O8 (124) double-chain cuprate

**Ammm (65)** · perovskite-derived · proposed in chunk 16

Primary for **1 host(s)**, 8 samples

- `Ba-Cu-Er-O` (8 samples, high confidence) — ErBa2Cu4O8 (5); ErBa2Cu3O7 (3)

> Proposed while annotating chunk 016: 5 of the 8 samples of the Ba-Cu-Er-O host are ErBa2Cu4O8 and only 3 are the 123 phase, so the host cannot be filed under ybco_cuprate alone.

> Ten hosts in the ledger are already assigned ybco_cuprate, and any of them containing a 124 composition should be re-checked against this entry when it is folded into v4.

> The 247 phase Y2Ba4Cu7O15 is an ordered 123-124 intergrowth and would belong here or in a third entry; no composition in this chunk needs it.

**Distinguished from:**
- `ybco_cuprate` — 123 has a SINGLE CuO chain and a variable oxygen content 6+d that is the doping knob; 124 has a pair of edge-sharing CuO chains, is oxygen stoichiometric and does not lose oxygen on heating, which is why its transport is reproducible where 123 depends on annealing
- `bscco_cuprate` — a rock-salt BiO double layer as reservoir, not CuO chains
- `cuprate_chain` — Sr2CuO3 and SrCuO2 are chain cuprates with no CuO2 planes at all; here the chains are a reservoir beside the planes

```proposal
id: ybco124_double_chain
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `sillenite_bi12mo20` — Sillenite (Bi12MO20)

**I23 (197)** · framework oxide · proposed in chunk 16

Primary for **1 host(s)**, 8 samples

- `Bi-O` (8 samples, medium confidence) — Bi2O3 (3); Bi24CoO37(Bi0.9La0.1)FeO3 (2); Bi24CoO37 (1); Bi12PbO19 (1); Bi25FeO3

> Proposed while annotating chunk 016: 5 of the 8 samples of the Bi-O host are sillenites (Bi24CoO37, Bi25FeO39, Bi12PbO19) and the taxonomy has no entry for them.

> The guest cation M is a stoichiometric constituent of the framework and not a dopant, even though Co, Fe and Pb fall below the 5 at.% split in these formulas and are listed as dopant candidates.

> Bi24CoO37 is the same structure written on a different normalisation (Bi12CoO18.5); sillenite compositions are routinely reported with non-integer oxygen because the framework tolerates vacancies.

**Distinguished from:**
- `bismite_alpha_bi2o3` — both are bismuth oxides and they coexist in the same host. The sillenite is a cubic body-centred framework of distorted BiO5 polyhedra built around an isolated MO4 tetrahedron, and it needs that guest cation; alpha-Bi2O3 is monoclinic with no tetrahedral guest site at all
- `fluorite_oxide` — delta-Bi2O3 above about 1000 K is a defect fluorite, and the sillenite framework is sometimes described as a fluorite derivative, but the sillenite is a distinct room-temperature cubic phase with ordered tetrahedral guests rather than a disordered anion-deficient fluorite
- `perovskite` — BiFeO3 is the perovskite of this chemistry and is often a second phase alongside Bi25FeO39; the formulas differ by an order of magnitude in Bi content

```proposal
id: sillenite_bi12mo20
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `caco2al8_pbam` — CaCo2Al8 / YbCo2Al8 type

**Pbam (55)** · close-packed intermetallic · proposed in chunk 16

Primary for **1 host(s)**, 8 samples

- `Ce-Co-Ga` (8 samples, medium confidence) — CeCo2Ga8 (8)

> Proposed while annotating chunk 016: the whole Ce-Co-Ga host is the single composition CeCo2Ga8 and the taxonomy has 1-2-10 and 1-2-20 cage entries but nothing at 1-2-8.

> The paper of this host is titled for heavy-fermion behaviour in the QUASI-ONE-DIMENSIONAL Kondo lattice CeCo2Ga8, and the Ce chains running along c are the reason; dimensionality is recorded as chain_or_network for that reason rather than 3D.

> Materials Project ranks CeGaCo C2/m higher on ICSD count for this element set, but no composition in the host is the equiatomic compound, so the ranking is about the chemistry and not about these samples.

**Distinguished from:**
- `ybfe2al10_cage` — the 1-2-10 cage compound CeFe2Al10, orthorhombic Cmcm, in which the rare earth sits inside a closed polyhedral cage. The 1-2-8 has the rare earth in open channels of the T-X framework and is the quasi-one-dimensional member of the same chemistry
- `cecr2al20_cage` — the 1-2-20 cage compound, cubic Fd-3m with a far more dilute rare-earth sublattice
- `thcr2si2_122` — a body-centred tetragonal layered intermetallic, not an orthorhombic channel framework

```proposal
id: caco2al8_pbam
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `mo2feb2_u3si2` — Mo2FeB2 (ordered U3Si2)

**P4/mbm (127)** · close-packed intermetallic · proposed in chunk 16

Primary for **1 host(s)**, 8 samples

- `Ce-Ga-Ni` (8 samples, medium confidence) — Ce2Ni2Ga (3); CeNiGa (2); CeNi4Ga (1); Ce(Ni0.865Ga0.135)5 (1); Ce(Ni0.9Ga0.1)5 

> Proposed while annotating chunk 016: Ce2Ni2Ga is 3 of the 8 samples of the Ce-Ga-Ni host, the largest single composition there, and the taxonomy has no 2-2-1 entry.

> The type is common across Ce and U intermetallics studied for heavy-fermion transport, so this entry is likely to be wanted again further down the tail.

> The space group comes from the structure literature on the R2T2X family rather than from a reference line for this compound, and should be confirmed in stage 2.

**Distinguished from:**
- `zrnial_fe2p` — the other common Ce-Ni-Ga stoichiometry, hexagonal P-62m at 1:1:1. The 2-2-1 is tetragonal and built from T2 dimers inside a net of R and X atoms, and both occur in the same host so they must be separated by composition
- `thcr2si2_122` — body-centred tetragonal at RT2X2, a layered BaAl4 derivative; this is a primitive tetragonal 2-2-1 with no layer stacking
- `cacu5` — the CeNi5-based end of the same host, hexagonal P6/mmm and far richer in the transition metal

```proposal
id: mo2feb2_u3si2
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `mps3_thiophosphate` — MPS3 (M2P2S6) layered thiophosphate

**C2/m (12)** · layered van der Waals · proposed in chunk 17

Primary for **1 host(s)**, 8 samples

- `Fe-P-S` (8 samples, high confidence) — FePS3 (8)

> Proposed while annotating chunk 017: the whole Fe-P-S host is FePS3, from one paper on the Mott-insulator metal-insulator transition. The taxonomy has no M2P2X6 entry.

> The antiferromagnetic ordering near 118 K that these 12-289 K measurements cross is magnetic, not structural, so it is not recorded as a phase change.

> This is a heavily studied two-dimensional magnet family, so MnPS3 and NiPS3 hosts are likely further down the tail.

> mp_id is taken from the chunk reference line only; stage 2 should confirm it by query.

**Distinguished from:**
- `cr2si2te6_layered` — the closest relative, and the pair that has to be told apart. Both stand a homonuclear dimer perpendicular to a CdI2-like sheet, but there the dimer is Si-Si and takes one third of the octahedral metal sites, giving R-3; here it is P-P, the metal fills the remaining two thirds in a honeycomb, and the stacking is monoclinic C2/m
- `cdi2_1t` — the undecorated parent sheet, every octahedral site taken by one metal and no dimer at all
- `mos2_2h` — trigonal-prismatic coordination and a binary sheet
- `pyrite` — also built on X2 dimers, but a three-dimensional cubic framework rather than a van der Waals stack

```proposal
id: mps3_thiophosphate
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `gd5si4_type` — R5(Si,Ge)4 slab intermetallic (Gd5Si4 / Gd5Si2Ge2)

**P2_1/a (14) for the monoclinic 5-2-2 composition, Pnma (62) for the Si-rich O(I) and Ge-rich O(II) settings** · close-packed intermetallic · proposed in chunk 17

Primary for **1 host(s)**, 8 samples

- `Gd-Ge-Si` (8 samples, high confidence) — Gd5Si2Ge2 (4); Gd5Si2.2Ge1.8 (1); Gd5Si1.7Ge2.3 (1); Gd5Si2.3Ge1.7 (1); Gd5(Si0.

> Proposed while annotating chunk 017: all 8 samples of the Gd-Ge-Si host are Gd5Si2-xGe2+x or Gd5(Si0.45Ge0.55)4, and the taxonomy has no 5-4 entry. Neither reference covers the host, so the space groups quoted here come from materials knowledge and must be confirmed in stage 2; mp_id is left null rather than guessed.

> The defining feature is slabs of R-T-R blocks joined by T-T dimers. Breaking or re-forming half of those dimers shears the structure between the monoclinic and the two orthorhombic settings without changing the prototype, which is why all three are one entry rather than three. That shear is the martensitic magnetostructural transition behind the giant magnetocaloric effect, and for Gd5Si2Ge2 it sits near room temperature, inside the measured window of these samples.

> The transition temperature moves strongly with the Si:Ge ratio, with pressure and with magnetic field, so no single value covers the whole host; the value recorded in the ledger is the Gd5Si2Ge2 zero-field figure.

**Distinguished from:**
- `laves_phase` — also a binary rare-earth intermetallic, but AB2 and tetrahedrally close-packed, with no covalent T-T dimers and no shear transition
- `mn5si3_d88` — the other rare-earth silicide motif near this stoichiometry, hexagonal P6_3/mcm, built from chains rather than from slabs joined by dimers
- `zintl_5_2_6` — shares the leading 5-2 numbers but is an antimonide Zintl framework of corner-shared AlSb4 tetrahedra, electron-precise and semiconducting
- `crb_feb_chain` — a 1:1 chain silicide, not a 5:4 slab structure

```proposal
id: gd5si4_type
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `lamox_la2mo2o9` — LAMOX (La2Mo2O9) oxide-ion conductor

**P2_13 (198) for the cubic beta phase above about 853 K, P2_1 (4) for the monoclinic alpha phase below it** · framework oxide · proposed in chunk 17

Primary for **1 host(s)**, 8 samples

- `La-Mo-O` (8 samples, medium confidence) — La2Mo2O7 (3); La1.85Sm0.15Mo1.85W0.15O9 (1); La1.80Sm0.20Mo1.80W0.20O9 (1); La2M

> Proposed while annotating chunk 017: five of the eight samples of the La-Mo-O host are La2Mo2O9 and its Sm/W co-substituted variants, from a paper explicitly about the alpha-beta phase transformation. The taxonomy has no LAMOX entry.

> The alpha-to-beta transition near 853 K is a genuine structural change and the measured 14-1273 K window crosses it, so it belongs in phases rather than in a single label. Substituting Sm for La or W for Mo suppresses the monoclinic alpha form and holds the cubic beta phase down to room temperature, which is the point of the co-doping paper, so on the substituted compositions the transition may not be crossed at all.

> The other three samples of that host are La2Mo2O7, a different quasi-one-dimensional bronze-like compound (Materials Project gives Pnnm mp-32061 at 1 ICSD reference); it is left in unresolved_crystalline rather than folded in here.

> mp_id left null: Materials Project offers no La2Mo2O9 entry among the rankings for this host.

**Distinguished from:**
- `fluorite_oxide` — LAMOX is derived from beta-SnWO4, not from fluorite. Its oxygen sublattice is intrinsically deficient and partly disordered, which is where the ionic conductivity comes from, and the cubic form is non-centrosymmetric
- `perovskite` — there is no corner-shared octahedral ABO3 network; Mo occupies a mixture of four-, five- and six-fold oxygen coordinations
- `pyrochlore` — the other framework near A2B2O7, cubic Fd-3m with an ordered anion vacancy; LAMOX carries one more oxygen per formula unit and its vacancies are disordered
- `tungsten_bronze` — a bronze needs a guest cation in tunnels of a stoichiometric MO3 network; here La is a framework constituent

```proposal
id: lamox_la2mo2o9
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `basi2_tetrahedral_zintl` — BaSi2 (orthorhombic Si4-tetrahedra Zintl phase)

**Pnma (62)** · Zintl phase · proposed in chunk 18

Primary for **1 host(s)**, 7 samples

- `Ba-Si` (7 samples, medium confidence) — BaSi2 (3); Ba0.98La0.02Si2 (1); Ba0.96La0.04Si2 (1); Ba0.92La0.08Si2 (1); Ba8Ni2

> Proposed while annotating chunk 018: six of the seven samples of the Ba-Si host are BaSi2 or La-doped BaSi2, and the taxonomy has SrSi2 but no entry for the orthorhombic BaSi2 type, which is the semiconductor these papers measure.

> TEDesignLab supports it directly: BaSi2 Pnma (62) mp-1477 at hull 0.000 on 9 ICSD references is the primary entry for the formula, against the P4_332 SrSi2-type polymorph at mp-7275, hull 0.014, 2 references. mp_id is left null here and resolved in stage 2.

> Each Si4 tetrahedron is a (Si4)4- anion, so the compound is a classic Zintl phase; the 1.3 eV gap and the semiconducting behaviour that makes it a thin-film solar and thermoelectric candidate follow from that electron count.

> La on the Ba site is the standard n-type substitution and is what the second paper of the host varies.

**Distinguished from:**
- `srsi2_chiral` — the same AE2 stoichiometry but a completely different anion topology -- SrSi2 is a chiral cubic three-connected infinite Si net in P4_332, whereas orthorhombic BaSi2 contains discrete Si4 tetrahedra with no Si-Si bonds between them. The cubic P4_332 polymorph of BaSi2 itself exists and belongs to srsi2_chiral, so the two entries meet inside one chemistry and are separated by polymorph, not by formula
- `clathrate_i` — the Ba8Si46 cage framework of the same chemistry, where silicon forms a fully connected four-bonded host lattice enclosing the barium; here barium is a counter-cation beside isolated anionic clusters, not a cage guest
- `caal2si2_zintl` — a layered 1-2-2 Zintl anion, not isolated tetrahedral clusters
- `diamond_cubic` — the Si4 tetrahedron is a molecular fragment of the diamond net, but the compound is a saltlike Zintl phase with a real band gap from charge transfer

```proposal
id: basi2_tetrahedral_zintl
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `formate_mof_perovskite` — Formate framework perovskite (metal-organic ABX3)

**Pnma (62) for the guanidinium members; R-3c (167) and P6_322 (182) for other A cations** · molecular / framework organic · proposed in chunk 18

Primary for **1 host(s)**, 7 samples

- `C-H-N-O` (7 samples, medium confidence) — [C(NH2)3]Cu(HCOO)3 (3); Ni(C3H10N2)2NO2ClO4 (2); C6H7N(CH3COO)0.5 (1); [C(NH2)3]

> Proposed while annotating chunk 018: four of the seven samples of the C-H-N-O host are guanidinium copper and zinc formates, from a paper on anisotropic heat conduction in metal-organic framework perovskites. The taxonomy has organic_polymer and a proposed two-dimensional conductive MOF but no entry for a molecular framework perovskite.

> Materials Project offers nothing usable for this host -- its rankings are small molecular solids of the same four elements such as urea H4CN2O mp-23778 -- so mp_id is null and the cell must come from the paper or from the CSD rather than from MP.

> The guanidinium cation is too large for the cavity to rotate freely, which is why the copper member is Jahn-Teller distorted and strongly anisotropic in its thermal conductivity; the A cation is therefore a structural variable, not a spectator.

> The host also holds polyaniline and a Haldane-chain nickel complex, so this entry covers only part of it and the host has to be split per composition.

**Distinguished from:**
- `perovskite` — topologically the same corner-connected ABX3 net, but the X bridge is a three-atom formate anion rather than a single oxide ion, so the octahedral M-M separation is about 6 A instead of 4 A and the framework is held together by covalent organic linkers plus hydrogen bonds to the A cation. Transport is not the oxide kind: these are thermal-conductivity and phase-transition materials, not electronic conductors
- `conductive_mof_2d` — a two-dimensional pi-conjugated MOF designed for electrical conduction; the formate perovskites are three-dimensional insulators studied for their anisotropic heat conduction and their order-disorder transitions
- `organic_polymer` — a crystalline framework with a defined cell and space group, not a semicrystalline conjugated polymer

```proposal
id: formate_mof_perovskite
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `zintl_2_1_2_a2cdsb2` — A2CdSb2 Zintl phase (2-1-2)

**space group not given** · Zintl phase · proposed in chunk 18

Primary for **1 host(s)**, 7 samples

- `Cd-Eu-Sb-Yb` (7 samples, medium confidence) — Yb0.75Eu0.25Cd2Sb2 (1); Yb0.5Eu0.5Cd2Sb2 (1); Yb1.64Eu0.36CdSb2 (1); Yb0.87Eu1.1

> Proposed while annotating chunk 018: four of the seven samples of the Cd-Eu-Sb-Yb host are (Yb,Eu)2CdSb2, from two papers on the Eu2-xYbxCdSb2 solid solution, and the remaining samples are ACd2Sb2 of the CaAl2Si2 type. The taxonomy carries 1-2-2, 3-1-3, 5-2-6, 9-4-9 and 11-6-12 Zintl entries but not 2-1-2.

> typical_space_group is deliberately null. Neither reference covers this host at all, and the reported symmetry of the A2CdSb2 family should be taken from the papers in stage 2 rather than guessed here; the structural signature that does identify it is the 2:1:2 cation-to-anion ratio.

> The interest in these compounds is an unusually low thermal conductivity near room temperature in a Zintl antimonide, which the Eu/Yb solid solution reduces further by mass and strain contrast on the A site.

**Distinguished from:**
- `caal2si2_zintl` — the 1-2-2 trigonal member of the same chemistry and the phase it coexists with in this host -- ACd2Sb2 has one A cation per two tetrahedral cations and a P-3m1 cell, while A2CdSb2 inverts that ratio to two A per one Cd and adopts a lower-symmetry anion network. The two are distinguished by the A:Cd ratio in the composition string and nothing else
- `zintl_3_1_3` — a different A:M:Pn ratio in the same Zintl series, with its own anion connectivity
- `zintl_5_2_6` — as above -- these ratios are the axis along which the family is organised
- `yb14mnsb11_zintl` — the 14-1-11 Zintl antimonide, a vastly larger cell containing isolated MnSb4 tetrahedra plus Sb3 units and free Sb anions

```proposal
id: zintl_2_1_2_a2cdsb2
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `cr3s4_defect_nias` — Cr3S4-type ordered-defect NiAs derivative

**C2/m (12), also set as I2/m** · close-packed chalcogenide · proposed in chunk 18

Primary for **1 host(s)**, 7 samples

- `Cr-Ni-S` (7 samples, high confidence) — NiCr2S4 (7)

> Proposed while annotating chunk 018: the whole Cr-Ni-S host is NiCr2S4 (7 samples) from a paper titled Ordered-Defect Sulfides as Thermoelectric Materials, and the taxonomy has the NiAs parent and the spinel but no entry for the ordered-vacancy monoclinic derivative.

> TEDesignLab supports the monoclinic cell: Cr2NiS4 C2/m (12) mp-27512, hull 0.056, 1 ICSD reference. That is a weak primary by the chunk convention, so it corroborates rather than settles it; the remaining Materials Project entries for the host are computed Cr-Ni-S orderings in P-1 and P2/m with no ICSD references at all.

> The vacancy ordering is what suppresses the lattice thermal conductivity, so this is the structural feature the thermoelectric claim rests on.

> Cr3S4 itself and the V3S4 analogue belong here, which is why the entry is named for the structure type rather than for NiCr2S4.

**Distinguished from:**
- `nias` — the parent structure, in which every octahedral site between the hexagonal anion layers is filled. Here the cations vacate half the sites in every second metal layer and order those vacancies, which lowers the symmetry to monoclinic and makes the compound a layered semiconductor rather than a metallic binary -- the ordered defects are the whole point of the material
- `spinel` — the other AB2X4 structure this formula can adopt, with tetrahedral A and cubic Fd-3m symmetry. FeCr2S4 is a spinel while NiCr2S4 is a Cr3S4-type monoclinic phase, so the formula alone does not decide it
- `cdi2_1t` — a fully vacant alternate layer giving a van der Waals gap, rather than a half-occupied one that still bonds the blocks together
- `mos2_2h` — trigonal-prismatic coordination and a true van der Waals gap

```proposal
id: cr3s4_defect_nias
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `th7fe3` — Th7Fe3 (hexagonal R7T3)

**P6_3mc (186)** · close-packed intermetallic · proposed in chunk 8

Primary for **0 host(s)**, 0 samples; listed as an alternative on 2 more


> Proposed while annotating chunk 008: (Ce0.9La0.1)7Ni3 sits in the Ce-La-Ni host, one of whose papers is titled for the heavy-fermion compound Ce7Ni3, and the taxonomy has no R7T3 entry.

> No Materials Project entry is offered for the composition in the chunk file, so mp_id is left null rather than guessed.

> The same structure carries La7Ni3 and the rest of the R7T3 rare-earth series, so the entry is likely to be needed again down the tail.

**Distinguished from:**
- `crb_feb_chain` — the equiatomic CeNi in the same host is the CrB-type chain structure; R7T3 is a distinct rare-earth-rich hexagonal phase
- `laves_phase` — R7T3 rather than AB2 -- CeNi2 in the same host is the C15 Laves phase
- `cacu5` — rare-earth-rich rather than transition-metal-rich, and P6_3mc rather than P6/mmm

```proposal
id: th7fe3
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
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
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `zr6coas2_type` — Zr6CoAs2 (filled Fe2P derivative)

**P-62m (189)** · close-packed intermetallic · proposed in chunk 12

Primary for **0 host(s)**, 0 samples; listed as an alternative on 2 more


> Proposed while annotating chunk 012: Zr6CoBi2 is 1 of the 12 samples of the Bi-Co-Zr host, the rest being half-Heusler ZrCoBi. Materials Project gives Zr6CoBi2 P-62m mp-1206046 at hull 0.000, but with no ICSD count shown, so the structure type is inferred from the space group and the R6TX2 stoichiometry and must be confirmed in stage 2.

> One sample only, so this is a placeholder that keeps the minority phase from being labelled half-Heusler, not a load-bearing entry.

**Distinguished from:**
- `half_heusler` — ZrCoBi in the same host is the cubic F-43m MgAgAs ordering at 1:1:1; the 6-1-2 phase is hexagonal and metal-rich, and that stoichiometry is how the host splits
- `zrnial_fe2p` — both derive from Fe2P and share P-62m, but ZrNiAl is the equiatomic RTX ordering while this is the metal-rich R6TX2 variant with additional filled sites
- `mn5si3_d88` — the other metal-rich hexagonal filled type; D8_8 is P6_3/mcm at M5X3, not P-62m at 6-1-2

```proposal
id: zr6coas2_type
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `bedt_ttf_salt` — BEDT-TTF radical-cation salt (organic molecular conductor)

**packing-motif dependent -- P2_1/c (14), Pnma (62) and C2/c (15) all occur** · molecular / organic · proposed in chunk 13

Primary for **0 host(s)**, 0 samples; listed as an alternative on 1 more


> Proposed while annotating chunk 013: two samples of the C-H-S host are C36H32Cl4GaS24 and C36H32AuBr2S24, which are (BEDT-TTF)4 salts with GaCl4 and AuBr2 counter-anions, from a paper on dimerisation in a new one-dimensional conductor. They were otherwise going to be filed as organic_polymer, which they are not -- they are crystalline molecular solids.

> The structure is a layered alternation of conducting BEDT-TTF donor sheets and insulating anion sheets. The packing motif letter -- alpha, beta, kappa, theta -- names the donor arrangement within the sheet and controls whether the salt is a metal, a superconductor or a Mott insulator, so the motif matters more than the space group and should be recorded in stage 2.

> typical_space_group is deliberately left as a list of the common settings rather than one value, because the motif and the anion together set it. No reference line covers these compounds; the Materials Project entries printed for the C-H-S host are unrelated metal thiolate and thiocyanate complexes.

**Distinguished from:**
- `organic_polymer` — a conjugated macromolecule such as polythiophene or PEDOT, semicrystalline at best and with no counter-anion sublattice. A BEDT-TTF salt is a fully crystalline molecular solid whose carrier count is fixed by the anion stoichiometry, not by a chemical doping level
- `graphite_layered` — conduction here is through overlap of sulfur orbitals between discrete donor molecules within a layer, not through an extended covalent sheet
- `co2_dry_ice_pa3` — a van der Waals molecular crystal of neutral molecules with no charge transfer and no conduction
- `chevrel` — the other charge-transfer framework in the taxonomy, but inorganic and built from metal clusters

```proposal
id: bedt_ttf_salt
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `tinisi_co2si` — TiNiSi (ordered Co2Si) equiatomic RTX

**Pnma (62)** · close-packed intermetallic · proposed in chunk 14

Primary for **0 host(s)**, 0 samples; listed as an alternative on 2 more


> Proposed while annotating chunk 014: CePdGa in the Ce-Ga-Pd host and CePtGe in the Ce-Ge-Pt host are equiatomic Pnma RTX compounds, a very common intermetallic type with no taxonomy entry. It is likely to be needed repeatedly down the tail, where equiatomic CeTX and related Kondo-lattice compounds are numerous.

> TiNiSi is the ordered ternary variant of the Co2Si (C23, PbCl2) type. Note that Materials Project prints CeGePt at Pmmn (59) mp-627355, a different Pnma-family setting or a genuinely different ordering; the space group for any individual member should be confirmed rather than assumed.

> mp_id left null.

**Distinguished from:**
- `zrnial_fe2p` — the other equiatomic RTX ordering, hexagonal P-62m and derived from Fe2P; many CeTX compounds exist in one form or the other and only diffraction separates them, so an assignment to either should stay at medium confidence until the paper is read
- `half_heusler` — cubic F-43m MgAgAs ordering at the same 1:1:1 stoichiometry, with the transition metal in a filled tetrahedral site; TiNiSi is its orthorhombic, more strongly bonded relative and the two are not interchangeable
- `crb_feb_chain` — trigonal-prismatic chains in a binary MX; TiNiSi is the ternary ordered Co2Si type and carries three distinct sites
- `ypd2si_ordered_cementite` — the RT2X member of the same Pnma family; the stoichiometry is what separates them

```proposal
id: tinisi_co2si
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `mgalb14_boride` — MgAlB14 / REAlB14 icosahedral boride

**Imma (74)** · cluster compound · proposed in chunk 14

Primary for **0 host(s)**, 0 samples; listed as an alternative on 1 more


> Proposed while annotating chunk 014: three Al-B samples are Y0.62Al1.24B14, Y0.62Al1.55B14 and Y0.62Al1.86B14, from a paper on a rapid synthesis route to complex thermoelectric borides. The formulae carry the partial metal occupancies explicitly, which is characteristic of the MgAlB14 family and is why Y and Al fractions should not be read as doping levels.

> Neither reference covers this compound; the space group is from the literature on MgAlB14 and REAlB14 and mp_id is left null.

**Distinguished from:**
- `alb12_icosahedral` — both are icosahedral aluminium borides, but this one is orthorhombic Imma with B12 icosahedra linked through bridging boron atoms and two distinct, partly occupied metal sites; that second metal site is what admits the rare earth
- `boron_carbide` — rhombohedral B4C with an inter-icosahedral C-B-C chain; here the linkage is a single bridging boron and the metals sit in framework voids
- `ub12_boride` — cuboctahedral B12 rather than icosahedral B12, and full metal occupancy
- `alb2` — no boron clusters at all

```proposal
id: mgalb14_boride
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `a15_cr3si` — Cr3Si (A15)

**Pm-3n (223)** · close-packed intermetallic · proposed in chunk 16

Primary for **0 host(s)**, 0 samples; listed as an alternative on 1 more


> Proposed while annotating chunk 016: V3Al is 1 of the 8 samples of the Al-V host and the taxonomy has no A15 entry, despite A15 being one of the most studied intermetallic families.

> V3Al appears here as the x equals 1 end of the (Fe1-xVx)3Al series studied as a Heusler-type thermoelectric, so the paper context is Heusler while the compound itself is not one. The Materials Project entry for AlV3 is unambiguous at Pm-3n.

**Distinguished from:**
- `d022_al3ti` — the tetragonal A3B ordering of the fcc lattice. A15 is not an fcc superstructure at all: the A atoms form three mutually orthogonal linear chains threading a bcc arrangement of B atoms, which is what gives the family its sharp density-of-states peak
- `cu3au_l12` — cubic A3B as well, but a simple fcc ordering with no A chains
- `full_heusler` — X2YZ on the bcc lattice, a different stoichiometry and a different site pattern

```proposal
id: a15_cr3si
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `mnp_b31` — MnP (B31)

**Pnma (62)** · close-packed intermetallic · proposed in chunk 16

Primary for **0 host(s)**, 0 samples; listed as an alternative on 1 more


> Proposed while annotating chunk 016: FeAs is 1 of the 8 samples of the As-Fe host, the other 7 being marcasite FeAs2, and the taxonomy has NiAs but no MnP distortion.

> The distinction matters for transport: FeAs2 is the narrow-gap semiconductor with the large thermopower that the papers of this host are about, while FeAs is metallic and antiferromagnetic.

**Distinguished from:**
- `nias` — the undistorted parent B8_1 structure. MnP is its orthorhombic distortion, in which the metal atoms pair into zigzag chains and the hexagonal cell is lost; the two are commonly confused because the distortion is continuous
- `marcasite` — an MX2 structure with X-X dimers, not MX. In the As-Fe host FeAs2 is marcasite and FeAs is this type, so the pair has to be kept apart
- `crb_feb_chain` — also orthorhombic with metal chains, but built from trigonal prisms around the metalloid rather than distorted octahedra

```proposal
id: mnp_b31
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `bismite_alpha_bi2o3` — alpha-Bi2O3 (bismite)

**P2_1/c (14)** · framework oxide · proposed in chunk 16

Primary for **0 host(s)**, 0 samples; listed as an alternative on 1 more


> Proposed while annotating chunk 016: Bi2O3 is 3 of the 8 samples of the Bi-O host and the taxonomy has no bismuth oxide entry.

> The beta (P-4b2), gamma (I23, which is a bismuth sillenite) and delta (Fm-3m) forms all exist. Gamma-Bi2O3 is the self-stabilised member of the sillenite family, so the two proposed entries meet in that one phase; that is a property of the chemistry rather than an overlap in the definitions.

> The transition to delta at about 1002 K sits just above the 930 K upper end of the measured range in this host, so no sample here crosses it, but a hotter measurement would.

**Distinguished from:**
- `sillenite_bi12mo20` — the binary oxide itself, monoclinic and with no guest tetrahedron, against the cubic guest-stabilised framework that dominates the rest of the Bi-O host
- `fluorite_oxide` — the SAME compound above about 1002 K: alpha-Bi2O3 converts to the defect-fluorite delta phase, which is the fast oxide-ion conductor. The two are one thermal sequence and not alternatives, so a measurement reaching above 1000 K must record both
- `corundum` — the other common A2O3 structure; Bi2O3 does not adopt it because the Bi 6s lone pair demands a one-sided coordination

```proposal
id: bismite_alpha_bi2o3
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `ymno3_hexagonal` — hexagonal YMnO3 manganite

**P6_3cm (185)** · framework oxide · proposed in chunk 16

Primary for **0 host(s)**, 0 samples


> Proposed while annotating chunk 016: needed as an other_polymorphs entry for the Dy-Mn-O host, where Materials Project ranks the hexagonal form PRIMARY while the samples are the orthorhombic perovskite.

> Dy is the last rare earth that gives the orthorhombic perovskite under ordinary synthesis; the hexagonal DyMnO3 that the reference lists is reached by thin-film growth or soft chemistry, not by the ceramic route these samples use.

> The type will be needed as a primary assignment as soon as a Y-Mn-O, Ho-Mn-O or Lu-Mn-O host appears further down the tail.

**Distinguished from:**
- `perovskite` — the SAME formula and the pair that has to be told apart across the whole RMnO3 series. The perovskite form has corner-sharing MnO6 octahedra; the hexagonal form has corner-sharing MnO5 trigonal BIPYRAMIDS in layers separated by R planes, is ferroelectric, and is not a perovskite at all despite the ABO3 formula. Large R (La to Dy) gives the perovskite, small R (Ho to Lu, Y, Sc) gives this
- `double_perovskite` — a B-site ordered perovskite, so octahedral throughout
- `alpha_nafeo2_layered` — also layered with an ABO3-like formula, but octahedral and rocksalt-derived

```proposal
id: ymno3_hexagonal
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

## `ksbo3_bi3ru3o11` — KSbO3-type Bi3Ru3O11 (edge-shared octahedral dimer framework)

**Pn-3 (201)** · framework oxide · proposed in chunk 18

Primary for **0 host(s)**, 0 samples; listed as an alternative on 1 more


> Proposed while annotating chunk 018: three of the seven samples of the Bi-O-Ru host are Bi3Ru3O11, which sits beside Bi2Ru2O7 pyrochlore in the same host and in the same papers. The taxonomy has the pyrochlore but no KSbO3-type entry, so the host cannot be split without one.

> Neither reference covers the compound. Materials Project ranks Bi2Ru2O7 Fd-3m mp-23445 first on 6 ICSD references, which is the pyrochlore member, and its remaining Bi-Ru-O entries are unrelated stoichiometries; the space group given here is from the structure literature on Bi3M3O11 (M = Ru, Os), not from a reference line, so mp_id is null.

> Bi3Ru3O11 is metallic while Bi2Ru2O7 is a poor metal or semimetal, so the distinction has a direct transport consequence and is not bookkeeping.

> The A3B3O11 formula is what identifies it in a composition list: the same elements at the pyrochlore ratio would read A2B2O7.

**Distinguished from:**
- `pyrochlore` — the closest relative and the other phase of the same Bi-Ru-O chemistry. Pyrochlore A2B2O7 is built from corner-sharing BO6 octahedra on a tetrahedral B network; the KSbO3 type is built from B2O10 pairs of edge-sharing octahedra linked at their corners, which gives a different framework, a different anion count per cation, and a cubic cell of about 9.3 A in Pn-3 rather than Fd-3m
- `perovskite` — no corner-sharing single-octahedron network and no twelve-coordinate A site
- `hollandite` — also a framework of edge-sharing octahedral units, but they form infinite double chains enclosing one-dimensional tunnels rather than isolated dimers

```proposal
id: ksbo3_bi3ru3o11
decision: accept
into:            # for merge/reject: the prototype id to use instead
notes: reviewed in bulk; all are real structure types and 74 of 75 are already in use
```

---

