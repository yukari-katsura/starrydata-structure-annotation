# Host systems -- chunk 001 of 73

Ranks 1-50 by sample count. These 50 host systems cover 24447 samples (46.99% of the TE set); cumulative through this chunk: 46.99%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Co-Sb
- rank 1 | 1778 samples | 373 papers | 954 compositions
- compositions: CoSb3 (296); Co4Sb12 (32); Co4Sb11.5Te0.5 (23); Ba0.3In0.2Co3.95Ni0.05Sb12 (22); Yb0.2Co4Sb12 (21); Yb0.3Co4Sb12 (17)
- dopant candidates (<5% at.): Yb (374), In (322), Ba (264), Te (253), Ni (189), Fe (140), Ce (94), Sr (85), Ca (80), Ga (71), La (61), Se (49), Sn (47), Ge (42), O (42), Nd (38), Al (31), Pr (29), Eu (23), Ti (22), Pb (22), Pd (19), Tl (19), Ir (18), Bi (18), S (17), Ag (16), Y (16), C (13), Zr (13), Rh (12), Br (10), Li (9), Zn (9), Mn (7), As (7), N (7), Cr (6), Sm (6), Dy (6), Gd (6), Si (6), K (5), U (5), Cd (3), W (3), I (3), Mo (3), V (3), Pt (2), Lu (2), Cu (1), H (1), M0+ (1), Na (1), Ru (1)
- seed hypothesis (confirm): skutterudite, filled_skutterudite  <-- MIXED, split per composition
- measured range: 16-864 K (5th-95th pct of 6570 curves; full span incl. outliers 10-1125 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CoSb3 Im-3 (204) mp-1317 [hull=0.000, icsd=17, PRIMARY]; CoSb P6_3/mmc (194) mp-2644 [hull=0.000, icsd=12, PRIMARY]; CoSb2 P2_1/c (14) mp-755 [hull=0.003, icsd=6, PRIMARY]; Tl(CoSb3)16 C2/m (12) mp-1217147 [hull=0.007, PRIMARY]; CoSb2 Pnnm (58) mp-9835 [hull=0.012, icsd=3]
- papers: https://doi.org/10.1016/j.actamat.2009.03.018 (Enhanced thermoelectric performance of dual-element-filled skutterudit...) | https://doi.org/10.1016/j.actamat.2011.01.064 (Excellent performance stability of Ba and In double-filled skutterudit...) | https://doi.org/10.1016/j.actamat.2011.12.028 (Rattler-seeded InSb nanoinclusions from metastable indium-filled In0.1...)

## Ca-Co-O
- rank 2 | 1682 samples | 343 papers | 565 compositions
- compositions: Ca3Co4O9 (622); Ca3Co2O6 (29); Ca2.7Bi0.3Co4O9 (27); Ca2.9La0.1Co4O9 (22); (Ca2CoO3)0.62CoO2 (15); Ca3Co3.95Fe0.05O9 (15)
- dopant candidates (<5% at.): Ag (147), Bi (145), La (97), Fe (82), Cu (58), Lu (53), Na (48), Ga (47), Sr (39), Y (38), Mn (32), Ni (27), C (26), Yb (25), Ba (25), Ce (21), Dy (19), Tb (19), Pr (19), B (18), Ho (17), Cr (16), Gd (16), Ru (16), Er (14), Eu (11), Cd (10), Mo (10), Pb (9), Nb (9), Ti (8), Zn (8), K (8), Ir (8), Rh (7), W (7), Sb (6), Nd (5), N (5), Si (5), Zr (5), F (3), Al (2), Re (2), Pt (2), Sm (2), Ta (2)
- seed hypothesis (confirm): misfit_cobaltite, ca3co2o6_chain  <-- MIXED, split per composition
- measured range: 12-1167 K (5th-95th pct of 4235 curves; full span incl. outliers 10-1252 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca3(CoO3)2 R-3c (167) mp-18792 [hull=0.004, icsd=9, PRIMARY]; Ca2Co2O5 P2_1/m (11) mp-1195056 [hull=0.012, icsd=3, PRIMARY]; Ca2CoO3 C2/m (12) mp-31623 [hull=0.181, icsd=1, PRIMARY]; Ca12ScCo7O24 C2 (5) mp-1227689 [hull=0.011, PRIMARY]; Ca3Co4O9 Cmm2 (35) mp-1096877 [hull=0.028, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2014.04.008 (Post-calcination, a novel method to synthesize cobalt oxide-based ther...) | https://doi.org/10.1002/adem.200500043 (Nanostructured Complex Cobalt Oxides as Potential Materials for Solar ...) | https://doi.org/10.1179/1743676113y.0000000083 (Homogeneous precipitation synthesis and thermoelectric properties of C...)

## Bi-Sb-Te
- rank 3 | 1473 samples | 347 papers | 537 compositions
- compositions: Bi0.5Sb1.5Te3 (348); Bi0.4Sb1.6Te3 (164); Bi0.48Sb1.52Te3 (47); (Bi0.25Sb0.75)2Te3 (28); (Bi0.2Sb0.8)2Te3 (23); Bi0.45Sb1.55Te3 (19)
- dopant candidates (<5% at.): Cu (67), Se (64), C (54), O (42), Ag (41), Pb (37), Si (30), In (27), Zn (17), Fe (17), Sn (16), Ga (14), Al (13), N (13), Na (13), Co (11), Mo (9), Mn (9), S (9), Mg (8), P (7), Au (7), Ni (7), Ti (7), H (6), Cd (6), Ge (6), B (5), Ba (4), La (4), Tl (3), Ru (2), Nd (2), Tb (1), Pd (1), W (1), I (1), Ta (1), Y (1), Zr (1)
- seed hypothesis (confirm): tetradymite
- solid-solution axis: Bi/(Bi+Sb) spans 0.13-0.90 (median 0.25) over 537 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 27-580 K (5th-95th pct of 5424 curves; full span incl. outliers 10-1441 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi(SbTe2)3 R3m (160) mp-1227403 [hull=0.824, PRIMARY, AMBIGUOUS]; Bi2Sb2Te3 R-3m (166) mp-1227407 [hull=0.712, PRIMARY]; BiSbTe2 P3m1 (156) mp-1227463 [hull=0.688, PRIMARY]; BiSbTe3 R3m (160) mp-1227340 [hull=0.632, PRIMARY]; Bi(SbTe2)3 Cm (8) mp-1227414 [hull=0.825]
- papers: https://doi.org/10.1016/j.actamat.2010.09.054 (Influence of powder morphology on thermoelectric anisotropy of spark-p...) | https://doi.org/10.1016/j.actamat.2011.04.040 (Fabrication and thermoelectric properties of c-axis-aligned Bi0.5Sb1.5...) | https://doi.org/10.1016/j.actamat.2014.10.062 (Enhanced thermoelectric and mechanical properties of zone melted p-typ...)

## O-Sr-Ti
- rank 4 | 1338 samples | 190 papers | 453 compositions
- compositions: SrTiO3 (196); SrTi0.8Nb0.2O3 (66); Sr0.9La0.1TiO3 (29); Sr0.95La0.05TiO3 (29); La0.1Dy0.1Sr0.75TiO3 (25); Sr0.7La0.2TiO3 (23)
- dopant candidates (<5% at.): La (418), Nb (396), Dy (74), Nd (73), Y (67), Gd (54), Pr (50), Sm (33), Ca (32), Ta (24), Ce (22), Ni (22), Bi (21), N (14), Ag (11), Yb (10), Eu (10), C (9), B (6), Co (6), W (5), Ba (4), Zr (4), Ru (4), In (4), Sc (3), Er (2), Fe (2), Cu (1)
- seed hypothesis (confirm): perovskite
- measured range: 18-1174 K (5th-95th pct of 2722 curves; full span incl. outliers 10-1298 K)
- [ref 1] TEDesignLab / ICSD: SrTiO3 I4/mcm (140) mp-4651 [hull=0.000, icsd=37, PRIMARY, AMBIGUOUS]; Sr3Ti2O7 I4/mmm (139) mp-3349 [hull=0.000, icsd=3, PRIMARY]; Sr4Ti3O10 I4/mmm (139) mp-31213 [hull=0.000, icsd=1, PRIMARY]; SrTiO3 Pm-3m (221) mp-5229 [hull=0.001, icsd=34]; SrTiO3 (46)
- [ref 2] MP, ranked by ICSD evidence: Sr2TiO4 I4/mmm (139) mp-5532 [hull=0.000, icsd=9, PRIMARY]; Sr5Ti7O19 Pmmm (47) mp-1202132 [hull=0.093, icsd=1, PRIMARY]; Sr25Ti39O103 P2/m (10) mp-1198567 [hull=0.041, icsd=1, PRIMARY]; SrTiO3 P6_3/mmc (194) mp-776018 [hull=0.039]
- papers: https://doi.org/10.1007/s00339-014-8515-z (Semiconducting large bandgap oxides as potential thermoelectric materi...) | https://doi.org/10.1143/apex.1.015007 (Thermal Stability of Giant Thermoelectric Seebeck Coefficient for SrTi...) | https://doi.org/10.1063/1.2890493 (The influence of oxygen deficiency on the thermoelectric properties of...)

## Pb-Te
- rank 5 | 1261 samples | 239 papers | 733 compositions
- compositions: PbTe (161); AgPb18SbTe20 (24); Pb0.98Na0.02Te1 (15); Pb0.98Na0.02Te (14); PbTe(PbI2)0.00009 (10); Pb0.96Na0.04Te (9)
- dopant candidates (<5% at.): Na (346), Sb (295), I (194), Ag (188), Eu (73), Bi (66), In (64), Cd (57), Se (53), Mg (45), Sn (45), S (42), K (40), Sr (37), Ca (29), Ge (27), Mn (26), Si (23), La (22), Zn (16), Yb (15), Tl (13), Cr (11), Cu (11), Ba (10), Cl (8), Al (8), Ti (8), Sc (7), C (6), Sm (6), Ce (5), Hg (4), Y (4), O (1)
- seed hypothesis (confirm): rocksalt
- measured range: 175-902 K (5th-95th pct of 4243 curves; full span incl. outliers 10-1235 K)
- [ref 1] TEDesignLab / ICSD: TePb Fm-3m (225) mp-19717 [hull=0.000, icsd=50, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: TePb3 I4/mmm (139) mp-1187450 [hull=0.202, PRIMARY]; TePb Pm-3m (221) mp-20943 [hull=0.218, icsd=4]; TePb Pnma (62) mp-685022 [hull=0.058, icsd=2]; TePb Pmn2_1 (31) mp-1101143 [hull=0.077]; TePb3 P6_3/mmc (194) mp-1187534 [hull=0.243]
- papers: https://doi.org/10.1021/ar400290f (Decoupling Interrelated Parameters for Designing High Performance Ther...) | https://doi.org/10.1021/am405410e (Exploration of Zn Resonance Levels and Thermoelectric Properties in I-...) | https://doi.org/10.1021/nn305971v (Core–Shell Nanoparticles As Building Blocks for the Bottom-Up Producti...)

## O-Zn
- rank 6 | 1060 samples | 173 papers | 325 compositions
- compositions: ZnO (206); Zn0.98Al0.02O (113); Zn0.99Al0.01O (33); Al0.032ZnO (16); Al0.016ZnO (16); S0.025C0.010ZnO (15)
- dopant candidates (<5% at.): Al (470), Ga (127), Ni (75), In (53), C (48), S (40), Ti (37), Fe (33), Si (33), Co (30), Ta (19), Ag (18), Sn (15), Zr (15), Dy (14), Mn (14), Sb (12), Cu (12), Li (10), Gd (6), Bi (5), Mg (5), Sm (5), Ce (4), F (4), Nb (3), Au (3), Mo (3), Er (2), B (1), N (1), Na (1), Ir (1)
- seed hypothesis (confirm): wurtzite
- measured range: 27-1179 K (5th-95th pct of 1872 curves; full span incl. outliers 10-1302 K)
- [ref 1] TEDesignLab / ICSD: ZnO P6_3mc (186) mp-2133 [hull=0.000, icsd=69, PRIMARY]; ZnO2 Pa-3 (205) mp-8484 [hull=0.143, icsd=2, PRIMARY]; ZnO Fm-3m (225) mp-2229 [hull=0.146, icsd=15]; ZnO F-43m (216) mp-1986 [hull=0.007, icsd=5]
- [ref 2] MP, ranked by ICSD evidence: ZnO Pm-3m (221) mp-13161 [hull=0.716, icsd=2]; ZnO2 P2_12_12_1 (19) mp-1102744 [hull=0.177, icsd=2]; ZnO2 P-3m1 (164) mp-1094003 [hull=0.452, icsd=1]; ZnO2 Immm (71) mp-1178680 [hull=0.608, icsd=1]; ZnO P4_2/mnm (136) mp-1093993 [hull=0.023]
- papers: https://doi.org/10.1021/am509050a (Thermoelectric Transport Properties of Fe-Enriched ZnO with High-Tempe...) | https://doi.org/10.1016/j.actamat.2013.02.021 (Sintering and annealing effects on ZnO microstructure and thermoelectr...) | https://doi.org/10.1063/1.4842035 (Enhanced thermoelectric figure of merit in nanostructured ZnO by nanoj...)

## Ca-Mn-O
- rank 7 | 1052 samples | 142 papers | 386 compositions
- compositions: CaMnO3 (122); Ca0.9Yb0.1MnO3 (38); CaMn0.95Nb0.05O3 (20); Ca0.9La0.1MnO3 (18); CaMn0.98Nb0.02O3 (18); CaMn0.99W0.01O3 (15)
- dopant candidates (<5% at.): Nb (156), Yb (121), Dy (105), La (91), Pr (82), W (79), Bi (72), Sr (57), Sm (54), Gd (47), Ta (35), Y (34), Mo (31), Ce (25), V (21), Ag (20), Nd (18), Lu (13), Zn (10), Fe (9), Er (8), Ho (7), Si (7), Eu (6), K (6), Cu (5), Tb (4), Na (4), Ru (4), Re (3), Sn (3), Pd (2), C (2), Ti (2), Ge (2), Tm (1)
- seed hypothesis (confirm): perovskite
- measured range: 22-1175 K (5th-95th pct of 2320 curves; full span incl. outliers 10-1474 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaMnO3 Pnma (62) mp-19201 [hull=0.034, icsd=30, PRIMARY]; Ca2MnO4 I4_1/acd (142) mp-19050 [hull=0.010, icsd=10, PRIMARY]; CaMn7O12 R-3 (148) mp-1105355 [hull=0.019, icsd=6, PRIMARY]; CaMn2O4 Pbcm (57) mp-18844 [hull=0.000, icsd=5, PRIMARY]; Ca3Mn2O7 I4/mmm (139) mp-19124 [hull=0.058, icsd=4, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2009.07.062 (High-temperature stability, structure and thermoelectric properties of...) | https://doi.org/10.1063/1.3477959 (Enhancement of thermoelectric efficiency in (Ca,Dy)MnO3–(Ca,Yb)MnO3 so...) | https://doi.org/10.1016/j.ceramint.2009.11.004 (Thermoelectric properties of layered Ca3.95RE0.05Mn3O10 compounds (RE=...)

## Bi-Te
- rank 8 | 955 samples | 324 papers | 292 compositions
- compositions: Bi2Te3 (446); Bi2Te2.85Se0.15 (30); BiTe (12); Bi0.46Te0.54 (10); Bi2Te2.8Se0.2 (10); Bi2Te2.82Se0.18 (9)
- dopant candidates (<5% at.): Se (198), Cu (49), Sb (42), Ga (31), I (26), S (22), Ag (16), Si (16), C (15), Ge (12), Sn (11), Cr (10), In (10), Cl (10), Ni (8), Pb (6), Fe (5), Mn (5), Lu (5), Ce (4), Br (4), O (4), Al (3), Y (3), Ru (3), Sm (2), Tl (2), Au (2), Pt (2), K (2), Er (1), Zn (1), Li (1)
- seed hypothesis (confirm): tetradymite
- measured range: 23-600 K (5th-95th pct of 3039 curves; full span incl. outliers 10-1173 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi2Te3 R-3m (166) mp-34202 [hull=0.000, icsd=23, PRIMARY]; BiTe P-3m1 (164) mp-23224 [hull=0.002, icsd=4, PRIMARY]; Bi2Te I-42d (122) mp-1227413 [hull=0.267, PRIMARY]; Bi4Te3 R-3m (166) mp-28229 [hull=0.002, PRIMARY]; Bi8Te7 P-3m1 (164) mp-1214397 [hull=0.182, PRIMARY]
- papers: https://doi.org/10.1021/am3002764 (Significant Enhancement in the Thermoelectric Performance of a Bismuth...) | https://doi.org/10.1021/am401444w (Wet-Chemical Synthesis and Consolidation of Stoichiometric Bismuth Tel...) | https://doi.org/10.1021/acsami.5b07596 (Enhanced Thermoelectric Performance of Nanostructured Bi2Te3through Si...)

## Bi-Cu-O-Se
- rank 9 | 749 samples | 84 papers | 245 compositions
- compositions: BiCuSeO (155); Bi0.96Pb0.04CuSeO (21); Bi0.94Pb0.06CuSeO (19); Bi0.875Ba0.125CuSeO (19); Bi0.9Sr0.1CuSeO (12); Bi0.92Pb0.08CuSeO (11)
- dopant candidates (<5% at.): Pb (197), Ca (49), Zn (48), Ba (35), Na (33), Ni (29), Ag (28), Al (25), Sr (23), Cd (15), Cl (15), Mg (12), Te (12), Br (12), La (10), In (10), Li (10), Fe (9), Sm (8), S (7), Mn (6), F (5), Yb (5), Sb (5), K (5), Eu (3), Ce (1), Ti (1), Zr (1)
- seed hypothesis (confirm): zrcusias_1111
- solid-solution axis: O/(O+Se) spans 0.10-0.65 (median 0.50) over 245 compositions
     CHECK: same periodic group, but oxygen often occupies its own sublattice (BiCuSeO, LaFeAsO) rather than substituting for the heavier chalcogen. Confirm the two share a site before treating this as a substitution axis.
- measured range: 52-931 K (5th-95th pct of 1994 curves; full span incl. outliers 10-975 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuBiSeO P4/nmm (129) mp-23116 [hull=0.000, icsd=4, PRIMARY]; CuBi2Se3O11 Aem2 (39) mp-1202656 [hull=0.110, icsd=1, PRIMARY]; CuBi2Se2O P4/mmm (123) mp-1213034 [hull=0.572, PRIMARY]; CuBiSeO Pmm2 (25) mp-1232038 [hull=0.351]
- papers: https://doi.org/10.1002/adma.201301675 (Enhanced Thermoelectric Properties of Pb-doped BiCuSeO Ceramics) | https://doi.org/10.1063/1.4799643 (Doping for higher thermoelectric properties in p-type BiCuSeO oxyselenide) | https://doi.org/10.1063/1.4894258 (Enhanced low temperature thermoelectric performance of Ag-doped BiCuSeO)

## Bi-Se-Te
- rank 10 | 634 samples | 144 papers | 291 compositions
- compositions: Bi2Te2.7Se0.3 (132); Bi2Te2.4Se0.6 (44); Cu0.01Bi2Te2.7Se0.3 (20); Bi2Te2Se (13); Bi2Te2.1Se0.9 (11); Bi2Te2.2Se0.8 (10)
- dopant candidates (<5% at.): Cu (88), I (54), Sb (28), Ag (24), B (20), In (19), O (15), S (15), Mg (15), C (14), Gd (10), Si (10), Sn (9), Ga (8), Mn (8), Ni (8), Al (7), Cl (7), W (7), Au (6), Fe (5), Lu (5), Y (4), Zn (4), Ba (4), Ce (3), Na (3), Li (3), Nb (3), H (2), N (2), Sm (1), Cd (1), Ge (1), Br (1), Co (1)
- seed hypothesis (confirm): tetradymite
- solid-solution axis: Se/(Se+Te) spans 0.08-0.90 (median 0.10) over 291 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 25-610 K (5th-95th pct of 2450 curves; full span incl. outliers 10-1334 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi2Te2Se R-3m (166) mp-29666 [hull=0.000, icsd=1, PRIMARY]; Bi2TeSe2 R-3m (166) mp-31406 [hull=0.037, icsd=1, PRIMARY]; Bi4(TeSe)3 Cm (8) mp-1227439 [hull=0.106, PRIMARY, AMBIGUOUS]; Bi2TeSe2 R3m (160) mp-1227356 [hull=0.073]; Bi4(TeSe)3 R3m (160) mp-1227438 [hull=0.106]
- papers: https://doi.org/10.1021/am405035z (Investigation of Reaction Mechanisms of Bismuth Tellurium Selenide Nan...) | https://doi.org/10.1021/nn507250r (Synthesis of Multishell Nanoplates by Consecutive Epitaxial Growth of ...) | https://doi.org/10.1016/j.actamat.2012.05.008 (Improving thermoelectric properties of n-type bismuth–telluride-based ...)

## Sn-Te
- rank 11 | 634 samples | 108 papers | 438 compositions
- compositions: SnTe (101); Sn1.03Te (10); AgSn18SbTe20 (9); Sn0.91Mn0.09Te (4); Sn1Te1 (4); (SnTe)16(AgBiTe2) (3)
- dopant candidates (<5% at.): In (133), Ag (102), Bi (80), Mn (72), Sb (70), Cd (63), Cu (54), Se (43), I (26), Mg (24), Zn (23), S (18), Na (11), Ca (11), O (11), Ge (10), Ti (9), V (8), Sr (7), Ga (7), Pb (6), Hg (6), Zr (6), Gd (5), La (4), Y (4), Pr (3), Cl (3), C (3), Zd0+ (2)
- seed hypothesis (confirm): rocksalt
- measured range: 293-913 K (5th-95th pct of 2741 curves; full span incl. outliers 10-1909 K)
- [ref 1] TEDesignLab / ICSD: SnTe F-43m (216) mp-16364 [hull=0.252, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: SnTe Fm-3m (225) mp-1883 [hull=0.000, icsd=23, PRIMARY]; Sn3Te I4/mmm (139) mp-1187080 [hull=0.206, PRIMARY]; SnTe3 Fm-3m (225) mp-978885 [hull=0.304, PRIMARY]; SnTe Pm-3m (221) mp-1481 [hull=0.240, icsd=2]; Sn3Te Pm-3m (221) mp-1187067 [hull=0.221]
- papers: https://doi.org/10.1016/j.actamat.2012.02.034 (Microstructure and thermoelectric properties of CoSb2.75Ge0.25−xTex pr...) | https://doi.org/10.1002/aenm.201100613 (Lead-Free Thermoelectrics: High Figure of Merit in p-type AgSnmSbTem+2) | https://doi.org/10.1002/aenm.201200083 (Increase in the Figure of Merit by Cd-Substitution in Sn1-xPbxTe and E...)

## Sb-Zn
- rank 12 | 537 samples | 131 papers | 252 compositions
- compositions: Zn4Sb3 (192); ZnSb (45); Zn3.96Mg0.04Sb3 (8); Zn4.08Sb3 (4); Zn0.97Cd0.03Sb (4); ZnSbCu0.001 (4)
- dopant candidates (<5% at.): Cu (53), In (37), Cd (21), Mg (21), P (21), Bi (15), Pb (15), Te (12), Ag (11), Ge (10), Se (7), Sn (6), Si (6), Mn (4), Sm (3), Ga (3), Fe (3), Pr (3), C (3), O (3), Gd (3), I (3), Co (3), Al (2), Cr (2), Hg (1)
- seed hypothesis (confirm): zn4sb3, znsb_cdsb  <-- MIXED, split per composition
- measured range: 12-714 K (5th-95th pct of 1832 curves; full span incl. outliers 10-763 K)
- [ref 1] TEDesignLab / ICSD: ZnSb Pbca (61) mp-753 [hull=0.000, icsd=5, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Zn6Sb5 R-3c (167) mp-1191566 [hull=0.028, icsd=2, PRIMARY]; ZnSb2 P-4n2 (118) mp-1077536 [hull=0.145, icsd=1, PRIMARY]; Zn3Sb I4/mmm (139) mp-971966 [hull=0.182, PRIMARY]; ZnSb3 Fm-3m (225) mp-971763 [hull=0.283, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2011.04.023 (Enhancement of the thermoelectric performance of β-Zn4Sb3 by in situ n...) | https://doi.org/10.1063/1.1689396 (Application of the compatibility factor to the design of segmented and...) | https://doi.org/10.1063/1.2404612 (Influence of sample compaction on the thermoelectric performance of Zn...)

## Mg-Si-Sn
- rank 13 | 522 samples | 94 papers | 304 compositions
- compositions: Mg2Si0.4Sn0.6 (68); Mg2Si0.6Sn0.4 (32); Mg2Si0.5Sn0.5 (20); Mg2Si0.8Sn0.2 (14); Mg2Si0.7Sn0.3 (13); Mg2.16(Si0.3Sn0.7)0.98Sb0.02 (9)
- dopant candidates (<5% at.): Sb (195), Bi (66), Ge (44), As (16), Li (15), O (14), Ti (11), Al (8), Zn (7), Ag (6), Ga (5), Co (5), La (5), Na (4), C (4), Pr (3), Cr (1)
- seed hypothesis (confirm): antifluorite
- solid-solution axis: Si/(Si+Sn) spans 0.20-0.82 (median 0.44) over 304 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 288-857 K (5th-95th pct of 1788 curves; full span incl. outliers 10-991 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg14SiSn P-6m2 (187) mp-1028270 [hull=0.051, PRIMARY]; Mg4SiSn R-3m (166) mp-1222116 [hull=0.032, PRIMARY]; Mg6SiSn Amm2 (38) mp-1021421 [hull=0.127, PRIMARY]; Mg6SiSn2 Immm (71) mp-1222095 [hull=0.017, PRIMARY]; Mg14SiSn Amm2 (38) mp-1028295 [hull=0.073]
- papers: https://doi.org/10.1016/j.actamat.2014.04.060 (Thermoelectric properties of highly efficient Bi-doped Mg2Si1−x−ySnxGe...) | https://doi.org/10.1016/j.actamat.2015.05.010 (Effect of microstructure on the thermal conductivity of nanostructured...) | https://doi.org/10.1002/aenm.201300174 (Low Electron Scattering Potentials in High Performance Mg2Si0.45Sn0.55...)

## Ba-Cu-O-Y
- rank 14 | 484 samples | 82 papers | 126 compositions
- compositions: YBa2Cu3O7 (237); YBa2Cu3O6.7 (12); YBa2Cu3O6.9 (8); YBa2Cu3O6.95 (8); Y0.9Ca0.1Ba2Cu3O7 (7); YBa2Cu3O6.94 (6)
- dopant candidates (<5% at.): Ca (49), Pr (25), Zn (14), Mn (13), La (13), Li (8), Co (7), Fe (7), Sr (6), Se (4), Ag (4), Cr (4), Ti (4), Cd (3), S (3), K (2), Nd (1), Sm (1)
- seed hypothesis (confirm): ybco_cuprate
- measured range: 13-1177 K (5th-95th pct of 544 curves; full span incl. outliers 10-1249 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2YCu3O7 Pmmm (47) mp-20674 [hull=0.023, icsd=47, PRIMARY]; Ba2Y(CuO2)4 Cmmm (65) mp-6790 [hull=0.000, icsd=32, PRIMARY]; Ba2Y(CuO2)3 P4/mmm (123) mp-22215 [hull=0.002, icsd=11, PRIMARY]; Ba4Y2Cu6O13 Pmmm (47) mp-20897 [hull=0.012, icsd=8, PRIMARY]; Ba2Y(Cu2O3)2 Cmmm (65) mp-643471 [hull=0.251, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.4754707 (Thermoelectric properties of YBa2Cu3O7−δ–La2/3Ca1/3MnO3 superlattices) | https://doi.org/10.1016/j.jallcom.2013.09.045 (Investigation of thermoelectric power with modification of two band mo...) | https://doi.org/10.1016/j.jmatprotec.2007.12.078 (A study on the thermoelectric power and thermal conductivity propertie...)

## Mg-Si
- rank 15 | 453 samples | 111 papers | 228 compositions
- compositions: Mg2Si (115); Mg2Si0.9875Sb0.0125 (19); Mg2Si0.98Ag0.02 (17); Mg2Si0.98Bi0.02 (7); Mg2Si0.98Sb0.02 (6); Mg2Si0.993Bi0.007 (6)
- dopant candidates (<5% at.): Sb (108), Bi (77), Al (55), Ag (25), Sn (14), O (11), B (10), Zn (10), Ti (8), Te (7), Li (7), Pb (5), P (5), Ca (5), Ge (5), Na (4), Y (4), Se (3), Cu (3), Sr (3), Ga (2), Zr (2), Nd (1), Co (1), Sm (1), Ta (1), Ni (1), Mn (1), In (1)
- seed hypothesis (confirm): antifluorite
- measured range: 288-879 K (5th-95th pct of 1578 curves; full span incl. outliers 10-1204 K)
- [ref 1] TEDesignLab / ICSD: Mg2Si Fm-3m (225) mp-1367 [hull=0.018, icsd=17, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Mg5Si6 C2/m (12) mp-1075430 [hull=0.171, icsd=1, PRIMARY]; Mg15Si P-6m2 (187) mp-1023509 [hull=0.051, PRIMARY]; Mg149Si P-6m2 (187) mp-1185634 [hull=0.000, PRIMARY]; Mg3Si Pmm2 (25) mp-1016216 [hull=0.152, PRIMARY]; Mg2Si3 P1 (1) mp-1073164 [hull=0.155, PRIMARY, AMBIGUOUS]
- papers: https://doi.org/10.1016/j.actamat.2014.04.007 (Simultaneous enhancement of mechanical and thermoelectric properties o...) | https://doi.org/10.1016/j.actamat.2014.05.041 (Microstructural effects on thermoelectric efficiency: A case study on ...) | https://doi.org/10.1063/1.4816802 (Conducting grain boundaries enhancing thermoelectric performance in do...)

## Ge-Te
- rank 16 | 450 samples | 94 papers | 258 compositions
- compositions: GeTe (73); Ge20Te80 (9); Ge0.95Bi0.05Te1.025 (8); (GeTe)90(AgSbTe2)10 (7); (GeTe)0.95(Bi2Te3)0.05 (7); (GeTe)19Sb2Te3 (6)
- dopant candidates (<5% at.): Bi (125), Sb (96), Ti (23), Cu (22), Se (21), In (18), Ag (17), Pb (17), Mn (15), I (15), Co (14), Cd (14), Sn (12), Al (12), Cr (7), Ta (7), Y (6), Si (5), C (5), S (5), Ga (5), Fe (4), Br (4), Yb (3), Ba (3), V (2), Li (1), Dy (1)
- seed hypothesis (confirm): gete_rhombohedral
- measured range: 297-821 K (5th-95th pct of 1874 curves; full span incl. outliers 10-884 K)
  !! MEASUREMENT CROSSES A TRANSITION: gete_rhombohedral -> rocksalt at ~700 K (R3m -> Fm-3m, ~700 K; shifts with Ge vacancy content and doping.)
     Record each phase with its own temperature range, not a single prototype.
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GeTe Fm-3m (225) mp-2612 [hull=0.016, icsd=16, PRIMARY]; Ge3Te I4/mmm (139) mp-976053 [hull=0.401, PRIMARY]; GeTe R3m (160) mp-938 [hull=0.000, icsd=12]; GeTe Pnma (62) mp-1080459 [hull=0.053, icsd=1]; GeTe Pbcn (60) mp-628781 [hull=0.111, icsd=1]
- papers: https://doi.org/10.1515/amm-2015-0104 (Microstructure And Thermoelectric Properties Of Tags-90 Compounds Fabr...) | https://doi.org/10.1021/cm902009t (High Thermoelectric Figure of Merit and Nanostructuring in Bulkp-type ...) | https://doi.org/10.1021/cm201717z (Real Structure and Thermoelectric Properties of GeTe-Rich Germanium An...)

## Co-Fe-Sb
- rank 17 | 408 samples | 99 papers | 265 compositions
- compositions: Pr0.02856Nd0.57144Fe3CoSb12 (52); La0.4FeCo3Sb12 (20); Ce0.6Fe2Co2Sb12 (10); La0.75Fe3CoSb12 (7); La0.8Ti0.1Ga0.1Fe3CoSb12 (7); (Pr0.0487Nd0.9513)0.44Fe2Co2Sb12 (7)
- dopant candidates (<5% at.): Nd (105), Pr (97), La (96), Ce (76), Yb (71), Ba (36), Ca (24), Sn (17), Ti (15), Ga (15), In (15), Tl (13), Sm (13), Dy (7), Ge (7), Se (6), Si (5), Gd (5), Pb (3), Te (3), U (3)
- seed hypothesis (confirm): skutterudite
- measured range: 119-863 K (5th-95th pct of 1461 curves; full span incl. outliers 10-889 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeCoSb4 P2/m (10) mp-1224950 [hull=0.029, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2013.07.052 (Dependence of thermoelectric behaviour on severe plastic deformation p...) | https://doi.org/10.1016/j.actamat.2013.09.006 (Realization of high thermoelectric performance in p-type unfilled tern...) | https://doi.org/10.1016/j.actamat.2015.07.027 (Enhanced thermoelectric performance of p-type filled skutterudites via...)

## Al-Fe-V
- rank 18 | 400 samples | 66 papers | 232 compositions
- compositions: Fe2VAl (56); Fe2VAl0.9Si0.1 (21); Fe2V0.9Ti0.1Al (17); Fe1.95V1.05Al (7); Fe2(V0.9Ti0.1)Al (6); Fe2V1.05Al0.95 (5)
- dopant candidates (<5% at.): Si (83), Ti (64), Ta (32), W (14), Sb (13), Co (13), Nb (7), Sn (6), Mo (6), Bi (4), Ir (4), Ge (4), Ga (2), Cr (1), Ce (1), Dy (1), Sm (1)
- seed hypothesis (confirm): full_heusler
- measured range: 11-978 K (5th-95th pct of 930 curves; full span incl. outliers 10-1275 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlVFe2 Fm-3m (225) mp-5778 [hull=0.000, icsd=3, PRIMARY]; AlV2Fe Cmm2 (35) mp-1228827 [hull=0.147, PRIMARY]; AlVFe2 P4/mmm (123) mp-1228816 [hull=0.047]; AlVFe2 F-43m (216) mp-1228804 [hull=0.290]
- papers: https://doi.org/10.2497/jjspm.57.207 (Off-stoichiometric Effects on Thermoelectric Properties of Fe2VAl-base...) | https://doi.org/10.1016/s0925-8388(02)00919-2 (High temperature thermoelectric properties of (Fe1−xVx)3Al Heusler typ...) | https://doi.org/10.1016/j.jallcom.2004.01.035 (Thermoelectric properties of Fe2TiAl Heusler alloys)

## Cu-La-O
- rank 19 | 397 samples | 79 papers | 205 compositions
- compositions: La2CuO4 (71); La1.85Sr0.15CuO4 (17); La1.92Ba0.08CuO4 (8); La1.875Ba0.125CuO4 (8); La1.8Sr0.2CuO4 (7); La1.85Y0.15CuO4 (5)
- dopant candidates (<5% at.): Sr (202), Ba (38), Mn (19), Ce (17), Mg (13), Eu (13), Ag (10), Gd (10), Zn (10), Ru (10), Co (9), Nd (9), Pr (8), Ti (8), Y (7), Fe (5), Ca (5), Ga (4), Al (3), Nb (2), Cr (2), Ni (2)
- seed hypothesis (confirm): ruddlesden_popper
- measured range: 10-973 K (5th-95th pct of 445 curves; full span incl. outliers 10-1279 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2CuO4 Cmce (64) mp-36480 [hull=0.057, icsd=33, PRIMARY]; La2Cu2O5 Pbam (55) mp-5696 [hull=0.052, icsd=5, PRIMARY]; La8Cu7O19 C2/c (15) mp-1181551 [hull=0.066, icsd=2, PRIMARY]; LaCuO3 R-3c (167) mp-3474 [hull=0.000, icsd=2, PRIMARY]; LaCuO2 R-3m (166) mp-20072 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1002/ecj.10003 (Thermoelectric properties of RE2−xMxCuO4oxide sintering bulks) | https://doi.org/10.1088/0953-8984/10/39/019 (Thermoelectric power of the system) | https://doi.org/10.1111/j.1551-2916.2009.02952.x (High-Temperature Thermoelectric Properties in the La2−xRxCuO4(R: Pr, Y...)

## La-Mn-O
- rank 20 | 377 samples | 95 papers | 173 compositions
- compositions: La0.8Sr0.2MnO3 (37); LaMnO3 (16); La0.9Na0.1MnO3 (14); La0.9Sr0.1MnO3 (13); La0.8Na0.2MnO3 (7); La0.975Na0.025MnO3 (7)
- dopant candidates (<5% at.): Sr (139), Ca (82), Na (59), K (32), Ag (30), Te (29), Cr (20), Bi (16), Sb (12), Pb (11), Mg (9), Li (8), Ba (8), Zr (8), Mo (6), Cu (5), V (5), Pr (4), Ga (4), Al (4), Zn (4), Ce (3), Fe (3), Sc (3), Sn (3), Er (2), Co (1), Dy (1), Eu (1), Rb (1)
- seed hypothesis (confirm): perovskite
- measured range: 10-984 K (5th-95th pct of 459 curves; full span incl. outliers 10-1479 K)
- [ref 1] TEDesignLab / ICSD: LaMn7O12 C2/m (12) mp-1189182 [hull=0.016, icsd=3, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: LaMnO3 R-3c (167) mp-19168 [hull=0.012, icsd=29, PRIMARY]; LaMn2O5 Pbam (55) mp-25694 [hull=0.000, icsd=2, PRIMARY]; La11Mn12O36 P2_1/m (11) mp-690363 [hull=0.011, PRIMARY, AMBIGUOUS]; La10Mn9O30 P-1 (2) mp-698607 [hull=0.008, PRIMARY]; La14Mn15O48 P-1 (2) mp-705798 [hull=0.028, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2013.01.201 (Magnetic, electric and thermoelectric behavior of electron-doped La1−x...) | https://doi.org/10.1063/1.4804937 (Cross-plane thermoelectric transport in p-type La0.67Sr0.33MnO3/LaMnO3...) | https://doi.org/10.1016/j.jmmm.2015.06.053 (Investigation on magnetic, electrical and thermoelectric power of Bi-s...)

## C
- rank 21 | 369 samples | 78 papers | 21 compositions
- compositions: C (333); B0.04C (13); Rb3C60 (3); K3C60 (2); B0.0005C (2); B0.001C (1)
- dopant candidates (<5% at.): B (19), Te (6), Bi (6), Rb (3), K (2), Ti (2), Si (1), W (1), V (1), Zr (1)
- seed hypothesis (confirm): graphite_layered, fulleride_a3c60  <-- MIXED, split per composition
- measured range: 11-1175 K (5th-95th pct of 643 curves; full span incl. outliers 10-1794 K)
- [ref 1] TEDesignLab / ICSD: C Fd-3m (227) mp-66 [hull=0.134, icsd=29, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: BaC20 Pm-3n (223) mp-28979 [hull=0.230, icsd=1, PRIMARY]; KC60 Pnnm (58) mp-29687 [hull=0.360, icsd=1, PRIMARY]; SrC20 Pm-3 (200) mp-28905 [hull=0.265, icsd=1, PRIMARY]; KBaC20 Imm2 (44) mp-1223585 [hull=0.234, PRIMARY]; C P6_3/mmc (194) mp-48 [hull=0.000, icsd=9]
- papers: https://doi.org/10.1063/1.2909150 (Configurational, electronic entropies and the thermoelectric propertie...) | https://doi.org/10.1063/1.3264087 (Disorder enhances thermoelectric figure of merit in armchair graphane ...) | https://doi.org/10.1063/1.4883892 (Thermoelectric properties of nanoporous three-dimensional graphene net...)

## O-Ti
- rank 22 | 367 samples | 86 papers | 121 compositions
- compositions: TiO2 (119); TiO (31); Ti2O3 (26); Sr0.1Ti0.9O3 (13); TiIn0.004O2 (9); Ti4O7 (9)
- dopant candidates (<5% at.): Nb (26), Sr (23), N (10), La (10), In (9), Ag (7), V (7), Fe (7), Al (6), Ta (6), Ir (6), Ca (5), Ba (5), Pb (5), Mg (3), Co (3), Cu (2), Cr (1), W (1)
- seed hypothesis (confirm): rutile, anatase, magneli_phase  <-- MIXED, split per composition
- measured range: 13-1076 K (5th-95th pct of 704 curves; full span incl. outliers 10-1274 K)
- [ref 1] TEDesignLab / ICSD: TiO2 P4_2/mnm (136) mp-2657 [hull=0.037, icsd=131, PRIMARY]; Ti2O3 R-3c (167) mp-458 [hull=0.000, icsd=20, PRIMARY]; TiO2 I4_1/amd (141) mp-390 [hull=0.006, icsd=38]; TiO2 Pbca (61) mp-1840 [hull=0.020, icsd=14]; TiO2 Pbcn (60) mp-1439 [hull=0.031, icsd=7]
- [ref 2] MP, ranked by ICSD evidence: TiO Fm-3m (225) mp-2664 [hull=0.271, icsd=10, PRIMARY]; Ti4O7 P-1 (2) mp-12205 [hull=0.006, icsd=9, PRIMARY]; Ti3O5 C2/m (12) mp-1147 [hull=0.000, icsd=3, PRIMARY]; Ti6O11 P-1 (2) mp-30524 [hull=0.011, icsd=3, PRIMARY]; TiO C2/m (12) mp-1203 [hull=0.043, icsd=2]
- papers: https://doi.org/10.1002/adem.201400183 (Manufacture and Testing of Thermoelectric Modules Consisting of BxC an...) | https://doi.org/10.1007/s00339-014-8515-z (Semiconducting large bandgap oxides as potential thermoelectric materi...) | https://doi.org/10.1063/1.2767775 (Thermoelectric property studies on bulk TiOx with x from 1 to 2)

## Pb-Se
- rank 23 | 353 samples | 56 papers | 236 compositions
- compositions: PbSe (46); Pb0.97Sm0.03Se (6); Pb0.91Sm0.09Se (6); Pb0.94Sm0.06Se (6); Ag0.85Pb18SbSe20 (5); Pb1Se1 (4)
- dopant candidates (<5% at.): Sb (75), Na (41), Ag (35), Cl (27), In (25), Al (20), Sm (18), Cu (18), Bi (14), Te (13), Ga (13), Sr (11), S (11), Br (11), Mg (10), Sn (7), Nb (5), Ba (5), Ca (5), K (5), Ni (5), Hg (5), B (3), Tl (3), Mn (3), Yb (2), Zn (1)
- seed hypothesis (confirm): rocksalt
- measured range: 90-926 K (5th-95th pct of 1282 curves; full span incl. outliers 11-990 K)
- [ref 1] TEDesignLab / ICSD: PbSe Fm-3m (225) mp-2201 [hull=0.000, icsd=34, PRIMARY]; PbSe Fmm2 (42) mp-22009 [hull=0.075, icsd=1]; PbSe Pnma (62) mp-1079172 [hull=0.076, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: PbSe2 I4/mcm (140) mp-982261 [hull=0.054, icsd=1, PRIMARY]; PbSe Cmcm (63) mp-1063670 [hull=0.052, icsd=2]; PbSe Pm-3m (221) mp-21214 [hull=0.239, icsd=1]
- papers: https://doi.org/10.1039/c4ce00714j (PbSe hierarchical nanostructures: solvothermal synthesis, growth mecha...) | https://doi.org/10.1039/c3ee43438a (Tuning bands of PbSe for better thermoelectric efficiency) | https://doi.org/10.1134/s2075113311050224 (Thermoelectric materials with low heat conductivity based on PbSe-Bi2S...)

## Co-Na-O
- rank 24 | 342 samples | 88 papers | 154 compositions
- compositions: NaCo2O4 (44); Na0.7CoO2 (23); Na0.75CoO2 (15); NaCoO2 (9); Na1.6Co2O4 (8); Na1.1Co2O4 (7)
- dopant candidates (<5% at.): Ag (41), Ni (34), Cu (17), Zn (10), Mn (9), Fe (6), Dy (5), Yb (4), Pb (4), Bi (4), Pd (4), Sm (2), Ru (2), B (1), Au (1), K (1), Rb (1), W (1), Sc (1), Cr (1), Mo (1), Ti (1), Rh (1)
- seed hypothesis (confirm): naxcoo2_layered
- measured range: 13-1100 K (5th-95th pct of 754 curves; full span incl. outliers 10-1441 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Na10Co4O9 P-1 (2) mp-616702 [hull=0.000, icsd=3, PRIMARY]; Na4(CoO2)7 P6_3/m (176) mp-18846 [hull=0.000, icsd=3, PRIMARY]; NaCoO2 R-3m (166) mp-18921 [hull=0.000, icsd=2, PRIMARY]; Na4CoO3 Cc (9) mp-18762 [hull=0.000, icsd=2, PRIMARY]; Na7(CoO3)2 C2/c (15) mp-19427 [hull=0.009, icsd=2, PRIMARY]
- papers: https://doi.org/10.1007/s00339-015-9089-0 (Magnetic and thermoelectric properties of B-substituted NaCoO2) | https://doi.org/10.1143/apex.4.065201 (Exfoliation Route to Nanostructured Cobalt Oxide with Enhanced Thermoe...) | https://doi.org/10.1063/1.1634371 (Enhanced thermoelectric properties of NaxCoO2 whisker crystals)

## Fe-Si
- rank 25 | 331 samples | 50 papers | 155 compositions
- compositions: FeSi2 (67); (FeSi2)0.75(Si0.8Ge0.2)0.25 (14); Fe0.98Co0.02Si2 (12); Fe0.95Co0.05Si2 (10); FeSi (7); Fe28.91Co0.59Si70.5 (6)
- dopant candidates (<5% at.): Co (97), Mn (47), Al (31), Ge (18), Cu (16), Cr (15), Zr (6), C (6), Ti (5), Os (4), Ir (4), O (4), Ru (4), Nb (2), Er (2), B (1), Sm (1), P (1)
- seed hypothesis (confirm): b20_fesi, beta_fesi2  <-- MIXED, split per composition
- measured range: 16-1170 K (5th-95th pct of 854 curves)
- [ref 1] TEDesignLab / ICSD: FeSi P2_13 (198) mp-871 [hull=0.000, icsd=19, PRIMARY]; FeSi2 Cmce (64) mp-1714 [hull=0.000, icsd=8, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Fe5Si3 P6_3/mcm (193) mp-449 [hull=0.034, icsd=21, PRIMARY]; Fe3Si Fm-3m (225) mp-910968 [hull=0.000, icsd=14, PRIMARY]; Fe2Si P-3m1 (164) mp-22787 [hull=0.007, icsd=2, PRIMARY]; Fe11Si5 Pm-3m (221) mp-19800 [hull=0.020, icsd=1, PRIMARY]; FeSi2 P4/mmm (123) mp-20738 [hull=0.060, icsd=6]
- papers: https://doi.org/10.1007/s00339-004-2596-z (Thermoelectric properties of Mn doped FeSix alloys hot-pressed from ni...) | https://doi.org/10.2497/jjspm.53.523 (Low Temperature Synthesis and Thermoelectric Properties of &beta;-FeSi...) | https://doi.org/10.2497/jjspm.57.247 (Metal Doping Effects on the Conduction Type and the Thermoelectric Pro...)

## Co-La-O
- rank 26 | 327 samples | 71 papers | 134 compositions
- compositions: LaCoO3 (64); La0.9Sr0.1CoO3 (18); La0.8Sr0.2CoO3 (14); La0.95Sr0.05CoO3 (9); LaCo0.9Ni0.1O3 (8); La0.8Ca0.2CoO3 (6)
- dopant candidates (<5% at.): Sr (104), Ni (32), Ca (22), Ba (19), Li (16), Te (14), Mn (12), Cu (11), Ti (10), Rh (8), Nb (5), B (4), Na (4), Fe (4), Ga (3), Eu (3), Mg (3), V (3), Ce (2), Cr (2), Sb (2), Pb (1)
- seed hypothesis (confirm): perovskite
- measured range: 14-1269 K (5th-95th pct of 547 curves; full span incl. outliers 10-1375 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaCoO3 R-3c (167) mp-19051 [hull=0.000, icsd=14, PRIMARY]; La4Co3O10 I4/mmm (139) mp-19196 [hull=0.060, icsd=3, PRIMARY]; La4(CoO3)3 Pnma (62) mp-622353 [hull=0.056, icsd=1, PRIMARY]; La2Co2O5 Pnma (62) mp-1199457 [hull=0.057, icsd=1, PRIMARY]; La(CoO)3 Cmmm (65) mp-1207333 [hull=0.795, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2007.05.020 (High-temperature thermoelectric properties of Ln(Co, Ni)O3 (Ln=La, Pr,...) | https://doi.org/10.1002/adem.200500043 (Nanostructured Complex Cobalt Oxides as Potential Materials for Solar ...) | https://doi.org/10.1016/j.ceramint.2010.08.024 (Effect of Ni substitution on electrical and thermoelectric properties ...)

## Ni-Sn-Ti
- rank 27 | 309 samples | 65 papers | 148 compositions
- compositions: TiNiSn (78); TiNi1.1Sn (8); TiNiCu0.05Sn (8); Ti0.9Hf0.1NiSn (5); TiNi2Sn (4); TiNiSn0.99Sb0.01 (4)
- dopant candidates (<5% at.): Sb (59), Mn (30), Hf (25), V (17), Zr (13), Cu (10), Nb (6), Y (6), Ta (6), Pt (4), Si (4), Fe (3), Sc (3), Co (2), C (2), N (2), Al (1), Ge (1)
- seed hypothesis (confirm): half_heusler
- measured range: 14-960 K (5th-95th pct of 1198 curves; full span incl. outliers 10-1178 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiNi2Sn Fm-3m (225) mp-3740 [hull=0.035, icsd=6, PRIMARY]; TiNiSn F-43m (216) mp-924130 [hull=0.000, icsd=3, PRIMARY]; Ti5NiSn3 P6_3/mcm (193) mp-1208243 [hull=0.017, PRIMARY]; TiNi2Sn P4/mmm (123) mp-1216749 [hull=0.136]
- papers: https://doi.org/10.1063/1.1868063 (Effect of Ti substitution on the thermoelectric properties of (Zr,Hf)N...) | https://doi.org/10.1063/1.4765358 (Enhanced thermoelectric properties of bulk TiNiSn via formation of a T...) | https://doi.org/10.1021/cm3011343 (Rapid Microwave Preparation of Thermoelectric TiNiSn and TiCoSb Half-H...)

## La-Mn-O-Sr
- rank 28 | 307 samples | 83 papers | 97 compositions
- compositions: La0.7Sr0.3MnO3 (66); La0.67Sr0.33MnO3 (45); La2SrMn3O9 (32); La0.6Sr0.4MnO3 (8); LaSr2Mn2O7 (7); La0.667Sr0.333MnO3 (5)
- dopant candidates (<5% at.): Cr (32), Co (23), Zn (12), Bi (9), Fe (7), Nd (6), Ru (5), Ni (4), Pr (4), Al (4), V (4), Y (3), In (2), Cu (2), Gd (1), Sm (1), Ti (1)
- seed hypothesis (confirm): perovskite
- measured range: 11-1115 K (5th-95th pct of 373 curves; full span incl. outliers 10-1272 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): KSr3La8Mn12O36 P2 (3) mp-744044 [hull=0.002, PRIMARY]; Sr2La2Mn4O11 I4/mmm (139) mp-1218776 [hull=0.065, PRIMARY]; Sr2LaMn2O7 I4/mmm (139) mp-1218756 [hull=0.000, PRIMARY]; Sr3La5Mn8O24 C2 (5) mp-691121 [hull=0.000, PRIMARY]; Sr3La9Mn11NiO36 P1 (1) mp-743659 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1063/1.4804937 (Cross-plane thermoelectric transport in p-type La0.67Sr0.33MnO3/LaMnO3...) | https://doi.org/10.1016/j.jallcom.2013.08.106 (Thermopower and electrical resistivity of La1−xSrxMnO3 (x=0.2, 0.3): E...) | https://doi.org/10.1016/j.jallcom.2014.08.005 (Electrical, thermal and magnetic properties of Bi doped La0.7−xBixSr0....)

## Ge-Si
- rank 29 | 301 samples | 84 papers | 118 compositions
- compositions: SiGe (32); Si0.8Ge0.2 (25); Si0.5Ge0.5 (21); Si80Ge20 (19); Si0.92Ge0.08 (13); Si0.7Ge0.3 (11)
- dopant candidates (<5% at.): P (64), B (26), Ga (26), W (9), Sb (6), Na (5), O (5), Fe (4), Sr (4), Ti (4), As (3), Au (3), Ag (3), Mo (1), C (1), Zr (1), Y (1), Mg (1)
- seed hypothesis (confirm): diamond_cubic
- solid-solution axis: Ge/(Ge+Si) spans 0.05-0.95 (median 0.20) over 118 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 54-1272 K (5th-95th pct of 831 curves; full span incl. outliers 12-1325 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Si3Ge Fm-3m (225) mp-972751 [hull=0.539, PRIMARY]; Si7Ge P-43m (215) mp-1094056 [hull=0.010, PRIMARY]; SiGe P2_1 (4) mp-1096549 [hull=0.020, PRIMARY]; SiGe3 I4/mmm (139) mp-1187004 [hull=0.421, PRIMARY]; SiGe F-43m (216) mp-1219182 [hull=0.031]
- papers: https://doi.org/10.1016/j.actamat.2013.10.062 (Influence of in situ formed MoSi2 inclusions on the thermoelectrical p...) | https://doi.org/10.1002/adma.200600527 (New Directions for Low-Dimensional Thermoelectric Materials) | https://doi.org/10.1002/anie.201408431 (Polymer Composites for Thermoelectric Applications)

## Bi-Sb
- rank 30 | 293 samples | 64 papers | 136 compositions
- compositions: Bi85Sb15 (29); Bi0.88Sb0.12 (23); Bi88Sb12 (13); Bi93Sb7 (9); Bi0.91Sb0.09 (9); Bi90Sb10 (7)
- dopant candidates (<5% at.): Sn (36), Pb (21), C (15), Te (12), Nb (8), Ag (6), Se (6), O (5), Ge (4), W (3), Zr (3), Ho (2), As (2), Li (2)
- seed hypothesis (confirm): a7_rhombohedral
- solid-solution axis: Bi/(Bi+Sb) spans 0.25-0.95 (median 0.87) over 136 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 11-468 K (5th-95th pct of 834 curves; full span incl. outliers 10-542 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi3Sb R3m (160) mp-1227319 [hull=0.000, PRIMARY]; BiSb R3m (160) mp-1227290 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1021/nn404692s (Bi1–xSbxAlloy Nanocrystals: Colloidal Synthesis, Charge Transport, and...) | https://doi.org/10.1007/s003390050947 (Thermoelectric properties of mechanically alloyed Bi-Sb alloys) | https://doi.org/10.1063/1.2009828 (Ag9TlTe5: A high-performance thermoelectric bulk material with extreme...)

## Se-Sn
- rank 31 | 287 samples | 64 papers | 130 compositions
- compositions: SnSe (108); Na0.03Sn0.965Se (12); Ag0.01Sn0.99Se (7); SnSe2 (5); Sn0.99SePb0.01 (4); Sn0.94SeBi0.06 (4)
- dopant candidates (<5% at.): Na (49), Pb (25), Cl (17), Br (17), Te (14), Ag (13), S (10), Bi (10), Cu (9), K (6), In (6), Tl (6), Ge (6), Nb (4), C (3), Sb (3), Zn (3), La (2), Gd (2), I (1), Li (1)
- seed hypothesis (confirm): layered_ges, cmcm_snse_ht  <-- MIXED, split per composition
- measured range: 293-921 K (5th-95th pct of 1147 curves; full span incl. outliers 11-980 K)
  !! MEASUREMENT CROSSES A TRANSITION: layered_ges -> cmcm_snse_ht at ~800 K (Pnma -> Cmcm, ~800 K for SnSe and ~880 K for SnS; the high-ZT regime.)
     Record each phase with its own temperature range, not a single prototype.
- [ref 1] TEDesignLab / ICSD: SnSe Pnma (62) mp-691 [hull=0.000, icsd=32, PRIMARY]; SnSe2 P-3m1 (164) mp-665 [hull=0.000, icsd=6, PRIMARY]; SnSe Cmcm (63) mp-2168 [hull=0.011, icsd=11]; SnSe Fm-3m (225) mp-2693 [hull=0.004, icsd=2]
- [ref 2] MP, ranked by ICSD evidence: Sn3Se Fm-3m (225) mp-1187055 [hull=0.260, PRIMARY, AMBIGUOUS]; Ba(SnSe)32 Cm (8) mp-1120806 [hull=0.035, PRIMARY]; SnSe P4/nmm (129) mp-8936 [hull=0.046, icsd=1]; SnSe Pmmn (59) mp-1205370 [hull=0.316, icsd=1]; Sn3Se Pm-3m (221) mp-1187043 [hull=0.270]
- papers: https://doi.org/10.1002/aenm.201500360 (Studies on Thermoelectric Properties of n-type Polycrystalline SnSe1-x...) | https://doi.org/10.1063/1.4880817 (Assessment of the thermoelectric performance of polycrystalline p-type...) | https://doi.org/10.3390/en8076275 (Investigation of the Anisotropic Thermoelectric Properties of Oriented...)

## Ni-Sn-Zr
- rank 32 | 280 samples | 68 papers | 147 compositions
- compositions: ZrNiSn (82); ZrNiSn0.98Sb0.02 (7); ZrNiSn0.99Sb0.01 (6); ZrNi1.1Sn (5); Zr0.98Ta0.02NiSn (5); Zr0.95Nb0.05NiSn (4)
- dopant candidates (<5% at.): Sb (50), Ti (24), Y (19), Nb (17), Co (16), Cu (13), Hf (11), Ta (11), V (11), La (10), Ge (9), Sc (7), Yb (5), In (4), Bi (3), Ce (3), O (2), Pb (1)
- seed hypothesis (confirm): half_heusler
- measured range: 91-1042 K (5th-95th pct of 1043 curves; full span incl. outliers 10-1127 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZrNi2Sn Fm-3m (225) mp-19877 [hull=0.048, icsd=4, PRIMARY]; Zr2Ni2Sn P4/mbm (127) mp-20146 [hull=0.024, icsd=2, PRIMARY]; ZrNiSn F-43m (216) mp-924129 [hull=0.000, icsd=2, PRIMARY]; ZrNi4Sn F-43m (216) mp-30807 [hull=0.034, icsd=1, PRIMARY]; Zr6NiSn2 P-62m (189) mp-1206510 [hull=0.003, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2010.04.028 (Vacancy site occupation by Co and Ir in half-Heusler ZrNiSn and conver...) | https://doi.org/10.1016/j.actamat.2014.11.042 (Microstructure and thermoelectric properties of a ZrNi 1.1 Sn half-Heu...) | https://doi.org/10.1002/aenm.201300336 (Effect of Hf Concentration on Thermoelectric Properties of Nanostructu...)

## Cu-Se
- rank 33 | 277 samples | 67 papers | 138 compositions
- compositions: Cu2Se (75); Cu1.98Se (15); Cu1.97Se (11); Cu2Se1.01 (8); Cu1.99Se (5); Cu1.965Pb0.015Se (5)
- dopant candidates (<5% at.): C (21), Pb (19), Ga (14), Ni (9), Bi (9), Ag (8), Fe (7), In (6), S (6), O (6), Ca (6), Sn (5), I (5), Br (4), Sb (4), Si (4), B (4), Al (3), F (3), Zn (2), Cl (1), Mn (1), Sm (1), Te (1)
- seed hypothesis (confirm): cu2se_superionic
- measured range: 281-999 K (5th-95th pct of 1121 curves; full span incl. outliers 10-1479 K)
  !! MEASUREMENT CROSSES A TRANSITION: cu2se_superionic -> cu2se_superionic at ~400 K (Ordered low-T superstructure -> cubic superionic, ~400 K. Cu2S transforms near ~376 K.)
     Record each phase with its own temperature range, not a single prototype.
- [ref 1] TEDesignLab / ICSD: Cu2Se Fm-3m (225) mp-16366 [hull=0.127, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: CuSe P6_3/mmc (194) mp-488 [hull=0.001, icsd=19, PRIMARY]; CuSe2 Pnnm (58) mp-2000 [hull=0.000, icsd=5, PRIMARY, AMBIGUOUS]; Cu3Se2 P-42_1m (113) mp-20683 [hull=0.000, icsd=5, PRIMARY]; Cu13Se8 F-43m (216) mp-32857 [hull=0.076, PRIMARY]; Cu27Se20 R3m (160) mp-684606 [hull=0.058, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2015.08.022 (Thermoelectric, thermodynamic, and structural properties in Cu1.94A0.0...) | https://doi.org/10.1021/acs.chemmater.5b02405 (Influence of Compensating Defect Formation on the Doping Efficiency an...) | https://doi.org/10.1088/1674-1056/20/8/087201 (Phase transition and high temperature thermoelectric properties of cop...)

## Mn-Si
- rank 34 | 277 samples | 74 papers | 119 compositions
- compositions: MnSi1.73 (41); MnSi1.7 (22); MnSi (20); MnSi1.74 (17); MnSi1.75 (17); Mn0.31Si0.69 (9)
- dopant candidates (<5% at.): Ge (29), Al (22), Cr (10), Te (8), Ag (8), Ce (6), Re (6), C (4), V (4), B (4), Ru (3), Fe (3), Ti (3), W (2), Y (1), Yb (1), Pb (1)
- seed hypothesis (confirm): hms_chimney_ladder
- measured range: 14-1015 K (5th-95th pct of 910 curves; full span incl. outliers 10-1151 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn5Si3 P6_3/mcm (193) mp-1111 [hull=0.045, icsd=17, PRIMARY]; MnSi P2_13 (198) mp-1431 [hull=0.000, icsd=9, PRIMARY]; Mn3Si Fm-3m (225) mp-20211 [hull=0.000, icsd=4, PRIMARY]; Mn4Si7 P-4c2 (116) mp-680339 [hull=0.001, icsd=3, PRIMARY]; Mn5Si2 P4_12_12 (92) mp-608655 [hull=0.066, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2009.07.005 (Crystal structure and thermoelectric properties of chimney–ladder comp...) | https://doi.org/10.1016/j.ceramint.2012.08.086 (Synthesis, characterization, and thermoelectric properties of nanostru...) | https://doi.org/10.1021/cm5023823 (Thermoelectric Properties of Undoped High Purity Higher Manganese Sili...)

## Fe-Sb
- rank 35 | 273 samples | 71 papers | 192 compositions
- compositions: FeSb2 (51); (Ce0.5092La0.2841Nd0.1568Pr0.0498)Fe4Sb12 (4); Ce0.40Yb0.53Fe4Sb12 (3); (Pr0.0487Nd0.9513)0.86Fe4Sb12 (3); Ba0.83Fe4Sb12 (3); (Pr0.487Nd0.9513)0.86Fe4Sb12 (3)
- dopant candidates (<5% at.): Ce (95), Pr (74), La (74), Co (68), Nd (61), Ni (53), Yb (42), Ca (25), Ba (12), Te (8), Nb (8), Sn (7), Se (6), Ru (5), Cu (4), In (4), Sm (4), Pt (2), As (2), Si (2), Cr (1)
- seed hypothesis (confirm): marcasite, skutterudite  <-- MIXED, split per composition
- measured range: 10-826 K (5th-95th pct of 1046 curves; full span incl. outliers 10-912 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeSb2 Pnnm (58) mp-20714 [hull=0.000, icsd=29, PRIMARY]; FeSb P6_3/mmc (194) mp-2619 [hull=0.040, icsd=3, PRIMARY]; CaCe(FeSb3)8 C2/m (12) mp-1228062 [hull=0.000, PRIMARY]; Fe4Sb3 P-6m2 (187) mp-1225139 [hull=0.447, PRIMARY]; Fe3Sb P6_3/mmc (194) mp-1184324 [hull=0.091, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2011.12.022 (Thermoelectric properties of p-type skutterudites YbxFe3.5Ni0.5Sb12 (0...) | https://doi.org/10.1063/1.4833055 (Correlated evolution of colossal thermoelectric effect and Kondo insul...) | https://doi.org/10.1143/apex.2.091102 (Huge Thermoelectric Power Factor: FeSb2versus FeAs2and RuSb2)

## Hf-Ni-Sn-Zr
- rank 36 | 261 samples | 58 papers | 149 compositions
- compositions: Hf0.6Zr0.4NiSn0.98Sb0.02 (15); Zr0.5Hf0.5NiSn (14); Hf0.5Zr0.5NiSn0.98Sb0.02 (13); Hf0.5Zr0.5NiSn (8); Hf0.6Zr0.4NiSn0.995Sb0.005 (8); Hf0.25Zr0.75NiSn0.99Sb0.01 (7)
- dopant candidates (<5% at.): Sb (156), Nb (18), Ti (12), V (10), Y (9), Ta (6), Bi (6), Pd (3), Pt (3), O (2), W (2), Co (1), Cr (1), Cu (1), Mn (1)
- seed hypothesis (confirm): half_heusler
- solid-solution axis: Hf/(Hf+Zr) spans 0.09-0.80 (median 0.60) over 149 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 15-1132 K (5th-95th pct of 1070 curves; full span incl. outliers 10-1174 K)
- papers: https://doi.org/10.1016/j.actamat.2009.02.026 (High-performance half-Heusler thermoelectric materials Hf1−x ZrxNiSn1−...) | https://doi.org/10.1002/aenm.201300336 (Effect of Hf Concentration on Thermoelectric Properties of Nanostructu...) | https://doi.org/10.1063/1.1868063 (Effect of Ti substitution on the thermoelectric properties of (Zr,Hf)N...)

## Co-O-Sr
- rank 37 | 246 samples | 91 papers | 139 compositions
- compositions: SrCoO3 (20); SrCo0.9Nb0.1O3 (13); SrCo0.8Fe0.2O3 (11); Sr6Co5O15 (10); Dy0.2Sr0.8CoO3 (6); SrSc0.175Nb0.025Co0.8O3 (5)
- dopant candidates (<5% at.): Nb (43), Fe (32), Y (29), Sc (16), Ce (12), La (10), Ca (9), Dy (9), Ti (8), Ho (8), Ru (8), Sm (7), Bi (6), Sb (5), Ni (3), Ga (3), Ta (3), Zr (3), Ir (3), Nd (3), Zn (3), Rh (2), C (2), Re (2), Mn (2), Mo (2), Pb (1), Ge (1), Er (1), F (1), Gd (1), Yb (1), Ba (1), P (1)
- seed hypothesis (confirm): perovskite
- measured range: 11-1175 K (5th-95th pct of 303 curves; full span incl. outliers 10-1309 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr6(CoO3)5 R32 (155) mp-19235 [hull=0.000, icsd=8, PRIMARY]; Sr2Co2O5 Ima2 (46) mp-644893 [hull=0.007, icsd=4, PRIMARY]; Sr5(CoO3)4 P-3c1 (165) mp-704141 [hull=0.002, icsd=2, PRIMARY]; Sr8Co8O23 I4/mmm (139) mp-606379 [hull=0.035, icsd=1, PRIMARY]; SrCo6O11 P6_3/mmc (194) mp-24862 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.2337080 (Transport properties of the thermoelectric layered cobalt oxide Pb–Sr–...) | https://doi.org/10.1039/b914661j (Novel thermoelectric properties of complex transition-metal oxides) | https://doi.org/10.1143/jjap.43.8208 (Thermoelectric Properties ofAn+2Con+1O3n+3(A=Ca, Sr, Ba,n=1–5))

## Sb-Te
- rank 38 | 234 samples | 78 papers | 72 compositions
- compositions: Sb2Te3 (127); Sb1.85In0.15Te3 (9); Ag0.01Sb1.85In0.15Te3 (7); Bi0.2Sb1.8Te3 (5); SbTe (4); Sb1.8In0.2Te3 (4)
- dopant candidates (<5% at.): In (50), Ag (19), Bi (11), B (9), Mg (8), Sn (6), Cu (4), Ga (3), Tl (3), Mn (3), C (3), Se (2), Cr (2), H (2), N (2), I (2), Ge (1), S (1), Co (1)
- seed hypothesis (confirm): tetradymite
- measured range: 15-681 K (5th-95th pct of 719 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sb2Te3 R-3m (166) mp-1201 [hull=1.017, icsd=26, PRIMARY]; Sb2Te P-3m1 (164) mp-6997 [hull=0.575, icsd=1, PRIMARY]; SbTe P-3m1 (164) mp-7716 [hull=0.854, icsd=1, PRIMARY]; Sb16Te3 R-3m (166) mp-640862 [hull=0.253, PRIMARY]; Sb8Te3 R-3m (166) mp-12826 [hull=0.466, PRIMARY]
- papers: https://doi.org/10.1021/acsami.5b02504 (A Facile Surfactant-Assisted Reflux Method for the Synthesis of Single...) | https://doi.org/10.1063/1.4887504 (Low thermal conductivity and high thermoelectric figure of merit in p-...) | https://doi.org/10.1063/1.4936123 (Decoupling electrical and thermal properties in antimony telluride bas...)

## Bi
- rank 39 | 220 samples | 40 papers | 24 compositions
- compositions: Bi (152); Sn0.025Bi95Sb5 (15); Sn0.012Bi95Sb5 (11); Sn0.076Bi95Sb5 (10); Bi98Sb2 (6); Bi93.4(Bi2Te3)1.3 (3)
- dopant candidates (<5% at.): Sb (50), Sn (37), Te (9), In (4), Li (4)
- seed hypothesis (confirm): a7_rhombohedral
- measured range: 10-388 K (5th-95th pct of 394 curves; full span incl. outliers 10-533 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi R-3m (166) mp-23152 [hull=0.000, icsd=8, PRIMARY]; Bi C2/m (12) mp-23157 [hull=0.067, icsd=2]; Bi Cmce (64) mp-1078637 [hull=0.109, icsd=2]; Bi P2_1/m (11) mp-1182070 [hull=0.059, icsd=1]; Bi Pmma (51) mp-1096851 [hull=0.123]
- papers: https://doi.org/10.1002/adma.201204010 (Enhancement of Thermoelectric Performance of Ball-Milled Bismuth Due t...) | https://doi.org/10.1016/0011-2275(79)90004-3 (Phonon-drag low temperature thermoelectric refrigeration) | https://doi.org/10.1007/s11051-008-9541-6 (Synthesis and thermoelectric characterisation of bismuth nanoparticles)

## Si
- rank 40 | 218 samples | 61 papers | 69 compositions
- compositions: Si (103); Si0.97Ge0.03 (15); SiAs0.006 (11); Si76.41Ge1.91Ga1.96P2.53 (5); (SiB0.0004)100(Si0.8Ge0.2)20 (4); Si98P2 (3)
- dopant candidates (<5% at.): P (40), Ge (35), B (31), As (14), Ga (8), W (4), Cr (2), Na (2), Sb (1), V (1), Al (1), Mo (1), Ni (1)
- seed hypothesis (confirm): diamond_cubic
- measured range: 20-1277 K (5th-95th pct of 494 curves; full span incl. outliers 10-1373 K)
- [ref 1] TEDesignLab / ICSD: Si Fd-3m (227) mp-149 [hull=0.000, icsd=30, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Si Ia-3 (206) mp-168 [hull=0.159, icsd=4]; Si P6_3/mmc (194) mp-165 [hull=0.011, icsd=3]; Si Cmce (64) mp-1079649 [hull=0.428, icsd=3]; Si Pm-3n (223) mp-971662 [hull=0.063, icsd=2]; Si P6/mmm (191) mp-1196961 [hull=0.081, icsd=2]
- papers: https://doi.org/10.1002/adem.201200233 (Thermoelectric Properties of Nanocrystalline Silicon from a Scaled-Up ...) | https://doi.org/10.1002/adfm.200900250 (Nanostructured Bulk Silicon as an Effective Thermoelectric Material) | https://doi.org/10.1002/adfm.201401201 (Nanograined Half-Heusler Semiconductors as Advanced Thermoelectrics: A...)

## Pb-S
- rank 41 | 207 samples | 30 papers | 154 compositions
- compositions: PbS (33); Pb1.01Bi0.02S1.03Cl0.02 (4); Pb0.96Bi0.04S (4); Pb0.98Na0.02S (3); Pb1.01Sb0.02S1.03Cl0.02 (3); Pb0.975Na0.025S(SrS)0.03 (2)
- dopant candidates (<5% at.): Cl (53), Na (35), Ga (21), Bi (20), Te (16), Ca (16), Sr (16), Cu (16), In (15), Sb (11), Sn (10), Ag (5), Zn (4), Cd (4), Li (4)
- seed hypothesis (confirm): rocksalt
- measured range: 298-931 K (5th-95th pct of 932 curves; full span incl. outliers 77-992 K)
- [ref 1] TEDesignLab / ICSD: PbS Fm-3m (225) mp-21276 [hull=0.000, icsd=33, PRIMARY]; PbS Cmcm (63) mp-1018115 [hull=0.038, icsd=3]; PbS Pma2 (28) mp-1078944 [hull=0.170, icsd=3]; PbS Pnma (62) mp-1091375 [hull=0.019, icsd=2]; PbS P2_1/m (11) mp-1087486 [hull=0.083, icsd=2]
- [ref 2] MP, ranked by ICSD evidence: Pb3S Pm-3m (221) mp-1186425 [hull=0.319, PRIMARY]; PbS2 I4/mcm (140) mp-1025039 [hull=0.000, PRIMARY]; PbS Amm2 (38) mp-1079543 [hull=0.164, icsd=2]; PbS Pm-3m (221) mp-21039 [hull=0.256, icsd=2]; PbS C2/m (12) mp-1067933 [hull=0.058, icsd=1]
- papers: https://doi.org/10.1021/nn305971v (Core–Shell Nanoparticles As Building Blocks for the Bottom-Up Producti...) | https://doi.org/10.1002/aenm.201200683 (High Thermoelectric Efficiency of n-type PbS) | https://doi.org/10.1007/s10582-005-0076-0 (Thermoelectric Properties of the TlBiS2-PbS Alloys)

## Ag-Sb-Te
- rank 42 | 206 samples | 44 papers | 124 compositions
- compositions: AgSbTe2 (41); Ag0.366Sb0.56Te (12); Ag0.9Sb1.1Te2.1 (9); Ag0.81Sb1.19Te2.19 (4); AgSbTe (4); AgSbTe1.98Se0.02 (3)
- dopant candidates (<5% at.): Se (20), Na (18), Sn (15), Ge (7), La (6), Pb (6), Bi (5), Ce (4), Yb (4), S (4), Mn (3), In (3), Co (3), Fe (2), Ni (2), Cu (1), Tl (1)
- seed hypothesis (confirm): rocksalt
- measured range: 81-700 K (5th-95th pct of 746 curves; full span incl. outliers 20-851 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AgSbTe2 R-3m (166) mp-12360 [hull=0.652, icsd=1, PRIMARY]; Ag3SbTe4 Pm-3m (221) mp-1214902 [hull=0.430, PRIMARY]; Ag3SbTe6 Cmmm (65) mp-1215084 [hull=1.419, PRIMARY]; AgSbTe2 P4/mmm (123) mp-12359 [hull=0.701, icsd=1]; AgSbTe2 P2/m (10) mp-1229055 [hull=1.083]
- papers: https://doi.org/10.1016/j.actamat.2010.04.007 (Phase compositions, nanoscale microstructures and thermoelectric prope...) | https://doi.org/10.1063/1.4896435 (Influence of nanoscale Ag2Te precipitates on the thermoelectric proper...) | https://doi.org/10.1063/1.2920210 (Low thermal conductivity and high thermoelectric figure of merit in n-...)

## Bi-Co-O-Sr
- rank 43 | 206 samples | 50 papers | 94 compositions
- compositions: Bi2Sr2Co2O8 (32); Bi2Sr2Co1.8O8 (29); Bi2Sr2Co2O9 (8); Bi1.6Pb0.4Sr2Co2O8 (7); Bi1.5Pb0.5Sr2.5Y0.5Co2O9 (4); Bi1.6Pb0.4Sr2Co1.8O8 (3)
- dopant candidates (<5% at.): Pb (76), Y (34), Ag (10), Ti (9), La (7), Ca (6), Ba (6), Rb (5), Si (4), C (4), Na (3), W (3), Ir (2), Cu (2), Al (2), Mo (2), Zr (2), B (1)
- seed hypothesis (confirm): misfit_cobaltite
- measured range: 10-998 K (5th-95th pct of 540 curves; full span incl. outliers 10-1038 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr6Co4Bi2O15 C222 (21) mp-704097 [hull=0.032, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2007.03.019 (Texture development in Bi1.5Pb0.5Sr1.7Y0.5Co2O9−δ layered cobaltite by...) | https://doi.org/10.1007/s00339-015-9169-1 (Thermoelectric sintered glass-ceramics with a Bi2Sr2Co2O x phase) | https://doi.org/10.1063/1.4801644 (Exotic reinforcement of thermoelectric power driven by Ca doping in la...)

## In-O
- rank 44 | 205 samples | 33 papers | 85 compositions
- compositions: In2O3 (48); In1.92(ZnCe)0.08O3 (25); In1.99Ge0.01O3 (9); In1.805Sn0.195O3 (5); In1.98Ce0.02O3 (4); In1.96Ce0.04O3 (4)
- dopant candidates (<5% at.): Zn (46), Ce (45), Ge (37), Sn (29), Ti (10), Ni (7), V (7), Ga (5), Mo (5), Co (4), Nd (4), Cu (3), Li (3), Mn (2), Lu (1), Mg (1), Si (1)
- seed hypothesis (confirm): bixbyite
- measured range: 14-1171 K (5th-95th pct of 366 curves; full span incl. outliers 10-1468 K)
- [ref 1] TEDesignLab / ICSD: In2O3 Pbcn (60) mp-1105681 [hull=0.050, icsd=4]; In2O3 R-3c (167) mp-22323 [hull=0.029, icsd=3]; In2O3 Pnma (62) mp-644741 [hull=0.244, icsd=2]
- [ref 2] MP, ranked by ICSD evidence: In2O3 Ia-3 (206) mp-22598 [hull=0.000, icsd=18, PRIMARY]; InO2 Pnnm (58) mp-1181008 [hull=0.228, icsd=1, PRIMARY]; InO P6_3mc (186) mp-1184809 [hull=0.310, PRIMARY]; InO3 Imm2 (44) mp-1181272 [hull=0.610, PRIMARY]; In2O3 Pbca (61) mp-1194571 [hull=0.042, icsd=1]
- papers: https://doi.org/10.1063/1.3529489 (Electronic structure and thermoelectric properties of In32−xGexO48 (x=...) | https://doi.org/10.1016/j.jallcom.2015.04.057 (Enhancement of thermoelectric properties in Sn doped (In0.95Lu0.05)2O3) | https://doi.org/10.1063/1.2986148 (Enhancement of the thermoelectric performances of In2O3 by the coupled...)

## Bi-Se
- rank 45 | 202 samples | 56 papers | 56 compositions
- compositions: Bi2Se3 (99); (Bi0.95Sb0.05)2Se3 (17); BiSe (7); Bi1.98Tl0.02Se3 (4); (Bi2Se3)0.95(TiO2)0.05 (4); (Bi2Se3)0.98(TiO2)0.02 (4)
- dopant candidates (<5% at.): Sb (22), Tl (13), O (12), Ti (12), Mn (10), Cu (10), Ca (6), Fe (5), Co (3), K (1), Rb (1), I (1), Li (1), Te (1), Er (1)
- seed hypothesis (confirm): tetradymite
- measured range: 10-699 K (5th-95th pct of 513 curves; full span incl. outliers 10-801 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi2Se3 Pnma (62) mp-23164 [hull=0.026, icsd=3, PRIMARY]; BiSe P-3m1 (164) mp-27902 [hull=0.008, icsd=2, PRIMARY]; Bi2Se P2_1/c (14) mp-1102082 [hull=0.154, icsd=1, PRIMARY]; Bi8Se7 P-3m1 (164) mp-680214 [hull=0.011, icsd=1, PRIMARY]; Bi8Se9 R-3m (166) mp-1190284 [hull=0.004, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/nn507250r (Synthesis of Multishell Nanoplates by Consecutive Epitaxial Growth of ...) | https://doi.org/10.1002/adma.201203764 (Surfactant-Free Scalable Synthesis of Bi2Te3and Bi2Se3Nanoflakes and E...) | https://doi.org/10.1063/1.4902159 (Thermochemically evolved nanoplatelets of bismuth selenide with enhanc...)

## O-V
- rank 46 | 186 samples | 52 papers | 41 compositions
- compositions: VO2 (86); V7O13 (13); V2O3 (10); V8O15 (8); SrV6O15 (6); V6O11 (6)
- dopant candidates (<5% at.): Sr (15), Cu (10), W (10), Fe (5), P (5), H (4), Ba (4), Na (3), Ti (1)
- seed hypothesis (confirm): rutile, vo2_monoclinic, v2o5_layered  <-- MIXED, split per composition
- measured range: 11-700 K (5th-95th pct of 214 curves; full span incl. outliers 10-842 K)
  !! MEASUREMENT CROSSES A TRANSITION: vo2_monoclinic -> rutile at ~340 K (M1 -> rutile metal-insulator transition, ~340 K.)
     Record each phase with its own temperature range, not a single prototype.
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): V2O3 R-3c (167) mp-18937 [hull=0.012, icsd=23, PRIMARY]; VO2 P4_2/mnm (136) mp-19094 [hull=0.000, icsd=19, PRIMARY]; VO Fm-3m (225) mp-19184 [hull=0.154, icsd=10, PRIMARY]; V3O5 P2/c (13) mp-622497 [hull=0.000, icsd=6, PRIMARY]; V6O13 Cm (8) mp-19457 [hull=0.023, icsd=5, PRIMARY, AMBIGUOUS]
- papers: https://doi.org/10.1021/ja203186f (Hydrogen-Incorporation Stabilization of Metallic VO2(R) Phase to Room ...) | https://doi.org/10.1063/1.1654062 (Transport and Structural Properties of VO2Films) | https://doi.org/10.1209/epl/i2003-00161-8 (V–V bond length fluctuations in VO x)

## Pb-Se-Te
- rank 47 | 184 samples | 41 papers | 127 compositions
- compositions: (Pb0.96Tl0.04) (Te0.85Se0.15) (10); (Pb0.98Tl0.02)(Te0.85Se0.15) (6); PbTe0.9Se0.1 (6); (Pb0.99Mg0.01)0.98Na0.02Te0.8Se0.2 (5); PbTe0.85Se0.15 (5); PbTe0.5Se0.5 (5)
- dopant candidates (<5% at.): Na (47), Tl (18), I (18), Sb (17), Mg (17), In (8), Sr (7), Ag (6), Bi (6), S (6), Ba (5), K (4), Sn (4), Cu (4), Sm (2), Yb (1), Ce (1)
- seed hypothesis (confirm): rocksalt
- solid-solution axis: Se/(Se+Te) spans 0.10-0.90 (median 0.25) over 127 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 291-920 K (5th-95th pct of 610 curves; full span incl. outliers 24-1295 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Te4Pb5Se I4/mmm (139) mp-1217406 [hull=0.000, PRIMARY]; TePb2Se R-3m (166) mp-1217291 [hull=0.011, PRIMARY]
- papers: https://doi.org/10.1039/c2ce25137j (Controllable synthesis and thermoelectric transport properties of bina...) | https://doi.org/10.1016/j.cap.2011.05.035 (Preparation and thermoelectric properties of AgPb18SbTe20−xSex (x = 1,...) | https://doi.org/10.1039/c1ee01895g (Combining alloy scattering of phonons and resonant electronic levels t...)

## Ca-La-Mn-O
- rank 48 | 180 samples | 50 papers | 89 compositions
- compositions: La0.7Ca0.3MnO3 (39); La0.67Ca0.33MnO3 (10); La0.5Ca0.5MnO3 (9); La0.625Ca0.375MnO3 (6); La0.525Pr0.1Ca0.375MnO3 (4); La0.7Ca0.26Na0.04MnO3 (4)
- dopant candidates (<5% at.): Ge (14), Bi (13), Cr (11), Sm (11), Pr (8), Ag (8), Te (6), Co (6), Na (5), Fe (5), Ba (5), Ti (5), Sr (4), V (2), K (2), Eu (1), Cu (1)
- seed hypothesis (confirm): perovskite
- measured range: 11-387 K (5th-95th pct of 222 curves; full span incl. outliers 10-1470 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaLaMn2O6 Pmn2_1 (31) mp-39689 [hull=0.002, icsd=2, PRIMARY]; Ca2LaMn3O9 Pnma (62) mp-1227659 [hull=0.009, PRIMARY]; Ca2LaMn2O7 I4/mmm (139) mp-1214095 [hull=0.024, PRIMARY]; Ca3La5Mn7FeO24 P1 (1) mp-694928 [hull=0.001, PRIMARY]; Ca3La5Mn7NiO24 P1 (1) mp-39207 [hull=0.003, PRIMARY]
- papers: https://doi.org/10.1063/1.4754707 (Thermoelectric properties of YBa2Cu3O7−δ–La2/3Ca1/3MnO3 superlattices) | https://doi.org/10.1063/1.4902850 (Colossal thermoelectric power in charge ordered lanthanum calcium mang...) | https://doi.org/10.1186/1556-276x-9-415 (La 1−xCaxMnO3 semiconducting nanostructures: morphology and thermoelec...)

## Hf-Ni-Sn-Ti-Zr
- rank 49 | 179 samples | 41 papers | 115 compositions
- compositions: Hf0.50Ti0.25Zr0.25NiSn0.99Sb0.01 (14); Ti0.3Zr0.35Hf0.35NiSn (10); Zr0.25Hf0.25Ti0.5NiSn0.994Sb0.006 (7); (Zr0.6Hf0.4)0.7Ti0.3NiSn (5); Ti0.5(Zr0.5Hf0.5)0.5NiSn (5); (Hf0.25Zr0.25Ti0.5)0.98Nb0.02NiSn (5)
- dopant candidates (<5% at.): Sb (94), Nb (17), Pd (10), Fe (10), Sc (6), Y (5), V (4), Ta (4), Bi (3), Cu (3), Te (1)
- seed hypothesis (confirm): half_heusler
- solid-solution axis: Hf/(Hf+Ti) spans 0.25-0.67 (median 0.41) over 115 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 21-994 K (5th-95th pct of 661 curves; full span incl. outliers 10-1171 K)
- papers: https://doi.org/10.1063/1.1868063 (Effect of Ti substitution on the thermoelectric properties of (Zr,Hf)N...) | https://doi.org/10.1063/1.2168019 (Effect of substitutions on the thermoelectric figure of merit of half-...) | https://doi.org/10.1063/1.3531662 (Thermoelectric properties and electronic structure of substituted Heus...)

## Pb-Sn-Te
- rank 50 | 176 samples | 34 papers | 144 compositions
- compositions: (Pb0.5Sn0.5Te)0.4955Te0.5045 (12); Pb0.6Sn0.4Te (9); Pb0.73Sn0.27Te (6); Sn0.70Pb0.30Te (5); PbSnTe (3); Pb0.5Sn0.5Te1 (2)
- dopant candidates (<5% at.): Sb (27), In (26), Cd (21), Ag (19), Na (13), I (11), Mn (9), Bi (6), Mg (6), K (4), Zn (4), Sc (2), Ge (1)
- seed hypothesis (confirm): rocksalt
- solid-solution axis: Pb/(Pb+Sn) spans 0.10-0.90 (median 0.50) over 144 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 281-838 K (5th-95th pct of 671 curves; full span incl. outliers 10-874 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sn4Te5Pb I4/mmm (139) mp-1219009 [hull=0.000, PRIMARY]; SnTe2Pb R-3m (166) mp-1218924 [hull=0.017, PRIMARY, AMBIGUOUS]; SnTe4Pb3 P4/mmm (123) mp-1218925 [hull=0.013, PRIMARY]; SnTe5Pb4 R-3m (166) mp-1218909 [hull=0.017, PRIMARY]; SnTe2Pb P4/mmm (123) mp-1218915 [hull=0.023]
- papers: https://doi.org/10.1002/aenm.201200083 (Increase in the Figure of Merit by Cd-Substitution in Sn1-xPbxTe and E...) | https://doi.org/10.1002/adma.200502770 (Nanostructuring and High Thermoelectric Efficiency in p-Type Ag(Pb1 –y...) | https://doi.org/10.1002/anie.201508492 (Tailoring of Electronic Structure and Thermoelectric Properties of a T...)
