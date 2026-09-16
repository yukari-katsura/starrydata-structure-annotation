# Host systems -- chunk 050 of 73

Ranks 2451-2500 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 97.79%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Al-Cu-Mg-O
- rank 2451 | 1 samples | 1 papers | 1 compositions
- compositions: CuAl0.8Mg0.2O2 (1)
- sample form: Bulk (1)
- measured range: 723-1073 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg14AlCuO16 Pmmm (47) mp-1036652 [hull=0.052, PRIMARY]; Mg30AlCuO32 P4/mmm (123) mp-1038308 [hull=0.024, PRIMARY]; Mg6AlCuO8 P4/mmm (123) mp-1033139 [hull=0.117, PRIMARY]; Mg14AlCuO16 P4/mmm (123) mp-1036556 [hull=0.067]
- papers: https://doi.org/10.1016/j.jeurceramsoc.2007.02.030 (Microstructure and high-temperature thermoelectric properties of polyc...)

## Al-Cu-Mn
- rank 2452 | 1 samples | 1 papers | 1 compositions
- compositions: Cu2MnAl (1)
- measured range: 17-292 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnAlCu2 Fm-3m (225) mp-905565 [hull=0.040, icsd=12, PRIMARY]; Mn5Al31Cu3 Cmcm (63) mp-1197126 [hull=0.032, icsd=1, PRIMARY]; Mn2AlCu3 R-3m (166) mp-1221881 [hull=0.169, PRIMARY]; Mn2Al2Cu I4mm (107) mp-1221904 [hull=0.213, PRIMARY]; Mn6Al31Cu2 Cmcm (63) mp-1211191 [hull=0.048, PRIMARY]
- papers: https://doi.org/10.1088/0305-4608/11/7/017 (The transport properties of Heusler alloys: 'ideal' local moment ferro...)

## Al-Cu-Mn-U
- rank 2453 | 1 samples | 1 papers | 1 compositions
- compositions: UCu3Mn2Al7 (1)
- measured range: 11-298 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jallcom.2005.12.049 (Low temperature specific heat and thermoelectric power of UCu3M2Al7 al...)

## Al-Cu-Os
- rank 2454 | 1 samples | 1 papers | 1 compositions
- compositions: Al65Cu20Os15 (1)
- measured range: 13-283 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1143/jjap.34.2415 (Electrical Transport Properties of Al-Cu-Os Icosahedral Quasicrystal)

## Al-Dy-Fe
- rank 2455 | 1 samples | 1 papers | 1 compositions
- compositions: DyFe5Al7 (1)
- measured range: 43-298 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Dy(Al2Fe)4 I4/mmm (139) mp-5091 [hull=0.000, icsd=6, PRIMARY]; Dy2Al2Fe15 P6_3/mmc (194) mp-1196052 [hull=0.029, icsd=5, PRIMARY]; Dy2Al5Fe12 P6_3/mmc (194) mp-1197186 [hull=0.090, icsd=2, PRIMARY]; Dy2Al3Fe14 R-3m (166) mp-1106052 [hull=0.038, icsd=1, PRIMARY]; Dy(AlFe)6 Immm (71) mp-1225629 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.92.014407 (Magnetic and magnetotransport behavior ofRFe5Al7(R=GdandDy): Observati...)

## Al-Er
- rank 2456 | 1 samples | 1 papers | 1 compositions
- compositions: ErAl2 (1)
- measured range: 21-279 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ErAl2 Fd-3m (227) mp-1208 [hull=0.000, icsd=16, PRIMARY]; ErAl3 Pm-3m (221) mp-2134 [hull=0.002, icsd=5, PRIMARY]; ErAl Pbcm (57) mp-1188739 [hull=0.000, icsd=2, PRIMARY]; Er3Al2 P4_2/mnm (136) mp-31181 [hull=0.000, icsd=1, PRIMARY]; Er2Al17 P6_3/mmc (194) mp-1201145 [hull=0.077, icsd=1, PRIMARY]
- papers: https://doi.org/10.1088/0305-4608/16/4/013 (Thermal conductivity of REAl2compounds (RE=rare earth))

