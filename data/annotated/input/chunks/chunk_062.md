# Host systems -- chunk 062 of 73

Ranks 3051-3100 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 98.95%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Cs-Gd-Mo-O
- rank 3051 | 1 samples | 1 papers | 1 compositions
- compositions: CsGd(MoO4)2 (1)
- measured range: 10-49 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CsGd(MoO4)2 P2/c (13) mp-1191993 [hull=0.002, icsd=1, PRIMARY]; CsGd(MoO4)2 Pccm (49) mp-1213392 [hull=0.000]; CsGd(MoO4)2 C2/c (15) mp-1213304 [hull=0.041]
- papers: https://doi.org/10.12693/aphyspola.118.971 (Thermal Conductivity of a Layered CsGd(MoO4)2Crystal)

## Cs-Ge-I-Sn
- rank 3052 | 1 samples | 1 papers | 1 compositions
- compositions: CsSn0.7Ge0.3I3 (1)
- measured range: 298-470 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1021/acs.jpcc.0c00459 (Enhanced Thermoelectric Performance in Lead-Free Inorganic CsSn1–xGexI...)

## Cs-Mo-Se
- rank 3053 | 1 samples | 1 papers | 1 compositions
- compositions: Cs2Mo12Se14 (1)
- measured range: 11-574 K (5th-95th pct of 2 curves; full span incl. outliers 11-618 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cs(MoSe)3 P6_3/m (176) mp-1104663 [hull=0.000, icsd=3, PRIMARY]; CsMo6Se7 R-3 (148) mp-5883 [hull=0.013, icsd=2, PRIMARY]; Cs2MoSe4 Pnma (62) mp-866654 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/acs.inorgchem.6b00781

## Cs-O-Os
- rank 3054 | 1 samples | 1 papers | 1 compositions
- compositions: CsOsO6 (1)
- measured range: 17-177 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CsOs2O9 Cc (9) mp-1192392 [hull=0.000, icsd=1, PRIMARY]; CsOsO3 Pm-3m (221) mp-1183914 [hull=0.247, PRIMARY]
- papers: https://doi.org/10.1016/j.physc.2007.03.023 (Chemical trends of superconducting properties in pyrochlore oxides)

## Cs-O-Ta-W
- rank 3055 | 1 samples | 1 papers | 1 compositions
- compositions: CsTaWO6 (1)
- measured range: 382-979 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CsTaWO6 Imma (74) mp-1225854 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1007/s11664-012-2382-1 (Extremely Low Thermal Conductivity in Oxides with Cage-Like Crystal St...)

## Cs-O-W
- rank 3056 | 1 samples | 1 papers | 1 compositions
- compositions: CsFe0.33W1.67O6 (1)
- dopant candidates (<5% at.): Fe (1)
- measured range: 324-1045 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cs(WO3)2 Fd-3m (227) mp-25175 [hull=0.013, icsd=1, PRIMARY]; Cs2WO4 Pnma (62) mp-1193656 [hull=0.000, icsd=1, PRIMARY]; Cs(WO3)3 P6/mmm (191) mp-763713 [hull=0.000, PRIMARY]; Cs2(WO4)3 P1 (1) mp-1227596 [hull=0.191, PRIMARY]; Cs2WO8 P2_1/c (14) mp-1213748 [hull=0.115, PRIMARY]
- papers: https://doi.org/10.1007/s11664-015-4179-5 (Crystal Structure and Thermoelectric Properties of β-Pyrochlore-Type A...)

## Cs-Sn
- rank 3057 | 1 samples | 1 papers | 1 compositions
- compositions: Cs8Sn44 (1)
- measured range: 11-224 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cs4Sn23 Pm-3n (223) mp-2496 [hull=0.000, icsd=3, PRIMARY]; CsSn I4_1/acd (142) mp-11055 [hull=0.006, icsd=2, PRIMARY]; Cs2Sn11 Ama2 (40) mp-1096991 [hull=0.046, PRIMARY]; CsSn3 P6_3/mmc (194) mp-865565 [hull=0.057, PRIMARY]
- papers: https://doi.org/10.1063/1.4983817 (High-temperature thermal conductivity of thermoelectric clathrates)

## Cu-Dy
- rank 3058 | 1 samples | 1 papers | 1 compositions
- compositions: Dy2Cu9 (1)
- measured range: 12-293 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DyCu Pm-3m (221) mp-2334 [hull=0.000, icsd=7, PRIMARY]; DyCu5 F-43m (216) mp-30578 [hull=0.000, icsd=2, PRIMARY]; DyCu2 Imma (74) mp-1071835 [hull=0.000, icsd=2, PRIMARY]; Dy6Cu23 Fm-3m (225) mp-1194041 [hull=0.015, icsd=1, PRIMARY]; DyCu7 Pmmm (47) mp-1225716 [hull=0.046, PRIMARY]
- papers: https://doi.org/10.1016/0375-9601(96)00055-2 (Electrical resistivity and thermopower of Gd2Cu9 and Dy2Cu9)

## Cu-Dy-In
- rank 3059 | 1 samples | 1 papers | 1 compositions
- compositions: DyInCu4 (1)
- measured range: 24-292 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DyInCu P-62m (189) mp-1080594 [hull=0.000, icsd=2, PRIMARY]; DyInCu2 Fm-3m (225) mp-22680 [hull=0.022, icsd=2, PRIMARY]; DyIn3Cu2 P6/mmm (191) mp-639756 [hull=0.171, icsd=1, PRIMARY]; DyInCu4 F-43m (216) mp-1080384 [hull=0.000, icsd=1, PRIMARY]; Dy(InCu)6 Immm (71) mp-1225823 [hull=0.008, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(94)01472-8 (Transport properties of RInCu4 with C15b-type structure)

## Cu-Dy-Se
- rank 3060 | 1 samples | 1 papers | 1 compositions
- compositions: DyCuSe2 (1)
- measured range: 297-767 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Dy(CuSe)3 R-3 (148) mp-1225403 [hull=0.006, PRIMARY]; Dy3CuSe6 Pca2_1 (29) mp-1225646 [hull=0.027, PRIMARY]; DyCuSe2 P3m1 (156) mp-675349 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2014.05.017 (Thermoelectric properties, crystal and electronic structure of semicon...)

## Cu-Dy-Te
- rank 3061 | 1 samples | 1 papers | 1 compositions
- compositions: Cu3DyTe3 (1)
- measured range: 299-902 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Dy(CuTe)3 R-3 (148) mp-1225395 [hull=0.035, PRIMARY]; Dy7(CuTe4)3 P1 (1) mp-676306 [hull=0.000, PRIMARY]; DyCuTe2 P2/m (10) mp-945779 [hull=0.016, PRIMARY]; DyCuTe2 P3m1 (156) mp-1225283 [hull=0.029]
- papers: https://doi.org/10.1021/acsami.0c09918 (Ternary Compounds Cu3RTe3 (R = Y, Sm, and Dy): A Family of New Thermoe...)

## Cu-Er-In
- rank 3062 | 1 samples | 1 papers | 1 compositions
- compositions: ErInCu4 (1)
- measured range: 32-290 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ErInCu P-62m (189) mp-3950 [hull=0.000, icsd=4, PRIMARY]; ErInCu2 Fm-3m (225) mp-4552 [hull=0.000, icsd=2, PRIMARY]; Er2InCu2 P4/mbm (127) mp-1078738 [hull=0.000, icsd=1, PRIMARY]; Er2In3Cu P3m1 (156) mp-1225615 [hull=0.033, PRIMARY]; ErInCu4 F-43m (216) mp-1206262 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(94)01472-8 (Transport properties of RInCu4 with C15b-type structure)

## Cu-Er-P-Zn
- rank 3063 | 1 samples | 1 papers | 1 compositions
- compositions: ErCuZnP2 (1)
- measured range: 304-788 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ErZnCuP2 P3m1 (156) mp-1225396 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1039/d0mh01112f (Experimental validation of high thermoelectric performance in RECuZnP2...)

## Cu-Er-Sb
- rank 3064 | 1 samples | 1 papers | 1 compositions
- compositions: Er3Cu3Sb4 (1)
- measured range: 13-394 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Er3Cu3Sb4 I-43d (220) mp-1105955 [hull=0.000, icsd=1, PRIMARY]; ErCuSb2 P4/nmm (129) mp-1079261 [hull=0.000, icsd=1, PRIMARY]; Er2CuSb3 P4/mmm (123) mp-1207353 [hull=3.219, PRIMARY]
- papers: https://doi.org/10.1063/1.367018 (Magnetic and thermoelectric properties of R3Cu3Sb4 (R=La, Ce, Gd, Er))

## Cu-Er-Se
- rank 3065 | 1 samples | 1 papers | 1 compositions
- compositions: ErCuSe2 (1)
- measured range: 299-765 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ErCuSe2 P3m1 (156) mp-675180 [hull=0.021, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2014.05.017 (Thermoelectric properties, crystal and electronic structure of semicon...)

## Cu-Eu-Sb
- rank 3066 | 1 samples | 1 papers | 1 compositions
- compositions: EuCuSb (1)
- measured range: 300-782 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): EuCuSb P6_3/mmc (194) mp-22292 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1021/acs.chemmater.0c02317 (Promising Zintl-Phase Thermoelectric Compound SrAgSb)

## Cu-Eu-Sb-Zn
- rank 3067 | 1 samples | 1 papers | 1 compositions
- compositions: EuZn0.25Cu0.5Sb (1)
- measured range: 301-971 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/j.jallcom.2019.152508 (Structure transition and thermoelectric properties related to AZn(1-x)...)

## Cu-Eu-Si
- rank 3068 | 1 samples | 1 papers | 1 compositions
- compositions: EuCu2Si2 (1)
- measured range: 13-270 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Eu(CuSi)2 I4/mmm (139) mp-3412 [hull=0.000, icsd=4, PRIMARY]; Eu2CuSi3 P-6m2 (187) mp-1225367 [hull=0.071, PRIMARY]; EuCuSi3 I-4m2 (119) mp-1225144 [hull=0.133, PRIMARY]
- papers: https://doi.org/10.1007/bf00116933 (Demagnetization due to interconfiguration fluctuations in the RE-Cu2Si...)

## Cu-Fe-In-Te
- rank 3069 | 1 samples | 1 papers | 1 compositions
- compositions: CuFeInTe3 (1)
- measured range: 299-451 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): InFe(CuTe2)2 I-4 (82) mp-1224565 [hull=0.097, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2015.08.128 (Thermoelectric transport properties of CuFeInTe 3)

## Cu-Fe-La-O
- rank 3070 | 1 samples | 1 papers | 1 compositions
- compositions: La0.80Sr0.20Fe0.60Cu0.40O3 (1)
- dopant candidates (<5% at.): Sr (1)
- measured range: 523-873 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaFe4(CuO4)3 Im-3 (204) mp-1105546 [hull=0.000, icsd=15, PRIMARY]
- papers: https://doi.org/10.1016/j.ceramint.2020.04.143 (Cobalt free LaxSr1-xFe1-yCuyO3-δ (x= 0.54, 0.8, y = 0.2, 0.4) perovski...)

## Cu-Fe-S-Ti
- rank 3071 | 1 samples | 1 papers | 1 compositions
- compositions: Ti2Cu3FeS4 (1)
- measured range: 72-381 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti3Fe(CuS4)2 R-3m (166) mp-1217187 [hull=0.043, PRIMARY]
- papers: https://doi.org/10.1039/c8qi00058a (Low temperature thermoelectric and magnetoresistive properties of Tl2C...)

## Cu-Fe-Sb
- rank 3072 | 1 samples | 1 papers | 1 compositions
- compositions: Cu0.75Fe0.25Sb3 (1)
- measured range: 82-792 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1063/1.3554403 (Thermoelectric properties of Co0.9Fe0.1Sb3-based skutterudite nanocomp...)

## Cu-Fe-Se-Ti
- rank 3073 | 1 samples | 1 papers | 1 compositions
- compositions: Ti2Cu3FeSe4 (1)
- measured range: 11-347 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1039/c8qi00058a (Low temperature thermoelectric and magnetoresistive properties of Tl2C...)

## Cu-Fe-Te-Ti
- rank 3074 | 1 samples | 1 papers | 1 compositions
- compositions: Ti2Cu3FeTe4 (1)
- measured range: 12-345 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1039/c8qi00058a (Low temperature thermoelectric and magnetoresistive properties of Tl2C...)

## Cu-Ga-La
- rank 3075 | 1 samples | 1 papers | 1 compositions
- compositions: LaCuGa (1)
- measured range: 23-292 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2Ga5Cu3 P-4m2 (115) mp-1223339 [hull=0.000, PRIMARY]; La2GaCu Immm (71) mp-1093608 [hull=2.233, PRIMARY]; LaGa3Cu I-4m2 (119) mp-1222853 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.42.2700 (Valence-fluctuation behavior of Yb ions and YbCuGa)

## Cu-Ga-La-O-Sr
- rank 3076 | 1 samples | 1 papers | 1 compositions
- compositions: La0.85Sr1.15GaCuO5 (1)
- measured range: 24-310 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrLaGaCuO5 Cm (8) mp-1218226 [hull=0.031, PRIMARY, AMBIGUOUS]; SrLaGaCuO5 Cc (9) mp-1173173 [hull=0.038]
- papers: https://doi.org/10.1103/physrevb.51.3104 (Thermoelectric power in single-layer copper oxides)

## Cu-Ga-U
- rank 3077 | 1 samples | 1 papers | 1 compositions
- compositions: UCu3.1Ga1.9 (1)
- measured range: 10-280 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UGaCu P6_3/mmc (194) mp-1077802 [hull=0.000, icsd=1, PRIMARY]; U(GaCu3)2 R3m (160) mp-1216918 [hull=0.109, PRIMARY]; U2Ga3Cu Pmm2 (25) mp-1216947 [hull=0.030, PRIMARY]; U2Ga5Cu3 P4mm (99) mp-1217218 [hull=0.094, PRIMARY]; U3(Ga2Cu)4 I-4m2 (119) mp-1216933 [hull=0.063, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(00)01176-2 (Large thermoelectric power in several metallic compounds of cerium and...)

## Cu-Ga-Yb
- rank 3078 | 1 samples | 1 papers | 1 compositions
- compositions: YbCuGa (1)
- measured range: 11-290 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(Ga2Cu)4 I4/mmm (139) mp-1103929 [hull=0.000, icsd=2, PRIMARY]; YbGa2Cu3 P6/mmm (191) mp-1207556 [hull=0.015, PRIMARY]; YbGa3Cu I-4m2 (119) mp-1215535 [hull=0.000, PRIMARY]; YbGaCu4 P-6m2 (187) mp-1215637 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.42.2700 (Valence-fluctuation behavior of Yb ions and YbCuGa)

## Cu-Gd-Sb-Y
- rank 3079 | 1 samples | 1 papers | 1 compositions
- compositions: Y1.5Gd1.5Cu3Sb4 (1)
- measured range: 11-551 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1109/ict.2006.331231 (Galvanomagnetic and Thermoelectric Properties of R3Cu3Sb4 Compounds)

## Cu-Gd-Se
- rank 3080 | 1 samples | 1 papers | 1 compositions
- compositions: GdCuSe2 (1)
- measured range: 299-764 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdCu5Se4 C2/m (12) mp-1224581 [hull=0.105, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2014.05.017 (Thermoelectric properties, crystal and electronic structure of semicon...)

## Cu-Ge-La
- rank 3081 | 1 samples | 1 papers | 1 compositions
- compositions: La2CuGe6 (1)
- measured range: 11-282 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(CuGe)2 I4/mmm (139) mp-20322 [hull=0.000, icsd=2, PRIMARY]; LaCuGe2 Cmcm (63) mp-1080588 [hull=0.000, icsd=1, PRIMARY]; La2CuGe6 Amm2 (38) mp-1095038 [hull=0.043, icsd=1, PRIMARY]; La2CuGe Immm (71) mp-1096524 [hull=2.215, PRIMARY]; La15CuGe9 P6_3mc (186) mp-1213468 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2007.04.286 (Electric transport in R2MGe6 ternary compounds (R=La, Ce, Gd, Tb, Dy, ...)

## Cu-Ge-O
- rank 3082 | 1 samples | 1 papers | 1 compositions
- compositions: CuGeO3 (1)
- measured range: 10-40 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuGeO3 Pmma (51) mp-1087506 [hull=0.043, icsd=26, PRIMARY]; Cu2GeO4 I4_1/amd (141) mp-9600 [hull=0.082, icsd=1, PRIMARY]; CuGeO3 Pbam (55) mp-1202570 [hull=0.029, icsd=1]; CuGeO3 Pmna (53) mp-1181636 [hull=0.051, icsd=1]
- papers: https://doi.org/10.1103/physrevb.58.r2913 (Thermal conductivity of the spin-Peierls compoundCuGeO3)

## Cu-Ge-P-S
- rank 3083 | 1 samples | 1 papers | 1 compositions
- compositions: Cu3P0.6Ge0.4S4 (1)
- measured range: 302-678 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1002/adfm.202000973 (Enargite Cu\n            3\n            PS\n            4\n           ...)

## Cu-Ge-Sb-Se
- rank 3084 | 1 samples | 1 papers | 1 compositions
- compositions: Ge25Se65Sb5.0Cu5.0 (1)
- measured range: 300-450 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.rinp.2019.102492 (Semiconducting chalcogenide Ge-Se-Sb-Cu as new prospective thermoelect...)

## Cu-Ge-Se-Sn
- rank 3085 | 1 samples | 1 papers | 1 compositions
- compositions: Cu2Sn0.5Ge0.5Se3 (1)
- measured range: 80-301 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/j.jallcom.2010.06.182 (Thermoelectric properties of the Cu2SnSe3–Cu2GeSe3 solid solution)

## Cu-Ge-Se-Sr
- rank 3086 | 1 samples | 1 papers | 1 compositions
- compositions: SrCu2GeSe4 (1)
- measured range: 321-674 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrCu2GeSe4 Ama2 (40) mp-16179 [hull=0.004, icsd=1, PRIMARY]
- papers: https://doi.org/10.1039/c8ta09660k (Origins of ultralow thermal conductivity in 1-2-1-4 quaternary selenides)

## Cu-Hg-Se-Sn
- rank 3087 | 1 samples | 1 papers | 1 compositions
- compositions: Cu2HgSnSe4 (1)
- measured range: 295-575 K (5th-95th pct of 5 curves)
- [ref 1] TEDesignLab / ICSD: Cu2SnHgSe4 I-42m (121) mp-16566 [hull=0.000, icsd=3, PRIMARY]
- papers: https://doi.org/10.1007/s11664-014-3075-8 (Thermoelectric Properties of Cu2HgSnSe4-Cu2HgSnTe4 Solid Solution)

## Cu-Hg-Sn-Te
- rank 3088 | 1 samples | 1 papers | 1 compositions
- compositions: Cu2HgSnTe4 (1)
- measured range: 295-575 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu2SnHgTe4 I-42m (121) mp-1079012 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1007/s11664-014-3075-8 (Thermoelectric Properties of Cu2HgSnSe4-Cu2HgSnTe4 Solid Solution)

## Cu-Ho-In
- rank 3089 | 1 samples | 1 papers | 1 compositions
- compositions: HoInCu4 (1)
- measured range: 23-294 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HoInCu P-62m (189) mp-3015 [hull=0.000, icsd=4, PRIMARY]; HoInCu2 Fm-3m (225) mp-30586 [hull=0.000, icsd=1, PRIMARY]; HoIn7Cu5 Imm2 (44) mp-1224226 [hull=0.060, PRIMARY]; Ho2In3Cu P3m1 (156) mp-1223982 [hull=0.034, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(94)01472-8 (Transport properties of RInCu4 with C15b-type structure)

## Cu-In-Mg-Te
- rank 3090 | 1 samples | 1 papers | 1 compositions
- compositions: Mg2Cu3In3Te8 (1)
- measured range: 313-875 K (5th-95th pct of 6 curves; full span incl. outliers 313-967 K)
- papers: https://doi.org/10.1021/acsaem.9b02004 (A2Cu3In3Te8 (A = Cd, Zn, Mn, Mg): A Type of Thermoelectric Material wi...)

## Cu-In-Mn-Se
- rank 3091 | 1 samples | 1 papers | 1 compositions
- compositions: Cu0.9In0.9Mn0.2Se2 (1)
- measured range: 302-560 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1103/physrevb.84.075203 (Thermoelectric properties of p-type CuInSe2chalcopyrites enhanced by i...)

## Cu-In-Mn-Te
- rank 3092 | 1 samples | 1 papers | 1 compositions
- compositions: Mn2Cu3In3Te8 (1)
- measured range: 313-875 K (5th-95th pct of 6 curves; full span incl. outliers 313-971 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn2InCuTe4 I4/mmm (139) mp-1221863 [hull=0.128, PRIMARY]; MnInCuTe3 Cm (8) mp-1221781 [hull=0.010, PRIMARY]
- papers: https://doi.org/10.1021/acsaem.9b02004 (A2Cu3In3Te8 (A = Cd, Zn, Mn, Mg): A Type of Thermoelectric Material wi...)

## Cu-In-O-V
- rank 3093 | 1 samples | 1 papers | 1 compositions
- compositions: Cu2In3VO9 (1)
- measured range: 308-580 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): VInCuO5 P2_1/c (14) mp-640894 [hull=0.033, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.ceramint.2016.11.040 (Semiconducting properties of Cu2In3VO9 ceramic material)

## Cu-In-Sb
- rank 3094 | 1 samples | 1 papers | 1 compositions
- compositions: (InSb)5Cu1 (1)
- measured range: 316-691 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/j.cap.2011.04.044 (Cu addition and its role in thermoelectric properties and nanostructur...)

## Cu-In-Se-Te
- rank 3095 | 1 samples | 1 papers | 1 compositions
- compositions: CuIn3Se4.5Te0.5 (1)
- measured range: 326-925 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): InCuTeSe I2_12_12_1 (24) mp-1224187 [hull=0.018, PRIMARY]
- papers: https://doi.org/10.1038/srep40224 (Enhanced thermoelectric performance of a chalcopyrite compound CuIn3Se...)

## Cu-In-Tb
- rank 3096 | 1 samples | 1 papers | 1 compositions
- compositions: TbInCu4 (1)
- measured range: 24-295 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TbInCu2 Fm-3m (225) mp-22685 [hull=0.022, icsd=5, PRIMARY]; TbInCu P-62m (189) mp-19782 [hull=0.000, icsd=4, PRIMARY]; TbInCu4 F-43m (216) mp-22229 [hull=0.000, icsd=3, PRIMARY]; Tb2InCu2 P4/mbm (127) mp-1079779 [hull=0.000, icsd=1, PRIMARY]; Tb(InCu)6 Immm (71) mp-1217863 [hull=0.012, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(94)01472-8 (Transport properties of RInCu4 with C15b-type structure)

## Cu-In-Tm
- rank 3097 | 1 samples | 1 papers | 1 compositions
- compositions: TmInCu4 (1)
- measured range: 29-288 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Tm2InCu2 P4/mbm (127) mp-1078916 [hull=0.000, icsd=1, PRIMARY]; TmInCu2 Fm-3m (225) mp-622636 [hull=0.008, icsd=1, PRIMARY]; TmIn7Cu5 Imm2 (44) mp-1216978 [hull=0.082, PRIMARY]; TmInCu4 F-43m (216) mp-1024957 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(94)01472-8 (Transport properties of RInCu4 with C15b-type structure)

## Cu-K-S
- rank 3098 | 1 samples | 1 papers | 1 compositions
- compositions: KCu6.8S4 (1)
- measured range: 321-574 K (5th-95th pct of 4 curves)
- [ref 1] TEDesignLab / ICSD: KCu3S2 C2/m (12) mp-9868 [hull=0.001, icsd=1, PRIMARY]; KCuS (33)
- [ref 2] MP, ranked by ICSD evidence: KCu4S3 P4/mmm (123) mp-27677 [hull=0.000, icsd=4, PRIMARY]; KCuS Pnma (62) mp-28270 [hull=0.000, icsd=1, PRIMARY]; K3(Cu4S3)2 C2/m (12) mp-17174 [hull=0.000, icsd=1, PRIMARY]; K3(CuS)4 Pbam (55) mp-1120730 [hull=0.000, PRIMARY]; KCu7S4 P1 (1) mp-1223529 [hull=0.019, PRIMARY]
- papers: https://doi.org/10.1039/c3ta12706k (Introducing kalium into copper sulfide for the enhancement of thermoel...)

## Cu-La-Mn-O-Sr
- rank 3099 | 1 samples | 1 papers | 1 compositions
- compositions: La0.75Sr0.25Cu0.5Mn0.5O3 (1)
- measured range: 472-1123 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2La2MnCuO8 C2/m (12) mp-1173270 [hull=0.009, PRIMARY]; Sr2La6Mn7CuO24 P1 (1) mp-738741 [hull=0.007, PRIMARY]; Sr3La9Mn10(CuO18)2 C2 (5) mp-698797 [hull=0.010, PRIMARY]; Sr4La4Mn7CuO24 P-1 (2) mp-698710 [hull=0.008, PRIMARY]; Sr5La5Mn9CuO30 P1 (1) mp-698602 [hull=0.006, PRIMARY]
- papers: https://doi.org/10.1016/j.electacta.2015.10.166 (Investigations on structures, thermal expansion and electrochemical pr...)

## Cu-La-O-Rh
- rank 3100 | 1 samples | 1 papers | 1 compositions
- compositions: La2CuRhO6 (1)
- measured range: 316-570 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2CuRhO6 P2_1/c (14) mp-1223365 [hull=0.009, PRIMARY]
- papers: https://doi.org/10.1016/j.materresbull.2009.11.008 (Electrical and magnetic properties of new rhodium perovskites: La2MRhO...)
