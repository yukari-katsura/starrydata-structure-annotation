# Host systems -- chunk 023 of 73

Ranks 1101-1150 by sample count. These 50 host systems cover 250 samples (0.48% of the TE set); cumulative through this chunk: 90.69%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Al-Mn-Ni
- rank 1101 | 5 samples | 1 papers | 1 compositions
- compositions: Ni2MnAl (5)
- measured range: 17-400 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnAlNi2 Fm-3m (225) mp-4922 [hull=0.000, icsd=3, PRIMARY]; Mn6Al31Ni2 Cmcm (63) mp-30179 [hull=0.030, icsd=1, PRIMARY]; MnAl2Ni P4/mmm (123) mp-1221656 [hull=0.000, PRIMARY]; MnAlNi6 P4/mmm (123) mp-1221740 [hull=0.106, PRIMARY]
- papers: Exchange bias effects in Heusler alloy Ni<sub>2</sub>MnAl/Fe bilayers

## Al-N-Ti
- rank 1102 | 5 samples | 3 papers | 4 compositions
- compositions: Ti2AlN (2); Ti4AlN2.9 (1); Al0.85Ti0.15N1.13 (1); Ti0.72Al0.28N (1)
- measured range: 10-469 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti2AlN P6_3/mmc (194) mp-1080056 [hull=0.000, icsd=6, PRIMARY]; Ti3AlN Pm-3m (221) mp-10675 [hull=0.017, icsd=1, PRIMARY]; TiAlN2 R-3m (166) mp-1217025 [hull=0.207, PRIMARY]
- papers: Electronic and thermal properties of Ti[sub 3]Al(C[sub 0.5],N[sub 0.5])[sub 2], Ti[sub 2]Al(C[sub 0.5],N[sub 0.5]) and Ti[sub 2]AlN | Development and electrical properties of wurtzite (Al,Ti)N materials for thin film thermistors | Zero temperature coefficient of resistance in back-end-of-the-line compatible titanium aluminum nitride films by atomic layer deposition

