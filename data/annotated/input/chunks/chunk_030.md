# Host systems -- chunk 030 of 73

Ranks 1451-1500 by sample count. These 50 host systems cover 200 samples (0.38% of the TE set); cumulative through this chunk: 93.57%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## In-N
- rank 1451 | 4 samples | 2 papers | 1 compositions
- compositions: InN (4)
- sample form: Film (4)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 16-573 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): InN P6_3mc (186) mp-22205 [hull=0.000, icsd=12, PRIMARY]; InN3 Pm-3m (221) mp-975606 [hull=2.393, PRIMARY]; InN F-43m (216) mp-20411 [hull=0.010, icsd=5]; InN Fm-3m (225) mp-20812 [hull=0.210, icsd=2]
- papers: https://doi.org/10.1063/1.3466913 (Pressure cycling of InN to 20 GPa: In situ transport properties and am...) | https://doi.org/10.1063/1.4875482 (Advantage of In- over N-polarity for disclosure of p-type conduction i...)

## In-Ni-O-Sn
- rank 1452 | 4 samples | 1 papers | 4 compositions
- compositions: In1.2Ni0.4Sn0.4O3 (1); InNi0.5Sn0.5O3 (1); In1.4Ni0.3Sn0.3O3 (1); In0.9Ni0.55Sn0.55O3 (1)
- sample form: Bulk (4)
- measured range: 10-321 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1063/1.2986148 (Enhancement of the thermoelectric performances of In2O3 by the coupled...)

## In-O-Ti
- rank 1453 | 4 samples | 1 papers | 4 compositions
- compositions: In12Ti10Al2MgO42 (1); In12Ti10Al2ZnO42 (1); In12Ti10Ga2MgO42 (1); In12Ti10Ga2ZnO42 (1)
- dopant candidates (<5% at.): Al (2), Mg (2), Zn (2), Ga (2)
- measured range: 297-845 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1111/jace.15920 (Phase stability, microstructure, and dielectric properties of quaterna...)

## In-Se-Te
- rank 1454 | 4 samples | 3 papers | 4 compositions
- compositions: In4Se0.5Te2.5 (1); In2(Te0.90Se0.10)5 (1); Fe0.05In1.95(Te0.90Se0.10)5 (1); In4(Se0.83Te0.17)3 (1)
- dopant candidates (<5% at.): Fe (1)
- sample form: Bulk (2); SingleCrystal (2)
- solid-solution axis: Se/(Se+Te) spans 0.10-0.83 (median 0.17) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 11-672 K (5th-95th pct of 19 curves)
- papers: https://doi.org/10.1063/1.3493269 (Thermoelectric properties of bipolar diffusion effect on In4Se3−xTex c...) | https://doi.org/10.1007/s11664-016-4778-9 (Improvement in Thermoelectric Properties by Tailoring at In and Te Sit...) | https://doi.org/10.1007/s11664-010-1492-x (Thermoelectric Properties of Spark Plasma-Sintered In4Se3-In4Te3)

## Ir-Na-O
- rank 1455 | 4 samples | 1 papers | 2 compositions
- compositions: Na3Ir3O8 (2); Na3.6Ir3O8 (2)
- sample form: SingleCrystal (2)
- measured range: 11-291 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Na2IrO3 C2/m (12) mp-754844 [hull=0.000, icsd=1, PRIMARY]; Na4IrO4 I4/m (87) mp-28698 [hull=0.000, icsd=1, PRIMARY]; NaIrO3 Cmcm (63) mp-1079568 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.91.075129 (Thermal conductivity across the metal-insulator transition in the sing...)

## Ir-Ni-Sn-Zr
- rank 1456 | 4 samples | 2 papers | 4 compositions
- compositions: Zr30.1Ni27.4Ir11.5Sn31.1 (1); Zr31.4Ni30.1Ir6.1Sn32.4 (1); Zr31.7Ni28.9Ir8.3Sn31.1 (1); ZrNiIr0.2Sn (1)
- sample form: Bulk (3)
- measured range: 304-1032 K (5th-95th pct of 21 curves)
- papers: https://doi.org/10.1016/j.actamat.2010.04.028 (Vacancy site occupation by Co and Ir in half-Heusler ZrNiSn and conver...) | https://doi.org/10.1007/s11837-014-1233-3 (Ordered Structures and Thermoelectric Properties of MNiSn (M = Ti, Zr,...)

## Ir-O-V
- rank 1457 | 4 samples | 1 papers | 1 compositions
- compositions: Ir0.71V0.29O2 (4)
- measured range: 19-323 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): VIrO3 Pm-3m (221) mp-972116 [hull=1.228, PRIMARY]
- papers: https://doi.org/10.1002/advs.202204424 (Enhanced Electron Correlation and Significantly Suppressed Thermal Con...)

## Ir-Ru-Se
- rank 1458 | 4 samples | 1 papers | 1 compositions
- compositions: Ru0.8Ir0.2Se2 (4)
- sample form: Bulk (4)
- measured range: 10-301 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1063/1.4913919 (Enhanced thermoelectric power and electronic correlations in RuSe2)

## K-Ni
- rank 1459 | 4 samples | 1 papers | 4 compositions
- compositions: K1Ni4 (1); K1Ni5 (1); K1Ni10 (1); K1Ni14 (1)
- measured range: 50-400 K (5th-95th pct of 12 curves)
- papers: https://doi.org/10.1021/acs.jpclett.9b00716 (Boosting the Seebeck Coefficient for Organic Coordination Polymers: Ro...)

