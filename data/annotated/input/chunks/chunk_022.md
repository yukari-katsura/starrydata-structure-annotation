# Host systems -- chunk 022 of 73

Ranks 1051-1100 by sample count. These 50 host systems cover 285 samples (0.55% of the TE set); cumulative through this chunk: 90.20%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## La-Mn-O-Ru-Sr
- rank 1051 | 6 samples | 1 papers | 6 compositions
- compositions: La0.7Sr0.3Mn0.7Ru0.3O3 (1); La0.7Sr0.3Mn0.5Ru0.5O3 (1); La0.7Sr0.3Mn0.75Ru0.25O3 (1); La0.7Sr0.3Mn0.6Ru0.4O3 (1); La0.7Sr0.3Mn0.4Ru0.6O3 (1); La0.7Sr0.3Mn0.3Ru0.7O3 (1)
- sample form: Bulk (6)
- measured range: 10-497 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr3La3Mn3RuO14 Amm2 (38) mp-1218547 [hull=0.038, PRIMARY]; SrLaMnRuO6 R3 (146) mp-39239 [hull=0.000, PRIMARY]; SrLaMnRuO6 Pc (7) mp-744086 [hull=0.037]
- papers: https://doi.org/10.1063/1.2761690 (Effects of Ru substitution for Mn on La0.7Sr0.3MnO3 perovskites)

## Li-O
- rank 1052 | 6 samples | 1 papers | 1 compositions
- compositions: Li2O (6)
- measured range: 377-969 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li2O Fm-3m (225) mp-1960 [hull=0.000, icsd=11, PRIMARY]; Li2O2 P6_3/mmc (194) mp-841 [hull=0.000, icsd=3, PRIMARY]; LiO2 C2/m (12) mp-1094135 [hull=0.288, icsd=3, PRIMARY]; LiO3 Imm2 (44) mp-1001790 [hull=0.198, icsd=1, PRIMARY]; Li2O2 P4/mmm (123) mp-1097030 [hull=0.294, icsd=1]
- papers: https://doi.org/10.1111/j.1151-2916.1988.tb05906.x (Effects of Fast Neutron Irradiation on Thermal Conductivity of Li2O an...)

## Lu-Sb
- rank 1053 | 6 samples | 1 papers | 1 compositions
- compositions: LuSb (6)
- measured range: 12-299 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LuSb Fm-3m (225) mp-516 [hull=0.000, icsd=4, PRIMARY]; LuSb2 C222 (21) mp-1008902 [hull=0.485, icsd=1, PRIMARY]; LuSb3 P6_3/mmc (194) mp-973615 [hull=0.222, PRIMARY]; LuSb Pm-3m (221) mp-1009007 [hull=0.330, icsd=2]
- papers: https://doi.org/10.1038/s41598-017-12792-8 (Fermi surface topology and magnetotransport in semimetallic LuSb)

## Mg-Y-Zn
- rank 1054 | 6 samples | 4 papers | 4 compositions
- compositions: Y8.7Mg34.6Zn56.8_IQC (3); Y12Mg29Zn59 (1); Y8.6Mg34.6Zn56.8_IQC (1); Y6.03Tb2.97Mg42Zn57 (1)
- dopant candidates (<5% at.): Tb (1)
- sample form: Bulk (1)
- measured range: 10-299 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YMgZn P-62m (189) mp-6908 [hull=0.000, icsd=1, PRIMARY]; Y2Mg3Zn4 P6_3/mmc (194) mp-1207783 [hull=0.112, PRIMARY]; Y2(MgZn)3 R3m (160) mp-1216143 [hull=0.014, PRIMARY]; Y2MgZn Immm (71) mp-1097626 [hull=2.462, PRIMARY]; YMg14Zn Amm2 (38) mp-1028093 [hull=0.046, PRIMARY, AMBIGUOUS]
- papers: https://doi.org/10.1063/1.1406555 (Electronic transport in Cd–Yb and Y–Mg–Zn quasicrystals) | https://doi.org/10.1103/physrevb.62.292 (Low-temperature thermal conductivity of a single-grain Y-Mg-Zn icosahe...) | https://doi.org/10.1080/13642819808206407 (Growth of large-grain R-Mg-Zn quasicrystals from the ternary melt (R =...)

## Mn-Re-Si
- rank 1055 | 6 samples | 4 papers | 4 compositions
- compositions: Mn30.64Re6Si63.36 (3); Mn30.4Re6Si63.6 (1); Mn28.4Re8Si63.6 (1); Mn30.4Re6.0Si63.6 (1)
- sample form: Ribbon (2); Bulk (1)
- measured range: 35-1041 K (5th-95th pct of 25 curves)
- papers: https://doi.org/10.7567/jjap.55.020301 (Thermoelectric properties of supersaturated Re solid solution of highe...) | https://doi.org/10.1007/s11664-019-07363-8 (Effect of Re Substitution on the Phase Stability of Complex MnSiγ) | https://doi.org/10.1016/j.jallcom.2018.10.209 (Effects of Re substitution for Mn on microstructures and properties in...)

