# Host systems -- chunk 058 of 73

Ranks 2851-2900 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 98.56%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Ca-Lu-Sb
- rank 2851 | 1 samples | 1 papers | 1 compositions
- compositions: CaLuSb3 (1)
- measured range: 300-598 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1021/acs.chemmater.1c03300 (Synthesis and Transport Properties of the Family of Zintl Phases Ca<su...)

## Ca-Mn-Mo-O
- rank 2852 | 1 samples | 1 papers | 1 compositions
- compositions: Ca2MnMoO6 (1)
- measured range: 18-306 K (5th-95th pct of 2 curves; full span incl. outliers 18-819 K)
- papers: https://doi.org/10.1063/1.1728294 (Effect of alkaline-earth and transition metals on the electrical trans...)

## Ca-Mn-O-Sm
- rank 2853 | 1 samples | 1 papers | 1 compositions
- compositions: Ca0.75Sm0.25MnO3 (1)
- measured range: 773-1073 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca3SmMn4O12 Pm (6) mp-1227761 [hull=0.009, PRIMARY]; CaSmMn2O6 Pmn2_1 (31) mp-1227151 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1007/s13391-015-5198-3 (Enhanced thermoelectric properties of Ca1-x Sm x Mn1-y W y O3-δ for po...)

## Ca-Mn-O-Ti
- rank 2854 | 1 samples | 1 papers | 1 compositions
- compositions: La0.1Ca0.9Mn0.7Ti0.3O3 (1)
- dopant candidates (<5% at.): La (1)
- measured range: 509-950 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca2TiMnO6 I4/m (87) mp-1080507 [hull=0.022, icsd=1, PRIMARY]; CaTi2MnO6 P4_2mc (105) mp-1194928 [hull=0.015, icsd=1, PRIMARY]; Ca2TiMnO6 P2_1/c (14) mp-1227706 [hull=0.008]
- papers: https://doi.org/10.1006/jssc.1996.0334 (Role of Tetravalent Ion in Metal–Insulator Transition in (La0.1Ca0.9)(...)

## Ca-O-Os
- rank 2855 | 1 samples | 1 papers | 1 compositions
- compositions: CaOsO3 (1)
- measured range: 11-396 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca2Os2O7 Imma (74) mp-2923 [hull=0.000, icsd=4, PRIMARY]; CaOsO3 Pnma (62) mp-1213970 [hull=0.088, PRIMARY]; CaOsO3 Pm-3m (221) mp-1016900 [hull=0.253]
- papers: https://doi.org/10.1021/ja4074408 (High-Pressure Synthesis of 5d Cubic Perovskite BaOsO<sub>3</sub> at 17...)

## Ca-O-Pr-Sb
- rank 2856 | 1 samples | 1 papers | 1 compositions
- compositions: Ca2Pr7Sb5O5 (1)
- measured range: 11-370 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca3Pr2Sb3O14 C2/m (12) mp-1214039 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2016.04.015 (Investigation of the transport properties and compositions of the Ca2R...)

## Ca-O-Re
- rank 2857 | 1 samples | 1 papers | 1 compositions
- compositions: Ca2Re2O7 (1)
- measured range: 26-242 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca(ReO5)2 C2/c (15) mp-1198612 [hull=0.186, icsd=2, PRIMARY]; Ca11(ReO6)4 I4_1 (80) mp-29532 [hull=0.000, icsd=1, PRIMARY]; Ca3ReO6 P2_1/c (14) mp-9457 [hull=0.000, icsd=1, PRIMARY]; Ca(ReO5)2 Cc (9) mp-1199701 [hull=0.190, icsd=1]
- papers: https://doi.org/10.1103/physrevb.83.125103 (Structural and electronic properties of pyrochlore-type<mml:math xmlns...)

## Ca-O-Sb-Sm
- rank 2858 | 1 samples | 1 papers | 1 compositions
- compositions: Ca2Sm7Sb5O5 (1)
- measured range: 10-372 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/j.jssc.2016.04.015 (Investigation of the transport properties and compositions of the Ca2R...)

