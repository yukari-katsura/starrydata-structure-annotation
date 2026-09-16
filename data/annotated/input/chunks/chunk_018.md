# Host systems -- chunk 018 of 73

Ranks 851-900 by sample count. These 50 host systems cover 350 samples (0.67% of the TE set); cumulative through this chunk: 87.84%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Ba-Ga-K-Sn
- rank 851 | 7 samples | 3 papers | 5 compositions
- compositions: K8Ba16Ga40Sn96 (2); K10.8Ba13.2Ga36.7Sn89.4 (2); K10.1Ba13.9Ga37.2Sn95.0 (1); K9.2Ba14.8Ga38.0Sn95.2 (1); K9Ba14.5Ga40.5Sn97.5 (1)
- measured range: 10-838 K (5th-95th pct of 16 curves)
- papers: https://doi.org/10.1063/1.4889822 (Thermoelectric and transport properties of sintered n-type K8Ba16Ga40S...) | https://doi.org/10.1103/physrevb.84.214101 (Off-center rattling and thermoelectric properties of type-II clathrate...) | https://doi.org/10.7567/1882-0786/ab587c (Power generation characteristics of thermoelectric conversion module u...)

## Ba-Si
- rank 852 | 7 samples | 4 papers | 5 compositions
- compositions: BaSi2 (3); Ba0.98La0.02Si2 (1); Ba0.96La0.04Si2 (1); Ba0.92La0.08Si2 (1); Ba8Ni2.6Si43.4 (1)
- dopant candidates (<5% at.): La (3), Ni (1)
- measured range: 11-971 K (5th-95th pct of 27 curves; full span incl. outliers 10-1164 K)
- [ref 1] TEDesignLab / ICSD: BaSi2 Pnma (62) mp-1477 [hull=0.000, icsd=9, PRIMARY]; Ba2Si Pnma (62) mp-9905 [hull=0.000, icsd=3, PRIMARY]; BaSi2 P4_332 (212) mp-7275 [hull=0.014, icsd=2]
- [ref 2] MP, ranked by ICSD evidence: Ba4Si23 Pm-3n (223) mp-640551 [hull=0.051, icsd=5, PRIMARY]; BaSi Cmcm (63) mp-2499 [hull=0.001, icsd=4, PRIMARY]; BaSi6 Cmcm (63) mp-1480 [hull=0.072, icsd=3, PRIMARY]; Ba3Si4 P4_2/mnm (136) mp-1619 [hull=0.000, icsd=3, PRIMARY]; BaSi2 P-3m1 (164) mp-7655 [hull=0.017, icsd=1]
- papers: https://doi.org/10.1063/1.2778747 (Thermoelectric properties of BaSi2, SrSi2, and LaSi) | https://doi.org/10.2320/matertrans.e-mra2008818 (Thermoelectric Properties of La-Doped BaSi<SUB>2</SUB>) | https://doi.org/10.1103/physrevb.83.205102 (Low-temperature magnetic, galvanomagnetic, and thermoelectric properti...)

## Be-Ti
- rank 853 | 7 samples | 1 papers | 1 compositions
- compositions: TiBe12 (7)
- measured range: 293-1274 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiBe2 Fd-3m (227) mp-912109 [hull=0.000, icsd=6, PRIMARY]; Ti2Be17 R-3m (166) mp-12648 [hull=0.000, icsd=4, PRIMARY]; TiBe Pm-3m (221) mp-11279 [hull=0.006, icsd=2, PRIMARY]; TiBe12 I4/mmm (139) mp-1104067 [hull=0.001, icsd=1, PRIMARY]; TiBe3 R-3m (166) mp-1103465 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1109/fusion.2009.5226458 (Beryllides for fusion reactors)

## Bi-Ca-Mg-Yb
- rank 854 | 7 samples | 2 papers | 7 compositions
- compositions: Ca0.5Yb0.5Mg2Bi2 (1); Ca0.7Yb0.3Mg2Bi2 (1); Ca0.3Yb0.7Mg2Bi2 (1); Ca0.5Yb0.5Mg2Bi1.99 (1); Ca0.75Yb0.25Mg1.9Zn0.1Bi1.98 (1); Ca0.65Yb0.35Mg1.9Zn0.1Bi1.98 (1)
- dopant candidates (<5% at.): Zn (3)
- solid-solution axis: Ca/(Ca+Mg) spans 0.13-0.28 (median 0.21) over 7 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 297-874 K (5th-95th pct of 35 curves)
- papers: https://doi.org/10.1039/c6ta00507a (Thermoelectric properties of Bi-based Zintl compounds Ca1−xYbxMg2Bi2) | https://doi.org/10.1016/j.mtphys.2020.100270 (Enhanced thermoelectric performance of P-type CaMg2Bi1.98 and optimize...)

## Bi-Cu-O-Sr-Y
- rank 855 | 7 samples | 2 papers | 2 compositions
- compositions: Bi2Sr2Ca0.2Y0.8Cu2O8 (5); Bi2Sr2YCu2O8 (2)
- dopant candidates (<5% at.): Ca (5)
- measured range: 30-310 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2YCu2(BiO4)2 Cccm (66) mp-1208863 [hull=0.089, PRIMARY]; Sr2YCu2(BiO4)2 I4/mmm (139) mp-1208753 [hull=0.123]
- papers: https://doi.org/10.1103/physrevb.45.10604 (Thermoelectric power ofBi2Sr2Ca1−xYxCu2O8+y) | https://doi.org/10.1103/physrevb.62.9172 (Microstructure, localizedCu2+spins, and transport properties ofBi2Sr2C...)

## Bi-Cu-Sb-Te
- rank 856 | 7 samples | 4 papers | 6 compositions
- compositions: Cu0.4Bi0.5Sb1.1Te3 (2); (Cu4Te3)0.1(Bi0.5Sb1.5Te3)0.9 (1); (Cu4Te3)0.2(Bi0.5Sb1.5Te3)0.8 (1); Cu0.5Bi0.4Sb1.6Te3.3 (1); Cu0.85Bi0.4Sb1.6Te3.5 (1); Cu0.3Bi0.5Sb1.2Te3 (1)
- measured range: 298-558 K (5th-95th pct of 25 curves)
- papers: https://doi.org/10.1016/j.jallcom.2005.04.217 (Thermoelectric performance of quaternary Cu–Bi–Sb–Te alloys prepared b...) | https://doi.org/10.1063/1.2745413 (High thermoelectric properties of p-type pseudobinary (Cu4Te3)x–(Bi0.5...) | https://doi.org/10.1016/j.nanoen.2012.07.004 (Facile synthesis of Cu7Te4 nanorods and the enhanced thermoelectric pr...)

