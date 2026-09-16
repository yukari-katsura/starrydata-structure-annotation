# Host systems -- chunk 071 of 73

Ranks 3501-3550 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 99.81%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## N-O-Si-Y
- rank 3501 | 1 samples | 1 papers | 1 compositions
- compositions: Y4Si2O7N5 (1)
- measured range: 296-1272 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y2Si3N4O3 P-42_1m (113) mp-6941 [hull=0.041, icsd=1, PRIMARY]; Y3Si5N9O Pbcm (57) mp-1207796 [hull=0.000, PRIMARY]; Y4Si2NO8 P2_1/c (14) mp-1207840 [hull=0.101, PRIMARY]
- papers: https://doi.org/10.1111/jace.15504 (Thermophysical properties of rare earth barium aluminates)

## N-O-U
- rank 3502 | 1 samples | 1 papers | 1 compositions
- compositions: (Gd2O3)3.53(UN)96.47 (1)
- dopant candidates (<5% at.): Gd (1)
- measured range: 300-1275 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U(N3O7)2 P2_1/c (14) mp-1196565 [hull=0.585, icsd=1, PRIMARY]; U(NO7)2 Cmc2_1 (36) mp-1197147 [hull=0.406, icsd=1, PRIMARY]; U(NO5)2 Cm (8) mp-1104949 [hull=0.545, icsd=1, PRIMARY]; UN2O11 P2_1/c (14) mp-1204308 [hull=0.438, icsd=1, PRIMARY]; U(N2O7)2 P2_1/c (14) mp-1179579 [hull=0.717, PRIMARY]
- papers: https://doi.org/10.1016/j.jnucmat.2021.152785 (Thermal conductivity of gadolinium added uranium mononitride fuel pell...)

## N-Pu-Zr
- rank 3503 | 1 samples | 1 papers | 1 compositions
- compositions: (Zr0.78Pu0.22)N (1)
- measured range: 507-1528 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jallcom.2008.05.077 (Thermophysical characterization of ZrN and (Zr,Pu)N)

## N-Yb
- rank 3504 | 1 samples | 1 papers | 1 compositions
- compositions: YbN (1)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbN Fm-3m (225) mp-1066 [hull=0.321, icsd=4, PRIMARY]; Yb3N2 R-3c (167) mp-864675 [hull=0.000, PRIMARY]; YbN2 P4_2/mnm (136) mp-864757 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.90.245206 (YbN: An intrinsic semiconductor with antiferromagnetic exchange)

## Na-Nb-O-Te
- rank 3505 | 1 samples | 1 papers | 1 compositions
- compositions: (NaNbO3)(TeO2) (1)
- measured range: 160-300 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/j.jallcom.2020.156630 (Effects of inorganic salt NaNbO3 composite on the thermoelectric prope...)

## Na-Ni-O
- rank 3506 | 1 samples | 1 papers | 1 compositions
- compositions: NaNiO2 (1)
- measured range: 352-660 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NaNiO2 C2/m (12) mp-19149 [hull=0.000, icsd=5, PRIMARY]; Na5NiO4 Pbca (61) mp-32318 [hull=0.000, icsd=2, PRIMARY]; Na2NiO2 Cmc2_1 (36) mp-18765 [hull=0.021, icsd=1, PRIMARY]; NaNi3O8 Cm (8) mp-1102157 [hull=0.397, icsd=1, PRIMARY]; Na2(NiO2)5 P-1 (2) mp-764347 [hull=0.003, PRIMARY]
- papers: https://doi.org/10.1016/0167-2738(90)90438-w (Electronic and electrochemical properties of nickel bronze, NaxNiO2)

## Na-Ni-O-Ti
- rank 3507 | 1 samples | 1 papers | 1 compositions
- compositions: Na0.4Ni0.2Ti0.8O2 (1)
- measured range: 301-1075 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Na2TiNiO4 P2/m (10) mp-1221264 [hull=0.018, PRIMARY]
- papers: https://doi.org/10.1016/s0272-8842(02)00050-0 (Thermoelectric characterization of NaxMx/2Ti1−x/2O2 (M=Co, Ni and Fe) ...)

## Nb-O-Sr-V
- rank 3508 | 1 samples | 1 papers | 1 compositions
- compositions: SrV0.7Nb0.3O3 (1)
- measured range: 614-1282 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1039/c5cp00069f (Structural and defect chemistry guidelines for Sr(V,Nb)O<sub>3</sub>-b...)

