# Host systems -- chunk 039 of 73

Ranks 1901-1950 by sample count. These 50 host systems cover 100 samples (0.19% of the TE set); cumulative through this chunk: 95.91%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## As-Na-Sn
- rank 1901 | 2 samples | 1 papers | 1 compositions
- compositions: NaSn2As2 (2)
- measured range: 302-369 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Na5SnAs3 P2_1/c (14) mp-5248 [hull=0.000, icsd=2, PRIMARY]; Na(SnAs)2 R-3m (166) mp-9378 [hull=0.000, icsd=1, PRIMARY]
- papers: Axis-dependent carrier polarity in polycrystalline NaSn2As2

## As-S-Th
- rank 1902 | 2 samples | 1 papers | 1 compositions
- compositions: ThAs1.23S0.77 (2)
- measured range: 12-321 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ThAsS P4/nmm (129) mp-1019358 [hull=0.000, icsd=1, PRIMARY]; Th2AsS2 P4/mmm (123) mp-1207041 [hull=2.147, PRIMARY]
- papers: Anomalous transport properties in thorium arsenosulphide crystals

## As-S-U
- rank 1903 | 2 samples | 1 papers | 1 compositions
- compositions: UAsS (2)
- measured range: 14-296 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UAsS P4/nmm (129) mp-4374 [hull=0.000, icsd=4, PRIMARY]; U2AsS R-3m (166) mp-1216688 [hull=0.002, PRIMARY]; U2AsS2 P4/mmm (123) mp-1206491 [hull=1.659, PRIMARY]
- papers: A Kondo-like thermoelectric power behaviour of UAsSe ferromagnet

## As-Se-Te
- rank 1904 | 2 samples | 1 papers | 1 compositions
- compositions: As2SeTe2 (2)
- measured range: 300-313 K (5th-95th pct of 2 curves)
- papers: Effect of γ-irradiation on non-linear I-V behaviour and thermoelectric measurements in amorphous semiconducting AsSeTe system

## Au-Ba-Ga-Ge
- rank 1905 | 2 samples | 1 papers | 2 compositions
- compositions: Ba8Au4Ga4Ge38 (1); Ba8Au3Ga7Ge36 (1)
- measured range: 10-771 K (5th-95th pct of 12 curves)
- papers: Thermoelectric properties of Au-containing type-I clathrates Ba8AuxGa16−3xGe30+2x

## Au-Ba-Ga-Si
- rank 1906 | 2 samples | 1 papers | 2 compositions
- compositions: Ba8Au4Ga4Si38 (1); Ba8Au3Ga7Si36 (1)
- measured range: 302-871 K (5th-95th pct of 4 curves)
- papers: Effect of Au substitution on thermoelectric properties of silicon clathrate compounds

## Au-Cu-Yb
- rank 1907 | 2 samples | 2 papers | 2 compositions
- compositions: YbCu4Au (1); YbAuCu4 (1)
- measured range: 10-276 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbCu4Au F-43m (216) mp-1077165 [hull=0.000, icsd=1, PRIMARY]
- papers: Low temperature hall effect and thermopower of YbCu4Au and YbCu4Pd | Thermoelectric power of YbMCu4 (M = Ag, Au and Pd) and YbPd2Si2

## Au-Yb
- rank 1908 | 2 samples | 1 papers | 2 compositions
- compositions: YbAu2 (1); YbAu3 (1)
- measured range: 10-269 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbAu2 I4/mmm (139) mp-1668 [hull=0.000, icsd=5, PRIMARY]; YbAu Pm-3m (221) mp-2818 [hull=0.006, icsd=3, PRIMARY]; YbAu4 I4/m (87) mp-11262 [hull=0.000, icsd=2, PRIMARY]; YbAu3 P6_3/mmc (194) mp-979985 [hull=0.012, PRIMARY]; YbAu Pnma (62) mp-1084808 [hull=0.000, icsd=1]
- papers: Thermal conductivity and thermoelectric power of Yb–Au system