## Bi-K-Sb-Se
- rank 857 | 7 samples | 2 papers | 6 compositions
- compositions: K2Bi4Sb4Se13 (2); K2Bi6.4Sb1.6Se13 (1); K2Bi5.6Sb2.4Se13 (1); K2Bi2.4Sb5.6Se13 (1); K2Bi1.6Sb6.4Se13 (1); K2Bi1.2Sb6.8Se13 (1)
- solid-solution axis: Bi/(Bi+Sb) spans 0.15-0.80 (median 0.50) over 6 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-399 K (5th-95th pct of 11 curves)
- papers: https://doi.org/10.1063/1.2365718 (Structure inhomogeneities, shallow defects, and charge transport in th...) | https://doi.org/10.1109/ict.2006.331383 (n-to-p Transition on K2Bi8-xSbxSe13 Series)

## Bi-Mg-Yb
- rank 858 | 7 samples | 3 papers | 4 compositions
- compositions: YbMg2Bi2 (4); YbMg2Bi1.88Sb0.1 (1); YbMg2Bi1.78Sb0.2 (1); YbMg2Bi1.98 (1)
- dopant candidates (<5% at.): Sb (2)
- measured range: 11-873 K (5th-95th pct of 39 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(MgBi)2 P-3m1 (164) mp-1068042 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.85.035202 (Thermoelectric transport properties of CaMg2Bi2, EuMg2Bi2, and YbMg2Bi2) | https://doi.org/10.1039/c6ta00507a (Thermoelectric properties of Bi-based Zintl compounds Ca1−xYbxMg2Bi2) | https://doi.org/10.1016/j.jmst.2020.04.052 (Enhanced thermoelectric properties of Zintl phase YbMg2Bi1.98 through ...)

## Bi-O-Ru
- rank 859 | 7 samples | 3 papers | 3 compositions
- compositions: Bi2Ru2O7 (3); Bi3Ru3O11 (3); Bi1.5Y0.5Ru2O7 (1)
- dopant candidates (<5% at.): Y (1)
- measured range: 11-1082 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi2Ru2O7 Fd-3m (227) mp-23445 [hull=0.000, icsd=6, PRIMARY]; Bi12RuO20 I23 (197) mp-1214239 [hull=0.055, PRIMARY]; Bi15Ru16O55 Cm (8) mp-686128 [hull=0.008, PRIMARY]; Bi16Ru16O55 R-3m (166) mp-685341 [hull=0.011, PRIMARY]; BiRu2O7 I2_12_12_1 (24) mp-753640 [hull=0.063, PRIMARY]
- papers: https://doi.org/10.2109/jcersj.112.298 (Thermoelectric Properties of CuO-Added AgSbO3 Ceramics) | https://doi.org/10.1016/s0921-4526(02)02483-3 (Transport, thermal and magnetic properties of Bi3Os3O11 and Bi3Ru3O11) | https://doi.org/10.1088/0953-8984/11/2/004 (Oxygen vacancy control in the defect pyrochlore: a way to tune the ele...)

## Bi-Pb-S
- rank 860 | 7 samples | 3 papers | 3 compositions
- compositions: Pb3Bi2S6 (3); PbBi2S4 (3); Pb0.9Cl0.1Bi2S3 (1)
- dopant candidates (<5% at.): Cl (1)
- measured range: 298-798 K (5th-95th pct of 37 curves)
- [ref 1] TEDesignLab / ICSD: Bi2PbS4 Pnma (62) mp-641924 [hull=0.002, icsd=16, PRIMARY]; Bi2(PbS2)3 C2/m (12) mp-629690 [hull=0.000, icsd=1, PRIMARY]; Bi2(PbS2)3 Cmcm (63) mp-1227695 [hull=0.010]
- [ref 2] MP, ranked by ICSD evidence: Bi2(Pb2S3)3 Cmcm (63) mp-1214399 [hull=0.000, icsd=1, PRIMARY]; Bi2Pb2S5 Pnma (62) mp-680181 [hull=0.018, icsd=1, PRIMARY]; Bi4PbS7 Cm (8) mp-1227567 [hull=0.003, PRIMARY]
- papers: https://doi.org/10.1039/c4ta05135a (Low lattice thermal conductivity in Pb5Bi6Se14, Pb3Bi2S6, and PbBi2S4:...) | https://doi.org/10.1016/j.jallcom.2015.10.052 (High performance thermoelectrics from earth-abundant materials: Enhanc...) | https://doi.org/10.1021/acs.chemmater.1c01387 (PbmBi2S3+m Homologous Series with Low Thermal Conductivity Prepared by...)

## C-Ge
- rank 861 | 7 samples | 1 papers | 2 compositions
- compositions: GeC0.12 (4); GeC0.06 (3)
- measured range: 302-1085 K (5th-95th pct of 10 curves)
- [ref 1] TEDesignLab / ICSD: GeC F-43m (216) mp-1002164 [hull=0.436, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ge3C P6_3/mmc (194) mp-973155 [hull=1.393, PRIMARY]; GeC Fm-3m (225) mp-1002165 [hull=1.271, icsd=1]; GeC P6_3mc (186) mp-1184550 [hull=0.441]
- papers: https://doi.org/10.1134/s1063783415030208 (Transport properties of nanocomposite thermoelectric materials based o...)

## C-H-N-O
- rank 862 | 7 samples | 3 papers | 4 compositions
- compositions: [C(NH2)3]Cu(HCOO)3 (3); Ni(C3H10N2)2NO2ClO4 (2); C6H7N(CH3COO)0.5 (1); [C(NH2)3]Zn(HCOO)3 (1)
- dopant candidates (<5% at.): Cu (3), Ni (2), Cl (2), Zn (1)
- measured range: 10-320 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): H4CN2O P-42_1m (113) mp-23778 [hull=0.000, icsd=23, PRIMARY]; ErCoH8C6(N3O2)2 Cmcm (63) mp-1200936 [hull=0.224, icsd=5, PRIMARY]; H10C2N2O5 P2_12_12 (18) mp-697408 [hull=0.023, icsd=5, PRIMARY]; H2C(NO)2 P2_1/c (14) mp-24332 [hull=0.442, icsd=4, PRIMARY]; HCNO C2/c (15) mp-1190216 [hull=0.000, icsd=3, PRIMARY]
- papers: https://doi.org/10.1016/j.synthmet.2014.01.007 (Investigating thermoelectric properties of doped polyaniline nanowires) | https://doi.org/10.1063/1.5086978 (Anisotropic heat conduction in the metal organic framework perovskites...) | https://doi.org/10.1063/1.4796180 (Large magnetic heat transport in a Haldane chain material Ni(C3H10N2)2...)

## C-Ta
- rank 863 | 7 samples | 2 papers | 5 compositions
- compositions: (W)0.52(TaC)99.48 (3); TaC (1); (W)0.84(TaC)99.16 (1); (W)1.05(TaC)98.95 (1); (W)0.21(TaC)99.79 (1)
- dopant candidates (<5% at.): W (6)
- measured range: 298-773 K (5th-95th pct of 7 curves; full span incl. outliers 298-1274 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TaC Fm-3m (225) mp-1086 [hull=0.000, icsd=37, PRIMARY]; Ta2C P-3m1 (164) mp-7088 [hull=0.000, icsd=2, PRIMARY]; Ta3C P6_3/mmc (194) mp-1187218 [hull=1.436, PRIMARY]; Ta3C2 P-3m1 (164) mp-1218120 [hull=0.001, PRIMARY]; Ta4C3 R3m (160) mp-1218000 [hull=0.035, PRIMARY]
- papers: https://doi.org/10.1016/j.jmat.2020.12.001 (Low temperature densification mechanism and properties of Ta1-Hf C sol...) | https://doi.org/10.1016/j.ijrmhm.2015.12.004 (Effect of hot rolling and annealing on the mechanical properties and t...)

## C-Th
- rank 864 | 7 samples | 2 papers | 7 compositions
- compositions: ThC0.858 (1); ThC0.91 (1); ThC0.787 (1); ThC0.809 (1); ThC0.823 (1); ThC0.808 (1)
- measured range: 12-1128 K (5th-95th pct of 16 curves; full span incl. outliers 12-1212 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ThC Fm-3m (225) mp-1164 [hull=0.000, icsd=12, PRIMARY]; ThC2 C2/c (15) mp-7224 [hull=0.000, icsd=2, PRIMARY]; Th2C3 I-43d (220) mp-1188514 [hull=0.000, icsd=1, PRIMARY]; Th4C3 R-3m (166) mp-1217395 [hull=0.000, PRIMARY]; Th5C4 R-3m (166) mp-1217379 [hull=0.008, PRIMARY]
- papers: https://doi.org/10.1063/1.1710161 (Electrical Properties of Nonstoichiometric Thorium Carbides) | https://doi.org/10.1016/0022-3697(64)90144-1 (Etude de la structure electronique des carbures de thorium, d'uranium ...)

## Ca
- rank 865 | 7 samples | 1 papers | 1 compositions
- compositions: Ca (7)
- measured range: 311-848 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca Fm-3m (225) mp-45 [hull=0.000, icsd=12, PRIMARY]; Ca Im-3m (229) mp-21 [hull=0.037, icsd=14]; Ca I4/mmm (139) mp-1183455 [hull=0.034, icsd=8]; Ca I4/mcm (140) mp-1008498 [hull=0.176, icsd=6]; Ca Cmcm (63) mp-1064227 [hull=0.019, icsd=3]
- papers: https://doi.org/10.1016/0022-5088(78)90162-5 (The electrical resistivity and thermoelectric power of Ca and Sr above...)

## Ca-Co-Cu-O
- rank 866 | 7 samples | 3 papers | 7 compositions
- compositions: Ca3Co3.2Cu0.8O9 (1); Ca1.93Pr0.07(Co1.23Cu0.77)O4(CoO2)1.60 (1); Ca1.80Pr0.20(Co1.10Cu0.90)O4(CoO2)1.60 (1); Ca2(Co1.3Cu0.7)O4(CoO2)1.59 (1); Ca1.73Pr0.27(Co1.03Cu0.97)O4(CoO2)1.60 (1); Ca1.7Pr0.3CoCuO4(CoO2)1.60 (1)
- dopant candidates (<5% at.): Pr (4)
- measured range: 11-383 K (5th-95th pct of 19 curves)
- papers: https://doi.org/10.1039/c2dt31346d (Enhanced electronic correlation and thermoelectric response by Cu-dopi...) | https://doi.org/10.1021/cm061163a (Double Modulation and Microstructure of the Thermoelectric Misfit Comp...) | https://doi.org/10.1109/ict.2002.1190298 (Development of new-type cobalt oxide thermoelectric materials)

## Ca-Co-Mn-O
- rank 867 | 7 samples | 2 papers | 3 compositions
- compositions: Ca3Co1.25Mn0.75O6 (3); Ca3CoMnO6 (3); Ca3Mn0.9Co3.1O9 (1)
- measured range: 10-1173 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca3MnCoO6 R-3c (167) mp-704674 [hull=0.054, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.ssc.2005.01.044 (The effect of Mn substitution on thermoelectric properties of Ca3MnxCo...) | https://doi.org/10.3390/ma12030497 (Thermoelectric Properties of Ca3Co2−xMnxO6 (x = 0.05, 0.2, 0.5, 0.75, ...)

## Ca-Co-O-Sr
- rank 868 | 7 samples | 6 papers | 5 compositions
- compositions: Sr1.9Ca1.2Y0.9Co4O10.5 (2); Ca2SrCo4O9 (2);  (Ca0.7Sr0.3)3Co4O9  (1); (Sr0.7Ca0.3)4Co3O9 (1); (Sr0.53Ca0.45)5Co4O12 (1)
- dopant candidates (<5% at.): Y (2)
- solid-solution axis: Ca/(Ca+Sr) spans 0.30-0.70 (median 0.46) over 5 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-991 K (5th-95th pct of 17 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2Ca6Co7CuO20 P1 (1) mp-1076470 [hull=0.038, PRIMARY]; Sr2Ca6Co7CuO24 Amm2 (38) mp-1099600 [hull=0.108, PRIMARY]; Sr4Ca4Co7CuO20 P1 (1) mp-1076175 [hull=0.035, PRIMARY]; Sr4Ca4Co7CuO24 Cm (8) mp-1099611 [hull=0.089, PRIMARY]; Sr6Ca2Co7CuO20 P1 (1) mp-1076118 [hull=0.028, PRIMARY]
- papers: https://doi.org/10.1039/b914661j (Novel thermoelectric properties of complex transition-metal oxides) | https://doi.org/10.1016/j.jallcom.2010.10.209 (Effect of Ca substitution by Sr on the thermoelectric properties of Ca...) | https://doi.org/10.1063/1.3276158 (Phase compatibility and thermoelectric properties of compounds in the ...)

## Ca-Cr-Fe-La-O
- rank 869 | 7 samples | 3 papers | 6 compositions
- compositions: (La0.3Ca0.7)0.97Fe0.7Cr0.3O3 (2); (La0.3Ca0.7)0.96Fe0.7Cr0.3O3 (1); (La0.3Ca0.7)Fe0.7Cr0.3O3 (1); (La0.3Ca0.7)0.99Fe0.7Cr0.3O3 (1); La0.3Ca0.7Fe0.7Cr0.3O3 (1); La0.75Ca0.25Cr0.75Fe0.25O3 (1)
- measured range: 298-1173 K (5th-95th pct of 7 curves)
- papers: https://doi.org/10.1016/j.jallcom.2022.166615 (Alleviated surface calcium segregation and improved electrocatalytic p...) | https://doi.org/10.1016/j.materresbull.2017.02.021 (Evaluation of La 0.3 Ca 0.7 Fe 1−y Cr y O 3−δ (y = 0.1–0.3) cathodes f...) | https://doi.org/10.1016/s0254-0584(00)00480-6 (Relative content of the Cr4+ ion and electrical conductivity of La0.75...)

## Ca-O-Sr-Ti
- rank 870 | 7 samples | 3 papers | 7 compositions
- compositions: Sr0.6Ca0.3La0.1TiO3 (1); Sr0.5Ca0.4La0.1TiO3 (1); Sr0.45Ca0.45La0.1TiO3 (1); Sr0.3Ca0.6La0.1TiO3 (1); Sr0.75Ca0.25Ti0.97Nb0.03O3 (1); Sr0.6Ca0.4Ti0.97Nb0.03O3 (1)
- dopant candidates (<5% at.): La (4), Nb (2), Nd (1)
- solid-solution axis: Ca/(Ca+Sr) spans 0.25-0.67 (median 0.40) over 7 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 16-868 K (5th-95th pct of 24 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2CaTi3O9 P1 (1) mp-1218872 [hull=0.012, PRIMARY, AMBIGUOUS]; Sr3CaTi4O12 C2 (5) mp-1218577 [hull=0.010, PRIMARY]; Sr7CaTi8O20 P1 (1) mp-1076695 [hull=0.070, PRIMARY]; Sr7CaTi8O24 Pm-3m (221) mp-1075922 [hull=0.010, PRIMARY]; SrCa3Ti4O12 Pm (6) mp-1218476 [hull=0.010, PRIMARY]
- papers: https://doi.org/10.1016/j.matlet.2004.08.012 (Substitution effect on the thermoelectric properties of alkaline earth...) | https://doi.org/10.1103/physrevb.85.075112 (Thermoelectric properties of the electron-doped perovskites Sr1−xCaxTi...) | https://doi.org/10.1103/physrevb.96.064105 (Thermoelectric and structural correlations in \n(Sr1−x−yCaxNdy)TiO3\n ...)

## Ca-O-Ti
- rank 871 | 7 samples | 4 papers | 6 compositions
- compositions: Ca0.9La0.1TiO3 (2); Sr0.15Ca0.75La0.1TiO3 (1); Nd0.1Ca0.9TiO3 (1); Nd0.2Ca0.8TiO3 (1); CaTi0.9Fe0.1O3 (1); CaTi0.8Fe0.2O3 (1)
- dopant candidates (<5% at.): La (3), Nd (2), Fe (2), Sr (1)
- measured range: 79-867 K (5th-95th pct of 17 curves)
- [ref 1] TEDesignLab / ICSD: CaTiO3 Pnma (62) mp-4019 [hull=0.000, icsd=55, PRIMARY]; CaTi2O4 Cmcm (63) mp-3463 [hull=0.026, icsd=3, PRIMARY]; Ca3Ti2O7 Cmc2_1 (36) mp-4163 [hull=0.003, icsd=2, PRIMARY]; CaTiO3 Pm-3m (221) mp-5827 [hull=0.064, icsd=12]; CaTiO3 I4/mcm (140) mp-3442 [hull=0.019, icsd=4]
- [ref 2] MP, ranked by ICSD evidence: CaTi2O6 C2/c (15) mp-1188864 [hull=0.177, icsd=2, PRIMARY]; Ca4Ti3O10 Pbca (61) mp-15315 [hull=0.002, icsd=1, PRIMARY]; Ca10Ti8NbFeO30 P-1 (2) mp-743819 [hull=0.000, PRIMARY]; CaTiO3 Cmcm (63) mp-1205364 [hull=0.013, icsd=2]; CaTi2O6 P-31m (162) mp-1079825 [hull=0.180, icsd=1]
- papers: https://doi.org/10.1016/j.matlet.2004.08.012 (Substitution effect on the thermoelectric properties of alkaline earth...) | https://doi.org/10.2320/matertrans.46.1466 (Thermoelectric Properties of Lanthanum-Doped Europium Titanate) | https://doi.org/10.1016/j.jallcom.2003.11.021 (Band filling dependence of the electrical transport of Nd1−xAxTiO3 (A=...)

## Ca-O-Zr
- rank 872 | 7 samples | 3 papers | 6 compositions
- compositions: CaZrO3 (2); CaMn0.1Zr0.9O3 (1); CaMn0.05Zr0.95O3 (1); CaMn0.15Zr0.85O3 (1); CaMn0.145Zr0.855O3 (1); CaMn0.24Zr0.76O3 (1)
- dopant candidates (<5% at.): Mn (5)
- measured range: 373-1473 K (5th-95th pct of 7 curves)
- [ref 1] TEDesignLab / ICSD: CaZrO3 Pnma (62) mp-4571 [hull=0.000, icsd=9, PRIMARY]; CaZrO3 (221)
- [ref 2] MP, ranked by ICSD evidence: Ca3Zr17O37 R3m (160) mp-674516 [hull=0.143, PRIMARY]; Ca3Zr2O7 Cmcm (63) mp-756052 [hull=0.047, PRIMARY]; CaZr4O9 C2/m (12) mp-675372 [hull=0.096, PRIMARY]; CaZrO3 Pba2 (32) mp-776024 [hull=0.025]
- papers: https://doi.org/10.1016/s0022-3115(01)00474-3 (Thermophysical properties of BaUO3) | https://doi.org/10.1016/j.ceramint.2022.09.166 (CaMn Zr(1-)O3: A novel NTC thermo-sensitive ceramic for applications i...) | https://doi.org/10.1016/j.ceramint.2023.05.082 (Vacancy defects reducing the accuracy and reliability of NTC sensors)

## Cd-Cu-In-Te
- rank 873 | 7 samples | 2 papers | 5 compositions
- compositions: Cd2Cu3In3Te8 (3); Cd1.9Cu3.1In3Te8 (1); Cd1.8Cu3.2In3Te8 (1); Cd1.7Cu3.3In3Te8 (1); Cd1.6Cu3.4In3Te8 (1)
- measured range: 311-970 K (5th-95th pct of 17 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cd2InCuTe4 I-42m (121) mp-1227025 [hull=0.014, PRIMARY]
- papers: https://doi.org/10.1021/acsaem.9b02004 (A2Cu3In3Te8 (A = Cd, Zn, Mn, Mg): A Type of Thermoelectric Material wi...) | https://doi.org/10.1016/j.mtphys.2020.100333 (Embedded in-situ nanodomains from chemical composition fluctuation in ...)

## Cd-Eu-Sb-Yb
- rank 874 | 7 samples | 3 papers | 7 compositions
- compositions: Yb0.75Eu0.25Cd2Sb2 (1); Yb0.5Eu0.5Cd2Sb2 (1); Yb1.64Eu0.36CdSb2 (1); Yb0.87Eu1.13CdSb2 (1); Yb1.15Eu0.85CdSb2 (1); Yb0.82Eu1.18CdSb2 (1)
- solid-solution axis: Eu/(Eu+Yb) spans 0.18-0.84 (median 0.50) over 7 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-650 K (5th-95th pct of 24 curves)
- papers: https://doi.org/10.1063/1.3501370 (Thermoelectric properties of YbxEu1−xCd2Sb2) | https://doi.org/10.1021/acs.chemmater.7b04517 (High Seebeck Coefficient and Unusually Low Thermal Conductivity Near A...) | https://doi.org/10.1021/acs.inorgchem.6b01947 (Synthesis, Characterization, and Low Temperature Transport Properties ...)

## Ce-Co-O-Sr
- rank 875 | 7 samples | 3 papers | 3 compositions
- compositions: Sr1.05Ce0.95CoO4 (3); SrCeCoO4 (3); Ce0.5Sr0.5Co0.8Fe0.2O3 (1)
- dopant candidates (<5% at.): Fe (1)
- measured range: 14-350 K (5th-95th pct of 7 curves; full span incl. outliers 14-873 K)
- papers: https://doi.org/10.1088/0022-3727/41/21/215009 (Structural, magnetic, electrical and thermal transport properties in t...) | https://doi.org/10.1088/0022-3727/41/4/045404 (Studies of structural, magnetic, electrical and thermal properties in ...) | https://doi.org/10.1016/j.jallcom.2019.03.301 (Highly conducting perovskite structured (M-SrCoFe-O3-δ, M = Ce, Ba) ca...)

## Co-Dy-O
- rank 876 | 7 samples | 4 papers | 4 compositions
- compositions: DyCoO3 (3); Dy0.9Ca0.1CoO3 (2); DyCo0.95Ni0.05O3 (1); Dy0.975Sr0.025CoO3 (1)
- dopant candidates (<5% at.): Ca (2), Ni (1), Sr (1)
- measured range: 153-1207 K (5th-95th pct of 14 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DyCoO3 Pnma (62) mp-24848 [hull=0.010, icsd=5, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2007.05.020 (High-temperature thermoelectric properties of Ln(Co, Ni)O3 (Ln=La, Pr,...) | https://doi.org/10.1016/j.jallcom.2009.04.100 (Influence of ionic sizes of rare earths on thermoelectric properties o...) | https://doi.org/10.2320/matertrans.m2009335 (Effects of Strontium Ion Doping on the Thermoelectric Properties of Dy...)

## Co-Fe-Nd-Sb
- rank 877 | 7 samples | 2 papers | 5 compositions
- compositions: Nd0.9Fe3CoSb12 (3); NdFe3CoSb12 (1); Nd1.0Fe3CoSb12 (1); Nd0.85Fe3CoSb12 (1); Nd0.95Fe3CoSb12 (1)
- measured range: 300-824 K (5th-95th pct of 35 curves)
- papers: https://doi.org/10.1007/s11664-015-3967-2 (Electronic Transport and Thermoelectric Properties of p-Type Nd z Fe4−...) | https://doi.org/10.1007/s11664-015-3997-9 (Super-rapid Preparation of Nanostructured Nd x Fe3CoSb12 Compounds and...)

## Co-Fe-Ni-Sb-Ti
- rank 878 | 7 samples | 2 papers | 6 compositions
- compositions: TiFe0.3Co0.2Ni0.5Sb (2); TiCo0.4(Ni0.5Fe0.5)0.6Sb (1); TiCo0.6(Ni0.5Fe0.5)0.4Sb (1); TiFe0.25Co0.25Ni0.5Sb (1); TiFe0.5Co0.2Ni0.3Sb (1); Ti0.85Hf0.15Fe0.3Co0.2Ni0.5Sb (1)
- dopant candidates (<5% at.): Hf (1)
- measured range: 10-974 K (5th-95th pct of 32 curves)
- papers: https://doi.org/10.1007/s11664-011-1517-0 (An Alternative Approach to Improve the Thermoelectric Properties of Ha...) | https://doi.org/10.1016/j.jmat.2020.12.015 (Enhanced thermoelectric performance in Ti(Fe, Co, Ni)Sb pseudo-ternary...)

## Co-Na-O-Ru
- rank 879 | 7 samples | 2 papers | 5 compositions
- compositions: Na0.71Co0.7Ru0.3O2 (2); Na0.71Co0.5Ru0.5O2 (2); Na0.71Co0.6Ru0.4O2 (1); Na0.71Co0.8Ru0.2O2 (1); NaCo2.5Ru0.5O4 (1)
- measured range: 10-388 K (5th-95th pct of 7 curves; full span incl. outliers 10-596 K)
- papers: https://doi.org/10.1016/j.jssc.2009.04.030 (Effect of ruthenium substitution in layered sodium cobaltate NaxCoO2: ...) | https://doi.org/10.1016/s0025-5408(00)00441-4 (Magnetic and thermoelectric properties of NaCo2−xMxO4 (M = Mn, Ru))

## Co-Nb-Sn-Ta
- rank 880 | 7 samples | 2 papers | 7 compositions
- compositions: CoNb0.5Ta0.5Sn (1); Ta0.6Nb0.4CoSn0.98Sb0.02 (1); Ta0.6Nb0.4CoSn (1); Ta0.6Nb0.4CoSn0.96Sb0.04 (1); Ta0.6Nb0.4CoSn0.94Sb0.06 (1); Ta0.6Nb0.4CoSn0.92Sb0.08 (1)
- dopant candidates (<5% at.): Sb (5)
- measured range: 298-974 K (5th-95th pct of 34 curves; full span incl. outliers 40-974 K)
- papers: https://doi.org/10.1016/j.jallcom.2004.04.096 (High temperature thermoelectric properties of CoTiSb half-Heusler comp...) | https://doi.org/10.1021/acsami.9b13603 (n-Type TaCoSn-Based Half-Heuslers as Promising Thermoelectric Materials)

## Co-Ni-Sn-Zr
- rank 881 | 7 samples | 3 papers | 7 compositions
- compositions: Zr30.5Ni32.2Co5.2Sn32.1 (1); Zr30.3Ni28.8Co9.6Sn31.3 (1); Zr30.1Ni25.6Co13.9Sn30.4 (1); ZrNi0.80Co0.20Sn (1); ZrNi0.70Co0.30Sn (1); ZrNiCo0.4Sn (1)
- measured range: 301-1052 K (5th-95th pct of 26 curves)
- papers: https://doi.org/10.1016/j.actamat.2010.04.028 (Vacancy site occupation by Co and Ir in half-Heusler ZrNiSn and conver...) | https://doi.org/10.2497/jjspm.57.218 (Effect of Transition Element Substitution on the p-type Thermoelectric...) | https://doi.org/10.1007/s11837-014-1233-3 (Ordered Structures and Thermoelectric Properties of MNiSn (M = Ti, Zr,...)

## Co-Rh-Si-Yb
- rank 882 | 7 samples | 1 papers | 7 compositions
- compositions: Yb(Rh0.82Co0.18)2Si2 (1); Yb(Rh0.805Co0.195)2Si2 (1); Yb(Rh0.32Co0.68)2Si2 (1); Yb(Rh0.22Co0.78)2Si2 (1); Yb(Rh0.73Co0.27)2Si2 (1); Yb(Rh0.62Co0.38)2Si2 (1)
- solid-solution axis: Co/(Co+Rh) spans 0.18-0.78 (median 0.38) over 7 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-309 K (5th-95th pct of 7 curves)
- papers: https://doi.org/10.1007/s10909-019-02187-6 (Thermopower Evolution in Yb(\n                \n                  \n  ...)

## Cr-Cu-Se
- rank 883 | 7 samples | 4 papers | 3 compositions
- compositions: CuCrSe2 (5); CuCr1.64V0.22Se4 (1); CuCr1.79V0.08Se4 (1)
- dopant candidates (<5% at.): V (2)
- measured range: 12-786 K (5th-95th pct of 25 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cr2CuSe4 Fd-3m (227) mp-3880 [hull=0.000, icsd=14, PRIMARY]; CrCuSe2 R3m (160) mp-7861 [hull=0.247, icsd=1, PRIMARY]; Cr4Cu3Se8 Imm2 (44) mp-674310 [hull=0.033, PRIMARY]; Cr8CoCu3Se16 P-4m2 (115) mp-1226059 [hull=0.018, PRIMARY]; ZnCr8Cu3Se16 R3m (160) mp-1215824 [hull=0.003, PRIMARY]
- papers: https://doi.org/10.1039/c3ta11903c (CuCrSe2: a high performance phonon glass and electron crystal thermoel...) | https://doi.org/10.1016/j.jpcs.2011.10.032 (Thermoelectric power of CuCrxVySe4 p-type spinel semiconductors) | https://doi.org/10.1111/jace.13860 (CuCrSe2\n Ternary Chromium Chalcogenide: Facile Fabrication, Doping an...)

## Cr-Ge-La
- rank 884 | 7 samples | 2 papers | 1 compositions
- compositions: LaCrGe3 (7)
- measured range: 10-302 K (5th-95th pct of 8 curves; full span incl. outliers 10-408 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaCrGe3 P6_3/mmc (194) mp-1080078 [hull=0.000, icsd=5, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/26/10/106001 (Heavy fermion and Kondo lattice behavior in the itinerant ferromagnet ...) | https://doi.org/10.1103/physrevlett.117.037207 (Ferromagnetic Quantum Critical Point Avoided by the Appearance of Anot...)

## Cr-Ni-S
- rank 885 | 7 samples | 1 papers | 1 compositions
- compositions: NiCr2S4 (7)
- measured range: 305-576 K (5th-95th pct of 21 curves)
- [ref 1] TEDesignLab / ICSD: Cr2NiS4 C2/m (12) mp-27512 [hull=0.056, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Cr11NiS16 P-1 (2) mp-1226263 [hull=0.026, PRIMARY, AMBIGUOUS]; Cr5NiS8 P-1 (2) mp-1226452 [hull=0.012, PRIMARY]; Cr11NiS16 C2/m (12) mp-1226505 [hull=0.030]; Cr5NiS8 P2/m (10) mp-1226130 [hull=0.028]
- papers: https://doi.org/10.1007/s11664-013-2941-0 (Ordered-Defect Sulfides as Thermoelectric Materials)

## Cr-Ru-Sb
- rank 886 | 7 samples | 1 papers | 7 compositions
- compositions: Cr0.8Ru0.2Sb2 (1); Cr0.7Ru0.3Sb2 (1); Cr0.4Ru0.6Sb2 (1); Cr0.3Ru0.7Sb2 (1); Cr0.2Ru0.8Sb2 (1); Cr0.6Ru0.4Sb2 (1)
- measured range: 78-629 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1016/j.jallcom.2004.04.058 (Structural and electrical properties of Cr1−xRuxSb2)

## Cu-In-La
- rank 887 | 7 samples | 4 papers | 6 compositions
- compositions: LaInCu2 (2); (Ce0.2La0.8)Cu5In (1); LaCu5In (1); Ce0.1La0.9Cu4In (1); Ce0.2La0.8Cu4In (1); LaCu4In (1)
- dopant candidates (<5% at.): Ce (3)
- measured range: 10-299 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaInCu2 Fm-3m (225) mp-20491 [hull=0.017, icsd=4, PRIMARY]; LaInCu5 Pnnm (58) mp-1203883 [hull=0.000, icsd=1, PRIMARY]; LaIn2Cu9 P4/mbm (127) mp-1211998 [hull=0.000, PRIMARY]; La2(InCu3)3 Pnnm (58) mp-1224933 [hull=0.020, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/16/12/007 (Specific heat, susceptibility, magnetotransport and thermoelectric pow...) | https://doi.org/10.1007/bf00683635 (Thermpower of Ce x Y1?x InCu2 and CeInCu y Ag2?y) | https://doi.org/10.1016/j.surfin.2019.100413 (Electrical resistivity, magnetic properties and thermoelectric power f...)

## Cu-La
- rank 888 | 7 samples | 3 papers | 5 compositions
- compositions: La2Cu04 (3); LaCu6 (1); Ce0.18La0.82Cu6 (1); Ce0.094La0.906Cu6 (1); Ce0.29La0.71Cu6 (1)
- dopant candidates (<5% at.): Ce (3)
- measured range: 10-292 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaCu5 P6/mmm (191) mp-2613 [hull=0.000, icsd=10, PRIMARY]; LaCu2 P6/mmm (191) mp-2051 [hull=0.000, icsd=4, PRIMARY]; LaCu6 Pnma (62) mp-636256 [hull=0.006, icsd=3, PRIMARY]; LaCu Pnma (62) mp-1078920 [hull=0.000, icsd=1, PRIMARY]; LaCu13 Fm-3c (226) mp-1194443 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(85)90302-6 (Point contact spectra and transport properties of the dense Kondo subs...) | https://doi.org/10.1016/0304-8853(87)90587-7 (Heavy fermion state in CeCu6) | https://doi.org/10.1103/physrevlett.58.2482 (Evidence for superconductivity inLa2CuO4)

## Cu-Mg-Se-Sn
- rank 889 | 7 samples | 1 papers | 7 compositions
- compositions: Cu2MgSnSe4 (1); Cu2.05Mg0.95SnSe4 (1); Cu2MgSn0.95In0.05Se4 (1); Cu2MgSn0.925In0.075Se4 (1); Cu2MgSn0.9In0.1Se4 (1); Cu2.075Mg0.925SnSe4 (1)
- dopant candidates (<5% at.): In (3)
- measured range: 304-714 K (5th-95th pct of 32 curves)
- papers: https://doi.org/10.1063/1.4933277 (A new wide band gap thermoelectric quaternary selenide Cu2MgSnSe4)

## Cu-Mn-O
- rank 890 | 7 samples | 2 papers | 7 compositions
- compositions: CuMnO2 (1); CuMn1.1O2 (1); CuMn1.15O2 (1); CuMn1.2O2 (1); CuMn1.05O2 (1); CuMn1.143O2 (1)
- measured range: 298-573 K (5th-95th pct of 31 curves; full span incl. outliers 21-574 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn3Cu3O8 P4_332 (212) mp-652534 [hull=0.017, icsd=1, PRIMARY]; Mn11Cu7O24 P1 (1) mp-765492 [hull=0.026, PRIMARY, AMBIGUOUS]; Mn(Cu3O4)2 Fm-3m (225) mp-769761 [hull=0.000, PRIMARY]; Mn13Cu11O32 C2/m (12) mp-1176662 [hull=0.020, PRIMARY]; Mn2CuO4 Cm (8) mp-34237 [hull=0.039, PRIMARY]
- papers: https://doi.org/10.1016/j.ceramint.2015.06.058 (Fabrication and thermoelectric properties of CuMn1+xO2 (x=0~0.2) ceramics) | https://doi.org/10.1103/physrevb.105.054409 (<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:mrow><...)

## Cu-Mo-S
- rank 891 | 7 samples | 3 papers | 7 compositions
- compositions: Cu4.0Mo6S8 (1); Cu4Mo6S8 (1); Cu2Mo6S8 (1); Cu2.5Mo6S8 (1); Cu3.5Mo6S8 (1); Cu3Mo6S8 (1)
- measured range: 301-953 K (5th-95th pct of 27 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu(Mo3S4)2 P1 (1) mp-675745 [hull=0.069, PRIMARY]; Cu3(Mo3S4)4 P1 (1) mp-675781 [hull=0.072, PRIMARY]
- papers: https://doi.org/10.1007/s11664-009-0975-0 (Thermoelectric Properties of Chevrel-Phase Sulfides M x Mo6S8 (M: Cr, ...) | https://doi.org/10.2320/matertrans.maw200918 (Preparation and Thermoelectric Properties of Chevrel-Phase Cu<I><SUB>x...) | https://doi.org/10.1016/j.apsusc.2019.144066 (Thermoelectric performance of Cu-doped MoS2 layered nanosheets for low...)

## Dy-S
- rank 892 | 7 samples | 1 papers | 7 compositions
- compositions: Cu0.100(Dy2S3)0.900 (1); Cu0.125(Dy2S3)0.875 (1); Cu0.006(Dy2S3)0.994 (1); Cu0.034(Dy2S3)0.966 (1); Cu0.039(Dy2S3)0.961 (1); Cu0.075(Dy2S3)0.925 (1)
- dopant candidates (<5% at.): Cu (7)
- measured range: 295-1275 K (5th-95th pct of 22 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DyS Fm-3m (225) mp-2470 [hull=0.000, icsd=4, PRIMARY]; Dy2S3 Pnma (62) mp-1270 [hull=0.000, icsd=2, PRIMARY]; DyS2 P4/nmm (129) mp-1018675 [hull=0.000, icsd=1, PRIMARY]; Dy5S7 C2/m (12) mp-1103125 [hull=0.000, icsd=1, PRIMARY]; DyS2 Fd-3m (227) mp-16328 [hull=1.608, icsd=1]
- papers: https://doi.org/10.1063/1.357900 (Thermoelectric properties of Cu‐doped dysprosium sesquisulfide)

## Er-Pd-Sb
- rank 893 | 7 samples | 6 papers | 2 compositions
- compositions: ErPdSb (6); ErPd2Sb (1)
- measured range: 10-992 K (5th-95th pct of 18 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Er3(SbPd2)4 Fm-3m (225) mp-1193806 [hull=0.032, icsd=1, PRIMARY]; ErSbPd F-43m (216) mp-11836 [hull=0.000, icsd=1, PRIMARY]; Er5SbPd2 I4/mcm (140) mp-1213250 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1063/1.2196109 (Thermoelectric and thermophysical properties of ErPdX (X=Sb and Bi) ha...) | https://doi.org/10.1109/ict.2005.1519966 (Physical properties of rare-earth-based Heusler phases REPdZ and REPd/...) | https://doi.org/10.1063/1.2756045 (High-temperature Hall measurements of lanthanide based ternary interme...)

## F-Mg
- rank 894 | 7 samples | 1 papers | 1 compositions
- compositions: MgF2 (7)
- measured range: 318-1108 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MgF2 P4_2/mnm (136) mp-1249 [hull=0.000, icsd=23, PRIMARY]; MgF3 I4/mmm (139) mp-1185862 [hull=0.481, PRIMARY]; MgF2 Pa-3 (205) mp-1746 [hull=0.067, icsd=6]; MgF2 Pnnm (58) mp-1072956 [hull=0.037, icsd=3]; MgF2 Pnma (62) mp-1102433 [hull=0.213, icsd=1]
- papers: https://doi.org/10.1111/j.1151-2916.1975.tb18765.x (Reproducibilities of Some Physical Properties of MgF2)

## Fe-Hf-Ni-Sb-Ti
- rank 895 | 7 samples | 3 papers | 7 compositions
- compositions: Ti0.7Hf0.3Fe0.6Ni0.4Sb (1); Ti0.8Hf0.2Fe0.6Ni0.4Sb (1); Ti1.6Hf0.4FeNiSb1.7Sn0.3 (1); Ti1.4Hf0.6FeNiSb1.7Sn0.3 (1); TiHfFeNiSb1.7Sn0.3 (1); Ti0.8Hf0.2Fe0.5Co0.15Ni0.35Sb (1)
- dopant candidates (<5% at.): Sn (3), Co (2)
- solid-solution axis: Hf/(Hf+Ti) spans 0.20-0.50 (median 0.25) over 7 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 299-974 K (5th-95th pct of 25 curves)
- papers: https://doi.org/10.1002/adfm.201905044 (Design of High‐Performance Disordered Half‐Heusler Thermoelectric Mate...) | https://doi.org/10.1002/pssa.202000096 (Enhanced Thermoelectric Properties in p‐Type Double Half‐Heusler Ti<su...) | https://doi.org/10.1016/j.jmat.2020.12.015 (Enhanced thermoelectric performance in Ti(Fe, Co, Ni)Sb pseudo-ternary...)

## Fe-Hf-Sb-Ti-V
- rank 896 | 7 samples | 4 papers | 3 compositions
- compositions: Fe(V0.8Hf0.2)0.8Ti0.2Sb (3); FeV0.49Nb0.15Hf0.16Ti0.2Sb (2); FeV0.64Hf0.16Ti0.2Sb (2)
- dopant candidates (<5% at.): Nb (2)
- measured range: 99-901 K (5th-95th pct of 38 curves)
- papers: https://doi.org/10.1016/j.jpowsour.2020.228768 (Optimizing the thermoelectric performance of FeVSb half-Heusler compou...) | https://doi.org/10.1016/j.jpcs.2020.109848 (Effects of spark plasma sintering on enhancing the thermoelectric perf...) | https://doi.org/10.1016/j.jallcom.2021.161838 (Transport and thermoelectric properties of Nb-doped FeV0.64Hf0.16Ti0.2...)

## Fe-Nd-Sb
- rank 897 | 7 samples | 4 papers | 5 compositions
- compositions: NdFe3.5Co0.5Sb12 (2); NdFe4Sb12 (2); Nd0.9Fe4Sb12 (1); Nd0.9Fe3.5Co0.5Sb12 (1); Nd0.9Fe3Sb12 (1)
- dopant candidates (<5% at.): Co (3)
- measured range: 297-873 K (5th-95th pct of 39 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd(FeSb3)4 Im-3 (204) mp-15026 [hull=0.000, icsd=1, PRIMARY]; NdFeSb3 Pbcm (57) mp-1201926 [hull=0.014, icsd=1, PRIMARY]; Nd2FeSb4 P-4m2 (115) mp-1220376 [hull=0.074, PRIMARY]; Nd3Fe3Sb7 P6_3/m (176) mp-1209931 [hull=0.021, PRIMARY]
- papers: https://doi.org/10.1002/aenm.201200503 (Skutterudite Unicouple Characterization for Energy Harvesting Applicat...) | https://doi.org/10.1063/1.3553842 (High-temperature electrical and thermal transport properties of fully ...) | https://doi.org/10.1007/s11664-015-3967-2 (Electronic Transport and Thermoelectric Properties of p-Type Nd z Fe4−...)

## Ga-In-Te-Tl
- rank 898 | 7 samples | 1 papers | 7 compositions
- compositions: TlIn0.7Ga0.3Te2 (1); TlIn0.6Ga0.4Te2 (1); TlIn0.5Ga0.5Te2 (1); TlIn0.3Ga0.7Te2 (1); TlIn0.8Ga0.2Te2 (1); TlIn0.4Ga0.6Te2 (1)
- solid-solution axis: Ga/(Ga+In) spans 0.20-0.80 (median 0.50) over 7 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 276-877 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TlIn2GaTe4 I222 (23) mp-1216591 [hull=0.024, PRIMARY]
- papers: https://doi.org/10.1134/s002016851007006x (X-ray diffraction characterization and electrical properties of TlIn1 ...)

## Ga-La-O
- rank 899 | 7 samples | 2 papers | 7 compositions
- compositions: La3Ga5.5Ta0.5O14 (1); La2Ga5SiO14 (1); (La0.85Sr0.15Ga0.8Mg0.2O2.825)91(Ce0.85Sm0.15O1.925)9.4 (1); (La0.85Sr0.15Ga0.8Mg0.2O2.825)97(Ce0.85Sm0.15O1.925)2.7 (1); La0.85Sr0.15Ga0.8Mg0.2O2.825 (1); (La0.85Sr0.15Ga0.8Mg0.2O2.825)8.7(Ce0.85Sm0.15O1.925)1.3 (1)
- dopant candidates (<5% at.): Mg (5), Sr (5), Ce (4), Sm (4), Ta (1), Si (1)
- measured range: 299-1073 K (5th-95th pct of 7 curves)
- [ref 1] TEDesignLab / ICSD: LaGaO3 R-3c (167) mp-3336 [hull=0.038, icsd=24, PRIMARY]; La3Ga5SnO14 P321 (150) mp-6788 [hull=0.000, icsd=2, PRIMARY]; LaGaO3 Pnma (62) mp-5837 [hull=0.032, icsd=18]; LaGaO3 R3c (161) mp-1078871 [hull=0.038, icsd=7]
- [ref 2] MP, ranked by ICSD evidence: La4Ga2O9 P2_1/c (14) mp-769915 [hull=0.000, icsd=1, PRIMARY]; La12Ga23WO56 P1 (1) mp-1223721 [hull=0.016, PRIMARY]; La10Mg(Ga3O10)3 P-1 (2) mp-695030 [hull=0.047, PRIMARY]; La12Ga23MoO56 P1 (1) mp-1224232 [hull=0.017, PRIMARY]; LaGaO3 Pm-3m (221) mp-1097026 [hull=0.096, icsd=1]
- papers: https://doi.org/10.1063/1.4891827 (Investigations on the thermal and piezoelectric properties of fresnoit...) | https://doi.org/10.1016/j.jeurceramsoc.2015.08.036 (Analysis of the microstructure and physical properties of La 0.85 Sr 0...)

## Ga-Mg
- rank 900 | 7 samples | 1 papers | 7 compositions
- compositions: (Mg2)1.08(Si0.3Sn0.7)0.05Ga0.95 (1); Mg2(Si0.3Sn0.7)0.05Ga0.95 (1); (Mg2)0.95(Si0.3Sn0.7)0.05Ga0.95 (1); (Mg2)1.025(Si0.3Sn0.7)0.05Ga0.95 (1); (Mg2)1.12(Si0.3Sn0.7)0.05Ga0.95 (1); (Mg2)1.05(Si0.3Sn0.7)0.05Ga0.95 (1)
- dopant candidates (<5% at.): Sn (7), Si (7)
- measured range: 298-802 K (5th-95th pct of 28 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MgGa2 P6_3/mmc (194) mp-30651 [hull=0.009, icsd=2, PRIMARY]; Mg5Ga2 Ibam (72) mp-1770 [hull=0.000, icsd=2, PRIMARY]; Mg2Ga5 I4/mmm (139) mp-27668 [hull=0.000, icsd=1, PRIMARY]; Mg2Ga P-62c (190) mp-30650 [hull=0.000, icsd=1, PRIMARY]; Mg149Ga P-6m2 (187) mp-1185597 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2012.07.027 (Enhanced hole concentration through Ga doping and excess of Mg and the...)
