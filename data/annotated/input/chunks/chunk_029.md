# Host systems -- chunk 029 of 73

Ranks 1401-1450 by sample count. These 50 host systems cover 200 samples (0.38% of the TE set); cumulative through this chunk: 93.19%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Cu-Fe-Ge-Se
- rank 1401 | 4 samples | 1 papers | 4 compositions
- compositions: Cu2Zn0.3Fe0.7GeSe4 (1); Cu2Zn0.2Fe0.8GeSe4 (1); Cu2Zn0.1Fe0.9GeSe4 (1); CuFeGeSe4 (1)
- dopant candidates (<5% at.): Zn (3)
- measured range: 298-678 K (5th-95th pct of 12 curves)
- [ref 1] TEDesignLab / ICSD: FeCu2GeSe4 I-42m (121) mp-1087471 [hull=0.038, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/ja308627v (Phonon Scattering through a Local Anisotropic Structural Disorder in t...)

## Cu-Fe-S-Se
- rank 1402 | 4 samples | 1 papers | 4 compositions
- compositions: CuFeS1.7Se0.3 (1); CuFeS1.5Se0.5 (1); CuFeS1.8Se0.2 (1); CuFeS1.6Se0.4 (1)
- solid-solution axis: S/(S+Se) spans 0.75-0.90 (median 0.85) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 77-678 K (5th-95th pct of 20 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeCuSeS I2_12_12_1 (24) mp-1224989 [hull=0.139, PRIMARY]
- papers: https://doi.org/10.1007/s11664-015-4029-5 (The Thermoelectric Properties and Solubility Limit of CuFeS2(1−x)Se2x)

## Cu-Gd-O
- rank 1403 | 4 samples | 3 papers | 3 compositions
- compositions: Gd2CuO4 (2); Gd1.55Pr0.3Ce0.15CuO4 (1); Gd1.75Pr0.1Ce0.15CuO4 (1)
- dopant candidates (<5% at.): Pr (2), Ce (2)
- sample form: Bulk (1)
- measured range: 81-955 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd2CuO4 I4/mmm (139) mp-4860 [hull=0.024, icsd=4, PRIMARY]; Gd(CuO2)2 I4_1/a (88) mp-20707 [hull=0.000, icsd=1, PRIMARY]; GdCuO3 Pm-3m (221) mp-1184481 [hull=0.158, PRIMARY]; Gd2CuO4 P2_1/c (14) mp-676060 [hull=0.026]
- papers: https://doi.org/10.1016/s0925-8388(02)00917-9 (Thermoelectric properties of layered rare earth copper oxides) | https://doi.org/10.1016/0921-4526(94)91263-7 (Thermoelectric power in Gd1.85−xPrxCe0.15CuO4 system) | https://doi.org/10.1016/s0925-8388(02)00875-7 (Thermophysical properties of layered rare earth copper oxides)

## Cu-Gd-O-Pr
- rank 1404 | 4 samples | 1 papers | 4 compositions
- compositions: Gd1.3Pr0.55Ce0.15CuO4 (1); Gd1.1Pr0.75Ce0.15CuO4 (1); Gd0.9Pr0.95Ce0.15CuO4 (1); Gd0.5Pr1.35Ce0.15CuO4 (1)
- dopant candidates (<5% at.): Ce (4)
- solid-solution axis: Gd/(Gd+Pr) spans 0.27-0.70 (median 0.59) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 82-302 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/0921-4526(94)91263-7 (Thermoelectric power in Gd1.85−xPrxCe0.15CuO4 system)

## Cu-Ge-Te
- rank 1405 | 4 samples | 3 papers | 4 compositions
- compositions: Cu15Ge7.5Te77.5 (1); Cu20Ge5Te75 (1); Cu0.10Bi0.05Ge0.85Te (1); ((GeTe)0.96(Bi2Te3)0.04)71.83(Cu)28.17 (1)
- dopant candidates (<5% at.): Bi (2)
- sample form: Bulk (1)
- measured range: 127-770 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu2GeTe3 Imm2 (44) mp-12806 [hull=0.000, icsd=1, PRIMARY]; Cu2GeTe3 Fdd2 (43) mp-1225891 [hull=0.001]; Cu2GeTe3 Cc (9) mp-674953 [hull=0.003]; Cu2GeTe3 P1 (1) mp-1225914 [hull=0.016]
- papers: https://doi.org/10.1039/b908579c (Conducting glasses as new potential thermoelectric materials: the Cu–G...) | https://doi.org/10.1063/1.4983404 (Carrier density control and enhanced thermoelectric performance of Bi ...) | https://doi.org/10.1557/mrc.2018.150 (Thermoelectric and mechanical properties of Ag and Cu doped (GeTe)0.96...)

## Cu-In-S
- rank 1406 | 4 samples | 1 papers | 4 compositions
- compositions: CuIn0.90Fe0.10S2 (1); CuIn0.875Fe0.125S2 (1); CuInS2 (1); CuIn0.85Fe0.15S2 (1)
- dopant candidates (<5% at.): Fe (3)
- sample form: Bulk (4)
- measured range: 301-574 K (5th-95th pct of 16 curves)
- [ref 1] TEDesignLab / ICSD: InCuS2 I-42d (122) mp-22736 [hull=0.000, icsd=13, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: In2CuS4 Fd-3m (227) mp-1212041 [hull=0.059, PRIMARY]; In5CuS8 F-43m (216) mp-674514 [hull=0.015, PRIMARY]; InCuS2 P3m1 (156) mp-1223996 [hull=0.075]; InCuS2 R3m (160) mp-1097021 [hull=0.082]
- papers: https://doi.org/10.1016/j.matchemphys.2014.03.034 (Structure–property relationships along the Fe-substituted CuInS2 serie...)

## Cu-In-Sn-Te
- rank 1407 | 4 samples | 1 papers | 4 compositions
- compositions: CuSn2InTe5 (1); CuSn7InTe9 (1); CuSn5InTe7 (1); CuSnInTe3 (1)
- measured range: 296-876 K (5th-95th pct of 19 curves)
- papers: https://doi.org/10.1016/j.actamat.2016.11.049 (Strategy to optimize the overall thermoelectric properties of SnTe via...)

## Cu-In-Y
- rank 1408 | 4 samples | 2 papers | 4 compositions
- compositions: Ce0.1Y0.9InCu2 (1); YInCu2 (1); Ce0.05Y0.95InCu2 (1); YInCu4 (1)
- dopant candidates (<5% at.): Ce (2)
- sample form: Bulk (1)
- measured range: 10-290 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y2InCu2 P4/mbm (127) mp-1079508 [hull=0.000, icsd=1, PRIMARY]; YInCu4 F-43m (216) mp-1071645 [hull=0.000, icsd=1, PRIMARY]; YInCu2 Fm-3m (225) mp-19946 [hull=0.031, icsd=1, PRIMARY]; YInCu P-62m (189) mp-1080624 [hull=0.000, icsd=1, PRIMARY]; Y2InCu Immm (71) mp-1096300 [hull=2.566, PRIMARY]
- papers: https://doi.org/10.1007/bf00683635 (Thermpower of Ce x Y1?x InCu2 and CeInCu y Ag2?y) | https://doi.org/10.1016/0304-8853(94)01472-8 (Transport properties of RInCu4 with C15b-type structure)

## Cu-Ir-Rh-S
- rank 1409 | 4 samples | 1 papers | 1 compositions
- compositions: CuIrRhS4 (4)
- sample form: Bulk (4)
- measured range: 13-300 K (5th-95th pct of 9 curves)
- papers: https://doi.org/10.1016/j.jmmm.2015.12.097 (Temperature dependence of thermodynamic and electrical properties of C...)

## Cu-La-Mg-O
- rank 1410 | 4 samples | 1 papers | 2 compositions
- compositions: La1.85Sr0.15Cu0.6Mg0.4O4 (2); La1.85Sr0.15Cu0.5Mg0.5O4 (2)
- dopant candidates (<5% at.): Sr (4)
- measured range: 20-297 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/s0375-9601(02)01270-7 (Transport mechanism in La1.85Sr0.15Cu1−xMgxO4 system)

## Cu-La-O-Se
- rank 1411 | 4 samples | 1 papers | 4 compositions
- compositions: LaCuOSe (1); La0.9Sr0.1CuOSe (1); La0.95Sr0.05CuOSe (1); La0.85Sr0.15CuOSe (1)
- dopant candidates (<5% at.): Sr (3)
- curator composition details (from the paper): thin film (2); polycrystalline (2)
- sample form: Bulk (4)
- measured range: 367-669 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2Cu(SeO3)4 P2_1/c (14) mp-18267 [hull=0.000, icsd=1, PRIMARY]; La2CuSe2O P4/mmm (123) mp-1211335 [hull=1.516, PRIMARY]; La4Cu3SeO12 Im-3m (229) mp-1147534 [hull=0.110, PRIMARY]; LaCu2SeO2 P4/mmm (123) mp-1207265 [hull=1.085, PRIMARY]
- papers: https://doi.org/10.1063/1.1646438 (Thermoelectric properties of layered oxyselenides La1−xSrxCuOSe (x=0 t...)

## Cu-Mn
- rank 1412 | 4 samples | 2 papers | 4 compositions
- compositions: Cu93.12Mn6.88 (1); Cu90.86Mn9.14 (1); Cu90.54Mn9.46 (1); Cu94.51Mn5.49 (1)
- measured range: 11-871 K (5th-95th pct of 7 curves; full span incl. outliers 11-968 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn4Cu R-3m (166) mp-1221725 [hull=0.133, PRIMARY]; MnCu3 P6_3/mmc (194) mp-974747 [hull=0.098, PRIMARY]
- papers: https://doi.org/10.1063/1.1722342 (Thermoelectric Power and Electrical Resistivity of Dilute Alloys of Mn...) | https://doi.org/10.1063/1.1729605 (Effects of Transition Metal Solutes on the Thermoelectric Power of Cop...)

## Cu-O-Sr-Tl
- rank 1413 | 4 samples | 1 papers | 4 compositions
- compositions: TlSr2(Er0.6Sr0.4)Cu2O7 (1); TlSr2(Er0.5Sr0.5)Cu2O7 (1); TlSr2(Er0.4Sr0.6)Cu2O7 (1); TlSr2(Er0.3Sr0.7)Cu2O7 (1)
- dopant candidates (<5% at.): Er (4)
- sample form: Bulk (4)
- measured range: 47-287 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2TlCuO5 P4/mmm (123) mp-620290 [hull=0.014, icsd=1, PRIMARY]; Sr4CaLaTl2(Cu2O7)2 I4/mmm (139) mp-1218536 [hull=0.010, PRIMARY]; Sr6Tl3Cu3O16 C2/m (12) mp-1218860 [hull=0.379, PRIMARY]
- papers: https://doi.org/10.1143/jjap.30.l1549 (Thermopower and Resistivity of 1212-Type Phase TlSr2(Er1-ySry)Cu2O7-δ)

## Cu-P-S
- rank 1414 | 4 samples | 1 papers | 4 compositions
- compositions: Cu3P0.9Ge0.1S4 (1); Cu3P0.8Ge0.2S4 (1); Cu3P0.7Ge0.3S4 (1); Cu3PS4 (1)
- dopant candidates (<5% at.): Ge (3)
- sample form: Bulk (4)
- measured range: 301-681 K (5th-95th pct of 16 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu3PS4 Pmn2_1 (31) mp-3934 [hull=0.000, icsd=4, PRIMARY]; Cu7PS6 P2_13 (198) mp-1196216 [hull=0.042, icsd=1, PRIMARY]; CuPS3 P4_2/mnm (136) mp-1105187 [hull=0.000, icsd=1, PRIMARY]; CuPS2 P3m1 (156) mp-1225675 [hull=0.239, PRIMARY]
- papers: https://doi.org/10.1002/adfm.202000973 (Enargite Cu\n            3\n            PS\n            4\n           ...)

## Cu-Se-Sn-W
- rank 1415 | 4 samples | 1 papers | 4 compositions
- compositions: Cu6WSnSe8 (1); Cu5.97WSnSe8 (1); Cu5.94WSnSe8 (1); Cu5.91WSnSe8 (1)
- sample form: Bulk (4)
- measured range: 322-774 K (5th-95th pct of 21 curves)
- papers: https://doi.org/10.1016/j.jssc.2021.122626 (The charge localization deteriorating the thermoelectric properties: T...)

## Cu-Si
- rank 1416 | 4 samples | 2 papers | 4 compositions
- compositions: Cu91.59Si8.41 (1); Cu94.77Si5.23 (1); Cu93.54Si6.46 (1); LaCu20.5Si2 (1)
- dopant candidates (<5% at.): La (1)
- sample form: Bulk (4)
- measured range: 17-1105 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu15Si4 I-43d (220) mp-14266 [hull=0.000, icsd=2, PRIMARY]; Cu3Si P6_3/mmc (194) mp-867317 [hull=0.012, PRIMARY]; Cu7Si2 P-3m1 (164) mp-1206157 [hull=0.060, PRIMARY]; Cu7Si6 P-1 (2) mp-1213668 [hull=2.792, PRIMARY]; Cu3Si I4/mmm (139) mp-972828 [hull=0.032]
- papers: https://doi.org/10.1063/1.1722001 (Thermoelectric Power and Electrical Resistivity of Dilute Alloys of Si...) | https://doi.org/10.1103/physrevb.64.195106 (Transport properties of the<mml:math xmlns:mml=\"http://www.w3.org/199...)

## Cu-Te-Tl
- rank 1417 | 4 samples | 3 papers | 3 compositions
- compositions: CuTl9Te5 (2); TlCu3Te2 (1); TlCu2Te2 (1)
- sample form: Bulk (4)
- measured range: 291-594 K (5th-95th pct of 18 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Tl4CuTe3 I4/mcm (140) mp-34765 [hull=0.193, icsd=1, PRIMARY]; Tl2CuTe2 I4/mmm (139) mp-1207270 [hull=0.587, PRIMARY]; TlCu3Te2 Pc (7) mp-1217029 [hull=0.051, PRIMARY]
- papers: https://doi.org/10.2320/matertrans.47.1432 (Thermoelectric and Thermophysical Characteristics of Cu<SUB>2</SUB>Te-...) | https://doi.org/10.1109/ict.2005.1519916 (Thermoelectric properties of ternary copper thallium telluride: CuTl/s...) | https://doi.org/10.1007/s11664-009-0664-z (Thermoelectric Properties of TlCu3Te2 and TlCu2Te2)

## Er-Fe-Mn-O-Zn
- rank 1418 | 4 samples | 1 papers | 4 compositions
- compositions: Mn0.58Zn0.37Er0.4Fe1.65O4 (1); Mn0.58Zn0.37Er0.6Fe1.45O4 (1); Mn0.58Zn0.37Er0.8Fe1.25O4 (1); Mn0.58Zn0.37Er1.0Fe1.05O4 (1)
- measured range: 318-540 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/s0167-577x(00)00342-6 (Thermoelectric power studies of erbium substituted Mn–Zn ferrites)

## Eu-Ni-O
- rank 1419 | 4 samples | 1 papers | 1 compositions
- compositions: EuNiO3 (4)
- measured range: 217-483 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): EuNiO3 Pnma (62) mp-32341 [hull=0.000, icsd=4, PRIMARY]; Eu2Ni2O5 Ima2 (46) mp-1076223 [hull=0.020, PRIMARY]; Eu2NiO4 I4/mmm (139) mp-770352 [hull=0.023, PRIMARY]; EuNiO3 Pm-3m (221) mp-1076460 [hull=0.037]; Eu2Ni2O5 Cm (8) mp-1097890 [hull=0.104]
- papers: https://doi.org/10.1021/acsami.9b12609 (A d-Band Electron Correlated Thermoelectric Thermistor Established in ...)

## Eu-Sb-Yb-Zn
- rank 1420 | 4 samples | 2 papers | 3 compositions
- compositions: Eu0.5Yb0.5Zn2Sb2 (2); Eu0.75Yb0.25Zn2Sb2 (1); Eu0.25Yb0.75Zn2Sb2 (1)
- sample form: Bulk (1)
- measured range: 303-774 K (5th-95th pct of 20 curves)
- papers: https://doi.org/10.1016/j.nanoen.2016.04.023 (Enhancement of thermoelectric performance of phase pure Zintl compound...) | https://doi.org/10.1016/j.jallcom.2017.01.350 (Thermoelectric properties of EuZn2Sb2 Zintl compounds: zT enhancement ...)

## Fe-Gd-Mn-O-Zn
- rank 1421 | 4 samples | 1 papers | 4 compositions
- compositions: Mn0.58Zn0.37Gd0.4Fe1.65O4 (1); Mn0.58Zn0.37Gd1.0Fe1.05O4 (1); Mn0.58Zn0.37Gd0.6Fe1.45O4 (1); Mn0.58Zn0.37Gd0.8Fe1.25O4 (1)
- measured range: 309-451 K (5th-95th pct of 4 curves; full span incl. outliers 309-494 K)
- papers: https://doi.org/10.1016/s0167-577x(01)00523-7 (Thermoelectric power studies of gadolinium substituted Mn–Zn–Gd ferrites)

## Fe-Hf-Sb-V
- rank 1422 | 4 samples | 3 papers | 3 compositions
- compositions: FeV0.8Hf0.2Sb (2); FeV0.7Hf0.3Sb (1); Fe(V0.8Hf0.2)Sb (1)
- sample form: Bulk (2)
- measured range: 99-900 K (5th-95th pct of 20 curves)
- papers: https://doi.org/10.1016/j.jallcom.2019.153413 (Transport and thermoelectric properties of Hf-doped FeVSb half-Heusler...) | https://doi.org/10.1016/j.jpowsour.2020.228768 (Optimizing the thermoelectric performance of FeVSb half-Heusler compou...) | https://doi.org/10.1016/j.jpcs.2020.109848 (Effects of spark plasma sintering on enhancing the thermoelectric perf...)

## Fe-In-Mg-O-Yb
- rank 1423 | 4 samples | 1 papers | 4 compositions
- compositions: In0.4Yb0.6FeZn0.1Mg0.9O4 (1); In0.4Yb0.6FeZn0.3Mg0.7O4 (1); In0.4Yb0.6FeMgO4 (1); In0.4Yb0.6FeZn0.2Mg0.8O4 (1)
- dopant candidates (<5% at.): Zn (3)
- sample form: Bulk (4)
- measured range: 297-1273 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/j.jallcom.2016.05.064 (Thermal and mechanical properties of Yb&Mg co-doped InFeZnO4)

## Fe-In-O
- rank 1424 | 4 samples | 1 papers | 1 compositions
- compositions: (In0.8Mo0.05Fe0.15)2O3 (4)
- dopant candidates (<5% at.): Mo (4)
- measured range: 266-350 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): InFeO3 P6_3/mmc (194) mp-24934 [hull=0.033, icsd=2, PRIMARY]; In(FeO2)2 R-3m (166) mp-24931 [hull=0.069, icsd=1, PRIMARY]; InFe11O16 Cmcm (63) mp-765206 [hull=0.078, PRIMARY]; InFe17O24 Imm2 (44) mp-1178184 [hull=0.142, PRIMARY]; InFe29O40 I-4 (82) mp-771512 [hull=0.039, PRIMARY]
- papers: https://doi.org/10.1063/1.3039807 (Effect of oxygen vacancy on ferromagnetism and electric transport of b...)

## Fe-In-O-Yb-Zn
- rank 1425 | 4 samples | 1 papers | 4 compositions
- compositions: In0.4Yb0.6FeZn0.7Mg0.3O4 (1); In0.4Yb0.6FeZnO4 (1); In0.4Yb0.6FeZn0.9Mg0.1O4 (1); In0.4Yb0.6FeZn0.8Mg0.2O4 (1)
- dopant candidates (<5% at.): Mg (3)
- sample form: Bulk (4)
- measured range: 297-1273 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/j.jallcom.2016.05.064 (Thermal and mechanical properties of Yb&Mg co-doped InFeZnO4)

## Fe-La-Mn-O
- rank 1426 | 4 samples | 4 papers | 4 compositions
- compositions: La(Fe0.40Mn0.60)O3 (1); La2FeMnO6 (1); LaFe0.25Mn0.75O3 (1); (La0.8Sr0.2)0.95Fe0.6Mn0.3Co0.1O3 (1)
- dopant candidates (<5% at.): Sr (1), Co (1)
- curator composition details (from the paper): polycrystalline (1)
- measured range: 152-1167 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La7SmMn2(Fe3O10)2 P1 (1) mp-1076418 [hull=0.071, PRIMARY]; La7SmMn2(FeO4)6 Cmm2 (35) mp-1076598 [hull=0.138, PRIMARY]; La7SmMn3(FeO4)5 P1 (1) mp-1076455 [hull=0.072, PRIMARY]; La7SmMn3Fe5O24 Cm (8) mp-1075984 [hull=0.119, PRIMARY]; La7SmMn4(FeO5)4 P1 (1) mp-1076172 [hull=0.074, PRIMARY]
- papers: https://doi.org/10.1149/1.2358840 (Electrical, Thermoelectric, and Structural Properties of La(M[sub x]Fe...) | https://doi.org/10.1016/j.jallcom.2017.03.331 (Magnetic properties, resistivity and magnetoresistance effects of doub...) | https://doi.org/10.1016/j.electacta.2015.04.085 (Assessment of LaM0.25Mn0.75O3- (M = Fe, Co, Ni, Cu) as promising catho...)

## Fe-Mn-O-Pr
- rank 1427 | 4 samples | 1 papers | 4 compositions
- compositions: Pr0.9Sr0.1Mn0.7Fe0.3O3 (1); Pr0.9Sr0.1Mn0.5Fe0.5O3 (1); Pr0.9Sr0.1Mn0.4Fe0.6O3 (1); Pr0.9Sr0.1Mn0.3Fe0.7O3 (1)
- dopant candidates (<5% at.): Sr (4)
- sample form: pellets (4)
- measured range: 143-841 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1007/s11664-017-5366-3 (High-Temperature Thermoelectric Properties of Perovskite-Type Pr0.9Sr0...)

## Fe-Nb-O-Sr
- rank 1428 | 4 samples | 1 papers | 3 compositions
- compositions: Sr2FeMo0.4Nb0.6O6 (2); Sr2FeNbO6 (1); Sr2FeMo0.2Nb0.8O6 (1)
- dopant candidates (<5% at.): Mo (3)
- sample form: Bulk (4)
- measured range: 368-1069 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2NbFeO6 Fm-3m (225) mp-1218741 [hull=0.000, PRIMARY]; SrNbFeO6 I-4 (82) mp-39995 [hull=0.176, PRIMARY]; Sr2NbFeO6 P4/mmm (123) mp-1218744 [hull=0.025]
- papers: https://doi.org/10.2497/jjspm.55.827 (Thermoelectric Property of Nb-doped Sr2FeMoO6 Double Perovskite Oxide)

## Fe-Pd-Sb
- rank 1429 | 4 samples | 1 papers | 1 compositions
- compositions: Fe2Pd2Sb12 (4)
- sample form: Bulk (4)
- measured range: 71-772 K (5th-95th pct of 5 curves; full span incl. outliers 71-827 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeSb6Pd C2/m (12) mp-1224896 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2009.12.085 (Synthesis, crystal structure and thermoelectric properties of the tern...)

## Fe-Ru-Sb
- rank 1430 | 4 samples | 2 papers | 4 compositions
- compositions: Ru0.5Fe0.5Sb2 (1); Ru0.75Fe0.25Sb2 (1); Ce(Fe3.6Ru0.4)4Sb12 (1); Ce(Fe3.5Ru0.5)4Sb12 (1)
- dopant candidates (<5% at.): Ce (2)
- sample form: Other (2)
- solid-solution axis: Fe/(Fe+Ru) spans 0.25-0.90 (median 0.87) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 12-853 K (5th-95th pct of 16 curves)
- papers: https://doi.org/10.1063/1.4833055 (Correlated evolution of colossal thermoelectric effect and Kondo insul...) | https://doi.org/10.7566/jpsj.82.124608 (Influence of Ru Substitution on the Thermoelectric Properties of Ce(Fe...)

## Fe-S-Te
- rank 1431 | 4 samples | 2 papers | 4 compositions
- compositions: Fe1.06Te0.86S0.14 (1); FeTe0.9S0.1 (1); FeTe0.8S0.2 (1); FeTe0.7S0.3 (1)
- solid-solution axis: S/(S+Te) spans 0.10-0.30 (median 0.20) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-300 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe4Te3S P4mm (99) mp-1225166 [hull=0.075, PRIMARY]; Fe4Te3S Amm2 (38) mp-1225021 [hull=0.109]
- papers: https://doi.org/10.1103/physrevb.95.184504 (Normal state above the upper critical field in \nFe1+yTe1−x(Se,S)x) | https://doi.org/10.1016/j.phpro.2014.09.028 (Thermal Conductivity and Electrical Resistivity of FeTe1-xSx Sintered ...)

## Fe-Sb-Sn-Ti
- rank 1432 | 4 samples | 3 papers | 4 compositions
- compositions: TiFe2Sn0.8Sb0.2 (1); Fe2TiSn0.8Sb0.2 (1); Fe2TiSn0.5Sb0.5 (1); Fe2TiSn0.75Sb0.25 (1)
- measured range: 12-378 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1007/s11665-018-3744-5 (Synthesis and Structural Characterization of Sb-Doped TiFe2Sn Heusler ...) | https://doi.org/10.1103/physrevmaterials.2.075403 (Thermoelectric properties of chemically substituted full-Heusler<mml:m...) | https://doi.org/10.1063/1.5110229 (Origin of the magnetic ground state developed upon Si, Ge, and Sb-subs...)

## Fe-Sb-Ta-Ti
- rank 1433 | 4 samples | 1 papers | 4 compositions
- compositions: Ta0.84Ti0.16FeSb (1); Ta0.74V0.1Ti0.16FeSb (1); Ta0.69V0.15Ti0.16FeSb (1); Ta0.79V0.05Ti0.16FeSb (1)
- dopant candidates (<5% at.): V (3)
- sample form: Bulk (4)
- measured range: 301-975 K (5th-95th pct of 21 curves)
- papers: https://doi.org/10.1038/s41467-018-08223-5 (Discovery of TaFeSb-based half-Heuslers with high thermoelectric perfo...)

## Fe-Si-Sn-Ti
- rank 1434 | 4 samples | 1 papers | 4 compositions
- compositions: Fe2TiSn0.4Si0.6 (1); Fe2TiSn0.2Si0.8 (1); Fe2TiSn0.8Si0.2 (1); Fe2TiSn0.6Si0.4 (1)
- solid-solution axis: Si/(Si+Sn) spans 0.20-0.80 (median 0.60) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 17-355 K (5th-95th pct of 12 curves)
- papers: https://doi.org/10.1134/s1063782617070363 (Preparation and study of the thermoelectric properties of Fe2TiSn1–x\n...)

## Fe-Te
- rank 1435 | 4 samples | 3 papers | 4 compositions
- compositions: FeTe2 (1); Fe0.9Co0.1Te2 (1); Fe1.04Te (1); FeTe (1)
- dopant candidates (<5% at.): Co (1)
- sample form: Bulk (2); SingleCrystal (1)
- measured range: 12-752 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeTe2 Pnnm (58) mp-19880 [hull=0.000, icsd=8, PRIMARY]; FeTe P4/nmm (129) mp-21273 [hull=0.081, icsd=4, PRIMARY]; Fe3Te Fm-3m (225) mp-1184307 [hull=0.311, PRIMARY]; Fe2Te3 R-3c (167) mp-685077 [hull=1.514, PRIMARY]; FeTe2 Pa-3 (205) mp-1102002 [hull=0.046, icsd=1]
- papers: https://doi.org/10.1063/1.2361088 (Preparation and thermoelectric properties of sintered Fe1−xCoxTe2 (0≤x...) | https://doi.org/10.1016/j.physc.2012.08.006 (Magnetothermoelectric effects in <mml:math altimg=\"si8.gif\" overflow...) | https://doi.org/10.1016/j.phpro.2014.09.028 (Thermal Conductivity and Electrical Resistivity of FeTe1-xSx Sintered ...)

## Ga-Sb-Se-Te
- rank 1436 | 4 samples | 1 papers | 4 compositions
- compositions: Ga7Sb2Te5Se5 (1); Ga12Sb2Te7.5Se7.5 (1); Ga7Sb2Te8Se2 (1); Ga12Sb2Te12Se3 (1)
- sample form: Bulk (4)
- solid-solution axis: Se/(Se+Te) spans 0.20-0.50 (median 0.50) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 322-725 K (5th-95th pct of 16 curves)
- papers: https://doi.org/10.1021/cm404115k (Enhancing the Thermoelectric Properties of Germanium Antimony Tellurid...)

## Ga-Sb-Sr
- rank 1437 | 4 samples | 1 papers | 4 compositions
- compositions: Sr3GaSb3 (1); Sr3Ga0.98Zn0.02Sb3 (1); Sr3Ga0.93Zn0.07Sb3 (1); Sr3Ga0.95Zn0.05Sb3 (1)
- dopant candidates (<5% at.): Zn (3)
- measured range: 306-984 K (5th-95th pct of 16 curves)
- papers: https://doi.org/10.1039/c2ee22378c (Thermoelectric properties of Sr3GaSb3 – a chain-forming Zintl compound)

## Ga-Sm
- rank 1438 | 4 samples | 1 papers | 1 compositions
- compositions: SmGa2 (4)
- sample form: SingleCrystal (4)
- measured range: 10-248 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SmGa2 P6/mmm (191) mp-477 [hull=0.000, icsd=4, PRIMARY]; SmGa Cmcm (63) mp-999177 [hull=0.000, icsd=3, PRIMARY]; Sm3Ga Pm-3m (221) mp-20366 [hull=0.073, icsd=2, PRIMARY]; Sm5Ga3 P4/ncc (130) mp-21658 [hull=0.000, icsd=1, PRIMARY]; Sm9Ga4 I4/m (87) mp-11415 [hull=0.003, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0921-4526(93)90665-s (Transport properties of RGa2 (R=La, Ce and Sm))

## Gd-La-S
- rank 1439 | 4 samples | 1 papers | 4 compositions
- compositions: LaGdS3 (1); LaGd1.01S3 (1); LaGd1.02S3 (1); LaGd1.03S3 (1)
- measured range: 298-975 K (5th-95th pct of 16 curves)
- papers: https://doi.org/10.1007/s11664-010-1436-5 (Preparation and Thermoelectric Properties of LaGd1+x S3 and SmGd1+x S3)

## Gd-Pd
- rank 1440 | 4 samples | 1 papers | 1 compositions
- compositions: Gd7Pd3 (4)
- sample form: SingleCrystal (4)
- measured range: 10-332 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdPd3 Pm-3m (221) mp-1064256 [hull=0.000, icsd=9, PRIMARY]; GdPd Cmcm (63) mp-11427 [hull=0.000, icsd=4, PRIMARY]; Gd3Pd2 P4/mbm (127) mp-22077 [hull=0.009, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2006.08.352 (Magnetoresistance behaviour and thermoelectric transport properties of...)

## Gd-Rh
- rank 1441 | 4 samples | 1 papers | 1 compositions
- compositions: Gd7Rh3 (4)
- sample form: SingleCrystal (4)
- measured range: 10-293 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdRh Pm-3m (221) mp-1742 [hull=0.000, icsd=5, PRIMARY]; GdRh2 Fd-3m (227) mp-20084 [hull=0.000, icsd=4, PRIMARY]; GdRh3 P6_3/mmc (194) mp-1191219 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2006.08.352 (Magnetoresistance behaviour and thermoelectric transport properties of...)

## Ge-Hg-Te-Tl
- rank 1442 | 4 samples | 1 papers | 4 compositions
- compositions: Tl2HgGeTe4 (1); I0.001Tl2HgGeTe3.999 (1); Pb0.001Tl1.999HgGeTe4 (1); As0.001Tl2HgGe0.999Te4 (1)
- dopant candidates (<5% at.): I (1), Pb (1), As (1)
- measured range: 80-301 K (5th-95th pct of 14 curves)
- papers: https://doi.org/10.1021/cm0518067 (Tl2AXTe4(A = Cd, Hg, Mn; X = Ge, Sn):  Crystal Structure, Electronic S...)

## Ge-K
- rank 1443 | 4 samples | 1 papers | 4 compositions
- compositions: K32Li2Ge175.5 (1); K8Li2Ge43.5 (1); K8Li1Ge43.75 (1); K32LiGe173.75 (1)
- dopant candidates (<5% at.): Li (4)
- measured range: 10-300 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): KGe P-43n (218) mp-2146 [hull=0.000, icsd=3, PRIMARY]; K3Ge17 Fd-3m (227) mp-1196998 [hull=0.000, icsd=1, PRIMARY]; K4Ge23 Pm-3n (223) mp-27800 [hull=0.000, icsd=1, PRIMARY]; K3Ge Fm-3m (225) mp-1184854 [hull=0.236, PRIMARY]; KGe I4_1/acd (142) mp-1201758 [hull=0.011, icsd=1]
- papers: https://doi.org/10.1007/s11664-015-3960-9 (Synthesis and Thermoelectric Properties of the Clathrate-I Phase K8Li ...)

## Ge-Pb-Sn
- rank 1444 | 4 samples | 1 papers | 1 compositions
- compositions: Ge0.6Pb0.3Sn0.1 (4)
- sample form: Bulk (4)
- measured range: 323-773 K (5th-95th pct of 16 curves)
- papers: https://doi.org/10.1021/jp103697s (Thermoelectric Properties Evolution of Spark Plasma Sintered (Ge0.6Pb0...)

## Ge-Ru-Y
- rank 1445 | 4 samples | 1 papers | 3 compositions
- compositions: Y3Ru4Ge13 (2); Y3Ru3.6Co0.4Ge13 (1); Y3Ru3.2Co0.8Ge13 (1)
- dopant candidates (<5% at.): Co (2)
- measured range: 11-797 K (5th-95th pct of 14 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y(GeRu)2 I4/mmm (139) mp-21001 [hull=0.000, icsd=2, PRIMARY]; Y2Ge5Ru3 Ibam (72) mp-620812 [hull=0.000, icsd=2, PRIMARY]; Y3Ge13Ru4 Pm-3n (223) mp-704462 [hull=0.023, icsd=2, PRIMARY]; Y2Ge2Ru C2/m (12) mp-1207905 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1063/1.2753592 (Thermoelectric properties of rare earth–ruthenium–germanium compounds)

## Ge-Se-Sn
- rank 1446 | 4 samples | 2 papers | 4 compositions
- compositions: Sn0.7Ge0.3Se (1); Sn0.9Ge0.1Se (1); Sn0.8Ge0.2Se (1); Ge0.79Ag0.01Sn0.2Se (1)
- dopant candidates (<5% at.): Ag (1)
- solid-solution axis: Ge/(Ge+Sn) spans 0.10-0.80 (median 0.30) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 14-701 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SnGeSe2 Pmc2_1 (26) mp-1218835 [hull=0.009, PRIMARY]
- papers: https://doi.org/10.1038/srep26774 (Giant Seebeck effect in Ge-doped SnSe) | https://doi.org/10.1016/j.jmat.2016.09.001 (Thermoelectric properties of GeSe)

## H-Mg-Ni
- rank 1447 | 4 samples | 1 papers | 4 compositions
- compositions: Mg2NiH0.7 (1); Mg2NiH1.3 (1); Mg2NiH3.5 (1); Mg2NiH4 (1)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg2NiH4 C2/c (15) mp-697331 [hull=0.000, icsd=4, PRIMARY]; MgNiH2 P4/mmm (123) mp-1017509 [hull=0.038, icsd=1, PRIMARY]; MgNiH P4/mmm (123) mp-1008881 [hull=0.036, icsd=1, PRIMARY]; MgNiH3 Pm-3m (221) mp-1017629 [hull=0.006, icsd=1, PRIMARY]; Mg2NiH2 P4_2/mnm (136) mp-1078818 [hull=0.109, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.69.115326 (Temperature dependence of magnetoresistance and Hall effect in<mml:mat...)

## Hg-Sn-Te-Tl
- rank 1448 | 4 samples | 1 papers | 4 compositions
- compositions: I0.001Tl2HgSnTe3.999 (1); Ga0.001Tl2HgSnTe3.999 (1); Tl2HgSnTe4 (1); Pb0.001Tl1.999HgSnTe4 (1)
- dopant candidates (<5% at.): I (1), Ga (1), Pb (1)
- measured range: 80-301 K (5th-95th pct of 15 curves)
- papers: https://doi.org/10.1021/cm0518067 (Tl2AXTe4(A = Cd, Hg, Mn; X = Ge, Sn):  Crystal Structure, Electronic S...)

## Hg-Te
- rank 1449 | 4 samples | 2 papers | 2 compositions
- compositions: HgTe (3); HgS0.045Te0.955 (1)
- dopant candidates (<5% at.): S (1)
- measured range: 91-397 K (5th-95th pct of 4 curves)
- [ref 1] TEDesignLab / ICSD: HgTe P3_121 (152) mp-358 [hull=0.063, icsd=3]; HgTe P3_221 (154) mp-1071269 [hull=0.068, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: HgTe F-43m (216) mp-2730 [hull=0.000, icsd=28, PRIMARY]; HgTe Fm-3m (225) mp-1811 [hull=0.153, icsd=5]; HgTe Cmcm (63) mp-1507 [hull=0.168, icsd=2]; HgTe Pm-3m (221) mp-13141 [hull=0.411, icsd=1]; HgTe I-4m2 (119) mp-1223902 [hull=0.174]
- papers: https://doi.org/10.1007/bf00549999 (Galvanomagnetic and thermoelectric properties of HgSx Te1?x solid solu...) | https://doi.org/10.1038/s41598-018-28043-3 (Semi-metals as potential thermoelectric materials)

## I-Mo-Sb
- rank 1450 | 4 samples | 1 papers | 4 compositions
- compositions: Mo3Sb7I0.75 (1); Mo3Sb7I1.25 (1); Mo3Sb7I1.50 (1); Mo3Sb7I1.00 (1)
- sample form: Bulk (4)
- measured range: 298-873 K (5th-95th pct of 20 curves)
- papers: https://doi.org/10.1063/1.5144156 (Beneficial influence of iodine substitution on the thermoelectric prop...)