## Mn-Se
- rank 1056 | 6 samples | 1 papers | 6 compositions
- compositions: MnSe (1); Mn0.999Na0.001Se (1); Mn0.99Na0.01Se (1); Mn0.97Na0.03Se (1); Mn0.995Na0.005Se (1); Mn0.98Na0.02Se (1)
- dopant candidates (<5% at.): Na (5)
- measured range: 297-749 K (5th-95th pct of 6 curves)
- [ref 1] TEDesignLab / ICSD: MnSe Fm-3m (225) mp-972 [hull=0.015, icsd=19, PRIMARY]; MnSe2 Pa-3 (205) mp-21321 [hull=0.000, icsd=3, PRIMARY]; MnSe F-43m (216) mp-2293 [hull=0.004, icsd=2]; MnSe P6_3mc (186) mp-999540 [hull=0.000, icsd=1]; MnSe P6_3/mmc (194) mp-10204 [hull=0.012, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: MnSe P4/nmm (129) mp-604910 [hull=0.031, icsd=1]
- papers: https://doi.org/10.1016/j.jallcom.2019.03.140 (Thermoelectric properties of p-type MnSe)

## Mo-Ru-Sb
- rank 1057 | 6 samples | 3 papers | 3 compositions
- compositions: Mo2.5Ru0.5Sb7 (3); Mo2.2Ru0.8Sb7 (2); Mo2.5Ru0.5Sb6.75Te0.25 (1)
- dopant candidates (<5% at.): Te (1)
- sample form: Bulk (2)
- measured range: 12-1000 K (5th-95th pct of 24 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sb28(Mo3Ru)3 Cm (8) mp-1219530 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1063/1.3097384 (Beneficial influence of Ru on the thermoelectric properties of Mo3Sb7) | https://doi.org/10.1007/s11664-009-0981-2 (Crystal Structure and High-Temperature Thermoelectric Properties of th...) | https://doi.org/10.1063/1.3388056 (Transport and magnetic properties of Mo2.5Ru0.5Sb7−xTex)

## N-V
- rank 1058 | 6 samples | 1 papers | 5 compositions
- compositions: VN (2); VN0.93 (1); VN0.88 (1); VN0.84 (1); VN0.76 (1)
- measured range: 299-996 K (5th-95th pct of 6 curves)
- [ref 1] TEDesignLab / ICSD: VN F-43m (216) mp-1001826 [hull=0.328, icsd=2]
- [ref 2] MP, ranked by ICSD evidence: VN Fm-3m (225) mp-925 [hull=0.191, icsd=28, PRIMARY]; V2N3 P-3m1 (164) mp-1069841 [hull=0.093, icsd=1, PRIMARY]; V2N P-31m (162) mp-684903 [hull=0.000, icsd=1, PRIMARY]; V8N P4_2/mnm (136) mp-1188283 [hull=0.000, icsd=1, PRIMARY]; V32N3 P2/m (10) mp-1216851 [hull=0.008, PRIMARY]
- papers: https://doi.org/10.1103/physrevmaterials.1.065002 (Phonon and electron contributions to the thermal conductivity of \nVNx...)

## Na-O
- rank 1059 | 6 samples | 1 papers | 1 compositions
- compositions: (SiO272)3.47(Al2O3)4.14(Na2O)44.3(K2O)2.24(MgO)15.72(CaO)30.13 (6)
- dopant candidates (<5% at.): Ca (6), Mg (6), Al (6), K (6), Si (6)
- sample form: Bulk (6)
- measured range: 302-1173 K (5th-95th pct of 6 curves)
- [ref 1] TEDesignLab / ICSD: Na2O Fm-3m (225) mp-2352 [hull=0.000, icsd=3, PRIMARY]; Na2O2 P-62m (189) mp-2340 [hull=0.000, icsd=2, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: NaO2 Pnnm (58) mp-1901 [hull=0.000, icsd=5, PRIMARY]; NaO3 Imm2 (44) mp-22464 [hull=0.079, icsd=3, PRIMARY]; Na6O Cmm2 (35) mp-1173794 [hull=0.142, PRIMARY]; Na2O9 P2_1/c (14) mp-1204051 [hull=0.020, PRIMARY]; Na2O2 Cmcm (63) mp-1094115 [hull=0.201, icsd=2]
- papers: https://doi.org/10.2109/jcersj.108.1256_381 (Thermal Conductivity Measurements of Float Glass at High Temperatures ...)

## Nb-Ni
- rank 1060 | 6 samples | 1 papers | 3 compositions
- compositions: Ni0.50Nb0.50 (4); Ni0.36Nb0.64 (1); Ni0.52Nb0.48 (1)
- measured range: 34-945 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NbNi3 Pmmn (59) mp-1451 [hull=0.001, icsd=7, PRIMARY]; Nb7Ni6 R-3m (166) mp-1104237 [hull=0.014, icsd=3, PRIMARY]; Nb3Ni Fm-3m (225) mp-999396 [hull=0.136, icsd=1, PRIMARY]; NbNi2 P6_3/mmc (194) mp-1103618 [hull=0.076, icsd=1, PRIMARY, AMBIGUOUS]; Nb5Ni Fd-3m (227) mp-669699 [hull=0.212, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/bf01957549 (Electrical resistivity and thermoelectric power of amorphous niobium-n...)

## Nd-Sb
- rank 1061 | 6 samples | 1 papers | 1 compositions
- compositions: (Pr4.76Nd95.24)0.44Fe2Co2Sb12 (6)
- dopant candidates (<5% at.): Pr (6), Fe (6), Co (6)
- measured range: 12-828 K (5th-95th pct of 18 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NdSb Fm-3m (225) mp-1586 [hull=0.000, icsd=12, PRIMARY]; NdSb2 Cmce (64) mp-1102139 [hull=0.005, icsd=3, PRIMARY]; Nd4Sb3 I-43d (220) mp-530 [hull=0.000, icsd=2, PRIMARY]; Nd2Sb I4/mmm (139) mp-12049 [hull=0.000, icsd=2, PRIMARY]; NdSb P4/mmm (123) mp-1213 [hull=0.259, icsd=3]
- papers: https://doi.org/10.1007/978-94-007-4984-9_7 (Changes of Thermoelectric Properties and Hardness After HPT Processing...)

## Nd-Te
- rank 1062 | 6 samples | 1 papers | 6 compositions
- compositions: Nd3Te4 (1); Nd2.84Te4 (1); Nd2.92Te4 (1); Nd2.9Te4 (1); Nd2.86Te4 (1); Nd2.78Te4 (1)
- sample form: compact (6)
- measured range: 58-1286 K (5th-95th pct of 30 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NdTe Fm-3m (225) mp-570 [hull=0.000, icsd=8, PRIMARY]; NdTe3 Cmcm (63) mp-740 [hull=0.000, icsd=5, PRIMARY]; Nd3Te4 I-43d (220) mp-2204 [hull=0.024, icsd=4, PRIMARY]; NdTe2 P4/nmm (129) mp-2550 [hull=0.000, icsd=3, PRIMARY]; Nd2Te3 Pnma (62) mp-16380 [hull=0.000, icsd=3, PRIMARY]
- papers: https://doi.org/10.1021/acs.chemmater.9b00964 (Synthesis and Characterization of Vacancy-Doped Neodymium Telluride fo...)

## Ni-O-Sr
- rank 1063 | 6 samples | 1 papers | 1 compositions
- compositions: Sr1.7Ce0.3NiO4 (6)
- dopant candidates (<5% at.): Ce (6)
- measured range: 17-886 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr(NiO2)4 R-3m (166) mp-18898 [hull=0.000, icsd=1, PRIMARY]; SrNiO2 Cmcm (63) mp-19190 [hull=0.100, icsd=1, PRIMARY]; Sr18Ni13O42 R3 (146) mp-705549 [hull=0.000, PRIMARY]; NaSr12Ni7O23 P1 (1) mp-1221033 [hull=0.063, PRIMARY]; Sr24Ni19O54 P1 (1) mp-698585 [hull=0.005, PRIMARY]
- papers: https://doi.org/10.1023/a:1021375405311 ([])

## Ni-Sb-Yb
- rank 1064 | 6 samples | 2 papers | 5 compositions
- compositions: YbNiSb (2); Yb1.3Ni0.9Sb0.8 (1); Yb1.28Ta0.01Ni0.87Sb0.84 (1); Yb0.78Ta0.07Ni1.2Sb0.95 (1); Yb0.95Ta0.03Ni1.07Sb0.95 (1)
- dopant candidates (<5% at.): Ta (3)
- sample form: Polycrystal (5); Bulk (1)
- measured range: 17-845 K (5th-95th pct of 28 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb2NiSb2 R3m (160) mp-1215858 [hull=0.075, PRIMARY]
- papers: https://doi.org/10.1557/proc-545-421 (Observed Properties and Electronic Structure of RNiSb Compounds (R = H...) | https://doi.org/10.1021/acsaem.2c02269 (Discovery of YbNiSb-Based Half-Heusler Alloys as Promising Thermoelect...)

## Ni-Sn-U
- rank 1065 | 6 samples | 3 papers | 5 compositions
- compositions: UNiSn (2); U2Ni2Sn (1); UNi4Sn (1); UNi2Sn (1); U3Ni3Sn4 (1)
- sample form: Polycrystal (6)
- measured range: 10-308 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UNi4Sn F-43m (216) mp-22197 [hull=0.037, icsd=4, PRIMARY]; UNiSn F-43m (216) mp-21425 [hull=0.116, icsd=3, PRIMARY]; U2Ni2Sn P4/mbm (127) mp-22813 [hull=0.035, icsd=3, PRIMARY]; UNi2Sn Fm-3m (225) mp-672374 [hull=0.031, icsd=1, PRIMARY]; UNiSn C2/m (12) mp-1217516 [hull=0.000]
- papers: https://doi.org/10.1016/0038-1098(95)00391-6 (Magnetoresistance and thermoelectric power in U2Ni2Sn) | https://doi.org/10.1143/jpsj.59.16 (Physical and Structural Properties of Ternary Uranium Compounds in the...) | https://doi.org/10.1143/jpsj.58.2495 (Anomalous Magnetic, Transport and Thermal Properties in the Half-Metal...)

## O-Os-Rb
- rank 1066 | 6 samples | 2 papers | 1 compositions
- compositions: RbOs2O6 (6)
- measured range: 11-300 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Rb(OsO3)2 Fd-3m (227) mp-5050 [hull=0.000, icsd=12, PRIMARY]; RbOs2O9 Pna2_1 (33) mp-1205111 [hull=0.000, icsd=1, PRIMARY]; RbOsO3 R-3 (148) mp-998602 [hull=0.000, PRIMARY]; RbOsO3 Pm-3m (221) mp-1040467 [hull=0.084]
- papers: https://doi.org/10.1016/j.physc.2007.03.023 (Chemical trends of superconducting properties in pyrochlore oxides) | https://doi.org/10.1016/j.physb.2006.01.323 (High-pressure effects on the superconductivity of β-pyrochlore oxides ...)

## O-Pu
- rank 1067 | 6 samples | 2 papers | 1 compositions
- compositions: PuO2 (6)
- measured range: 298-1499 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PuO2 Fm-3m (225) mp-1959 [hull=0.000, icsd=5, PRIMARY]; Pu2O3 P-3m1 (164) mp-21423 [hull=0.067, icsd=5, PRIMARY]; PuO Fm-3m (225) mp-806 [hull=0.095, icsd=2, PRIMARY]; Pu3O2 R-3c (167) mp-867185 [hull=0.193, PRIMARY]; Pu2O3 Ia-3 (206) mp-637224 [hull=0.000, icsd=1]
- papers: https://doi.org/10.1016/j.jnucmat.2008.05.003 (Applicability of CeO2 as a surrogate for PuO2 in a MOX fuel development) | https://doi.org/10.1016/j.jallcom.2014.12.204 (Thermal conductivity of UO2 and PuO2 from first-principles)

## O-Sb-Zn
- rank 1068 | 6 samples | 2 papers | 5 compositions
- compositions: Zn0.9In0.1Sb2O6 (2); Zn7Sb2O12 (1); Zn0.95Al0.05Sb2O6 (1); ZnSb2O6 (1); Zn0.9Al0.1Sb2O6 (1)
- dopant candidates (<5% at.): Al (2), In (2)
- sample form: Bulk (5)
- measured range: 295-880 K (5th-95th pct of 8 curves; full span incl. outliers 295-1073 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zn(SbO2)2 P4_2/mbc (135) mp-5388 [hull=0.013, icsd=9, PRIMARY]; Zn(SbO3)2 P4_2/mnm (136) mp-3188 [hull=0.000, icsd=2, PRIMARY]; Zn7(SbO6)2 C2/c (15) mp-675797 [hull=0.009, PRIMARY, AMBIGUOUS]; Zn7(SbO6)2 P-1 (2) mp-1215862 [hull=0.013]
- papers: https://doi.org/10.1016/j.jallcom.2007.01.080 (Improvement of thermoelectric properties with the addition of Sb to ZnO) | https://doi.org/10.1002/pssa.200669537 (Thermoelectric properties of Zn1-xMxSb2O6(M = Al, In))

## O-Sm-Ta
- rank 1069 | 6 samples | 1 papers | 6 compositions
- compositions: (Sm3TaO7)0.92(ZrO2)0.08 (1); Sm3TaO7 (1); (Sm3TaO7)0.98(ZrO2)0.02 (1); (Sm3TaO7)0.96(ZrO2)0.04 (1); (Sm3TaO7)0.94(ZrO2)0.06 (1); (Sm3TaO7)0.90(ZrO2)0.10 (1)
- dopant candidates (<5% at.): Zr (5)
- sample form: Bulk (6)
- measured range: 371-1173 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SmTaO4 C2/c (15) mp-3756 [hull=0.005, icsd=2, PRIMARY]; Sm3TaO7 Cmcm (63) mp-1192238 [hull=0.003, icsd=1, PRIMARY]; Sm3Ta17O47 P2/m (10) mp-765640 [hull=0.000, PRIMARY]; Sm2Ta2O9 P2_1/c (14) mp-1208912 [hull=0.148, PRIMARY]; SmTaO4 P2/c (13) mp-12931 [hull=0.000, icsd=1]
- papers: https://doi.org/10.1080/21870764.2021.1907025 (Investigation of thermophysical properties of ZrO2-Sm3TaO7 ceramics)

## O-Ti-W
- rank 1070 | 6 samples | 1 papers | 6 compositions
- compositions: Ti0.87W0.13O (1); Ti0.79W0.21O (1); Ti0.74W0.26O (1); Ti0.6W0.4O (1); Ti0.54W0.46O (1); Ti0.42W0.58O (1)
- measured range: 11-319 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti3(WO6)2 P2_1/c (14) mp-776763 [hull=0.040, PRIMARY]; Ti7(WO5)6 P3 (143) mp-853224 [hull=0.074, PRIMARY]; TiWO4 P2/m (10) mp-765868 [hull=0.051, PRIMARY]
- papers: https://doi.org/10.1116/1.1525818 (Epitaxial Ti1-xWxN alloys grown on MgO(001) by ultrahigh vacuum reacti...)

## O-Ti-Zn
- rank 1071 | 6 samples | 1 papers | 6 compositions
- compositions: (NiO)0.3(TiO)20(ZnO)79.7 (1); (NiO)6(TiO)12(ZnO)82 (1); (NiO)6(TiO)10(ZnO)84 (1); (NiO)4.5(TiO)10(ZnO)85.5 (1); (NiO)5(TiO)11(ZnO)84 (1); (NiO)4.9(TiO)11(ZnO)84.1 (1)
- dopant candidates (<5% at.): Ni (6)
- measured range: 80-756 K (5th-95th pct of 6 curves)
- [ref 1] TEDesignLab / ICSD: TiZnO3 R-3 (148) mp-14142 [hull=0.028, icsd=2, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ti3Zn2O8 P4_332 (212) mp-29104 [hull=0.000, icsd=1, PRIMARY]; CaTi8Zn2O19 P1 (1) mp-1227270 [hull=0.024, PRIMARY]; TaTi9Al3Zn23O48 P1 (1) mp-695545 [hull=0.053, PRIMARY]; TiZn2O4 Imma (74) mp-33631 [hull=0.046, PRIMARY]; TiZnO3 R3c (161) mp-1078470 [hull=0.055, icsd=1]
- papers: https://doi.org/10.1016/0038-1101(63)90004-2 (Positive temperature coefficient of electrical resistivity in some ZnO...)

## P-Pt-Sr
- rank 1072 | 6 samples | 1 papers | 1 compositions
- compositions: SrPt10P4 (6)
- measured range: 13-276 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr(P3Pt2)2 C2/c (15) mp-8507 [hull=0.000, icsd=1, PRIMARY]; Sr(PPt3)2 Pa-3 (205) mp-1194990 [hull=0.000, icsd=1, PRIMARY]; SrPPt P-6m2 (187) mp-1217967 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevmaterials.1.064801 (Superconductivity in the ternary compound \nSrPt10P4\n with complex ne...)

## P-Si
- rank 1073 | 6 samples | 3 papers | 6 compositions
- compositions: Si0.94P0.06 (1); Si0.95Ge0.05P0.04Ga0.05P0.05 (1); Si94.5P4(GaP)1.5 (1); Si93.5P5(GaP)1.5 (1); Si92.5P5(GaP)2.5 (1); Si91.5P5(GaP)3.5 (1)
- dopant candidates (<5% at.): Ga (5), Ge (1)
- sample form: Bulk (6)
- measured range: 300-1214 K (5th-95th pct of 33 curves)
- [ref 1] TEDesignLab / ICSD: SiP Cmc2_1 (36) mp-2798 [hull=0.000, icsd=2, PRIMARY]; SiP2 Pbam (55) mp-9996 [hull=0.000, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: SiP2 Pa-3 (205) mp-21065 [hull=0.018, icsd=10, PRIMARY]; Si3P Fm-3m (225) mp-972741 [hull=0.627, PRIMARY]; SiP F-43m (216) mp-8097 [hull=0.385, icsd=1]
- papers: https://doi.org/10.1002/aelm.201600171 (The Role of Electron-Phonon Interaction in Heavily Doped Fine-Grained ...) | https://doi.org/10.1063/1.1352686 (Thermoelectric properties of heavily GaP- and P-doped Si0.95Ge0.05) | https://doi.org/10.1021/acsami.1c12200 (High-Performance n-Type Ge-Free Silicon Thermoelectric Material from S...)

## P-W
- rank 1074 | 6 samples | 2 papers | 1 compositions
- compositions: WP2 (6)
- measured range: 12-300 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PW Pnma (62) mp-2420 [hull=0.000, icsd=5, PRIMARY]; P2W Cmc2_1 (36) mp-11328 [hull=0.000, icsd=3, PRIMARY]; PW3 I-4 (82) mp-1106195 [hull=0.076, icsd=1, PRIMARY]; P3W Fm-3m (225) mp-1186361 [hull=0.748, PRIMARY]; P2W C2/m (12) mp-11329 [hull=0.015, icsd=2]
- papers: https://doi.org/10.1038/s41467-018-06688-y (Thermal and electrical signatures of a hydrodynamic electron fluid in ...) | https://doi.org/10.1038/s41535-018-0136-x (Departure from the Wiedemann–Franz law in WP2 driven by mismatch in T-...)

## Pb-Pr
- rank 1075 | 6 samples | 1 papers | 1 compositions
- compositions: PrPb3 (6)
- measured range: 10-10 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrPb3 Pm-3m (221) mp-20939 [hull=0.000, icsd=3, PRIMARY]; Pr3Pb Pm-3m (221) mp-21481 [hull=0.000, icsd=2, PRIMARY]; Pr5Pb3 P6_3/mcm (193) mp-1188302 [hull=0.000, icsd=2, PRIMARY]; PrPb2 I4_1/amd (141) mp-1103021 [hull=0.000, icsd=1, PRIMARY]; PrPb2 I4/mmm (139) mp-1207242 [hull=0.346]
- papers: https://doi.org/10.1088/1742-6596/683/1/012031 (Non-Fermi Liquid Properties in a Cubic Pr-Based Compound PrPb3under Ma...)

## Pb-Te-Tl
- rank 1076 | 6 samples | 2 papers | 5 compositions
- compositions: Tl4PbTe3 (2); Tl8.10Pb1.90Te6 (1); Tl7.95Pb2.05Te6 (1); Tl8.05Pb1.95Te6 (1); Tl8.075Pb1.925Te6 (1)
- sample form: Bulk (5); OrientedBulk (1)
- measured range: 298-690 K (5th-95th pct of 29 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Tl4Te3Pb I4/mcm (140) mp-20740 [hull=0.000, icsd=5, PRIMARY]
- papers: https://doi.org/10.1002/aenm.201400348 (Improved Bulk Materials with Thermoelectric Figure-of-Merit Greater th...) | https://doi.org/10.1063/1.2181427 (Thermoelectric properties of Tl–X–Te (X=Ge, Sn, and Pb) compounds with...)

## Pd-U-Y
- rank 1077 | 6 samples | 2 papers | 6 compositions
- compositions: Y0.8U0.2Pd3 (1); Y0.6U0.4Pd3 (1); Y0.7U0.3Pd3 (1); U0.2Y0.8Pd3 (1); U0.3Y0.7Pd3 (1); U0.4Y0.6Pd3 (1)
- sample form: Bulk (3); Polycrystal (3)
- solid-solution axis: U/(U+Y) spans 0.20-0.40 (median 0.30) over 6 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-299 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y4UPd15 P4/mmm (123) mp-1216177 [hull=0.000, PRIMARY]; YUPd6 P4/mmm (123) mp-1215718 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.49.6400 (Evidence for the Kondo effect and crossover in transport behavior forx...) | https://doi.org/10.1016/0921-4526(94)91847-3 (Evidence for Kondo effect and crossover in electronic structure for x ...)

## Pt-Te
- rank 1078 | 6 samples | 2 papers | 6 compositions
- compositions: PtTe2 (1); Pt1.01TeAg0.003 (1); Pt1.01TeAg0.005 (1); Pt1.01TeAg0.001 (1); Pt1.01TeAg0.002 (1); Pt1.01TeAg0.004 (1)
- dopant candidates (<5% at.): Ag (5)
- sample form: cylinder (5)
- measured range: 298-775 K (5th-95th pct of 30 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Te2Pt P-3m1 (164) mp-399 [hull=0.000, icsd=6, PRIMARY]; Te4Pt3 R-3m (166) mp-8628 [hull=0.000, icsd=2, PRIMARY]; TePt R-3m (166) mp-11693 [hull=0.000, icsd=2, PRIMARY]; Te4Pt3 C2/m (12) mp-21042 [hull=0.598, icsd=1]
- papers: https://doi.org/10.1002/adma.200900312 (Binary-Phased Nanoparticles for Enhanced Thermoelectric Properties) | https://doi.org/10.1021/acs.chemmater.2c03542 (Fine Tuning of Defects Enables High Carrier Mobility and Enhanced Ther...)

## S-Se-W
- rank 1079 | 6 samples | 1 papers | 6 compositions
- compositions: W0.94Nb0.06Se1.7S0.3 (1); W0.96Nb0.04Se1.7S0.3 (1); W0.98Nb0.02Se1.7S0.3 (1); W0.98Nb0.02Se1.8S0.2 (1); W0.98Nb0.02Se1.6S0.4 (1); W0.98Nb0.02Se1.5S0.5 (1)
- dopant candidates (<5% at.): Nb (6)
- sample form: Bulk (6)
- measured range: 20-652 K (5th-95th pct of 22 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): W2Se3S P3m1 (156) mp-1028686 [hull=0.010, PRIMARY]; W2SeS3 P3m1 (156) mp-1028558 [hull=0.010, PRIMARY]; W3(Se2S)2 P-6m2 (187) mp-1025588 [hull=0.013, PRIMARY, AMBIGUOUS]; W3(SeS2)2 P3m1 (156) mp-1025577 [hull=0.013, PRIMARY, AMBIGUOUS]; WSeS P-3m1 (164) mp-1216174 [hull=0.010, PRIMARY, AMBIGUOUS]
- papers: https://doi.org/10.1111/jace.16455 (Thermoelectric properties of W\n            \n              1−\n      ...)

## S-Tb
- rank 1080 | 6 samples | 3 papers | 3 compositions
- compositions: Tb2S3 (3); TbS1.43 (2); TbS (1)
- sample form: Bulk (3)
- measured range: 98-981 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TbS2 P4/nmm (129) mp-7135 [hull=0.000, icsd=3, PRIMARY]; TbS Fm-3m (225) mp-1610 [hull=0.000, icsd=3, PRIMARY]; Tb2S3 Pnma (62) mp-9323 [hull=0.000, icsd=1, PRIMARY]; Tb5S7 C2/m (12) mp-1095641 [hull=0.000, icsd=1, PRIMARY]; Tb3S Pm-3m (221) mp-1187302 [hull=0.718, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2005.10.065 (Effect of non-stoichiometry on thermoelectric properties of -Tb2S3−x) | https://doi.org/10.1016/j.jallcom.2007.04.078 (Thermoelectric properties of Th3P4-type rare-earth sulfides Ln2S3 (Ln=...) | https://doi.org/10.1134/s0020168514040049 (Preparation and electrical and optical properties of TbS films)

## S-W
- rank 1081 | 6 samples | 4 papers | 3 compositions
- compositions: WS2 (4); WS2C0.02 (1); WS2C0.1 (1)
- dopant candidates (<5% at.): C (2)
- sample form: Bulk (3); Film (1)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 99-782 K (5th-95th pct of 24 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): WS2 P6_3/mmc (194) mp-224 [hull=0.000, icsd=5, PRIMARY]; W21S8 I4/m (87) mp-1207867 [hull=0.516, PRIMARY]; WS P6_3mc (186) mp-1004526 [hull=0.430, PRIMARY]; WS2 R3m (160) mp-9813 [hull=0.004, icsd=2]; WS2 P-3m1 (164) mp-1028441 [hull=0.001]
- papers: https://doi.org/10.1039/c5ee03813h (Chemically exfoliated transition metal dichalcogenide nanosheet-based ...) | https://doi.org/10.1038/s41598-020-57991-y (A thin film efficient pn-junction thermoelectric device fabricated by ...) | https://doi.org/10.3390/cryst10020140 (Enhanced Thermoelectric Properties of WS2/Single-Walled Carbon Nanohor...)

## Sb-Sr-Zn
- rank 1082 | 6 samples | 4 papers | 2 compositions
- compositions: SrZn2Sb2 (3); SrZnSb2 (3)
- sample form: Other (1); Bulk (1)
- measured range: 12-727 K (5th-95th pct of 13 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr(ZnSb)2 P-3m1 (164) mp-7431 [hull=0.000, icsd=1, PRIMARY]; SrZnSb2 Pnma (62) mp-12275 [hull=0.000, icsd=1, PRIMARY]; Sr2ZnSb2 P-6m2 (187) mp-1218373 [hull=0.064, PRIMARY]
- papers: https://doi.org/10.1039/b914172c (Electronic structure and transport in thermoelectric compounds AZn2Sb2...) | https://doi.org/10.1007/s11664-010-1151-2 (Thermoelectric Properties of Polycrystalline SrZn2Sb2 Prepared by Spar...) | https://doi.org/10.1063/1.3158553 (Transport properties of the layered Zintl compound SrZnSb2)

## Si-Ti
- rank 1083 | 6 samples | 3 papers | 3 compositions
- compositions: Si95Ti5 (3); Ti5Si3 (2); TiSi2 (1)
- sample form: Bulk (5)
- measured range: 302-1071 K (5th-95th pct of 17 curves; full span incl. outliers 302-1137 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiSi2 Fddd (70) mp-2582 [hull=0.006, icsd=6, PRIMARY]; Ti5Si3 P6_3/mcm (193) mp-2108 [hull=0.000, icsd=6, PRIMARY]; TiSi Pnma (62) mp-7092 [hull=0.000, icsd=3, PRIMARY]; Ti3Si P4_2/n (86) mp-980420 [hull=0.016, icsd=2, PRIMARY]; Ti2Si F-43m (216) mp-1008689 [hull=0.966, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2003.12.008 (Electrical and thermal properties of single crystalline Mo 5 X 3  (X=S...) | https://doi.org/10.1063/5.0016049 (Synthesis and characterization of bulk Si–Ti nanocomposite and compari...) | https://doi.org/10.1007/bf00792195 (Physical properties of Cr1−xTixSiyyyand Cr1−xTaxSi2+y solid solutions)

## Ta-W
- rank 1084 | 6 samples | 1 papers | 6 compositions
- compositions: W0.25Ta0.75 (1); W0.5Ta0.5 (1); W0.67Ta0.33 (1); W0.05Ta0.95 (1); W0.1Ta0.9 (1); W0.85Ta0.15 (1)
- measured range: 12-299 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ta3W Fm-3m (225) mp-1187206 [hull=0.000, PRIMARY]; TaW Cmmm (65) mp-1217811 [hull=0.010, PRIMARY]; TaW3 Fm-3m (225) mp-979289 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1063/1.327772 (Thermoelectric power of tantalum‐tungsten alloys)

## U-Zr
- rank 1085 | 6 samples | 2 papers | 6 compositions
- compositions: U86Zr14 (1); U8.8Zr91.2 (1); U65.4Zr34.6 (1); U47.8Zr52.2 (1); U27.6Zr72.4 (1); U23.87Zr76.13 (1)
- sample form: Bulk (1)
- measured range: 287-885 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zr2U P-6m2 (187) mp-1215541 [hull=0.196, PRIMARY]; ZrU Cmmm (65) mp-1215193 [hull=0.237, PRIMARY]; ZrU3 I4/mmm (139) mp-1183047 [hull=0.385, PRIMARY]; Zr2U P6/mmm (191) mp-1206978 [hull=0.296]
- papers: https://doi.org/10.1016/0022-3115(88)90127-4 (Thermophysical properties of uranium-zirconium alloys) | https://doi.org/10.1016/s0022-3115(01)00444-5 (Thermal properties of hydride fuel 45% U–ZrH1.6)

## Ag-Bi-O-Se
- rank 1086 | 5 samples | 2 papers | 5 compositions
- compositions: (Bi2O2Se)51.68(Ag)48.32 (1); (Bi2O2Se)43.01(Ag)56.99 (1); (Bi2O2Se)78.19(Ag)21.81 (1); (Bi2O2Se)62.94(Ag)37.06 (1); BiAgOSe (1)
- sample form: Bulk (5)
- solid-solution axis: O/(O+Se) spans 0.50-0.67 (median 0.67) over 5 compositions
     CHECK: same periodic group, but oxygen often occupies its own sublattice (BiCuSeO, LaFeAsO) rather than substituting for the heavier chalcogen. Confirm the two share a site before treating this as a substitution axis.
- measured range: 201-674 K (5th-95th pct of 17 curves)
- papers: https://doi.org/10.3390/ma8041568 (Enhanced Thermoelectric Performance of Bi2O2Se with Ag Addition) | https://doi.org/10.1021/acs.chemmater.7b04962 (Substituting Copper with Silver in the BiMOCh Layered Compounds (M = C...)

## Ag-Cu-I-Mo-O
- rank 1087 | 5 samples | 1 papers | 5 compositions
- compositions: (Cu0.95Ag0.05I)30(Ag2O)35(MoO3)35 (1); (Cu0.9Ag0.1I)30(Ag2O)35(MoO3)35 (1); (Cu0.8Ag0.2I)30(Ag2O)35(MoO3)35 (1); (Cu0.85Ag0.15I)30(Ag2O)35(MoO3)35 (1); (Cu0.75Ag0.25I)30(Ag2O)35(MoO3)35 (1)
- measured range: 294-444 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/s0921-5107(02)00081-8 (An evaluation of superionic properties of the ternary system (Cu1−xAgx...)

## Ag-Cu-S-Se
- rank 1088 | 5 samples | 1 papers | 5 compositions
- compositions: (Ag0.2Cu0.8)2S0.7Se0.3 (1); (Ag0.2Cu0.785)2S0.7Se0.3 (1); (Ag0.2Cu0.78)2S0.7Se0.3 (1); (Ag0.2Cu0.795)2S0.7Se0.3 (1); (Ag0.2Cu0.79)2S0.7Se0.3 (1)
- sample form: Bulk (5)
- measured range: 299-804 K (5th-95th pct of 25 curves)
- papers: https://doi.org/10.1002/aenm.202100883 (p‐Type Plastic Inorganic Thermoelectric Materials)

## Ag-Ga-S
- rank 1089 | 5 samples | 1 papers | 5 compositions
- compositions: Ag9GaS6 (1); Ag9Ga(S0.92Se0.08)6 (1); Ag9Ga(S0.97Se0.03)6 (1); Ag9Ga(S0.95Se0.05)6 (1); Ag9Ga(S0.9Se0.1)6 (1)
- dopant candidates (<5% at.): Se (4)
- sample form: Bulk (5)
- measured range: 299-806 K (5th-95th pct of 30 curves)
- [ref 1] TEDesignLab / ICSD: GaAgS2 I-42d (122) mp-5342 [hull=0.000, icsd=16, PRIMARY]; GaAgS2 (9)
- [ref 2] MP, ranked by ICSD evidence: GaAgS2 R3m (160) mp-1096972 [hull=0.176]
- papers: https://doi.org/10.1016/j.mtphys.2018.09.001 (Thermoelectric properties of Ag9GaS6 with ultralow lattice thermal con...)

## Ag-Ge-Mn-Sb-Te
- rank 1090 | 5 samples | 1 papers | 5 compositions
- compositions: AgMnGeSbTe4 (1); (AgMnGeSbTe4)0.99(Ag8GeTe6)0.01 (1); (AgMnGeSbTe4)0.96(Ag8GeTe6)0.04 (1); (AgMnGeSbTe4)0.98(Ag8GeTe6)0.02 (1); (AgMnGeSbTe4)0.97(Ag8GeTe6)0.03 (1)
- sample form: Polycrystal (5)
- measured range: 299-776 K (5th-95th pct of 30 curves)
- papers: https://doi.org/10.1002/adfm.202103197 (High Entropy Semiconductor AgMnGeSbTe\n            4\n            with...)

## Ag-Pb-Sb-Te
- rank 1091 | 5 samples | 2 papers | 4 compositions
- compositions: AgPb4SbTe6 (2); AgPb2SbTe4 (1); AgPb6SbTe8 (1); AgPb8SbTe10 (1)
- sample form: Bulk (1)
- measured range: 297-672 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AgSb(Te8Pb7)2 I4/mmm (139) mp-1229237 [hull=0.098, PRIMARY]; AgSbTe3Pb Imm2 (44) mp-1229036 [hull=0.468, PRIMARY]
- papers: https://doi.org/10.1109/ict.2005.1519883 (Thermoelectric properties of n-type Ag-Pb-Sb-Te compounds) | https://doi.org/10.1016/j.ijhydene.2015.12.205 (Structural, characterization and electrical properties of AgPbmSbTem+2...)

## Ag-S-Se
- rank 1092 | 5 samples | 2 papers | 5 compositions
- compositions: Ag4SeS (1); Ag2Se0.8S0.2 (1); Ag2Se0.55S0.45 (1); Ag2Se0.7S0.3 (1); Ag2Se0.6S0.4 (1)
- sample form: Bulk (5)
- solid-solution axis: S/(S+Se) spans 0.20-0.50 (median 0.40) over 5 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 294-472 K (5th-95th pct of 24 curves)
- papers: https://doi.org/10.1021/ja2104476 (Superionic Phase Transition in Silver Chalcogenide Nanocrystals Realiz...) | https://doi.org/10.34133/2020/6591981 (Crystalline Structure-Dependent Mechanical and Thermoelectric Performa...)

## Ag-Se-Si
- rank 1093 | 5 samples | 1 papers | 1 compositions
- compositions: Ag8SiSe6 (5)
- sample form: Polycrystal (5)
- measured range: 300-425 K (5th-95th pct of 13 curves)
- papers: https://doi.org/10.1021/acs.chemmater.7b00767 (High Electron Mobility and Disorder Induced by Silver Ion Migration Le...)

## Al-Au-Yb
- rank 1094 | 5 samples | 2 papers | 5 compositions
- compositions: Au49Al34Yb17 (1); Au50Al35Yb15 (1); Au48Al37Yb15 (1); Au49Al36Yb15 (1); Au51Al34Yb15 (1)
- measured range: 17-883 K (5th-95th pct of 21 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbAlAu Pnma (62) mp-12784 [hull=0.000, icsd=2, PRIMARY]; YbAl7Au3 R-3c (167) mp-16625 [hull=0.000, icsd=1, PRIMARY]; YbAl3Au I4mm (107) mp-1215459 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2015.08.081 (Thermoelectric properties of Tsai-type Au–Al–RE (RE: Yb, Tm, Gd) quasi...) | https://doi.org/10.1016/j.jallcom.2013.10.073 (Electronic density of states and metastability of icosahedral Au–Al–Yb...)

## Al-Cu
- rank 1095 | 5 samples | 4 papers | 3 compositions
- compositions: Cu76.12Al23.88 (2); Al2Cu (2); Al57.7Cu37.7Fe3.5Si1.1 (1)
- dopant candidates (<5% at.): Fe (1), Si (1)
- measured range: 10-873 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al2Cu I4/mcm (140) mp-998 [hull=0.021, icsd=6, PRIMARY]; Al4Cu9 P-43m (215) mp-593 [hull=0.000, icsd=5, PRIMARY]; AlCu3 Pm-3m (221) mp-1008555 [hull=0.009, icsd=2, PRIMARY]; AlCu C2/m (12) mp-2500 [hull=0.000, icsd=2, PRIMARY]; Al3Cu2 P-3m1 (164) mp-10886 [hull=0.034, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/s12598-011-0443-x (Effects of cryogenic treatment on the thermal physical properties of C...) | https://doi.org/10.1109/ict.2007.4569499 (Low thermal conductivity of Al-based icosahedral quasicrystals and app...) | https://doi.org/10.1016/j.jallcom.2017.08.156 (Study on thermal conductivity and electrical resistivity of Al-Cu allo...)

## Al-Dy
- rank 1096 | 5 samples | 4 papers | 1 compositions
- compositions: DyAl2 (5)
- sample form: Bulk (1)
- measured range: 10-247 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DyAl2 Fd-3m (227) mp-803 [hull=0.000, icsd=17, PRIMARY]; DyAl Pbcm (57) mp-433 [hull=0.000, icsd=4, PRIMARY]; DyAl3 R-3m (166) mp-1103088 [hull=0.006, icsd=2, PRIMARY]; Dy2Al Pnma (62) mp-1102728 [hull=0.000, icsd=1, PRIMARY]; Dy2Al17 P6_3/mmc (194) mp-1198587 [hull=0.070, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(83)90564-4 (Thermoelectric power of RAl2) | https://doi.org/10.1109/tjmj.1988.4563688 (Preparation of a High Density Complex Type Magnetic Mixture of RAl2 Sy...) | https://doi.org/10.1088/0305-4608/16/4/013 (Thermal conductivity of REAl2compounds (RE=rare earth))

## Al-F-V
- rank 1097 | 5 samples | 1 papers | 5 compositions
- compositions: (F0.99Re0.01)2VAl (1); (F0.98Re0.02)2VAl (1); (F0.96Re0.04)2VAl (1); F2VAl (1); (F0.94Re0.06)2VAl (1)
- dopant candidates (<5% at.): Re (4)
- sample form: Bulk (5)
- measured range: 12-1243 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.2320/jinstmet.71.208 (Effects of Re Substitution on Thermoelectric Properties of Pseudogap S...)

## Al-Fe-Pd
- rank 1098 | 5 samples | 3 papers | 5 compositions
- compositions: Al71Pd20Re3.15Fe5.85 (1); Al71Pd20Re3.15Fe5.85_IQC (1); Al70Pd20Fe8Mn2 (1); Al70Pd20Fe6Mn4 (1); Al70Pd20Fe10 (1)
- dopant candidates (<5% at.): Re (2), Mn (2)
- sample form: Bulk (1)
- measured range: 12-932 K (5th-95th pct of 9 curves)
- papers: https://doi.org/10.1063/1.2716212 (Improvement of thermoelectric properties of icosahedral AlPdRe quasicr...) | https://doi.org/10.1088/1468-6996/15/4/044802 (Metallic–covalent bonding conversion and thermoelectric properties of ...) | https://doi.org/10.1088/0953-8984/6/49/016 (Thermal stability, electrical and magnetic properties of icosahedral A...)

## Al-La-Ru
- rank 1099 | 5 samples | 2 papers | 2 compositions
- compositions: Ce0.1La0.9Ru2Al10 (3); Ce0.3La0.7Ru2Al10 (2)
- dopant candidates (<5% at.): Ce (5)
- sample form: SingleCrystal (3); Polycrystal (2)
- measured range: 10-314 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La5Al2Ru3 I2_13 (199) mp-1185199 [hull=0.000, icsd=1, PRIMARY]; La(Al5Ru)2 Cmcm (63) mp-1211269 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1143/jpsj.79.063709 (Anisotropic Transport Properties of CeRu2Al10) | https://doi.org/10.1088/1361-648x/abfee3 (Effects of Y- and La-doping on the magnetic ordering, Kondo effect, an...)

## Al-Mg
- rank 1100 | 5 samples | 3 papers | 3 compositions
- compositions: Al3Mg2 (2); Al94.6Mg5.2Mn0.1Cr0.1 (2); Mg91.39Al8.23Zn0.38 (1)
- dopant candidates (<5% at.): Mn (2), Cr (2), Zn (1)
- sample form: Bulk (2)
- measured range: 14-300 K (5th-95th pct of 5 curves; full span incl. outliers 14-573 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg17Al12 I-43m (217) mp-2151 [hull=0.028, icsd=5, PRIMARY]; Mg13Al16 I-43m (217) mp-1194114 [hull=0.068, icsd=1, PRIMARY]; MgAl2 I4_1/amd (141) mp-1102064 [hull=0.065, icsd=1, PRIMARY]; Mg23Al30 R-3 (148) mp-17659 [hull=0.033, icsd=1, PRIMARY]; Mg13Al14 Im-3m (229) mp-12766 [hull=0.112, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2007.04.010 (Magnetic and transport properties of the giant-unit-cell Al3.26Mg2 com...) | https://doi.org/10.1088/0022-3735/16/7/030 (Thermal and superconducting properties of an aluminium alloy for gravi...) | https://doi.org/10.1016/j.scriptamat.2008.10.022 (Thermal diffusivity and thermal conductivity of Mg–Zn–rare earth eleme...)