## Ca-O-Sn
- rank 2859 | 1 samples | 1 papers | 1 compositions
- compositions: Ca3SnO (1)
- measured range: 11-295 K (5th-95th pct of 4 curves)
- [ref 1] TEDesignLab / ICSD: CaSnO3 Pnma (62) mp-4438 [hull=0.014, icsd=11, PRIMARY]; Ca2SnO4 Pbam (55) mp-4747 [hull=0.000, icsd=2, PRIMARY]; CaSnO3 R-3 (148) mp-4190 [hull=0.000, icsd=2]; CaSnO3 (225)
- [ref 2] MP, ranked by ICSD evidence: Ca3SnO Pm-3m (221) mp-29241 [hull=0.000, icsd=3, PRIMARY]; CaSnO6 Pn-3 (201) mp-1201737 [hull=0.692, icsd=1, PRIMARY]; CaSnO3 Pm-3m (221) mp-7986 [hull=0.195, icsd=4]; CaSnO6 Pn-3m (224) mp-1197808 [hull=0.762, icsd=1]; CaSnO3 P-1 (2) mp-1182670 [hull=0.557]
- papers: https://doi.org/10.1063/1.4952393 (Thermoelectric properties of antiperovskite calcium oxides Ca3PbO and ...)

## Ca-O-Sr
- rank 2860 | 1 samples | 1 papers | 1 compositions
- compositions: CaSrO3 (1)
- measured range: 18-297 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr3CaO4 Pm-3m (221) mp-1079940 [hull=0.034, icsd=1, PRIMARY]; SrCa3O4 Pm-3m (221) mp-978844 [hull=0.040, icsd=1, PRIMARY]; SrCaO2 P4/mmm (123) mp-1017988 [hull=0.049, icsd=1, PRIMARY]; SrCaO3 Pm-3m (221) mp-978842 [hull=0.456, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.103.205109 (Separated transport relaxation scales and interband scattering in thin...)

## Ca-Pb-S
- rank 2861 | 1 samples | 1 papers | 1 compositions
- compositions: PbS0.9Cl0.1CaS (1)
- dopant candidates (<5% at.): Cl (1)
- measured range: 305-734 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/j.jallcom.2015.10.052 (High performance thermoelectrics from earth-abundant materials: Enhanc...)

## Ca-Sb-Sm
- rank 2862 | 1 samples | 1 papers | 1 compositions
- compositions: Ca3SmSb3 (1)
- measured range: 300-599 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1021/acs.chemmater.1c03300 (Synthesis and Transport Properties of the Family of Zintl Phases Ca<su...)

## Ca-Sb-Tb
- rank 2863 | 1 samples | 1 papers | 1 compositions
- compositions: Ca3TbSb3 (1)
- measured range: 300-579 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1021/acs.chemmater.1c03300 (Synthesis and Transport Properties of the Family of Zintl Phases Ca<su...)

## Cd-Co-O
- rank 2864 | 1 samples | 1 papers | 1 compositions
- compositions: Ag0.15Cd2.9Ca0.1Co4O9 (1)
- dopant candidates (<5% at.): Ag (1), Ca (1)
- measured range: 374-957 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cd(CoO2)2 Fd-3m (227) mp-771736 [hull=0.000, PRIMARY]; Cd6(CoO3)5 R32 (155) mp-769964 [hull=0.084, PRIMARY]; CdCoO3 R-3 (148) mp-770662 [hull=0.034, PRIMARY, AMBIGUOUS]; Cd(CoO2)2 I4_1/amd (141) mp-1178498 [hull=0.065]; Cd(CoO2)2 P1 (1) mp-769705 [hull=0.122]
- papers: https://doi.org/10.1021/acsami.9b13607 (Filiform Metal Silver Nanoinclusions To Enhance Thermoelectric Perform...)

## Cd-Cu-Eu-Sb
- rank 2865 | 1 samples | 1 papers | 1 compositions
- compositions: Eu9Cd3.8Cu1.5Sb9 (1)
- measured range: 297-775 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1021/acs.chemmater.5b03808 (Coinage-Metal-Stuffed Eu9Cd4Sb9: Metallic Compounds with Anomalous Low...)

## Cd-Cu-Mn-Se-Sn
- rank 2866 | 1 samples | 1 papers | 1 compositions
- compositions: Cu2Cd0.5Mn0.5SnSe4 (1)
- measured range: 300-722 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnCdCu4(SnSe4)2 C2 (5) mp-1221832 [hull=0.004, PRIMARY]
- papers: https://doi.org/10.1038/srep05774 (Enhanced Thermoelectric Performance of Cu2CdSnSe4 by Mn Doping: Experi...)

## Cd-Cu-Yb
- rank 2867 | 1 samples | 1 papers | 1 compositions
- compositions: YbCdCu4 (1)
- measured range: 12-124 K (5th-95th pct of 2 curves; full span incl. outliers 12-291 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb5CdCu2 I4/mcm (140) mp-1190072 [hull=0.000, icsd=1, PRIMARY]; YbCdCu4 F-43m (216) mp-12009 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevmaterials.8.013401 (Revisiting the heavy-fermion compound \n<mml:math xmlns:mml=\"http://w...)

## Cd-Er
- rank 2868 | 1 samples | 1 papers | 1 compositions
- compositions: Cd83.7Er16.3 (1)
- measured range: 17-295 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ErCd Pm-3m (221) mp-867 [hull=0.000, icsd=4, PRIMARY]; ErCd2 C2/m (12) mp-1062169 [hull=0.431, icsd=2, PRIMARY]; Er11Cd45 F-43m (216) mp-1204723 [hull=0.020, icsd=1, PRIMARY]; ErCd3 Cmcm (63) mp-7303 [hull=0.000, icsd=1, PRIMARY]; ErCd6 Immm (71) mp-1227922 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1080/14786435.2010.544685 (Low-temperature structural stability of Cd6M(M = Ho, Er, Tm and Lu) cu...)

## Cd-Ga-Te
- rank 2869 | 1 samples | 1 papers | 1 compositions
- compositions: Cd0.89Ga0.11Te (1)
- measured range: 10-300 K (5th-95th pct of 2 curves; full span incl. outliers 10-390 K)
- [ref 1] TEDesignLab / ICSD: Cd(GaTe2)2 I-4 (82) mp-13949 [hull=0.000, icsd=4, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Cd(Ga3Te5)2 C2 (5) mp-36641 [hull=0.004, PRIMARY]; Cd3(GaTe3)2 C2 (5) mp-1226989 [hull=0.025, PRIMARY]
- papers: https://doi.org/10.1016/j.jcrysgro.2011.12.048 (Structural analysis, growth and characterization of cadmium gallium te...)

## Cd-Gd
- rank 2870 | 1 samples | 1 papers | 1 compositions
- compositions: GdCd (1)
- measured range: 99-292 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdCd Pm-3m (221) mp-1031 [hull=0.000, icsd=6, PRIMARY]; GdCd2 P6/mmm (191) mp-20965 [hull=0.000, icsd=2, PRIMARY]; GdCd3 P6_3/mmc (194) mp-22138 [hull=0.000, icsd=1, PRIMARY]; Gd3Cd P6_3/mmc (194) mp-1184421 [hull=0.060, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(88)90183-7 (Electrical and thermoelectric transport properties of RZn and RCd comp...)

## Cd-Ge-Te-Tl
- rank 2871 | 1 samples | 1 papers | 1 compositions
- compositions: Tl2CdGeTe4 (1)
- measured range: 81-300 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1021/cm0518067 (Tl2AXTe4(A = Cd, Hg, Mn; X = Ge, Sn):  Crystal Structure, Electronic S...)

## Cd-Ho
- rank 2872 | 1 samples | 1 papers | 1 compositions
- compositions: Cd83.7Ho16.3 (1)
- measured range: 18-300 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HoCd Pm-3m (221) mp-170 [hull=0.000, icsd=2, PRIMARY]; HoCd2 P6/mmm (191) mp-11301 [hull=0.000, icsd=1, PRIMARY]; Ho11Cd45 F-43m (216) mp-1197508 [hull=0.016, icsd=1, PRIMARY]; HoCd3 Cmcm (63) mp-11302 [hull=0.000, icsd=1, PRIMARY]; HoCd6 Immm (71) mp-1225485 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1080/14786435.2010.544685 (Low-temperature structural stability of Cd6M(M = Ho, Er, Tm and Lu) cu...)

## Cd-In-O
- rank 2873 | 1 samples | 1 papers | 1 compositions
- compositions: CdIn2O4 (1)
- measured range: 300-387 K (5th-95th pct of 1 curves)
- [ref 1] TEDesignLab / ICSD: CdIn2O4 Fd-3m (227) mp-19803 [hull=0.000, icsd=3, PRIMARY]; CdIn2O4 (141)
- [ref 2] MP, ranked by ICSD evidence: CdIn2O4 Imma (74) mp-675464 [hull=0.078]
- papers: https://doi.org/10.1016/0040-6090(87)90207-0 (Preparation, electrical properties and optical characterization of Cd2...)

## Cd-Lu
- rank 2874 | 1 samples | 1 papers | 1 compositions
- compositions: Cd83.7Lu16.3 (1)
- measured range: 18-296 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LuCd Pm-3m (221) mp-2217 [hull=0.000, icsd=2, PRIMARY]; Lu11Cd45 F-43m (216) mp-1199571 [hull=0.034, icsd=1, PRIMARY]; LuCd2 P-3m1 (164) mp-1062310 [hull=0.003, icsd=1, PRIMARY]; LuCd3 Cmcm (63) mp-11306 [hull=0.000, icsd=1, PRIMARY]; Lu3Cd Pm-3m (221) mp-1185440 [hull=0.071, PRIMARY]
- papers: https://doi.org/10.1080/14786435.2010.544685 (Low-temperature structural stability of Cd6M(M = Ho, Er, Tm and Lu) cu...)

## Cd-Mg-O
- rank 2875 | 1 samples | 1 papers | 1 compositions
- compositions: Cd0.89Mg0.11O (1)
- measured range: 320-1003 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg3CdO4 Pm-3m (221) mp-1099255 [hull=0.129, PRIMARY]
- papers: https://doi.org/10.1016/j.matchemphys.2016.02.069 (Tuning of the microstructure and thermoelectric properties of CdO cera...)

## Cd-Nd
- rank 2876 | 1 samples | 1 papers | 1 compositions
- compositions: NdCd (1)
- measured range: 12-281 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NdCd Pm-3m (221) mp-991061 [hull=0.000, icsd=3, PRIMARY]; Nd11Cd45 F-43m (216) mp-1205000 [hull=0.012, icsd=1, PRIMARY]; NdCd11 Pm-3m (221) mp-1198736 [hull=0.000, icsd=1, PRIMARY]; NdCd2 P-3m1 (164) mp-1062206 [hull=0.473, icsd=1, PRIMARY]; Nd3Cd P6_3/mmc (194) mp-1186265 [hull=0.056, PRIMARY, AMBIGUOUS]
- papers: https://doi.org/10.1016/0304-8853(88)90183-7 (Electrical and thermoelectric transport properties of RZn and RCd comp...)

## Cd-O-Ru
- rank 2877 | 1 samples | 1 papers | 1 compositions
- compositions: Cd2Ru2O7 (1)
- measured range: 30-396 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CdRuO3 Pm-3m (221) mp-1016849 [hull=0.336, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/14/5/102 (Fluctuation effects on the physical properties of Cd<sub>2</sub>Re<sub...)

## Cd-Pr
- rank 2878 | 1 samples | 1 papers | 1 compositions
- compositions: PrCd (1)
- measured range: 12-190 K (5th-95th pct of 2 curves; full span incl. outliers 12-241 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrCd Pm-3m (221) mp-646 [hull=0.000, icsd=6, PRIMARY]; PrCd2 P6/mmm (191) mp-2324 [hull=0.000, icsd=3, PRIMARY]; Pr11Cd45 F-43m (216) mp-1204245 [hull=0.014, icsd=1, PRIMARY]; PrCd11 Pm-3m (221) mp-1201245 [hull=0.000, icsd=1, PRIMARY]; Pr3Cd I4/mmm (139) mp-975641 [hull=0.056, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(88)90183-7 (Electrical and thermoelectric transport properties of RZn and RCd comp...)

## Cd-Se
- rank 2879 | 1 samples | 1 papers | 1 compositions
- compositions: CdSe (1)
- measured range: 77-437 K (5th-95th pct of 1 curves)
- [ref 1] TEDesignLab / ICSD: CdSe P6_3mc (186) mp-1070 [hull=0.001, icsd=25, PRIMARY]; CdSe2 Pa-3 (205) mp-1095493 [hull=0.081, icsd=1, PRIMARY]; CdSe F-43m (216) mp-2691 [hull=0.000, icsd=10]
- [ref 2] MP, ranked by ICSD evidence: Cd3Se4 Cm (8) mp-1232349 [hull=0.096, PRIMARY]; Cd3Se I4/mmm (139) mp-1183665 [hull=0.271, PRIMARY]; CdSe Fm-3m (225) mp-1055 [hull=0.146, icsd=4]
- papers: https://doi.org/10.1016/0254-0584(87)90087-3 (DC galvanomagnetic and thermoelectric effects in an undoped single cry...)

## Cd-Sm
- rank 2880 | 1 samples | 1 papers | 1 compositions
- compositions: Cd6Sm_IAC (1)
- measured range: 10-29 K (5th-95th pct of 2 curves; full span incl. outliers 10-298 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SmCd Pm-3m (221) mp-572 [hull=0.000, icsd=4, PRIMARY]; SmCd2 P6/mmm (191) mp-30495 [hull=0.000, icsd=1, PRIMARY]; SmCd11 Pm-3m (221) mp-1203399 [hull=0.000, icsd=1, PRIMARY]; Sm3Cd P6_3/mmc (194) mp-979339 [hull=0.062, PRIMARY, AMBIGUOUS]; SmCd3 P6_3/mmc (194) mp-979465 [hull=0.000, PRIMARY, AMBIGUOUS]
- papers: https://doi.org/10.1103/physrevb.85.014203 (Structural and magnetic transitions in the crystalline approximant Cd6Sm)

## Cd-Sn-Te-Tl
- rank 2881 | 1 samples | 1 papers | 1 compositions
- compositions: Tl2CdSnTe4 (1)
- measured range: 80-302 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1021/cm0518067 (Tl2AXTe4(A = Cd, Hg, Mn; X = Ge, Sn):  Crystal Structure, Electronic S...)

## Cd-Tm
- rank 2882 | 1 samples | 1 papers | 1 compositions
- compositions: Cd83.7Tm16.3 (1)
- measured range: 18-290 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TmCd Pm-3m (221) mp-2502 [hull=0.000, icsd=3, PRIMARY]; TmCd2 P6/mmm (191) mp-11311 [hull=0.000, icsd=1, PRIMARY]; Tm11Cd45 F-43m (216) mp-1202074 [hull=0.025, icsd=1, PRIMARY]; TmCd3 Cmcm (63) mp-30502 [hull=0.000, icsd=1, PRIMARY]; TmCd2 P-3m1 (164) mp-1008673 [hull=0.418, icsd=1]
- papers: https://doi.org/10.1080/14786435.2010.544685 (Low-temperature structural stability of Cd6M(M = Ho, Er, Tm and Lu) cu...)

## Cd-Y
- rank 2883 | 1 samples | 1 papers | 1 compositions
- compositions: Cd6Y (1)
- measured range: 12-298 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YCd Pm-3m (221) mp-915 [hull=0.000, icsd=4, PRIMARY]; YCd2 P6/mmm (191) mp-1331 [hull=0.000, icsd=2, PRIMARY]; YCd3 Cmcm (63) mp-2349 [hull=0.000, icsd=2, PRIMARY]; Y11Cd45 F-43m (216) mp-1199736 [hull=0.009, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2003.10.073 (Novel phase transition in the Cd6M intermetallics)

## Ce-Co
- rank 2884 | 1 samples | 1 papers | 1 compositions
- compositions: CeCo2 (1)
- measured range: 11-283 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeCo5 P6/mmm (191) mp-764 [hull=0.018, icsd=19, PRIMARY]; CeCo2 Fd-3m (227) mp-1112 [hull=0.000, icsd=15, PRIMARY]; Ce2Co17 P6_3/mmc (194) mp-2216 [hull=0.000, icsd=10, PRIMARY]; Ce2Co7 P6_3/mmc (194) mp-1196386 [hull=0.012, icsd=4, PRIMARY]; Ce4ZrCo25 Cmmm (65) mp-1227615 [hull=0.032, PRIMARY]
- papers: https://doi.org/10.1016/s0921-4526(96)00583-2 (Transport properties in CeCo2 single crystal)

## Ce-Co-Cu-Si
- rank 2885 | 1 samples | 1 papers | 1 compositions
- compositions: CeCo0.8Cu0.2Si (1)
- measured range: 208-373 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeCoCuSi2 I-4m2 (119) mp-1226624 [hull=0.053, PRIMARY]
- papers: https://doi.org/10.1134/s0031918x13080085 (Thermoelectric properties of rare-earth alloys)

## Ce-Co-Fe-O-Sr
- rank 2886 | 1 samples | 1 papers | 1 compositions
- compositions: Ce0.4Sr0.6Co0.7Fe0.3O3 (1)
- measured range: 574-871 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jallcom.2019.03.301 (Highly conducting perovskite structured (M-SrCoFe-O3-δ, M = Ce, Ba) ca...)

## Ce-Co-Ge-H
- rank 2887 | 1 samples | 1 papers | 1 compositions
- compositions: CeCoGeH1.0 (1)
- measured range: 14-291 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeCoGeH P4/nmm (129) mp-644499 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/18/26/022 (Influence of Ce–H bonding on the physical properties of the hydrides C...)

## Ce-Co-Ge-Yb
- rank 2888 | 1 samples | 1 papers | 1 compositions
- compositions: Yb2CeCo4Ge13 (1)
- measured range: 239-380 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/j.jallcom.2012.09.024 (Thermoelectric properties of Pr3Rh4Sn13-type Yb3Co4Ge13 and Yb3Co4Sn13...)

## Ce-Co-H-Si
- rank 2889 | 1 samples | 1 papers | 1 compositions
- compositions: CeCoSiH1.0 (1)
- measured range: 11-290 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1088/0953-8984/18/26/022 (Influence of Ce–H bonding on the physical properties of the hydrides C...)

## Ce-Co-Ni-Si
- rank 2890 | 1 samples | 1 papers | 1 compositions
- compositions: Ce2Ni2.5Co0.5Si (1)
- measured range: 30-298 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/s0925-8388(99)00483-1 (Thermoelectric properties of the intermediate valent cerium intermetal...)

## Ce-Co-Rh-Sn
- rank 2891 | 1 samples | 1 papers | 1 compositions
- compositions: CeRh0.75Co0.25Sn (1)
- measured range: 15-282 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/s0921-4526(02)02235-4 (Thermoelectric and magnetic properties of CeRh1$minus;xMxSn (M=Co, Ni,...)

## Ce-Co-Ru-Sn
- rank 2892 | 1 samples | 1 papers | 1 compositions
- compositions: Ce3CoRu3Sn13 (1)
- measured range: 13-298 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1103/physrevb.94.235151 (Doping effect on the electronic structure and thermodynamic properties...)

## Ce-Cr-Ge
- rank 2893 | 1 samples | 1 papers | 1 compositions
- compositions: CeCrGe3 (1)
- measured range: 11-300 K (5th-95th pct of 2 curves; full span incl. outliers 11-400 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeCrGe3 P6_3/mmc (194) mp-20650 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/26/10/106001 (Heavy fermion and Kondo lattice behavior in the itinerant ferromagnet ...)

## Ce-Cr-Ni
- rank 2894 | 1 samples | 1 papers | 1 compositions
- compositions: CeNi4Cr (1)
- measured range: 10-298 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1140/epjb/e2011-20159-1 (Thermal transport in the intermetallic compound CeNi4Cr)

## Ce-Cs-Cu-Te
- rank 2895 | 1 samples | 1 papers | 1 compositions
- compositions: Cs0.772Ce2Cu5.232Te6 (1)
- measured range: 292-669 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1021/cm201574a (Syntheses, Structures, and Magnetic and Thermoelectric Properties of D...)

## Ce-Cu-Ga
- rank 2896 | 1 samples | 1 papers | 1 compositions
- compositions: CeCu4Ga (1)
- measured range: 11-299 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce2Ga12Cu P4/nbm (125) mp-5981 [hull=0.000, icsd=2, PRIMARY]; Ce2Ga3Cu P3m1 (156) mp-1226999 [hull=0.000, PRIMARY]; Ce2Ga5Cu3 P-4m2 (115) mp-1226949 [hull=0.000, PRIMARY]; CeGa2Cu3 Cmmm (65) mp-1226676 [hull=0.000, PRIMARY]; CeGa3Cu I-4m2 (119) mp-1226613 [hull=0.003, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2009.10.028 (Thermoelectric power in (, Ni; , Ga) compounds)

## Ce-Cu-La-Sn
- rank 2897 | 1 samples | 1 papers | 1 compositions
- compositions: CeLa4CuSn3 (1)
- measured range: 13-281 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1007/s10582-004-0413-8 (Formation of Heavy-fermion State in Ce5-xLaxCuSn3)

## Ce-Ga-H-Ir
- rank 2898 | 1 samples | 1 papers | 1 compositions
- compositions: CeIrGaH1.8 (1)
- measured range: 12-298 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1021/cm0705338 (Hydrogenation of the Ce(Rh1-xIrx)Ga System:  Occurrence of Antiferroma...)

## Ce-Ga-H-Ir-Rh
- rank 2899 | 1 samples | 1 papers | 1 compositions
- compositions: Ce(Rh0.46Ir0.54)GaH1.8 (1)
- measured range: 10-298 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1021/cm0705338 (Hydrogenation of the Ce(Rh1-xIrx)Ga System:  Occurrence of Antiferroma...)

## Ce-Ga-H-Ni
- rank 2900 | 1 samples | 1 papers | 1 compositions
- compositions: CeNiGaH1.1 (1)
- measured range: 11-284 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1103/physrevb.71.214437 (From intermediate valence to magnetic behavior without long-range orde...)
