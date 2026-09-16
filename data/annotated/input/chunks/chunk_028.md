# Host systems -- chunk 028 of 73

Ranks 1351-1400 by sample count. These 50 host systems cover 200 samples (0.38% of the TE set); cumulative through this chunk: 92.81%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Ce-Fe-Mn-O-Zn
- rank 1351 | 4 samples | 1 papers | 4 compositions
- compositions: Mn0.58Zn0.37Ce0.4Fe1.65O4 (1); Mn0.58Zn0.37Ce0.6Fe1.45O4 (1); Mn0.58Zn0.37Ce0.8Fe1.25O4 (1); Mn0.58Zn0.37Ce1.0Fe1.05O4 (1)
- measured range: 310-490 K (5th-95th pct of 4 curves)
- papers: Thermoelectric power studies of cerium substituted Mn–Zn ferrites

## Ce-Ge-Ni-Ti
- rank 1352 | 4 samples | 1 papers | 4 compositions
- compositions: CeTi0.7Ni0.3Ge3 (1); CeTi0.6Ni0.4Ge3 (1); CeTi0.56Ni0.44Ge3 (1); CeTi0.55Ni0.45Ge3 (1)
- measured range: 10-294 K (5th-95th pct of 4 curves)
- papers: Ferromagnetic quantum critical behavior in heavy-fermion compounds CeTi1−xNixGe3

## Ce-Mg-Ni-Y
- rank 1353 | 4 samples | 2 papers | 2 compositions
- compositions: CeYMgNi2 (2); Ce0.5Y0.5MgNi4 (2)
- measured range: 210-373 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeY(MgNi4)2 R3m (160) mp-1226870 [hull=0.000, PRIMARY]
- papers: Thermoelectric Power and Electron Scattering in Metal Alloys | Thermoelectric properties of rare-earth alloys

## Ce-Nd-Pd-Th
- rank 1354 | 4 samples | 1 papers | 4 compositions
- compositions: Th0.2(Nd0.6Ce0.4)0.8Pd3 (1); Th0.2(Nd0.7Ce0.3)0.8Pd3 (1); Th0.3(Nd0.7Ce0.3)0.7Pd3 (1); Th0.3(Nd0.6Ce0.4)0.7Pd3 (1)
- solid-solution axis: Ce/(Ce+Th) spans 0.41-0.62 (median 0.55) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 12-303 K (5th-95th pct of 16 curves)
- papers: Modification of the thermoelectric properties of CePd3 by the substitution of neodymium and thorium

