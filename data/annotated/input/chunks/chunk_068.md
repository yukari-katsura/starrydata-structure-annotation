# Host systems -- chunk 068 of 73

Ranks 3351-3400 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 99.52%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Hf-Ni-Sn-W-Zr
- rank 3351 | 1 samples | 1 papers | 1 compositions
- compositions: (Hf0.6Zr0.4)NiSn0.99Sb0.01W0.175 (1)
- dopant candidates (<5% at.): Sb (1)
- sample form: Bulk (1)
- measured range: 309-946 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/j.mattod.2020.01.002 (Decoupled phononic-electronic transport in multi-phase n-type half-Heu...)

## Hf-Ni-Sn-Y-Zr
- rank 3352 | 1 samples | 1 papers | 1 compositions
- compositions: (Hf0.6Zr0.4)0.8Y0.2NiSn (1)
- measured range: 303-875 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1557/jmr.2011.82 (P-type doping of Hf0.6Zr0.4NiSn half-Heusler thermoelectric materials ...)

## Hf-Ni-Zr
- rank 3353 | 1 samples | 1 papers | 1 compositions
- compositions: Hf0.75Zr0.25NiSb0.01 (1)
- dopant candidates (<5% at.): Sb (1)
- curator composition details (from the paper): Hf0.75Zr0.25NiSn with 0% V and 1% Sb (white circles) (1)
- measured range: 321-1091 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1103/physrevb.83.235211 (Introduction of resonant states and enhancement of thermoelectric prop...)

