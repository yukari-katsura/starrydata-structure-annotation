# Host systems -- chunk 065 of 73

Ranks 3201-3250 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 99.23%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Eu-Ga-P
- rank 3201 | 1 samples | 1 papers | 1 compositions
- compositions: Eu3Ga2P4 (1)
- measured range: 294-791 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Eu3(GaP2)2 C2/c (15) mp-1189104 [hull=0.000, icsd=1, PRIMARY]; Eu3GaP3 Cmce (64) mp-1194348 [hull=0.000, icsd=1, PRIMARY]; Eu(GaP)2 P2/m (10) mp-1226022 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1021/ic302400q (Phase Characterization, Thermal Stability, High-Temperature Transport ...)

## Eu-Gd-S-Sm
- rank 3202 | 1 samples | 1 papers | 1 compositions
- compositions: SmEuGdS4 (1)
- sample form: Bulk (1)
- measured range: 302-934 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.jallcom.2009.04.076 (Synthesis of multinary rare-earth sulfides PrGdS3, NdGdS3, and SmEuGdS...)

## Eu-Ge-Pd
- rank 3203 | 1 samples | 1 papers | 1 compositions
- compositions: Eu3Pd20Ge6 (1)
- measured range: 12-293 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): EuGe3Pd I4mm (107) mp-1068422 [hull=0.000, icsd=3, PRIMARY]; EuGePd P2_1/c (14) mp-20615 [hull=0.000, icsd=1, PRIMARY]; EuGePd2 Pnma (62) mp-1188312 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1143/jpsj.71.1222 (Thermoelectric Properties of Valence-Fluctuating Eu Compound with a Cl...)

## Eu-In-O-Ta
- rank 3204 | 1 samples | 1 papers | 1 compositions
- compositions: Eu2InTaO7 (1)
- sample form: pellets (1)
- measured range: 293-1071 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jeurceramsoc.2020.06.027 (Thermal and oxygen transport properties of complex pyrochlore RE2InTaO...)

