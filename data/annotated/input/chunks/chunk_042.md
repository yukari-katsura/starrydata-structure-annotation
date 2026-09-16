# Host systems -- chunk 042 of 73

Ranks 2051-2100 by sample count. These 50 host systems cover 100 samples (0.19% of the TE set); cumulative through this chunk: 96.49%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Ca-Fe-Mn-O
- rank 2051 | 2 samples | 2 papers | 2 compositions
- compositions: Ca0.9Y0.1Mn0.75Fe0.25O3 (1); CaMn0.7Fe0.3O3 (1)
- dopant candidates (<5% at.): Y (1)
- sample form: Bulk (1)
- measured range: 200-1173 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca2MnFeO5 Pnma (62) mp-619355 [hull=0.010, PRIMARY]; Ca4MnFe3O10 P2_1/c (14) mp-1227204 [hull=0.004, PRIMARY]; SrCa7Mn6(FeO10)2 P1 (1) mp-1077691 [hull=0.068, PRIMARY]; SrCa7Mn6(FeO12)2 Amm2 (38) mp-1077667 [hull=0.094, PRIMARY]
- papers: https://doi.org/10.1007/s10853-012-6834-z (High-temperature thermoelectric properties of Ca0.9Y0.1Mn1−x Fe x O3 (...) | https://doi.org/10.1063/1.4770378 (Transport and magnetic properties of Fe doped CaMnO<sub>3</sub>)

