# Host systems -- chunk 056 of 73

Ranks 2751-2800 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 98.37%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Bi-Fe-O-Sr
- rank 2751 | 1 samples | 1 papers | 1 compositions
- compositions: Bi0.50Sr0.50FeO3 (1)
- curator composition details (from the paper): bulk (pressed and sintered) (1)
- measured range: 572-1013 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr15Fe10(Bi5O23)2 C222 (21) mp-617430 [hull=0.010, icsd=2, PRIMARY]; BaSr6Fe3Bi3O16 I4mm (107) mp-1227908 [hull=0.079, PRIMARY]; Sr2FeBiO6 Fm-3m (225) mp-1205525 [hull=0.031, PRIMARY]; Sr4Fe4Bi5PbO18 Amm2 (38) mp-1218774 [hull=0.164, PRIMARY]; Sr4Fe6Bi7PbO24 Amm2 (38) mp-1218820 [hull=0.167, PRIMARY]
- papers: https://doi.org/10.1016/j.matchemphys.2016.11.052 (Sr doped BiMO 3 (M = Mn, Fe, Y) perovskites: Structure correlated ther...)

## Bi-Fe-S
- rank 2752 | 1 samples | 1 papers | 1 compositions
- compositions: FeBi4S7 (1)
- sample form: Bulk (1)
- measured range: 299-701 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeBi4S7 C2/m (12) mp-1095303 [hull=0.126, icsd=1, PRIMARY]
- papers: https://doi.org/10.1002/adfm.201904112 (XBi\n            4\n            S\n            7\n            (X = Mn,...)

## Bi-Fe-Te
- rank 2753 | 1 samples | 1 papers | 1 compositions
- compositions: Bi1.7Fe0.3Te3 (1)
- sample form: SingleCrystal (1)
- measured range: 301-475 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1007/s11664-014-3438-1 (Transport Property Measurements in Doped Bi2Te3 Single Crystals Obtain...)

## Bi-Fe-Zr
- rank 2754 | 1 samples | 1 papers | 1 compositions
- compositions: Zr6FeBi2 (1)
- sample form: Bulk (1)
- measured range: 10-275 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zr6FeBi2 P-62m (189) mp-1205897 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(99)00537-x (Thermoelectric properties of ternary transition metal antimonides)

## Bi-Gd-Ir-O
- rank 2755 | 1 samples | 1 papers | 1 compositions
- compositions: BiGdIr2O7 (1)
- measured range: 25-299 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1007/s10948-019-05418-9 (Magnetic and Electrical Behavior of Gd Doping Pyrochlore Bi2Ir2O7)