## Eu-In-P
- rank 3205 | 1 samples | 1 papers | 1 compositions
- compositions: Eu3In2P4 (1)
- measured range: 296-773 K (5th-95th pct of 3 curves; full span incl. outliers 296-842 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Eu3(InP2)2 Pnnm (58) mp-1188263 [hull=0.000, icsd=1, PRIMARY]; Eu3InP3 Pnma (62) mp-1193614 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/ic302400q (Phase Characterization, Thermal Stability, High-Temperature Transport ...)

## Eu-Ir-O
- rank 3206 | 1 samples | 1 papers | 1 compositions
- compositions: Eu2Ir2O7 (1)
- measured range: 10-314 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Eu2Ir2O7 Fd-3m (227) mp-641683 [hull=0.000, icsd=3, PRIMARY]; Eu3IrO7 Cmcm (63) mp-17981 [hull=0.000, icsd=1, PRIMARY]; EuIrO3 Pm-3m (221) mp-1184445 [hull=0.329, PRIMARY]
- papers: https://doi.org/10.1143/jpsj.76.043706 (Metal–Insulator Transition in Pyrochlore IridatesLn2Ir2O7(Ln= Nd, Sm, ...)

## Eu-Ir-Si
- rank 3207 | 1 samples | 1 papers | 1 compositions
- compositions: EuIr2Si2 (1)
- sample form: SingleCrystal (1)
- measured range: 11-294 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Eu(SiIr)2 I4/mmm (139) mp-21849 [hull=0.000, icsd=4, PRIMARY]; EuSi3Ir I4mm (107) mp-1069707 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.101.235106 (Valence effect on the thermopower of Eu systems)

## Eu-La-S
- rank 3208 | 1 samples | 1 papers | 1 compositions
- compositions: La2.2Eu0.8S4 (1)
- measured range: 676-1074 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2EuS4 I-42d (122) mp-677272 [hull=0.000, PRIMARY]; LaEuS2 R-3m (166) mp-1222958 [hull=0.031, PRIMARY]
- papers: https://doi.org/10.1063/1.344267 (Thermal conductivity of La3−xRxS4where R=Sm, Eu, and Yb)

## Eu-Ni-P
- rank 3209 | 1 samples | 1 papers | 1 compositions
- compositions: EuNi2P2 (1)
- sample form: SingleCrystal (1)
- measured range: 10-293 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Eu(NiP)2 I4/mmm (139) mp-3758 [hull=0.000, icsd=2, PRIMARY]; Eu(Ni5P3)2 Cmce (64) mp-21672 [hull=0.007, icsd=1, PRIMARY]; Eu2Ni12P7 P-6 (174) mp-1191284 [hull=0.021, icsd=1, PRIMARY]; Eu2Ni12P5 P2_1/m (11) mp-1213550 [hull=0.000, PRIMARY]; Eu2Ni7P4 Pmn2_1 (31) mp-1213320 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.101.235106 (Valence effect on the thermopower of Eu systems)

## Eu-O-Ta
- rank 3210 | 1 samples | 1 papers | 1 compositions
- compositions: EuTa2O6 (1)
- sample form: Powder (1)
- measured range: 10-396 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): EuTaO4 P2/c (13) mp-5957 [hull=0.000, icsd=2, PRIMARY, AMBIGUOUS]; EuTa2O6 P4/mmm (123) mp-20092 [hull=0.015, icsd=2, PRIMARY]; Eu2Ta2O7 Cmcm (63) mp-1191288 [hull=0.000, icsd=1, PRIMARY]; Eu3TaO6 Fm-3m (225) mp-21406 [hull=0.047, icsd=1, PRIMARY]; Eu5Ta4O15 P-3m1 (164) mp-1192440 [hull=0.019, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.4893011 (Structure and physical properties of EuTa2O6 tungsten bronze polymorph)

## Eu-O-Zr
- rank 3211 | 1 samples | 1 papers | 1 compositions
- compositions: Eu2Zr2O7 (1)
- measured range: 293-1072 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): EuZrO3 Pnma (62) mp-1106293 [hull=0.000, icsd=4, PRIMARY]; Eu2Zr2O7 Fd-3m (227) mp-685944 [hull=0.000, icsd=1, PRIMARY]; Eu2ZrO4 I4/mmm (139) mp-1206153 [hull=0.072, PRIMARY]; EuZr4O9 Imm2 (44) mp-755810 [hull=0.060, PRIMARY]; EuZrO3 Pm-3m (221) mp-771055 [hull=0.000]
- papers: https://doi.org/10.1016/j.jeurceramsoc.2020.06.027 (Thermal and oxygen transport properties of complex pyrochlore RE2InTaO...)