## Nb-O-Y
- rank 3509 | 1 samples | 1 papers | 1 compositions
- compositions: Y3NbO7 (1)
- measured range: 294-1273 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YNbO4 I4_1/a (88) mp-1095229 [hull=0.002, icsd=20, PRIMARY]; Y3NbO7 Cm (8) mp-676261 [hull=0.246, PRIMARY, AMBIGUOUS]; YNbO2 I4_1/amd (141) mp-1207699 [hull=0.644, PRIMARY]; YNbO4 C2/c (15) mp-5387 [hull=0.000, icsd=13]; Y3NbO7 Cmme (67) mp-1101623 [hull=0.254]
- papers: https://doi.org/10.1002/adma.201808222 (Diffused Lattice Vibration and Ultralow Thermal Conductivity in the Bi...)

## Nb-O-Yb
- rank 3510 | 1 samples | 1 papers | 1 compositions
- compositions: Yb3NbO7 (1)
- measured range: 294-1273 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbNbO4 C2/c (15) mp-5466 [hull=0.000, icsd=2, PRIMARY]; YbNbO3 Pm-3m (221) mp-1187578 [hull=0.020, PRIMARY]
- papers: https://doi.org/10.1002/adma.201808222 (Diffused Lattice Vibration and Ultralow Thermal Conductivity in the Bi...)

## Nb-S-Sm
- rank 3511 | 1 samples | 1 papers | 1 compositions
- compositions: (Sm2S2)2NbS2 (1)
- measured range: 14-298 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1007/s11664-012-2443-5 (Crystal Structure and Thermoelectric Properties of Misfit-Layered Sulf...)

## Nb-S-Tm
- rank 3512 | 1 samples | 1 papers | 1 compositions
- compositions: (Tm2S2)2NbS2 (1)
- measured range: 10-297 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1007/s11664-012-2443-5 (Crystal Structure and Thermoelectric Properties of Misfit-Layered Sulf...)

## Nb-Si-Ta-Te
- rank 3513 | 1 samples | 1 papers | 1 compositions
- compositions: (Ta0.5Nb0.5)4SiTe4 (1)
- measured range: 10-298 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1063/1.5023427 (Large thermoelectric power factor in one-dimensional telluride Nb4SiTe...)

## Nb-Sn
- rank 3514 | 1 samples | 1 papers | 1 compositions
- compositions: Nb3Sn (1)
- measured range: 14-27 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nb3Sn Pm-3n (223) mp-1326 [hull=0.000, icsd=23, PRIMARY]; NbSn2 Fddd (70) mp-1046 [hull=0.000, icsd=3, PRIMARY]; Nb6Sn5 Immm (71) mp-1192223 [hull=0.004, icsd=1, PRIMARY]; NbSn3 P6_3/mmc (194) mp-1186237 [hull=0.410, PRIMARY]
- papers: https://doi.org/10.1299/kikaib.53.2181 (A study of the heat conduction of superconductors. (1st report Measure...)

## Nd-O-Si
- rank 3515 | 1 samples | 1 papers | 1 compositions
- compositions: Nd2SiO5 (1)
- measured range: 293-293 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd2Si2O7 P4_1 (76) mp-15225 [hull=0.000, icsd=1, PRIMARY, AMBIGUOUS]; KNd9(Si3O13)2 P3 (143) mp-1223480 [hull=0.000, PRIMARY]; La3Nd11(Si3O13)3 P6_3 (173) mp-1224647 [hull=0.000, PRIMARY]; NaNd9(Si3O13)2 P3 (143) mp-1221031 [hull=0.000, PRIMARY]; Nd4CdSi3O13 P6_3 (173) mp-1220265 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2020.06.012 (Tailoring thermal properties of multi-component rare earth monosilicates)

