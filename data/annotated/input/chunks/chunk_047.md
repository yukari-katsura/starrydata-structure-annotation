# Host systems -- chunk 047 of 73

Ranks 2301-2350 by sample count. These 50 host systems cover 100 samples (0.19% of the TE set); cumulative through this chunk: 97.45%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Mn-O-Tm
- rank 2301 | 2 samples | 1 papers | 1 compositions
- compositions: TmMnO3 (2)
- measured range: 13-184 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Tm2Mn2O7 Fd-3m (227) mp-769918 [hull=0.000, icsd=1, PRIMARY]; TmMn2O5 Pbam (55) mp-1207725 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.86.174413 (Low-temperature heat transport, specific heat, and magnetic properties...)

## Mo
- rank 2302 | 2 samples | 2 papers | 1 compositions
- compositions: Mo (2)
- measured range: 12-277 K (5th-95th pct of 4 curves; full span incl. outliers 12-1080 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mo Im-3m (229) mp-129 [hull=0.000, icsd=16, PRIMARY]; Mo Fm-3m (225) mp-8637 [hull=0.428, icsd=1]; Mo P6_3/mmc (194) mp-1066523 [hull=0.448, icsd=1]; Mo P2/c (13) mp-1190217 [hull=0.479, icsd=1]; Mo P6/mmm (191) mp-1056004 [hull=0.908, icsd=1]
- papers: https://doi.org/10.1063/1.1735807 (Low‐Temperature Transport Properties of Commercial Metals and Alloys. ...) | https://doi.org/10.1016/j.jnucmat.2008.01.033 (Microstructure and thermal conductivity of Mo–TiC cermets processed by...)

## Mo-O-Y
- rank 2303 | 2 samples | 2 papers | 1 compositions
- compositions: Y2Mo2O7 (2)
- measured range: 12-274 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y5(MoO6)2 C2/m (12) mp-18821 [hull=0.001, icsd=2, PRIMARY]; Y2Mo4O15 P2_1/c (14) mp-1203448 [hull=0.018, icsd=1, PRIMARY]; Y2(MoO4)3 P-42_1m (113) mp-1198660 [hull=0.027, icsd=1, PRIMARY]; Y2Mo2O7 Fd-3m (227) mp-19679 [hull=0.016, icsd=1, PRIMARY]; BaY2(MoO4)4 C2/c (15) mp-1214357 [hull=0.043, PRIMARY]
- papers: https://doi.org/10.1016/0022-3697(86)90030-2 (Thermoelectric power of RE2Mo2O7 pyrochlores) | https://doi.org/10.1016/0022-4596(89)90067-4 (Magnetic and electrical properties of R2Mo2O7 pyrochlore compounds)

## Mo-Ru-Sb-Te
- rank 2304 | 2 samples | 1 papers | 2 compositions
- compositions: Mo2.5Ru0.5Sb6.5Te0.5 (1); Mo2.5Ru0.5Sb6Te (1)
- measured range: 10-1002 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1063/1.3388056 (Transport and magnetic properties of Mo2.5Ru0.5Sb7−xTex)

## Mo-Ru-Se
- rank 2305 | 2 samples | 1 papers | 2 compositions
- compositions: Mo4Ru2Se8 (1); Ti0.3Mo5RuSe8 (1)
- dopant candidates (<5% at.): Ti (1)
- measured range: 286-1273 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mo2RuSe4 P-1 (2) mp-1221499 [hull=0.002, PRIMARY]; Mo2RuSe4 P1 (1) mp-1221491 [hull=0.047]
- papers: https://doi.org/10.1016/j.jssc.2006.04.022 (Thermoelectric and structural properties of a new Chevrel phase: Ti0.3...)

## Mo-Si
- rank 2306 | 2 samples | 1 papers | 2 compositions
- compositions: Mo5Si3 (1); MoSi3 (1)
- measured range: 315-1058 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Si2Mo I4/mmm (139) mp-2592 [hull=0.000, icsd=14, PRIMARY]; SiMo3 Pm-3n (223) mp-1275 [hull=0.000, icsd=9, PRIMARY]; Si3Mo5 I4/mcm (140) mp-1332 [hull=0.000, icsd=5, PRIMARY]; Si2Mo3 P4/mbm (127) mp-1087230 [hull=0.139, icsd=1, PRIMARY]; Si3Mo P6_3/mmc (194) mp-978525 [hull=0.620, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2003.12.008 (Electrical and thermal properties of single crystalline Mo 5 X 3  (X=S...)

## N
- rank 2307 | 2 samples | 2 papers | 1 compositions
- compositions: N2 (2)
- measured range: 11-24 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): N2 Pa-3 (205) mp-25 [hull=0.000, icsd=4, PRIMARY]; N2 P2_13 (198) mp-154 [hull=0.000, icsd=3]; N2 P6_3/mmc (194) mp-1061298 [hull=0.000, icsd=2]; N2 I-43m (217) mp-1080711 [hull=0.000, icsd=1]; N2 Pmna (53) mp-1189505 [hull=0.000, icsd=1]
- papers: https://doi.org/10.1103/physrevb.67.172102 (High thermal conductivity of solid nitrous oxide at low temperatures) | https://doi.org/10.1103/physrevb.74.224302 (Low-temperature thermal conductivity of cryocrystals formed by linear ...)

## N-Np-Pu
- rank 2308 | 2 samples | 1 papers | 2 compositions
- compositions: (NpN)67(PuN)33 (1); (NpN)33(PuN)67 (1)
- measured range: 756-1627 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/s0925-8388(98)00168-6 (Thermal conductivity of actinide mononitride solid solutions)

## N-Pu
- rank 2309 | 2 samples | 2 papers | 1 compositions
- compositions: PuN (2)
- measured range: 433-1874 K (5th-95th pct of 2 curves; full span incl. outliers 433-1981 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PuN Fm-3m (225) mp-1719 [hull=0.000, icsd=7, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2008.05.077 (Thermophysical characterization of ZrN and (Zr,Pu)N) | https://doi.org/10.1016/s0925-8388(01)00875-1 (A molecular dynamics study on uranium–plutonium mixed nitride)

## N-Si
- rank 2310 | 2 samples | 2 papers | 2 compositions
- compositions: (Si3N4)99(Y2O3)0.5(Nd2O3)0.5 (1); (Si3N4)97.8(Y2O3)2.2 (1)
- dopant candidates (<5% at.): O (2), Y (2), Nd (1)
- measured range: 11-1217 K (5th-95th pct of 2 curves; full span incl. outliers 11-1297 K)
- [ref 1] TEDesignLab / ICSD: Si3N4 P6_3/m (176) mp-988 [hull=0.000, icsd=41, PRIMARY]; Si3N4 P31c (159) mp-2245 [hull=0.000, icsd=17]; Si3N4 Fd-3m (227) mp-2075 [hull=0.147, icsd=4]; Si3N4 I-43d (220) mp-11607 [hull=0.100, icsd=1]; Si3N4 Pnma (62) mp-641539 [hull=0.287, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: Si2N3 Cmc2_1 (36) mp-1080623 [hull=0.354, icsd=1, PRIMARY]; Si12HN8 P4mm (99) mp-976267 [hull=0.365, PRIMARY]; Si3N2 Pm-3m (221) mp-971682 [hull=0.251, PRIMARY]; Si3N4 P6_3/mmc (194) mp-40793 [hull=0.493]
- papers: https://doi.org/10.2109/jcersj.104.49 (Effect of Grain Growth on the Thermal Conductivity of Silicon Nitride) | https://doi.org/10.1023/a:1006696126661 (Thermal conductivity of Y2O3-doped Si3N4 ceramic at 4 to 1000 K)

## N-Si-W
- rank 2311 | 2 samples | 2 papers | 2 compositions
- compositions: W3.8Si3N4 (1); SiNW (1)
- measured range: 50-1167 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/j.ceramint.2016.02.001 (Fabrication and contact resistivity of W–Si 3 N 4 /TiB 2 –Si 3 N 4 /p–...) | https://doi.org/10.1002/cssc.201403492 (Thermoelectric Properties of Nanowires with a Graphitic Shell)

## N-Ti-U
- rank 2312 | 2 samples | 1 papers | 1 compositions
- compositions: Ti0.6U0.4N (2)
- measured range: 300-1474 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.jnucmat.2009.01.027 (Thermophysical properties of several nitrides prepared by spark plasma...)

## N-U-Zr
- rank 2313 | 2 samples | 1 papers | 1 compositions
- compositions: Zr0.6U0.4N (2)
- measured range: 291-1271 K (5th-95th pct of 2 curves; full span incl. outliers 291-1475 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZrUN2 I4_1/amd (141) mp-35739 [hull=0.000, PRIMARY, AMBIGUOUS]; ZrUN2 R-3m (166) mp-1215248 [hull=0.000]
- papers: https://doi.org/10.1016/j.jnucmat.2009.01.027 (Thermophysical properties of several nitrides prepared by spark plasma...)

## Na-Nb-O
- rank 2314 | 2 samples | 1 papers | 2 compositions
- compositions: Na0.8Sr0.2NbO3 (1); Na0.85Sr0.15NbO3 (1)
- dopant candidates (<5% at.): Sr (2)
- measured range: 14-276 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NaNbO3 Pm-3m (221) mp-3136 [hull=0.041, icsd=34, PRIMARY]; NaNbO2 P6_3/mmc (194) mp-3744 [hull=0.000, icsd=3, PRIMARY]; Na5NbO5 C2/c (15) mp-5477 [hull=0.000, icsd=2, PRIMARY]; NaNb3O8 Pmmn (59) mp-623854 [hull=0.000, icsd=1, PRIMARY]; Na2Nb4O11 Cc (9) mp-1202153 [hull=0.027, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0038-1098(84)90351-x (Conduction mechanism in polycrystalline Na1−xSrxNbO3 niobium bronzes)

## Na-O-Rh
- rank 2315 | 2 samples | 1 papers | 1 compositions
- compositions:  Na0.83RhO2 (2)
- measured range: 305-797 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NaRhO2 R-3m (166) mp-8830 [hull=0.000, icsd=1, PRIMARY]; Na3Cd(RhO2)8 Pm (6) mp-1221278 [hull=0.018, PRIMARY]
- papers: https://doi.org/10.1038/srep04390 (Superior thermoelectric response in the 3R phases of hydrated Na\n    ...)

## Na-O-W
- rank 2316 | 2 samples | 1 papers | 2 compositions
- compositions: Na0.25WO3 (1); Na0.46WO3 (1)
- measured range: 33-301 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Na2WO4 Fd-3m (227) mp-18803 [hull=0.000, icsd=4, PRIMARY]; NaWO3 Pm-3m (221) mp-19328 [hull=0.052, icsd=3, PRIMARY]; Na2W2O7 Cmce (64) mp-25800 [hull=0.021, icsd=2, PRIMARY]; Na5Y(WO4)4 I4_1/a (88) mp-18944 [hull=0.006, icsd=2, PRIMARY]; Na4W4O15 P-1 (2) mp-1191377 [hull=0.085, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.materresbull.2005.05.001 (Synthesis and electrical properties of cubic NaxWO3 thin films across ...)

## Na-Si
- rank 2317 | 2 samples | 2 papers | 2 compositions
- compositions: Na22Si136 (1); Na8Si46 (1)
- measured range: 11-300 K (5th-95th pct of 2 curves)
- [ref 1] TEDesignLab / ICSD: NaSi C2/c (15) mp-2402 [hull=0.000, icsd=4, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Na4Si23 Pm-3n (223) mp-186 [hull=0.007, icsd=18, PRIMARY]; NaSi6 Cmcm (63) mp-1104400 [hull=0.044, icsd=1, PRIMARY]; Na3Si34 R-3m (166) mp-1221235 [hull=0.029, PRIMARY]; Na3Si17 Fd-3m (227) mp-1180295 [hull=0.000, PRIMARY]; Na3Si Fm-3m (225) mp-1186079 [hull=0.160, PRIMARY]
- papers: https://doi.org/10.1007/s11664-008-0641-y (Synthesis, Crystal Structure, and Transport Properties of Na22Si136) | https://doi.org/10.1103/physrevb.64.153201 (Transport properties ofNa8Si46)

## Nb-O-Y-Zr
- rank 2318 | 2 samples | 1 papers | 1 compositions
- compositions: (Nb2O5)10(Y2O3)10(ZrO2)80 (2)
- measured range: 377-1261 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/s1359-6454(00)00295-0 (Thermal properties of zirconia co-doped with trivalent and pentavalent...)

## Nb-Rh
- rank 2319 | 2 samples | 2 papers | 1 compositions
- compositions: Rh3Nb (2)
- measured range: 301-1099 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NbRh P4/mmm (123) mp-1963 [hull=0.000, icsd=2, PRIMARY]; NbRh3 Pm-3m (221) mp-2449 [hull=0.000, icsd=2, PRIMARY]; Nb3Rh Pm-3n (223) mp-1545 [hull=0.000, icsd=2, PRIMARY]; Nb4Rh Fmmm (69) mp-1220441 [hull=0.102, PRIMARY]; NbRh2 Pm (6) mp-1220414 [hull=0.104, PRIMARY]
- papers: https://doi.org/10.1595/147106706x106182 (Thermophysical Properties of Rh<SUB>3</SUB>X for Ultra-High Temperatur...) | https://doi.org/10.1016/s0925-8388(03)00006-9 (Thermal conductivity and thermal expansion of L12 intermetallic compou...)

## Nb-S-Yb
- rank 2320 | 2 samples | 2 papers | 2 compositions
- compositions: (Yb1.90S2)0.62NbS2 (1); (Yb2S2)2NbS2 (1)
- measured range: 10-301 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1143/jjap.43.l1202 (Preparation and Thermoelectric Properties of Misfit-Layered Sulfide [Y...) | https://doi.org/10.1007/s11664-012-2443-5 (Crystal Structure and Thermoelectric Properties of Misfit-Layered Sulf...)

## Nb-Ta-Te
- rank 2321 | 2 samples | 1 papers | 2 compositions
- compositions: Ta0.8Nb0.2Te2 (1); Ta0.5Nb0.5Te2 (1)
- measured range: 11-319 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TaNbTe4 P1 (1) mp-1217942 [hull=0.004, PRIMARY]
- papers: https://doi.org/10.1209/0295-5075/109/17003 (Structural, electrical, and thermoelectric properties of distorted 1T-...)

## Nd
- rank 2322 | 2 samples | 1 papers | 1 compositions
- compositions: Nd (2)
- measured range: 10-291 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd P6_3/mmc (194) mp-123 [hull=0.000, icsd=10, PRIMARY]; Nd Fm-3m (225) mp-159 [hull=0.011, icsd=2]; Nd Im-3m (229) mp-4 [hull=0.133, icsd=2]; Nd R-3m (166) mp-974788 [hull=0.007]
- papers: https://doi.org/10.1063/1.325726 (Thermoelectric power of Nd1−xLaxand Ce1−xLaxalloys)

## Nd-O
- rank 2323 | 2 samples | 1 papers | 1 compositions
- compositions: NdO (2)
- measured range: 15-271 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd2O3 P-3m1 (164) mp-2763 [hull=0.030, icsd=11, PRIMARY]; NdO3 P6_3/m (176) mp-1180065 [hull=0.410, icsd=4, PRIMARY]; NdO2 I4/mmm (139) mp-1077718 [hull=0.079, icsd=2, PRIMARY]; NdO Fm-3m (225) mp-754545 [hull=0.080, PRIMARY]; Nd2O5 C2/c (15) mp-985608 [hull=0.031, PRIMARY]
- papers: https://doi.org/10.1016/0375-9601(80)90035-3 (Transport properties of SmO)

## Nd-O-Ru
- rank 2324 | 2 samples | 2 papers | 1 compositions
- compositions: Nd2Ru2O7 (2)
- measured range: 294-849 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd2Ru2O7 Fd-3m (227) mp-19930 [hull=0.010, icsd=11, PRIMARY]; Nd3RuO7 Cmcm (63) mp-17753 [hull=0.000, icsd=2, PRIMARY, AMBIGUOUS]; Nd2RuO5 Pnma (62) mp-1210187 [hull=0.089, PRIMARY]; Nd3RuO7 P2_1/m (11) mp-1204904 [hull=0.003, icsd=2]; Nd3RuO7 Pnma (62) mp-1200843 [hull=0.001, icsd=1]
- papers: https://doi.org/10.1088/0953-8984/25/18/186004 (Structural disorder, magnetism, and electrical and thermoelectric prop...) | https://doi.org/10.1007/s12034-017-1491-0 (Chemical synthesis and characterization of nano-sized rare-earth ruthe...)

## Nd-O-Sn
- rank 2325 | 2 samples | 1 papers | 2 compositions
- compositions: Nd2Sn2O7 (1); (Yb2Zr2O7)0.2(Nd2Sn2O7)0.8 (1)
- dopant candidates (<5% at.): Yb (1), Zr (1)
- measured range: 298-1272 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd2Sn2O7 Fd-3m (227) mp-17114 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1111/jace.13979 (Low Thermal Conductivity of Rare-Earth Zirconate-Stannate Solid Soluti...)

## Ni-P
- rank 2326 | 2 samples | 1 papers | 1 compositions
- compositions: NiP2 (2)
- measured range: 12-298 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ni2P P-62m (189) mp-21167 [hull=0.003, icsd=7, PRIMARY]; Ni3P I-4 (82) mp-2296 [hull=0.000, icsd=6, PRIMARY]; Ni5P4 P6_3mc (186) mp-1920 [hull=0.000, icsd=4, PRIMARY]; NiP2 C2/c (15) mp-486 [hull=0.011, icsd=3, PRIMARY]; Ni12P5 I4/m (87) mp-2790 [hull=0.000, icsd=3, PRIMARY]
- papers: https://doi.org/10.1021/acs.chemmater.9b00565 (NiP2: A Story of Two Divergent Polymorphic Multifunctional Materials)

## Ni-Pt-Sb-U
- rank 2327 | 2 samples | 1 papers | 1 compositions
- compositions: U3Ni1.9Co0.1PtSb4 (2)
- dopant candidates (<5% at.): Co (2)
- measured range: 11-349 K (5th-95th pct of 7 curves)
- papers: https://doi.org/10.1063/1.5128593 (Uranium-based materials for thermoelectric applications)

## Ni-Sb
- rank 2328 | 2 samples | 2 papers | 2 compositions
- compositions: NiSb (1); Ni4Sb12 (1)
- measured range: 201-690 K (5th-95th pct of 3 curves; full span incl. outliers 201-946 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NiSb P6_3/mmc (194) mp-810 [hull=0.000, icsd=12, PRIMARY]; NiSb2 Pnnm (58) mp-19895 [hull=0.000, icsd=9, PRIMARY]; Ni3Sb Pmmn (59) mp-672371 [hull=0.000, icsd=3, PRIMARY]; NiSb3 Im-3 (204) mp-1106023 [hull=0.008, icsd=2, PRIMARY]; Ni5Sb2 C2/m (12) mp-2409 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.1545158 (Effect of NiSb on the thermoelectric properties of skutterudite CoSb3) | https://doi.org/10.1063/1.1781762 (Structural study of Fe doped and Ni substituted thermoelectric skutter...)

## Ni-Sb-Sn-Te
- rank 2329 | 2 samples | 1 papers | 1 compositions
- compositions: (Sn12Sb2Te15)25.95(NiTe2)74.05 (2)
- measured range: 298-774 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.1002/zaac.202000224 (Hall‐effect Measurements and Transport Properties of Heterostructures ...)

## Ni-Sb-Sn-Tm
- rank 2330 | 2 samples | 1 papers | 2 compositions
- compositions: (TmNiSb)0.75(TmNiSn)0.25 (1); (TmNiSb)0.3(TmNiSn)0.7 (1)
- measured range: 312-1004 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1063/1.5038395 (Power factor enhancement in a composite based on the half-Heusler anti...)

## Ni-Sb-Sn-Zr
- rank 2331 | 2 samples | 2 papers | 2 compositions
- compositions: NiZrSn0.72Sb0.28 (1); ZrNiSn0.8Sb0.2 (1)
- measured range: 320-854 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zr10NiSnSb4 I422 (97) mp-1215855 [hull=0.022, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(03)00547-4 (High temperature thermoelectric properties of NiZrSn half-Heusler comp...) | https://doi.org/10.1016/j.jallcom.2006.02.075 (Thermoelectric properties of half-Heusler alloys Zr1−xYxNiSn1−ySby)

## Ni-Sb-Y
- rank 2332 | 2 samples | 2 papers | 1 compositions
- compositions: YNiSb (2)
- measured range: 20-399 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YNiSb F-43m (216) mp-11520 [hull=0.000, icsd=1, PRIMARY]; Y5Ni2Sb I4/mcm (140) mp-1207758 [hull=0.006, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/15/4/304 (Thermoelectrical properties of the compounds ScMVIIISb and YMVIIISb (M...) | https://doi.org/10.1557/proc-545-421 (Observed Properties and Electronic Structure of RNiSb Compounds (R = H...)

## Ni-Si-U
- rank 2333 | 2 samples | 1 papers | 1 compositions
- compositions: UNi2Si2 (2)
- measured range: 14-294 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U(SiNi)2 I4/mmm (139) mp-20596 [hull=0.000, icsd=6, PRIMARY]; U3(SiNi)4 Immm (71) mp-9903 [hull=0.040, icsd=1, PRIMARY]; U2(Si2Ni)3 Cmmm (65) mp-1207979 [hull=0.015, PRIMARY]; U(SiNi5)2 Immm (71) mp-1217045 [hull=0.036, PRIMARY]; U2Si3Ni Pmm2 (25) mp-1216879 [hull=0.030, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/3/24/010 (Magnet susceptibility, thermoelectric power and specific heat of UNi2Si2)

## Ni-Si-Yb
- rank 2334 | 2 samples | 2 papers | 2 compositions
- compositions: YbNi4Si (1); YbNi2Si2 (1)
- measured range: 11-296 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(SiNi)2 I4/mmm (139) mp-5916 [hull=0.000, icsd=2, PRIMARY]; Yb3(SiNi3)2 Im-3m (229) mp-1191851 [hull=0.000, icsd=1, PRIMARY]; YbSi2Ni Cmcm (63) mp-972406 [hull=0.000, icsd=1, PRIMARY]; YbSi3Ni5 Pnma (62) mp-1201820 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.materresbull.2007.02.041 (Specific heat, electrical resistivity and thermoelectric power of YbNi4Si) | https://doi.org/10.1023/a:1021801903961 (Thermopower of Yb Heavy Fermion Compounds at High Pressure)

## Ni-Sn-Y-Zr
- rank 2335 | 2 samples | 1 papers | 2 compositions
- compositions: Zr0.8Y0.2NiSn (1); Zr0.75Y0.25NiSn (1)
- measured range: 80-370 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.jssc.2009.12.009 (Synthesis, electronic transport and magnetic properties of Zr1−xYxNiSn...)

## Ni-Sn-Yb
- rank 2336 | 2 samples | 2 papers | 1 compositions
- compositions: YbNiSn (2)
- measured range: 10-294 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbNiSn Pnma (62) mp-22162 [hull=0.000, icsd=5, PRIMARY]; Yb5(Ni2Sn5)2 P4/mbm (127) mp-1198689 [hull=0.000, icsd=1, PRIMARY]; Yb7Ni4Sn13 P4/m (83) mp-1191537 [hull=0.000, icsd=1, PRIMARY]; YbNi4Sn F-43m (216) mp-1207519 [hull=0.009, PRIMARY]
- papers: https://doi.org/10.1016/s0921-4526(98)00397-4 (Crystal field excitations in the ferromagnetic Kondo lattice: YbNiSn) | https://doi.org/10.1023/a:1021801903961 (Thermopower of Yb Heavy Fermion Compounds at High Pressure)

## O-P-Zr
- rank 2337 | 2 samples | 1 papers | 2 compositions
- compositions: (Ca0.5Sr0.5Zr4P6O24)4(Y0.08Zr0.94O2)96 (1); (Ca0.5Sr0.5Zr4P6O24)5.09(Y0.08Zr0.94O2)94.91 (1)
- dopant candidates (<5% at.): Y (2), Ca (2), Sr (2)
- measured range: 325-1474 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZrP2O7 Pa-3 (205) mp-5024 [hull=0.000, icsd=10, PRIMARY]; Zr2P2O9 Cmce (64) mp-27132 [hull=0.001, icsd=6, PRIMARY]; ZrP2O9 P2_1/c (14) mp-1197919 [hull=0.297, icsd=2, PRIMARY]; CsZr2Al(PO4)4 Pbcm (57) mp-1019720 [hull=0.000, icsd=1, PRIMARY]; Zr(PO5)2 P2_1 (4) mp-1178611 [hull=0.443, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/s0921-5093(99)00468-2 (The role of NZP additions in plasma-sprayed YSZ: microstructure, therm...)

## O-Pb-Re
- rank 2338 | 2 samples | 2 papers | 2 compositions
- compositions: Pb2Re2O7 (1); PbRe2O5 (1)
- measured range: 13-377 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Re2PbO8 P31m (157) mp-29305 [hull=0.000, icsd=1, PRIMARY]; Re3Pb3O10 I4_1/amd (141) mp-677311 [hull=0.048, PRIMARY]; Re4Pb4O13 F-43m (216) mp-1219547 [hull=0.062, PRIMARY]; Re6Pb5O19 P2/c (13) mp-674367 [hull=0.006, PRIMARY]; Re6Pb6O19 Pnn2 (34) mp-758073 [hull=0.008, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.83.125103 (Structural and electronic properties of pyrochlore-type<mml:math xmlns...) | https://doi.org/10.1016/j.jssc.2020.121359 (Spin–orbit-coupled metal candidate PbRe2O6)

## O-Ru-Sn-Sr
- rank 2339 | 2 samples | 1 papers | 2 compositions
- compositions: SrRu0.33Sn0.67O3 (1); SrRu0.56Sn0.44O3 (1)
- measured range: 11-300 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1063/5.0061902 (Effects of Sn substitution in SrRuO<sub>3</sub> epitaxial films)

## O-Ru-Y
- rank 2340 | 2 samples | 1 papers | 2 compositions
- compositions: Y2Ru2O7 (1); Bi0.5Y1.5Ru2O7 (1)
- dopant candidates (<5% at.): Bi (1)
- measured range: 475-1077 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y2Ru2O7 Fd-3m (227) mp-20643 [hull=0.024, icsd=2, PRIMARY]
- papers: https://doi.org/10.2109/jcersj.112.298 (Thermoelectric Properties of CuO-Added AgSbO3 Ceramics)

## O-Sm-Sn
- rank 2341 | 2 samples | 1 papers | 2 compositions
- compositions: (Yb2Zr2O7)0.2(Sm2Sn2O7)0.8 (1); Sm2Sn2O7 (1)
- dopant candidates (<5% at.): Yb (1), Zr (1)
- measured range: 298-1272 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sm2Sn2O7 Fd-3m (227) mp-2883 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1111/jace.13979 (Low Thermal Conductivity of Rare-Earth Zirconate-Stannate Solid Soluti...)

## O-Sr-Ta-Ti
- rank 2342 | 2 samples | 1 papers | 2 compositions
- compositions: Sr0.85Ti0.70Ta0.30O3 (1); SrTi0.70Ta0.30O3 (1)
- measured range: 369-1268 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr3Ta2Ti6O21 P6_3/mcm (193) mp-1208814 [hull=0.054, PRIMARY]; Sr3Ta4Ti4O21 C2/c (15) mp-1218665 [hull=0.030, PRIMARY]; Sr3Ta4TiO15 Pc (7) mp-1218658 [hull=0.037, PRIMARY]
- papers: https://doi.org/10.1021/acs.chemmater.5b01389 (Boosting Thermoelectric Performance by Controlled Defect Chemistry Eng...)

## O-Sr-W
- rank 2343 | 2 samples | 1 papers | 1 compositions
- compositions: SrWO4 (2)
- measured range: 303-544 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrWO4 I4_1/a (88) mp-19163 [hull=0.000, icsd=10, PRIMARY]; Sr3WO6 Cc (9) mp-1203086 [hull=0.013, icsd=1, PRIMARY, AMBIGUOUS]; Sr2WO5 Pnma (62) mp-772676 [hull=0.006, icsd=1, PRIMARY]; Sr5W3O14 Cc (9) mp-779884 [hull=0.020, PRIMARY, AMBIGUOUS]; Sr3W2O9 R-3c (167) mp-769815 [hull=0.072, PRIMARY]
- papers: https://doi.org/10.1063/1.2335510 (Growth and thermal properties of SrWO4 single crystal)

## O-Ta-Y-Zr
- rank 2344 | 2 samples | 1 papers | 1 compositions
- compositions: (Ta2O5)10(Y2O3)10(ZrO2)80 (2)
- measured range: 381-1063 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/s1359-6454(00)00295-0 (Thermal properties of zirconia co-doped with trivalent and pentavalent...)

## O-Te
- rank 2345 | 2 samples | 2 papers | 1 compositions
- compositions: TeO2 (2)
- measured range: 80-300 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TeO2 P4_12_12 (92) mp-557 [hull=0.011, icsd=10, PRIMARY]; TeO3 R-3c (167) mp-2552 [hull=0.000, icsd=5, PRIMARY]; Te2O5 P2_1 (4) mp-12177 [hull=0.000, icsd=2, PRIMARY]; TeO6 Fd-3c (228) mp-1201116 [hull=0.782, icsd=1, PRIMARY]; NaU(Te3O8)2 Pa-3 (205) mp-1195585 [hull=0.047, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2020.156630 (Effects of inorganic salt NaNbO3 composite on the thermoelectric prope...) | https://doi.org/10.1016/0038-1098(81)90677-3 (Temperature dependence of the thermal conductivity for tellurium dioxide)

## O-Ti-Y
- rank 2346 | 2 samples | 1 papers | 1 compositions
- compositions: YTiO3 (2)
- measured range: 180-304 K (5th-95th pct of 2 curves)
- [ref 1] TEDesignLab / ICSD: Y2Ti2O7 Fd-3m (227) mp-5373 [hull=0.009, icsd=15, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: YTiO3 Pnma (62) mp-4355 [hull=0.059, icsd=5, PRIMARY]; Y2TiO5 Pnma (62) mp-17559 [hull=0.000, icsd=2, PRIMARY]; Y16Ti16O35 P1 (1) mp-685259 [hull=0.333, PRIMARY]; Y4Ti3SnO14 R-3m (166) mp-1216103 [hull=0.011, PRIMARY]; Y2Ti2O7 C2/m (12) mp-685370 [hull=0.041]
- papers: https://doi.org/10.1103/physrevb.71.184431 (Evidence for two electronic phases inY1−xLaxTiO3from thermoelectric an...)

## O-V-Y
- rank 2347 | 2 samples | 2 papers | 2 compositions
- compositions: VYO (1); Ca0.1Y0.9VO3 (1)
- dopant candidates (<5% at.): Ca (1)
- measured range: 123-292 K (5th-95th pct of 2 curves; full span incl. outliers 123-383 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YVO3 Pnma (62) mp-18883 [hull=0.000, icsd=14, PRIMARY]; YVO4 I4_1/amd (141) mp-19133 [hull=0.000, icsd=9, PRIMARY]; Y2VO5 C2/c (15) mp-1201610 [hull=0.062, icsd=1, PRIMARY]; Y2V2O7 Fd-3m (227) mp-642779 [hull=0.670, icsd=1, PRIMARY]; GdY3V4O16 C222 (21) mp-1224509 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.ceramint.2020.05.053 (Abnormal dependence of microstructures and electrical properties of Y-...) | https://doi.org/10.1007/s12043-002-0164-7 (Local-moment formation and metal-nonmetal transition in Ca1−x Y x VO3 ...)

## Os-Sb-Sr
- rank 2348 | 2 samples | 1 papers | 1 compositions
- compositions: SrOs4Sb12 (2)
- measured range: 11-286 K (5th-95th pct of 3 curves; full span incl. outliers 11-499 K)
- papers: https://doi.org/10.1016/j.physb.2006.03.067 (Roles of spin fluctuations and rattling in magnetic and thermoelectric...)

## P-Ru
- rank 2349 | 2 samples | 1 papers | 2 compositions
- compositions: La0.3Ce0.7Ru4P12 (1); La0.2Ce0.8Ru4P12 (1)
- dopant candidates (<5% at.): Ce (2), La (2)
- measured range: 99-678 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): P2Ru Pnnm (58) mp-1413 [hull=0.000, icsd=5, PRIMARY]; PRu Pnma (62) mp-12636 [hull=0.000, icsd=2, PRIMARY]; PRu2 Pnma (62) mp-21911 [hull=0.000, icsd=2, PRIMARY]; P4Ru P-1 (2) mp-27173 [hull=0.000, icsd=1, PRIMARY]; P3Ru P-1 (2) mp-28400 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1109/ict.2002.1190265 (La doping effect in thermoelectric properties of skutterudite compound...)

## P-S-Th
- rank 2350 | 2 samples | 1 papers | 1 compositions
- compositions: ThPS (2)
- measured range: 10-315 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ThPS P4/nmm (129) mp-12876 [hull=0.002, icsd=2, PRIMARY]; Th(PS3)2 P4_2/m (84) mp-14249 [hull=0.000, icsd=1, PRIMARY]; Th2P2S P4/mmm (123) mp-1207155 [hull=1.723, PRIMARY]; Th2PS2 P4/mmm (123) mp-1208352 [hull=3.534, PRIMARY]
- papers: https://doi.org/10.1016/j.ssc.2004.11.017 (Crystal growth, structure and electrical properties of thorium phospho...)
