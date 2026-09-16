# Host systems -- chunk 031 of 73

Ranks 1501-1550 by sample count. These 50 host systems cover 157 samples (0.30% of the TE set); cumulative through this chunk: 93.88%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## S-V
- rank 1501 | 4 samples | 1 papers | 1 compositions
- compositions: V5S8 (4)
- measured range: 12-296 K (5th-95th pct of 4 curves)
- [ref 1] TEDesignLab / ICSD: VS Pnma (62) mp-1868 [hull=0.069, icsd=6, PRIMARY]; V5S8 C2/m (12) mp-690772 [hull=0.005, icsd=6, PRIMARY]; V5S4 I4/m (87) mp-1133 [hull=0.000, icsd=2, PRIMARY]; V3S I-42m (121) mp-7945 [hull=0.000, icsd=2, PRIMARY]; VS P6_3/mmc (194) mp-849065 [hull=0.203, icsd=3]
- [ref 2] MP, ranked by ICSD evidence: V3S4 C2/m (12) mp-850014 [hull=0.022, icsd=8, PRIMARY]; VS2 P6_3/mmc (194) mp-1013525 [hull=0.000, icsd=2, PRIMARY]; VS2 P-3m1 (164) mp-849054 [hull=0.020, icsd=2]; VS2 P-1 (2) mp-849060 [hull=0.019, icsd=1]; VS2 P1 (1) mp-655446 [hull=1.902, icsd=1]
- papers: https://doi.org/10.1088/1674-1056/abab85 (Intercalation of van der Waals layered materials: A route towards engi...)

