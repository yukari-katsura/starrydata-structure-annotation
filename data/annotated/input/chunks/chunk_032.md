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
- papers: Anomalously low thermal conductivity and thermoelectric properties of new cationic clathrates in the Sn-In-As-I system | Synthesis, Crystal Structure, and Thermoelectric Properties of Clathrates in the Sn-In-As-I System

## As-In-P
- rank 1552 | 3 samples | 1 papers | 3 compositions
- compositions: InAs0.8P0.2 (1); InAs0.9P0.1 (1); InAs0.6P0.4 (1)
- measured range: 291-1064 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): In2AsP R3m (160) mp-1223837 [hull=0.013, PRIMARY, AMBIGUOUS]; In4As3P Pmm2 (25) mp-1223887 [hull=0.018, PRIMARY]; In4AsP3 Amm2 (38) mp-1223884 [hull=0.013, PRIMARY]; In2AsP P-4m2 (115) mp-1223851 [hull=0.015]
- papers: InAs1‐xPx as a Thermoelectric Material

## As-Na-O-Ti
- rank 1553 | 3 samples | 1 papers | 1 compositions
- compositions: Na2Ti2As2O (3)
- measured range: 10-301 K (5th-95th pct of 3 curves; full span incl. outliers 10-348 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NaTi2(AsO4)3 R-3c (167) mp-1200852 [hull=0.000, icsd=1, PRIMARY]; NaTiAsO5 P2_1/c (14) mp-1201259 [hull=0.000, icsd=1, PRIMARY]; Na2Ti2As2O I4/mmm (139) mp-1025360 [hull=0.000, PRIMARY]
- papers: Physical properties of the layered pnictide oxidesNa2Ti2P2O(P=As,Sb)

## As-Pt
- rank 1554 | 3 samples | 1 papers | 3 compositions
- compositions: PtAs2 (1); Pt0.99Rh0.01As2 (1); Pt0.995Rh0.005As2 (1)
- dopant candidates (<5% at.): Rh (2)
- measured range: 11-599 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): As2Pt Pa-3 (205) mp-2513 [hull=0.000, icsd=8, PRIMARY]; AsPt3 P6_3/mmc (194) mp-1183320 [hull=0.232, PRIMARY, AMBIGUOUS]; AsPt3 Pm-3m (221) mp-1183186 [hull=0.234]
- papers: Enhancing high-temperature thermoelectric properties of PtAs2 by Rh doping

## As-Sb-Se-Te-Tl
- rank 1555 | 3 samples | 1 papers | 3 compositions
- compositions: As17.65Sb11.76Se8.82Te44.12Tl17.65 (1); As15.38Sb15.38Se7.69Te46.15Tl15.38 (1); As11.11Sb22.22Se5.56Te50Tl11.11 (1)
- measured range: 103-335 K (5th-95th pct of 3 curves)
- papers: Thermoelectric Properties of Diphasal Systems Combining As2Te3 and Tl2Se with Sb2Te3, Bi2Te3, or Sb2Se3

## As-Se-Th
- rank 1556 | 3 samples | 1 papers | 2 compositions
- compositions: ThAsSe (2); ThAs0.67Se0.33 (1)
- measured range: 12-316 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ThAsSe P4/nmm (129) mp-1019357 [hull=0.000, icsd=1, PRIMARY]; Th2AsSe2 P4/mmm (123) mp-1207178 [hull=1.887, PRIMARY]
- papers: Thermoelectric power in off-stoichiometric ThAsSe system