## B-C-O
- rank 1909 | 2 samples | 1 papers | 2 compositions
- compositions: (B4C)85.25(TiO2)14.75 (1); (B4C)81.26(TiO2)18.74 (1)
- dopant candidates (<5% at.): Ti (2)
- measured range: 294-1073 K (5th-95th pct of 8 curves)
- papers: In Situ Preparation and Thermoelectric Properties of B4C1−x –TiB2 Composites

## B-C-Si-Zr
- rank 1910 | 2 samples | 1 papers | 2 compositions
- compositions: (SiC)0.28ZrB2 (1); (La2O3)0.007(SiC)0.28ZrB2 (1)
- dopant candidates (<5% at.): O (1), La (1)
- measured range: 295-2170 K (5th-95th pct of 2 curves)
- papers: Thermal properties of La2O3-doped ZrB2- and HfB2-based ultra-high temperature ceramics

## B-C-U
- rank 1911 | 2 samples | 1 papers | 1 compositions
- compositions: UB2C (2)
- measured range: 10-292 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UBC Cmcm (63) mp-5816 [hull=0.000, icsd=3, PRIMARY]; UB2C R-3m (166) mp-11332 [hull=0.051, icsd=2, PRIMARY]; U4B3C5 Pmm2 (25) mp-1216723 [hull=0.004, PRIMARY]
- papers: Electron correlation effects and ferromagnetic order in β-UB2C

## B-Ca-Sr
- rank 1912 | 2 samples | 2 papers | 2 compositions
- compositions: Ca0.5Sr0.5B6 (1); Ca0.5B3Sr0.5B3 (1)
- measured range: 289-1074 K (5th-95th pct of 6 curves; full span incl. outliers 289-1121 K)
- papers: High-pressure densified solid solutions of alkaline earth hexaborides (Ca/Sr, Ca/Ba, Sr/Ba) and their high-temperature thermoelectric properties | Reduction of thermal conductivity and origin of carrier in alkaline-earth hexaborides

