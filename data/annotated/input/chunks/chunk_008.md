# Host systems -- chunk 008 of 73

Ranks 351-400 by sample count. These 50 host systems cover 930 samples (1.79% of the TE set); cumulative through this chunk: 77.51%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Fe-O-Zn
- rank 351 | 20 samples | 8 papers | 14 compositions
- compositions: ZnFe2O4 (5); Zn0.750Fe0.171O (2); Zn0.945Fe1.78O3.71 (2); Li0.25Zn0.5La0.04Fe2.01O4 (1); Li0.05Zn0.9La0.04Fe2.01O4 (1); Li0.15Zn0.7La0.04Fe2.11O4 (1)
- dopant candidates (<5% at.): Li (6), La (3), Cu (1), Ni (1)
- seed hypothesis (confirm): spinel
- measured range: 11-1073 K (5th-95th pct of 37 curves; full span incl. outliers 11-2802 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zn(FeO2)2 Fd-3m (227) mp-19313 [hull=0.000, icsd=31, PRIMARY]; LiZn4Fe13O24 Cm (8) mp-769606 [hull=0.075, PRIMARY]; LiZn2Fe9O16 Cm (8) mp-771993 [hull=0.057, PRIMARY]; LiZn6Fe17O32 Cm (8) mp-771348 [hull=0.106, PRIMARY]; Zn(Fe2O3)4 P1 (1) mp-1100888 [hull=0.030, PRIMARY]
- papers: Thermoelectric Transport Properties of Fe-Enriched ZnO with High-Temperature Nanostructure Refinement | Correlation of the physico chemical properties of Zn-substituted Li–La ferrite | Electrical Conductivity and Thermoelectric Power of LithiumZinc Ferrites

## Nb
- rank 352 | 20 samples | 5 papers | 1 compositions
- compositions: Nb (20)
- seed hypothesis (confirm): solid_solution_alloy
- measured range: 10-1407 K (5th-95th pct of 21 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nb Im-3m (229) mp-75 [hull=0.000, icsd=18, PRIMARY]; Nb C2/m (12) mp-1104341 [hull=0.000, icsd=1]; Nb Fm-3m (225) mp-8636 [hull=0.342, icsd=1]; Nb P1 (1) mp-1094120 [hull=0.199]
- papers: Intrinsic thermoelectric power of group VB metals | Thermoelectric Properties of Niobium in the Temperature Range 300°–1200°K | Thermoelectric properties of certain metals with a high melting point

## O-Pr-Ti
- rank 353 | 20 samples | 3 papers | 4 compositions
- compositions: Sr0.15Pr0.567TiO3 (9); Pr0.67TiO3 (9); Pr0.6Ca0.1TiO3 (1); PrTiO3 (1)
- dopant candidates (<5% at.): Sr (9), Ca (1)
- measured range: 22-973 K (5th-95th pct of 25 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Pr2Ti2O7 P2_1 (4) mp-15201 [hull=0.000, icsd=1, PRIMARY]; Pr2TiO5 Pnma (62) mp-1195324 [hull=0.000, icsd=1, PRIMARY]; Pr10Ti9GaO34 P2_1/c (14) mp-1211796 [hull=0.017, PRIMARY]; Pr5Ti4GaO17 Pc (7) mp-1220762 [hull=0.015, PRIMARY]; PrTiO3 R-3c (167) mp-753948 [hull=0.029, PRIMARY]
- papers: Neodymium-Strontium Titanate: A New Ceramic for an Old Problem | Enhancing the thermoelectric properties of Sr\n            \n              1−\n              x\n            \n            Pr\n            \n              2\n              x\n              /3\n            \n            □\n            \n              x\n            \n            /3\n            TiO\n            \n              3±\n              δ\n            \n            through control of crystal structure and microstructure | Nonlinear Behavior in the Electrical Resistance of Strongly Correlated Insulators

## S-Sn-Ti
- rank 354 | 20 samples | 6 papers | 11 compositions
- compositions: (SnS)1.2(TiS2)2 (4); Sn1.2Ti0.8S3 (3); (SnS)0.6(CuCl)0.02(TiS2)0.98 (2); (Sb0.04Sn0.96S)1.2(Cu0.02Ti0.98S2)2 (2); (SnCl2)0.02(SnS)0.98(TiS2)1.67 (2); (SnS)1.2(Cu0.02Ti0.98S2)2 (2)
- dopant candidates (<5% at.): Cu (6), Cl (4), Sb (2), Ag (2), Nb (2)
- seed hypothesis (confirm): misfit_layered_chalcogenide
- measured range: 305-722 K (5th-95th pct of 106 curves; full span incl. outliers 26-774 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti3Sn5S12 Pm (6) mp-1217186 [hull=0.014, PRIMARY]
- papers: Intercalation: Building a Natural Superlattice for Better Thermoelectric Performance in Layered Chalcogenides | Low-Thermal-Conductivity (MS)1+x(TiS2)2 (M = Pb, Bi, Sn) Misfit Layer Compounds for Bulk Thermoelectric Materials | Effect of multisite alloying and chloride doping for realizing a high thermoelectric performance in misfit-layered chalcogenide

## Al-Ce-Cu-Ni
- rank 355 | 19 samples | 4 papers | 5 compositions
- compositions: Ce(Ni0.7Cu0.3)2Al3 (11); Ce(Ni0.6Cu0.4)2Al3 (4); Ce(Ni0.8Cu0.2)2Al3 (2); Ce(Ni0.4Cu0.6)2Al3 (1); Ce(Ni0.5Cu0.5)2Al3 (1)
- measured range: 10-296 K (5th-95th pct of 29 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeAl(CuNi)2 Cmmm (65) mp-1226666 [hull=0.023, PRIMARY]; CeAl(CuNi)2 Amm2 (38) mp-1226667 [hull=0.098]
- papers: Mangnetoresistance Of Heavy Fermion-like Compound Ce(Ni1-xCux)2Al3 | Magnetic, Thermal and Transport Properties of Ce(Ni1-xCux)2Al3: The Dominant Role of Electronic Change | Enhancement in thermoelectric power of Ce(Ni1−xCux)2Al3: An implication of two-band conduction

## Al-Co-Ni
- rank 356 | 19 samples | 8 papers | 5 compositions
- compositions: Al74Ni10Co16 (6); Al69.7Co10.0Ni20.3 (5); Al70Ni15Co15 (4); Al65Ni20Co15 (3); Al71Ni16Co13 (1)
- seed hypothesis (confirm): quasicrystal_approximant
- measured range: 10-872 K (5th-95th pct of 32 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al18Co5Ni3 Cm (8) mp-1229050 [hull=0.003, PRIMARY]; Al2CoNi P4/mmm (123) mp-1228913 [hull=0.013, PRIMARY]; Al9Co2Ni Immm (71) mp-1228742 [hull=0.017, PRIMARY]; AlCo2Ni I4/mmm (139) mp-1214822 [hull=0.104, PRIMARY]; AlCoNi6 P4/mmm (123) mp-1228972 [hull=0.019, PRIMARY]
- papers: Intrinsic anisotropic magnetic, electrical, and thermal transport properties of<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mi>d</mml:mi></mml:math>-Al-Co-Ni decagonal quasicrystals | Heat Transport in Aluminum-Based Quasicrystals i-AlPdMn, i-AlCuFe, and d-AlCoNi | Micro-surface and bulk thermal behavior of a single-grain decagonal Al–Ni–Co quasicrystal

## As-Ga
- rank 357 | 19 samples | 7 papers | 2 compositions
- compositions: GaAs (13); (AlAs)1(GaAs)10 (6)
- dopant candidates (<5% at.): Al (6)
- seed hypothesis (confirm): sphalerite
- measured range: 11-360 K (5th-95th pct of 30 curves; full span incl. outliers 10-1182 K)
- [ref 1] TEDesignLab / ICSD: GaAs F-43m (216) mp-2534 [hull=0.000, icsd=29, PRIMARY]; GaAs P6_3mc (186) mp-8883 [hull=0.013, icsd=2]
- [ref 2] MP, ranked by ICSD evidence: Ga3As Pm-3m (221) mp-1184232 [hull=0.257, PRIMARY]; GaAs3 Fm-3m (225) mp-1183979 [hull=0.506, PRIMARY]; GaAs Pa-3 (205) mp-15619 [hull=0.144, icsd=1]; GaAs Imm2 (44) mp-603640 [hull=0.353, icsd=1]; GaAs Pmm2 (25) mp-1059094 [hull=0.437, icsd=1]
- papers: Nanograined Half-Heusler Semiconductors as Advanced Thermoelectrics: An Ab Initio High-Throughput Statistical Study | Evolution of structural and thermoelectric properties of indium-ion-implanted epitaxial GaAs | Influence of embedded indium nanocrystals on GaAs thermoelectric properties

## As-Ga-In
- rank 358 | 19 samples | 5 papers | 13 compositions
- compositions: (TbAs)0.0636InGaAs (3); InGaAs (3); (ErAs)0.002In0.53Ga0.4Al0.06As (2); (TbAs)1.12(In0.53Ga0.47As)98.88 (2); (TbAs)0.0247InGaAs (1); In0.53Ga0.4Al0.06As (1)
- dopant candidates (<5% at.): Tb (12), Al (3), Er (3)
- seed hypothesis (confirm): sphalerite
- measured range: 31-780 K (5th-95th pct of 41 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): In2GaAs3 I-4m2 (119) mp-1223859 [hull=0.027, PRIMARY]; InGa5As4 R3m (160) mp-1224045 [hull=0.135, PRIMARY]; InGaAs2 P-4m2 (115) mp-1223781 [hull=0.030, PRIMARY]; InGaAs2 R3m (160) mp-1223791 [hull=0.035]
- papers: Thermoelectric Transport in InGaAs with High Concentration of Rare-Earth TbAs Embedded Nanoparticles | ErAs:InGaAs∕InGaAlAs superlattice thin-film power generator array | Cross-plane lattice and electronic thermal conductivities of ErAs:InGaAs∕InGaAlAs superlattices

## Ba-Co-La-O
- rank 359 | 19 samples | 8 papers | 8 compositions
- compositions: LaBaCo2O5.5 (6); La0.5Ba0.5CoO3 (6); La0.7Ba0.3CoO3 (2); La0.3Ba0.7Co0.8Nb0.2O3 (1); Ba0.4La0.6Co0.8Fe0.2O3 (1); Ba0.6La0.4Co0.8Fe0.2O3 (1)
- dopant candidates (<5% at.): Fe (2), Nb (1), Pr (1), Ti (1), Sb (1)
- seed hypothesis (confirm): layered_double_perovskite
- measured range: 12-1238 K (5th-95th pct of 21 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaLa(CoO3)2 P4/mmm (123) mp-24855 [hull=0.072, icsd=1, PRIMARY]; Ba3La7Mn2(Co4O15)2 P2/m (10) mp-694945 [hull=0.048, PRIMARY]; Ba3La7Mn(Co3O10)3 P2/m (10) mp-704461 [hull=0.051, PRIMARY]; Ba4La4Co8O17 P2_1/c (14) mp-1229302 [hull=0.111, PRIMARY]; Ba4La4Co8O23 C2/m (12) mp-1228530 [hull=0.041, PRIMARY]
- papers: Electron transport and thermoelectric properties of layered perovskite LaBaCo2O5.5 | Transport and Magnetic Properties of R1-xAxCoO3(R = La, Pr and Nd; A = Ba, Sr and Ca) | Effect of Nb5+ content on the high temperature properties of the mixed conductors system La1−xBaxCo1−yNbyO3−δ with 0.6 ≤ x ≤ 1.0 and 0 ≤ y ≤ 0.4

## Bi-F-O-Pr-S
- rank 360 | 19 samples | 1 papers | 2 compositions
- compositions: PrO0.3F0.7BiS2 (10); PrO0.5F0.5BiS2 (9)
- seed hypothesis (confirm): bis2_layered
- measured range: 12-295 K (5th-95th pct of 2 curves)
- papers: Superconducting and magneto-transport properties of BiS2 based superconductor PrO1-xFxBiS2 (x = 0 to 0.9)

## Bi-K-Se
- rank 361 | 19 samples | 7 papers | 10 compositions
- compositions: K2Bi8Se13 (10); K1.5Rb0.5Bi8Se13 (1); K1.8Rb0.2Bi8Se13 (1); K2Bi7.2Sb0.8Se13 (1); K2(Bi0.95Mn0.05)8Se13 (1); K2Bi8(Se0.95Te0.05)13 (1)
- dopant candidates (<5% at.): Cl (4), Rb (2), Sb (1), Mn (1), Te (1)
- seed hypothesis (confirm): bi_chalcogenide_complex
- measured range: 12-874 K (5th-95th pct of 48 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): K2Bi8Se13 C2/m (12) mp-28800 [hull=0.000, icsd=1, PRIMARY]; K3BiSe3 P2_13 (198) mp-28980 [hull=0.000, icsd=1, PRIMARY]; KBiSe2 I4_1/amd (141) mp-36539 [hull=0.054, PRIMARY]; K2Bi8Se13 P2_1/m (11) mp-1224244 [hull=0.030]; KBiSe2 P4/mmm (123) mp-1223436 [hull=0.209]
- papers: Thermoelectric Properties and Site-Selective Rb+/K+Distribution in the K2-xRbxBi8Se13Series | Structure inhomogeneities, shallow defects, and charge transport in the series of thermoelectric materials K2Bi8−xSbxSe13 | Thermoelectric Properties of Hot-Pressed β-K2Bi8Se13−x S x Materials

## Bi-S-Ti
- rank 362 | 19 samples | 5 papers | 15 compositions
- compositions: (BiS)1.2(TiS2)2 (4); (BiS)1.2(Ti0.95Cr0.05S2)2 (2); (BiS)1.2(Ti0.95Fe0.05S2)2 (1); (BiS)1.2(Ti0.95Co0.05S2)2 (1); (BiS)1.2(Ti0.95Ni0.05S2)2 (1); (BiS)1.2(Ti0.95V0.05S2)2 (1)
- dopant candidates (<5% at.): Cr (4), Fe (1), Co (1), Ni (1), V (1), Mn (1), Cu (1), Zn (1), Ca (1), Sr (1), Mg (1)
- seed hypothesis (confirm): misfit_layered_chalcogenide
- measured range: 297-785 K (5th-95th pct of 92 curves; full span incl. outliers 15-792 K)
- papers: Effects of Transition Metal Substitution on the Thermoelectric Properties of Metallic (BiS)1.2(TiS2)2 Misfit Layer Sulfide | Effects of alkaline earth doping on the thermoelectric properties of misfit layer sulfides | Enhanced thermoelectric properties of bismuth intercalated compounds BixTiS2

## C-H-N
- rank 363 | 19 samples | 7 papers | 14 compositions
- compositions: C6H7N (6); Ag0.001(C6H7N) (1); Ag0.002(C6H7N) (1); Ag0.003(C6H7N) (1); Ag0.004(C6H7N) (1); C6H7NCl0.1 (1)
- dopant candidates (<5% at.): Ag (4), Cl (2), Ni (1), Se (1), Bi (1)
- seed hypothesis (confirm): organic_polymer
- measured range: 200-413 K (5th-95th pct of 92 curves; full span incl. outliers 158-527 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): H5CN3 Pbca (61) mp-1196017 [hull=0.007, icsd=7, PRIMARY]; HC2N3 P1 (1) mp-1200473 [hull=0.005, icsd=4, PRIMARY]; H2CN2 P2_1/c (14) mp-30094 [hull=0.041, icsd=2, PRIMARY]; CuH12Pt(CN2)4 Pnma (62) mp-1196682 [hull=0.104, icsd=2, PRIMARY]; CrCoH18(CN2)6 R-3 (148) mp-24376 [hull=0.070, icsd=2, PRIMARY]
- papers: One-pot fabrication and thermoelectric properties of Ag nanoparticles–polyaniline hybrid nanocomposites | A three-in-one improvement in thermoelectric properties of polyaniline brought by nanostructures | Investigating thermoelectric properties of doped polyaniline nanowires

## Cd-Eu-Sb
- rank 364 | 19 samples | 10 papers | 9 compositions
- compositions: EuCd2Sb2 (8); Eu11Cd6Sb12 (4); Eu11Cd6Sb11As (1); Eu11Cd3Sb12 (1); Eu11Cd5ZnSb12 (1); EuCd1.9Mn0.1Sb2 (1)
- dopant candidates (<5% at.): Zn (2), Mn (2), As (1), Yb (1)
- seed hypothesis (confirm): caal2si2_zintl, zintl_11_6_12  <-- MIXED, split per composition
- measured range: 12-780 K (5th-95th pct of 80 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Eu(CdSb)2 P-3m1 (164) mp-19774 [hull=0.000, icsd=1, PRIMARY]
- papers: High-Temperature Thermoelectric Properties of the Solid–Solution Zintl Phase Eu11Cd6Sb12–xAsx(x< 3) | High Temperature Thermoelectric Properties of the Solid-Solution Zintl Phase Eu11Cd6–xZnxSb12 | Thermoelectric properties of Eu(Zn1−xCdx)2Sb2

## Ce-La-Ni
- rank 365 | 19 samples | 4 papers | 15 compositions
- compositions: (Ce0.75La0.25)Ni (2); (Ce0.5La0.5)Ni (2); (Ce0.1La0.9)Ni (2); (Ce0.9La0.1)7Ni3 (2); (Ce0.82La0.18)Ni2 (1); (Ce0.25La0.75)Ni (1)
- seed hypothesis (confirm): crb_feb_chain
- solid-solution axis: Ce/(Ce+La) spans 0.10-0.90 (median 0.50) over 15 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-300 K (5th-95th pct of 43 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaCeNi10 Pmmm (47) mp-1223428 [hull=0.000, PRIMARY]
- papers: Thermoelectric power of (Ce1−xLax)Ni single crystals | Thermoelectric power of some Ce compounds of the dilute Kondo type | Transport properties of heavy fermion compound Ce7Ni3

## Co-Hf-Sb-Sn-Ti
- rank 366 | 19 samples | 6 papers | 8 compositions
- compositions: Ti0.5Hf0.5CoSb0.8Sn0.2 (7); Hf0.8Ti0.2CoSb0.8Sn0.2 (4); Hf0.7Ti0.3CoSb0.8Sn0.2 (3); (Hf0.72Zr0.1Ti0.18)CoSb0.8Sn0.2 (1); Ti0.75Hf0.25CoSb0.8Sn0.2 (1); Ti0.25Hf0.75CoSb0.8Sn0.2 (1)
- dopant candidates (<5% at.): Zr (1), Cu (1), Te (1), Ni (1), Se (1)
- solid-solution axis: Hf/(Hf+Ti) spans 0.25-0.80 (median 0.70) over 8 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 23-1091 K (5th-95th pct of 73 curves)
- papers: Thermoelectric Property Study of Nanostructured p-Type Half-Heuslers (Hf, Zr, Ti)CoSb0.8Sn0.2 | Fine tuning of thermoelectric performance in phase-separated half-Heusler compounds | Enhanced thermoelectric performance in the p-type half-Heusler (Ti/Zr/Hf)CoSb0.8Sn0.2 system via phase separation

## Co-In-S-Sn
- rank 367 | 19 samples | 3 papers | 19 compositions
- compositions: Co3Sn1.6In0.4S2 (1); Co3Sn1.4In0.6S2 (1); Co3Sn1.3In0.7S2 (1); Co3Sn1.2In0.8S2 (1); Co3Sn1.15In0.85S2 (1); Co3Sn1.1In0.9S2 (1)
- dopant candidates (<5% at.): Fe (4), Se (1)
- seed hypothesis (confirm): shandite
- measured range: 30-679 K (5th-95th pct of 69 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): InCo3SnS2 R-3m (166) mp-1077901 [hull=0.000, icsd=2, PRIMARY]
- papers: Interplay of Metal-Atom Ordering, Fermi Level Tuning, and Thermoelectric Properties in Cobalt Shandites Co3M2S2(M = Sn, In) | The effect of simultaneous substitution on the electronic band structure and thermoelectric properties of Se-doped Co3SnInS2 with the Kagome lattice | Improved Thermoelectric Performance through Double Substitution in Shandite-Type Mixed-Metal Sulfides

## Co-La-Ni-O
- rank 368 | 19 samples | 10 papers | 10 compositions
- compositions: LaCo0.7Ni0.3O3 (4); LaNi0.7Co0.3O3 (3); LaNi0.6Co0.4O3 (3); LaCo0.6Ni0.4O3 (2); LaCo0.5Ni0.5O3 (2); LaNiCoO3 (1)
- dopant candidates (<5% at.): Fe (1)
- measured range: 14-1171 K (5th-95th pct of 30 curves; full span incl. outliers 13-1238 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2CoNiO6 R-3 (148) mp-1223259 [hull=0.000, PRIMARY]
- papers: Thermoelectric properties of LaNi[sub 1−x]Co[sub x]O[sub 3] solid solution | Development of Perovskite-type Cobaltates and Manganates for Thermoelectric Oxide Modules | Fabrication of p- and n-type Thermoelectric Cobalt Oxides through the Powder-In-Tube Method

## Co-O-Pr-Sr
- rank 369 | 19 samples | 8 papers | 13 compositions
- compositions: SrPrCoO4 (3); Pr0.7Sr0.3CoO3 (3); Pr0.5Sr0.5CoO3 (3); Pr0.75Sr1.25CoO4 (1); Pr0.6Sr0.4CoO3 (1); PrBa0.42Sr0.5Co2O5 (1)
- dopant candidates (<5% at.): Cu (4), Fe (2), Nb (2), Ba (1)
- seed hypothesis (confirm): ruddlesden_popper
- measured range: 12-1166 K (5th-95th pct of 19 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrPr(CoO3)2 Pc (7) mp-1218091 [hull=0.000, PRIMARY]
- papers: Studies of structural, magnetic, electrical and thermal properties in layered perovskite cobaltite SrLnCoO4 (Ln = La, Ce, Pr, Nd, Eu, Gd and Tb) | Transport and Magnetic Properties of R1-xAxCoO3(R = La, Pr and Nd; A = Ba, Sr and Ca) | Dielectric, magnetic, and magnetotransport properties in Sr doped two-dimensional RE2CoO4 (RE=Pr,Eu) compounds

## Co-O-Y
- rank 370 | 19 samples | 4 papers | 11 compositions
- compositions: YCoO3 (6); Y0.9Ca0.1CoO3 (2); Y0.95Ca0.05CoO3 (2); Y0.99Ca0.01CoO3 (2); Y0.95Sr0.05CoO3 (1); Y0.85Sr0.15CoO3 (1)
- dopant candidates (<5% at.): Ca (6), Sr (4), Ni (3)
- measured range: 118-1091 K (5th-95th pct of 40 curves; full span incl. outliers 110-3000 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YCoO3 Pnma (62) mp-691138 [hull=0.021, icsd=5, PRIMARY]; Y2Co2O5 P4/mmm (123) mp-1187759 [hull=0.419, PRIMARY]
- papers: Effect of Sr substitution on electrical transport and thermoelectric properties of Y1−xSrxCoO3 (0≤x≤0.2) prepared by sol–gel process | Electrical transport and thermoelectric properties of Ni-doped perovskite-type YCo1−xNixO3(0 ≤x≤ 0.07) prepared by sol-gel process | Electrical transport and thermoelectric properties of Y1−xCaxCoO3 (0⩽x⩽0.1) at high temperatures

## Co-Pt-Sb-Sn-Zr
- rank 371 | 19 samples | 2 papers | 9 compositions
- compositions: Zr(Co0.8Pt0.2)(Sb0.7Sn0.3) (3); Zr(Co0.8Pt0.2)(Sb0.8Sn0.2) (2); Zr(Co0.6Pt0.4)(Sb0.75Sn0.25) (2); Zr(Co0.7Pt0.3)(Sb0.8Sn0.2) (2); Zr(Co0.7Pt0.3)(Sb0.7Sn0.3) (2); Zr(Co0.8Pt0.2)(Sb0.65Sn0.35) (2)
- measured range: 11-318 K (5th-95th pct of 52 curves)
- papers: Half-Heusler phases as prospective p-type thermoelectric materials | Thermoelectric properties of semimetallic (Zr, Hf)CoSb half-Heusler phases

## Cu-La-O-S
- rank 372 | 19 samples | 4 papers | 19 compositions
- compositions: LaCu0.97SO (1); LaCuSO (1); LaCu0.98SO (1); LaCu0.99SO (1); La0.925Sr0.075Cu0.925Mn0.075SO (1); LaCu0.925Mn0.075SO (1)
- dopant candidates (<5% at.): Sr (7), Ca (6), Ni (6), Mn (5)
- seed hypothesis (confirm): zrcusias_1111
- measured range: 11-300 K (5th-95th pct of 26 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaCuSO P4/nmm (129) mp-6088 [hull=0.000, icsd=4, PRIMARY]; La2CuS2O P4/mmm (123) mp-1213297 [hull=1.547, PRIMARY]; La5Cu6S7O4 Ima2 (46) mp-1223375 [hull=0.010, PRIMARY]
- papers: Effects of the Cu off-stoichiometry on transport properties of wide gap p-type semiconductor, layered oxysulfide LaCuSO | Sr and Mn co-doped LaCuSO: A wide band gap oxide diluted magnetic semiconductor with <i>T<sub>C</sub></i> around 200 K | Electrical resistivity and photoemission spectra of layered oxysulfide (La1$minus;xCaxO)Cu1$minus;xNixS

## Cu-O-Pr
- rank 373 | 19 samples | 5 papers | 11 compositions
- compositions: Pr1.85Ce0.15CuO4 (9); Gd0.3Pr1.55Ce0.15CuO4 (1); Gd0.05Pr1.8Ce0.15CuO4 (1); Pr2Cu0.999Zn0.001O4 (1); Pr2Cu0.997Zn0.003O4 (1); Pr2Cu0.99Zn0.01O4 (1)
- dopant candidates (<5% at.): Ce (12), Zn (6), Gd (2)
- seed hypothesis (confirm): ruddlesden_popper
- measured range: 10-301 K (5th-95th pct of 19 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Pr2CuO4 I4/mmm (139) mp-4181 [hull=0.000, icsd=12, PRIMARY]; PrCuO2 R-3m (166) mp-13694 [hull=0.000, icsd=2, PRIMARY]; Pr2Cu2O5 Pbam (55) mp-1188871 [hull=0.061, icsd=1, PRIMARY]; Pr(CuO2)2 I4_1/a (88) mp-1101476 [hull=0.000, PRIMARY]; PrCuO3 Pm-3m (221) mp-1186515 [hull=0.026, PRIMARY]
- papers: Superconductivity and thermoelectric power ofPr1.85Ce0.15CuO4−y | Thermoelectric power in Gd1.85−xPrxCe0.15CuO4 system | Thermoelectric power ofNd1.85Ce0.15CuO4−yandPr1.85Ce0.15CuO4−y

## Ga-Sb
- rank 374 | 19 samples | 4 papers | 15 compositions
- compositions: (GaSb)89.92(FeGa1.3)10.08 (3); (GaSb)2.85(Ga2Te3)0.05 (2); (GaSb)3 (2); Ga0.99Zn0.01Sb (1); Ga0.998Zn0.002Sb (1); Ga0.999Zn0.001Sb (1)
- dopant candidates (<5% at.): Te (9), Zn (4), Fe (3)
- measured range: 81-875 K (5th-95th pct of 67 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GaSb F-43m (216) mp-1156 [hull=0.000, icsd=15, PRIMARY]; Ga3Sb I4/mmm (139) mp-1184258 [hull=0.155, PRIMARY]; GaSb3 Fm-3m (225) mp-1184224 [hull=0.272, PRIMARY]; GaSb P6_3mc (186) mp-1018059 [hull=0.015, icsd=1]; GaSb I-4m2 (119) mp-1224785 [hull=0.193]
- papers: Thermoelectric properties of Zn-doped GaSb | Improved Thermoelectric Properties in Ga2Te3-GaSb Vacancy Compounds | Nanostructuring and Thermoelectric Characterization of (GaSb)3(1−x)(Ga2Te3) x

## H-Pd
- rank 375 | 19 samples | 1 papers | 9 compositions
- compositions: Pd0.97Ce0.03H0.5 (6); Pd0.95Ge0.05H (6); PdH0.66 (1); PdH0.47 (1); PdH0.86 (1); PdH0.7 (1)
- dopant candidates (<5% at.): Ge (6), Ce (6)
- seed hypothesis (confirm): interstitial_hydride
- measured range: 82-297 K (5th-95th pct of 19 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HPd Fm-3m (225) mp-24289 [hull=0.000, icsd=2, PRIMARY]; H3Pd4 R-3m (166) mp-1224413 [hull=0.001, PRIMARY]; H4Pd3 P4mm (99) mp-1224352 [hull=0.102, PRIMARY]; HPd3 P6_3/mmc (194) mp-983407 [hull=0.520, PRIMARY]; HPd P6_3mc (186) mp-1184548 [hull=0.000]
- papers: Thermoelectric power of hydrogenated palladium and some of its dilute alloys, between 80 and 300 K

## Ir-O-Y
- rank 376 | 19 samples | 5 papers | 10 compositions
- compositions: Y2Ir2O7 (7); Y1.7Bi0.3Ir2O7 (2); Y1.8Bi0.2Ir2O7 (2); Y1.9Bi0.1Ir2O7 (2); Y1.6Bi0.4Ir2O7 (1); Y1.68Bi0.32Ir2O7 (1)
- dopant candidates (<5% at.): Bi (9), Cr (3)
- seed hypothesis (confirm): pyrochlore
- measured range: 10-348 K (5th-95th pct of 19 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y2Ir2O7 Fd-3m (227) mp-1191749 [hull=0.000, icsd=1, PRIMARY]
- papers: Spin–Glass-like Transition and Hall Resistivity of Y2-xBixIr2O7 | Coexistence of high electrical conductivity and weak ferromagnetism in Cr doped Y    2Ir    2O    7 pyrochlore iridates | Nonequilibrium low temperature phase in pyrochlore iridate Y2Ir2O7: Possibility of glass-like dynamics

## N-U
- rank 377 | 19 samples | 8 papers | 4 compositions
- compositions: UN (14); (GdN)5.07(UN)94.93 (2); (GdN)9.97(UN)90.03 (2); U2N3 (1)
- dopant candidates (<5% at.): Gd (4)
- seed hypothesis (confirm): rocksalt_nitride_carbide
- measured range: 243-1981 K (5th-95th pct of 21 curves; full span incl. outliers 243-2596 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UN Fm-3m (225) mp-1865 [hull=0.000, icsd=25, PRIMARY]; U2N3 P-3m1 (164) mp-973 [hull=0.019, icsd=6, PRIMARY]; UN2 Fm-3m (225) mp-1776 [hull=0.000, icsd=2, PRIMARY]; U16N25 R3 (146) mp-32742 [hull=0.006, PRIMARY]; U4N7 I4cm (108) mp-32590 [hull=0.000, PRIMARY]
- papers: Uranium Nitride U2N3 as a novel thermoelectric material | Material property correlations for uranium mononitride | Coupled analysis for new fuel design using UN and UC for SCWR

## Nb-O-W
- rank 378 | 19 samples | 4 papers | 12 compositions
- compositions: Nb8W9O47 (4); Nb4W13O47 (3); Nb5W12O47 (3); (W1.083O3)0.31(Nb2.1O5)0.69 (1); (W1.083O3)0.48(Nb2.1O5)0.52 (1); (W1.083O3)0.67(Nb2.1O5)0.33 (1)
- seed hypothesis (confirm): block_shear_niobate
- measured range: 299-1171 K (5th-95th pct of 60 curves; full span incl. outliers 298-1273 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nb12WO33 C2 (5) mp-1198790 [hull=0.041, icsd=1, PRIMARY]; NbWO7 Ima2 (46) mp-1220547 [hull=0.376, PRIMARY]; Nb12WO33 P1 (1) mp-704637 [hull=0.007]
- papers: Single-step preparation and consolidation of reduced early-transition-metal oxide/metal n-type thermoelectric composites | Tetragonal tungsten bronzes Nb8−xW9+xO47−δ: optimization strategies and transport properties of a new n-type thermoelectric oxide | Thermophysical properties of rare earth barium aluminates

## Ag-S-Te
- rank 379 | 18 samples | 2 papers | 12 compositions
- compositions: Ag3.95TeS (3); Ag4.08TeS (3); Ag4TeS (3); Ag2Te0.8S0.2 (1); Ag3.92TeS (1); Ag2Te0.6S0.4 (1)
- seed hypothesis (confirm): ag2se_naumannite
- solid-solution axis: S/(S+Te) spans 0.20-0.50 (median 0.50) over 12 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 297-723 K (5th-95th pct of 78 curves)
  !! MEASUREMENT CROSSES A TRANSITION: ag2se_naumannite -> bcc_superionic at ~406 K (P212121 -> bcc superionic, ~406 K. Ag2Te transforms near ~418 K.)
     Record each phase with its own temperature range, not a single prototype.
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ag2TeS3 Cc (9) mp-29163 [hull=0.000, icsd=1, PRIMARY]
- papers: Semiconductor glass with superior flexibility and high room temperature thermoelectric performance | Ductile inorganic amorphous/crystalline composite Ag4TeS with phonon-glass electron-crystal transport behavior and excellent stability of high thermoelectric performance on plastic deformation

## Al-La
- rank 380 | 18 samples | 7 papers | 10 compositions
- compositions: LaAl2 (6); (La0.9901Ce0.0099)Al2 (2); (La0.985Ce0.015)Al2 (2); (La0.9936Ce0.0064)Al2 (2); Ce0.01La0.99Al3 (1); Ce0.1La0.9Al3 (1)
- dopant candidates (<5% at.): Ce (11)
- seed hypothesis (confirm): laves_phase
- measured range: 10-324 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaAl2 Fd-3m (227) mp-2694 [hull=0.000, icsd=15, PRIMARY]; LaAl3 P6_3/mmc (194) mp-959 [hull=0.000, icsd=4, PRIMARY]; LaAl4 I4/mmm (139) mp-21109 [hull=0.017, icsd=3, PRIMARY]; La3Al P6_3/mmc (194) mp-1084828 [hull=0.023, icsd=2, PRIMARY]; La3Al11 Immm (71) mp-16505 [hull=0.000, icsd=2, PRIMARY]
- papers: Thermoelectric power of RAl2 | Giant thermoelectric power of (La, Ce)Al2 | Influence of the crystalline field on the Kondo effect: Cerium and ytterbium impurities

## Al-Ru
- rank 381 | 18 samples | 6 papers | 15 compositions
- compositions: RuAl2 (4); Ru0.85Fe0.15Al1.95Si0.05 (1); Ru0.9Fe0.1Al2 (1); Ru0.85Fe0.15Al2 (1); (Ru0.85Fe0.15)0.98Mn0.02Al2 (1); (Ru0.85Fe0.15)0.95Mn0.05Al2 (1)
- dopant candidates (<5% at.): Fe (6), Ce (3), Si (2), Mn (2), Y (2), La (1)
- measured range: 12-975 K (5th-95th pct of 41 curves; full span incl. outliers 11-1091 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al2Ru Fddd (70) mp-10910 [hull=0.000, icsd=2, PRIMARY]; Al13Ru4 C2/m (12) mp-17880 [hull=0.000, icsd=2, PRIMARY]; Al3Ru2 I4/mmm (139) mp-1070580 [hull=0.001, icsd=1, PRIMARY]; Al12Ru P-43m (215) mp-1198296 [hull=0.142, icsd=1, PRIMARY]; Al3Ru P6_3/mmc (194) mp-1188814 [hull=0.177, icsd=1, PRIMARY]
- papers: Synthesis and thermoelectric properties of silicon- and manganese-doped Ru1−xFexAl2 | Thermoelectric Properties of Binary Semiconducting Intermetallic Compounds Al<SUB>2</SUB>Ru and Ga<SUB>2</SUB>Ru Synthesized by Spark Plasma Sintering Process | Microstructure and Thermal Conductivity of RuAl<sub>2</sub> Prepared by a Single-Roll Melt-Spinning Method

## Ba-Co-O-Pr
- rank 382 | 18 samples | 6 papers | 14 compositions
- compositions: Pr0.5Ba0.5CoO3 (3); Pr0.7Ba0.3CoO3 (2); Pr0.94BaCo2O5 (2); Pr0.94BaCo2O6 (1); Pr0.9Ca0.1BaCo2O5 (1); PrBaCo2O5 (1)
- dopant candidates (<5% at.): Sr (6), Ca (5)
- seed hypothesis (confirm): layered_double_perovskite
- measured range: 12-1123 K (5th-95th pct of 18 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaPr(CoO3)2 P4/mmm (123) mp-24856 [hull=0.079, icsd=2, PRIMARY]; Ba2Pr2Co4O11 I4/mmm (139) mp-1228571 [hull=0.041, PRIMARY]; Ba2Pr3(CoO3)5 P-1 (2) mp-1229013 [hull=0.062, PRIMARY]; Ba4Pr4Co8O23 P4/mmm (123) mp-1228513 [hull=0.065, PRIMARY]; Ba6Pr2Co4O15 P1 (1) mp-1228751 [hull=0.000, PRIMARY]
- papers: Transport and Magnetic Properties of R1-xAxCoO3(R = La, Pr and Nd; A = Ba, Sr and Ca) | Praseodymium-deficiency Pr0.94BaCo2O6- double perovskite: A promising high performance cathode material for intermediate-temperature solid oxide fuel cells | A-site calcium-doped Pr 1−x Ca x BaCo 2 O 5+δ double perovskites as cathodes for intermediate-temperature solid oxide fuel cells

## Ba-O-Pb-Sr
- rank 383 | 18 samples | 5 papers | 17 compositions
- compositions: Sr0.7Ba0.3PbO3 (2); Sr0.6Ba0.4PbO3 (1); Sr0.5Ba0.5PbO3 (1); Ba0.4Sr0.6PbO3 (1); Ba0.4Sr0.6Pb1.2O3.4 (1); Ba0.4Sr0.6Pb1.1O3.2 (1)
- dopant candidates (<5% at.): Bi (5), La (4)
- solid-solution axis: Ba/(Ba+Sr) spans 0.30-0.50 (median 0.40) over 17 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 295-1082 K (5th-95th pct of 32 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaSr(PbO3)2 Pmc2_1 (26) mp-1227843 [hull=0.007, PRIMARY]
- papers: Preparation of Perovskite-Type Sr1-xBaxPbO3 Ceramics by an Oxalate Coprecipitation Method and the Thermoelectric Properties | Synthesis and thermoelectric properties of ceramics based on barium-strontium metaplumbates | Thermoelectric properties of A-site doped perovskites (Sr0.6Ba0.4)1−xMxPbO3 (M=La, K)

## Bi-C-Te
- rank 384 | 18 samples | 10 papers | 15 compositions
- compositions: Bi2Te3C0.6 (2); Bi2Te3C0.67 (2); Bi2Te3C2 (2); Bi2Te3C0.3 (1); Bi2Te3C3 (1); Bi2Te3C0.5 (1)
- seed hypothesis (confirm): composite_multiphase
- measured range: 14-496 K (5th-95th pct of 81 curves)
- papers: The influence of CNTs on the thermoelectric properties of a CNT/Bi2Te3 composite | Fabrication and Thermoelectric Properties of Graphene/Bi2Te3Composite Materials | Fabrication Process and Thermoelectric Properties of CNT/Bi2(Se,Te)3Composites

## Cd-Sb-Yb-Zn
- rank 385 | 18 samples | 4 papers | 15 compositions
- compositions: YbCd1.6Zn0.4Sb2 (3); YbCd1.2Zn0.8Sb2 (2); YbCd0.4Zn1.6Sb2 (1); YbCdZnSb2 (1); YbCd0.8Zn1.2Sb2 (1); Yb(Zn0.8Cd0.2)2Sb2 (1)
- seed hypothesis (confirm): caal2si2_zintl
- solid-solution axis: Cd/(Cd+Zn) spans 0.20-0.85 (median 0.60) over 15 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 297-705 K (5th-95th pct of 75 curves)
- papers: Synthesis and high thermoelectric efficiency of Zintl phase YbCd2−xZnxSb2 | Zintl phase compounds AM2Sb2 (A=Ca, Sr, Ba, Eu, Yb; M=Zn, Cd) and their substitution variants: a class of potential thermoelectric materials | Designing high-performance layered thermoelectric materials through orbital engineering

## Co-Fe-Na-O
- rank 386 | 18 samples | 4 papers | 8 compositions
- compositions: NaCo1.6Fe0.4O4 (3); NaCo1.4Fe0.6O4 (3); NaCo1.5Fe0.5O4 (2); NaCo0.8Fe1.2O4 (2); NaCo0.6Fe1.4O4 (2); NaCoFeO4 (2)
- seed hypothesis (confirm): naxcoo2_layered
- measured range: 51-1436 K (5th-95th pct of 26 curves)
- papers: Thermoelectric Properties of NaCo2–x Fe x O y | Thermoelectric Properties of NaCo2 − x Fe x O y | Thermopower Enhancement from Engineering the Na0.7CoO2 Interacting Fermiology via Fe Doping

## Cr-Ni
- rank 387 | 18 samples | 8 papers | 14 compositions
- compositions: Ni0.95Cr0.05 (4); Ni0.90Cr0.10 (2); Ni1.56Cr0.18 (1); NiCr (1); CrNi (1); Ni68.6Cr31.4 (1)
- seed hypothesis (confirm): solid_solution_alloy
- measured range: 10-1299 K (5th-95th pct of 19 curves; full span incl. outliers 10-2493 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cr3Ni Pm-3m (221) mp-1008278 [hull=0.148, icsd=1, PRIMARY]; CrNi3 I4/mmm (139) mp-1007923 [hull=0.001, icsd=1, PRIMARY]; Cr2Ni Fd-3m (227) mp-1077252 [hull=0.269, icsd=1, PRIMARY]; CrNi2 Fd-3m (227) mp-1077077 [hull=0.214, icsd=1, PRIMARY]; Cr22Ni50Mo3 P1 (1) mp-767825 [hull=0.000, PRIMARY]
- papers: Electrical and thermoelectric properties of some metallic thermoelectric materials | Transport properties of some hydrogenated nickel-based alloys | Effect of dissolved hydrogen on electron transport in nickel–chromium alloys

## Cu-Ge-Se
- rank 388 | 18 samples | 5 papers | 16 compositions
- compositions: Cu2GeSe3 (3); Cu2Ge0.95In0.05Se3 (1); Cu2Ge0.9In0.1Se3 (1); Cu2Ge0.85In0.15Se3 (1); Cu2.00Ge0.96Se2.82 (1); Cu2.00Ge0.93Se2.79 (1)
- dopant candidates (<5% at.): In (3), Sb (1)
- seed hypothesis (confirm): cu2gese3
- measured range: 15-752 K (5th-95th pct of 68 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu2GeSe3 Imm2 (44) mp-4728 [hull=0.000, icsd=2, PRIMARY]; Cu8GeSe6 Cc (9) mp-1225860 [hull=0.062, PRIMARY]; Cu2GeSe3 Cc (9) mp-677105 [hull=0.002, icsd=1]; Cu2GeSe3 Fdd2 (43) mp-1225866 [hull=0.004]
- papers: Crystallographic Control at the Nanoscale To Enhance Functionality: Polytypic Cu2GeSe3Nanoparticles as Thermoelectric Materials | Thermoelectric properties of Indium doped Cu2GeSe3 | Thermoelectric properties of ternary diamondlike semiconductors Cu2Ge1+xSe3

## Cu-O-Ti
- rank 389 | 18 samples | 3 papers | 18 compositions
- compositions: Cu17.94(TiO2)82.06 (1); Cu21.83(TiO2)78.17 (1); Cu25.53(TiO2)74.47 (1); Cu30.73(TiO2)69.27 (1); Cu38.59(TiO2)61.41 (1); Cu45.59(TiO2)54.41 (1)
- dopant candidates (<5% at.): Ru (7), Y (5), Ca (4), Cr (4), Mn (4), Nd (1), Er (1), Gd (1), La (1), Sm (1), Ho (1)
- seed hypothesis (confirm): composite_multiphase
- measured range: 173-976 K (5th-95th pct of 18 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti3Cu3O Fd-3m (227) mp-21457 [hull=0.000, icsd=2, PRIMARY]; Ti4Cu2O Fd-3m (227) mp-22432 [hull=0.000, icsd=2, PRIMARY]; Ti3CuO8 P-4m2 (115) mp-1103016 [hull=0.081, icsd=1, PRIMARY]; Er2Ti12(CuO4)9 P-3 (147) mp-1225949 [hull=0.061, PRIMARY]; Dy2Ti12(CuO4)9 P-3 (147) mp-1225647 [hull=0.060, PRIMARY]
- papers: Effect of Cu powder addition on thermoelectric properties of Cu/TiO2−x composites | Novel thermoelectric properties of complex transition-metal oxides | Analysis of complex impedance and electrical conductivity of YCr0.5Mn0.5O3–CaCu3Ti4O12 negative temperature coefficient ceramics

## Gd-Mn-O-Sr
- rank 390 | 18 samples | 3 papers | 5 compositions
- compositions: Gd0.5Sr0.5MnO3 (6); Gd0.6Sr0.4MnO3 (3); Gd0.7Sr0.3MnO3 (3); Gd0.4Sr0.6MnO3 (3); Gd0.3Sr0.7MnO3 (3)
- measured range: 11-1144 K (5th-95th pct of 18 curves)
- papers: Colossal thermoelectric power in Gd-Sr manganites | Structural, electrical, magnetic and thermal properties of Gd1–xSrxMnO3 (0.2≤x≤0.5) manganites | Role of structural distortion on thermoelectric aspects of heavily Sr2+ doped GdMnO3

## Ge-Pb-Sn-Te
- rank 391 | 18 samples | 4 papers | 12 compositions
- compositions: Ge0.5Sn0.25Pb0.25Te (7); Ge0.5Sn0.25Pb0.25TeAg0.003 (1); Ge0.6Sn0.1Pb0.3Te (1); Ge0.5Sn0.25Pb0.25Te1.0009Bi0.0006 (1); Sn0.47Cd0.03Ge0.25Pb0.25Te (1); Sn0.8Ge0.1Pb0.1Te (1)
- dopant candidates (<5% at.): Cd (3), Ag (1), Bi (1)
- solid-solution axis: Ge/(Ge+Sn) spans 0.11-0.86 (median 0.35) over 12 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 296-886 K (5th-95th pct of 73 curves)
- papers: Phase morphology effects on the thermoelectric properties of Pb0.25Sn0.25Ge0.5Te | High Thermoelectric Figure of Merit and Nanostructuring in Bulkp-type Gex(SnyPb1−y)1−xTe Alloys Following a Spinodal Decomposition Reaction† | Band Inversion Induced Multiple Electronic Valleys for High Thermoelectric Performance of SnTe with Strong Lattice Softening

## Ge-Pt
- rank 392 | 18 samples | 3 papers | 18 compositions
- compositions: Pr0.5Ce0.5Pt4Ge12 (1); Pr0.25Ce0.75Pt4Ge12 (1); Pr0.7Ce0.3Pt4Ge12 (1); Pr0.55Ce0.45Pt4Ge12 (1); Pr0.375Ce0.625Pt4Ge12 (1); Pr0.5Eu0.5Pt4Ge12 (1)
- dopant candidates (<5% at.): Pr (10), Ce (10), La (8), Eu (5), Th (3)
- measured range: 12-297 K (5th-95th pct of 18 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GePt3 I4/mcm (140) mp-16315 [hull=0.000, icsd=4, PRIMARY]; Ge2Pt3 Pnma (62) mp-21673 [hull=0.000, icsd=2, PRIMARY]; Ge2Pt Pnnm (58) mp-1543 [hull=0.003, icsd=2, PRIMARY]; GePt2 P-62m (189) mp-20061 [hull=0.031, icsd=2, PRIMARY]; Ge3Pt P6_3/mmc (194) mp-1184728 [hull=0.326, PRIMARY]
- papers: Probing the superconductivity ofPrPt4Ge12through Ce substitution | Crossover and coexistence of superconductivity and antiferromagnetism in the filled-skutterudite system \nPr1−xEuxPt4Ge12 | Superconducting and normal state properties of the systemsLa1−xMxPt4Ge12(M = Ce,Th)

## La-S
- rank 393 | 18 samples | 5 papers | 17 compositions
- compositions: LaS1.48 (2); La2Ti0.075S2.67 (1); LaS1.42 (1); LaS1.45 (1); LaS1.35 (1); LaS1.41 (1)
- dopant candidates (<5% at.): Ca (3), Ti (1), Eu (1), Yb (1), Sm (1)
- seed hypothesis (confirm): th3p4
- measured range: 296-1457 K (5th-95th pct of 45 curves; full span incl. outliers 287-1500 K)
- [ref 1] TEDesignLab / ICSD: LaS2 Pnma (62) mp-1508 [hull=0.000, icsd=3, PRIMARY]; La2S3 Pnma (62) mp-7475 [hull=0.000, icsd=3, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: LaS Fm-3m (225) mp-2350 [hull=0.000, icsd=12, PRIMARY]; La3S4 I-43d (220) mp-567 [hull=0.023, icsd=7, PRIMARY]; La10US16 P-4 (81) mp-675741 [hull=0.045, PRIMARY]; La4S7 I-42m (121) mp-1223154 [hull=0.078, PRIMARY]; LaS2 P4/nmm (129) mp-1018751 [hull=0.095, icsd=2]
- papers: Thermoelectric properties of lanthanum sesquisulfide with Ti additive | Preparation of γ‐LaSy(1.33<y<1.50) alloys by the pressure‐assisted reaction sintering method and their thermoelectric properties | Thermoelectric properties of lanthanum sulfide

## Mo-O-Sr
- rank 394 | 18 samples | 11 papers | 17 compositions
- compositions: SrMoO3 (2); SrMg0.1Mo0.9O3 (1); SrMo0.9Co0.1O3 (1); SrMo0.9Fe0.1O3 (1); SrMo0.8Fe0.2O3 (1); SrMo0.9Mg0.1O3 (1)
- dopant candidates (<5% at.): Pr (5), Mg (3), Fe (3), Al (2), Co (1)
- seed hypothesis (confirm): perovskite
- measured range: 10-1123 K (5th-95th pct of 18 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrMoO4 I4_1/a (88) mp-18834 [hull=0.000, icsd=13, PRIMARY]; SrMoO3 Pm-3m (221) mp-18747 [hull=0.071, icsd=5, PRIMARY]; Sr2MoO4 I4/mmm (139) mp-19237 [hull=0.011, icsd=1, PRIMARY]; Sr3MoO6 Fm-3m (225) mp-1205668 [hull=0.110, PRIMARY]; Sr3Mo2O7 I4/mmm (139) mp-1208726 [hull=0.030, PRIMARY]
- papers: Thermal and electrical properties of perovskite-type strontium molybdate | Electrochemical Performance of SrMg<sub>0.1</sub>Mo<sub>0.9</sub>O<sub>3</sub>-Based Composites for Solid Oxide Fuel Cell Anodes | SrMo0.9Co0.1O3−δ: A potential anode for intermediate-temperature solid-oxide fuel cells (IT-SOFC)

## Nb-Si-Te
- rank 395 | 18 samples | 3 papers | 14 compositions
- compositions: Nb3SiTe6 (3); Nb4SiTe4 (3); (Nb0.99Ti0.01)4SiTe4 (1); (Nb0.995Ti0.005)4SiTe4 (1); (Nb0.998Ti0.002)4SiTe4 (1); (Nb0.95Ti0.05)4SiTe4 (1)
- dopant candidates (<5% at.): Mo (7), Ti (4), Sb (1)
- measured range: 10-302 K (5th-95th pct of 51 curves; full span incl. outliers 10-374 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nb2SiTe4 P2_1/c (14) mp-29072 [hull=0.000, icsd=1, PRIMARY]; Nb4SiTe4 Pbam (55) mp-1232409 [hull=0.000, PRIMARY]; Nb2SiTe4 P-1 (2) mp-1173475 [hull=0.030]; Nb2SiTe4 P1 (1) mp-690578 [hull=0.270]
- papers: Hole-doped M4SiTe4 (M = Ta, Nb) as an efficient p-type thermoelectric material for low-temperature applications | Thermoelectric properties of layered ternary telluride \nNb3SiTe6 | Large thermoelectric power factor in one-dimensional telluride Nb4SiTe4and substituted compounds

## O-Sr-V
- rank 396 | 18 samples | 5 papers | 13 compositions
- compositions: SrVO3 (5); La0.2Sr0.8VO3 (2); SrTi0.17V0.83O3 (1); SrV0.97Nb0.03O3 (1); SrV0.9Nb0.1O3 (1); SrV0.8Nb0.2O3 (1)
- dopant candidates (<5% at.): Nb (8), La (5), Y (3), Ti (1)
- seed hypothesis (confirm): perovskite
- measured range: 11-1283 K (5th-95th pct of 18 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrV6O11 P6_3/mmc (194) mp-25128 [hull=0.034, icsd=4, PRIMARY]; Sr2VO4 I4/mmm (139) mp-18972 [hull=0.026, icsd=4, PRIMARY]; Sr5V3ClO12 P6_3/m (176) mp-705168 [hull=0.000, icsd=4, PRIMARY]; SrVO3 Pm-3m (221) mp-18717 [hull=0.036, icsd=3, PRIMARY]; Sr2V2O7 P-1 (2) mp-19368 [hull=0.001, icsd=2, PRIMARY]
- papers: Thermoelectric response in the incoherent transport region near Mott transition: The case study of La1−xSrxVO3 | Metal-insulator transition in SrTi<sub>1−</sub><sub><i>x</i></sub>V<sub><i>x</i></sub>O<sub>3</sub>thin films | Solid-phase epitaxial growth of the correlated-electron transparent conducting oxide \n<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:mrow><mml:mi>SrV</mml:mi><mml:msub><mml:mi mathvariant=\"normal\">O</mml:mi><mml:mn>3</mml:mn></mml:msub></mml:mrow></mml:math>

## Pb-Se-Sn-Te
- rank 397 | 18 samples | 5 papers | 17 compositions
- compositions: PbSnTeSe (2); Pb0.94SnTeSeLa0.06 (1); Pb0.92SnTeSeLa0.08 (1); Pb0.98SnTeSeLa0.02 (1); Pb1SnTeSeLa0 (1); Pb0.9SnTeSeLa0.1 (1)
- dopant candidates (<5% at.): La (5), Na (4)
- solid-solution axis: Pb/(Pb+Sn) spans 0.20-0.89 (median 0.50) over 17 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 297-879 K (5th-95th pct of 90 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SnTePbSe R3m (160) mp-1218892 [hull=0.024, PRIMARY]; SnTePbSe P4/mmm (123) mp-1218887 [hull=0.065]
- papers: Thermoelectric performance of PbSnTeSe high-entropy alloys | Thermoelectric transport properties of Pb–Sn–Te–Se system | Tuning figure of merit in Na doped nanocrystalline PbSnTeSe high entropy alloy via band engineering

## Se-Te
- rank 398 | 18 samples | 7 papers | 18 compositions
- compositions: Te95Se5 (1); ((Te85Se15)45As35Cu25)0.9(Bi0.5Sb1.5Te3)0.1 (1); ((Te85Se15)45As35Cu25)0.7(Bi0.5Sb1.5Te3)0.3 (1); ((Te85Se15)45As35Cu25)0.5(Bi0.5Sb1.5Te3)0.5 (1); (Te85Se15)45As35Cu25 (1); (Bi2Se3)6.1(Te3)93.9 (1)
- dopant candidates (<5% at.): Sb (10), As (6), Cu (4), Bi (4), Ag (3)
- seed hypothesis (confirm): trigonal_te, amorphous  <-- MIXED, split per composition
- solid-solution axis: Se/(Se+Te) spans 0.05-0.29 (median 0.09) over 18 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 295-701 K (5th-95th pct of 59 curves; full span incl. outliers 293-774 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Te3Se P6_3/mmc (194) mp-1187404 [hull=0.200, PRIMARY]
- papers: Effect of selenium on the thermoelectric properties of tellurium | Comprehensive study of tellurium based glass ceramics for thermoelectric application | Effects of Bi2Se3Amount in Thermoelectric Performance of Bi2(TeSe)3Materials Fabricated by High-Energy Ball Milling

## Ag-In-Se
- rank 399 | 17 samples | 5 papers | 12 compositions
- compositions: AgIn5Se8 (5); AgInSe2 (2); Ag0.95InZn0.05Se2 (1); Ag0.9InZn0.1Se2 (1); Ag0.975In0.975Zn0.05Se2 (1); Ag0.95In0.95Zn0.1Se2 (1)
- dopant candidates (<5% at.): Zn (5), Cd (2)
- seed hypothesis (confirm): chalcopyrite
- measured range: 298-908 K (5th-95th pct of 56 curves)
- [ref 1] TEDesignLab / ICSD: InAgSe2 I-42d (122) mp-20554 [hull=0.000, icsd=13, PRIMARY]; In5AgSe8 (111)
- [ref 2] MP, ranked by ICSD evidence: In5AgSe8 C2 (5) mp-1224092 [hull=0.003, PRIMARY]; In2AgSe4 I-4 (82) mp-1025331 [hull=0.090, PRIMARY]; InAgSe2 R-3m (166) mp-1007685 [hull=0.099, icsd=1]; InAgSe2 R3m (160) mp-1223807 [hull=0.071]; InAgSe2 I4_1/amd (141) mp-35071 [hull=0.111]
- papers: Microstructure modulation responsible for the improvement in thermoelectric property of a wide-gap AgIn5Se8 semiconductor | Site occupations of Zn in AgInSe2-based chalcopyrites responsible for modified structures and significantly improved thermoelectric performance | Modified structures and improved thermoelectric property in Ag-added polycrystalline In2Se3

## Al-As-Ga-In
- rank 400 | 17 samples | 7 papers | 10 compositions
- compositions: Er0.003InGa0.8Al0.2As (5); InGa0.8Al0.2AsEr0.0006 (3); (InGaAs)0.8(InAlAs)0.2(ErAs)0.006 (2); In0.53Ga0.27Al0.20As(ErAs)0.006 (1); Er0.006(In0.52Al0.48As)0.5(In0.53Ga0.47As)0.5 (1); (In0.52Al0.48As)0.5(In0.53Ga0.47As)0.5 (1)
- dopant candidates (<5% at.): Er (16)
- seed hypothesis (confirm): sphalerite
- solid-solution axis: Al/(Al+Ga) spans 0.20-0.51 (median 0.40) over 10 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 38-854 K (5th-95th pct of 35 curves)
- papers: Recent Developments in Semiconductor Thermoelectric Physics and Materials | Thermoelectric power generator module of 16×16 Bi2Te3 and 0.6% ErAs:(InGaAs)1−x(InAlAs)x segmented elements | High efficiency semimetal/semiconductor nanocomposite thermoelectric materials