## Nd-O-Ta
- rank 3516 | 1 samples | 1 papers | 1 compositions
- compositions: NdTa3O9 (1)
- measured range: 373-1073 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NdTaO4 C2/c (15) mp-4718 [hull=0.004, icsd=4, PRIMARY]; Nd3TaO7 Cmcm (63) mp-31417 [hull=0.000, icsd=2, PRIMARY]; NdTa3O9 P2_1/m (11) mp-28653 [hull=0.000, icsd=1, PRIMARY]; NdTa7O19 P-6c2 (188) mp-14676 [hull=0.000, icsd=1, PRIMARY]; NdTa2O6 P4/mmm (123) mp-1205976 [hull=0.062, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2021.117152 (Spontaneously formed nanostructures in double perovskite rare-earth ta...)

## Nd-O-Yb-Zr
- rank 3517 | 1 samples | 1 papers | 1 compositions
- compositions: (Nd0.6Yb0.4)2Zr2O7 (1)
- measured range: 301-1471 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.ceramint.2018.10.213 (Effects of Yb3+ doping on phase structure, thermal conductivity and fr...)

## Nd-Os-P
- rank 3518 | 1 samples | 1 papers | 1 compositions
- compositions: NdOs4P12 (1)
- measured range: 15-299 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd(P3Os)4 Im-3 (204) mp-1188451 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1143/jpsjs.80sa.sa025 (Thermal Properties of Filled Skutterudite PrOs4P12)

## Nd-Os-Sb
- rank 3519 | 1 samples | 1 papers | 1 compositions
- compositions: NdOs4Sb12 (1)
- measured range: 13-247 K (5th-95th pct of 2 curves; full span incl. outliers 13-297 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd(Sb3Os)4 Im-3 (204) mp-3569 [hull=0.000, icsd=4, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.72.014519 (Transport properties of the heavy-fermion superconductorPrOs4Sb12)

## Nd-Rh
- rank 3520 | 1 samples | 1 papers | 1 compositions
- compositions: Nd7Rh3 (1)
- measured range: 12-294 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NdRh2 Fd-3m (227) mp-2290 [hull=0.000, icsd=2, PRIMARY]; NdRh3 P6_3/mmc (194) mp-864699 [hull=0.000, icsd=1, PRIMARY]; Nd3Rh2 R-3 (148) mp-1104743 [hull=0.000, icsd=1, PRIMARY]; NdRh Cmcm (63) mp-999335 [hull=0.000, icsd=1, PRIMARY]; Nd4Rh Pm (6) mp-1220520 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(98)00458-7 (Magnetic and electrical properties of the intermetallic compounds R7Rh...)

## Nd-Ru
- rank 3521 | 1 samples | 1 papers | 1 compositions
- compositions: NdRu2 (1)
- measured range: 12-289 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NdRu2 Fd-3m (227) mp-1781 [hull=0.000, icsd=6, PRIMARY]; Nd3Ru Pnma (62) mp-1106300 [hull=0.000, icsd=2, PRIMARY]; Nd5Ru2 C2/c (15) mp-1103979 [hull=0.000, icsd=2, PRIMARY]; NdRu3 P6/mmm (191) mp-1064690 [hull=0.624, icsd=1, PRIMARY]; Nd4Ru Fd-3m (227) mp-1209953 [hull=0.453, PRIMARY]
- papers: https://doi.org/10.1016/0921-4526(94)00430-4 (Transport properties of (Ce1−xRx)Ru2 (R  La, Nd))

## Nd-Ru-Sb
- rank 3522 | 1 samples | 1 papers | 1 compositions
- compositions: NdRu4Sb12 (1)
- measured range: 20-291 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd(Sb3Ru)4 Im-3 (204) mp-1189354 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/14/45/317 (Transport properties in the filled-skutterudite compounds RERu4Sb12 (R...)

## Nd-Ru-Si
- rank 3523 | 1 samples | 1 papers | 1 compositions
- compositions: NdRu2Si2 (1)
- measured range: 11-263 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd(SiRu)2 I4/mmm (139) mp-4013 [hull=0.000, icsd=6, PRIMARY]; NdSiRu P4/nmm (129) mp-5239 [hull=0.000, icsd=3, PRIMARY]; NdSi3Ru I4mm (107) mp-1069041 [hull=0.000, icsd=1, PRIMARY]; NdSi2Ru P2_1/m (11) mp-28665 [hull=0.000, icsd=1, PRIMARY]; Nd20(Si3Ru)3 Amm2 (38) mp-1220608 [hull=0.042, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(92)91082-5 (Transport properties and magnetic phases of NdRu2Si2)

## Nd-Ru-Sn
- rank 3524 | 1 samples | 1 papers | 1 compositions
- compositions: NdRuSn3 (1)
- measured range: 16-297 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NdSn3Ru Pm-3n (223) mp-1198161 [hull=0.000, icsd=2, PRIMARY]; Nd(Sn3Ru2)2 I-42m (121) mp-1205655 [hull=0.000, PRIMARY]; Nd2Sn4Ru Amm2 (38) mp-1220534 [hull=0.029, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/3/45/014 (Transport and magnetic properties of RERuSn3(RE=La, Ce, Pr, Nd, Sm): a...)

## Nd-Te-Tl
- rank 3525 | 1 samples | 1 papers | 1 compositions
- compositions: Tl9NdTe6 (1)
- measured range: 314-552 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NdTlTe2 R-3m (166) mp-999319 [hull=0.000, icsd=1, PRIMARY]; Nd3TlTe6 Cmmm (65) mp-1207323 [hull=2.277, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2015.01.025 (Thermoelectric properties of hot-pressed Tl9LnTe6 (Ln=La, Ce, Pr, Nd, ...)

## Ni-O-Ru-Sr
- rank 3526 | 1 samples | 1 papers | 1 compositions
- compositions: SrNiRu5O11 (1)
- measured range: 10-294 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2NiRuO6 Fm-3m (225) mp-1078758 [hull=0.000, icsd=1, PRIMARY]; SrNiRu5O11 P6_3/m (176) mp-1198840 [hull=0.057, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.95.024433 (Structure and physical properties of<mml:math xmlns:mml=\"http://www.w...)

## Ni-P-Sr
- rank 3527 | 1 samples | 1 papers | 1 compositions
- compositions: SrNi2P4 (1)
- measured range: 13-300 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr(Ni5P3)2 Cmce (64) mp-16156 [hull=0.002, icsd=1, PRIMARY, AMBIGUOUS]; Sr(NiP)2 Immm (71) mp-29167 [hull=0.000, icsd=1, PRIMARY]; Sr(NiP2)2 Fddd (70) mp-1103788 [hull=0.000, icsd=1, PRIMARY]; SrNi5P3 Cmcm (63) mp-18632 [hull=0.000, icsd=1, PRIMARY]; Sr(Ni5P3)2 Pnma (62) mp-680220 [hull=0.003, icsd=1]
- papers: https://doi.org/10.1021/acs.chemmater.5b01592 (Twisted Kelvin Cells and Truncated Octahedral Cages in the Crystal Str...)

## Ni-P-Yb
- rank 3528 | 1 samples | 1 papers | 1 compositions
- compositions: Yb2Ni12P7 (1)
- measured range: 10-289 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(Ni2P)2 P4_2/mnm (136) mp-16066 [hull=0.000, icsd=2, PRIMARY]; Yb5Ni19P12 C2/m (12) mp-1201580 [hull=0.000, icsd=1, PRIMARY]; Yb6Ni20P13 P-6 (174) mp-1207641 [hull=0.000, PRIMARY]; Yb9(Ni13P6)2 P-6m2 (187) mp-1207845 [hull=0.000, PRIMARY]; YbNi5P3 Cmcm (63) mp-1207542 [hull=0.012, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/26/42/425601 (Crossover between Fermi liquid and non-Fermi liquid behavior in the no...)

## Ni-Pd-Sn-Ti
- rank 3529 | 1 samples | 1 papers | 1 compositions
- compositions: Ti0.95Hf0.05Ni0.8Pd0.2Sn0.99Sb0.01 (1)
- dopant candidates (<5% at.): Hf (1), Sb (1)
- measured range: 305-948 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/j.intermet.2006.08.008 (High temperature thermoelectric properties of TiNiSn-based half-Heusle...)

## Ni-Pr-Sn
- rank 3530 | 1 samples | 1 papers | 1 compositions
- compositions: Pr9Ni24Sn49 (1)
- measured range: 14-288 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrNiSn Pnma (62) mp-22164 [hull=0.000, icsd=3, PRIMARY]; PrNi5Sn P6_3/mmc (194) mp-1193428 [hull=0.000, icsd=2, PRIMARY]; Pr2Ni2Sn Immm (71) mp-1068489 [hull=0.000, icsd=1, PRIMARY]; Pr(Ni2Sn)2 I4/mcm (140) mp-1104946 [hull=0.000, icsd=1, PRIMARY]; Pr3Ni2Sn7 Cmmm (65) mp-1103584 [hull=0.471, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2004.08.006 (Magnetic and electrical transport properties of RE9Ni24Sn49 compounds ...)

## Ni-Pt-Sn-Zr
- rank 3531 | 1 samples | 1 papers | 1 compositions
- compositions: ZrNi0.7Pt0.3Sn (1)
- measured range: 295-966 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.2320/matertrans.47.1453 (Substitution Effect on Thermoelectric Properties of ZrNiSn Based Half-...)

## Ni-Rb-Sn
- rank 3532 | 1 samples | 1 papers | 1 compositions
- compositions: Rb9Ni24Sn49 (1)
- papers: https://doi.org/10.1016/j.intermet.2004.08.006 (Magnetic and electrical transport properties of RE9Ni24Sn49 compounds ...)

## Ni-S
- rank 3533 | 1 samples | 1 papers | 1 compositions
- compositions: NiS2 (1)
- measured range: 302-622 K (5th-95th pct of 3 curves)
- [ref 1] TEDesignLab / ICSD: NiS P6_3/mmc (194) mp-594 [hull=0.104, icsd=13]; NiS (186)
- [ref 2] MP, ranked by ICSD evidence: NiS2 Pa-3 (205) mp-2282 [hull=0.000, icsd=16, PRIMARY]; NiS R3m (160) mp-1547 [hull=0.015, icsd=11, PRIMARY]; Ni3S2 R32 (155) mp-362 [hull=0.000, icsd=11, PRIMARY]; Ni3S4 Fd-3m (227) mp-1050 [hull=0.000, icsd=3, PRIMARY]; Ni9S8 I-42d (122) mp-1202035 [hull=0.101, icsd=1, PRIMARY]
- papers: https://doi.org/10.1109/ict.2003.1287526 (Thermoelectric figure of merit of M-sulphides (M=Fe, Co, Ni, Pd) thin ...)

## Ni-Sc-Sn-Ti-Zr
- rank 3534 | 1 samples | 1 papers | 1 compositions
- compositions: Ti16.6Zr6.8Ni31.4Sc9.7Sn30.9In1.0 (1)
- dopant candidates (<5% at.): In (1)
- measured range: 13-965 K (5th-95th pct of 4 curves; full span incl. outliers 13-1022 K)
- papers: https://doi.org/10.1557/opl.2013.217 (Thermoelectric behaviour of p- and n- type Ti-Ni-Sn half Heusler alloy...)

## Ni-Se
- rank 3535 | 1 samples | 1 papers | 1 compositions
- compositions: NiSe (1)
- measured range: 299-525 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NiSe P6_3/mmc (194) mp-662 [hull=0.048, icsd=11, PRIMARY]; NiSe2 Pa-3 (205) mp-20901 [hull=0.009, icsd=8, PRIMARY]; Ni3Se2 R32 (155) mp-2056 [hull=0.000, icsd=6, PRIMARY]; Ni3Se4 C2/m (12) mp-573 [hull=0.000, icsd=2, PRIMARY]; Ni19Se20 P-1 (2) mp-685124 [hull=0.040, PRIMARY]
- papers: https://doi.org/10.1039/c3ta13456c (Understanding of the contact of nanostructured thermoelectric n-type B...)

## Ni-Si
- rank 3536 | 1 samples | 1 papers | 1 compositions
- compositions: Ni93.93Si6.07 (1)
- measured range: 73-773 K (5th-95th pct of 2 curves; full span incl. outliers 73-836 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SiNi Pnma (62) mp-351 [hull=0.000, icsd=11, PRIMARY]; SiNi3 Pm-3m (221) mp-828 [hull=0.000, icsd=10, PRIMARY]; SiNi2 Pnma (62) mp-1118 [hull=0.000, icsd=9, PRIMARY]; Si2Ni Fm-3m (225) mp-2291 [hull=0.000, icsd=6, PRIMARY]; Si12Ni31 P321 (150) mp-27276 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1063/1.1722001 (Thermoelectric Power and Electrical Resistivity of Dilute Alloys of Si...)

## Ni-Sm-Sn
- rank 3537 | 1 samples | 1 papers | 1 compositions
- compositions: Sm9Ni24Sn49 (1)
- measured range: 13-277 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SmNiSn Pnma (62) mp-1104463 [hull=0.000, icsd=2, PRIMARY]; Sm2NiSn4 Pnma (62) mp-645182 [hull=0.000, icsd=1, PRIMARY]; Sm(NiSn)2 P4/nmm (129) mp-1080144 [hull=0.000, icsd=1, PRIMARY]; Sm(Ni2Sn)2 I4/mcm (140) mp-1104730 [hull=0.000, PRIMARY]; Sm3(Ni3Sn2)2 P6_3mc (186) mp-1209076 [hull=0.130, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2004.08.006 (Magnetic and electrical transport properties of RE9Ni24Sn49 compounds ...)

## Ni-Sn
- rank 3538 | 1 samples | 1 papers | 1 compositions
- compositions: Ni3Sn4 (1)
- measured range: 298-680 K (5th-95th pct of 2 curves; full span incl. outliers 298-722 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ni3Sn P6_3/mmc (194) mp-20112 [hull=0.000, icsd=5, PRIMARY]; Ni3Sn4 C2/m (12) mp-20174 [hull=0.000, icsd=4, PRIMARY]; Ni3Sn2 Pnma (62) mp-669720 [hull=0.000, icsd=1, PRIMARY]; NiSn Pbam (55) mp-680646 [hull=0.006, icsd=1, PRIMARY]; Ni7Sn8 P2/m (10) mp-1219822 [hull=0.013, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2020.106988 (Role of secondary phases and thermal cycling on thermoelectric propert...)

## Ni-Sn-Tb
- rank 3539 | 1 samples | 1 papers | 1 compositions
- compositions: Tb9Ni24Sn49 (1)
- measured range: 10-296 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TbNiSn Pnma (62) mp-22299 [hull=0.000, icsd=2, PRIMARY]; Tb2Ni2Sn Immm (71) mp-1068217 [hull=0.000, icsd=1, PRIMARY, AMBIGUOUS]; Tb6Ni2Sn Immm (71) mp-1105993 [hull=0.029, icsd=1, PRIMARY]; TbNiSn2 Pnma (62) mp-1198844 [hull=0.000, icsd=1, PRIMARY]; Tb9Ni24Sn49 C2/m (12) mp-1217867 [hull=0.025, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2004.08.006 (Magnetic and electrical transport properties of RE9Ni24Sn49 compounds ...)

## Ni-Sn-Th
- rank 3540 | 1 samples | 1 papers | 1 compositions
- compositions: ThNiSn (1)
- measured range: 11-311 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ThNiSn F-43m (216) mp-22786 [hull=0.000, icsd=2, PRIMARY]; Th(NiSn)2 P4/nmm (129) mp-980110 [hull=0.000, icsd=1, PRIMARY]; Th3Ni3Sn4 I-43d (220) mp-1189639 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1143/jpsj.58.2495 (Anomalous Magnetic, Transport and Thermal Properties in the Half-Metal...)

## Ni-Sn-Tm
- rank 3541 | 1 samples | 1 papers | 1 compositions
- compositions: TmNiSn (1)
- measured range: 339-995 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TmNiSn Pnma (62) mp-1102179 [hull=0.000, icsd=2, PRIMARY]; Tm2NiSn6 Cmmm (65) mp-1079270 [hull=0.000, icsd=1, PRIMARY]; Tm2Ni2Sn P4/mbm (127) mp-1095204 [hull=0.000, icsd=1, PRIMARY]; Tm6Ni2Sn Immm (71) mp-1188573 [hull=0.001, icsd=1, PRIMARY]; TmNiSn2 Pnma (62) mp-1197522 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.5038395 (Power factor enhancement in a composite based on the half-Heusler anti...)

## Ni-Sn-V-Zr
- rank 3542 | 1 samples | 1 papers | 1 compositions
- compositions: Zr0.8V0.2NiSn (1)
- measured range: 300-873 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1021/acsaem.7b00203 (Vanadium-Doping-Induced Resonant Energy Levels for the Enhancement of ...)

## Ni-Sn-Y
- rank 3543 | 1 samples | 1 papers | 1 compositions
- compositions: Y9Ni24Sn49 (1)
- measured range: 12-274 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YNiSn Pnma (62) mp-22617 [hull=0.000, icsd=3, PRIMARY]; YNiSn2 Pnma (62) mp-21981 [hull=0.000, icsd=2, PRIMARY]; Y2Ni2Sn Immm (71) mp-1068331 [hull=0.000, icsd=1, PRIMARY]; Y2Ni7Sn3 Cmce (64) mp-1203938 [hull=0.000, icsd=1, PRIMARY]; Y4NiSn8 Pmm2 (25) mp-1216215 [hull=0.030, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2004.08.006 (Magnetic and electrical transport properties of RE9Ni24Sn49 compounds ...)

## Ni-V
- rank 3544 | 1 samples | 1 papers | 1 compositions
- compositions: Ni3V (1)
- measured range: 272-1071 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): VNi3 I4/mmm (139) mp-171 [hull=0.000, icsd=5, PRIMARY]; VNi2 Immm (71) mp-11531 [hull=0.000, icsd=2, PRIMARY]; V3Ni Pm-3n (223) mp-7226 [hull=0.000, icsd=1, PRIMARY]; VNi R-3m (166) mp-1216313 [hull=0.192, PRIMARY]; V3Ni2 P2/m (10) mp-1216708 [hull=0.002, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2014.12.006 (Thermal conductivity of Ni3V–Ni3Al pseudo-binary alloys)

## Ni-Y
- rank 3545 | 1 samples | 1 papers | 1 compositions
- compositions: YNi2 (1)
- measured range: 11-982 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YNi2 Fd-3m (227) mp-1019 [hull=0.000, icsd=20, PRIMARY]; YNi5 P6/mmm (191) mp-2152 [hull=0.000, icsd=11, PRIMARY]; YNi Pnma (62) mp-1364 [hull=0.000, icsd=5, PRIMARY]; Y3Ni Pnma (62) mp-1105633 [hull=0.000, icsd=2, PRIMARY]; Y2Ni17 P6_3/mmc (194) mp-1196175 [hull=0.016, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/j.jmmm.2010.09.036 (Electrical properties and spin fluctuations studies of Y(Co1−xNix)2 co...)

## Np-O
- rank 3546 | 1 samples | 1 papers | 1 compositions
- compositions: NpO2 (1)
- measured range: 570-1467 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NpO2 Fm-3m (225) mp-2616 [hull=0.000, icsd=6, PRIMARY]; NpO Fm-3m (225) mp-6927 [hull=0.165, icsd=1, PRIMARY]; Np2O3 R-3c (167) mp-1186221 [hull=0.111, PRIMARY]
- papers: https://doi.org/10.1016/j.jnucmat.2009.01.005 (Thermophysical properties of NpO2, AmO2 and CmO2)

## O-Os
- rank 3547 | 1 samples | 1 papers | 1 compositions
- compositions: OsO2 (1)
- measured range: 26-295 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): OsO2 P4_2/mnm (136) mp-996 [hull=0.000, icsd=5, PRIMARY]; Os3O Fm-3m (225) mp-1186352 [hull=1.155, PRIMARY, AMBIGUOUS]; OsO2 Pa-3 (205) mp-1095264 [hull=0.076, icsd=1]; Os3O P6_3/mmc (194) mp-1186373 [hull=1.162]
- papers: https://doi.org/10.1016/j.jcrysgro.2003.10.021 (Growth and characterization of OsO2 single crystals)

## O-Os-Sr
- rank 3548 | 1 samples | 1 papers | 1 compositions
- compositions: SrOsO3 (1)
- measured range: 10-397 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrOsO3 Pnma (62) mp-1105153 [hull=0.070, icsd=4, PRIMARY]; SrOsO2 I4_1/amd (141) mp-1208673 [hull=0.706, PRIMARY]; SrOsO3 Pm-3m (221) mp-867195 [hull=0.102]
- papers: https://doi.org/10.1021/ja4074408 (High-Pressure Synthesis of 5d Cubic Perovskite BaOsO<sub>3</sub> at 17...)

## O-Os-Y
- rank 3549 | 1 samples | 1 papers | 1 compositions
- compositions: Y2Os2O7 (1)
- measured range: 25-302 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YOsO3 Pm-3m (221) mp-979436 [hull=0.734, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.93.134426 (Fragile singlet ground-state magnetism in the pyrochlore osmates<mml:m...)

## O-P-W
- rank 3550 | 1 samples | 1 papers | 1 compositions
- compositions: K1.2P4W8O32 (1)
- dopant candidates (<5% at.): K (1)
- measured range: 12-289 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PWO5 Pna2_1 (33) mp-32540 [hull=0.000, icsd=1, PRIMARY]; P2W2O11 Pnma (62) mp-19522 [hull=0.000, icsd=1, PRIMARY]; P2WO8 C2/m (12) mp-687234 [hull=0.000, icsd=1, PRIMARY, AMBIGUOUS]; P(W3O10)2 P2_12_12_1 (19) mp-652282 [hull=0.003, icsd=1, PRIMARY]; P3RuW2O15 C2/c (15) mp-1194833 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.93.235126 (Detailed investigation of the phase transition in<mml:math xmlns:mml=\...)