## B-Ce-Cr
- rank 1913 | 2 samples | 1 papers | 2 compositions
- compositions: CeCrB6 (1); Y0.05Ce0.95CrB6 (1)
- dopant candidates (<5% at.): Y (1)
- measured range: 11-806 K (5th-95th pct of 6 curves; full span incl. outliers 11-943 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(CrB3)2 Immm (71) mp-2873 [hull=0.000, icsd=2, PRIMARY]; CeCrB4 Pbam (55) mp-1191927 [hull=0.003, icsd=1, PRIMARY]
- papers: Thermoelectricity and electronic properties of<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:mrow><mml:msub><mml:mi mathvariant=\"normal\">Y</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mo>−</mml:mo><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Ce</mml:mi><mml:mi>x</mml:mi></mml:msub><mml:msub><mml:mi>CrB</mml:mi><mml:mn>4</mml:mn></mml:msub></mml:mrow></mml:math>

## B-Co-Ni
- rank 1914 | 2 samples | 1 papers | 2 compositions
- compositions: Ni0.1Co0.9B (1); Ni0.5Co0.5B (1)
- measured range: 438-948 K (5th-95th pct of 2 curves)
- papers: Seebeck coefficients of iron group elements borides

## B-Co-S
- rank 1915 | 2 samples | 2 papers | 2 compositions
- compositions: Ce0.1Fe0.7Co3.3SB12 (1); Ce0.05Yb0.05Fe0.14Co3.86SB12 (1)
- dopant candidates (<5% at.): Fe (2), Ce (2), Yb (1)
- measured range: 116-470 K (5th-95th pct of 4 curves)
- papers: Properties of thermoelectric Ce0.09Fe0.67Co3.33Sb12/FeSb2Te multi-layered structures prepared by laser ablation | Thermoelectric properties of the new skutterudites (Ce-Yb)/sub y/Fe/sub 4-x/(Co/Ni)/sub x/Sb/sub 12/

## B-Cr
- rank 1916 | 2 samples | 1 papers | 1 compositions
- compositions: CrB (2)
- measured range: 293-293 K (5th-95th pct of 2 curves; full span incl. outliers 293-1222 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CrB2 P6/mmm (191) mp-374 [hull=0.070, icsd=7, PRIMARY]; CrB Cmcm (63) mp-260 [hull=0.010, icsd=7, PRIMARY]; Cr3B4 Immm (71) mp-889 [hull=0.019, icsd=6, PRIMARY]; Cr5B3 I4/mcm (140) mp-15617 [hull=0.000, icsd=5, PRIMARY]; CrB4 Pnnm (58) mp-1078278 [hull=0.000, icsd=4, PRIMARY]
- papers: Thermophysical and mechanical properties of CrB and FeB

## B-Cr-Fe
- rank 1917 | 2 samples | 1 papers | 2 compositions
- compositions: Fe74Co2.5Cr7.5B16 (1); Fe74Cr10B16 (1)
- dopant candidates (<5% at.): Co (1)
- measured range: 312-602 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cr9FeB6 I4/m (87) mp-1226337 [hull=0.007, PRIMARY]; CrFe3B2 Fmm2 (42) mp-1226213 [hull=0.049, PRIMARY]; CrFeB2 Pmc2_1 (26) mp-1226310 [hull=0.042, PRIMARY]
- papers: Electrical resistivity and thermoelectric power of Fe74Co10−x Cr x B16 metallic glasses

## B-Cr-Fe-O-Zr
- rank 1918 | 2 samples | 1 papers | 1 compositions
- compositions: (Fe57Cr15Nb4B20Si4)0.12(Y2O3)0.2(ZrO2)0.8 (2)
- dopant candidates (<5% at.): Nb (2), Si (2), Y (2)
- measured range: 374-873 K (5th-95th pct of 2 curves)
- papers: Novel Fe-Based Amorphous Composite Coating with a Unique Interfacial Layer Improving Thermal Barrier Application

## B-Cu-O
- rank 1919 | 2 samples | 2 papers | 1 compositions
- compositions: CuBO2 (2)
- measured range: 306-973 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu(BO2)2 I-42d (122) mp-4870 [hull=0.000, icsd=3, PRIMARY]; Cu2BO6 Pnma (62) mp-1196064 [hull=0.323, icsd=1, PRIMARY]; Cu3B7IO13 F-43c (219) mp-651682 [hull=0.024, icsd=1, PRIMARY]; Cu3(BO3)2 P2_1 (4) mp-1226691 [hull=0.050, PRIMARY]; Cu3B7ClO13 Pca2_1 (29) mp-1213325 [hull=0.012, PRIMARY]
- papers: High temperature thermoelectric properties of delafossite CuBO<inf>2</inf> | Cu\n                B\n                  O\n                  2\n          : A p-type transparent oxide

## B-Dy
- rank 1920 | 2 samples | 2 papers | 1 compositions
- compositions: DyB12 (2)
- measured range: 10-67 K (5th-95th pct of 2 curves; full span incl. outliers 10-1025 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DyB4 P4/mbm (127) mp-2719 [hull=0.000, icsd=3, PRIMARY]; DyB2 P6/mmm (191) mp-2057 [hull=0.000, icsd=2, PRIMARY]; DyB12 Fm-3m (225) mp-1103476 [hull=0.000, icsd=1, PRIMARY]
- papers: Transition and rare earth element dodecaborides | Thermal conductivity of metal dodecaborides with a UB12 structure

## B-F-H-O-P
- rank 1921 | 2 samples | 2 papers | 1 compositions
- compositions: PBFDO (2)
- measured range: 10-482 K (5th-95th pct of 6 curves)
- papers: A solution-processed n-type conducting polymer with ultrahigh conductivity | A Scalable Fully Printed Organic Thermoelectric Generator for Harsh Environments Enabled by a Stable n‐type Polymer

## B-Ho
- rank 1922 | 2 samples | 2 papers | 1 compositions
- compositions: HoB12 (2)
- measured range: 10-28 K (5th-95th pct of 2 curves; full span incl. outliers 10-1033 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HoB2 P6/mmm (191) mp-2267 [hull=0.000, icsd=3, PRIMARY]; HoB12 Fm-3m (225) mp-1104585 [hull=0.000, icsd=1, PRIMARY]
- papers: Transition and rare earth element dodecaborides | Thermal conductivity of metal dodecaborides with a UB12 structure

## B-K-O
- rank 1923 | 2 samples | 1 papers | 2 compositions
- compositions: (K2O)20(B2O3)80 (1); (K2O)30(B2O3)70 (1)
- measured range: 1073-1273 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): KB5O8 Pbca (61) mp-12183 [hull=0.000, icsd=2, PRIMARY]; KB5O12 Aea2 (41) mp-1180867 [hull=0.543, icsd=2, PRIMARY]; KBO2 R-3c (167) mp-3919 [hull=0.000, icsd=2, PRIMARY]; K2B4O7 P-1 (2) mp-17166 [hull=0.000, icsd=1, PRIMARY]; KB3O5 C2/c (15) mp-1196090 [hull=0.022, icsd=1, PRIMARY]
- papers: Thermal Conductivity of Molten Li2O-B2O3and K2O-B2O3Systems

## B-Li-O
- rank 1924 | 2 samples | 1 papers | 2 compositions
- compositions: (Li2O)30(B2O3)70 (1); (Li2O)20(B2O3)80 (1)
- measured range: 1123-1273 K (5th-95th pct of 2 curves; full span incl. outliers 1123-1473 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li2B4O7 I4_1cd (110) mp-4779 [hull=0.000, icsd=23, PRIMARY]; LiB3O5 Pna2_1 (33) mp-3660 [hull=0.007, icsd=7, PRIMARY]; Li6Cu(B2O5)2 P-1 (2) mp-1191302 [hull=0.013, icsd=3, PRIMARY]; LiBO2 P2_1/c (14) mp-3635 [hull=0.000, icsd=3, PRIMARY]; Li3B11O18 P2_1/c (14) mp-1020014 [hull=0.000, icsd=2, PRIMARY]
- papers: Thermal Conductivity of Molten Li2O-B2O3and K2O-B2O3Systems

## B-Mo
- rank 1925 | 2 samples | 1 papers | 2 compositions
- compositions: MoB4 (1); Mo2B5 (1)
- measured range: 300-1212 K (5th-95th pct of 2 curves; full span incl. outliers 300-1256 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): B2Mo R-3m (166) mp-2331 [hull=0.003, icsd=8, PRIMARY]; BMo2 I4/mcm (140) mp-2501 [hull=0.020, icsd=5, PRIMARY]; B5Mo2 R-3m (166) mp-7229 [hull=0.450, icsd=4, PRIMARY]; BMo I4_1/amd (141) mp-1890 [hull=0.000, icsd=3, PRIMARY]; B4Mo P6_3/mmc (194) mp-1106346 [hull=0.536, icsd=3, PRIMARY]
- papers: Some physical properties of the higher borides of molybdenum and tungsten

## B-Mo-Si
- rank 1926 | 2 samples | 1 papers | 1 compositions
- compositions: Mo5SiB2 (2)
- measured range: 12-1062 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SiB2Mo5 I4/mcm (140) mp-4984 [hull=0.000, icsd=4, PRIMARY]
- papers: Electrical and thermal properties of single crystalline Mo 5 X 3  (X=Si, B, C) and related transition metal 5-3 silicides

## B-Nb
- rank 1927 | 2 samples | 1 papers | 2 compositions
- compositions: (NbB2)87.09(SiC)12.91 (1); NbB2 (1)
- dopant candidates (<5% at.): Si (1), C (1)
- measured range: 303-573 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NbB2 P6/mmm (191) mp-450 [hull=0.005, icsd=14, PRIMARY]; NbB Cmcm (63) mp-2580 [hull=0.000, icsd=6, PRIMARY]; Nb3B2 P4/mbm (127) mp-20689 [hull=0.000, icsd=4, PRIMARY]; Nb3B4 Immm (71) mp-10255 [hull=0.000, icsd=3, PRIMARY]; Nb5B6 Cmmm (65) mp-1102394 [hull=0.002, icsd=1, PRIMARY]
- papers: Effects ofSiCandSiC-GNP additions on the mechanical properties and oxidation behavior of NbB2

## B-O-Zn
- rank 1928 | 2 samples | 1 papers | 1 compositions
- compositions: (TiB2)9.7(ZnO)90.3 (2)
- dopant candidates (<5% at.): Ti (2)
- measured range: 179-843 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zn4B6O13 I-43m (217) mp-4812 [hull=0.000, icsd=6, PRIMARY]; ZnB4O7 Pbca (61) mp-12233 [hull=0.000, icsd=2, PRIMARY]; Zn3B7ClO13 R3c (161) mp-23609 [hull=0.001, icsd=2, PRIMARY]; Zn3B7BrO13 Pca2_1 (29) mp-1179542 [hull=0.006, icsd=1, PRIMARY]; Zn4B6SeO12 I-43m (217) mp-14921 [hull=0.000, icsd=1, PRIMARY]
- papers: Preparation and thermoelectric properties of ZnO-TiB/sub 2/ composites

## B-Si
- rank 1929 | 2 samples | 1 papers | 1 compositions
- compositions: Si92B8 (2)
- measured range: 286-1069 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SiB6 Pm-3m (221) mp-7700 [hull=0.477, icsd=1, PRIMARY]; Dy2Si9B36C Cm (8) mp-1225372 [hull=0.000, PRIMARY]; Si3B P6_3/mmc (194) mp-972733 [hull=0.923, PRIMARY]; Lu2Si9B36C Cm (8) mp-1222448 [hull=0.000, PRIMARY]; SiB P6_3mc (186) mp-978495 [hull=0.413, PRIMARY]
- papers: Thermoelectric properties of Si/SiB3 sub-micro composite prepared by melt-spinning technique

## B-W
- rank 1930 | 2 samples | 1 papers | 2 compositions
- compositions: WB4 (1); W2B5 (1)
- measured range: 364-1191 K (5th-95th pct of 2 curves; full span incl. outliers 364-1267 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BW I4_1/amd (141) mp-7832 [hull=0.000, icsd=5, PRIMARY]; BW2 I4/mcm (140) mp-1113 [hull=0.000, icsd=5, PRIMARY]; B4W P6_3/mmc (194) mp-29651 [hull=0.599, icsd=3, PRIMARY]; B2W P6/mmm (191) mp-10144 [hull=0.256, icsd=1, PRIMARY]; B5W2 R-3m (166) mp-8079 [hull=0.547, icsd=1, PRIMARY]
- papers: Some physical properties of the higher borides of molybdenum and tungsten

## Ba-Bi-Fe-O-Ti
- rank 1931 | 2 samples | 1 papers | 2 compositions
- compositions: Ba0.4Bi0.6Ti0.4Fe0.6O3 (1); Ba0.6Bi0.4Ti0.6Fe0.4O3 (1)
- measured range: 463-543 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba3Ti3Fe3(BiO9)2 P3m1 (156) mp-1228452 [hull=0.122, PRIMARY]; BaTiFe3(BiO4)3 R3 (146) mp-1227513 [hull=0.029, PRIMARY]
- papers: Design, structural evolution, optical, electrical and dielectric properties of perovskite ceramics Ba1-xBixTi1-xFexO3 (0 ≤ x ≤ 0.8)

## Ba-Bi-Mn-O-Ti
- rank 1932 | 2 samples | 1 papers | 2 compositions
- compositions: Ba0.7Bi0.3Ti0.7Mn0.3O3 (1); Ba0.6Bi0.4Ti0.6Mn0.4O3 (1)
- measured range: 293-383 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaTiMnBiO6 F-43m (216) mp-1227378 [hull=0.166, PRIMARY]
- papers: Synthesis, structural refinement and physical properties of novel perovskite ceramics Ba1-xBixTi1-xMnxO3 (x = 0.3 and 0.4)

## Ba-Ca-Cu-O-Y
- rank 1933 | 2 samples | 1 papers | 2 compositions
- compositions: YBa0.8Ca1.2Cu3O7 (1); YBaCaCu3O7 (1)
- measured range: 63-302 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba10CaY4(Cu3O7)5 P-1 (2) mp-1228878 [hull=0.038, PRIMARY]; Ba8CaY3(CuO2)12 C2/m (12) mp-1228323 [hull=0.040, PRIMARY]
- papers: Metal-insulator transition in YBa2−xCaxCu3O7−δ system

## Ba-Ca-Fe-Nb-O
- rank 1934 | 2 samples | 1 papers | 2 compositions
- compositions: BaCa0.33Nb0.42Fe0.25O3 (1); BaCa0.33Nb0.34Fe0.33O3 (1)
- measured range: 573-1173 K (5th-95th pct of 2 curves)
- papers: Role of Dopants in Fine-Tuning the Electrical and Catalytic Properties of Barium Niobate Perovskites Towards High-Temperature Electrolyzer Application

## Ba-Ca-Nb-O
- rank 1935 | 2 samples | 1 papers | 2 compositions
- compositions: BaCa0.33Nb0.5Fe0.17O3 (1); BaCa0.33Nb0.57Y0.1O3 (1)
- dopant candidates (<5% at.): Fe (1), Y (1)
- measured range: 573-1174 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2CaNbO6 Fm-3m (225) mp-1214679 [hull=0.044, PRIMARY]; Ba3CaNb2O9 P-3m1 (164) mp-1214569 [hull=0.000, PRIMARY]; Ba5Ca2Nb3O15 I4/m (87) mp-1228343 [hull=0.021, PRIMARY]; Ba8Ca3Nb5O24 I4/mmm (139) mp-1228256 [hull=0.022, PRIMARY]
- papers: Role of Dopants in Fine-Tuning the Electrical and Catalytic Properties of Barium Niobate Perovskites Towards High-Temperature Electrolyzer Application

## Ba-Co-Dy-O
- rank 1936 | 2 samples | 2 papers | 2 compositions
- compositions: BaDyCo4O7 (1); DyBaCo4O7 (1)
- measured range: 300-997 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaDy2CoO5 Pnma (62) mp-19364 [hull=0.000, icsd=2, PRIMARY]; BaDyCo4O7 P6_3mc (186) mp-18804 [hull=0.023, icsd=2, PRIMARY]; Ba2Dy2Co4O11 Pmmm (47) mp-1214700 [hull=0.108, PRIMARY]; BaDy2CoO5 Immm (71) mp-19164 [hull=0.016, icsd=1]
- papers: Structural and thermoelectric properties of BaRCo4O7 (R = Dy, Ho, Er, Tm, Yb, and Lu) | Electronic transport and thermoelectric properties of RBaCo4O7 (R=Dy, Ho, Y, Er)

## Ba-Co-Er-O
- rank 1937 | 2 samples | 2 papers | 2 compositions
- compositions: BaErCo4O7 (1); ErBaCo4O7 (1)
- measured range: 297-995 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaEr2CoO5 Pnma (62) mp-25677 [hull=0.000, icsd=2, PRIMARY]; BaEr2CoO5 Immm (71) mp-18746 [hull=0.020, icsd=1]
- papers: Structural and thermoelectric properties of BaRCo4O7 (R = Dy, Ho, Er, Tm, Yb, and Lu) | Electronic transport and thermoelectric properties of RBaCo4O7 (R=Dy, Ho, Y, Er)

## Ba-Co-Fe-Nd-O
- rank 1938 | 2 samples | 2 papers | 2 compositions
- compositions: NdBaFeCoO5 (1); NdBaCoFeO5 (1)
- measured range: 300-1068 K (5th-95th pct of 3 curves; full span incl. outliers 300-1122 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2Nd2Fe(CoO4)3 Amm2 (38) mp-1228516 [hull=0.080, PRIMARY]; Ba2Nd2Fe3CoO12 P-4m2 (115) mp-1228604 [hull=0.090, PRIMARY]; BaNdFeCoO6 P4mm (99) mp-1227838 [hull=0.067, PRIMARY]
- papers: Synthesis and properties of LnBaFeCoO5 + δ (Ln = Nd, Sm, Gd) | Improved electrochemical performance and thermal expansion compatibility of LnBaCoFeO5+–Sm0.2Ce0.8O1.9 (Ln Pr and Nd) composite cathodes for IT-SOFCs

## Ba-Co-Fe-O-Sm
- rank 1939 | 2 samples | 2 papers | 2 compositions
- compositions: SmBaFeCoO5 (1); SmBa0.75Ca0.25CoFeO5 (1)
- dopant candidates (<5% at.): Ca (1)
- measured range: 146-1023 K (5th-95th pct of 3 curves; full span incl. outliers 146-1073 K)
- papers: Synthesis and properties of LnBaFeCoO5 + δ (Ln = Nd, Sm, Gd) | Ca and Fe co-doped SmBaCo2O5 +  layered perovskite as an efficient cathode for intermediate-temperature solid oxide fuel cells

## Ba-Co-Ga-O
- rank 1940 | 2 samples | 1 papers | 2 compositions
- compositions: Y0.5Ca0.5BaCo3.2Ga0.8O7 (1); Y0.5Ca0.4In0.1BaCo3.2Ga0.8O7 (1)
- dopant candidates (<5% at.): Y (2), Ca (2), In (1)
- measured range: 572-1172 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba6Ga2Co11O26 P-3m1 (164) mp-642047 [hull=0.076, PRIMARY]
- papers: Phase stability and electrochemical performance of Y0.5Ca0.5−xInxBaCo3.2Ga0.8O7+δ (x = 0 and 0.1) as cathodes for intermediate temperature solid oxide fuel cells

## Ba-Co-La-O-Ti
- rank 1941 | 2 samples | 1 papers | 2 compositions
- compositions: La0.25Ba0.749Sb0.001Co0.5Ti0.5O3 (1); La0.35Ba0.6494Sb0.0006Co0.7Ti0.3O3 (1)
- dopant candidates (<5% at.): Sb (2)
- measured range: 296-513 K (5th-95th pct of 2 curves)
- papers: Resistivity Control by Solid-State Reaction of Perovskite-Type Oxides

## Ba-Co-Nb-O
- rank 1942 | 2 samples | 1 papers | 2 compositions
- compositions: La0.2Ba0.8Co0.7Nb0.3O3 (1); La0.2Ba0.8Co0.6Nb0.4O3 (1)
- dopant candidates (<5% at.): La (2)
- measured range: 299-1177 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba3Nb2CoO9 P-3m1 (164) mp-600864 [hull=0.000, icsd=1, PRIMARY]; Ba2NbCoO6 Fm-3m (225) mp-1228382 [hull=0.066, PRIMARY]; Ba6Nb9CoO30 Cmm2 (35) mp-1228527 [hull=0.036, PRIMARY]; Ba8Nb6CoO24 P-3m1 (164) mp-640790 [hull=0.000, PRIMARY]
- papers: Effect of Nb5+ content on the high temperature properties of the mixed conductors system La1−xBaxCo1−yNbyO3−δ with 0.6 ≤ x ≤ 1.0 and 0 ≤ y ≤ 0.4

## Ba-Co-O-Sb
- rank 1943 | 2 samples | 1 papers | 1 compositions
- compositions: Ba3CoSb2O9 (2)
- measured range: 11-99 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba3CoSb2O9 P6_3/mmc (194) mp-19337 [hull=0.000, icsd=2, PRIMARY]
- papers: Thermal Conductivity in the Triangular-Lattice Antiferromagnet Ba3CoSb2O9

## Ba-Cu-Ga-Ge
- rank 1944 | 2 samples | 1 papers | 2 compositions
- compositions: Ba8.12Cu3.05Ga7.19Ge35.64 (1); Ba8.11Cu4.12Ga4.06Ge37.71 (1)
- measured range: 300-300 K (5th-95th pct of 4 curves)
- papers: Effect of Cu Substitution on Thermoelectric Properties of Ge Clathrates

## Ba-Cu-Ge-Zn
- rank 1945 | 2 samples | 1 papers | 2 compositions
- compositions: Ba8Cu3Zn3Ga1Ge39 (1); Ba8Cu3Zn3Ge40 (1)
- dopant candidates (<5% at.): Ga (1)
- measured range: 323-474 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba4Zn2CuGe20 Ama2 (40) mp-1229043 [hull=0.000, PRIMARY]
- papers: Theoretical and Experimental Study on Thermoelectric Properties of Ba8TM x Ga y Ge46–x–y (TM = Zn, Cu, Ag) Type I Clathrates

## Ba-Cu-K-Se
- rank 1946 | 2 samples | 1 papers | 2 compositions
- compositions: Ba0.7K0.3Cu2Se2 (1); Ba0.65K0.35Cu2Se2 (1)
- measured range: 301-836 K (5th-95th pct of 8 curves)
- papers: Enhancement of the thermoelectric properties of BaCu2Se2 by potassium doping

## Ba-Cu-Li-O-Y
- rank 1947 | 2 samples | 1 papers | 1 compositions
- compositions: Li1.625YBa2Cu3O7 (2)
- measured range: 77-297 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba14LiY7(Cu10O21)2 P1 (1) mp-774711 [hull=0.008, PRIMARY]; Ba4LiY2Cu5O14 Cm (8) mp-757073 [hull=0.022, PRIMARY]
- papers: Influence of lithium on the electronic structure of YBa2Cu3O7−δ

## Ba-Cu-O-Si
- rank 1948 | 2 samples | 1 papers | 1 compositions
- compositions: BaCuSi4O10 (2)
- measured range: 11-295 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaCu(Si2O5)2 P4/ncc (130) mp-6127 [hull=0.014, icsd=4, PRIMARY]; BaCu2Si2O7 Pnma (62) mp-22407 [hull=0.042, icsd=3, PRIMARY]; BaCu(SiO3)2 I4_1cd (110) mp-1197716 [hull=0.017, icsd=2, PRIMARY]; Ba2CuSi2O7 P-42_1m (113) mp-11613 [hull=0.040, icsd=1, PRIMARY]; BaCu(SiO3)2 P4_2/nmc (137) mp-1182662 [hull=0.027, icsd=1]
- papers: Heat capacity, thermal expansion and heat transport in the Han Blue (BaCuSi4O10): Observation of structural phase transitions

## Ba-Cu-O-Sm-Sr
- rank 1949 | 2 samples | 1 papers | 2 compositions
- compositions: SmBaSrCu3O7 (1); SmBa1.2Sr0.8Cu3O7 (1)
- measured range: 81-290 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba3SrSm2(CuO2)6 I4mm (107) mp-1228212 [hull=0.015, PRIMARY]; Ba8Sr2Sm5(Cu3O7)5 Pmm2 (25) mp-1229001 [hull=0.024, PRIMARY]; BaSrSm(CuO2)3 P4mm (99) mp-1227431 [hull=0.026, PRIMARY]; BaSrSmCu3O7 Pmm2 (25) mp-1227474 [hull=0.028, PRIMARY]
- papers: The thermoelectric power of the system SmBa2-xSrxCu3O7-δ

## Ba-Cu-O-Sr
- rank 1950 | 2 samples | 1 papers | 2 compositions
- compositions: Y0.4Pr0.6Ba1.2Sr0.8Cu3O7 (1); Y0.4Pr0.6BaSrCu3O7 (1)
- dopant candidates (<5% at.): Pr (2), Y (2)
- measured range: 10-275 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba3Sr(Cu2O5)2 P1 (1) mp-1076189 [hull=0.095, PRIMARY]; Ba3Sr(CuO3)4 P4/mmm (123) mp-1099602 [hull=0.069, PRIMARY]; Ba4Sr4CoCu7O24 Cm (8) mp-1099676 [hull=0.056, PRIMARY]; Ba6Sr2CoCu7O20 P1 (1) mp-1076296 [hull=0.098, PRIMARY]; Ba6Sr2CoCu7O24 Amm2 (38) mp-1076247 [hull=0.071, PRIMARY]
- papers: Induction of superconductivity in Y0.4Pr0.6Ba2−xSrxCu3O7 system with increasing Sr substitution
