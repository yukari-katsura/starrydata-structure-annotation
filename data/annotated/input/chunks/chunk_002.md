# Host systems -- chunk 002 of 73

Ranks 51-100 by sample count. These 50 host systems cover 5621 samples (10.80% of the TE set); cumulative through this chunk: 57.79%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Ba-Ga-Ge
- rank 51 | 173 samples | 45 papers | 79 compositions
- compositions: Ba8Ga16Ge30 (82); Ba24Ga12Ge88 (3); Ba8Ga16Ge20 (3); Ba24Ga15Ge85 (2); Ba8Ga16Zn2.6Ge27.4 (2); Ba8Ga12Ge34 (2)
- dopant candidates (<5% at.): Ni (11), Zn (11), Yb (7), O (4), Ti (4), Pt (3), In (3), Au (2), Al (2), Sb (2), Cu (2), Ag (1), Eu (1)
- seed hypothesis (confirm): clathrate_i
- sample form: Bulk (35); SingleCrystal (1)
- measured range: 13-1026 K (5th-95th pct of 465 curves; full span incl. outliers 10-1175 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaGaGe P6_3/mmc (194) mp-1102026 [hull=0.000, icsd=1, PRIMARY]; Ba4Ga3Ge20 Pm-3n (223) mp-1214614 [hull=0.019, PRIMARY]; BaGaGe P-6m2 (187) mp-1227942 [hull=0.002]
- papers: https://doi.org/10.1021/acsami.5b04910 (Thermoelectric Properties of Ga/Ag Codoped Type-III Ba24Ge100Clathrate...) | https://doi.org/10.1016/j.actamat.2005.12.032 (High thermoelectric performance of type-III clathrate compounds of the...) | https://doi.org/10.1002/adfm.200901817 (On the Design of High-Efficiency Thermoelectric Clathrates through a S...)

## Ge-Sb-Te
- rank 52 | 173 samples | 46 papers | 107 compositions
- compositions: Ge2Sb2Te5 (19); (GeTe)17Sb2Te3 (6); (CoGe2)0.15(GeTe)12Sb2Te3 (6); (GeTe)12Sb2Te3 (6); (CoGe2)0.2(GeTe)17Sb2Te3 (6); Ge4SbTe5 (4)
- dopant candidates (<5% at.): Co (16), In (13), Ag (11), Al (8), Bi (6), I (4), Se (4), S (3), Zn (3), Y (2), Cu (1), Cd (1), Sn (1), Cr (1), Ta (1)
- seed hypothesis (confirm): gst_homologous
- sample form: Bulk (92); Film (14); Polycrystal (8); Other (5); Ribbon (4)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 293-826 K (5th-95th pct of 695 curves; full span incl. outliers 10-924 K)
  !! MEASUREMENT CROSSES A TRANSITION: gst_homologous -> rocksalt at ~420 K (Amorphous -> metastable cubic, ~420 K; cubic -> stable layered above ~500 K.)
     Record each phase with its own temperature range, not a single prototype.
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ge2Sb2Te5 P-3m1 (164) mp-1224375 [hull=0.572, icsd=2, PRIMARY]; GeSb4Te7 P-3m1 (164) mp-29641 [hull=0.850, icsd=1, PRIMARY]; Ge(SbTe2)2 R3m (160) mp-1224350 [hull=0.732, PRIMARY]; Ge(SbTe)4 P-3m1 (164) mp-1224378 [hull=0.768, PRIMARY]; Ge13Sb13Te32 P1 (1) mp-1120824 [hull=0.624, PRIMARY]
- papers: https://doi.org/10.1063/1.4893236 (Enhanced thermoelectric performance of In-substituted GeSb6Te10 with h...) | https://doi.org/10.1007/s00339-007-4006-9 (Microstructures and thermoelectric properties of GeSbTe based layered ...) | https://doi.org/10.1002/chem.201102331 (Elemental Distribution and Thermoelectric Properties of Layered Tellur...)

## Cu-S-Sb
- rank 53 | 156 samples | 34 papers | 102 compositions
- compositions: Cu12Sb4S13 (33); Cu3SbS4 (4); Cu3Sb0.89Bi0.06Sn0.05S4 (4); Cu10Cu2Sb4S13 (3); Cu11.5Zn0.5Sb4S13 (2); Cu11.5Co0.5Sb4S13 (2)
- dopant candidates (<5% at.): Te (27), Bi (19), Zn (18), Sn (15), Se (14), Ni (10), Ge (10), Co (9), Ag (8), Mn (7), In (4), Fe (3), As (2), Hg (1)
- seed hypothesis (confirm): tetrahedrite
- sample form: Bulk (71); Other (7); Polycrystal (5); SingleCrystal (4)
- measured range: 16-727 K (5th-95th pct of 645 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu12Sb4S13 I-43m (217) mp-647164 [hull=0.000, icsd=7, PRIMARY]; CuSbS2 Pnma (62) mp-4468 [hull=0.000, icsd=6, PRIMARY]; Cu3SbS4 I-42m (121) mp-5702 [hull=0.000, icsd=5, PRIMARY]; Cu3SbS3 I-43m (217) mp-647606 [hull=0.040, icsd=2, PRIMARY]; Cu11Sb4S13 Cm (8) mp-676076 [hull=0.069, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2015.08.040 (Thermoelectric properties of Co substituted synthetic tetrahedrite) | https://doi.org/10.1002/aenm.201200650 (High Performance Thermoelectricity in Earth-Abundant Compounds Based o...) | https://doi.org/10.1143/apex.5.051201 (Thermoelectric Properties of Mineral Tetrahedrites Cu$_{10}$Tr$_{2}$Sb...)

## Bi-Ca-Cu-O-Sr
- rank 54 | 155 samples | 47 papers | 68 compositions
- compositions: Bi2Sr2CaCu2O8 (50); Bi1.75Pb0.35Sr2Ca2Cu3O10 (14); (Bi0.8Pb0.2)2Sr2Ca2Cu3O10 (4); Bi1.65Pb0.35Sr2Ca2Cu3O10 (4); BiSr2Ca2.4Cu3.1O8 (4); (Bi0.8Pb0.2)4Sr3Ca3Cu4O11 (4)
- dopant candidates (<5% at.): Pb (58), Ce (7), V (5), Na (5), Nd (5), Y (4), Gd (3), K (3), Ag (3), Si (3), Yb (3), Al (3), Au (2), Er (1), Ba (1)
- seed hypothesis (confirm): bscco_cuprate
- sample form: Bulk (68); SingleCrystal (16); Polycrystal (4); Film (3); Powder (2)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- solid-solution axis: Ca/(Ca+Sr) spans 0.29-0.60 (median 0.50) over 68 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 11-308 K (5th-95th pct of 218 curves; full span incl. outliers 10-1110 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2Ca3Cu4(BiO6)2 I4/mmm (139) mp-1191679 [hull=0.051, icsd=1, PRIMARY]; Sr10Ca4Cu10Bi11O40 I4/m (87) mp-1218959 [hull=0.094, PRIMARY]; Sr2Ca2Cu3(BiO5)2 I4/mmm (139) mp-1209015 [hull=0.051, PRIMARY]; Sr2Ca2Cu3BiO8 Fmmm (69) mp-1173287 [hull=0.162, PRIMARY]; Sr2CaCu2(BiO4)2 Ccc2 (37) mp-1218930 [hull=0.037, PRIMARY]
- papers: https://doi.org/10.1007/s10909-006-9296-3 (Thermoelectric Power and Thermal Conduction Studies on the Gd Substitu...) | https://doi.org/10.1007/s10948-008-0315-2 (A Study on Thermoelectric Power and Electrical Properties of Bi-2223 S...) | https://doi.org/10.1007/s10948-008-0317-0 (Thermoelectric Properties of Bi-2223 Superconductors at Different Cond...)

## In-O-Zn
- rank 55 | 153 samples | 23 papers | 73 compositions
- compositions: (ZnO)5In2O3 (15); In2O3(ZnO)5 (14); (In2O3)70.99(ZnO)29.01 (13); (ZnO)7In2O3 (8); (ZnO)6.0In2O3 (5); In2O3(ZnO)9 (5)
- dopant candidates (<5% at.): Al (25), Ga (14), Y (8), Ce (8), Ti (3), Ca (1), Mg (1)
- seed hypothesis (confirm): homologous_inmo3_zno
- sample form: Bulk (30); Polycrystal (8)
- measured range: 15-1248 K (5th-95th pct of 251 curves; full span incl. outliers 10-1324 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZnIn2O4 Fd-3m (227) mp-756297 [hull=0.029, icsd=1, PRIMARY]; Zn2In2O5 P6_3mc (186) mp-1094040 [hull=0.084, PRIMARY]; Zn3In2O6 P1 (1) mp-682284 [hull=0.036, PRIMARY, AMBIGUOUS]; Zn4In2O7 P6_3/mmc (194) mp-1216040 [hull=0.067, PRIMARY]; ZnIn2O4 Pnma (62) mp-770218 [hull=0.070]
- papers: https://doi.org/10.1016/j.ceramint.2011.06.068 (Synthesis and post-annealing effects on the transport properties of th...) | https://doi.org/10.1007/s13391-013-0025-1 (A study of electrodes for thermoelectric oxides) | https://doi.org/10.1143/jjap.43.7133 (Thermoelectric Properties of Highly Textured Ca-Doped (ZnO)mIn2O3Ceramics)

## Cr-Si
- rank 56 | 146 samples | 37 papers | 60 compositions
- compositions: CrSi2 (60); Cr0.33Si0.67 (8); Cr0.28Si0.72 (5); Cr0.35Si0.65 (3); Cr0.95Nb0.05Si2 (3); Cr0.9Nb0.1Si2 (2)
- dopant candidates (<5% at.): Nb (11), Mn (8), Al (7), Mo (7), W (6), Ta (5), Cu (4), Ti (3), V (3), Ge (2), Ne (2)
- seed hypothesis (confirm): crsi2_c40
- sample form: Film (22); Bulk (10)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 79-1068 K (5th-95th pct of 273 curves; full span incl. outliers 13-1298 K)
- [ref 1] TEDesignLab / ICSD: CrSi2 P6_222 (180) mp-1222 [hull=0.011, icsd=9, PRIMARY]; CrSi2 P6_422 (181) mp-11191 [hull=0.011, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: Cr3Si Pm-3n (223) mp-729 [hull=0.000, icsd=15, PRIMARY]; CrSi P2_13 (198) mp-7576 [hull=0.069, icsd=4, PRIMARY]; Cr5Si3 I4/mcm (140) mp-7506 [hull=0.041, icsd=3, PRIMARY]; Cr3Si5 I4/mcm (140) mp-1105936 [hull=0.527, icsd=1, PRIMARY]; CrSi2 I4/mmm (139) mp-8937 [hull=0.000, icsd=1]
- papers: https://doi.org/10.1007/s13391-015-4475-5 (Formation and thermoelectric properties of Si/CrSi2/Si(001) heterostru...) | https://doi.org/10.1016/j.jallcom.2007.06.129 (Role of milling parameters and impurity on the thermoelectric properti...) | https://doi.org/10.1007/s11664-013-2510-6 (Effect of Composition on Thermoelectric Properties of Polycrystalline ...)

## In-Se
- rank 57 | 145 samples | 38 papers | 91 compositions
- compositions: In4Se3 (29); In4Se2.35 (7); InSe (5); In4Se2.5 (4); In0.99Si0.01Se (3); In2Se3 (3)
- dopant candidates (<5% at.): Sn (19), Si (14), Cu (13), Cl (11), Pb (11), Te (7), Yb (5), Fe (3), Br (3), I (3), Na (1), Ca (1), Zn (1), Ga (1), O (1), Sr (1), Ti (1), Ba (1), F (1)
- seed hypothesis (confirm): layered_in2se3, in4se3  <-- MIXED, split per composition
- sample form: Bulk (110); Film (1)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 291-795 K (5th-95th pct of 648 curves; full span incl. outliers 10-906 K)
- [ref 1] TEDesignLab / ICSD: InSe R3m (160) mp-22691 [hull=0.000, icsd=8, PRIMARY]; In4Se3 Pnnm (58) mp-19932 [hull=0.018, icsd=7, PRIMARY]; In6Se7 P2_1/m (11) mp-1192955 [hull=0.044, icsd=2, PRIMARY]; InSe P6_3/mmc (194) mp-20485 [hull=0.001, icsd=5]; InSe P-6m2 (187) mp-1079260 [hull=0.005, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: In2Se3 R-3m (166) mp-1068548 [hull=0.522, icsd=5, PRIMARY]; In2Se Pnnm (58) mp-627397 [hull=0.107, icsd=1, PRIMARY]; In23Se28 Cm (8) mp-1225539 [hull=0.048, PRIMARY]; InSe C2/m (12) mp-21405 [hull=0.036, icsd=2]; In2Se3 P-3m1 (164) mp-1017565 [hull=0.050, icsd=1]
- papers: https://doi.org/10.1016/j.actamat.2015.08.062 (The roles of Yb-substitution on thermoelectric properties of In4−xYbxSe3) | https://doi.org/10.1002/adma.201004739 (Enhancement of the Thermoelectric Figure-of-Merit in a Wide Temperatur...) | https://doi.org/10.1063/1.3266579 (Thermoelectric properties and anisotropic electronic band structure on...)

## Al-Pd-Re
- rank 58 | 142 samples | 31 papers | 68 compositions
- compositions: Al70.5Pd21Re8.5 (21); Al70Re10Pd20 (11); Al70Pd22.5Re7.5 (10); Al71Pd20Re9 (9); Al70Pd20Re10 (9); Al70Re8.6Pd21.4 (6)
- dopant candidates (<5% at.): Ga (16), Ru (5), Fe (4), Mn (4), Co (4)
- seed hypothesis (confirm): quasicrystal_approximant
- sample form: Bulk (44)
- measured range: 10-994 K (5th-95th pct of 251 curves; full span incl. outliers 10-1241 K)
- papers: https://doi.org/10.1063/1.1611636 (Effect of Ru substitution for Re on the thermoelectric properties of A...) | https://doi.org/10.1063/1.2716212 (Improvement of thermoelectric properties of icosahedral AlPdRe quasicr...) | https://doi.org/10.1007/s11664-009-1065-z (Thermoelectric Properties of Icosahedral Al-Pd-(Mn or Re) Quasicrystal...)

## Bi-Mg-Sb
- rank 59 | 140 samples | 23 papers | 114 compositions
- compositions: Mg3.2Sb1.5Bi0.49Te0.01 (13); Mg3.032Y0.018SbBi (4); Mg3.047Y0.003SbBi (4); Mg3.1Sb1.5Bi0.49Te0.01 (4); Mg3.19Y0.01Sb1.5Bi0.5 (3); Mg3.2Sb1.5Bi0.49Se0.01 (2)
- dopant candidates (<5% at.): Te (73), Y (20), Se (14), Co (12), Mo (9), Mn (6), La (5), Nb (4), Nd (4), Ce (3), Na (3), Yb (2), Ta (1), W (1), Ni (1), Zn (1), Fe (1), Hf (1), V (1)
- seed hypothesis (confirm): caal2si2_zintl
- sample form: Bulk (78); Polycrystal (9)
- solid-solution axis: Bi/(Bi+Sb) spans 0.17-0.85 (median 0.25) over 114 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 200-775 K (5th-95th pct of 550 curves; full span incl. outliers 11-862 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg14BiSb P-6m2 (187) mp-1026422 [hull=0.060, PRIMARY, AMBIGUOUS]; Mg6BiSb Amm2 (38) mp-1017143 [hull=0.095, PRIMARY]; Mg14BiSb Amm2 (38) mp-1026433 [hull=0.062]
- papers: https://doi.org/10.1007/s11664-012-2417-7 (On the Thermoelectric Properties of Zintl Compounds Mg3Bi2−x Pn x (Pn ...) | https://doi.org/10.1088/0022-3727/39/24/035 (Electrical and thermoelectric properties of nanocrystal substitutional...) | https://doi.org/10.1073/pnas.1711725114 (Manipulation of ionized impurity scattering for achieving high thermoe...)

## Co-Sb-Ti
- rank 60 | 135 samples | 36 papers | 79 compositions
- compositions: TiCoSb (37); CoTiSb (8); TiCoSn0.05Sb0.95 (3); TiCo0.9Ni0.1Sb (2); TiCo0.95Ni0.05Sb (2); TiCoSn0.01Sb0.99 (2)
- dopant candidates (<5% at.): Fe (15), Ni (13), Sn (12), Sc (9), Ge (7), Ta (7), Cu (5), V (5), Bi (4), In (4), Pd (3), Nb (3), Zr (2), Mn (1), Si (1), Hf (1)
- seed hypothesis (confirm): half_heusler
- sample form: Bulk (33)
- measured range: 12-985 K (5th-95th pct of 495 curves; full span incl. outliers 10-1168 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiCoSb F-43m (216) mp-5967 [hull=0.000, icsd=31, PRIMARY]; Ti5CoSb2 I4/mcm (140) mp-1208246 [hull=0.000, PRIMARY]; Ti5CoSb3 P6_3/mcm (193) mp-1208267 [hull=0.039, PRIMARY]
- papers: https://doi.org/10.1021/cm3011343 (Rapid Microwave Preparation of Thermoelectric TiNiSn and TiCoSb Half-H...) | https://doi.org/10.1016/j.jallcom.2004.04.096 (High temperature thermoelectric properties of CoTiSb half-Heusler comp...) | https://doi.org/10.1016/j.jallcom.2004.07.074 (Effects of partial substitution of Co by Ni on the high-temperature th...)

## As-Fe-La-O
- rank 61 | 130 samples | 14 papers | 46 compositions
- compositions: LaFeAsO0.89F0.11 (20); La0.85Sr0.15OFeAs (9); LaFeAsO (8); LaFe0.9Co0.1AsO0.89F0.11 (6); LaFe0.9975Co0.0025AsO0.89F0.11 (4); LaFe0.97Co0.03AsO0.89F0.11 (4)
- dopant candidates (<5% at.): F (99), Co (40), Ru (19), Sr (10), Mn (5), P (1)
- seed hypothesis (confirm): zrcusias_1111
- sample form: Polycrystal (17); Bulk (10)
- measured range: 10-301 K (5th-95th pct of 190 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaFeAsO P4/nmm (129) mp-1080678 [hull=0.099, icsd=17, PRIMARY]; La2FeAs2O P4/mmm (123) mp-1211381 [hull=1.553, PRIMARY]
- papers: https://doi.org/10.1063/1.3466990 (Thermoelectric properties of LaFeAsO1−y at low temperature) | https://doi.org/10.1143/jpsj.80.044704 (Thermoelectric Properties of LaFePO1-xFxand LaFeAsO1-xFx–Possibility o...) | https://doi.org/10.1016/j.jallcom.2010.08.138 (Electrical transport properties of F-doped LaFeAsO oxypnictide)

## Fe-O
- rank 62 | 129 samples | 31 papers | 68 compositions
- compositions: Fe3O4 (48); Fe2O3 (15); Fe1.9975P0.0025O3 (1); Fe1.995P0.005O3 (1); Fe1.995V0.005O3 (1); Fe1.9925V0.0075O3 (1)
- dopant candidates (<5% at.): Co (30), Ba (28), Sr (25), La (17), Zn (12), Ti (8), Pr (7), Ru (6), Cu (6), Y (5), P (4), V (4), Li (4), Gd (4), F (3), Nd (3), Sm (3), Sn (2), Ni (2), Mg (1), Mn (1), Cr (1)
- seed hypothesis (confirm): corundum
- sample form: Bulk (6); SingleCrystal (5); Film (3)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 55-1075 K (5th-95th pct of 172 curves; full span incl. outliers 11-1553 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe3O4 Fd-3m (227) mp-715490 [hull=0.000, icsd=100, PRIMARY]; Fe2O3 R-3c (167) mp-24972 [hull=0.000, icsd=65, PRIMARY]; FeO2 Pnma (62) mp-1103327 [hull=0.164, icsd=15, PRIMARY]; FeO Fm-3m (225) mp-18905 [hull=0.414, icsd=14, PRIMARY]; Fe4O5 Cmcm (63) mp-1188678 [hull=0.073, icsd=4, PRIMARY]
- papers: https://doi.org/10.1063/1.4737409 (Very high thermoelectric power factor in a Fe3O4/SiO2/p-type Si(100) h...) | https://doi.org/10.1002/er.3052 (Thermoelectric properties of P-doped and V-doped Fe2O3for renewable en...) | https://doi.org/10.1002/qua.22282 (High thermoelectric performance of metal-substituted samples of α-Fe2O...)

## O-Ru-Sr
- rank 63 | 128 samples | 42 papers | 32 compositions
- compositions: SrRuO3 (56); Sr2RuO4 (36); Sr3Ru2O7 (3); Sr4Ru3O10 (2); SrRu0.982Co0.018O4 (2); Sr2Ru2O4 (2)
- dopant candidates (<5% at.): La (6), Cr (4), Gd (3), Co (3), Mn (2), Ti (2), Ca (1), Fe (1), Sn (1)
- sample form: SingleCrystal (18); Bulk (6)
- measured range: 11-1022 K (5th-95th pct of 156 curves; full span incl. outliers 10-1271 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2RuO4 I4/mmm (139) mp-4596 [hull=0.000, icsd=42, PRIMARY]; SrRuO3 Pnma (62) mp-22390 [hull=0.000, icsd=24, PRIMARY]; Sr3Ru2O7 I4/mmm (139) mp-5868 [hull=0.015, icsd=3, PRIMARY]; Sr4Ru3O10 Cmce (64) mp-680680 [hull=0.002, icsd=1, PRIMARY]; Sr4Ru6ClO18 I23 (197) mp-1193929 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2004.06.053 (Thermoelectric properties of perovskite type strontium ruthenium oxide) | https://doi.org/10.1016/j.jallcom.2012.01.150 (Thermoelectric properties of Ca1−xSrxRuO3 compounds prepared by spark ...) | https://doi.org/10.1016/j.mseb.2008.12.026 (Thermoelectric properties of alkaline earth ruthenates prepared by SPS)

## B
- rank 64 | 124 samples | 28 papers | 89 compositions
- compositions: YB66 (13); B (11); V1.5B105 (4); B105 (3); Co1.0B105 (3); YbB44Si2 (2)
- dopant candidates (<5% at.): Y (43), Si (16), Al (13), V (12), Fe (10), Cr (10), Co (7), Zr (7), Cu (6), Yb (5), Nd (3), Sm (3), Er (2), Gd (2), Sr (2), W (2), Tm (2), Mn (1), Mo (1), Zn (1), Rh (1), Ti (1), Tb (1), C (1), Mg (1), Ho (1)
- seed hypothesis (confirm): boron_carbide
- sample form: Bulk (38); SingleCrystal (5); Film (3); Wire (2)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 39-1074 K (5th-95th pct of 225 curves; full span incl. outliers 10-1130 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): B R-3m (166) mp-160 [hull=0.000, icsd=8, PRIMARY]; V2(B24C)3 P222 (16) mp-1217011 [hull=0.024, PRIMARY]; YbLuB24 R-3m (166) mp-1215587 [hull=0.038, PRIMARY]; ZrScB24 R3m (160) mp-1215238 [hull=0.014, PRIMARY]; ZrUB24 R-3m (166) mp-1215198 [hull=0.016, PRIMARY]
- papers: https://doi.org/10.1063/1.4758297 (Excellent p-n control in a high temperature thermoelectric boride) | https://doi.org/10.1039/b916028k (Effect of Zn doping on improving crystal quality and thermoelectric pr...) | https://doi.org/10.1063/1.1883726 (High temperature thermoelectric properties of B12 icosahedral cluster-...)

## Fe-La-O-Sr
- rank 65 | 122 samples | 55 papers | 59 compositions
- compositions: La0.6Sr0.4Co0.2Fe0.8O3 (26); La0.6Sr0.4FeO3 (12); La0.5Sr0.5Al0.2Fe0.8O3 (11); La0.4Sr0.6Co0.2Fe0.8O3 (4); (La0.6Sr0.4)(Co0.2Fe0.8)O3 (3); La0.5Sr0.5Co0.2Fe0.8O3 (3)
- dopant candidates (<5% at.): Co (54), Al (12), Ni (9), Mo (7), Nb (7), Ti (5), Ba (5), Ca (5), Pr (4), Cu (4), Ta (3), Cr (3), Zn (2), Mn (2), Sc (1), W (1), Sm (1), Nd (1), Ce (1)
- seed hypothesis (confirm): perovskite
- sample form: rod-shaped (25); disk (7); pellets (3); Plate (2); Bulk (1)
- measured range: 292-1274 K (5th-95th pct of 127 curves; full span incl. outliers 80-1375 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2La(FeO3)3 P-3m1 (164) mp-1218808 [hull=0.001, PRIMARY]; SrLa(FeO3)2 R32 (155) mp-1218237 [hull=0.000, PRIMARY]; SrLa2Fe2O7 I4mm (107) mp-1217886 [hull=0.045, PRIMARY]; SrLaFeO4 I4mm (107) mp-1218154 [hull=0.013, PRIMARY, AMBIGUOUS]; SrLaFeO4 Cmcm (63) mp-1218176 [hull=0.020]
- papers: https://doi.org/10.2320/jinstmet.ja201516 (P-Type Thermoelectric Properties of Pr<sub>1&minus;<i>x</i></sub>Sr<su...) | https://doi.org/10.1016/j.jallcom.2006.05.012 (Power factor of La1−xSrxFeO3 and LaFe1−yNiyO3) | https://doi.org/10.1016/j.jpowsour.2007.05.052 (Structural and electrical properties of selected La1−xSrxCo0.2Fe0.8O3 ...)

## Mg-Sn
- rank 66 | 118 samples | 26 papers | 64 compositions
- compositions: Mg2Sn (34); Mg2Sn0.95Si0.05 (5); Ag0.01Mg2Sn (5); Ag0.005Mg2Sn (4); (Mg2Sn)99Ag1 (3); Ag0.0015Mg2Sn (3)
- dopant candidates (<5% at.): Ag (41), Sb (13), Si (9), Ge (6), Bi (3), Ni (1), In (1), Cu (1), Zn (1), Li (1)
- seed hypothesis (confirm): antifluorite
- sample form: Bulk (60)
- measured range: 16-773 K (5th-95th pct of 399 curves; full span incl. outliers 10-826 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg2Sn Fm-3m (225) mp-2343 [hull=0.000, icsd=10, PRIMARY]; Mg9Sn5 R3 (146) mp-31503 [hull=0.003, icsd=1, PRIMARY]; Mg3Sn P6_3/m (176) mp-643067 [hull=0.026, icsd=1, PRIMARY]; Mg15Sn P-6m2 (187) mp-1023593 [hull=0.019, PRIMARY]; Mg149Sn P-6m2 (187) mp-1185637 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1142/s1793604713400055 (STUDY OF ELECTRON, PHONON AND CRYSTAL STABILITY VERSUS THERMOELECTRIC ...) | https://doi.org/10.1063/1.4898013 (Electronic structure and thermoelectric properties of p-type Ag-doped ...) | https://doi.org/10.1007/s11664-010-1150-3 (Eutectic Microstructure and Thermoelectric Properties of Mg2Sn)

## Cd-O
- rank 67 | 116 samples | 16 papers | 39 compositions
- compositions: CdO (50); (SiC)0.05(CdO)0.95 (8); (SiC)0.03(CdO)0.97 (8); (SiC)0.01(CdO)0.99 (8); (SiC)0.08(CdO)0.92 (8); Cd0.97Ba0.03O (1)
- dopant candidates (<5% at.): Si (32), C (32), Mg (10), Ca (5), Pr (4), Ba (3), Er (3), Ag (3), N (3), Cu (3), Zn (3), Al (2)
- seed hypothesis (confirm): rocksalt_oxide
- sample form: Bulk (26); Polycrystal (5); SingleCrystal (1)
- measured range: 320-1023 K (5th-95th pct of 287 curves; full span incl. outliers 35-1077 K)
- [ref 1] TEDesignLab / ICSD: CdO2 Pa-3 (205) mp-2310 [hull=0.064, icsd=4, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: CdO Fm-3m (225) mp-1132 [hull=0.000, icsd=14, PRIMARY]; CdO2 P-3m1 (164) mp-1096866 [hull=0.424, icsd=3]; CdO2 Cm (8) mp-1096876 [hull=0.411, icsd=2]; CdO P6_3mc (186) mp-13119 [hull=0.007, icsd=1]
- papers: https://doi.org/10.1007/s40145-015-0153-1 (Effect of sintering temperature on thermoelectric properties of CdO ce...) | https://doi.org/10.1111/jace.13780 (Enhanced Thermoelectric Performance of CdO Ceramics Via Ba2+Doping) | https://doi.org/10.1016/j.jeurceramsoc.2013.02.025 (The effect of Er3+ doping on the structure and thermoelectric properti...)

## Cu-Sb-Se
- rank 68 | 113 samples | 22 papers | 86 compositions
- compositions: Cu3SbSe4 (17); Cu3SbSe3 (6); Cu3Sb0.98Sn0.02Se4 (3); Cu2.95SbSe4 (2); Cu2.925SbSe4 (2); CuSbSe2 (2)
- dopant candidates (<5% at.): Sn (39), Hf (12), Zr (10), Bi (9), Ag (9), In (5), Sc (4), Y (4), Al (3), Ga (2), Cd (2), Pb (1), Ti (1)
- seed hypothesis (confirm): famatinite, skinnerite_cu3sbse3  <-- MIXED, split per composition
- sample form: Bulk (46); Film (6); SingleCrystal (2)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 294-674 K (5th-95th pct of 517 curves; full span incl. outliers 10-702 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu3SbSe4 I-42m (121) mp-9814 [hull=0.000, icsd=4, PRIMARY]; CuSbSe2 Pnma (62) mp-20331 [hull=0.000, icsd=4, PRIMARY]; Cu3SbSe3 Pnma (62) mp-29476 [hull=0.035, icsd=1, PRIMARY]; Cu3SbSe4 R3m (160) mp-1225801 [hull=0.118]
- papers: https://doi.org/10.1063/1.4904996 (Thermoelectric and mechanical properties of spark plasma sintered Cu3S...) | https://doi.org/10.1039/c3ce41583j (Cu2HgSnSe4 nanoparticles: synthesis and thermoelectric properties) | https://doi.org/10.1039/c3dt52447g (Co-precipitation synthesis of nanostructured Cu3SbSe4and its Sn-doped ...)

## Ba-Ga-Sn
- rank 69 | 112 samples | 23 papers | 80 compositions
- compositions: Ba8Ga16Sn30 (26); Ba8Ga15.9Zn0.006Sn30.1 (3); Ba7.99Ga15.84Cu0.004Sn30.16 (2); Ba8Ga16.6Sn29.4 (2); Ba7.98Ga15.8Cu0.018Sn30.2 (2); Ba8Ga15CuSn30 (2)
- dopant candidates (<5% at.): Cu (19), Zn (12), Ge (10), In (5), Sb (3), Eu (3), Al (2), K (2)
- seed hypothesis (confirm): clathrate_i, clathrate_viii  <-- MIXED, split per composition
- sample form: SingleCrystal (5)
- measured range: 26-643 K (5th-95th pct of 319 curves; full span incl. outliers 10-695 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba4Ga22Sn I-43m (217) mp-1214544 [hull=0.122, PRIMARY]; Ba4GaSn3 Pmm2 (25) mp-1228036 [hull=0.022, PRIMARY]; BaGa3Sn I4mm (107) mp-1227967 [hull=0.024, PRIMARY]; BaGaSn P-3m1 (164) mp-1228005 [hull=0.062, PRIMARY]
- papers: https://doi.org/10.1021/acs.chemmater.5b00025 (Thermoelectric Properties ofp-Type Clathrate Ba8.0Ga15.9ZnySn30.1Singl...) | https://doi.org/10.1016/j.jallcom.2010.07.121 (Optimization of thermoelectric properties of type-VIII clathrate Ba8Ga...) | https://doi.org/10.1016/j.jallcom.2012.05.049 (Thermoelectric properties of type-VIII clathrate Ba8Ga16Sn30 doped wit...)

## S-Ti
- rank 70 | 109 samples | 31 papers | 60 compositions
- compositions: TiS2 (38); Ti1.008S2 (2); Ti1.025S2 (2); Ti1.031S2 (2); TiS3 (2); Ag0.02TiS2 (2)
- dopant candidates (<5% at.): Nb (8), Ag (5), Co (5), Cu (4), Ta (4), Cd (3), Mg (3), Nd (3), Gd (2), Bi (2), Li (2), Ce (2), Zr (2), Mo (2), Sn (2), As (1), Pb (1), Se (1), V (1)
- seed hypothesis (confirm): cdi2_1t
- sample form: Bulk (40); pellets (7); SingleCrystal (5)
- measured range: 11-820 K (5th-95th pct of 368 curves)
- [ref 1] TEDesignLab / ICSD: TiS2 P-3m1 (164) mp-2156 [hull=0.000, icsd=18, PRIMARY]; TiS3 P2_1/m (11) mp-9920 [hull=0.000, icsd=4, PRIMARY]; TiS2 C2/m (12) mp-1062030 [hull=0.005, icsd=2]; TiS2 Pnnm (58) mp-1072088 [hull=0.119, icsd=1]; TiS2 P6_3/mmc (194) mp-1077021 [hull=0.144, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: Ti2S Pnnm (58) mp-616559 [hull=0.000, icsd=3, PRIMARY]; TiS P-6m2 (187) mp-1018028 [hull=0.000, icsd=1, PRIMARY]; Ti8S3 C2/m (12) mp-680850 [hull=0.010, icsd=1, PRIMARY]; Ti3S2 R32 (155) mp-1217073 [hull=0.299, PRIMARY]; TiS2 Pnma (62) mp-1101969 [hull=0.284, icsd=2]
- papers: https://doi.org/10.1016/j.actamat.2012.09.035 (Thermoelectric properties of prepared by CS2 sulfurization) | https://doi.org/10.1016/j.actamat.2014.06.032 (Electron doping and phonon scattering in Ti1+xS2 thermoelectric compounds) | https://doi.org/10.1063/1.2217190 (Thermoelectric properties of doped titanium disulfides)

## Bi-O-Se
- rank 71 | 108 samples | 21 papers | 46 compositions
- compositions: Bi2O2Se (37); Bi1.98La0.02O2Se (5); Bi1.96La0.04O2Se (5); Bi1.92La0.08O2Se (5); Bi1.94La0.06O2Se (5); (Bi2Se3)0.8(TiO2)0.2 (4)
- dopant candidates (<5% at.): La (21), Ti (11), Nb (9), Ge (4), Cl (4), Te (3), Sb (3), Sn (2)
- seed hypothesis (confirm): bi2o2se_layered
- sample form: Bulk (56); Powder (4); Polycrystal (4); Film (1)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- solid-solution axis: O/(O+Se) spans 0.11-0.68 (median 0.67) over 46 compositions
     CHECK: same periodic group, but oxygen often occupies its own sublattice (BiCuSeO, LaFeAsO) rather than substituting for the heavier chalcogen. Confirm the two share a site before treating this as a substitution axis.
- measured range: 297-824 K (5th-95th pct of 388 curves; full span incl. outliers 11-923 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi2(SeO3)3 P2_1/c (14) mp-29833 [hull=0.000, icsd=1, PRIMARY]; Bi2Se3O10 C2/c (15) mp-1193554 [hull=0.000, icsd=1, PRIMARY]; Bi2SeO5 Aem2 (39) mp-29839 [hull=0.000, icsd=1, PRIMARY]; BiSeO6 P2_1/c (14) mp-1198307 [hull=0.531, icsd=1, PRIMARY]; Bi2SeO6 Cmce (64) mp-754798 [hull=0.065, PRIMARY]
- papers: https://doi.org/10.1111/jace.13619 (Enhanced Thermoelectric Properties of Bi2O2Se Ceramics by Bi Deficiencies) | https://doi.org/10.3390/ma8041568 (Enhanced Thermoelectric Performance of Bi2O2Se with Ag Addition) | https://doi.org/10.1016/j.matchemphys.2009.08.067 (Thermoelectric properties of Bi2O2Se)

## Cu-Se-Sn
- rank 72 | 108 samples | 18 papers | 85 compositions
- compositions: Cu2SnSe3 (11); Cu2Sn0.82In0.18Se2.7S0.3 (4); Cu2Ga0.05Sn0.95Se3 (3); Cu2Ga0.075Sn0.925Se3 (3); Cu2Ga0.025Sn0.975Se3 (3); (Cu2Sn0.95Ga0.05Se3)0.91(In2Se3)0.09 (2)
- dopant candidates (<5% at.): In (34), Ga (15), S (12), Ag (9), Zn (6), Mn (5), Fe (4), Ge (3), Co (3), C (3)
- sample form: Bulk (68); Polycrystal (5)
- measured range: 39-854 K (5th-95th pct of 524 curves)
- [ref 1] TEDesignLab / ICSD: Cu2SnSe3 Cc (9) mp-11658 [hull=0.000, icsd=2, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Cu5Sn2Se7 C2 (5) mp-1103757 [hull=0.000, icsd=1, PRIMARY]; Cu2SnSe3 Imm2 (44) mp-1225786 [hull=0.013]; Cu2SnSe3 Fdd2 (43) mp-1225953 [hull=0.021]
- papers: https://doi.org/10.1016/j.actamat.2013.04.003 (Investigation of thermoelectric properties of Cu2GaxSn1−xSe3 diamond-l...) | https://doi.org/10.1021/cm101589c (Cu−Se Bond Network and Thermoelectric Compounds with Complex Diamondli...) | https://doi.org/10.1039/c4dt01457j (Structural evolvement and thermoelectric properties of Cu3−xSnxSe3 com...)

## Bi-S
- rank 73 | 107 samples | 28 papers | 53 compositions
- compositions: Bi2S3 (48); (BiCl3)0.025Bi2S3 (4); (Bi2S3)0.995(BiCl3)0.005 (3); (HfCl4)0.025Bi2S3 (2); Bi2S2.90 (2); (Bi2S2.94Se0.06)0.995(BiCl3)0.005 (1)
- dopant candidates (<5% at.): Cl (22), Ag (10), Cu (9), Br (7), Se (4), Zn (4), O (4), In (4), Pb (4), Sn (4), Hf (2)
- seed hypothesis (confirm): stibnite
- sample form: Bulk (42); Plate (7); Polycrystal (6); Film (1)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 293-783 K (5th-95th pct of 484 curves; full span incl. outliers 10-845 K)
- [ref 1] TEDesignLab / ICSD: Bi2S3 Pnma (62) mp-22856 [hull=0.000, icsd=23, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: BiS Amm2 (38) mp-28677 [hull=0.222, icsd=1, PRIMARY]; Bi2S P2_1/c (14) mp-1103100 [hull=0.169, icsd=1, PRIMARY]; BiS2 C2/m (12) mp-971673 [hull=0.000, icsd=1, PRIMARY]; BiS3 P6_3/mmc (194) mp-1183481 [hull=0.421, PRIMARY]; BiS C2/m (12) mp-1064840 [hull=0.285, icsd=1]
- papers: https://doi.org/10.1002/aenm.201100775 (Tellurium-Free Thermoelectric: The Anisotropic n-Type Semiconductor Bi2S3) | https://doi.org/10.1039/b913462j (Wet chemical synthesis and thermoelectric properties of V-VI one- and ...) | https://doi.org/10.1016/j.jallcom.2011.11.072 (Fabrication and properties of Bi2−xAg3xS3 thermoelectric polycrystals)

## Co-La-O-Sr
- rank 74 | 107 samples | 37 papers | 33 compositions
- compositions: La0.6Sr0.4CoO3 (22); La0.6Sr0.4Co0.8Fe0.2O3 (19); La0.7Sr0.3CoO3 (18); La0.5Sr0.5CoO3 (9); SrLaCoO4 (4); Sr1.05La0.95CoO4 (3)
- dopant candidates (<5% at.): Fe (29), Cu (6), Ta (4), Mn (3), Nb (3), Ba (2), Sb (2), V (1)
- sample form: rod-shaped (13); pellets (4); Bulk (3)
- measured range: 11-1268 K (5th-95th pct of 117 curves; full span incl. outliers 10-1322 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2LaCoO6 Fm-3m (225) mp-1080670 [hull=0.135, icsd=1, PRIMARY]; Sr3La(CoO4)2 Amm2 (38) mp-1218340 [hull=0.004, PRIMARY]; Sr3La7Ga(Co3O10)3 C2 (5) mp-1173241 [hull=0.015, PRIMARY]; Sr4La(CoO3)5 C2/m (12) mp-1218687 [hull=0.015, PRIMARY]; SrLa(CoO3)2 Fm-3m (225) mp-1218224 [hull=0.127, PRIMARY]
- papers: https://doi.org/10.1063/1.3699038 (Thermoelectric and magnetic properties of nanocrystalline La0.7Sr0.3CoO3) | https://doi.org/10.1016/j.jssc.2008.08.017 (Thermoelectric properties of polycrystalline La1−xSrxCoO3) | https://doi.org/10.1088/0022-3727/41/21/215009 (Structural, magnetic, electrical and thermal transport properties in t...)

## Cu-Nd-O
- rank 75 | 107 samples | 17 papers | 31 compositions
- compositions: Nd1.85Ce0.15CuO4 (30); Nd2CuO4 (14); Nd2CuO3.8F0.2 (13); Nd1.90Ce0.10CuO4 (4); Nd1.95Ce0.05CuO4 (4); Nd2CuO3.9F0.1 (4)
- dopant candidates (<5% at.): Ce (57), F (33), Ca (3), Ni (1), Zn (1), Sr (1), Ba (1), Ru (1)
- seed hypothesis (confirm): ruddlesden_popper
- sample form: Bulk (27); pellets (1); SingleCrystal (1)
- measured range: 10-900 K (5th-95th pct of 116 curves; full span incl. outliers 10-961 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd2CuO4 I4/mmm (139) mp-4158 [hull=0.000, icsd=21, PRIMARY]; Nd(CuO2)2 I4_1/a (88) mp-4371 [hull=0.000, icsd=2, PRIMARY]; NdCuO2 R-3m (166) mp-4886 [hull=0.000, icsd=2, PRIMARY]; Nd2Cu2O5 Pbam (55) mp-21025 [hull=0.069, icsd=1, PRIMARY]; Nd12Cu6O25 C2/m (12) mp-662567 [hull=0.067, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/bf01589742 (Thermoelectric properties of the Nd2−x Ce x CuO4−y system) | https://doi.org/10.1016/s0925-8388(02)00917-9 (Thermoelectric properties of layered rare earth copper oxides) | https://doi.org/10.1016/s0925-8388(02)00989-1 (Thermoelectric properties of Ni- and Zn-doped Nd2CuO4)

## La-Ni-O
- rank 76 | 107 samples | 39 papers | 41 compositions
- compositions: LaNiO3 (49); La2NiO4 (8); La0.9Bi0.1NiO3 (4); La0.97Sr0.03NiO3 (4); La0.99Sr0.01NiO3 (3); La4Ni3O10 (3)
- dopant candidates (<5% at.): Sr (11), Cu (5), Bi (5), Al (5), Fe (3), Co (3), Mn (3), Mo (3), Pb (2), K (1), Ti (1), Nd (1), Au (1)
- seed hypothesis (confirm): perovskite
- sample form: Bulk (9); cylinder (3)
- measured range: 11-1235 K (5th-95th pct of 122 curves; full span incl. outliers 10-1556 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2NiO4 I4/mmm (139) mp-25091 [hull=0.064, icsd=14, PRIMARY]; LaNiO3 R-3c (167) mp-19339 [hull=0.000, icsd=10, PRIMARY]; La3Ni2O7 Cmcm (63) mp-18926 [hull=0.016, icsd=2, PRIMARY]; LaNiO2 P4/mmm (123) mp-25097 [hull=0.395, icsd=2, PRIMARY]; La2Ni2O5 C2/c (15) mp-19073 [hull=0.120, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/s13391-013-0034-0 (Thermoelectric properties of a doped LaNiO3 perovskite system prepared...) | https://doi.org/10.1149/1.2358840 (Electrical, Thermoelectric, and Structural Properties of La(M[sub x]Fe...) | https://doi.org/10.1149/1.3559186 (Electrical Conductivity and Thermoelectric Power of La2NiO4+δ)

## Ba-Co-O-Sr
- rank 77 | 105 samples | 40 papers | 49 compositions
- compositions: Ba0.5Sr0.5Co0.8Fe0.2O3 (44); Ba0.6Sr0.4Co0.9Nb0.1O3 (4); Ba0.6Sr0.4Co0.8Fe0.2O3 (4); (Sr0.75Ba0.25)6Co5O15 (2); (Sr0.5Ba0.5)7Co6O18 (2); Ba0.475Sr0.475Sm0.05Co0.8Fe0.2O3 (2)
- dopant candidates (<5% at.): Fe (91), Sm (11), Nb (10), La (7), Ti (4), Nd (3), Ce (2), Zr (1), Y (1), Gd (1), Zn (1), Mn (1)
- seed hypothesis (confirm): perovskite
- sample form: rod-shaped (19); pellets (5); Plate (4); Other (2)
- solid-solution axis: Ba/(Ba+Sr) spans 0.25-0.60 (median 0.50) over 49 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 91-1268 K (5th-95th pct of 109 curves; full span incl. outliers 10-1273 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba3Sr(CoO3)4 Pmm2 (25) mp-1228377 [hull=0.000, PRIMARY]; BaSr(CoO3)2 P-6m2 (187) mp-1205807 [hull=0.028, PRIMARY]; BaSr3(CoO3)4 Pmm2 (25) mp-1227831 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1143/jjap.43.8208 (Thermoelectric Properties ofAn+2Con+1O3n+3(A=Ca, Sr, Ba,n=1–5)) | https://doi.org/10.1252/jcej.07we146 (Thermoelectric Properties of Delafossite-Type Oxide CuFe1–xNixO2 (0 ≤ ...) | https://doi.org/10.1039/c9qm00067d (High-pressure synthesis of highly oxidized Ba<sub>0.5</sub>Sr<sub>0.5<...)

## O-W
- rank 78 | 103 samples | 21 papers | 64 compositions
- compositions: WO3 (15); WO2.90 (11); W0.95Ti0.05O3 (6); WO2.9 (5); (Bi2O3)0.005WO3 (3); (Bi2O3)0.025WO3 (3)
- dopant candidates (<5% at.): Ti (11), Bi (9), Ca (6), Zn (5), Ni (5), La (4), Tb (4), Sn (4), Ce (3), Ta (3), Co (3), Na (3)
- seed hypothesis (confirm): reo3_wo3
- sample form: Bulk (24); Other (12)
- measured range: 49-1100 K (5th-95th pct of 237 curves; full span incl. outliers 11-1224 K)
  !! DISTORTION SERIES (WO3): the measured range spans 5 steps of one prototype --
       epsilon  Pc (7)  -230 K
       delta    P-1 (2)  230-290 K
       gamma    P2_1/n (14)  290-603 K mp-619461
       beta     Pbcn (60)  603-1013 K
       alpha    P4/ncc (130)  1013-1170 K
     The cubic ReO3 aristotype is essentially never observed for WO3 at ambient pressure below the melt; every measured tungsten trioxide is a tilt-distorted variant. A transport run from room temperature to 1200 K passes through three of these steps.
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): WO3 P2_1/c (14) mp-619461 [hull=0.000, icsd=8, PRIMARY]; WO2 P4_2/mnm (136) mp-19372 [hull=0.000, icsd=2, PRIMARY]; W2O7 Fd-3m (227) mp-1178760 [hull=0.297, icsd=2, PRIMARY]; W18O49 P2/m (10) mp-19529 [hull=0.000, icsd=2, PRIMARY]; W3O10 Fmm2 (42) mp-1104455 [hull=0.177, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/j.ceramint.2011.08.041 (Effect of CeO2 on the thermoelectric properties of WO3-based ceramics) | https://doi.org/10.1016/j.jallcom.2012.03.022 (Improvement of thermoelectric properties of WO3 ceramics by ZnO addition) | https://doi.org/10.1016/j.jallcom.2013.07.052 (Effect of La2O3 on high-temperature thermoelectric properties of WO3)

## Al-Mn-Pd
- rank 79 | 102 samples | 32 papers | 44 compositions
- compositions: Al70Pd20Mn10 (17); Al70Mn9Pd21 (13); Al70Pd21Mn9 (8); Al71.5Pd20.3Mn8.2 (6); Al72Pd19.5Mn8.5 (4); Al70Pd22Mn8 (3)
- dopant candidates (<5% at.): Ga (6), Re (5), Fe (2), Si (1)
- seed hypothesis (confirm): quasicrystal_approximant
- sample form: Bulk (10)
- measured range: 10-975 K (5th-95th pct of 134 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnAlPd2 Fm-3m (225) mp-10891 [hull=0.031, icsd=1, PRIMARY]; MnAlPd2 P4/mmm (123) mp-1221718 [hull=0.061]
- papers: https://doi.org/10.1063/1.2990772 (Thermoelectric properties of polygrained icosahedral Al[sub 71−x]Ga[su...) | https://doi.org/10.1007/s11664-009-1065-z (Thermoelectric Properties of Icosahedral Al-Pd-(Mn or Re) Quasicrystal...) | https://doi.org/10.1524/zkri.2009.1061 (Thermoelectric performance of Al–Pd–Mn quasicrystals: comparison with ...)

## Cr-Cu-O
- rank 80 | 102 samples | 16 papers | 29 compositions
- compositions: CuCr0.97Mg0.03O2 (16); CuCrO2 (15); CuCr0.85Mg0.15O2 (14); CuCr0.98Mg0.02O2 (8); CuCr0.99Mg0.01O2 (8); CuCr0.96Mg0.04O2 (7)
- dopant candidates (<5% at.): Mg (74), Ni (6), Ca (2), Sn (2), Zn (1), Co (1), Fe (1), Mn (1), V (1), Sr (1), Ba (1)
- seed hypothesis (confirm): delafossite
- sample form: Bulk (41); Film (5)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 32-1128 K (5th-95th pct of 219 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CrCuO2 R-3m (166) mp-796545 [hull=0.000, icsd=10, PRIMARY]; Cr2CuO4 I4_1/amd (141) mp-1103973 [hull=0.017, icsd=6, PRIMARY]; Cr(CuO3)2 P2_1/c (14) mp-1199882 [hull=0.092, icsd=1, PRIMARY]; Cr3(CuO6)2 P2_1/c (14) mp-764630 [hull=0.054, PRIMARY]; Cr4Cu11O30 P-1 (2) mp-1213972 [hull=0.072, PRIMARY]
- papers: https://doi.org/10.1143/jjap.47.59 (Effect of Doping on Thermoelectric Properties of Delafossite-Type Oxid...) | https://doi.org/10.1143/jjap.46.1071 (Structural, Magnetic and Thermoelectric Properties of Delafossite-type...) | https://doi.org/10.1088/0022-3727/48/49/495103 (Effects of spin entropy and lattice strain from mixed-trivalent Fe3+/C...)

## Cu-S
- rank 81 | 102 samples | 24 papers | 49 compositions
- compositions: Cu1.8S (13); Cu1.97S (12); Cu2S (12); (Cu2S)0.95(Cu5FeS4)0.05 (5); (Cu2S)0.99(Cu5FeS4)0.01 (5); (Cu2S)0.90(Cu5FeS4)0.10 (5)
- dopant candidates (<5% at.): Fe (19), Mn (8), Te (4), Bi (4), Na (3), Ni (3), Ti (3), Se (2), Sn (2)
- sample form: Bulk (62); Film (1); SingleCrystal (1)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 74-973 K (5th-95th pct of 408 curves; full span incl. outliers 11-1007 K)
- [ref 1] TEDesignLab / ICSD: Cu2S P4_32_12 (96) mp-618991 [hull=0.045, icsd=1, PRIMARY]; Cu2S (194)
- [ref 2] MP, ranked by ICSD evidence: CuS P6_3/mmc (194) mp-504 [hull=0.000, icsd=12, PRIMARY]; CuS2 Pa-3 (205) mp-1068 [hull=0.005, icsd=5, PRIMARY]; Cu7S4 Pnma (62) mp-624299 [hull=0.000, icsd=1, PRIMARY]; Cu18S11 P1 (1) mp-684898 [hull=0.079, PRIMARY]; Cu11S16 Cm (8) mp-675278 [hull=0.229, PRIMARY]
- papers: https://doi.org/10.1039/c1cc16368j (Synthesis and transport property of Cu1.8S as a promising thermoelectr...) | https://doi.org/10.1039/c4ee02428a (Sulfide bornite thermoelectric material: a natural mineral with ultral...) | https://doi.org/10.2497/jjspm.61.18 (Synthesis and Thermoelectric Properties of Carrier-Doped CuFeS2 Sinter...)

## Nb-O-Sr
- rank 82 | 102 samples | 20 papers | 45 compositions
- compositions: Sr0.61Ba0.39Nb2O6 (26); Sr5Nb5O17 (6); SrNbO3 (6); Sr1.8La0.2Nb2O7 (5); Sr2Nb2O7 (3); Sr0.85NbO3 (3)
- dopant candidates (<5% at.): Ba (42), La (21), Ti (4), F (3), Li (3), C (2), W (1), K (1)
- seed hypothesis (confirm): perovskite
- sample form: Bulk (21); SingleCrystal (9); OrientedBulk (4); Polycrystal (3)
- measured range: 11-1074 K (5th-95th pct of 204 curves; full span incl. outliers 10-1273 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2Nb2O7 Cmc2_1 (36) mp-3870 [hull=0.002, icsd=2, PRIMARY]; Sr2Nb5O9 P4/mmm (123) mp-22772 [hull=0.037, icsd=2, PRIMARY]; SrNb8O14 Pbam (55) mp-3790 [hull=0.000, icsd=2, PRIMARY]; SrNb2O6 P2_1/c (14) mp-4591 [hull=0.000, icsd=2, PRIMARY]; SrNbO3 Pnma (62) mp-10339 [hull=0.008, icsd=1, PRIMARY, AMBIGUOUS]
- papers: https://doi.org/10.1007/s00339-014-8515-z (Semiconducting large bandgap oxides as potential thermoelectric materi...) | https://doi.org/10.1016/j.ceramint.2015.01.157 (Effects of Ti addition on properties of Sr2Nb2O7 thermoelectric ceramics) | https://doi.org/10.1557/jmr.2010.78 (Thermoelectric power factor enhancement of textured ferroelectric Sr x...)

## Al-Cu-O
- rank 83 | 99 samples | 19 papers | 32 compositions
- compositions: CuAlO2 (33); CuAl0.9Fe0.1O2 (11); Ca5(CuAlO2)95 (5); Ca2(CuAlO2)98 (5); Sr(CuAlO2)99 (5); Ca(CuAlO2)99 (5)
- dopant candidates (<5% at.): Ca (21), Sr (14), Fe (13), Mg (8), Ni (6), Ag (3), Zn (1), C (1)
- seed hypothesis (confirm): delafossite
- sample form: Bulk (37)
- measured range: 291-1141 K (5th-95th pct of 187 curves; full span incl. outliers 173-1143 K)
- [ref 1] TEDesignLab / ICSD: AlCuO2 R-3m (166) mp-3748 [hull=0.000, icsd=10, PRIMARY]; AlCuO2 P6_3/mmc (194) mp-3098 [hull=0.000, icsd=3]
- [ref 2] MP, ranked by ICSD evidence: Al4Cu2O7 F-43m (216) mp-29225 [hull=0.420, icsd=1, PRIMARY]; Al2CuO4 P3m1 (156) mp-34728 [hull=0.061, PRIMARY, AMBIGUOUS]; AlCuO3 P2_1/c (14) mp-776172 [hull=0.077, PRIMARY]; AlCuO2 C2/m (12) mp-1182995 [hull=0.106]; Al2CuO4 Fd-3m (227) mp-27719 [hull=0.063]
- papers: https://doi.org/10.1016/j.ceramint.2011.12.079 (Effects of mechanical milling on preparation and properties of CuAl1−x...) | https://doi.org/10.1016/j.cap.2014.06.024 (Thermoelectric and optical properties of CuAlO2 synthesized by direct ...) | https://doi.org/10.1016/j.jallcom.2006.07.067 (Improvement in thermoelectric properties of CuAlO2 by adding Fe2O3)

## Cu-Fe-S
- rank 84 | 99 samples | 19 papers | 52 compositions
- compositions: CuFeS2 (20); Zn0.03Cu0.97FeS2 (9); Cu5FeS4 (7); Cu0.95Fe1.05S2 (4); Zn0.05Cu1.95FeS2 (4); Cu5.04Fe0.96S4 (3)
- dopant candidates (<5% at.): Zn (15), Mn (7), Co (6), Se (2), In (1), Si (1)
- seed hypothesis (confirm): chalcopyrite
- sample form: Bulk (51)
- measured range: 11-701 K (5th-95th pct of 411 curves; full span incl. outliers 10-901 K)
- [ref 1] TEDesignLab / ICSD: FeCuS2 I-42d (122) mp-3497 [hull=0.112, icsd=10, PRIMARY]; Fe2CuS3 Pnma (62) mp-605485 [hull=0.086, icsd=9, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Fe(CuS)2 F-43m (216) mp-672708 [hull=0.170, icsd=2, PRIMARY]; FeCu3S4 I-42m (121) mp-1078387 [hull=0.007, icsd=1, PRIMARY]; FeCu3S8 R-3 (148) mp-1224980 [hull=0.017, PRIMARY, AMBIGUOUS]; FeCu5S4 Pm (6) mp-675830 [hull=0.078, PRIMARY]; FeCuS2 P-4m2 (115) mp-640073 [hull=0.111, icsd=1]
- papers: https://doi.org/10.1002/anie.201505517 (Thermoelectricity Generation and Electron-Magnon Scattering in a Natur...) | https://doi.org/10.7567/apex.6.043001 (High Thermoelectric Power Factor in a Carrier-Doped Magnetic Semicondu...) | https://doi.org/10.1039/c4ee02428a (Sulfide bornite thermoelectric material: a natural mineral with ultral...)

## Cu-In-Te
- rank 85 | 98 samples | 25 papers | 57 compositions
- compositions: CuInTe2 (33); Cu0.88Ag0.1InTe2 (3); Cu0.9InTe2 (2); Cu0.95InTe2 (2); CuIn0.9Zn0.1Te2 (2); CuIn0.95Zn0.05Te2 (2)
- dopant candidates (<5% at.): Zn (22), Ni (5), Ag (3), Cd (3), O (2), Ti (2), Mn (2)
- seed hypothesis (confirm): chalcopyrite
- sample form: Bulk (77); Polycrystal (1)
- measured range: 78-860 K (5th-95th pct of 385 curves; full span incl. outliers 10-889 K)
- [ref 1] TEDesignLab / ICSD: InCuTe2 I-42d (122) mp-22261 [hull=0.000, icsd=18, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: In5CuTe8 C2 (5) mp-1224528 [hull=0.000, PRIMARY]; InCuTe2 P-4m2 (115) mp-1224091 [hull=0.009]; InCuTe2 R3m (160) mp-1224060 [hull=0.049]; InCuTe2 P4/mmm (123) mp-1223863 [hull=0.235]
- papers: https://doi.org/10.1002/adma.201400058 (High-Performance Pseudocubic Thermoelectric Materials from Non-cubic C...) | https://doi.org/10.1063/1.4935051 (Tuning the carrier concentration to improve the thermoelectric perform...) | https://doi.org/10.1063/1.3678044 (High-temperature thermoelectric properties of Cu1–xInTe2 with a chalco...)

## Fe-Nb-Sb
- rank 86 | 98 samples | 25 papers | 62 compositions
- compositions: NbFeSb (14); Nb0.95Ti0.05FeSb (8); Nb0.95Hf0.05FeSb (4); Nb0.95Zr0.05FeSb (4); FeNbSb (3); Ti0.15Nb0.85FeSb (3)
- dopant candidates (<5% at.): Ti (30), Hf (26), Zr (12), Ir (8), Co (6), V (4), Ta (3), Sn (3)
- seed hypothesis (confirm): half_heusler
- sample form: Bulk (54); Polycrystal (2)
- measured range: 19-1200 K (5th-95th pct of 362 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NbFeSb F-43m (216) mp-9437 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1039/c4ee03042g (Band engineering of high performance p-type FeNbSb based half-Heusler ...) | https://doi.org/10.1016/s0925-8388(99)00537-x (Thermoelectric properties of ternary transition metal antimonides) | https://doi.org/10.1038/ncomms9144 (Realizing high figure of merit in heavy-band p-type half-Heusler therm...)

## Ir-O-Sr
- rank 87 | 96 samples | 20 papers | 32 compositions
- compositions: SrIrO3 (35); Sr2IrO4 (21); Sr2Ir0.9Rh0.1O4 (3); Sr1.95La0.05IrO4 (3); Sr2Ir0.95Rh0.05O4 (2); Sr2Ir0.8Rh0.2O4 (2)
- dopant candidates (<5% at.): Ca (9), Rh (7), Sn (7), La (5), Ba (4), Eu (3), Ti (1), Pt (1)
- seed hypothesis (confirm): perovskite
- sample form: Bulk (5); Polycrystal (3)
- measured range: 10-398 K (5th-95th pct of 110 curves; full span incl. outliers 10-598 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2IrO4 I4_1/acd (142) mp-4998 [hull=0.000, icsd=8, PRIMARY]; SrIrO3 C2/c (15) mp-1193907 [hull=0.003, icsd=1, PRIMARY]; Sr4IrO6 R-3c (167) mp-9039 [hull=0.000, icsd=1, PRIMARY]; Sr4Ir3O10 I4/mmm (139) mp-1208702 [hull=0.091, PRIMARY]; Sr3Ir2O7 Ccce (68) mp-753375 [hull=0.018, PRIMARY]
- papers: https://doi.org/10.1007/s11664-008-0642-x (Transport Properties and Cationic Substitutions in Sr2IrO4) | https://doi.org/10.1088/0953-8984/20/29/295201 (Insight on the electronic state of Sr2IrO4revealed by cationic substit...) | https://doi.org/10.1038/s41535-020-00286-2 (Quest for quantum states via field-altering technology)

## Mg-Sb
- rank 88 | 93 samples | 27 papers | 57 compositions
- compositions: Mg3Sb2 (31); Mg3.5Sc0.04Sb1.97Te0.03 (3); Mg2.9875Na0.0125Sb2 (2); Mg2.99Ag0.01Sb2 (2); Mg3.2Sb2 (2); Mg3.8Sb2 (2)
- dopant candidates (<5% at.): Te (16), Y (9), Sc (8), Ag (8), Na (4), Sn (4), Bi (3), Pb (3), Cu (2), C (1), Li (1)
- seed hypothesis (confirm): caal2si2_zintl
- sample form: Bulk (85); SingleCrystal (1)
- measured range: 258-860 K (5th-95th pct of 387 curves; full span incl. outliers 10-1053 K)
- [ref 1] TEDesignLab / ICSD: Mg3Sb2 P-3m1 (164) mp-2646 [hull=0.000, icsd=7, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Mg15Sb P-6m2 (187) mp-1023488 [hull=0.038, PRIMARY]; Mg149Sb P-6m2 (187) mp-1185628 [hull=0.000, PRIMARY]; Mg2Sb Immm (71) mp-1185773 [hull=0.114, PRIMARY]; Mg2Sb3 P-3m1 (164) mp-1206370 [hull=0.131, PRIMARY]; Mg3Sb Pm-3m (221) mp-1094724 [hull=0.064, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2015.04.023 (Thermoelectric properties of Na-doped Zintl compound: Mg 3− x Na x Sb 2) | https://doi.org/10.1016/j.jallcom.2009.04.130 (Transport and thermoelectric properties of nanocrystal substitutional ...) | https://doi.org/10.1007/s11664-012-2417-7 (On the Thermoelectric Properties of Zintl Compounds Mg3Bi2−x Pn x (Pn ...)

## Sb-Yb
- rank 89 | 93 samples | 31 papers | 57 compositions
- compositions: Yb14MnSb11 (18); Yb14MgSb11 (7); Yb14Mn1.05Sb11 (4); Yb4Sb3 (3); Yb11GaSb9 (3); Yb10LaCdSb9 (2)
- dopant candidates (<5% at.): Mn (50), Mg (15), Al (13), Zn (8), La (7), Pr (4), Sm (4), Bi (4), Lu (3), Ga (3), Fe (3), Cd (2), Ge (2), Ca (2), Ba (2), In (1), Y (1)
- sample form: Bulk (37); SingleCrystal (8); pellets (2)
- measured range: 295-1285 K (5th-95th pct of 331 curves; full span incl. outliers 11-1327 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbSb Fm-3m (225) mp-1916 [hull=0.269, icsd=5, PRIMARY]; Yb4Sb3 I-43d (220) mp-1295 [hull=0.000, icsd=3, PRIMARY]; Yb5Sb3 P6_3/mcm (193) mp-201 [hull=0.000, icsd=2, PRIMARY, AMBIGUOUS]; YbSb2 Cmcm (63) mp-7138 [hull=0.000, icsd=2, PRIMARY]; Yb11Sb10 I4/mmm (139) mp-17402 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1002/aenm.201400348 (Improved Bulk Materials with Thermoelectric Figure-of-Merit Greater th...) | https://doi.org/10.1002/adfm.200800298 (Traversing the Metal-Insulator Transition in a Zintl Phase: Rational E...) | https://doi.org/10.1143/apex.5.031801 (Improved Thermoelectric Properties in Lu-doped Yb$_{14}$MnSb$_{11}$ Zi...)

## Te
- rank 90 | 92 samples | 17 papers | 47 compositions
- compositions: Te (33); Te0.98As0.02 (8); SnSeTe30 (4); Te98.4Se1.6 (2); Te99.6Se0.4 (2); Te97Se3 (2)
- dopant candidates (<5% at.): Se (19), Bi (17), Sb (15), As (15), Sn (4), Ag (4), O (1)
- seed hypothesis (confirm): trigonal_te
- sample form: Bulk (24); Film (6); Polycrystal (4)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 19-925 K (5th-95th pct of 235 curves; full span incl. outliers 10-1080 K)
  !! MEASUREMENT CROSSES A TRANSITION: trigonal_te -> melt/decomposition at ~723 K (Melts at ~723 K, inside the range of many high-T runs.)
     Record each phase with its own temperature range, not a single prototype.
- [ref 1] TEDesignLab / ICSD: Te P3_121 (152) mp-19 [hull=0.000, icsd=20, PRIMARY]; Te (154)
- [ref 2] MP, ranked by ICSD evidence: Te Pm-3m (221) mp-10654 [hull=0.044, icsd=2]; Te P2_12_12 (18) mp-1064307 [hull=0.121, icsd=2]; Te Pmma (51) mp-105 [hull=0.042, icsd=1]; Te Cmmm (65) mp-9924 [hull=0.151, icsd=1]; Te Pmc2_1 (26) mp-1178952 [hull=0.038]
- papers: https://doi.org/10.1016/j.jallcom.2015.06.127 (Structure and thermoelectric properties of Bi–Te alloys obtained by no...) | https://doi.org/10.1002/pssc.201300192 (Galvanomagnetic and thermoelectric properties of Te doped single-cryst...) | https://doi.org/10.1007/bf00891150 (Effect of selenium on the thermoelectric properties of tellurium)

## Ba-Fe-O
- rank 91 | 91 samples | 31 papers | 62 compositions
- compositions: BaNb0.05Fe0.95O3 (8); Ba0.95La0.05FeO3 (6); BaFeO3 (6); Ba2Fe2O5 (4); BaFe0.9Y0.1O3 (3); Ba0.95La0.05Fe0.9Nb0.1O3 (2)
- dopant candidates (<5% at.): La (17), Nb (16), Y (13), Ce (11), Zr (8), In (6), Pr (6), Ni (5), Co (4), Sr (4), Cu (4), Nd (3), Zn (3), Ca (2), Al (2), Gd (1), Sm (1), Ti (1)
- seed hypothesis (confirm): perovskite
- sample form: rod-shaped (15); Bulk (3); disk (2)
- measured range: 298-1224 K (5th-95th pct of 96 curves; full span incl. outliers 296-1374 K)
- [ref 1] TEDesignLab / ICSD: BaFe4O7 (176) [PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: BaFeO3 Pm-3m (221) mp-19035 [hull=0.000, icsd=5, PRIMARY]; Ba(FeO2)2 Cmc2_1 (36) mp-19154 [hull=0.000, icsd=2, PRIMARY]; Ba2Fe2O5 P2_1/c (14) mp-654312 [hull=0.000, icsd=1, PRIMARY]; Ba2Fe6O11 Pnnm (58) mp-652683 [hull=0.002, icsd=1, PRIMARY]; Ba4Fe9O20 C2/m (12) mp-1182448 [hull=0.066, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/s10854-012-1020-2 (New promising Co-free thermoelectric ceramic based on Ba–Fe–oxide) | https://doi.org/10.1088/2053-1591/aad10e (Variation in electrical conductivity of A<sub>2</sub>Fe<sub>2</sub>O<s...) | https://doi.org/10.1016/j.materresbull.2016.09.007 (Synthesis and characterization of the oxygen-deficient perovskite BaFe...)

## Ge-Pb-Te
- rank 92 | 91 samples | 20 papers | 67 compositions
- compositions: Ge0.87Pb0.13Te (10); Ge0.76Sb0.08Pb0.12Te (8); Ge0.86Pb0.1Bi0.04Te (6); Pb0.988Sb0.012Te(GeTe)0.13 (2); Ge0.4Pb0.6Te (2); Ge0.55Pb0.45Te (2)
- dopant candidates (<5% at.): Bi (27), Sb (13), Yb (9), Mn (3), I (1), Ag (1), Sm (1)
- seed hypothesis (confirm): gete_rhombohedral
- sample form: Bulk (56); Composite (1); Polycrystal (1)
- solid-solution axis: Ge/(Ge+Pb) spans 0.11-0.90 (median 0.82) over 67 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 200-784 K (5th-95th pct of 365 curves)
  !! MEASUREMENT CROSSES A TRANSITION: gete_rhombohedral -> rocksalt at ~700 K (R3m -> Fm-3m, ~700 K; shifts with Ge vacancy content and doping.)
     Record each phase with its own temperature range, not a single prototype.
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GeTe2Pb P4/mmm (123) mp-1224318 [hull=0.079, PRIMARY]; GeTe4Pb3 P4/mmm (123) mp-1224448 [hull=0.043, PRIMARY]; GeTe5Pb4 R-3m (166) mp-1224514 [hull=0.026, PRIMARY]
- papers: https://doi.org/10.1002/aenm.201200970 (Controlling Metallurgical Phase Separation Reactions of the Ge0.87Pb0....) | https://doi.org/10.1016/j.intermet.2014.09.004 (Phases and thermoelectric properties of Ge1−x(Pb0.9Yb0.1)xTe alloys) | https://doi.org/10.1016/j.jallcom.2013.09.104 (Enhanced thermoelectric properties of (Pb1−xYbxTe)0.15(GeTe)0.85 compo...)

## Cu-O
- rank 93 | 89 samples | 9 papers | 31 compositions
- compositions: CuO (9); Cu0.94Ni0.05Li0.01O (7); Al0.03(CuO)0.97 (5); Al0.005(CuO)0.995 (5); Cu0.92Ni0.05Li0.03O (5); Cu0.92Zn0.05Li0.03O (5)
- dopant candidates (<5% at.): Li (34), Al (20), Ni (16), Zn (14), C (3), Se (3), Cl (3), Bi (3), Na (1), K (1), Mn (1)
- seed hypothesis (confirm): tenorite, cuprite  <-- MIXED, split per composition
- sample form: Bulk (11)
- measured range: 18-1250 K (5th-95th pct of 131 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuO P4_2/mmc (131) mp-1692 [hull=0.000, icsd=29, PRIMARY, AMBIGUOUS]; Cu2O Pn-3m (224) mp-361 [hull=0.000, icsd=17, PRIMARY]; CuO2 Cmcm (63) mp-1181499 [hull=0.193, icsd=5, PRIMARY]; Cu4O3 I4_1/amd (141) mp-1478 [hull=0.010, icsd=2, PRIMARY]; Cu8O Amm2 (38) mp-704745 [hull=0.179, icsd=1, PRIMARY]
- papers: https://doi.org/10.7567/jjap.52.031102 (Thermoelectric Properties of Li-Doped CuO) | https://doi.org/10.1016/j.jallcom.2010.09.089 (Synthesis and characterization of cuprous oxide dendrites: New simplif...) | https://doi.org/10.1557/opl.2012.1571 (Thermoelectric properties of Li-doped Cu0.95-x M0.05Li x O (M=Mn, Ni, Zn))

## O-Sn
- rank 94 | 89 samples | 15 papers | 30 compositions
- compositions: SnO2 (20); Sn0.99Sb0.01O2 (13); Sn0.97Sb0.03O2 (12); Sn0.95Sb0.05O2 (8); Sn0.98Sb0.02O2 (4); Sn0.96Sb0.04O2 (4)
- dopant candidates (<5% at.): Sb (51), Ta (5), Ti (4), F (3), Zn (3), Co (3), Cu (1), Fe (1), In (1), Ga (1), Al (1)
- seed hypothesis (confirm): rutile
- sample form: Film (4)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 24-1074 K (5th-95th pct of 112 curves)
- [ref 1] TEDesignLab / ICSD: SnO2 P4_2/mnm (136) mp-856 [hull=0.000, icsd=44, PRIMARY]; SnO P4/nmm (129) mp-2097 [hull=0.000, icsd=5, PRIMARY]; SnO2 Pa-3 (205) mp-697 [hull=0.100, icsd=7]; SnO Cmc2_1 (36) mp-1078644 [hull=0.126, icsd=1]; SnO2 (58)
- [ref 2] MP, ranked by ICSD evidence: Sn3O4 P4/mnc (128) mp-1179450 [hull=0.357, icsd=1, PRIMARY]; Sn3O8 Immm (71) mp-1219002 [hull=0.450, PRIMARY]; Sn2O P4/mmm (123) mp-1206688 [hull=0.407, PRIMARY]; Sn5O6 P2_1/c (14) mp-978114 [hull=0.000, PRIMARY]; SnO2 Fm-3m (225) mp-12979 [hull=0.245, icsd=4]
- papers: https://doi.org/10.1016/j.jallcom.2007.09.001 (Thermoelectric properties of Sn1−x−yTiySbxO2 ceramics) | https://doi.org/10.1063/1.4891855 (Linear temperature behavior of thermopower and strong electron-electro...) | https://doi.org/10.1007/s11664-010-1506-8 (Thermoelectric Properties of SnO2 Ceramics Doped with Sb and Zn)

## Pb-S-Te
- rank 95 | 88 samples | 19 papers | 67 compositions
- compositions: K0.025Pb1Te0.7S0.3 (3); Pb0.98Na0.02Te0.88S0.12 (3); (PbTe)0.28(PbS)0.72 (2); K0.005Pb1Te0.7S0.3 (2); Pb0.98In0.02Te0.8S0.2 (2); (PbTe)94(PbSnS2)6(PbI2)0.055 (2)
- dopant candidates (<5% at.): Na (28), K (14), Sb (11), Cl (7), Se (7), Sn (6), I (6), In (5), Bi (3), Tl (2), Ag (2)
- seed hypothesis (confirm): rocksalt
- sample form: Bulk (22); pellets (5)
- solid-solution axis: S/(S+Te) spans 0.10-0.84 (median 0.20) over 67 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 295-924 K (5th-95th pct of 306 curves; full span incl. outliers 81-958 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TePb2S R-3m (166) mp-1217283 [hull=0.022, PRIMARY]; TePb2S P4/mmm (123) mp-1217286 [hull=0.088]
- papers: https://doi.org/10.1021/nn305971v (Core–Shell Nanoparticles As Building Blocks for the Bottom-Up Producti...) | https://doi.org/10.1039/c1ee01895g (Combining alloy scattering of phonons and resonant electronic levels t...) | https://doi.org/10.1039/c2ee22495j (PbTe–PbSnS2 thermoelectric composites: low lattice thermal conductivit...)

## O-U
- rank 96 | 87 samples | 22 papers | 33 compositions
- compositions: UO2 (43); (Gd2O3)7.64(UO2)92.36 (9); (UO2)93.07(Gd2O3)6.93 (3); Mg0.05U0.95O2 (2); Mg0.15U0.85O2 (2); (U0.99Dy0.01)O2 (1)
- dopant candidates (<5% at.): Gd (15), Dy (5), Pu (5), Mg (4), Al (1), Ce (1)
- seed hypothesis (confirm): fluorite_oxide
- sample form: Bulk (27); pellets (1)
- measured range: 238-2773 K (5th-95th pct of 98 curves; full span incl. outliers 88-2977 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UO2 Fm-3m (225) mp-1597 [hull=0.000, icsd=28, PRIMARY]; U3O8 P-62m (189) mp-308 [hull=0.000, icsd=8, PRIMARY]; UO3 I4_1/amd (141) mp-294 [hull=0.087, icsd=6, PRIMARY]; UO4 Pbca (61) mp-1178859 [hull=0.362, icsd=2, PRIMARY]; UO Fm-3m (225) mp-7830 [hull=0.221, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/s0022-3115(99)00273-1 (Thermophysical properties of uranium dioxide) | https://doi.org/10.1016/0022-3115(91)90384-j (Fabrication of high density UO2 fuel pellets involving sol-gel microsp...) | https://doi.org/10.1016/j.jnucmat.2005.10.009 (Thermal conductivity and acid dissolution behavior of MgO–ZrO2 ceramic...)

## Ag-Se
- rank 97 | 86 samples | 24 papers | 35 compositions
- compositions: Ag2Se (46); Ag2.001Se1.01 (5); Ag2.0027Se (2); Ag2.0006Se (2); AgSb0.02Ba0.02Se2 (1); Ag1.9Se1.1 (1)
- dopant candidates (<5% at.): Cu (5), Sb (1), Ba (1), P (1), Hg (1), Sn (1), S (1), Te (1)
- seed hypothesis (confirm): ag2se_naumannite, bcc_superionic  <-- MIXED, split per composition
- sample form: Bulk (38); Film (18); Powder (1); Module (1)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 23-674 K (5th-95th pct of 285 curves; full span incl. outliers 10-723 K)
  !! MEASUREMENT CROSSES A TRANSITION: ag2se_naumannite -> bcc_superionic at ~406 K (P212121 -> bcc superionic, ~406 K. Ag2Te transforms near ~418 K.)
     Record each phase with its own temperature range, not a single prototype.
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AgSe F-43m (216) mp-379 [hull=0.139, icsd=2, PRIMARY]; AgSe5 Cc (9) mp-1101086 [hull=0.109, icsd=1, PRIMARY]; Ag3Se P6_3/mmc (194) mp-1183249 [hull=0.076, PRIMARY]; Ag2Se P2_12_12_1 (19) mp-754954 [hull=0.006, PRIMARY]; Ag2Se Fm-3m (225) mp-1229100 [hull=0.034]
- papers: https://doi.org/10.1021/acsami.5b06492 (Contrasting the Role of Mg and Ba Doping on the Microstructure and The...) | https://doi.org/10.1063/1.4824353 (Enhanced thermoelectric performance in the very low thermal conductivi...) | https://doi.org/10.1063/1.2429727 (Effect of nonstoichiometry on the thermoelectric properties of a Ag2Se...)

## C-Si
- rank 98 | 85 samples | 23 papers | 34 compositions
- compositions: SiC (43); Si1.1C (3); SiC0.7 (3); Si1.23C (3); SiCN0.002 (2); Al0.015SiC (2)
- dopant candidates (<5% at.): Al (23), B (14), N (6), O (1)
- seed hypothesis (confirm): sic_polytype
- sample form: Bulk (43); Film (6); Wire (3)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- solid-solution axis: C/(C+Si) spans 0.41-0.93 (median 0.50) over 34 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 75-1280 K (5th-95th pct of 170 curves; full span incl. outliers 11-2073 K)
- [ref 1] TEDesignLab / ICSD: SiC F-43m (216) mp-8062 [hull=0.001, icsd=10, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Si8C3 P-1 (2) mp-1179504 [hull=0.561, icsd=1, PRIMARY]; SiC2 Pa-3 (205) mp-1102811 [hull=0.981, icsd=1, PRIMARY]; Si5C3 R3 (146) mp-1219306 [hull=0.873, PRIMARY]; Si8HgC18 P-1 (2) mp-1219839 [hull=1.378, PRIMARY]; SiC3 I4/mmm (139) mp-972848 [hull=2.330, PRIMARY]
- papers: https://doi.org/10.1134/s0020168506110069 (Thermoelectric properties of vapor-grown polycrystalline cubic SiC) | https://doi.org/10.1007/s11664-010-1129-0 (Preparation and Thermoelectric Characterization of SiC-B4C Composites) | https://doi.org/10.1007/bf01689320 (Thermoelectric energy conversion by porous SiC ceramics)

## Bi-Ca-Co-O
- rank 99 | 84 samples | 29 papers | 43 compositions
- compositions: Bi2Ca2Co1.7O8 (23); Bi1.68Ca2O4(CoO2)1.6 (6); Bi2Ca2Co2O8 (4); Bi1.5Pb0.5Ca2Co2O8 (4); Bi2.5Ca2.5Co2O10 (3); (Bi2Ca2CoO6) (2)
- dopant candidates (<5% at.): Pb (17), Nd (5), Ag (5), Sc (4), Y (4), Sr (2), Cu (2), La (2), Al (1)
- seed hypothesis (confirm): misfit_cobaltite
- sample form: Bulk (37); SingleCrystal (3); OrientedBulk (1)
- measured range: 11-1073 K (5th-95th pct of 195 curves)
- papers: https://doi.org/10.1063/1.4801644 (Exotic reinforcement of thermoelectric power driven by Ca doping in la...) | https://doi.org/10.3989/cyv.242014 (Processing effects on the thermoelectric properties of Bi<sub>2</sub>C...) | https://doi.org/10.1016/j.ceramint.2015.01.070 (The effect of environmental conditions on the mechanical and thermoele...)

## Cu-S-Sn
- rank 100 | 84 samples | 26 papers | 43 compositions
- compositions: Cu26V2Sn6S32 (18); Cu2SnS3 (11); Cu4Sn7S16 (6); Cu24Zn2V2Sn6S32 (2); Cu2Sn0.9In0.1S3 (2); Cu4SnS4 (2)
- dopant candidates (<5% at.): V (26), Fe (11), In (7), Zn (5), Co (3), Se (2), Cl (2), Ni (2), Ta (1), Nb (1)
- seed hypothesis (confirm): colusite
- sample form: Bulk (72)
- measured range: 78-792 K (5th-95th pct of 385 curves; full span incl. outliers 10-896 K)
- [ref 1] TEDesignLab / ICSD: Cu2SnS3 Cc (9) mp-10519 [hull=0.000, icsd=2, PRIMARY]; Cu4SnS4 (62) [PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Cu(SnS2)4 F-43m (216) mp-1184041 [hull=0.018, PRIMARY]; Cu4Sn15S32 Cm (8) mp-685340 [hull=0.062, PRIMARY]; Cu4Sn7S16 R3m (160) mp-675137 [hull=0.013, PRIMARY]; Cu2SnS3 Imm2 (44) mp-1225832 [hull=0.000]; Cu2SnS3 Fdd2 (43) mp-1225965 [hull=0.002]
- papers: https://doi.org/10.1063/1.4896998 (High-performance thermoelectric minerals: Colusites Cu26V2M6S32 (M = G...) | https://doi.org/10.1021/ic401310c (Enhanced Thermoelectric Figure of Merit in Stannite–Kuramite Solid Sol...) | https://doi.org/10.1016/j.jallcom.2005.09.030 (Crystal structure, electronic structure and thermoelectric properties ...)