## B-Be
- rank 1557 | 3 samples | 1 papers | 3 compositions
- compositions: Be2B (1); Be4B (1); BeB6 (1)
- measured range: 323-1297 K (5th-95th pct of 3 curves; full span incl. outliers 323-1785 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Be2B Fm-3m (225) mp-1432 [hull=0.054, icsd=3, PRIMARY]; BeB2 P6/mmm (191) mp-1009823 [hull=0.126, icsd=2, PRIMARY]; Be4B P4/nmm (129) mp-27757 [hull=0.000, icsd=1, PRIMARY]; Be4B25 P2/c (13) mp-1227634 [hull=0.213, PRIMARY]
- papers: Thermal Diffusivity of Be4B, Be2B, and BeB6

## B-C-Hf
- rank 1558 | 3 samples | 1 papers | 3 compositions
- compositions: (B4C)50(HfB2)50 (1); (B4C)65(HfB2)35 (1); (B4C)70(HfB2)30 (1)
- measured range: 296-972 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HfBC P6_3/mmc (194) mp-1232375 [hull=0.550, PRIMARY]
- papers: Effect of microstructure on mechanical, electrical and thermal properties of B4C-HfB2 composites prepared by arc melting

## B-C-Ho-N
- rank 1559 | 3 samples | 3 papers | 1 compositions
- compositions: HoB17CN (3)
- measured range: 301-1038 K (5th-95th pct of 4 curves)
- papers: Thermoelectric properties of homologous p- and n-type boron-rich borides | Homologous rare earth boron cluster compounds: a possible n-type counterpart to boron carbide | Doping effect in N-type rare earth boron carbonitrides

## B-C-O-Y
- rank 1560 | 3 samples | 1 papers | 1 compositions
- compositions: YBCO (3)
- measured range: 30-140 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YBCO7 Pbca (61) mp-1197370 [hull=0.560, icsd=1, PRIMARY]
- papers: Interaction of carriers with phonons in single- and poly-crystalline high Tc superconductors estimated from phonon thermal conductivity

## B-C-Ti
- rank 1561 | 3 samples | 2 papers | 3 compositions
- compositions: (TiB2)73.61(SiC)11.27(C)15.12 (1); (TiB2)0.1(C)0.9 (1); (TiB2)0.2(C)0.8 (1)
- dopant candidates (<5% at.): Si (1)
- measured range: 298-1016 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiBC P6_3/mmc (194) mp-1232377 [hull=0.307, PRIMARY]
- papers: Microstructures and properties of silicon carbide- and graphene nanoplatelet-reinforced titanium diboride composites | Thermal transport in CKC TiB2-doped graphite

## B-Ca-Fe-O
- rank 1562 | 3 samples | 1 papers | 3 compositions
- compositions: (CaO)30(B2O3)56(Fe2O3)14 (1); (CaO)30(B2O3)47(Fe2O3)23 (1); (CaO)30(B2O3)54(Fe2O3)16 (1)
- measured range: 418-501 K (5th-95th pct of 3 curves)
- papers: Electronic properties of calcium borate glasses containing iron oxide

## B-Ce-Pd
- rank 1563 | 3 samples | 1 papers | 3 compositions
- compositions: CePd3B0.25 (1); CePd3B0.3 (1); CePd3B0.4 (1)
- measured range: 13-297 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeBPd3 Pm-3m (221) mp-19948 [hull=0.213, icsd=2, PRIMARY]; Ce2BPd6 P4/mmm (123) mp-1226779 [hull=0.117, PRIMARY]
- papers: Study of the thermoelectric properties of

## B-Co-Na-O
- rank 1564 | 3 samples | 1 papers | 3 compositions
- compositions: Na0.7Co0.75B0.25O2 (1); Na0.7Co0.625B0.375O2 (1); Na0.7Co0.25B0.75O2 (1)
- measured range: 15-300 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Na2Co2(B4O7)3 C2/c (15) mp-704577 [hull=0.012, icsd=1, PRIMARY]; Na3Co(BO3)2 P2_1/c (14) mp-773604 [hull=0.059, PRIMARY]; Na6Co2B4SO16 Fd-3 (203) mp-851008 [hull=0.067, PRIMARY]; NaCoBO3 C2/c (15) mp-1101692 [hull=0.049, PRIMARY]
- papers: Magnetic and thermoelectric properties of B-substituted NaCoO2

## B-Cr-Y
- rank 1565 | 3 samples | 2 papers | 3 compositions
- compositions: YCrB4 (1); Y0.95Ce0.05CrB6 (1); YCrB6 (1)
- dopant candidates (<5% at.): Ce (1)
- measured range: 10-1002 K (5th-95th pct of 8 curves; full span incl. outliers 10-1073 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YCrB4 Pbam (55) mp-20450 [hull=0.000, icsd=1, PRIMARY]
- papers: Applying an electron counting rule to screen prospective thermoelectric alloys: The thermoelectric properties of YCrB4 and Er3CrB7-type phases | Thermoelectricity and electronic properties of<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:mrow><mml:msub><mml:mi mathvariant=\"normal\">Y</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mo>−</mml:mo><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Ce</mml:mi><mml:mi>x</mml:mi></mml:msub><mml:msub><mml:mi>CrB</mml:mi><mml:mn>4</mml:mn></mml:msub></mml:mrow></mml:math>

## B-Er
- rank 1566 | 3 samples | 3 papers | 2 compositions
- compositions: ErB12 (2); Er1.12B17.64CN (1)
- dopant candidates (<5% at.): C (1), N (1)
- measured range: 11-1037 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ErB4 P4/mbm (127) mp-2847 [hull=0.000, icsd=5, PRIMARY]; ErB6 Pm-3m (221) mp-1296 [hull=0.054, icsd=4, PRIMARY]; ErB2 P6/mmm (191) mp-1774 [hull=0.000, icsd=3, PRIMARY]; ErB12 Fm-3m (225) mp-1104598 [hull=0.000, icsd=1, PRIMARY]; Ca(Er2B15)2 P4/mmm (123) mp-1227415 [hull=0.051, PRIMARY]
- papers: Doping effect in N-type rare earth boron carbonitrides | Transition and rare earth element dodecaborides | Thermal conductivity of metal dodecaborides with a UB12 structure

## B-Fe-Ni-P
- rank 1567 | 3 samples | 2 papers | 1 compositions
- compositions: Fe40Ni40P14B6 (3)
- measured range: 20-508 K (5th-95th pct of 4 curves)
- papers: Thermoelectric power in some ferromagnetic Fe based amorphous alloys | Transport properties of Fe-Ni Glasses

## B-Fe-O
- rank 1568 | 3 samples | 2 papers | 1 compositions
- compositions: Fe2OBO3 (3)
- measured range: 163-649 K (5th-95th pct of 3 curves; full span incl. outliers 163-794 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe3B7IO13 R3c (161) mp-1194881 [hull=0.000, icsd=2, PRIMARY]; Fe2B2O5 P-1 (2) mp-19333 [hull=0.000, icsd=2, PRIMARY]; Fe3BO6 Pnma (62) mp-25746 [hull=0.025, icsd=2, PRIMARY]; FeBO3 R-3c (167) mp-19097 [hull=0.000, icsd=1, PRIMARY]; Fe5(BO3)6 Pmmn (59) mp-1198168 [hull=0.113, icsd=1, PRIMARY]
- papers: Role of t2gversus egInteractions in the Physical Properties of A2OBO3(A = Mn, Fe) | Electrical transport in charge-orderedFe2OBO3: Resistive switching and pressure effects

## B-Lu-Ni
- rank 1569 | 3 samples | 1 papers | 3 compositions
- compositions: LuNi2B2 (1); Lu0.925Yb0.075Ni2B2 (1); Lu0.8Yb0.2Ni2B2 (1)
- dopant candidates (<5% at.): Yb (2)
- measured range: 10-296 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Lu3Ni7B2 P6_3/mmc (194) mp-865190 [hull=0.000, icsd=2, PRIMARY]; Lu2(Ni5B3)3 Cmce (64) mp-1201139 [hull=0.000, icsd=1, PRIMARY]; Lu2(Ni7B2)3 Fm-3m (225) mp-1193129 [hull=0.000, icsd=1, PRIMARY]; Lu2(NiB2)3 Cmmm (65) mp-8771 [hull=0.000, icsd=1, PRIMARY]; Lu4NiB13 P4/mnc (128) mp-1200891 [hull=0.072, icsd=1, PRIMARY]
- papers: Physical properties of Lu1−xYbxNi2B2C

## B-Mo-Y
- rank 1570 | 3 samples | 1 papers | 3 compositions
- compositions: YMoB4 (1); YMoB3.8C0.2 (1); YMo0.8Fe0.2B4 (1)
- dopant candidates (<5% at.): C (1), Fe (1)
- measured range: 315-1031 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YB4Mo Pbam (55) mp-7691 [hull=0.000, icsd=1, PRIMARY]; YB2Mo Amm2 (38) mp-1215920 [hull=0.098, PRIMARY]
- papers: Applying an electron counting rule to screen prospective thermoelectric alloys: The thermoelectric properties of YCrB4 and Er3CrB7-type phases

## B-N
- rank 1571 | 3 samples | 2 papers | 1 compositions
- compositions: BN (3)
- measured range: 13-295 K (5th-95th pct of 3 curves; full span incl. outliers 13-600 K)
- [ref 1] TEDesignLab / ICSD: BN P6_3mc (186) mp-2653 [hull=0.093, icsd=7]
- [ref 2] MP, ranked by ICSD evidence: BN F-43m (216) mp-1639 [hull=0.076, icsd=20, PRIMARY]; B13N2 R-3m (166) mp-534 [hull=0.138, icsd=1, PRIMARY]; B9N I4/mmm (139) mp-1079812 [hull=2.544, icsd=1, PRIMARY]; B24N4O Pna2_1 (33) mp-1182541 [hull=0.481, PRIMARY]; BN P6_3/mmc (194) mp-7991 [hull=0.000, icsd=11]
- papers: Nonmetallic crystals with high thermal conductivity | Experimental observation of high thermal conductivity in boron arsenide

## B-N-Si-Ti
- rank 1572 | 3 samples | 1 papers | 3 compositions
- compositions: (TiB2)8Si3N4 (1); (TiB2)3Si3N4 (1); (TiB2)4.7Si3N4 (1)
- measured range: 291-1163 K (5th-95th pct of 6 curves)
- papers: Fabrication and contact resistivity of W–Si 3 N 4 /TiB 2 –Si 3 N 4 /p–SiGe thermoelectric joints

## B-Ni-Yb
- rank 1573 | 3 samples | 1 papers | 3 compositions
- compositions: Lu0.2Yb0.8Ni2B2 (1); Lu0.1Yb0.9Ni2B2 (1); YbNi2B2 (1)
- dopant candidates (<5% at.): Lu (2)
- measured range: 10-295 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbNiB4 Pbam (55) mp-21181 [hull=0.074, icsd=2, PRIMARY]; Yb2(Ni2B)5 Pbca (61) mp-1204889 [hull=0.008, icsd=1, PRIMARY]; Yb2(Ni7B2)3 Fm-3m (225) mp-1193375 [hull=0.000, icsd=1, PRIMARY]; Yb3Ni13B2 P6/mmm (191) mp-865970 [hull=0.000, icsd=1, PRIMARY]; Yb2(NiB2)3 Cmmm (65) mp-14344 [hull=0.055, icsd=1, PRIMARY]
- papers: Physical properties of Lu1−xYbxNi2B2C

## B-O-Ti-Zn
- rank 1574 | 3 samples | 1 papers | 1 compositions
- compositions: (TiB2)19.46(ZnO)80.54 (3)
- measured range: 175-852 K (5th-95th pct of 12 curves)
- papers: Preparation and thermoelectric properties of ZnO-TiB/sub 2/ composites

## B-V
- rank 1575 | 3 samples | 2 papers | 3 compositions
- compositions: VB2 (1); V11B89 (1); V32B68 (1)
- measured range: 52-299 K (5th-95th pct of 3 curves; full span incl. outliers 52-1080 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): VB2 P6/mmm (191) mp-1491 [hull=0.000, icsd=17, PRIMARY]; V3B2 P4/mbm (127) mp-2091 [hull=0.000, icsd=4, PRIMARY]; V2B3 Cmcm (63) mp-9208 [hull=0.000, icsd=2, PRIMARY]; VB Cmcm (63) mp-9973 [hull=0.000, icsd=2, PRIMARY]; V5B3 I4/mcm (140) mp-1188836 [hull=0.059, icsd=1, PRIMARY]
- papers: Vanadium Concentration Dependence of Thermoelectric Properties of &beta;-Rhombohedral Boron Prepared by Spark Plasma Sintering | Low Critical Concentration of Metal–Insulator Transition of Vanadium Doped Amorphous Boron

## Ba-Bi-O
- rank 1576 | 3 samples | 1 papers | 3 compositions
- compositions: BaBiO3 (1); BaBi0.9Sb0.1O3 (1); BaBi0.8Sb0.2O3 (1)
- dopant candidates (<5% at.): Sb (2)
- measured range: 417-971 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaBiO3 C2/m (12) mp-22942 [hull=0.000, icsd=10, PRIMARY]; Ba2Bi2O5 P2_1/c (14) mp-28670 [hull=0.000, icsd=1, PRIMARY]; Ba13Bi11O36 P-1 (2) mp-758120 [hull=0.000, PRIMARY]; Ba10Ce(Bi3O10)3 P-1 (2) mp-1228865 [hull=0.000, PRIMARY]; Ba2Bi6O11 C2/m (12) mp-674537 [hull=0.242, PRIMARY]
- papers: Electrical conduction and thermoelectric properties of perovskite-type BaBi1−xSbxO3

## Ba-Bi-O-Sb
- rank 1577 | 3 samples | 1 papers | 3 compositions
- compositions: BaBi0.7Sb0.3O3 (1); BaBi0.6Sb0.4O3 (1); BaBi0.5Sb0.5O3 (1)
- measured range: 474-973 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2BiSbO6 R-3 (148) mp-23091 [hull=0.000, icsd=3, PRIMARY]; Ba2BiSbO6 C2/m (12) mp-23127 [hull=0.000, icsd=2]; Ba2BiSbO6 P-1 (2) mp-1182508 [hull=0.966]
- papers: Electrical conduction and thermoelectric properties of perovskite-type BaBi1−xSbxO3

## Ba-C-Co-O
- rank 1578 | 3 samples | 1 papers | 1 compositions
- compositions: Ba3Co2O6(CO3)0.7 (3)
- measured range: 298-1109 K (5th-95th pct of 5 curves)
- papers: Thermoelectric properties of Ba3Co2O6(CO3)0.7 containing one-dimensional CoO6 octahedral columns

## Ba-Co-Cu-O-Pr
- rank 1579 | 3 samples | 1 papers | 3 compositions
- compositions: PrBa0.7Ca0.3CoCuO5 (1); PrBa0.9Ca0.1CoCuO5 (1); PrBa0.8Ca0.2CoCuO5 (1)
- dopant candidates (<5% at.): Ca (3)
- measured range: 374-1123 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2PrCoCu2O7 Pmmm (47) mp-1214590 [hull=0.023, PRIMARY]
- papers: Ca-doped PrBa1-Ca CoCuO5+ (x = 0–0.2) as cathode materials for solid oxide fuel cells

## Ba-Co-Fe-Sb
- rank 1580 | 3 samples | 2 papers | 3 compositions
- compositions: Ba0.9Fe2Co2Sb12 (1); BaFe3Co1Sb12 (1); Ba0.86Fe3CoSb12 (1)
- measured range: 15-493 K (5th-95th pct of 5 curves)
- papers: Effects of Co Substitution on Magnetic and Thermoelectric Properties of BaFe4Sb12 | Magnetic and thermoelectric properties of BayFe4−xCoxSb12

## Ba-Co-Ge
- rank 1581 | 3 samples | 1 papers | 3 compositions
- compositions: Ba8Co3Ge43 (1); Ba6Co2Ge23 (1); Ba6Co5Ge20 (1)
- measured range: 12-302 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba(CoGe)2 I4/mmm (139) mp-1070253 [hull=0.000, icsd=1, PRIMARY]
- papers: Synthesis, Transport and Magnetic Properties of Ba-Co-Ge Clathrates

## Ba-Co-O-Pr-Sr
- rank 1582 | 3 samples | 2 papers | 3 compositions
- compositions: Pr0.94Ba0.5Sr0.5Co2O5 (1); PrBa0.5Sr0.5Co2O5 (1); PrBa0.46Sr0.5Co2O5 (1)
- measured range: 321-1072 K (5th-95th pct of 3 curves)
- papers: Addressing the origin of highly catalytic activity of A-site Sr-doped perovskite cathodes for intermediate-temperature solid oxide fuel cells | Evaluation of A-site Ba-deficient PrBa0.5-Sr0.5Co2O5+ (x = 0, 0.04 and 0.08) as cathode materials for solid oxide fuel cells

## Ba-Cu-Fe-O-Pr
- rank 1583 | 3 samples | 2 papers | 2 compositions
- compositions: PrBaCuFeO5 (2); La0.25Pr0.75BaCuFeO5 (1)
- dopant candidates (<5% at.): La (1)
- measured range: 294-1085 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba4Pr4Fe4Cu4O21 I4/mmm (139) mp-1228619 [hull=0.021, PRIMARY]; BaPrFeCuO5 P4mm (99) mp-1206136 [hull=0.000, PRIMARY]
- papers: Thermoelectric properties of layered ferrocuprates LnBaCuFeO5 + δ (Ln= La, Pr, Nd, Sm, Gd-Lu) | Structure and properties of solid solutions of La1 − x Pr x BaCuFeO5 + δ

## Ba-Cu-Ge-Si-Sn
- rank 1584 | 3 samples | 1 papers | 1 compositions
- compositions: Ba8Cu5Si6Ge32Sn3 (3)
- measured range: 422-824 K (5th-95th pct of 3 curves)
- papers: Nanostructured clathrates and clathrate-based nanocomposites

## Ba-Cu-Lu-O
- rank 1585 | 3 samples | 1 papers | 3 compositions
- compositions: LuBa2.0Cu3O7 (1); LuBa1.6Sr0.4Cu3O7 (1); LuBa1.5Sr0.5Cu3O7 (1)
- dopant candidates (<5% at.): Sr (2)
- measured range: 60-289 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2Lu(CuO2)3 P4/mmm (123) mp-21868 [hull=0.022, icsd=2, PRIMARY]; Ba2LuCu3O7 Pmmm (47) mp-20324 [hull=0.037, icsd=1, PRIMARY]
- papers: Structure and superconductivity studies on LnBa2−xSrxCu3O7 (Ln=Yb and Lu; 0.0≤x≤0.5)

## Ba-Cu-O-Tl
- rank 1586 | 3 samples | 1 papers | 1 compositions
- compositions: Tl2Ba2CuO6 (3)
- measured range: 27-286 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2Tl2CuO6 Cmce (64) mp-6027 [hull=0.006, icsd=3, PRIMARY]; Ba2TlCuO5 P4/mmm (123) mp-20942 [hull=0.065, icsd=1, PRIMARY]; Ba2TlCu3O7 Pmmm (47) mp-1147544 [hull=0.065, PRIMARY]; Ba4Tl4Cu2O11 Cm (8) mp-1228311 [hull=0.061, PRIMARY]; Ba2Tl2CuO6 C2/m (12) mp-1228363 [hull=0.011]
- papers: Systematic thermopower measurements of the thallium cuprates Tl(Ba,Sr)2Cam−1CumO2m+3−δ and Tl2Ba2Cam−1CumO2m+4+δ

## Ba-Fe-O-Pr
- rank 1587 | 3 samples | 2 papers | 3 compositions
- compositions: PrBa0.97Fe2O (1); PrBaFe2O5 (1); BaCe0.2Fe0.5Pr0.3O3 (1)
- dopant candidates (<5% at.): Ce (1)
- measured range: 573-1073 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba6Pr2Fe4O15 Cc (9) mp-1228608 [hull=0.000, PRIMARY]
- papers: Evaluation of Ba-deficient PrBa<sub>1−x</sub>Fe<sub>2</sub>O<sub>5+δ</sub> oxides as cathode materials for intermediate-temperature solid oxide fuel cells | Enhanced oxygen reduction reaction activity of BaCe0.2Fe0.8O3-δ cathode for proton-conducting solid oxide fuel cells via Pr-doping

## Ba-Ga-Ge-In
- rank 1588 | 3 samples | 1 papers | 3 compositions
- compositions: Ba8Ga13In3Ge30 (1); Ba8Ga7In9Ge30 (1); Ba8Ga10In6Ge30 (1)
- measured range: 323-949 K (5th-95th pct of 12 curves)
- papers: Effect of In additions on the thermoelectric properties of the type-I clathrate compound Ba8Ga16Ge30

## Ba-Ge-In
- rank 1589 | 3 samples | 2 papers | 3 compositions
- compositions: Ba24In12Ge88 (1); Ba8In16Ge30 (1); Ba6Ge21.93In3.07 (1)
- measured range: 83-925 K (5th-95th pct of 12 curves; full span incl. outliers 83-972 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaInGe P3m1 (156) mp-1227944 [hull=0.041, PRIMARY]
- papers: Crystal structure and thermoelectric properties of type-III clathrate compounds in the Ba–In–Ge system | Structure and Thermoelectric Properties of Ba6Ge25−x, Ba6Ge23Sn2, and Ba6Ge22In3: Zintl Phases with a Chiral Clathrate Structure

## Ba-Mn-Sb
- rank 1590 | 3 samples | 2 papers | 1 compositions
- compositions: BaMn2Sb2 (3)
- measured range: 297-778 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaMnSb2 I4/mmm (139) mp-29206 [hull=0.089, icsd=1, PRIMARY]
- papers: Synthesis and thermoelectric properties of BaMn2Sb2 single crystals | Preparation and thermoelectric properties of BaMn2−xZnxSb2 zintl compounds

## Ba-Mn-Sb-Zn
- rank 1591 | 3 samples | 1 papers | 3 compositions
- compositions: BaMn1.3Zn0.7Sb2 (1); BaMn1.7Zn0.3Sb2 (1); BaMn1.5Zn0.5Sb2 (1)
- measured range: 298-725 K (5th-95th pct of 9 curves)
- papers: Preparation and thermoelectric properties of BaMn2−xZnxSb2 zintl compounds

## Ba-Nd-O
- rank 1592 | 3 samples | 1 papers | 3 compositions
- compositions: NdBa2(Cu0.06Zn0.04)3O7 (1); NdBa2(Cu0.08Zn0.02)3O7 (1); NdBa2(Cu0.02Zn0.08)3O7 (1)
- dopant candidates (<5% at.): Cu (3), Zn (3)
- measured range: 11-118 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaNd2O4 Pnma (62) mp-2892 [hull=0.000, icsd=5, PRIMARY]; BaNdO3 R-3c (167) mp-754307 [hull=0.111, PRIMARY]; BaNdO3 Pm-3m (221) mp-755877 [hull=0.174]
- papers: Electrical resistivity and thermal conductivity of NdBa2(Cu1−ZZnZ)3O7−Y and the phonon transport model

## Bi-C-Sb
- rank 1593 | 3 samples | 1 papers | 2 compositions
- compositions: Bi0.85Sb0.15C0.08 (2); Bi0.85Sb0.15C0.12 (1)
- measured range: 149-361 K (5th-95th pct of 18 curves)
- papers: Unraveling the thermoelectric performance of Bismuth Antimony/graphene nanocomposite synthesized by spark plasma extrusion

## Bi-C-Sb-Si-Te
- rank 1594 | 3 samples | 2 papers | 2 compositions
- compositions: (Bi0.26Sb0.74)2Te3(SiC)0.9 (2); (Bi0.5Sb1.5Te3)70.9(SiC)29.1 (1)
- measured range: 304-524 K (5th-95th pct of 7 curves)
- papers: Effects of SiC Nanodispersion on the Thermoelectric Properties of p-Type and n-Type Bi2Te3-Based Alloys | From thermoelectric bulk to nanomaterials: Current progress for Bi2Te3and CoSb3

## Bi-Cu-O-Pb-Sr
- rank 1595 | 3 samples | 2 papers | 3 compositions
- compositions: PbBiSr2Cu3O8 (1); (Bi1.35Pb0.85)(Sr1.47La0.38)CuO6 (1); (Bi1.35Pb0.85)(Sr1.40La0.45)CuO6 (1)
- dopant candidates (<5% at.): La (2)
- measured range: 73-390 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr4CaYCu4Bi2(PbO8)2 P2/c (13) mp-1218870 [hull=0.016, PRIMARY]
- papers: Thermoelectric study of PbxBi2-xSr2Ca2Cu3Oy superconductors | Contribution of electronic structure to thermoelectric power in(Bi,Pb)2(Sr,La)2CuO6+δ

## Bi-Cu-Si
- rank 1596 | 3 samples | 1 papers | 3 compositions
- compositions: Bi8Cu4.8Si41.2 (1); Bi8Cu4.8Si41.2(SiC)2.42 (1); Bi8Cu4.8Si41.2(SiC)0.79 (1)
- dopant candidates (<5% at.): C (2)
- measured range: 422-773 K (5th-95th pct of 3 curves)
- papers: Nanostructured clathrates and clathrate-based nanocomposites

## Bi-Eu-Mg
- rank 1597 | 3 samples | 1 papers | 2 compositions
- compositions: EuMg2 Bi2 (2); EuMg2Bi2 (1)
- measured range: 10-600 K (5th-95th pct of 19 curves)
- papers: Thermoelectric transport properties of CaMg2Bi2, EuMg2Bi2, and YbMg2Bi2

## Bi-Fe-La-O
- rank 1598 | 3 samples | 1 papers | 3 compositions
- compositions: La0.5Bi0.3Sr0.2FeO3 (1); La0.4Bi0.4Sr0.2FeO3 (1); La0.3Bi0.5Sr0.2FeO3 (1)
- dopant candidates (<5% at.): Sr (3)
- measured range: 823-1073 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaFe4(BiO4)3 Pm (6) mp-1222983 [hull=0.029, PRIMARY]; LaFe5Bi4O15 P1 (1) mp-1223162 [hull=0.027, PRIMARY]
- papers: Bismuth Doped Lanthanum Ferrite Perovskites as Novel Cathodes for Intermediate-Temperature Solid Oxide Fuel Cells

## Bi-Ga-In-Te
- rank 1599 | 3 samples | 1 papers | 3 compositions
- compositions: (Bi)20.45(In)21.98(Ga)9.93(Te)47.64 (1); (Bi)17.83(In)28(Ga)12.61(Te)41.55 (1); (Bi)23.26(In)15.42(Ga)7.05(Te)54.27 (1)
- measured range: 288-368 K (5th-95th pct of 15 curves)
- papers: Ternary Bi2Te3In2Te3Ga2Te3 (n-type) thermoelectric film on a flexible PET substrate for use in wearables

## Bi-Gd
- rank 1600 | 3 samples | 1 papers | 1 compositions
- compositions: GdBi (3)
- measured range: 13-47 K (5th-95th pct of 3 curves; full span incl. outliers 13-97 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdBi Fm-3m (225) mp-614481 [hull=0.000, icsd=3, PRIMARY]; GdBi3 P6_3/mmc (194) mp-1184501 [hull=0.066, PRIMARY, AMBIGUOUS]; GdBi3 I4/mmm (139) mp-1184536 [hull=0.072]
- papers: Extreme magnetoresistance in magnetic rare-earth monopnictides