## Ca-Fe-Nd-O
- rank 2052 | 2 samples | 2 papers | 2 compositions
- compositions: La0.18Nd0.32Ca0.26Ba0.24FeO3 (1); Nd0.6Ca0.4FeO3 (1)
- dopant candidates (<5% at.): Ba (1), La (1)
- sample form: rod-shaped (1)
- measured range: 330-1073 K (5th-95th pct of 2 curves; full span incl. outliers 330-1223 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaNdFeO4 Cmc2_1 (36) mp-1227142 [hull=0.049, PRIMARY]
- papers: https://doi.org/10.1002/fuce.201000048 (Effect of the A Cation Size Disorder on the Properties of an Iron Pero...) | https://doi.org/10.1016/j.ceramint.2006.03.035 (Synthesis and electrical properties of Ln0.6Ca0.4FeO3−δ (LnPr, Nd, Sm)...)

## Ca-Gd-Mn-O
- rank 2053 | 2 samples | 2 papers | 2 compositions
- compositions: CaGdMnO3 (1); Gd0.3Ca0.7MnO3 (1)
- sample form: Bulk (1)
- measured range: 41-700 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1100/2012/149670 (Thermoelectric Properties of Ca1−xGdxMnO3−δ(0.00, 0.02, and 0.05) Systems) | https://doi.org/10.1016/j.jmmm.2009.07.054 (The effect of Gd-doping on the charge ordering state of Bi0.3−xGdxCa0....)

## Ca-La-S
- rank 2054 | 2 samples | 1 papers | 2 compositions
- compositions: La2.27Ca0.73S4 (1); La2.53Ca0.47S4 (1)
- measured range: 298-1222 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca(LaS2)2 I-42d (122) mp-35421 [hull=0.013, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(01)00926-4 (Phase relation and thermoelectric properties of the ternary lanthanum ...)

## Ca-O-Ti-Y
- rank 2055 | 2 samples | 1 papers | 2 compositions
- compositions: Y0.61Ca0.39TiO3 (1); Y0.58Ca0.42TiO3 (1)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca3YTi4O12 Pm (6) mp-1227620 [hull=0.000, PRIMARY]; CaY3Ti4O12 Pm (6) mp-1227117 [hull=0.031, PRIMARY]; CaYTi2O6 Pmn2_1 (31) mp-1227099 [hull=0.011, PRIMARY]
- papers: https://doi.org/10.1016/s0921-4526(97)00021-5 (Specific heat and thermoelectric power of Mott transition compound Y0....)

## Ca-Pt-Sn
- rank 2056 | 2 samples | 1 papers | 1 compositions
- compositions: Ca3Pt4Sn12 (2)
- sample form: SingleCrystal (2)
- measured range: 10-300 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca2Sn5Pt3 Pnma (62) mp-21774 [hull=0.000, icsd=1, PRIMARY]; CaSnPt Pnma (62) mp-1102040 [hull=0.000, icsd=1, PRIMARY]; Ca3Sn13Pt4 Pm-3n (223) mp-1214141 [hull=0.008, PRIMARY]
- papers: https://doi.org/10.1039/d4tc04812a (Large magnetoresistance and thermoelectric properties of a quasi-skutt...)

## Cd-Cr-S
- rank 2057 | 2 samples | 1 papers | 1 compositions
- compositions: CdCr2S4 (2)
- measured range: 11-292 K (5th-95th pct of 4 curves)
- [ref 1] TEDesignLab / ICSD: Cr2CdS4 Fd-3m (227) mp-4338 [hull=0.000, icsd=12, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Cr8Cd3CuS16 R3m (160) mp-1226128 [hull=0.013, PRIMARY]
- papers: https://doi.org/10.1209/0295-5075/104/17005 (Magnetic-polaron–induced colossal magnetocapacitance in CdCr2S4)

## Cd-Eu-Mn-Sb
- rank 2058 | 2 samples | 1 papers | 2 compositions
- compositions: EuCd1.6Mn0.4Sb2 (1); EuCd1.4Mn0.6Sb2 (1)
- sample form: Bulk (2)
- measured range: 312-678 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.1016/s1002-0721(14)60531-7 (Effect of manganese doping on the thermoelectric properties of Zintl p...)

## Cd-Fe-Mn-O
- rank 2059 | 2 samples | 1 papers | 2 compositions
- compositions: Mn0.6Cd0.4Fe2O4 (1); Mn0.4Cd0.6Fe2O4 (1)
- measured range: 310-599 K (5th-95th pct of 2 curves; full span incl. outliers 310-674 K)
- papers: https://doi.org/10.1016/s0167-577x(00)00015-x (Thermoelectric power and electrical conductivity of cadmium-substitute...)

## Cd-O-Pr-W
- rank 2060 | 2 samples | 1 papers | 1 compositions
- compositions: CdPr2W2O10 (2)
- measured range: 297-494 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1080/14786435.2012.704427 (Dielectric and magnetic permittivities of three new ceramic tungstates...)

## Cd-O-Sn
- rank 2061 | 2 samples | 2 papers | 1 compositions
- compositions: Cd2SnO4 (2)
- measured range: 97-360 K (5th-95th pct of 2 curves)
- [ref 1] TEDesignLab / ICSD: CdSnO3 R-3 (148) mp-754329 [hull=0.000, icsd=3, PRIMARY]; Cd2SnO4 Pbam (55) mp-5966 [hull=0.000, icsd=3, PRIMARY]; CdSnO3 Pnma (62) mp-849371 [hull=0.030, icsd=3]
- [ref 2] MP, ranked by ICSD evidence: Cd18Sn19O56 P1 (1) mp-685363 [hull=0.124, PRIMARY]; Cd2SnO4 Fd-3m (227) mp-1104726 [hull=0.099, icsd=1]; CdSnO3 P2_1/m (11) mp-1182642 [hull=0.165]; CdSnO3 Pm-3m (221) mp-1016881 [hull=0.346]; Cd2SnO4 Imma (74) mp-675857 [hull=0.001]
- papers: https://doi.org/10.1016/0040-6090(85)90404-3 (Electrical and optical properties of conducting N-type Cd2SnO4 thin films) | https://doi.org/10.1016/0040-6090(87)90207-0 (Preparation, electrical properties and optical characterization of Cd2...)

## Cd-Sn-Te
- rank 2062 | 2 samples | 1 papers | 2 compositions
- compositions: SnCd0.12Te (1); SnCd0.15Te (1)
- measured range: 298-824 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CdSnTe2 R-3m (166) mp-1226740 [hull=0.094, PRIMARY]
- papers: https://doi.org/10.1039/c6ra02658c (Enhanced thermopower in rock-salt SnTe–CdTe from band convergence)

## Cd-Tb
- rank 2063 | 2 samples | 2 papers | 2 compositions
- compositions: TbCd (1); Cd6Tb (1)
- measured range: 10-233 K (5th-95th pct of 3 curves; full span incl. outliers 10-295 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TbCd Pm-3m (221) mp-721 [hull=0.000, icsd=5, PRIMARY]; TbCd2 P6/mmm (191) mp-30497 [hull=0.000, icsd=1, PRIMARY]; Tb11Cd45 F-43m (216) mp-1197394 [hull=0.004, icsd=1, PRIMARY]; TbCd3 P6_3/mmc (194) mp-30498 [hull=0.001, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(88)90183-7 (Electrical and thermoelectric transport properties of RZn and RCd comp...) | https://doi.org/10.1103/physrevb.82.220201 (Long-range magnetic order in the quasicrystalline approximant<mml:math...)

## Cd-Te-Zn
- rank 2064 | 2 samples | 1 papers | 2 compositions
- compositions: Cd0.80Zn0.20TeIn0.0005 (1); Cd0.8Zn0.2Te (1)
- dopant candidates (<5% at.): In (1)
- sample form: SingleCrystal (2)
- measured range: 292-1324 K (5th-95th pct of 5 curves)
- [ref 1] TEDesignLab / ICSD: ZnCdTe2 I-42d (122) mp-971837 [hull=0.005, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: ZnCdTe Cc (9) mp-1232381 [hull=0.258, PRIMARY]; ZnCdTe2 R3m (160) mp-1215406 [hull=0.025]
- papers: https://doi.org/10.1063/1.4921025 (Thermal conductivity, electrical conductivity, and thermoelectric prop...)

## Ce-Co-In-Rh
- rank 2065 | 2 samples | 1 papers | 1 compositions
- compositions: (CeCoIn5)5(CeRhIn5)5 (2)
- papers: https://doi.org/10.1103/physrevlett.120.187002 (Tuning the Pairing Interaction in a \nd\n-Wave Superconductor by Param...)

## Ce-Co-Sn
- rank 2066 | 2 samples | 1 papers | 1 compositions
- compositions: Ce3Co4Sn13 (2)
- measured range: 12-296 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce3Co4Sn13 Pm-3n (223) mp-21915 [hull=0.013, icsd=5, PRIMARY]
- papers: https://doi.org/10.12693/aphyspola.127.309 (Thermoelectric Properties of Heavy Fermion Compound Ce3Co4Sn13)

## Ce-Cu-Gd-O-Ru-Sr
- rank 2067 | 2 samples | 1 papers | 1 compositions
- compositions: RuSr2GdCeCu2O10 (2)
- sample form: Bulk (2)
- measured range: 55-250 K (5th-95th pct of 3 curves; full span incl. outliers 55-299 K)
- papers: https://doi.org/10.1063/1.2784962 (Magnetothermopower and magnetoresistivity of RuSr2Gd2−xCexCu2O10+δ (x=...)

## Ce-Cu-Ni-Sb
- rank 2068 | 2 samples | 1 papers | 2 compositions
- compositions: Ce3Cu2.25Ni0.75Sb4 (1); Ce3Cu2.5Ni0.5Sb4 (1)
- measured range: 10-379 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1016/j.jallcom.2015.09.104 (Semiconducting behaviour of Ce3 Cu3 Sb4 revisited)

## Ce-Cu-Se
- rank 2069 | 2 samples | 1 papers | 2 compositions
- compositions: Ce0.8Cu0.2Se2 (1); Ce0.7Cu0.3Se2 (1)
- sample form: Bulk (2)
- measured range: 309-922 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeCuSe2 P2_1/c (14) mp-11791 [hull=0.026, icsd=3, PRIMARY]; Ce5CuSe8 I-4 (82) mp-675739 [hull=0.069, PRIMARY]
- papers: https://doi.org/10.1063/1.3311558 (Thermoelectricity and localized f-band control by dp-hybridization on ...)

## Ce-Cu-Sn
- rank 2070 | 2 samples | 2 papers | 1 compositions
- compositions: Ce5CuSn3 (2)
- sample form: Bulk (1)
- measured range: 10-294 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeCuSn P6_3/mmc (194) mp-22761 [hull=0.009, icsd=5, PRIMARY]; Ce(CuSn)2 P4/nmm (129) mp-1080173 [hull=0.000, icsd=3, PRIMARY]; Ce5CuSn3 P6_3/mcm (193) mp-1190264 [hull=0.011, icsd=1, PRIMARY]; CeCu5Sn Pnma (62) mp-637204 [hull=0.000, icsd=1, PRIMARY]; Ce2(CuSn)3 P4/mmm (123) mp-1206459 [hull=2.187, PRIMARY]
- papers: https://doi.org/10.1007/s10582-004-0413-8 (Formation of Heavy-fermion State in Ce5-xLaxCuSn3) | https://doi.org/10.1016/j.jallcom.2004.04.054 (Magnetic, electronic transport and thermodynamic properties of Ce5CuSn3)

## Ce-Fe-O-P
- rank 2071 | 2 samples | 1 papers | 2 compositions
- compositions: La0.1Ce0.9FePO (1); CeFePO (1)
- dopant candidates (<5% at.): La (1)
- measured range: 11-297 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce2FeP2O P4/mmm (123) mp-1213918 [hull=1.698, PRIMARY]
- papers: https://doi.org/10.1209/0295-5075/123/57002 (Spin glass, single-ion and dense Kondo effects in La\n                ...)

## Ce-Fe-Si
- rank 2072 | 2 samples | 2 papers | 1 compositions
- compositions: CeFe2Si2 (2)
- measured range: 15-802 K (5th-95th pct of 3 curves; full span incl. outliers 15-904 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(FeSi)2 I4/mmm (139) mp-3035 [hull=0.000, icsd=7, PRIMARY]; CeFeSi P4/nmm (129) mp-20245 [hull=0.000, icsd=3, PRIMARY]; CeFeSi2 Cmcm (63) mp-1025450 [hull=0.000, icsd=1, PRIMARY]; CeFe9Si4 I4/mcm (140) mp-1193262 [hull=0.010, icsd=1, PRIMARY]; Ce2Fe20Si2C P-1 (2) mp-1227651 [hull=0.058, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2006.08.353 (Peculiarities of the intermediate valence state of Ce in CeM2Si2 (M=Fe...) | https://doi.org/10.1016/s0925-8388(02)00858-7 (Thermoelectric power in compounds with an intermediate valence of Ce: ...)

## Ce-Gd-O-Zr
- rank 2073 | 2 samples | 1 papers | 2 compositions
- compositions: (Gd0.7Ce0.3)2Zr2O7.3 (1); (Gd0.5Ce0.5)2Zr2O7.5 (1)
- sample form: Bulk (2)
- measured range: 299-972 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1007/s10853-017-1212-5 (Ultralow thermal conductivity of cerium-doped Nd2Zr2O7 over a wide dop...)

## Ce-Ge-In-Rh
- rank 2074 | 2 samples | 1 papers | 2 compositions
- compositions: CeRh0.8Ge0.2In (1); CeRh0.7Ge0.3In (1)
- sample form: Bulk (2)
- measured range: 10-300 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/j.intermet.2014.09.001 (Electronic properties of CeRh1−xGexIn; evolution from an intermediate-...)

## Ce-Ge-Si
- rank 2075 | 2 samples | 1 papers | 2 compositions
- compositions: CeSi1.6Ge0.4 (1); CeSiGe (1)
- sample form: Bulk (2)
- measured range: 240-380 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce2SiGe Pmc2_1 (26) mp-1226899 [hull=0.016, PRIMARY]; CeSiGe Imma (74) mp-1226579 [hull=0.030, PRIMARY]; CeSiGe I4_1md (109) mp-1206173 [hull=0.051]
- papers: https://doi.org/10.1016/j.jallcom.2005.07.053 (Thermoelectric properties of the solid solutions based on ThSi2-type C...)

## Ce-Mn-O-Sr
- rank 2076 | 2 samples | 2 papers | 1 compositions
- compositions: Sr0.7Ce0.3MnO3 (2)
- sample form: pellets (1)
- measured range: 320-1270 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2CeMn3O9 C2/m (12) mp-1218910 [hull=0.024, PRIMARY]; Sr3CeMn4O12 Im-3m (229) mp-1218514 [hull=0.032, PRIMARY]; Sr4CeMn5O15 C2/m (12) mp-1218672 [hull=0.026, PRIMARY]
- papers: https://doi.org/10.1023/a:1009936515152 ([]) | https://doi.org/10.1016/s0025-5408(00)00456-6 (Study on the structural and electrical properties of Sr1−xCexMnO3−α (x...)

## Ce-Ni-P
- rank 2077 | 2 samples | 1 papers | 2 compositions
- compositions: CeNi2(As0.1P0.9)2 (1); CeNi2P2 (1)
- dopant candidates (<5% at.): As (1)
- measured range: 11-299 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce25Ni49P33 P-6m2 (187) mp-680512 [hull=0.029, icsd=1, PRIMARY]; Ce6Ni6P17 I-43m (217) mp-1193687 [hull=0.000, icsd=1, PRIMARY]; CeNiP P6_3/mmc (194) mp-1103629 [hull=0.000, icsd=1, PRIMARY]; Ce9(Ni13P6)2 P-6m2 (187) mp-649704 [hull=0.032, icsd=1, PRIMARY]; Ce2Ni12P5 P2_1/m (11) mp-1214085 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1038/s41598-019-48662-8 (Heavy fermion quantum criticality at dilute carrier limit in CeNi2−δ(A...)

## Ce-Ni-Rh-Si
- rank 2078 | 2 samples | 1 papers | 2 compositions
- compositions: CeRh1.7Ni0.3Si2 (1); CeRh1.6Ni0.4Si2 (1)
- sample form: Polycrystal (2)
- measured range: 11-299 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/0038-1098(89)90175-0 (Thermoelectric power behaviour of CeRh2−xNixSi2 alloys)

## Ce-O-Si
- rank 2079 | 2 samples | 1 papers | 2 compositions
- compositions: (Ce3Si2)26.53(CeO2)73.47 (1); (Ce3Si2)13.4(CeO2)86.6 (1)
- measured range: 298-1272 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce2Si2O7 P4_1 (76) mp-672208 [hull=0.000, icsd=3, PRIMARY, AMBIGUOUS]; CeSiO4 I4_1/amd (141) mp-10523 [hull=0.033, icsd=1, PRIMARY]; CaCe4Si3O13 P6_3 (173) mp-1229253 [hull=0.000, PRIMARY]; Ce2Si2O7 P2_1/c (14) mp-662527 [hull=0.000, icsd=3]
- papers: https://doi.org/10.1016/j.net.2020.07.016 (Fabrication and thermal conductivity of CeO2–Ce3Si2 composite)

## Ce-O-Sm
- rank 2080 | 2 samples | 1 papers | 2 compositions
- compositions: Ce0.7Sm0.3O1.85 (1); Ce0.5Sm0.5O1.75 (1)
- measured range: 473-1274 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce2Sm2O7 Fd-3m (227) mp-752400 [hull=0.081, PRIMARY]; Ce4SmO10 I4/m (87) mp-1226911 [hull=0.026, PRIMARY]; Ce4SmO9 Imm2 (44) mp-754306 [hull=0.026, PRIMARY]; Ce5Sm2O13 R3m (160) mp-753792 [hull=0.035, PRIMARY]; Ce9SmO20 P-1 (2) mp-676636 [hull=0.012, PRIMARY]
- papers: https://doi.org/10.1007/s40145-016-0196-y (Ce1−x\n                            Sm\n                x\n            ...)

## Ce-O-Zr
- rank 2081 | 2 samples | 2 papers | 2 compositions
- compositions: (ZrO2)0.5(Ce02)0.5 (1); (Nd0.2Ce0.8)2Zr2O7.8 (1)
- dopant candidates (<5% at.): Nd (1)
- sample form: Powder (1); Bulk (1)
- measured range: 290-973 K (5th-95th pct of 2 curves; full span incl. outliers 290-1808 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeZrO4 P2_13 (198) mp-4843 [hull=0.062, icsd=3, PRIMARY]; Ce3Zr5O16 C222 (21) mp-1019589 [hull=0.046, icsd=1, PRIMARY]; Ce7ZrO16 P4/mmm (123) mp-1191683 [hull=0.022, icsd=1, PRIMARY]; Ce5Zr3O16 C222 (21) mp-1019595 [hull=0.040, icsd=1, PRIMARY]; CeZr3O8 C2/c (15) mp-1019600 [hull=0.045, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/s11666-997-0071-z (Thermal and mechanical properties of ZrO2-CeO2 plasma-sprayed coatings) | https://doi.org/10.1007/s10853-017-1212-5 (Ultralow thermal conductivity of cerium-doped Nd2Zr2O7 over a wide dop...)

## Ce-Os
- rank 2082 | 2 samples | 1 papers | 1 compositions
- compositions: CeOs2 (2)
- sample form: Bulk (1)
- measured range: 11-297 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeOs2 Fd-3m (227) mp-2098 [hull=0.000, icsd=5, PRIMARY]; Ce3Os Pnma (62) mp-1188974 [hull=0.000, icsd=1, PRIMARY]; Ce4Os Fd-3m (227) mp-1213963 [hull=0.526, PRIMARY]; CeOs2 P6_3/mmc (194) mp-1102302 [hull=0.000, icsd=2]
- papers: https://doi.org/10.1007/bf02570272 (Evidence of the different valence states in the C14 and C15 phases CeOs2)

## Ce-Pb
- rank 2083 | 2 samples | 2 papers | 1 compositions
- compositions: CePb3 (2)
- sample form: Polycrystal (1)
- measured range: 10-252 K (5th-95th pct of 3 curves; full span incl. outliers 10-292 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CePb3 Pm-3m (221) mp-20225 [hull=0.000, icsd=4, PRIMARY]; Ce5Pb3 P6_3/mcm (193) mp-1190312 [hull=0.000, icsd=1, PRIMARY]; CePb2 I4/mmm (139) mp-1206707 [hull=0.252, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(88)90399-x (Thermoelectric power of Ce(Pb1−xSnx)3) | https://doi.org/10.1016/0304-8853(87)90605-6 (Seebeck coefficient of heavy fermion compounds)

## Ce-Rh
- rank 2084 | 2 samples | 2 papers | 2 compositions
- compositions: CeRh2 (1); Ce7Rh3 (1)
- sample form: Polycrystal (1)
- measured range: 11-297 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeRh3 Pm-3m (221) mp-1518 [hull=0.000, icsd=9, PRIMARY]; CeRh2 Fd-3m (227) mp-951 [hull=0.000, icsd=8, PRIMARY]; CeRh Cmcm (63) mp-1018117 [hull=0.000, icsd=2, PRIMARY]; Ce5Rh4 Pnma (62) mp-680602 [hull=0.024, icsd=2, PRIMARY]; Ce5Rh3 P4/ncc (130) mp-1200347 [hull=0.028, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/j.physb.2005.03.028 (Crossover in charge transport of CeM2) | https://doi.org/10.1016/s0925-8388(98)00458-7 (Magnetic and electrical properties of the intermetallic compounds R7Rh...)

## Ce-Rh-Sb
- rank 2085 | 2 samples | 2 papers | 1 compositions
- compositions: CeRhSb (2)
- measured range: 10-290 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce2Sb4Rh3 Pnma (62) mp-1200949 [hull=0.000, icsd=1, PRIMARY]; CeSbRh Pnma (62) mp-22249 [hull=0.000, icsd=1, PRIMARY]; Ce2Sb3Rh4 P4mm (99) mp-1227249 [hull=0.200, PRIMARY]; CeSbRh C2/m (12) mp-1226674 [hull=0.157]
- papers: https://doi.org/10.1016/0921-4526(94)90919-9 (Thermopower and resistivity of CeRhSb and CePtSn) | https://doi.org/10.1016/0921-4526(94)91903-8 (Thermoelectric power of Ce-based Kondo alloys)

## Ce-Sb-Te
- rank 2086 | 2 samples | 1 papers | 2 compositions
- compositions: CeTe1.5Sb0.5 (1); CeTe1.75Sb0.25 (1)
- sample form: SingleCrystal (2)
- measured range: 100-300 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeSbTe P4/nmm (129) mp-917643 [hull=0.035, icsd=2, PRIMARY]; Ce2SbTe P4/mmm (123) mp-1226772 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1063/1.4756911 (Dimensional crossover of charge density wave and thermoelectric proper...)

## Ce-Th
- rank 2087 | 2 samples | 2 papers | 1 compositions
- compositions: Th94Ce6 (2)
- measured range: 12-287 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce3Th I4/mmm (139) mp-1183824 [hull=0.011, PRIMARY]; CeTh R-3m (166) mp-1226523 [hull=0.017, PRIMARY]; CeTh3 Pm-3m (221) mp-1183732 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1007/bf00655253 (The thermoelectric power of someThCe alloys) | https://doi.org/10.1007/bf00655330 (Comments upon ?the thermoelectric power of someThCe alloys? and an alt...)

## Cl-Cr
- rank 2088 | 2 samples | 1 papers | 1 compositions
- compositions: CrCl3 (2)
- measured range: 10-97 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CrCl2 Pnnm (58) mp-22857 [hull=0.062, icsd=10, PRIMARY]; CrCl3 C2/m (12) mp-27630 [hull=0.001, icsd=2, PRIMARY]; CrCl P6_3mc (186) mp-1183702 [hull=0.760, PRIMARY]
- papers: https://doi.org/10.48550/ARXIV.2305.13268 (Spin-phonon scattering-induced low thermal conductivity in a van der W...)

## Cl-Fe
- rank 2089 | 2 samples | 1 papers | 1 compositions
- compositions: FeCl2 (2)
- measured range: 11-47 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeCl2 R-3m (166) mp-23229 [hull=0.000, icsd=4, PRIMARY]; FeCl3 R-3 (148) mp-23204 [hull=0.096, icsd=4, PRIMARY]; FeCl Pm-3m (221) mp-985588 [hull=0.925, PRIMARY]; FeCl4 Cmmm (65) mp-1225059 [hull=0.000, PRIMARY]; FeCl6 Cmmm (65) mp-1207367 [hull=0.333, PRIMARY]
- papers: https://doi.org/10.48550/ARXIV.2305.13268 (Spin-phonon scattering-induced low thermal conductivity in a van der W...)

## Co-Cr-O-Y
- rank 2090 | 2 samples | 1 papers | 1 compositions
- compositions: Y0.8Ca0.2Cr0.7Co0.3O3 (2)
- dopant candidates (<5% at.): Ca (2)
- measured range: 893-1259 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1149/1.3337156 (Calcium- and Cobalt-Doped Yttrium Chromites as an Interconnect Materia...)

## Co-Cu-Fe-O
- rank 2091 | 2 samples | 1 papers | 2 compositions
- compositions: Cu0.6Co0.4Fe2O4 (1); Cu0.4Co0.6Fe2O4 (1)
- measured range: 310-874 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.jallcom.2006.02.002 (Thermoelectric power studies of Cu–Co ferrites)

## Co-Cu-Hf-Sb-Sn-Te-Ti
- rank 2092 | 2 samples | 1 papers | 1 compositions
- compositions: (Hf0.7Ti0.3CoSb0.8Sn0.2)0.75(Cu1.96Ni0.04Te0.97Se0.03)0.25 (2)
- dopant candidates (<5% at.): Ni (2), Se (2)
- measured range: 321-1024 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.1039/c8ta04372h (Enhancing the thermoelectric performance of a p-type half-Heusler allo...)

## Co-Cu-Hf-Sb-Sn-Ti
- rank 2093 | 2 samples | 1 papers | 1 compositions
- compositions: (Hf0.7Ti0.3CoSb0.8Sn0.2)0.85(Cu1.96Ni0.04Te0.97Se0.03)0.15 (2)
- dopant candidates (<5% at.): Te (2), Ni (2), Se (2)
- measured range: 320-1024 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1039/c8ta04372h (Enhancing the thermoelectric performance of a p-type half-Heusler allo...)

## Co-Eu-P
- rank 2094 | 2 samples | 1 papers | 1 compositions
- compositions: EuCo2P2 (2)
- measured range: 11-294 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Eu(CoP)2 I4/mmm (139) mp-20038 [hull=0.000, icsd=2, PRIMARY]; Eu2Co12P7 P-6 (174) mp-1191681 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.94.014422 (EuCo2P2: A model molecular-field helical Heisenberg antiferromagnet)

## Co-Fe-Ga
- rank 2095 | 2 samples | 2 papers | 2 compositions
- compositions: Fe0.75Co0.25Ga3 (1); Fe0.5Co0.5Ga3 (1)
- sample form: Bulk (1)
- measured range: 12-395 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GaFeCo2 Fm-3m (225) mp-30551 [hull=0.000, icsd=2, PRIMARY]; GaFe2Co Fm-3m (225) mp-636212 [hull=0.130, icsd=1, PRIMARY]; Ga2FeCo P4/mmm (123) mp-1224867 [hull=0.058, PRIMARY]; GaFe2Co F-43m (216) mp-1224895 [hull=0.285]
- papers: https://doi.org/10.3762/bjnano.4.54 (Structural and thermoelectric properties of TMGa3(TM = Fe, Co) thin films) | https://doi.org/10.1016/j.jallcom.2014.04.117 (Thermoelectric performance of intermetallic FeGa3 with Co doping)

## Co-Fe-Ga-Ge
- rank 2096 | 2 samples | 1 papers | 2 compositions
- compositions: Fe0.75Co0.25Ga2.65Ge0.35 (1); Fe0.50Co0.50Ga2.65Ge0.35 (1)
- sample form: Bulk (2)
- measured range: 83-874 K (5th-95th pct of 14 curves)
- papers: https://doi.org/10.1063/1.4938474 (Improved thermoelectric properties in heavily doped FeGa3)

## Co-Fe-Ge-O
- rank 2097 | 2 samples | 1 papers | 2 compositions
- compositions: Co1.5Ge0.5Fe1.0O4 (1); Co1.4Ge0.4Fe1.2O4 (1)
- measured range: 310-658 K (5th-95th pct of 2 curves; full span incl. outliers 310-719 K)
- papers: https://doi.org/10.1016/s0925-8388(02)01327-0 (Thermoelectric power studies of Co–Ge ferrites)

## Co-Fe-Hf-Ni-Sb-Ti
- rank 2098 | 2 samples | 1 papers | 2 compositions
- compositions: Ti0.75Hf0.25Fe0.3Co0.2Ni0.5Sb (1); Ti0.8Hf0.2Fe0.3Co0.2Ni0.5Sb (1)
- measured range: 299-974 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.1016/j.jmat.2020.12.015 (Enhanced thermoelectric performance in Ti(Fe, Co, Ni)Sb pseudo-ternary...)

## Co-Fe-Mn-O
- rank 2099 | 2 samples | 1 papers | 1 compositions
- compositions: Mn0.5Co0.5Fe2O4 (2)
- sample form: Bulk (2)
- measured range: 471-974 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn2Fe3Co3O16 Cm (8) mp-772328 [hull=0.109, PRIMARY]; Mn3Fe2Co3O16 Cm (8) mp-1176503 [hull=0.069, PRIMARY]; Mn3Fe3(CoO8)2 Cm (8) mp-770195 [hull=0.129, PRIMARY]
- papers: https://doi.org/10.1109/ict.2006.331222 (Thermoelectric Properties of Sintered (MnyCo1-y) Fe2O4)

## Co-Fe-O-Pr-Sr
- rank 2100 | 2 samples | 1 papers | 2 compositions
- compositions: Pr0.4Sr0.6Co0.3Fe0.6Nb0.1O3 (1); Pr0.4Sr0.6Co0.5Fe0.4Nb0.1O3 (1)
- dopant candidates (<5% at.): Nb (2)
- measured range: 360-1169 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrPrFeCoO6 P1 (1) mp-1218109 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2020.154738 (Effects of cobalt and iron proportions in Pr0.4Sr0.6Co0.9-xFexNb0.1O3-...)