## Hf-Sb
- rank 3354 | 1 samples | 1 papers | 1 compositions
- compositions: HfSb2 (1)
- measured range: 56-290 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HfSb2 Pnnm (58) mp-2180 [hull=0.000, icsd=3, PRIMARY]; Hf3Sb I-4 (82) mp-15964 [hull=0.000, icsd=2, PRIMARY]; HfSb P2_13 (198) mp-1079914 [hull=0.000, icsd=1, PRIMARY, AMBIGUOUS]; Hf5Sb3 Pnma (62) mp-17466 [hull=0.000, icsd=1, PRIMARY]; Hf2Sb3 P4/mmm (123) mp-1206519 [hull=3.408, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2017.12.014 (Constitution of the binary M-Sb systems (M = Ti, Zr, Hf) and physical ...)

## Hf-Te-Tl
- rank 3355 | 1 samples | 1 papers | 1 compositions
- compositions: Tl4HfTe4 (1)
- sample form: Bulk (1)
- measured range: 322-561 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Hf(TlTe)4 R-3 (148) mp-984696 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1039/c0jm01363c (Syntheses, crystal structures and thermoelectric properties of two new...)

## Hf-Te-Zr
- rank 3356 | 1 samples | 1 papers | 1 compositions
- compositions: (Hf0.5Zr0.5)Te5 (1)
- sample form: Bulk (1)
- measured range: 10-329 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Hf5ZrTe8 P1 (1) mp-678358 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1109/ict.2007.4569474 (Thermoelectric properties of Hf<inf>1&#x2212;x</inf>Zr<inf>x</inf>Te<i...)

## Hf-V
- rank 3357 | 1 samples | 1 papers | 1 compositions
- compositions: HfV2 (1)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HfV2 Fd-3m (227) mp-1043 [hull=0.029, icsd=34, PRIMARY]; Hf4V Fd-3m (227) mp-1212224 [hull=0.941, PRIMARY]; HfV2 Imma (74) mp-1071274 [hull=0.030, icsd=2]; HfV2 I4_1/amd (141) mp-1077017 [hull=0.029, icsd=1]
- papers: https://doi.org/10.1007/bf01304460 (Normal-state and superconducting properties of HfV2)

## Hg-O-Os
- rank 3358 | 1 samples | 1 papers | 1 compositions
- compositions: Hg2Os2O7 (1)
- measured range: 22-297 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Hg2Os2O7 Fd-3m (227) mp-22089 [hull=0.033, icsd=16, PRIMARY]; HgOsO3 Pm-3m (221) mp-1016840 [hull=0.309, PRIMARY]
- papers: https://doi.org/10.1039/b109715f (The synthesis, structure and properties of Hg2Os2O7)

## Ho-In
- rank 3359 | 1 samples | 1 papers | 1 compositions
- compositions: HoIn3 (1)
- sample form: Bulk (1)
- measured range: 11-50 K (5th-95th pct of 2 curves; full span incl. outliers 11-290 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ho2In P6_3/mmc (194) mp-20686 [hull=0.000, icsd=7, PRIMARY]; HoIn3 Pm-3m (221) mp-21431 [hull=0.000, icsd=6, PRIMARY]; Ho5In3 I4/mcm (140) mp-1189750 [hull=0.000, icsd=1, PRIMARY]; Ho3In5 Cmcm (63) mp-1188109 [hull=0.000, icsd=1, PRIMARY]; HoIn Pm-3m (221) mp-30728 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0038-1098(89)90423-7 (Thermoelectric power of the REIn3 single crystals where RE = La, Ce, P...)

## Ho-La-O-Sb
- rank 3360 | 1 samples | 1 papers | 1 compositions
- compositions: La1.5Ho1.5SbO3 (1)
- measured range: 11-394 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1021/ic302292w (Synthesis, Crystal Structure, and Electronic Properties of the Tetrago...)

## Ho-Mg-Zn
- rank 3361 | 1 samples | 1 papers | 1 compositions
- compositions: Ho8.7Mg34.6Zn56.8_IQC (1)
- measured range: 13-300 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ho13(Mg2Zn27)2 P6_3/mmc (194) mp-1213598 [hull=0.007, PRIMARY]; HoMgZn2 Fm-3m (225) mp-861981 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1080/13642819808206407 (Growth of large-grain R-Mg-Zn quasicrystals from the ternary melt (R =...)

## Ho-Mn-Si
- rank 3362 | 1 samples | 1 papers | 1 compositions
- compositions: Ho2Mn3Si5 (1)
- measured range: 23-290 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ho(MnSi)2 I4/mmm (139) mp-5796 [hull=0.000, icsd=5, PRIMARY]; HoMnSi Pnma (62) mp-20380 [hull=0.042, icsd=4, PRIMARY]; Ho4MnSi7 Amm2 (38) mp-1212286 [hull=0.106, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(01)01363-9 (Magnetism and electronic transport in R2Mn3Si5 (R=Dy, Ho and Er) compo...)

## Ho-Mo-O
- rank 3363 | 1 samples | 1 papers | 1 compositions
- compositions: Ho2Mo2O7 (1)
- measured range: 83-298 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ho2(MoO4)3 Pba2 (32) mp-1196327 [hull=0.000, icsd=1, PRIMARY]; Ho5(MoO6)2 C2/m (12) mp-1105194 [hull=0.019, icsd=1, PRIMARY]; KHo2Cu(MoO4)4 C2/c (15) mp-1203708 [hull=0.027, icsd=1, PRIMARY]; Ho4Mo4O11 Pbam (55) mp-654187 [hull=0.172, PRIMARY]; HoMoO5 P2_1/c (14) mp-1212177 [hull=0.105, PRIMARY]
- papers: https://doi.org/10.1016/0025-5408(80)90094-x (Electrical properties of Ln2Mo2O7 pyrochlores (Ln=SmYb,Y))

## Ho-O-Os
- rank 3364 | 1 samples | 1 papers | 1 compositions
- compositions: HoOs2O7 (1)
- measured range: 25-304 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1103/physrevb.93.134426 (Fragile singlet ground-state magnetism in the pyrochlore osmates<mml:m...)

## Ho-Sb
- rank 3365 | 1 samples | 1 papers | 1 compositions
- compositions: HoSb (1)
- measured range: 15-299 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ho5Sb3 P6_3/mcm (193) mp-2681 [hull=0.000, icsd=10, PRIMARY]; HoSb Fm-3m (225) mp-2050 [hull=0.000, icsd=8, PRIMARY]; HoSb2 C222 (21) mp-7925 [hull=0.543, icsd=2, PRIMARY]; Ho4Sb3 I-43d (220) mp-2124 [hull=0.025, icsd=2, PRIMARY]; Ho2Sb5 P2_1/m (11) mp-11140 [hull=0.008, icsd=1, PRIMARY]
- papers: https://doi.org/10.1038/s41598-020-69414-z (Observation of gapped state in rare-earth monopnictide HoSb)

## I-Li
- rank 3366 | 1 samples | 1 papers | 1 compositions
- compositions: LiI (1)
- measured range: 776-956 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiI Fm-3m (225) mp-22899 [hull=0.036, icsd=4, PRIMARY]
- papers: https://doi.org/10.1007/s10765-008-0545-3 (Toward Physical Modeling of Laser Welding: Thermophysics Revisited)

## I-Mn-Pd
- rank 3367 | 1 samples | 1 papers | 1 compositions
- compositions: AI70.5Pd22.5Mn7 (1)
- dopant candidates (<5% at.): A0+ (1)
- measured range: 11-266 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1007/bf02570341 (Resistivity, hall effect and thermopower in AIPdMn and AlCuFe quasicry...)

## I-S
- rank 3368 | 1 samples | 1 papers | 1 compositions
- compositions: B0.0009SI (1)
- dopant candidates (<5% at.): B (1)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): As(S8I)3 R3m (160) mp-30934 [hull=0.000, icsd=1, PRIMARY]; Sn(S4I)4 Fdd2 (43) mp-649878 [hull=0.055, icsd=1, PRIMARY]
- papers: https://doi.org/10.1109/ted.2006.878020 (Physical Model for the Resistivity and Temperature Coefficient of Resi...)

## I-Sb-Sn
- rank 3369 | 1 samples | 1 papers | 1 compositions
- compositions: Sn38Sb8I8 (1)
- sample form: Bulk (1)
- measured range: 291-525 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1063/1.2209207 (Preparation and thermoelectric properties of sintered iodine-containin...)

## In
- rank 3370 | 1 samples | 1 papers | 1 compositions
- compositions: In (1)
- measured range: 10-11 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): In I4/mmm (139) mp-1055994 [hull=0.000, icsd=21, PRIMARY, AMBIGUOUS]; In Fm-3m (225) mp-85 [hull=0.003, icsd=21]; In R-3m (166) mp-1184502 [hull=0.000]; In P6_3/mmc (194) mp-973111 [hull=0.011]; In I-43m (217) mp-1184693 [hull=0.021]
- papers: https://doi.org/10.1103/physrevb.21.1842 (Experimental study of thermoelectricity in superconducting indium)

## In-Ir
- rank 3371 | 1 samples | 1 papers | 1 compositions
- compositions: IrIn3 (1)
- sample form: Bulk (1)
- measured range: 16-347 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): In3Ir P4_2/mnm (136) mp-630976 [hull=0.000, icsd=3, PRIMARY]; In2Ir Fddd (70) mp-22812 [hull=0.000, icsd=2, PRIMARY]; In3Ir Pnma (62) mp-636498 [hull=0.003, icsd=1]
- papers: https://doi.org/10.1063/1.4793493 (Thermoelectric properties of intermetallic semiconducting RuIn3 and me...)

## In-K-Sn
- rank 3372 | 1 samples | 1 papers | 1 compositions
- compositions: K8In8Sn38 (1)
- sample form: Bulk (1)
- measured range: 106-425 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1088/0022-3727/45/45/455308 (Preparation and thermoelectric properties of sinteredn-type K8M8Sn38(M...)

## In-La-Ni
- rank 3373 | 1 samples | 1 papers | 1 compositions
- compositions: LaNiIn (1)
- sample form: Bulk (1)
- measured range: 17-305 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaIn2Ni9 P4/mbm (127) mp-1191038 [hull=0.000, icsd=3, PRIMARY]; LaIn4Ni Cmcm (63) mp-20303 [hull=0.000, icsd=2, PRIMARY]; La2InNi2 P4/mbm (127) mp-1095144 [hull=0.000, icsd=1, PRIMARY, AMBIGUOUS]; LaInNi2 Pmma (51) mp-21207 [hull=0.000, icsd=1, PRIMARY]; La11In9Ni4 Cmmm (65) mp-974045 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.7567/jjaps.26s3.549 (Magnetic and Transport Properties of New Kondo Compounds CeTIn (T=Ni, ...)

## In-La-Rh
- rank 3374 | 1 samples | 1 papers | 1 compositions
- compositions: LaRhIn (1)
- sample form: Polycrystal (1)
- measured range: 11-294 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaIn5Rh P4/mmm (123) mp-21479 [hull=0.000, icsd=2, PRIMARY]; La2InRh2 P4/mbm (127) mp-20907 [hull=0.008, icsd=1, PRIMARY]; LaIn2Rh Cmcm (63) mp-21002 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1143/jjap.42.6512 (Thermoelectric Properties of Single-Crystal CeRhSn with Valence Fluctu...)

## In-Mo-O
- rank 3375 | 1 samples | 1 papers | 1 compositions
- compositions: In4Ti1.5Mo0.5Mo14O26 (1)
- dopant candidates (<5% at.): Ti (1)
- curator composition details (from the paper): single crystal (1)
- measured range: 12-293 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): In2(MoO4)3 P2_1/c (14) mp-705134 [hull=0.000, icsd=1, PRIMARY]; In5(Mo9O14)2 P2_1/c (14) mp-1204440 [hull=0.271, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2015.03.030 (The cluster compound In4Ti1.5Mo0.5Mo14O26 containing Mo14 clusters and...)

## In-Nd
- rank 3376 | 1 samples | 1 papers | 1 compositions
- compositions: NdIn3 (1)
- sample form: Bulk (1)
- measured range: 10-50 K (5th-95th pct of 2 curves; full span incl. outliers 10-295 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NdIn3 Pm-3m (221) mp-21197 [hull=0.000, icsd=5, PRIMARY]; Nd2In P6_3/mmc (194) mp-21295 [hull=0.000, icsd=4, PRIMARY]; Nd3In Pm-3m (221) mp-21483 [hull=0.000, icsd=4, PRIMARY]; NdIn Pm-3m (221) mp-1206423 [hull=0.000, PRIMARY]; Nd3In P6_3/mmc (194) mp-1186302 [hull=0.015]
- papers: https://doi.org/10.1016/0038-1098(89)90423-7 (Thermoelectric power of the REIn3 single crystals where RE = La, Ce, P...)

## In-Nd-O-Ta
- rank 3377 | 1 samples | 1 papers | 1 compositions
- compositions: Nd2InTaO7 (1)
- sample form: pellets (1)
- measured range: 292-1072 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jeurceramsoc.2020.06.027 (Thermal and oxygen transport properties of complex pyrochlore RE2InTaO...)

## In-O-Pr-Ta
- rank 3378 | 1 samples | 1 papers | 1 compositions
- compositions: Pr2InTaO7 (1)
- sample form: pellets (1)
- measured range: 292-1071 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jeurceramsoc.2020.06.027 (Thermal and oxygen transport properties of complex pyrochlore RE2InTaO...)

## In-O-Sm-Ta
- rank 3379 | 1 samples | 1 papers | 1 compositions
- compositions: Sm2InTaO7 (1)
- sample form: pellets (1)
- measured range: 293-1072 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jeurceramsoc.2020.06.027 (Thermal and oxygen transport properties of complex pyrochlore RE2InTaO...)

## In-P
- rank 3380 | 1 samples | 1 papers | 1 compositions
- compositions: InP (1)
- measured range: 148-1158 K (5th-95th pct of 2 curves)
- [ref 1] TEDesignLab / ICSD: InP F-43m (216) mp-20351 [hull=0.000, icsd=15, PRIMARY]; InP P6_3mc (186) mp-966800 [hull=0.006, icsd=2]
- [ref 2] MP, ranked by ICSD evidence: InP3 R-3m (166) mp-20050 [hull=0.050, icsd=1, PRIMARY]; InP Fm-3m (225) mp-20457 [hull=0.237, icsd=3]
- papers: https://doi.org/10.1002/adfm.201401201 (Nanograined Half-Heusler Semiconductors as Advanced Thermoelectrics: A...)

## In-Pb-Sb
- rank 3381 | 1 samples | 1 papers | 1 compositions
- compositions: Pb0008In4Sb2.5 (1)
- curator composition details (from the paper): In4Se2.5 + M (0.8 at.%) from In (99.99%), Se (99.99%), Cu (99.99%), Pb (99.9%) and I2 (99.... (1)
- measured range: 292-723 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1039/c4ta05508j (Multiple heteroatom induced carrier engineering and hierarchical nanos...)

## In-Pd
- rank 3382 | 1 samples | 1 papers | 1 compositions
- compositions: InPd (1)
- sample form: SingleCrystal (1)
- measured range: 14-382 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): InPd3 Pm-3m (221) mp-31337 [hull=0.029, icsd=6, PRIMARY]; In3Pd5 Pbam (55) mp-22146 [hull=0.000, icsd=4, PRIMARY]; InPd Pm-3m (221) mp-21215 [hull=0.003, icsd=3, PRIMARY]; InPd2 Pnma (62) mp-22646 [hull=0.000, icsd=3, PRIMARY]; In3Pd P6_3/mmc (194) mp-1185043 [hull=0.235, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2014.07.007 (Physical properties of the InPd intermetallic catalyst)

## In-Pd-U
- rank 3383 | 1 samples | 1 papers | 1 compositions
- compositions: UPd2In (1)
- sample form: Polycrystal (1)
- measured range: 10-302 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UInPd P-62m (189) mp-1078683 [hull=0.133, icsd=2, PRIMARY]; U2InPd2 P4/mbm (127) mp-646426 [hull=0.161, icsd=1, PRIMARY]
- papers: https://doi.org/10.1143/jpsj.58.1918 (Stractural and Magnetic Phase Transitions in a New Heavy-Fermion Compo...)

## In-Pr
- rank 3384 | 1 samples | 1 papers | 1 compositions
- compositions: PrIn3 (1)
- sample form: Bulk (1)
- measured range: 10-50 K (5th-95th pct of 2 curves; full span incl. outliers 10-296 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrIn3 Pm-3m (221) mp-20903 [hull=0.000, icsd=5, PRIMARY]; Pr2In P6_3/mmc (194) mp-19854 [hull=0.010, icsd=2, PRIMARY]; Pr3In Pm-3m (221) mp-19764 [hull=0.000, icsd=2, PRIMARY]; Pr3In5 Cmcm (63) mp-1189599 [hull=0.000, icsd=1, PRIMARY]; PrIn Pm-3m (221) mp-20023 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0038-1098(89)90423-7 (Thermoelectric power of the REIn3 single crystals where RE = La, Ce, P...)

## In-Pr-Se-Tl
- rank 3385 | 1 samples | 1 papers | 1 compositions
- compositions: Tl2InPrSe4 (1)
- measured range: 322-1014 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrTl2InSe4 I-42m (121) mp-1219751 [hull=0.094, PRIMARY]
- papers: https://doi.org/10.1023/a:1021874732551 ([])

## In-Pt-U
- rank 3386 | 1 samples | 1 papers | 1 compositions
- compositions: UPt2In (1)
- measured range: 10-289 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U2InPt2 P4/mbm (127) mp-1079136 [hull=0.000, icsd=2, PRIMARY, AMBIGUOUS]; UInPt P-62m (189) mp-1078582 [hull=0.009, icsd=2, PRIMARY]; UInPt2 P6_3/mmc (194) mp-1079904 [hull=0.131, icsd=1, PRIMARY]; U2InPt2 P4_2/mnm (136) mp-1188266 [hull=0.000, icsd=2]
- papers: https://doi.org/10.1016/s0925-8388(00)01176-2 (Large thermoelectric power in several metallic compounds of cerium and...)

## In-Pt-Yb
- rank 3387 | 1 samples | 1 papers | 1 compositions
- compositions: YbPtIn (1)
- sample form: Polycrystal (1)
- measured range: 10-278 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbInPt P-62m (189) mp-1078378 [hull=0.000, icsd=2, PRIMARY]; YbIn2Pt Cmcm (63) mp-1078504 [hull=0.000, icsd=1, PRIMARY]; YbIn4Pt Cmcm (63) mp-21897 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.61.9467 (Low-temperature properties of the Yb-based heavy-fermion antiferromagn...)

## In-Rh-Th
- rank 3388 | 1 samples | 1 papers | 1 compositions
- compositions: Th2Rh2In (1)
- measured range: 10-284 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1088/0953-8984/18/19/019 (Specific heat and electronic transport properties of medium heavy-ferm...)

## In-Rh-U
- rank 3389 | 1 samples | 1 papers | 1 compositions
- compositions: U2Rh2In (1)
- measured range: 11-297 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U2In8Rh P4/mmm (123) mp-1095324 [hull=0.000, icsd=1, PRIMARY]; U2InRh2 P4/mbm (127) mp-646609 [hull=0.000, icsd=1, PRIMARY]; UInRh P-62m (189) mp-1091404 [hull=0.042, icsd=1, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/18/19/019 (Specific heat and electronic transport properties of medium heavy-ferm...)

## In-S
- rank 3390 | 1 samples | 1 papers | 1 compositions
- compositions: In2S3 (1)
- measured range: 299-774 K (5th-95th pct of 5 curves)
- [ref 1] TEDesignLab / ICSD: InS Pnnm (58) mp-19795 [hull=0.000, icsd=8, PRIMARY]; In6S7 (11) [PRIMARY]; InS P2_1/c (14) mp-630528 [hull=0.028, icsd=1]; In2S3 R-3c (167) mp-22375 [hull=0.030, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: In2S3 I4_1/amd (141) mp-22216 [hull=0.000, icsd=6, PRIMARY]; In5S4 Pa-3 (205) mp-22846 [hull=0.077, icsd=1, PRIMARY]; In11S16 P-4m2 (115) mp-1224223 [hull=0.009, PRIMARY]; In10CuAgS16 P-4m2 (115) mp-1224550 [hull=0.001, PRIMARY]; In2S3 Cc (9) mp-673633 [hull=0.026]
- papers: https://doi.org/10.1063/1.4939210 (Thermoelectric properties of β-Indium sulfide with sulphur deficiencies)

## In-Sb-Yb
- rank 3391 | 1 samples | 1 papers | 1 compositions
- compositions: Yb5In2Sb6 (1)
- sample form: Bulk (1)
- measured range: 294-875 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb5(InSb3)2 Pbam (55) mp-628593 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1039/c4dt03773a (Thermoelectric properties of the Zintl phases Yb5M2Sb6 (M = Al, Ga, In))

## In-Sc
- rank 3392 | 1 samples | 1 papers | 1 compositions
- compositions: Sc3In (1)
- measured range: 10-25 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sc3In P6_3/mmc (194) mp-19713 [hull=0.000, icsd=2, PRIMARY]; ScIn3 Pm-3m (221) mp-20539 [hull=0.000, icsd=2, PRIMARY]; Sc2In P6_3/mmc (194) mp-31348 [hull=0.000, icsd=1, PRIMARY]; ScIn P4/mmm (123) mp-1207100 [hull=0.000, PRIMARY]; ScIn2 Cmmm (65) mp-1206268 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/0378-4363(77)90197-8 (Spin fluctuations in itinerant electron ferromagnet Sc3In)

## In-Se-Si-Te
- rank 3393 | 1 samples | 1 papers | 1 compositions
- compositions: In0.9Si0.1Se0.9Te0.1 (1)
- sample form: Bulk (1)
- measured range: 299-686 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1007/s13391-021-00278-9 (Thermoelectric Properties of Te-doped In0.9Si0.1Se with Enhanced Effec...)

## In-Sm
- rank 3394 | 1 samples | 1 papers | 1 compositions
- compositions: SmIn3 (1)
- sample form: Bulk (1)
- measured range: 11-49 K (5th-95th pct of 2 curves; full span incl. outliers 11-289 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SmIn3 Pm-3m (221) mp-19977 [hull=0.000, icsd=6, PRIMARY]; Sm2In P6_3/mmc (194) mp-19816 [hull=0.000, icsd=4, PRIMARY]; Sm3In Pm-3m (221) mp-21202 [hull=0.000, icsd=3, PRIMARY]; SmIn Pm-3m (221) mp-20298 [hull=0.000, icsd=1, PRIMARY]; Sm3In P6_3/mmc (194) mp-1005752 [hull=0.014]
- papers: https://doi.org/10.1016/0038-1098(89)90423-7 (Thermoelectric power of the REIn3 single crystals where RE = La, Ce, P...)

## In-Tb
- rank 3395 | 1 samples | 1 papers | 1 compositions
- compositions: TbIn3 (1)
- sample form: SingleCrystal (1)
- measured range: 12-276 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TbIn3 Pm-3m (221) mp-20920 [hull=0.000, icsd=6, PRIMARY]; Tb2In P6_3/mmc (194) mp-20608 [hull=0.000, icsd=4, PRIMARY]; Tb3In P6_3/mmc (194) mp-1187299 [hull=0.008, PRIMARY]
- papers: https://doi.org/10.1016/0038-1098(91)90402-h (Resistivity and thermopower of monocrystalline TbIn3 and DyIn3)

## In-Tm
- rank 3396 | 1 samples | 1 papers | 1 compositions
- compositions: TmIn3 (1)
- sample form: Bulk (1)
- measured range: 12-50 K (5th-95th pct of 2 curves; full span incl. outliers 12-292 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TmIn3 Pm-3m (221) mp-21177 [hull=0.000, icsd=6, PRIMARY]; Tm2In P6_3/mmc (194) mp-21486 [hull=0.000, icsd=2, PRIMARY]; Tm5In3 P6_3/mcm (193) mp-1188632 [hull=0.021, icsd=1, PRIMARY]; Tm3In5 Pnma (62) mp-1208700 [hull=0.000, PRIMARY]; Tm3In Pm-3m (221) mp-1187699 [hull=0.014, PRIMARY, AMBIGUOUS]
- papers: https://doi.org/10.1016/0038-1098(89)90423-7 (Thermoelectric power of the REIn3 single crystals where RE = La, Ce, P...)

## Ir
- rank 3397 | 1 samples | 1 papers | 1 compositions
- compositions: Ir (1)
- measured range: 99-1401 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ir Fm-3m (225) mp-101 [hull=0.000, icsd=7, PRIMARY]; Ir Pmma (51) mp-1060567 [hull=3.870, icsd=1]
- papers: https://doi.org/10.1007/s11664-010-1409-8 (Measurement and Calculation of the Absolute Thermoelectric Power of Rh...)

## Ir-La-Sn
- rank 3398 | 1 samples | 1 papers | 1 compositions
- compositions: LaIrSn (1)
- measured range: 13-277 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La3Sn13Ir4 Pm-3n (223) mp-1197480 [hull=0.000, icsd=2, PRIMARY]; La5(Sn5Ir2)2 P4/mbm (127) mp-1198240 [hull=0.003, icsd=1, PRIMARY]; La2Sn4Ir Amm2 (38) mp-1223426 [hull=0.043, PRIMARY]; LaSnIr P-62m (189) mp-1205954 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(00)01176-2 (Large thermoelectric power in several metallic compounds of cerium and...)

## Ir-Nb
- rank 3399 | 1 samples | 1 papers | 1 compositions
- compositions: Ir3Nb (1)
- measured range: 298-1088 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NbIr P4/mmm (123) mp-1359 [hull=0.000, icsd=5, PRIMARY]; Nb3Ir Pm-3n (223) mp-1458 [hull=0.000, icsd=4, PRIMARY]; NbIr3 Pm-3m (221) mp-1339 [hull=0.000, icsd=2, PRIMARY]; Nb5Ir7 Pmm2 (25) mp-1220502 [hull=0.092, PRIMARY]; NbIr Pmma (51) mp-1095683 [hull=0.015, icsd=1]
- papers: https://doi.org/10.1595/147106708x361321 (Thermophysical Properties of L1<SUB><B>2</B></SUB> Intermetallic Compo...)

## Ir-Nd-O
- rank 3400 | 1 samples | 1 papers | 1 compositions
- compositions: Nd2Ir2O7 (1)
- measured range: 13-317 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd3IrO7 Cmcm (63) mp-9559 [hull=0.000, icsd=2, PRIMARY]; Nd2Ir2O7 Fd-3m (227) mp-1190299 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1143/jpsj.76.043706 (Metal–Insulator Transition in Pyrochlore IridatesLn2Ir2O7(Ln= Nd, Sm, ...)