## La-Li-Mn-O
- rank 1460 | 4 samples | 1 papers | 1 compositions
- compositions: La3LiMn4O12 (4)
- sample form: Bulk (4)
- measured range: 10-400 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiLa2Mn3O9 P-3m1 (164) mp-1222383 [hull=0.107, PRIMARY]; LiLa3MnO7 P2_1/c (14) mp-769464 [hull=0.000, PRIMARY, AMBIGUOUS]; LiLa4MnO8 I4_1/amd (141) mp-770950 [hull=0.036, PRIMARY, AMBIGUOUS]; LiLa6Mn3O14 Pc (7) mp-771521 [hull=0.045, PRIMARY]; LiLa3MnO7 P2_1/m (11) mp-1222623 [hull=0.001]
- papers: https://doi.org/10.1007/s00339-016-9731-5 (Effect of bismuth doping on the physical properties of La–Li–Mn–O mang...)

## La-Mn-Nd-O-Sr
- rank 1461 | 4 samples | 3 papers | 3 compositions
- compositions: (La0.5Nd0.5)0.7Sr0.3MnO3 (2); Nd0.4La0.3Sr0.3MnO3 (1); La0.35Nd0.35Sr0.3MnO3 (1)
- sample form: pellets (2)
- measured range: 27-373 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1007/s00339-020-3333-y (Nature of correlated polaron hopping mechanism in A-site cation disord...) | https://doi.org/10.1016/s0921-4526(02)00820-7 (X-ray diffraction, magnetic and electrical properties in the manganite...) | https://doi.org/10.1063/1.372291 (Effect of annealing in reduced oxygen pressure on the electrical trans...)

## La-O-Ru
- rank 1462 | 4 samples | 2 papers | 4 compositions
- compositions: LaRuO3 (1); LaRu0.95Cr0.05O3 (1); LaRu0.98Cr0.02O3 (1); LaRu0.9Cr0.1O3 (1)
- dopant candidates (<5% at.): Cr (3)
- measured range: 345-1273 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2RuO5 P2_1/c (14) mp-5299 [hull=0.024, icsd=2, PRIMARY]; La3RuO7 Cmcm (63) mp-3222 [hull=0.000, icsd=2, PRIMARY]; La3Ru3O11 Pn-3 (201) mp-5032 [hull=0.007, icsd=2, PRIMARY]; LaRuO3 Pnma (62) mp-20472 [hull=0.048, icsd=1, PRIMARY]; La19(RuO6)8 P1 (1) mp-766364 [hull=0.016, PRIMARY]
- papers: https://doi.org/10.1007/s12034-017-1491-0 (Chemical synthesis and characterization of nano-sized rare-earth ruthe...) | https://doi.org/10.1016/j.ssc.2016.02.003 (Fabrication, characterization and electrical conductivity of Ru-doped ...)

## La-Ru-Sb
- rank 1463 | 4 samples | 3 papers | 1 compositions
- compositions: LaRu4Sb12 (4)
- sample form: SingleCrystal (2)
- measured range: 10-292 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(Sb3Ru)4 Im-3 (204) mp-1188603 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.physb.2006.03.067 (Roles of spin fluctuations and rattling in magnetic and thermoelectric...) | https://doi.org/10.1088/0953-8984/14/45/317 (Transport properties in the filled-skutterudite compounds RERu4Sb12 (R...) | https://doi.org/10.1016/s0921-4526(01)01295-9 (Unusual behavior in the heavy Fermion semi-metal CeRu4Sb12)

## La-Te-Yb
- rank 1464 | 4 samples | 1 papers | 4 compositions
- compositions: Yb0.079La0.348Te0.574 (1); La2.2Yb0.52Te4 (1); La1.58Yb1.63Te4 (1); Yb0.086La0.34Te0.574 (1)
- sample form: Bulk (4)
- solid-solution axis: La/(La+Yb) spans 0.49-0.81 (median 0.81) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 296-1264 K (5th-95th pct of 15 curves)
- papers: https://doi.org/10.1021/cm1004054 (Optimizing Thermoelectric Efficiency in La3−xTe4via Yb Substitution)

## Li
- rank 1465 | 4 samples | 1 papers | 1 compositions
- compositions: Li20 (4)
- measured range: 463-1163 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li Im-3m (229) mp-135 [hull=0.000, icsd=13, PRIMARY]; Li Fm-3m (225) mp-51 [hull=0.003, icsd=5]; Li R-3m (166) mp-1018134 [hull=0.001, icsd=3]; Li P6_3/mmc (194) mp-976411 [hull=0.002, icsd=3]; Li P6/mmm (191) mp-1063005 [hull=0.013, icsd=1]
- papers: https://doi.org/10.1016/0022-3115(80)90036-7 (Porosity dependence on thermal diffusivity and thermal conductivity of...)

