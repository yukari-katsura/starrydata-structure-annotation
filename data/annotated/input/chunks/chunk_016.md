# Host systems -- chunk 016 of 73

Ranks 751-800 by sample count. These 50 host systems cover 403 samples (0.77% of the TE set); cumulative through this chunk: 86.45%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Si-Sn
- rank 751 | 9 samples | 1 papers | 9 compositions
- compositions: Sn0.28Si0.72 (1); Sn0.33Si0.67 (1); Sn0.34Si0.66 (1); Sn0.38Si0.62 (1); Sn0.46Si0.54 (1); Sn0.47Si0.53 (1)
- solid-solution axis: Si/(Si+Sn) spans 0.30-0.72 (median 0.54) over 9 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 12-301 K (5th-95th pct of 9 curves)
- [ref 1] TEDesignLab / ICSD: SiSn F-43m (216) mp-1009813 [hull=0.150, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Si18Sn Cm (8) mp-1094080 [hull=0.920, PRIMARY]; SiSn3 Pm-3m (221) mp-978494 [hull=0.321, PRIMARY, AMBIGUOUS]; SiSn3 P-1 (2) mp-1187081 [hull=0.330]
- papers: Electric Evolution in Sputter-Deposited Sn&lt;sub&gt;&lt;i&gt;c&lt;/i&gt;&lt;sub&gt;Sn&lt;/sub&gt;&lt;/sub&gt;Si&lt;sub&gt;1−&lt;i&gt;c&lt;/i&gt;&lt;sub&gt;Sn&lt;/sub&gt;&lt;/sub&gt; Alloy Films

## Ti
- rank 752 | 9 samples | 7 papers | 3 compositions
- compositions: Ti (7); Li(Ti0.99V0.01)24 (1); Ti97Al3 (1)
- dopant candidates (<5% at.): Li (1), V (1), Al (1)
- measured range: 11-1063 K (5th-95th pct of 16 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti P6_3/mmc (194) mp-46 [hull=0.007, icsd=31, PRIMARY]; Ti Im-3m (229) mp-73 [hull=0.114, icsd=5]; Ti P6/mmm (191) mp-72 [hull=0.000, icsd=2]; Ti Fm-3m (225) mp-6985 [hull=0.063, icsd=2]
- papers: Titanium-based silicide quantum dot superlattices for thermoelectrics applications | Electrical and thermal properties of titanium hydrides | Thermal conductivities of Ti-SiC and Ti-TiB2 particulate composites

## Zn
- rank 753 | 9 samples | 6 papers | 3 compositions
- compositions: Zn (4); Zn0978Al0.02Ga0.002 (4); YbCoNiZn20 (1)
- dopant candidates (<5% at.): Al (4), Ga (4), Yb (1), Co (1), Ni (1)
- measured range: 11-1072 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zn P6_3/mmc (194) mp-79 [hull=0.000, icsd=30, PRIMARY]; ZrZn22 Fd-3m (227) mp-30888 [hull=0.003, icsd=2, PRIMARY]; HfZn22 Fd-3m (227) mp-1201271 [hull=0.028, icsd=1, PRIMARY]; Zn R-3m (166) mp-1187812 [hull=0.007]
- papers: Electronic transport properties of liquid Ga–Zn alloys | Thermal conductivity and Lorenz function of zinc under pressure | Solid-liquid interfacial energy of Al-Zn solid-solutions in equilibrium with Al-Zn liquid

## Ag-Ca-Sb-Zn
- rank 754 | 8 samples | 1 papers | 8 compositions
- compositions: CaZn0.35Ag0.3Sb (1); CaZn0.25Ag0.5Sb (1); CaZn0.4Ag0.18Sb (1); CaZn0.4Ag0.14Sb (1); CaZn0.4Ag0.2Sb (1); CaZn0.3Ag0.4Sb (1)
- measured range: 319-1073 K (5th-95th pct of 40 curves)
- papers: Defect modulation on CaZn1−xAg1−ySb (0 < x < 1; 0 < y <1) Zintl phases and enhanced thermoelectric properties with high zT plateaus

## Al-Ba-Ga-Sn
- rank 755 | 8 samples | 2 papers | 4 compositions
- compositions: Ba8Ga12Al4Sn30 (5); Ba8Ga10Al6Sn30 (1); Ba8Ga8Al8Sn30 (1); Ba8Ga6Al10Sn30 (1)
- solid-solution axis: Al/(Al+Ga) spans 0.25-0.63 (median 0.50) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 296-601 K (5th-95th pct of 18 curves)
- papers: Enhancement of thermoelectric efficiency in type-VIII clathrate Ba8Ga16Sn30 by Al substitution for Ga | Thermoelectric performance of Zn-substituted type-VIII clathrate Ba8Ga16Sn30 single crystals

## Al-Co-U
- rank 756 | 8 samples | 1 papers | 1 compositions
- compositions: UCoAl (8)
- measured range: 10-50 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UAlCo P-62m (189) mp-1079367 [hull=0.100, icsd=3, PRIMARY]; U2AlCo2 P4/mbm (127) mp-21269 [hull=0.097, icsd=1, PRIMARY]; U2(Al3Co)3 Cmcm (63) mp-641651 [hull=0.054, icsd=1, PRIMARY]; UAl4Co P-62m (189) mp-30914 [hull=0.047, icsd=1, PRIMARY]; U2AlCo3 P6_3/mmc (194) mp-30176 [hull=0.053, icsd=1, PRIMARY]
- papers: Metamagnetic Transition in UCoAl Probed by Thermoelectric Measurements

## Al-Fe-Ta-V
- rank 757 | 8 samples | 4 papers | 3 compositions
- compositions: Fe2V0.75Ta0.25Al (5); Fe2(V0.7Ta0.2Ti0.1)Al (2); Fe2VTa1.12Al0.88 (1)
- dopant candidates (<5% at.): Ti (2)
- measured range: 16-796 K (5th-95th pct of 15 curves)
- papers: Thermoelectric properties of the Heusler-type Fe2VTaxAl1−x alloys | Effects of Heavy Element Substitution on Electronic Structure and Lattice Thermal Conductivity of Fe2VAl Thermoelectric Material | Thermoelectric Properties of Fe2VAl and Fe2V0.75M0.25Al (M = Mo, Nb, Ta) Alloys: First-Principles Calculations

## Al-Ni-V
- rank 758 | 8 samples | 2 papers | 4 compositions
- compositions: Ni2VAl1.08 (5); Ni75V18Al7 (1); Ni75V14Al11 (1); Ni75V10Al15 (1)
- measured range: 11-1074 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlVNi2 Fm-3m (225) mp-10899 [hull=0.045, icsd=1, PRIMARY]; Al2VNi9 P4/mmm (123) mp-1228540 [hull=0.000, PRIMARY]; Al4VNi15 P4/mmm (123) mp-1228506 [hull=0.007, PRIMARY]; AlVNi F-43m (216) mp-961650 [hull=0.819, PRIMARY]; AlVNi2 P4/mmm (123) mp-1228840 [hull=0.052]
- papers: Thermal conductivity of Ni3V–Ni3Al pseudo-binary alloys | Off-stoichiometric effect on magnetic and electron transport properties of Fe2⁢VAl1.35 and Ni2⁢VAl: A comparative study

## Al-O-Zr
- rank 759 | 8 samples | 1 papers | 8 compositions
- compositions: (Al2O3)77.09(ZrO2)22.91 (1); (Al2O3)45.69(ZrO2)54.31 (1); (Al2O3)35.93(ZrO2)64.07 (1); (Al2O3)26.5(ZrO2)73.5 (1); (Al2O3)17.38(ZrO2)82.62 (1); (Al2O3)8.55(ZrO2)91.45 (1)
- measured range: 374-1270 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zr10Al6O P3m1 (156) mp-1215954 [hull=0.023, PRIMARY]; Zr10Al6O P-31m (162) mp-1215691 [hull=0.034]
- papers: Thermal Conductivity of Al2O3-ZrO2 Composite Ceramics

## Al-V
- rank 760 | 8 samples | 5 papers | 8 compositions
- compositions: V3Al (1); PrV2Al20 (1); LaV2Al20 (1); Al3V (1); Al3V0.95Ti0.05 (1); Al3V0.9Ti0.1 (1)
- dopant candidates (<5% at.): Ti (2), Pr (1), La (1), Sm (1)
- measured range: 11-1074 K (5th-95th pct of 14 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al3V I4/mmm (139) mp-2554 [hull=0.000, icsd=5, PRIMARY]; AlV3 Pm-3n (223) mp-1387 [hull=0.000, icsd=3, PRIMARY]; Al23V4 P6_3/mmc (194) mp-30335 [hull=0.004, icsd=2, PRIMARY]; Pr(Al10V)2 Fd-3m (227) mp-1204963 [hull=0.000, icsd=1, PRIMARY]; La(Al10V)2 Fd-3m (227) mp-1195666 [hull=0.000, icsd=1, PRIMARY]
- papers: High temperature thermoelectric properties of (Fe1−xVx)3Al Heusler type compounds | Thermoelectric Power Anomaly of PrTi2Al20and PrV2Al20with Non-Kramers Γ3Ground State | Reduction of lattice thermal conductivity of pseudogap intermetallic compound Al3V

## As-Fe
- rank 761 | 8 samples | 5 papers | 5 compositions
- compositions: FeAs2 (4); Fe(As0.99Se0.01)2 (1); Fe(As0.975Se0.025)2 (1); Fe(As0.95Se0.05)2 (1); FeAs (1)
- dopant candidates (<5% at.): Se (3)
- measured range: 10-308 K (5th-95th pct of 20 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeAs Pnma (62) mp-427 [hull=0.000, icsd=16, PRIMARY]; FeAs2 Pnnm (58) mp-2008 [hull=0.000, icsd=10, PRIMARY]; Fe2As P4/nmm (129) mp-20426 [hull=0.062, icsd=5, PRIMARY]; Fe12As5 R32 (155) mp-17977 [hull=0.047, icsd=1, PRIMARY]
- papers: Huge Thermoelectric Power Factor: FeSb2versus FeAs2and RuSb2 | Highly dispersive electron relaxation and colossal thermoelectricity in the correlated semiconductor FeSb2 | Narrow band gap and enhanced thermoelectricity in FeSb2

## As-Fe-K-Sr
- rank 762 | 8 samples | 1 papers | 8 compositions
- compositions: K0.522Sr0.48Fe2As2 (1); K0.62Sr0.38Fe2As2 (1); K0.72Sr0.28Fe2As2 (1); K0.35Sr0.65Fe2As2 (1); K0.42Sr0.58Fe2As2 (1); K0.27Sr0.73Fe2As2 (1)
- measured range: 13-326 K (5th-95th pct of 8 curves)
- papers: Evidence of quantum criticality in the phase diagram ofKxSr1−xFe2As2from measurements of transport and thermoelectricity

## B-C-Si-Ti
- rank 763 | 8 samples | 2 papers | 8 compositions
- compositions: (TiB2)76.55(SiC)23.45 (1); (TiB2)76.25(SiC)22.19(C)1.57 (1); (TiB2)75.05(SiC)17.24(C)7.71 (1); (TiB2)74.47(SiC)14.83(C)10.7 (1); (TiB2)82.22(SiC)17.78 (1); (TiB2)76.4(SiC)22.82(C)0.78 (1)
- measured range: 298-573 K (5th-95th pct of 8 curves; full span incl. outliers 298-1260 K)
- papers: Microstructures and properties of silicon carbide- and graphene nanoplatelet-reinforced titanium diboride composites | Thermal diffusivity and microstructure of spark plasma sintered TiB2SiC Ti composite

## B-La
- rank 764 | 8 samples | 4 papers | 3 compositions
- compositions: LaB6 (6); Ce0.25La0.75B6 (1); Ce0.05La0.95B6 (1)
- dopant candidates (<5% at.): Ce (2)
- measured range: 10-259 K (5th-95th pct of 12 curves; full span incl. outliers 10-300 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaB6 Pm-3m (221) mp-2680 [hull=0.000, icsd=20, PRIMARY]; LaB4 P4/mbm (127) mp-7283 [hull=0.000, icsd=2, PRIMARY]
- papers: Thermal conductivity of CeB6 and LaB6 | Thermoelectric power in Ce1−xLaxB6 Kondo systems | Thermal conductivity of LaB6: the role of phonons

## Ba-Ca-Cu-Hg-O
- rank 765 | 8 samples | 2 papers | 2 compositions
- compositions: HgBa2Ca2Cu3O8 (5); Hg0.82Re0.18Ba2Ca2Cu3O8 (3)
- dopant candidates (<5% at.): Re (3)
- measured range: 87-302 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2CaCu2HgO6 P4/mmm (123) mp-6879 [hull=0.013, icsd=6, PRIMARY]; Ba10Ca5Cu10Hg5O31 P-1 (2) mp-1229139 [hull=0.027, PRIMARY]; Ba2Ca3Cu4HgO10 P4/mmm (123) mp-1228579 [hull=0.022, PRIMARY]; Ba2CaCu(HgO3)2 P4/mmm (123) mp-1214691 [hull=0.269, PRIMARY]; Ba4Ca4Cu6Hg2O17 I4/mmm (139) mp-1228265 [hull=0.055, PRIMARY]
- papers: Transport properties of single-crystal HgBa2Ca2Cu3O8+δ | Distortion of ReO6 octahedron in the Hg0.82Re0.18Ba2Ca2Cu3O8+d superconductor

## Ba-Ca-Cu-O-Tl
- rank 766 | 8 samples | 2 papers | 3 compositions
- compositions: TlBa2Ca2Cu3O9 (3); Tl2Ba2Ca2Cu3O10 (3); Tl2Ba2CaCu2O8 (2)
- measured range: 29-293 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2CaTl2(CuO4)2 I4/mmm (139) mp-6885 [hull=0.009, icsd=3, PRIMARY]; Ba6Ca6Tl5Cu9O29 P4/mmm (123) mp-680433 [hull=0.022, icsd=2, PRIMARY]; Ba8Ca8Tl7(Cu4O13)3 I4/mmm (139) mp-1204270 [hull=0.002, icsd=2, PRIMARY]; Ba2CaTlCu2O7 P4/mmm (123) mp-632802 [hull=0.049, icsd=1, PRIMARY]; Ba2Ca4TlCu5O13 Pmm2 (25) mp-1229126 [hull=0.022, PRIMARY]
- papers: Systematic thermopower measurements of the thallium cuprates Tl(Ba,Sr)2Cam−1CumO2m+3−δ and Tl2Ba2Cam−1CumO2m+4+δ | Thermoelectric power of the thallium-based superconductorTl2Ba2Ca2Cu3O10−δ

## Ba-Cu-Er-O
- rank 767 | 8 samples | 2 papers | 2 compositions
- compositions: ErBa2Cu4O8 (5); ErBa2Cu3O7 (3)
- measured range: 15-300 K (5th-95th pct of 8 curves; full span incl. outliers 15-407 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2Er(CuO2)4 Cmmm (65) mp-6583 [hull=0.004, icsd=6, PRIMARY]; Ba2ErCu3O7 Pmmm (47) mp-622110 [hull=0.028, icsd=2, PRIMARY]; Ba10Er5Cu15O34 P-1 (2) mp-1229210 [hull=0.023, PRIMARY]
- papers: Normal-state transport properties of the high-Tc superconductor ErBa2Cu4O8 | Thermopower ofRBa2Cu3O7−x(R=Y,Er)

## Ba-O-Sr-Ti
- rank 768 | 8 samples | 3 papers | 8 compositions
- compositions: Ba0.5Sr0.4La0.1TiO3 (1); Ba0.3Sr0.6La0.1TiO3 (1); Ba0.7Sr0.3TiO3 (1); Ba0.65Sr0.35TiO3 (1); (Y2O3)0.0016(Ba0.7Sr0.3TiO3)0.9984 (1); (Y2O3)0.0024(Ba0.7Sr0.3TiO3)0.9976 (1)
- dopant candidates (<5% at.): Y (4), La (2)
- solid-solution axis: Ba/(Ba+Sr) spans 0.33-0.70 (median 0.70) over 8 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 223-865 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2Sr2CaTi5O15 Pm (6) mp-1228440 [hull=0.023, PRIMARY]; Ba2Sr6Ti7MnO24 Cmm2 (35) mp-1076337 [hull=0.042, PRIMARY]; Ba2SrTi3O9 Cmm2 (35) mp-1228362 [hull=0.007, PRIMARY]; Ba3Sr5Ti7MnO20 P1 (1) mp-1076186 [hull=0.120, PRIMARY]; Ba3Sr5Ti7MnO24 Cm (8) mp-1075974 [hull=0.015, PRIMARY]
- papers: Thermoelectric properties of doped BaTiO3–SrTiO3 solid solution | Temperature-dependent resistivity performance of Mn/Y-doped Ba1Sr TiO3 compositions with potential thermal control applications | Effect of Yttrium Doping on Microstructure and Temperature Resistance Characteristics of Barium Strontium Titanate Ferroelectric Ceramics

## Bi-In-Te
- rank 769 | 8 samples | 4 papers | 5 compositions
- compositions: (Bi2Te3)32.5(In2Te3)7.5 (3); Bi33.5In7.5Te59 (2); Bi35.6In6.2Te58.2 (1); Bi1.7In0.3Sb0.2Te3 (1); (Bi)26.46(In)8.13(Ga)3.77(Te)61.64 (1)
- dopant candidates (<5% at.): Sb (1), Ga (1)
- measured range: 288-571 K (5th-95th pct of 38 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): In3BiTe4 I422 (97) mp-1223965 [hull=0.206, PRIMARY]; InBi3Te4 Pm (6) mp-1224344 [hull=0.200, PRIMARY]
- papers: Anisotropic n-Type Bi2Te3–In2Te3Thermoelectric Material Produced by Seeding Zone Melting and Solid State Transformation | Two-Step Annealing Leading to Refined Bi2Te3-In2Te3 Lamellar Structures for Tuning of Thermoelectric Properties | Ultralow Thermal Conductivity in Dual‐Doped n‐Type Bi\n            2\n            Te\n            3\n            Material for Enhanced Thermoelectric Properties

## Bi-O
- rank 770 | 8 samples | 4 papers | 5 compositions
- compositions: Bi2O3 (3); Bi24CoO37(Bi0.9La0.1)FeO3 (2); Bi24CoO37 (1); Bi12PbO19 (1); Bi25FeO39 (1)
- dopant candidates (<5% at.): Co (3), Fe (3), La (2), Pb (1)
- measured range: 87-930 K (5th-95th pct of 14 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Si(Bi3O5)4 I23 (197) mp-23492 [hull=0.007, icsd=14, PRIMARY]; Bi2O3 P2_1/c (14) mp-23262 [hull=0.000, icsd=10, PRIMARY]; Ge(Bi3O5)4 I23 (197) mp-23352 [hull=0.001, icsd=4, PRIMARY]; ReBi9O17 P2_1/c (14) mp-1197231 [hull=0.007, icsd=3, PRIMARY]; CrBi8O15 P2_1/m (11) mp-705013 [hull=0.003, icsd=1, PRIMARY]
- papers: Thermoelectric properties of Co-doped BiFeO3 and Bi24CoO37^|^ndash;BiFeO3 compound systems | Studies of the electrical properties of bismuth oxide films | Electrical and thermal properties of Bi/sub 2/O/sub 3/, PbO and mixed oxides of Bi/sub 2/O/sub 3/-PbO system

## Bi-O-Ti
- rank 771 | 8 samples | 2 papers | 6 compositions
- compositions: Bi4Ti3O12 (3); Na0.5Bi4.5Ti4O15 (1); Na0.5Bi4.482Er0.018Ti4O15 (1); Na0.5Bi4.475Er0.025Ti4O15 (1); Na0.5Bi4.494Er0.006Ti4O15 (1); Na0.5Bi4.488Er0.012Ti4O15 (1)
- dopant candidates (<5% at.): Na (5), Er (4)
- measured range: 373-1273 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti3(BiO3)4 Aea2 (41) mp-23427 [hull=0.000, icsd=7, PRIMARY]; Ti(Bi3O5)4 I23 (197) mp-23494 [hull=0.008, icsd=3, PRIMARY]; Ti4Bi2O11 C2/m (12) mp-28962 [hull=0.006, icsd=1, PRIMARY]; Ti2Bi2O7 Pna2_1 (33) mp-1200889 [hull=0.011, icsd=1, PRIMARY]; Ti8BiO7 Cmmm (65) mp-1105121 [hull=0.025, icsd=1, PRIMARY]
- papers: Anisotropic thermal conductivity of the Aurivillus phase, bismuth titanate (Bi4Ti3O12): A natural nanostructured superlattice | Thermal stability and enhanced electrical properties of Er<sup>3+</sup>-modified Na<sub>0.5</sub>Bi<sub>4.5</sub>Ti<sub>4</sub>O<sub>15</sub> lead-free piezoelectric ceramics

## Bi-S-Sb-Te
- rank 772 | 8 samples | 2 papers | 8 compositions
- compositions: BiSbSTe2 (1); Bi1.5Sb0.5Te2S (1); Bi1.0Sb1.0Te2S (1); Bi0.5Sb1.5Te2S (1); Bi1.0Sb0.95Sn0.05Te2S (1); Bi1.0Sb0.9Sn0.1Te2S (1)
- dopant candidates (<5% at.): Sn (2), Cl (1)
- solid-solution axis: Bi/(Bi+Sb) spans 0.25-0.75 (median 0.53) over 8 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-380 K (5th-95th pct of 36 curves)
- papers: Crystal structure, electronic structure and thermoelectric properties of n-type BiSbSTe2 | Thermoelectric properties of the tetradymite-type Bi2Te2S–Sb2Te2S solid solution

## Bi-Se-Sn
- rank 773 | 8 samples | 4 papers | 4 compositions
- compositions: SnBi4Se7 (3); Bi0.8Sn0.2Se (2); Bi0.9Sn0.1Se (2); (SnSe2)0.67(BiSe2)0.33 (1)
- measured range: 90-674 K (5th-95th pct of 27 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sn4Bi2Se7 C2/m (12) mp-675477 [hull=0.033, PRIMARY]
- papers: Thermoelectric properties of a eutectic SnSe2-Bi2Se3 alloy | Preparation and thermoelectric power of SnBi4Se7 | Impurity band in SnBi4Se7: thermoelectric power and electrical resistivity measurements

## C-Cu
- rank 774 | 8 samples | 2 papers | 8 compositions
- compositions: (C)84.43(Cu)15.11(Ti)0.46 (1); (C)91.45(Cu)8.55 (1); (C)90.02(Cu)9.69(Ti)0.29 (1); (C)86.93(Cu)13.07 (1); Cu9.69Ti0.29C90.02 (1); Cu8.55C91.45 (1)
- dopant candidates (<5% at.): Ti (4)
- measured range: 292-1272 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuC6 Cmmm (65) mp-1213653 [hull=1.354, PRIMARY]
- papers: Effects of titanium impregnation on the thermal conductivity of carbon/copper composite materials | Effects of titanium addition on the microstructure of carbon/copper composite materials

## C-N-Th
- rank 775 | 8 samples | 1 papers | 8 compositions
- compositions: ThC0.778N0.108 (1); ThC0.625N0.275 (1); ThC0.461N0.489 (1); ThC0.203N0.738 (1); ThC0.29N0.937 (1); ThC0.537N0.380 (1)
- measured range: 72-711 K (5th-95th pct of 18 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ThCN C2/m (12) mp-30521 [hull=0.105, icsd=1, PRIMARY]; Th2CN R-3m (166) mp-1217332 [hull=0.000, PRIMARY]
- papers: Electrical Properties of Thorium Carbonitrides

## C-O-Ti
- rank 776 | 8 samples | 3 papers | 4 compositions
- compositions: TiO2@TiCO (5); (Ti0.96Nb0.04O2)5TiC (1); (TiO2)5TiC (1); (TiO2)13.07C86.93 (1)
- dopant candidates (<5% at.): Nb (1)
- measured range: 372-1031 K (5th-95th pct of 26 curves; full span incl. outliers 79-1033 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti2C2O9 Cmce (64) mp-1198230 [hull=0.540, icsd=1, PRIMARY]
- papers: Semiconducting large bandgap oxides as potential thermoelectric materials for high-temperature power generation? | Effect of coated TiO2 nano-particle on thermoelectric performance of TiC0.5O0.5 Ceramics | Metal-to-insulator transition near room temperature in graphene oxide and graphene oxide + TiO2 thin films

## C-Si-Ti
- rank 777 | 8 samples | 2 papers | 3 compositions
- compositions: (SiC)8.3Ti91.7 (6); (Ti)91.7(SiC)8.3 (1); (Ti)83.08(SiC)16.92 (1)
- measured range: 333-950 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti3SiC2 P6_3/mmc (194) mp-5659 [hull=0.000, icsd=16, PRIMARY]; Ti2SiC P6_3/mmc (194) mp-1079908 [hull=0.019, icsd=2, PRIMARY]; Ti12AlSi3C8 P6_3/mmc (194) mp-1197979 [hull=0.007, icsd=1, PRIMARY]; Ti5Si3C P6_3/mcm (193) mp-995201 [hull=0.000, PRIMARY]
- papers: The effect of interfacial reaction on thermal properties of titanium reinforced with particulate SiC | Thermal conductivities of Ti-SiC and Ti-TiB2 particulate composites

## C-Zr
- rank 778 | 8 samples | 3 papers | 2 compositions
- compositions: ZrC (7); ZrC0.99N0.03 (1)
- dopant candidates (<5% at.): N (1)
- measured range: 103-2393 K (5th-95th pct of 8 curves; full span incl. outliers 103-2617 K)
- [ref 1] TEDesignLab / ICSD: ZrC F-43m (216) mp-1009894 [hull=0.614, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: ZrC Fm-3m (225) mp-2795 [hull=0.000, icsd=43, PRIMARY]; Zr10C9 C2/c (15) mp-684623 [hull=0.000, PRIMARY]; Zr3C P6_3/mmc (194) mp-1188023 [hull=1.149, PRIMARY]; ZrC Pm-3m (221) mp-1009878 [hull=1.221, icsd=2]; ZrC P6_3/mmc (194) mp-1014307 [hull=0.172]
- papers: Thermal properties and thermal shock resistance of liquid phase sintered ZrC–Mo cermets | Densification, mechanical and thermal properties of ZrC1− ceramics fabricated by two-step reactive hot pressing of ZrC and ZrH2 powders | Processing and properties of ZrC, ZrN and ZrCN ceramics: a review

## Ca-Nd-O-Ti
- rank 779 | 8 samples | 2 papers | 8 compositions
- compositions: Nd0.4Ca0.6TiO3 (1); Nd0.3Ca0.7TiO3 (1); Nd0.5Ca0.5TiO3 (1); Ca0.61Nd0.26Ti0.98(Al0.5Nb0.5)0.02O3 (1); Ca0.61Nd0.26Ti0.88(Al0.5Nb0.5)0.12O3 (1); Ca0.61Nd0.26TiO3 (1)
- dopant candidates (<5% at.): Al (4), Nb (4)
- measured range: 85-673 K (5th-95th pct of 8 curves)
- papers: Band filling dependence of the electrical transport of Nd1−xAxTiO3 (A=Ca, Sr and Ba) | Characterization of structural and electrical properties of Ca0.61Nd0.26TiO3 ceramic tailored by complex ions (Al0.5Nb0.5)4+

## Ca-Sb
- rank 780 | 8 samples | 3 papers | 8 compositions
- compositions: Ca14MgSb11 (1); Ca16Sb11 (1); Ca13LaMnSb11 (1); Ca13CeMnSb11 (1); Ca13PrMnSb11 (1); Ca13NdMnSb11 (1)
- dopant candidates (<5% at.): Mn (6), Mg (1), La (1), Ce (1), Pr (1), Nd (1), Gd (1), Sm (1)
- measured range: 14-1083 K (5th-95th pct of 13 curves; full span incl. outliers 14-1275 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca5Sb3 Pnma (62) mp-17564 [hull=0.000, icsd=2, PRIMARY, AMBIGUOUS]; Ca2Sb I4/mmm (139) mp-9925 [hull=0.000, icsd=2, PRIMARY]; Ca11Sb10 I4/mmm (139) mp-12241 [hull=0.000, icsd=1, PRIMARY]; CaSb2 P2_1/m (11) mp-7493 [hull=0.000, icsd=1, PRIMARY]; Ca3Sb2 Pm-3m (221) mp-1013546 [hull=0.379, PRIMARY]
- papers: Yb14MgSb11and Ca14MgSb11—New Mg-Containing Zintl Compounds and Their Structures, Bonding, and Thermoelectric Properties | Thermoelectric properties and electronic structure calculations of low thermal conductivity Zintl phase series M16X11 (M=Ca and Yb; X=Sb and Bi) | On the Extended Series of Quaternary Zintl Phases Ca13REMnSb11 (RE = La-Nd, Sm, Gd-Dy)

## Cd-Mg-Sb
- rank 781 | 8 samples | 2 papers | 8 compositions
- compositions: (Mg0.9Cd0.1)3Sb2 (1); (Mg0.7Cd0.3)3Sb2 (1); (Mg0.8Cd0.2)3Sb2 (1); (Mg0.7Cd0.25Ag0.05)3Sb2 (1); Mg2.39Li0.01Cd0.8Sb2 (1); Mg2.69Li0.01Cd0.5Sb2 (1)
- dopant candidates (<5% at.): Li (4), Ag (1)
- measured range: 21-779 K (5th-95th pct of 36 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg14CdSb P-6m2 (187) mp-1026437 [hull=0.036, PRIMARY]; Mg6CdSb Amm2 (38) mp-1017201 [hull=0.082, PRIMARY]; Mg14CdSb Amm2 (38) mp-1026438 [hull=0.053]
- papers: Transport and thermoelectric properties of nanocrystal substitutional semiconductor alloys (Mg1−xCdx)3Sb2 doped with Ag | Enhancing the Thermoelectric Performance of p-Type Mg3Sb2 via Codoping of Li and Cd

## Cd-S
- rank 782 | 8 samples | 2 papers | 3 compositions
- compositions: CdS (6); Co0.01Cd0.99S (1); Co0.05Cd0.95S (1)
- dopant candidates (<5% at.): Co (2)
- measured range: 100-438 K (5th-95th pct of 15 curves)
- [ref 1] TEDesignLab / ICSD: CdS P6_3mc (186) mp-672 [hull=0.000, icsd=23, PRIMARY]; CdS2 Pa-3 (205) mp-1095440 [hull=0.000, icsd=1, PRIMARY]; CdS F-43m (216) mp-2469 [hull=0.001, icsd=14]; CdS Fm-3m (225) mp-370 [hull=0.134, icsd=8]
- [ref 2] MP, ranked by ICSD evidence: Cd2S P3m1 (156) mp-1120762 [hull=0.216, PRIMARY]; CdS Pmmn (59) mp-1181862 [hull=0.135]; CdS P3m1 (156) mp-1021511 [hull=0.253]
- papers: On the surface morphology and transport properties of chemical bath deposited CoxCd1−xS thin films: A correlation | Thermoelectric and photothermoelectric effects in semiconductors: CdS single crystals

## Ce-Co-Ga
- rank 783 | 8 samples | 1 papers | 1 compositions
- compositions: CeCo2Ga8 (8)
- measured range: 11-296 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeGaCo C2/m (12) mp-1071448 [hull=0.000, icsd=5, PRIMARY]; Ce(Ga4Co)2 Pbam (55) mp-1196595 [hull=0.000, icsd=1, PRIMARY]; Ce2Ga2Co15 R-3m (166) mp-1106200 [hull=0.061, icsd=1, PRIMARY]; Ce8Ga3Co P6_3mc (186) mp-1192313 [hull=0.007, icsd=1, PRIMARY]; CeGa4Co9 I4/mcm (140) mp-1006277 [hull=0.014, icsd=1, PRIMARY]
- papers: Heavy fermion behavior in the quasi-one-dimensional Kondo lattice CeCo2Ga8

## Ce-Co-In
- rank 784 | 8 samples | 4 papers | 1 compositions
- compositions: CeCoIn5 (8)
- measured range: 10-300 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce2In8Co P4/mmm (123) mp-19989 [hull=0.000, icsd=1, PRIMARY]; CeIn5Co P4/mmm (123) mp-19961 [hull=0.000, icsd=1, PRIMARY]
- papers: Universal linear-temperature resistivity: possible quantum diffusion transport in strongly correlated superconductors | Direct visualization of coexisting channels of interaction in CeSb | Tuning the Pairing Interaction in a \nd\n-Wave Superconductor by Paramagnons Injected through Interfaces

## Ce-Fe-La-O-P
- rank 785 | 8 samples | 1 papers | 8 compositions
- compositions: La0.7Ce0.3FePO (1); La0.6Ce0.4FePO (1); La0.5Ce0.5FePO (1); La0.4Ce0.6FePO (1); La0.33Ce0.67FePO (1); La0.3Ce0.7FePO (1)
- solid-solution axis: Ce/(Ce+La) spans 0.20-0.80 (median 0.60) over 8 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-298 K (5th-95th pct of 8 curves)
- papers: Spin glass, single-ion and dense Kondo effects in La\n                    <sub>1−x</sub>\n                    Ce\n                    <sub>x</sub>\n                    FePO

## Ce-Ga-Ni
- rank 786 | 8 samples | 5 papers | 5 compositions
- compositions: Ce2Ni2Ga (3); CeNiGa (2); CeNi4Ga (1); Ce(Ni0.865Ga0.135)5 (1); Ce(Ni0.9Ga0.1)5 (1)
- measured range: 10-884 K (5th-95th pct of 13 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeGa2Ni Cmmm (65) mp-1025446 [hull=0.000, icsd=3, PRIMARY]; CeGaNi P-62m (189) mp-31492 [hull=0.000, icsd=2, PRIMARY]; Ce3Ga10Ni Pmmm (47) mp-1104373 [hull=0.023, icsd=1, PRIMARY]; Ce3(GaNi)2 Pbcm (57) mp-1194147 [hull=0.038, icsd=1, PRIMARY]; Ce2Ga10Ni I4/mmm (139) mp-7720 [hull=0.015, icsd=1, PRIMARY]
- papers: Thermoelectric power in (, Ni; , Ga) compounds | Dependence of the CeNi5 thermoelectric power on strong 4f-electron instability | From intermediate valence to magnetic behavior without long-range order by hydrogenation of the ternary gallide CeNiGa

## Ce-Ge-Ni-Si
- rank 787 | 8 samples | 2 papers | 8 compositions
- compositions: CeNi2(Ge0.8Si0.2)2 (1); CeNi2(Ge0.7Si0.3)2 (1); CeNi2(Ge0.6Si0.4)2 (1); CeNi2(Ge0.75Si0.25)2 (1); CeNi2(Si0.87Ge0.13)2 (1); CeNi2(Si0.25Ge0.75)2 (1)
- solid-solution axis: Ge/(Ge+Si) spans 0.13-0.80 (median 0.70) over 8 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 11-394 K (5th-95th pct of 8 curves)
- papers: Anomalous Behavior on Specific Heat and Thermoelectric Power in Wide Range of Temperatures in CeNi2(Ge1-xSix)2 | Influence of chemical composition on the X-ray photoemission, thermopower, specific heat, and magnetic properties of CeNi2(Si1-yGey)2

## Ce-S
- rank 788 | 8 samples | 2 papers | 8 compositions
- compositions: CeS1.41(SrS)0.07 (1); CeS1.38 (1); CeS1.41 (1); CeS1.43 (1); CeS1.34 (1); CeS1.40 (1)
- dopant candidates (<5% at.): Sr (2), Eu (1)
- measured range: 295-1286 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeS Fm-3m (225) mp-1096 [hull=0.000, icsd=15, PRIMARY]; CeS2 Pnma (62) mp-20594 [hull=0.011, icsd=4, PRIMARY]; Ce3S4 I-43d (220) mp-1382 [hull=0.003, icsd=3, PRIMARY]; Ce2S3 Pnma (62) mp-20973 [hull=0.000, icsd=2, PRIMARY]; Ce10S19 P4_2/n (86) mp-645688 [hull=0.001, icsd=1, PRIMARY]
- papers: Thermoelectric Properties of Some Cerium Sulfide Semiconductors from 4° to 1300°K | Preparation and thermoelectric properties of ternary rare earth sulfide γ-Ce3–xEuxS4

## Co-Gd-O-Sr
- rank 789 | 8 samples | 3 papers | 4 compositions
- compositions: Gd0.7Sr0.3CoO3 (3); SrGdCoO4 (3); Sr3GdCo3.9Ga0.1O10.5 (1); Sr3GdCo4O10.5 (1)
- dopant candidates (<5% at.): Ga (1)
- measured range: 10-1156 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrGd2Co2O7 P4_2/mnm (136) mp-606149 [hull=0.041, icsd=1, PRIMARY]; SrGd(CoO3)2 Fm-3m (225) mp-1218287 [hull=0.173, PRIMARY]; SrGdCoO4 I4mm (107) mp-1218232 [hull=0.062, PRIMARY]; SrGdCoO4 Cmcm (63) mp-1218280 [hull=0.115]
- papers: High-Temperature Thermoelectric and Microstructural Characteristics of Cobalt-Based Oxides with Ga Substituted on the Co-Site | Studies of structural, magnetic, electrical and thermal properties in layered perovskite cobaltite SrLnCoO4 (Ln = La, Ce, Pr, Nd, Eu, Gd and Tb) | Spin-state transition, magnetic, electrical and thermal transport properties of the perovskite cobalt oxide Gd0.7Sr0.3CoO3

## Co-Ge-Si
- rank 790 | 8 samples | 3 papers | 8 compositions
- compositions: CoSi0.9Ge0.1 (1); CoSi0.7Ge0.3 (1); CoSi0.6Ge0.4 (1); CoSi0.5Ge0.5 (1); CoSi0.88Ge0.1B0.02 (1); CoSi0.78Ge0.2B0.02 (1)
- dopant candidates (<5% at.): B (2)
- solid-solution axis: Ge/(Ge+Si) spans 0.10-0.50 (median 0.20) over 8 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 11-349 K (5th-95th pct of 30 curves; full span incl. outliers 10-614 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co2SiGe P2_1 (4) mp-1226449 [hull=0.029, PRIMARY]; Co3SiGe2 P1 (1) mp-1226179 [hull=0.022, PRIMARY]
- papers: High thermoelectric power factor in alloys based on CoSi | Isovalent substitutes play in different ways: Effects of isovalent substitution on the thermoelectric properties of CoSi0.98B0.02 | Thermoelectric properties of the CoSi1−xGex alloys

## Co-La-Mn-O-Sr
- rank 791 | 8 samples | 6 papers | 8 compositions
- compositions: La0.7Sr0.3Mn0.5Co0.5O3 (1); La0.7Sr0.3Mn0.3Co0.7O3 (1); La0.5Sr0.5Mn0.5Co0.5O3 (1); La0.75Sr0.25Co0.5Mn0.5O3 (1); La0.6Sr0.4Co0.5Ni0.2Mn0.3O3 (1); La0.25Sr0.75Co0.5Mn0.5O3 (1)
- dopant candidates (<5% at.): Ni (1)
- measured range: 52-1123 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2LaMnCoO7 I4mm (107) mp-1218748 [hull=0.028, PRIMARY]; SrLaMnCoO6 F-43m (216) mp-622615 [hull=0.007, PRIMARY]
- papers: Magnetic and transport behaviors of Co substitution in La0.7Sr0.3MnO3 perovskite | Effect of Fe and Co doping on structural and electrical properties of La0.5Sr1.5MnO4 layered-structure and the corresponding La0.5Sr0.5MnO3 perovskite | Investigations on structures, thermal expansion and electrochemical properties of La0.75Sr0.25Cu0.5−xCoxMn0.5O3−δ (x=0, 0.25, and 0.5) as potential cathodes for intermediate temperature solid oxide fuel cells

## Co-Sb-Sn
- rank 792 | 8 samples | 5 papers | 8 compositions
- compositions: CoSb2.7Sn0.3 (1); CoSb2.6Sn0.4 (1); CoSb2.5Sn0.5 (1); CoSb2.8Sn0.2 (1); Sn1.75Co8Sb24 (1); Pr0.5Co4Sb10Sn2 (1)
- dopant candidates (<5% at.): Ce (2), Pr (1)
- measured range: 296-772 K (5th-95th pct of 28 curves; full span incl. outliers 11-818 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co4SnSb12 Im-3 (204) mp-15868 [hull=0.055, icsd=1, PRIMARY]; Co10SnSb30 C2/m (12) mp-1227035 [hull=0.026, PRIMARY]; Co5(SnSb)2 P-6m2 (187) mp-1226073 [hull=0.105, PRIMARY]
- papers: Thermoelectric properties of Sn-doped CoSb3 prepared by encapsulated induction melting | Thermoelectric properties of SnzCo8Sb24 skutterudites | Ground state properties and thermoelectric behavior of PrFe/sub 4-x/TM/sub x/Sb/sub 12-y/Sn/sub y/ (TM = Co, Ni)

## Co-Sb-Sn-Ti
- rank 793 | 8 samples | 6 papers | 5 compositions
- compositions: TiCoSb0.8Sn0.2 (4); CoTi0.8Nb0.1Ta0.1Sb0.8Sn0.2 (1); TiCo1.03Sb0.8Sn0.2 (1); TiCo1.05Sb0.8Sn0.2 (1); TiCoSb0.75Sn0.25 (1)
- dopant candidates (<5% at.): Nb (1), Ta (1)
- measured range: 27-981 K (5th-95th pct of 37 curves)
- papers: High temperature thermoelectric properties of CoTiSb half-Heusler compounds | Fine tuning of thermoelectric performance in phase-separated half-Heusler compounds | Enhanced thermoelectric performance in the p-type half-Heusler (Ti/Zr/Hf)CoSb0.8Sn0.2 system via phase separation

## Co-Zn
- rank 794 | 8 samples | 3 papers | 6 compositions
- compositions: YbCo2Zn20 (3); YCo2Zn20 (1); YbCo1.86Ni0.14Zn20 (1); YbCo1.8Ni0.2Zn20 (1); YbCo1.9Ni0.1Zn20 (1); YbCo1.5Ni0.5Zn20 (1)
- dopant candidates (<5% at.): Yb (7), Ni (4), Y (1)
- measured range: 10-390 K (5th-95th pct of 26 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd(Zn10Co)2 Fd-3m (227) mp-1204825 [hull=0.000, icsd=1, PRIMARY]; U(Zn10Co)2 Fd-3m (227) mp-1202337 [hull=0.000, icsd=1, PRIMARY]; Zn11Co2 I-43m (217) mp-1192361 [hull=0.000, icsd=1, PRIMARY]; Zn13Co C2/m (12) mp-30568 [hull=0.000, icsd=1, PRIMARY]; Zr(Zn10Co)2 Fd-3m (227) mp-1195250 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric power of the YbT2Zn20(T=Fe, Ru, Os, Ir, Rh, and Co) heavy fermions | Enhanced thermoelectric performance of heavy-fermion compounds YbTM2Zn20 (TM = Co, Rh, Ir) at low temperatures | Effect of Ni Doping on the Thermoelectric Properties of YbCo2Zn20

## Cr-Cu-Te
- rank 795 | 8 samples | 1 papers | 8 compositions
- compositions: Cu1.3Cr2Te4 (1); Cu1.0Cr2Te4 (1); Cu1.1Cr2Te4 (1); Cu1.4Cr2Te4 (1); Cu1.5Cr2Te4 (1); Cu1.2Cr2Te4 (1)
- measured range: 16-341 K (5th-95th pct of 8 curves; full span incl. outliers 16-429 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cr2CuTe4 Fd-3m (227) mp-22625 [hull=0.000, icsd=3, PRIMARY]; Cr4Cu3Te8 Imm2 (44) mp-675546 [hull=0.021, PRIMARY]
- papers: Electronic transport properties of stuffed compositions of ferromagnetic copper chromium telluride: Cu1+xCr2Te4 (x=0–1)

## Cr-Mn-O-Y
- rank 796 | 8 samples | 3 papers | 6 compositions
- compositions: YMn0.5Cr0.5O3 (3); YCr0.6Mn0.4O3 (1); YCr0.5Mn0.5O3 (1); Y1.7La0.3MnCrO6 (1); Y1.6La0.2MnCrO6 (1); Y1.9La0.1MnCrO6 (1)
- dopant candidates (<5% at.): La (3)
- measured range: 25-301 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y2MnCrO6 P2_1/c (14) mp-1189214 [hull=0.016, icsd=2, PRIMARY]; YMnCrO5 Pbam (55) mp-1207744 [hull=0.034, PRIMARY]
- papers: Electrical conductivity anomaly and X-ray photoelectron spectroscopy investigation of YCr<sub>1−</sub><sub><i>x</i></sub>Mn<sub><i>x</i></sub>O<sub>3</sub> negative temperature coefficient ceramics | Effects of La-doping on the ferrimagnetism in double perovskite Y2MnCrO6 | Evolution of electric polarization and magnetic properties in half-Cr-doped YMnO3 films in response to epitaxial strain

## Cr-S
- rank 797 | 8 samples | 3 papers | 2 compositions
- compositions: Cr2S3 (4); Cr3S4 (4)
- measured range: 10-980 K (5th-95th pct of 16 curves)
- [ref 1] TEDesignLab / ICSD: CrS P6_3/mmc (194) mp-523 [hull=0.089, icsd=6, PRIMARY]; Cr3S4 C2/m (12) mp-1077959 [hull=0.019, icsd=4]; CrS (15); Cr2S3 (148)
- [ref 2] MP, ranked by ICSD evidence: Cr5S6 P-31c (163) mp-1311 [hull=0.021, icsd=6, PRIMARY]; Cr3S4 P2_1/m (11) mp-849071 [hull=0.000, icsd=5, PRIMARY]; Cr2S3 R3 (146) mp-849081 [hull=0.000, icsd=2, PRIMARY]; CrS2 C2/m (12) mp-849082 [hull=0.003, icsd=2, PRIMARY]; Cr5S8 Cm (8) mp-849084 [hull=0.000, icsd=1, PRIMARY]
- papers: Transport, thermoelectric, and magnetic properties of a dense Cr2S3 ceramic | Thermoelectric properties of chromium sulfo-selenides | About the Impact of Defect Phases on the Thermoelectric Properties of Cr\n            <sub>3</sub>\n            S\n            <sub>\n              4–\n              <i>x</i>\n            </sub>\n            Se\n            <sub>\n              <i>x</i>\n            </sub>

## Cu-Fe-Sb-Ti
- rank 798 | 8 samples | 2 papers | 8 compositions
- compositions: TiFeCu0.20Sb (1); TiFeCu0.25Sb (1); TiFe0.67Cu0.33Sb (1); TiFe0.70Cu0.32Sb (1); TiFe0.75Cu0.30Sb (1); TiFe0.80Cu0.28Sb (1)
- measured range: 323-966 K (5th-95th pct of 40 curves)
- papers: Structure and thermoelectric properties of half-Heusler-like TiFeCu Sb alloys | Strategic Design and Mechanistic Understanding of Vacancy‐Filling Heusler Thermoelectric Semiconductors

## Cu-O-Sr-Y
- rank 799 | 8 samples | 1 papers | 4 compositions
- compositions: YSr1.5Cu2.8Cr0.2O7 (2); Y0.8Ca0.2Sr1.5Cu2.8Cr0.2O7 (2); Y0.7Ca0.3Sr1.5Cu2.8Cr0.2O7 (2); Y0.8Ca0.2Sr1.6Ba0.4Cu2.7Ga0.3O7 (2)
- dopant candidates (<5% at.): Cr (6), Ca (6), Ba (2), Ga (2)
- measured range: 12-300 K (5th-95th pct of 8 curves; full span incl. outliers 12-346 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2YCu3O7 Pmmm (47) mp-985569 [hull=0.021, PRIMARY]; Sr3Y2FeCu3BiO12 Amm2 (38) mp-1218551 [hull=0.057, PRIMARY]; Sr6Y3Fe(Cu4O11)2 P2/m (10) mp-1218669 [hull=0.023, PRIMARY]; Sr8Y4Cu11CO28 Amm2 (38) mp-1173193 [hull=0.024, PRIMARY]; Sr3Y2FeCu3BiO12 P2_1/m (11) mp-1173223 [hull=0.237]
- papers: Comparison of carrier concentration determined by structural and electrical studies of cation substituted YSr2Cu3O7−δ

## Dy-Mn-O
- rank 800 | 8 samples | 4 papers | 5 compositions
- compositions: DyMnO3 (4); Dy0.9Eu0.1MnO3 (1); Dy0.9K0.1MnO3 (1); Dy0.8K0.2MnO3 (1); Dy0.9Bi0.1MnO3 (1)
- dopant candidates (<5% at.): K (2), Eu (1), Bi (1)
- measured range: 135-301 K (5th-95th pct of 8 curves; full span incl. outliers 135-1366 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DyMnO3 P6_3cm (185) mp-636982 [hull=0.000, icsd=2, PRIMARY]; DyMn2O5 Pbam (55) mp-25040 [hull=0.000, icsd=1, PRIMARY]; DyMn2O4 R-3m (166) mp-1096947 [hull=0.033, PRIMARY]; Dy2Mn2O7 Fd-3m (227) mp-779967 [hull=0.000, PRIMARY]; DyMnO3 Pnma (62) mp-25019 [hull=0.023, icsd=2]
- papers: Modification of low temperature magnetic interactions in Dy1−xEuxMnO3 | Effects of Dy sub lattice dilution on transport and magnetic properties in Dy1-xKxMnO3 | Role of trivalent bismuth ion substitution at Dy site on the physical properties of DyMnO3
