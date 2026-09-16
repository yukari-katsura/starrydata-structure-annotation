# Host systems -- chunk 072 of 73

Ranks 3551-3600 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 99.91%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## O-Pb
- rank 3551 | 1 samples | 1 papers | 1 compositions
- compositions: PbO (1)
- measured range: 291-663 K (5th-95th pct of 1 curves)
- [ref 1] TEDesignLab / ICSD: PbO P4/nmm (129) mp-19921 [hull=0.000, icsd=21, PRIMARY]; Pb3O4 P4_2/mbc (135) mp-22633 [hull=0.000, icsd=13, PRIMARY]; Pb2O3 P2_1/c (14) mp-20078 [hull=0.010, icsd=1, PRIMARY]; PbO2 P4_2/mnm (136) mp-20725 [hull=0.000, icsd=7]; Pb3O4 Pbam (55) mp-21452 [hull=0.000, icsd=7]
- [ref 2] MP, ranked by ICSD evidence: PbO2 Pnma (62) mp-1101843 [hull=0.058, icsd=9, PRIMARY]; Pb3O Pm-3m (221) mp-1186421 [hull=0.731, PRIMARY, AMBIGUOUS]; Pb3O5 Cmce (64) mp-651870 [hull=0.043, PRIMARY]; PbO2 Pbcn (60) mp-20633 [hull=0.008, icsd=6]; PbO2 Fm-3m (225) mp-20158 [hull=0.106, icsd=1]
- papers: https://doi.org/10.1109/icsd.2004.1350310 (Electrical and thermal properties of Bi/sub 2/O/sub 3/, PbO and mixed ...)

## O-Pb-Te
- rank 3552 | 1 samples | 1 papers | 1 compositions
- compositions: Pb0.409Te0.417Ag0.012O0.162 (1)
- dopant candidates (<5% at.): Ag (1)
- measured range: 295-398 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TePb2O5 C2/c (15) mp-1105700 [hull=0.000, icsd=2, PRIMARY]; Te3(PbO4)2 Cmcm (63) mp-21922 [hull=0.000, icsd=2, PRIMARY]; Te5PbO11 C2/c (15) mp-1203659 [hull=0.009, icsd=1, PRIMARY]; TePb5O8 P2_1/c (14) mp-1201764 [hull=0.000, icsd=1, PRIMARY]; TePb2O5 Cc (9) mp-624234 [hull=0.000, icsd=1]
- papers: https://doi.org/10.1063/1.4984050 (Enhancement of thermoelectric power of PbTe thin films by Ag ion impla...)

## O-Pr-Ru
- rank 3553 | 1 samples | 1 papers | 1 compositions
- compositions: Pr2Ru2O7 (1)
- measured range: 380-822 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Pr2Ru2O7 Fd-3m (227) mp-3430 [hull=0.044, icsd=3, PRIMARY]; Pr3RuO7 Cmcm (63) mp-5433 [hull=0.000, icsd=2, PRIMARY]; PrRuO3 Pnma (62) mp-20186 [hull=0.078, icsd=1, PRIMARY]; Pr3Bi(Ru2O7)2 R-3m (166) mp-1219861 [hull=0.023, PRIMARY]; Pr2RuO5 Pnma (62) mp-1209517 [hull=0.126, PRIMARY]
- papers: https://doi.org/10.1007/s12034-017-1491-0 (Chemical synthesis and characterization of nano-sized rare-earth ruthe...)

## O-Pu-Th
- rank 3554 | 1 samples | 1 papers | 1 compositions
- compositions: Th0.7Pu0.3O2 (1)
- measured range: 498-1392 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jallcom.2014.12.204 (Thermal conductivity of UO2 and PuO2 from first-principles)

## O-Pu-U
- rank 3555 | 1 samples | 1 papers | 1 compositions
- compositions: (U)82.26(PuO2)17.74 (1)
- measured range: 773-1273 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jnucmat.2017.11.010 (U-PuO2, U-PuC, U-PuN cermet fuel for fast reactor)