## Ce-O-Sb-Zn
- rank 1355 | 4 samples | 1 papers | 4 compositions
- compositions: Ce0.92Sr0.08ZnSbO (1); CeZnSbO (1); Ce0.96Sr0.04ZnSbO (1); Ce0.9Sr0.1ZnSbO (1)
- dopant candidates (<5% at.): Sr (3)
- measured range: 330-730 K (5th-95th pct of 20 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeZnSbO P4/nmm (129) mp-22620 [hull=0.029, icsd=2, PRIMARY]
- papers: Ce 1−x Sr x ZnSbO: New thermoelectric materials formed between intermetallics and oxides

## Ce-O-Sr
- rank 1356 | 4 samples | 1 papers | 2 compositions
- compositions: SrCe0.95Tm0.05O3 (2); SrCe0.75Zr0.20Tm0.05O3 (2)
- dopant candidates (<5% at.): Tm (4), Zr (2)
- measured range: 973-1173 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrCeO3 Pnma (62) mp-22428 [hull=0.008, icsd=14, PRIMARY]; Sr2CeO4 Pbam (55) mp-15743 [hull=0.000, icsd=3, PRIMARY]; SrCe2O4 Pnma (62) mp-770812 [hull=0.042, PRIMARY]
- papers: Effect of Zirconium Doping on Hydrogen Permeation through Strontium Cerate Membranes

## Ce-O-Sr-Zr
- rank 1357 | 4 samples | 1 papers | 1 compositions
- compositions: Sr(Ce0.6Zr0.4)0.85Y0.15O3 (4)
- dopant candidates (<5% at.): Y (4)
- measured range: 772-1172 K (5th-95th pct of 4 curves)
- papers: The proton conduction and hydrogen permeation characteristic of Sr(Ce0.6Zr0.4)0.85Y0.15O3−δ ceramic separation membrane

## Ce-Pd-Sn
- rank 1358 | 4 samples | 4 papers | 2 compositions
- compositions: CePdSn (3); Ce2Pd2.05Sn0.95 (1)
- measured range: 11-301 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeSnPd Pnma (62) mp-21490 [hull=0.000, icsd=5, PRIMARY]; Ce(Sn2Pd)2 Cmcm (63) mp-1104512 [hull=0.024, icsd=1, PRIMARY]; Ce(SnPd)2 P4/nmm (129) mp-1080026 [hull=0.002, icsd=1, PRIMARY]; CeSn3Pd2 Pbcm (57) mp-1191226 [hull=0.000, icsd=1, PRIMARY]; Ce4Sn25Pd12 Im-3 (204) mp-1202847 [hull=0.038, icsd=1, PRIMARY]
- papers: Thermoelectric power of the Kondo-lattice system: CePdSn | Transport properties of Ce2Ni2Sn and Ce2Pd2.05Sn0.95 Kondo lattice systems | Thermoelectric power of Ce-based Kondo alloys

## Ce-Pd-Y
- rank 1359 | 4 samples | 1 papers | 4 compositions
- compositions: Ce0.78Y0.22Pd3 (1); Ce0.22Y0.78Pd3 (1); Ce0.59Y0.41Pd3 (1); Ce0.4Y0.6Pd3 (1)
- solid-solution axis: Ce/(Ce+Y) spans 0.22-0.78 (median 0.59) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 14-296 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeYPd6 P4/mmm (123) mp-1226462 [hull=0.000, PRIMARY]
- papers: Thermoelectric power investigation of the (Ce, Y)Pd3 system

## Ce-Rh-Ru-Si
- rank 1360 | 4 samples | 1 papers | 4 compositions
- compositions: Ce(Rh0.80Ru0.20)2Si2 (1); Ce(Rh0.6Ru0.4)2Si2 (1); Ce(Rh0.75Ru0.25)2Si2	 (1); Ce(Rh0.65Ru0.35)2Si2 (1)
- measured range: 11-294 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeSi2RuRh I-4m2 (119) mp-1226491 [hull=0.000, PRIMARY]
- papers: Electrical resistivity and thermopower studies of Ce(Rh1−xRux)2Si2 compounds with 0 ⩽ x ⩽ 0.4

## Ce-Se
- rank 1361 | 4 samples | 2 papers | 3 compositions
- compositions: CeSe2 (2); CeSe1.9Sn0.1 (1); Ce0.9Cu0.1Se2 (1)
- dopant candidates (<5% at.): Sn (1), Cu (1)
- measured range: 10-897 K (5th-95th pct of 17 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeSe Fm-3m (225) mp-906175 [hull=0.000, icsd=7, PRIMARY]; CeSe2 P2_1/c (14) mp-1320 [hull=0.040, icsd=4, PRIMARY]; Ce10Se14O I4_1/acd (142) mp-1198305 [hull=0.008, icsd=1, PRIMARY]; Ce10Se19 P4_2/n (86) mp-652044 [hull=0.023, icsd=1, PRIMARY]; Ca(Ce2Se3)4 Cc (9) mp-38870 [hull=0.005, PRIMARY]
- papers: Low-temperature thermoelectric properties of the CeSe2−xSnx compounds | Thermoelectricity and localized f-band control by dp-hybridization on the Ce1−xCuxSe2 compounds

## Ce-Si
- rank 1362 | 4 samples | 4 papers | 2 compositions
- compositions: CeSi2 (3); Ce3Si2 (1)
- measured range: 206-380 K (5th-95th pct of 9 curves; full span incl. outliers 206-1273 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeSi2 I4_1/amd (141) mp-1072078 [hull=0.000, icsd=11, PRIMARY]; CeSi Pnma (62) mp-21115 [hull=0.000, icsd=8, PRIMARY]; Ce5Si4 P4_12_12 (92) mp-1196829 [hull=0.009, icsd=5, PRIMARY]; Ce3Si2 P4/mbm (127) mp-1079007 [hull=0.001, icsd=3, PRIMARY]; Ce2Si7 Cmmm (65) mp-1079241 [hull=0.070, icsd=1, PRIMARY]
- papers: Thermoelectric properties of the solid solutions based on ThSi2-type CeSi2 compound | Thermoelectric Power and Electron Scattering in Metal Alloys | Thermoelectric properties of rare-earth alloys

## Cl-Cu-Te
- rank 1363 | 4 samples | 1 papers | 1 compositions
- compositions: Cu9.1Te4Cl3 (4)
- measured range: 294-523 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuTe2Cl P2_1/c (14) mp-30971 [hull=0.000, icsd=1, PRIMARY]
- papers: Cu9.1Te4Cl3: A Thermoelectric Compound with Low Thermal and High Electrical Conductivity

## Cm-O
- rank 1364 | 4 samples | 2 papers | 2 compositions
- compositions: Cm2O3 (3); CmO2 (1)
- measured range: 297-1277 K (5th-95th pct of 4 curves)
- papers: Thermophysical properties of NpO2, AmO2 and CmO2 | Modelling thermal conductivity and self-irradiation effects in mixed oxide fuels

## Co
- rank 1365 | 4 samples | 3 papers | 3 compositions
- compositions: Co (2); Rb3Co60 (1); K3Co60 (1)
- dopant candidates (<5% at.): Rb (1), K (1)
- measured range: 14-762 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co P6_3/mmc (194) mp-54 [hull=0.000, icsd=10, PRIMARY]; Co Fm-3m (225) mp-102 [hull=0.019, icsd=10]; Co Fd-3m (227) mp-1072089 [hull=0.207, icsd=2]; Co P6_3mc (186) mp-669382 [hull=0.120, icsd=1]; Co P4_2/mnm (136) mp-1193227 [hull=0.130, icsd=1]
- papers: Compatibility between Co-Metallized PbTe Thermoelectric Legs and an Ag–Cu–In Brazing Alloy | Skew scattering dominated anomalous Hall effect in Co<sub> <i>x</i> </sub>(MgO)<sub>100−<i>x</i> </sub> granular thin films | Fermi-liquid behavior in the electrical resistivity of<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">K</mml:mi></mml:mrow><mml:mrow><mml:mn>3</mml:mn></mml:mrow></mml:msub></mml:mrow></mml:math><mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">C</mml:mi></mml:mrow><mml:mrow><mml:mn>60</mml:mn></mml:mrow></mml:msub></mml:mrow></mml:math>and<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">Rb</mml:mi></mml:mrow><mml:mrow><mml:mn>3</mml:mn></mml:mrow></mml:msub></mml:mrow></mml:math><mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">C</mml:mi></mml:mrow><mml:mrow><mml:mn>60</mml:mn></mml:mrow></mml:msub></mml:mrow></mml:math>

## Co-Cr-Fe-O
- rank 1366 | 4 samples | 1 papers | 4 compositions
- compositions: CoCrFeO4 (1); CoCr0.5Fe1.5O4 (1); CoCr0.7Fe1.3O4 (1); CoCr0.9Fe1.1O4 (1)
- measured range: 299-885 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CrFeCoO4 Imma (74) mp-1226366 [hull=0.065, PRIMARY]
- papers: Thermoelectric power studies of Co–Cr nano ferrites

## Co-Cu
- rank 1367 | 4 samples | 1 papers | 4 compositions
- compositions: Co15Cu85 (1); Co20Cu80 (1); Co30Cu70 (1); Co25Cu75 (1)
- measured range: 13-270 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co3Cu I4/mmm (139) mp-1183752 [hull=0.124, PRIMARY]
- papers: Enhancement of thermoelectric efficiency in granular Co-Cu thin films from spin-dependent scattering

## Co-Cu-La-O
- rank 1368 | 4 samples | 2 papers | 4 compositions
- compositions: LaCo0.75Cu0.25O3 (1); LaMn0.1Co0.6Cu0.3O3 (1); LaMn0.05Co0.55Cu0.4O3 (1); LaCo0.5Cu0.5O3 (1)
- dopant candidates (<5% at.): Mn (2)
- measured range: 325-1183 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La3Co2CuO9 P-3c1 (165) mp-1223344 [hull=0.014, PRIMARY]; La7SmCo5(CuO8)3 Cm (8) mp-1075961 [hull=0.067, PRIMARY]; La7SmCo5Cu3O20 P1 (1) mp-1076880 [hull=0.071, PRIMARY]; La7SmCo6(CuO10)2 P1 (1) mp-1076871 [hull=0.067, PRIMARY]; La7SmCo6(CuO12)2 Cmm2 (35) mp-1077605 [hull=0.077, PRIMARY]
- papers: The effect of Cu substitution on microstructure and thermoelectric properties of LaCoO3 ceramics | Investigation of the quasi-ternary system LaMnO3–LaCoO3–“LaCuO3”. II: The series LaMn0.25−x Co0.75−x Cu2x O3−δ and LaMn0.75−x Co0.25−x Cu2x O3−δ

## Co-Cu-S-Ti
- rank 1369 | 4 samples | 1 papers | 2 compositions
- compositions: Cu2CoTi3S8 (2); Cu2Co1.5Ti2.5S8 (2)
- measured range: 297-679 K (5th-95th pct of 20 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti3Co(CuS4)2 R-3m (166) mp-1217164 [hull=0.033, PRIMARY]; TiCoCuS4 Imma (74) mp-1216991 [hull=0.046, PRIMARY]
- papers: A comparative study of thermoelectric Cu2TrTi3S8 (Tr = Co and Sc) thiospinels: Enhanced Seebeck coefficient via electronic structure modification

## Co-Fe-Hf-Nb-Sb-Ta-Ti-V-Zr
- rank 1370 | 4 samples | 1 papers | 4 compositions
- compositions: Ti0.167Zr0.167Hf0.167V0.167Nb0.167Ta0.167Fe0.7Co0.3Sb (1); Ti0.167Zr0.167Hf0.167V0.167Nb0.167Ta0.167Fe0.5Co0.5Sb (1); Ti0.167Zr0.167Hf0.167V0.167Nb0.167Ta0.167Fe0.6Co0.4Sb (1); Ti0.167Zr0.167Hf0.167V0.167Nb0.167Ta0.167Fe0.4Co0.6Sb (1)
- measured range: 319-924 K (5th-95th pct of 20 curves)
- papers: Synthesis and thermoelectric properties of high-entropy half-Heusler MFe1−xCoxSb (M = equimolar Ti, Zr, Hf, V, Nb, Ta)

## Co-Fe-La-Si
- rank 1371 | 4 samples | 4 papers | 4 compositions
- compositions: Ce0.05La0.95Co10Fe2Si (1); Ce0.05La0.95Co10Fe2Si	 (1); LaFe11.05Co0.91Si1.04 (1); LaFe10.5Co1.0Si1.5 (1)
- dopant candidates (<5% at.): Ce (2)
- measured range: 89-374 K (5th-95th pct of 8 curves)
- papers: Thermoelectric Power and Electron Scattering in Metal Alloys | Thermoelectric properties of rare-earth alloys | The maximal cooling power of magnetic and thermoelectric refrigerators with La(FeCoSi)13 alloys

## Co-Ge
- rank 1372 | 4 samples | 1 papers | 4 compositions
- compositions: Co0.96Fe0.04Ge (1); Co0.96Ni0.04Ge (1); CoGe (1); Co0.92Ni0.08Ge (1)
- dopant candidates (<5% at.): Ni (2), Fe (1)
- measured range: 12-300 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co2Ge P6_3/mmc (194) mp-1667 [hull=0.051, icsd=4, PRIMARY]; CoGe C2/m (12) mp-21237 [hull=0.000, icsd=3, PRIMARY]; Co5Ge7 I4mm (107) mp-22732 [hull=0.570, icsd=2, PRIMARY]; CoGe2 Cmce (64) mp-30045 [hull=0.000, icsd=1, PRIMARY]; Co3Ge2 P-6m2 (187) mp-1226445 [hull=0.068, PRIMARY]
- papers: Band-filling dependence of thermoelectric properties in B20-type CoGe

## Co-H-O
- rank 1373 | 4 samples | 2 papers | 3 compositions
- compositions: H0.3CoO2 (2); Na0.33K0.02(H2O)1.33CoO2 (1); Na0.07K0.21(H2O)0.63CoO2 (1)
- dopant candidates (<5% at.): Na (2), K (2)
- measured range: 11-289 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CoHO2 R-3m (166) mp-31526 [hull=0.000, icsd=1, PRIMARY]; Co(HO)2 P-3m1 (164) mp-25489 [hull=0.186, icsd=1, PRIMARY]; CoHO2 P6_3/mmc (194) mp-743839 [hull=0.125, icsd=1]; CoHO2 P1 (1) mp-1181722 [hull=0.111]; Co(HO)2 C2 (5) mp-625953 [hull=0.046]
- papers: Thermopower and Co K-edge studies of potassium sodium cobalt oxyhydrates Na0.33K0.02(H2O)1.33CoO2−δ and Na0.07K0.21(H2O)0.63CoO2−δ | Weakly correlated triangular lattice metal HxCoO2withxap0.3

## Co-Hf-Rh-Sb-Zr
- rank 1374 | 4 samples | 2 papers | 4 compositions
- compositions: Zr0.5Hf0.5Co0.4Rh0.6Sb0.99Sn0.01 (1); Zr0.5Hf0.5Co0.8Rh0.2Sb0.99Sn0.01 (1); Zr0.5Hf0.5Co0.7Rh0.3Sb0.99Sn0.01 (1); Zr0.5Hf0.5Co0.4Rh0.6Sb0.85Sn0.15 (1)
- dopant candidates (<5% at.): Sn (4)
- solid-solution axis: Co/(Co+Rh) spans 0.40-0.80 (median 0.70) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 300-773 K (5th-95th pct of 21 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HfZrCoSb2Rh R3m (160) mp-1224248 [hull=0.692, PRIMARY]
- papers: Effects of Rh on the thermoelectric performance of the p-type Zr0.5Hf0.5Co1−xRhxSb0.99Sn0.01 half-Heusler alloys | Thermoelectric performance of nanostructured p-type Zr0.5Hf0.5Co0.4Rh0.6Sb1−xSnx half-Heusler alloys

## Co-Hf-Sn
- rank 1375 | 4 samples | 2 papers | 2 compositions
- compositions: Co2HfSn (3); HfCo1.5Sn (1)
- measured range: 11-779 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HfCo2Sn Fm-3m (225) mp-20730 [hull=0.000, icsd=5, PRIMARY]; HfCoSn P-62c (190) mp-22315 [hull=0.000, icsd=2, PRIMARY]; Hf5CoSn3 P6_3/mcm (193) mp-1212526 [hull=0.000, PRIMARY]; HfCoSn P-62m (189) mp-1080733 [hull=0.178, icsd=1]
- papers: MCo1.5Sn (M = Ti, Zr, and Hf) ternary compounds: a class of three-quarter Heusler compounds | Synthesis and Characterization of Thermoelectric Co2XSn (X = Zr, Hf) Heusler Alloys

## Co-In-S-Se-Sn
- rank 1376 | 4 samples | 1 papers | 4 compositions
- compositions: Co3InSnS1.6Se0.4 (1); Co3InSnSSe (1); Co3InSnS1.4Se0.6 (1); Co3InSnS1.2Se0.8 (1)
- solid-solution axis: S/(S+Se) spans 0.50-0.80 (median 0.70) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 28-297 K (5th-95th pct of 20 curves)
- papers: The effect of simultaneous substitution on the electronic band structure and thermoelectric properties of Se-doped Co3SnInS2 with the Kagome lattice

## Co-In-Sb
- rank 1377 | 4 samples | 3 papers | 4 compositions
- compositions: In0.9Fe0.5Co3.5Sb12 (1); In1.2Co4Sb12 (1); (InSb)0.4In0.5Co4Sb12 (1); (InSb)0.5In0.5Co4Sb12 (1)
- dopant candidates (<5% at.): Fe (1)
- measured range: 11-722 K (5th-95th pct of 17 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): In(CoSb3)16 C2/m (12) mp-1224696 [hull=0.009, PRIMARY]; In(CoSb3)20 C2/m (12) mp-1224652 [hull=0.007, PRIMARY]
- papers: Low-Temperature Transport Properties of In x Fe y Co4−y Sb12 | Thermoelectric Properties of Co4Sb12 Skutterudite Materials with Partial In Filling and Excess In Additions | Enhanced Thermoelectric Properties of In-Filled Co4Sb12 with InSb Nanoinclusions

## Co-Li-Na-O
- rank 1378 | 4 samples | 2 papers | 4 compositions
- compositions: Li0.41Na0.31CoO2 (1); Li0.40Na0.18CoO2 (1); Li0.40Na0.36CoO2 (1); Li0.42Na0.36CoO2 (1)
- solid-solution axis: Li/(Li+Na) spans 0.53-0.69 (median 0.57) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 11-768 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Na2Li2CoO4 P2_1/c (14) mp-763254 [hull=0.022, PRIMARY]; Na2Li2CoO4 P1 (1) mp-861533 [hull=0.046]
- papers: Magnetic and thermoelectric properties of layered LixNayCoO2 | Electrical and Magnetic Properties of the Li

## Co-Li-Ni-O
- rank 1379 | 4 samples | 2 papers | 4 compositions
- compositions: LiNi0.5Co0.5O2 (1); LiNi0.25Co0.75O2 (1); LiNi0.8Co0.2O2 (1); LiCo0.8Ni0.2O2 (1)
- measured range: 14-1181 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li10Co3Ni7O20 P-1 (2) mp-769555 [hull=0.005, PRIMARY, AMBIGUOUS]; Li10CoNi9O20 P1 (1) mp-765279 [hull=0.000, PRIMARY, AMBIGUOUS]; Li2Co(NiO3)2 Aea2 (41) mp-761662 [hull=0.066, PRIMARY]; Li2Co2NiO6 P-1 (2) mp-1178201 [hull=0.090, PRIMARY]; Li2Co3NiO8 P4_332 (212) mp-762296 [hull=0.001, PRIMARY, AMBIGUOUS]
- papers: Transport properties of the LiNi1−yCoyO2 system | Thermoelectric properties of LiCo1−xMxO2(M = Cu, Mg, Ni, Zn): Comparison with LiyCoO2and NayCoO2systems

## Co-Mn-Sn-Ti
- rank 1380 | 4 samples | 1 papers | 4 compositions
- compositions: Co2Mn0.8Ti0.2Sn (1); Co2Mn0.6Ti0.4Sn (1); Co2Mn0.4Ti0.6Sn (1); Co2Mn0.2Ti0.8Sn (1)
- measured range: 10-395 K (5th-95th pct of 12 curves)
- papers: Phase-separation-induced changes in the magnetic and transport properties of the quaternary Heusler alloyCo2Mn1−xTixSn

## Co-Nb-Sn-Ti
- rank 1381 | 4 samples | 2 papers | 4 compositions
- compositions: CoNb0.8Ti0.2Sn (1); CoNb0.2Ti0.8Sn (1); CoNb0.5Ti0.5Sn (1); Nb0.8Ti0.2CoSn (1)
- measured range: 321-842 K (5th-95th pct of 13 curves)
- papers: High temperature thermoelectric properties of CoNb1−xMxSn half-Heusler compounds | Impact of Nb vacancies and p-type doping of the NbCoSn–NbCoSb half-Heusler thermoelectrics

## Co-Ni-O
- rank 1382 | 4 samples | 1 papers | 4 compositions
- compositions: Ca0.01NiCo2O4 (1); NiCo2O4 (1); Ca0.03NiCo2O4 (1); Ca0.05NiCo2O4 (1)
- dopant candidates (<5% at.): Ca (3)
- measured range: 295-1074 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co(NiO2)2 Fd-3m (227) mp-769882 [hull=0.054, PRIMARY]; Co(NiO2)4 C2/m (12) mp-772058 [hull=0.014, PRIMARY]; Co2NiO4 Imma (74) mp-38683 [hull=0.000, PRIMARY]; Co2NiO6 Cmce (64) mp-761554 [hull=0.043, PRIMARY, AMBIGUOUS]; Co3NiO8 R-3m (166) mp-765866 [hull=0.071, PRIMARY, AMBIGUOUS]
- papers: Synthesis and thermoelectric characterization of polycrystalline Ni1-xCaxCo2O4(x=0–0.05) spinel materials

## Co-Ni-Sn-Ti
- rank 1383 | 4 samples | 2 papers | 3 compositions
- compositions: TiNiCo0.25Sn (2); TiNiCo0.75Sn (1); TiNiCo0.5Sn (1)
- measured range: 309-732 K (5th-95th pct of 19 curves; full span incl. outliers 309-1022 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti2CoNiSn2 R3m (160) mp-1217160 [hull=0.689, PRIMARY]; Ti8Co3NiSn4 R-3m (166) mp-1217234 [hull=0.242, PRIMARY]; TiCoNiSn F-43m (216) mp-1216950 [hull=0.050, PRIMARY]
- papers: Metal Distributions, Efficient n-Type Doping, and Evidence for in-Gap States in TiNiMySn (M = Co, Ni, Cu) half-Heusler Nanocomposites | Thermoelectric properties control of Half-Heusler compounds by lattice defects and interfaces introduced based on the close relationship with Heusler compounds

## Co-O-Ru
- rank 1384 | 4 samples | 1 papers | 4 compositions
- compositions: Co2.35Ru0.65O4.43 (1); Co2.5Ru0.5O4.3 (1); Co2.4Ru0.6O4.4 (1); Co2.3Ru0.7O4.47 (1)
- measured range: 299-1076 K (5th-95th pct of 14 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co2RuO4 Imma (74) mp-34586 [hull=0.029, PRIMARY, AMBIGUOUS]; Co5RuO8 R-3m (166) mp-35690 [hull=0.040, PRIMARY]; Co7(RuO6)2 P1 (1) mp-690550 [hull=0.034, PRIMARY]; Co9Ru3O16 P-1 (2) mp-698596 [hull=0.024, PRIMARY]; Co2RuO4 C2/c (15) mp-767177 [hull=0.037]
- papers: Synthesis, crystal structures and high-temperature thermoelectric properties of spinel-type cobalt ruthenium oxides

## Co-O-Sb
- rank 1385 | 4 samples | 3 papers | 3 compositions
- compositions: (CoSb3)0.9(ZrO2)0.1 (2); (CoSb3)92.17(Al2O3)7.83 (1); (ZrO2)0.1(CoSb3)0.9 (1)
- dopant candidates (<5% at.): Zr (3), Al (1)
- measured range: 296-799 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co(SbO2)2 P4_2/mbc (135) mp-1193389 [hull=0.000, icsd=2, PRIMARY]; Co(SbO3)2 P4_2/mnm (136) mp-24845 [hull=0.000, icsd=1, PRIMARY]; Co(SbO9)2 P3 (143) mp-1201975 [hull=0.910, icsd=1, PRIMARY]; Co2Sb2O7 Fd-3m (227) mp-1192102 [hull=0.139, icsd=1, PRIMARY]; Co2SbO6 Cmce (64) mp-859782 [hull=0.091, PRIMARY]
- papers: Effects of Nano-α-Al2O3 Dispersion on the Thermoelectric and Mechanical Properties of CoSb3 Composites | Nano ZrO2/CoSb3 composites with improved thermoelectric figure of merit | Processing and Characterization of Nano-structured ZrO2/CoSb3 Thermoelectric Composites

## Co-O-Sb-Zr
- rank 1386 | 4 samples | 3 papers | 3 compositions
- compositions: (CoSb3)0.7(ZrO2)0.3 (2); (ZrO2)0.3CoSb3 (1); (ZrO2)0.3(CoSb3)0.7 (1)
- measured range: 267-773 K (5th-95th pct of 11 curves)
- papers: Control of thermoelectric properties in ZrO2/CoSb3 nano-dispersed composites | Nano ZrO2/CoSb3 composites with improved thermoelectric figure of merit | Processing and Characterization of Nano-structured ZrO2/CoSb3 Thermoelectric Composites

## Co-O-Sr-Tb
- rank 1387 | 4 samples | 2 papers | 2 compositions
- compositions: SrTbCoO4 (3); Sr0.7Tb0.3CoO3 (1)
- measured range: 12-350 K (5th-95th pct of 4 curves; full span incl. outliers 12-1123 K)
- papers: Studies of structural, magnetic, electrical and thermal properties in layered perovskite cobaltite SrLnCoO4 (Ln = La, Ce, Pr, Nd, Eu, Gd and Tb) | Design of Sr<sub>0.7</sub>R<sub>0.3</sub>CoO<sub>3-δ</sub>(R = Tb and Er) Perovskites Performing as Cathode Materials in Solid Oxide Fuel Cells

## Co-S
- rank 1388 | 4 samples | 2 papers | 1 compositions
- compositions: CoS2 (4)
- measured range: 10-678 K (5th-95th pct of 14 curves)
- [ref 1] TEDesignLab / ICSD: Co9S8 Fm-3m (225) mp-1513 [hull=0.000, icsd=7, PRIMARY]; Co3S4 Fd-3m (227) mp-943 [hull=0.000, icsd=6, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: CoS2 Pa-3 (205) mp-2070 [hull=0.000, icsd=19, PRIMARY]; CoS P6_3/mmc (194) mp-1274 [hull=0.194, icsd=6, PRIMARY]; Co2S3 R-3c (167) mp-1183728 [hull=0.008, PRIMARY]; Co3S P6_3/mmc (194) mp-1183733 [hull=0.490, PRIMARY]; CoS2 Pbca (61) mp-850049 [hull=0.016, icsd=20]
- papers: Thermoelectric figure of merit of M-sulphides (M=Fe, Co, Ni, Pd) thin films | Transport and magnetic properties of highly densified CoS2 ceramic

## Co-S-Sn
- rank 1389 | 4 samples | 2 papers | 4 compositions
- compositions: Co3Sn2S2 (1); Co3Sn1.8In0.2S2 (1); Co2.667Fe0.333Sn1.8In0.2S2 (1); Co2.667Fe0.333Sn1.7In0.3S2 (1)
- dopant candidates (<5% at.): In (3), Fe (2)
- measured range: 297-678 K (5th-95th pct of 16 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co3(SnS)2 R-3m (166) mp-19807 [hull=0.000, icsd=13, PRIMARY]
- papers: Interplay of Metal-Atom Ordering, Fermi Level Tuning, and Thermoelectric Properties in Cobalt Shandites Co3M2S2(M = Sn, In) | Improved Thermoelectric Performance through Double Substitution in Shandite-Type Mixed-Metal Sulfides

## Co-Sb-U
- rank 1390 | 4 samples | 1 papers | 1 compositions
- compositions: UCo0.5Sb2 (4)
- measured range: 10-284 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U3Co3Sb4 I-43d (220) mp-1188905 [hull=0.000, icsd=2, PRIMARY]
- papers: Weak localization effect in the strongly ferromagnetic Kondo compoundUCo0.5Sb2

## Co-Sn-Zr
- rank 1391 | 4 samples | 2 papers | 2 compositions
- compositions: Co2ZrSn (3); ZrCo1.5Sn (1)
- measured range: 15-777 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZrCo2Sn Fm-3m (225) mp-914303 [hull=0.000, icsd=7, PRIMARY]; ZrCoSn P-62m (189) mp-30563 [hull=0.000, icsd=2, PRIMARY]; Zr6CoSn2 P-62m (189) mp-1206072 [hull=0.001, PRIMARY]; Zr18Co5Sn4 Pm (6) mp-1216388 [hull=0.000, PRIMARY]
- papers: MCo1.5Sn (M = Ti, Zr, and Hf) ternary compounds: a class of three-quarter Heusler compounds | Synthesis and Characterization of Thermoelectric Co2XSn (X = Zr, Hf) Heusler Alloys

## Co-Te
- rank 1392 | 4 samples | 1 papers | 1 compositions
- compositions: Co0.76Te (4)
- measured range: 77-295 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CoTe2 Pnnm (58) mp-9945 [hull=0.016, icsd=8, PRIMARY]; CoTe P6_3/mmc (194) mp-788 [hull=0.091, icsd=3, PRIMARY]; Co19Te34 P-1 (2) mp-684822 [hull=0.003, PRIMARY]; Co5Te6 R-3 (148) mp-1226090 [hull=0.049, PRIMARY]; Co3Te I4/mmm (139) mp-1183699 [hull=0.299, PRIMARY]
- papers: Thermoelectric and magnetic measurements on polycrystalline and single-crystal Co1−xTe

## Cr-Fe-Si
- rank 1393 | 4 samples | 2 papers | 4 compositions
- compositions: (Fe0.9Cr01Si2)0.995Cu0.005 (1); Fe0.9Cr0.1Si (1); Fe0.85Cr0.15Si (1); Fe0.875Cr0.125Si (1)
- dopant candidates (<5% at.): Cu (1)
- measured range: 11-942 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CrFe2Si Fm-3m (225) mp-1018068 [hull=0.077, icsd=1, PRIMARY]; CrFe11Si4 R-3m (166) mp-1226343 [hull=0.024, PRIMARY]; CrFeSi2 P2_1 (4) mp-1226256 [hull=0.055, PRIMARY]
- papers: High temperature thermoelectric properties of p- and n-type β-FeSi2 with some dopants | Metal to insulator transition and an impurity band conduction in Fe 1−x Cr x Si

## Cr-La-S
- rank 1394 | 4 samples | 1 papers | 1 compositions
- compositions: (LaS)1.20CrS2 (4)
- measured range: 297-972 K (5th-95th pct of 16 curves)
- [ref 1] TEDesignLab / ICSD: LaCrS3 Pnma (62) mp-10328 [hull=0.000, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: La4CrS7 P6_3 (173) mp-1191612 [hull=0.230, icsd=1, PRIMARY]; La3CrS6 Pnnm (58) mp-1211604 [hull=0.024, PRIMARY]
- papers: Microstructural Control and Thermoelectric Properties of Misfit Layered Sulfides (LaS)1+mTS2(T = Cr, Nb): The Natural Superlattice Systems

## Cr-N-O
- rank 1395 | 4 samples | 1 papers | 4 compositions
- compositions: Cr(N0.89O0.11) (1); Cr(N0.87O0.13) (1); Cr(N0.81O0.19) (1); Cr(N0.55O0.45) (1)
- measured range: 76-291 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CrN3O4 Pnma (62) mp-1197873 [hull=2.240, icsd=2, PRIMARY]; CrN3O8 Pca2_1 (29) mp-1194673 [hull=2.060, icsd=2, PRIMARY]; Cr2N2O7 C2/c (15) mp-1181809 [hull=0.676, icsd=1, PRIMARY]; Cr(NO2)2 C2/m (12) mp-1105281 [hull=0.793, icsd=1, PRIMARY]; Cr4PN3O16 R3m (160) mp-1191548 [hull=1.048, icsd=1, PRIMARY]
- papers: Changes in the electric resistivity of CrN subsequent to oxygen dissolution

## Cr-O-Sn
- rank 1396 | 4 samples | 1 papers | 4 compositions
- compositions: (CrO2)0.8(SnO2)0.2 (1); (CrO2)0.6(SnO2)0.4 (1); (CrO2)0.5(SnO2)0.5 (1); (CrO2)0.3(SnO2)0.7 (1)
- measured range: 11-300 K (5th-95th pct of 4 curves)
- papers: Magnetic and magnetotransport properties of half-metallic CrO2-SnO2 composites

## Cr-Si-V
- rank 1397 | 4 samples | 1 papers | 4 compositions
- compositions: Cr0.8V0.2Si2 (1); Cr0.7V0.3Si2 (1); Cr0.51V0.49Si2 (1); Cr0.26V0.74Si2 (1)
- measured range: 60-321 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): V(CrSi3)2 C222 (21) mp-1216563 [hull=0.017, PRIMARY]; V2(CrSi)3 Ibam (72) mp-1216681 [hull=0.015, PRIMARY]; V3Cr3Si2 R32 (155) mp-1216481 [hull=0.000, PRIMARY]; VCrSi Amm2 (38) mp-1216382 [hull=0.246, PRIMARY]; VCrSi4 P2 (3) mp-1216378 [hull=0.016, PRIMARY]
- papers: Thermoelectric and magnetic properties of Cr1 − xVxSi2 solid solutions

## Cu-Er-O-Sr-Tl
- rank 1398 | 4 samples | 1 papers | 4 compositions
- compositions: TlSr2ErCu2O7 (1); TlSr2(Er0.8Sr0.2)Cu2O7 (1); TlSr2(Er0.7Sr0.3)Cu2O7 (1); TlSr2(Er0.9Sr0.1)Cu2O7 (1)
- measured range: 22-290 K (5th-95th pct of 4 curves)
- papers: Thermopower and Resistivity of 1212-Type Phase TlSr2(Er1-ySry)Cu2O7-δ

## Cu-Er-Te
- rank 1399 | 4 samples | 2 papers | 4 compositions
- compositions: Cu2ErTe3 (1); Cu2.9Ag0.1ErTe3 (1); Cu2.7Ag0.3ErTe3 (1); Cu3ErTe3 (1)
- dopant candidates (<5% at.): Ag (2)
- measured range: 297-903 K (5th-95th pct of 19 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Er(CuTe)3 Pmn2_1 (31) mp-640885 [hull=0.000, icsd=1, PRIMARY]; Er7(CuTe4)3 Cm (8) mp-685943 [hull=0.008, PRIMARY]; ErCuTe2 P3m1 (156) mp-1225521 [hull=0.033, PRIMARY]; Er(CuTe)3 R-3 (148) mp-1225130 [hull=0.048]; ErCuTe2 P-3m1 (164) mp-1206650 [hull=0.103]
- papers: Cu3ErTe3: a new promising thermoelectric material predicated by high-throughput screening | Ternary Compounds Cu3RTe3 (R = Y, Sm, and Dy): A Family of New Thermoelectric Materials with Trigonal Structures

## Cu-Fe-Ge-S
- rank 1400 | 4 samples | 1 papers | 1 compositions
- compositions: Cu22Fe8Ge4S32 (4)
- measured range: 300-701 K (5th-95th pct of 20 curves)
- [ref 1] TEDesignLab / ICSD: FeCu2GeS4 I-42m (121) mp-917359 [hull=0.041, icsd=5, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Fe2Cu13(GeS8)2 P-43m (215) mp-1227624 [hull=0.017, PRIMARY]; FeCu6GeS8 F-43m (216) mp-1225017 [hull=0.000, PRIMARY]; FeCu2GeS4 I-4 (82) mp-1225065 [hull=0.042]
- papers: Structure, microstructure and thermoelectric properties of germanite-type Cu22Fe8Ge4S32 compounds