## Al-Er-O
- rank 2457 | 1 samples | 1 papers | 1 compositions
- compositions: Er3Al5O12 (1)
- sample form: Bulk (1)
- measured range: 298-1273 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Er3Al5O12 Ia-3d (230) mp-3384 [hull=0.000, icsd=4, PRIMARY]; ErAlO3 Pnma (62) mp-756458 [hull=0.018, PRIMARY]; ErAlO3 P6_3/mmc (194) mp-754184 [hull=0.086]; ErAlO3 Pm-3m (221) mp-1184150 [hull=0.186]
- papers: https://doi.org/10.1002/adem.201100122 (Y3−xErxAl5O12 Aluminate Ceramics: Preparation, Thermal Properties and ...)

## Al-Fe-Ga-Nb-V
- rank 2458 | 1 samples | 1 papers | 1 compositions
- compositions: Fe2V0.8Nb0.2Al0.8Ga0.2 (1)
- measured range: 198-598 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1134/s1063782619130207 (Electrical Transport Properties of Nb and Ga Double Substituted Fe2VAl...)

## Al-Fe-Ga-V
- rank 2459 | 1 samples | 1 papers | 1 compositions
- compositions: Fe2VAl0.8Ga0.2 (1)
- measured range: 198-597 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1134/s1063782619130207 (Electrical Transport Properties of Nb and Ga Double Substituted Fe2VAl...)

