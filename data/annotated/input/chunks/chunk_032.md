# Host systems -- chunk 032 of 73

Ranks 1551-1600 by sample count. These 50 host systems cover 150 samples (0.29% of the TE set); cumulative through this chunk: 94.16%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## As-I-In-Sn
- rank 1551 | 3 samples | 2 papers | 3 compositions
- compositions: Sn17.8In4.0As21.7I8 (1); Sn15.1In8.0As21.5I8 (1); Sn14.6In9As21.5I8 (1)
- measured range: 77-333 K (5th-95th pct of 11 curves)
- papers: https://doi.org/10.1134/s106378261111025x (Anomalously low thermal conductivity and thermoelectric properties of ...) | https://doi.org/10.1002/zaac.201100287 (Synthesis, Crystal Structure, and Thermoelectric Properties of Clathra...)

## As-In-P
- rank 1552 | 3 samples | 1 papers | 3 compositions
- compositions: InAs0.8P0.2 (1); InAs0.9P0.1 (1); InAs0.6P0.4 (1)
- measured range: 291-1064 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): In2AsP R3m (160) mp-1223837 [hull=0.013, PRIMARY, AMBIGUOUS]; In4As3P Pmm2 (25) mp-1223887 [hull=0.018, PRIMARY]; In4AsP3 Amm2 (38) mp-1223884 [hull=0.013, PRIMARY]; In2AsP P-4m2 (115) mp-1223851 [hull=0.015]
- papers: https://doi.org/10.1063/1.1776977 (InAs1‐xPx as a Thermoelectric Material)

## As-Na-O-Ti
- rank 1553 | 3 samples | 1 papers | 1 compositions
- compositions: Na2Ti2As2O (3)
- measured range: 10-301 K (5th-95th pct of 3 curves; full span incl. outliers 10-348 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NaTi2(AsO4)3 R-3c (167) mp-1200852 [hull=0.000, icsd=1, PRIMARY]; NaTiAsO5 P2_1/c (14) mp-1201259 [hull=0.000, icsd=1, PRIMARY]; Na2Ti2As2O I4/mmm (139) mp-1025360 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.80.144516 (Physical properties of the layered pnictide oxidesNa2Ti2P2O(P=As,Sb))

## As-Pt
- rank 1554 | 3 samples | 1 papers | 3 compositions
- compositions: PtAs2 (1); Pt0.99Rh0.01As2 (1); Pt0.995Rh0.005As2 (1)
- dopant candidates (<5% at.): Rh (2)
- sample form: Bulk (3)
- measured range: 11-599 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): As2Pt Pa-3 (205) mp-2513 [hull=0.000, icsd=8, PRIMARY]; AsPt3 P6_3/mmc (194) mp-1183320 [hull=0.232, PRIMARY, AMBIGUOUS]; AsPt3 Pm-3m (221) mp-1183186 [hull=0.234]
- papers: https://doi.org/10.1063/1.4819953 (Enhancing high-temperature thermoelectric properties of PtAs2 by Rh do...)

## As-Sb-Se-Te-Tl
- rank 1555 | 3 samples | 1 papers | 3 compositions
- compositions: As17.65Sb11.76Se8.82Te44.12Tl17.65 (1); As15.38Sb15.38Se7.69Te46.15Tl15.38 (1); As11.11Sb22.22Se5.56Te50Tl11.11 (1)
- measured range: 103-335 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1063/1.1702619 (Thermoelectric Properties of Diphasal Systems Combining As2Te3 and Tl2...)

## As-Se-Th
- rank 1556 | 3 samples | 1 papers | 2 compositions
- compositions: ThAsSe (2); ThAs0.67Se0.33 (1)
- sample form: SingleCrystal (3)
- measured range: 12-316 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ThAsSe P4/nmm (129) mp-1019357 [hull=0.000, icsd=1, PRIMARY]; Th2AsSe2 P4/mmm (123) mp-1207178 [hull=1.887, PRIMARY]
- papers: https://doi.org/10.1016/j.physb.2006.01.371 (Thermoelectric power in off-stoichiometric ThAsSe system)