## Lu-Ni-Sb
- rank 1466 | 4 samples | 3 papers | 1 compositions
- compositions: LuNiSb (4)
- measured range: 11-994 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LuNiSb F-43m (216) mp-20185 [hull=0.000, icsd=2, PRIMARY]; Lu5Ni2Sb I4/mcm (140) mp-1210754 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2019.152596 (High-temperature power factor of half-Heusler phases RENiSb (RE = Sc, ...) | https://doi.org/10.1016/j.matpr.2019.02.055 (Effect of secondary LuNiSn phase on thermoelectric properties of half-...) | https://doi.org/10.1103/physrevapplied.14.054046 (Thermoelectric Performance of the Half-Heusler Phases \n<mml:math xmln...)

## Mg-O-Ti
- rank 1467 | 4 samples | 2 papers | 4 compositions
- compositions: MgTi2O5(TiN)0.359 (1); MgTi2O5 (1); MgTi2.67O6.34(TiN)0.455 (1); Ti0.73Mg0.27O (1)
- dopant candidates (<5% at.): N (2)
- sample form: Bulk (3)
- measured range: 11-973 K (5th-95th pct of 16 curves)
- [ref 1] TEDesignLab / ICSD: MgTiO3 R-3 (148) mp-3771 [hull=0.000, icsd=30, PRIMARY]; MgTi2O4 P4_12_12 (92) mp-1194382 [hull=0.017, icsd=1, PRIMARY, AMBIGUOUS]
- [ref 2] MP, ranked by ICSD evidence: MgTi2O5 Cmcm (63) mp-28232 [hull=0.000, icsd=1, PRIMARY]; Mg2TiO P-1 (2) mp-675042 [hull=0.667, PRIMARY]; Mg11Ti25O60 P1 (1) mp-757825 [hull=0.000, PRIMARY]; Mg2Ti2O5 Ima2 (46) mp-1076652 [hull=0.254, PRIMARY]; MgTi2O4 Fd-3m (227) mp-27872 [hull=0.017, icsd=1]
- papers: https://doi.org/10.1016/j.scriptamat.2019.11.008 (Thermoelectric properties of MgTi2O5/TiN conductive composites prepare...) | https://doi.org/10.1016/j.actamat.2020.09.001 (Mg-doping enhanced superconductivity and ferromagnetism in Ti1−\n Mg O...)

## Mg-Si-Sr
- rank 1468 | 4 samples | 2 papers | 4 compositions
- compositions: Mg2Si0.7Sr0.3 (1); Mg2Si0.8Sr0.2 (1); Mg2Si0.75Sr0.25 (1); Sr2Mg4Si3 (1)
- solid-solution axis: Mg/(Mg+Sr) spans 0.67-0.91 (median 0.89) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 302-850 K (5th-95th pct of 15 curves)
- [ref 1] TEDesignLab / ICSD: SrMgSi Pnma (62) mp-15642 [hull=0.000, icsd=2, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Sr13(MgSi10)2 Pbam (55) mp-29546 [hull=0.000, icsd=1, PRIMARY]; SrMgSi2 Pnma (62) mp-29002 [hull=0.000, icsd=1, PRIMARY]; SrMg6Si Amm2 (38) mp-1017456 [hull=0.175, PRIMARY]; SrMg14Si Amm2 (38) mp-1026717 [hull=0.108, PRIMARY]; SrMgSi F-43m (216) mp-962059 [hull=0.874]
- papers: https://doi.org/10.1007/s11664-012-2450-6 (High-Performance p-Type Magnesium Silicon Thermoelectrics) | https://doi.org/10.1007/s11664-016-4658-3 (Thermoelectric Hexagonal A-Mg-Si with A = Sr and Ba Zintl Phases)

## Mg-Tb-Zn
- rank 1469 | 4 samples | 2 papers | 2 compositions
- compositions: Tb8.7Mg34.6Zn56.8_IQC (3); Y1.08Tb7.92Mg42Zn57 (1)
- dopant candidates (<5% at.): Y (1)
- measured range: 10-297 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TbMgZn2 Fm-3m (225) mp-1187349 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1080/13642819808206407 (Growth of large-grain R-Mg-Zn quasicrystals from the ternary melt (R =...) | https://doi.org/10.1103/physrevb.59.308 (Magnetic and transport properties of single-grainR−Mg−Znicosahedral qu...)

## Mn-Ni-Sn-Ti
- rank 1470 | 4 samples | 2 papers | 4 compositions
- compositions: Ti6.2Ni33.9Mn36.4Sn30.9Bi0.4 (1); Ti0.967Mn0.163Ni0.98Sn1.04 (1); Ti0.984Mn0.19Ni1.01Sn1.013 (1); Ti0.855Mn0.20Ni1.06Sn0.98 (1)
- dopant candidates (<5% at.): Bi (1)
- sample form: Bulk (3)
- measured range: 20-888 K (5th-95th pct of 19 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiMn(Ni2Sn)2 R-3m (166) mp-1217085 [hull=0.044, PRIMARY]
- papers: https://doi.org/10.1557/opl.2013.217 (Thermoelectric behaviour of p- and n- type Ti-Ni-Sn half Heusler alloy...) | https://doi.org/10.1063/1.4979816 (Optimized thermoelectric performance of the n-type half-Heusler materi...)

## Mn-O-Pb-Pr
- rank 1471 | 4 samples | 2 papers | 3 compositions
- compositions: Pr0.67Pb0.33MnO3 (2); Pr0.7Pb0.3MnO3 (1); La0.2Pr0.5Pb0.3MnO3 (1)
- dopant candidates (<5% at.): La (1)
- sample form: rod-shaped (2)
- measured range: 42-299 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Pr3Mn4PbO12 Pm (6) mp-1220019 [hull=0.023, PRIMARY]
- papers: https://doi.org/10.1088/0022-3727/40/3/005 (Thermopower studies of Pr0.67D0.33MnO3manganite system) | https://doi.org/10.1109/tmag.2005.854827 (Variation of magnetic and transport properties in magnetoresistive oxi...)

## Mn-O-Sn-Te
- rank 1472 | 4 samples | 1 papers | 4 compositions
- compositions: (SnTe)85.47(MnO2)14.53 (1); (SnTe)81.52(MnO2)18.48 (1); (SnTe)77.92(MnO2)22.08 (1); (SnTe)74.63(MnO2)25.37 (1)
- solid-solution axis: O/(O+Te) spans 0.25-0.40 (median 0.36) over 4 compositions
     CHECK: same periodic group, but oxygen often occupies its own sublattice (BiCuSeO, LaFeAsO) rather than substituting for the heavier chalcogen. Confirm the two share a site before treating this as a substitution axis.
- measured range: 300-874 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn3Sn3(TeO8)2 Cm (8) mp-772482 [hull=0.060, PRIMARY]
- papers: https://doi.org/10.1021/acs.chemmater.9b00747 (Facile Route to High-Performance SnTe-Based Thermoelectric Materials: ...)

## Mn-O-Tb
- rank 1473 | 4 samples | 1 papers | 4 compositions
- compositions: Tb0.95Al0.05MnO3 (1); Tb0.9Al0.1MnO3 (1); TbMnO3 (1); Tb0.8Al0.2MnO3 (1)
- dopant candidates (<5% at.): Al (3)
- sample form: Bulk (4)
- measured range: 10-379 K (5th-95th pct of 14 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TbMnO3 Pnma (62) mp-25030 [hull=0.000, icsd=5, PRIMARY]; TbMn2O5 Pbam (55) mp-25028 [hull=0.000, icsd=1, PRIMARY]; Tb2Mn2O7 Fd-3m (227) mp-769812 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2015.08.195 (Effect of the Al-doping on the electrical and thermoelectric response ...)

## Mn-O-Zn
- rank 1474 | 4 samples | 2 papers | 2 compositions
- compositions: Zn0.89Mn0.1Al0.01O (2); Zn0.88Mn0.12O (2)
- dopant candidates (<5% at.): Al (2)
- sample form: Bulk (1)
- measured range: 107-1020 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn2ZnO4 I4_1/amd (141) mp-18751 [hull=0.000, icsd=3, PRIMARY]; Mn3ZnO10 R-3 (148) mp-1193234 [hull=0.315, icsd=3, PRIMARY]; Mn3ZnO7 R-3 (148) mp-1192094 [hull=0.000, icsd=1, PRIMARY]; Mn11ZnO16 C222 (21) mp-861549 [hull=0.005, PRIMARY]; Mn6Zn3O16 P2_1 (4) mp-774014 [hull=0.063, PRIMARY]
- papers: https://doi.org/10.2109/jcersj2.15282 (Sintering characteristics and thermoelectric properties of Mn&ndash;Al...) | https://doi.org/10.1063/1.2402097 (An electron paramagnetic resonance study of n-type Zn1−xMnxO: A dilute...)

## Mn-Pb-Sn-Te
- rank 1475 | 4 samples | 2 papers | 4 compositions
- compositions: Pb0.60Mn0.15Sn0.25Te1.00 (1); Pb0.65Mn0.10Sn0.25Te1.00 (1); (Sn0.8Pb0.2)0.88Mn0.12Te (1); (Sn0.8Pb0.2)0.85Mn0.15Te (1)
- sample form: Bulk (2)
- solid-solution axis: Pb/(Pb+Sn) spans 0.20-0.72 (median 0.71) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 295-725 K (5th-95th pct of 16 curves)
- papers: https://doi.org/10.1016/j.mssp.2015.02.053 (Thermoelectric properties of Pb0.75−xMnxSn0.25Te alloys with variable ...) | https://doi.org/10.1007/s11664-016-4352-5 (Enhanced Thermoelectric Properties of Sn0.8Pb0.2Te Alloy by Mn Substit...)

## Mo-Nd-O
- rank 1476 | 4 samples | 2 papers | 3 compositions
- compositions: (Nd0.8Er0.2)2Mo2O7 (2); (Nd0.95Yb0.05)2Mo2O7 (1); (Nd0.9Yb0.1)2Mo2O7 (1)
- dopant candidates (<5% at.): Er (2), Yb (2)
- sample form: Bulk (2)
- measured range: 11-301 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd2Mo2O7 I4_1/a (88) mp-690122 [hull=0.000, icsd=1, PRIMARY]; KLiNd2(MoO4)4 C2/c (15) mp-636225 [hull=0.000, icsd=1, PRIMARY]; BaNd2(MoO4)4 C2/c (15) mp-622521 [hull=0.005, icsd=1, PRIMARY]; RbLiNd2(MoO4)4 C2/c (15) mp-630867 [hull=0.000, icsd=1, PRIMARY]; LiNd2Tl(MoO4)4 C2/c (15) mp-630880 [hull=0.007, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0022-3697(86)90030-2 (Thermoelectric power of RE2Mo2O7 pyrochlores) | https://doi.org/10.1016/0025-5408(80)90094-x (Electrical properties of Ln2Mo2O7 pyrochlores (Ln=SmYb,Y))

## Mo-Pd-Rh-Ru
- rank 1477 | 4 samples | 1 papers | 4 compositions
- compositions: Mo35Ru31Rh9Pd25 (1); Mo30Ru43Rh14Pd13 (1); Mo20Ru54Rh15Pd11 (1); Mo43Ru34Rh12Pd11 (1)
- sample form: Bulk (1)
- measured range: 286-1273 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MoPdRuRh P3m1 (156) mp-1221443 [hull=0.089, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(02)01211-2 (Thermophysical properties of Mo–Ru–Rh–Pd alloys)

## Mo-Se
- rank 1478 | 4 samples | 4 papers | 3 compositions
- compositions: Mo6Se8 (2); Mo3Se4 (1); MoSe2 (1)
- sample form: Bulk (1)
- measured range: 101-1088 K (5th-95th pct of 7 curves)
- [ref 1] TEDesignLab / ICSD: MoSe2 P6_3/mmc (194) mp-1634 [hull=0.000, icsd=7, PRIMARY]; Mo9Se11 Cmcm (63) mp-299 [hull=0.083, icsd=2, PRIMARY]; MoSe2 R3m (160) mp-7581 [hull=0.000]
- [ref 2] MP, ranked by ICSD evidence: Mo3Se4 R-3 (148) mp-21021 [hull=0.064, icsd=7, PRIMARY]; Co(Mo3Se4)4 P1 (1) mp-675208 [hull=0.076, PRIMARY]; LaMo12PbSe16 R-3 (148) mp-1223020 [hull=0.038, PRIMARY]; Mo3Se Pm-3n (223) mp-1206038 [hull=0.588, PRIMARY]; Mo9Se11 P6_3/m (176) mp-638048 [hull=0.068, icsd=1]
- papers: https://doi.org/10.1016/j.jssc.2006.04.022 (Thermoelectric and structural properties of a new Chevrel phase: Ti0.3...) | https://doi.org/10.1109/ict.2003.1287497 (Thermoelectric properties of Mo/sub 6/Se/sub 8/-based chevrel phase wi...) | https://doi.org/10.1016/s0925-8388(01)01791-1 (Thermoelectric properties of Mo3Te4)

## N-Nb-O
- rank 1479 | 4 samples | 2 papers | 2 compositions
- compositions: NbON0.17 (2); Nb0.36Ru0.04O0.52N0.07 (2)
- dopant candidates (<5% at.): Ru (2)
- sample form: Film (2)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 333-1277 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NbNO P2_1/c (14) mp-7596 [hull=0.000, icsd=3, PRIMARY]; Nb10N11O Pc (7) mp-1173557 [hull=0.040, PRIMARY]; Nb40(NO)17 R3m (160) mp-676894 [hull=0.459, PRIMARY]; Nb27N37O3 Cm (8) mp-1173578 [hull=0.109, PRIMARY]; Nb40N21O16 P1 (1) mp-685674 [hull=0.408, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/27/11/115501 (Vacancy filling effect in thermoelectric NbO) | https://doi.org/10.1016/j.physb.2015.10.001 (Enhanced thermoelectric performance of amorphous Nb based oxynitrides)

## N-Nb-O-Ru
- rank 1480 | 4 samples | 1 papers | 2 compositions
- compositions: Nb0.38Ru0.06O0.48N0.07 (2); Nb0.29Ru0.07O0.58N0.06 (2)
- sample form: Film (2)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 334-927 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1016/j.physb.2015.10.001 (Enhanced thermoelectric performance of amorphous Nb based oxynitrides)

## N-O-Zn
- rank 1481 | 4 samples | 1 papers | 2 compositions
- compositions: ZnO0.42N0.30 (2); ZnO0.48N0.27 (2)
- measured range: 11-297 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zn(NO6)2 Pnma (62) mp-1197468 [hull=0.635, icsd=1, PRIMARY]; Zn(NO4)2 P2_1/c (14) mp-1190906 [hull=0.329, icsd=1, PRIMARY]; Zn5(N2O7)2 C2/m (12) mp-1190627 [hull=0.900, icsd=1, PRIMARY]; Zn3(NO5)2 P2_1/c (14) mp-1198332 [hull=0.206, icsd=1, PRIMARY]; Zn5(NO8)2 C2/m (12) mp-1191296 [hull=0.400, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.5089679 (Thermoelectric properties of amorphous ZnOxNy thin films at room tempe...)

## Na-Nb-O-Sr
- rank 1482 | 4 samples | 1 papers | 4 compositions
- compositions: Na0.5Sr0.5NbO3 (1); Na0.7Sr0.3NbO3 (1); Na0.6Sr0.4NbO3 (1); Na0.4Sr0.6NbO3 (1)
- measured range: 15-277 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NaSr3NbO6 R-3c (167) mp-6361 [hull=0.000, icsd=2, PRIMARY]; Na2Sr2Nb4O13 Imm2 (44) mp-1221316 [hull=0.108, PRIMARY]; NaSr2Nb5O15 Cmm2 (35) mp-1220952 [hull=0.054, PRIMARY]; NaSrNb2O6 Cmmm (65) mp-1220869 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/0038-1098(84)90351-x (Conduction mechanism in polycrystalline Na1−xSrxNbO3 niobium bronzes)

## Na-Pb-S
- rank 1483 | 4 samples | 1 papers | 4 compositions
- compositions: Pb0.98Na0.2S (1); Pb0.975Na0.25S (1); Pb0.97Na0.3S (1); Pb0.96Na0.4S (1)
- measured range: 302-733 K (5th-95th pct of 20 curves)
- papers: https://doi.org/10.1021/ja301772w (Thermoelectrics with Earth Abundant Elements: High Performance p-type ...)

## Nb-Si
- rank 1484 | 4 samples | 1 papers | 1 compositions
- compositions: NbSi2 (4)
- measured range: 178-635 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NbSi2 P6_222 (180) mp-2478 [hull=0.000, icsd=9, PRIMARY]; Nb5Si3 I4/mcm (140) mp-13686 [hull=0.000, icsd=5, PRIMARY]; Nb3Si P4_2/n (86) mp-17848 [hull=0.017, icsd=3, PRIMARY]; Nb3Si2 P4/mbm (127) mp-1078996 [hull=0.019, icsd=1, PRIMARY]; Nb3Si Pm-3n (223) mp-10229 [hull=0.097, icsd=3]
- papers: https://doi.org/10.1088/0022-3727/23/3/015 (Electrical transport properties of NbSi<sub>2</sub>thin films)

## Nd-O-Pd
- rank 1485 | 4 samples | 1 papers | 1 compositions
- compositions: Nd2PdO4 (4)
- measured range: 10-282 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd(PdO2)2 I4_1/a (88) mp-15051 [hull=0.000, icsd=1, PRIMARY]; Nd4PdO7 P-1 (2) mp-29791 [hull=0.007, icsd=1, PRIMARY]; Nd2Pd2O5 P4_2/m (84) mp-1209848 [hull=0.000, PRIMARY]; Nd2PdO4 I4/mmm (139) mp-1025319 [hull=0.369, PRIMARY]; Nd2PdO4 Fd-3m (227) mp-1210248 [hull=0.487]
- papers: https://doi.org/10.1063/1.4994043 (Molecular beam epitaxy of Nd2PdO4 thin           films)

## Nd-O-Sb-Se
- rank 1486 | 4 samples | 1 papers | 2 compositions
- compositions: NdO0.8F0.2SbSe2 (2); NdO0.8F0.2Sb0.8As0.2Se2 (2)
- dopant candidates (<5% at.): F (4), As (2)
- measured range: 298-672 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.3390/ma13092164 (Crystal Structure and Thermoelectric Transport Properties of As-Doped ...)

## Nd-O-Ti
- rank 1487 | 4 samples | 3 papers | 4 compositions
- compositions: Nd0.8Ca0.2TiO3 (1); Nd0.9Ca0.1TiO3 (1); Nd0.6Sr0.1TiO3 (1); Ba3.45Nd9.7Ti18O54 (1)
- dopant candidates (<5% at.): Ca (2), Sr (1), Ba (1)
- sample form: Bulk (2)
- measured range: 81-1079 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd2TiO5 Pnma (62) mp-17904 [hull=0.000, icsd=4, PRIMARY]; Nd2Ti2O7 P2_1 (4) mp-12193 [hull=0.000, icsd=3, PRIMARY]; NdTiO3 Pnma (62) mp-3119 [hull=0.042, icsd=3, PRIMARY]; Nd2Ti4O11 C2/c (15) mp-654139 [hull=0.000, icsd=1, PRIMARY]; Nd11Ti16O48 Amm2 (38) mp-1173643 [hull=0.095, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2003.11.021 (Band filling dependence of the electrical transport of Nd1−xAxTiO3 (A=...) | https://doi.org/10.1007/s11664-014-3058-9 (Neodymium-Strontium Titanate: A New Ceramic for an Old Problem) | https://doi.org/10.1007/s11664-015-4275-6 (Ba6−3x Nd8+2x Ti18O54 Tungsten Bronze: A New High-Temperature n-Type O...)

## Ni-O-Y
- rank 1488 | 4 samples | 1 papers | 1 compositions
- compositions: YNiO3 (4)
- measured range: 219-483 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YNiO3 Pnma (62) mp-19242 [hull=0.000, icsd=3, PRIMARY]
- papers: https://doi.org/10.1021/acsami.9b12609 (A d-Band Electron Correlated Thermoelectric Thermistor Established in ...)

## Ni-P-Si
- rank 1489 | 4 samples | 1 papers | 4 compositions
- compositions: NiSi2.98B0.02P4 (1); NiSi2.9B0.1P4 (1); NiSi2.8B0.2P4 (1); NiSi3P4 (1)
- dopant candidates (<5% at.): B (3)
- sample form: Bulk (4)
- measured range: 10-795 K (5th-95th pct of 32 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Si2Ni5P3 Pbca (61) mp-649521 [hull=0.055, icsd=1, PRIMARY]; Si2NiP3 Imm2 (44) mp-28945 [hull=0.002, icsd=1, PRIMARY]; Si3NiP4 I-42m (121) mp-8311 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.4794992 (Thermoelectric properties of polycrystalline NiSi3P4)

## O
- rank 1490 | 4 samples | 2 papers | 4 compositions
- compositions: CeTiO33.1 (1); SrCo0.8Nb0.1NiO30.1 (1); SrCo0.7Nb0.1NiO30.2 (1); SrCo0.6Nb0.1NiO30.3 (1)
- dopant candidates (<5% at.): Sr (3), Ni (3), Co (3), Nb (3), Ce (1), Ti (1)
- sample form: rod-shaped (3)
- measured range: 19-1073 K (5th-95th pct of 5 curves)
- [ref 1] TEDesignLab / ICSD: O2 C2/m (12) mp-12957 [hull=0.000, icsd=5, PRIMARY]; O2 (61)
- [ref 2] MP, ranked by ICSD evidence: O2 R-3m (166) mp-610917 [hull=0.024, icsd=5]; O2 Fd-3m (227) mp-1057818 [hull=1.954, icsd=4]; O2 P4_12_12 (92) mp-1091399 [hull=0.007, icsd=1]; O2 C2/c (15) mp-1087546 [hull=0.032, icsd=1]; O2 Fmmm (69) mp-607540 [hull=0.112, icsd=1]
- papers: https://doi.org/10.1088/0953-8984/9/26/010 (Electronic states of perovskite-type and systems with a metal - insula...) | https://doi.org/10.1039/c9se01096c (A highly active and stable cathode for oxygen reduction in intermediat...)

## O-Pr-Zr
- rank 1491 | 4 samples | 2 papers | 1 compositions
- compositions: Pr2Zr2O7 (4)
- measured range: 293-873 K (5th-95th pct of 4 curves; full span incl. outliers 293-1072 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrZrO14 Fd-3m (227) mp-1210241 [hull=0.619, PRIMARY]
- papers: https://doi.org/10.31349/revmexfis.67.255 (Electrical and thermal conductivities of rare-earth A2Zr2O7 (A = Pr, N...) | https://doi.org/10.1016/j.jeurceramsoc.2020.06.027 (Thermal and oxygen transport properties of complex pyrochlore RE2InTaO...)

## O-Rh-Zn
- rank 1492 | 4 samples | 2 papers | 4 compositions
- compositions: Li0.25Zn0.5Rh2O4 (1); Zn0.5Rh2O4 (1); ZnRh2O4 (1); ZnRh1.8Mg0.2O4 (1)
- dopant candidates (<5% at.): Li (1), Mg (1)
- sample form: Film (2)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 11-873 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zn(RhO2)2 Fd-3m (227) mp-5146 [hull=0.000, icsd=2, PRIMARY]; ZnRhO3 Pm-3m (221) mp-1016880 [hull=0.766, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2012.03.054 (Synthesis and thermoelectric properties of the novel A-site deficient ...) | https://doi.org/10.1109/ict.2007.4569441 (Mg substitution effects of new thermoelectric Rh oxides)

## O-Sc-W
- rank 1493 | 4 samples | 1 papers | 1 compositions
- compositions: Sc0.67WO4 (4)
- measured range: 19-304 K (5th-95th pct of 4 curves; full span incl. outliers 19-598 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sc2(WO4)3 Pbcn (60) mp-19588 [hull=0.008, icsd=5, PRIMARY]; Sc2(WO4)3 P2/c (13) mp-1219450 [hull=0.025]
- papers: https://doi.org/10.1016/j.jssc.2010.04.039 (High-pressure synthesis, crystal and electronic structures of a new sc...)

## O-Si-Zn
- rank 1494 | 4 samples | 1 papers | 4 compositions
- compositions: (ZnO)4.2(SiO2)3.3 (1); (ZnO)4.9(SiO2)3.3 (1); (ZnO)5.6(SiO2)3.3 (1); (ZnO)6.3(SiO2)3.3 (1)
- measured range: 73-296 K (5th-95th pct of 4 curves)
- [ref 1] TEDesignLab / ICSD: Zn2SiO4 Pnma (62) mp-1020594 [hull=0.010, icsd=1]; Zn2SiO4 Pbca (61) mp-1020636 [hull=0.052, icsd=1]; Zn2SiO4 P2_1/c (14) mp-1020721 [hull=0.111, icsd=1]; Zn2SiO4 Imma (74) mp-1020717 [hull=0.122, icsd=1]; ZnSiO3 R-3 (148) mp-1020623 [hull=0.148, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: Zn2SiO5 Imm2 (44) mp-1189355 [hull=0.435, icsd=6, PRIMARY]; Zn2SiO4 R-3 (148) mp-3789 [hull=0.000, icsd=5, PRIMARY]; ZnSiO3 Pbca (61) mp-619034 [hull=0.054, icsd=2, PRIMARY, AMBIGUOUS]; Zn4Si2O9 Imm2 (44) mp-1103526 [hull=0.147, icsd=2, PRIMARY]; KMn2Zn3(Si2O5)6 P6cc (184) mp-704116 [hull=0.018, icsd=1, PRIMARY]
- papers: https://doi.org/10.1134/s106378261911023x (Structure and Electrical Properties of (ZnO/SiO2)25 Thin Films)

## O-Sm
- rank 1495 | 4 samples | 2 papers | 1 compositions
- compositions: SmO (4)
- measured range: 12-298 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sm2O3 Ia-3 (206) mp-218 [hull=0.000, icsd=10, PRIMARY]; SmO Fm-3m (225) mp-1611 [hull=0.112, icsd=2, PRIMARY]; SmO2 P2_1/m (11) mp-1077235 [hull=0.152, icsd=1, PRIMARY]; SmO3 P6_3/m (176) mp-1025421 [hull=0.420, icsd=1, PRIMARY]; Sm2O I4_1/amd (141) mp-33104 [hull=0.070, PRIMARY]
- papers: https://doi.org/10.1016/0375-9601(80)90035-3 (Transport properties of SmO) | https://doi.org/10.1103/physrevb.95.125111 (Samarium monoxide epitaxial thin film as a possible heavy-fermion comp...)

## O-Zn-Zr
- rank 1496 | 4 samples | 1 papers | 1 compositions
- compositions: (Zn0.993Al0.007O)85.86(ZrO2)14.14 (4)
- dopant candidates (<5% at.): Al (4)
- sample form: Bulk (2)
- measured range: 423-1223 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZrZnO3 Pm-3m (221) mp-1016883 [hull=0.759, PRIMARY]
- papers: https://doi.org/10.1039/c8ta01463a (A self-forming nanocomposite concept for ZnO-based thermoelectrics)

## P-Zn
- rank 1497 | 4 samples | 2 papers | 1 compositions
- compositions: Zn3P2 (4)
- sample form: Film (2)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 79-793 K (5th-95th pct of 5 curves)
- [ref 1] TEDesignLab / ICSD: ZnP2 P4_12_12 (92) mp-2782 [hull=0.000, icsd=4, PRIMARY]; ZnP4 P4_12_12 (92) mp-14587 [hull=0.061, icsd=1, PRIMARY]; ZnP2 P2_1/c (14) mp-1392 [hull=0.003, icsd=3]; ZnP2 P4_32_12 (96) mp-11025 [hull=0.000, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: Zn3P2 P4_2/nmc (137) mp-2071 [hull=0.000, icsd=8, PRIMARY]; Zn3P Pm-3m (221) mp-1187918 [hull=0.301, PRIMARY]; Zn2P Pn-3m (224) mp-1207457 [hull=0.397, PRIMARY]; ZnP P6_3mc (186) mp-971863 [hull=0.320, PRIMARY]; Zn3P2 Ia-3 (206) mp-1197170 [hull=0.027, icsd=1]
- papers: https://doi.org/10.1016/j.jallcom.2016.06.145 (Low thermal conductivity in nanocrystalline Zn 3 P 2) | https://doi.org/10.1063/1.341744 (Electrical and thermoelectrical properties of Zn3P2films grown by the ...)

## Pb
- rank 1498 | 4 samples | 4 papers | 2 compositions
- compositions: Pb (3); Pb99.975TeNa0.025 (1)
- dopant candidates (<5% at.): Te (1), Na (1)
- measured range: 20-550 K (5th-95th pct of 5 curves; full span incl. outliers 20-688 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Pb Fm-3m (225) mp-20483 [hull=0.000, icsd=14, PRIMARY]; Pb P6_3/mmc (194) mp-1186444 [hull=0.016, icsd=3]; Pb Im-3m (229) mp-22692 [hull=0.047, icsd=1]; Pb R-3m (166) mp-1057273 [hull=0.069, icsd=1]; Pb I4/mcm (140) mp-1102666 [hull=0.081, icsd=1]
- papers: https://doi.org/10.1063/1.1663273 (Thermal conductivity, electrical resistivity, and thermoelectric power...) | https://doi.org/10.1063/1.353016 (Thin gold wires as reference for thermoelectric power measurements of ...) | https://doi.org/10.1063/1.4974049 (Heavy hole effect on the thermoelectric properties of highly doped p-t...)

## Pd-Sb-Y
- rank 1499 | 4 samples | 4 papers | 1 compositions
- compositions: YPdSb (4)
- sample form: Bulk (1)
- measured range: 12-398 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y3(SbPd2)4 Fm-3m (225) mp-1207804 [hull=0.000, PRIMARY]; Y5SbPd2 I4/mcm (140) mp-1207717 [hull=0.000, PRIMARY]; YSbPd F-43m (216) mp-1215892 [hull=0.532, PRIMARY]; YSbPd2 Fm-3m (225) mp-865513 [hull=0.000, PRIMARY]; YSbPd2 P4/mmm (123) mp-1215895 [hull=0.188]
- papers: https://doi.org/10.1088/0953-8984/15/4/304 (Thermoelectrical properties of the compounds ScMVIIISb and YMVIIISb (M...) | https://doi.org/10.1109/ict.2005.1519966 (Physical properties of rare-earth-based Heusler phases REPdZ and REPd/...) | https://doi.org/10.1103/physrevb.72.094409 (Magnetic and transport properties of the rare-earth-based Heusler phas...)

## Ru-Si
- rank 1500 | 4 samples | 3 papers | 2 compositions
- compositions: Ru2Si3 (3); Ru2Si3Mn0.01 (1)
- dopant candidates (<5% at.): Mn (1)
- measured range: 11-872 K (5th-95th pct of 8 curves; full span incl. outliers 11-1268 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Si3Ru2 Pbcn (60) mp-22192 [hull=0.000, icsd=5, PRIMARY]; SiRu P2_13 (198) mp-1078867 [hull=0.000, icsd=4, PRIMARY]; SiRu2 Pnma (62) mp-10025 [hull=0.029, icsd=2, PRIMARY]; Si2Ru P4/mmm (123) mp-7754 [hull=0.127, icsd=1, PRIMARY]; Si3Ru5 Pbam (55) mp-1105935 [hull=0.033, icsd=1, PRIMARY]
- papers: https://doi.org/10.1109/ict.2003.1287473 (Thermoelectric properties of Mn-doped Ru/sub 2/Si/sub 3/) | https://doi.org/10.1016/s0022-0248(02)01686-x (Floating zone growth and characterization of semiconducting Ru2Si3 sin...) | https://doi.org/10.1063/1.40139 (A promising new thermoelectric material: Ruthenium silicide)
