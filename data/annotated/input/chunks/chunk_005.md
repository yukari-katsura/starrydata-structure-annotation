# Host systems -- chunk 005 of 73

Ranks 201-250 by sample count. These 50 host systems cover 1644 samples (3.16% of the TE set); cumulative through this chunk: 71.07%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Ga-Ge-Sr
- rank 201 | 38 samples | 12 papers | 31 compositions
- compositions: Sr8Ga16Ge30 (5); Sr7.44Ga15.54Si1.57Ge29.45 (2); Sr8Al0Ga16.5Ge29.5 (2); K7Sr17Ga40Ge96 (2); Sr14.8Ga28.6Ge56.6 (1); Sr14.5Ga30.2Ge55.3 (1)
- dopant candidates (<5% at.): Sn (5), K (4), In (3), Si (2)
- seed hypothesis (confirm): clathrate_i
- measured range: 11-933 K (5th-95th pct of 119 curves; full span incl. outliers 10-1003 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrGaGe P6_3/mmc (194) mp-1102705 [hull=0.000, icsd=1, PRIMARY]; SrGaGe P-6m2 (187) mp-1218272 [hull=0.005]
- papers: https://doi.org/10.1063/1.121747 (Semiconducting Ge clathrates: Promising candidates for thermoelectric ...) | https://doi.org/10.1063/1.2194187 (Thermoelectric properties of sintered clathrate compounds Sr8GaxGe46−x...) | https://doi.org/10.1063/1.3100205 (Synthesis and thermoelectric properties of type-VIII germanium clathra...)

## Sb-Sn-Te
- rank 202 | 38 samples | 14 papers | 34 compositions
- compositions: Sn12Sb2Te15 (2); Sn0.85Sb0.15Te (2); (Sn12Sb2Te15)44.09(NiTe2)55.91 (2); (Sn12Sb2Te15)81.11(NiTe2)18.89 (2); (Ag0.366Sb0.558Te)0.2(SnTe)0.8 (1); Sn0.067Sb0.667Te0.266 (1)
- dopant candidates (<5% at.): Ag (8), In (5), Ni (4), Cl (3), Zn (2), Bi (2)
- measured range: 291-874 K (5th-95th pct of 190 curves; full span incl. outliers 75-876 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sn(SbTe2)2 R-3m (166) mp-27947 [hull=0.726, icsd=2, PRIMARY]
- papers: https://doi.org/10.1002/chem.201102331 (Elemental Distribution and Thermoelectric Properties of Layered Tellur...) | https://doi.org/10.1002/aenm.201100460 (SnTe-AgSbTe2 Thermoelectric Alloys) | https://doi.org/10.1039/c6ee00728g (The origin of low thermal conductivity in Sn1−xSbxTe: phonon scatterin...)

## Ca-O-V
- rank 203 | 37 samples | 8 papers | 12 compositions
- compositions: CaVO3 (11); CaV1.01O2.81 (9); CaV0.9Ti0.1O3 (3); CaV0.8Ti0.2O3 (3); CaV0.95Ti0.05O3 (2); CaV0.98O2.81 (2)
- dopant candidates (<5% at.): Ti (8), Y (2), Mo (1)
- seed hypothesis (confirm): perovskite
- measured range: 13-999 K (5th-95th pct of 37 curves; full span incl. outliers 12-1123 K)
- [ref 1] TEDesignLab / ICSD: CaV2O6 C2/m (12) mp-32526 [hull=0.000, icsd=2, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: CaV3O7 Pnma (62) mp-19347 [hull=0.000, icsd=20, PRIMARY]; Ca5V3O13 P6_3/m (176) mp-1196692 [hull=0.002, icsd=2, PRIMARY]; Ca5V3ClO12 P6_3/m (176) mp-1202595 [hull=0.000, icsd=2, PRIMARY]; Ca2V2O7 P-1 (2) mp-32434 [hull=0.000, icsd=2, PRIMARY]; CaVO3 Pnma (62) mp-25150 [hull=0.002, icsd=2, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.69.245118 (X-ray diffraction, magnetic, and transport study of lattice instabilit...) | https://doi.org/10.1116/1.5001341 (Self-regulated growth of CaVO3 by hybrid molecular beam           epitaxy) | https://doi.org/10.1063/1.4798963 (Metal-insulator transition induced in CaVO3 thin films)

## Cr
- rank 204 | 37 samples | 9 papers | 31 compositions
- compositions: Cr (7); Cr0.967Fe0.033 (1); Cr0.992Fe0.018 (1); Cr0.951Fe0.049 (1); Cr99.1Si0.9 (1); Cr98.1Si1.9 (1)
- dopant candidates (<5% at.): Si (15), Mo (7), Fe (6), Al (5), Ni (4)
- seed hypothesis (confirm): solid_solution_alloy
- measured range: 12-689 K (5th-95th pct of 49 curves; full span incl. outliers 11-1260 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cr Im-3m (229) mp-90 [hull=0.000, icsd=11, PRIMARY]; Cr Pm-3n (223) mp-17 [hull=0.068, icsd=2]; Cr P6_3/mmc (194) mp-89 [hull=0.406, icsd=2]; Cr P4_2/mnm (136) mp-1192789 [hull=0.248, icsd=1]; Cr Cmcm (63) mp-1059289 [hull=0.306, icsd=1]
- papers: https://doi.org/10.1016/0031-8914(71)90095-4 (Thermoelectric power of antiferromagnetic chromium-iron alloys) | https://doi.org/10.1103/physrevb.8.2099 (Thermoelectric Power of Chromium below the Néel Temperature) | https://doi.org/10.1007/bf02737562 (Absolute thermoelectric power of chromium-silicon alloys)

## Mo-Sb-Te
- rank 205 | 37 samples | 9 papers | 25 compositions
- compositions: Mo3Sb5.4Te1.6 (5); Mo3Sb5.2Te1.8 (4); Ni0.05Mo3Sb5.4Te1.6 (4); Ni0.06Mo3Sb5.4Te1.6 (2); Mo3Sb6Te (2); MoSb5.4Te1.6 (1)
- dopant candidates (<5% at.): Ni (16), Fe (4), Si (3), C (3), O (3), Al (3), Mn (1), Co (1)
- seed hypothesis (confirm): ir3ge7
- measured range: 11-997 K (5th-95th pct of 171 curves; full span incl. outliers 10-1050 K)
- papers: https://doi.org/10.1021/cm0708517 (Thermoelectric Properties of Re3Ge0.6As6.4and Re3GeAs6in Comparison to...) | https://doi.org/10.1039/c1ee01406d (Optimized thermoelectric properties of Mo3Sb7−xTex with significant ph...) | https://doi.org/10.1016/j.jallcom.2006.03.030 (High temperature thermoelectric properties of Mo3Sb7−xTex for x=1.6 an...)

## Al-O
- rank 206 | 36 samples | 17 papers | 15 compositions
- compositions: Al2O3 (18); (Al2O3)87.45(SiO2)12.55 (4); (Al2O3)93(CaO)3.88(MgO)2.45(SiO2)0.2(Na2O)0.4(Fe2O3)0.06(TiO2)0.01 (2); (Al2O3)80.5(CaO)3.25(MgO)14.48(SiO2)0.46(Na2O)0.44(Fe2O3)0.02(TiO2)0.85 (1); (Al2O3)81.62(CaO)2.28(MgO)15.2(SiO2)0.4(Na2O)0.46(Fe2O3)0.03(TiO2)0.01 (1); (Al2O3)88.33(ZrO2)11.67 (1)
- dopant candidates (<5% at.): Mg (9), Si (8), La (6), Ca (4), Na (4), Fe (4), Ti (4), Nd (3), Sc (3), Zr (1), Y (1), Ce (1), Zn (1)
- seed hypothesis (confirm): corundum
- measured range: 20-1278 K (5th-95th pct of 59 curves)
- [ref 1] TEDesignLab / ICSD: Al2O3 R-3c (167) mp-1143 [hull=0.000, icsd=76, PRIMARY]; Al2O3 Pbcn (60) mp-1938 [hull=0.093, icsd=4]; Al2O3 C2/m (12) mp-7048 [hull=0.009, icsd=1]; Al2O3 P2/c (13) mp-759943 [hull=0.033]
- [ref 2] MP, ranked by ICSD evidence: AlO2 Cmcm (63) mp-1096799 [hull=0.292, icsd=15, PRIMARY]; NaAl11O17 P6_3/mmc (194) mp-3405 [hull=0.000, icsd=5, PRIMARY]; SrAl12O19 P6_3/mmc (194) mp-6995 [hull=0.003, icsd=3, PRIMARY]; AlO3 P-31m (162) mp-1182868 [hull=0.647, icsd=2, PRIMARY]; CaZrAl9BO18 P6_3 (173) mp-1197323 [hull=0.003, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2012.12.091 (The influence of α- and γ-Al2O3 phases on the thermoelectric propertie...) | https://doi.org/10.1002/aenm.201301927 (Enhanced Thermoelectric Power Factor of NaxCoO2Thin Films by Structura...) | https://doi.org/10.1063/1.1513188 (Transport and structural properties of binary skutterudite CoSb3 thin ...)

## Bi-Ce-Pd
- rank 207 | 36 samples | 1 papers | 1 compositions
- compositions: Ce3Bi4Pd3 (36)
- seed hypothesis (confirm): y3au3sb4
- measured range: 10-40 K (5th-95th pct of 38 curves; full span incl. outliers 10-300 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeBiPd F-43m (216) mp-604453 [hull=0.000, icsd=2, PRIMARY]; Ce4Bi8Pd3 P-4m2 (115) mp-1226947 [hull=0.012, PRIMARY]
- papers: https://doi.org/10.1038/s41467-019-13421-w (Magnetic field-tuned Fermi liquid in a Kondo insulator)

## Co-O
- rank 208 | 36 samples | 11 papers | 18 compositions
- compositions: CoO2 (5); Co3Co3.8In0.2O9 (4); Co3Co3.9In0.1O9 (4); Co3O4 (3); CoO (3); Na0.09CoO2 (2)
- dopant candidates (<5% at.): In (8), Ti (4), Na (2), Pr (2), La (2), Nd (2), Ba (2), Sr (2), Ca (2), Cu (2), Li (1)
- measured range: 11-1134 K (5th-95th pct of 42 curves)
- [ref 1] TEDesignLab / ICSD: CoO F-43m (216) mp-715460 [hull=0.000, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: Co3O4 Fd-3m (227) mp-18748 [hull=0.000, icsd=26, PRIMARY]; CoO Fm-3m (225) mp-19079 [hull=0.020, icsd=23, PRIMARY]; CoO2 R-3m (166) mp-715480 [hull=0.014, icsd=6, PRIMARY]; CoO4 P2_1/m (11) mp-1079523 [hull=0.572, icsd=1, PRIMARY]; Co21O40 I-4 (82) mp-851287 [hull=0.064, PRIMARY]
- papers: https://doi.org/10.1109/14.68226 (Correlation between thermal expansion and Seebeck coefficient in polyc...) | https://doi.org/10.1109/ict.2006.331228 (P-type thermoelectric properties of sintered (NiyCo1-y)xFe3-xO4 with s...) | https://doi.org/10.1143/jjap.44.l966 (Control of Epitaxial Growth Orientation and Anisotropic Thermoelectric...)

## Fe
- rank 209 | 36 samples | 10 papers | 10 compositions
- compositions: Fe (21); Fe99.08C0.32Si0.01Mn0.49P0.02Al0.07Nb0.01 (3); Fe96.12C2.19Si0.58Mn0.72P0.11Cr0.24Ni0.05 (3); Fe98.95C0.32Si0.03Mn0.59P0.03Al0.07Nb0.01 (3); Fe22Cr (1); Fe99.603Si0.397 (1)
- dopant candidates (<5% at.): Si (13), Mn (10), C (10), P (9), Al (6), Nb (6), Cr (5), Ni (3), Mo (1)
- seed hypothesis (confirm): solid_solution_alloy
- measured range: 18-2194 K (5th-95th pct of 49 curves; full span incl. outliers 14-2285 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe Fm-3m (225) mp-150 [hull=0.148, icsd=46, PRIMARY]; Fe Im-3m (229) mp-13 [hull=0.000, icsd=31]; Fe P6_3/mmc (194) mp-136 [hull=0.080, icsd=12]; Fe P4_2/mnm (136) mp-1194030 [hull=0.170, icsd=1]; Fe P6/mmm (191) mp-1096950 [hull=0.492]
- papers: https://doi.org/10.1016/j.jallcom.2013.08.096 (Characterization of the interface between an Fe–Cr alloy and the p-typ...) | https://doi.org/10.1007/s11664-012-2457-z (Characterization of the Thermoelectric Behavior of Plastically Deforme...) | https://doi.org/10.1063/1.1145257 (Highly sensitive method for simultaneous measurements of thermal condu...)

## Ga-Ru
- rank 210 | 36 samples | 9 papers | 28 compositions
- compositions: Ga67Ru33 (4); RuGa3 (4); Ga66.6Ru33.4 (2); RuGa2 (2); Ga66.2Ru33.8 (1); Ga66.4Ru33.6 (1)
- dopant candidates (<5% at.): Re (6), Ir (4), Zn (3)
- seed hypothesis (confirm): fega3
- measured range: 60-975 K (5th-95th pct of 149 curves; full span incl. outliers 10-983 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ga2Ru Fddd (70) mp-1072429 [hull=0.000, icsd=2, PRIMARY]; Ga3Ru P4_2/mnm (136) mp-672204 [hull=0.000, icsd=2, PRIMARY]; GaRu Pm-3m (221) mp-22320 [hull=0.000, icsd=1, PRIMARY]; Ga2Ru Fd-3m (227) mp-1213370 [hull=0.399]
- papers: https://doi.org/10.1016/j.jallcom.2010.07.204 (Composition dependence of thermoelectric properties of binary narrow-g...) | https://doi.org/10.1063/1.1803947 (Thermoelectric properties of semiconductorlike intermetallic compounds...) | https://doi.org/10.1063/1.4729772 (Thermoelectric properties of FeGa3-type narrow-bandgap intermetallic c...)

## La-O-Sr-Ti
- rank 211 | 36 samples | 9 papers | 20 compositions
- compositions: Sr0.5La0.33TiO3 (7); Sr0.3La0.47TiO3 (7); La0.3Sr0.7TiO3 (5); Sr0.5La0.5TiO3 (1); Sr2.7LaTi2O7 (1); Sr0.6La0.4TiO3 (1)
- dopant candidates (<5% at.): Sc (4), Ce (4), Ag (1)
- measured range: 72-1273 K (5th-95th pct of 53 curves; full span incl. outliers 11-1273 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr14La6Mg3Ti17O60 Cm (8) mp-686467 [hull=0.007, PRIMARY]; Sr2La3Ti2O10 P2_1/m (11) mp-1208909 [hull=0.055, PRIMARY]; Sr4LaTi5O15 C2/m (12) mp-1218562 [hull=0.000, PRIMARY]; Sr9LaTi10O30 P-1 (2) mp-695042 [hull=0.000, PRIMARY]; SrLa2Ti3O9 P-3m1 (164) mp-1218904 [hull=0.023, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/21/43/435603 (Correlation and phonon effects for the electronic transport and thermo...) | https://doi.org/10.1016/s1002-0721(14)60073-9 (Thermoelectric properties of Sr0.9La0.1TiO3 and Sr2.7La0.3Ti2O7 with 1...) | https://doi.org/10.1021/acs.chemmater.5b04616 (High-Figure-of-Merit Thermoelectric La-Doped A-Site-Deficient SrTiO3Ce...)

## B-Yb
- rank 212 | 35 samples | 3 papers | 6 compositions
- compositions: YbB6 (30); YbB5.7 (1); YbB5.9 (1); YbB6.1 (1); YbB6.3 (1); Tm0.2Yb0.8B12 (1)
- dopant candidates (<5% at.): Tm (1)
- seed hypothesis (confirm): cab6_hexaboride
- measured range: 11-1050 K (5th-95th pct of 42 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbB6 Pm-3m (221) mp-419 [hull=0.000, icsd=8, PRIMARY]; YbB12 Fm-3m (225) mp-1103888 [hull=0.083, icsd=3, PRIMARY]; YbB2 P6/mmm (191) mp-10145 [hull=0.140, icsd=2, PRIMARY]; YbB4 P4/mbm (127) mp-1189298 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1088/1757-899x/20/1/012007 (Thermoelectric and electrical properties of p-type YbB6) | https://doi.org/10.1134/s0021364009050099 (Antiferromagnetic instability and the metal-insulator transition in Tm...) | https://doi.org/10.1103/physrevb.97.121101 (Coexistence of metallic and insulating channels in compressed \nYbB6)

## Co-Nb-Sb
- rank 213 | 35 samples | 11 papers | 25 compositions
- compositions: NbCoSb (9); Nb0.85CoSb (3); V0.12Nb0.88CoSb (1); NbCo1.3Sb (1); Ta0.12Nb0.88CoSb (1); NbCo1.2Sb (1)
- dopant candidates (<5% at.): Ni (4), Sn (2), V (1), Ta (1), Hf (1), Ti (1), Zr (1)
- seed hypothesis (confirm): half_heusler
- measured range: 27-1129 K (5th-95th pct of 146 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NbCoSb F-43m (216) mp-31460 [hull=0.017, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.materresbull.2015.06.022 (A new n-type half-Heusler thermoelectric material NbCoSb) | https://doi.org/10.1039/c5ra21404a (Thermal conductivity reduction by isoelectronic elements V and Ta for ...) | https://doi.org/10.3390/ma11050773 (The Effects of Excess Co on the Phase Composition and Thermoelectric P...)

## Ga-O-Zn
- rank 214 | 35 samples | 6 papers | 9 compositions
- compositions: Ga2O3(ZnO)9 (12); (GaO1.5)0.18(ZnO)0.82 (5); (Ga0.8In0.2)2O3(ZnO)9 (5); (Ga0.6In0.4)2O3(ZnO)9 (5); (Ga2O3(ZnO)9)97.42(B2O3)2.58 (4); Ga2O3(ZnO)13 (1)
- dopant candidates (<5% at.): In (10), B (4)
- seed hypothesis (confirm): homologous_inmo3_zno
- measured range: 303-1060 K (5th-95th pct of 69 curves)
- [ref 1] TEDesignLab / ICSD: Zn(GaO2)2 Fd-3m (227) mp-5794 [hull=0.000, icsd=13, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: ZnGaO3 Pm-3m (221) mp-971733 [hull=0.731, PRIMARY]
- papers: https://doi.org/10.1039/c1ra00315a (Electrical, optical, and thermoelectric properties of Ga2O3(ZnO)9) | https://doi.org/10.1063/1.4729560 (An enhancement of a thermoelectric power factor in a Ga-doped ZnO syst...) | https://doi.org/10.1016/j.jeurceramsoc.2016.02.017 (Thermoelectric transport properties of naturally nanostructured Ga–ZnO...)

## Mn-Nd-O-Sr
- rank 215 | 35 samples | 13 papers | 17 compositions
- compositions: Nd0.7Sr0.3MnO3 (12); Nd0.67Sr0.33MnO3 (7); (La0.25Nd0.75)0.7Sr0.3MnO3 (2); Nd0.65Sr0.35MnO3 (1); Nd0.50Sr0.50MnO3 (1); Nd0.43Sr0.57MnO3 (1)
- dopant candidates (<5% at.): Cu (5), La (4), Ce (1)
- measured range: 10-368 K (5th-95th pct of 43 curves; full span incl. outliers 10-1325 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2NdMn2O7 I4/mmm (139) mp-1218717 [hull=0.009, PRIMARY, AMBIGUOUS]; Sr2NdMn3O9 C2/c (15) mp-1218797 [hull=0.007, PRIMARY]; Sr3NdMn2O8 Amm2 (38) mp-1218352 [hull=0.000, PRIMARY]; Sr4NdMn5O15 C2/m (12) mp-1218675 [hull=0.027, PRIMARY]; SrNd2Mn3O9 Pnma (62) mp-1218259 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1063/1.3191680 (Magnon drag contribution to thermopower of Nd0.67Sr0.33MnO3 nanocrysta...) | https://doi.org/10.1016/j.jmmm.2003.12.1048 (Thermoelectric properties of filling controlled manganites) | https://doi.org/10.1063/1.2976365 (Strain enhanced spin polarization in Nd0.43Sr0.57MnO3/YBa2Cu3O7 bilayers)

## S-Se-Sn
- rank 216 | 35 samples | 7 papers | 17 compositions
- compositions: SnS0.5Se0.5 (5); SnS0.8Se0.2 (5); SnS0.2Se0.8 (3); SnSe0.7S0.3 (3); Na0.02Sn0.98S0.5Se0.5 (2); SnS0.6Se0.4 (2)
- dopant candidates (<5% at.): Na (9), I (2)
- seed hypothesis (confirm): layered_ges
- solid-solution axis: S/(S+Se) spans 0.10-0.90 (median 0.50) over 17 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 301-917 K (5th-95th pct of 175 curves)
  !! MEASUREMENT CROSSES A TRANSITION: layered_ges -> cmcm_snse_ht at ~800 K (Pnma -> Cmcm, ~800 K for SnSe and ~880 K for SnS; the high-ZT regime.)
     Record each phase with its own temperature range, not a single prototype.
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sn2SeS Pmc2_1 (26) mp-1218960 [hull=0.008, PRIMARY]; Sn2SeS2 Pnma (62) mp-1219003 [hull=0.019, PRIMARY]; SnSeS P3m1 (156) mp-1218912 [hull=0.017, PRIMARY]
- papers: https://doi.org/10.1002/aenm.201500360 (Studies on Thermoelectric Properties of n-type Polycrystalline SnSe1-x...) | https://doi.org/10.1039/c4ta06955b (Thermoelectric performance of SnS and SnS–SnSe solid solution) | https://doi.org/10.1038/srep43262 (Thermoelectric SnS and SnS-SnSe solid solutions prepared by mechanical...)

## Al-Fe
- rank 217 | 34 samples | 9 papers | 13 compositions
- compositions: Al13Fe4_DAC (9); Al13Fe4 (4); Al76.5Fe21.3Ni2.2 (3); Fe4Al9.7 (2); Fe3Al (2); Fe4Al9.0 (2)
- dopant candidates (<5% at.): Ni (3), V (1)
- seed hypothesis (confirm): quasicrystal_approximant
- measured range: 10-976 K (5th-95th pct of 46 curves; full span incl. outliers 10-1276 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlFe Pm-3m (221) mp-2658 [hull=0.000, icsd=9, PRIMARY]; AlFe3 Fm-3m (225) mp-2018 [hull=0.000, icsd=4, PRIMARY]; Al8Fe5 I-43m (217) mp-1193259 [hull=0.033, icsd=3, PRIMARY]; Al9Fe2 P2_1/c (14) mp-1191778 [hull=0.000, icsd=1, PRIMARY]; Al12Fe7 P-1 (2) mp-1214901 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(02)00919-2 (High temperature thermoelectric properties of (Fe1−xVx)3Al Heusler typ...) | https://doi.org/10.2320/jinstmet.jaw201504 (Effect of Anomalous Crystal Structure of Iron Aluminides Fe<sub>2</sub...) | https://doi.org/10.1088/0953-8984/15/6/314 (Thermal and electrical transport properties of ordered FeAl2)

## As-Fe-Nd-O
- rank 218 | 34 samples | 4 papers | 20 compositions
- compositions: NdFeAsO0.89F0.11 (4); NdFe0.98Ru0.02AsO0.89F0.11 (3); NdFe0.99Ru0.01AsO0.89F0.11 (3); NdFe0.85Ru0.15AsO0.89F0.11 (3); NdFe0.9Ru0.1AsO0.89F0.11 (3); NdFe0.955Ru0.045AsO0.89F0.11 (2)
- dopant candidates (<5% at.): F (25), Ru (21), Rh (7)
- seed hypothesis (confirm): zrcusias_1111
- measured range: 11-300 K (5th-95th pct of 34 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NdFeAsO P4/nmm (129) mp-622621 [hull=0.141, icsd=9, PRIMARY]; Nd2FeAs2O P4/mmm (123) mp-1209831 [hull=1.595, PRIMARY]; SrNd5Fe6(AsO)6 P-1 (2) mp-694989 [hull=0.172, PRIMARY]; SrNd7Fe8(AsO)8 I4mm (107) mp-705458 [hull=0.162, PRIMARY]
- papers: https://doi.org/10.1016/j.physc.2009.04.013 (Thermoelectric power of RFeAsO (R=Ce, Pr, Nd, Sm and Gd)) | https://doi.org/10.1143/jpsj.79.023702 (Effects of Ru Doping on the Transport Behavior and Superconducting Tra...) | https://doi.org/10.1103/physrevb.79.212502 (Evidence of spin-density-wave order inRFeAsO1−xFxfrom measurements of ...)

## Ba-O-Sn
- rank 219 | 34 samples | 11 papers | 16 compositions
- compositions: BaSnO3 (11); Ba0.95La0.05SnO3 (6); Ba0.9La0.1SnO3 (3); Ba0.99La0.01SnO3 (2); BaSn0.95Co0.05O3 (1); BaSn0.9Co0.1O3 (1)
- dopant candidates (<5% at.): La (18), Co (4), Sr (1), Gd (1)
- seed hypothesis (confirm): perovskite
- measured range: 11-1074 K (5th-95th pct of 52 curves)
- [ref 1] TEDesignLab / ICSD: BaSnO3 Pm-3m (221) mp-3163 [hull=0.000, icsd=11, PRIMARY]; Ba2SnO4 I4/mmm (139) mp-3359 [hull=0.000, icsd=4, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ba3SnO Pm-3m (221) mp-29243 [hull=0.000, icsd=2, PRIMARY]; Ba2SnO16 P-1 (2) mp-1182572 [hull=0.363, PRIMARY]; Ba3Sn2O7 Cmcm (63) mp-770846 [hull=0.000, PRIMARY]; Ba4Sn3O10 Cmce (64) mp-768510 [hull=0.006, PRIMARY]; BaSnO3 Imma (74) mp-1178513 [hull=0.000]
- papers: https://doi.org/10.2497/jjspm.54.639 (Preparation of Semiconductive La-Doped BaSnO3 by a Polymerized Complex...) | https://doi.org/10.2497/jjspm.56.555 (High-Temperature Thermoelectric Properties of La-Doped Ba1-xSrxSnO3 Ce...) | https://doi.org/10.2497/jjspm.58.149 (Thermoelectric Properties of P -Type BaSnO3 Ceramics Doped with Cobalt)

## Bi-Cu-Se
- rank 220 | 34 samples | 6 papers | 24 compositions
- compositions: Cu1.6915Zn0.0085Bi4.7Se8 (2); Cu1.6745Zn0.0255Bi4.7Se8 (2); Cu1.6745In0.0255Bi4.7Se8 (2); Cu1.7Bi4.6745Zn0.0255Se8 (2); Cu1.7Bi4.6745In0.0255Se8 (2); Cu1.7Bi4.7Se8 (2)
- dopant candidates (<5% at.): Zn (8), In (8), I (2)
- measured range: 82-771 K (5th-95th pct of 130 curves; full span incl. outliers 11-775 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu6BiSe6 Pnma (62) mp-1199896 [hull=0.021, icsd=1, PRIMARY]; CuBiSe2 R-3m (166) mp-1225678 [hull=0.112, PRIMARY]
- papers: https://doi.org/10.1021/ic5014945 (Effects of Doping on Transport Properties in Cu–Bi–Se-Based Thermoelec...) | https://doi.org/10.1039/c3ta11457k (Cu–Bi–Se-based pavonite homologue: a promising thermoelectric material...) | https://doi.org/10.1155/2013/502150 (Electronic and Thermal Transport Properties of Complex Structured Cu-B...)

## Cr-N
- rank 221 | 34 samples | 10 papers | 16 compositions
- compositions: CrN (17); Cr0.975V0.025N (2); Cr0.95V0.05N (2); CrO0.09N0.91 (1); Cr0.975Mo0.025N (1); Cr0.97Mo0.01W0.02N (1)
- dopant candidates (<5% at.): V (4), Mo (3), W (3), O (1), Al (1), Si (1)
- seed hypothesis (confirm): rocksalt_nitride_carbide
- measured range: 10-847 K (5th-95th pct of 80 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CrN Fm-3m (225) mp-1000440 [hull=0.137, icsd=14, PRIMARY]; Cr2N P-31m (162) mp-8780 [hull=0.000, icsd=1, PRIMARY]; Cr3N2 R-3c (167) mp-1096882 [hull=0.014, PRIMARY]; Cr3N4 P6_3/m (176) mp-1014345 [hull=0.042, PRIMARY]; CrN2 Pnnm (58) mp-1080200 [hull=0.137, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2010.10.046 (Magnetic influence on thermoelectric properties of CrO0.1N0.9) | https://doi.org/10.1063/1.3120280 (Thermoelectric properties of stoichiometric and hole-doped CrN) | https://doi.org/10.1063/1.4861845 (Thermoelectric properties of heavy-element doped CrN)

## Fe-Ga
- rank 222 | 34 samples | 9 papers | 27 compositions
- compositions: FeGa3 (7); Fe0.95Co0.05Ga3 (2); FeGa2.85Ge0.15 (1); FeGa2.90Al0.10 (1); FeGa2.94In0.06 (1); FeGa2.97Zn0.03 (1)
- dopant candidates (<5% at.): Co (9), Ge (7), Sn (3), Al (2), In (2), Zn (2)
- seed hypothesis (confirm): fega3
- measured range: 11-872 K (5th-95th pct of 129 curves; full span incl. outliers 10-963 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ga3Fe P4_2/mnm (136) mp-636368 [hull=0.000, icsd=6, PRIMARY]; GaFe3 Pm-3m (221) mp-19870 [hull=0.000, icsd=4, PRIMARY]; GaFe P-6m2 (187) mp-1224926 [hull=0.120, PRIMARY]; GaFe2 Fmmm (69) mp-1224880 [hull=0.147, PRIMARY]; GaFe4 Fmmm (69) mp-1224889 [hull=0.114, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2004.09.035 (Electrical and thermoelectric properties of the intermetallic FeGa3) | https://doi.org/10.1063/1.1803947 (Thermoelectric properties of semiconductorlike intermetallic compounds...) | https://doi.org/10.1063/1.4938474 (Improved thermoelectric properties in heavily doped FeGa3)

## Ba-Bi-O-Pb
- rank 223 | 33 samples | 3 papers | 20 compositions
- compositions: BaPb0.7Bi0.3O3 (2); BaPb0.65Bi0.35O3 (2); BaPb0.6Bi0.4O3 (2); Ba0.8Sr0.2Pb0.7Bi0.3O3 (2); Ba0.8Sr0.2Pb0.6Bi0.4O3 (2); Ba0.8Sr0.2Pb0.55Bi0.45O3 (2)
- dopant candidates (<5% at.): Sr (19), K (1)
- measured range: 11-300 K (5th-95th pct of 33 curves; full span incl. outliers 10-877 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba3Bi2PbO9 C2/m (12) mp-1228435 [hull=0.001, PRIMARY]; Ba3BiPb2O9 P-1 (2) mp-1228457 [hull=0.006, PRIMARY]; Ba4Bi(PbO4)3 C2/m (12) mp-1228269 [hull=0.000, PRIMARY, AMBIGUOUS]; Ba4Bi3PbO12 C2/m (12) mp-1228338 [hull=0.000, PRIMARY]; Ba5BiPb4O15 C2/m (12) mp-1228869 [hull=0.000, PRIMARY, AMBIGUOUS]
- papers: https://doi.org/10.1016/s0921-4534(99)00539-0 (Metal–insulator transition and superconductivity in Sr- and La-substit...) | https://doi.org/10.1103/physrevb.51.576 (Coexistence of electrons and holes inBaBi0.25Pb0.75O3−δdetected by the...) | https://doi.org/10.1016/j.jallcom.2014.12.274 (Hydrothermal synthesis of a new Bi-based (Ba0.82K0.18)(Bi0.53Pb0.47)O3...)

## Ba-Co-O-Y
- rank 224 | 33 samples | 8 papers | 22 compositions
- compositions: YBaCo4O7 (6); YBaCo2O5 (2); YBaCo3.7Zn0.3O7 (2); YBaCo3.8Zn0.2O7 (2); YBaCo3.8Al0.2O7 (2); YBaCo3.8Ga0.2O7 (2)
- dopant candidates (<5% at.): Ag (4), Ga (4), Al (4), Zn (4), Ca (3)
- seed hypothesis (confirm): swedenborgite
- measured range: 11-1000 K (5th-95th pct of 51 curves; full span incl. outliers 10-1123 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaYCo4O7 Cmc2_1 (36) mp-1194048 [hull=0.016, icsd=5, PRIMARY, AMBIGUOUS]; BaYCo2O5 P4/mmm (123) mp-24839 [hull=0.067, icsd=5, PRIMARY]; Ba6Y2Co4O15 P2/c (13) mp-1196872 [hull=0.000, icsd=2, PRIMARY]; BaY(CoO2)4 Pca2_1 (29) mp-646218 [hull=0.072, icsd=1, PRIMARY]; Ba2YCoO5 P2_1/c (14) mp-1205054 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/s12034-008-0137-7 (A novel method to control oxygen stoichiometry and thermoelectric prop...) | https://doi.org/10.1007/s11664-013-2631-y (Thermoelectric Properties of Y1−x Ag x BaCo4O7+δ Ceramics) | https://doi.org/10.1016/j.physb.2006.03.089 (Electronic transport and thermoelectric properties of RBaCo4O7 (R=Dy, ...)

## Ce-Co-Fe-Sb
- rank 225 | 33 samples | 13 papers | 17 compositions
- compositions: Ce0.9CoFe3Sb12 (7); CeFe3CoSb12 (6); Ce0.9Fe3CoSb12 (6); (CeFe3CoSb12)0.8(FeSb2)0.2 (1); (CeFe3CoSb12)0.9(FeSb2)0.1 (1); (BaFe12O19)0.001CeFe3CoSb12 (1)
- dopant candidates (<5% at.): O (6), Ba (4), Sn (3), Mo (2)
- seed hypothesis (confirm): skutterudite, filled_skutterudite  <-- MIXED, split per composition
- measured range: 77-821 K (5th-95th pct of 131 curves; full span incl. outliers 18-824 K)
- papers: https://doi.org/10.2497/jjspm.54.15 (Thermoelectric Properties of CeFe3CoSb12-FeSb2 Composite) | https://doi.org/10.1016/j.jallcom.2010.06.040 (Thermoelectric properties of rare earths filled CoSb3 based nanostruct...) | https://doi.org/10.1063/1.4740072 (Thermoelectric properties and Kondo behavior in indium incorporated p-...)

## Cu-Mn-Te
- rank 226 | 33 samples | 4 papers | 26 compositions
- compositions: Cu4Mn2Te4 (7); Cu4Mn2.1Te4 (2); Cu4.3Mn2Te4 (1); Cu3.7Zn0.3Mn2Te4 (1); Cu4Mn1.7Fe0.3Te4 (1); Cu3.9In0.1Mn2Te4 (1)
- dopant candidates (<5% at.): In (6), Cl (3), Co (3), Ni (3), Zn (1), Fe (1)
- measured range: 297-840 K (5th-95th pct of 129 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn(CuTe)2 F-43m (216) mp-1222078 [hull=0.015, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2018.04.214 (Single parabolic band behavior of thermoelectric p-type Cu4Mn2Te4) | https://doi.org/10.1021/acs.inorgchem.8b00301 (Thermoelectric Properties of Variants of Cu4Mn2Te4 with Spinel-Related...) | https://doi.org/10.1039/c7dt03223d (Enhanced thermoelectric performance in ternary spinel Cu4Mn2Te4via the...)

## Hf-Ni-Sn
- rank 227 | 33 samples | 18 papers | 11 compositions
- compositions: HfNiSn (20); HfNiSn0.98Sb0.02 (2); HfNiSn0.99In0.01 (2); HfNiSn0.995In0.005 (2); Hf0.9Zr0.1NiSn (1); Hf0.70Zr0.15Ti0.15NiSn0.975Sb0.025 (1)
- dopant candidates (<5% at.): Sb (4), Zr (4), In (4), Ti (3)
- seed hypothesis (confirm): half_heusler
- measured range: 10-1076 K (5th-95th pct of 96 curves; full span incl. outliers 10-1128 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HfNi2Sn Fm-3m (225) mp-4828 [hull=0.047, icsd=2, PRIMARY]; HfNiSn F-43m (216) mp-924128 [hull=0.000, icsd=1, PRIMARY]; Hf5NiSn3 P6_3/mcm (193) mp-1212523 [hull=0.020, icsd=1, PRIMARY]; Hf2Ni2Sn P4/mbm (127) mp-646507 [hull=0.021, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2009.02.026 (High-performance half-Heusler thermoelectric materials Hf1−x ZrxNiSn1−...) | https://doi.org/10.1007/s11837-014-1233-3 (Ordered Structures and Thermoelectric Properties of MNiSn (M = Ti, Zr,...) | https://doi.org/10.1007/s11664-009-1032-8 (Reduced Grain Size and Improved Thermoelectric Properties of Melt Spun...)

## Ba-Co-Fe-O
- rank 228 | 32 samples | 12 papers | 22 compositions
- compositions: BaCo0.4Fe0.4Zr0.1Y0.1O3 (9); BaCo0.4Fe0.4Y0.2O3 (2); BaCo0.4Fe0.4Zn0.1Y0.1O3 (2); Ba2Co2Fe11.6Ti0.2Mn0.2O22 (1); Ba2Co2Fe12O22 (1); Ba2Co2Fe10.4Ti0.8Mn0.8O22 (1)
- dopant candidates (<5% at.): Y (20), Zr (13), Ti (6), Mn (5), Mg (2), Zn (2), La (2), Sn (1), Nb (1), Pr (1), Nd (1)
- measured range: 299-1175 K (5th-95th pct of 38 curves)
- papers: https://doi.org/10.1039/c3nj00309d (Electrical and thermoelectric attributes of Ba2Co2Fe12−2x(Ti–Mn)xO22 a...) | https://doi.org/10.1016/j.ssi.2023.116203 (Oxygen non-stoichiometry and mixed conductivity of Ti -doped BaCo0.4Fe...) | https://doi.org/10.1016/j.ceramint.2021.12.200 (Phase stability and hydrogen permeation performance of BaCo0·4Fe0·4Zr0...)

## Bi-Cu-O-Se-Y
- rank 229 | 32 samples | 3 papers | 5 compositions
- compositions: Bi2YO4Cu2Se2 (12); Bi2YO4Cu2Se1.9I0.1 (5); Bi2YO4Cu2Se1.85I0.15 (5); Bi2YO4Cu2Se1.8I0.2 (5); Bi2YO4Cu2Se1.95I0.05 (5)
- dopant candidates (<5% at.): I (20)
- seed hypothesis (confirm): zrcusias_1111
- measured range: 14-882 K (5th-95th pct of 33 curves)
- papers: https://doi.org/10.1002/ejic.201500159 (Semiconducting BiOCuSe Thermoelectrics and Its Metallic Derivative Bi2...) | https://doi.org/10.1016/j.jssc.2016.03.032 (Electrical and thermal transport properties of layered Bi 2 YO 4 Cu 2 ...) | https://doi.org/10.1103/physrevb.90.085144 (CuSe-based layered compoundBi2YO4Cu2Se2as a quasi-two-dimensional metal)

## Mn-O-Sm-Sr
- rank 230 | 32 samples | 8 papers | 7 compositions
- compositions: Sm0.55Sr0.45MnO3 (25); Sm0.50Sr0.50MnO3 (2); Sm0.56Sr0.44MnO3 (1); Sm0.45Ce0.1Sr0.45MnO3 (1); Sm0.5Ce0.05Sr0.45MnO3 (1); Sm0.5Sr0.5MnO3 (1)
- dopant candidates (<5% at.): Ce (2), Ag (1)
- measured range: 12-328 K (5th-95th pct of 32 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrSm3Mn4O12 Pm (6) mp-1218118 [hull=0.000, PRIMARY]; SrSmMn2O6 Pmn2_1 (31) mp-1217787 [hull=0.006, PRIMARY]
- papers: https://doi.org/10.1016/j.jmmm.2015.08.033 (Connection of thermopower and giant magnetothermopower with magnetic a...) | https://doi.org/10.1088/0953-8984/20/7/075221 (Phase separation and stability in Sm0.50Sr0.50MnO3: effects of cation ...) | https://doi.org/10.1016/s0921-4526(00)00483-x (Time-resolved thermoelectrical effect in Sm0.56Sr0.44MnO3 perovskite)

## Ca-La-Mn-O-Pr
- rank 231 | 31 samples | 3 papers | 6 compositions
- compositions: LaPrCaMn3O9 (9); La0.275Pr0.35Ca0.375MnO3 (8); La0.375Pr0.25Ca0.375MnO3 (7); La0.325Pr0.3Ca0.375MnO3 (3); La0.25Pr0.375Ca0.375MnO3 (3); La0.325Pr0.30Ca0.375MnO3 (1)
- solid-solution axis: La/(La+Pr) spans 0.40-0.60 (median 0.52) over 6 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-334 K (5th-95th pct of 35 curves)
- papers: https://doi.org/10.1103/physrevlett.84.2961 (Thermal and Electronic Transport Properties and Two-Phase Mixtures inL...) | https://doi.org/10.1073/pnas.1920502117 (Direct experimental evidence of physical origin of electronic phase se...) | https://doi.org/10.1063/1.2786570 (Competition between coexisting phases in (La,Pr)CaMnO3 manganites)

## Ca-Mn-O-Sr
- rank 232 | 31 samples | 5 papers | 15 compositions
- compositions: Ca0.45Sr0.4Ho0.15MnO3 (5); Ca0.5Sr0.4Ho0.1MnO3 (5); Ca0.55Sr0.4Ho0.05MnO3 (5); Ca0.7Sr0.3Mn0.96Mo0.04O3 (3); Ca0.4Sr0.6Mn0.96Mo0.04O3 (3); Ca0.5Sr0.5MnO3 (1)
- dopant candidates (<5% at.): Ho (19), Mo (9), Pb (4)
- solid-solution axis: Ca/(Ca+Sr) spans 0.25-0.75 (median 0.56) over 15 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 11-1189 K (5th-95th pct of 59 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2Ca2NdMn5O15 P1 (1) mp-1219128 [hull=0.029, PRIMARY]; Sr2Ca6Mn7FeO20 P1 (1) mp-1099810 [hull=0.061, PRIMARY]; Sr2Ca6Mn7FeO24 Amm2 (38) mp-1099788 [hull=0.095, PRIMARY]; Sr2Ca6TiMn7O20 P1 (1) mp-1076877 [hull=0.061, PRIMARY]; Sr2Ca6TiMn7O24 Amm2 (38) mp-1099702 [hull=0.090, PRIMARY]
- papers: https://doi.org/10.1039/c5tc02318a (Crystal structure and thermoelectric properties of Sr–Mo substituted C...) | https://doi.org/10.1063/1.3505756 (Cosubstitution effect on the magnetic, transport, and thermoelectric p...) | https://doi.org/10.1016/j.jssc.2005.01.025 (Influence of A-site cation size on structural and physical properties ...)

## Cd-Sb-Yb
- rank 233 | 31 samples | 10 papers | 18 compositions
- compositions: YbCd2Sb2 (14); YbCd1.85Mn0.15Sb2 (1); YbCd1.95Mn0.05Sb2 (1); YbCd1.8Mn0.2Sb2 (1); YbCd1.9Mn0.1Sb2 (1); Yb0.8Ca0.2Cd2Sb2 (1)
- dopant candidates (<5% at.): Na (5), Mn (4), Mg (2), Zn (2), Ca (1)
- seed hypothesis (confirm): caal2si2_zintl
- measured range: 298-700 K (5th-95th pct of 132 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(CdSb)2 P-3m1 (164) mp-9257 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1063/1.3040321 (Synthesis and high thermoelectric efficiency of Zintl phase YbCd2−xZnxSb2) | https://doi.org/10.1002/ejic.201100282 (Enhanced Thermoelectric Figure of Merit of Zintl Phase YbCd2-xMnxSb2 b...) | https://doi.org/10.1063/1.3327443 (Zintl phase Yb1−xCaxCd2Sb2 with tunable thermoelectric properties indu...)

## Co-Sb-Te
- rank 234 | 31 samples | 16 papers | 23 compositions
- compositions: CoSb2.8Te0.2 (6); CoSb2.75Ge0.05Te0.2 (3); CoSb2.7Te0.3 (2); Co0.98Ni0.02(Sb0.25Te0.75)3 (1); CoSb2.75Te0.25 (1); Co0.98Ni0.02(Sb0.75Te0.25)3 (1)
- dopant candidates (<5% at.): Ge (9), Sn (6), Ni (2), Bi (2), Si (1)
- seed hypothesis (confirm): skutterudite
- measured range: 13-805 K (5th-95th pct of 113 curves; full span incl. outliers 11-949 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co2SbTe P-6m2 (187) mp-675568 [hull=0.396, PRIMARY]; CoSbTe P2/m (10) mp-1226005 [hull=0.471, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2012.02.034 (Microstructure and thermoelectric properties of CoSb2.75Ge0.25−xTex pr...) | https://doi.org/10.1063/1.1852072 (Nanostructured Co1−xNix(Sb1−yTey)3 skutterudites: Theoretical modeling...) | https://doi.org/10.1063/1.2815671 (Enhanced thermoelectric properties in CoSb3-xTex alloys prepared by me...)

## Mn-O-Pr
- rank 235 | 31 samples | 11 papers | 19 compositions
- compositions: Pr0.8Sr0.2MnO3 (4); Pr0.9Sr0.1MnO3 (3); Pr0.9Te0.1MnO3 (3); La0.18Pr0.72Te0.1MnO3 (3); Pr0.65Ca0.2Sr0.15MnO3 (2); Pr0.65Ca0.15Sr0.2MnO3 (2)
- dopant candidates (<5% at.): Sr (17), Ca (6), Te (6), K (4), Na (4), La (3), Bi (2), Fe (2)
- measured range: 11-1240 K (5th-95th pct of 37 curves; full span incl. outliers 10-1353 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrMnO3 Pnma (62) mp-25037 [hull=0.000, icsd=9, PRIMARY]; PrMn2O5 Pbam (55) mp-25704 [hull=0.000, icsd=4, PRIMARY]; PrMn7O12 C2/m (12) mp-1188985 [hull=0.021, icsd=2, PRIMARY]; Pr12Mn11O36 P2_1/c (14) mp-1173483 [hull=0.006, PRIMARY]; Pr7Mn8O24 Cm (8) mp-699531 [hull=0.028, PRIMARY]
- papers: https://doi.org/10.2320/jinstmet.ja201516 (P-Type Thermoelectric Properties of Pr<sub>1&minus;<i>x</i></sub>Sr<su...) | https://doi.org/10.1016/j.jallcom.2007.11.046 (Electrical resistivity, thermoelectric power and electron spin resonan...) | https://doi.org/10.1016/j.jmmm.2004.07.004 (Non-adiabatic small-polaron hopping conduction in Pr0.65Ca0.35−xSrxMnO...)

## O-Pb-Pd
- rank 236 | 31 samples | 8 papers | 15 compositions
- compositions: PbPdO2 (9); PbPd0.9Co0.1O2 (5); PbPd0.94Li0.06O2 (2); PbPd0.96Li0.04O2 (2); PbPd0.92Li0.08O2 (2); PbPd0.98Li0.02O2 (2)
- dopant candidates (<5% at.): Li (8), Cu (5), Co (5), Zn (1), Mn (1), V (1), Gd (1)
- measured range: 10-609 K (5th-95th pct of 47 curves; full span incl. outliers 10-815 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PdPbO2 Imma (74) mp-22367 [hull=0.000, icsd=4, PRIMARY]; Pd2PbO4 I4_1/a (88) mp-1103838 [hull=0.000, icsd=2, PRIMARY]; Pd(PbO3)2 P4_2/ncm (138) mp-1195421 [hull=0.541, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2004.06.089 (Metal–insulator transition and large thermoelectric power of a layered...) | https://doi.org/10.1021/acs.chemmater.6b00447 (High Thermopower with Metallic Conductivity inp-Type Li-Substituted Pb...) | https://doi.org/10.1016/j.jallcom.2004.11.040 (Cu doping and pressure effect on a layered palladium oxide: PbPdO2)

## O-Ru
- rank 237 | 31 samples | 8 papers | 1 compositions
- compositions: RuO2 (31)
- seed hypothesis (confirm): rutile
- measured range: 11-451 K (5th-95th pct of 31 curves; full span incl. outliers 10-1012 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): RuO2 P4_2/mnm (136) mp-825 [hull=0.000, icsd=16, PRIMARY]; RuO2 Pa-3 (205) mp-8909 [hull=0.066, icsd=5]; RuO2 Fm-3m (225) mp-1008785 [hull=0.193, icsd=3]
- papers: https://doi.org/10.1088/1361-6528/aa98ea (Ambipolar thermoelectric power of chemically-exfoliated RuO2 nanosheets) | https://doi.org/10.1063/1.3115030 (Determination of the room temperature thermal conductivity of RuO2 by ...) | https://doi.org/10.1016/j.tsf.2004.10.032 (Epitaxial growth of ruthenium dioxide films by chemical vapor depositi...)

## Ag-Sb-Sn-Te
- rank 238 | 30 samples | 8 papers | 22 compositions
- compositions: AgSn4SbTe6 (7); AgSn2SbTe4 (2); AgSn5SbTe7 (2); (Ag0.366Sb0.558Te)0.9(SnTe)0.1 (1); (Ag0.366Sb0.558Te)0.85(SnTe)0.15 (1); (Ag0.366Sb0.558Te)0.75(SnTe)0.25 (1)
- dopant candidates (<5% at.): I (5), Si (3), C (3), In (1)
- measured range: 79-810 K (5th-95th pct of 139 curves; full span incl. outliers 17-875 K)
- papers: https://doi.org/10.1002/aenm.201100613 (Lead-Free Thermoelectrics: High Figure of Merit in p-type AgSnmSbTem+2) | https://doi.org/10.1016/j.jallcom.2014.06.176 (Composition optimization of p-type AgSnmSbTem+2 thermoelectric materia...) | https://doi.org/10.1007/s10854-015-3644-5 (Fine-grained lead-free p-type AgSn4SbTe6 thermoelectric materials synt...)

## Al-Ca-Sb
- rank 239 | 30 samples | 9 papers | 23 compositions
- compositions: Ca5Al2Sb6 (5); Ca4.75Na0.25Al2Sb6 (2); Ca5Al1.9Zn0.1Sb6 (2); Ca3AlSb3 (2); Ca4.95Na0.05Al2Sb6 (1); Ca5Al1.8In0.2Sb6 (1)
- dopant candidates (<5% at.): Zn (9), Na (8), Mn (4), In (2), Zb0+ (1)
- seed hypothesis (confirm): zintl_5_2_6
- measured range: 294-1080 K (5th-95th pct of 105 curves; full span incl. outliers 285-1143 K)
- [ref 1] TEDesignLab / ICSD: Ca5(AlSb3)2 Pbam (55) mp-8439 [hull=0.000, icsd=2, PRIMARY]; Ca3AlSb3 (62) [PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ca11AlSb9 Iba2 (45) mp-1214215 [hull=0.000, PRIMARY]; Ca(AlSb)2 P-3m1 (164) mp-1147656 [hull=0.185, PRIMARY]
- papers: https://doi.org/10.1002/adfm.201000970 (The Zintl Compound Ca5Al2Sb6 for Low-Cost Thermoelectric Power Generation) | https://doi.org/10.1039/c4dt02206h (Thermoelectric properties of the Ca5Al2−xInxSb6solid solution) | https://doi.org/10.1007/s11664-012-1951-7 (Thermoelectric Properties of Mn-Doped Ca5Al2Sb6)

## Ba-Cu-O
- rank 240 | 30 samples | 10 papers | 18 compositions
- compositions: Pr0.4Y0.6Ba2Cu3O7 (5); (Pr0.5Y0.5)1.06Ba1.94Cu3O7 (5); (Ba2CuO3 )10(CaCuO2)3 (3); Y0.5Pr0.5Ba2Cu3O7 (2); Y0.4Pr0.6Ba2Cu3O7 (2); Y0.6Nd0.4Ba2Cu3O7 (1)
- dopant candidates (<5% at.): Y (27), Pr (24), Ca (5), Sr (3), Nd (2), Sm (1)
- seed hypothesis (confirm): ybco_cuprate
- measured range: 11-1179 K (5th-95th pct of 32 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaCu3O4 Cmmm (65) mp-3988 [hull=0.014, icsd=3, PRIMARY]; Ba(CuO)2 I4_1/amd (141) mp-7374 [hull=0.000, icsd=1, PRIMARY]; Ba2CuO6 P2_1/c (14) mp-1182377 [hull=0.216, icsd=1, PRIMARY]; Ba2CuO3 Immm (71) mp-8790 [hull=0.000, icsd=1, PRIMARY]; Ba2(CuO2)3 P2/m (10) mp-615789 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jmatprotec.2007.12.078 (A study on the thermoelectric power and thermal conductivity propertie...) | https://doi.org/10.1134/s1063783415120124 (Determination of parameters of a system of charge carriers in Y1–2x Ca...) | https://doi.org/10.1016/s0025-5408(01)00539-6 (Thermoelectric power of samarium substituted Y1−xSmxBa2Cu3O7−δ superco...)

## Ba-Eu-O-Ti
- rank 241 | 30 samples | 3 papers | 14 compositions
- compositions: Ba0.6Eu0.4TiO3 (5); Ba0.5Eu0.5TiO3 (5); Ba0.4Eu0.6TiO3 (5); Ba0.3Eu0.7TiO3 (5); Ba0.7Eu0.3Ti0.999Nb0.001O3 (1); Ba0.7Eu0.3Ti0.997Nb0.003O3 (1)
- dopant candidates (<5% at.): Nb (9)
- measured range: 12-1126 K (5th-95th pct of 58 curves; full span incl. outliers 11-1174 K)
- papers: https://doi.org/10.1016/j.jssc.2019.121050 (Large thermoelectric response of B-site doped ferroelectrics: Ba0.7Eu0...) | https://doi.org/10.1103/physrevb.98.165303 (Quasilocal plasmons in the insulator-metal transition in the Mott-type...) | https://doi.org/10.1039/c7cp00020k (Tailoring the structure and thermoelectric properties of BaTiO<sub>3</...)

## Cd-Cu-Se-Sn
- rank 242 | 30 samples | 8 papers | 16 compositions
- compositions: Cu2CdSnSe4 (10); Cu2.05Cd0.95SnSe4 (2); Cu2CdSn0.975In0.025Se4 (2); Cu2.1Cd0.8SnSe3.4 (2); Cu2CdSn0.9In0.1Se4 (2); Cu2CdSn0.95In0.05Se4 (2)
- dopant candidates (<5% at.): In (6), Zn (3), Mn (3)
- seed hypothesis (confirm): stannite_kesterite
- measured range: 293-771 K (5th-95th pct of 109 curves)
- [ref 1] TEDesignLab / ICSD: CdCu2SnSe4 I-42m (121) mp-16565 [hull=0.000, icsd=2, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Cd4FeCu10(SnSe4)5 C2 (5) mp-1229234 [hull=0.021, PRIMARY]
- papers: https://doi.org/10.1002/adma.200900409 (Improved Thermoelectric Properties of Cu-Doped Quaternary Chalcogenide...) | https://doi.org/10.1021/cm2031812 (Composition Control and Thermoelectric Properties of Quaternary Chalco...) | https://doi.org/10.1016/j.intermet.2014.06.014 (Crystal structure and thermoelectric properties of Cu2Cd1−xZnxSnSe4 so...)

## Fe-Sb-Te
- rank 243 | 30 samples | 8 papers | 17 compositions
- compositions: FeSb2Te (8); FeSb1.84Te0.16 (6); FeSb2.2Te0.8 (2); FeSb2.05Te0.95 (1); FeSb2.15Te0.85 (1); FeSb2Te1 (1)
- dopant candidates (<5% at.): In (4), Sn (3)
- measured range: 10-802 K (5th-95th pct of 140 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeSbTe P2_1/c (14) mp-1102580 [hull=0.507, icsd=1, PRIMARY]; Fe2SbTe3 Pm (6) mp-1224691 [hull=0.404, PRIMARY]; FeSbTe P2/m (10) mp-1224850 [hull=0.554]
- papers: https://doi.org/10.1016/j.actamat.2013.09.006 (Realization of high thermoelectric performance in p-type unfilled tern...) | https://doi.org/10.1063/1.4731251 (Enhancement of the thermoelectric properties in doped FeSb2 bulk crystals) | https://doi.org/10.1007/s10909-014-1148-y (Enhanced Thermoelectric Performance of Te-doped FeSb $$_{2}$$ 2 Nanoco...)

## Mn-O
- rank 244 | 30 samples | 7 papers | 11 compositions
- compositions: Nd0.2Ca0.2Sr0.2Ba0.2Y0.2MnO3 (5); La0.2Ca0.2Sr0.2Ba0.2Y0.2MnO3 (5); Ho0.2Ca0.2Sr0.2Ba0.2Y0.2MnO3 (5); Lu0.2Ca0.2Sr0.2Ba0.2Y0.2MnO3 (5); MnO2 (3); MnO (2)
- dopant candidates (<5% at.): Ca (22), Sr (22), Ba (21), Y (21), La (9), Nd (8), Ho (5), Lu (5), Sm (2), Gd (1), Pr (1)
- measured range: 11-1237 K (5th-95th pct of 30 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnO Fm-3m (225) mp-19006 [hull=0.000, icsd=14, PRIMARY]; MnO2 Pnma (62) mp-19326 [hull=0.008, icsd=9, PRIMARY]; Mn3O4 I4_1/amd (141) mp-18759 [hull=0.000, icsd=7, PRIMARY]; Mn2O3 Pbca (61) mp-1172875 [hull=0.000, icsd=4, PRIMARY]; MnO3 Imma (74) mp-1086672 [hull=0.492, icsd=2, PRIMARY]
- papers: https://doi.org/10.1209/epl/i2003-00161-8 (V–V bond length fluctuations in VO x) | https://doi.org/10.1088/0957-4484/23/8/085401 (Giant Seebeck coefficient thermoelectric device of MnO2powder) | https://doi.org/10.1016/0040-6031(93)80436-e (Thermal constants for Ni, NiO, MgO, MnO and CoO at low temperatures)

## Ag-Pb-Te
- rank 245 | 29 samples | 13 papers | 27 compositions
- compositions: Pb42.32Te44.12Ag13.55 (3); (Pb0.9814La0.0186Te)0.9462(Ag2Te)0.0538 (1); (PbTe)0.945(Ag2Te)0.055 (1); (Pb0.9636La0.0364Te)0.945(Ag2Te)0.055 (1); (Pb0.9906La0.0094Te)0.9457(Ag2Te)0.0543 (1); Ag0.15Pb0.99La0.01Te (1)
- dopant candidates (<5% at.): La (7), Na (3)
- measured range: 293-774 K (5th-95th pct of 105 curves)
- papers: https://doi.org/10.1002/adfm.201000878 (High Thermoelectric Performance in PbTe Due to Large Nanoscale Ag2Te P...) | https://doi.org/10.1021/cm803437x (Improvement in the Thermoelectric Figure of Merit by La/Ag Cosubstitut...) | https://doi.org/10.1063/1.3517088 (Effect of Ag or Sb addition on the thermoelectric properties of PbTe)

## Al-Re-Si
- rank 246 | 29 samples | 8 papers | 16 compositions
- compositions: Al74.6Re17.4Si8 (5); Al75.6Re17.4Si7 (4); Al71.6Re17.4Si11 (3); Al72.6Re17.4Si10 (3); Al73.6Re17.4Si9 (3); Al5.7Re4.7Si4.3 (1)
- seed hypothesis (confirm): quasicrystal_approximant
- measured range: 11-973 K (5th-95th pct of 44 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al17(Re2Si)2 Pm-3 (200) mp-16569 [hull=0.000, icsd=1, PRIMARY]; AlReSi I4mm (107) mp-1228809 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1039/c5tc01608h (MoSi2-type narrow band gap intermetallic compound Al6Re5Si4 as a therm...) | https://doi.org/10.1103/physrevb.70.144202 (Thermoelectric properties ofAl82.6−xRe17.4Six(7⩽x⩽12)1∕1-cubic approxi...) | https://doi.org/10.1088/1468-6996/15/4/044802 (Metallic–covalent bonding conversion and thermoelectric properties of ...)

## Ca-Fe-La-O
- rank 247 | 29 samples | 12 papers | 16 compositions
- compositions: La0.5Ca0.5FeO3 (5); La0.6Ca0.4Fe0.8Ni0.2O3 (4); La0.6Ca0.4FeO3 (3); La0.6Ca0.4Co0.2Fe0.8O3 (3); La0.3Ca0.7Fe0.8Cr0.2O3 (2); La0.7Ca0.3FeO3 (2)
- dopant candidates (<5% at.): Co (6), Ni (5), Cr (5), Ba (1)
- measured range: 303-1255 K (5th-95th pct of 29 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaLa2(FeO3)3 Pnma (62) mp-1227525 [hull=0.000, PRIMARY]; CaLa3(FeO3)4 Pm (6) mp-1227194 [hull=0.000, PRIMARY]; CaLaFeO4 I4mm (107) mp-1227068 [hull=0.057, PRIMARY, AMBIGUOUS]; CaLaFeO4 C222_1 (20) mp-1227123 [hull=0.058]
- papers: https://doi.org/10.1016/j.jpowsour.2021.230907 (Understanding the favorable CO2 tolerance of Ca-doped LaFeO3 perovskit...) | https://doi.org/10.1007/s40843-020-1567-2 (Tailored Sr-Co-free perovskite oxide as an air electrode for high-perf...) | https://doi.org/10.1016/j.matlet.2018.11.180 (Time degradation of electronic and ionic transport in perovskite-like ...)

## Fe-Sb-Yb
- rank 248 | 29 samples | 11 papers | 17 compositions
- compositions: YbFe4Sb12 (6); YbFe3.5Ni0.5Sb12 (2); Yb0.9Fe3.5Ni0.5Sb12 (2); Yb0.95Fe3.5Pt0.5Sb12 (2); Yb0.92Fe4Sb12 (2); YbFe3.5Pt0.5Sb12 (2)
- dopant candidates (<5% at.): Ni (8), Pt (8), Mg (3), Ce (1)
- seed hypothesis (confirm): skutterudite, filled_skutterudite  <-- MIXED, split per composition
- measured range: 11-1250 K (5th-95th pct of 106 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(FeSb3)4 Im-3 (204) mp-1207658 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2011.12.022 (Thermoelectric properties of p-type skutterudites YbxFe3.5Ni0.5Sb12 (0...) | https://doi.org/10.1016/j.intermet.2011.04.015 (Thermoelectric properties of P-type Yb-filled skutterudite YbxFeyCo4-y...) | https://doi.org/10.1063/1.1999854 (Improved thermoelectric properties in double-filled Cey∕2Yby∕2Fe4−x(Co...)

## Ge-Mg
- rank 249 | 29 samples | 10 papers | 12 compositions
- compositions: Mg2Ge (15); Mg2Ge0.98Sb0.02 (2); Mg2Ge0.98Bi0.02 (2); Mg2Ge0.99Bi0.01 (2); Mg2.2Ge (1); Mg2.2Ge0.995Sb0.005 (1)
- dopant candidates (<5% at.): Sb (6), Bi (6), Li (1)
- seed hypothesis (confirm): antifluorite
- measured range: 103-831 K (5th-95th pct of 83 curves; full span incl. outliers 15-843 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg2Ge Fm-3m (225) mp-408 [hull=0.000, icsd=8, PRIMARY]; Mg3Ge P6_3/m (176) mp-642855 [hull=0.132, icsd=1, PRIMARY]; Mg19Ge5 P-43m (215) mp-1232376 [hull=0.326, PRIMARY]; Mg5Ge Amm2 (38) mp-1185804 [hull=0.111, PRIMARY, AMBIGUOUS]; MgGe C2/m (12) mp-1185865 [hull=0.133, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2014.08.010 (Influence of Sb doping on thermoelectric properties of Mg2Ge materials) | https://doi.org/10.3938/jkps.64.690 (Thermoelectric properties of Mg2Si1−x Ge x prepared by using a solid-s...) | https://doi.org/10.1016/j.tsf.2007.02.053 (Composition dependent thermoelectric properties of sintered Mg2Si1−xGe...)

## Ge-Pb-Se-Te
- rank 250 | 29 samples | 5 papers | 28 compositions
- compositions: Ge0.55Pb0.45Te0.5Se0.5 (2); Ge0.5Pb0.5Te0.5Se0.5 (1); Ge0.6Pb0.4Te0.5Se0.5 (1); Ge0.8Pb0.2Te0.5Se0.5 (1); Ge0.75Pb0.25Te0.5Se0.5 (1); Ge0.9Pb0.1Te0.5Se0.5 (1)
- dopant candidates (<5% at.): Sm (10), Cu (7)
- solid-solution axis: Se/(Se+Te) spans 0.10-0.80 (median 0.50) over 28 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 200-800 K (5th-95th pct of 131 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GeTe(PbSe)2 P3m1 (156) mp-1224368 [hull=0.027, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2014.04.036 (High thermoelectric performance of Ge1−xPbxSe0.5Te0.5 due to (Pb, Se) ...) | https://doi.org/10.1126/sciadv.abc0726 (Electronic quality factor for thermoelectrics) | https://doi.org/10.1016/j.matdes.2018.08.001 (Se-Sm co-doping strategy for tuning the structural and thermoelectric ...)