## O-Rb-Ta-W
- rank 3556 | 1 samples | 1 papers | 1 compositions
- compositions: RbTaWO6 (1)
- measured range: 378-980 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1007/s11664-012-2382-1 (Extremely Low Thermal Conductivity in Oxides with Cage-Like Crystal St...)

## O-Rb-W
- rank 3557 | 1 samples | 1 papers | 1 compositions
- compositions: RbFe0.33W1.67O6 (1)
- dopant candidates (<5% at.): Fe (1)
- measured range: 328-1026 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Rb2WO4 C2/m (12) mp-18864 [hull=0.000, icsd=2, PRIMARY]; Rb(WO3)3 P6mm (183) mp-1194279 [hull=0.008, icsd=1, PRIMARY, AMBIGUOUS]; Rb2W2O7 P2_1/c (14) mp-19144 [hull=0.000, icsd=1, PRIMARY]; Rb(WO4)8 C2/m (12) mp-1198691 [hull=0.350, icsd=1, PRIMARY]; Rb(WO3)6 Pnnm (58) mp-698610 [hull=0.000, PRIMARY, AMBIGUOUS]
- papers: https://doi.org/10.1007/s11664-015-4179-5 (Crystal Structure and Thermoelectric Properties of β-Pyrochlore-Type A...)

## O-Rh-Te
- rank 3558 | 1 samples | 1 papers | 1 compositions
- compositions: Rh2TeO6 (1)
- measured range: 319-806 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Te(RhO3)2 P4_2/mnm (136) mp-1208293 [hull=0.044, PRIMARY]
- papers: https://doi.org/10.1016/j.materresbull.2011.07.007 (Synthesis, magnetic and thermoelectric properties of Rh2MO6 (M=Mo, Te,...)

## O-Rh-W
- rank 3559 | 1 samples | 1 papers | 1 compositions
- compositions: Rh2WO6 (1)
- measured range: 322-804 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Rh2WO6 P4_2/mnm (136) mp-1209123 [hull=0.023, PRIMARY]
- papers: https://doi.org/10.1016/j.materresbull.2011.07.007 (Synthesis, magnetic and thermoelectric properties of Rh2MO6 (M=Mo, Te,...)

## O-Ru-Sm
- rank 3560 | 1 samples | 1 papers | 1 compositions
- compositions: Sm2Ru2O7 (1)
- measured range: 286-768 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sm3RuO7 Cmcm (63) mp-5779 [hull=0.005, icsd=2, PRIMARY]; Sm2Ru2O7 Fd-3m (227) mp-17113 [hull=0.008, icsd=1, PRIMARY]; Sm2RuO5 Pnma (62) mp-1209143 [hull=0.106, PRIMARY]; Sm3Bi(Ru2O7)2 R-3m (166) mp-1219209 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1007/s12034-017-1491-0 (Chemical synthesis and characterization of nano-sized rare-earth ruthe...)

## O-Ru-Sr-Y
- rank 3561 | 1 samples | 1 papers | 1 compositions
- compositions: Sr2YRuO6 (1)
- measured range: 312-1246 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2YRuO6 P2_1/c (14) mp-14430 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2008.09.003 (High-temperature thermoelectric properties of Sr2RuYO6 and Sr2RuErO6 d...)

