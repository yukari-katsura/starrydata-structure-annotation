# Host systems -- chunk 053 of 73

Ranks 2601-2650 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 98.08%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## B-La-N-Ni
- rank 2601 | 1 samples | 1 papers | 1 compositions
- compositions: La3Ni2B2N3 (1)
- measured range: 13-284 K (5th-95th pct of 2 curves; full span incl. outliers 13-759 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La3Ni2B2N3 I4/mmm (139) mp-6114 [hull=0.000, icsd=3, PRIMARY]; LaNiBN P4/nmm (129) mp-20881 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.83.115131 (Anderson lattice in the intermediate valence compound Ce3Ni2B2N3−δ)

## B-Li
- rank 2602 | 1 samples | 1 papers | 1 compositions
- compositions: LiB (1)
- measured range: 14-304 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiB P6_3/mmc (194) mp-1001835 [hull=0.000, icsd=3, PRIMARY]; LiB11 I-4m2 (119) mp-1103120 [hull=0.749, icsd=2, PRIMARY]; Li5B4 R3m (160) mp-27658 [hull=0.665, icsd=1, PRIMARY]; LiB9 P6_3cm (185) mp-1105976 [hull=0.130, icsd=1, PRIMARY]; Li2B P6/mmm (191) mp-1222698 [hull=0.484, PRIMARY]
- papers: https://doi.org/10.1002/zaac.200600117 (LiBx (0.82 < × ≤ 1.0) – an Incommensurate Composite Structure below 150 K)

## B-Lu
- rank 2603 | 1 samples | 1 papers | 1 compositions
- compositions: LuB12 (1)
- measured range: 10-306 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LuB12 Fm-3m (225) mp-1104289 [hull=0.000, icsd=3, PRIMARY]; LuB2 P6/mmm (191) mp-11219 [hull=0.000, icsd=3, PRIMARY]; LuB6 Pm-3m (221) mp-12660 [hull=0.090, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/0925-8388(94)05070-8 (Transition and rare earth element dodecaborides)

## B-Lu-Ni-Yb
- rank 2604 | 1 samples | 1 papers | 1 compositions
- compositions: Lu0.66Yb0.34Ni2B2 (1)
- measured range: 11-291 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1080/14786430600651962 (Physical properties of Lu1−xYbxNi2B2C)

## B-Mn-Ru-Ti
- rank 2605 | 1 samples | 1 papers | 1 compositions
- compositions: Ti9Mn2Ru18B8 (1)
- measured range: 299-974 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti9Mn2(B4Ru9)2 P4/mbm (127) mp-1197511 [hull=0.014, icsd=1, PRIMARY]; Ti8Mn3(B4Ru9)2 Cmmm (65) mp-1217647 [hull=0.025, PRIMARY]
- papers: https://doi.org/10.1007/s11664-014-3423-8 (Thermoelectric Properties of Pseudogap Ti10Ru19B8 \tand Ti9TM2Ru18B8 (...)

## B-N-Ti
- rank 2606 | 1 samples | 1 papers | 1 compositions
- compositions: (TiB2)18Si3N4 (1)
- dopant candidates (<5% at.): Si (1)
- measured range: 291-1167 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti4B2N3 R3m (160) mp-1217108 [hull=0.805, PRIMARY]
- papers: https://doi.org/10.1016/j.ceramint.2016.02.001 (Fabrication and contact resistivity of W–Si 3 N 4 /TiB 2 –Si 3 N 4 /p–...)

## B-Nb-S
- rank 2607 | 1 samples | 1 papers | 1 compositions
- compositions: Nb2SB (1)
- measured range: 299-1072 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jallcom.2021.160344 (Synthesis and characterization of ternary layered Nb2SB ceramics fabri...)

## B-Nb-Si
- rank 2608 | 1 samples | 1 papers | 1 compositions
- compositions: Nb5SiB2 (1)
- measured range: 16-996 K (5th-95th pct of 3 curves; full span incl. outliers 16-1075 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nb5Si3B P6_3/mcm (193) mp-1106165 [hull=0.000, icsd=1, PRIMARY]; Nb10(SiB)3 Fmm2 (42) mp-1220752 [hull=0.011, PRIMARY]; Nb5SiB2 I4/mcm (140) mp-1209930 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2003.12.008 (Electrical and thermal properties of single crystalline Mo 5 X 3  (X=S...)

## B-Nd
- rank 2609 | 1 samples | 1 papers | 1 compositions
- compositions: NdB6 (1)
- measured range: 10-100 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NdB6 Pm-3m (221) mp-1929 [hull=0.000, icsd=9, PRIMARY]; NdB4 P4/mbm (127) mp-1632 [hull=0.000, icsd=2, PRIMARY]; NdB12 Fm-3m (225) mp-1004756 [hull=0.051, PRIMARY]; NdB4 C2/m (12) mp-1097873 [hull=0.795]; NdB4 Immm (71) mp-995182 [hull=1.123]
- papers: https://doi.org/10.1103/physrevb.54.r5207 (Thermal conductivity ofRB6(R=Ce,Pr,Nd,Sm,Gd) single crystals)

## B-Ni
- rank 2610 | 1 samples | 1 papers | 1 compositions
- compositions: NiB (1)
- measured range: 527-946 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ni2B I4/mcm (140) mp-2536 [hull=0.000, icsd=7, PRIMARY]; Ni3B Pnma (62) mp-2058 [hull=0.000, icsd=7, PRIMARY]; NiB Cmcm (63) mp-14019 [hull=0.005, icsd=2, PRIMARY]; Ni4B3 Pnma (62) mp-640067 [hull=0.000, icsd=2, PRIMARY]; Ni23B6 Fm-3m (225) mp-20962 [hull=0.025, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2003.07.005 (Seebeck coefficients of iron group elements borides)

## B-Ni-P
- rank 2611 | 1 samples | 1 papers | 1 compositions
- compositions: Ni80P14B6 (1)
- measured range: 67-396 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/0304-8853(80)90831-8 (Transport properties of Fe-Ni Glasses)

## B-Ni-Ru-Ti
- rank 2612 | 1 samples | 1 papers | 1 compositions
- compositions: Ti9Ni2Ru18B8 (1)
- measured range: 299-974 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti9Ni2(B4Ru9)2 P4/mbm (127) mp-1199093 [hull=0.033, icsd=1, PRIMARY]; Ti8Ni3(B4Ru9)2 P4/mbm (127) mp-1217553 [hull=0.049, PRIMARY]
- papers: https://doi.org/10.1007/s11664-014-3423-8 (Thermoelectric Properties of Pseudogap Ti10Ru19B8 \tand Ti9TM2Ru18B8 (...)

## B-Pr-Rh
- rank 2613 | 1 samples | 1 papers | 1 compositions
- compositions: PrRh4.8B2 (1)
- measured range: 300-300 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrB2Rh3 P6/mmm (191) mp-5369 [hull=0.000, icsd=4, PRIMARY]; PrBRh3 Pm-3m (221) mp-5200 [hull=0.000, icsd=2, PRIMARY]; Pr(BRh)4 P4_2/nmc (137) mp-1179918 [hull=0.008, icsd=1, PRIMARY]; Pr4(BRh4)3 P4/mmm (123) mp-1219901 [hull=0.041, PRIMARY]
- papers: https://doi.org/10.1063/1.5005869 (Thermal conductivity of PrRh4.8B2, a layered boride compound)

## B-Re-Tb
- rank 2614 | 1 samples | 1 papers | 1 compositions
- compositions: TbReB4 (1)
- measured range: 12-349 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Tb2ReB6 Pbam (55) mp-1198929 [hull=0.000, icsd=1, PRIMARY]; Tb3ReB7 Cmcm (63) mp-972380 [hull=0.000, icsd=1, PRIMARY]; TbReB4 Pbam (55) mp-1192121 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1002/ejic.201501038 (Crystal Structure, Magnetic, Electronic, and Thermal Transport Propert...)

## B-Ru-Ta
- rank 2615 | 1 samples | 1 papers | 1 compositions
- compositions: TaRuB (1)
- measured range: 26-346 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TaBRu Pbam (55) mp-1195237 [hull=0.000, icsd=1, PRIMARY]; Ta3B2Ru5 P4/mbm (127) mp-1188194 [hull=0.000, icsd=1, PRIMARY]; Ta7(B4Ru3)2 P6/m (175) mp-1191981 [hull=0.000, icsd=1, PRIMARY]; TaBRu Pmma (51) mp-1205358 [hull=0.013, icsd=1]
- papers: https://doi.org/10.1088/0953-8984/27/41/415701 (Synthesis, crystal structure and properties of the new superconductors...)

## B-Ru-Ti
- rank 2616 | 1 samples | 1 papers | 1 compositions
- compositions: Ti10Ru19B8 (1)
- measured range: 300-974 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1007/s11664-014-3423-8 (Thermoelectric Properties of Pseudogap Ti10Ru19B8 \tand Ti9TM2Ru18B8 (...)

## B-Si-V
- rank 2617 | 1 samples | 1 papers | 1 compositions
- compositions: V5SiB2 (1)
- measured range: 318-869 K (5th-95th pct of 2 curves; full span incl. outliers 318-1070 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): V5SiB2 I4/mcm (140) mp-10126 [hull=0.000, icsd=3, PRIMARY]; V5Si2B I4/mcm (140) mp-1188856 [hull=0.247, icsd=1, PRIMARY]; V5Si3B P6_3/mcm (193) mp-1188823 [hull=0.006, icsd=1, PRIMARY]; V10Si6B P-31m (162) mp-1216643 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2003.12.008 (Electrical and thermal properties of single crystalline Mo 5 X 3  (X=S...)

## B-Tb
- rank 2618 | 1 samples | 1 papers | 1 compositions
- compositions: TbB12 (1)
- measured range: 12-296 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TbB6 Pm-3m (221) mp-12763 [hull=0.014, icsd=4, PRIMARY]; TbB2 P6/mmm (191) mp-965 [hull=0.000, icsd=2, PRIMARY]; TbB12 Fm-3m (225) mp-1104066 [hull=0.000, icsd=1, PRIMARY]; TbB4 P4/mbm (127) mp-19984 [hull=1.144, PRIMARY]
- papers: https://doi.org/10.1016/0925-8388(94)05070-8 (Transition and rare earth element dodecaborides)

## B-W-Y
- rank 2619 | 1 samples | 1 papers | 1 compositions
- compositions: YWB4 (1)
- measured range: 334-999 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y3B7W Cmcm (63) mp-14373 [hull=0.000, icsd=1, PRIMARY]; YB4W Pbam (55) mp-1190755 [hull=0.000, icsd=1, PRIMARY]; YB4W3 Pmm2 (25) mp-1215950 [hull=0.077, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2010.05.110 (Applying an electron counting rule to screen prospective thermoelectri...)

## B-Y
- rank 2620 | 1 samples | 1 papers | 1 compositions
- compositions: YB12 (1)
- measured range: 400-1048 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YB6 Pm-3m (221) mp-2203 [hull=0.030, icsd=9, PRIMARY]; YB4 P4/mbm (127) mp-637 [hull=0.000, icsd=5, PRIMARY]; YB12 Fm-3m (225) mp-7817 [hull=0.000, icsd=3, PRIMARY]; YB2 P6/mmm (191) mp-1542 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1007/bf01164105 (Thermal conductivity of metal dodecaborides with a UB12 structure)

## Ba-Bi-C-Co-O
- rank 2621 | 1 samples | 1 papers | 1 compositions
- compositions: Bi1.975Na0.025Ba2Co2O8C0.8 (1)
- dopant candidates (<5% at.): Na (1)
- measured range: 304-950 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/j.ceramint.2017.01.113 (Enhanced thermoelectric properties of CNT dispersed and Na-doped Bi 2 ...)

## Ba-Bi-Ca-Mg
- rank 2622 | 1 samples | 1 papers | 1 compositions
- compositions: (Ca0.5Ba0.5)0.995Na0.005Mg2Bi1.98 (1)
- dopant candidates (<5% at.): Na (1)
- measured range: 298-873 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.34133/2020/5016564 (Achieving High Thermoelectric Performance in Rare-Earth Element-Free C...)

## Ba-Bi-Co-O-Pb
- rank 2623 | 1 samples | 1 papers | 1 compositions
- compositions: ((Bi0.8Pb0.8)2Ba2O4)0.5CoO2 (1)
- measured range: 35-803 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1063/1.2206134 (Pb-for-Bi substitution for enhancing thermoelectric characteristics of...)

## Ba-Bi-Co-O-Sr
- rank 2624 | 1 samples | 1 papers | 1 compositions
- compositions: Bi2SrBaCo2O8 (1)
- measured range: 15-300 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1063/1.4931893 (Anisotropic electrical and thermal conductivity in Bi2AE2Co2O8+δ [AE =...)

## Ba-Bi-Fe-O
- rank 2625 | 1 samples | 1 papers | 1 compositions
- compositions: BaFe0.5Sn0.2Bi0.3O3 (1)
- dopant candidates (<5% at.): Sn (1)
- measured range: 573-973 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2Fe4Bi2O11 P4mm (99) mp-1228508 [hull=0.121, PRIMARY]; BaFe5Bi4O15 Cc (9) mp-1228771 [hull=0.054, PRIMARY]
- papers: https://doi.org/10.1021/acsaem.3c00014 (Improving Electrocatalytic Activity of Cobalt-Free Barium Ferrite-Base...)

## Ba-Bi-Mg
- rank 2626 | 1 samples | 1 papers | 1 compositions
- compositions: (Ca0.25Ba0.75)0.995Na0.005Mg2Bi1.98 (1)
- dopant candidates (<5% at.): Ca (1), Na (1)
- measured range: 298-873 K (5th-95th pct of 6 curves)
- [ref 1] TEDesignLab / ICSD: Ba(MgBi)2 P-3m1 (164) mp-29209 [hull=0.000, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: BaMg14Bi Amm2 (38) mp-1026537 [hull=0.126, PRIMARY]; BaMg6Bi Amm2 (38) mp-1016607 [hull=0.225, PRIMARY]; BaMg14Bi P-6m2 (187) mp-1026527 [hull=0.179]
- papers: https://doi.org/10.34133/2020/5016564 (Achieving High Thermoelectric Performance in Rare-Earth Element-Free C...)

## Ba-Bi-Mn
- rank 2627 | 1 samples | 1 papers | 1 compositions
- compositions: BaMn2Bi2 (1)
- measured range: 10-334 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba(MnBi)2 I4/mmm (139) mp-1068010 [hull=0.278, icsd=1, PRIMARY]; BaMnBi2 I4/mmm (139) mp-1079799 [hull=0.182, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.4828779 (Large thermopower in the antiferromagnetic semiconductor BaMn2Bi2)

## Ba-Bi-O-Pb-Sr
- rank 2628 | 1 samples | 1 papers | 1 compositions
- compositions: Sr0.7Ba0.3Pb0.75Bi0.25O3 (1)
- measured range: 368-1068 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.ssc.2008.04.009 (Bi doping effect on the thermoelectric properties of perovskite-type S...)

## Ba-Bi-Rb
- rank 2629 | 1 samples | 1 papers | 1 compositions
- compositions: (Rb0.45Ba0.55)Bi0.5803  (1)
- measured range: 24-213 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/0921-4534(89)91183-0 (Superconducting (Rb,Ba)BiO 3 thin films grown by molecular beam epitaxy)

## Ba-Ca-Co-O
- rank 2630 | 1 samples | 1 papers | 1 compositions
- compositions: (CaBa)Co2O5 (1)
- measured range: 288-974 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jmat.2015.04.003 (Anomalous redox properties and ultrafast chemical sensing behavior of ...)

## Ba-Ca-Ir-O
- rank 2631 | 1 samples | 1 papers | 1 compositions
- compositions: Ba3CaIr2O9 (1)
- measured range: 141-299 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba3CaIr2O9 C2/c (15) mp-17448 [hull=0.000, icsd=1, PRIMARY]; Ba2CaIrO6 Fm-3m (225) mp-20841 [hull=0.000, icsd=1, PRIMARY]; Ba6Ca2Ir3RuO18 P3m1 (156) mp-1228306 [hull=0.000, PRIMARY]; Ba3CaIr2O9 P-3m1 (164) mp-13369 [hull=0.021, icsd=1]
- papers: https://doi.org/10.1103/physrevb.97.064408 (Ba3MIr2O9\n hexagonal perovskites in the light of spin-orbit coupling ...)

## Ba-Cd-Cu-O-S-Y
- rank 2632 | 1 samples | 1 papers | 1 compositions
- compositions: YBa2Cu2.2(CdS)0.8O7 (1)
- measured range: 89-300 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1143/jjap.34.5592 (Thermopower of $\\bf YBa_{2}Cu_{3-{\\ninmbi z}}(CdS)_{\\ninmbi z}O_{7-...)

## Ba-Cd-Si
- rank 2633 | 1 samples | 1 papers | 1 compositions
- compositions: Ba8Cd7Si39 (1)
- measured range: 17-251 K (5th-95th pct of 2 curves; full span incl. outliers 17-708 K)
- papers: https://doi.org/10.1088/0953-8984/21/38/385404 (Clathrates Ba8{Zn,Cd}xSi46−x,x∼7: synthesis, crystal structure and the...)

## Ba-Ce-Co-O
- rank 2634 | 1 samples | 1 papers | 1 compositions
- compositions: Ba(CeCo)0.4(FeZr)0.1O3 (1)
- dopant candidates (<5% at.): Fe (1), Zr (1)
- measured range: 573-1174 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1002/smll.202203207 (Electrokinetic Insights into the Triple Ionic and Electronic Conductiv...)

## Ba-Ce-O-Zr
- rank 2635 | 1 samples | 1 papers | 1 compositions
- compositions: BaZr0.4Ce0.4Y0.2O3 (1)
- dopant candidates (<5% at.): Y (1)
- measured range: 573-1173 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2CeZrO6 P4/mmm (123) mp-1228386 [hull=0.032, PRIMARY]; Ba5Ce4ZrO15 C2/m (12) mp-1228442 [hull=0.009, PRIMARY, AMBIGUOUS]; Ba5Ce4ZrO15 P-1 (2) mp-1228741 [hull=0.010]; Ba5Ce4ZrO15 Cmmm (65) mp-1228097 [hull=0.039]
- papers: https://doi.org/10.1016/j.jpowsour.2018.03.029 (In situ formation of a 3D core-shell and triple-conducting oxygen redu...)

## Ba-Co-Cu-Ho-O
- rank 2636 | 1 samples | 1 papers | 1 compositions
- compositions: Ba2HoCu2.0Co1.0O6 (1)
- measured range: 271-392 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2HoCoCu2O7 Pmmm (47) mp-1214661 [hull=0.034, PRIMARY]
- papers: https://doi.org/10.1063/1.3078810 (Thermoelectric and structural characterization of Ba2Ho(Cu3−xCox)O6+y)

## Ba-Co-Eu-O
- rank 2637 | 1 samples | 1 papers | 1 compositions
- compositions: EuBaCo2O5.5 (1)
- measured range: 673-873 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1007/s12034-008-0137-7 (A novel method to control oxygen stoichiometry and thermoelectric prop...)

## Ba-Co-Fe-O-Pr
- rank 2638 | 1 samples | 1 papers | 1 compositions
- compositions: PrBaCoFeO5 (1)
- measured range: 523-1123 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jallcom.2016.05.322 (Improved electrochemical performance and thermal expansion compatibili...)

## Ba-Co-La-O-Sr
- rank 2639 | 1 samples | 1 papers | 1 compositions
- compositions: LaBa0.5Sr0.5Co2O5 (1)
- measured range: 673-1072 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba4Sr2La2Co4O15 Cc (9) mp-1228696 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1039/c7ra00125h (Oxygen permeation, thermal expansion behavior and electrochemical prop...)

## Ba-Co-O-Sm-Sr
- rank 2640 | 1 samples | 1 papers | 1 compositions
- compositions: SmBa0.5Sr0.5Co2O5 (1)
- measured range: 574-1071 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba4Sr2Sm2Co4O15 P1 (1) mp-1228582 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.electacta.2016.04.069 (Electrical, thermal and electrochemical properties of SmBa1−xSrxCo2O5+...)

## Ba-Co-O-Ti
- rank 2641 | 1 samples | 1 papers | 1 compositions
- compositions: La0.2Ba0.7988Sb0.0012Co0.4Ti0.6O3 (1)
- dopant candidates (<5% at.): La (1), Sb (1)
- measured range: 295-513 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1557/proc-365-47 (Resistivity Control by Solid-State Reaction of Perovskite-Type Oxides)

## Ba-Co-O-Tm
- rank 2642 | 1 samples | 1 papers | 1 compositions
- compositions: BaTmCo4O7 (1)
- measured range: 299-853 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaTmCo4O7 Pna2_1 (33) mp-1203002 [hull=0.002, icsd=1, PRIMARY, AMBIGUOUS]; BaTmCo4O7 Cc (9) mp-1192892 [hull=0.005, icsd=1]
- papers: https://doi.org/10.1063/1.3663526 (Structural and thermoelectric properties of BaRCo4O7 (R = Dy, Ho, Er, ...)

## Ba-Co-O-Zr
- rank 2643 | 1 samples | 1 papers | 1 compositions
- compositions: BaCo0.6Zr0.4O3 (1)
- measured range: 323-1001 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.ceramint.2020.05.307 (Self-assembled cubic-hexagonal perovskite nanocomposite as intermediat...)

## Ba-Cu-Dy-Fe-O
- rank 2644 | 1 samples | 1 papers | 1 compositions
- compositions: DyBaCuFeO5 (1)
- measured range: 293-996 K (5th-95th pct of 3 curves; full span incl. outliers 293-1042 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaDyFeCuO5 P4mm (99) mp-1207068 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1134/s1063783409020073 (Thermoelectric properties of layered ferrocuprates LnBaCuFeO5 + δ (Ln=...)

## Ba-Cu-Er-Fe-O
- rank 2645 | 1 samples | 1 papers | 1 compositions
- compositions: ErBaCuFeO5 (1)
- measured range: 295-993 K (5th-95th pct of 3 curves; full span incl. outliers 295-1046 K)
- papers: https://doi.org/10.1134/s1063783409020073 (Thermoelectric properties of layered ferrocuprates LnBaCuFeO5 + δ (Ln=...)

## Ba-Cu-Fe-Ho-O
- rank 2646 | 1 samples | 1 papers | 1 compositions
- compositions: HoBaCuFeO5 (1)
- measured range: 292-996 K (5th-95th pct of 3 curves; full span incl. outliers 292-1045 K)
- papers: https://doi.org/10.1134/s1063783409020073 (Thermoelectric properties of layered ferrocuprates LnBaCuFeO5 + δ (Ln=...)

## Ba-Cu-Fe-La-O-Pr
- rank 2647 | 1 samples | 1 papers | 1 compositions
- compositions: La0.5Pr0.5BaCuFeO5 (1)
- measured range: 305-1057 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1134/s1087659612020058 (Structure and properties of solid solutions of La1 − x Pr x BaCuFeO5 + δ)

## Ba-Cu-Fe-La-O-Sm
- rank 2648 | 1 samples | 1 papers | 1 compositions
- compositions: Sm0.5La0.5BaCuFeO5 (1)
- measured range: 301-1021 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/j.materresbull.2014.10.046 (Thermoelectric properties of Sm1−xLaxBaCuFeO5 ceramics)

## Ba-Cu-Fe-Lu-O
- rank 2649 | 1 samples | 1 papers | 1 compositions
- compositions: LuBaCuFeO5 (1)
- measured range: 297-993 K (5th-95th pct of 3 curves; full span incl. outliers 297-1046 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaLuFeCuO5 P4mm (99) mp-611393 [hull=0.013, icsd=1, PRIMARY]
- papers: https://doi.org/10.1134/s1063783409020073 (Thermoelectric properties of layered ferrocuprates LnBaCuFeO5 + δ (Ln=...)

## Ba-Cu-Fe-Nd-O
- rank 2650 | 1 samples | 1 papers | 1 compositions
- compositions: NdBaCuFeO5 (1)
- measured range: 295-994 K (5th-95th pct of 2 curves; full span incl. outliers 295-1054 K)
- papers: https://doi.org/10.1134/s1063783409020073 (Thermoelectric properties of layered ferrocuprates LnBaCuFeO5 + δ (Ln=...)
