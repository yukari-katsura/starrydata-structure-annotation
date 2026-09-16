# Host systems -- chunk 011 of 73

Ranks 501-550 by sample count. These 50 host systems cover 648 samples (1.25% of the TE set); cumulative through this chunk: 81.74%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Cu-Ge-Si-Yb
- rank 501 | 14 samples | 2 papers | 9 compositions
- compositions: YbCu2Si1.75Ge0.25 (2); YbCu2SiGe (2); YbCu2Si1.25Ge0.75 (2); YbCu2Si0.75Ge1.25 (2); YbCu2Si0.25Ge1.75 (2); YbCu2Si1.5Ge0.5 (1)
- seed hypothesis (confirm): thcr2si2_122
- solid-solution axis: Ge/(Ge+Si) spans 0.13-0.88 (median 0.50) over 9 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 78-350 K (5th-95th pct of 34 curves)
- papers: Influence of rare earth doping on thermoelectric properties of SrTiO3 ceramics | Interplay of chemical expansion, Yb valence, and low temperature thermoelectricity in the YbCu2Si2−xGex solid solution

## Cu-Ni-Ti
- rank 502 | 14 samples | 1 papers | 7 compositions
- compositions: Ti50Ni45Cu5 (2); Ti50Ni42.5Cu7.5 (2); Ti50Ni25Cu25 (2); Ti50Ni20Cu30 (2); Ti50Ni40Cu10 (2); Ti50Ni35Cu15 (2)
- measured range: 12-386 K (5th-95th pct of 26 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiCuNi2 Pmmn (59) mp-1079193 [hull=0.017, icsd=1, PRIMARY]; Ti2CuNi Pmm2 (25) mp-1217130 [hull=0.060, PRIMARY]; Ti8Cu3Ni P4/mmm (123) mp-1217065 [hull=0.000, PRIMARY]; TiCuNi I4mm (107) mp-1216850 [hull=0.000, PRIMARY]; TiCuNi2 I4/mmm (139) mp-1207070 [hull=0.012]
- papers: Cu-substitution effect on thermoelectric properties of the TiNi-based shape memory alloys

## La-Ni
- rank 503 | 14 samples | 7 papers | 6 compositions
- compositions: LaNi (6); La7Ni3 (3); LaNi5 (2); La(Ni0.965Ga0.035)5 (1); La2Ni7 (1); (Ce0.12La0.88)Ni2 (1)
- dopant candidates (<5% at.): Ga (1), Ce (1)
- seed hypothesis (confirm): crb_feb_chain
- measured range: 10-883 K (5th-95th pct of 27 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaNi5 P6/mmm (191) mp-2317 [hull=0.000, icsd=48, PRIMARY]; LaNi2 Fd-3m (227) mp-2708 [hull=0.020, icsd=8, PRIMARY]; LaNi3 R-3m (166) mp-2764 [hull=0.000, icsd=6, PRIMARY]; LaNi Cmcm (63) mp-1064719 [hull=0.000, icsd=5, PRIMARY]; La3Ni Pnma (62) mp-1189497 [hull=0.001, icsd=4, PRIMARY]
- papers: Thermoelectric power of (Ce1−xLax)Ni single crystals | Dependence of the CeNi5 thermoelectric power on strong 4f-electron instability | Transport coefficients of intermediate valent CeNix intermetallic compounds

## La-Te
- rank 504 | 14 samples | 5 papers | 14 compositions
- compositions: La2Te3 (1); Yb0.044La0.377Te0.579 (1); Yb0.02La0.399Te0.584 (1); Yb0.029La0.392Te0.578 (1); La2.8Ca0.2Te4 (1); La3Te4 (1)
- dopant candidates (<5% at.): Yb (3), Pb (3), Sb (2), Ca (1)
- measured range: 297-1272 K (5th-95th pct of 56 curves)
- [ref 1] TEDesignLab / ICSD: LaTe2 (7)
- [ref 2] MP, ranked by ICSD evidence: LaTe2 P4/nmm (129) mp-1329 [hull=0.002, icsd=8, PRIMARY]; La3Te4 I-43d (220) mp-879 [hull=0.001, icsd=6, PRIMARY]; LaTe Fm-3m (225) mp-1560 [hull=0.000, icsd=5, PRIMARY]; LaTe3 Cmcm (63) mp-1078612 [hull=0.000, icsd=3, PRIMARY]; La2Te5 Cmcm (63) mp-1104212 [hull=0.003, icsd=1, PRIMARY]
- papers: Application of the compatibility factor to the design of segmented and cascaded thermoelectric generators | Optimizing Thermoelectric Efficiency in La3−xTe4via Yb Substitution | Mechanochemical synthesis and high temperature thermoelectric properties of calcium-doped lanthanum telluride La3−xCaxTe4

## Mo-O-Rb
- rank 505 | 14 samples | 6 papers | 5 compositions
- compositions: Rb0.3MoO3 (10); Rb1.5Mo8O16 (1); Rb0.3Mo0.999W0.001O3 (1); Rb0.3Mo0.997W0.003O3 (1); Rb0.3Mo0.995W0.005O3 (1)
- dopant candidates (<5% at.): W (3)
- seed hypothesis (confirm): tungsten_bronze
- measured range: 18-290 K (5th-95th pct of 14 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Rb2MoO4 C2/m (12) mp-19212 [hull=0.000, icsd=1, PRIMARY]; Rb4Te(MoO4)6 C2/c (15) mp-1199659 [hull=0.175, icsd=1, PRIMARY]; Rb3FeMo4O15 P2_1/c (14) mp-1199199 [hull=0.006, icsd=1, PRIMARY]; Rb3(MoO3)10 C2/m (12) mp-1202770 [hull=0.019, icsd=1, PRIMARY]; Rb2Te(MoO5)3 P2_1/c (14) mp-1179896 [hull=0.382, icsd=1, PRIMARY]
- papers: Structural, Magnetic and Electronic Transport Properties of Novel Hollandite-Type Molybdenum Oxide, Rb1.5Mo8O16 | Electronic structure and transport properties of K-doped blue bronze Rb0.15K0.15MoO3 | Thermal transport properties and electronic structure of W-doped rubidium blue bronzes Rb0.3Mo1−xWxO3 (x=0, 0.001, 0.003, 0.005)

## N-Sc
- rank 506 | 14 samples | 4 papers | 9 compositions
- compositions: ScN (6);  ScN (1);  Sc0.96Nb0.04N (1); Sc0.93Nb0.07N (1); Sc0.962Mg0.038N (1); Sc0.967Mg0.033N (1)
- dopant candidates (<5% at.): Mg (5), Nb (2)
- measured range: 296-841 K (5th-95th pct of 17 curves)
- [ref 1] TEDesignLab / ICSD: ScN Fm-3m (225) mp-2857 [hull=0.000, icsd=11, PRIMARY]; ScN Pm-3m (221) mp-12981 [hull=1.033, icsd=5]
- [ref 2] MP, ranked by ICSD evidence: Sc39N34 P-3m1 (164) mp-685209 [hull=0.007, PRIMARY]; ScN F-43m (216) mp-1009750 [hull=0.304, icsd=2]
- papers: Anomalously high thermoelectric power factor in epitaxial ScN thin films | Thermoelectric properties of epitaxial ScN films deposited by reactive magnetron sputtering onto MgO(001) substrates | Reduction of the thermal conductivity of the thermoelectric material ScN by Nb alloying

## Pt-Sb
- rank 507 | 14 samples | 3 papers | 12 compositions
- compositions: Pt0.99Ir0.01Sb2 (2); PtSb2 (2); Pt0.9Ir0.1Sb2 (1); Pt0.97Ir0.03Sb2 (1); PtSb (1); PtSb1.998Te0.002 (1)
- dopant candidates (<5% at.): Te (7), Ir (4)
- seed hypothesis (confirm): pyrite
- measured range: 11-756 K (5th-95th pct of 57 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sb2Pt Pa-3 (205) mp-562 [hull=0.000, icsd=4, PRIMARY]; SbPt P6_3/mmc (194) mp-2845 [hull=0.000, icsd=4, PRIMARY]; SbPt3 I4/mmm (139) mp-1078755 [hull=0.033, icsd=2, PRIMARY]; SbPt7 Fm-3m (225) mp-1030 [hull=0.007, icsd=2, PRIMARY]; Sb2Pt3 Ibam (72) mp-15659 [hull=0.000, icsd=1, PRIMARY]
- papers: Enhanced thermoelectric properties by Ir doping of PtSb2 with pyrite structure | Investigation of the correlation between stoichiometry and thermoelectric properties in a PtSb2single crystal | Low-Temperature Thermoelectric Properties of PtSb2−x\n            Te\n                x\n            \nfor Cryogenic Peltier Cooling Applications

## W
- rank 508 | 14 samples | 7 papers | 7 compositions
- compositions: W (8); W0.98Ta0.02 (1); (W)99.76(TiC)0.24 (1); (W)99.92(TiC)0.08 (1); (W)99.6(TiC)0.4 (1); (W)99.44(TiC)0.56 (1)
- dopant candidates (<5% at.): Ti (5), C (5), Ta (1)
- measured range: 10-1404 K (5th-95th pct of 16 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): W Im-3m (229) mp-91 [hull=0.000, icsd=14, PRIMARY]; W Fm-3m (225) mp-8641 [hull=0.480, icsd=1]; W Pbcm (57) mp-1065340 [hull=0.500, icsd=1]; W P2/m (10) mp-1191581 [hull=1.200, icsd=1]; W Pm-3n (223) mp-11334 [hull=0.090]
- papers: Thermoelectric Properties of Niobium in the Temperature Range 300°–1200°K | Electronic transport properties of liquid Ga–Zn alloys | Low‐Temperature Transport Properties of Commercial Metals and Alloys. IV. Reactor Grade Be, Mo, and W

## Ag-Bi-S
- rank 509 | 13 samples | 5 papers | 9 compositions
- compositions: AgBi3S5 (5); AgSb0.3Bi2.7S5 (1); AgBiS2 (1); AgBiS1.02Se0.08 (1); AgBi3S5.00 (1); AgBi3S5.04 (1)
- dopant candidates (<5% at.): Sb (1), Se (1), Cl (1)
- seed hypothesis (confirm): bi_chalcogenide_complex
- measured range: 80-806 K (5th-95th pct of 64 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AgBi3S5 C2/m (12) mp-23474 [hull=0.000, icsd=2, PRIMARY]; AgBiS2 R-3m (166) mp-29678 [hull=0.016, icsd=1, PRIMARY]; Ag3Bi8S13 C2/m (12) mp-1214935 [hull=0.034, PRIMARY]; Ag3Bi7S12 C2/m (12) mp-1229165 [hull=0.008, PRIMARY]; AgBiS2 P-3m1 (164) mp-1172905 [hull=0.015]
- papers: Crystal Growth, Thermoelectric Properties, and Electronic Structure of AgBi3S5and AgSbxBi3-xS5(x= 0.3) | Cation Disorder and Bond Anharmonicity Optimize the Thermoelectric Properties in Kinetically Stabilized Rocksalt AgBiS2Nanocrystals | Synthesis and transport properties of AgBi3S5 ternary sulfide compound

## Ag-Ge-Te
- rank 510 | 13 samples | 7 papers | 11 compositions
- compositions: Ag8GeTe6 (2); (GeTe)5.5AgIn0.5Sb0.5Te2 (2); (GeTe)0.92(Ag8GeTe6)0.08 (1); (GeTe)0.98(Ag8GeTe6)0.02 (1); (GeTe)0.95(Ag8GeTe6)0.05 (1); (GeTe)0.96(Ag8GeTe6)0.04 (1)
- dopant candidates (<5% at.): Sb (3), In (2), Bi (1)
- measured range: 81-798 K (5th-95th pct of 45 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ag8GeTe6 P1 (1) mp-685969 [hull=0.020, PRIMARY]
- papers: Thermoelectric properties of Ag8GeTe6 | High thermoelectric performance of GeTe–Ag8GeTe6 eutectic composites | TAGS-related indium compounds and their thermoelectric properties – the solid solution series (GeTe)xAgInySb1−yTe2 (x = 1–12; y = 0.5 and 1)

## Al-Ba-Ge
- rank 511 | 13 samples | 5 papers | 5 compositions
- compositions: Ba8Al16Ge30 (7); Ba24Al12Ge88 (3); Ba24Al9Ge91 (1); Ba8Al14Ge32 (1); Ba8Al18Ge28 (1)
- seed hypothesis (confirm): clathrate_i
- measured range: 12-1053 K (5th-95th pct of 37 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaAlGe P-6m2 (187) mp-13272 [hull=0.000, icsd=2, PRIMARY]; Ba(AlGe)2 I4/mmm (139) mp-31059 [hull=0.009, icsd=1, PRIMARY]; Ba10Al3Ge7 P6_3/mcm (193) mp-27568 [hull=0.005, icsd=1, PRIMARY]; Ba3(AlGe)2 Immm (71) mp-10669 [hull=0.000, icsd=1, PRIMARY]
- papers: Host Structure Engineering in Thermoelectric Clathrates | Thermoelectric properties and crystal structure of type-III clathrate compounds in the Ba–Al–Ge system | Crystal structure and thermoelectric properties of type-III clathrate compounds in the Ba–In–Ge system

## Al-Ce-Cu
- rank 512 | 13 samples | 4 papers | 3 compositions
- compositions: CeCu4Al (7); Ce0.8La0.2Cu4Al (5); CeCu4Al8 (1)
- dopant candidates (<5% at.): La (5)
- measured range: 10-351 K (5th-95th pct of 18 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(Al2Cu)4 I4/mmm (139) mp-20003 [hull=0.000, icsd=3, PRIMARY]; CeAl3Cu I4mm (107) mp-1069443 [hull=0.000, icsd=3, PRIMARY]; Ce3Mn(Al3Cu)8 Pm-3m (221) mp-669550 [hull=0.120, icsd=1, PRIMARY]; CeAlCu P-62m (189) mp-1079868 [hull=0.000, icsd=1, PRIMARY]; CeAl2Cu3 Cmmm (65) mp-1226644 [hull=0.000, PRIMARY]
- papers: Thermopower of Ce1−xLaxCu4Al intermetallic compounds | Thermopower of Ce1–xLaxCu4Al in applied magnetic fields | Thermopower and thermal conductivity of Kondo lattice CeCu4Al

## Al-Fe-Si
- rank 513 | 13 samples | 3 papers | 10 compositions
- compositions: Al25.7Fe37.1Si37.1 (4); Al27.4Fe36.5Si36.1 (1); Al25.5Fe36.5Si38 (1); Al25.3Fe36.5Si38.2 (1); Al27.7Fe36.5Si35.8 (1); Al25.7Fe36.5Si38.2 (1)
- dopant candidates (<5% at.): Mn (1)
- seed hypothesis (confirm): quasicrystal_approximant
- measured range: 300-856 K (5th-95th pct of 37 curves; full span incl. outliers 11-856 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al2(FeSi)3 P-1 (2) mp-29110 [hull=0.000, icsd=2, PRIMARY]; Al2Fe3Si4 Cmcm (63) mp-29111 [hull=0.010, icsd=2, PRIMARY]; Al3Fe2Si3 P2_1/c (14) mp-29066 [hull=0.000, icsd=2, PRIMARY]; Al3Fe2Si Fd-3m (227) mp-1190708 [hull=0.000, icsd=1, PRIMARY]; Al3FeSi2 I4cm (108) mp-1228467 [hull=0.023, PRIMARY]
- papers: Conduction type control and power factor enhancement of the thermoelectric material Al2Fe3Si3 | Extremely small thermal conductivity of the Al-based Mackay-type<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:mn>1</mml:mn><mml:mo>∕</mml:mo><mml:mn>1</mml:mn></mml:mrow></mml:math>-cubic approximants | Characterization and Preparation of Nanostructured Al2Fe3Si3 Thermoelectric Materials

## Al-Si
- rank 514 | 13 samples | 1 papers | 2 compositions
- compositions: Si0.93Al0.07 (9); Si0.84Al0.16 (4)
- measured range: 295-785 K (5th-95th pct of 14 curves; full span incl. outliers 295-831 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al4Si19 P1 (1) mp-1203554 [hull=0.233, icsd=1, PRIMARY]; Al4Si R-3m (166) mp-1228120 [hull=0.085, PRIMARY]; AlSi Pm-3m (221) mp-1021666 [hull=0.272, PRIMARY]
- papers: Thermoelectric effect of silicon films prepared by aluminum-induced crystallization

## As-Ba-Fe-K
- rank 515 | 13 samples | 3 papers | 5 compositions
- compositions: Ba0.6K0.4Fe2As2 (8); Ba0.7K0.3Fe2As2 (2); Ba0.5K0.5Fe2As2 (1); Ba0.3K0.7Fe2As2 (1); Ba0.4K0.6Fe2As2 (1)
- seed hypothesis (confirm): thcr2si2_122
- measured range: 11-300 K (5th-95th pct of 19 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): K2Ba(FeAs)6 C2/m (12) mp-1223766 [hull=0.003, PRIMARY]; KBa(FeAs)4 Cmmm (65) mp-1223517 [hull=0.005, PRIMARY]; KBa2(FeAs)6 C2/m (12) mp-1223567 [hull=0.001, PRIMARY]; KBa3(FeAs)8 P-1 (2) mp-1223625 [hull=0.000, PRIMARY]; KBa4(FeAs)10 I4/m (87) mp-1223626 [hull=0.009, PRIMARY]
- papers: Thermoelectric properties of electron- and hole-dopedBaFe2As2 | Transport properties and superconductivity in Ba1-xMxFe2As2(M=La and K) with double FeAs layers | Pressure effects on the superconducting thin film Ba<sub>1−</sub><sub><i>x</i></sub>K<sub><i>x</i></sub>Fe<sub>2</sub>As<sub>2</sub>

## As-Fe-La-O-P
- rank 516 | 13 samples | 1 papers | 13 compositions
- compositions: La0.9Sr0.1FeAs0.4P0.6O (1); La0.9Sr0.1FeAs0.2P0.8O (1); LaFeAs0.7P0.3O0.86F0.14 (1); LaFeAs0.6P0.4O0.86F0.14 (1); LaFeAs0.5P0.5O0.86F0.14 (1); LaFeAs0.4P0.6O0.86F0.14 (1)
- dopant candidates (<5% at.): Sr (7), F (6)
- solid-solution axis: As/(As+P) spans 0.20-0.80 (median 0.50) over 13 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-301 K (5th-95th pct of 13 curves)
- papers: Three superconducting phases with different categories of pairing in hole- and electron-doped \nLaFeAs1−xPxO

## As-Fe-O-Sm
- rank 517 | 13 samples | 7 papers | 10 compositions
- compositions: SmFeAsO0.88F0.12 (3); SmFeAsO (2); SmFe0.95Co0.05AsO (1); SmFe0.9Co0.1AsO (1); SmFe0.85Co0.15AsO (1); SmFeAsO0.85 (1)
- dopant candidates (<5% at.): F (4), Co (3), La (1)
- seed hypothesis (confirm): zrcusias_1111
- measured range: 10-300 K (5th-95th pct of 18 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SmFeAsO P4/nmm (129) mp-1078897 [hull=0.205, icsd=5, PRIMARY]; Sm2Fe2As2O P-4m2 (115) mp-1219198 [hull=0.819, PRIMARY]; Sm2FeAs2O P4/mmm (123) mp-1208903 [hull=1.541, PRIMARY]
- papers: Thermoelectric power of RFeAsO (R=Ce, Pr, Nd, Sm and Gd) | Thermoelectric properties of FeAs based superconductors, with thick perovskite- and Sm-O fluorite-type blocking layers | Effect of Co-doping on the resistivity and thermopower of SmFe1-xCoxAsO (0.0≤x≤0.3)

## B-Co-Fe
- rank 518 | 13 samples | 5 papers | 12 compositions
- compositions: Fe74Co10B16 (2); Fe74Co7.5Cr2.5B16 (1); (Fe0.92Co0.08)84B16 (1); (Fe0.94Co0.06)84B16 (1); Fe0.5Co0.5B (1); Fe0.1Co0.9B (1)
- dopant candidates (<5% at.): O (5), Al (5), Cr (1), Si (1)
- measured range: 10-945 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeCo2B Pnma (62) mp-1188282 [hull=0.155, icsd=1, PRIMARY]; Fe3Co3B2 P2_1 (4) mp-1225207 [hull=0.014, PRIMARY]; FeCoB Fmmm (69) mp-1224984 [hull=0.016, PRIMARY]; FeCoB2 Pmc2_1 (26) mp-1224999 [hull=0.020, PRIMARY]
- papers: Electrical resistivity and thermoelectric power of Fe74Co10−x Cr x B16 metallic glasses | Influence of small amounts of Co and Ni additives on thermoelectric power in amorphous Fe&lt;inf&gt;84&lt;/inf&gt;B&lt;inf&gt;16&lt;/inf&gt; | Seebeck coefficients of iron group elements borides

## B-U
- rank 519 | 13 samples | 5 papers | 3 compositions
- compositions: UB4 (8); UB2 (4); UB12 (1)
- seed hypothesis (confirm): ub12_boride
- measured range: 12-1674 K (5th-95th pct of 27 curves; full span incl. outliers 10-1775 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UB2 P6/mmm (191) mp-1514 [hull=0.000, icsd=9, PRIMARY]; UB12 Fm-3m (225) mp-22319 [hull=0.000, icsd=8, PRIMARY]; UB4 P4/mbm (127) mp-619 [hull=0.000, icsd=8, PRIMARY]
- papers: Boron isotope effects on the thermoelectric properties of UB4 at low temperatures | Physical properties of cage-like compound UB12 | Thermophysical and mechanical property assessment of UB2 and UB4 sintered via spark plasma sintering

## Ba-Fe-La-O
- rank 520 | 13 samples | 7 papers | 11 compositions
- compositions: La0.5Ba0.5FeO3 (3); La0.4Ba0.6Fe0.8Zn0.2O3 (1); La0.26Sm0.24Sr0.14Ba0.36FeO3 (1); La0.39Sm0.11Sr0.21Ba0.29FeO3 (1); La0.34Nd0.16Sr0.12Ba0.38FeO3 (1); Ba0.5La0.5FeO3 (1)
- dopant candidates (<5% at.): Sr (3), Sm (2), Co (2), Zn (1), Nd (1), Ni (1)
- measured range: 292-1175 K (5th-95th pct of 13 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2La(FeO3)3 P-3m1 (164) mp-1228521 [hull=0.000, PRIMARY]; BaLa(FeO3)2 Fm-3m (225) mp-1227910 [hull=0.029, PRIMARY]; BaLa2Fe2O7 I4/mmm (139) mp-1227917 [hull=0.000, PRIMARY]; BaLaFeO4 I4mm (107) mp-1227839 [hull=0.035, PRIMARY]
- papers: Evaluation of La0.4Ba0.6Fe0.8Zn0.2O3−δ + Sm0.2Ce0.8O1.9 as a potential cobalt-free composite cathode for intermediate temperature solid oxide fuel cells | Effect of the Synthetic Method on the Structure and Electrical Conductivity of La<sub>0.5</sub>Ba<sub>0.5</sub>FeO<sub>3</sub> as SOFC Cathode Materials | Structure and properties of perovskites for SOFC cathodes as a function of the A-site cation size disorder

## Bi-Cu-O-Se-Te
- rank 521 | 13 samples | 2 papers | 3 compositions
- compositions: BiCuSe0.8Te0.2O (5); BiCuSe0.7Te0.3O (4); BiCuSe0.6Te0.4O (4)
- seed hypothesis (confirm): zrcusias_1111
- measured range: 296-924 K (5th-95th pct of 17 curves)
- papers: Enhanced thermoelectric performance of a BiCuSeO system via band gap tuning | Band structure manipulated by high pressure-assisted Te doping realizing improvement in thermoelectric performance of BiCuSeO system

## Bi-Pb-Se-Te
- rank 522 | 13 samples | 4 papers | 13 compositions
- compositions: PbBi4(Te0.90Se0.10)7 (1); PbBi4(Te0.80Se0.20)7 (1); PbBi2(Te0.8Se0.2)4 (1); PbBi2(Te0.5Se0.5)4 (1); PbBi6(Te0.75Se0.25)10 (1); Pb2Bi6(Te0.4Se0.6)11 (1)
- solid-solution axis: Se/(Se+Te) spans 0.10-0.75 (median 0.40) over 13 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 82-749 K (5th-95th pct of 33 curves; full span incl. outliers 81-842 K)
- papers: Thermoelectric Properties of PbBi4Te7-Based Anion-Substituted Layered Solid Solutions | Thermoelectric materials based on layered chalcogenides of bismuth and lead | Thermoelectric materials based on anion-substituted solid solutions in the Pb,Bi‖Se,Te ternary reciprocal system

## Ca-Rh-Sn
- rank 523 | 13 samples | 1 papers | 1 compositions
- compositions: Ca2.8La0.2Rh4Sn13 (13)
- dopant candidates (<5% at.): La (13)
- measured range: 10-10 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca3Sn13Rh4 Pm-3n (223) mp-4363 [hull=0.000, icsd=4, PRIMARY]; CaSn2Rh Cmcm (63) mp-11959 [hull=0.000, icsd=1, PRIMARY]; CaSnRh2 Fm-3m (225) mp-861935 [hull=0.000, PRIMARY]
- papers: The effective increase in atomic scale disorder by doping and superconductivity in Ca3Rh4Sn13

## Cd-Te
- rank 524 | 13 samples | 3 papers | 10 compositions
- compositions: CdTe (4); CdTe0.995Cl0.005 (1); CdTe0.99Cl0.01 (1); CdTe0.97Cl0.03 (1); CdTe0.95Cl0.05 (1); Sn0.02CdTe (1)
- dopant candidates (<5% at.): Cl (4), Sn (2), Ge (2), In (1)
- measured range: 298-1679 K (5th-95th pct of 35 curves; full span incl. outliers 298-1825 K)
- [ref 1] TEDesignLab / ICSD: CdTe F-43m (216) mp-406 [hull=0.000, icsd=41, PRIMARY]; CdTe P6_3mc (186) mp-12779 [hull=0.004, icsd=3]
- [ref 2] MP, ranked by ICSD evidence: Cd3Te I4/mmm (139) mp-1183651 [hull=0.305, PRIMARY]; CdTe Fm-3m (225) mp-2388 [hull=0.179, icsd=6]; CdTe P3_121 (152) mp-1492 [hull=0.107, icsd=4]; CdTe Cmcm (63) mp-1008471 [hull=0.182, icsd=2]; CdTe P4/mmm (123) mp-12581 [hull=0.482, icsd=1]
- papers: Thermal conductivity, electrical conductivity, and thermoelectric properties of CdTe and Cd0.8Zn0.2Te crystals between room temperature and 780oC | Thermoelectric Properties of CdTe1−x Cl x Material Prepared by Spark Plasma Sintering Method | Transport Properties and Viscosity of Liquid CdTe Doped with In, Ge, and Sn

## Ce-La-Mn-O
- rank 525 | 13 samples | 2 papers | 9 compositions
- compositions: La0.4Ce0.6MnO3 (4); La0.7Ce0.3MnO3 (2); La0.6Ce0.4MnO3 (1); La0.5Ce0.5MnO3 (1); (La0.7Sr0.3MnO3)0.5(CeO2)0.5 (1); (La0.7Sr0.3MnO3)0.45(CeO2)0.55 (1)
- dopant candidates (<5% at.): Sr (5)
- solid-solution axis: Ce/(Ce+La) spans 0.30-0.64 (median 0.50) over 9 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-339 K (5th-95th pct of 17 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaCe2Mn3O9 Cmmm (65) mp-1223081 [hull=0.267, PRIMARY]; LaCeMn2O6 R32 (155) mp-1222969 [hull=0.096, PRIMARY]
- papers: Studies of transport and magnetic properties of Ce-doped LaMnO3 | Enhanced tunable magnetoresistance properties over a wide temperature range in epitaxial (La<sub>0.7</sub>Sr<sub>0.3</sub>MnO<sub>3</sub>)<sub>1−x</sub>:(CeO<sub>2</sub>)<sub>x</sub> nanocomposites

## Ce-Ni-Si
- rank 526 | 13 samples | 10 papers | 6 compositions
- compositions: CeNi2Si2 (7); Ce(Ni0.9Pd0.1)2Si2 (2); CeNi4Si (1); Ce2Ni3Si5 (1); Ce(Ni0.95Cu0.05)2Si2 (1); CeNi9Si4 (1)
- dopant candidates (<5% at.): Pd (2), Cu (1)
- measured range: 10-800 K (5th-95th pct of 23 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(SiNi)2 I4/mmm (139) mp-4537 [hull=0.000, icsd=13, PRIMARY]; CeSi2Ni Cmcm (63) mp-15653 [hull=0.000, icsd=3, PRIMARY]; CeSiNi I4_1md (109) mp-20710 [hull=0.000, icsd=2, PRIMARY]; CeSi4Ni9 I4/mcm (140) mp-31051 [hull=0.004, icsd=2, PRIMARY]; Ce2Si5Ni3 Ibam (72) mp-1183797 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric properties of the intermediate valent cerium intermetallic Ce2Ni3Si5 doped with Pd, Co, and Cu | Electronic structure and thermoelectric power of CeNi4Si | Peculiarities of the intermediate valence state of Ce in CeM2Si2 (M=Fe, Co, Ni) compounds

## Ce-O-Sr-Ti
- rank 527 | 13 samples | 3 papers | 11 compositions
- compositions: Sr0.7Ce0.3TiO2.9 (2); Sr0.6Ce0.4TiO2.9 (2); Sr0.5Ce0.5TiO2.9 (1); Sr0.5Ce05TiO2.9 (1); Sr0.7Ce0.3TiO3.0 (1); Sr0.6Ce0.4TiO3.0 (1)
- measured range: 10-976 K (5th-95th pct of 17 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2Ce2Ti5O15 R-3m (166) mp-1218863 [hull=0.055, PRIMARY]
- papers: Correlation and phonon effects for the electronic transport and thermoelectric power factors in the metal–band-insulator crossover of perovskite-type titanates | Parallel syntheses and thermoelectric properties of Ce-doped SrTiO3 thin films | Electronic states of perovskite-type and systems with a metal - insulator transition

## Co-Hf-Sb-Sn-Ti-Zr
- rank 528 | 13 samples | 3 papers | 5 compositions
- compositions: Ti0.3Zr0.35Hf0.35CoSb0.8Sn0.2 (9); Ti0.3Zr0.35Hf0.35CoSb0.6Sn0.4 (1); Ti0.3Zr0.35Hf0.35CoSb0.5Sn0.5 (1); Ti0.3Zr0.35Hf0.35CoSb0.75Sn0.2 (1); Ti0.3Zr0.35Hf0.35CoSb0.7Sn0.3 (1)
- measured range: 16-883 K (5th-95th pct of 24 curves)
- papers: Segmented Thermoelectric Oxide-Based Module for High-Temperature Waste Heat Harvesting | Charge carrier concentration optimization of thermoelectric p-type half-Heusler compounds | High performance p-type segmented leg of misfit-layered cobaltite and half-Heusler alloy

## Co-Ni-Zr
- rank 529 | 13 samples | 1 papers | 3 compositions
- compositions: Co0.71Ni0.29Zr2 (6); Co0.846Ni0.154Zr2 (5); Co0.79Ni0.21Zr2 (2)
- seed hypothesis (confirm): cual2_c16
- measured range: 11-392 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zr2CoNi Amm2 (38) mp-1215600 [hull=0.000, PRIMARY]; Zr4CoNi I422 (97) mp-1215379 [hull=0.007, PRIMARY]; Zr5Co4Ni P4/mmm (123) mp-1215360 [hull=0.057, PRIMARY]; ZrCoNi Imma (74) mp-1215275 [hull=0.024, PRIMARY]
- papers: Anisotropy of the normal state properties of the superconducting Co1?x Ni x Zr2 system

## Co-O-Sr-Tl
- rank 530 | 13 samples | 2 papers | 10 compositions
- compositions: Tl2Sr3Co3O9 (3); Tl0.4SrCoO3 (2); Tl0.6SrCoO4.1 (1); Tl0.6SrCoO3.7 (1); Tl0.6SrCoO4.28 (1); Tl0.54SrCoO3 (1)
- dopant candidates (<5% at.): Bi (1)
- measured range: 10-299 K (5th-95th pct of 13 curves)
- papers: Large Thermopower in Metallic Misfit Cobaltites | Searching for new thermoelectric materials: some examples among oxides, sulfides and selenides

## Co-O-Zn
- rank 531 | 13 samples | 4 papers | 10 compositions
- compositions: Zn0.85Co0.15O (3); Zn0.90Co0.10O (2); Bi0.025ZnCo1.975O4 (1); ZnCo2O4 (1); Bi0.1ZnCo1.9O4 (1); Bi0.05ZnCo1.95O4 (1)
- dopant candidates (<5% at.): Bi (4)
- seed hypothesis (confirm): wurtzite
- measured range: 309-678 K (5th-95th pct of 33 curves; full span incl. outliers 14-678 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zn(Co2O5)2 C2/m (12) mp-1215794 [hull=0.145, PRIMARY]; Zn3Co9O16 R3m (160) mp-766725 [hull=0.034, PRIMARY]; Zn4CoO5 P3m1 (156) mp-1215675 [hull=0.005, PRIMARY]; Zn5Co19O32 R3m (160) mp-861852 [hull=0.000, PRIMARY]; ZnCoO2 R-3m (166) mp-779972 [hull=0.097, PRIMARY]
- papers: Enhancing the thermoelectric power factor of nanostructured ZnCo2O4 by Bi substitution | A facile synthesis, structural, morphological and electrical characterizations of Zn1-xCoxO nanocrystals for thermoelectric applications | Role of cobalt doping on the electrical conductivity of ZnO nanoparticles

## Cu-La-Nd-O
- rank 532 | 13 samples | 3 papers | 11 compositions
- compositions: La1.4Nd0.4Sr0.2CuO4 (2); La1.36Nd0.4Sr0.24CuO4 (2); (La0.640Nd0.285Ca0.035Sr0.024Ba0.016)2CuO4 (1); (La0.704Nd0.221Ca0.013Sr0.047Ba0.015)2CuO4 (1); La1.21Nd0.6Sr0.19CuO4 (1); La1.32Nd0.6Sr0.08CuO4 (1)
- dopant candidates (<5% at.): Sr (13), Ca (2), Ba (2)
- measured range: 10-298 K (5th-95th pct of 13 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La3Nd(CuO4)2 P4mm (99) mp-1223089 [hull=0.002, PRIMARY]; LaNdCuO4 I4mm (107) mp-1222802 [hull=0.002, PRIMARY]; La3Nd(CuO4)2 Cm (8) mp-1223168 [hull=0.067]; LaNdCuO4 C2/m (12) mp-1222994 [hull=0.079]
- papers: True Tolerance Factor Effects in Ln3+1.85M2+0.15CuO4 Superconductors | Thermopower across the stripe critical point of<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mtext>La</mml:mtext></mml:mrow><mml:mrow><mml:mn>1.6</mml:mn><mml:mo>−</mml:mo><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mrow><mml:mtext>Nd</mml:mtext></mml:mrow><mml:mrow><mml:mn>0.4</mml:mn></mml:mrow></mml:msub><mml:msub><mml:mrow><mml:mtext>Sr</mml:mtext></mml:mrow><mml:mi>x</mml:mi></mml:msub><mml:msub><mml:mrow><mml:mtext>CuO</mml:mtext></mml:mrow><mml:mn>4</mml:mn></mml:msub></mml:mrow></mml:math>: Evidence for a quantum critical point in a hole-doped high-<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mi>T</mml:mi><mml:mi>c</mml:mi></mml:msub></mml:mrow></mml:math>superconductor | Consequences of stripe order for the transport properties of rare earth doped La2−xSrxCuO4

## Cu-La-Si
- rank 533 | 13 samples | 3 papers | 9 compositions
- compositions: Ce0.06La0.94Cu2.05Si2 (2); Ce0.01La0.99Cu2.05Si2 (2); Ce0.2La0.8Cu2.05Si2 (2); Ce0.04La0.96Cu2.05Si2 (2); Ce0.2La0.8Cu2Si2 (1); Ce0.1La0.9Cu2.05Si2 (1)
- dopant candidates (<5% at.): Ce (12)
- seed hypothesis (confirm): thcr2si2_122
- measured range: 10-331 K (5th-95th pct of 13 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(CuSi)2 I4/mmm (139) mp-3995 [hull=0.000, icsd=6, PRIMARY]; LaCuSi P6_3/mmc (194) mp-4835 [hull=0.000, icsd=2, PRIMARY]; La2CuSi3 P-6m2 (187) mp-1223228 [hull=0.000, PRIMARY]; LaCuSi P-6m2 (187) mp-1222888 [hull=0.016]
- papers: Electric and magnetic properties of the Kondo-lattice compound CeCu2Si2 | Transport properties of the<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">Ce</mml:mi></mml:mrow><mml:mrow><mml:mi>x</mml:mi></mml:mrow></mml:msub></mml:mrow><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">La</mml:mi></mml:mrow><mml:mrow><mml:mn>1</mml:mn><mml:mi>−</mml:mi><mml:mi>x</mml:mi></mml:mrow></mml:msub></mml:mrow><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">Cu</mml:mi></mml:mrow><mml:mrow><mml:mn>2.05</mml:mn></mml:mrow></mml:msub></mml:mrow><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">Si</mml:mi></mml:mrow><mml:mrow><mml:mn>2</mml:mn></mml:mrow></mml:msub></mml:mrow></mml:math>heavy-fermion alloy system | Behaviour of thermopower at the transition from impurity Kondo towards heavy fermion regime in CexLa1−xCu2.05Si2

## Cu-S-Se
- rank 534 | 13 samples | 5 papers | 8 compositions
- compositions: Cu1.97Se0.5S0.5 (6); Cu2Se0.81S0.19 (1); Cu1.8Se0.5S0.5 (1); Cu1.8Se0.7S0.3 (1); Cu1.8Se0.3S0.7 (1); Cu1.98S0.16Se0.84 (1)
- solid-solution axis: S/(S+Se) spans 0.16-0.80 (median 0.50) over 8 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 299-974 K (5th-95th pct of 35 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu2SeS3 Cc (9) mp-1120816 [hull=0.098, PRIMARY]; CuSeS P2_13 (198) mp-1225747 [hull=0.071, PRIMARY]
- papers: Enhanced thermoelectric efficiency of Cu 2−x Se–Cu 2 S composite by incorporating Cu 2 S nanoparticles | Enhanced thermoelectric properties of Cu1.8Se1−xSx alloys prepared by mechanical alloying and spark plasma sintering | Improvement of thermoelectric properties and their correlations with electron effective mass in Cu1.98SxSe1−x

## Fe-Nb-Sb-Ta-Ti
- rank 535 | 13 samples | 2 papers | 6 compositions
- compositions: (Nb0.8Ta0.2)0.8Ti0.2FeSb (6); (Nb0.64Ta0.36)0.8Ti0.2FeSb (3); (Nb0.68Ta0.32)0.8Ti0.2FeSb (1); (Nb0.76Ta0.24)0.8Ti0.2FeSb (1); (Nb0.80Ta0.20)0.8Ti0.2FeSb (1); (Nb0.60Ta0.40)0.8Ti0.2FeSb (1)
- solid-solution axis: Nb/(Nb+Ta) spans 0.60-0.80 (median 0.76) over 6 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 298-1202 K (5th-95th pct of 49 curves)
- papers: Unique Role of Refractory Ta Alloying in Enhancing the Figure of Merit of NbFeSb Thermoelectric Materials | Half‐Heusler Thermoelectric Module with High Conversion Efficiency and High Power Density

## Ga-Te
- rank 536 | 13 samples | 7 papers | 7 compositions
- compositions: Ga1.9Cu0.05Sb0.1Te2.95 (4); Ga2Te3 (4); Ga20Te80 (1); GaTe (1); Ga2Cu0.05Sb0.05Te2.9 (1); Ga2Cu0.05Sb0.1Te2.85 (1)
- dopant candidates (<5% at.): Sb (7), Cu (7)
- measured range: 173-862 K (5th-95th pct of 34 curves; full span incl. outliers 129-871 K)
- [ref 1] TEDesignLab / ICSD: Ga2Te5 I4/m (87) mp-2371 [hull=0.000, icsd=3, PRIMARY]; GaTe P6_3/mmc (194) mp-10009 [hull=0.004, icsd=1, PRIMARY]; GaTe (12)
- [ref 2] MP, ranked by ICSD evidence: Ga2Te3 R-3m (166) mp-1070116 [hull=0.332, icsd=1, PRIMARY]; Ga7Te10 R32 (155) mp-18388 [hull=0.000, icsd=1, PRIMARY]; Ga3Te I4/mmm (139) mp-1184010 [hull=0.203, PRIMARY]; Ga2Te3 Cc (9) mp-38970 [hull=0.000]; Ga2Te3 Imm2 (44) mp-1224840 [hull=0.016]
- papers: Thermoelectric properties of splat‐cooled amorphous In20Te80, Ga20Te80, and Ge15Te85 | Thermoelectric power (TEP) of layered chalcogenides GaTe crystals | Engineered cation vacancy plane responsible for the reduction in lattice thermal conductivity and improvement in the thermoelectric property of Ga2Te3-based semiconductors

## Mn-Ni-Sb-Ti
- rank 537 | 13 samples | 1 papers | 8 compositions
- compositions: NiTi0.65Mn0.35Sb (5); NiTi0.6Mn0.4Sb (2); NiTi0.5Mn0.5Sb (1); NiTi0.8Mn0.2Sb (1); NiTi0.7Mn0.3Sb (1); NiTi0.4Mn0.6Sb (1)
- seed hypothesis (confirm): quaternary_heusler
- measured range: 12-300 K (5th-95th pct of 16 curves)
- papers: Galvanomagnetic properties of disordered Mn semi-Heusler phases with Anderson localisation

## Pb-S-Zn
- rank 538 | 13 samples | 2 papers | 2 compositions
- compositions: (PbS)0.5(ZnS)0.5 (12); Pb0.3Zn0.7S (1)
- measured range: 262-896 K (5th-95th pct of 15 curves)
- papers: Thermoelectric properties of the PbSZnS alloy semiconductor and its application to solar energy conversion | Growth, characterization and transport properties of Pb x Zn1−x S mixed crystals

## Sb-Te-Tl
- rank 539 | 13 samples | 5 papers | 9 compositions
- compositions: TlSbTe2 (4); Tl9SbTe6 (2); TlSbTe6 (1); Tl9Sb0.95Sn0.05Te6 (1); Tl9Sb0.97Sn0.03Te6 (1); Tl9Sb0.9Sn0.1Te6 (1)
- dopant candidates (<5% at.): Sn (3), Pb (3)
- measured range: 297-720 K (5th-95th pct of 51 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TlSbTe2 R-3m (166) mp-4573 [hull=0.597, icsd=3, PRIMARY]; Tl9SbTe6 I4 (79) mp-34292 [hull=0.146, PRIMARY]; TlSbTe2 C2/m (12) mp-634989 [hull=0.951]; Tl9SbTe6 P4/m (83) mp-686086 [hull=0.148]
- papers: Thermoelectric properties of thallium antimony telluride | Thermoelectric properties of Sn- and Pb-doped Tl9BiTe6 and Tl9SbTe6 | Thermoelectric Properties of Thallium Compounds with Extremely Low Thermal Conductivity

## Sn
- rank 540 | 13 samples | 3 papers | 6 compositions
- compositions: Sn (8); Sb0.0000007Sn (1); Sb0.000007Sn (1); Sb0.0000003Sn (1); Sb0.000002Sn (1); Sb0.000003Sn (1)
- dopant candidates (<5% at.): Sb (5)
- measured range: 10-434 K (5th-95th pct of 13 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sn I4_1/amd (141) mp-84 [hull=0.040, icsd=39, PRIMARY]; Sn I4/mmm (139) mp-55 [hull=0.055, icsd=41]; Sn Immm (71) mp-1056308 [hull=0.066, icsd=41]; Sn Im-3m (229) mp-7162 [hull=0.073, icsd=40]; Sn Fd-3m (227) mp-117 [hull=0.000, icsd=5]
- papers: Thermoelectric power and structural properties in two-phase Sn/SnTe alloys | Electron‐irradiation‐induced damage production effects in lightly doped n ‐ and p ‐type α‐tin | Size and temperature effects on thermoelectric power of β‐tin thin films

## Ag-Cu-Yb
- rank 541 | 12 samples | 4 papers | 5 compositions
- compositions: YbAgCu4 (8); YbCu4.3Ag0.7 (1); YbCu4.15Ag0.85 (1); YbCu4.5Ag0.5 (1); YbCu4Ag (1)
- seed hypothesis (confirm): aube5
- measured range: 10-301 K (5th-95th pct of 39 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbCu4Ag F-43m (216) mp-1077741 [hull=0.000, icsd=2, PRIMARY]
- papers: Nanostructured YbAgCu4for Potentially Cryogenic Thermoelectric Cooling | Thermoelectric power of heavy-fermion system | Advancing Cryogenic Cooling with Self-Modulated YbAgCu<sub>4</sub> for Enhanced Thermoelectric Efficiency below Liquid-Nitrogen Temperatures

## Ag-La-Mn-O
- rank 542 | 12 samples | 4 papers | 9 compositions
- compositions: La0.7Ag0.3MnO3 (3); La0.75Ag0.25MnO3 (2); (La0.75K0.25MnO3)(Ag2O)0.2 (1); (La0.75K0.25MnO3)(Ag2O)0.3 (1); (La0.75K0.25MnO3)(Ag2O)0.4 (1); Ag0.3La0.7Ca0.24Na0.06MnO3 (1)
- dopant candidates (<5% at.): K (3), Ca (2), Na (2)
- measured range: 12-399 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La3Mn4AgO12 P2 (3) mp-1223238 [hull=0.056, PRIMARY]
- papers: Thermopower Studies of Polycrystalline Ag Doped LaMnO3 Manganites | High-performance La0.75K0.25MnO3:xAg2O composites based on electron-lattice and electron-magnetic coupling mechanism | Enhancement of magnetoresistance and near room-temperature temperature coefficient of resistivity in polycrystalline La0.7Ca0.24Na0.06MnO3 by silver doping

## Ag-Se-Sn
- rank 543 | 12 samples | 4 papers | 10 compositions
- compositions: Ag8SnSe6 (3); AgSn0.975Sn0.025Se2 (1); Ag7.975Cu0.025SnSe6 (1); Ag7.925Cu0.075SnSe6 (1); Ag7.95Cu0.05SnSe6 (1); Ag7.9Cu0.1SnSe6 (1)
- dopant candidates (<5% at.): Cu (4), Ta (4)
- seed hypothesis (confirm): argyrodite
- measured range: 155-789 K (5th-95th pct of 54 curves)
  !! MEASUREMENT CROSSES A TRANSITION: argyrodite -> argyrodite at ~330 K (Order-disorder transition to the cubic superionic phase, ~320-350 K.)
     Record each phase with its own temperature range, not a single prototype.
- [ref 1] TEDesignLab / ICSD: Ag8SnSe6 Pmn2_1 (31) mp-17984 [hull=0.000, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ag2SnSe3 Cc (9) mp-1096812 [hull=0.000, PRIMARY]; AgSnSe2 R-3m (166) mp-1229011 [hull=0.000, PRIMARY]
- papers: High thermoelectric properties for Sn-doped AgSbSe2 | N-type thermoelectric Ag8SnSe6 with extremely low lattice thermal conductivity by replacing Ag with Cu | Enhancement and manipulation of the thermoelectric properties of n-type argyrodite Ag8SnSe6 with ultralow thermal conductivity by controlling the carrier concentration through Ta doping

## Al-Fe-Ti-V
- rank 544 | 12 samples | 7 papers | 11 compositions
- compositions: Fe2(V0.7W0.1Ti0.2)Al (2); Fe2V0.6Ti0.3W0.1Al (1); Fe2V0.7Ti0.2W0.1Al (1); Fe2V0.65Ti0.25W0.1Al (1); (Fe1.97Co0.03)(V0.8Ti0.2)Al (1); Fe2V0.78Ti0.3Al0.92 (1)
- dopant candidates (<5% at.): W (5), Co (1), Ta (1)
- measured range: 16-797 K (5th-95th pct of 35 curves; full span incl. outliers 16-1243 K)
- papers: Effects of Heavy Element Substitution on Electronic Structure and Lattice Thermal Conductivity of Fe2VAl Thermoelectric Material | Effect of Ti Substitution on Thermoelectric Properties of W-Doped Heusler Fe2VAl Alloy | Thermoelectric Properties of P-Type Heusler Compounds (Fe<SUB>2&minus;<I>x</I></SUB>Co<I><SUB>x</SUB></I>)(V<SUB>1&minus;<I>y</I></SUB>Ti<I><SUB>y</SUB></I>)Al

## Al-Mn
- rank 545 | 12 samples | 3 papers | 6 compositions
- compositions: MnAl (5); Al22.5Mn77.5 (3); Al14.3Mn85.7 (1); Al20Mn80 (1); Al6Mn (1); Al17.5Mn82.5 (1)
- seed hypothesis (confirm): l10_tetragonal
- measured range: 10-299 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnAl6 Cmcm (63) mp-173 [hull=0.000, icsd=5, PRIMARY]; MnAl P4/mmm (123) mp-771 [hull=0.000, icsd=3, PRIMARY]; Mn4Al11 P-1 (2) mp-2856 [hull=0.000, icsd=2, PRIMARY]; Mn14Al56Ge3 P-3 (147) mp-706448 [hull=0.000, icsd=1, PRIMARY]; Mn5Al8 R3m (160) mp-1194040 [hull=0.075, icsd=1, PRIMARY]
- papers: Magnetic and electrical properties of icosahedral quasicrystalline Al-Mn alloys | Structural, Thermal and Electrical Properties of Al&ndash;Mn Quasicrystals Obtained by Melt Quenching | Orbital two-channel Kondo effect in epitaxial ferromagnetic L10-MnAl films

## Al-Pd
- rank 546 | 12 samples | 8 papers | 11 compositions
- compositions: Al71Pd20Re4.05Ru4.95_IQC (2); Al72.9Pd22.9Mn4.2 (1); Al71Pd20Re4.05Ru4.95 (1); Al73Pd22.9Mn4.1 (1); Al72.7Pd23.2Mn4.1 (1); Al70Pd22.5(Re0.5Mn0.5)7.5 (1)
- dopant candidates (<5% at.): Re (7), Mn (6), Ru (4), Fe (1), Co (1)
- measured range: 10-954 K (5th-95th pct of 33 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlPd Pm-3m (221) mp-829 [hull=0.033, icsd=3, PRIMARY]; Al21Pd8 I4_1/a (88) mp-1498 [hull=0.000, icsd=2, PRIMARY]; AlPd2 Pnma (62) mp-2824 [hull=0.000, icsd=2, PRIMARY]; Al2Pd Fm-3m (225) mp-16522 [hull=0.037, icsd=1, PRIMARY]; Al3Pd2 P-3m1 (164) mp-10901 [hull=0.000, icsd=1, PRIMARY]
- papers: Effect of Ru substitution for Re on the thermoelectric properties of AlPdRe icosahedral quasicrystals | Magnetic, electrical, thermal transport, and thermoelectric properties of theξ′andΨcomplex metallic alloy phases in the Al-Pd-Mn system | Thermoelectric properties of Al-Pd-Re(-Ru) icosahedral quasicrystals

## Al-Si-Sr
- rank 547 | 12 samples | 5 papers | 9 compositions
- compositions: SrAl2Si2 (3); SrSi1.8Al0.2 (2); Sr1Al2Si2 (1); Sr0.95Y0.05Al2Si2 (1); Sr0.9Y0.1Al2Si2 (1); Sr0.85Y0.15Al2Si2 (1)
- dopant candidates (<5% at.): Y (4), Eu (1)
- seed hypothesis (confirm): caal2si2_zintl
- measured range: 10-1167 K (5th-95th pct of 29 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr(AlSi)2 P-3m1 (164) mp-6931 [hull=0.000, icsd=2, PRIMARY]; SrAlSi P-6m2 (187) mp-3698 [hull=0.000, icsd=2, PRIMARY]; Sr3(AlSi)2 Immm (71) mp-7068 [hull=0.000, icsd=1, PRIMARY]
- papers: Structure and high-temperature thermoelectric properties of SrAl2Si2 | Investigation of Al substitution on the thermoelectric properties of SrSi2 | Electronic structure and transport properties of SrAl2Si2: Effect of yttrium substitution

## As-F-Fe-Nd-O
- rank 548 | 12 samples | 1 papers | 1 compositions
- compositions: NdFeAsOF (12)
- measured range: 17-403 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd4Fe4As4O3F I-42m (121) mp-1220250 [hull=0.169, PRIMARY]; Nd5Fe5As5O4F P-1 (2) mp-698941 [hull=0.160, PRIMARY]
- papers: Anisotropy of the transport properties of NdFeAs(O,F) thin films grown on vicinal substrates

## B-P
- rank 549 | 12 samples | 6 papers | 2 compositions
- compositions: BP (11); B12P2 (1)
- seed hypothesis (confirm): sphalerite
- measured range: 12-1068 K (5th-95th pct of 13 curves; full span incl. outliers 12-1384 K)
- [ref 1] TEDesignLab / ICSD: BP F-43m (216) mp-1479 [hull=0.000, icsd=6, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: B6P R-3m (166) mp-28395 [hull=0.000, icsd=3, PRIMARY]; B13P2 R-3m (166) mp-13862 [hull=0.962, icsd=1, PRIMARY]; B13P R3m (160) mp-1228630 [hull=0.116, PRIMARY]; B8P Cm (8) mp-1228676 [hull=0.151, PRIMARY]; BP P6_3mc (186) mp-1008559 [hull=0.012, icsd=1]
- papers: Thermoelectric Properties of Boron and Boron Phosphide CVD Wafers | Thermoelectric properties of boron phosphide | Thermoelectric figure of merit of boron phosphide

## Ba-Cu-Fe-La-O
- rank 550 | 12 samples | 3 papers | 10 compositions
- compositions: LaBaCuFeO5 (2); LaBa(Cu0.5Fe0.5)1.9W0.1O5 (2);  LaBaCuFeO5 (1); La0.75Pr0.25BaCuFeO5 (1); LaBaCuFe0.95Zn0.05O5 (1); LaBaCu0.9Co0.1FeO5 (1)
- dopant candidates (<5% at.): Co (2), W (2), Pr (1), Zn (1), Mn (1), Nb (1), Ni (1)
- measured range: 293-1077 K (5th-95th pct of 24 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2La2Fe2Cu2O11 P4mm (99) mp-706229 [hull=0.090, PRIMARY]; BaLaFe2Cu2O11 Pmm2 (25) mp-705604 [hull=0.281, PRIMARY]
- papers: Thermoelectric properties of layered ferrocuprates LnBaCuFeO5 + δ (Ln= La, Pr, Nd, Sm, Gd-Lu) | Structure and properties of solid solutions of La1 − x Pr x BaCuFeO5 + δ | Effect of heterovalent substitutions in the Cu and Fe sites on the thermal expansion and electrical properties of the layered ferrocuprate LaBaCuFeO5 + δ