## B-Be
- rank 1557 | 3 samples | 1 papers | 3 compositions
- compositions: Be2B (1); Be4B (1); BeB6 (1)
- measured range: 323-1297 K (5th-95th pct of 3 curves; full span incl. outliers 323-1785 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Be2B Fm-3m (225) mp-1432 [hull=0.054, icsd=3, PRIMARY]; BeB2 P6/mmm (191) mp-1009823 [hull=0.126, icsd=2, PRIMARY]; Be4B P4/nmm (129) mp-27757 [hull=0.000, icsd=1, PRIMARY]; Be4B25 P2/c (13) mp-1227634 [hull=0.213, PRIMARY]
- papers: https://doi.org/10.1111/j.1151-2916.1974.tb10833.x (Thermal Diffusivity of Be4B, Be2B, and BeB6)

## B-C-Hf
- rank 1558 | 3 samples | 1 papers | 3 compositions
- compositions: (B4C)50(HfB2)50 (1); (B4C)65(HfB2)35 (1); (B4C)70(HfB2)30 (1)
- measured range: 296-972 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HfBC P6_3/mmc (194) mp-1232375 [hull=0.550, PRIMARY]
- papers: https://doi.org/10.1016/j.jeurceramsoc.2016.06.049 (Effect of microstructure on mechanical, electrical and thermal propert...)

## B-C-Ho-N
- rank 1559 | 3 samples | 3 papers | 1 compositions
- compositions: HoB17CN (3)
- measured range: 301-1038 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/j.jssc.2006.03.030 (Thermoelectric properties of homologous p- and n-type boron-rich borides) | https://doi.org/10.1109/ict.2006.331324 (Homologous rare earth boron cluster compounds: a possible n-type count...) | https://doi.org/10.1109/ict.2007.4569503 (Doping effect in N-type rare earth boron carbonitrides)

## B-C-O-Y
- rank 1560 | 3 samples | 1 papers | 1 compositions
- compositions: YBCO (3)
- curator composition details (from the paper): YBCO (1)
- sample form: SingleCrystal (2); Polycrystal (1)
- measured range: 30-140 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YBCO7 Pbca (61) mp-1197370 [hull=0.560, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0921-4526(95)00690-7 (Interaction of carriers with phonons in single- and poly-crystalline h...)

## B-C-Ti
- rank 1561 | 3 samples | 2 papers | 3 compositions
- compositions: (TiB2)73.61(SiC)11.27(C)15.12 (1); (TiB2)0.1(C)0.9 (1); (TiB2)0.2(C)0.8 (1)
- dopant candidates (<5% at.): Si (1)
- curator composition details (from the paper): 10mol% TiB2-doped graphites (1); TiB2-doped graphites (1)
- sample form: SingleCrystal (2)
- measured range: 298-1016 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiBC P6_3/mmc (194) mp-1232377 [hull=0.307, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2017.09.244 (Microstructures and properties of silicon carbide- and graphene nanopl...) | https://doi.org/10.1016/s0022-3115(97)00287-0 (Thermal transport in CKC TiB2-doped graphite)

## B-Ca-Fe-O
- rank 1562 | 3 samples | 1 papers | 3 compositions
- compositions: (CaO)30(B2O3)56(Fe2O3)14 (1); (CaO)30(B2O3)47(Fe2O3)23 (1); (CaO)30(B2O3)54(Fe2O3)16 (1)
- measured range: 418-501 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1063/1.322559 (Electronic properties of calcium borate glasses containing iron oxide)

## B-Ce-Pd
- rank 1563 | 3 samples | 1 papers | 3 compositions
- compositions: CePd3B0.25 (1); CePd3B0.3 (1); CePd3B0.4 (1)
- measured range: 13-297 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeBPd3 Pm-3m (221) mp-19948 [hull=0.213, icsd=2, PRIMARY]; Ce2BPd6 P4/mmm (123) mp-1226779 [hull=0.117, PRIMARY]
- papers: https://doi.org/10.1016/j.physb.2006.01.545 (Study of the thermoelectric properties of)

## B-Co-Na-O
- rank 1564 | 3 samples | 1 papers | 3 compositions
- compositions: Na0.7Co0.75B0.25O2 (1); Na0.7Co0.625B0.375O2 (1); Na0.7Co0.25B0.75O2 (1)
- measured range: 15-300 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Na2Co2(B4O7)3 C2/c (15) mp-704577 [hull=0.012, icsd=1, PRIMARY]; Na3Co(BO3)2 P2_1/c (14) mp-773604 [hull=0.059, PRIMARY]; Na6Co2B4SO16 Fd-3 (203) mp-851008 [hull=0.067, PRIMARY]; NaCoBO3 C2/c (15) mp-1101692 [hull=0.049, PRIMARY]
- papers: https://doi.org/10.1007/s00339-015-9089-0 (Magnetic and thermoelectric properties of B-substituted NaCoO2)

## B-Cr-Y
- rank 1565 | 3 samples | 2 papers | 3 compositions
- compositions: YCrB4 (1); Y0.95Ce0.05CrB6 (1); YCrB6 (1)
- dopant candidates (<5% at.): Ce (1)
- sample form: Bulk (2)
- measured range: 10-1002 K (5th-95th pct of 8 curves; full span incl. outliers 10-1073 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YCrB4 Pbam (55) mp-20450 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2010.05.110 (Applying an electron counting rule to screen prospective thermoelectri...) | https://doi.org/10.1103/physrevb.103.195121 (Thermoelectricity and electronic properties of<mml:math xmlns:mml=\"ht...)

## B-Er
- rank 1566 | 3 samples | 3 papers | 2 compositions
- compositions: ErB12 (2); Er1.12B17.64CN (1)
- dopant candidates (<5% at.): C (1), N (1)
- curator composition details (from the paper): 8% ErB6 and 4% ErB4 was added to ErB17CN (1)
- measured range: 11-1037 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ErB4 P4/mbm (127) mp-2847 [hull=0.000, icsd=5, PRIMARY]; ErB6 Pm-3m (221) mp-1296 [hull=0.054, icsd=4, PRIMARY]; ErB2 P6/mmm (191) mp-1774 [hull=0.000, icsd=3, PRIMARY]; ErB12 Fm-3m (225) mp-1104598 [hull=0.000, icsd=1, PRIMARY]; Ca(Er2B15)2 P4/mmm (123) mp-1227415 [hull=0.051, PRIMARY]
- papers: https://doi.org/10.1109/ict.2007.4569503 (Doping effect in N-type rare earth boron carbonitrides) | https://doi.org/10.1016/0925-8388(94)05070-8 (Transition and rare earth element dodecaborides) | https://doi.org/10.1007/bf01164105 (Thermal conductivity of metal dodecaborides with a UB12 structure)

## B-Fe-Ni-P
- rank 1567 | 3 samples | 2 papers | 1 compositions
- compositions: Fe40Ni40P14B6 (3)
- sample form: Ribbon (2)
- measured range: 20-508 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/0022-3093(86)90064-5 (Thermoelectric power in some ferromagnetic Fe based amorphous alloys) | https://doi.org/10.1016/0304-8853(80)90831-8 (Transport properties of Fe-Ni Glasses)

## B-Fe-O
- rank 1568 | 3 samples | 2 papers | 1 compositions
- compositions: Fe2OBO3 (3)
- measured range: 163-649 K (5th-95th pct of 3 curves; full span incl. outliers 163-794 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe3B7IO13 R3c (161) mp-1194881 [hull=0.000, icsd=2, PRIMARY]; Fe2B2O5 P-1 (2) mp-19333 [hull=0.000, icsd=2, PRIMARY]; Fe3BO6 Pnma (62) mp-25746 [hull=0.025, icsd=2, PRIMARY]; FeBO3 R-3c (167) mp-19097 [hull=0.000, icsd=1, PRIMARY]; Fe5(BO3)6 Pmmn (59) mp-1198168 [hull=0.113, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/cm0609698 (Role of t2gversus egInteractions in the Physical Properties of A2OBO3(...) | https://doi.org/10.1103/physrevb.82.165106 (Electrical transport in charge-orderedFe2OBO3: Resistive switching and...)

## B-Lu-Ni
- rank 1569 | 3 samples | 1 papers | 3 compositions
- compositions: LuNi2B2 (1); Lu0.925Yb0.075Ni2B2 (1); Lu0.8Yb0.2Ni2B2 (1)
- dopant candidates (<5% at.): Yb (2)
- sample form: SingleCrystal (3)
- measured range: 10-296 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Lu3Ni7B2 P6_3/mmc (194) mp-865190 [hull=0.000, icsd=2, PRIMARY]; Lu2(Ni5B3)3 Cmce (64) mp-1201139 [hull=0.000, icsd=1, PRIMARY]; Lu2(Ni7B2)3 Fm-3m (225) mp-1193129 [hull=0.000, icsd=1, PRIMARY]; Lu2(NiB2)3 Cmmm (65) mp-8771 [hull=0.000, icsd=1, PRIMARY]; Lu4NiB13 P4/mnc (128) mp-1200891 [hull=0.072, icsd=1, PRIMARY]
- papers: https://doi.org/10.1080/14786430600651962 (Physical properties of Lu1−xYbxNi2B2C)

## B-Mo-Y
- rank 1570 | 3 samples | 1 papers | 3 compositions
- compositions: YMoB4 (1); YMoB3.8C0.2 (1); YMo0.8Fe0.2B4 (1)
- dopant candidates (<5% at.): C (1), Fe (1)
- measured range: 315-1031 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YB4Mo Pbam (55) mp-7691 [hull=0.000, icsd=1, PRIMARY]; YB2Mo Amm2 (38) mp-1215920 [hull=0.098, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2010.05.110 (Applying an electron counting rule to screen prospective thermoelectri...)

## B-N
- rank 1571 | 3 samples | 2 papers | 1 compositions
- compositions: BN (3)
- measured range: 13-295 K (5th-95th pct of 3 curves; full span incl. outliers 13-600 K)
- [ref 1] TEDesignLab / ICSD: BN P6_3mc (186) mp-2653 [hull=0.093, icsd=7]
- [ref 2] MP, ranked by ICSD evidence: BN F-43m (216) mp-1639 [hull=0.076, icsd=20, PRIMARY]; B13N2 R-3m (166) mp-534 [hull=0.138, icsd=1, PRIMARY]; B9N I4/mmm (139) mp-1079812 [hull=2.544, icsd=1, PRIMARY]; B24N4O Pna2_1 (33) mp-1182541 [hull=0.481, PRIMARY]; BN P6_3/mmc (194) mp-7991 [hull=0.000, icsd=11]
- papers: https://doi.org/10.1016/0022-3697(73)90092-9 (Nonmetallic crystals with high thermal conductivity) | https://doi.org/10.1126/science.aat5522 (Experimental observation of high thermal conductivity in boron arsenide)

## B-N-Si-Ti
- rank 1572 | 3 samples | 1 papers | 3 compositions
- compositions: (TiB2)8Si3N4 (1); (TiB2)3Si3N4 (1); (TiB2)4.7Si3N4 (1)
- sample form: Bulk (3)
- measured range: 291-1163 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1016/j.ceramint.2016.02.001 (Fabrication and contact resistivity of W–Si 3 N 4 /TiB 2 –Si 3 N 4 /p–...)

## B-Ni-Yb
- rank 1573 | 3 samples | 1 papers | 3 compositions
- compositions: Lu0.2Yb0.8Ni2B2 (1); Lu0.1Yb0.9Ni2B2 (1); YbNi2B2 (1)
- dopant candidates (<5% at.): Lu (2)
- sample form: SingleCrystal (3)
- measured range: 10-295 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbNiB4 Pbam (55) mp-21181 [hull=0.074, icsd=2, PRIMARY]; Yb2(Ni2B)5 Pbca (61) mp-1204889 [hull=0.008, icsd=1, PRIMARY]; Yb2(Ni7B2)3 Fm-3m (225) mp-1193375 [hull=0.000, icsd=1, PRIMARY]; Yb3Ni13B2 P6/mmm (191) mp-865970 [hull=0.000, icsd=1, PRIMARY]; Yb2(NiB2)3 Cmmm (65) mp-14344 [hull=0.055, icsd=1, PRIMARY]
- papers: https://doi.org/10.1080/14786430600651962 (Physical properties of Lu1−xYbxNi2B2C)

## B-O-Ti-Zn
- rank 1574 | 3 samples | 1 papers | 1 compositions
- compositions: (TiB2)19.46(ZnO)80.54 (3)
- sample form: Bulk (3)
- measured range: 175-852 K (5th-95th pct of 12 curves)
- papers: https://doi.org/10.1109/ict.2002.1190285 (Preparation and thermoelectric properties of ZnO-TiB/sub 2/ composites)

## B-V
- rank 1575 | 3 samples | 2 papers | 3 compositions
- compositions: VB2 (1); V11B89 (1); V32B68 (1)
- measured range: 52-299 K (5th-95th pct of 3 curves; full span incl. outliers 52-1080 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): VB2 P6/mmm (191) mp-1491 [hull=0.000, icsd=17, PRIMARY]; V3B2 P4/mbm (127) mp-2091 [hull=0.000, icsd=4, PRIMARY]; V2B3 Cmcm (63) mp-9208 [hull=0.000, icsd=2, PRIMARY]; VB Cmcm (63) mp-9973 [hull=0.000, icsd=2, PRIMARY]; V5B3 I4/mcm (140) mp-1188836 [hull=0.059, icsd=1, PRIMARY]
- papers: https://doi.org/10.2320/matertrans.m2010272 (Vanadium Concentration Dependence of Thermoelectric Properties of &bet...) | https://doi.org/10.1143/jpsj.80.024709 (Low Critical Concentration of Metal–Insulator Transition of Vanadium D...)

## Ba-Bi-O
- rank 1576 | 3 samples | 1 papers | 3 compositions
- compositions: BaBiO3 (1); BaBi0.9Sb0.1O3 (1); BaBi0.8Sb0.2O3 (1)
- dopant candidates (<5% at.): Sb (2)
- curator composition details (from the paper): The logarithmic values in Fig 10A were converted by making them exponents of 10
original ... (1)
- measured range: 417-971 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaBiO3 C2/m (12) mp-22942 [hull=0.000, icsd=10, PRIMARY]; Ba2Bi2O5 P2_1/c (14) mp-28670 [hull=0.000, icsd=1, PRIMARY]; Ba13Bi11O36 P-1 (2) mp-758120 [hull=0.000, PRIMARY]; Ba10Ce(Bi3O10)3 P-1 (2) mp-1228865 [hull=0.000, PRIMARY]; Ba2Bi6O11 C2/m (12) mp-674537 [hull=0.242, PRIMARY]
- papers: https://doi.org/10.1016/j.ssc.2012.02.025 (Electrical conduction and thermoelectric properties of perovskite-type...)

## Ba-Bi-O-Sb
- rank 1577 | 3 samples | 1 papers | 3 compositions
- compositions: BaBi0.7Sb0.3O3 (1); BaBi0.6Sb0.4O3 (1); BaBi0.5Sb0.5O3 (1)
- measured range: 474-973 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2BiSbO6 R-3 (148) mp-23091 [hull=0.000, icsd=3, PRIMARY]; Ba2BiSbO6 C2/m (12) mp-23127 [hull=0.000, icsd=2]; Ba2BiSbO6 P-1 (2) mp-1182508 [hull=0.966]
- papers: https://doi.org/10.1016/j.ssc.2012.02.025 (Electrical conduction and thermoelectric properties of perovskite-type...)

## Ba-C-Co-O
- rank 1578 | 3 samples | 1 papers | 1 compositions
- compositions: Ba3Co2O6(CO3)0.7 (3)
- curator composition details (from the paper): single crystal (1)
- sample form: Bulk (2)
- measured range: 298-1109 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1063/1.3174428 (Thermoelectric properties of Ba3Co2O6(CO3)0.7 containing one-dimension...)

## Ba-Co-Cu-O-Pr
- rank 1579 | 3 samples | 1 papers | 3 compositions
- compositions: PrBa0.7Ca0.3CoCuO5 (1); PrBa0.9Ca0.1CoCuO5 (1); PrBa0.8Ca0.2CoCuO5 (1)
- dopant candidates (<5% at.): Ca (3)
- measured range: 374-1123 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2PrCoCu2O7 Pmmm (47) mp-1214590 [hull=0.023, PRIMARY]
- papers: https://doi.org/10.1016/j.ceramint.2021.11.310 (Ca-doped PrBa1-Ca CoCuO5+ (x = 0–0.2) as cathode materials for solid o...)

## Ba-Co-Fe-Sb
- rank 1580 | 3 samples | 2 papers | 3 compositions
- compositions: Ba0.9Fe2Co2Sb12 (1); BaFe3Co1Sb12 (1); Ba0.86Fe3CoSb12 (1)
- curator composition details (from the paper): see Fig. 1 (2)
- sample form: Bulk (1)
- measured range: 15-493 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1143/jjap.45.4025 (Effects of Co Substitution on Magnetic and Thermoelectric Properties o...) | https://doi.org/10.1016/j.physb.2006.03.078 (Magnetic and thermoelectric properties of BayFe4−xCoxSb12)

## Ba-Co-Ge
- rank 1581 | 3 samples | 1 papers | 3 compositions
- compositions: Ba8Co3Ge43 (1); Ba6Co2Ge23 (1); Ba6Co5Ge20 (1)
- measured range: 12-302 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba(CoGe)2 I4/mmm (139) mp-1070253 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/s11664-015-4259-6 (Synthesis, Transport and Magnetic Properties of Ba-Co-Ge Clathrates)

## Ba-Co-O-Pr-Sr
- rank 1582 | 3 samples | 2 papers | 3 compositions
- compositions: Pr0.94Ba0.5Sr0.5Co2O5 (1); PrBa0.5Sr0.5Co2O5 (1); PrBa0.46Sr0.5Co2O5 (1)
- measured range: 321-1072 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/j.elecom.2022.107341 (Addressing the origin of highly catalytic activity of A-site Sr-doped ...) | https://doi.org/10.1016/j.jallcom.2021.160759 (Evaluation of A-site Ba-deficient PrBa0.5-Sr0.5Co2O5+ (x = 0, 0.04 and...)

## Ba-Cu-Fe-O-Pr
- rank 1583 | 3 samples | 2 papers | 2 compositions
- compositions: PrBaCuFeO5 (2); La0.25Pr0.75BaCuFeO5 (1)
- dopant candidates (<5% at.): La (1)
- curator composition details (from the paper): La1−xPrxBaCuFeO5+δ (2)
- measured range: 294-1085 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba4Pr4Fe4Cu4O21 I4/mmm (139) mp-1228619 [hull=0.021, PRIMARY]; BaPrFeCuO5 P4mm (99) mp-1206136 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1134/s1063783409020073 (Thermoelectric properties of layered ferrocuprates LnBaCuFeO5 + δ (Ln=...) | https://doi.org/10.1134/s1087659612020058 (Structure and properties of solid solutions of La1 − x Pr x BaCuFeO5 + δ)

## Ba-Cu-Ge-Si-Sn
- rank 1584 | 3 samples | 1 papers | 1 compositions
- compositions: Ba8Cu5Si6Ge32Sn3 (3)
- measured range: 422-824 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1002/pssa.201532642 (Nanostructured clathrates and clathrate-based nanocomposites)

## Ba-Cu-Lu-O
- rank 1585 | 3 samples | 1 papers | 3 compositions
- compositions: LuBa2.0Cu3O7 (1); LuBa1.6Sr0.4Cu3O7 (1); LuBa1.5Sr0.5Cu3O7 (1)
- dopant candidates (<5% at.): Sr (2)
- measured range: 60-289 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2Lu(CuO2)3 P4/mmm (123) mp-21868 [hull=0.022, icsd=2, PRIMARY]; Ba2LuCu3O7 Pmmm (47) mp-20324 [hull=0.037, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0025-5408(92)90147-r (Structure and superconductivity studies on LnBa2−xSrxCu3O7 (Ln=Yb and ...)

## Ba-Cu-O-Tl
- rank 1586 | 3 samples | 1 papers | 1 compositions
- compositions: Tl2Ba2CuO6 (3)
- measured range: 27-286 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2Tl2CuO6 Cmce (64) mp-6027 [hull=0.006, icsd=3, PRIMARY]; Ba2TlCuO5 P4/mmm (123) mp-20942 [hull=0.065, icsd=1, PRIMARY]; Ba2TlCu3O7 Pmmm (47) mp-1147544 [hull=0.065, PRIMARY]; Ba4Tl4Cu2O11 Cm (8) mp-1228311 [hull=0.061, PRIMARY]; Ba2Tl2CuO6 C2/m (12) mp-1228363 [hull=0.011]
- papers: https://doi.org/10.1016/0921-4534(95)00366-5 (Systematic thermopower measurements of the thallium cuprates Tl(Ba,Sr)...)

## Ba-Fe-O-Pr
- rank 1587 | 3 samples | 2 papers | 3 compositions
- compositions: PrBa0.97Fe2O (1); PrBaFe2O5 (1); BaCe0.2Fe0.5Pr0.3O3 (1)
- dopant candidates (<5% at.): Ce (1)
- sample form: rod-shaped (1)
- measured range: 573-1073 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba6Pr2Fe4O15 Cc (9) mp-1228608 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1039/c5ra19555a (Evaluation of Ba-deficient PrBa<sub>1−x</sub>Fe<sub>2</sub>O<sub>5+δ</...) | https://doi.org/10.1016/j.jpowsour.2021.229776 (Enhanced oxygen reduction reaction activity of BaCe0.2Fe0.8O3-δ cathod...)

## Ba-Ga-Ge-In
- rank 1588 | 3 samples | 1 papers | 3 compositions
- compositions: Ba8Ga13In3Ge30 (1); Ba8Ga7In9Ge30 (1); Ba8Ga10In6Ge30 (1)
- sample form: Bulk (3)
- measured range: 323-949 K (5th-95th pct of 12 curves)
- papers: https://doi.org/10.1063/1.2743815 (Effect of In additions on the thermoelectric properties of the type-I ...)

## Ba-Ge-In
- rank 1589 | 3 samples | 2 papers | 3 compositions
- compositions: Ba24In12Ge88 (1); Ba8In16Ge30 (1); Ba6Ge21.93In3.07 (1)
- sample form: Bulk (2)
- measured range: 83-925 K (5th-95th pct of 12 curves; full span incl. outliers 83-972 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaInGe P3m1 (156) mp-1227944 [hull=0.041, PRIMARY]
- papers: https://doi.org/10.1063/1.2803745 (Crystal structure and thermoelectric properties of type-III clathrate ...) | https://doi.org/10.1006/jssc.2000.8777 (Structure and Thermoelectric Properties of Ba6Ge25−x, Ba6Ge23Sn2, and ...)

## Ba-Mn-Sb
- rank 1590 | 3 samples | 2 papers | 1 compositions
- compositions: BaMn2Sb2 (3)
- sample form: SingleCrystal (2); Bulk (1)
- measured range: 297-778 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaMnSb2 I4/mmm (139) mp-29206 [hull=0.089, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2008.10.080 (Synthesis and thermoelectric properties of BaMn2Sb2 single crystals) | https://doi.org/10.1007/s10854-012-0820-8 (Preparation and thermoelectric properties of BaMn2−xZnxSb2 zintl compo...)

## Ba-Mn-Sb-Zn
- rank 1591 | 3 samples | 1 papers | 3 compositions
- compositions: BaMn1.3Zn0.7Sb2 (1); BaMn1.7Zn0.3Sb2 (1); BaMn1.5Zn0.5Sb2 (1)
- sample form: Bulk (3)
- measured range: 298-725 K (5th-95th pct of 9 curves)
- papers: https://doi.org/10.1007/s10854-012-0820-8 (Preparation and thermoelectric properties of BaMn2−xZnxSb2 zintl compo...)

## Ba-Nd-O
- rank 1592 | 3 samples | 1 papers | 3 compositions
- compositions: NdBa2(Cu0.06Zn0.04)3O7 (1); NdBa2(Cu0.08Zn0.02)3O7 (1); NdBa2(Cu0.02Zn0.08)3O7 (1)
- dopant candidates (<5% at.): Cu (3), Zn (3)
- sample form: Bulk (3)
- measured range: 11-118 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaNd2O4 Pnma (62) mp-2892 [hull=0.000, icsd=5, PRIMARY]; BaNdO3 R-3c (167) mp-754307 [hull=0.111, PRIMARY]; BaNdO3 Pm-3m (221) mp-755877 [hull=0.174]
- papers: https://doi.org/10.1016/s0921-4534(97)00687-4 (Electrical resistivity and thermal conductivity of NdBa2(Cu1−ZZnZ)3O7−...)

## Bi-C-Sb
- rank 1593 | 3 samples | 1 papers | 2 compositions
- compositions: Bi0.85Sb0.15C0.08 (2); Bi0.85Sb0.15C0.12 (1)
- sample form: Bulk (3)
- measured range: 149-361 K (5th-95th pct of 18 curves)
- papers: https://doi.org/10.1016/j.jallcom.2021.161399 (Unraveling the thermoelectric performance of Bismuth Antimony/graphene...)

## Bi-C-Sb-Si-Te
- rank 1594 | 3 samples | 2 papers | 2 compositions
- compositions: (Bi0.26Sb0.74)2Te3(SiC)0.9 (2); (Bi0.5Sb1.5Te3)70.9(SiC)29.1 (1)
- sample form: Bulk (1)
- measured range: 304-524 K (5th-95th pct of 7 curves)
- papers: https://doi.org/10.1007/s11664-010-1476-x (Effects of SiC Nanodispersion on the Thermoelectric Properties of p-Ty...) | https://doi.org/10.1002/pssa.201532614 (From thermoelectric bulk to nanomaterials: Current progress for Bi2Te3...)

## Bi-Cu-O-Pb-Sr
- rank 1595 | 3 samples | 2 papers | 3 compositions
- compositions: PbBiSr2Cu3O8 (1); (Bi1.35Pb0.85)(Sr1.47La0.38)CuO6 (1); (Bi1.35Pb0.85)(Sr1.40La0.45)CuO6 (1)
- dopant candidates (<5% at.): La (2)
- sample form: Bulk (1)
- measured range: 73-390 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr4CaYCu4Bi2(PbO8)2 P2/c (13) mp-1218870 [hull=0.016, PRIMARY]
- papers: https://doi.org/10.1016/0038-1098(91)90232-k (Thermoelectric study of PbxBi2-xSr2Ca2Cu3Oy superconductors) | https://doi.org/10.1103/physrevb.72.024533 (Contribution of electronic structure to thermoelectric power in(Bi,Pb)...)

## Bi-Cu-Si
- rank 1596 | 3 samples | 1 papers | 3 compositions
- compositions: Bi8Cu4.8Si41.2 (1); Bi8Cu4.8Si41.2(SiC)2.42 (1); Bi8Cu4.8Si41.2(SiC)0.79 (1)
- dopant candidates (<5% at.): C (2)
- measured range: 422-773 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1002/pssa.201532642 (Nanostructured clathrates and clathrate-based nanocomposites)

## Bi-Eu-Mg
- rank 1597 | 3 samples | 1 papers | 2 compositions
- compositions: EuMg2 Bi2 (2); EuMg2Bi2 (1)
- sample form: Bulk (3)
- measured range: 10-600 K (5th-95th pct of 19 curves)
- papers: https://doi.org/10.1103/physrevb.85.035202 (Thermoelectric transport properties of CaMg2Bi2, EuMg2Bi2, and YbMg2Bi2)

## Bi-Fe-La-O
- rank 1598 | 3 samples | 1 papers | 3 compositions
- compositions: La0.5Bi0.3Sr0.2FeO3 (1); La0.4Bi0.4Sr0.2FeO3 (1); La0.3Bi0.5Sr0.2FeO3 (1)
- dopant candidates (<5% at.): Sr (3)
- sample form: rod-shaped (3)
- measured range: 823-1073 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaFe4(BiO4)3 Pm (6) mp-1222983 [hull=0.029, PRIMARY]; LaFe5Bi4O15 P1 (1) mp-1223162 [hull=0.027, PRIMARY]
- papers: https://doi.org/10.1021/am5017045 (Bismuth Doped Lanthanum Ferrite Perovskites as Novel Cathodes for Inte...)

## Bi-Ga-In-Te
- rank 1599 | 3 samples | 1 papers | 3 compositions
- compositions: (Bi)20.45(In)21.98(Ga)9.93(Te)47.64 (1); (Bi)17.83(In)28(Ga)12.61(Te)41.55 (1); (Bi)23.26(In)15.42(Ga)7.05(Te)54.27 (1)
- sample form: Film (3)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 288-368 K (5th-95th pct of 15 curves)
- papers: https://doi.org/10.1016/j.energy.2017.12.063 (Ternary Bi2Te3In2Te3Ga2Te3 (n-type) thermoelectric film on a flexible ...)

## Bi-Gd
- rank 1600 | 3 samples | 1 papers | 1 compositions
- compositions: GdBi (3)
- measured range: 13-47 K (5th-95th pct of 3 curves; full span incl. outliers 13-97 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdBi Fm-3m (225) mp-614481 [hull=0.000, icsd=3, PRIMARY]; GdBi3 P6_3/mmc (194) mp-1184501 [hull=0.066, PRIMARY, AMBIGUOUS]; GdBi3 I4/mmm (139) mp-1184536 [hull=0.072]
- papers: https://doi.org/10.1103/physrevb.97.081108 (Extreme magnetoresistance in magnetic rare-earth monopnictides)
