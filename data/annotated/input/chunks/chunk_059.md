# Host systems -- chunk 059 of 73

Ranks 2901-2950 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 98.66%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Ce-Ga-H-Rh
- rank 2901 | 1 samples | 1 papers | 1 compositions
- compositions: CeRhGaH1.8 (1)
- sample form: Bulk (1)
- measured range: 15-298 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1021/cm0705338 (Hydrogenation of the Ce(Rh1-xIrx)Ga System:  Occurrence of Antiferroma...)

## Ce-Ga-Ir
- rank 2902 | 1 samples | 1 papers | 1 compositions
- compositions: Ce2Ir3Ga9 (1)
- sample form: Polycrystal (1)
- measured range: 11-308 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce2(Ga3Ir)3 Cmcm (63) mp-1213877 [hull=0.000, PRIMARY]; CeGaIr Pnma (62) mp-1213791 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(98)00408-3 (Transport and magnetic properties of new ternary Ce2T3X9-compounds (T=...)

## Ce-Ga-Pt
- rank 2903 | 1 samples | 1 papers | 1 compositions
- compositions: CePtGa (1)
- measured range: 13-292 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeGaPt Pnma (62) mp-1103487 [hull=0.000, icsd=1, PRIMARY]; CeGa3Pt I-4m2 (119) mp-1226576 [hull=0.016, PRIMARY]; CeGaPt4 P-6m2 (187) mp-1226944 [hull=0.095, PRIMARY]
- papers: https://doi.org/10.1016/0921-4526(94)91903-8 (Thermoelectric power of Ce-based Kondo alloys)

## Ce-Ga-Ru
- rank 2904 | 1 samples | 1 papers | 1 compositions
- compositions: Ce2Ru3Ga9 (1)
- sample form: Polycrystal (1)
- measured range: 11-350 K (5th-95th pct of 2 curves; full span incl. outliers 11-390 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce2(Ga3Ru)3 Cmcm (63) mp-1214327 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2018.09.131 (Revisiting the physical properties of Ce2Ru3Ga9: Intermediate valence,...)

## Ce-Ga-Si
- rank 2905 | 1 samples | 1 papers | 1 compositions
- compositions: CeSiGa (1)
- sample form: Bulk (1)
- measured range: 240-380 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeGaSi Imma (74) mp-1226572 [hull=0.000, PRIMARY]; CeGaSi I4_1md (109) mp-1206504 [hull=0.017]
- papers: https://doi.org/10.1016/j.jallcom.2005.07.053 (Thermoelectric properties of the solid solutions based on ThSi2-type C...)

## Ce-Ge
- rank 2906 | 1 samples | 1 papers | 1 compositions
- compositions: CeGe2 (1)
- measured range: 10-17 K (5th-95th pct of 2 curves; full span incl. outliers 10-298 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeGe2 I4_1/amd (141) mp-21055 [hull=0.000, icsd=5, PRIMARY]; Ce5Ge4 Pnma (62) mp-1200696 [hull=0.000, icsd=3, PRIMARY]; CeGe Pnma (62) mp-1079395 [hull=0.000, icsd=3, PRIMARY]; Ce3Ge P4_2/n (86) mp-1200337 [hull=0.032, icsd=1, PRIMARY]; CeGe5 Immm (71) mp-984703 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/bf00683635 (Thermpower of Ce x Y1?x InCu2 and CeInCu y Ag2?y)

## Ce-Ge-H-Ru
- rank 2907 | 1 samples | 1 papers | 1 compositions
- compositions: CeRuGeH (1)
- sample form: Bulk (1)
- measured range: 12-301 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1088/0953-8984/22/4/046003 (A study on the antiferromagnetic behavior of the hydride CeRuGeH adopt...)

## Ce-Ge-Mn
- rank 2908 | 1 samples | 1 papers | 1 compositions
- compositions: Ce2MnGe6 (1)
- sample form: Bulk (1)
- measured range: 16-283 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(MnGe)2 I4/mmm (139) mp-21089 [hull=0.000, icsd=7, PRIMARY]; CeMnGe P4/nmm (129) mp-21399 [hull=0.049, icsd=3, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2007.04.286 (Electric transport in R2MGe6 ternary compounds (R=La, Ce, Gd, Tb, Dy, ...)

## Ce-Ge-Sb
- rank 2909 | 1 samples | 1 papers | 1 compositions
- compositions: Ce4Sb1.5Ge1.5 (1)
- measured range: 11-384 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce5GeSb2 Pnma (62) mp-1213986 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.physb.2014.03.023 (Ferromagnetism and transport properties of the Kondo system Ce4Sb1.5Ge1.5)

## Ce-H-In-Pd
- rank 2910 | 1 samples | 1 papers | 1 compositions
- compositions: CePdInH (1)
- sample form: Bulk (1)
- measured range: 12-280 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1088/0953-8984/18/5/026 (The Doniach diagram and hydrogenation of the ternary compounds CePdIn ...)

## Ce-H-Pd-Sn
- rank 2911 | 1 samples | 1 papers | 1 compositions
- compositions: CePdSnH (1)
- sample form: Bulk (1)
- measured range: 14-275 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1088/0953-8984/18/5/026 (The Doniach diagram and hydrogenation of the ternary compounds CePdIn ...)

## Ce-H-Rh-Sb
- rank 2912 | 1 samples | 1 papers | 1 compositions
- compositions: CeRhSbH0.2 (1)
- sample form: Bulk (1)
- measured range: 11-297 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1021/cm062168a (Inducing Magnetism in the Kondo Semiconductor CeRhSb through Hydrogena...)

## Ce-Ho-O-Sb
- rank 2913 | 1 samples | 1 papers | 1 compositions
- compositions: Ce1.5Ho1.5SbO3 (1)
- measured range: 11-401 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1021/ic302292w (Synthesis, Crystal Structure, and Electronic Properties of the Tetrago...)

## Ce-Ir-Sn
- rank 2914 | 1 samples | 1 papers | 1 compositions
- compositions: CeIrSn (1)
- measured range: 13-279 K (5th-95th pct of 2 curves; full span incl. outliers 13-488 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(SnIr)2 P4/nmm (129) mp-21358 [hull=0.081, icsd=2, PRIMARY]; Ce3Sn13Ir4 Pm-3n (223) mp-1200449 [hull=0.000, icsd=2, PRIMARY]; CeSnIr P-62m (189) mp-20835 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(00)01176-2 (Large thermoelectric power in several metallic compounds of cerium and...)

## Ce-La-Ni-Sn
- rank 2915 | 1 samples | 1 papers | 1 compositions
- compositions: Ce0.5La0.5NiSn (1)
- measured range: 11-198 K (5th-95th pct of 2 curves; full span incl. outliers 11-258 K)
- papers: https://doi.org/10.1016/0921-4526(90)90211-c (Gap formation in CeNiSn at low temperatures)

## Ce-La-Ru
- rank 2916 | 1 samples | 1 papers | 1 compositions
- compositions: (Ce0.75La0.25)Ru2 (1)
- sample form: Polycrystal (1)
- measured range: 11-288 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaCeRu4 F-43m (216) mp-1222913 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/0921-4526(94)00430-4 (Transport properties of (Ce1−xRx)Ru2 (R  La, Nd))

## Ce-Li
- rank 2917 | 1 samples | 1 papers | 1 compositions
- compositions: Ce7Li3 (1)
- sample form: Bulk (1)
- measured range: 12-277 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li3Ce Fm-3m (225) mp-1185231 [hull=0.344, PRIMARY]; LiCe3 Pm-3m (221) mp-1185343 [hull=0.270, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(00)01129-4 (Electrical resistivity and thermoelectric power study of the heavy-fer...)

## Ce-Mn-Pr-Si
- rank 2918 | 1 samples | 1 papers | 1 compositions
- compositions: Ce0.6Pr0.4Mn2Si2 (1)
- measured range: 19-370 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/s0925-8388(02)00858-7 (Thermoelectric power in compounds with an intermediate valence of Ce: ...)

## Ce-Mn-Si
- rank 2919 | 1 samples | 1 papers | 1 compositions
- compositions: CeMn2Si2 (1)
- measured range: 44-351 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(MnSi)2 I4/mmm (139) mp-2965 [hull=0.000, icsd=8, PRIMARY]; CeMnSi2 Cmcm (63) mp-5901 [hull=0.000, icsd=3, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(02)00858-7 (Thermoelectric power in compounds with an intermediate valence of Ce: ...)

## Ce-Nb-S
- rank 2920 | 1 samples | 1 papers | 1 compositions
- compositions: (Ce2S2)2NbS2 (1)
- curator composition details (from the paper): We assigned the [NbS2] slab to subsystem 1 and the [Ln2S2] block to subsystem 2 (1)
- measured range: 13-299 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1007/s11664-012-2443-5 (Crystal Structure and Thermoelectric Properties of Misfit-Layered Sulf...)

## Ce-Nd-O-Zr
- rank 2921 | 1 samples | 1 papers | 1 compositions
- compositions: (Nd0.5Ce0.5)2Zr2O7.5 (1)
- sample form: Bulk (1)
- measured range: 298-973 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeNd4Zr3O14 R-3m (166) mp-1226623 [hull=0.022, PRIMARY]
- papers: https://doi.org/10.1007/s10853-017-1212-5 (Ultralow thermal conductivity of cerium-doped Nd2Zr2O7 over a wide dop...)

## Ce-Ni-Rh-Sn
- rank 2922 | 1 samples | 1 papers | 1 compositions
- compositions: CeRh0.75Ni0.25Sn (1)
- sample form: Bulk (1)
- measured range: 10-283 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/s0921-4526(02)02235-4 (Thermoelectric and magnetic properties of CeRh1$minus;xMxSn (M=Co, Ni,...)

## Ce-Ni-Sb
- rank 2923 | 1 samples | 1 papers | 1 compositions
- compositions: CeNiSb2 (1)
- sample form: Bulk (1)
- measured range: 12-287 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(NiSb)2 P4/nmm (129) mp-1078924 [hull=0.000, icsd=4, PRIMARY]; CeNiSb2 P4/nmm (129) mp-22539 [hull=0.000, icsd=3, PRIMARY]; CeNiSb P-6m2 (187) mp-1226516 [hull=0.000, PRIMARY]; Ce(NiSb)2 I4/mmm (139) mp-1226918 [hull=0.164]
- papers: https://doi.org/10.1016/0304-8853(94)01418-3 (Kondo lattice behaviour in CeTSb2 compounds (T  Ni, Cu and Ag))

## Ce-O-P-Ru
- rank 2924 | 1 samples | 1 papers | 1 compositions
- compositions: CeRuPO (1)
- measured range: 11-15 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CePRuO P4/nmm (129) mp-21372 [hull=0.000, icsd=1, PRIMARY]; Ce2P2RuO P4/mmm (123) mp-1213899 [hull=1.707, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.91.035130 (Avoided ferromagnetic quantum critical point in CeRuPO)

## Ce-O-Sm-Zr
- rank 2925 | 1 samples | 1 papers | 1 compositions
- compositions: Sm2(Zr0.7Ce0.3)2O7 (1)
- measured range: 292-1672 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1002/adem.200700153 (Preparation and Thermophysical Properties of Sm2(Ce0.3Zr0.7)2O7 Ceramic)

## Ce-O-U
- rank 2926 | 1 samples | 1 papers | 1 compositions
- compositions: U0.80Ce0.20O2 (1)
- measured range: 360-1359 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce2U2O9 I4/mmm (139) mp-1226883 [hull=0.232, PRIMARY]; Ce2U3O10 C2/m (12) mp-773114 [hull=0.000, PRIMARY]; Ce2UO6 P-3m1 (164) mp-1226776 [hull=0.000, PRIMARY, AMBIGUOUS]; Ce3UO8 R-3m (166) mp-1226924 [hull=0.000, PRIMARY]; Ce4UO10 R-3m (166) mp-1226869 [hull=0.000, PRIMARY, AMBIGUOUS]
- papers: https://doi.org/10.1016/j.jnucmat.2008.05.003 (Applicability of CeO2 as a surrogate for PuO2 in a MOX fuel development)

## Ce-P-Si
- rank 2927 | 1 samples | 1 papers | 1 compositions
- compositions: Ce2P3Si (1)
- measured range: 13-295 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeSiP3 Pna2_1 (33) mp-651900 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(99)00483-1 (Thermoelectric properties of the intermediate valent cerium intermetal...)

## Ce-Pd-Sc
- rank 2928 | 1 samples | 1 papers | 1 compositions
- compositions: Ce0.75Sc0.25Pd3 (1)
- measured range: 84-353 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeScPd6 P4/mmm (123) mp-1226501 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1007/s11664-011-1788-5 (Thermoelectric Properties of Ce1−x Sc x Pd3)

## Ce-Rh-Ru-Sn
- rank 2929 | 1 samples | 1 papers | 1 compositions
- compositions: CeRh0.75Ru0.25Sn (1)
- sample form: Bulk (1)
- measured range: 17-283 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/s0921-4526(02)02235-4 (Thermoelectric and magnetic properties of CeRh1$minus;xMxSn (M=Co, Ni,...)

## Ce-Ru-Sb-Sn
- rank 2930 | 1 samples | 1 papers | 1 compositions
- compositions: Ce3Ru4Sn11.05Sb1.95 (1)
- sample form: Polycrystal (1)
- measured range: 12-295 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1103/physrevb.94.235151 (Doping effect on the electronic structure and thermodynamic properties...)

## Ce-S-Sr
- rank 2931 | 1 samples | 1 papers | 1 compositions
- compositions: Ce1.47(SrS)0.4 (1)
- measured range: 317-1116 K (5th-95th pct of 2 curves; full span incl. outliers 317-1178 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr(CeS2)2 I-42d (122) mp-33392 [hull=0.033, PRIMARY]
- papers: https://doi.org/10.1063/1.1777182 (Thermoelectric Properties of Some Cerium Sulfide Semiconductors from 4...)

## Ce-Sb-Se
- rank 2932 | 1 samples | 1 papers | 1 compositions
- compositions: CeSbSe (1)
- measured range: 10-20 K (5th-95th pct of 2 curves; full span incl. outliers 10-297 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeSbSe Pnma (62) mp-1103153 [hull=0.000, icsd=1, PRIMARY]; Ce(SbSe2)2 C2/m (12) mp-1080285 [hull=0.299, PRIMARY]; Ce2Sb2Se5 P2_1/c (14) mp-1080287 [hull=0.137, PRIMARY]; Ce2Sb2Se5 Pnma (62) mp-1080286 [hull=0.176]
- papers: https://doi.org/10.1103/physrevb.96.014421 (Possible devil's staircase in the Kondo lattice CeSbSe)

## Ce-Sb-Zn
- rank 2933 | 1 samples | 1 papers | 1 compositions
- compositions: (Zn0.7Ce0.3)4Sb3 (1)
- measured range: 301-674 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce2ZnSb4 P-4m2 (115) mp-1226796 [hull=0.000, PRIMARY]; Ce4Zn3Sb8 P-4m2 (115) mp-1226943 [hull=0.030, PRIMARY]
- papers: https://doi.org/10.1016/j.scriptamat.2019.08.037 (Dislocation-induced ultra-low lattice thermal conductivity in rare ear...)

## Ce-Se-Sn
- rank 2934 | 1 samples | 1 papers | 1 compositions
- compositions: CeSe1.8Sn0.2 (1)
- sample form: Bulk (1)
- measured range: 13-301 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce2SnSe4 Pnma (62) mp-1006368 [hull=0.077, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2014.08.130 (Low-temperature thermoelectric properties of the CeSe2−xSnx compounds)

## Ce-Si-Y
- rank 2935 | 1 samples | 1 papers | 1 compositions
- compositions: Y0.5Ce0.5Si2 (1)
- sample form: Bulk (1)
- measured range: 240-380 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(YSi)4 P2_12_12_1 (19) mp-1227796 [hull=0.029, PRIMARY]; Ce2YSi2 P4/mbm (127) mp-1207182 [hull=0.018, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2005.07.053 (Thermoelectric properties of the solid solutions based on ThSi2-type C...)

## Ce-Sn
- rank 2936 | 1 samples | 1 papers | 1 compositions
- compositions: CeSn3 (1)
- measured range: 16-274 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeSn3 Pm-3m (221) mp-1911 [hull=0.000, icsd=10, PRIMARY]; Ce5Sn3 I4/mcm (140) mp-637308 [hull=0.000, icsd=4, PRIMARY]; Ce3Sn Pm-3m (221) mp-20735 [hull=0.000, icsd=4, PRIMARY]; Ce5Sn4 Pnma (62) mp-21693 [hull=0.000, icsd=3, PRIMARY]; Ce3Sn5 Cmcm (63) mp-1189084 [hull=0.003, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(85)90291-4 (Thermoelectric power and electrical resistivity of Ce(In1-xSnx)3 and (...)

## Ce-Te-Tl
- rank 2937 | 1 samples | 1 papers | 1 compositions
- compositions: Tl9CeTe6 (1)
- sample form: Bulk (1)
- measured range: 316-551 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(Tl3Te2)3 I4/m (87) mp-1106203 [hull=0.000, icsd=1, PRIMARY]; CeTlTe2 I4/mcm (140) mp-1079792 [hull=0.160, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2015.01.025 (Thermoelectric properties of hot-pressed Tl9LnTe6 (Ln=La, Ce, Pr, Nd, ...)

## Ce-Zn
- rank 2938 | 1 samples | 1 papers | 1 compositions
- compositions: CeZn11 (1)
- sample form: SingleCrystal (1)
- measured range: 12-298 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeZn Pm-3m (221) mp-986 [hull=0.037, icsd=5, PRIMARY]; CeZn5 P6/mmm (191) mp-394 [hull=0.011, icsd=5, PRIMARY]; CeZn11 I4_1/amd (141) mp-640370 [hull=0.004, icsd=4, PRIMARY]; CeZn2 Imma (74) mp-1385 [hull=0.000, icsd=3, PRIMARY]; Ce3Zn22 I4_1/amd (141) mp-698212 [hull=0.008, icsd=3, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.88.054410 (Anisotropic transport and magnetic properties and magnetic-field tuned...)

## Cl-Cs-Tm
- rank 2939 | 1 samples | 1 papers | 1 compositions
- compositions: CsTmCl3 (1)
- measured range: 300-1000 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cs2TmCl4 I4/mmm (139) mp-1077991 [hull=0.081, icsd=1, PRIMARY]; Cs2TmCl5 Pnma (62) mp-1213743 [hull=0.000, PRIMARY]; Cs3TmCl6 Fm-3m (225) mp-1112342 [hull=0.026, PRIMARY]; CsTm2Cl7 Pnma (62) mp-1213262 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1002/qua.26141 (A theoretical study of the structural, thermoelectric, and spin‐orbit ...)

## Cl-Cu
- rank 2940 | 1 samples | 1 papers | 1 compositions
- compositions: CuCl (1)
- measured range: 1103-1273 K (5th-95th pct of 2 curves)
- [ref 1] TEDesignLab / ICSD: CuCl F-43m (216) mp-22914 [hull=0.000, icsd=4, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: CuCl2 C2/m (12) mp-30999 [hull=0.000, icsd=2, PRIMARY]; Cu3Cl Pm-3m (221) mp-1183968 [hull=0.518, PRIMARY]; CuCl3 Cmmm (65) mp-1213141 [hull=0.061, PRIMARY]; CuCl4 I-42m (121) mp-32829 [hull=0.091, PRIMARY]; CuCl Pa-3 (205) mp-23287 [hull=0.036, icsd=2]
- papers: https://doi.org/10.1051/epjconf/20111501003 (Electrical properties of molten CuCl-Cu2Se mixtures)

## Cl-In-Li
- rank 2941 | 1 samples | 1 papers | 1 compositions
- compositions: Li3InCl6 (1)
- measured range: 148-348 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li3InCl6 C2 (5) mp-676109 [hull=0.000, PRIMARY]; Li3InCl6 Fm-3m (225) mp-1111288 [hull=0.231]
- papers: https://doi.org/10.1002/smll.202101693 (Good Solid‐State Electrolytes Have Low, Glass‐Like Thermal Conductivity)

## Cl-La-P-Zn
- rank 2942 | 1 samples | 1 papers | 1 compositions
- compositions: La3Zn4P6Cl (1)
- sample form: SingleCrystal (1)
- measured range: 10-401 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1021/acs.chemmater.6b01752 (Enclathration of X@La4 Tetrahedra in Channels of Zn–P Frameworks in La...)

## Cl-Li
- rank 2943 | 1 samples | 1 papers | 1 compositions
- compositions: LiCl (1)
- measured range: 149-499 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiCl Fm-3m (225) mp-22905 [hull=0.000, icsd=5, PRIMARY]; LiCl P6_3mc (186) mp-1185319 [hull=0.000]
- papers: https://doi.org/10.1002/smll.202101693 (Good Solid‐State Electrolytes Have Low, Glass‐Like Thermal Conductivity)

## Cl-Li-P-S
- rank 2944 | 1 samples | 1 papers | 1 compositions
- compositions: Li6PS5Cl (1)
- measured range: 148-348 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li5P(S2Cl)2 Amm2 (38) mp-1040450 [hull=0.008, PRIMARY]; Li6PS5Cl F-43m (216) mp-985592 [hull=0.080, PRIMARY]
- papers: https://doi.org/10.1002/smll.202101693 (Good Solid‐State Electrolytes Have Low, Glass‐Like Thermal Conductivity)

## Cl-Li-Y
- rank 2945 | 1 samples | 1 papers | 1 compositions
- compositions: Li3YCl6 (1)
- measured range: 149-348 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1002/smll.202101693 (Good Solid‐State Electrolytes Have Low, Glass‐Like Thermal Conductivity)

## Cl-Se-Sn
- rank 2946 | 1 samples | 1 papers | 1 compositions
- compositions: SnSe0.95(NbCl5)0.03 (1)
- dopant candidates (<5% at.): Nb (1)
- sample form: Bulk (1)
- measured range: 309-816 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1039/d0tc02959a (Investigating the thermoelectric performance of n-type SnSe: the syner...)

## Co-Cr-Fe-Ni
- rank 2947 | 1 samples | 1 papers | 1 compositions
- compositions: CoCrFeNi (1)
- sample form: Bulk (1)
- measured range: 376-1158 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CrFeCoNi Pm (6) mp-1012640 [hull=0.060, PRIMARY]; CrFeCoNi P1 (1) mp-1096923 [hull=0.132]
- papers: https://doi.org/10.1063/1.4935489 (High-entropy alloys as high-temperature thermoelectric materials)

## Co-Cr-Fe-O-Zn
- rank 2948 | 1 samples | 1 papers | 1 compositions
- compositions: Co0.5Zn0.5Cr0.4Fe1.6O4 (1)
- curator composition details (from the paper): polycrystalline (1)
- measured range: 303-394 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jmmm.2015.04.104 (Investigation of structural and temperature dependent electromagnetic ...)

## Co-Cr-Ni-Si
- rank 2949 | 1 samples | 1 papers | 1 compositions
- compositions: (Cr)18.92(W)1.13(C)1.72(Si)14.75(B)3.83(Ni)15(Co)44.64 (1)
- dopant candidates (<5% at.): B (1), C (1), W (1)
- sample form: Coating (1)
- measured range: 573-872 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1007/s11666-017-0681-z (Intermetallic Al-, Fe-, Co- and Ni-Based Thermal Barrier Coatings Prep...)

## Co-Cu-Fe-Ge-Ni
- rank 2950 | 1 samples | 1 papers | 1 compositions
- compositions: FeCoNiCuGe (1)
- papers: https://doi.org/10.1016/j.tsf.2022.139083 (Thin films made by reactive sputtering of high entropy alloy FeCoNiCuG...)