## O-Sc-Si
- rank 3562 | 1 samples | 1 papers | 1 compositions
- compositions: Sc2SiO5 (1)
- measured range: 293-293 K (5th-95th pct of 1 curves)
- [ref 1] TEDesignLab / ICSD: Sc2Si2O7 C2/m (12) mp-5594 [hull=0.000, icsd=4, PRIMARY]; Sc2Si2O7 Fd-3m (227) mp-7640 [hull=0.085, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: SrSc4Si5O17 P2_1/m (11) mp-1198043 [hull=0.003, icsd=1, PRIMARY]; Sc2SiO5 C2/c (15) mp-1209079 [hull=0.017, PRIMARY]; ScSiO3 Pm-3m (221) mp-1186993 [hull=0.709, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2020.06.012 (Tailoring thermal properties of multi-component rare earth monosilicates)

## O-Sm-Ti
- rank 3563 | 1 samples | 1 papers | 1 compositions
- compositions: Sm0.6Ca0.1TiO3 (1)
- dopant candidates (<5% at.): Ca (1)
- measured range: 327-911 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sm2Ti2O7 Fd-3m (227) mp-3335 [hull=0.010, icsd=4, PRIMARY]; Sm2TiO5 Pnma (62) mp-770806 [hull=0.000, icsd=2, PRIMARY]; SmTiO3 Pnma (62) mp-22416 [hull=0.049, icsd=2, PRIMARY]; Sm2Ti2O5 Imma (74) mp-1099757 [hull=0.198, PRIMARY]; Sm3MgTi4O14 R-3m (166) mp-1219216 [hull=0.054, PRIMARY]
- papers: https://doi.org/10.1007/s11664-014-3058-9 (Neodymium-Strontium Titanate: A New Ceramic for an Old Problem)

## O-Sn-Te
- rank 3564 | 1 samples | 1 papers | 1 compositions
- compositions: (SnTe)89.82(MnO2)10.18 (1)
- dopant candidates (<5% at.): Mn (1)
- measured range: 299-873 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SnTe3O8 Ia-3 (206) mp-12231 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/acs.chemmater.9b00747 (Facile Route to High-Performance SnTe-Based Thermoelectric Materials: ...)

## O-Sn-Yb
- rank 3565 | 1 samples | 1 papers | 1 compositions
- compositions: Yb2Sn2O7 (1)
- measured range: 297-1270 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb2Sn2O7 Fd-3m (227) mp-20342 [hull=0.009, icsd=1, PRIMARY]; Yb3SnO Pm-3m (221) mp-11651 [hull=0.000, icsd=1, PRIMARY]; YbSnO3 Pm-3m (221) mp-1187515 [hull=0.126, PRIMARY]
- papers: https://doi.org/10.1111/jace.15504 (Thermophysical properties of rare earth barium aluminates)

## O-Ta-Yb
- rank 3566 | 1 samples | 1 papers | 1 compositions
- compositions: YbTa3O9 (1)
- measured range: 373-1073 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbTaO4 P2/c (13) mp-4574 [hull=0.000, icsd=2, PRIMARY]; Yb4Ta25O68 P-62c (190) mp-1202362 [hull=0.000, icsd=1, PRIMARY]; YbTaO3 Pm-3m (221) mp-1187479 [hull=0.025, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2021.117152 (Spontaneously formed nanostructures in double perovskite rare-earth ta...)

## O-Tb-W
- rank 3567 | 1 samples | 1 papers | 1 compositions
- compositions: (WO)0.95(Tb4O7)0.05 (1)
- measured range: 520-971 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Tb2(WO4)3 P2_1/c (14) mp-770516 [hull=0.016, PRIMARY]; Tb2WO6 P2_12_12_1 (19) mp-771443 [hull=0.000, PRIMARY, AMBIGUOUS]; TbWO5 P2_1/c (14) mp-1208379 [hull=0.130, PRIMARY]; Tb2(WO4)3 C2/c (15) mp-770351 [hull=0.034]; Tb2(WO4)3 Pba2 (32) mp-770342 [hull=0.043]
- papers: https://doi.org/10.1007/s10854-013-1353-5 (Microstructure and thermoelectric properties of tungsten trioxide cera...)

## O-Te-Ti
- rank 3568 | 1 samples | 1 papers | 1 compositions
- compositions: TiTe3O8 (1)
- measured range: 303-572 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiTe3O8 Ia-3 (206) mp-5214 [hull=0.000, icsd=2, PRIMARY]; Ti3TeO8 P1 (1) mp-774922 [hull=0.074, PRIMARY]; TiTeO3 Pm-3m (221) mp-1187488 [hull=0.595, PRIMARY]
- papers: https://doi.org/10.1039/c7tc05382g (Tailored fabrication of a prospective acousto–optic crystal TiTe3O8 en...)

## O-Ti-Zr
- rank 3569 | 1 samples | 1 papers | 1 compositions
- compositions: Zr0.76Y0.08Ti0.16O1.96 (1)
- dopant candidates (<5% at.): Y (1)
- measured range: 472-1273 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZrTi2O P6/mmm (191) mp-27296 [hull=0.324, icsd=1, PRIMARY]; Zr3TiO8 I-42m (121) mp-1207388 [hull=0.033, PRIMARY]; Zr5Ti7O24 Pc (7) mp-761840 [hull=0.031, PRIMARY, AMBIGUOUS]; ZrTi2O6 P1 (1) mp-757504 [hull=0.047, PRIMARY]; ZrTiO3 Pm-3m (221) mp-1183045 [hull=0.725, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2013.05.038 (Effect of lattice defects on thermal conductivity of Ti-doped, Y2O3-st...)

## O-Tl
- rank 3570 | 1 samples | 1 papers | 1 compositions
- compositions: Tl2O3 (1)
- measured range: 22-298 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Tl2O3 Ia-3 (206) mp-1658 [hull=0.000, icsd=8, PRIMARY]; Tl2O R-3m (166) mp-27484 [hull=0.000, icsd=1, PRIMARY]; Tl4O3 P2_1/m (11) mp-27684 [hull=0.000, icsd=1, PRIMARY]; TlO Aem2 (39) mp-1179154 [hull=0.095, icsd=1, PRIMARY]; TlO2 Pnnm (58) mp-1188665 [hull=0.347, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0025-5408(70)90031-0 (Single crystal data for “TlOF” and Tl2O3)

## O-Tm
- rank 3571 | 1 samples | 1 papers | 1 compositions
- compositions: Tm2O3 (1)
- measured range: 298-673 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Tm2O3 Ia-3 (206) mp-1767 [hull=0.000, icsd=7, PRIMARY]; TmO3 P6_3/m (176) mp-1178953 [hull=0.454, icsd=1, PRIMARY]; TmO2 P2_1/m (11) mp-1206313 [hull=0.180, PRIMARY]; Tm2O3 P-3m1 (164) mp-13067 [hull=0.081, icsd=1]; TmO3 Fm-3m (225) mp-979074 [hull=0.555]
- papers: https://doi.org/10.1016/j.jeurceramsoc.2020.07.029 (Vacuum sintering of novel transparent Tm2O3 ceramics: Effect of silica...)

## O-V-Zn
- rank 3572 | 1 samples | 1 papers | 1 compositions
- compositions: Zn1.5Cu0.5V2O7 (1)
- dopant candidates (<5% at.): Cu (1)
- measured range: 422-823 K (5th-95th pct of 3 curves; full span incl. outliers 422-922 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): V2ZnO4 Fd-3m (227) mp-18879 [hull=0.000, icsd=4, PRIMARY]; V2Zn2O7 C2/c (15) mp-19707 [hull=0.000, icsd=1, PRIMARY]; V2ZnO6 C2 (5) mp-1178789 [hull=0.028, icsd=1, PRIMARY]; V2Zn3O8 Cmce (64) mp-19582 [hull=0.030, icsd=1, PRIMARY]; V8ZnO24 P-1 (2) mp-1199959 [hull=0.245, icsd=1, PRIMARY]
- papers: https://doi.org/10.2320/matertrans.e-mra2007856 (Thermoelectric Properties and Phase Transition of (Zn<I><SUB>x</SUB></...)

## Os-P
- rank 3573 | 1 samples | 1 papers | 1 compositions
- compositions: OsP2 (1)
- measured range: 299-460 K (5th-95th pct of 2 curves; full span incl. outliers 299-689 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): P4Os P2_1/c (14) mp-1087509 [hull=0.000, icsd=1, PRIMARY, AMBIGUOUS]; P4Os P-1 (2) mp-1103842 [hull=0.000, icsd=1]
- papers: https://doi.org/10.1021/ic501733z (Crystal Growth and Characterization of the Narrow-Band-Gap Semiconduct...)

## Os-P-Pr
- rank 3574 | 1 samples | 1 papers | 1 compositions
- compositions: PrOs4P12 (1)
- measured range: 13-301 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Pr(P3Os)4 Im-3 (204) mp-1188990 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1143/jpsjs.80sa.sa025 (Thermal Properties of Filled Skutterudite PrOs4P12)

## Os-Pr-Sb
- rank 3575 | 1 samples | 1 papers | 1 compositions
- compositions: PrOs4Sb12 (1)
- measured range: 11-283 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Pr(Sb3Os)4 Im-3 (204) mp-4251 [hull=0.000, icsd=15, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.72.014519 (Transport properties of the heavy-fermion superconductorPrOs4Sb12)

## Os-Sb
- rank 3576 | 1 samples | 1 papers | 1 compositions
- compositions: OsSb2 (1)
- measured range: 303-497 K (5th-95th pct of 2 curves; full span incl. outliers 303-698 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sb2Os Pnnm (58) mp-2695 [hull=0.000, icsd=6, PRIMARY]
- papers: https://doi.org/10.1021/ic501733z (Crystal Growth and Characterization of the Narrow-Band-Gap Semiconduct...)

## Os-Si
- rank 3577 | 1 samples | 1 papers | 1 compositions
- compositions: OsSi2 (1)
- measured range: 287-1105 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Si2Os Cmce (64) mp-17123 [hull=0.000, icsd=4, PRIMARY]; Si3Os2 Pbcn (60) mp-16608 [hull=0.000, icsd=3, PRIMARY]; SiOs P2_13 (198) mp-2488 [hull=0.012, icsd=3, PRIMARY]; Si3Os I4/mmm (139) mp-978508 [hull=0.600, PRIMARY]; Si2Os C2/m (12) mp-1072645 [hull=0.031, icsd=1]
- papers: https://doi.org/10.1016/0022-0248(83)90424-4 (Osmium disilicide: Preparation, crystal growth, and physical propertie...)

## Os-Zn
- rank 3578 | 1 samples | 1 papers | 1 compositions
- compositions: YbOs2Zn20 (1)
- dopant candidates (<5% at.): Yb (1)
- measured range: 12-298 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U(Zn10Os)2 Fd-3m (227) mp-1202410 [hull=0.000, icsd=1, PRIMARY]; Zn3Os I4/mmm (139) mp-971960 [hull=0.119, PRIMARY]; ZnOs P-6m2 (187) mp-1187910 [hull=0.210, PRIMARY]; ZnOs3 P6_3/mmc (194) mp-1187960 [hull=0.399, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.86.115110 (Thermoelectric power of the YbT2Zn20(T=Fe, Ru, Os, Ir, Rh, and Co) hea...)

## P-Rb-Se-Sn
- rank 3579 | 1 samples | 1 papers | 1 compositions
- compositions: Rb4Sn5P4Se20 (1)
- measured range: 301-522 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1002/anie.201104050 (Rb4Sn5P4Se20: A Semimetallic Selenophosphate)

## P-S-Ti-Tl
- rank 3580 | 1 samples | 1 papers | 1 compositions
- compositions: TlTiPS5 (1)
- measured range: 80-299 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti2Tl3P5S18 Cc (9) mp-1217446 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1021/cm050412c (Exploring Thallium Compounds as Thermoelectric Materials:  Seventeen N...)

## P-Sn
- rank 3581 | 1 samples | 1 papers | 1 compositions
- compositions: Sn3P4 (1)
- measured range: 10-292 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SnP Fm-3m (225) mp-475 [hull=0.033, icsd=2, PRIMARY]; SnP3 R-3m (166) mp-7541 [hull=0.005, icsd=2, PRIMARY]; Sn4P3 R-3m (166) mp-27410 [hull=0.000, icsd=1, PRIMARY]; Sn16P15 P1 (1) mp-673683 [hull=0.298, PRIMARY]; Sn3P P6_3/mmc (194) mp-1187044 [hull=0.285, PRIMARY]
- papers: https://doi.org/10.1021/cm702655g (Highly Disordered Crystal Structure and Thermoelectric Properties of S...)

## P-Th
- rank 3582 | 1 samples | 1 papers | 1 compositions
- compositions: Th3P4 (1)
- measured range: 105-1114 K (5th-95th pct of 2 curves; full span incl. outliers 105-1165 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ThP Fm-3m (225) mp-931 [hull=0.000, icsd=6, PRIMARY]; Th3P4 I-43d (220) mp-1347 [hull=0.000, icsd=3, PRIMARY]; Th2P11 P2_1/c (14) mp-29281 [hull=0.021, icsd=1, PRIMARY]; ThP2 Pnma (62) mp-1103645 [hull=0.032, icsd=1, PRIMARY]; ThP7 P2_12_12_1 (19) mp-28410 [hull=0.038, icsd=1, PRIMARY]
- papers: https://doi.org/10.1149/1.2423585 (Some X-Ray and Thermoelectric Studies on Cubic Th[sub 3]X[sub 4] Compo...)

## P-Yb-Zn
- rank 3583 | 1 samples | 1 papers | 1 compositions
- compositions: YbZn2P2 (1)
- measured range: 312-996 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(ZnP)2 P-3m1 (164) mp-9582 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1088/0022-3727/44/15/155406 (High Seebeck coefficientAMXP2(A= Ca and Yb;M,X= Zn, Cu and Mn) Zintl p...)

## Pb-Rb-Sb-Se
- rank 3584 | 1 samples | 1 papers | 1 compositions
- compositions: Rb1.45Pb3.1Sb7.45Se15 (1)
- measured range: 180-294 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1021/cm0003323 (Modular Construction of A1+xM4-2xM‘7+xSe15(A = K, Rb; M = Pb, Sn; M‘ =...)

## Pb-S-Sn
- rank 3585 | 1 samples | 1 papers | 1 compositions
- compositions: Pb0.9Sn0.1S (1)
- measured range: 297-924 K (5th-95th pct of 5 curves)
- [ref 1] TEDesignLab / ICSD: SnPbS3 Pnma (62) mp-1188095 [hull=0.008, icsd=2, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: SnPbS2 Pmc2_1 (26) mp-1218951 [hull=0.031, icsd=1, PRIMARY]; SnPb4S5 I4/mmm (139) mp-1218954 [hull=0.000, PRIMARY]; SnPbS2 R-3m (166) mp-1218952 [hull=0.042]; SnPbS2 P1 (1) mp-1218961 [hull=0.060]
- papers: https://doi.org/10.1021/jacs.0c00306 (Band Sharpening and Band Alignment Enable High Quality Factor to Enhan...)

## Pb-S-Sn-Ti
- rank 3586 | 1 samples | 1 papers | 1 compositions
- compositions: TiS2(PbSnS3)0.5 (1)
- measured range: 346-647 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1002/adsu.201800046 (Recent Advances of Layered Thermoelectric Materials)

## Pb-S-Sr
- rank 3587 | 1 samples | 1 papers | 1 compositions
- compositions: PbS0.9Cl0.1SrS (1)
- dopant candidates (<5% at.): Cl (1)
- measured range: 302-731 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr3PbS4 Pmmm (47) mp-1218560 [hull=0.000, PRIMARY]; SrPb3S4 R-3m (166) mp-1218031 [hull=0.013, PRIMARY]; SrPbS2 R-3m (166) mp-1218019 [hull=0.010, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2015.10.052 (High performance thermoelectrics from earth-abundant materials: Enhanc...)

## Pb-Sb
- rank 3588 | 1 samples | 1 papers | 1 compositions
- compositions: AgPb10Sb12 (1)
- dopant candidates (<5% at.): Ag (1)
- measured range: 300-480 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sb3Pb P6_3/mmc (194) mp-973199 [hull=0.186, PRIMARY]; SbPb Fm-3m (225) mp-1206982 [hull=0.070, PRIMARY]; SbPb3 P-6m2 (187) mp-1219498 [hull=0.087, PRIMARY, AMBIGUOUS]; SbPb4 R-3m (166) mp-1219484 [hull=0.054, PRIMARY]; SbPb Cmmm (65) mp-1219460 [hull=0.133]
- papers: https://doi.org/10.1016/j.jallcom.2008.02.040 (Preparation and thermoelectric properties of AgPbmSbTe2+m alloys)

## Pb-Se-Sr
- rank 3589 | 1 samples | 1 papers | 1 compositions
- compositions: Pb0.88Sr0.12Se (1)
- measured range: 295-901 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1039/c3ee43438a (Tuning bands of PbSe for better thermoelectric efficiency)

## Pb-Se-Tl
- rank 3590 | 1 samples | 1 papers | 1 compositions
- compositions: Tl4PbSe3 (1)
- measured range: 357-447 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Tl4PbSe3 P4/ncc (130) mp-1195087 [hull=0.000, icsd=2, PRIMARY]; Tl4PbSe3 I4/mcm (140) mp-1189804 [hull=0.015, icsd=1]
- papers: https://doi.org/10.1134/s0020168511070156 (Phase equilibria in the Tl2Se-PbSe system and growth and properties of...)

## Pb-Sn
- rank 3591 | 1 samples | 1 papers | 1 compositions
- compositions: Ag0.9Pb7.2Sn10.8Sb0.6Te (1)
- dopant candidates (<5% at.): Te (1), Ag (1), Sb (1)
- measured range: 345-675 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sn3Pb P6_3/mmc (194) mp-1187117 [hull=0.057, PRIMARY]; SnPb P-6m2 (187) mp-972692 [hull=0.050, PRIMARY]; SnPb3 P6_3/mmc (194) mp-1187118 [hull=0.066, PRIMARY]; Sn3Pb Pmmm (47) mp-1219045 [hull=0.069]
- papers: https://doi.org/10.1002/adma.200502770 (Nanostructuring and High Thermoelectric Efficiency in p-Type Ag(Pb1 –y...)

## Pd-Pu-Sn
- rank 3592 | 1 samples | 1 papers | 1 compositions
- compositions: PuPd2Sn (1)
- measured range: 10-297 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Pu2SnPd2 P4/mbm (127) mp-640044 [hull=0.738, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.77.014431 (Extensive studies of antiferromagneticPuPd2Sn)

## Pd-Rh
- rank 3593 | 1 samples | 1 papers | 1 compositions
- compositions: Pd92.9Rh7.1 (1)
- measured range: 13-99 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Pd3Rh I4/mmm (139) mp-1186442 [hull=0.071, PRIMARY]; PdRh R-3m (166) mp-1219925 [hull=0.081, PRIMARY]
- papers: https://doi.org/10.1007/bf00655330 (Comments upon ?the thermoelectric power of someThCe alloys? and an alt...)

## Pd-S
- rank 3594 | 1 samples | 1 papers | 1 compositions
- compositions: PdS (1)
- measured range: 304-602 K (5th-95th pct of 3 curves)
- [ref 1] TEDesignLab / ICSD: PdS P4_2/m (84) mp-20250 [hull=0.000, icsd=4, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: PdS2 Pbca (61) mp-13682 [hull=0.000, icsd=4, PRIMARY]; Pd4S P-42_1c (114) mp-7819 [hull=0.000, icsd=3, PRIMARY]; Pd16S7 I-43m (217) mp-393 [hull=0.000, icsd=3, PRIMARY]; Pd3S Fm-3m (225) mp-1186431 [hull=0.334, PRIMARY]; PdS3 I4/mmm (139) mp-1186463 [hull=0.380, PRIMARY]
- papers: https://doi.org/10.1109/ict.2003.1287526 (Thermoelectric figure of merit of M-sulphides (M=Fe, Co, Ni, Pd) thin ...)

## Pd-Sb-Sc
- rank 3595 | 1 samples | 1 papers | 1 compositions
- compositions: ScPdSb (1)
- measured range: 90-397 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1088/0953-8984/15/4/304 (Thermoelectrical properties of the compounds ScMVIIISb and YMVIIISb (M...)

## Pd-Sb-Tb
- rank 3596 | 1 samples | 1 papers | 1 compositions
- compositions: TbPdSb (1)
- measured range: 11-299 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TbSbPd P6_3/mmc (194) mp-1019315 [hull=0.000, icsd=1, PRIMARY]; TbSb2Pd P4/nmm (129) mp-1095192 [hull=0.000, icsd=1, PRIMARY]; Tb5SbPd2 I4/mcm (140) mp-1208413 [hull=0.007, PRIMARY]; Tb2Sb3Pd P4/mmm (123) mp-1207366 [hull=3.387, PRIMARY]; TbSbPd C2/m (12) mp-1217541 [hull=0.185]
- papers: https://doi.org/10.1016/j.jallcom.2017.06.014 (Magnetic and transport properties of half-Heuslers, RPdSb (R = Gd and Tb))

## Pd-Si-Y
- rank 3597 | 1 samples | 1 papers | 1 compositions
- compositions: Y2PdSi3 (1)
- measured range: 12-294 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y(SiPd)2 I4/mmm (139) mp-1069988 [hull=0.000, icsd=3, PRIMARY]; Y3Si3Pd2 Cmcm (63) mp-14244 [hull=0.005, icsd=1, PRIMARY]; YSiPd2 Pnma (62) mp-28024 [hull=0.000, icsd=1, PRIMARY]; Y2Si3Pd P6_3/mmc (194) mp-1207726 [hull=0.000, PRIMARY]; Y2SiPd Immm (71) mp-1097423 [hull=2.669, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.62.425 (Magnetic, thermal, and transport properties of single crystals of anti...)

## Pd-Sn-Th
- rank 3598 | 1 samples | 1 papers | 1 compositions
- compositions: ThPdSn (1)
- measured range: 18-297 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ThSnPd2 Fm-3m (225) mp-865677 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevmaterials.2.074401 (Magnetic and electronic properties of NpPdSn)

## Pd-Sn-Yb
- rank 3599 | 1 samples | 1 papers | 1 compositions
- compositions: Yb2Pd3Sn5 (1)
- measured range: 19-499 K (5th-95th pct of 2 curves; full span incl. outliers 19-544 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbSnPd Pnma (62) mp-3204 [hull=0.000, icsd=3, PRIMARY]; YbSnPd2 Fm-3m (225) mp-4053 [hull=0.000, icsd=3, PRIMARY]; Yb3(SnPd)2 Pbcm (57) mp-1202245 [hull=0.000, icsd=2, PRIMARY]; YbSn2Pd Cmcm (63) mp-16641 [hull=0.000, icsd=1, PRIMARY]; Yb2SnPd2 P4/mbm (127) mp-1205601 [hull=0.018, PRIMARY]
- papers: https://doi.org/10.1143/jpsj.72.1745 (Magnetic and Thermoelectric Properties of a Heterogeneous Mixed-Valenc...)

## Pd-U
- rank 3600 | 1 samples | 1 papers | 1 compositions
- compositions: UPd3 (1)
- measured range: 12-297 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UPd3 P6_3/mmc (194) mp-30841 [hull=0.000, icsd=5, PRIMARY]; UPd4 R-3m (166) mp-1216788 [hull=0.372, PRIMARY]
- papers: https://doi.org/10.1143/jpsj.59.3687 (Some Characteristics of the Thermoelectric Power in Uranium Intermetal...)