## Eu-S
- rank 3212 | 1 samples | 1 papers | 1 compositions
- compositions: EuS (1)
- measured range: 11-291 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): EuS Fm-3m (225) mp-20587 [hull=0.000, icsd=18, PRIMARY]; Eu3S4 I-43d (220) mp-1103738 [hull=0.000, icsd=9, PRIMARY]; Eu2S3 Pnma (62) mp-1106110 [hull=0.099, icsd=1, PRIMARY]; Eu3S P6_3/mmc (194) mp-1184541 [hull=0.431, PRIMARY]; EuS3 I4/mmm (139) mp-1184315 [hull=0.249, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.5.4877 (Resistivity and Hall Effect of EuS in Fields up to 140 kOe)

## Eu-Sb-Se
- rank 3213 | 1 samples | 1 papers | 1 compositions
- compositions: EuSbSe3 (1)
- sample form: Bulk (1)
- measured range: 300-570 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Eu(SbSe2)2 Pnma (62) mp-1192961 [hull=0.042, icsd=3, PRIMARY]; Eu3Sb4Se9 Pnma (62) mp-1200385 [hull=0.017, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/ic501808y (Crystal Cluster Growth and Physical Properties of the EuSbSe3and EuBiS...)

## F-Ho
- rank 3214 | 1 samples | 1 papers | 1 compositions
- compositions: HoF3 (1)
- measured range: 79-294 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1007/bf00859487 (Thermal conductivity of rare earth fluoride crystals)

## F-Mn-O-Se-Sr
- rank 3215 | 1 samples | 1 papers | 1 compositions
- compositions: Sr2F2Mn2Se2O (1)
- measured range: 122-333 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.jallcom.2013.05.048 (Synthesis, structure and properties of the new layered manganese oxyse...)

## F-O-Ru-Sr
- rank 3216 | 1 samples | 1 papers | 1 compositions
- compositions: Sr2RuO3F (1)
- measured range: 21-297 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1039/c6ce02358d (Topotactic fluorination of perovskite strontium ruthenate thin films u...)

## F-O-Tl
- rank 3217 | 1 samples | 1 papers | 1 compositions
- compositions: TlOF (1)
- measured range: 20-298 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Tl16O15F17 Cm (8) mp-758418 [hull=0.000, PRIMARY]; TlOF Cm (8) mp-685515 [hull=0.012, PRIMARY]
- papers: https://doi.org/10.1016/0025-5408(70)90031-0 (Single crystal data for “TlOF” and Tl2O3)

## F-Sb-Sr-Zn
- rank 3218 | 1 samples | 1 papers | 1 compositions
- compositions: SrFZnSb (1)
- sample form: Bulk (1)
- measured range: 323-754 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/j.jallcom.2020.155497 (Thermoelectric properties and thermal expansion of quaternary layered ...)

## Fe-Ga-Ge-V
- rank 3219 | 1 samples | 1 papers | 1 compositions
- compositions: Fe2VGa0.8Ge0.2 (1)
- sample form: Bulk (1)
- measured range: 12-297 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1088/0953-8984/20/25/255233 (Effects of Ge substitution on the thermoelectric properties and pseudo...)

## Fe-Ga-Mg-Mn-Si
- rank 3220 | 1 samples | 1 papers | 1 compositions
- compositions: Mg0.65Si0.38Ga0.1Fe0.1Mn0.1Cr0.01Cu0.01Ti0.01V0.01Zn0.01Ca0.001Pb0.001 (1)
- dopant candidates (<5% at.): Cr (1), Cu (1), Ti (1), V (1), Zn (1), Ca (1), Pb (1)
- measured range: 11-282 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1063/1.1735617 (Low‐Temperature Transport Properties of Commercial Metals and Alloys. ...)

## Fe-Ge-La
- rank 3221 | 1 samples | 1 papers | 1 compositions
- compositions: LaFeGe3 (1)
- sample form: SingleCrystal (1)
- measured range: 25-291 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(FeGe)2 I4/mmm (139) mp-20527 [hull=0.008, icsd=3, PRIMARY]; LaFeGe3 I4mm (107) mp-19743 [hull=0.000, icsd=2, PRIMARY]; La15FeGe9 P6_3mc (186) mp-1201203 [hull=0.000, icsd=1, PRIMARY]; La5FeGe3 P6_3/mcm (193) mp-1211823 [hull=0.120, PRIMARY]; LaFeGe P-6m2 (187) mp-1222908 [hull=0.201, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.52.10136 (CeFeGe3: A concentrated Kondo compound with a stable valency and high ...)

## Fe-H-La-Si
- rank 3222 | 1 samples | 1 papers | 1 compositions
- compositions: La(Fe0.88Si0.12)13H1.0 (1)
- measured range: 20-354 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1063/1.1643774 (Thermal transport properties of magnetic refrigerants La(FexSi1−x)13 a...)

## Fe-H-Ni-Sb
- rank 3223 | 1 samples | 1 papers | 1 compositions
- compositions: Ba0.06Sr0.01DD0.14Yb0.01Fe2.2Ni1.8Sb12 (1)
- dopant candidates (<5% at.): Ba (1), Sr (1), Yb (1)
- measured range: 297-798 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/j.actamat.2013.03.031 (New p- and n-type skutterudites with ZT>1 and nearly identical thermal...)

## Fe-Hf-P
- rank 3224 | 1 samples | 1 papers | 1 compositions
- compositions: Hf2Fe12P7 (1)
- measured range: 10-297 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Hf4FeP P4/mcc (124) mp-1102664 [hull=0.066, icsd=1, PRIMARY]; HfFeP Pnma (62) mp-22434 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/978-94-007-4984-9_3 (Thermoelectric Properties of Correlated Electron Systems Ln 3Pt4Ge6and...)

## Fe-Hf-Sn-Ti
- rank 3225 | 1 samples | 1 papers | 1 compositions
- compositions: Hf0.25Ti0.75Fe2Sn (1)
- sample form: pellets (1)
- measured range: 299-896 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.3390/inorganics12120322 (Effects of Ti and Sn Substitutions on Magnetic and Transport Propertie...)

## Fe-La-Mo-O-Sr
- rank 3226 | 1 samples | 1 papers | 1 compositions
- compositions: Sr1.5La0.5FeMoO6 (1)
- measured range: 13-239 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr11LaFe6(MoO6)6 P1 (1) mp-735565 [hull=0.004, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.74.054423 (La-induced changes in the magnetic and electronic properties ofSr2−xLa...)

## Fe-La-O-S
- rank 3227 | 1 samples | 1 papers | 1 compositions
- compositions: La2O2Fe2OS2 (1)
- measured range: 172-307 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2Fe2S2O3 I4/mmm (139) mp-1211279 [hull=0.157, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.92.155139 (Mott-Kondo insulator behavior in the iron oxychalcogenides)

## Fe-La-O-Se
- rank 3228 | 1 samples | 1 papers | 1 compositions
- compositions: La2O2Fe2OSe2 (1)
- measured range: 151-312 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2Fe(SeO)2 C2/m (12) mp-1078132 [hull=0.000, icsd=1, PRIMARY, AMBIGUOUS]; La4FeSe6O P6_3mc (186) mp-689533 [hull=0.058, icsd=1, PRIMARY]; La2Fe(SeO)2 Pna2_1 (33) mp-1201876 [hull=0.008, icsd=1]
- papers: https://doi.org/10.1103/physrevb.92.155139 (Mott-Kondo insulator behavior in the iron oxychalcogenides)

## Fe-La-O-Zn
- rank 3229 | 1 samples | 1 papers | 1 compositions
- compositions: La0.80Sr0.20Zn0.40Fe0.60O3 (1)
- dopant candidates (<5% at.): Sr (1)
- sample form: disk (1)
- measured range: 573-873 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1039/d2nj04295a (Evaluation of La<sub><i>x</i></sub>Sr<sub>1−<i>x</i></sub>Zn<sub><i>y<...)

## Fe-Li-Ni-O
- rank 3230 | 1 samples | 1 papers | 1 compositions
- compositions: Li0.5Ni0.5Fe2O4 (1)
- curator composition details (from the paper): LiNI (1)
- measured range: 299-753 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li10Fe3Ni7O20 P2/m (10) mp-771052 [hull=0.005, PRIMARY]; Li10FeNi9O20 P-1 (2) mp-769545 [hull=0.006, PRIMARY]; Li2Fe(NiO3)2 P-1 (2) mp-762917 [hull=0.046, PRIMARY]; Li2Fe2NiO6 C2/m (12) mp-762754 [hull=0.160, PRIMARY]; Li2Fe3NiO8 P4_332 (212) mp-776112 [hull=0.024, PRIMARY]
- papers: https://doi.org/10.1179/1433075x13y.0000000117 (Thermoelectric performance of polyparaphenylene/Li0·5Ni0·5Fe2O4nanocom...)

## Fe-Mg-Mn
- rank 3231 | 1 samples | 1 papers | 1 compositions
- compositions: Mg4.10Mn0.51Fe0.28Cr0.1Si0.1Zn0.1Cu 0.07Ti0.02 (1)
- dopant candidates (<5% at.): Cr (1), Si (1), Zn (1), Cu (1), Ti (1)
- measured range: 14-114 K (5th-95th pct of 2 curves; full span incl. outliers 14-278 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg14MnFe Amm2 (38) mp-1028160 [hull=0.122, PRIMARY]; Mg6MnFe Amm2 (38) mp-1023148 [hull=0.211, PRIMARY]; Mg14MnFe P-6m2 (187) mp-1028142 [hull=0.133]
- papers: https://doi.org/10.1063/1.1735617 (Low‐Temperature Transport Properties of Commercial Metals and Alloys. ...)

## Fe-Mn-O-Sr
- rank 3232 | 1 samples | 1 papers | 1 compositions
- compositions: Sr1.6La0.4FeMnO6 (1)
- dopant candidates (<5% at.): La (1)
- curator composition details (from the paper): polycrystalline (1)
- measured range: 573-1125 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaSr7Mn2(Fe3O10)2 P1 (1) mp-1076181 [hull=0.025, PRIMARY]; BaSr7Mn2(FeO4)6 Amm2 (38) mp-1076408 [hull=0.016, PRIMARY]; Sr3MnFeO7 I4mm (107) mp-1218478 [hull=0.014, PRIMARY]; Sr5Mn(Fe2O5)2 Pmmm (47) mp-1218469 [hull=0.036, PRIMARY]; Sr6Mn3FeO14 Amm2 (38) mp-1218555 [hull=0.014, PRIMARY]
- papers: https://doi.org/10.1039/c8ta10061f (Electron doping of Sr<sub>2</sub>FeMoO<sub>6−δ</sub> as high performan...)

## Fe-Mo-O
- rank 3233 | 1 samples | 1 papers | 1 compositions
- compositions: Mo0.4Fe2.6O4 (1)
- curator composition details (from the paper): thin film (1)
- measured range: 100-180 K (5th-95th pct of 1 curves)
- [ref 1] TEDesignLab / ICSD: FeMoO4 C2/m (12) mp-624662 [hull=0.056, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Fe2(MoO4)3 P2_1/c (14) mp-705435 [hull=0.002, icsd=3, PRIMARY]; CsFe5(MoO4)7 P2_1/m (11) mp-1196710 [hull=0.013, icsd=1, PRIMARY]; Fe(MoO5)2 P-1 (2) mp-1181634 [hull=0.533, PRIMARY]; Fe2Mo4O7 Cm (8) mp-1181867 [hull=0.259, PRIMARY]; Fe2MoO4 Imma (74) mp-33537 [hull=0.019, PRIMARY]
- papers: https://doi.org/10.1088/2053-1591/aad14b (Magnetic properties and electronic state of Mo<sub> <i>x</i> </sub>Fe<...)

## Fe-Mo-O-Pb
- rank 3234 | 1 samples | 1 papers | 1 compositions
- compositions: Pb2FeMoO6 (1)
- measured range: 11-392 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1063/1.4817584 (Magnetic properties and magnetoresistance effect of Pb<sub>2</sub>FeMo...)

## Fe-Mo-O-Sr-V
- rank 3235 | 1 samples | 1 papers | 1 compositions
- compositions: Sr2FeMo0.5V0.5O6 (1)
- sample form: Bulk (1)
- measured range: 27-313 K (5th-95th pct of 2 curves; full span incl. outliers 27-852 K)
- papers: https://doi.org/10.1016/s0925-8388(03)00740-0 (Studies of electrical transport properties of Sr2Fe(Mo, V)O6 compound)

## Fe-Mo-S
- rank 3236 | 1 samples | 1 papers | 1 compositions
- compositions: Fe1.3Mo6S8 (1)
- sample form: Bulk (1)
- measured range: 296-957 K (5th-95th pct of 4 curves)
- [ref 1] TEDesignLab / ICSD: Fe(MoS2)2 Cc (9) mp-1193219 [hull=0.145, icsd=4, PRIMARY]; FeMo3S4 P-1 (2) mp-27380 [hull=0.109, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Fe(Mo3S4)2 R-3 (148) mp-1103998 [hull=0.127, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/s11664-009-0975-0 (Thermoelectric Properties of Chevrel-Phase Sulfides M x Mo6S8 (M: Cr, ...)

## Fe-Na-O-Ti
- rank 3237 | 1 samples | 1 papers | 1 compositions
- compositions: Na0.4Fe0.2Ti0.8O2 (1)
- curator composition details (from the paper): NaxMx/2Ti1−x/2O2 (M=Co, Ni and Fe) (1)
- measured range: 568-1047 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NaTiFeO4 Pnma (62) mp-648745 [hull=0.236, icsd=1, PRIMARY]; Na3CaTi3Fe5O16 Pm (6) mp-1173821 [hull=0.287, PRIMARY]; Na3TiFe3O8 P2/m (10) mp-1221213 [hull=0.014, PRIMARY]; NaTi3FeO8 Cm (8) mp-1220877 [hull=0.008, PRIMARY]; NaTiFeO4 Pmc2_1 (26) mp-1220922 [hull=0.007]
- papers: https://doi.org/10.1016/s0272-8842(02)00050-0 (Thermoelectric characterization of NaxMx/2Ti1−x/2O2 (M=Co, Ni and Fe) ...)

## Fe-Nb-Sb-Sn
- rank 3238 | 1 samples | 1 papers | 1 compositions
- compositions: NbFeSb0.84Sn0.16 (1)
- measured range: 322-974 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/j.actamat.2020.07.028 (Tuning of the electronic and phononic properties of NbFeSb half-Heusle...)

## Fe-Ni
- rank 3239 | 1 samples | 1 papers | 1 compositions
- compositions: Fe0.5Ni0.5 (1)
- measured range: 11-281 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeNi3 Pm-3m (221) mp-1418 [hull=0.000, icsd=6, PRIMARY]; Fe3Ni I4/mmm (139) mp-1007862 [hull=0.074, icsd=2, PRIMARY]; FeNi P4/mmm (123) mp-2213 [hull=0.000, icsd=2, PRIMARY]; Fe2Ni Fd-3m (227) mp-1077745 [hull=0.225, icsd=1, PRIMARY]; FeNi2 Fd-3m (227) mp-1072076 [hull=0.202, icsd=1, PRIMARY]
- papers: https://doi.org/10.26565/2222-5617-2022-37 (37)

## Fe-Ni-O-Pr
- rank 3240 | 1 samples | 1 papers | 1 compositions
- compositions: PrNi0.4Fe0.6O3 (1)
- curator composition details (from the paper): The logarithmic values in Fig 11a were converted by making them exponents of 10
original ... (1)
- measured range: 323-1173 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.3390/ma15062166 (Nickel-Containing Perovskites, PrNi0.4Fe0.6O3–δ and PrNi0.4Co0.6O3–δ, ...)

## Fe-Ni-Sb-Ti-Zr
- rank 3241 | 1 samples | 1 papers | 1 compositions
- compositions:  (Zr(Fe0.5Ni0.5)Sb)0.67(TiSb)0.33 (1)
- measured range: 329-845 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.scriptamat.2013.07.006 (Reduced thermal conductivity in nanolamellar composite comprising half...)

## Fe-Ni-Sb-Tl
- rank 3242 | 1 samples | 1 papers | 1 compositions
- compositions: TlFe2.5Ni1.5Sb12 (1)
- sample form: Bulk (1)
- measured range: 324-772 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1063/1.4861157 (Thermoelectric properties of Tl-filled Co-free p-type skutterudites: T...)

## Fe-O-Pb
- rank 3243 | 1 samples | 1 papers | 1 compositions
- compositions: PbFeO3 (1)
- sample form: pellets (1)
- measured range: 354-628 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe12PbO19 Cmcm (63) mp-1199651 [hull=0.064, icsd=1, PRIMARY]; FePbO3 Pm-3m (221) mp-973579 [hull=0.181, PRIMARY]; Fe12PbO19 P6_3/mmc (194) mp-640908 [hull=0.094]
- papers: https://doi.org/10.1038/s41467-021-22064-9 (Observation of novel charge ordering and spin reorientation in perovsk...)

## Fe-O-Sb
- rank 3244 | 1 samples | 1 papers | 1 compositions
- compositions: SbFeO3 (1)
- measured range: 200-398 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe(SbO2)2 P4_2/mbc (135) mp-656060 [hull=0.000, icsd=13, PRIMARY]; Fe(SbO3)4 P1 (1) mp-770991 [hull=0.082, PRIMARY]; FeSbO4 Cmmm (65) mp-675127 [hull=0.000, PRIMARY, AMBIGUOUS]; Fe(SbO2)2 P2_1/c (14) mp-601696 [hull=0.119, icsd=1]; Fe(SbO2)2 P4_2/m (84) mp-601882 [hull=0.101]
- papers: https://doi.org/10.3390/ma15238369 (Influence of Sb3+ Cations on the Structural, Magnetic and Electrical P...)

## Fe-O-Si
- rank 3245 | 1 samples | 1 papers | 1 compositions
- compositions: Fe2SiO4 (1)
- measured range: 294-1073 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe2SiO4 Fd-3m (227) mp-18816 [hull=0.037, icsd=29, PRIMARY]; FeSiO3 Pbca (61) mp-630331 [hull=0.012, icsd=7, PRIMARY]; Fe3(SiO4)2 P2_1/c (14) mp-31859 [hull=0.044, icsd=2, PRIMARY]; FeSiO4 Pnma (62) mp-1191756 [hull=0.248, icsd=1, PRIMARY, AMBIGUOUS]; Fe3Si2O9 C2/m (12) mp-1193684 [hull=0.158, icsd=1, PRIMARY]
- papers: https://doi.org/10.2320/matertrans.m2009097 (Physical Properties of Iron-Oxide Scales on Si-Containing Steels at Hi...)

## Fe-O-V
- rank 3246 | 1 samples | 1 papers | 1 compositions
- compositions: FeV2O6 (1)
- measured range: 153-271 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): V3(FeO6)2 P2_12_12_1 (19) mp-1196228 [hull=0.190, icsd=1, PRIMARY]; V4Fe2O13 P2_1/c (14) mp-1200054 [hull=0.004, icsd=1, PRIMARY]; VFeO4 Cmcm (63) mp-18949 [hull=0.015, icsd=1, PRIMARY]; V14Fe5O32 P1 (1) mp-1101241 [hull=0.056, PRIMARY]; V(FeO2)2 Imma (74) mp-690463 [hull=0.019, PRIMARY]
- papers: https://doi.org/10.1088/1742-6596/1441/1/012012 (Physico-chemical properties of V1-XFeX O2 and FeV2O6)

## Fe-Os-Si
- rank 3247 | 1 samples | 1 papers | 1 compositions
- compositions: Fe0.80Os0.20Si1.96Al0.04 (1)
- dopant candidates (<5% at.): Al (1)
- sample form: Bulk (1)
- measured range: 299-899 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1021/acsami.0c00321 (Doubled Thermoelectric Figure of Merit in p-Type β-FeSi2 via Synergist...)

## Fe-P-Yb
- rank 3248 | 1 samples | 1 papers | 1 compositions
- compositions: Yb2Fe12P7 (1)
- measured range: 10-299 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb2Fe12P7 P-6 (174) mp-1191755 [hull=0.000, icsd=2, PRIMARY]; Yb(FeP3)4 Im-3 (204) mp-12956 [hull=0.000, icsd=1, PRIMARY]; YbFe5P3 Pnma (62) mp-1197850 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/978-94-007-4984-9_3 (Thermoelectric Properties of Correlated Electron Systems Ln 3Pt4Ge6and...)

## Fe-Pt-Sb-Yb
- rank 3249 | 1 samples | 1 papers | 1 compositions
- compositions: YbFe3PtSb12 (1)
- measured range: 12-737 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1063/1.4800827 (Thermoelectric performance of p-type skutterudites YbxFe4−yPtySb12 (0....)

## Fe-Sb-Sn-Te
- rank 3250 | 1 samples | 1 papers | 1 compositions
- compositions: FeSb2Te0.8Sn0.2 (1)
- sample form: Bulk (1)
- measured range: 297-683 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1007/s11664-015-4325-0 (The Influence of Sn Additions on the Thermoelectric and Transport Prop...)
