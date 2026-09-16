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
- papers: Intercalation of van der Waals layered materials: A route towards engineering of electron correlation

## Sb-Te-Yb
- rank 1502 | 4 samples | 2 papers | 4 compositions
- compositions: YbSb2Te4 (1); (YbTe)0.8(YbSb)0.2 (1); (YbTe)0.2(YbSb)0.8 (1); (YbTe)0.5(YbSb)0.5 (1)
- measured range: 287-827 K (5th-95th pct of 16 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(SbTe2)2 I-42d (122) mp-675892 [hull=0.836, PRIMARY]; Yb3(Sb7Te12)2 P1 (1) mp-675683 [hull=0.966, PRIMARY]
- papers: Synthesis and thermoelectric properties of YbSb2Te4 | Synthesis and Thermoelectric Properties of the YbTe-YbSb System

## Sb-Th
- rank 1503 | 4 samples | 1 papers | 2 compositions
- compositions: Th3Sb4 (3); Th3(As0.05Sb0.95)4 (1)
- dopant candidates (<5% at.): As (1)
- measured range: 102-1218 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ThSb Fm-3m (225) mp-1751 [hull=0.000, icsd=2, PRIMARY]; Th3Sb4 I-43d (220) mp-552 [hull=0.000, icsd=2, PRIMARY]; ThSb2 P4/nmm (129) mp-7568 [hull=0.000, icsd=2, PRIMARY]; Th2Sb3 P4/mmm (123) mp-1207006 [hull=3.607, PRIMARY]; ThSb Pm-3m (221) mp-10637 [hull=0.094, icsd=1]
- papers: Some X-Ray and Thermoelectric Studies on Cubic Th[sub 3]X[sub 4] Compounds

## Se-V
- rank 1504 | 4 samples | 3 papers | 1 compositions
- compositions: VSe2 (4)
- measured range: 10-700 K (5th-95th pct of 4 curves)
- [ref 1] TEDesignLab / ICSD: VSe P6_3/mmc (194) mp-29131 [hull=0.176, icsd=4, PRIMARY]; V2Se9 C2/c (15) mp-28256 [hull=0.000, icsd=1, PRIMARY]; VSe P4/nmm (129) mp-604914 [hull=0.123, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: VSe2 P-3m1 (164) mp-694 [hull=0.000, icsd=4, PRIMARY]; V3Se4 C2/m (12) mp-22700 [hull=0.000, icsd=4, PRIMARY]; V5Se4 I4/m (87) mp-1087497 [hull=0.000, icsd=1, PRIMARY]; V23Se40 C2/m (12) mp-685047 [hull=0.021, PRIMARY]
- papers: Intercalation of van der Waals layered materials: A route towards engineering of electron correlation | Fabrication and thermoelectric properties of bulk VSe2 with layered structure | Influence of interstitial V on structure and properties of ferecrystalline ([SnSe]1.15)1(V1+Se2)n for n=1, 2, 3, 4, 5, and 6

## Se-W
- rank 1505 | 4 samples | 3 papers | 1 compositions
- compositions: WSe2 (4)
- measured range: 101-673 K (5th-95th pct of 9 curves)
- [ref 1] TEDesignLab / ICSD: WSe2 P6_3/mmc (194) mp-1821 [hull=0.000, icsd=4, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: WSe2 P-3m1 (164) mp-1028698 [hull=0.000]; WSe2 P-6m2 (187) mp-1025572 [hull=0.000]
- papers: A Review of the Characteristics, Synthesis, and Thermodynamics of Type-II Weyl Semimetal WTe2 | The role of mid-gap phonon modes in thermal transport of transition metal dichalcogenides | Decoupling of thermal and electrical conductivities by adjusting the anisotropic nature in tungsten diselenide causing significant enhancement in thermoelectric performance

## Ta
- rank 1506 | 4 samples | 4 papers | 1 compositions
- compositions: Ta (4)
- measured range: 15-373 K (5th-95th pct of 4 curves; full span incl. outliers 15-1563 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ta Im-3m (229) mp-50 [hull=0.000, icsd=11, PRIMARY]; Ta P-42_1m (113) mp-42 [hull=0.005, icsd=5]; Ta Fm-3m (225) mp-6986 [hull=0.246, icsd=2]; Ta P4_2/mnm (136) mp-697196 [hull=1.211, icsd=2]; Ta P6_322 (182) mp-1095086 [hull=1.329, icsd=1]
- papers: Intrinsic thermoelectric power of group VB metals | Thermoelectric properties of certain metals with a high melting point | Thermoelectric power of tantalum‐tungsten alloys

## Te-W
- rank 1507 | 4 samples | 1 papers | 1 compositions
- compositions: WTe2 (4)
- measured range: 201-497 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Te2W Pmn2_1 (31) mp-22693 [hull=0.000, icsd=5, PRIMARY]; Te2W P6_3/mmc (194) mp-1019322 [hull=0.025, icsd=1]; Te2W P-3m1 (164) mp-1028586 [hull=0.026]; Te2W P-6m2 (187) mp-1025573 [hull=0.027]
- papers: A Review of the Characteristics, Synthesis, and Thermodynamics of Type-II Weyl Semimetal WTe2

## Ag-Au-Cu-Si
- rank 1508 | 3 samples | 1 papers | 1 compositions
- compositions: Au49Cu26.9Ag5.5Pd2.3Si16.3 (3)
- dopant candidates (<5% at.): Pd (3)
- measured range: 12-392 K (5th-95th pct of 4 curves)
- papers: Thermoelectric properties of Au-based metallic glass at low temperatures

## Ag-Ba-Bi-Co-O
- rank 1509 | 3 samples | 1 papers | 3 compositions
- compositions: Bi2BaAg2Co2O9 (1); Bi2Ba1.5Ag1.5Co2O9 (1); Bi2Ba2AgCo2O9 (1)
- measured range: 11-338 K (5th-95th pct of 9 curves)
- papers: A narrow band contribution with Anderson localization in Ag-doped layered cobaltites Bi2Ba3Co2Oy

## Ag-Ba-Cu-O-Y
- rank 1510 | 3 samples | 1 papers | 3 compositions
- compositions: (Ag2O)41.82(YBa2Cu3O7)58.18 (1); (Ag2O)55.2(YBa2Cu3O7)44.8 (1); (Ag2O)65.71(YBa2Cu3O7)34.29 (1)
- measured range: 11-260 K (5th-95th pct of 3 curves)
- papers: Possibility of Ag2O+YBa2Cu3O7−X ceramics for low temperature thermoelectricrefrigeration

## Ag-Bi-Ca-Cu-O-Sr
- rank 1511 | 3 samples | 1 papers | 3 compositions
- compositions: Ag2.3Bi1.6Pb0.4Sr1.6Ca2Cu3O10 (1); AgBi1.6Pb0.4Sr1.6Ca2Cu3O10 (1); Ag9Bi1.6Pb0.4Sr1.6Ca2Cu3O10 (1)
- dopant candidates (<5% at.): Pb (3)
- measured range: 102-299 K (5th-95th pct of 3 curves)
- papers: Thermoelectric power studies on the BPSCCO system with silver addition

## Ag-Bi-Cl-S
- rank 1512 | 3 samples | 1 papers | 3 compositions
- compositions: AgBi3S4.2Cl0.8 (1); AgBi3S3.35Cl1.65 (1); AgBi3S2.5Cl2.5 (1)
- measured range: 299-802 K (5th-95th pct of 15 curves)
- papers: High Thermoelectric Performance in Electron-Doped AgBi3S5 with Ultralow Thermal Conductivity

## Ag-Bi-Cu-O-Se
- rank 1513 | 3 samples | 1 papers | 3 compositions
- compositions: BiCu0.80Ag0.20SeO (1); BiCu0.70Ag0.30SeO (1); BiCu0.60Ag0.40SeO (1)
- measured range: 12-301 K (5th-95th pct of 15 curves)
- papers: Enhanced low temperature thermoelectric performance of Ag-doped BiCuSeO

## Ag-Br-Cl-Te
- rank 1514 | 3 samples | 2 papers | 3 compositions
- compositions: Ag5Te2Cl0.6Br0.4 (1); Ag5Te2Cl0.4Br0.6 (1); Ag10Te4Br1.6Cl1.4 (1)
- measured range: 302-499 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ag10Te4BrCl P2_1/c (14) mp-1229222 [hull=0.008, PRIMARY]
- papers: Effects of partial anion substitution on the thermoelectric properties of silver(I) chalcogenide halides in the system Ag5Q2X with Q=Te, Se and S and X=Br and Cl | A conceptional approach to materials for resistivity switching and thermoelectrics

## Ag-C-Te
- rank 1515 | 3 samples | 1 papers | 3 compositions
- compositions: Ag2Te3C2 (1); Ag2TeC5 (1); Ag2TeC9 (1)
- measured range: 324-539 K (5th-95th pct of 10 curves)
- papers: n-Type Carbon Nanotubes/Silver Telluride Nanohybrid Buckypaper with a High-Thermoelectric Figure of Merit

## Ag-Ce-Sb
- rank 1516 | 3 samples | 2 papers | 1 compositions
- compositions: CeAgSb2 (3)
- measured range: 10-295 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce2(AgSb)3 P4/mmm (123) mp-1206228 [hull=0.962, PRIMARY]
- papers: Thermoelectric power of RAgSb2(R = Y, La, Ce, and Dy) in zero and applied magnetic fields | Kondo lattice behaviour in CeTSb2 compounds (T  Ni, Cu and Ag)

## Ag-Cu-Te-Tl
- rank 1517 | 3 samples | 1 papers | 3 compositions
- compositions: Ag0.8Cu0.2TlTe (1); Ag0.7Cu0.3TlTe (1); Ag0.6Cu0.4TlTe (1)
- measured range: 300-563 K (5th-95th pct of 15 curves)
- papers: Enhancement of thermoelectric figure of merit of AgTlTe by tuning the carrier concentration

## Ag-In-Sb-Te
- rank 1518 | 3 samples | 1 papers | 3 compositions
- compositions: AgIn0.6Sb0.4Te2 (1); AgIn0.5Sb0.5Te2 (1); AgIn0.4Sb0.6Te2 (1)
- measured range: 11-300 K (5th-95th pct of 12 curves)
- papers: A high-pressure route to thermoelectrics with low thermal conductivity: The solid solution series AgInxSb1−xTe2 (x=0.1–0.6)

## Ag-In-Yb
- rank 1519 | 3 samples | 1 papers | 1 compositions
- compositions: Ag42In42Yb16_IQC (3)
- measured range: 11-303 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbInAg2 Fm-3m (225) mp-865789 [hull=0.000, PRIMARY]
- papers: Electrical and thermal transport properties of icosahedral and decagonal quasicrystals

## Ag-La-Sb
- rank 1520 | 3 samples | 1 papers | 1 compositions
- compositions: LaAgSb2 (3)
- measured range: 12-292 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaAgSb2 P4/nmm (129) mp-20271 [hull=0.000, icsd=5, PRIMARY]; La2AgSb3 P4/mmm (123) mp-1206475 [hull=3.031, PRIMARY]
- papers: Thermoelectric power of RAgSb2(R = Y, La, Ce, and Dy) in zero and applied magnetic fields

## Ag-N-Ta
- rank 1521 | 3 samples | 1 papers | 3 compositions
- compositions: Ag0.3(TaN)0.7 (1); Ag0.27(TaN)0.73 (1); Ag0.25(TaN)0.75 (1)
- measured range: 186-367 K (5th-95th pct of 3 curves)
- papers: Electrical Resistivities and TCR Behavior of Co-Sputtered TaN-(Ag, Cu) Nanocomposites

## Ag-O-Pb-Te
- rank 1522 | 3 samples | 1 papers | 3 compositions
- compositions: Pb0.374Te0.357Ag0.143O0.126 (1); Pb0.407Te0.399Ag0.054O0.14 (1); 	Pb0.381Te0.378Ag0.107O0.134 (1)
- measured range: 290-401 K (5th-95th pct of 6 curves)
- papers: Enhancement of thermoelectric power of PbTe thin films by Ag ion implantation

## Ag-Sb-Y
- rank 1523 | 3 samples | 1 papers | 1 compositions
- compositions: YAgSb2 (3)
- measured range: 10-294 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YAgSb2 P4/nmm (129) mp-1078739 [hull=0.000, icsd=1, PRIMARY]; Y2AgSb3 P4/mmm (123) mp-1206111 [hull=3.079, PRIMARY]
- papers: Thermoelectric power of RAgSb2(R = Y, La, Ce, and Dy) in zero and applied magnetic fields

## Ag-Sn-Te
- rank 1524 | 3 samples | 2 papers | 3 compositions
- compositions: Sn0.94Gd0.06Ag0.11Te (1); Sn0.85In0.05Ag0.10Te (1); Sn0.82In0.06Ag0.12Te (1)
- dopant candidates (<5% at.): In (2), Gd (1)
- measured range: 300-824 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AgSnTe2 P4/mmm (123) mp-1229006 [hull=0.052, PRIMARY]
- papers: Promoting SnTe as an Eco-Friendly Solution for p-PbTe Thermoelectric via Band Convergence and Interstitial Defects | Outstanding thermoelectric properties of solvothermal-synthesized Sn1−3xInxAg2xTe micro-crystals through defect engineering and band tuning

## Al-As-In-Sb
- rank 1525 | 3 samples | 1 papers | 1 compositions
- compositions: (InAs)33.4(AlSb)31.8 (3)
- measured range: 81-299 K (5th-95th pct of 3 curves)
- papers: Nanoscale heat transfer and nanostructured thermoelectrics

## Al-Ba-K-Sn
- rank 1526 | 3 samples | 2 papers | 2 compositions
- compositions: K10Ba14Al35Ga4Sn97 (2); K9Ba15Al38Sn98 (1)
- dopant candidates (<5% at.): Ga (2)
- measured range: 100-637 K (5th-95th pct of 8 curves)
- papers: Preparation and thermoelectric properties of sintered type-II clathrates (K,Ba) 24 (Al,Sn) 136 | Predicting Ground-State Configurations and Electronic Properties of the Thermoelectric Clathrates Ba8AlxSi46–x and Sr8AlxSi46–x

## Al-C-Cr-O
- rank 1527 | 3 samples | 1 papers | 3 compositions
- compositions: (Al2O3)80.1(Cr3C2)19.9 (1); (Al2O3)70.13(Cr3C2)29.87 (1); (Al2O3)60.15(Cr3C2)39.85 (1)
- measured range: 297-871 K (5th-95th pct of 3 curves)
- papers: Heat conduction of composites and its dependence on the microstructure of Al2O3-Cr3 C2 composite

## Al-C-Ni-Ti
- rank 1528 | 3 samples | 1 papers | 3 compositions
- compositions: (TiC)76.88(Ni3Al)23.12 (1); (TiC)59.64(Ni3Al)40.36 (1); (TiC)35.65(Ni3Al)64.35 (1)
- measured range: 290-1316 K (5th-95th pct of 3 curves)
- papers: Densification and Thermal Properties of TiC-Ni3Al Composites Materials.

## Al-Co-O
- rank 1529 | 3 samples | 1 papers | 3 compositions
- compositions: Co63Al13O24 (1); Co66Al11O23 (1); Co74Al8O18 (1)
- measured range: 10-59 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al2CoO4 Fd-3m (227) mp-36447 [hull=0.000, icsd=1, PRIMARY]; AlCoO3 R-3 (148) mp-1178576 [hull=0.046, PRIMARY]; Al2CoO4 R3m (160) mp-694863 [hull=0.022]; Al2CoO4 Cm (8) mp-37621 [hull=0.027]; Al2CoO4 P3m1 (156) mp-705606 [hull=0.034]
- papers: Transport properties of ferromagnetic granular Co–Al–O films

## Al-Co-Si-Ti
- rank 1530 | 3 samples | 1 papers | 3 compositions
- compositions: Co2TiAl0.75Si0.25 (1); Co2TiAl0.25Si0.75 (1); Co2TiAl0.5Si0.5 (1)
- measured range: 10-1034 K (5th-95th pct of 9 curves)
- papers: Tuning the carrier concentration for thermoelectrical application in the quaternary Heusler compound Co2TiAl(1−x)Six

## Al-Cu-Ir
- rank 1531 | 3 samples | 1 papers | 3 compositions
- compositions: Al68.3Cu5Ir26.7_IAC_1_0 (1); Al67.3Cu6Ir26.7_IAC_1_0 (1); Al66.3Cu7Ir26.7_IAC_1_0 (1)
- measured range: 363-962 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al2CuIr Cmme (67) mp-1079890 [hull=0.000, icsd=1, PRIMARY]; Al2CuIr Immm (71) mp-1093789 [hull=2.590]
- papers: Anomalous effects of Cu-doping on structural and thermoelectric properties of the Al-Ir cubic quasicrystalline approximant

## Al-Fe-Mg-O
- rank 1532 | 3 samples | 2 papers | 3 compositions
- compositions: Mg0.4Al0.8Li0.30Fe1.50O4 (1); Mg0.5Al1.0Li0.25Fe1.25O4 (1); Mg0.75Fe0.41Al1.85O4 (1)
- dopant candidates (<5% at.): Li (2)
- measured range: 14-677 K (5th-95th pct of 3 curves; full span incl. outliers 14-738 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg14AlFeO16 Pmmm (47) mp-1036658 [hull=0.086, PRIMARY]; Mg30AlFeO32 P4/mmm (123) mp-1038379 [hull=0.040, PRIMARY]; Mg6AlFeO8 P4/mmm (123) mp-1033177 [hull=0.190, PRIMARY]; MgAlFeO4 Imma (74) mp-1222041 [hull=0.035, PRIMARY]; Mg14AlFeO16 P4/mmm (123) mp-1036709 [hull=0.108]
- papers: Thermoelectric power studies of magnesium and aluminium substituted lithium ferrites | Thermal Conductivity of MgO,Al2O3, MgAl2O4, andFe3O4Crystals from 3° to 300°K

## Al-Fe-Nb-Ru
- rank 1533 | 3 samples | 1 papers | 3 compositions
- compositions: Ru1.75Fe0.25NbAl (1); Ru1.62Fe0.38NbAl (1); Ru1.50Fe0.50NbAl (1)
- measured range: 11-298 K (5th-95th pct of 12 curves)
- papers: Physical properties of the full Heusler-type Ru2-Fe NbAl (x = 0.00–0.50) alloys

## Al-Fe-O-Sb
- rank 1534 | 3 samples | 1 papers | 3 compositions
- compositions: Al0.75Sb0.25FeO3 (1); Al0.25Sb0.75FeO3 (1); Al0.5Sb0.5FeO3 (1)
- measured range: 200-398 K (5th-95th pct of 3 curves)
- papers: Influence of Sb3+ Cations on the Structural, Magnetic and Electrical Properties of AlFeO3 Multiferroic Perovskite with Humidity Sensors Applicative Characteristics

## Al-Fe-V-W
- rank 1535 | 3 samples | 2 papers | 1 compositions
- compositions: Fe2V0.8W0.2Al (3)
- measured range: 11-818 K (5th-95th pct of 8 curves)
- papers: Thermoelectric performance of a metastable thin-film Heusler alloy | Stoichiometric and off-stoichiometric full Heusler \n<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:mrow><mml:msub><mml:mi>Fe</mml:mi><mml:mn>2</mml:mn></mml:msub><mml:msub><mml:mi mathvariant=\"normal\">V</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mo>−</mml:mo><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi mathvariant=\"normal\">W</mml:mi><mml:mi>x</mml:mi></mml:msub><mml:mi>Al</mml:mi></mml:mrow></mml:math>\n thermoelectric systems

## Al-Ga-Mn-Pd
- rank 1536 | 3 samples | 1 papers | 3 compositions
- compositions: Al64.9Pd20.7Mn8.4Ga6_IQC (1); Al62.9Pd20.7Mn8.4Ga8_IQC (1); Al60.9Pd20.7Mn8.4Ga10_IQC (1)
- measured range: 19-247 K (5th-95th pct of 3 curves)
- papers: Structural, tribological and resistivity studies of Ga substituted (Al71−xGax)Pd21Mn8 icosahedral and other intermetallic phases

## Al-In-Mn-Si
- rank 1537 | 3 samples | 1 papers | 3 compositions
- compositions: Mn2.7Cr0.3Si4Al1.4In0.6 (1); Mn2.7Cr0.3Si4Al1.2In0.8 (1); Mn2.7Cr0.3Si4AlIn (1)
- dopant candidates (<5% at.): Cr (3)
- measured range: 298-898 K (5th-95th pct of 15 curves)
- papers: Structural Investigation and Indium Substitution in the Thermoelectric Mn2.7Cr0.3Si4Al2−x In x Series

## Al-Ir-Rh
- rank 1538 | 3 samples | 1 papers | 3 compositions
- compositions: Al73.3Rh6.675Ir20.025_IAC (1); Al73.3Rh13.35Ir13.35_IAC (1); Al73.3Rh20.025Ir6.675_IAC (1)
- measured range: 299-903 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al2IrRh Fm-3m (225) mp-862694 [hull=0.000, PRIMARY]
- papers: Band engineering in Al-TM (TM=Rh, Ir) quasicrystalline approximants via alloying and enhancement of thermoelectric properties

## Al-La-O-Sr
- rank 1539 | 3 samples | 3 papers | 3 compositions
- compositions: SrLaAlO4 (1); LaSrAlO4 (1); (La0.7Sr0.3)(Al0.8Fe0.2)O3 (1)
- dopant candidates (<5% at.): Fe (1)
- measured range: 13-348 K (5th-95th pct of 3 curves; full span incl. outliers 13-1263 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2LaAlO5 Fmmm (69) mp-1218761 [hull=0.031, PRIMARY]; SrLa2Al2O7 I4/mmm (139) mp-1218238 [hull=0.020, PRIMARY]; SrLaAl3O7 Cmm2 (35) mp-1218220 [hull=0.000, PRIMARY]; SrLaAlO4 I4mm (107) mp-1218184 [hull=0.017, PRIMARY]
- papers: Strain Effect on Oxygen Evolution Reaction Activity of Epitaxial NdNiO<sub>3</sub> Thin Films | Tuning the electronic properties of epitaxial strained CaFeO3−δ thin films | Temperature-independent sensors based on perovskite-type oxides

## Al-Lu
- rank 1540 | 3 samples | 3 papers | 2 compositions
- compositions: LuAl3 (2); LuAl2 (1)
- measured range: 10-300 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LuAl2 Fd-3m (227) mp-1234 [hull=0.000, icsd=6, PRIMARY]; LuAl3 Pm-3m (221) mp-2805 [hull=0.000, icsd=4, PRIMARY]; LuAl Pbcm (57) mp-16507 [hull=0.000, icsd=1, PRIMARY]; Lu3Al2 P4_2/mnm (136) mp-16508 [hull=0.000, icsd=1, PRIMARY]; Lu3Al P6_3/mmc (194) mp-973266 [hull=0.007, PRIMARY]
- papers: Thermoelectric Properties of Yb1−x (Er,Lu) x Al3 Solid Solutions | Nernst effect of the intermediate valence compound YbAl3: revisiting the thermoelectric properties | Electrical resistivity, thermal conductivity and thermopower of nonmagnetic REAL2 compounds

## Al-Lu-Yb
- rank 1541 | 3 samples | 1 papers | 3 compositions
- compositions: Yb0.75Lu0.25Al3 (1); Yb0.5Lu0.5Al3 (1); Yb0.25Lu0.75Al3 (1)
- measured range: 80-300 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbLuAl4 F-43m (216) mp-1215433 [hull=0.023, PRIMARY]
- papers: Thermoelectric Properties of Yb1−x (Er,Lu) x Al3 Solid Solutions

## Al-Ni-U
- rank 1542 | 3 samples | 2 papers | 2 compositions
- compositions: UNiAl (2); UNi2Al3 (1)
- measured range: 12-283 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UAlNi P-62m (189) mp-1079086 [hull=0.158, icsd=7, PRIMARY]; UAl3Ni2 P6/mmm (191) mp-2903 [hull=0.108, icsd=5, PRIMARY]; U3Al19Ni5 Cmcm (63) mp-1196284 [hull=0.032, icsd=1, PRIMARY]; UAlNi4 F-43m (216) mp-16519 [hull=0.061, icsd=1, PRIMARY]; UAlNi Amm2 (38) mp-1079129 [hull=0.172, icsd=7]
- papers: Large thermoelectric power in several metallic compounds of cerium and uranium | Thermoelectric power of a UNiAl single crystal

## Al-Ni-Yb
- rank 1543 | 3 samples | 3 papers | 2 compositions
- compositions: YbNi0.8Al4.2 (2); YbNi3Al9 (1)
- measured range: 10-300 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb4Al23Ni6 C2/m (12) mp-18482 [hull=0.000, icsd=1, PRIMARY]; YbAl2Ni Cmcm (63) mp-12782 [hull=0.000, icsd=1, PRIMARY]; YbAlNi P-62m (189) mp-1078733 [hull=0.018, icsd=1, PRIMARY]; Yb2AlNi2 Immm (71) mp-1207023 [hull=0.000, PRIMARY]; YbAlNi Amm2 (38) mp-1215764 [hull=0.071]
- papers: YbNi0.8Al4.2: A novel intermetallic compound with an enhanced thermoelectric power factor | Intermediate valence behaviour of Yb in a new intermetallic compound YbNi0.8Al4.2 | Thin film growth of heavy fermion chiral magnet YbNi<sub>3</sub>Al<sub>9</sub>

## Al-Ru-U
- rank 1544 | 3 samples | 1 papers | 1 compositions
- compositions: URu2Al10 (3)
- measured range: 10-289 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UAlRu P-62m (189) mp-1080013 [hull=0.084, icsd=2, PRIMARY]; U(Al5Ru)2 Cmcm (63) mp-1193796 [hull=0.000, icsd=1, PRIMARY]
- papers: Crystal structure and physical properties of a new intermetallic compound URu2Al10

## Al-Sn-Yb
- rank 1545 | 3 samples | 1 papers | 3 compositions
- compositions: YbAl2.8Sn0.2 (1); YbAl2.5Sn0.5 (1); YbAl2.7Sn0.3 (1)
- measured range: 299-674 K (5th-95th pct of 15 curves)
- papers: Influence of Sn substitution on the thermoelectric properties in YbAl3

## As-Ca-Fe-O-Ti
- rank 1546 | 3 samples | 1 papers | 1 compositions
- compositions: (Fe2As2)Ca4(Mg0.25Ti0.75)3O8 (3)
- dopant candidates (<5% at.): Mg (3)
- measured range: 11-299 K (5th-95th pct of 6 curves)
- papers: Thermoelectric properties of FeAs based superconductors, with thick perovskite- and Sm-O fluorite-type blocking layers

## As-Co
- rank 1547 | 3 samples | 3 papers | 3 compositions
- compositions: CoAs3 (1); CoAs2 (1); CoAs (1)
- measured range: 11-874 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CoAs Pnma (62) mp-583 [hull=0.000, icsd=9, PRIMARY]; CoAs3 Im-3 (204) mp-452 [hull=0.000, icsd=8, PRIMARY]; CoAs2 P2_1/c (14) mp-2715 [hull=0.000, icsd=5, PRIMARY]; Co2As P-62m (189) mp-18206 [hull=0.062, icsd=4, PRIMARY]; Co5As2 P6_3cm (185) mp-16316 [hull=0.075, icsd=1, PRIMARY]
- papers: Thermoelectric properties of CoSb3and related alloys | Electrical/thermal transport and electronic structure of the binary cobalt pnictides CoPn2 (Pn = As and Sb) | Properties of binary transition-metal arsenides (TAs)

## As-Cu-S-Zn
- rank 1548 | 3 samples | 1 papers | 1 compositions
- compositions: Cu10.0Zn1.8Fe0.2As2.7Sb1.3S13 (3)
- dopant candidates (<5% at.): Sb (3), Fe (3)
- measured range: 87-721 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zn3Cu6(AsS3)4 P1 (1) mp-1215617 [hull=0.010, PRIMARY]
- papers: Solvothermal Synthesis of Tetrahedrite: Speeding Up the Process of Thermoelectric Material Generation

## As-Cu-Se-Te
- rank 1549 | 3 samples | 1 papers | 3 compositions
- compositions: Cu27.5As12.5Te54Se6 (1); Cu25As15Te54Se6 (1); Cu30As10Te54Se6 (1)
- measured range: 300-375 K (5th-95th pct of 12 curves)
- papers: Thermal stability and thermoelectric properties of CuxAs40−xTe60−ySey semiconducting glasses

## As-Fe-Sr
- rank 1550 | 3 samples | 1 papers | 3 compositions
- compositions: K0.17Sr0.83Fe2As2 (1); K0.22Sr0.78Fe2As2 (1); K0.12Sr0.88Fe2As2 (1)
- dopant candidates (<5% at.): K (3)
- measured range: 12-319 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr(FeAs)2 I4/mmm (139) mp-4488 [hull=0.000, icsd=6, PRIMARY]; NaSr4(FeAs)10 I4/m (87) mp-1221018 [hull=0.000, PRIMARY]
- papers: Evidence of quantum criticality in the phase diagram ofKxSr1−xFe2As2from measurements of transport and thermoelectricity