## Bi-Gd-O
- rank 2756 | 1 samples | 1 papers | 1 compositions
- compositions: Gd8Bi3O8 (1)
- sample form: Bulk (1)
- measured range: 11-362 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd2BiO2 I4/mmm (139) mp-1070662 [hull=0.000, icsd=1, PRIMARY]; Gd3BiO3 C2/m (12) mp-1103896 [hull=0.018, icsd=1, PRIMARY]; Gd(BiO2)4 Cm (8) mp-756698 [hull=0.058, PRIMARY]; Gd3(BiO4)2 Cm (8) mp-1178246 [hull=0.043, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2015.10.004 (Synthesis, crystal structure, and physical properties of the Gd 3 BiO ...)

## Bi-Ge-Mg-Si
- rank 2757 | 1 samples | 1 papers | 1 compositions
- compositions: Mg2Si0.7Ge0.3Bi0.2 (1)
- measured range: 322-824 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.3938/jkps.65.57 (Thermoelectric properties of Mg2Si0.7Ge0.3Bi m prepared using a solid-...)

## Bi-Ge-Pb-Te
- rank 2758 | 1 samples | 1 papers | 1 compositions
- compositions: (Ge0.87Pb0.13Te)0.93(Bi2Te3)0.07 (1)
- sample form: Bulk (1)
- measured range: 299-773 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1021/acsami.9b04984 (Stacking Fault-Induced Minimized Lattice Thermal Conductivity in the H...)

## Bi-I-O
- rank 2759 | 1 samples | 1 papers | 1 compositions
- compositions: BiOI (1)
- sample form: SingleCrystal (1)
- measured range: 13-297 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BiIO P4/nmm (129) mp-22987 [hull=0.000, icsd=5, PRIMARY]; Bi(IO3)3 P2_1/c (14) mp-31259 [hull=0.000, icsd=1, PRIMARY]; Bi4I2O5 P2_1 (4) mp-30130 [hull=0.000, icsd=1, PRIMARY]; Bi2I4O13 P2_12_12_1 (19) mp-1204764 [hull=0.000, icsd=1, PRIMARY]; BiI3O11 P-1 (2) mp-1194377 [hull=0.281, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.4972047 (Influence of the reduced dimensionality on the thermodynamical and ele...)

## Bi-I-O-Sr
- rank 2760 | 1 samples | 1 papers | 1 compositions
- compositions: IBi2Sr2Ca0.6Y0.4O8 (1)
- dopant candidates (<5% at.): Ca (1), Y (1)
- measured range: 16-286 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrBi3I3O4 I4mm (107) mp-1218434 [hull=0.052, PRIMARY]
- papers: https://doi.org/10.1016/0921-4534(92)90573-u (Structural and superconducting properties of iodine-intercalated Bi2Sr...)

## Bi-Ir-Na-O
- rank 2761 | 1 samples | 1 papers | 1 compositions
- compositions: Bi2NaIrO6 (1)
- curator composition details (from the paper): single crystal (1)
- measured range: 102-340 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1002/chem.201804226 (On\n            <i>J</i>\n            <sub>eff</sub>\n            =0 G...)

## Bi-K-O-V
- rank 2762 | 1 samples | 1 papers | 1 compositions
- compositions: K0.5Bi0.5VO3 (1)
- sample form: Bulk (1)
- measured range: 249-299 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): K3V3(BiO6)2 C2/c (15) mp-622115 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/acs.chemmater.8b02379 (Na1/2Bi1/2VO3 and K1/2Bi1/2VO3: New Lead-Free Tetragonal Perovskites w...)

## Bi-K-Se-Sn
- rank 2763 | 1 samples | 1 papers | 1 compositions
- compositions: K1.46Sn3.09Bi7.45Se15 (1)
- measured range: 80-295 K (5th-95th pct of 3 curves; full span incl. outliers 80-350 K)
- papers: https://doi.org/10.1021/cm0003323 (Modular Construction of A1+xM4-2xM‘7+xSe15(A = K, Rb; M = Pb, Sn; M‘ =...)

## Bi-La-Mn-Ni-O
- rank 2764 | 1 samples | 1 papers | 1 compositions
- compositions: LaBiMn1.33Ni0.67O5.96 (1)
- measured range: 108-400 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1039/b705027e (Enhancement of ferromagnetism by Co and Ni substitution in the perovsk...)

## Bi-La-O-Pb-S
- rank 2765 | 1 samples | 1 papers | 1 compositions
- compositions: LaPbBiS3O (1)
- sample form: Bulk (1)
- measured range: 10-323 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1021/ic501687h (Design and Synthesis of a New Layered Thermoelectric Material LaPbBiS3O)

## Bi-Li-Te
- rank 2766 | 1 samples | 1 papers | 1 compositions
- compositions: Li1.1Bi2Se0.3Te2.7 (1)
- dopant candidates (<5% at.): Se (1)
- measured range: 14-500 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiBiTe2 P4/mmm (123) mp-1222394 [hull=0.278, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2012.11.028 (Structural modifications and non-monotonic carrier concentration in Bi...)

## Bi-Li-Tl
- rank 2767 | 1 samples | 1 papers | 1 compositions
- compositions: Li2TlBi (1)
- measured range: 199-499 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li2TlBi Fm-3m (225) mp-865713 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1038/s41467-019-08542-1 (Designing chemical analogs to PbTe with intrinsic high band degeneracy...)

## Bi-Mg-O-Si
- rank 2768 | 1 samples | 1 papers | 1 compositions
- compositions: Mg2SiBi5O7.5 (1)
- measured range: 304-864 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg14SiBiO16 Pmmm (47) mp-1034633 [hull=0.341, PRIMARY]; Mg30SiBiO32 P4/mmm (123) mp-1039843 [hull=0.163, PRIMARY]; Mg6SiBiO8 P4/mmm (123) mp-1030926 [hull=0.672, PRIMARY]; Mg14SiBiO16 P4/mmm (123) mp-1034587 [hull=0.377]
- papers: https://doi.org/10.1016/j.intermet.2012.08.026 (Fabrication and thermoelectric properties of Mg2Si-based composites us...)

## Bi-Mg-P
- rank 2769 | 1 samples | 1 papers | 1 compositions
- compositions: Mg3Bi1.5P0.5 (1)
- sample form: Bulk (1)
- measured range: 83-855 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1007/s11664-012-2417-7 (On the Thermoelectric Properties of Zintl Compounds Mg3Bi2−x Pn x (Pn ...)

## Bi-Mg-Sm-Yb
- rank 2770 | 1 samples | 1 papers | 1 compositions
- compositions: Sm0.5Yb0.5Mg2Bi1.99 (1)
- sample form: Bulk (1)
- measured range: 304-774 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1039/c9ta13224d (Achieving high-performance p-type SmMg2Bi2 thermoelectric materials th...)

## Bi-Mn-O
- rank 2771 | 1 samples | 1 papers | 1 compositions
- compositions: Bi2Mn4O10 (1)
- curator composition details (from the paper): polycrystalline (1)
- measured range: 307-572 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnBiO3 C2/c (15) mp-25035 [hull=0.027, icsd=9, PRIMARY]; Mn7BiO12 C2/m (12) mp-1189861 [hull=0.037, icsd=2, PRIMARY]; Mn2Bi3O7 Cmc2_1 (36) mp-1190266 [hull=0.071, icsd=2, PRIMARY]; Mn16Bi16O45 I-43d (220) mp-1198549 [hull=0.042, icsd=1, PRIMARY]; Mn(Bi5O8)5 C2 (5) mp-763158 [hull=0.030, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2015.08.165 (Magnetic and transport properties assisted by local distortions in Bi ...)

## Bi-Mn-O-Ti
- rank 2772 | 1 samples | 1 papers | 1 compositions
- compositions: (La0.7Sr0.3MnO3)72(SrBi4Ti4O15)28 (1)
- dopant candidates (<5% at.): La (1), Sr (1)
- sample form: Bulk (1)
- measured range: 299-802 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/j.jallcom.2020.157001 (Colossal seebeck coefficient in Aurivillius phase-perovskite oxide com...)

## Bi-Mn-Sb
- rank 2773 | 1 samples | 1 papers | 1 compositions
- compositions: Mn3.2Sb1.5Bi0.49Se0.01 (1)
- dopant candidates (<5% at.): Se (1)
- sample form: Bulk (1)
- measured range: 322-724 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn4BiSb3 Pmm2 (25) mp-1221739 [hull=0.058, PRIMARY]
- papers: https://doi.org/10.1021/acsami.0c01004 (Realizing a High ZT of 1.6 in N-Type Mg3Sb2-Based Zintl Compounds thro...)

## Bi-Mo-O
- rank 2774 | 1 samples | 1 papers | 1 compositions
- compositions: Bi2Mo2O9 (1)
- sample form: Bulk (1)
- measured range: 323-823 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi(MoO5)2 P2_1/m (11) mp-1193126 [hull=0.327, icsd=2, PRIMARY]; Bi2(MoO4)3 P2_1/c (14) mp-32039 [hull=0.000, icsd=2, PRIMARY]; Bi2MoO6 Pca2_1 (29) mp-25708 [hull=0.000, icsd=2, PRIMARY]; RbLiBi2(MoO4)4 C2/c (15) mp-650024 [hull=0.003, icsd=1, PRIMARY]; BaBi2(MoO4)4 C2/c (15) mp-642792 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2015.05.166 (Low thermal conductivity of Bi 2 Mo 2 O 9 ceramics)

## Bi-Mo-Se
- rank 2775 | 1 samples | 1 papers | 1 compositions
- compositions: MoBi2Se5 (1)
- measured range: 303-498 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.materresbull.2012.08.026 (Synthesis of fibrous reticulate nanocrystalline n-type MoBi2(Se1−xTex)...)

## Bi-N-Sb-Te
- rank 2776 | 1 samples | 1 papers | 1 compositions
- compositions: (Bi0.4Sb1.6Te3)93.24(C3N4)6.76 (1)
- dopant candidates (<5% at.): C (1)
- sample form: Bulk (1)
- measured range: 303-476 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/j.jallcom.2020.156872 (Graphitic carbon nitride-bismuth antimony telluride nanocomposites: A ...)

## Bi-Na-O-V
- rank 2777 | 1 samples | 1 papers | 1 compositions
- compositions: Na0.5Bi0.5VO3 (1)
- sample form: Bulk (1)
- measured range: 150-297 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Na3V4(Bi10O21)2 C2/m (12) mp-1210725 [hull=0.022, PRIMARY]; NaV2Bi3O10 P1 (1) mp-1220913 [hull=0.000, PRIMARY]; NaV4Bi13O30 C2 (5) mp-1212549 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1021/acs.chemmater.8b02379 (Na1/2Bi1/2VO3 and K1/2Bi1/2VO3: New Lead-Free Tetragonal Perovskites w...)

## Bi-Na-Sn-Te
- rank 2778 | 1 samples | 1 papers | 1 compositions
- compositions: NaSn5BiTe7 (1)
- sample form: Bulk (1)
- measured range: 322-861 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1021/jacs.0c05650 (Contrasting SnTe–NaSbTe2 and SnTe–NaBiTe2 Thermoelectric Alloys: High ...)

## Bi-Ni-Y
- rank 2779 | 1 samples | 1 papers | 1 compositions
- compositions: YNiBi (1)
- measured range: 26-924 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y5Ni2Bi I4/mcm (140) mp-1189582 [hull=0.008, icsd=1, PRIMARY]; YNiBi F-43m (216) mp-30460 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.4921811 (Synthesis and thermoelectric properties of half-Heusler alloy YNiBi)

## Bi-O-Pb
- rank 2780 | 1 samples | 1 papers | 1 compositions
- compositions: Bi6Pb2O11 (1)
- measured range: 289-660 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi12PbO20 I23 (197) mp-667342 [hull=0.018, icsd=1, PRIMARY]; Bi10(Pb2O7)3 P-1 (2) mp-758225 [hull=0.019, PRIMARY]; Bi12Pb4O21 P-1 (2) mp-1214432 [hull=0.064, PRIMARY]; Bi12PbO19 R3 (146) mp-757785 [hull=0.029, PRIMARY]
- papers: https://doi.org/10.1109/icsd.2004.1350310 (Electrical and thermal properties of Bi/sub 2/O/sub 3/, PbO and mixed ...)

## Bi-O-Ru-Y
- rank 2781 | 1 samples | 1 papers | 1 compositions
- compositions: BiYRu2O7 (1)
- sample form: Bulk (1)
- measured range: 477-1074 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y3Bi(Ru2O7)2 R-3m (166) mp-1216097 [hull=0.012, PRIMARY]; YBi3(Ru2O7)2 R-3m (166) mp-1215993 [hull=0.010, PRIMARY]; YBiRu2O7 Imma (74) mp-1215989 [hull=0.016, PRIMARY]
- papers: https://doi.org/10.2109/jcersj.112.298 (Thermoelectric Properties of CuO-Added AgSbO3 Ceramics)

## Bi-O-Sb-Te-Y
- rank 2782 | 1 samples | 1 papers | 1 compositions
- compositions: (Bi0.5Sb1.5Te3)84.08(Y2O3)15.92 (1)
- sample form: Bulk (1)
- measured range: 299-500 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1016/j.intermet.2016.11.002 (Enhanced Seebeck coefficient by energy filtering in Bi-Sb-Te based com...)

## Bi-O-Sb-Te-Zn
- rank 2783 | 1 samples | 1 papers | 1 compositions
- compositions: (Bi0.5Sb1.5Te3)69.78(ZnO)30.22 (1)
- sample form: Bulk (1)
- measured range: 294-460 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/j.jallcom.2016.10.076 (Carriers concentration tailoring and phonon scattering from n-type zin...)

## Bi-O-Sb-Te-Zr
- rank 2784 | 1 samples | 1 papers | 1 compositions
- compositions: ((Bi2Te3)0.25(Sb2Te3)0.75)74.24(ZrO2)25.76 (1)
- curator composition details (from the paper): p-type Bi2Te3 + 75%Sb2Te3 (hereafter referred to as BiSbTe) alloy powder+ 6 wt%ZrO2 (1)
- sample form: Composite (1)
- measured range: 299-500 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1063/1.4984914 (Enhanced thermoelectric figure-of-merit in Bi-Sb-Te nanocomposites wit...)

## Bi-O-Se-Sn
- rank 2785 | 1 samples | 1 papers | 1 compositions
- compositions: Bi1.25Sn0.75O2Se (1)
- measured range: 298-773 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1007/s10832-014-9969-2 (High-temperature thermoelectric behaviors of Sn-doped n-type Bi2O2Se c...)

## Bi-O-Se-Te
- rank 2786 | 1 samples | 1 papers | 1 compositions
- compositions: (Bi2Te2.7Se0.3)90.28(Y2O3)9.72 (1)
- dopant candidates (<5% at.): Y (1)
- sample form: Bulk (1)
- measured range: 300-501 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi2Te2SeO10 C2/c (15) mp-1192658 [hull=0.022, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/acsami.1c12722 (Realize High Thermoelectric Properties in n-Type Bi2Te2.7Se0.3/Y2O3 Na...)

## Bi-O-Sr
- rank 2787 | 1 samples | 1 papers | 1 compositions
- compositions: Bi2Sr2Ca0.6Y0.4O8 (1)
- dopant candidates (<5% at.): Ca (1), Y (1)
- measured range: 27-287 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2Bi2O5 Pnma (62) mp-23357 [hull=0.000, icsd=2, PRIMARY]; Sr(BiO2)2 C2/m (12) mp-29048 [hull=0.000, icsd=1, PRIMARY]; Sr4BiO7 P2_1 (4) mp-1191534 [hull=0.032, icsd=1, PRIMARY]; SrBiO3 P2_1/c (14) mp-29164 [hull=0.000, icsd=1, PRIMARY]; Sr4Bi2O I4/mmm (139) mp-1025351 [hull=0.000, PRIMARY, AMBIGUOUS]
- papers: https://doi.org/10.1016/0921-4534(92)90573-u (Structural and superconducting properties of iodine-intercalated Bi2Sr...)

## Bi-O-Te
- rank 2788 | 1 samples | 1 papers | 1 compositions
- compositions: Bi2O2Te (1)
- sample form: Bulk (1)
- measured range: 302-667 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi2TeO5 Aem2 (39) mp-23334 [hull=0.000, icsd=2, PRIMARY]; Bi2Te2O7 Pbcn (60) mp-667426 [hull=0.000, icsd=1, PRIMARY]; Bi2Te4O11 P2_1/c (14) mp-28990 [hull=0.000, icsd=1, PRIMARY]; Bi2TeO2 I4/mmm (139) mp-849872 [hull=0.003, icsd=1, PRIMARY]; Bi2TeO6 Cmce (64) mp-27251 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2015.02.026 (Synthesis, characterisation and thermoelectric properties of the oxyte...)

## Bi-O-Te-Zn
- rank 2789 | 1 samples | 1 papers | 1 compositions
- compositions: (Bi2Te2.7Se0.3)66.3(ZnO)33.7 (1)
- dopant candidates (<5% at.): Se (1)
- sample form: Bulk (1)
- measured range: 306-496 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/j.jallcom.2016.10.076 (Carriers concentration tailoring and phonon scattering from n-type zin...)

## Bi-Pb-Sn-Te
- rank 2790 | 1 samples | 1 papers | 1 compositions
- compositions: Sn0.6Pb0.4Bi2Te4 (1)
- measured range: 27-292 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/j.jssc.2014.12.016 (Transport properties of the SnBi2Te4–PbBi2Te4 solid solution)

## Bi-Pt
- rank 2791 | 1 samples | 1 papers | 1 compositions
- compositions: (Ce0.09La0.01)3Bi4Pt3 (1)
- dopant candidates (<5% at.): Ce (1), La (1)
- sample form: SingleCrystal (1)
- measured range: 11-300 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi2Pt Pa-3 (205) mp-22864 [hull=0.003, icsd=4, PRIMARY]; BiPt P6_3/mmc (194) mp-1066078 [hull=0.000, icsd=2, PRIMARY]; BiPt3 I4/mmm (139) mp-1183477 [hull=0.152, PRIMARY, AMBIGUOUS]; Bi2Pt P31m (157) mp-1078313 [hull=0.010, icsd=2]; Bi2Pt C2/m (12) mp-1092293 [hull=0.036, icsd=1]
- papers: https://doi.org/10.1103/physrevb.50.18142 (Substitutional effects on the electronic transport of the Kondo semico...)

## Bi-S-Sb-Se-Te
- rank 2792 | 1 samples | 1 papers | 1 compositions
- compositions: Bi1.6Sb0.4Te2.4Se0.3S0.3 (1)
- sample form: Bulk (1)
- measured range: 299-450 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1134/s1063783406120080 (Thermoelectric properties of multicomponent solid solutions based on b...)

## Bi-S-Tl
- rank 2793 | 1 samples | 1 papers | 1 compositions
- compositions: TlBiS2 (1)
- measured range: 78-300 K (5th-95th pct of 2 curves)
- [ref 1] TEDesignLab / ICSD: Tl4Bi2S5 Pnma (62) mp-23408 [hull=0.000, icsd=1, PRIMARY]; TlBiS2 (166)
- [ref 2] MP, ranked by ICSD evidence: TlBiS2 I4_1/amd (141) mp-36946 [hull=0.124, PRIMARY]; Tl3BiS6 Cmmm (65) mp-1209731 [hull=1.318, PRIMARY]; Tl(BiS2)3 Cmmm (65) mp-1207370 [hull=1.364, PRIMARY]; TlBiS2 P4/mmm (123) mp-1216528 [hull=0.207]
- papers: https://doi.org/10.1007/s10582-005-0076-0 (Thermoelectric Properties of the TlBiS2-PbS Alloys)

## Bi-Sb-Zn
- rank 2794 | 1 samples | 1 papers | 1 compositions
- compositions: (Zn2Sb3)75.9Bi24.1 (1)
- measured range: 294-592 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1038/s41427-020-0197-8 (Conversion of p–n conduction type by spinodal decomposition in Zn-Sb-B...)

## Bi-Sn
- rank 2795 | 1 samples | 1 papers | 1 compositions
- compositions: Sn0.95Bi0.05 (1)
- measured range: 12-331 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sn3Bi Fm-3m (225) mp-1038778 [hull=0.070, PRIMARY]; SnBi I-4m2 (119) mp-1218964 [hull=0.063, PRIMARY]; SnBi3 Fm-3m (225) mp-978882 [hull=0.138, PRIMARY]; Sn3Bi I4/mmm (139) mp-1039344 [hull=0.088]; Sn3Bi Pm-3m (221) mp-1187024 [hull=0.100]
- papers: https://doi.org/10.1016/j.jallcom.2016.07.093 (Role of chemical doping on the enhancement of thermoelectric performan...)

## Br-C-H-N
- rank 2796 | 1 samples | 1 papers | 1 compositions
- compositions: (BrC6H4NH2)2CuBr2 (1)
- dopant candidates (<5% at.): Cu (1)
- sample form: Film (1)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 40-388 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuH12C6(Br3N2)2 P-1 (2) mp-1200376 [hull=0.176, icsd=2, PRIMARY]; CdH24C4(BrN2)6 P2_1/c (14) mp-707501 [hull=0.000, icsd=1, PRIMARY]; CdH8C4(BrN4)2 P2_1/c (14) mp-1204632 [hull=0.053, icsd=1, PRIMARY]; CoH12C2(Br2N)2 P2_1/c (14) mp-1195995 [hull=0.034, icsd=1, PRIMARY]; H10C3BrN P2_1/m (11) mp-1193595 [hull=0.104, icsd=1, PRIMARY]
- papers: https://doi.org/10.1039/d2ta07409e (Giant power factor and high air stability in an n-type metal–organic c...)

## Br-I-P-Sn
- rank 2797 | 1 samples | 1 papers | 1 compositions
- compositions: Sn24P19.3Br4I4 (1)
- measured range: 36-291 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.solidstatesciences.2007.05.008 (Crystal structure, thermoelectric and magnetic properties of the type-...)

## Br-La-P-Zn
- rank 2798 | 1 samples | 1 papers | 1 compositions
- compositions: La3Zn4P6.6Br0.8 (1)
- sample form: SingleCrystal (1)
- measured range: 11-402 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1021/acs.chemmater.6b01752 (Enclathration of X@La4 Tetrahedra in Channels of Zn–P Frameworks in La...)

## Br-Li
- rank 2799 | 1 samples | 1 papers | 1 compositions
- compositions: LiBr (1)
- measured range: 99-399 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiBr Fm-3m (225) mp-23259 [hull=0.025, icsd=4, PRIMARY]; LiBr P6_3mc (186) mp-976280 [hull=0.000]
- papers: https://doi.org/10.1088/0953-8984/1/25/009 (Thermal conductivity and heat capacity of solid LiBr and RbF under pre...)

## C-Cl-H
- rank 2800 | 1 samples | 1 papers | 1 compositions
- compositions: (CH3Cl)27.88(C)72.12 (1)
- curator composition details (from the paper): PVC,  CH3Cl ,name polyvinyl chloride, CAS.No: 9002-86-2

C/PVC=8:13 (1)
- sample form: Film (1)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 290-340 K (5th-95th pct of 5 curves; full span incl. outliers 290-380 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): H3CCl Cmc2_1 (36) mp-1078233 [hull=0.078, icsd=4, PRIMARY]; FeH20C8NCl4 Pca2_1 (29) mp-1194614 [hull=0.046, icsd=2, PRIMARY]; AlSnPH18(C3Cl2)2 Pnma (62) mp-1199681 [hull=0.037, icsd=1, PRIMARY]; AlSiPH9C3NCl6 P2_1/c (14) mp-1197294 [hull=0.123, icsd=1, PRIMARY]; FeH12C4NCl4 Pma2 (28) mp-603940 [hull=0.085, icsd=1, PRIMARY]
- papers: https://doi.org/10.1002/adma.201405463 (Novel Hybrid Organic Thermoelectric Materials:Three-Component Hybrid F...)
