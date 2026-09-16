# Host systems -- chunk 003 of 73

Ranks 101-150 by sample count. These 50 host systems cover 3118 samples (5.99% of the TE set); cumulative through this chunk: 63.79%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Ba-Co-O
- rank 101 | 83 samples | 28 papers | 39 compositions
- compositions: Ba2Co9O14 (11); BaCo0.7Fe0.2Nb0.1O3 (7); BaCo0.7Fe0.18Nb0.12O3 (5); BaCo0.7Fe0.22Nb0.08O3 (5); Ba0.8Sr0.2Co0.8Fe0.2O3 (4); Ba1.9La0.1Co9O14 (3)
- dopant candidates (<5% at.): Fe (41), Nb (35), La (13), Bi (8), In (6), Y (6), Sr (5), Zr (4), Ta (4), Na (3), K (2), Cl (1)
- seed hypothesis (confirm): perovskite
- measured range: 25-1223 K (5th-95th pct of 96 curves; full span incl. outliers 11-1342 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaCoO3 P6_3/mmc (194) mp-18965 [hull=0.000, icsd=4, PRIMARY]; Ba5Co5O14 P-3m1 (164) mp-24896 [hull=0.007, icsd=2, PRIMARY]; Ba12(CoO3)11 C2/c (15) mp-1195315 [hull=0.005, icsd=1, PRIMARY]; Ba2CoO4 Pnma (62) mp-19602 [hull=0.006, icsd=1, PRIMARY]; BaCoO2 P3_121 (152) mp-19086 [hull=0.000, icsd=1, PRIMARY]
- papers: High-temperature thermoelectric properties of layered BaxCoO2 | Overview of Electrons and Orbitals in a Nearly One-Dimensional Co3+/Co4+System | Magnetic and Transport Properties of Ba2Co9O14and Ba1.9A0.1Co9O14(A=La or Na)

## Ba-Ge-Zn
- rank 102 | 81 samples | 6 papers | 52 compositions
- compositions: Ba8Ni0.8Zn6.4Ge38.8 (6); Ba8Zn7.62Ge38.38 (5); Ba8Zn7.33Ge38.67 (4); Ba8Zn8Ge38 (4); Ba8Zn7.78Ge38.22 (4); Ba8Ni2.4Zn3.6Ge40.0 (4)
- dopant candidates (<5% at.): Ni (36), Sn (30), K (1)
- measured range: 12-977 K (5th-95th pct of 212 curves; full span incl. outliers 10-1081 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaZnGe P6_3/mmc (194) mp-11818 [hull=0.000, icsd=1, PRIMARY]; Ba(ZnGe)2 I4/mmm (139) mp-1206924 [hull=0.000, PRIMARY]; Ba16Zn9Ge80Pd3 Pm (6) mp-1229324 [hull=0.000, PRIMARY]; Ba4Zn11Ge12 Pm-3n (223) mp-1214758 [hull=0.150, PRIMARY]
- papers: Influence of Sn-substitution on the thermoelectric properties of the clathrate type-I, Ba8ZnxGe46−x−ySny | Tuning of band gap and thermoelectric properties of type-I clathrate Ba8NixZnyGe46−x−y−zSnz | Crystal structure and thermoelectric properties of KxBa8−xZnyGe46−y clathrates

## B-C
- rank 103 | 77 samples | 26 papers | 44 compositions
- compositions: B4C (16); B13C2 (5); ErB22C2N (4); B9C (4); Y1.08B22.3C2N (3); B0.1C (2)
- dopant candidates (<5% at.): N (17), Y (16), Er (5), O (3), Ti (3), Hf (1)
- seed hypothesis (confirm): boron_carbide
- measured range: 31-1474 K (5th-95th pct of 143 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): B13C2 R-3m (166) mp-576 [hull=0.000, icsd=4, PRIMARY]; B4C R-3m (166) mp-696746 [hull=0.037, icsd=3, PRIMARY]; BC5 P3m1 (156) mp-1018649 [hull=0.268, icsd=2, PRIMARY]; BC7 P-4m2 (115) mp-1078935 [hull=0.207, icsd=1, PRIMARY]; B9C I4/mmm (139) mp-1182537 [hull=2.582, icsd=1, PRIMARY]
- papers: Manufacture and Testing of Thermoelectric Modules Consisting of BxC and TiOxElements | Configurational, electronic entropies and the thermoelectric properties of nanocarbon ensembles | Thermoelectric power generation using doped MWCNTs

## Ba-Co-Gd-O
- rank 104 | 77 samples | 11 papers | 43 compositions
- compositions: GdBaCo2O5.5 (23); GdBaCo2O5 (6); GdBaCo2O5.165 (2); GdBaCo2O5.3 (2); BaGd1.8Ca0.2CoO5 (2); BaGd2CoO5 (2)
- dopant candidates (<5% at.): Ca (8), La (4), Sr (4), Ce (4), Fe (2)
- measured range: 12-1176 K (5th-95th pct of 108 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaGdCo2O5 Pmmm (47) mp-1079551 [hull=0.069, icsd=3, PRIMARY]; Ba2Gd2Co4O11 Pmmm (47) mp-1189405 [hull=0.111, icsd=1, PRIMARY]; Ba4CaGd3(Co4O11)2 Fmm2 (42) mp-1229195 [hull=0.094, PRIMARY]; BaGd(CoO3)2 P4/mmm (123) mp-1214665 [hull=0.197, PRIMARY]; BaGdCo2O5 P4/mmm (123) mp-1080062 [hull=0.170, icsd=2]
- papers: A novel method to control oxygen stoichiometry and thermoelectric properties in (RE)BaCo2O5+δ | Thermoelectric properties of GdBaCo2−x Fe x O5+δ ceramics | Origin of the large thermoelectric power in oxygen-variableRBaCo2O5+x(R=Gd,Nd)

## Fe-O-Sr
- rank 105 | 77 samples | 27 papers | 44 compositions
- compositions: SrFeO3 (13); Sr3Fe2O7 (4); Sr2.85Sm0.15Fe2O7 (4); SrFe0.9Mo0.1O3 (4); SrFe0.9Ti0.1O3 (3); Sr2.9Sm0.1Fe2O7 (3)
- dopant candidates (<5% at.): Nb (10), Co (9), W (8), Sm (7), Mo (7), Cu (4), La (3), Ca (3), Ti (3), Bi (2), Ta (2), Hf (1), K (1)
- seed hypothesis (confirm): perovskite
- measured range: 21-1213 K (5th-95th pct of 86 curves; full span incl. outliers 12-1274 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2Fe2O5 Ima2 (46) mp-616640 [hull=0.000, icsd=15, PRIMARY]; Sr4Fe4O11 Cmmm (65) mp-24955 [hull=0.005, icsd=12, PRIMARY]; Sr2FeO4 I4/mmm (139) mp-19102 [hull=0.000, icsd=4, PRIMARY]; SrFeO2 P4/mmm (123) mp-24964 [hull=0.011, icsd=4, PRIMARY]; Sr8Fe8O23 I4/mmm (139) mp-19004 [hull=0.000, icsd=4, PRIMARY]
- papers: Structural and Thermoelectric Properties of Rare-Earth-Substituted Sr<sub>3</sub>Fe<sub>2</sub>O<sub>7</sub> | Structural and electrical properties of selected La1−xSrxCo0.2Fe0.8O3 and La0.6Sr0.4Co0.2Fe0.6Ni0.2O3 perovskite type oxides | Synthesis, Crystal Chemistry, and Electrical Properties of the Intergrowth Oxides Sr4−xCaxFe6−yCoyO13+δ

## Al-Ba-Si
- rank 106 | 76 samples | 21 papers | 31 compositions
- compositions: Ba8Al16Si30 (18); Ba8Al15Si31 (16); Ba8Al14Si31 (5); Ba7SrAl16Si30 (4); Ba7.7B0.1887Al14.8Si31.0 (3); Ba7.8B0.1699Al14.6Si31.2 (3)
- dopant candidates (<5% at.): B (8), Ga (6), Sr (5), Eu (4), P (3)
- seed hypothesis (confirm): clathrate_i
- measured range: 24-1250 K (5th-95th pct of 194 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba(AlSi)2 Pnma (62) mp-5506 [hull=0.000, icsd=3, PRIMARY]; Ba3(AlSi)2 Immm (71) mp-9578 [hull=0.000, icsd=1, PRIMARY]; BaAlSi P-6m2 (187) mp-13149 [hull=0.000, icsd=1, PRIMARY]; Ba(AlSi)2 I4/mmm (139) mp-12863 [hull=0.007, icsd=1]
- papers: Thermoelectric Properties and Microstructure of Ba8Al14Si31and EuBa7Al13Si33 | Thermoelectric Properties of Ba8Al16Si30-Based Clathrate Prepared by Combining Arc Melting and Spark Plasma Sintering Methods | Synthesis, Structure, and High-Temperature Thermoelectric Properties of Boron-Doped Ba8Al14Si31Clathrate I Phases

## Cu-Ga-Te
- rank 107 | 76 samples | 21 papers | 38 compositions
- compositions: CuGaTe2 (34); Cu2Ga4Te7 (3); CuGa3Te5 (2); Cu3Ga5Te9 (2); CuGa0.99Zn0.01Te2 (2); CuGa0.99Gd0.01Te2 (1)
- dopant candidates (<5% at.): Zn (6), Fe (5), Gd (3), Ag (3), Sb (3), Se (3), C (1), Mn (1)
- seed hypothesis (confirm): chalcopyrite
- measured range: 17-968 K (5th-95th pct of 272 curves)
- [ref 1] TEDesignLab / ICSD: GaCuTe2 I-42d (122) mp-3839 [hull=0.000, icsd=11, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ga5CuTe8 P-42m (111) mp-1212671 [hull=0.004, PRIMARY]; GaCuTe2 R3m (160) mp-1224825 [hull=0.051]; GaCuTe2 R-3m (166) mp-1224815 [hull=0.191]; GaCuTe2 I4_1/amd (141) mp-676248 [hull=0.205]; GaCuTe2 P4/mmm (123) mp-1224787 [hull=0.211]
- papers: Chalcopyrite CuGaTe2: A High-Efficiency Bulk Thermoelectric Material | High-Performance Pseudocubic Thermoelectric Materials from Non-cubic Chalcopyrite Compounds | High-temperature thermoelectric properties of Cu2Ga4Te7 with defect zinc-blende structure

## Ba-Cu-Si
- rank 108 | 75 samples | 11 papers | 41 compositions
- compositions: Ba8Cu4.8Si41.2 (13); Ba8Cu4.8Si42(SiC)1.3 (5); Ba8Cu4.8Si42(SiC)0.65 (5); Ba8Cu4.8Si42(SiC)2 (5); Ba8Cu4.8Si42 (5); Ba8Cu6Si40 (4)
- dopant candidates (<5% at.): C (15), Eu (7), Ag (3)
- seed hypothesis (confirm): clathrate_i
- measured range: 67-977 K (5th-95th pct of 217 curves; full span incl. outliers 16-1471 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba8CuSi16 Pm (6) mp-1192107 [hull=0.026, icsd=1, PRIMARY]; BaCu9Si4 I4/mcm (140) mp-11143 [hull=0.000, icsd=1, PRIMARY]; Ba4Cu3Si20 Pm-3n (223) mp-1214552 [hull=0.000, PRIMARY]; Ba4Cu2Si21 Ama2 (40) mp-1228302 [hull=0.000, PRIMARY]; Ba8CuSi16 P1 (1) mp-1182738 [hull=0.068, icsd=1]
- papers: Influence of PCA on thermoelectric properties and hardness of nanostructured Ba–Cu–Si clathrates | Effect of Europium Substitution on Thermoelectric Properties of Noble-Metal Silicon Clathrates with Ba<sub>8&minus;</sub><i><sub>x</sub></i>Eu<i><sub>x</sub></i>Cu<i><sub>y</sub></i>Si<sub>46&minus;</sub><i><sub>y</sub></i> Nominal Compositions | Thermoelectric properties of Ba-Cu-Si clathrates

## Ag-Ge-Sb-Te
- rank 109 | 74 samples | 23 papers | 32 compositions
- compositions: (GeTe)85(AgSbTe2)15 (17); (AgSbTe2)15(GeTe)85 (9); (GeTe)85 (AgSbTe2 )15 (4); (GeTe)0.85(AgSbTe2)0.15 (3); Ge0.53Ag0.13Sb0.27Te (3); Ge0.61Ag0.11Sb0.22Te (3)
- dopant candidates (<5% at.): Dy (4), Se (3), Yb (1), Ce (1)
- seed hypothesis (confirm): gst_homologous
- measured range: 20-775 K (5th-95th pct of 268 curves; full span incl. outliers 10-872 K)
  !! MEASUREMENT CROSSES A TRANSITION: gst_homologous -> rocksalt at ~420 K (Amorphous -> metastable cubic, ~420 K; cubic -> stable layered above ~500 K.)
     Record each phase with its own temperature range, not a single prototype.
- papers: Application of the compatibility factor to the design of segmented and cascaded thermoelectric generators | Ag9TlTe5: A high-performance thermoelectric bulk material with extremely low thermal conductivity | Yb14MnSb11:  New High Efficiency Thermoelectric Material for Power Generation

## Ni-Sn-Ti-Zr
- rank 110 | 74 samples | 20 papers | 31 compositions
- compositions: Ti0.5Zr0.5NiSn (20); Ti0.5Zr0.5NiSn0.98Sb0.02 (5); Zr0.7Ti0.2Nb0.1NiSn (4); Ti0.5Zr0.5NiSn0.99Sb0.01 (4); (Zr0.5Ti0.5NiSn0.994Sb0.006)98.24(HfO2)1.76 (4); Zr0.5Ti0.5NiSn (3)
- dopant candidates (<5% at.): Sb (24), Nb (4), O (4), Hf (4), Ge (1)
- solid-solution axis: Ti/(Ti+Zr) spans 0.20-0.80 (median 0.50) over 31 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 291-1035 K (5th-95th pct of 283 curves; full span incl. outliers 19-1073 K)
- papers: Ordered Structures and Thermoelectric Properties of MNiSn (M = Ti, Zr, Hf)-Based Half-Heusler Compounds Affected by Close Relationship with Heusler Compounds | Thermoelectric properties of Ge doped n-type TixZr1−xNiSn0.975Ge0.025 half-Heusler alloys | Compositions and thermoelectric properties of XNiSn (X = Ti, Zr, Hf) half-Heusler alloys

## Co-Nb-Sn
- rank 111 | 73 samples | 17 papers | 39 compositions
- compositions: NbCoSn (14); NbCoSn0.9Sb0.1 (5); NbCoSn0.98Sb0.02 (3); NbCoSn0.85Sb0.15 (3); NbCoSn0.96Sb0.04 (2); Nb0.99Ti0.01CoSn0.92Sb0.08 (2)
- dopant candidates (<5% at.): Sb (32), Ti (12), Sc (7), Pt (7), Hf (3), Mo (1)
- seed hypothesis (confirm): half_heusler
- measured range: 292-1027 K (5th-95th pct of 334 curves; full span incl. outliers 287-1138 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NbCo2Sn Fm-3m (225) mp-4583 [hull=0.127, icsd=5, PRIMARY]; NbCoSn F-43m (216) mp-1094088 [hull=0.000, icsd=1, PRIMARY]; NbCo2Sn Pmma (51) mp-1205387 [hull=0.117, icsd=1]; NbCo2Sn P4/mmm (123) mp-1220370 [hull=0.205]
- papers: Thermoelectric properties of directionally solidified half-Heusler compound NbCoSn alloys | Thermoelectric Properties of Doped Half-Heuslers NbCoSn1-xSbxand Nb0.99Ti0.01CoSn1-xSbx | Ordered Structures and Thermoelectric Properties of MNiSn (M = Ti, Zr, Hf)-Based Half-Heusler Compounds Affected by Close Relationship with Heusler Compounds

## Mn-Sn-Te
- rank 112 | 73 samples | 9 papers | 37 compositions
- compositions: Sn0.89Mn0.14Te(Cu2Te)0.05 (6); Sn0.85Mn0.15Te (5); (SnTe)0.83(MnTe)0.15Bi0.02 (5); Sn0.9Mn0.14Te(Cu2Te)0.05 (4); Sn0.86Mn0.14Te(Cu2Te)0.05 (4); Sn0.93Mn0.14Te(Cu2Te)0.05 (3)
- dopant candidates (<5% at.): Cu (45), Bi (6), Ge (6), In (4), I (1)
- measured range: 297-927 K (5th-95th pct of 204 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn2SnTe4 Pnma (62) mp-1192988 [hull=0.044, icsd=1, PRIMARY]; MnSnTe2 R-3m (166) mp-1221681 [hull=0.432, PRIMARY]
- papers: Synergistically optimized electrical and thermal transport properties of SnTe via alloying high-solubility MnTe | Phases and thermoelectric properties in stoichiometric Sn 1−x Mn x Te and non-stoichiometric Sn 1−y Mn 1.1y Te alloys | Promoting SnTe as an Eco-Friendly Solution for p-PbTe Thermoelectric via Band Convergence and Interstitial Defects

## Al-Cu-Fe
- rank 113 | 72 samples | 27 papers | 33 compositions
- compositions: Al62Cu25.5Fe12.5 (14); Al63Cu25Fe12 (9); Al70Cu20Fe10 (6); Al62.5Cu25Fe12.5_IQC (5); Al62.5Cu25Fe12.5 (5); Al63Cu24.5Fe12.5_IQC (4)
- dopant candidates (<5% at.): Co (3), Pt (3), Au (2)
- seed hypothesis (confirm): quasicrystal_approximant
- measured range: 10-972 K (5th-95th pct of 93 curves; full span incl. outliers 10-1756 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al7FeCu2 P4/mnc (128) mp-4689 [hull=0.000, icsd=2, PRIMARY]; Al2FeCu Immm (71) mp-1096521 [hull=2.360, PRIMARY]; Al37(Fe6Cu)2 Cm (8) mp-1228719 [hull=0.000, PRIMARY]; Al39Fe7Cu24 Pm-3 (200) mp-31403 [hull=0.214, PRIMARY]
- papers: Thermoelectric properties ofAl82.6−xRe17.4Six(7⩽x⩽12)1∕1-cubic approximants | Thermal and thermoelectric properties of icosahedral Al62Cu25.5Fe12.5 quasicrystal | Modeling the electronic transport properties of Al–Cu–Fe phases

## Cu-Se-Sn-Zn
- rank 114 | 72 samples | 17 papers | 46 compositions
- compositions: Cu2ZnSnSe4 (20); Cu2ZnSn0.90In0.10Se4 (4); Cu2.05ZnSn0.95Se4 (3); Cu2.1Zn0.9SnSe4 (3); Cu2.075ZnSn0.925Se4 (1); Cu2.15ZnSn0.85Se4 (1)
- dopant candidates (<5% at.): In (9), Te (9), Pb (9), Ga (7), Cd (4)
- seed hypothesis (confirm): stannite_kesterite
- measured range: 297-802 K (5th-95th pct of 307 curves; full span incl. outliers 11-992 K)
- [ref 1] TEDesignLab / ICSD: ZnCu2SnSe4 (121)
- [ref 2] MP, ranked by ICSD evidence: ZnCu2SnSe4 I-4 (82) mp-1078918 [hull=0.000, icsd=1, PRIMARY]; Zn4Cu11(SnSe4)5 I-4 (82) mp-1215879 [hull=0.005, PRIMARY]; Zn4FeCu10(SnSe4)5 C2 (5) mp-1216277 [hull=0.021, PRIMARY]
- papers: Synthesis and Characterization of Nanostructured Stannite Cu2ZnSnSe4and Ag2ZnSnSe4for Thermoelectric Applications | Large-Scale Colloidal Synthesis of Non-Stoichiometric Cu2ZnSnSe4Nanocrystals for Thermoelectric Applications | Thermoelectric properties of chalcogenide based Cu2+xZnSn1−xSe4

## Mo-O
- rank 115 | 72 samples | 25 papers | 21 compositions
- compositions: Mo4O11 (19); Li0.9Mo6O17 (12); Mo8O23 (9); MoO2 (4); Rb0.15K0.15MoO3 (4); K0.05MoO2 (3)
- dopant candidates (<5% at.): Li (12), K (10), Rb (4), La (2), Ce (2), Sm (2), Nd (2), Na (2), Pr (1), Bi (1), Tl (1), S (1)
- seed hypothesis (confirm): reo3_wo3
- measured range: 10-1155 K (5th-95th pct of 105 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MoO2 P4_2/mnm (136) mp-715476 [hull=0.012, icsd=7, PRIMARY]; Mo4O11 Pna2_1 (33) mp-622101 [hull=0.018, icsd=6, PRIMARY]; Mo8O23 P2/c (13) mp-19540 [hull=0.009, icsd=4, PRIMARY]; MoO3 P2_1/c (14) mp-18856 [hull=0.000, icsd=3, PRIMARY]; Mo3O10 Aea2 (41) mp-1180281 [hull=0.186, icsd=2, PRIMARY]
- papers: Thermoelectric properties of molybdenum oxides LnMo8O14 (Ln=La, Ce, Pr, Nd and Sm) | High thermoelectric performance of reduced lanthanide molybdenum oxides densified by spark plasma sintering | Thermoelectric power of RE2Mo2O7 pyrochlores

## Ce-Fe-Sb
- rank 116 | 71 samples | 31 papers | 41 compositions
- compositions: CeFe4Sb12 (25); CeFe3.5Co0.5Sb12 (3); Ce0.85Fe4Sb12 (2); CeFe3.9Co0.1Sb12 (2); Ce0.9Fe3.5Ni0.5Sb12 (2); CeFe3.9Ga0.1Sb12 (2)
- dopant candidates (<5% at.): Co (15), Ni (8), Ga (5), Zn (4), Ge (4), Mn (3), In (2), Te (2), Yb (1)
- seed hypothesis (confirm): skutterudite, filled_skutterudite  <-- MIXED, split per composition
- measured range: 12-854 K (5th-95th pct of 277 curves; full span incl. outliers 10-989 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeFeSb2 P4/nmm (129) mp-1079507 [hull=0.002, icsd=2, PRIMARY]; Ce(FeSb3)4 Im-3 (204) mp-1181682 [hull=0.000, icsd=1, PRIMARY]
- papers: Application of the compatibility factor to the design of segmented and cascaded thermoelectric generators | Thermoelectric properties of metal/molecule/metal junction for different lengths of polythiophene | Thermo-elektrische Verbindungen. Strom aus Abwärme

## Ba-Bi-Co-O
- rank 117 | 70 samples | 20 papers | 34 compositions
- compositions: Bi2Ba2Co2O8 (13); Bi2Ba2O4(CoO2)2 (8); (Bi0.9Ba1.4O2)CoO2 (4); (Bi2Ba2O4)0.5CoO2 (4); Bi2Ba1.8Co2.2O8 (3); (Bi0.95Ba1.5O2)CoO2 (2)
- dopant candidates (<5% at.): Pb (18), Na (5), C (4), Ag (3), Cu (2), Rh (1), La (1), Sr (1)
- seed hypothesis (confirm): misfit_cobaltite
- measured range: 11-951 K (5th-95th pct of 177 curves)
- papers: Growth rate effect on microstructure and thermoelectric properties of melt grown Bi2Ba2Co2Oxtextured ceramics | Thermoelectric properties of bismuth based cobalt-rhodium oxides with hexagonal (Co,Rh)O2 layers | High-temperature Thermoelectric Properties of Cu-substituted Bi2Ba2Co2-xCuxOy Oxides

## Ge-Mg-Si
- rank 118 | 69 samples | 16 papers | 44 compositions
- compositions: Mg2Si0.5Ge0.5 (10); Mg2Si0.6Ge0.4 (6); Mg2Si0.7Ge0.3 (4); Mg2Si0.3Ge0.7 (3); (Mg2Si)0.7(Ge)0.3 (2); (Mg2Si)0.3(Ge)0.7 (2)
- dopant candidates (<5% at.): Bi (17), Sb (14), La (3), C (3), Ga (2), Ag (1)
- seed hypothesis (confirm): antifluorite
- solid-solution axis: Ge/(Ge+Si) spans 0.09-0.80 (median 0.41) over 44 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 298-923 K (5th-95th pct of 233 curves; full span incl. outliers 293-1172 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg4SiGe R-3m (166) mp-1222125 [hull=0.005, PRIMARY, AMBIGUOUS]; Mg6SiGe2 Immm (71) mp-1222090 [hull=0.004, PRIMARY]; Mg4SiGe P4/mmm (123) mp-1222108 [hull=0.007]; Mg4SiGe F-43m (216) mp-1222117 [hull=0.492]
- papers: Thermoelectric properties and electronic structure of p-type Mg2Si and Mg2Si0.6Ge0.4 compounds doped with Ga | Local structure and thermoelectric properties of Mg 2 Si 0.977− x Ge x Bi 0.023  (0.1  ⩽  x  ⩽  0.4) | Thermoelectric Performance of Sb- and La-Doped Mg2Si0.5Ge0.5

## Ba-O-Ti
- rank 119 | 66 samples | 17 papers | 51 compositions
- compositions: BaTiO3 (6); Ba0.8Eu0.2TiO3 (5); (BaTiO3)9(SrRuO3)3(BaTiO3)10 (4); La0.002Ba0.97Bi0.015Na0.015TiO3 (2); Ba0.9La0.1TiO3 (2); (Gd2O3)0.0020(BaTiO3)0.9980 (2)
- dopant candidates (<5% at.): La (17), Bi (14), Gd (10), Na (10), Sr (6), Eu (6), Cr (5), Nb (5), Ru (5), Sm (4), Lu (4), Mn (4), Ho (3), Ni (3), Zn (3), Sb (2), Nd (1), Li (1), K (1), Fe (1), Co (1)
- seed hypothesis (confirm): perovskite
- measured range: 10-1120 K (5th-95th pct of 79 curves; full span incl. outliers 10-1173 K)
- [ref 1] TEDesignLab / ICSD: BaTiO3 Pm-3m (221) mp-2998 [hull=0.015, icsd=94, PRIMARY]; BaTi2O5 C2/m (12) mp-3943 [hull=0.022, icsd=4, PRIMARY]; BaTi4O9 Pmmn (59) mp-3175 [hull=0.009, icsd=3, PRIMARY]; Ba2TiO4 P2_1/c (14) mp-3397 [hull=0.000, icsd=2, PRIMARY]; BaTiO3 P4mm (99) mp-5986 [hull=0.003, icsd=47]
- [ref 2] MP, ranked by ICSD evidence: Ba2Ti6O13 C2/m (12) mp-7733 [hull=0.000, icsd=2, PRIMARY]; Ba4Ti13O30 Cmce (64) mp-29298 [hull=0.000, icsd=1, PRIMARY]; Ba2TiO4 P4/mmm (123) mp-36194 [hull=0.160]
- papers: PTCR and Thermoelectric Properties of Isovalent Co-Doped BaTiO3Nanoceramics | Thermoelectric properties of doped BaTiO3–SrTiO3 solid solution | Thermoelectric Properties of Lanthanum-Doped Europium Titanate

## Co-Sb-Zr
- rank 120 | 65 samples | 24 papers | 37 compositions
- compositions: ZrCoSb (19); ZrCoSb0.9Sn0.1 (7); ZrCoSb0.85Sn0.15 (2); ZrFe0.1Co0.9Sb (2); ZrCo(Sb0.9Sn0.1) (2); ZrCo0.96Ni0.04Sb (2)
- dopant candidates (<5% at.): Sn (28), Te (4), Ta (4), Ni (3), V (3), Fe (2), Pt (2), Hf (1), Si (1), Nb (1)
- seed hypothesis (confirm): half_heusler
- measured range: 19-993 K (5th-95th pct of 268 curves; full span incl. outliers 10-1175 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zr5CoSb3 P6_3/mcm (193) mp-1207404 [hull=0.000, icsd=1, PRIMARY]; ZrCoSb F-43m (216) mp-22377 [hull=0.612, icsd=1, PRIMARY]; Zr6CoSb2 P-62m (189) mp-1205892 [hull=0.000, PRIMARY]
- papers: High-Thermoelectric Figure of Merit Realized in p-Type Half-Heusler Compounds: ZrCoSnxSb1-x | Peculiarities of thermoelectric half-Heusler phase formation in Zr–Co–Sb ternary system | Microstructure and thermoelectric properties in Fe-doped ZrCoSb half-Heusler compounds

## Cu-Fe-O
- rank 121 | 65 samples | 20 papers | 38 compositions
- compositions: CuFeO2 (12); CuFe0.99Ni0.01O2 (8); CuFe0.98Ni0.02O2 (3); CuFe2O4 (3); CuFe0.95Ni0.05O2 (2); CuFe0.96Ni0.04O2 (2)
- dopant candidates (<5% at.): Ni (21), Sn (5), Li (5), Pt (4), Cr (4), Pd (3), Co (3), Zn (2), Gd (1), Mg (1), Ti (1), Mn (1), Cd (1)
- seed hypothesis (confirm): delafossite
- measured range: 296-1159 K (5th-95th pct of 128 curves; full span incl. outliers 16-1174 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeCuO2 R-3m (166) mp-796603 [hull=0.000, icsd=9, PRIMARY]; Fe13Cu5O24 P-1 (2) mp-763652 [hull=0.098, PRIMARY]; Fe2CuO4 Fd-3m (227) mp-770107 [hull=0.065, PRIMARY, AMBIGUOUS]; Fe5CuO8 F-43m (216) mp-33300 [hull=0.067, PRIMARY]; Fe9Cu3O16 P-1 (2) mp-705842 [hull=0.102, PRIMARY]
- papers: Thermoelectric power in Gd3+-substituted Cu-Cd ferrites | Synthesis and Thermoelectric Properties of Cu0.95Pt0.05Fe0.97Sn0.03O2Delafossite-Oxide | Thermoelectric Properties ofAn+2Con+1O3n+3(A=Ca, Sr, Ba,n=1–5)

## Ba-Fe-O-Sr
- rank 122 | 62 samples | 24 papers | 37 compositions
- compositions: Ba0.5Sr0.5FeO3 (9); Ba0.5Sr0.5Co0.2Fe0.8O3 (9); Ba0.5Sr0.5Fe0.9Cu0.1O3 (4); Ba0.5Sr0.5Fe0.9Nb0.1O3 (3); Ba0.5Sr0.5Fe0.8Cu0.2O3 (3); Ba0.5Sr0.5Zn0.2Fe0.8O3 (2)
- dopant candidates (<5% at.): Co (17), Cu (13), Mg (8), Mn (7), Zn (5), La (5), Ti (3), Ce (3), Nb (3), Al (3), Zr (1), Ni (1), Mo (1)
- measured range: 299-1223 K (5th-95th pct of 62 curves; full span incl. outliers 292-1273 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaSr(FeO2)4 P-31m (162) mp-24938 [hull=0.012, icsd=3, PRIMARY]; Ba4Sr(FeO3)5 P4/mmm (123) mp-1228328 [hull=0.003, PRIMARY]; BaSr(FeO3)2 P4/mmm (123) mp-1227735 [hull=0.003, PRIMARY]; BaSr4(FeO2)5 P4/mmm (123) mp-1227731 [hull=0.016, PRIMARY, AMBIGUOUS]; BaSr4(FeO3)5 Cmmm (65) mp-1227727 [hull=0.005, PRIMARY, AMBIGUOUS]
- papers: Cobalt-free Ba0.5Sr0.5Fe0.8Cu0.1Ti0.1O3−δ as a bi-functional electrode material for solid oxide fuel cells | X-ray photoelectron spectra, conductivity, and oxygen permeation characteristics of (Ba0.5Sr0.5)(Fe1-xCex)O3-δ (x = 0–1.0) perovskites | XRD, XANES, and Electrical Conductivity Analysis of La- and Zr-Doped Ba0.5Sr0.5Fe0.9Cu0.1O3-δ Suitable for IT-SOFC Cathodes

## Ce-Cu
- rank 123 | 62 samples | 15 papers | 10 compositions
- compositions: CeCu6 (32); CeCu5.9Au0.1 (10); CeCu2 (7); Ce26Cu74 (6); CeCu5.8Au0.2 (2); Ce0.8La0.2Cu6 (1)
- dopant candidates (<5% at.): Au (12), La (4)
- seed hypothesis (confirm): cecu6
- measured range: 10-301 K (5th-95th pct of 90 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeCu5 P6/mmm (191) mp-761 [hull=0.026, icsd=10, PRIMARY]; CeCu6 Pnma (62) mp-21708 [hull=0.000, icsd=5, PRIMARY]; CeCu2 Imma (74) mp-2801 [hull=0.000, icsd=3, PRIMARY]; CeCu Pnma (62) mp-636198 [hull=0.074, icsd=2, PRIMARY]; Ce3Cu I4/mmm (139) mp-1183872 [hull=0.160, PRIMARY]
- papers: Thermoelectric properties of nanocomposite heavy fermion CeCu6 | Anomalous thermopower in heavy-fermion compounds CeB6, CeAl3, and CeCu6 − x Au x | Thermodynamic and transport properties of CeCu6

## Fe-Sn-Ti
- rank 124 | 62 samples | 13 papers | 34 compositions
- compositions: Fe2TiSn (17); TiFe2Sn (6); Fe2TiSn0.95Ge0.05 (3); Fe2TiSn0.95Si0.05 (3); Fe1.9Ti1.1Sn (2); Fe2.05Ti0.95Sn (2)
- dopant candidates (<5% at.): Mn (6), Sb (4), Si (3), Ge (3), V (2), In (2), Hf (1), Y (1)
- seed hypothesis (confirm): full_heusler
- measured range: 11-898 K (5th-95th pct of 196 curves; full span incl. outliers 10-976 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiFe2Sn Fm-3m (225) mp-19963 [hull=0.000, icsd=4, PRIMARY]; TiFeSn F-43m (216) mp-22589 [hull=0.714, icsd=1, PRIMARY]; Ti5FeSn3 P6_3/mcm (193) mp-1208517 [hull=0.019, PRIMARY]
- papers: Thermal and transport properties of the Heusler-type compounds Fe2−xTi1+xSn | Magnetic and transport properties in Heusler-type Fe2TiSn compound | Thermoelectric Properties of Heusler Fe2TiSn Alloys

## Ag-Te
- rank 125 | 61 samples | 19 papers | 24 compositions
- compositions: Ag2Te (25); Ag1.995Pb0.005Te (3); Ag1.98Pb0.02Te (3); Ag1.96Pb0.04Te (3); Ag1.99Pb0.01Te (3); Ag2Sb0.015Te0.985 (2)
- dopant candidates (<5% at.): Pb (19), Sb (10), Br (1), Bi (1), S (1)
- seed hypothesis (confirm): ag2se_naumannite, bcc_superionic  <-- MIXED, split per composition
- measured range: 298-776 K (5th-95th pct of 216 curves; full span incl. outliers 290-970 K)
  !! MEASUREMENT CROSSES A TRANSITION: ag2se_naumannite -> bcc_superionic at ~406 K (P212121 -> bcc superionic, ~406 K. Ag2Te transforms near ~418 K.)
     Record each phase with its own temperature range, not a single prototype.
- [ref 1] TEDesignLab / ICSD: AgTe (62) [PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ag2Te P2_1/c (14) mp-1592 [hull=0.000, icsd=3, PRIMARY]; Ag7Te4 P6/mmm (191) mp-28228 [hull=0.237, icsd=1, PRIMARY]; AgTe3 Im-3m (229) mp-28246 [hull=0.011, icsd=1, PRIMARY]; Ag2Te Pc (7) mp-684798 [hull=0.034]; Ag2Te Cmce (64) mp-32811 [hull=0.037]
- papers: Ternary eutectic growth of nanostructured thermoelectric Ag-Pb-Te materials | Enhanced thermoelectric performance in the very low thermal conductivity Ag2Se0.5Te0.5 | Thermoelectric properties of α- and β-Ag2Te

## Nd-Ni-O
- rank 126 | 61 samples | 19 papers | 17 compositions
- compositions: NdNiO3 (37); Nd0.8Sr0.2NiO3 (5); Nd2Ni0.9Co0.1O4 (2); Nd2Ni0.9Cu0.1O4 (2); Nd0.9Sr0.1NiO3 (2); Nd2NiO4 (2)
- dopant candidates (<5% at.): Sr (7), Cu (3), La (3), Co (2), Eu (1), Al (1), Mn (1), Fe (1)
- seed hypothesis (confirm): perovskite
- measured range: 11-1073 K (5th-95th pct of 58 curves; full span incl. outliers 10-1122 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NdNiO3 Pnma (62) mp-25591 [hull=0.000, icsd=14, PRIMARY]; Nd2NiO4 Cmce (64) mp-18737 [hull=0.062, icsd=4, PRIMARY]; Nd4Ni3O8 I4/mmm (139) mp-18738 [hull=0.242, icsd=3, PRIMARY]; Nd(NiO2)2 Cmce (64) mp-1210181 [hull=0.254, PRIMARY]; Nd2NiO4 I4/mmm (139) mp-19191 [hull=0.104, icsd=4]
- papers: Magnetothermopower in Nd1−xEuxNiO3 compounds | A d-Band Electron Correlated Thermoelectric Thermistor Established in Metastable Perovskite Family of Rare-Earth Nickelates | Tunable resistivity exponents in the metallic phase of epitaxial nickelates

## Ce-Pd
- rank 127 | 60 samples | 13 papers | 39 compositions
- compositions: CePd3 (13); CePd3B0.05 (3); CePd3Al0.05 (2); CePd3Ge0.02 (2); CePd3Ga0.02 (2); CePd3Mg0.02 (2)
- dopant candidates (<5% at.): Al (11), B (10), Sn (8), Ge (4), Ga (4), Mg (4), Rh (4), Sc (3), Ag (3), Si (2), Be (2), Ca (1), Y (1), In (1)
- seed hypothesis (confirm): cu3au_l12
- measured range: 10-353 K (5th-95th pct of 129 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CePd3 Pm-3m (221) mp-906843 [hull=0.000, icsd=21, PRIMARY]; CePd5 P6/mmm (191) mp-22217 [hull=0.087, icsd=2, PRIMARY]; Ce7Pd3 P6_3mc (186) mp-1188284 [hull=0.049, icsd=2, PRIMARY]; CePd Cmcm (63) mp-1018086 [hull=0.000, icsd=2, PRIMARY]; Ce3Pd4 R-3 (148) mp-1103851 [hull=0.000, icsd=1, PRIMARY]
- papers: Enhanced thermoelectric properties of CePd3−xPtx | Relationship between structure, magnetism, and thermoelectricity in CePd3Mx alloys | Thermoelectric Properties of Ce1−x Sc x Pd3

## Co-Si
- rank 128 | 60 samples | 16 papers | 24 compositions
- compositions: CoSi (32); CoSi0.95Ge0.05 (2); CoSi0.995B0.005 (2); CoSi0.98Ge0.02 (2); (Si0.99B0.01)95Co5 (2); CoSi0.98B0.02 (2)
- dopant candidates (<5% at.): B (9), Ge (6), Ni (4), Al (2), O (2)
- seed hypothesis (confirm): b20_fesi
- measured range: 11-1032 K (5th-95th pct of 191 curves; full span incl. outliers 10-1311 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CoSi P2_13 (198) mp-7577 [hull=0.000, icsd=6, PRIMARY]; Co2Si Pnma (62) mp-19905 [hull=0.000, icsd=4, PRIMARY]; CoSi2 Fm-3m (225) mp-2379 [hull=0.003, icsd=4, PRIMARY]; Co3Si P6_3/mmc (194) mp-1079393 [hull=0.077, icsd=1, PRIMARY]; Co2Si3 P-4c2 (116) mp-1105498 [hull=0.197, icsd=1, PRIMARY]
- papers: High thermoelectric power factor in alloys based on CoSi | Effects of Ge and B substitution on thermoelectric properties of CoSi | Effects of Al doping on the thermoelectric performance of CoSi single crystal

## Bi-Fe-O
- rank 129 | 58 samples | 12 papers | 30 compositions
- compositions: BiFeO3 (11); La0.05Bi0.95FeO3 (5); La0.1Bi0.9FeO3 (5); La0.15Bi0.85FeO3 (5); Bi0.91Nd0.09Fe0.91Mn0.09O3 (3); Bi0.91Ho0.09FeO3 (2)
- dopant candidates (<5% at.): La (22), Mn (13), Nd (11), Co (4), Ho (4), Sr (3), Ba (2), Ca (2), Sb (1), Sm (1), Eu (1), Ti (1)
- seed hypothesis (confirm): perovskite
- measured range: 17-1092 K (5th-95th pct of 67 curves; full span incl. outliers 10-1210 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeBiO3 R3c (161) mp-24932 [hull=0.020, icsd=76, PRIMARY]; Fe4Bi2O9 Pnma (62) mp-1196085 [hull=0.036, icsd=2, PRIMARY]; Fe(Bi5O8)5 P23 (195) mp-765035 [hull=0.027, PRIMARY]; DyFe5Bi4O15 P1 (1) mp-1226261 [hull=0.035, PRIMARY]; Fe5Bi4O13F P4_22_12 (94) mp-1225422 [hull=0.017, PRIMARY]
- papers: Thermoelectric properties of Co-doped BiFeO3 and Bi24CoO37^|^ndash;BiFeO3 compound systems | Percolation Conduction in Hybrid Thermoelectric Material Consisting of Bi0.88Sb0.12 and Barium Ferrite Particles | Phonon Scattering by Paramagnetic Ions of Europium and Samarium in Bismuth Ferrite

## Bi-Sn-Te
- rank 130 | 57 samples | 9 papers | 47 compositions
- compositions: SnBi2Te4 (5); SnBi4Te7 (4); (Bi2Te3)47.5(SnTe)52.5 (2); (Bi2Te3)50(SnTe)50 (2); Bi1.6Sn0.4Te2.94Se0.06 (2); SnBi6Te10 (1)
- dopant candidates (<5% at.): In (8), Ga (8), Tl (3), Pb (3), Se (2)
- seed hypothesis (confirm): homologous_tetradymite
- measured range: 28-695 K (5th-95th pct of 186 curves; full span incl. outliers 11-783 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SnBi4Te7 P-3m1 (164) mp-1101917 [hull=0.190, icsd=1, PRIMARY]; Sn(BiTe2)2 R-3m (166) mp-38605 [hull=0.000, PRIMARY]; Sn3BiTe4 R-3m (166) mp-1218987 [hull=0.119, PRIMARY]; SnBi3Te4 Cm (8) mp-1218955 [hull=0.210, PRIMARY]; Sn(BiTe2)2 Cm (8) mp-677596 [hull=0.025]
- papers: Solvothermal preparation and thermoelectric properties of ternary Sn–Bi–Te alloy | Thermoelectric Properties of Stoichiometric Compounds in the (SnTe)x(Bi2Te3)ySystem | Effects of Cation Site Substitutions on the Thermoelectric Performance of Layered SnBi2Te4utilizing the Triel Elements Ga, In, and Tl

## Fe-La-O
- rank 131 | 57 samples | 22 papers | 33 compositions
- compositions: La0.8Sr0.2FeO3 (10); La0.8Sr0.2Co0.2Fe0.8O3 (5); La0.8Ca0.2Fe0.8Ni0.2O3 (4); La0.9Sr0.1FeO3 (3); LaFeO3 (3); La0.8Sr0.2Fe0.9Nb0.1O3 (2)
- dopant candidates (<5% at.): Sr (34), Co (12), Ni (8), Ca (8), Al (4), Cu (3), Nb (2), Ta (2), Ba (2), Bi (2), Zn (1)
- measured range: 216-1340 K (5th-95th pct of 83 curves; full span incl. outliers 170-1375 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaFeO3 R-3c (167) mp-1078634 [hull=0.012, icsd=11, PRIMARY]; La3FeO6 Cmc2_1 (36) mp-1180667 [hull=0.000, icsd=1, PRIMARY]; LaFe12O19 P6_3/mmc (194) mp-642250 [hull=0.064, icsd=1, PRIMARY]; La4FeO8 Cmmm (65) mp-770617 [hull=0.078, PRIMARY]; La3Fe5O12 Ia-3d (230) mp-1212003 [hull=0.013, PRIMARY]
- papers: Influence of Sr substitution on thermoelectric properties of La1−xSrxFeO3 ceramics | Electrical, Thermoelectric, and Structural Properties of La(M[sub x]Fe[sub 1−x])O[sub 3] (M=Mn, Ni, Cu) | P-Type Thermoelectric Properties of Pr<sub>1&minus;<i>x</i></sub>Sr<sub><i>x</i></sub>MnO<sub>3</sub> (0.1≦<i>x</i>≦0.3) and La<sub>1&minus;<i>x</i></sub>Sr<sub><i>x</i></sub>FeO<sub>3</sub> (0.1≦<i>x</i>≦0.3)

## Cu
- rank 132 | 55 samples | 13 papers | 30 compositions
- compositions: Cu (16); Cu99.91Cr0.09 (3); CuFe0.000115 (3); Be2.75Ni1.9Cu95.35 (3); Cu99.7Fe0.3 (3); Cu99.4Fe0.6 (2)
- dopant candidates (<5% at.): Fe (11), Si (4), Mn (4), Pd (4), Pt (4), Ba (4), Y (4), Cr (3), Be (3), Ni (3), Bi (2), Sr (2), Ca (2)
- seed hypothesis (confirm): solid_solution_alloy
- measured range: 10-1112 K (5th-95th pct of 80 curves; full span incl. outliers 10-1311 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu Fm-3m (225) mp-30 [hull=0.000, icsd=18, PRIMARY]; Cu I4/mmm (139) mp-1010136 [hull=0.035, icsd=2]; Cu Im-3m (229) mp-998890 [hull=0.035, icsd=1]; Cu Cmcm (63) mp-1059259 [hull=0.150, icsd=1]; Cu P2/m (10) mp-1056079 [hull=1.942, icsd=1]
- papers: Thermoelectric Power and Electrical Resistivity of Dilute Alloys of Silicon in Copper, Nickel, and Iron | Thermoelectric Power and Electrical Resistivity of Dilute Alloys of Mn, Pd, and Pt in Cu, Ag, and Au | Effects of Transition Metal Solutes on the Thermoelectric Power of Copper and Gold

## Fe-Nb-Sb-Ti
- rank 133 | 55 samples | 15 papers | 28 compositions
- compositions: Fe1.05Nb0.75Ti0.25Sb (10); Nb0.8Ti0.2FeSb (7); FeNb0.8Ti0.2Sb (4); Nb0.8Ti0.2Fe1.02Sb (4); Nb0.75Ti0.25FeSb (3); Nb0.6Ti0.4FeSb0.95Sn0.05 (3)
- dopant candidates (<5% at.): Bi (4), Sn (3), Ta (2), V (2)
- seed hypothesis (confirm): half_heusler
- measured range: 293-1161 K (5th-95th pct of 230 curves; full span incl. outliers 10-1202 K)
- papers: Band engineering of high performance p-type FeNbSb based half-Heusler thermoelectric materials for figure of merit zT > 1 | NbFeSb-based p-type half-Heuslers for power generation applications | Achieving high power factor and output power density in p-type half-Heuslers Nb1-xTixFeSb

## Ge-Mg-Sn
- rank 134 | 55 samples | 8 papers | 52 compositions
- compositions: Mg2Ge0.4Sn0.6 (2); Mg1.98Li0.02Ge0.4Sn0.6 (2); Mg2Sn0.75Ge0.25 (2); Mg2Ge0.2Sn0.8 (1); Mg1.995Ag0.005Ge0.4Sn0.6 (1); Mg1.96Ag0.04Ge0.4Sn0.6 (1)
- dopant candidates (<5% at.): Li (15), Si (8), Sb (6), Bi (5), Ag (4), P (3), Y (3), Na (3), Ga (3), La (1)
- seed hypothesis (confirm): antifluorite
- solid-solution axis: Ge/(Ge+Sn) spans 0.19-0.80 (median 0.26) over 52 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 296-773 K (5th-95th pct of 263 curves; full span incl. outliers 27-776 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg4SnGe F-43m (216) mp-1222113 [hull=0.308, PRIMARY]; Mg6Sn2Ge P-3m1 (164) mp-1222093 [hull=0.026, PRIMARY]
- papers: Improving p-type thermoelectric performance of Mg2(Ge,Sn) compounds via solid solution and Ag doping | Thermoelectric properties of materials near the band crossing line in Mg 2 Sn–Mg 2 Ge–Mg 2 Si system | Thermoelectric performance of Li doped, p-type Mg 2 (Ge,Sn) and comparison with Mg 2 (Si,Sn)

## Si-Sr
- rank 135 | 55 samples | 9 papers | 25 compositions
- compositions: SrSi2 (15); Sr0.9Ca0.1Si2 (4); Sr0.85Ca0.15Si2 (3); Sr0.92Ca0.08Si2 (3); Sr0.93Ba0.07Si2 (3); Sr0.9Ba0.1Si2 (2)
- dopant candidates (<5% at.): Ca (17), Ba (10), Y (5), Al (4), Ge (4)
- seed hypothesis (confirm): srsi2_chiral
- measured range: 10-717 K (5th-95th pct of 159 curves; full span incl. outliers 10-1162 K)
- [ref 1] TEDesignLab / ICSD: Sr2Si Pnma (62) mp-1106 [hull=0.000, icsd=4, PRIMARY]; Sr5Si3 I4/mcm (140) mp-746 [hull=0.000, icsd=4, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: SrSi2 I4_1/amd (141) mp-1727 [hull=0.000, icsd=5, PRIMARY, AMBIGUOUS]; SrSi Cmcm (63) mp-2661 [hull=0.000, icsd=4, PRIMARY]; SrSi6 Cmcm (63) mp-1009 [hull=0.073, icsd=2, PRIMARY]; Sr2Si3 Imm2 (44) mp-1218710 [hull=0.094, PRIMARY]; SrSi2 P4_332 (212) mp-496 [hull=0.003, icsd=5]
- papers: Thermoelectric properties of BaSi2, SrSi2, and LaSi | Chemical pressure effect on thermoelectric properties of Ca and Ba substituted SrSi2 alloys | Investigation of Al substitution on the thermoelectric properties of SrSi2

## Ba-Cu-Ge-Si
- rank 136 | 54 samples | 9 papers | 26 compositions
- compositions: Ba8Cu4.5Si6Ge35.5 (17); Ba8Cu5Si6Ge34.4Sn0.6 (5); Ba8Cu6Si16Ge24 (3); Ba8Cu5Si6Ge34.2Sn0.8 (3); Ba8.0Cu4.7Ge35.2Si6.2 (2); Ba8Cu5Si6Ge34.52Sn0.48 (2)
- dopant candidates (<5% at.): Sn (12)
- seed hypothesis (confirm): clathrate_i
- solid-solution axis: Ge/(Ge+Si) spans 0.15-0.93 (median 0.68) over 26 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 291-875 K (5th-95th pct of 176 curves; full span incl. outliers 10-926 K)
- papers: Structural and Thermoelectric Properties of Ba8Cu x Si23-x Ge23 (4.5 ≤ x ≤ 7) | Structural and thermoelectric properties of Ba8Cu5SixGe41−xclathrates | Thermoelectric properties of meltspun Ba8Cu5(Si,Ge,Sn)41 clathrates

## Bi-Ge-Te
- rank 137 | 53 samples | 12 papers | 24 compositions
- compositions: GeBi2Te4 (19); (GeTe) 0.937(Bi2Se0.2Te2.8)0.063 (9); GeBi4Te7 (4); GeBi3.6Sb0.4Te7 (1); Ge0.90Bi0.10Te (1); Cu0.001Ge0.92Bi4Te7 (1)
- dopant candidates (<5% at.): Se (9), Cu (3), Fe (3), Sb (2), In (1)
- seed hypothesis (confirm): homologous_tetradymite
- measured range: 11-772 K (5th-95th pct of 125 curves; full span incl. outliers 10-850 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ge(BiTe2)2 R-3m (166) mp-27948 [hull=0.005, icsd=2, PRIMARY]; GeBi4Te7 P-3m1 (164) mp-29644 [hull=0.004, icsd=1, PRIMARY]; Ge2Bi2Te5 P-3m1 (164) mp-1206551 [hull=0.141, PRIMARY]; Ge2Bi2Te5 R3m (160) mp-1224417 [hull=0.157]
- papers: Thermoelectric efficiency of (1 − x)(GeTe) x(Bi2Se0.2Te2.8) and implementation into highly performing thermoelectric power generators | Single-crystal growth and thermoelectric properties of Ge(Bi,Sb)4Te7 | Reduction of thermal conductivity through nanostructuring enhances the thermoelectric figure of merit in Ge1−xBixTe

## Co-Li-O
- rank 138 | 53 samples | 10 papers | 41 compositions
- compositions: Li0.9CoO2 (5); Li0.75CoO2 (3); Li0.98CoO2 (3); LiCoO2 (3); Li0.60CoO2 (2); Li1.1Co0.85Ni0.15O2 (2)
- dopant candidates (<5% at.): Mg (8), Ni (7), Ca (1), Na (1)
- seed hypothesis (confirm): alpha_nafeo2_layered
- measured range: 11-1174 K (5th-95th pct of 102 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiCoO2 R-3m (166) mp-24850 [hull=0.000, icsd=25, PRIMARY]; Li6CoO4 P4_2/nmc (137) mp-18925 [hull=0.000, icsd=1, PRIMARY]; Li8CoO6 P6_3cm (185) mp-31531 [hull=0.000, icsd=1, PRIMARY]; Li(CoO2)3 C2/m (12) mp-763697 [hull=0.045, PRIMARY]; Li(CoO2)2 P2_1 (4) mp-774082 [hull=0.000, PRIMARY]
- papers: Magnetic and thermoelectric properties of layered LixNayCoO2 | Impact of lithium composition on the thermoelectric properties of the layered cobalt oxide system LixCoO2 | The thermodynamic and thermoelectric properties of LixTiS2 and LixCoO2

## Fe-O-Pr-Sr
- rank 139 | 52 samples | 16 papers | 29 compositions
- compositions: Pr0.6Sr0.4FeO3 (6); Pr0.5Sr0.5FeO3 (5); Pr0.7Sr0.3FeO3 (4); Pr0.4Sr0.6FeO3 (4); Pr0.3Sr0.7FeO3 (4); Pr0.6Sr0.4Fe0.8Ni0.2O3 (2)
- dopant candidates (<5% at.): Co (12), Cu (7), Ni (6), Mo (6), Nb (5), W (3), Nd (1), Ba (1), Ca (1), La (1)
- seed hypothesis (confirm): perovskite
- measured range: 166-1174 K (5th-95th pct of 50 curves; full span incl. outliers 86-1238 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2Pr(FeO3)3 C2/m (12) mp-1218794 [hull=0.000, PRIMARY]; SrPr(FeO3)2 Pmn2_1 (31) mp-1218069 [hull=0.000, PRIMARY]; SrPr3(FeO3)4 Pm (6) mp-1218104 [hull=0.000, PRIMARY]
- papers: High-Temperature Thermoelectric Properties of Pr<sub>1−</sub><i><sub>x</sub></i>Sr<i><sub>x</sub></i>FeO<sub>3</sub> (0.1 ≤ <i>x</i> ≤ 0.7) | Mo-doped Pr 0.6 Sr 0.4 Fe 0.8 Ni 0.2 O 3-δ as potential electrodes for intermediate-temperature symmetrical solid oxide fuel cells | Characterization of Pr<sub>0.5</sub>A<sub>0.5</sub>Fe<sub>0.9</sub>W<sub>0.1</sub>O<sub>3−<i>δ</i></sub> (A = Ca, Sr and Ba) as symmetric electrodes for solid oxide fuel cells

## Fe-Se
- rank 140 | 52 samples | 7 papers | 4 compositions
- compositions: FeSe (47); Fe0.89Se (3); FeSe2 (1); Fe1.98Y0.02Se2 (1)
- dopant candidates (<5% at.): Y (1)
- seed hypothesis (confirm): fese_pbo
- measured range: 11-554 K (5th-95th pct of 101 curves)
- [ref 1] TEDesignLab / ICSD: FeSe P6_3/mmc (194) mp-1065506 [hull=0.195, icsd=36]; FeSe Pnma (62) mp-1078538 [hull=0.194, icsd=19]
- [ref 2] MP, ranked by ICSD evidence: FeSe P4/nmm (129) mp-20311 [hull=0.000, icsd=56, PRIMARY]; FeSe2 Pnnm (58) mp-760 [hull=0.000, icsd=7, PRIMARY]; Fe3Se4 C2/m (12) mp-2780 [hull=0.081, icsd=7, PRIMARY]; Fe3Se Pm-3m (221) mp-1184256 [hull=0.538, PRIMARY]; Fe9Se8 P4mm (99) mp-1106121 [hull=0.066, PRIMARY]
- papers: Effect of Vacancies on Magnetism, Electrical Transport, and Thermoelectric Performance of Marcasite FeSe2−δ(δ = 0.05) | The magnetic and thermoelectric properties of NiAs-type Fe0.89Se | Giant thermoelectric power factor in ultrathin FeSe superconductor

## Ca-Mn-O-Pr
- rank 141 | 51 samples | 13 papers | 22 compositions
- compositions: Pr0.625Ca0.375MnO3 (5); Pr0.5Ca0.5MnO3 (5); Pr0.67Ca0.33MnO3 (4); Pr0.6Ca0.4MnO3 (4); Pr0.575Ca0.425MnO3 (4); Pr0.55Ca0.45MnO3 (4)
- dopant candidates (<5% at.): La (9), Pb (2), Y (2), Sr (1), Ba (1), Co (1)
- seed hypothesis (confirm): perovskite
- measured range: 11-1273 K (5th-95th pct of 58 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca6Pr6Mn11CrO36 P1 (1) mp-706248 [hull=0.000, PRIMARY]; CaPr2Mn3O9 P1 (1) mp-1147781 [hull=0.303, PRIMARY]; CaPrMn2O6 Pmn2_1 (31) mp-40630 [hull=0.002, PRIMARY]
- papers: High-temperature thermoelectric properties of Ca1−xPrxMnO3−δ (0⩽x<1) | Ferro-antiferromagnetic coupling and unusual transport properties of ferro-antiferromagnetic (100−x) La0.7Pb0.3MnO3+xPr0.63Ca0.37MnO3 (x=0–85wt%) composites | Non-adiabatic small-polaron hopping conduction in Pr0.65Ca0.35−xSrxMnO3 perovskites above the metal–insulator transition temperature

## S-Sn
- rank 142 | 51 samples | 11 papers | 24 compositions
- compositions: SnS (13); Sn0.98Na0.02S (5); SnS2 (4); Sn0.995Na0.005S (3); Sn0.97Na0.03S (3); SnS0.91Se0.09 (2)
- dopant candidates (<5% at.): Na (14), Ag (10), Se (4), Br (4)
- seed hypothesis (confirm): layered_ges, cmcm_snse_ht  <-- MIXED, split per composition
- measured range: 298-885 K (5th-95th pct of 214 curves; full span incl. outliers 166-997 K)
  !! MEASUREMENT CROSSES A TRANSITION: layered_ges -> cmcm_snse_ht at ~800 K (Pnma -> Cmcm, ~800 K for SnSe and ~880 K for SnS; the high-ZT regime.)
     Record each phase with its own temperature range, not a single prototype.
- [ref 1] TEDesignLab / ICSD: SnS2 P-3m1 (164) mp-1170 [hull=0.000, icsd=25, PRIMARY]; SnS Pnma (62) mp-2231 [hull=0.000, icsd=19, PRIMARY]; Sn2S3 Pnma (62) mp-1509 [hull=0.005, icsd=6, PRIMARY]; SnS Fm-3m (225) mp-1876 [hull=0.045, icsd=2]; SnS Cmcm (63) mp-1379 [hull=0.063, icsd=2]
- [ref 2] MP, ranked by ICSD evidence: Sn3S7 C2/c (15) mp-1202007 [hull=0.256, icsd=1, PRIMARY, AMBIGUOUS]; Sn3S Fm-3m (225) mp-1187038 [hull=0.329, PRIMARY]; SnS Aem2 (39) mp-8781 [hull=0.048, icsd=2]; SnS P-1 (2) mp-1064497 [hull=0.052, icsd=1]; SnS2 Fd-3m (227) mp-1095397 [hull=0.011, icsd=1]
- papers: Thermoelectric Properties of Sn-S Bulk Materials Prepared by Mechanical Alloying and Spark Plasma Sintering | Thermoelectrics with earth abundant elements: low thermal conductivity and high thermopower in doped SnS | Thermoelectric performance of SnS and SnS–SnSe solid solution

## As-Cd
- rank 143 | 50 samples | 3 papers | 2 compositions
- compositions: Cd3As2 (49); Cd3(P0.1As0.8)2 (1)
- dopant candidates (<5% at.): P (1)
- seed hypothesis (confirm): cd3as2
- measured range: 11-500 K (5th-95th pct of 238 curves)
- [ref 1] TEDesignLab / ICSD: CdAs2 I4_122 (98) mp-471 [hull=0.000, icsd=3, PRIMARY]; CdAs Pbca (61) mp-7373 [hull=0.015, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Cd3As2 P4_2/nmc (137) mp-1372 [hull=0.000, icsd=4, PRIMARY]; Cd3As I4/mmm (139) mp-1183587 [hull=0.166, PRIMARY]; CdAs3 P6_3/mmc (194) mp-1183659 [hull=0.437, PRIMARY]; Cd3As2 I4_1/acd (142) mp-1199496 [hull=0.059, icsd=2]; Cd3As2 P4_2/nbc (133) mp-1201202 [hull=0.021, icsd=1]
- papers: Physical and electronic properties of semiconducting solid solutions of the Cd3 As2Cd3 P2 system | Magnetic Field‐Enhanced Thermoelectric Performance in Dirac Semimetal Cd\n            3\n            As\n            2\n            Crystals with Different Carrier Concentrations | Magnetic-field enhanced high-thermoelectric performance in topological Dirac semimetal Cd 3 As 2 crystal

## Bi-Cs-Te
- rank 144 | 50 samples | 8 papers | 27 compositions
- compositions: CsBi4Te6 (11); (SbI3)0.0005CsBi4Te6 (8); In0.06CsBi4Te6.09 (3); CsBi4.001Te6 (2); Sb0.0006CsBi4Te6 (2); CsBi4Te6.01 (2)
- dopant candidates (<5% at.): Sb (14), I (11), Sn (7), In (7), Zn (2), Mg (2), Se (1), Pb (1)
- seed hypothesis (confirm): csbi4te6
- measured range: 11-665 K (5th-95th pct of 81 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cs(Bi2Te3)2 C2/m (12) mp-1204077 [hull=0.189, icsd=1, PRIMARY]; Cs(Bi2Te3)2 Cm (8) mp-672338 [hull=0.000]
- papers: Thermoelectric properties of metal/molecule/metal junction for different lengths of polythiophene | Thermo-elektrische Verbindungen. Strom aus Abwärme | A New Thermoelectric Material: CsBi4Te6

## In-Sb
- rank 145 | 50 samples | 19 papers | 22 compositions
- compositions: InSb (22); (InSb)91.48(MnSb)8.52 (4); Ga0.03In0.97Sb (3); (InSb)97.5(NiSb)2.5 (2); ZnIn18GeSb20 (2); (InSb)50Cu1 (1)
- dopant candidates (<5% at.): Zn (8), Ga (4), Mn (4), Cu (3), Ni (3), Ge (2), Pb (1), I (1)
- seed hypothesis (confirm): sphalerite
- measured range: 13-774 K (5th-95th pct of 140 curves; full span incl. outliers 10-1165 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): InSb F-43m (216) mp-20012 [hull=0.000, icsd=26, PRIMARY]; In5Sb3 I4/mcm (140) mp-1188565 [hull=0.121, icsd=1, PRIMARY]; In3Sb Pm-3m (221) mp-1021668 [hull=0.086, PRIMARY]; In2Sb P6_3/mmc (194) mp-1207221 [hull=0.089, PRIMARY]; InSb2 Pmmm (47) mp-1212332 [hull=1.522, PRIMARY]
- papers: Radiation-Corrected Harman Method for Characterization of Thermoelectric Materials | Nanograined Half-Heusler Semiconductors as Advanced Thermoelectrics: An Ab Initio High-Throughput Statistical Study | Thermoelectric properties and figure of merit of a Te-doped InSb bulk single crystal

## Sb-Yb-Zn
- rank 146 | 50 samples | 17 papers | 28 compositions
- compositions: YbZn2Sb2 (17); Yb9Zn4.2Sb9 (3); YbZn1.95Mn0.05Sb2 (2); YbZn1.85Mn0.15Sb2 (2); YbZn1.8Mn0.2Sb2 (2); YbZn1.9Mn0.1Sb2 (2)
- dopant candidates (<5% at.): Mn (9), In (5), Ge (4), La (3)
- seed hypothesis (confirm): caal2si2_zintl, zintl_9_4_9  <-- MIXED, split per composition
- measured range: 296-869 K (5th-95th pct of 185 curves; full span incl. outliers 22-985 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(ZnSb)2 P-3m1 (164) mp-1068431 [hull=0.000, icsd=3, PRIMARY]; Yb2ZnSb2 Pm (6) mp-1216147 [hull=0.000, PRIMARY]
- papers: Enhanced thermoelectric performance via randomly arranged nanopores: Excellent transport properties of YbZn2Sb2 nanoporous materials | Zintl Phases as Thermoelectric Materials: Tuned Transport Properties of the Compounds CaxYb1-xZn2Sb2 | Synthesis and high thermoelectric efficiency of Zintl phase YbCd2−xZnxSb2

## Al-Mn-Si
- rank 147 | 49 samples | 16 papers | 42 compositions
- compositions: Al74.6Mn17.4Si8 (3); Al32Cr1.5Mn32.5Si34 (2); Al0.37Mn0.30Ru0.03Si0.3 (2); Al32CrMn33Si34 (2); Al71.6Mn17.4Si11 (2); Al73.6Mn17.4Si9 (2)
- dopant candidates (<5% at.): Cr (19), In (5), Fe (2), Ru (2), W (1), Ta (1), F (1)
- seed hypothesis (confirm): hms_chimney_ladder
- measured range: 10-977 K (5th-95th pct of 135 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn3Al9Si P6_3/mmc (194) mp-15819 [hull=0.000, icsd=1, PRIMARY]; Mn3(Al2Si)2 C2 (5) mp-1221843 [hull=0.040, PRIMARY]
- papers: Synthesis of Mn(AlxSi1-x)2+^|^delta; Solid Solutions Using NaAlSi and Their Thermoelectric Properties | Thermoelectric properties of Al–Mn–Si C40 phase containing small amount of W or Ta | Thermoelectric properties of n-type Mn3−xCrxSi4Al2 in air

## Fe-Sb-V
- rank 148 | 49 samples | 16 papers | 37 compositions
- compositions: FeVSb (7); FeV0.99Sb0.99 (3); FeV0.9Ti0.1Sb (2); VFeSb (2); FeV0.9Hf0.1Sb (2); Fe(V0.905Hf0.045Ti0.050)Sb (2)
- dopant candidates (<5% at.): Hf (10), Ti (8), Se (5), Te (5), Sn (5), Nb (3), Zr (2)
- seed hypothesis (confirm): half_heusler
- measured range: 298-960 K (5th-95th pct of 194 curves; full span incl. outliers 56-1051 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): VFeSb P6_3/mmc (194) mp-1071423 [hull=0.298, icsd=1, PRIMARY]; VFeSb F-43m (216) mp-10756 [hull=0.454, icsd=1]
- papers: Thermoelectric properties of FeVSb half-Heusler compounds by levitation melting and spark plasma sintering | Synthesis and thermoelectric properties of fine-grained FeVSb system half-Heusler compound polycrystals with high phase purity | Enhanced phonon scattering by mass and strain field fluctuations in Nb substituted FeVSb half-Heusler thermoelectric materials

## Al-Yb
- rank 149 | 48 samples | 15 papers | 16 compositions
- compositions: YbAl3 (33); Yb1.05Al3B0.10 (1); Yb1.05Al3C0.10 (1); Yb1.05Al3 (1); Yb1.05Al3B0.05 (1); Yb1.05Al3C0.05 (1)
- dopant candidates (<5% at.): O (4), Fe (4), B (2), C (2), Sn (2), Y (1), Sb (1)
- seed hypothesis (confirm): cu3au_l12
- measured range: 14-679 K (5th-95th pct of 215 curves; full span incl. outliers 10-750 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbAl2 Fd-3m (227) mp-969 [hull=0.000, icsd=9, PRIMARY]; YbAl3 Pm-3m (221) mp-1259 [hull=0.088, icsd=7, PRIMARY]; Yb4Al Fd-3m (227) mp-1207597 [hull=0.522, PRIMARY]; Yb3Al Fm-3m (225) mp-1187947 [hull=0.084, PRIMARY]
- papers: Synthesis, crystal structure, and thermoelectric properties of the YbAl3-ScAl3 solid solution | Effect of addition of B or C on thermoelectric properties of heavy fermion intermetallic compound YbAl3 | Influence of Sn substitution on the thermoelectric properties in YbAl3

## Ba-Cu-Eu-O
- rank 150 | 48 samples | 4 papers | 14 compositions
- compositions: EuBa2Cu3O7 (14); EuBa2Cu3O6.68 (4); EuBa2Cu3O6.58 (4); EuBa2Cu3O6.79 (4); EuBa2Cu3O6.48 (4); EuBa2Cu3O6.53 (2)
- seed hypothesis (confirm): ybco_cuprate
- measured range: 11-296 K (5th-95th pct of 48 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2EuCu3O7 Pmmm (47) mp-622211 [hull=0.018, icsd=1, PRIMARY]; Ba2Eu(CuO2)4 Cmmm (65) mp-1214709 [hull=0.005, PRIMARY]; Ba4Eu2Cu6O13 Fmmm (69) mp-1228334 [hull=0.014, PRIMARY]; BaEu2CuO5 Pnma (62) mp-1214737 [hull=0.019, PRIMARY]
- papers: Thermoelectric power in the normal state of high-Tc superconductors RBa2Cu3Ox (R = yttrium or rare earth) | Perspective on RBa2Cu3Ox materials from oxygen deficiency studies | Structural and electronic anisotropy in polycrystalline compactions of the high-Tc superconductor EuBa2Cu3O7−δ