## Al-Fe-Gd
- rank 2460 | 1 samples | 1 papers | 1 compositions
- compositions: GdFe5Al7 (1)
- measured range: 42-295 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd(Al2Fe)4 I4/mmm (139) mp-1104719 [hull=0.000, icsd=2, PRIMARY]; Gd(AlFe)6 Immm (71) mp-1224928 [hull=0.000, PRIMARY]; Gd2AlFe3 R-3m (166) mp-1225145 [hull=0.089, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.92.014407 (Magnetic and magnetotransport behavior ofRFe5Al7(R=GdandDy): Observati...)

## Al-Fe-Ge-V
- rank 2461 | 1 samples | 1 papers | 1 compositions
- compositions: Fe2VAl0.80Ge0.20 (1)
- sample form: Bulk (1)
- measured range: 14-400 K (5th-95th pct of 2 curves; full span incl. outliers 14-996 K)
- papers: https://doi.org/10.1103/physrevb.74.115115 (Thermal and transport properties of the Heusler-typeFe2VAl1−xGex(0≤x≤0...)

## Al-Fe-La-O-Sr
- rank 2462 | 1 samples | 1 papers | 1 compositions
- compositions: (La0.7Sr0.3)(Al0.7Fe0.3)O3 (1)
- sample form: disk (1)
- measured range: 374-1262 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1063/1.4883042 (Temperature-independent sensors based on perovskite-type oxides)

## Al-Fe-Li-O
- rank 2463 | 1 samples | 1 papers | 1 compositions
- compositions: Mg0.2Al0.4Li0.40Fe2.00O4 (1)
- dopant candidates (<5% at.): Mg (1)
- measured range: 318-1084 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li2Al2FeO6 C2 (5) mp-770845 [hull=0.093, PRIMARY]; Li2AlFeO4 Pc (7) mp-772267 [hull=0.017, PRIMARY, AMBIGUOUS]; Li3Al(FeO3)2 P-1 (2) mp-1177725 [hull=0.042, PRIMARY]; Li3Al2FeO6 C2/m (12) mp-770727 [hull=0.020, PRIMARY]; Li3AlFeO4 I4_1/a (88) mp-772439 [hull=0.019, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2004.09.059 (Thermoelectric power studies of magnesium and aluminium substituted li...)

## Al-Fe-Ni
- rank 2464 | 1 samples | 1 papers | 1 compositions
- compositions: Fe2NiAl (1)
- measured range: 301-586 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlFe2Ni Fm-3m (225) mp-31186 [hull=0.233, icsd=1, PRIMARY]; Al27(FeNi2)2 P1 (1) mp-1229168 [hull=0.000, PRIMARY]; Al2FeNi P4/mmm (123) mp-1228910 [hull=0.000, PRIMARY, AMBIGUOUS]; Al5FeNi Amm2 (38) mp-1228374 [hull=0.000, PRIMARY]; Al2FeNi Fm-3m (225) mp-867330 [hull=0.000]
- papers: https://doi.org/10.1063/1.5029868 (Magnetic and thermoelectric properties of melt-spun ribbons of Fe2XAl ...)

## Al-Fe-S-V
- rank 2465 | 1 samples | 1 papers | 1 compositions
- compositions: Fe2VAl0.9SI0.1 (1)
- dopant candidates (<5% at.): I (1)
- sample form: Bulk (1)
- measured range: 343-748 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1143/jjap.47.1512 (Development and Evaluation of High-Strength Fe2VAl Thermoelectric Module)

## Al-Fe-Ta
- rank 2466 | 1 samples | 1 papers | 1 compositions
- compositions: Al70Fe20Ta10 (1)
- measured range: 13-299 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ta3AlFe8 P3m1 (156) mp-1218090 [hull=0.038, PRIMARY]; TaAlFe Amm2 (38) mp-1218064 [hull=0.054, PRIMARY]; TaAlFe4 P-3m1 (164) mp-1218027 [hull=0.099, PRIMARY]
- papers: https://doi.org/10.1143/jjap.27.l5 (A New Icosahedral Al-Fe-Ta Alloy Prepared by Rapid Solidification)

## Al-Ga-La
- rank 2467 | 1 samples | 1 papers | 1 compositions
- compositions: Ce0.2La0.8Al2Ga2 (1)
- dopant candidates (<5% at.): Ce (1)
- sample form: Bulk (1)
- measured range: 11-274 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1103/physrevb.43.3204 (Antiferromagnetism inCe1−xLaxAl2Ga2andCe1−yYyAl2Ga2Kondo-lattice systems)

## Al-Gd-O-Sr
- rank 2468 | 1 samples | 1 papers | 1 compositions
- compositions: Gd2SrAl2O7 (1)
- sample form: Bulk (1)
- measured range: 301-1276 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1111/jace.15504 (Thermophysical properties of rare earth barium aluminates)

## Al-Ge-La
- rank 2469 | 1 samples | 1 papers | 1 compositions
- compositions: LaAlGe (1)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(AlGe)2 P-3m1 (164) mp-10580 [hull=0.000, icsd=2, PRIMARY]; La2Al2Ge Cmcm (63) mp-1079988 [hull=0.000, icsd=1, PRIMARY]; La2Al3Ge4 Cmce (64) mp-669456 [hull=0.010, icsd=1, PRIMARY]; LaAlGe I4_1md (109) mp-11511 [hull=0.000, icsd=1, PRIMARY]; La2Al3Ge P-6m2 (187) mp-1223244 [hull=0.027, PRIMARY]
- papers: https://doi.org/10.1116/6.0001306 (Experimental study of transport properties of Weyl semimetal LaAlGe th...)

## Al-Ge-Li
- rank 2470 | 1 samples | 1 papers | 1 compositions
- compositions: LiAlGe (1)
- measured range: 12-635 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiAlGe F-43m (216) mp-5920 [hull=0.000, icsd=2, PRIMARY]; LiAl2Ge Fm-3m (225) mp-1207174 [hull=0.301, PRIMARY]
- papers: https://doi.org/10.1007/s11664-010-1076-9 (Investigation of the Thermoelectric Properties of LiAlSi and LiAlGe)

## Al-Ir-La
- rank 2471 | 1 samples | 1 papers | 1 compositions
- compositions: La2Ir3Al9 (1)
- sample form: Polycrystal (1)
- measured range: 12-299 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2(Al3Ir)3 Cmcm (63) mp-1211311 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2021.160925 (A new look at the ground state properties of Ce2Ir3Al9: Coexistence of...)

## Al-Ir-Pd
- rank 2472 | 1 samples | 1 papers | 1 compositions
- compositions: Al64.5Ir22Pd13.5_IAC_1_0 (1)
- measured range: 18-298 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1524/zkri.2009.1102 (Synthesis and superstructure of Al—Ir, Al—Ir—Pd crystalline approximan...)

## Al-Ir-Yb
- rank 2473 | 1 samples | 1 papers | 1 compositions
- compositions: Yb2Ir3Al9 (1)
- sample form: Polycrystal (1)
- measured range: 11-309 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb2(Al3Ir)3 Cmcm (63) mp-1207613 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.60.1136 (Magnetic, transport, and thermal properties of<mml:math xmlns:mml=\"ht...)

## Al-K-Sn
- rank 2474 | 1 samples | 1 papers | 1 compositions
- compositions: K8Al8Sn38 (1)
- sample form: Bulk (1)
- measured range: 106-394 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1088/0022-3727/45/45/455308 (Preparation and thermoelectric properties of sinteredn-type K8M8Sn38(M...)

## Al-La-Mg-O-Ta
- rank 2475 | 1 samples | 1 papers | 1 compositions
- compositions: La4MgAl2TaO12 (1)
- measured range: 291-1273 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1002/adma.201808222 (Diffused Lattice Vibration and Ultralow Thermal Conductivity in the Bi...)

## Al-La-Mn-O-Sr
- rank 2476 | 1 samples | 1 papers | 1 compositions
- compositions: La0.5Sr0.5Mn0.75Al0.25O3 (1)
- curator composition details (from the paper): polycrystalline (1)
- measured range: 70-297 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1088/0022-3727/49/3/035001 (Al<sup>3+</sup>doping effects and high-field phase diagram of La<sub>0...)

## Al-La-O-Sr-Ta
- rank 2477 | 1 samples | 1 papers | 1 compositions
- compositions: (La0.3Sr0.7)(Al0.65Ta0.35)O3 (1)
- curator composition details (from the paper): thin film (1)
- measured range: 28-400 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr3LaTaAl3O12 Cmmm (65) mp-1232343 [hull=0.023, PRIMARY]; Sr6La2Ta3Al5O24 R-3m (166) mp-676456 [hull=0.000, PRIMARY]; Sr3LaTaAl3O12 Amm2 (38) mp-1232342 [hull=0.035]
- papers: https://doi.org/10.1088/1361-6463/ab3ddb (High-temperature ferromagnetic insulating phase in strained La<sub>0.8...)

## Al-La-O-Ta
- rank 2478 | 1 samples | 1 papers | 1 compositions
- compositions: La2AlTaO7 (1)
- sample form: Bulk (1)
- measured range: 294-1473 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.ceramint.2016.10.005 (Thermal properties of La3TaO7 and La2AlTaO7 oxides)

## Al-Li-Si
- rank 2479 | 1 samples | 1 papers | 1 compositions
- compositions: LiAlSi (1)
- measured range: 10-657 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiAlSi F-43m (216) mp-3161 [hull=0.000, icsd=4, PRIMARY]; Li12Al3Si4 I-43d (220) mp-14378 [hull=0.084, icsd=1, PRIMARY]; Li8Al3Si5 P-43m (215) mp-30134 [hull=0.200, icsd=1, PRIMARY]; Li2AlSi P6_3/mmc (194) mp-1210755 [hull=0.077, PRIMARY]
- papers: https://doi.org/10.1007/s11664-010-1076-9 (Investigation of the Thermoelectric Properties of LiAlSi and LiAlGe)

## Al-Mg-O-Si
- rank 2480 | 1 samples | 1 papers | 1 compositions
- compositions: Mg2SiAl5O7.5 (1)
- measured range: 304-861 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg3Al2(SiO4)3 Ia-3d (230) mp-6073 [hull=0.039, icsd=55, PRIMARY]; Mg2Al4Si5O18 Cccm (66) mp-6174 [hull=0.000, icsd=16, PRIMARY]; CsMg4Al9(SiO4)9 P1 (1) mp-695133 [hull=0.019, PRIMARY]; KMg4Al9(SiO4)9 P1 (1) mp-686653 [hull=0.022, PRIMARY]; Ca3Mg9Al8(SiO4)12 C2 (5) mp-1227888 [hull=0.039, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2012.08.026 (Fabrication and thermoelectric properties of Mg2Si-based composites us...)

## Al-Mg-Zn
- rank 2481 | 1 samples | 1 papers | 1 compositions
- compositions: Mg36.3Al32.0Zn31.7 (1)
- measured range: 10-304 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg19Al4Zn15 Cmcm (63) mp-1204993 [hull=0.032, icsd=1, PRIMARY]; Mg2Al4Zn3 P6_3/mmc (194) mp-1189454 [hull=0.115, icsd=1, PRIMARY]; Mg14AlZn P-6m2 (187) mp-1028199 [hull=0.022, PRIMARY, AMBIGUOUS]; Mg17Al11Zn Cm (8) mp-1185781 [hull=0.023, PRIMARY]; Mg16Al12Zn Cm (8) mp-1185721 [hull=0.028, PRIMARY, AMBIGUOUS]
- papers: https://doi.org/10.1016/j.jallcom.2006.05.026 (Electrical, magnetic, thermal and thermoelectric properties of the “Be...)

## Al-Mn-Pd-Si
- rank 2482 | 1 samples | 1 papers | 1 compositions
- compositions: Al67.0Pd11.5Mn14.6Si6.9 (1)
- curator composition details (from the paper): Composition was evaluateb by EMPA.
Nominal composition: Al67Pd11Mn14Si8 (1)
- sample form: Bulk (1)
- measured range: 369-956 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1524/zkri.2009.1061 (Thermoelectric performance of Al–Pd–Mn quasicrystals: comparison with ...)

## Al-N-Si
- rank 2483 | 1 samples | 1 papers | 1 compositions
- compositions: YSmSi10.45Al1.55O1.3N14.7 (1)
- dopant candidates (<5% at.): O (1), Y (1), Sm (1)
- curator composition details (from the paper): Y-Sm/α-SiAlON (1)
- sample form: Bulk (1)
- measured range: 299-1073 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YAl6Si18(N15O)2 P1 (1) mp-677127 [hull=0.092, PRIMARY]; YAl6Si30(N15O)3 P1 (1) mp-686618 [hull=0.066, PRIMARY]
- papers: https://doi.org/10.1111/j.1551-2916.2007.01993.x (Experimental and Finite Element Study of the Thermal Conductivity of ?...)

## Al-Na-Sn
- rank 2484 | 1 samples | 1 papers | 1 compositions
- compositions: Na1.76Al1.76Sn4.24 (1)
- sample form: Bulk (1)
- measured range: 294-471 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1021/acs.chemmater.5b04239 (Synthesis, Crystal Structure, and Thermoelectric Properties of Na2+xAl...)

## Al-Nb
- rank 2485 | 1 samples | 1 papers | 1 compositions
- compositions: TiAl48Nb6 (1)
- dopant candidates (<5% at.): Ti (1)
- curator composition details (from the paper): Ti–48Al–6Nb (at.%) (1)
- sample form: Bulk (1)
- measured range: 299-1074 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nb3Al Pm-3n (223) mp-796 [hull=0.050, icsd=19, PRIMARY]; NbAl3 I4/mmm (139) mp-1842 [hull=0.000, icsd=10, PRIMARY]; Nb2Al P4_2/mnm (136) mp-18427 [hull=0.000, icsd=6, PRIMARY]; Nb4Al Fmmm (69) mp-1220481 [hull=0.119, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2009.12.005 (Pore structures and thermal insulating properties of high Nb containin...)

## Al-Ni-Y
- rank 2486 | 1 samples | 1 papers | 1 compositions
- compositions: YNiAl4 (1)
- sample form: Bulk (1)
- measured range: 10-300 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y3(AlNi3)2 Im-3m (229) mp-4577 [hull=0.000, icsd=3, PRIMARY]; YAlNi P-62m (189) mp-13095 [hull=0.000, icsd=3, PRIMARY]; YAl4Ni Cmcm (63) mp-3602 [hull=0.000, icsd=3, PRIMARY]; YAl2Ni Cmcm (63) mp-13094 [hull=0.000, icsd=3, PRIMARY]; YAl3Ni Pnma (62) mp-4054 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/18/46/004 (Intermediate valence behaviour of Yb in a new intermetallic compound Y...)

## Al-O-Si
- rank 2487 | 1 samples | 1 papers | 1 compositions
- compositions: (Al2O3)20(MgO)15(TiO2)9(SiO2)56 (1)
- dopant candidates (<5% at.): Mg (1), Ti (1)
- curator composition details (from the paper): SiO2:56%, Al2O3:20%, MgO:15%, TiO2:9% (1)
- sample form: Bulk (1)
- measured range: 293-1273 K (5th-95th pct of 1 curves)
- [ref 1] TEDesignLab / ICSD: Al2Si4O11 P-1 (2) mp-707135 [hull=0.033, icsd=2, PRIMARY]; Al2SiO5 C2/c (15) mp-9515 [hull=0.100, icsd=1]; Al2SiO5 Cmcm (63) mp-9516 [hull=0.109, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: Al2SiO5 Pnnm (58) mp-4753 [hull=0.000, icsd=27, PRIMARY, AMBIGUOUS]; Ca2Al4Si8O33 C2/m (12) mp-1200127 [hull=0.367, icsd=6, PRIMARY]; Al2Si2O9 P1 (1) mp-1103547 [hull=0.311, icsd=5, PRIMARY]; CaAl2(Si3O10)2 Pc (7) mp-1197130 [hull=0.296, icsd=3, PRIMARY]; Al(SiO3)2 P-1 (2) mp-1105328 [hull=0.190, icsd=2, PRIMARY]
- papers: https://doi.org/10.1002/adma.201808222 (Diffused Lattice Vibration and Ultralow Thermal Conductivity in the Bi...)

## Al-Os-Pd
- rank 2488 | 1 samples | 1 papers | 1 compositions
- compositions: Al72Pd17Os11_IQC (1)
- measured range: 13-297 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al2OsPd Immm (71) mp-1095763 [hull=2.981, PRIMARY]
- papers: https://doi.org/10.1080/09500830110120659 (New stable icosahedral phases in Al-Pd-Ru and Al-Pd-Os systems)

## Al-Pd-Pu
- rank 2489 | 1 samples | 1 papers | 1 compositions
- compositions: PuPd5Al2 (1)
- sample form: Bulk (1)
- measured range: 11-296 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PuAl2Pd5 I4/mmm (139) mp-1091385 [hull=0.000, icsd=1, PRIMARY]; PuAl3Pd2 P6/mmm (191) mp-1206289 [hull=0.009, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.77.092405 (Magnetic and electronic properties of antiferromagneticPuPd5Al2)

## Al-Pd-Tc
- rank 2490 | 1 samples | 1 papers | 1 compositions
- compositions: Al70Pd21Tc9 (1)
- measured range: 13-294 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al2TcPd Fm-3m (225) mp-1183135 [hull=0.019, PRIMARY]; Al2TcPd Immm (71) mp-1097597 [hull=2.808]
- papers: https://doi.org/10.1134/1.1332136 (Thermodynamic and kinetic properties of an icosahedral quasicrystallin...)

## Al-Pd-Th
- rank 2491 | 1 samples | 1 papers | 1 compositions
- compositions: ThPd5Al2 (1)
- measured range: 13-297 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ThAlPd P-62m (189) mp-1078527 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.79.134525 (Kondo behavior in superconductingNpPd5Al2)

## Al-Pd-U
- rank 2492 | 1 samples | 1 papers | 1 compositions
- compositions: UPd2Al3 (1)
- measured range: 12-293 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UAl3Pd2 P6/mmm (191) mp-4561 [hull=0.091, icsd=3, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(00)01176-2 (Large thermoelectric power in several metallic compounds of cerium and...)

## Al-Pt-Yb
- rank 2493 | 1 samples | 1 papers | 1 compositions
- compositions: Yb2Pt6Al15 (1)
- sample form: SingleCrystal (1)
- measured range: 11-199 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbAlPt Pnma (62) mp-1102117 [hull=0.000, icsd=1, PRIMARY]; Yb4(Al8Pt3)3 P-1 (2) mp-1207592 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1088/1367-2630/10/9/093017 (Investigation of Yb2Pt6Al15single crystals: heavy fermion system with ...)

## Al-Rb-Si
- rank 2494 | 1 samples | 1 papers | 1 compositions
- compositions: Rb8Al8Si38 (1)
- measured range: 10-398 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1002/chem.201403416 (A Combined Metal-Halide/Metal Flux Synthetic Route towards Type-I Clat...)

## Al-Re-Ru-Si
- rank 2495 | 1 samples | 1 papers | 1 compositions
- compositions: Ru0.24Re0.73Si1.5364Al0.1336 (1)
- sample form: Rod (1)
- measured range: 313-968 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/j.actamat.2008.12.039 (Thermoelectric properties of ternary and Al-containing quaternary Ru1−...)

## Al-Rh-Yb
- rank 2496 | 1 samples | 1 papers | 1 compositions
- compositions: Yb2Rh3Al9 (1)
- sample form: Polycrystal (1)
- measured range: 11-304 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbAlRh Pnma (62) mp-1207572 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.60.1136 (Magnetic, transport, and thermal properties of<mml:math xmlns:mml=\"ht...)

## Al-Si-Yb
- rank 2497 | 1 samples | 1 papers | 1 compositions
- compositions: Yb2Si2Al (1)
- measured range: 21-268 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(AlSi)2 P-3m1 (164) mp-10405 [hull=0.000, icsd=1, PRIMARY]; Yb2AlSi2 P4/mbm (127) mp-10532 [hull=0.028, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.98.075101 (Intermediate valence in single crystalline \nYb2Si2Al)

## Al-Ti-V
- rank 2498 | 1 samples | 1 papers | 1 compositions
- compositions: Al3V0.7Ti0.3 (1)
- measured range: 297-1065 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti2AlV F-43m (216) mp-999068 [hull=0.136, icsd=1, PRIMARY]; TiAl2V P4/mmm (123) mp-1217015 [hull=0.025, PRIMARY]; TiAlV2 Cmm2 (35) mp-1217032 [hull=0.125, PRIMARY]
- papers: https://doi.org/10.1002/pssb.201552650 (Reduction of lattice thermal conductivity of pseudogap intermetallic c...)

## Al-Tm
- rank 2499 | 1 samples | 1 papers | 1 compositions
- compositions: TmAl2 (1)
- measured range: 14-277 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TmAl2 Fd-3m (227) mp-858 [hull=0.000, icsd=4, PRIMARY]; TmAl Pbcm (57) mp-16721 [hull=0.000, icsd=2, PRIMARY]; TmAl3 Pm-3m (221) mp-768 [hull=0.000, icsd=2, PRIMARY]; Tm3Al2 P4_2/mnm (136) mp-982635 [hull=0.001, icsd=1, PRIMARY]; Tm3Al P6_3/mmc (194) mp-1187635 [hull=0.008, PRIMARY]
- papers: https://doi.org/10.1088/0305-4608/16/4/013 (Thermal conductivity of REAl2compounds (RE=rare earth))

## Al-Y-Yb
- rank 2500 | 1 samples | 1 papers | 1 compositions
- compositions: (YbAl3)0.95(Y5Sb3)0.05 (1)
- dopant candidates (<5% at.): Sb (1)
- sample form: pellets (1)
- measured range: 300-673 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbYAl4 F-43m (216) mp-1215441 [hull=0.021, PRIMARY]; YbYAl6 P6_3/mmc (194) mp-1215596 [hull=0.032, PRIMARY]
- papers: https://doi.org/10.1007/s11664-014-2997-5 (Effects of Second Phase Yb5Sb3 on the Thermoelectric Properties of YbAl3)
