# Host systems -- chunk 070 of 73

Ranks 3451-3500 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 99.72%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Lu-O-V
- rank 3451 | 1 samples | 1 papers | 1 compositions
- compositions: Lu2V2O7 (1)
- measured range: 21-286 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LuVO4 I4_1/amd (141) mp-18993 [hull=0.000, icsd=30, PRIMARY]; Lu2V2O7 Fd-3m (227) mp-25127 [hull=0.004, icsd=3, PRIMARY]; LuVO3 Pnma (62) mp-769783 [hull=0.005, icsd=2, PRIMARY]; Lu4V4O13 F-43m (216) mp-691150 [hull=0.208, PRIMARY]; LuVO2 I4_1/amd (141) mp-1210719 [hull=0.516, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.91.205107 (Electronic transport in the ferromagnetic pyrochlore<mml:math xmlns:mm...)

## Lu-O-Zr
- rank 3452 | 1 samples | 1 papers | 1 compositions
- compositions: Lu2Zr2O7 (1)
- measured range: 300-1272 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Lu4Zr3O12 P-1 (2) mp-1222825 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.scriptamat.2019.12.006 (Multicomponent high-entropy zirconates with comprehensive properties f...)

## Lu-Pd-Si
- rank 3453 | 1 samples | 1 papers | 1 compositions
- compositions: Lu3Pd20Si6 (1)
- measured range: 14-299 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Lu(SiPd)2 I4/mmm (139) mp-3507 [hull=0.000, icsd=3, PRIMARY]; LuSiPd2 Pnma (62) mp-1189950 [hull=0.000, icsd=1, PRIMARY]; Lu2Si3Pd Pmm2 (25) mp-1222316 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2008.09.208 (Physical phenomena of the cage compounds RE3Pd20Si6 (RE=Yb, Lu))

## Lu-Pt-Sb
- rank 3454 | 1 samples | 1 papers | 1 compositions
- compositions: LuPtSb (1)
- measured range: 20-276 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LuSbPt F-43m (216) mp-10194 [hull=0.000, icsd=1, PRIMARY]; Lu5SbPt2 I4/mcm (140) mp-1210524 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1038/nmat2771 (Half-Heusler ternary compounds as new multifunctional experimental pla...)

## Lu-Sb-Zn
- rank 3455 | 1 samples | 1 papers | 1 compositions
- compositions: (Zn0.7Lu0.3)4Sb3 (1)
- measured range: 300-675 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.scriptamat.2019.08.037 (Dislocation-induced ultra-low lattice thermal conductivity in rare ear...)

## Lu-Si
- rank 3456 | 1 samples | 1 papers | 1 compositions
- compositions: Lu5Si3 (1)
- measured range: 13-294 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Lu5Si3 P6_3/mcm (193) mp-11908 [hull=0.000, icsd=4, PRIMARY]; LuSi2 P6/mmm (191) mp-1103 [hull=0.098, icsd=4, PRIMARY]; LuSi Cmcm (63) mp-1001612 [hull=0.000, icsd=2, PRIMARY]; Lu3Si Pm-3m (221) mp-1185426 [hull=0.238, PRIMARY, AMBIGUOUS]; LuSi3 Pm-3m (221) mp-973668 [hull=0.234, PRIMARY]
- papers: https://doi.org/10.7567/1347-4065/ab5b85 (Thermoelectric properties of Yb5Si3)

## Lu-Zn
- rank 3457 | 1 samples | 1 papers | 1 compositions
- compositions: LuZn (1)
- measured range: 27-296 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Lu2Zn17 R-3m (166) mp-30715 [hull=0.000, icsd=2, PRIMARY]; Lu6Zn23 Fm-3m (225) mp-1192910 [hull=0.006, icsd=1, PRIMARY]; LuZn Pm-3m (221) mp-11496 [hull=0.000, icsd=1, PRIMARY]; LuZn12 I4/mmm (139) mp-1104393 [hull=0.008, icsd=1, PRIMARY]; LuZn2 Imma (74) mp-1024948 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(88)90183-7 (Electrical and thermoelectric transport properties of RZn and RCd comp...)

## Mg-Na-Pb
- rank 3458 | 1 samples | 1 papers | 1 compositions
- compositions: Na2Mg3Pb2 (1)
- measured range: 299-597 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Na2MgPb P6_3/mmc (194) mp-1078372 [hull=0.003, icsd=1, PRIMARY]; NaMgPb2 Fm-3m (225) mp-865107 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.7567/jjap.54.07jc04 (Synthesis of Na2Mg3X2 (X = Sn, Pb) and Na4Mg4Sn3 and their crystal str...)

## Mg-Ni
- rank 3459 | 1 samples | 1 papers | 1 compositions
- compositions: Mg2Ni (1)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg2Ni P6_222 (180) mp-2137 [hull=0.000, icsd=13, PRIMARY]; MgNi2 P6_3/mmc (194) mp-2675 [hull=0.000, icsd=6, PRIMARY]; MgNi P4/mmm (123) mp-1018140 [hull=0.048, icsd=1, PRIMARY, AMBIGUOUS]; MgNi3 Pm-3m (221) mp-1063661 [hull=0.114, icsd=1, PRIMARY]; Nd(Mg10Ni)2 Fd-3m (227) mp-1195878 [hull=0.010, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.69.115326 (Temperature dependence of magnetoresistance and Hall effect in<mml:mat...)

## Mg-Ni-Sb
- rank 3460 | 1 samples | 1 papers | 1 compositions
- compositions: MgNiSb (1)
- measured range: 199-379 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MgNiSb F-43m (216) mp-15778 [hull=0.000, icsd=1, PRIMARY]; MgNi2Sb Fm-3m (225) mp-30773 [hull=0.072, icsd=1, PRIMARY]; Mg6NiSb Amm2 (38) mp-1099292 [hull=0.157, PRIMARY]; Mg14NiSb Amm2 (38) mp-1028357 [hull=0.079, PRIMARY, AMBIGUOUS]; Mg14NiSb P-6m2 (187) mp-1028340 [hull=0.080]
- papers: https://doi.org/10.1016/j.jallcom.2005.04.012 (Thermoelectric properties of ScCoSb, ScNi0.86Sb and MgNiSb compounds)

## Mg-O-Sb-Si
- rank 3461 | 1 samples | 1 papers | 1 compositions
- compositions: Mg2SiSb5O7.5 (1)
- measured range: 305-865 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/j.intermet.2012.08.026 (Fabrication and thermoelectric properties of Mg2Si-based composites us...)

## Mg-O-Zn
- rank 3462 | 1 samples | 1 papers | 1 compositions
- compositions: Zn0.8379Mg0.1596Al0.0025O (1)
- dopant candidates (<5% at.): Al (1)
- measured range: 286-1165 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg2ZnO3 P-3m1 (164) mp-1222123 [hull=0.047, PRIMARY]; Mg3ZnO4 Pm-3m (221) mp-1024045 [hull=0.032, PRIMARY, AMBIGUOUS]; MgZn2O3 P-3m1 (164) mp-1221931 [hull=0.095, PRIMARY]; MgZn3O4 Cm (8) mp-1221958 [hull=0.013, PRIMARY]; MgZn4O5 P3m1 (156) mp-1221986 [hull=0.013, PRIMARY]
- papers: https://doi.org/10.1063/1.1489091 (Thermoelectric properties of (Zn1−yMgy)1−xAlxO ceramics prepared by th...)

## Mg-Pb
- rank 3463 | 1 samples | 1 papers | 1 compositions
- compositions: Mg2Pb (1)
- measured range: 10-181 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg2Pb Fm-3m (225) mp-20724 [hull=0.000, icsd=7, PRIMARY]; Mg149Pb P-6m2 (187) mp-1185570 [hull=0.000, PRIMARY]; Mg3Pb I4/mmm (139) mp-978293 [hull=0.012, PRIMARY, AMBIGUOUS]; Mg5Pb R32 (155) mp-1185832 [hull=0.024, PRIMARY, AMBIGUOUS]; MgPb C2/m (12) mp-1185919 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1063/1.1663609 (Thermal conductivity of magnesium plumbide)

## Mg-Pb-Sb
- rank 3464 | 1 samples | 1 papers | 1 compositions
- compositions: Mg3Sb1.7Pb0.3 (1)
- measured range: 323-774 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1039/c4ra04889j (Enhancing thermoelectric properties of a p-type Mg3Sb2- based Zintl ph...)

## Mg-Pt-Si
- rank 3465 | 1 samples | 1 papers | 1 compositions
- compositions: MgPtSi (1)
- measured range: 15-297 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg2SiPt P6_3/mmc (194) mp-14793 [hull=0.000, icsd=1, PRIMARY]; Mg5(Si8Pt5)2 F-43m (216) mp-30324 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.91.174514 (Superconductivity in MgPtSi: An orthorhombic variant of<mml:math xmlns...)

## Mg-S-Si-Sn
- rank 3466 | 1 samples | 1 papers | 1 compositions
- compositions: Mg2Si0.5Sn0.5S (1)
- measured range: 299-772 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1039/c1jm00025j (Flux synthesis and thermoelectric properties of eco-friendly Sb doped ...)

## Mg-Si-Yb
- rank 3467 | 1 samples | 1 papers | 1 compositions
- compositions: Yb2MgSi2 (1)
- measured range: 12-300 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb2MgSi2 P4/mbm (127) mp-13357 [hull=0.082, icsd=1, PRIMARY]; YbMgSi Pnma (62) mp-864619 [hull=0.000, icsd=1, PRIMARY]; Yb7Mg3Si8 P2_1 (4) mp-1215837 [hull=0.083, PRIMARY]
- papers: https://doi.org/10.1007/s00339-016-0300-8 (Thermoelectric and magnetic properties of Yb2MgSi2 prepared by spark p...)

## Mg-Zn
- rank 3468 | 1 samples | 1 papers | 1 compositions
- compositions: Y4.5Tb4.5Mg42Zn57 (1)
- dopant candidates (<5% at.): Y (1), Tb (1)
- measured range: 14-292 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MgZn2 P6_3/mmc (194) mp-1124 [hull=0.000, icsd=8, PRIMARY]; Mg2Zn11 Pm-3 (200) mp-30784 [hull=0.000, icsd=1, PRIMARY]; Mg4Zn7 C2/m (12) mp-680671 [hull=0.000, icsd=1, PRIMARY]; Mg149Zn P-6m2 (187) mp-1185642 [hull=0.000, PRIMARY]; Mg2Zn Cmcm (63) mp-1094422 [hull=0.026, PRIMARY, AMBIGUOUS]
- papers: https://doi.org/10.1103/physrevb.59.308 (Magnetic and transport properties of single-grainR−Mg−Znicosahedral qu...)

## Mn-Mo-S
- rank 3469 | 1 samples | 1 papers | 1 compositions
- compositions: Mn1.3Mo6S8 (1)
- measured range: 300-960 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1007/s11664-009-0975-0 (Thermoelectric Properties of Chevrel-Phase Sulfides M x Mo6S8 (M: Cr, ...)

## Mn-Na-Nd-O
- rank 3470 | 1 samples | 1 papers | 1 compositions
- compositions: Nd0.75Na0.25MnO3 (1)
- measured range: 13-343 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1063/1.4826089 (Giant magnetothermopower in charge ordered Nd0.75Na0.25MnO3)

## Mn-Na-O
- rank 3471 | 1 samples | 1 papers | 1 compositions
- compositions: Na0.7MnO2 (1)
- measured range: 304-817 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NaMnO2 C2/m (12) mp-18957 [hull=0.000, icsd=3, PRIMARY]; Na4Mn2O5 Fddd (70) mp-18869 [hull=0.000, icsd=2, PRIMARY]; Na2Mn3O7 P-1 (2) mp-19080 [hull=0.000, icsd=2, PRIMARY]; Na5MnO4 Pmn2_1 (31) mp-32013 [hull=0.003, icsd=1, PRIMARY]; Na6MnO4 P6_3mc (186) mp-19321 [hull=0.017, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0167-2738(87)90064-6 (Relation between ionic and electronic defects of Na0.7MnO2 bronze and ...)

## Mn-Ni-S
- rank 3472 | 1 samples | 1 papers | 1 compositions
- compositions: Mn0.9Ni0.1S (1)
- measured range: 81-898 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.3938/jkps.62.2059 (Magnetic and thermoelectric properties of the Mn1−X Ni X S solid solut...)

## Mn-O-Ru-Tl
- rank 3473 | 1 samples | 1 papers | 1 compositions
- compositions: Tl2MnRuO7 (1)
- measured range: 36-216 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/s0304-8853(99)00744-1 (Magnetoresistance in Tl2Mn2O7 pyrochlore: magnetic and charge density ...)

## Mn-O-Si-Sr
- rank 3474 | 1 samples | 1 papers | 1 compositions
- compositions: Sr0.7Si0.3MnO3 (1)
- measured range: 773-1073 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaSr2Mn2(Si2O7)2 C2 (5) mp-19122 [hull=0.001, icsd=2, PRIMARY]; Sr2MnSi2O7 P-42_1m (113) mp-1191740 [hull=0.000, icsd=1, PRIMARY]; SrMn2(SiO5)2 P2_1/m (11) mp-1218300 [hull=0.207, PRIMARY, AMBIGUOUS]; SrMn2(SiO5)2 Cmcm (63) mp-1208671 [hull=0.215]
- papers: https://doi.org/10.1016/j.powtec.2015.02.035 (Fabrication and thermoelectric properties of Sr1−xSixMnO3−δ)

## Mn-O-Sm
- rank 3475 | 1 samples | 1 papers | 1 compositions
- compositions: SmMnO3 (1)
- measured range: 320-1367 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SmMnO3 Pnma (62) mp-25026 [hull=0.000, icsd=5, PRIMARY]; SmMn2O5 Pbam (55) mp-19358 [hull=0.000, icsd=2, PRIMARY]; Sm2Mn2O7 Fd-3m (227) mp-769900 [hull=0.000, PRIMARY]; Sm2Mn2O5 Ima2 (46) mp-1076289 [hull=0.150, PRIMARY]; SmMnO3 Pm-3m (221) mp-1075973 [hull=0.212]
- papers: https://doi.org/10.1016/j.jssc.2004.12.006 (Structural, transport, and magnetic properties of RMnO3 perovskites (R...)

## Mn-O-Sn-Sr
- rank 3476 | 1 samples | 1 papers | 1 compositions
- compositions: Sr0.85Pb0.15Mn0.75Sn0.25O3 (1)
- dopant candidates (<5% at.): Pb (1)
- measured range: 303-423 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1007/s11664-022-09733-1 (Synthesis and Characterization of Sr0.85Pb0.15Mn1−xSnxO3 Perovskite Ma...)

## Mn-O-Sr-Ti
- rank 3477 | 1 samples | 1 papers | 1 compositions
- compositions: Sr0.7Ti0.3MnO3 (1)
- measured range: 772-1073 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaSr7Ti5Mn3O20 P1 (1) mp-1100246 [hull=0.088, PRIMARY]; BaSr7Ti5Mn3O24 Cm (8) mp-1099624 [hull=0.016, PRIMARY]; BaSr7Ti6Mn2O20 P1 (1) mp-1076196 [hull=0.143, PRIMARY]; BaSr7Ti6Mn2O24 Amm2 (38) mp-1075988 [hull=0.012, PRIMARY]; Sr2TiMnO5 Ima2 (46) mp-1076627 [hull=0.043, PRIMARY]
- papers: https://doi.org/10.1007/s13391-014-4237-9 (Structural and thermoelectric properties of n-type Sr1−x Ti x MnO3−δ p...)

## Mn-O-Sr-Y
- rank 3478 | 1 samples | 1 papers | 1 compositions
- compositions: Y0.7Sr0.3MnO3 (1)
- measured range: 293-1295 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2YMn2O7 P2_1/m (11) mp-1218597 [hull=0.019, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.66.132413 (Reentrant metallic transition at a temperature above<mml:math xmlns:mm...)

## Mn-P-Rh
- rank 3479 | 1 samples | 1 papers | 1 compositions
- compositions: MnRhP (1)
- measured range: 79-578 K (5th-95th pct of 2 curves; full span incl. outliers 79-627 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnPRh P-62m (189) mp-1079405 [hull=0.298, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(01)01793-5 (Electrical properties of the transition metal compound MnRhP)

## Mn-Pd-Sn
- rank 3480 | 1 samples | 1 papers | 1 compositions
- compositions: Pd2MnSn (1)
- measured range: 12-304 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnSnPd2 Fm-3m (225) mp-20481 [hull=0.000, icsd=6, PRIMARY]; Mn2SnPd3 P-3m1 (164) mp-1221536 [hull=0.015, PRIMARY]; Mn3Sn2Pd5 R-3m (166) mp-1222087 [hull=0.014, PRIMARY]; MnSnPd2 P4/mmm (123) mp-1221549 [hull=0.098]
- papers: https://doi.org/10.1088/0305-4608/11/7/017 (The transport properties of Heusler alloys: 'ideal' local moment ferro...)

## Mn-S
- rank 3481 | 1 samples | 1 papers | 1 compositions
- compositions: Mn0.95Ni0.05S (1)
- dopant candidates (<5% at.): Ni (1)
- measured range: 243-1048 K (5th-95th pct of 1 curves)
- [ref 1] TEDesignLab / ICSD: MnS Fm-3m (225) mp-850034 [hull=0.060, icsd=24, PRIMARY]; MnS2 Pa-3 (205) mp-870682 [hull=0.111, icsd=16, PRIMARY]; MnS F-43m (216) mp-850037 [hull=0.000, icsd=2]; MnS P6_3mc (186) mp-850036 [hull=0.018, icsd=2]; MnS2 Pnnm (58) mp-1018804 [hull=0.029, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: Mn3S Pm-3m (221) mp-975439 [hull=0.477, PRIMARY]; Mn2S3 R-3c (167) mp-974355 [hull=0.041, PRIMARY]; MnS Pm-3m (221) mp-850100 [hull=0.471, icsd=1]; MnS2 P2_1/c (14) mp-1095335 [hull=0.297, icsd=1]
- papers: https://doi.org/10.3938/jkps.62.2059 (Magnetic and thermoelectric properties of the Mn1−X Ni X S solid solut...)

## Mn-S-Te
- rank 3482 | 1 samples | 1 papers | 1 compositions
- compositions: MnTe0.9S0.1 (1)
- measured range: 326-770 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1063/1.4868584 (Thermoelectric study of crossroads material MnTe via sulfur doping)

## Mn-Sb
- rank 3483 | 1 samples | 1 papers | 1 compositions
- compositions: MnSb (1)
- measured range: 84-393 K (5th-95th pct of 2 curves; full span incl. outliers 84-788 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnSb P6_3/mmc (194) mp-786 [hull=0.000, icsd=24, PRIMARY]; Mn2Sb P4/nmm (129) mp-20664 [hull=0.123, icsd=10, PRIMARY]; Mn3Sb Pm-3m (221) mp-1636 [hull=0.110, icsd=3, PRIMARY]; Mn14Sb13 C2/c (15) mp-684805 [hull=0.021, PRIMARY]; Mn27Sb26 P1 (1) mp-684881 [hull=0.007, PRIMARY]
- papers: https://doi.org/10.1134/s0020168516040105 (Anisotropic electrical properties of a eutectic InSb + MnSb composite)

## Mn-Se-Te
- rank 3484 | 1 samples | 1 papers | 1 compositions
- compositions: MnTe0.9Se0.1 (1)
- measured range: 323-823 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn2TeSe R-3m (166) mp-1221790 [hull=0.044, PRIMARY]; Mn3Te2Se Immm (71) mp-1221758 [hull=0.056, PRIMARY]; Mn4Te3Se P-6m2 (187) mp-1221977 [hull=0.033, PRIMARY]
- papers: https://doi.org/10.1021/acsami.9b10207 (Reducing Lattice Thermal Conductivity of MnTe by Se Alloying toward Hi...)

## Mn-Si-Tb
- rank 3485 | 1 samples | 1 papers | 1 compositions
- compositions: Tb2Mn3Si5 (1)
- measured range: 18-300 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TbMnSi P4/nmm (129) mp-20822 [hull=0.000, icsd=4, PRIMARY]; Tb(MnSi)2 I4/mmm (139) mp-5677 [hull=0.000, icsd=2, PRIMARY]; Tb2Mn3Si5 P4/mnc (128) mp-639228 [hull=0.000, icsd=2, PRIMARY]; TbMnSi Pnma (62) mp-20597 [hull=0.065, icsd=2]
- papers: https://doi.org/10.1016/s0925-8388(00)01451-1 (Multi-magnetic transitions in Tb2Mn3Si5)

## Mn-Si-Ti
- rank 3486 | 1 samples | 1 papers | 1 compositions
- compositions: TiMnSi2 (1)
- measured range: 299-1110 K (5th-95th pct of 4 curves; full span incl. outliers 299-1180 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiMnSi2 Pbam (55) mp-21606 [hull=0.000, icsd=3, PRIMARY]; Ti2Mn4Si5 Ibam (72) mp-17553 [hull=0.215, icsd=1, PRIMARY]; Ti2MnSi F-43m (216) mp-999047 [hull=0.228, icsd=1, PRIMARY]; TiMn2Si Fm-3m (225) mp-865652 [hull=0.000, PRIMARY]; TiMnSi4 P2 (3) mp-1216867 [hull=0.078, PRIMARY]
- papers: https://doi.org/10.1007/s11664-009-1019-5 (Thermoelectric Properties of Zr3Mn4Si6 and TiMnSi2)

## Mn-Si-Zr
- rank 3487 | 1 samples | 1 papers | 1 compositions
- compositions: Zr3Mn4Si6 (1)
- measured range: 303-1110 K (5th-95th pct of 4 curves; full span incl. outliers 303-1170 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZrMnSi Pnma (62) mp-22227 [hull=0.000, icsd=2, PRIMARY]; ZrMnSi2 Immm (71) mp-18059 [hull=0.007, icsd=1, PRIMARY, AMBIGUOUS]; Zr3(Mn2Si3)2 P4_2/mbc (135) mp-31310 [hull=0.002, icsd=1, PRIMARY]; Zr3Mn8Si P3m1 (156) mp-1215733 [hull=0.093, PRIMARY]; ZrMnSi2 Pbam (55) mp-1197723 [hull=0.013, icsd=1]
- papers: https://doi.org/10.1007/s11664-009-1019-5 (Thermoelectric Properties of Zr3Mn4Si6 and TiMnSi2)

## Mn-Sn-Th
- rank 3488 | 1 samples | 1 papers | 1 compositions
- compositions: Th4Mn13Sn5 (1)
- measured range: 11-297 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.intermet.2009.01.008 (The structure and magnetic properties of Th4Mn13Sn5)

## Mo-Nd-O-Y
- rank 3489 | 1 samples | 1 papers | 1 compositions
- compositions: (Nd0.6Y0.4)2Mo2O7 (1)
- measured range: 17-279 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NdY3(Mo4O15)2 P1 (1) mp-1220215 [hull=0.015, PRIMARY]
- papers: https://doi.org/10.1016/0022-3697(86)90030-2 (Thermoelectric power of RE2Mo2O7 pyrochlores)

## Mo-Nd-O-Yb
- rank 3490 | 1 samples | 1 papers | 1 compositions
- compositions: (Nd0.5Yb0.5)2Mo2O7 (1)
- measured range: 89-516 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/0025-5408(80)90094-x (Electrical properties of Ln2Mo2O7 pyrochlores (Ln=SmYb,Y))

## Mo-Ni-S
- rank 3491 | 1 samples | 1 papers | 1 compositions
- compositions: Ni2.0Mo6S8 (1)
- measured range: 302-961 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NiMo3S4 P-1 (2) mp-685980 [hull=0.086, PRIMARY]
- papers: https://doi.org/10.1007/s11664-009-0975-0 (Thermoelectric Properties of Chevrel-Phase Sulfides M x Mo6S8 (M: Cr, ...)

## Mo-Ni-Sb
- rank 3492 | 1 samples | 1 papers | 1 compositions
- compositions: Ni0.3Mo2.7Ni0.3Sb7 (1)
- measured range: 314-905 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/j.jallcom.2013.04.196 (Effect of heavy doping of nickel in compound Mo3Sb7: Structure and the...)

## Mo-O-Rh
- rank 3493 | 1 samples | 1 papers | 1 compositions
- compositions: Rh2MoO6 (1)
- measured range: 319-803 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mo(RhO3)2 P4_2/mnm (136) mp-25070 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.materresbull.2011.07.007 (Synthesis, magnetic and thermoelectric properties of Rh2MO6 (M=Mo, Te,...)

## Mo-O-Sm
- rank 3494 | 1 samples | 1 papers | 1 compositions
- compositions: Sm2Mo2O7 (1)
- measured range: 89-586 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sm2(MoO4)3 C2/c (15) mp-646397 [hull=0.000, icsd=4, PRIMARY]; Sm2Mo2O7 Fd-3m (227) mp-687092 [hull=0.000, icsd=2, PRIMARY]; SmMo5O8 P2_1/c (14) mp-19565 [hull=0.289, icsd=1, PRIMARY]; Sm4Mo4O11 Pbam (55) mp-19635 [hull=0.118, icsd=1, PRIMARY]; Sm2MoO6 C2/c (15) mp-25065 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0025-5408(80)90094-x (Electrical properties of Ln2Mo2O7 pyrochlores (Ln=SmYb,Y))

## Mo-O-Sn
- rank 3495 | 1 samples | 1 papers | 1 compositions
- compositions: SnMo4O6 (1)
- measured range: 11-296 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SnMo5O8 P2_1/c (14) mp-19524 [hull=0.240, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/cm000646q (Synthesis, Characterization, and Electronic Structure of a New Molybde...)

## Mo-O-Tb
- rank 3496 | 1 samples | 1 papers | 1 compositions
- compositions: Tb2Mo2O7 (1)
- measured range: 12-281 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Tb2Mo2O7 Fd-3m (227) mp-19200 [hull=0.006, icsd=4, PRIMARY]; Tb2(MoO4)3 Pba2 (32) mp-19534 [hull=0.000, icsd=3, PRIMARY, AMBIGUOUS]; Tb5(MoO6)2 C2/m (12) mp-1105460 [hull=0.005, icsd=1, PRIMARY]; Tb4Mo4O11 Pbam (55) mp-32040 [hull=0.158, icsd=1, PRIMARY]; KTb2Cu(MoO4)4 C2/c (15) mp-699636 [hull=0.020, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0022-3697(86)90030-2 (Thermoelectric power of RE2Mo2O7 pyrochlores)

## Mo-O-Tm
- rank 3497 | 1 samples | 1 papers | 1 compositions
- compositions: Tm2Mo2O7 (1)
- measured range: 34-303 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaTm2(MoO4)4 C2/c (15) mp-1214443 [hull=0.012, PRIMARY]; KLiTm2(MoO4)4 C2/c (15) mp-1211810 [hull=0.014, PRIMARY]; Tm2Mo4O15 P2_1/c (14) mp-1208057 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/0022-3697(86)90030-2 (Thermoelectric power of RE2Mo2O7 pyrochlores)

## Mo-O-Yb
- rank 3498 | 1 samples | 1 papers | 1 compositions
- compositions: Yb2Mo2O7 (1)
- measured range: 85-612 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaYb2(MoO4)4 C2/c (15) mp-704669 [hull=0.000, icsd=1, PRIMARY]; KLiYb2(MoO4)4 C2/c (15) mp-1211614 [hull=0.087, PRIMARY]; Yb2Mo4O15 P2_1/c (14) mp-1207731 [hull=0.108, PRIMARY]; Yb6MoO12 P-1 (2) mp-1209232 [hull=0.652, PRIMARY]; YbMoO4 I4_1/a (88) mp-1207551 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/0025-5408(80)90094-x (Electrical properties of Ln2Mo2O7 pyrochlores (Ln=SmYb,Y))

## Mo-Pb-S
- rank 3499 | 1 samples | 1 papers | 1 compositions
- compositions: PbMo6S7.8 (1)
- measured range: 307-852 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mo6PbS8 P-1 (2) mp-1104554 [hull=0.035, icsd=1, PRIMARY]; BiMo30(PbS10)4 P-1 (2) mp-1229231 [hull=0.040, PRIMARY]
- papers: https://doi.org/10.2320/matertrans.e-m2011808 (Preparation of Single-Phase Pb-Filled Chevrel-Phase Sulfide and Its Th...)

## Mo-Sb-Ti
- rank 3500 | 1 samples | 1 papers | 1 compositions
- compositions: Ti0.9Mo1.1Sb4 (1)
- measured range: 303-545 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiSb4Mo Cm (8) mp-1216683 [hull=0.003, PRIMARY]
- papers: https://doi.org/10.1021/ic0619254 (Crystal Structure, Electronic Structure, and Physical Properties of Ti...)
