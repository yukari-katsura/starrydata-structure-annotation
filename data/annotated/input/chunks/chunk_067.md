# Host systems -- chunk 067 of 73

Ranks 3301-3350 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 99.43%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Ge-Ho-Sn
- rank 3301 | 1 samples | 1 papers | 1 compositions
- compositions: HoSnGe (1)
- measured range: 11-193 K (5th-95th pct of 2 curves; full span incl. outliers 11-297 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HoSnGe Cmcm (63) mp-1077485 [hull=0.000, icsd=1, PRIMARY]
- papers: A comparative study of HoSn1.1Ge0.9 and DySn1.1Ge0.9 compounds using magnetic, magneto-thermal and magneto-transport measurements

## Ge-In-Sb
- rank 3302 | 1 samples | 1 papers | 1 compositions
- compositions: GeIn0.6Sb5.4 (1)
- measured range: 303-712 K (5th-95th pct of 3 curves)
- papers: Enhanced thermoelectric performance of In-substituted GeSb6Te10 with homologous structure

## Ge-Ir-Y
- rank 3303 | 1 samples | 1 papers | 1 compositions
- compositions: Y3Ir4Ge13 (1)
- measured range: 10-286 K (5th-95th pct of 2 curves; full span incl. outliers 10-355 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y5(Ge5Ir2)2 P4/mbm (127) mp-1196414 [hull=0.016, icsd=2, PRIMARY]; YGeIr Pnma (62) mp-1102373 [hull=0.000, icsd=2, PRIMARY]; Y3Ge13Ir4 Pm-3n (223) mp-1200412 [hull=0.024, icsd=1, PRIMARY]
- papers: Thermal and transport properties of the cubic semimetal Y3Ir4Ge13: on the metallic border of thermoelectric merit

## Ge-K-Li
- rank 3304 | 1 samples | 1 papers | 1 compositions
- compositions: K32Li10.8Ge171.3 (1)
- measured range: 11-297 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): K3LiGe4 Pnma (62) mp-1211905 [hull=0.000, PRIMARY]
- papers: Synthesis and Thermoelectric Properties of the Clathrate-I Phase K8Li x Ge44−x/4□2−3x/4

## Ge-K-Sr
- rank 3305 | 1 samples | 1 papers | 1 compositions
- compositions: K8Sr16Ge96 (1)
- papers: Synthesis and thermoelectric properties of semiconducting germanium-based type-II clathrate (K,Sr) 24 (Ga,Ge) 136

## Ge-La-Mn
- rank 3306 | 1 samples | 1 papers | 1 compositions
- compositions: La2MnGe6 (1)
- measured range: 11-280 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(MnGe)2 I4/mmm (139) mp-22760 [hull=0.000, icsd=5, PRIMARY]; LaMnGe P4/nmm (129) mp-20195 [hull=0.128, icsd=3, PRIMARY]
- papers: Electric transport in R2MGe6 ternary compounds (R=La, Ce, Gd, Tb, Dy, Ho; M=Mn, Ni, Cu)

## Ge-La-Pt-Yb
- rank 3307 | 1 samples | 1 papers | 1 compositions
- compositions: (Yb0.7La0.3)PtGe (1)
- measured range: 13-279 K (5th-95th pct of 1 curves)
- papers: Electrical and magnetic properties of YbPdGe and YbPtGe

## Ge-Li-O-P
- rank 3308 | 1 samples | 1 papers | 1 compositions
- compositions: Li1.5Al0.5Ge1.5(PO4)3 (1)
- dopant candidates (<5% at.): Al (1)
- measured range: 148-498 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li10Ge(PO6)2 P1 (1) mp-632815 [hull=0.070, PRIMARY]; LiGe2(PO4)3 R-3 (148) mp-1021510 [hull=0.002, PRIMARY]; Li10Ge(PO6)2 P4_2mc (105) mp-696130 [hull=0.111]
- papers: Good Solid‐State Electrolytes Have Low, Glass‐Like Thermal Conductivity

## Ge-Li-Sb-Te
- rank 3309 | 1 samples | 1 papers | 1 compositions
- compositions: (GeTe)11(LiSbTe2)2 (1)
- measured range: 293-722 K (5th-95th pct of 4 curves; full span incl. outliers 293-773 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li2GeSb2Te5 R3m (160) mp-1222750 [hull=0.574, PRIMARY]; LiGe3SbTe5 R3m (160) mp-1222357 [hull=0.275, PRIMARY]; LiGeSbTe3 P3m1 (156) mp-1222311 [hull=0.451, PRIMARY]
- papers: The Solid Solution Series (GeTe)x(LiSbTe2)2(1 ≤x≤ 11) and the Thermoelectric Properties of (GeTe)11(LiSbTe2)2

## Ge-Li-Zn
- rank 3310 | 1 samples | 1 papers | 1 compositions
- compositions: Li2ZnGe (1)
- measured range: 60-1191 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li2ZnGe F-43m (216) mp-12411 [hull=0.008, icsd=1, PRIMARY]; Li13Zn11Ge12 P-6m2 (187) mp-1223160 [hull=0.176, PRIMARY]; Li2ZnGe3 P3m1 (156) mp-1222627 [hull=0.023, PRIMARY]
- papers: Ternary germanide Li2ZnGe: A new candidate for high temperature thermoelectrics

## Ge-Lu-Ru
- rank 3311 | 1 samples | 1 papers | 1 compositions
- compositions: Lu3Ru4Ge13 (1)
- measured range: 13-802 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Lu3Ge13Ru4 Pm-3n (223) mp-1203006 [hull=0.033, icsd=1, PRIMARY]; Lu3Ge3Ru2 Cmcm (63) mp-1188368 [hull=0.000, icsd=1, PRIMARY]; LuGe2Ru Pbam (55) mp-1195981 [hull=0.000, icsd=1, PRIMARY]; LuGeRu Pnma (62) mp-22051 [hull=0.000, icsd=1, PRIMARY]; Lu4Ge8Ru Pmm2 (25) mp-1222645 [hull=0.069, PRIMARY]
- papers: Thermoelectric properties of rare earth–ruthenium–germanium compounds

## Ge-Mn
- rank 3312 | 1 samples | 1 papers | 1 compositions
- compositions: MnGe (1)
- measured range: 10-300 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn5Ge3 P6_3/mcm (193) mp-617291 [hull=0.012, icsd=12, PRIMARY]; MnGe P2_13 (198) mp-1078464 [hull=0.000, icsd=6, PRIMARY]; Mn11Ge8 Pnma (62) mp-654223 [hull=0.017, icsd=5, PRIMARY]; Mn3Ge P6_3/mmc (194) mp-1078873 [hull=0.074, icsd=3, PRIMARY]; Mn5Ge2 Ibam (72) mp-632686 [hull=0.086, icsd=3, PRIMARY]
- papers: Topological Nernst effect in a three-dimensional skyrmion-lattice phase

## Ge-Mn-Si
- rank 3313 | 1 samples | 1 papers | 1 compositions
- compositions: MnSi0.90Ge0.10 (1)
- measured range: 14-295 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn10(SiGe)3 P-62m (189) mp-1222206 [hull=0.052, PRIMARY]; Mn5Si2Ge Amm2 (38) mp-1221552 [hull=0.051, PRIMARY]
- papers: Substitutional effect on the transport properties of MnSi

## Ge-Mo
- rank 3314 | 1 samples | 1 papers | 1 compositions
- compositions: MoGe1.769 (1)
- measured range: 299-973 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ge2Mo I4/mmm (139) mp-10201 [hull=0.022, icsd=3, PRIMARY]; GeMo3 Pm-3n (223) mp-494 [hull=0.000, icsd=3, PRIMARY]; Ge3Mo5 I4/mcm (140) mp-17094 [hull=0.038, icsd=2, PRIMARY]; Ge3Mo I4/mmm (139) mp-1184671 [hull=0.551, PRIMARY]; Ge2Mo Pnma (62) mp-13688 [hull=0.000, icsd=1]
- papers: Tuning valence electron concentration in the Mo13Ge23-Ru2Ge3 pseudobinary system for enhancement of the thermoelectric properties

## Ge-Na
- rank 3315 | 1 samples | 1 papers | 1 compositions
- compositions: Na4Ge13 (1)
- measured range: 13-300 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NaGe P2_1/c (14) mp-29657 [hull=0.000, icsd=3, PRIMARY]; Na12SnGe8 P4_12_12 (92) mp-645945 [hull=0.000, icsd=1, PRIMARY]; Na3Ge Fm-3m (225) mp-1185667 [hull=0.071, PRIMARY]
- papers: Zintl Ions within Framework Channels: The Complex Structure and Low-Temperature Transport Properties of Na4Ge13

## Ge-Ni-Tb
- rank 3316 | 1 samples | 1 papers | 1 compositions
- compositions: Tb2NiGe6 (1)
- measured range: 11-280 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TbNiGe2 Cmcm (63) mp-4288 [hull=0.000, icsd=5, PRIMARY]; Tb(NiGe)2 I4/mmm (139) mp-3329 [hull=0.000, icsd=4, PRIMARY]; Tb3NiGe2 Pnma (62) mp-1191273 [hull=0.000, icsd=1, PRIMARY]; TbNiGe Pnma (62) mp-21424 [hull=0.000, icsd=1, PRIMARY]; TbNiGe3 Cmmm (65) mp-1087235 [hull=0.000, icsd=1, PRIMARY]
- papers: Electric transport in R2MGe6 ternary compounds (R=La, Ce, Gd, Tb, Dy, Ho; M=Mn, Ni, Cu)

## Ge-O
- rank 3317 | 1 samples | 1 papers | 1 compositions
- compositions: GeO2 (1)
- measured range: 295-673 K (5th-95th pct of 1 curves)
- [ref 1] TEDesignLab / ICSD: GeO2 P3_121 (152) mp-733 [hull=0.000, icsd=36, PRIMARY]; GeO2 P4_2/mnm (136) mp-470 [hull=0.004, icsd=23]; GeO2 P3_221 (154) mp-223 [hull=0.000, icsd=6]; GeO2 Pnnm (58) mp-1072104 [hull=0.006, icsd=6]; GeO2 Pa-3 (205) mp-2633 [hull=0.225, icsd=2]
- [ref 2] MP, ranked by ICSD evidence: Ge7HO20 P-43m (215) mp-1193690 [hull=0.569, icsd=1, PRIMARY]; Ge7O16 P-43m (215) mp-1191730 [hull=0.236, icsd=1, PRIMARY]; Ge7O23 P-43m (215) mp-1181291 [hull=0.648, icsd=1, PRIMARY]; Ge5O11 Cm (8) mp-1224586 [hull=0.313, PRIMARY]; Ge3O I4/mmm (139) mp-1184665 [hull=0.861, PRIMARY]
- papers: Thermal conductivity of rutile germanium dioxide

## Ge-O-Sb-Ta-Te
- rank 3318 | 1 samples | 1 papers | 1 compositions
- compositions: (Ge2Sb2Te3)80.8(Ta2O5)19.2 (1)
- measured range: 305-571 K (5th-95th pct of 1 curves)
- papers: Stress reduction and performance improvement of phase change memory cell by using Ge2Sb2Te5–TaOx composite films

## Ge-O-Sb-Te
- rank 3319 | 1 samples | 1 papers | 1 compositions
- compositions: (Ge2Sb2Te3)83.9(Ta2O5)16.1 (1)
- dopant candidates (<5% at.): Ta (1)
- measured range: 305-570 K (5th-95th pct of 1 curves)
- papers: Stress reduction and performance improvement of phase change memory cell by using Ge2Sb2Te5–TaOx composite films

## Ge-Os-Pr
- rank 3320 | 1 samples | 1 papers | 1 compositions
- compositions: Pr3Os4Ge13 (1)
- measured range: 11-295 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Pr3Ge13Os4 Pm-3n (223) mp-1197909 [hull=0.030, icsd=1, PRIMARY]
- papers: Promising thermoelectric properties of heavy-fermion semimetal Pr3Os4Ge13

## Ge-P-Zn
- rank 3321 | 1 samples | 1 papers | 1 compositions
- compositions: ZnGeP2 (1)
- measured range: 321-431 K (5th-95th pct of 1 curves)
- [ref 1] TEDesignLab / ICSD: ZnGeP2 I-42d (122) mp-4524 [hull=0.000, icsd=13, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: ZnGeP2 P-4m2 (115) mp-1215424 [hull=0.031]
- papers: Some Electrical Properties of ZnGeP2Crystals

## Ge-Pb-Se
- rank 3322 | 1 samples | 1 papers | 1 compositions
- compositions: Ge0.89Ag0.01Pb0.1Se (1)
- dopant candidates (<5% at.): Ag (1)
- measured range: 302-701 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ge3PbSe4 Pm (6) mp-1224389 [hull=0.029, PRIMARY]
- papers: Thermoelectric properties of GeSe

## Ge-Pd
- rank 3323 | 1 samples | 1 papers | 1 compositions
- compositions: Pd0.95Ge0.05 (1)
- measured range: 84-300 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GePd2 P-62m (189) mp-423 [hull=0.000, icsd=4, PRIMARY]; GePd Pnma (62) mp-1424 [hull=0.000, icsd=2, PRIMARY]; Ge9Pd25 P-3 (147) mp-15843 [hull=0.006, icsd=2, PRIMARY]; GePd5 C2/m (12) mp-1103057 [hull=0.000, icsd=1, PRIMARY]; Ge3Pd Pm-3m (221) mp-1184682 [hull=0.301, PRIMARY]
- papers: Thermoelectric power of hydrogenated palladium and some of its dilute alloys, between 80 and 300 K

## Ge-Pd-Y
- rank 3324 | 1 samples | 1 papers | 1 compositions
- compositions: YPdGe (1)
- measured range: 10-299 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YGePd2 Pnma (62) mp-1207627 [hull=0.000, icsd=1, PRIMARY]; YGePd Imm2 (44) mp-1190225 [hull=0.000, icsd=1, PRIMARY]; Y2Ge6Pd Amm2 (38) mp-1205800 [hull=0.042, PRIMARY]; YGe2Pd Immm (71) mp-1207628 [hull=0.000, PRIMARY]; Y2GePd Immm (71) mp-1093907 [hull=2.560, PRIMARY]
- papers: Electrical and magnetic properties of YbPdGe and YbPtGe

## Ge-Pd-Yb
- rank 3325 | 1 samples | 1 papers | 1 compositions
- compositions: YbPdGe (1)
- measured range: 10-290 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(GePd)2 I4/mmm (139) mp-3296 [hull=0.000, icsd=3, PRIMARY]; Yb2Ge6Pd Cmce (64) mp-10789 [hull=0.000, icsd=1, PRIMARY]; YbGe2Pd Immm (71) mp-1189703 [hull=0.000, icsd=1, PRIMARY]; Yb3(GePd)4 Immm (71) mp-10415 [hull=0.019, icsd=1, PRIMARY]; Yb2Ge3Pd Pmm2 (25) mp-1215854 [hull=0.000, PRIMARY]
- papers: Electrical and magnetic properties of YbPdGe and YbPtGe

## Ge-Pr-Rh
- rank 3326 | 1 samples | 1 papers | 1 compositions
- compositions: Pr2Rh3Ge (1)
- measured range: 11-298 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Pr(GeRh)2 I4/mmm (139) mp-2896 [hull=0.000, icsd=6, PRIMARY]; PrGe3Rh I4mm (107) mp-13072 [hull=0.000, icsd=2, PRIMARY]; Pr(Ge2Rh3)2 P-6m2 (187) mp-1102817 [hull=0.000, icsd=1, PRIMARY]; Pr2Ge5Rh3 Ibam (72) mp-975634 [hull=0.000, icsd=1, PRIMARY]; Pr2GeRh3 R-3m (166) mp-1077830 [hull=0.000, icsd=1, PRIMARY]
- papers: A new ternary magnetically ordered heavy fermion compound Pr<sub>2</sub>Rh<sub>3</sub>Ge: magnetic, electronic and thermodynamic properties

## Ge-Pt-Th
- rank 3327 | 1 samples | 1 papers | 1 compositions
- compositions: ThPt4Ge12 (1)
- measured range: 20-290 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Th(GePt)2 P4/nmm (129) mp-1078793 [hull=0.000, icsd=1, PRIMARY]; Th(Ge3Pt)4 Im-3 (204) mp-1208358 [hull=0.014, icsd=1, PRIMARY]; Th(GePt)2 I4/mmm (139) mp-21889 [hull=0.102, icsd=1]
- papers: Superconducting and normal state properties of the systemsLa1−xMxPt4Ge12(M = Ce,Th)

## Ge-Pt-Y
- rank 3328 | 1 samples | 1 papers | 1 compositions
- compositions: YPtGe (1)
- measured range: 14-297 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y3Ge13Pt4 Cc (9) mp-1200879 [hull=0.061, icsd=1, PRIMARY, AMBIGUOUS]; Y(GePt)2 Pmn2_1 (31) mp-1084838 [hull=0.011, icsd=1, PRIMARY]; YGePt Pnma (62) mp-1095607 [hull=0.000, icsd=1, PRIMARY]; YGe2Pt Immm (71) mp-1105716 [hull=0.000, icsd=1, PRIMARY]; Y2(GePt3)3 C2/c (15) mp-1207911 [hull=0.000, PRIMARY]
- papers: Electrical and magnetic properties of YbPdGe and YbPtGe

## Ge-Rh
- rank 3329 | 1 samples | 1 papers | 1 compositions
- compositions: Rh17Ge22 (1)
- measured range: 338-983 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GeRh Pnma (62) mp-22239 [hull=0.000, icsd=2, PRIMARY]; GeRh2 Pnma (62) mp-22585 [hull=0.000, icsd=2, PRIMARY]; Ge3Rh5 Pbam (55) mp-624221 [hull=0.011, icsd=2, PRIMARY]; Ge4Rh P3_121 (152) mp-1104286 [hull=0.029, icsd=1, PRIMARY]; Ge22Rh17 I-42d (122) mp-1203373 [hull=0.000, icsd=1, PRIMARY]
- papers: Crystal structure and thermoelectric properties of the incommensurate chimney–ladder compound RhGeγ (γ ∼ 1.293)

## Ge-Rh-Y
- rank 3330 | 1 samples | 1 papers | 1 compositions
- compositions: Y2Rh3Ge (1)
- measured range: 19-298 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y(GeRh)2 I4/mmm (139) mp-4889 [hull=0.000, icsd=2, PRIMARY]; Y(GeRh2)2 Pnma (62) mp-1192507 [hull=0.000, icsd=1, PRIMARY]; Y2Ge5Rh3 C2/c (15) mp-1106022 [hull=0.000, icsd=1, PRIMARY]; Y2GeRh3 R-3m (166) mp-10214 [hull=0.000, icsd=1, PRIMARY]; Y3Ge13Rh4 Pm-3n (223) mp-1195758 [hull=0.022, icsd=1, PRIMARY]
- papers: A new ternary magnetically ordered heavy fermion compound Pr<sub>2</sub>Rh<sub>3</sub>Ge: magnetic, electronic and thermodynamic properties

## Ge-Ru-Sm
- rank 3331 | 1 samples | 1 papers | 1 compositions
- compositions: Sm3Ru4Ge13 (1)
- measured range: 10-302 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SmGeRu Pnma (62) mp-20655 [hull=0.012, icsd=3, PRIMARY]; Sm(GeRu)2 I4/mmm (139) mp-21224 [hull=0.000, icsd=2, PRIMARY]; Sm3(GeRu)2 Pbcm (57) mp-1194691 [hull=0.000, icsd=2, PRIMARY]; Sm3Ge13Ru4 Pm-3n (223) mp-1200023 [hull=0.034, icsd=2, PRIMARY]; Sm2Ge2Ru C2/m (12) mp-22044 [hull=0.000, icsd=1, PRIMARY]
- papers: Field-insensitive heavy fermion features and phase transition in the caged-structure quasi-skutterudite Sm3 Ru4 Ge13

## Ge-Ru-Yb
- rank 3332 | 1 samples | 1 papers | 1 compositions
- compositions: YbRu2Ge2 (1)
- measured range: 10-16 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(GeRu)2 I4/mmm (139) mp-21366 [hull=0.000, icsd=1, PRIMARY]; Yb2Ge4Ru3 C2/c (15) mp-642651 [hull=0.000, icsd=1, PRIMARY]; Yb3Ge13Ru4 Pm-3n (223) mp-1202771 [hull=0.040, icsd=1, PRIMARY]
- papers: Divergence of the quadrupole-strain susceptibility of the electronic nematic system YbRu2Ge2

## Ge-S
- rank 3333 | 1 samples | 1 papers | 1 compositions
- compositions: GeS (1)
- measured range: 303-1001 K (5th-95th pct of 2 curves)
- [ref 1] TEDesignLab / ICSD: GeS Pnma (62) mp-2242 [hull=0.000, icsd=6, PRIMARY]; GeS2 I-42d (122) mp-7582 [hull=0.021, icsd=3, PRIMARY]; GeS Cmcm (63) mp-12910 [hull=0.045, icsd=1]; GeS2 (43)
- [ref 2] MP, ranked by ICSD evidence: Ge2S5 P-1 (2) mp-1193697 [hull=0.265, icsd=1, PRIMARY]; GeS2 Pc (7) mp-1197287 [hull=0.011, icsd=1]; GeS2 I4_1/acd (142) mp-622213 [hull=0.019, icsd=1]; GeS2 P4_2/nmc (137) mp-1071032 [hull=0.096, icsd=1]
- papers: High-efficient thermoelectric materials: The case of orthorhombic IV-VI compounds

## Ge-Sb-Yb-Zn
- rank 3334 | 1 samples | 1 papers | 1 compositions
- compositions: YbZn2Sb1.60Ge0.40 (1)
- measured range: 299-701 K (5th-95th pct of 1 curves)
- papers: Zintl phase compounds AM2Sb2 (A=Ca, Sr, Ba, Eu, Yb; M=Zn, Cd) and their substitution variants: a class of potential thermoelectric materials

## Ge-Sr
- rank 3335 | 1 samples | 1 papers | 1 compositions
- compositions: SrGe5.6 (1)
- measured range: 17-296 K (5th-95th pct of 2 curves; full span incl. outliers 17-501 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrGe2 Pnma (62) mp-1244 [hull=0.010, icsd=4, PRIMARY]; SrGe Cmcm (63) mp-2147 [hull=0.000, icsd=3, PRIMARY]; SrGe3 I4/mmm (139) mp-1105296 [hull=0.073, icsd=2, PRIMARY]; Sr2Ge Pnma (62) mp-2576 [hull=0.000, icsd=2, PRIMARY]; Sr5Ge3 I4/mcm (140) mp-17757 [hull=0.003, icsd=1, PRIMARY]
- papers: High-Pressure Synthesis and Transport Properties of a New Binary Germanide, SrGe6-δ(δ ≅ 0.5), with a Cagelike Structure

## Ge-V
- rank 3336 | 1 samples | 1 papers | 1 compositions
- compositions: V17Ge31 (1)
- measured range: 308-915 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): V3Ge Pm-3n (223) mp-1078697 [hull=0.000, icsd=17, PRIMARY]; V5Ge3 I4/mcm (140) mp-1105285 [hull=0.000, icsd=2, PRIMARY, AMBIGUOUS]; V11Ge8 Pnma (62) mp-1199253 [hull=0.000, icsd=2, PRIMARY]; V17Ge31 P-4n2 (118) mp-680383 [hull=0.000, icsd=1, PRIMARY]; VGe2 P6_222 (180) mp-1084800 [hull=0.021, icsd=1, PRIMARY]
- papers: Crystal Structure and Thermoelectric Properties of the Incommensurate Chimney–Ladder Compound VGeγ (γ ~1.82)

## H-La-Mg-O
- rank 3337 | 1 samples | 1 papers | 1 compositions
- compositions: Mg2SiLa5(OH)15 (1)
- dopant candidates (<5% at.): Si (1)
- measured range: 308-866 K (5th-95th pct of 4 curves)
- papers: Fabrication and thermoelectric properties of Mg2Si-based composites using reduction reaction with additives

## H-Li-O-P
- rank 3338 | 1 samples | 1 papers | 1 compositions
- compositions: LiH2PO4 (1)
- measured range: 149-399 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiPH2O3 Pna2_1 (33) mp-23931 [hull=0.000, icsd=3, PRIMARY]; LiP(HO2)2 Pna2_1 (33) mp-24610 [hull=0.000, icsd=3, PRIMARY]; Li2PH3O4 P2_1/c (14) mp-1198271 [hull=0.009, icsd=2, PRIMARY]; LiP(HO)2 C2/m (12) mp-642650 [hull=0.015, icsd=2, PRIMARY]; Li4P5HO15 P-1 (2) mp-765567 [hull=0.002, icsd=1, PRIMARY]
- papers: Nuclear magnetic resonance study of the superprotonic conduction in LiH<sub>2</sub>PO<sub>4</sub>

## H-Na-O-Ti
- rank 3339 | 1 samples | 1 papers | 1 compositions
- compositions: NaHTi3O7 (1)
- measured range: 472-758 K (5th-95th pct of 2 curves; full span incl. outliers 472-1045 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Na2TiH4O5 P-1 (2) mp-1191567 [hull=0.160, icsd=1, PRIMARY]; NaTi2HO5 P1 (1) mp-1079509 [hull=0.124, icsd=1, PRIMARY]; Na2TiH4O5 Immm (71) mp-1102810 [hull=0.226, icsd=1]
- papers: Large Seebeck Coefficients of Protonated Titanate Nanotubes for High-Temperature Thermoelectric Conversion

## H-O-P-V
- rank 3340 | 1 samples | 1 papers | 1 compositions
- compositions: VPO5(H2O)2 (1)
- measured range: 201-413 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): V2NiP2(H4O7)2 I4/m (87) mp-25608 [hull=0.008, icsd=2, PRIMARY]; V2CoP2(H4O7)2 I4/m (87) mp-25478 [hull=0.009, icsd=2, PRIMARY]; VPH5O7 P2_1/c (14) mp-1195952 [hull=0.007, icsd=2, PRIMARY]; KV2P2H4O13 P-1 (2) mp-643841 [hull=0.114, icsd=1, PRIMARY]; V2P2H2O11 Pmmn (59) mp-1198775 [hull=0.055, icsd=1, PRIMARY]
- papers: Thermomechanical and thermoelectrical properties of vanadyl phosphate dihydrate

## H-O-Rb-Se
- rank 3341 | 1 samples | 1 papers | 1 compositions
- compositions: Rb3H(SeO4)2 (1)
- measured range: 369-446 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): RbH3(SeO3)2 P2_12_12_1 (19) mp-24022 [hull=0.000, icsd=2, PRIMARY]; Rb2ZnH12(SeO7)2 P2_1/c (14) mp-24182 [hull=0.000, icsd=2, PRIMARY]; RbHSeO4 P1 (1) mp-695829 [hull=0.000, icsd=2, PRIMARY]; Rb2CoH12(SeO7)2 P2_1/c (14) mp-633474 [hull=0.020, icsd=1, PRIMARY]; Rb2MgH12(SeO7)2 P2_1/c (14) mp-780006 [hull=0.000, icsd=1, PRIMARY]
- papers: Evidence for proton conduction below superionic transition on Rb3H(SeO4)2

## H-P-Se
- rank 3342 | 1 samples | 1 papers | 1 compositions
- compositions: (PDPPSe)(FeCl3)0.012 (1)
- dopant candidates (<5% at.): Cl (1), Fe (1)
- measured range: 298-377 K (5th-95th pct of 1 curves)
- papers: Multi-heterojunctioned plastics with high thermoelectric figure of merit

## H-Pb-Sb-Te
- rank 3343 | 1 samples | 1 papers | 1 compositions
- compositions: Pb0.8TSb0.2Te1.1 (1)
- measured range: 331-623 K (5th-95th pct of 4 curves)
- papers: Largely enhanced thermoelectric properties of the binary-phased PbTe–Sb2Te3 nanocomposites

## H-S-Ti
- rank 3344 | 1 samples | 1 papers | 1 compositions
- compositions: TiS2(C6H16N)0.025 (1)
- dopant candidates (<5% at.): C (1), N (1)
- measured range: 299-413 K (5th-95th pct of 5 curves)
- papers: Ultrahigh thermoelectric power factor in flexible hybrid inorganic-organic superlattice

## H-U-Zr
- rank 3345 | 1 samples | 1 papers | 1 compositions
- compositions: U23.87(ZrH1.6)76.13 (1)
- measured range: 292-766 K (5th-95th pct of 1 curves)
- papers: Thermal properties of hydride fuel 45% U–ZrH1.6

## He-Te
- rank 3346 | 1 samples | 1 papers | 1 compositions
- compositions: HeTe5 (1)
- measured range: 34-307 K (5th-95th pct of 1 curves)
- papers: Enhancement of the power factor of the transition metal pentatelluride HfTe5 by rare-earth doping

## Hf-Ir
- rank 3347 | 1 samples | 1 papers | 1 compositions
- compositions: Ir3Hf (1)
- measured range: 298-1096 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HfIr3 Pm-3m (221) mp-2126 [hull=0.000, icsd=4, PRIMARY]; HfIr P2_1/m (11) mp-1007786 [hull=0.000, icsd=1, PRIMARY]; Hf5Ir3 P6_3/mcm (193) mp-1189573 [hull=0.000, icsd=1, PRIMARY]; HfIr Pmma (51) mp-1018055 [hull=0.020, icsd=1]; HfIr Pm-3m (221) mp-1002122 [hull=0.059, icsd=1]
- papers: Thermophysical Properties of L1<SUB><B>2</B></SUB> Intermetallic Compounds of Iridium

## Hf-N
- rank 3348 | 1 samples | 1 papers | 1 compositions
- compositions: HfN0.92 (1)
- measured range: 292-1099 K (5th-95th pct of 1 curves)
- [ref 1] TEDesignLab / ICSD: Hf3N4 I-43d (220) mp-11660 [hull=0.069, icsd=2, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: HfN Fm-3m (225) mp-2828 [hull=0.000, icsd=20, PRIMARY]; HfN2 Pa-3 (205) mp-1102429 [hull=0.413, icsd=1, PRIMARY]; Hf2N P4_2/mnm (136) mp-864647 [hull=0.000, PRIMARY]; Hf3N2 R-3m (166) mp-1224388 [hull=0.000, PRIMARY]; Hf4N3 I4/mmm (139) mp-32994 [hull=0.025, PRIMARY]
- papers: Mechanical, Thermal, and Oxidation Properties of Refractory Hafnium and zirconium Compounds

## Hf-Ni-Pb-Sn-Zr
- rank 3349 | 1 samples | 1 papers | 1 compositions
- compositions: Zr0.5Hf0.3Ni0.5Pb0.2Sn0.99Sb0.01 (1)
- dopant candidates (<5% at.): Sb (1)
- measured range: 298-1005 K (5th-95th pct of 5 curves)
- papers: Thermoelectric properties of ZrNiSn-based half-Heusler compounds by solid state reaction method

## Hf-Ni-Pd-Sn-Ti
- rank 3350 | 1 samples | 1 papers | 1 compositions
- compositions: Ti0.5Hf0.5Ni0.5Pd0.5Sn0.99Sb0.01 (1)
- dopant candidates (<5% at.): Sb (1)
- measured range: 300-946 K (5th-95th pct of 6 curves)
- papers: High temperature thermoelectric properties of TiNiSn-based half-Heusler compounds
