# Host systems -- chunk 012 of 73

Ranks 551-600 by sample count. These 50 host systems cover 581 samples (1.12% of the TE set); cumulative through this chunk: 82.86%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Bi-C-Sb-Te
- rank 551 | 12 samples | 3 papers | 4 compositions
- compositions: Bi0.5Sb1.5Te3C0.28 (9); Bi0.5Sb1.5Te3C0.4 (1); Bi0.4Sb1.6Te3C0.5 (1); Bi0.5Sb1.5Te3C0.34 (1)
- seed hypothesis (confirm): composite_multiphase
- curator composition details (from the paper): V/V % (1); 1%CNT/Bi0.4Sb1.6Te3 (1)
- sample form: Bulk (11)
- measured range: 25-576 K (5th-95th pct of 53 curves)
- papers: https://doi.org/10.1002/pssa.201127075 (C60-doping of nanostructured Bi-Sb-Te thermoelectrics) | https://doi.org/10.1063/1.4834700 (Thermoelectric and mechanical properties of multi-walled carbon nanotu...) | https://doi.org/10.1002/adfm.202008851 (Significant Enhancement of Thermoelectric Figure of Merit in BiSbTe‐Ba...)

## Bi-Co-Zr
- rank 552 | 12 samples | 4 papers | 10 compositions
- compositions: ZrCoBi (3); ZrCo0.9Ni0.1Bi (1); ZrCo0.95Ni0.05Bi (1); Zr6CoBi2 (1); ZrCo0.97Pd0.03Bi (1); ZrCo0.91Pd0.09Bi (1)
- dopant candidates (<5% at.): Pd (3), Sn (3), Ni (2)
- sample form: Bulk (8); Other (4)
- measured range: 13-985 K (5th-95th pct of 47 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZrCoBi F-43m (216) mp-31451 [hull=0.000, icsd=1, PRIMARY]; Zr6CoBi2 P-62m (189) mp-1206046 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1007/s11664-007-0153-1 (Thermoelectric Properties of Half-Heusler Bismuthides ZrCo1−x Ni x Bi ...) | https://doi.org/10.1016/s0925-8388(99)00537-x (Thermoelectric properties of ternary transition metal antimonides) | https://doi.org/10.3390/ma11050728 (Synthesis and Thermoelectric Properties of Pd-Doped ZrCoBi Half-Heusle...)

## Bi-Cu-S
- rank 553 | 12 samples | 2 papers | 11 compositions
- compositions: Cu4Bi4S9 (2); Cu1.6Bi4.577Zn0.023S8 (1); Cu1.592Zn0.008Bi4.6S8 (1); Cu1.6Bi4.6S7.96Se0.04 (1); Cu1.576Zn0.024Bi4.6S8 (1); Cu1.576In0.024Bi4.6S8 (1)
- dopant candidates (<5% at.): Zn (4), In (4), Se (1)
- seed hypothesis (confirm): bi_chalcogenide_complex
- sample form: Bulk (2)
- measured range: 292-673 K (5th-95th pct of 60 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuBiS2 Pnma (62) mp-22982 [hull=0.000, icsd=4, PRIMARY]; Cu4Bi5PbS11 C2/m (12) mp-672295 [hull=0.030, icsd=1, PRIMARY]; Cu4(BiS2)5 C2/m (12) mp-27124 [hull=0.008, icsd=1, PRIMARY]; Cu6AgBi12PbS22 P2_1/m (11) mp-651706 [hull=0.024, icsd=1, PRIMARY]; Cu4Bi4S9 Pnma (62) mp-683991 [hull=0.033, PRIMARY]
- papers: https://doi.org/10.1039/c5ce02143j (Importance of crystal chemistry with interstitial site determining the...) | https://doi.org/10.1021/acsami.9b11115 (Cu4Bi4Se9: A Thermoelectric Symphony of Rattling, Anharmonic Lone-pair...)

## C-Co-Sb
- rank 554 | 12 samples | 4 papers | 11 compositions
- compositions: CoSb3C0.5 (2); CoSb3C0.35 (1); CoSb3C0.46 (1); CoSb3C0.57 (1); CoSb3C0.8 (1); Ba0.25Co4Sb12.07(BaC60)0.03 (1)
- dopant candidates (<5% at.): Ba (5), Ni (1), Te (1)
- curator composition details (from the paper): CoSb3/G because the graphene content is estimated to be only 1.5 wt% (1); CoSb3/graphene mixture (CoSb3 + G) was obtained by grinding bare CoSb3 and graphene with a... (1)
- sample form: Bulk (6)
- measured range: 24-854 K (5th-95th pct of 59 curves)
- papers: https://doi.org/10.1063/1.1687997 (Enhanced thermoelectric figure of merit of CoSb3 via large-defect scat...) | https://doi.org/10.1063/1.2811936 (Influence of fullerene dispersion on high temperature thermoelectric p...) | https://doi.org/10.1039/c3ta13202a (Enhanced thermoelectric properties of p-type CoSb3/graphene nanocomposite)

## Ca-Cu-O-Ru-Ti
- rank 555 | 12 samples | 2 papers | 7 compositions
- compositions: CaCu3Ti2.5Ru1.5O12 (3); CaCu3Ti3RuO12 (2); CaCu3Ti2Ru2O12 (2); CaCu3Ti1.5Ru2.5O12 (2); CaCu3TiRu3O12 (1); CaCu3Ti3Ru1O12 (1)
- seed hypothesis (confirm): cacu3ti4o12
- curator composition details (from the paper): polycrystalline (5)
- measured range: 11-298 K (5th-95th pct of 13 curves)
- papers: https://doi.org/10.1016/j.progsolidstchem.2007.01.013 (Thermoelectric properties of the AA′3B4O12-type ordered perovskite oxides) | https://doi.org/10.1103/physrevb.95.195141 (Electronic phase transition between localized and itinerant states in ...)

## Ca-Fe-O-Ti
- rank 556 | 12 samples | 2 papers | 2 compositions
- compositions: CaTi0.7Fe0.3O3 (11); CaTi0.5Fe0.5O3 (1)
- measured range: 294-1482 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaTi2FeO6 P4_2/nmc (137) mp-1200872 [hull=0.065, icsd=1, PRIMARY]; Ca3Ti(FeO4)2 P2_1 (4) mp-1227734 [hull=0.000, PRIMARY]; Ca4Ti3FeO12 P2/m (10) mp-1227247 [hull=0.022, PRIMARY]; CaTi4(FeO4)3 Im-3 (204) mp-24950 [hull=0.030, PRIMARY]
- papers: https://doi.org/10.1021/acsanm.2c04537 (Nanoscale Iron Redistribution during Thermochemical Decomposition of C...) | https://doi.org/10.1007/bf02430388 (Resistivity relaxation, a new approach to study ionic mobility in pero...)

## Ca-Ir-O
- rank 557 | 12 samples | 4 papers | 1 compositions
- compositions: CaIrO3 (12)
- seed hypothesis (confirm): perovskite, post_perovskite  <-- MIXED, split per composition
- sample form: rod-shaped (1)
- measured range: 10-1023 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaIrO3 Cmcm (63) mp-4243 [hull=0.000, icsd=18, PRIMARY]; Ca4IrO6 R-3c (167) mp-4100 [hull=0.023, icsd=2, PRIMARY]; Ca15Ni(IrO6)4 P2 (3) mp-1227837 [hull=0.033, PRIMARY, AMBIGUOUS]; Ca7Ni(IrO6)2 R32 (155) mp-1227125 [hull=0.045, PRIMARY]; CaIrO3 Pm-3m (221) mp-1016872 [hull=0.314]
- papers: https://doi.org/10.1063/1.4921460 (Persistent semi-metal-like nature of epitaxial perovskite CaIrO<sub>3<...) | https://doi.org/10.2109/jcersj2.117.466 (Thermoelectricity of CaIrO3 ceramics prepared by spark plasma sintering) | https://doi.org/10.1063/1.5129235 (Contrasted Sn substitution effects on Dirac line node semimetals SrIrO...)

## Ca-La-Rh-Sn
- rank 558 | 12 samples | 1 papers | 1 compositions
- compositions: Ca1.5La1.5Rh4Sn13 (12)
- papers: https://doi.org/10.1088/1367-2630/aae4a8 (The effective increase in atomic scale disorder by doping and supercon...)

## Cd-Eu-Sb-Zn
- rank 559 | 12 samples | 4 papers | 12 compositions
- compositions: Eu11Cd4.5Zn1.5Sb12 (1); Eu11Cd1.6Zn4.4Sb12 (1); EuZnCdSb2 (1); EuZn1.4Cd0.6Sb2 (1); Eu(Zn0.7Cd0.3)2Sb2 (1); Eu(Zn0.5Cd0.5)2Sb2 (1)
- seed hypothesis (confirm): zintl_11_6_12
- sample form: Bulk (6); Other (2)
- solid-solution axis: Cd/(Cd+Zn) spans 0.27-0.85 (median 0.65) over 12 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 298-773 K (5th-95th pct of 55 curves)
- papers: https://doi.org/10.1021/acs.chemmater.5b01301 (High Temperature Thermoelectric Properties of the Solid-Solution Zintl...) | https://doi.org/10.1039/b916346h (Thermoelectric properties of Eu(Zn1−xCdx)2Sb2) | https://doi.org/10.1016/s1002-0721(12)60398-6 (Zintl phase compounds AM2Sb2 (A=Ca, Sr, Ba, Eu, Yb; M=Zn, Cd) and thei...)

## Ce-Co-Ge
- rank 560 | 12 samples | 5 papers | 11 compositions
- compositions: CeCo2Ge2 (2); CeCoGe3 (1); Ce5Co4Ge13 (1); Ce2Co3Ge5 (1); Ce2CoGe3 (1); CeCo0.86Ge2 (1)
- dopant candidates (<5% at.): Fe (1)
- sample form: Bulk (3); Polycrystal (2)
- measured range: 10-301 K (5th-95th pct of 21 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(CoGe)2 I4/mmm (139) mp-20933 [hull=0.000, icsd=4, PRIMARY]; CeCoGe3 I4mm (107) mp-21116 [hull=0.000, icsd=3, PRIMARY]; CeCoGe2 Cmcm (63) mp-1079178 [hull=0.000, icsd=2, PRIMARY]; Ce2Co3Ge5 Ibam (72) mp-1188584 [hull=0.000, icsd=1, PRIMARY]; CeCoGe P4/nmm (129) mp-21339 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2011.03.033 (Magnetic, electric and thermoelectric properties of ternary intermetal...) | https://doi.org/10.1016/j.intermet.2014.03.021 (Magnetic and related properties of Ce5CoGe2, CeCoGe and CeCo2Ge2) | https://doi.org/10.1088/0953-8984/26/25/255601 (Electrical and thermal transport properties of intermetallicRCoGe2(R= ...)

## Ce-Rh-Sn
- rank 561 | 12 samples | 3 papers | 8 compositions
- compositions: CeRhSn (5); CeRh0.95Ni0.05Sn (1); CeRh0.9Ni0.1Sn (1); CeRh0.95Co0.05Sn (1); CeRh0.95Ru0.05Sn (1); CeRh0.9Ru0.1Sn (1)
- dopant candidates (<5% at.): Ni (2), Co (2), Ru (2)
- seed hypothesis (confirm): crb_feb_chain
- sample form: Bulk (9); SingleCrystal (2)
- measured range: 10-302 K (5th-95th pct of 20 curves; full span incl. outliers 10-486 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce3Sn13Rh4 Pm-3n (223) mp-7203 [hull=0.000, icsd=4, PRIMARY]; CeSnRh P-62m (189) mp-12374 [hull=0.000, icsd=3, PRIMARY]; Ce(Sn2Rh)2 Pnma (62) mp-1193462 [hull=0.000, icsd=1, PRIMARY]; Ce(SnRh)2 P4/nmm (129) mp-1079827 [hull=0.046, icsd=1, PRIMARY]; Ce5(Sn5Rh2)2 P4/mbm (127) mp-1199090 [hull=0.030, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(00)01176-2 (Large thermoelectric power in several metallic compounds of cerium and...) | https://doi.org/10.1016/s0921-4526(02)02235-4 (Thermoelectric and magnetic properties of CeRh1$minus;xMxSn (M=Co, Ni,...) | https://doi.org/10.1143/jjap.42.6512 (Thermoelectric Properties of Single-Crystal CeRhSn with Valence Fluctu...)

## Co-Fe-Sb-Yb
- rank 562 | 12 samples | 6 papers | 5 compositions
- compositions: Yb0.9Fe3CoSb12 (5); Yb0.9Fe3 CoSb12 (4); Yb0.85La0Fe2.7Co1.3Sb12 (1); Yb0.85Fe3CoSb12 (1); Yb0.90Fe3CoSb12 (1)
- sample form: Bulk (5)
- measured range: 299-824 K (5th-95th pct of 52 curves)
- papers: https://doi.org/10.1016/j.intermet.2012.08.005 (Thermoelectric properties of p-type YbxLayFe2.7Co1.3Sb12 double-filled...) | https://doi.org/10.1007/s11664-012-2253-9 (Preparation and Thermoelectric Properties of p-Type Yb-Filled Skutteru...) | https://doi.org/10.3938/jkps.63.1764 (Effects of heat treatment on the thermoelectric properties of Yb-fille...)

## Co-Mg-O
- rank 563 | 12 samples | 1 papers | 12 compositions
- compositions: Co34(MgO)66 (1); Co36(MgO)64 (1); Co39(MgO)61 (1); Co42(MgO)58 (1); Co47(MgO)53 (1); Co50(MgO)50 (1)
- seed hypothesis (confirm): rocksalt_oxide
- measured range: 15-302 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg(CoO2)4 F-43m (216) mp-1222210 [hull=0.126, PRIMARY]; Mg2Co2O5 Ima2 (46) mp-1076088 [hull=0.183, PRIMARY]; Mg2Co7O12 P1 (1) mp-761510 [hull=0.056, PRIMARY]; Mg2CoO4 Fd-3m (227) mp-769655 [hull=0.063, PRIMARY]; Mg3CoO4 Pm-3m (221) mp-1099254 [hull=0.107, PRIMARY]
- papers: https://doi.org/10.1088/1361-648x/aa8315 (Skew scattering dominated anomalous Hall effect in Co<sub> <i>x</i> </...)

## Co-Ni-Sb-Ti
- rank 564 | 12 samples | 4 papers | 12 compositions
- compositions: TiCo0.8Ni0.2Sb (1); TiCo0.6Ni0.4Sb (1); TiCo0.4Ni0.6Sb (1); TiCo0.3Ni0.7Sb (1); TiCo0.2Ni0.8Sb (1); TiCo0.7Ni0.3Sb (1)
- dopant candidates (<5% at.): Sn (2)
- sample form: Bulk (3)
- measured range: 81-970 K (5th-95th pct of 35 curves)
- papers: https://doi.org/10.1016/s0925-8388(01)01618-8 (Electric transport and magnetic properties of TiCo1−xNixSb solid solution) | https://doi.org/10.1016/j.jssc.2019.04.041 (Phase stability and thermoelectric properties of TiCoSb-TiM2Sn (M = Ni...) | https://doi.org/10.1016/j.scriptamat.2020.04.036 (Thermoelectric properties of half-Heusler high-entropy Ti2NiCoSn1-xSb1...)

## Co-O-V
- rank 565 | 12 samples | 2 papers | 2 compositions
- compositions: Co3V2O8 (11); CoV2O4 (1)
- seed hypothesis (confirm): spinel
- sample form: SingleCrystal (11)
- measured range: 10-193 K (5th-95th pct of 12 curves; full span incl. outliers 10-300 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): V2CoO8 Pnma (62) mp-1194802 [hull=0.228, icsd=3, PRIMARY]; V2CoO6 C2/m (12) mp-19311 [hull=0.010, icsd=1, PRIMARY, AMBIGUOUS]; V2Co2O7 P2_1/c (14) mp-622282 [hull=0.000, PRIMARY]; V2CoO4 Fd-3m (227) mp-765825 [hull=0.000, PRIMARY]; V3Co10AsO20 C2/m (12) mp-1208112 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.7566/jpsj.89.044702 (Nonlinear Behavior in the Electrical Resistance of Strongly Correlated...) | https://doi.org/10.1063/1.4953790 (Heat switch effect in an antiferromagnetic insulator Co3V2O8)

## Cs-I-Sn
- rank 566 | 12 samples | 3 papers | 7 compositions
- compositions: CsSnI2.99Cl0.01 (5); CsSnI3 (2); CsSn0.8Ge0.2I3 (1); CsSn0.9Ge0.1I3 (1); (CsSnI3)0.995(PbI2)0.005 (1); (CsSnI3)0.99(PbI2)0.01 (1)
- dopant candidates (<5% at.): Cl (5), Pb (3), Ge (2)
- curator composition details (from the paper): 1% mixed CsSnI3−xClx perovskite thin films (5)
- sample form: Polycrystal (4); Bulk (3)
- measured range: 293-522 K (5th-95th pct of 55 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CsSnI3 Pnma (62) mp-27381 [hull=0.000, icsd=2, PRIMARY, AMBIGUOUS]; Cs2SnI6 Fm-3m (225) mp-27636 [hull=0.000, icsd=2, PRIMARY]; CsSnI3 P4/mbm (127) mp-616378 [hull=0.003, icsd=2]; CsSnI3 Pm-3m (221) mp-614013 [hull=0.007, icsd=2]
- papers: https://doi.org/10.1038/s41467-019-13773-3 (Enhanced control of self-doping in halide perovskites for improved the...) | https://doi.org/10.1021/acs.jpcc.0c00459 (Enhanced Thermoelectric Performance in Lead-Free Inorganic CsSn1–xGexI...) | https://doi.org/10.1016/j.matlet.2021.131127 (Enhanced thermoelectric performance in inorganic CsSnI3 perovskite by ...)

## Cu-In-Te-Zn
- rank 567 | 12 samples | 4 papers | 10 compositions
- compositions: Zn2Cu3In3Te8 (3); Cu0.9In0.9Zn0.2Te2 (1); Zn1.9Cu3.1In3Te8 (1); Zn1.8Cu3.2In3Te8 (1); Zn1.7Cu3.3In3Te8 (1); Zn1.6Cu3.4In3Te8 (1)
- dopant candidates (<5% at.): Ag (4)
- seed hypothesis (confirm): stannite_kesterite
- sample form: Bulk (2)
- measured range: 318-874 K (5th-95th pct of 49 curves; full span incl. outliers 314-967 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zn2InCuTe4 I-42m (121) mp-1215701 [hull=0.010, PRIMARY]
- papers: https://doi.org/10.1039/c4dt01909a (Lattice defects and thermoelectric properties: the case of p-type CuIn...) | https://doi.org/10.1021/acsaem.9b02004 (A2Cu3In3Te8 (A = Cd, Zn, Mn, Mg): A Type of Thermoelectric Material wi...) | https://doi.org/10.1016/j.mtphys.2020.100333 (Embedded in-situ nanodomains from chemical composition fluctuation in ...)

## Cu-Ir-La-O
- rank 568 | 12 samples | 1 papers | 5 compositions
- compositions: La2CuIrO6 (4); Ba0.2La1.8CuIrO6 (2); Ba0.4La1.6CuIrO6 (2); Ca0.2La1.8CuIrO6 (2); Ca0.4La1.6CuIrO6 (2)
- dopant candidates (<5% at.): Ba (4), Ca (4)
- measured range: 320-773 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2CuIrO6 P2_1/c (14) mp-1211597 [hull=0.032, PRIMARY]
- papers: https://doi.org/10.1103/physrevmaterials.5.054604 (Iridium valence variation and carrier sign tuning in \n(Ca,Ba)xLa2−xCu...)

## Fe-Mn-O-Zn
- rank 569 | 12 samples | 6 papers | 12 compositions
- compositions: Mn0.5Zn0.5La0.05Fe1.95O4 (1); Mn0.5Zn0.5Th0.05Fe1.95O4 (1); Mn0.5Zn0.5Tb0.05Fe1.95O4 (1); Mn0.5Zn0.5Ce0.05Fe1.95O4 (1); Mn0.4Zn0.6Fe2O4 (1); Mn0.4Zn0.6In0.035Fe1.965O4 (1)
- dopant candidates (<5% at.): In (3), Ce (2), La (1), Th (1), Tb (1), Er (1), Gd (1)
- seed hypothesis (confirm): spinel
- curator composition details (from the paper): Mn0.58−x/2 Zn0.37−x/2 MxFe2.05O4 (1)
- measured range: 300-613 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn3Zn(FeO2)8 R3m (160) mp-1221853 [hull=0.072, PRIMARY]; MnZn(FeO2)4 F-43m (216) mp-1221602 [hull=0.000, PRIMARY]; MnZn3(FeO2)8 P-4m2 (115) mp-1221586 [hull=0.015, PRIMARY]
- papers: https://doi.org/10.1016/j.ceramint.2005.07.014 (Enhancement of the physical properties of rare-earth-substituted Mn–Zn...) | https://doi.org/10.1016/j.jmmm.2014.12.031 (Study of conduction phenomena in indium substituted Mn–Zn nano-ferrites) | https://doi.org/10.1023/a:1004571418384 ([])

## Fe-Sb-Se
- rank 570 | 12 samples | 2 papers | 11 compositions
- compositions: FeSb2Se4 (2); FeSb1.85Sn0.15Se4 (1); FeSb1.9Sn0.1Se4 (1); FeSb1.8Sn0.2Se4 (1); FeSb1.98Sn0.02Se4 (1); FeSb1.95In0.05Se4 (1)
- dopant candidates (<5% at.): In (6), Sn (4)
- curator composition details (from the paper): p-type Ferromagnetic semiconductors (FMSs) (5)
- sample form: Polycrystal (12)
- measured range: 15-699 K (5th-95th pct of 51 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeSbSe P2_1/c (14) mp-1103256 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/jacs.9b01884 (Charge Disproportionation Triggers Bipolar Doping in FeSb2–xSnxSe4 Fer...) | https://doi.org/10.1021/acs.chemmater.6b03293 (Indium Preferential Distribution Enables Electronic Engineering of Mag...)

## Li-Mn-O
- rank 571 | 12 samples | 2 papers | 7 compositions
- compositions: Li1.006Mn1.994O4 (4); Li0.98Mn2O4 (3); Li1.03Mn1.97O4 (1); Li0.4Mn2O4 (1); Li0.68Mn2O4 (1); Li0.8Mn2O4 (1)
- seed hypothesis (confirm): spinel
- measured range: 233-302 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiMn2O4 Fd-3m (227) mp-25015 [hull=0.038, icsd=23, PRIMARY]; LiMnO2 Pmmn (59) mp-18767 [hull=0.004, icsd=6, PRIMARY]; Li2MnO3 C2/m (12) mp-18988 [hull=0.000, icsd=5, PRIMARY]; LiMnO4 Cmcm (63) mp-19438 [hull=0.143, icsd=2, PRIMARY]; LiMn4O8 P2_13 (198) mp-1195443 [hull=0.035, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/s0167-2738(01)01022-0 (Conduction mechanism in operating a LiMn2O4 cathode) | https://doi.org/10.1016/s0167-2738(02)00191-1 (Electrochemical and chemical deintercalation of LiMn2O4)

## Li-O-Ru
- rank 572 | 12 samples | 2 papers | 8 compositions
- compositions: Li2RuO3 (3); Li2Ru0.95Ti0.05O3 (2); Li2Ru0.9Ti0.1O3 (2); Li2Ru0.9Ir0.1O3 (1); Li2Ru0.8Ir0.2O3 (1); Li2Ru0.7Ti0.3O3 (1)
- dopant candidates (<5% at.): Ti (6), Ir (3)
- sample form: Bulk (8)
- measured range: 20-612 K (5th-95th pct of 17 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li2RuO3 C2/m (12) mp-4630 [hull=0.000, icsd=3, PRIMARY]; Li(RuO2)2 Pnma (62) mp-1193147 [hull=0.068, icsd=1, PRIMARY]; LiRuO2 Pnnm (58) mp-28254 [hull=0.102, icsd=1, PRIMARY]; NaLi2(RuO2)6 P-1 (2) mp-1201246 [hull=0.015, icsd=1, PRIMARY]; Li11(RuO3)8 P1 (1) mp-757395 [hull=0.050, PRIMARY]
- papers: https://doi.org/10.1039/c5tc01619c (Ruthenium oxide as a thermoelectric material: unconventional thermoele...) | https://doi.org/10.1103/physrevb.100.165119 (Magnetic and electrical anisotropy with correlation and orbital effect...)

## Mg-O
- rank 573 | 12 samples | 6 papers | 2 compositions
- compositions: MgO (11); (MgO)0.96(Al2O3)0.04 (1)
- dopant candidates (<5% at.): Al (1)
- seed hypothesis (confirm): rocksalt
- sample form: Bulk (2)
- measured range: 10-1000 K (5th-95th pct of 13 curves; full span incl. outliers 10-1154 K)
- [ref 1] TEDesignLab / ICSD: MgO Fm-3m (225) mp-1265 [hull=0.000, icsd=54, PRIMARY]; MgO2 Pa-3 (205) mp-2589 [hull=0.024, icsd=2]; MgO P6_3/mmc (194) mp-1192189 [hull=0.040, icsd=1]; MgO Ibam (72) mp-1192043 [hull=0.063, icsd=1]; MgO P6/mcc (192) mp-1190533 [hull=0.113, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: MgO2 C2/m (12) mp-1180260 [hull=0.531, icsd=9, PRIMARY]; BaMg30AlO32 P4/mmm (123) mp-1037958 [hull=0.107, PRIMARY]; YMg30BO32 P4/mmm (123) mp-1037198 [hull=0.129, PRIMARY]; YMg30AlO32 P4/mmm (123) mp-1038325 [hull=0.088, PRIMARY]; BaHfMg14O16 P4/mmm (123) mp-1033883 [hull=0.310, PRIMARY, AMBIGUOUS]
- papers: https://doi.org/10.1002/aenm.201301927 (Enhanced Thermoelectric Power Factor of NaxCoO2Thin Films by Structura...) | https://doi.org/10.1017/s1431927614003894 (Revealing the Origin of “Phonon Glass-Electron Crystal” Behavior in Th...) | https://doi.org/10.1063/1.357390 (Superconducting fast microbolometers operating below their critical te...)

## Mg-Sn-Te
- rank 574 | 12 samples | 2 papers | 10 compositions
- compositions: Sn0.91Mg0.12Te(Cu2Te)0.05 (3); Sn0.91Mg0.12Te(Cu2Te)0.01 (1); Sn0.91Mg0.12Te(Cu2Te)0.03 (1); Sn0.91Mg0.12Te (1); Sn0.8Ge0.05Mg0.2Te(Cu2Te)0.05 (1); Sn0.81Ge0.05Mg0.2Te(Cu2Te)0.05 (1)
- dopant candidates (<5% at.): Cu (10), Ge (6)
- sample form: Bulk (6)
- measured range: 298-904 K (5th-95th pct of 49 curves)
- papers: https://doi.org/10.1021/acsenergylett.6b00671 (Interstitial Defects Improving Thermoelectric SnTe in Addition to Band...) | https://doi.org/10.1016/j.mtphys.2019.03.005 (Maximization of transporting bands for high-performance SnTe alloy the...)

## Mn-O-V
- rank 575 | 12 samples | 3 papers | 7 compositions
- compositions: MnV2O4 (4); Mn2VO4 (2); Mn1.67V1.33O4 (2); Mn(V0.95Cr0.05)2O4 (1); Mn0.95Zn0.05V2O4 (1); Mn(V0.9Cr0.1)2O4 (1)
- dopant candidates (<5% at.): Zn (2), Cr (2)
- seed hypothesis (confirm): spinel
- measured range: 101-300 K (5th-95th pct of 17 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaMn9V6(HO13)2 Pa-3 (205) mp-1194843 [hull=0.000, icsd=2, PRIMARY]; Mn2V2O7 C2/m (12) mp-19142 [hull=0.000, icsd=2, PRIMARY]; MnV2O8 Pnma (62) mp-1203804 [hull=0.236, icsd=2, PRIMARY]; Mn3V2O8 Cmce (64) mp-19692 [hull=0.000, icsd=2, PRIMARY]; BaMn9V6O26 Pa-3 (205) mp-1196033 [hull=0.040, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/s10853-014-8444-4 (Transport, magnetic and structural properties of Mott insulator MnV2O4...) | https://doi.org/10.7566/jpsj.89.044702 (Nonlinear Behavior in the Electrical Resistance of Strongly Correlated...) | https://doi.org/10.1063/1.3124361 (Nonadiabatic small polarons, positive magnetoresistance, and ferrimagn...)

## Mn-Pb-Te
- rank 576 | 12 samples | 1 papers | 7 compositions
- compositions: Pb0.88Mn0.12Te1Na0.04 (2); Pb0.7Mn0.3Te1Na0.04 (2); Pb0.64Mn0.36Te1Na0.04 (2); Pb0.76Mn0.24Te1Na0.04 (2); Pb0.76Mn0.18Te1Na0.04 (2); Pb0.82Mn0.18Te1Na0.04 (1)
- dopant candidates (<5% at.): Na (12)
- measured range: 323-725 K (5th-95th pct of 25 curves)
- papers: https://doi.org/10.1016/j.actamat.2016.03.059 (Eutectic microstructures and thermoelectric properties of MnTe-rich pr...)

## Ni-Sb-Sc
- rank 577 | 12 samples | 7 papers | 2 compositions
- compositions: ScNiSb (11); ScNi0.86Sb (1)
- seed hypothesis (confirm): half_heusler
- sample form: Bulk (2); Other (1)
- measured range: 10-992 K (5th-95th pct of 33 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ScNiSb F-43m (216) mp-3432 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2005.04.012 (Thermoelectric properties of ScCoSb, ScNi0.86Sb and MgNiSb compounds) | https://doi.org/10.1088/0953-8984/15/4/304 (Thermoelectrical properties of the compounds ScMVIIISb and YMVIIISb (M...) | https://doi.org/10.1109/ict.2002.1190283 (Thermoelectric properties of the compounds YM/sup 10/Sb and ScM/sup 10...)

## Pt-Sb-Y
- rank 578 | 12 samples | 5 papers | 2 compositions
- compositions: YPtSb (8); PtYSb (4)
- curator composition details (from the paper): deposited at 500degC (1); deposited at 700degC (1); deposited at 800degC (1); deposited at 600degC (1)
- sample form: Bulk (7)
- measured range: 11-968 K (5th-95th pct of 20 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YSbPt F-43m (216) mp-4964 [hull=0.000, icsd=2, PRIMARY]; Y5SbPt2 I4/mcm (140) mp-1207703 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.7567/jjap.52.041804 (High Temperature Thermoelectric Properties of Half-Heusler Compound PtYSb) | https://doi.org/10.1088/0953-8984/15/4/304 (Thermoelectrical properties of the compounds ScMVIIISb and YMVIIISb (M...) | https://doi.org/10.1063/1.3663569 (Transport and optical properties of the gapless Heusler compound PtYSb)

## Rh-Si-Yb
- rank 579 | 12 samples | 4 papers | 4 compositions
- compositions: YbRh3Si7 (7); YbRh2Si2 (3); Yb0.98La0.02Rh2Si2 (1); Yb(Rh0.94Ir0.06)2Si2 (1)
- dopant candidates (<5% at.): La (1), Ir (1)
- sample form: SingleCrystal (5)
- measured range: 10-297 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(SiRh)2 I4/mmm (139) mp-10626 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1103/physrevlett.109.156405 (Thermoelectric Response Near a Quantum Critical Point ofβ−YbAlB4andYbR...) | https://doi.org/10.1103/physrevx.8.041047 (Anomalous Metamagnetism in the Low Carrier Density Kondo Lattice \nYbR...) | https://doi.org/10.1007/s10909-019-02187-6 (Thermopower Evolution in Yb(\n                \n                  \n  ...)

## Sb
- rank 580 | 12 samples | 5 papers | 3 compositions
- compositions: Sb (10); (Cu2O)0.15Sn0.4Ba0.4Sb11.6 (1); Bi1Sb90 (1)
- dopant candidates (<5% at.): Sn (1), Ba (1), Cu (1), O (1), Bi (1)
- sample form: Bulk (1)
- measured range: 11-621 K (5th-95th pct of 21 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sb R-3m (166) mp-104 [hull=0.000, icsd=13, PRIMARY]; Sb Pm-3m (221) mp-133 [hull=0.049, icsd=7]; Sb Im-3m (229) mp-7761 [hull=0.234, icsd=2]; Sb P6_3/mmc (194) mp-80 [hull=0.280, icsd=2]; Sb I4/mmm (139) mp-10631 [hull=0.312, icsd=1]
- papers: https://doi.org/10.1016/0022-3093(84)90047-4 (Thermoelectric properties of amorphous antimony) | https://doi.org/10.1088/0022-3727/48/45/455309 (The effect of Cu2O nanoparticle dispersion on the thermoelectric prope...) | https://doi.org/10.1016/0038-1101(72)90173-6 (BiSb alloys for magneto-thermoelectric and thermomagnetic cooling)

## Th
- rank 581 | 12 samples | 3 papers | 7 compositions
- compositions: Th96Ce4 (4); Th98Ce2 (2); Th (2); Th99.5U0.5 (1); Th97U3 (1); Th98U2 (1)
- dopant candidates (<5% at.): Ce (6), U (4)
- seed hypothesis (confirm): solid_solution_alloy
- measured range: 10-297 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Th Fm-3m (225) mp-37 [hull=0.000, icsd=9, PRIMARY]; Th Im-3m (229) mp-11343 [hull=0.130, icsd=1]
- papers: https://doi.org/10.1007/bf00628323 (Superconductivity and normal-state properties ofThU alloys) | https://doi.org/10.1007/bf00655253 (The thermoelectric power of someThCe alloys) | https://doi.org/10.1007/bf00655330 (Comments upon ?the thermoelectric power of someThCe alloys? and an alt...)

## Ag-Co-Na-O
- rank 582 | 11 samples | 3 papers | 5 compositions
- compositions: Na0.55Ag0.45Co2O4 (4); Na0.6Ag0.4Co2O4 (4); Ag0.4NaCo2O4 (1); Na1.7Ag0.5Co1.5O4 (1); Na1.7Ag0.4Co1.6O4 (1)
- sample form: Bulk (2)
- measured range: 367-1099 K (5th-95th pct of 19 curves)
- papers: https://doi.org/10.2497/jjspm.55.90 (Effects of Mechanical Milling with Ag Powder on Thermoelectric Propert...) | https://doi.org/10.1016/j.jallcom.2007.12.012 (Self-ignition route to Ag-doped Na1.7Co2O4 and its thermoelectric prop...) | https://doi.org/10.1088/1757-899x/774/1/012056 (Effect of Doping Radio on Thermoelectric Properties of Na1-xAgxCO2O4)

## Ag-Cu-Ga-Te
- rank 583 | 11 samples | 3 papers | 8 compositions
- compositions: Cu0.5Ag0.5GaTe2 (2); Cu0.75Ag0.25GaTe2 (2); Cu0.7Ag0.3GaTe2 (2); Cu0.25Ag0.75GaTe2 (1); Cu0.65Ag0.35GaTe2 (1); Cu0.6Ag0.4GaTe2 (1)
- dopant candidates (<5% at.): In (1)
- seed hypothesis (confirm): chalcopyrite
- sample form: Bulk (9); Polycrystal (2)
- solid-solution axis: Ag/(Ag+Cu) spans 0.20-0.75 (median 0.35) over 8 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 298-855 K (5th-95th pct of 58 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ga2CuAgTe4 I-4 (82) mp-1224861 [hull=0.009, PRIMARY]
- papers: https://doi.org/10.7567/jjap.52.081801 (Thermoelectric Properties of Chalcopyrite-Type CuGaTe2with Ag Substitu...) | https://doi.org/10.1039/c6ta10770b (Substitutional defects enhancing thermoelectric CuGaTe2) | https://doi.org/10.1021/jacs.1c01801 (Ultralow Thermal Conductivity in Diamondoid Structures and High Thermo...)

## Ag-Mo-Se
- rank 584 | 11 samples | 4 papers | 9 compositions
- compositions: Ag3.4Mo9Se11 (2); Ag3.8Mo9Se11 (2); Ag3.5Mo9Se11 (1); Ag3.7Mo9Se11 (1); Ag3.9Mo9Se11 (1); Ag3.6Cu0.2Mo9Se11 (1)
- dopant candidates (<5% at.): Cu (2)
- sample form: Bulk (10)
- measured range: 299-833 K (5th-95th pct of 45 curves)
- [ref 1] TEDesignLab / ICSD: Ag(MoSe)3 P6_3/m (176) mp-1105028 [hull=0.120, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ag(Mo3Se4)2 R-3 (148) mp-1103642 [hull=0.078, icsd=4, PRIMARY]
- papers: https://doi.org/10.1063/1.3579261 (Promising thermoelectric properties in AgxMo9Se11 compounds (3.4≤x≤3.9)) | https://doi.org/10.1007/s11664-012-1906-z (Optimization of Bulk Thermoelectrics: Influence of Cu Insertion in Ag3...) | https://doi.org/10.1007/s11664-010-1413-z (Cage-Shaped Mo9 Chalcogenides: Promising Thermoelectric Materials with...)

## Al-Ba-Ga-Ge
- rank 585 | 11 samples | 3 papers | 9 compositions
- compositions: Ba8Al4Ga12Ge30 (3); Ba8Ga16Al3.0Ge27.0 (1); Ba8Ga16Al4Ge26 (1); Ba8Ga16Al5Ge25 (1); Ba8Al8Ga8Ge30 (1); Ba8Al5.28Ga10.72Ge30 (1)
- seed hypothesis (confirm): clathrate_i
- sample form: Bulk (3); SingleCrystal (1)
- solid-solution axis: Al/(Al+Ga) spans 0.16-0.50 (median 0.24) over 9 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 296-974 K (5th-95th pct of 29 curves; full span incl. outliers 295-1074 K)
- papers: https://doi.org/10.1063/1.2902504 (High temperature thermoelectric transport properties of p-type Ba8Ga16...) | https://doi.org/10.1002/aelm.202000782 (Enhanced Thermoelectric Performance of Ba\n            8\n            ...) | https://doi.org/10.1021/acs.chemmater.1c00731 (Order–Disorder Transition in Inorganic Clathrates Controls Electrical ...)

## Al-Co-Fe-Ti
- rank 586 | 11 samples | 2 papers | 7 compositions
- compositions: (Fe0.2Co0.8)2TiAl (4); (Fe0.3Co0.7)2TiAl (2); (Fe0.5Co0.5)2TiAl (1); (Fe0.65Co0.35)2TiAl (1); (Fe0.55Co0.45)2TiAl (1); (Fe0.4Co0.6)2TiAl (1)
- sample form: Bulk (11)
- measured range: 13-1259 K (5th-95th pct of 21 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiAlFeCo F-43m (216) mp-998980 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2004.01.035 (Thermoelectric properties of Fe2TiAl Heusler alloys) | https://doi.org/10.2320/jinstmet.72.464 (Thermoelectric Properties of Heusler-Type (Fe1-xCox)2TiAl Alloys)

## Al-Fe-Mo-V
- rank 587 | 11 samples | 2 papers | 2 compositions
- compositions: Fe2V0.75Mo0.25Al (10); Fe2(V0.8Mo0.2)Al (1)
- seed hypothesis (confirm): full_heusler
- measured range: 96-802 K (5th-95th pct of 12 curves)
- papers: https://doi.org/10.1007/s11664-015-4265-8 (Thermoelectric Properties of Fe2VAl and Fe2V0.75M0.25Al (M = Mo, Nb, T...) | https://doi.org/10.2320/jinstmet1952.66.7_767 (Doping Effects on Thermoelectric Properties of the Pseudogap Fe2VAl Sy...)

## Al-Fe-Nb-V
- rank 588 | 11 samples | 3 papers | 2 compositions
- compositions: Fe2V0.75Nb0.25Al (9); Fe2V0.8Nb0.2Al (2)
- sample form: Bulk (1)
- measured range: 100-963 K (5th-95th pct of 18 curves)
- papers: https://doi.org/10.1016/j.jallcom.2009.06.202 (Effect of Nb substitution for V on the thermoelectric properties of Fe...) | https://doi.org/10.1007/s11664-015-4265-8 (Thermoelectric Properties of Fe2VAl and Fe2V0.75M0.25Al (M = Mo, Nb, T...) | https://doi.org/10.1134/s1063782619130207 (Electrical Transport Properties of Nb and Ga Double Substituted Fe2VAl...)

## Al-Fe-Si-V
- rank 589 | 11 samples | 6 papers | 9 compositions
- compositions: Fe2VAl0.8Si0.2 (3); Fe2VAl0.7Si0.3 (1); Fe2VAl0.6Si0.4 (1); Fe2VAl0.5Si0.5 (1); Fe2V(Al0.8Si0.2) (1); Fe2.2V0.8Al0.6Si0.4 (1)
- seed hypothesis (confirm): full_heusler
- sample form: Bulk (5)
- measured range: 11-400 K (5th-95th pct of 29 curves; full span incl. outliers 11-1094 K)
- papers: https://doi.org/10.1103/physrevb.75.064204 (Thermoelectric properties of quaternary Heusler alloysFe2VAl1−xSix) | https://doi.org/10.1088/1757-899x/18/14/142001 (Development of thermoelectric materials based on Fe2VAl Heusler compou...) | https://doi.org/10.1007/s11664-008-0626-x (High Thermoelectric Power Factor Near Room Temperature in Full-Heusler...)

## Al-Ir
- rank 590 | 11 samples | 4 papers | 9 compositions
- compositions: Al73Ir27_IAC_1_0 (3); Al73.2Ir26.8 (1); Al73.8Ir26.2 (1); Al72.3CuIr26.7_IAC_1_0 (1); Al73.3Ir26.7_IAC (1); Al71.3Cu2Ir26.7_IAC_1_0 (1)
- dopant candidates (<5% at.): Cu (4)
- measured range: 17-961 K (5th-95th pct of 17 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlIr Pm-3m (221) mp-1885 [hull=0.000, icsd=3, PRIMARY]; Al3Ir P6_3/mmc (194) mp-2294 [hull=0.000, icsd=2, PRIMARY]; Al9Ir2 P2_1/c (14) mp-12003 [hull=0.000, icsd=2, PRIMARY]; Al3Ir Pm-3n (223) mp-1200220 [hull=0.098, icsd=1]
- papers: https://doi.org/10.2320/matertrans.e-m2020845 (Vacancy Control and Enhancement of Thermoelectric Properties of Al–Ir ...) | https://doi.org/10.1016/j.jallcom.2020.156904 (Band engineering in Al-TM (TM=Rh, Ir) quasicrystalline approximants vi...) | https://doi.org/10.1016/j.jallcom.2018.05.199 (Anomalous effects of Cu-doping on structural and thermoelectric proper...)

## Al-O-Y
- rank 591 | 11 samples | 5 papers | 4 compositions
- compositions: Y3Al5O12 (6); (Y3Al5O12)14.66(Al2O3)85.34 (3); (Y2O3)58.35(Al2O3)41.15 (CeO2)0.5 (1); (Y2O3)30.61(Al2O3)68.89 (CeO2)0.5 (1)
- dopant candidates (<5% at.): Ce (2)
- seed hypothesis (confirm): garnet
- curator composition details (from the paper): commercially available Ce-doped YAG + α-Al2O3 (3); commercially available Ce-doped YAG (1)
- sample form: Bulk (7); Coating (4)
- measured range: 293-1571 K (5th-95th pct of 11 curves)
- [ref 1] TEDesignLab / ICSD: YAlO3 Pnma (62) mp-3792 [hull=0.019, icsd=17, PRIMARY]; YAlO3 P6_3/mmc (194) mp-7964 [hull=0.102, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: Y3Al5O12 Ia-3d (230) mp-3050 [hull=0.000, icsd=15, PRIMARY]; Y4Al2O9 P2_1/c (14) mp-5409 [hull=0.011, icsd=8, PRIMARY]; Ca3Y9Al18CrSiO48 P1 (1) mp-744910 [hull=0.022, PRIMARY]; Y3AlO6 Cmc2_1 (36) mp-754979 [hull=0.018, PRIMARY]; Y9Lu3Al20O48 C2 (5) mp-1216268 [hull=0.001, PRIMARY]
- papers: https://doi.org/10.1007/s11666-018-0728-9 (Low Thermal Conductivity Yttrium Aluminum Garnet Thermal Barrier Coati...) | https://doi.org/10.1007/s11666-018-0701-7 (Higher Temperature Thermal Barrier Coatings with the Combined Use of Y...) | https://doi.org/10.1002/adem.201100122 (Y3−xErxAl5O12 Aluminate Ceramics: Preparation, Thermal Properties and ...)

## As-Cs-Mo
- rank 592 | 11 samples | 1 papers | 1 compositions
- compositions: Cs2Mo3As3 (11)
- measured range: 10-13 K (5th-95th pct of 12 curves; full span incl. outliers 10-283 K)
- papers: https://doi.org/10.1063/1.5139472 (Synthesis and superconductivity of a novel quasi-one-dimensional terna...)

## B-C-Ni-Yb
- rank 593 | 11 samples | 1 papers | 1 compositions
- compositions: YbNi2B2C (11)
- seed hypothesis (confirm): borocarbide_1221
- curator composition details (from the paper): unannealed (3); annealing conditions: 950degC 150h (3); annealing conditions: 950degC 50h (2); annealing conditions: 950degC 20h (1); annealing conditions: 950degC 100h (1)
- sample form: SingleCrystal (11)
- measured range: 10-301 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbNi2B2C I4/mmm (139) mp-6286 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.66.132504 (Drastic annealing effects in transport properties of single crystals o...)

## B-Sr
- rank 594 | 11 samples | 7 papers | 4 compositions
- compositions: SrB6 (8); Sr0.75Ba0.25B6 (1); Ca0.25Sr0.75B6 (1); Ca0.25B1.5Sr0.75B4.5 (1)
- dopant candidates (<5% at.): Ca (2), Ba (1)
- sample form: Bulk (2); Film (1)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 293-1075 K (5th-95th pct of 22 curves; full span incl. outliers 291-1120 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrB6 Pm-3m (221) mp-242 [hull=0.000, icsd=8, PRIMARY]; SrB2 P6/mmm (191) mp-1008755 [hull=0.533, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2006.01.025 (Improvement of thermoelectric properties of alkaline-earth hexaborides) | https://doi.org/10.1016/j.jssc.2014.10.001 (High-pressure densified solid solutions of alkaline earth hexaborides ...) | https://doi.org/10.1109/ict.2002.1190293 (Thermoelectric properties of metal-hexaborides)

## Ba-Cu-Gd-O
- rank 595 | 11 samples | 6 papers | 3 compositions
- compositions: GdBa2Cu3O7 (9); Gd1Ba2Cu3O7 (1); (GdBa2Cu3O7)0.8(Gd2O3)0.2 (1)
- seed hypothesis (confirm): ybco_cuprate
- curator composition details (from the paper): thin film (1)
- sample form: Bulk (2)
- measured range: 77-300 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2GdCu3O7 Pmmm (47) mp-19813 [hull=0.018, icsd=3, PRIMARY]; BaGd2CuO5 Pnma (62) mp-1182677 [hull=0.030, icsd=2, PRIMARY]; Ba2Gd(CuO2)4 Cmmm (65) mp-1214720 [hull=0.000, PRIMARY]; Ba10Gd4Y(Cu3O7)5 Pmmm (47) mp-1229238 [hull=0.027, PRIMARY]; Ba4Gd(CuO3)3 Pm-3n (223) mp-1214933 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1007/bf02744736 (Low percolation concentration for zero thermoelectric power in Y1Ba2Cu...) | https://doi.org/10.1088/0022-3727/26/2/016 (Normal state transport properties in superconducting oxides RBa2Cu3O7-...) | https://doi.org/10.1103/physrevb.36.3913 (Normal-state properties ofABa2Cu3O7−ycompounds (A=YandGd): Electron-el...)

## Ba-Ir-O
- rank 596 | 11 samples | 3 papers | 3 compositions
- compositions: BaIrO3 (9); Ba2IrO4 (1); Ba2Ir3O9 (1)
- measured range: 10-322 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaIrO3 Pm-3m (221) mp-5660 [hull=0.141, icsd=3, PRIMARY]; Ba4Ir3O10 P2_1/c (14) mp-17102 [hull=0.000, icsd=1, PRIMARY, AMBIGUOUS]; Ba2IrO4 I4/mmm (139) mp-755117 [hull=0.021, icsd=1, PRIMARY]; Ba7Ir6O19 C2/m (12) mp-28867 [hull=0.008, icsd=1, PRIMARY]; Ba(IrO3)2 R3 (146) mp-674187 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.80.104430 (Transition from a weak ferromagnetic insulator to an exchange-enhanced...) | https://doi.org/10.1103/physrevb.83.155118 (Ba<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\...) | https://doi.org/10.1016/j.jallcom.2004.04.062 (Ba2Ir3O9: a new 5d mixed-valence metallic oxide with KSbO3-type structure)

## Ba-Ni-Si
- rank 597 | 11 samples | 4 papers | 9 compositions
- compositions: Ba8Ni3.5Si42.0 (3); Ba8Ni3.5Si41.0 (1); Ba8Ni2.9Si43.1 (1); Ba8Ni3.1Si39.9 (1); Ba8Ni2.8Si43.2 (1); Ba8Ni3.4Si39.6 (1)
- dopant candidates (<5% at.): Pt (1)
- seed hypothesis (confirm): clathrate_i
- sample form: Bulk (4); SingleCrystal (1)
- measured range: 10-1074 K (5th-95th pct of 27 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba(SiNi)2 Cmcm (63) mp-27388 [hull=0.000, icsd=1, PRIMARY]; Ba2Si3Ni P-62m (189) mp-29819 [hull=0.000, PRIMARY]; Ba8Si43Ni3 R32 (155) mp-1228480 [hull=0.003, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2012.02.054 (Crystal structure and thermoelectric properties of clathrate, Ba8Ni3.5...) | https://doi.org/10.1103/physrevb.83.205102 (Low-temperature magnetic, galvanomagnetic, and thermoelectric properti...) | https://doi.org/10.1007/s11664-015-4238-y (High-Temperature Thermoelectric Properties of Polycrystalline Silicon ...)

## Bi-Cu-O-Te
- rank 598 | 11 samples | 4 papers | 11 compositions
- compositions: BiCuOTe (1); Bi0.99Pb0.01CuOTe (1); Bi0.96Pb0.04CuOTe (1); Bi0.94Pb0.06CuOTe (1); Bi0.98Pb0.02CuOTe (1); BiCuTeO (1)
- dopant candidates (<5% at.): Pb (4)
- curator composition details (from the paper): Bi1−xPbxCuOTe (4)
- sample form: Bulk (10)
- measured range: 296-723 K (5th-95th pct of 47 curves; full span incl. outliers 11-725 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuBi2Te2O P4/mmm (123) mp-1213110 [hull=0.546, PRIMARY]
- papers: https://doi.org/10.1039/c4ta04057k (Point defect-assisted doping mechanism and related thermoelectric tran...) | https://doi.org/10.1063/1.5102141 (Comparisons of electrical/magneto-transport properties of degenerate s...) | https://doi.org/10.1016/j.mtphys.2020.100248 (Highly improved thermoelectric performance of BiCuTeO achieved by decr...)

## Bi-K-S-Se
- rank 599 | 11 samples | 2 papers | 7 compositions
- compositions: K2Bi8Se7S6 (4); K2Bi8Se7S6  (2); K2Bi8Se9S4 (1); K2Bi8Se5S8 (1); K2Bi8Se7S6.002 (1); K2Bi8Se7S6.01 (1)
- seed hypothesis (confirm): bi_chalcogenide_complex
- solid-solution axis: S/(S+Se) spans 0.31-0.62 (median 0.46) over 7 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 85-672 K (5th-95th pct of 39 curves)
- papers: https://doi.org/10.1007/s11664-012-2331-z (Thermoelectric Properties of Hot-Pressed β-K2Bi8Se13−x S x Materials) | https://doi.org/10.1109/ict.2006.331346 (Thermoelectric Properties of Pressed Pellets and Pressureless Sinterin...)

## Bi-O-Sb-Te
- rank 600 | 11 samples | 7 papers | 8 compositions
- compositions: (Bi0.5Sb1.5Te3)91.26(Sb2O3)8.74 (4); (Mg1.25Al0.75Si4O11H)0.03Bi0.42Sb1.58Te3 (1); (BiSbTe)87.89(RuO2)12.11 (1); (Bi0.5Sb1.5Te3)87.21(Sb2O3)12.79 (1); (Bi0.5Sb1.5Te3)94.06(Ta2O5)5.94 (1); (Bi0.5Sb1.5Te3)88.72(Nd2O3)11.28 (1)
- dopant candidates (<5% at.): Si (1), Mg (1), H (1), Al (1), Ru (1), Ta (1), Nd (1), Y (1), Zr (1)
- curator composition details (from the paper): BiSbTe/1.5wt% D-ATP (1); p-type Bi2Te3 + 75%Sb2Te3 (hereafter referred to as BiSbTe) alloy powder+ 4 wt%ZrO2 (1)
- sample form: Bulk (8); Composite (1)
- measured range: 299-550 K (5th-95th pct of 44 curves)
- papers: https://doi.org/10.1039/c3ra23219k (Effect of dehydrated-attapulgite nanoinclusions on the thermoelectric ...) | https://doi.org/10.4028/www.scientific.net/kem.512-515.1651 (The Influence of RuO<sub>2</sub> Addition on the Thermoelectric Proper...) | https://doi.org/10.1039/c8ta08238c (Enhanced thermoelectric performance of Bi–Sb–Te/Sb2O3 nanocomposites b...)