## Al-Nb-Ru
- rank 1103 | 5 samples | 2 papers | 2 compositions
- compositions: Ru2NbAl (4); Ru1.87Fe0.13NbAl (1)
- dopant candidates (<5% at.): Fe (1)
- measured range: 11-299 K (5th-95th pct of 14 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NbAlRu2 Fm-3m (225) mp-11537 [hull=0.000, icsd=1, PRIMARY]
- papers: Ferromagnetically correlated clusters in semimetallic \n<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:mrow><mml:msub><mml:mi>Ru</mml:mi><mml:mn>2</mml:mn></mml:msub><mml:mi>NbAl</mml:mi></mml:mrow></mml:math>\n Heusler alloy and its thermoelectric properties | Physical properties of the full Heusler-type Ru2-Fe NbAl (x = 0.00–0.50) alloys

## Al-Sb-Sr
- rank 1104 | 5 samples | 2 papers | 4 compositions
- compositions: Sr5Al2Sb6 (2); Sr3AlSb3 (1); Sr3Al0.95Sb3Zn0.05 (1); Sr5Al1.95Zn0.05Sb6 (1)
- dopant candidates (<5% at.): Zn (2)
- measured range: 297-1020 K (5th-95th pct of 13 curves)
- [ref 1] TEDesignLab / ICSD: Sr3AlSb3 Cmce (64) mp-17667 [hull=0.000, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Sr5(AlSb3)2 Pnma (62) mp-28392 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric Properties and Electronic Structure of the Zintl-Phase Sr3AlSb3 | Thermoelectric properties and electronic structure of the Zintl phase Sr5Al2Sb6

## Al-Sc
- rank 1105 | 5 samples | 2 papers | 5 compositions
- compositions: ScAl3 (1); Yb0.15Sc0.85Al2 (1); Yb0.05Sc0.95Al2 (1); Yb0.1Sc0.9Al2 (1); ScAl2 (1)
- dopant candidates (<5% at.): Yb (3)
- measured range: 10-350 K (5th-95th pct of 16 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ScAl2 Fd-3m (227) mp-813 [hull=0.000, icsd=7, PRIMARY]; ScAl3 Pm-3m (221) mp-2121 [hull=0.000, icsd=5, PRIMARY]; Sc2Al P6_3/mmc (194) mp-11220 [hull=0.000, icsd=3, PRIMARY]; ScAl Pm-3m (221) mp-331 [hull=0.000, icsd=2, PRIMARY]; Sc3Al P6_3/mmc (194) mp-862259 [hull=0.000, PRIMARY]
- papers: Synthesis, crystal structure, and thermoelectric properties of the YbAl3-ScAl3 solid solution | Enhanced thermoelectric power factor in Yb1−xScxAl2 alloys using chemical pressure tuning of the Yb valence

## Al-Sr
- rank 1106 | 5 samples | 1 papers | 1 compositions
- compositions: SrAl4 (5)
- measured range: 13-299 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrAl4 I4/mmm (139) mp-2775 [hull=0.000, icsd=4, PRIMARY]; SrAl2 Imma (74) mp-22318 [hull=0.000, icsd=3, PRIMARY, AMBIGUOUS]; Sr8Al7 P2_13 (198) mp-11224 [hull=0.000, icsd=3, PRIMARY]; Sr2Al C2/c (15) mp-1102672 [hull=0.127, icsd=2, PRIMARY]; Sr5Al9 R-3m (166) mp-1109 [hull=0.000, icsd=2, PRIMARY]
- papers: Characteristic Fermi surfaces and charge density wave in SrAl4 and related compounds with the BaAl4-type tetragonal structure

## Am-O
- rank 1107 | 5 samples | 3 papers | 2 compositions
- compositions: AmO2 (3); Am2O3 (2)
- measured range: 300-1468 K (5th-95th pct of 5 curves; full span incl. outliers 300-1797 K)
- papers: Fundamental Research on Actinide Materials for Sustainable Fuel Cycles in JAEA | Thermophysical properties of NpO2, AmO2 and CmO2 | Modelling thermal conductivity and self-irradiation effects in mixed oxide fuels

## As-Ce-Ru
- rank 1108 | 5 samples | 2 papers | 1 compositions
- compositions: CeRu4As12 (5)
- measured range: 10-322 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(As3Ru)4 Im-3 (204) mp-1021508 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric properties of the Kondo semiconductor CeRu4As12 prepared under high pressure | Non-Fermi liquid behavior in the filled skutterudite compound CeRu4As12

## As-Co-Sb
- rank 1109 | 5 samples | 3 papers | 5 compositions
- compositions: CoSb2.7As0.3 (1); CoSb2.63As0.37 (1); Co0.99Ni0.01Sb2.75As0.25 (1); Yb0.30Co2.9Fe0.8Sb9As3.1 (1); CoAsSb (1)
- dopant candidates (<5% at.): Ni (1), Fe (1), Yb (1)
- solid-solution axis: As/(As+Sb) spans 0.08-0.50 (median 0.12) over 5 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 23-996 K (5th-95th pct of 13 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co2SbAs P-6m2 (187) mp-1226441 [hull=0.055, PRIMARY]
- papers: Thermoelectric properties of CoSb3and related alloys | High-temperature thermoelectric properties of p-type skutterudites Ba0.15Yb x Co3FeSb12 and Yb y Co3FeSb9As3 | Thermoelectric Properties of CoAsSb: An Experimental and Theoretical Study

## As-Fe-H-La-O-P
- rank 1110 | 5 samples | 1 papers | 5 compositions
- compositions: LaFeAs0.6P0.4O0.75H0.25 (1); LaFeAs0.4P0.6O0.90H0.30 (1); LaFeAs0.8P0.2O0.75H0.25 (1); LaFeAs0.8P0.2O0.70H0.30 (1); LaFeAs0.6P0.4O0.90H0.30 (1)
- solid-solution axis: As/(As+P) spans 0.40-0.80 (median 0.60) over 5 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-298 K (5th-95th pct of 5 curves)
- papers: Three superconducting phases with different categories of pairing in hole- and electron-doped \nLaFeAs1−xPxO

## As-Fe-N-O-Th
- rank 1111 | 5 samples | 1 papers | 5 compositions
- compositions: ThFeAsN0.7O0.3 (1); ThFeAsN0.6O0.4 (1); ThFeAsN0.4O0.6 (1); ThFeAsN0.8O0.2 (1); ThFeAsN0.5O0.5 (1)
- solid-solution axis: As/(As+N) spans 0.56-0.71 (median 0.62) over 5 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-35 K (5th-95th pct of 5 curves)
- papers: Peculiar phase diagram with isolated superconducting regions in ThFeAsN<sub>1−<i>x</i> </sub>O<sub> <i>x</i> </sub>

## As-Fe-O-Sr-V
- rank 1112 | 5 samples | 2 papers | 2 compositions
- compositions: Sr2VFeAsO3 (4); SrVFeAsO3 (1)
- measured range: 11-297 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2VFeAsO3 P4/nmm (129) mp-1106248 [hull=0.087, icsd=3, PRIMARY]
- papers: Annealing induced superconductivity in perovskite-related iron-based mixed anion compounds Sr<sub>2</sub>VFeAsO<sub>3−δ</sub> | Superconducting critical current density enhanced to 285 A cm<sup>−2</sup> for Sr<sub>2</sub>VFeAsO<sub>3−<i>δ</i> </sub> tapes fabricated by ex situ powder-in-tube process

## As-Re
- rank 1113 | 5 samples | 2 papers | 5 compositions
- compositions: Re3As6.70In0.30 (1); Re3Sn0.1As6.9 (1); Re3Sn0.2As6.8 (1); Ni0.05Re3Sn0.2As6.8 (1); Co0.05Re3Sn0.2As6.8 (1)
- dopant candidates (<5% at.): Sn (4), In (1), Ni (1), Co (1)
- measured range: 76-963 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Re3As7 Im-3m (229) mp-2473 [hull=0.000, icsd=4, PRIMARY]; ReAs3 Fm-3m (225) mp-1186907 [hull=0.650, PRIMARY]
- papers: Synthesis and thermoelectric properties of Re3As6.6In0.4with Ir3Ge7crystal structure | New Ternary Arsenides for High-Temperature Thermoelectric Applications

## B-Co-Mg
- rank 1114 | 5 samples | 1 papers | 2 compositions
- compositions: (MgB2)1.5Co0.5 (4); (MgB2)1.7Co0.3 (1)
- measured range: 10-298 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg14CoB Amm2 (38) mp-1028436 [hull=0.241, PRIMARY]; Mg6CoB Amm2 (38) mp-1022088 [hull=0.144, PRIMARY]; Mg14CoB P-6m2 (187) mp-1028392 [hull=0.286]
- papers: Co-addition into MgB2: The structural and electronic properties of (MgB2)2−xCox

## B-Eu
- rank 1115 | 5 samples | 3 papers | 3 compositions
- compositions: EuB6 (3); Eu0.9La0.1B6 (1); Eu0.8La0.2B6 (1)
- dopant candidates (<5% at.): La (2)
- measured range: 10-297 K (5th-95th pct of 5 curves; full span incl. outliers 10-1317 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): EuB6 Pm-3m (221) mp-1077914 [hull=0.000, icsd=13, PRIMARY]; EuB12 Fm-3m (225) mp-1096955 [hull=0.105, PRIMARY]
- papers: Thermoelectric power study of | The effect of structural defects on thermal conductivity polycrystalline AlB12 and EuB6 | Thermal conductivity ofEuB6

## B-Ni-U
- rank 1116 | 5 samples | 2 papers | 1 compositions
- compositions: UNi4B (5)
- measured range: 10-296 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U2(Ni7B2)3 Fm-3m (225) mp-10130 [hull=0.000, icsd=1, PRIMARY]; UNiB4 I4/mmm (139) mp-972320 [hull=0.000, icsd=1, PRIMARY]
- papers: Large thermoelectric power in several metallic compounds of cerium and uranium | Magnetic phase diagram and low-dimensional excitations of hexagonal UNi4B

## B-Th
- rank 1117 | 5 samples | 1 papers | 2 compositions
- compositions: ThB4 (3); ThB6 (2)
- measured range: 78-686 K (5th-95th pct of 14 curves; full span incl. outliers 78-746 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ThB6 Pm-3m (221) mp-1756 [hull=0.000, icsd=9, PRIMARY]; ThB12 Fm-3m (225) mp-12570 [hull=0.007, icsd=2, PRIMARY]; Th3B Pm-3m (221) mp-979412 [hull=0.737, PRIMARY]; Th2B15 P4/mmm (123) mp-1217367 [hull=0.009, PRIMARY]
- papers: Electrical Properties of Thorium Borides

## Ba-Bi-K-O
- rank 1118 | 5 samples | 3 papers | 3 compositions
- compositions: Ba0.62K0.38BiO3 (2); Ba0.6K0.4BiO3 (2); (K1.00)(Ba1.00)3(Bi0.89Na0.11)4O12 (1)
- dopant candidates (<5% at.): Na (1)
- measured range: 13-299 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): KBa4Bi3O I4/mcm (140) mp-23571 [hull=0.000, icsd=2, PRIMARY]; K2Ba(BiO3)3 P-3m1 (164) mp-1223672 [hull=0.024, PRIMARY]; KBa2(BiO3)3 P-3m1 (164) mp-1223518 [hull=0.009, PRIMARY]; KBa2Bi2O7 I4mm (107) mp-1223506 [hull=0.000, PRIMARY]; KBa2Bi2O9 P-3m1 (164) mp-1223544 [hull=0.200, PRIMARY]
- papers: Thermoelectric power of superconducting Ba-K-Bi-O crystals | Thermoelectric power ofBa1−xKxBiO3 | Hydrothermal Synthesis, Crystal Structure, and Superconductivity of a Double-Perovskite Bi Oxide

## Ba-Ca-Mg-Si
- rank 1119 | 5 samples | 1 papers | 1 compositions
- compositions: Ba1.9Ca2.4Mg9.7Si7 (5)
- measured range: 14-983 K (5th-95th pct of 8 curves)
- papers: Thermoelectric Properties of Ba1.9Ca2.4Mg9.7Si7: A New Silicide Zintl Phase with the Zr2Fe12P7Structure Type

## Ba-Cu-O-Yb
- rank 1120 | 5 samples | 1 papers | 4 compositions
- compositions: YbBa1.9Sr0.1Cu3O7 (2); YbBa1.7Sr0.3Cu3O7 (1); YbBa1.8Sr0.2Cu3O7 (1); YbBa2Cu3O7 (1)
- dopant candidates (<5% at.): Sr (4)
- measured range: 72-290 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaYb2CuO5 Pnma (62) mp-6323 [hull=0.000, icsd=3, PRIMARY]; Ba4Yb(CuO3)3 Pm-3n (223) mp-653337 [hull=0.000, icsd=1, PRIMARY]; Ba2Yb(CuO2)4 Cmmm (65) mp-15039 [hull=0.008, icsd=1, PRIMARY]; Ba10Yb2Cu4O17 I4/mmm (139) mp-1229250 [hull=0.340, PRIMARY]; Ba2YbCu3O7 Pmmm (47) mp-1214570 [hull=0.040, PRIMARY]
- papers: Structure and superconductivity studies on LnBa2−xSrxCu3O7 (Ln=Yb and Lu; 0.0≤x≤0.5)

## Ba-Cu-P-Zn
- rank 1121 | 5 samples | 1 papers | 1 compositions
- compositions: Ba8Cu12.8Zn11.2P28.8 (5)
- measured range: 10-347 K (5th-95th pct of 5 curves)
- papers: Breaking the Tetra-Coordinated Framework Rule: New Clathrate Ba8\n                        M\n                        24\nP28+δ\n                        \n (M\n=Cu/Zn)

## Ba-La-O-Zr
- rank 1122 | 5 samples | 1 papers | 5 compositions
- compositions: Ba0.7La0.3Y0.02Zr0.38Mn0.2Fe0.2Co0.2O3 (1); Ba0.7La0.3Y0.06Zr0.34Mn0.2Fe0.2Co0.2O3 (1); Ba0.7La0.3Zr0.4Mn0.2Fe0.2Co0.2O3 (1); Ba0.7La0.3Y0.04Zr0.36Mn0.2Fe0.2Co0.2O3 (1); Ba0.7La0.3Y0.08Zr0.32Mn0.2Fe0.2Co0.2O3 (1)
- dopant candidates (<5% at.): Mn (5), Fe (5), Co (5), Y (4)
- measured range: 297-1073 K (5th-95th pct of 5 curves)
- papers: High-Performance La0.5Ba0.5Co1/3Mn1/3Fe1/3O3−δ-BaZr1−zYzO3−δ Cathode Composites via an Exsolution Mechanism for Protonic Ceramic Fuel Cells

## Ba-Mn-Nd-O
- rank 1123 | 5 samples | 3 papers | 2 compositions
- compositions: NdBaMn2O6 (4); Nd0.5Ba0.5MnO3 (1)
- measured range: 21-398 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaNd2Mn2O7 I4/mmm (139) mp-18861 [hull=0.002, icsd=4, PRIMARY]; BaNdMn2O6 P4/mmm (123) mp-25004 [hull=0.033, icsd=2, PRIMARY]; Ba5Nd8Mn4O21 I4/m (87) mp-19460 [hull=0.000, icsd=1, PRIMARY]
- papers: Physical properties and crystal structure analysis of double-perovskite \n<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:mrow><mml:msub><mml:mi>NdBaMn</mml:mi><mml:mn>2</mml:mn></mml:msub><mml:msub><mml:mi mathvariant=\"normal\">O</mml:mi><mml:mn>6</mml:mn></mml:msub></mml:mrow></mml:math>\n by using single crystals | Variation of structural and magnetic properties of mixed-valent manganites through A-site cationic ordering | <i>A</i>-site Randomness Effect on Structural and Physical Properties of Ba-based Perovskite Manganites

## Ba-Nd-O-Ti
- rank 1124 | 5 samples | 2 papers | 5 compositions
- compositions: Nd0.3Ba0.7TiO3 (1); Nd0.4Ba0.6TiO3 (1); Nd0.7Ba0.3TiO3 (1); Ba6Nd8Ti18O54 (1); Ba5.19Nd8.54Ti18O54 (1)
- measured range: 81-1012 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaNd2Ti3O10 Cmcm (63) mp-6622 [hull=0.008, icsd=5, PRIMARY]; Ba6Nd2Ti4O17 P6_3/mmc (194) mp-16662 [hull=0.026, icsd=1, PRIMARY]; BaNd2Ti3O10 P2_1/m (11) mp-6285 [hull=0.001, icsd=2]
- papers: Band filling dependence of the electrical transport of Nd1−xAxTiO3 (A=Ca, Sr and Ba) | Ba6−3x Nd8+2x Ti18O54 Tungsten Bronze: A New High-Temperature n-Type Oxide Thermoelectric

## Ba-O-Si-Ti
- rank 1125 | 5 samples | 1 papers | 1 compositions
- compositions: Ba2TiSi2O8 (5)
- measured range: 295-871 K (5th-95th pct of 5 curves)
- [ref 1] TEDesignLab / ICSD: Ba2Ti(SiO4)2 P4bm (100) mp-6081 [hull=0.000, icsd=8, PRIMARY]; BaTi(SiO3)3 P-6c2 (188) mp-6661 [hull=0.000, icsd=7, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ba4Ti6Si4O25 P2/c (13) mp-1214645 [hull=0.052, PRIMARY]; Ba8Ti3Co(SiO4)8 P4 (75) mp-1228423 [hull=0.013, PRIMARY]; BaTi(SiO3)3 P31c (159) mp-1198599 [hull=0.001, icsd=3]
- papers: Investigations on the thermal and piezoelectric properties of fresnoite Ba2TiSi2O8 single crystals

## Ba-O-Zr
- rank 1126 | 5 samples | 5 papers | 2 compositions
- compositions: BaZrO3 (4); BaZr0.8Co0.2O3 (1)
- dopant candidates (<5% at.): Co (1)
- measured range: 276-1295 K (5th-95th pct of 5 curves; full span incl. outliers 276-1373 K)
- [ref 1] TEDesignLab / ICSD: BaZrO3 Pm-3m (221) mp-3834 [hull=0.000, icsd=8, PRIMARY]; Ba2ZrO4 I4/mmm (139) mp-8335 [hull=0.000, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ba2ZrO6 P4/mmm (123) mp-1228078 [hull=0.337, PRIMARY]; Ba2Zr7O16 R-3 (148) mp-769802 [hull=0.028, PRIMARY]; Ba3Zr2O7 I4/mmm (139) mp-755895 [hull=0.000, PRIMARY]; Ba4CaZr5O15 I-42m (121) mp-1228424 [hull=0.028, PRIMARY]; BaZrO3 I4/mcm (140) mp-1019544 [hull=0.000, icsd=1]
- papers: Thermoelectric properties of perovskite type barium molybdate | Thermoelectric properties of perovskite type strontium ruthenium oxide | Zirconates as New Materials for Thermal Barrier Coatings

## Ba-Pd-Sb-Sn
- rank 1127 | 5 samples | 1 papers | 2 compositions
- compositions: Ba0.97Pd4Sn6.90Sb4.97 (4); Ba1.0Pd4Sn7.1Sb5.2 (1)
- measured range: 11-356 K (5th-95th pct of 6 curves)
- papers: Ba x Pd4Sn y Sb12−y : A New Palladium-Containing Skutterudite

## Bi-Ca-Co-O-Sr
- rank 1128 | 5 samples | 4 papers | 3 compositions
- compositions: Bi2SrCaCo2O8 (2); Bi2Sr1.6Ca1.4Co2O9 (2); Bi1.8Pb0.2Sr2Ca2Co3O12 (1)
- dopant candidates (<5% at.): Pb (1)
- measured range: 10-752 K (5th-95th pct of 11 curves; full span incl. outliers 10-870 K)
- papers: Exotic reinforcement of thermoelectric power driven by Ca doping in layered Bi2Sr2−xCaxCo2Oy | Intrinsically modified thermoelectric performance of alkaline-earth isovalently substituted [Bi2AE2O4][CoO2]y single crystals | Fabrication and properties of textured Bi-based cobaltite thermoelectric rods by zone melting

## Bi-Ca-Cu-O-Pb-Sr
- rank 1129 | 5 samples | 1 papers | 5 compositions
- compositions: Bi1.7Pb2.925Nd0.075Sr2Ca3Cu4O12 (1); Bi1.7Pb3Sr2Ca3Cu4O12 (1); Bi1.7Pb2.975Nd0.025Sr2Ca3Cu4O12 (1); Bi1.7Pb2.950Nd0.050Sr2Ca3Cu4O12 (1); Bi1.7Pb2.9Nd0.1Sr2Ca3Cu4O12 (1)
- dopant candidates (<5% at.): Nd (4)
- measured range: 10-300 K (5th-95th pct of 10 curves)
- papers: Thermoelectric power and thermal conduction studies on the Nd substituted BPSCCO (2234) superconductors

## Bi-Co-Sn-Zr
- rank 1130 | 5 samples | 2 papers | 4 compositions
- compositions: ZrCoBi0.65Sb0.15Sn0.20 (2); ZrCoBi0.80Sn0.20 (1); ZrCoBi0.70Sb0.10Sn0.20 (1); ZrCoBi0.75Sb0.05Sn0.20 (1)
- dopant candidates (<5% at.): Sb (4)
- measured range: 298-976 K (5th-95th pct of 24 curves)
- papers: Discovery of ZrCoBi based half Heuslers with high thermoelectric conversion efficiency | Realizing high conversion efficiency of Mg3Sb2-based thermoelectric materials

## Bi-Dy-Pd
- rank 1131 | 5 samples | 5 papers | 2 compositions
- compositions: DyPdBi (4); DyPd2Bi (1)
- measured range: 10-300 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DyBiPd F-43m (216) mp-1009543 [hull=0.000, icsd=1, PRIMARY]; Dy5BiPd2 I4/mcm (140) mp-1212882 [hull=0.000, PRIMARY]
- papers: Physical properties of rare-earth-based Heusler phases REPdZ and REPd/sub 2/Z (Z = Sb,Bi) | Magnetic and transport properties of the rare-earth-based Heusler phasesRPdZandRPd2Z(Z=Sb,Bi) | Magnetic and transport properties of rare-earth-based half-Heusler phasesRPdBi: Prospective systems for topological quantum phenomena

## Bi-I-S
- rank 1132 | 5 samples | 1 papers | 2 compositions
- compositions: Bi13S18I2 (3); (Bi13S18I2)0.98(BiCl3)0.02 (2)
- dopant candidates (<5% at.): Cl (2)
- measured range: 313-788 K (5th-95th pct of 25 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BiSI Pnma (62) mp-23514 [hull=0.003, icsd=2, PRIMARY]; Bi19(S9I)3 R3 (146) mp-1227984 [hull=0.011, PRIMARY]
- papers: Manipulating Band Structure through Reconstruction of Binary Metal Sulfide for High-Performance Thermoelectrics in Solution-Synthesized Nanostructured Bi13\nS18\nI2

## Bi-Ir-O-Y
- rank 1133 | 5 samples | 1 papers | 3 compositions
- compositions: Y1.2Bi0.8Ir2O7 (2); Y0.8Bi1.2Ir2O7 (2); Y1.4Bi0.6Ir2O7 (1)
- measured range: 14-347 K (5th-95th pct of 5 curves)
- papers: Spin–Glass-like Transition and Hall Resistivity of Y2-xBixIr2O7

## Bi-La-Mn-O
- rank 1134 | 5 samples | 3 papers | 4 compositions
- compositions: LaBiMn2O6.20 (2); LaBiMn1.5Co0.5O6.04 (1); La0.55Bi0.3K0.15MnO3 (1); La0.6Bi04Mn0.6Ni0.4O2.9 (1)
- dopant candidates (<5% at.): Co (1), K (1), Ni (1)
- measured range: 14-400 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La3Mn8BiO20 Pm (6) mp-1223206 [hull=0.002, PRIMARY]; LaMn2BiO6 Pmc2_1 (26) mp-1222893 [hull=0.015, PRIMARY]; LaMn4(BiO4)3 Pm (6) mp-1222881 [hull=0.019, PRIMARY]; LaMn8Bi3O20 Pm (6) mp-1222927 [hull=0.001, PRIMARY]
- papers: Enhancement of ferromagnetism by Co and Ni substitution in the perovskite LaBiMn2O6+δ | The room temperature inflection of magnetism and anomalous thermoelectric power in lacunar compounds of La0.85−xBixK0.15MnO3 | Incoherent effect of Fe and Ni substitutions in the ferromagnetic-insulator La0.6Bi0.4MnO3+δ

## Bi-Mn-S
- rank 1135 | 5 samples | 2 papers | 4 compositions
- compositions: MnBi4S7 (2); MnBi4S6.86 (1); Mn1.03Bi4S7 (1); MnBi4S6.51Se0.35 (1)
- dopant candidates (<5% at.): Se (1)
- measured range: 300-772 K (5th-95th pct of 20 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnBi4S7 C2/m (12) mp-1095372 [hull=0.010, icsd=1, PRIMARY]
- papers: XBi\n            4\n            S\n            7\n            (X = Mn, Fe): New Cost‐Efficient Layered\n            n\n            ‐Type Thermoelectric Sulfides with Ultralow Thermal Conductivity | Thermoelectricity of n-type MnBi4S7-7xSe7x solid solution

## Bi-Mo-Se-Te
- rank 1136 | 5 samples | 1 papers | 5 compositions
- compositions: MoBi2(Se0.8Te0.2)5 (1); MoBi2(Se0.4Te0.6)5 (1); MoBi2(Se0.2Te0.8)5 (1); MoBi2(Se0.5Te0.5)5 (1); MoBi2(Se0.3Te0.7)5 (1)
- solid-solution axis: Se/(Se+Te) spans 0.20-0.80 (median 0.40) over 5 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 303-498 K (5th-95th pct of 5 curves)
- papers: Synthesis of fibrous reticulate nanocrystalline n-type MoBi2(Se1−xTex)5 thin films: Thermocooling applications

## Bi-Nb-O-Sr
- rank 1137 | 5 samples | 1 papers | 1 compositions
- compositions: SrBi2Nb2O9 (5)
- measured range: 12-292 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrNb2Bi2O9 Cmc2_1 (36) mp-23614 [hull=0.000, icsd=2, PRIMARY]
- papers: Thermal conductivity of SrBi2Nb2O9 ferroelectric thin films

## Bi-Nd-O-Ru
- rank 1138 | 5 samples | 1 papers | 2 compositions
- compositions: NdBiRu2O7 (3); Nd1.4Bi0.6Ru2O7 (2)
- measured range: 306-999 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd3Bi(Ru2O7)2 R-3m (166) mp-1220276 [hull=0.000, PRIMARY]; NdBi3(Ru2O7)2 R-3m (166) mp-1220207 [hull=0.003, PRIMARY]; NdBiRu2O7 Imma (74) mp-1220214 [hull=0.003, PRIMARY]
- papers: Thermoelectric properties of Ln2−xBixRu2O7 pyrochlores (Ln=Nd and Yb)

## Bi-O-Ru-Yb
- rank 1139 | 5 samples | 1 papers | 2 compositions
- compositions: YbBiRu2O7 (3); Yb1.4Bi0.6Ru2O7 (2)
- measured range: 300-999 K (5th-95th pct of 5 curves)
- papers: Thermoelectric properties of Ln2−xBixRu2O7 pyrochlores (Ln=Nd and Yb)

## Bi-Pb-S-Tl
- rank 1140 | 5 samples | 1 papers | 5 compositions
- compositions: (TlBiS2)0.2(PbS)1.6 (1); (TlBiS2)0.5PbS (1); (TlBiS2)0.9(PbS)0.2 (1); (TlBiS2)0.3(PbS)1.4 (1); (TlBiS2)0.7(PbS)0.6 (1)
- measured range: 78-299 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TlBiPbS3 Imm2 (44) mp-1216860 [hull=0.042, PRIMARY]
- papers: Thermoelectric Properties of the TlBiS2-PbS Alloys

## C-Cr
- rank 1141 | 5 samples | 3 papers | 4 compositions
- compositions: Cr3C2 (2); (Cr2AlC)32(Cr7C3)68 (1); (Cr3C2)90.07(SiC)9.93 (1); (Cr3C2)81.11(SiC)18.89 (1)
- dopant candidates (<5% at.): Si (2), Al (1)
- measured range: 298-877 K (5th-95th pct of 5 curves; full span incl. outliers 298-1473 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cr23C6 Fm-3m (225) mp-723 [hull=0.000, icsd=11, PRIMARY]; Cr3C2 Pnma (62) mp-20937 [hull=0.000, icsd=9, PRIMARY]; Cr7C3 Pnma (62) mp-19855 [hull=0.000, icsd=4, PRIMARY]; CrC Fm-3m (225) mp-579 [hull=0.256, icsd=3, PRIMARY]; Cr3C Pnma (62) mp-1189286 [hull=0.015, icsd=3, PRIMARY]
- papers: Thermal diffusivity of plasma-sprayed Cr3C2–NiCr coatings | Effect of Cr7C3 on the mechanical, thermal, and electrical properties of Cr2AlC | Thermal conduction in Cr3C2/SiC composite

## C-Ga-Mn
- rank 1142 | 5 samples | 2 papers | 5 compositions
- compositions: Mn2.95Fe0.05GaC (1); Mn2.95Cr0.05GaC (1); Mn3GaC (1); Mn3Ga0.95Zn0.05C (1); Mn3Ga0.85Zn0.15C (1)
- dopant candidates (<5% at.): Zn (2), Fe (1), Cr (1)
- measured range: 80-543 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn3GaC Pm-3m (221) mp-21313 [hull=0.000, icsd=5, PRIMARY]
- papers: Transport Properties of Ternary Magnetic Compounds Mn3-xMxGaC (M=Cr and Fe) | Transport properties of the intermetallic compounds Mn3Ga1−xZnxC

## C-H
- rank 1143 | 5 samples | 3 papers | 3 compositions
- compositions: C10H14S (3); CsC24(C2H4)1.4 (1); (C42H62S4)(FeCl3)0.012 (1)
- dopant candidates (<5% at.): S (4), Cs (1), Cl (1), Fe (1)
- measured range: 16-480 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HC2 P2_1/c (14) mp-603334 [hull=0.106, icsd=2, PRIMARY]; BH17C6NCl P2_1 (4) mp-1204476 [hull=0.124, icsd=1, PRIMARY]; AlBH15C4N Pnma (62) mp-1195069 [hull=0.180, icsd=1, PRIMARY]; CuSi2BiP3(H3C)15 Fdd2 (43) mp-1204513 [hull=0.056, icsd=1, PRIMARY]; GaH19C8 R-3c (167) mp-605088 [hull=0.092, icsd=1, PRIMARY]
- papers: Thermoelectric Properties of Cesium&ndash;Graphite Intercalation Compounds | Multi-heterojunctioned plastics with high thermoelectric figure of merit | Highly anisotropic P3HT films with enhanced thermoelectric performance via organic small molecule epitaxy

## C-H-I-N-Sn
- rank 1144 | 5 samples | 1 papers | 1 compositions
- compositions: CH3NH3SnI3 (5)
- measured range: 11-298 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sn3H28C9IN P2_13 (198) mp-1199776 [hull=0.129, icsd=1, PRIMARY]; SnH20C7IN P2_1/c (14) mp-1203750 [hull=0.139, icsd=1, PRIMARY]; SnH5CI3N2 Amm2 (38) mp-1102654 [hull=0.032, icsd=1, PRIMARY]; SnH8C2I3N Pna2_1 (33) mp-1200236 [hull=0.056, icsd=1, PRIMARY]; SnH6CI3N P1 (1) mp-995238 [hull=0.031, PRIMARY]
- papers: Charge-transport in tin-iodide perovskite CH3NH3SnI3: origin of high conductivity

## C-H-O
- rank 1145 | 5 samples | 4 papers | 2 compositions
- compositions: (C14H14O5S2)63.12(C2H6O2)36.88 (4); C6H7N(C7H8SO3)0.5 (1)
- dopant candidates (<5% at.): S (5), N (1)
- measured range: 101-320 K (5th-95th pct of 16 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnH9C4NO6 Pnma (62) mp-656241 [hull=0.101, icsd=7, PRIMARY]; H3CO3 P2_1/c (14) mp-1194227 [hull=0.063, icsd=3, PRIMARY]; CuH11C5NO6 C2/c (15) mp-698401 [hull=0.204, icsd=2, PRIMARY]; CoH9C4NO6 Pnma (62) mp-743542 [hull=0.115, icsd=2, PRIMARY]; CuH9C5NO5 P-1 (2) mp-1201220 [hull=0.218, icsd=2, PRIMARY]
- papers: Investigating thermoelectric properties of doped polyaniline nanowires | Thermoelectric Performance of Poly(3,4-Ethylenedioxy-thiophene)/Poly(Styrenesulfonate) Pellets and Films | Highly conducting free-standing poly(3,4-ethylenedioxythiophene)/poly(styrenesulfonate) films with improved thermoelectric performances

## C-Mo-Ti
- rank 1146 | 5 samples | 1 papers | 5 compositions
- compositions: (Mo)79.37(TiC)20.63 (1); (Mo)68.12(TiC)31.88 (1); (Mo)29.94(TiC)70.06 (1); (Mo)89.97(TiC)10.03 (1); (Mo)56.18(TiC)43.82 (1)
- measured range: 293-1082 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiMoC2 R-3m (166) mp-1216711 [hull=0.045, PRIMARY]
- papers: Microstructure and thermal conductivity of Mo–TiC cermets processed by hot isostatic pressing

## C-Ni-Sm
- rank 1147 | 5 samples | 1 papers | 1 compositions
- compositions: SmNiC2 (5)
- measured range: 10-299 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SmNiC2 Amm2 (38) mp-999144 [hull=0.000, icsd=2, PRIMARY]; Sm2Ni22C3 Cmce (64) mp-1199812 [hull=0.012, icsd=1, PRIMARY]
- papers: Magnon gap formation and charge density wave effect on thermoelectric properties in the SmNiC2compound

## C-O
- rank 1148 | 5 samples | 2 papers | 1 compositions
- compositions: CO2 (5)
- measured range: 10-119 K (5th-95th pct of 5 curves; full span incl. outliers 10-347 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CO2 Pa-3 (205) mp-20066 [hull=0.000, icsd=6, PRIMARY]; CO P2_13 (198) mp-11875 [hull=0.665, icsd=1, PRIMARY, AMBIGUOUS]; C61O2 P2_1/c (14) mp-1197923 [hull=0.365, icsd=1, PRIMARY]; CrC32O5 P2_1/c (14) mp-1200737 [hull=1.231, icsd=1, PRIMARY]; Cr(C7O2)3 P2_1/c (14) mp-1198466 [hull=1.172, icsd=1, PRIMARY]
- papers: Low-temperature thermal conductivity of cryocrystals formed by linear three-atom molecules | Thickness dependence of magnetic and transport properties of chromium dioxide (CrO/sub 2/) strained epitaxial thin films

## C-O-Si
- rank 1149 | 5 samples | 1 papers | 3 compositions
- compositions: SiOC (3); (SiOC)97.77(BN)2.23 (1); (SiOC)89.37(BN)10.63 (1)
- dopant candidates (<5% at.): B (2), N (2)
- measured range: 303-872 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Si17CO34 Fd-3m (227) mp-1204567 [hull=0.168, icsd=1, PRIMARY]; Si9C4NO18 C2 (5) mp-1203759 [hull=0.362, icsd=1, PRIMARY]; Si12CO24 Cm (8) mp-1219366 [hull=0.212, PRIMARY]; Si(CO)2 Immm (71) mp-1001082 [hull=1.492, PRIMARY]; Si3C10NO7 Pca2_1 (29) mp-1199602 [hull=0.785, PRIMARY]
- papers: Polymer-Derived Silicon Oxycarbide Ceramics as Promising Next-Generation Sustainable Thermoelectrics

## Ca-Fe-O-Re
- rank 1150 | 5 samples | 1 papers | 1 compositions
- compositions: Ca2FeReO6 (5)
- measured range: 10-402 K (5th-95th pct of 5 curves; full span incl. outliers 10-452 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca2FeReO6 P2_1/c (14) mp-31763 [hull=0.000, icsd=2, PRIMARY]
- papers: The narrow conduction band(s) of Ca2FeReO6 detected by thermopower