## Sb-Te-Yb
- rank 1502 | 4 samples | 2 papers | 4 compositions
- compositions: YbSb2Te4 (1); (YbTe)0.8(YbSb)0.2 (1); (YbTe)0.2(YbSb)0.8 (1); (YbTe)0.5(YbSb)0.5 (1)
- measured range: 287-827 K (5th-95th pct of 16 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(SbTe2)2 I-42d (122) mp-675892 [hull=0.836, PRIMARY]; Yb3(Sb7Te12)2 P1 (1) mp-675683 [hull=0.966, PRIMARY]
- papers: https://doi.org/10.1002/pssr.200701228 (Synthesis and thermoelectric properties of YbSb2Te4) | https://doi.org/10.1007/s11664-015-4202-x (Synthesis and Thermoelectric Properties of the YbTe-YbSb System)

## Sb-Th
- rank 1503 | 4 samples | 1 papers | 2 compositions
- compositions: Th3Sb4 (3); Th3(As0.05Sb0.95)4 (1)
- dopant candidates (<5% at.): As (1)
- measured range: 102-1218 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ThSb Fm-3m (225) mp-1751 [hull=0.000, icsd=2, PRIMARY]; Th3Sb4 I-43d (220) mp-552 [hull=0.000, icsd=2, PRIMARY]; ThSb2 P4/nmm (129) mp-7568 [hull=0.000, icsd=2, PRIMARY]; Th2Sb3 P4/mmm (123) mp-1207006 [hull=3.607, PRIMARY]; ThSb Pm-3m (221) mp-10637 [hull=0.094, icsd=1]
- papers: https://doi.org/10.1149/1.2423585 (Some X-Ray and Thermoelectric Studies on Cubic Th[sub 3]X[sub 4] Compo...)

## Se-V
- rank 1504 | 4 samples | 3 papers | 1 compositions
- compositions: VSe2 (4)
- measured range: 10-700 K (5th-95th pct of 4 curves)
- [ref 1] TEDesignLab / ICSD: VSe P6_3/mmc (194) mp-29131 [hull=0.176, icsd=4, PRIMARY]; V2Se9 C2/c (15) mp-28256 [hull=0.000, icsd=1, PRIMARY]; VSe P4/nmm (129) mp-604914 [hull=0.123, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: VSe2 P-3m1 (164) mp-694 [hull=0.000, icsd=4, PRIMARY]; V3Se4 C2/m (12) mp-22700 [hull=0.000, icsd=4, PRIMARY]; V5Se4 I4/m (87) mp-1087497 [hull=0.000, icsd=1, PRIMARY]; V23Se40 C2/m (12) mp-685047 [hull=0.021, PRIMARY]
- papers: https://doi.org/10.1088/1674-1056/abab85 (Intercalation of van der Waals layered materials: A route towards engi...) | https://doi.org/10.1016/j.ssc.2020.113983 (Fabrication and thermoelectric properties of bulk VSe2 with layered st...) | https://doi.org/10.1016/j.jssc.2015.08.013 (Influence of interstitial V on structure and properties of ferecrystal...)

## Se-W
- rank 1505 | 4 samples | 3 papers | 1 compositions
- compositions: WSe2 (4)
- measured range: 101-673 K (5th-95th pct of 9 curves)
- [ref 1] TEDesignLab / ICSD: WSe2 P6_3/mmc (194) mp-1821 [hull=0.000, icsd=4, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: WSe2 P-3m1 (164) mp-1028698 [hull=0.000]; WSe2 P-6m2 (187) mp-1025572 [hull=0.000]
- papers: https://doi.org/10.3390/ma11071185 (A Review of the Characteristics, Synthesis, and Thermodynamics of Type...) | https://doi.org/10.1088/1361-648x/ab4aaa (The role of mid-gap phonon modes in thermal transport of transition me...) | https://doi.org/10.1016/j.jiec.2017.11.033 (Decoupling of thermal and electrical conductivities by adjusting the a...)

## Ta
- rank 1506 | 4 samples | 4 papers | 1 compositions
- compositions: Ta (4)
- measured range: 15-373 K (5th-95th pct of 4 curves; full span incl. outliers 15-1563 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ta Im-3m (229) mp-50 [hull=0.000, icsd=11, PRIMARY]; Ta P-42_1m (113) mp-42 [hull=0.005, icsd=5]; Ta Fm-3m (225) mp-6986 [hull=0.246, icsd=2]; Ta P4_2/mnm (136) mp-697196 [hull=1.211, icsd=2]; Ta P6_322 (182) mp-1095086 [hull=1.329, icsd=1]
- papers: https://doi.org/10.1063/1.3698169 (Intrinsic thermoelectric power of group VB metals) | https://doi.org/10.1007/bf00976954 (Thermoelectric properties of certain metals with a high melting point) | https://doi.org/10.1063/1.327772 (Thermoelectric power of tantalum‐tungsten alloys)

## Te-W
- rank 1507 | 4 samples | 1 papers | 1 compositions
- compositions: WTe2 (4)
- measured range: 201-497 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Te2W Pmn2_1 (31) mp-22693 [hull=0.000, icsd=5, PRIMARY]; Te2W P6_3/mmc (194) mp-1019322 [hull=0.025, icsd=1]; Te2W P-3m1 (164) mp-1028586 [hull=0.026]; Te2W P-6m2 (187) mp-1025573 [hull=0.027]
- papers: https://doi.org/10.3390/ma11071185 (A Review of the Characteristics, Synthesis, and Thermodynamics of Type...)

## Ag-Au-Cu-Si
- rank 1508 | 3 samples | 1 papers | 1 compositions
- compositions: Au49Cu26.9Ag5.5Pd2.3Si16.3 (3)
- dopant candidates (<5% at.): Pd (3)
- measured range: 12-392 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1134/s0021364015070127 (Thermoelectric properties of Au-based metallic glass at low temperatures)

## Ag-Ba-Bi-Co-O
- rank 1509 | 3 samples | 1 papers | 3 compositions
- compositions: Bi2BaAg2Co2O9 (1); Bi2Ba1.5Ag1.5Co2O9 (1); Bi2Ba2AgCo2O9 (1)
- measured range: 11-338 K (5th-95th pct of 9 curves)
- papers: https://doi.org/10.1063/1.2795622 (A narrow band contribution with Anderson localization in Ag-doped laye...)

## Ag-Ba-Cu-O-Y
- rank 1510 | 3 samples | 1 papers | 3 compositions
- compositions: (Ag2O)41.82(YBa2Cu3O7)58.18 (1); (Ag2O)55.2(YBa2Cu3O7)44.8 (1); (Ag2O)65.71(YBa2Cu3O7)34.29 (1)
- measured range: 11-260 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/s0011-2275(05)80050-5 (Possibility of Ag2O+YBa2Cu3O7−X ceramics for low temperature thermoele...)

## Ag-Bi-Ca-Cu-O-Sr
- rank 1511 | 3 samples | 1 papers | 3 compositions
- compositions: Ag2.3Bi1.6Pb0.4Sr1.6Ca2Cu3O10 (1); AgBi1.6Pb0.4Sr1.6Ca2Cu3O10 (1); Ag9Bi1.6Pb0.4Sr1.6Ca2Cu3O10 (1)
- dopant candidates (<5% at.): Pb (3)
- measured range: 102-299 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/0921-4534(93)90779-p (Thermoelectric power studies on the BPSCCO system with silver addition)

## Ag-Bi-Cl-S
- rank 1512 | 3 samples | 1 papers | 3 compositions
- compositions: AgBi3S4.2Cl0.8 (1); AgBi3S3.35Cl1.65 (1); AgBi3S2.5Cl2.5 (1)
- measured range: 299-802 K (5th-95th pct of 15 curves)
- papers: https://doi.org/10.1021/jacs.7b02399 (High Thermoelectric Performance in Electron-Doped AgBi3S5 with Ultralo...)

## Ag-Bi-Cu-O-Se
- rank 1513 | 3 samples | 1 papers | 3 compositions
- compositions: BiCu0.80Ag0.20SeO (1); BiCu0.70Ag0.30SeO (1); BiCu0.60Ag0.40SeO (1)
- measured range: 12-301 K (5th-95th pct of 15 curves)
- papers: https://doi.org/10.1063/1.4894258 (Enhanced low temperature thermoelectric performance of Ag-doped BiCuSeO)

## Ag-Br-Cl-Te
- rank 1514 | 3 samples | 2 papers | 3 compositions
- compositions: Ag5Te2Cl0.6Br0.4 (1); Ag5Te2Cl0.4Br0.6 (1); Ag10Te4Br1.6Cl1.4 (1)
- measured range: 302-499 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ag10Te4BrCl P2_1/c (14) mp-1229222 [hull=0.008, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2011.01.031 (Effects of partial anion substitution on the thermoelectric properties...) | https://doi.org/10.1016/j.solidstatesciences.2011.02.012 (A conceptional approach to materials for resistivity switching and the...)

## Ag-C-Te
- rank 1515 | 3 samples | 1 papers | 3 compositions
- compositions: Ag2Te3C2 (1); Ag2TeC5 (1); Ag2TeC9 (1)
- measured range: 324-539 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.1021/am4059167 (n-Type Carbon Nanotubes/Silver Telluride Nanohybrid Buckypaper with a ...)

## Ag-Ce-Sb
- rank 1516 | 3 samples | 2 papers | 1 compositions
- compositions: CeAgSb2 (3)
- measured range: 10-295 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce2(AgSb)3 P4/mmm (123) mp-1206228 [hull=0.962, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/23/47/476001 (Thermoelectric power of RAgSb2(R = Y, La, Ce, and Dy) in zero and appl...) | https://doi.org/10.1016/0304-8853(94)01418-3 (Kondo lattice behaviour in CeTSb2 compounds (T  Ni, Cu and Ag))

## Ag-Cu-Te-Tl
- rank 1517 | 3 samples | 1 papers | 3 compositions
- compositions: Ag0.8Cu0.2TlTe (1); Ag0.7Cu0.3TlTe (1); Ag0.6Cu0.4TlTe (1)
- measured range: 300-563 K (5th-95th pct of 15 curves)
- papers: https://doi.org/10.1063/1.2756037 (Enhancement of thermoelectric figure of merit of AgTlTe by tuning the ...)

## Ag-In-Sb-Te
- rank 1518 | 3 samples | 1 papers | 3 compositions
- compositions: AgIn0.6Sb0.4Te2 (1); AgIn0.5Sb0.5Te2 (1); AgIn0.4Sb0.6Te2 (1)
- measured range: 11-300 K (5th-95th pct of 12 curves)
- papers: https://doi.org/10.1016/j.jssc.2013.07.027 (A high-pressure route to thermoelectrics with low thermal conductivity...)

## Ag-In-Yb
- rank 1519 | 3 samples | 1 papers | 1 compositions
- compositions: Ag42In42Yb16_IQC (3)
- measured range: 11-303 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbInAg2 Fm-3m (225) mp-865789 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1039/c2cs35036j (Electrical and thermal transport properties of icosahedral and decagon...)

## Ag-La-Sb
- rank 1520 | 3 samples | 1 papers | 1 compositions
- compositions: LaAgSb2 (3)
- measured range: 12-292 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaAgSb2 P4/nmm (129) mp-20271 [hull=0.000, icsd=5, PRIMARY]; La2AgSb3 P4/mmm (123) mp-1206475 [hull=3.031, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/23/47/476001 (Thermoelectric power of RAgSb2(R = Y, La, Ce, and Dy) in zero and appl...)

## Ag-N-Ta
- rank 1521 | 3 samples | 1 papers | 3 compositions
- compositions: Ag0.3(TaN)0.7 (1); Ag0.27(TaN)0.73 (1); Ag0.25(TaN)0.75 (1)
- measured range: 186-367 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.3938/jkps.54.2323 (Electrical Resistivities and TCR Behavior of Co-Sputtered TaN-(Ag, Cu)...)

## Ag-O-Pb-Te
- rank 1522 | 3 samples | 1 papers | 3 compositions
- compositions: Pb0.374Te0.357Ag0.143O0.126 (1); Pb0.407Te0.399Ag0.054O0.14 (1); 	Pb0.381Te0.378Ag0.107O0.134 (1)
- measured range: 290-401 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1063/1.4984050 (Enhancement of thermoelectric power of PbTe thin films by Ag ion impla...)

## Ag-Sb-Y
- rank 1523 | 3 samples | 1 papers | 1 compositions
- compositions: YAgSb2 (3)
- measured range: 10-294 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YAgSb2 P4/nmm (129) mp-1078739 [hull=0.000, icsd=1, PRIMARY]; Y2AgSb3 P4/mmm (123) mp-1206111 [hull=3.079, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/23/47/476001 (Thermoelectric power of RAgSb2(R = Y, La, Ce, and Dy) in zero and appl...)

## Ag-Sn-Te
- rank 1524 | 3 samples | 2 papers | 3 compositions
- compositions: Sn0.94Gd0.06Ag0.11Te (1); Sn0.85In0.05Ag0.10Te (1); Sn0.82In0.06Ag0.12Te (1)
- dopant candidates (<5% at.): In (2), Gd (1)
- measured range: 300-824 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AgSnTe2 P4/mmm (123) mp-1229006 [hull=0.052, PRIMARY]
- papers: https://doi.org/10.1002/adma.201605887 (Promoting SnTe as an Eco-Friendly Solution for p-PbTe Thermoelectric v...) | https://doi.org/10.1039/c9ta11614a (Outstanding thermoelectric properties of solvothermal-synthesized Sn1−...)

## Al-As-In-Sb
- rank 1525 | 3 samples | 1 papers | 1 compositions
- compositions: (InAs)33.4(AlSb)31.8 (3)
- measured range: 81-299 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1109/tcapt.2006.875895 (Nanoscale heat transfer and nanostructured thermoelectrics)

## Al-Ba-K-Sn
- rank 1526 | 3 samples | 2 papers | 2 compositions
- compositions: K10Ba14Al35Ga4Sn97 (2); K9Ba15Al38Sn98 (1)
- dopant candidates (<5% at.): Ga (2)
- measured range: 100-637 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1016/j.jallcom.2016.09.231 (Preparation and thermoelectric properties of sintered type-II clathrat...) | https://doi.org/10.1021/acs.chemmater.6b05027 (Predicting Ground-State Configurations and Electronic Properties of th...)

## Al-C-Cr-O
- rank 1527 | 3 samples | 1 papers | 3 compositions
- compositions: (Al2O3)80.1(Cr3C2)19.9 (1); (Al2O3)70.13(Cr3C2)29.87 (1); (Al2O3)60.15(Cr3C2)39.85 (1)
- measured range: 297-871 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/0956-7151(94)00303-y (Heat conduction of composites and its dependence on the microstructure...)

## Al-C-Ni-Ti
- rank 1528 | 3 samples | 1 papers | 3 compositions
- compositions: (TiC)76.88(Ni3Al)23.12 (1); (TiC)59.64(Ni3Al)40.36 (1); (TiC)35.65(Ni3Al)64.35 (1)
- measured range: 290-1316 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.2497/jjspm.43.278 (Densification and Thermal Properties of TiC-Ni3Al Composites Materials.)

## Al-Co-O
- rank 1529 | 3 samples | 1 papers | 3 compositions
- compositions: Co63Al13O24 (1); Co66Al11O23 (1); Co74Al8O18 (1)
- measured range: 10-59 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al2CoO4 Fd-3m (227) mp-36447 [hull=0.000, icsd=1, PRIMARY]; AlCoO3 R-3 (148) mp-1178576 [hull=0.046, PRIMARY]; Al2CoO4 R3m (160) mp-694863 [hull=0.022]; Al2CoO4 Cm (8) mp-37621 [hull=0.027]; Al2CoO4 P3m1 (156) mp-705606 [hull=0.034]
- papers: https://doi.org/10.1088/1742-6596/200/1/012141 (Transport properties of ferromagnetic granular Co–Al–O films)

## Al-Co-Si-Ti
- rank 1530 | 3 samples | 1 papers | 3 compositions
- compositions: Co2TiAl0.75Si0.25 (1); Co2TiAl0.25Si0.75 (1); Co2TiAl0.5Si0.5 (1)
- measured range: 10-1034 K (5th-95th pct of 9 curves)
- papers: https://doi.org/10.1016/j.scriptamat.2010.07.001 (Tuning the carrier concentration for thermoelectrical application in t...)

## Al-Cu-Ir
- rank 1531 | 3 samples | 1 papers | 3 compositions
- compositions: Al68.3Cu5Ir26.7_IAC_1_0 (1); Al67.3Cu6Ir26.7_IAC_1_0 (1); Al66.3Cu7Ir26.7_IAC_1_0 (1)
- measured range: 363-962 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al2CuIr Cmme (67) mp-1079890 [hull=0.000, icsd=1, PRIMARY]; Al2CuIr Immm (71) mp-1093789 [hull=2.590]
- papers: https://doi.org/10.1016/j.jallcom.2018.05.199 (Anomalous effects of Cu-doping on structural and thermoelectric proper...)

## Al-Fe-Mg-O
- rank 1532 | 3 samples | 2 papers | 3 compositions
- compositions: Mg0.4Al0.8Li0.30Fe1.50O4 (1); Mg0.5Al1.0Li0.25Fe1.25O4 (1); Mg0.75Fe0.41Al1.85O4 (1)
- dopant candidates (<5% at.): Li (2)
- measured range: 14-677 K (5th-95th pct of 3 curves; full span incl. outliers 14-738 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg14AlFeO16 Pmmm (47) mp-1036658 [hull=0.086, PRIMARY]; Mg30AlFeO32 P4/mmm (123) mp-1038379 [hull=0.040, PRIMARY]; Mg6AlFeO8 P4/mmm (123) mp-1033177 [hull=0.190, PRIMARY]; MgAlFeO4 Imma (74) mp-1222041 [hull=0.035, PRIMARY]; Mg14AlFeO16 P4/mmm (123) mp-1036709 [hull=0.108]
- papers: https://doi.org/10.1016/j.jallcom.2004.09.059 (Thermoelectric power studies of magnesium and aluminium substituted li...) | https://doi.org/10.1103/physrev.126.427 (Thermal Conductivity of MgO,Al2O3, MgAl2O4, andFe3O4Crystals from 3° t...)

## Al-Fe-Nb-Ru
- rank 1533 | 3 samples | 1 papers | 3 compositions
- compositions: Ru1.75Fe0.25NbAl (1); Ru1.62Fe0.38NbAl (1); Ru1.50Fe0.50NbAl (1)
- measured range: 11-298 K (5th-95th pct of 12 curves)
- papers: https://doi.org/10.1016/j.jallcom.2023.169318 (Physical properties of the full Heusler-type Ru2-Fe NbAl (x = 0.00–0.5...)

## Al-Fe-O-Sb
- rank 1534 | 3 samples | 1 papers | 3 compositions
- compositions: Al0.75Sb0.25FeO3 (1); Al0.25Sb0.75FeO3 (1); Al0.5Sb0.5FeO3 (1)
- measured range: 200-398 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.3390/ma15238369 (Influence of Sb3+ Cations on the Structural, Magnetic and Electrical P...)

## Al-Fe-V-W
- rank 1535 | 3 samples | 2 papers | 1 compositions
- compositions: Fe2V0.8W0.2Al (3)
- measured range: 11-818 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1038/s41586-019-1751-9 (Thermoelectric performance of a metastable thin-film Heusler alloy) | https://doi.org/10.1103/physrevb.102.075117 (Stoichiometric and off-stoichiometric full Heusler \n<mml:math xmlns:m...)

## Al-Ga-Mn-Pd
- rank 1536 | 3 samples | 1 papers | 3 compositions
- compositions: Al64.9Pd20.7Mn8.4Ga6_IQC (1); Al62.9Pd20.7Mn8.4Ga8_IQC (1); Al60.9Pd20.7Mn8.4Ga10_IQC (1)
- measured range: 19-247 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/j.jallcom.2012.09.130 (Structural, tribological and resistivity studies of Ga substituted (Al...)

## Al-In-Mn-Si
- rank 1537 | 3 samples | 1 papers | 3 compositions
- compositions: Mn2.7Cr0.3Si4Al1.4In0.6 (1); Mn2.7Cr0.3Si4Al1.2In0.8 (1); Mn2.7Cr0.3Si4AlIn (1)
- dopant candidates (<5% at.): Cr (3)
- measured range: 298-898 K (5th-95th pct of 15 curves)
- papers: https://doi.org/10.1007/s11664-016-4365-0 (Structural Investigation and Indium Substitution in the Thermoelectric...)

## Al-Ir-Rh
- rank 1538 | 3 samples | 1 papers | 3 compositions
- compositions: Al73.3Rh6.675Ir20.025_IAC (1); Al73.3Rh13.35Ir13.35_IAC (1); Al73.3Rh20.025Ir6.675_IAC (1)
- measured range: 299-903 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al2IrRh Fm-3m (225) mp-862694 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2020.156904 (Band engineering in Al-TM (TM=Rh, Ir) quasicrystalline approximants vi...)

## Al-La-O-Sr
- rank 1539 | 3 samples | 3 papers | 3 compositions
- compositions: SrLaAlO4 (1); LaSrAlO4 (1); (La0.7Sr0.3)(Al0.8Fe0.2)O3 (1)
- dopant candidates (<5% at.): Fe (1)
- measured range: 13-348 K (5th-95th pct of 3 curves; full span incl. outliers 13-1263 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2LaAlO5 Fmmm (69) mp-1218761 [hull=0.031, PRIMARY]; SrLa2Al2O7 I4/mmm (139) mp-1218238 [hull=0.020, PRIMARY]; SrLaAl3O7 Cmm2 (35) mp-1218220 [hull=0.000, PRIMARY]; SrLaAlO4 I4mm (107) mp-1218184 [hull=0.017, PRIMARY]
- papers: https://doi.org/10.1021/acsami.8b21301 (Strain Effect on Oxygen Evolution Reaction Activity of Epitaxial NdNiO...) | https://doi.org/10.1063/1.5098025 (Tuning the electronic properties of epitaxial strained CaFeO3−δ thin f...) | https://doi.org/10.1063/1.4883042 (Temperature-independent sensors based on perovskite-type oxides)

## Al-Lu
- rank 1540 | 3 samples | 3 papers | 2 compositions
- compositions: LuAl3 (2); LuAl2 (1)
- measured range: 10-300 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LuAl2 Fd-3m (227) mp-1234 [hull=0.000, icsd=6, PRIMARY]; LuAl3 Pm-3m (221) mp-2805 [hull=0.000, icsd=4, PRIMARY]; LuAl Pbcm (57) mp-16507 [hull=0.000, icsd=1, PRIMARY]; Lu3Al2 P4_2/mnm (136) mp-16508 [hull=0.000, icsd=1, PRIMARY]; Lu3Al P6_3/mmc (194) mp-973266 [hull=0.007, PRIMARY]
- papers: https://doi.org/10.1007/s11664-012-2401-2 (Thermoelectric Properties of Yb1−x (Er,Lu) x Al3 Solid Solutions) | https://doi.org/10.1088/0953-8984/27/10/105601 (Nernst effect of the intermediate valence compound YbAl3: revisiting t...) | https://doi.org/10.1016/0022-5088(85)90212-7 (Electrical resistivity, thermal conductivity and thermopower of nonmag...)

## Al-Lu-Yb
- rank 1541 | 3 samples | 1 papers | 3 compositions
- compositions: Yb0.75Lu0.25Al3 (1); Yb0.5Lu0.5Al3 (1); Yb0.25Lu0.75Al3 (1)
- measured range: 80-300 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbLuAl4 F-43m (216) mp-1215433 [hull=0.023, PRIMARY]
- papers: https://doi.org/10.1007/s11664-012-2401-2 (Thermoelectric Properties of Yb1−x (Er,Lu) x Al3 Solid Solutions)

## Al-Ni-U
- rank 1542 | 3 samples | 2 papers | 2 compositions
- compositions: UNiAl (2); UNi2Al3 (1)
- measured range: 12-283 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UAlNi P-62m (189) mp-1079086 [hull=0.158, icsd=7, PRIMARY]; UAl3Ni2 P6/mmm (191) mp-2903 [hull=0.108, icsd=5, PRIMARY]; U3Al19Ni5 Cmcm (63) mp-1196284 [hull=0.032, icsd=1, PRIMARY]; UAlNi4 F-43m (216) mp-16519 [hull=0.061, icsd=1, PRIMARY]; UAlNi Amm2 (38) mp-1079129 [hull=0.172, icsd=7]
- papers: https://doi.org/10.1016/s0925-8388(00)01176-2 (Large thermoelectric power in several metallic compounds of cerium and...) | https://doi.org/10.1016/s0921-4526(99)00198-2 (Thermoelectric power of a UNiAl single crystal)

## Al-Ni-Yb
- rank 1543 | 3 samples | 3 papers | 2 compositions
- compositions: YbNi0.8Al4.2 (2); YbNi3Al9 (1)
- measured range: 10-300 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb4Al23Ni6 C2/m (12) mp-18482 [hull=0.000, icsd=1, PRIMARY]; YbAl2Ni Cmcm (63) mp-12782 [hull=0.000, icsd=1, PRIMARY]; YbAlNi P-62m (189) mp-1078733 [hull=0.018, icsd=1, PRIMARY]; Yb2AlNi2 Immm (71) mp-1207023 [hull=0.000, PRIMARY]; YbAlNi Amm2 (38) mp-1215764 [hull=0.071]
- papers: https://doi.org/10.1016/j.jallcom.2006.09.167 (YbNi0.8Al4.2: A novel intermetallic compound with an enhanced thermoel...) | https://doi.org/10.1088/0953-8984/18/46/004 (Intermediate valence behaviour of Yb in a new intermetallic compound Y...) | https://doi.org/10.1063/5.0035385 (Thin film growth of heavy fermion chiral magnet YbNi<sub>3</sub>Al<sub...)

## Al-Ru-U
- rank 1544 | 3 samples | 1 papers | 1 compositions
- compositions: URu2Al10 (3)
- measured range: 10-289 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UAlRu P-62m (189) mp-1080013 [hull=0.084, icsd=2, PRIMARY]; U(Al5Ru)2 Cmcm (63) mp-1193796 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2011.02.008 (Crystal structure and physical properties of a new intermetallic compo...)

## Al-Sn-Yb
- rank 1545 | 3 samples | 1 papers | 3 compositions
- compositions: YbAl2.8Sn0.2 (1); YbAl2.5Sn0.5 (1); YbAl2.7Sn0.3 (1)
- measured range: 299-674 K (5th-95th pct of 15 curves)
- papers: https://doi.org/10.1016/j.jallcom.2014.02.112 (Influence of Sn substitution on the thermoelectric properties in YbAl3)

## As-Ca-Fe-O-Ti
- rank 1546 | 3 samples | 1 papers | 1 compositions
- compositions: (Fe2As2)Ca4(Mg0.25Ti0.75)3O8 (3)
- dopant candidates (<5% at.): Mg (3)
- measured range: 11-299 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1016/j.physc.2015.06.015 (Thermoelectric properties of FeAs based superconductors, with thick pe...)

## As-Co
- rank 1547 | 3 samples | 3 papers | 3 compositions
- compositions: CoAs3 (1); CoAs2 (1); CoAs (1)
- measured range: 11-874 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CoAs Pnma (62) mp-583 [hull=0.000, icsd=9, PRIMARY]; CoAs3 Im-3 (204) mp-452 [hull=0.000, icsd=8, PRIMARY]; CoAs2 P2_1/c (14) mp-2715 [hull=0.000, icsd=5, PRIMARY]; Co2As P-62m (189) mp-18206 [hull=0.062, icsd=4, PRIMARY]; Co5As2 P6_3cm (185) mp-16316 [hull=0.075, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.360402 (Thermoelectric properties of CoSb3and related alloys) | https://doi.org/10.1063/1.4923087 (Electrical/thermal transport and electronic structure of the binary co...) | https://doi.org/10.1088/0953-2048/25/8/084016 (Properties of binary transition-metal arsenides (TAs))

## As-Cu-S-Zn
- rank 1548 | 3 samples | 1 papers | 1 compositions
- compositions: Cu10.0Zn1.8Fe0.2As2.7Sb1.3S13 (3)
- dopant candidates (<5% at.): Sb (3), Fe (3)
- measured range: 87-721 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zn3Cu6(AsS3)4 P1 (1) mp-1215617 [hull=0.010, PRIMARY]
- papers: https://doi.org/10.1021/acsami.5b07141 (Solvothermal Synthesis of Tetrahedrite: Speeding Up the Process of The...)

## As-Cu-Se-Te
- rank 1549 | 3 samples | 1 papers | 3 compositions
- compositions: Cu27.5As12.5Te54Se6 (1); Cu25As15Te54Se6 (1); Cu30As10Te54Se6 (1)
- measured range: 300-375 K (5th-95th pct of 12 curves)
- papers: https://doi.org/10.1016/j.jssc.2013.04.015 (Thermal stability and thermoelectric properties of CuxAs40−xTe60−ySey ...)

## As-Fe-Sr
- rank 1550 | 3 samples | 1 papers | 3 compositions
- compositions: K0.17Sr0.83Fe2As2 (1); K0.22Sr0.78Fe2As2 (1); K0.12Sr0.88Fe2As2 (1)
- dopant candidates (<5% at.): K (3)
- measured range: 12-319 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr(FeAs)2 I4/mmm (139) mp-4488 [hull=0.000, icsd=6, PRIMARY]; NaSr4(FeAs)10 I4/m (87) mp-1221018 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.79.104504 (Evidence of quantum criticality in the phase diagram ofKxSr1−xFe2As2fr...)
