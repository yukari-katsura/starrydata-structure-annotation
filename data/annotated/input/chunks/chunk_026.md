# Host systems -- chunk 026 of 73

Ranks 1251-1300 by sample count. These 50 host systems cover 203 samples (0.39% of the TE set); cumulative through this chunk: 92.04%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## S-Zn
- rank 1251 | 5 samples | 2 papers | 2 compositions
- compositions: ZnS (4); Al0.02ZnS (1)
- dopant candidates (<5% at.): Al (1)
- measured range: 180-334 K (5th-95th pct of 9 curves; full span incl. outliers 180-380 K)
- [ref 1] TEDesignLab / ICSD: ZnS F-43m (216) mp-10695 [hull=0.000, icsd=26, PRIMARY]; ZnS2 Pa-3 (205) mp-1102743 [hull=0.000, icsd=1, PRIMARY]; ZnS P6_3mc (186) mp-9946 [hull=0.001, icsd=3]; ZnS R3m (160) mp-13456 [hull=0.002, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: ZnS P3m1 (156) mp-647075 [hull=0.000, icsd=1]
- papers: https://doi.org/10.1063/1.92170 (Electrical conductivity of Al‐implanted films of ZnS) | https://doi.org/10.7567/jjap.54.031203 (Photo-Seebeck effect in ZnS)

## Sb-Te-U
- rank 1252 | 5 samples | 3 papers | 1 compositions
- compositions: USbTe (5)
- sample form: SingleCrystal (5)
- measured range: 10-316 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): USbTe P4/nmm (129) mp-7935 [hull=0.142, icsd=2, PRIMARY]; U2SbTe R-3m (166) mp-1216679 [hull=0.208, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2005.02.042 (Electrical transport properties of USbSe and USbTe) | https://doi.org/10.1002/pssa.200306425 (Unusual transport properties of USbTe ferromagnet) | https://doi.org/10.1002/pssb.200562455 (Kondo phenomena of structural defects in USbTe ferromagnet)

## Zr
- rank 1253 | 5 samples | 4 papers | 2 compositions
- compositions: Zr (4); Zr97.5Er2.5 (1)
- dopant candidates (<5% at.): Er (1)
- sample form: Bulk (1)
- measured range: 291-1024 K (5th-95th pct of 5 curves; full span incl. outliers 291-1592 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zr P6_3/mmc (194) mp-131 [hull=0.000, icsd=17, PRIMARY]; Zr Im-3m (229) mp-41 [hull=0.084, icsd=4]; Zr Ibam (72) mp-1077723 [hull=0.020, icsd=1]; Zr Fm-3m (225) mp-8635 [hull=0.041, icsd=1]; Zr P6/mmm (191) mp-1056376 [hull=0.340, icsd=1]
- papers: https://doi.org/10.1007/bf00976954 (Thermoelectric properties of certain metals with a high melting point) | https://doi.org/10.1016/0022-3115(88)90127-4 (Thermophysical properties of uranium-zirconium alloys) | https://doi.org/10.3327/taesj.j14.040 (Phase State and Thermal and Mechanical Properties of Zr-Er Alloys)

## Ag-Al-Mg
- rank 1254 | 4 samples | 1 papers | 4 compositions
- compositions: Mg65Al20Ag15 (1); Mg75Al10Ag15 (1); Mg45Al40Ag15 (1); Mg35Al50Ag15 (1)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg32Al36Ag13 Im-3 (204) mp-31506 [hull=0.035, icsd=1, PRIMARY]; Mg16Al12Ag Cm (8) mp-1185647 [hull=0.027, PRIMARY]; Mg17Al11Ag Cm (8) mp-865489 [hull=0.027, PRIMARY]; MgAlAg Amm2 (38) mp-1222060 [hull=0.035, PRIMARY]; MgAlAg2 Fm-3m (225) mp-865919 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1143/jjap.27.l944 (New Icosahedral and Amorphous Phases in Mg-Al-Ag System Prepared by Li...)

## Ag-As-Ba
- rank 1255 | 4 samples | 1 papers | 4 compositions
- compositions: BaAgAs (1); BaAgAs0.97S0.03 (1); BaAgAs0.95Sb0.05 (1); BaAgAs0.95Bi0.05 (1)
- dopant candidates (<5% at.): S (1), Sb (1), Bi (1)
- sample form: Polycrystal (4)
- measured range: 303-974 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaAgAs P6_3/mmc (194) mp-7359 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1002/adfm.202100583 (Exceptional Performance Driven by Planar Honeycomb Structure in a New ...)

## Ag-Bi-Pb-Se
- rank 1256 | 4 samples | 1 papers | 4 compositions
- compositions: AgPbBiSe3 (1); AgPbBiSe2.98Br0.02 (1); AgPbBiSe2.97I0.03 (1); AgPbBiSe2.97Cl0.03 (1)
- dopant candidates (<5% at.): Br (1), I (1), Cl (1)
- sample form: Bulk (4)
- measured range: 296-818 K (5th-95th pct of 16 curves)
- papers: https://doi.org/10.1039/c9sc00485h (Bonding heterogeneity and lone pair induced anharmonicity resulted in ...)

## Ag-Ca-Co-O
- rank 1257 | 4 samples | 1 papers | 4 compositions
- compositions: Ag2Ca3Co4O9 (1); AgCa3Co4O9 (1); Ag1.6Ca3Co4O9 (1); Ag3.3Ca3Co4O9 (1)
- sample form: Bulk (4)
- measured range: 663-1034 K (5th-95th pct of 12 curves)
- papers: https://doi.org/10.1016/j.jallcom.2006.12.102 (Fabrication and thermoelectric properties of Ca3Co4O9/Ag composites)

## Ag-Cr-O
- rank 1258 | 4 samples | 1 papers | 4 compositions
- compositions: AgCr0.84Mg0.16O2 (1); AgCr0.88Mg0.12O2 (1); AgCr0.96Mg0.04O2 (1); AgCr0.92Mg0.08O2 (1)
- dopant candidates (<5% at.): Mg (4)
- measured range: 163-300 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CrAgO2 R-3m (166) mp-19378 [hull=0.000, icsd=2, PRIMARY]; Cr2Ag2O7 P-1 (2) mp-1172885 [hull=0.021, PRIMARY]; CrAgO4 Cmcm (63) mp-777097 [hull=0.000, PRIMARY]; CrAgO2 R3m (160) mp-1096875 [hull=0.092]; CrAgO4 P2_1/c (14) mp-850137 [hull=0.029]
- papers: https://doi.org/10.1039/c6tc04848j (Facile chemical solution synthesis of p-type delafossite Ag-based tran...)

## Ag-Ge-P
- rank 1259 | 4 samples | 1 papers | 4 compositions
- compositions: Ag6Ge10P12.05 (1); Ag6Ge10P12 (1); Ag6Ge10P12.03 (1); Ag6Ge10P12.1 (1)
- sample form: Bulk (1)
- measured range: 259-747 K (5th-95th pct of 20 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ag3Ge5P6 I-43m (217) mp-17862 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/acsami.9b17269 (Origin of High Thermoelectric Performance in Earth-Abundant Phosphide–...)

## Ag-Ge-Sb-Se
- rank 1260 | 4 samples | 2 papers | 4 compositions
- compositions: GeAg0.3Sb0.3Se1.6 (1); GeAg0.15Sb0.15Se1.3 (1); GeAg0.2Sb0.2Se1.4 (1); (GeSe)0.85(AgSbSe2)0.15 (1)
- sample form: Bulk (1)
- measured range: 296-718 K (5th-95th pct of 17 curves)
- papers: https://doi.org/10.1002/anie.201708134 (High Thermoelectric Performance of New Rhombohedral Phase of GeSe stab...) | https://doi.org/10.1002/adma.202300893 (Doping by Design: Enhanced Thermoelectric Performance of GeSe Alloys T...)

## Ag-Ge-Sb-Se-Te
- rank 1261 | 4 samples | 2 papers | 4 compositions
- compositions: (GeTe)75(AgSbTe2)18.75(AgSbSe2)6.25 (1); GeSeAg0.3Sb0.3Te0.6 (1); GeSeAg0.15Sb0.15Te0.3 (1); GeSeAg0.2Sb0.2Te0.4 (1)
- sample form: Polycrystal (3); Bulk (1)
- solid-solution axis: Se/(Se+Te) spans 0.10-0.77 (median 0.71) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 297-755 K (5th-95th pct of 19 curves)
- papers: https://doi.org/10.1016/j.synthmet.2020.116606 (Preparation and characterization of nanostructured (GeTe)75(AgSbTe2)x(...) | https://doi.org/10.1039/c8ta01393d (Synergetic optimization of electronic and thermal transport for high-p...)

## Ag-H-Pd
- rank 1262 | 4 samples | 1 papers | 4 compositions
- compositions: Pd0.86Ag0.14H0.71 (1); Pd0.77Ag0.23H0.71 (1); Pd0.61Ag0.39H0.2 (1); Pd0.61Ag0.39H0.44 (1)
- measured range: 80-234 K (5th-95th pct of 4 curves; full span incl. outliers 80-298 K)
- papers: https://doi.org/10.1016/j.jallcom.2004.11.060 (Influence of hydrogen on electron transport of palladium alloyed with ...)

## Ag-K-Se
- rank 1263 | 4 samples | 1 papers | 1 compositions
- compositions: KAg3Se2 (4)
- sample form: Bulk (4)
- measured range: 10-823 K (5th-95th pct of 4 curves)
- [ref 1] TEDesignLab / ICSD: KAg3Se2 C2/m (12) mp-9782 [hull=0.000, icsd=1, PRIMARY]; KAgSe P4/nmm (129) mp-16236 [hull=0.000, icsd=1, PRIMARY]; K2Ag4Se3 (12) [PRIMARY]
- papers: https://doi.org/10.1021/jacs.8b04888 (Ag2Se to KAg3Se2: Suppressing Order–Disorder Transitions via Reduced D...)

## Ag-Mn
- rank 1264 | 4 samples | 1 papers | 4 compositions
- compositions: Ag92.63Mn7.37 (1); Ag92.43Mn7.57 (1); Ag88.86Mn11.14 (1); Ag85.42Mn14.58 (1)
- measured range: 76-947 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1063/1.1722342 (Thermoelectric Power and Electrical Resistivity of Dilute Alloys of Mn...)

## Ag-O-Sb
- rank 1265 | 4 samples | 2 papers | 1 compositions
- compositions: AgSbO3 (4)
- sample form: Bulk (4)
- measured range: 298-880 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ag3SbO4 P4_122 (91) mp-1202934 [hull=0.014, icsd=1, PRIMARY]; Ag7Sb9O25 R3m (160) mp-766328 [hull=0.052, PRIMARY]; AgSbO12 P4_2/n (86) mp-1215022 [hull=0.453, PRIMARY]; AgSbO3 C2 (5) mp-860791 [hull=0.044, PRIMARY]; AgSbO12 Fd-3m (227) mp-1214924 [hull=1.047]
- papers: https://doi.org/10.1016/j.jallcom.2009.12.190 (Thermoelectric properties of AgSbO3 with defect pyrochlore structure) | https://doi.org/10.1007/s11664-011-1525-0 (Microstructure and Thermoelectric Properties of AgSbO3 Ceramics Prepar...)

## Ag-S-Ti
- rank 1266 | 4 samples | 1 papers | 4 compositions
- compositions: Ag0.32TiS2 (1); Ag0.6TiS2 (1); Ag0.8TiS2 (1); Ag0.98TiS2 (1)
- measured range: 315-472 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti3AgS6 R-3 (148) mp-1217143 [hull=0.004, PRIMARY]; Ti6AgS12 C2/m (12) mp-675920 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/0167-2738(83)90153-4 (The thermoelectric power in solid solution electrodes: A disregarded p...)

## Ag-Sb-Sr
- rank 1267 | 4 samples | 1 papers | 4 compositions
- compositions: Sr1.02AgSb (1); SrAgSb (1); Sr1.01AgSb (1); Sr1.03AgSb (1)
- sample form: Bulk (4)
- measured range: 299-783 K (5th-95th pct of 24 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr(Ag2Sb)2 R-3m (166) mp-1077980 [hull=0.000, icsd=1, PRIMARY]; SrAgSb P6_3/mmc (194) mp-11217 [hull=0.211, icsd=1, PRIMARY]; Sr2AgSb Immm (71) mp-1095891 [hull=1.474, PRIMARY]
- papers: https://doi.org/10.1021/acs.chemmater.0c02317 (Promising Zintl-Phase Thermoelectric Compound SrAgSb)

## Al-Au-Tm
- rank 1268 | 4 samples | 2 papers | 2 compositions
- compositions: Au49Al36Tm15 (2); Au49Al34Tm17 (2)
- measured range: 11-874 K (5th-95th pct of 13 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TmAl7Au3 R-3c (167) mp-16627 [hull=0.000, icsd=1, PRIMARY]; TmAlAu Pnma (62) mp-1102248 [hull=0.000, icsd=1, PRIMARY]; TmAlAu2 Fm-3m (225) mp-972272 [hull=0.015, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2015.08.081 (Thermoelectric properties of Tsai-type Au–Al–RE (RE: Yb, Tm, Gd) quasi...) | https://doi.org/10.7566/jpsj.84.024721 (Localized Electron Magnetism in the Icosahedral Au–Al–Tm Quasicrystal ...)

## Al-Ce-Ni-Pd
- rank 1269 | 4 samples | 1 papers | 2 compositions
- compositions: CePd0.6Ni0.4Al (2); CePd0.8Ni0.2Al (2)
- sample form: SingleCrystal (4)
- measured range: 10-299 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/s0921-4526(01)01092-4 (Thermoelectric power of CePd1−xNixAl single crystals)

## Al-Ce-Pd
- rank 1270 | 4 samples | 1 papers | 2 compositions
- compositions: CePdAl (2); CePd0.9Ni0.1Al (2)
- dopant candidates (<5% at.): Ni (2)
- sample form: SingleCrystal (4)
- measured range: 10-290 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeAl3Pd2 P6/mmm (191) mp-4785 [hull=0.000, icsd=5, PRIMARY]; CeAlPd P-62m (189) mp-21158 [hull=0.000, icsd=4, PRIMARY]; Ce(AlPd)2 P4/nmm (129) mp-1078340 [hull=0.018, icsd=3, PRIMARY]; CeAlPd2 Pnma (62) mp-1106138 [hull=0.000, icsd=1, PRIMARY]; Ce2Al11Pd3 P4mm (99) mp-1226920 [hull=0.029, PRIMARY]
- papers: https://doi.org/10.1016/s0921-4526(01)01092-4 (Thermoelectric power of CePd1−xNixAl single crystals)

## Al-Co-Cu-Fe
- rank 1271 | 4 samples | 2 papers | 4 compositions
- compositions: Al65Cu20Co5Fe10 (1); Al65Cu20Co10Fe5 (1); Al65Cu20Co7.5Fe7.5 (1); Al65Cu20Co6Fe9 (1)
- measured range: 10-304 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/s0925-8388(97)00004-2 (Electron transport in Al65Cu20Co15−xFex quasicrystals) | https://doi.org/10.1007/bf02744767 (Electrical resistivity and point contact studies on Al-Pd-Mn icosahedr...)

## Al-Cr-Cu-Fe-Ni
- rank 1272 | 4 samples | 1 papers | 4 compositions
- compositions: Ni2CuCrFeAl1.5 (1); Ni2CuCrFeAl0.5 (1); Ni2CuCrFeAl1.0 (1); Ni2CuCrFeAl2.5 (1)
- sample form: Bulk (4)
- measured range: 10-1124 K (5th-95th pct of 24 curves)
- papers: https://doi.org/10.1088/2053-1591/ab7d5a (Thermoelectric behaviour with high lattice thermal conductivity of Nic...)

## Al-Cu-Fe-Si
- rank 1273 | 4 samples | 2 papers | 4 compositions
- compositions: Al53Cu25.5Fe12.5Si9 (1); Al65.9Cu7.5Fe17.0Si9.6 (1); Al65.2Cu8.0Fe17.0Si9.8 (1); Al64.5Cu8.0Fe17.1Si10.4 (1)
- measured range: 10-294 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1109/ict.2007.4569499 (Low thermal conductivity of Al-based icosahedral quasicrystals and app...) | https://doi.org/10.1103/physrevb.74.054206 (Extremely small thermal conductivity of the Al-based Mackay-type<mml:m...)

## Al-Cu-U
- rank 1274 | 4 samples | 1 papers | 4 compositions
- compositions: UCu4Al8 (1); UCu5Al7 (1); UCu5.75Al6.25 (1); UCu4.5Al7.5 (1)
- sample form: Bulk (4)
- measured range: 10-300 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U(Al2Cu)4 I4/mmm (139) mp-7248 [hull=0.011, icsd=2, PRIMARY]; U2AlCu3 P6_3/mmc (194) mp-7775 [hull=0.162, icsd=1, PRIMARY]; UAl5Cu6 Fddd (70) mp-1191305 [hull=0.000, icsd=1, PRIMARY]; UAl2Cu Fm-3m (225) mp-19872 [hull=0.455, icsd=1, PRIMARY]; U2Al3Cu7 P2/m (10) mp-1216892 [hull=0.096, PRIMARY]
- papers: https://doi.org/10.1016/j.physb.2011.01.038 (Non-Fermi-liquid behavior in UCu4+xAl8−x compounds)

## Al-Fe-Mn
- rank 1275 | 4 samples | 2 papers | 2 compositions
- compositions: Al72.5Mn21.5Fe6.0 (3); Fe2MnAl (1)
- measured range: 10-354 K (5th-95th pct of 8 curves; full span incl. outliers 10-823 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnAlFe2 Fm-3m (225) mp-31185 [hull=0.000, icsd=1, PRIMARY]; MnAl12Fe Amm2 (38) mp-1221672 [hull=0.000, PRIMARY]; MnAl2Fe Immm (71) mp-1093629 [hull=2.699, PRIMARY]; MnAlFe2 F-43m (216) mp-1221620 [hull=0.047]
- papers: https://doi.org/10.1080/14786435.2010.511595 (Anisotropic transport properties of the Al13TM4and T-Al–Mn–Fe complex ...) | https://doi.org/10.1134/s1063783415040149 (Specific features of the properties of half-metallic ferromagnetic Heu...)

## Al-Fe-Ni-O
- rank 1276 | 4 samples | 1 papers | 4 compositions
- compositions: NiAlFeO4 (1); NiAl0.4Fe1.6O4 (1); NiAl0.6Fe1.4O4 (1); NiAl0.8Fe1.2O4 (1)
- measured range: 308-832 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/j.matlet.2006.03.139 (Electrical conduction in Ni–Al ferrites)

## Al-Hg-Se
- rank 1277 | 4 samples | 1 papers | 4 compositions
- compositions: (Hg3Se)0.5(Al2Se3)0.5Mn0.0015 (1); (Hg3Se)0.7(Al2Se3)0.3Mn0.001 (1); (Hg3Se)0.5(Al2Se3)0.5Mn0.001 (1); (Hg3Se)0.5(Al2Se3)0.5Mn0.0011 (1)
- dopant candidates (<5% at.): Mn (4)
- measured range: 76-299 K (5th-95th pct of 4 curves)
- [ref 1] TEDesignLab / ICSD: Al2HgSe4 I-4 (82) mp-3038 [hull=0.000, icsd=4, PRIMARY]; Al2HgSe4 Fd-3m (227) mp-1103510 [hull=0.048, icsd=2]
- [ref 2] MP, ranked by ICSD evidence: Al2Hg5Se8 P1 (1) mp-685952 [hull=0.025, PRIMARY]
- papers: https://doi.org/10.1134/s0020168510050043 (Electrical and optical properties of manganese-doped (3HgSe)1 − x (Al2...)

## Al-Mg-Sb
- rank 1278 | 4 samples | 1 papers | 1 compositions
- compositions: Mg5Al2Sb6 (4)
- sample form: Bulk (4)
- measured range: 19-302 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg(AlSb)2 P-3m1 (164) mp-1232396 [hull=0.233, PRIMARY]; Mg14AlSb P-6m2 (187) mp-1028232 [hull=0.041, PRIMARY]; Mg16Al12Sb R3m (160) mp-1185708 [hull=0.063, PRIMARY]; Mg6AlSb Amm2 (38) mp-1023281 [hull=0.098, PRIMARY]; Mg14AlSb Amm2 (38) mp-1028233 [hull=0.059]
- papers: https://doi.org/10.1007/s10854-014-2500-3 (Thermoelectric and mechanical properties of Mg–Al–Sb alloys)

## Al-N-Ta
- rank 1279 | 4 samples | 1 papers | 1 compositions
- compositions: TaAlN (4)
- measured range: 306-772 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ta4AlN3 P6_3/mmc (194) mp-1188888 [hull=0.185, icsd=1, PRIMARY]
- papers: https://doi.org/10.3131/jvsj.50.173 (Fabrication of High TCR TaAl-N Thin Film by Reactive Sputtering Method)

## Al-Ru-Si
- rank 1280 | 4 samples | 2 papers | 4 compositions
- compositions: Al67.2Si9.2Ru23.6 (1); Al67.63Si8.2Ru24.2_IAC_1_0 (1); Al67.5Si7.5Cu2Ru23_IAC_1_0 (1); Al65.6Si8.1Cu4.1Ru22.1_IAC_1_0 (1)
- dopant candidates (<5% at.): Cu (2)
- measured range: 300-811 K (5th-95th pct of 13 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlSiRu2 Fm-3m (225) mp-862778 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevmaterials.3.061601 (Experimental realization of a semiconducting quasicrystalline approxim...) | https://doi.org/10.1103/physrevmaterials.5.125401 (Effects of Cu doping on thermoelectric properties of Al–Si–Ru semicond...)

## Al-Sb-Zn
- rank 1281 | 4 samples | 2 papers | 4 compositions
- compositions: (AlSb)0.9(Zn4Sb3)0.1 (1); (AlSb)0.8(Zn4Sb3)0.2 (1); (AlSb)0.7(Zn4Sb3)0.3 (1); (Al0.995Mg0.005Sb)0.9(Zn4Sb3)0.1 (1)
- dopant candidates (<5% at.): Mg (1)
- sample form: Bulk (4)
- measured range: 306-858 K (5th-95th pct of 19 curves)
- papers: https://doi.org/10.1016/j.mssp.2020.104974 (Composite fabrication for improvement of thermoelectric properties in ...) | https://doi.org/10.1007/s13391-020-00241-0 (Improvement of Thermoelectric Properties of AlSb by Incorporation of M...)

## Al-Y
- rank 1282 | 4 samples | 4 papers | 2 compositions
- compositions: YAl2 (3); YAl3 (1)
- measured range: 10-499 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YAl2 Fd-3m (227) mp-2322 [hull=0.000, icsd=18, PRIMARY]; YAl3 R-3m (166) mp-2451 [hull=0.002, icsd=7, PRIMARY]; Y3Al2 P4_2/mnm (136) mp-16723 [hull=0.005, icsd=4, PRIMARY]; YAl Cmcm (63) mp-1064953 [hull=0.008, icsd=3, PRIMARY]; Y2Al Pnma (62) mp-11230 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/s0921-4526(97)00157-9 (Transport phenomena in spin fluctuations systems) | https://doi.org/10.1088/0953-8984/7/33/008 (The transport properties of RCo2compounds) | https://doi.org/10.1016/0022-5088(85)90212-7 (Electrical resistivity, thermal conductivity and thermopower of nonmag...)

## As-Cu-Te
- rank 1283 | 4 samples | 1 papers | 4 compositions
- compositions: Cu30As15Te55 (1); Cu20As25Te55 (1); Cu25As20Te55 (1); Cu35As10Te55 (1)
- sample form: Ribbon (4)
- measured range: 101-299 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuTeAs Pnma (62) mp-1184180 [hull=0.027, PRIMARY]
- papers: https://doi.org/10.1007/s11664-010-1486-8 (Chalcogenide Glasses as Prospective Thermoelectric Materials)

## As-F-Fe-La-O
- rank 1284 | 4 samples | 2 papers | 2 compositions
- compositions: LaFeAsO0.8F0.2 (3); LaAsFeO0.775F0.225 (1)
- measured range: 10-299 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1016/j.jallcom.2010.08.138 (Electrical transport properties of F-doped LaFeAsO oxypnictide) | https://doi.org/10.1143/jpsj.79.094702 (Superconducting Transition Temperatures and Transport Properties of La...)

## As-F-Fe-O-Sm
- rank 1285 | 4 samples | 2 papers | 2 compositions
- compositions: SmFeAsO0.8F0.2 (3); SmAsFeO0.8F0.2 (1)
- sample form: Bulk (3)
- measured range: 11-294 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sm6Fe6As6O5F P2_1/m (11) mp-697821 [hull=0.169, PRIMARY]
- papers: https://doi.org/10.1016/j.physc.2015.06.015 (Thermoelectric properties of FeAs based superconductors, with thick pe...) | https://doi.org/10.1103/physrevb.79.212502 (Evidence of spin-density-wave order inRFeAsO1−xFxfrom measurements of ...)

## As-Fe-H-La-O
- rank 1286 | 4 samples | 1 papers | 4 compositions
- compositions: LaFeAs1O0.75H0.25 (1); LaFeAs0.8P0.1O0.90H0.30 (1); LaFeAs0.9P0.1O0.75H0.25 (1); LaFeAsO0.70H0.30 (1)
- dopant candidates (<5% at.): P (2)
- measured range: 12-297 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1103/physrevb.95.214515 (Three superconducting phases with different categories of pairing in h...)

## As-Fe-K
- rank 1287 | 4 samples | 2 papers | 4 compositions
- compositions: K0.87Sr0.13Fe2As2 (1); Ba0.2K0.8Fe2As2 (1); Ba0.1K0.9Fe2As2 (1); KFe2As2 (1)
- dopant candidates (<5% at.): Ba (2), Sr (1)
- sample form: SingleCrystal (3); Polycrystal (1)
- measured range: 12-300 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): K(FeAs)2 I4/mmm (139) mp-675576 [hull=0.000, icsd=2, PRIMARY]; KFeAs2 I-4m2 (119) mp-1223459 [hull=0.268, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.79.104504 (Evidence of quantum criticality in the phase diagram ofKxSr1−xFe2As2fr...) | https://doi.org/10.1103/physrevb.81.235107 (Thermoelectric properties of electron- and hole-dopedBaFe2As2)

## As-Fe-La-Mn-O
- rank 1288 | 4 samples | 1 papers | 4 compositions
- compositions: LaFe0.5Mn0.5AsO0.89Fe0.11 (1); LaFe0.8Mn0.2AsO0.89Fe0.11 (1); LaFe0.3Mn0.7AsO0.89Fe0.11 (1); LaFe0.2Mn0.8AsO0.89Fe0.11 (1)
- sample form: Polycrystal (4)
- measured range: 10-298 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1143/jpsj.79.014710 (Studies on Effects of Impurity Doping and NMR Measurements of La 1111 ...)

## As-Ga-Mn
- rank 1289 | 4 samples | 1 papers | 1 compositions
- compositions: GaMnAs (4)
- measured range: 10-293 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1063/1.2108131 (Resistivity minima and Kondo effect in ferromagnetic GaMnAs films)

## As-Ge
- rank 1290 | 4 samples | 1 papers | 2 compositions
- compositions: GeAs (3); Sn0.08Ge0.92As (1)
- dopant candidates (<5% at.): Sn (1)
- sample form: Bulk (3)
- measured range: 10-663 K (5th-95th pct of 20 curves; full span incl. outliers 10-726 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GeAs2 Pbam (55) mp-17524 [hull=0.000, icsd=3, PRIMARY]; GeAs C2/m (12) mp-9548 [hull=0.000, icsd=2, PRIMARY]; Ge3As Fm-3m (225) mp-1184561 [hull=0.363, PRIMARY]; GeAs3 R3m (160) mp-1224319 [hull=0.097, PRIMARY]; GeAs I4mm (107) mp-7591 [hull=0.096, icsd=1]
- papers: https://doi.org/10.1021/acs.chemmater.6b00567 (GeAs: Highly Anisotropic van der Waals Thermoelectric Material)

## As-Ge-Re
- rank 1291 | 4 samples | 2 papers | 2 compositions
- compositions: Re3GeAs6 (2); Re3Ge0.6As6.4 (2)
- sample form: Bulk (2)
- measured range: 10-989 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ReGeAs C2/m (12) mp-1219536 [hull=0.008, PRIMARY]
- papers: https://doi.org/10.1021/cm0708517 (Thermoelectric Properties of Re3Ge0.6As6.4and Re3GeAs6in Comparison to...) | https://doi.org/10.1007/s11664-008-0623-0 (New Ternary Arsenides for High-Temperature Thermoelectric Applications)

## As-Ge-Sb-Se
- rank 1292 | 4 samples | 1 papers | 4 compositions
- compositions: As14Ge14Se66Sb6 (1); As14Ge14Se63Sb9 (1); As14Ge14Se60Sb12 (1); As14Ge14Se57Sb15 (1)
- sample form: Bulk (4)
- solid-solution axis: As/(As+Sb) spans 0.48-0.70 (median 0.61) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 300-450 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1039/c5dt02047f (Semiconducting quaternary chalcogenide glasses as new potential thermo...)

## As-La-O-Zn
- rank 1293 | 4 samples | 1 papers | 4 compositions
- compositions: La0.975Sr0.025ZnAsO (1); LaZnAsO (1); La0.95Sr0.05ZnAsO (1); La0.925Sr0.075ZnAsO (1)
- dopant candidates (<5% at.): Sr (3)
- sample form: Bulk (4)
- measured range: 310-774 K (5th-95th pct of 20 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2ZnAs2O P4/mmm (123) mp-1211347 [hull=1.373, PRIMARY]; LaZn2AsO2 P4/mmm (123) mp-1206306 [hull=1.150, PRIMARY]
- papers: https://doi.org/10.1007/s11664-020-08439-6 (Thermoelectric Properties of La1-xSrxZnAsO)

## As-Na-Zn
- rank 1294 | 4 samples | 1 papers | 4 compositions
- compositions: NaZn3.98Cu0.02As3 (1); NaZn3.96Cu0.04As3 (1); NaZn3.94Cu0.06As3 (1); NaZn4As3 (1)
- dopant candidates (<5% at.): Cu (3)
- sample form: Bulk (4)
- measured range: 10-280 K (5th-95th pct of 20 curves)
- [ref 1] TEDesignLab / ICSD: NaZnAs P4/nmm (129) mp-13097 [hull=0.000, icsd=2, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: NaZn4As3 R-3m (166) mp-1078703 [hull=0.000, icsd=1, PRIMARY]; NaZnAs F-43m (216) mp-34240 [hull=0.130]
- papers: https://doi.org/10.1016/j.jssc.2020.121588 (Thermoelectric properties of NaZn4-Cu As3 crystalized in the rhombohed...)

## As-Nd-O-Sb-Se
- rank 1295 | 4 samples | 1 papers | 2 compositions
- compositions: NdO0.8F0.2Sb0.6As0.4Se2 (2); NdO0.8F0.2Sb0.4As0.6Se2 (2)
- dopant candidates (<5% at.): F (4)
- measured range: 298-673 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.3390/ma13092164 (Crystal Structure and Thermoelectric Transport Properties of As-Doped ...)

## As-Sb-Th
- rank 1296 | 4 samples | 1 papers | 4 compositions
- compositions: Th3(As0.9Sb0.1)4 (1); Th3(As0.75Sb0.25)4 (1); Th3(As0.25Sb0.75)4 (1); Th3(As0.1Sb0.9)4 (1)
- sample form: compact (4)
- solid-solution axis: As/(As+Sb) spans 0.10-0.90 (median 0.75) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 287-1218 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Th3(SbAs)2 I2_13 (199) mp-1217386 [hull=0.041, PRIMARY]
- papers: https://doi.org/10.1149/1.2423585 (Some X-Ray and Thermoelectric Studies on Cubic Th[sub 3]X[sub 4] Compo...)

## As-U
- rank 1297 | 4 samples | 2 papers | 2 compositions
- compositions: U3As4 (2); UAs2 (2)
- measured range: 10-299 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UAs Fm-3m (225) mp-2104 [hull=0.000, icsd=14, PRIMARY]; UAs2 P4/nmm (129) mp-1657 [hull=0.000, icsd=4, PRIMARY]; U3As4 I-43d (220) mp-606 [hull=0.000, icsd=4, PRIMARY]; U2As3 P4/mmm (123) mp-1207355 [hull=3.815, PRIMARY]; UAs Pm-3m (221) mp-21087 [hull=0.135, icsd=1]
- papers: https://doi.org/10.1063/1.2737904 (Giant anisotropic magnetoresistance and magnetothermopower in cubic 3:...) | https://doi.org/10.1016/s0921-4526(01)01337-0 (A Kondo-like thermoelectric power behaviour of UAsSe ferromagnet)

## Au-Fe
- rank 1298 | 4 samples | 1 papers | 1 compositions
- compositions: AuFe (4)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe3Au I4/mmm (139) mp-1184272 [hull=0.137, PRIMARY]; FeAu R-3m (166) mp-1224962 [hull=0.247, PRIMARY]; FeAu3 Fm-3m (225) mp-973557 [hull=0.158, PRIMARY]; Fe3Au P6_3/mmc (194) mp-1184413 [hull=0.152]
- papers: https://doi.org/10.1007/bf00681768 (Absolute thermoelectric power ofAuFe alloys between 0.01 K and 7 K)

## Au-Mn
- rank 1299 | 4 samples | 2 papers | 4 compositions
- compositions: Au86.91Mn13.01 (1); Au81.36Mn18.64 (1); Au93.17Mn6.83 (1); Au0.9Mn0.1 (1)
- measured range: 15-945 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnAu2 I4/mmm (139) mp-11252 [hull=0.000, icsd=4, PRIMARY]; Mn2Au I4/mmm (139) mp-30409 [hull=0.235, icsd=2, PRIMARY]; MnAu4 I4/m (87) mp-12565 [hull=0.000, icsd=2, PRIMARY]; Mn2Au5 C2/m (12) mp-30410 [hull=0.016, icsd=2, PRIMARY]; MnAu P4/mmm (123) mp-12675 [hull=0.071, icsd=1, PRIMARY, AMBIGUOUS]
- papers: https://doi.org/10.1063/1.1722342 (Thermoelectric Power and Electrical Resistivity of Dilute Alloys of Mn...) | https://doi.org/10.1063/1.1729605 (Effects of Transition Metal Solutes on the Thermoelectric Power of Cop...)

## B-Ba
- rank 1300 | 4 samples | 2 papers | 3 compositions
- compositions: BaB6 (2); Ca0.25Ba0.75B6 (1); Sr0.25Ba0.75B6 (1)
- dopant candidates (<5% at.): Ca (1), Sr (1)
- measured range: 306-1075 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaB6 Pm-3m (221) mp-954 [hull=0.000, icsd=7, PRIMARY]; Ba3NaB24 P4/mmm (123) mp-1228056 [hull=0.009, PRIMARY]; Ba3SmB24 P4/mmm (123) mp-1228060 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2014.10.001 (High-pressure densified solid solutions of alkaline earth hexaborides ...) | https://doi.org/10.1109/ict.2003.1287498 (Thermoelectric properties of divalent hexaborides)
