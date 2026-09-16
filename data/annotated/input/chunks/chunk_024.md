# Host systems -- chunk 024 of 73

Ranks 1151-1200 by sample count. These 50 host systems cover 250 samples (0.48% of the TE set); cumulative through this chunk: 91.17%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Ca-Fe-O-Sm
- rank 1151 | 5 samples | 4 papers | 4 compositions
- compositions: Sm0.6Ca0.4FeO3 (2); Sm0.5Ca0.5FeO3 (1); Sm0.75Ca0.25FeO3 (1); Sm0.7Ca0.3FeO3 (1)
- measured range: 295-1273 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/j.ssi.2017.12.038 (Oxygen permeation properties of mixed conductive Sm0.5Ca0.5FeO3) | https://doi.org/10.2109/jcersj2.16280 (Crystal structure and oxygen permeation properties of Sm&lt;sub&gt;1&a...) | https://doi.org/10.1016/j.memsci.2014.03.047 (Comparative investigation of dual-phase membranes containing cobalt an...)

## Ca-Mn-O-Sm-Sr
- rank 1152 | 5 samples | 2 papers | 2 compositions
- compositions: Sm0.5Ca0.25Sr0.25MnO3 (4); Sm0.50Sr0.25Ca0.25MnO3 (1)
- measured range: 15-296 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1088/0953-8984/20/7/075221 (Phase separation and stability in Sm0.50Sr0.50MnO3: effects of cation ...) | https://doi.org/10.1038/s41427-018-0085-7 (Huge magnetoresistance and ultrasharp metamagnetic transition in polyc...)

## Ca-Mo-O-V
- rank 1153 | 5 samples | 2 papers | 5 compositions
- compositions: Ca(V0.5Mo0.5)O3 (1); CaV0.7Mo0.3O3 (1); CaV0.5Mo0.5O3 (1); CaV0.6Mo0.4O3 (1); CaV0.4Mo0.6O3 (1)
- measured range: 299-1123 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca2VMoO6 P2_1/c (14) mp-1227834 [hull=0.054, PRIMARY]
- papers: https://doi.org/10.1016/j.jpowsour.2008.12.035 (Structure, thermal stability and electrical properties of Ca(V0.5Mo0.5...) | https://doi.org/10.1016/j.materresbull.2020.110904 (The effect of Mo concentration on the electrical properties of CaV1-xM...)

## Ca-O-V-Y
- rank 1154 | 5 samples | 1 papers | 5 compositions
- compositions: Ca0.7Y0.3VO3 (1); Ca0.6Y0.4VO3 (1); Ca0.5Y0.5VO3 (1); Ca0.4Y0.6VO3 (1); Ca0.3Y0.7VO3 (1)
- measured range: 18-298 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1007/s12043-002-0164-7 (Local-moment formation and metal-nonmetal transition in Ca1−x Y x VO3 ...)

## Ca-P-Zn
- rank 1155 | 5 samples | 2 papers | 4 compositions
- compositions: CaZn1.9Cu0.1P2 (2); Ca0.99Na0.01Zn2P2 (1); CaZn1.8Cu0.2P2 (1); CaZn2P2 (1)
- dopant candidates (<5% at.): Cu (3), Na (1)
- measured range: 78-990 K (5th-95th pct of 21 curves; full span incl. outliers 77-1073 K)
- [ref 1] TEDesignLab / ICSD: Ca(ZnP)2 P-3m1 (164) mp-9569 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1007/s11664-013-2895-2 (Thermoelectric Properties of Light-Element-Containing Zintl Compounds ...) | https://doi.org/10.1088/0022-3727/44/15/155406 (High Seebeck coefficientAMXP2(A= Ca and Yb;M,X= Zn, Cu and Mn) Zintl p...)

## Ca-Si
- rank 1156 | 5 samples | 2 papers | 5 compositions
- compositions: CaSi (1); Ca5Si3 (1); Ca2Na0.00006Si (1); Ca2Na0.0001Si (1); Ca2Na0.0002Si (1)
- dopant candidates (<5% at.): Na (3)
- measured range: 297-972 K (5th-95th pct of 11 curves)
- [ref 1] TEDesignLab / ICSD: Ca2Si Pnma (62) mp-2517 [hull=0.000, icsd=5, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: CaSi2 I4_1/amd (141) mp-862 [hull=0.013, icsd=15, PRIMARY]; CaSi Cmcm (63) mp-1563 [hull=0.000, icsd=14, PRIMARY]; Ca5Si3 I4/mcm (140) mp-793 [hull=0.000, icsd=2, PRIMARY]; CaSi3 I4/mmm (139) mp-1205346 [hull=0.092, icsd=1, PRIMARY]; Ca14Si19 R-3c (167) mp-29013 [hull=0.003, icsd=1, PRIMARY]
- papers: https://doi.org/10.1109/ict.2006.331351 (Thermoelectric properties of calcium silicides) | https://doi.org/10.1088/1757-899x/18/14/142014 (Effect of Na Addition on Electric Properties of Ca2Si Sintered Compacts)

## Cd-Fe-Ni-O
- rank 1157 | 5 samples | 2 papers | 3 compositions
- compositions: Cd0.6Ni0.4Fe2O4 (2); Cd0.4Ni0.6Fe2O4 (2); Cd0.5Ni0.5Fe2O4 (1)
- measured range: 298-931 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CdFe4NiO8 R3m (160) mp-1226789 [hull=0.066, PRIMARY]
- papers: https://doi.org/10.1007/bf02745227 (DC resistivity and thermoelectric power in Ni-Cd ferrites) | https://doi.org/10.1023/a:1013790129045 ([])

## Cd-Mn-Sb-Yb
- rank 1158 | 5 samples | 1 papers | 5 compositions
- compositions: YbCd1.4Mn0.6Sb2 (1); YbCdMnSb2 (1); YbCd0.5Mn1.5Sb2 (1); YbCd1.2Mn0.8Sb2 (1); YbCd1.6Mn0.4Sb2 (1)
- measured range: 298-651 K (5th-95th pct of 25 curves)
- papers: https://doi.org/10.1002/ejic.201100282 (Enhanced Thermoelectric Figure of Merit of Zintl Phase YbCd2-xMnxSb2 b...)

## Ce-Co-Fe-Ge
- rank 1159 | 5 samples | 1 papers | 5 compositions
- compositions: CeCo0.7Fe0.3Ge3 (1); CeCo0.5Fe0.5Ge3 (1); CeCo0.4Fe0.6Ge3 (1); CeCo0.3Fe0.7Ge3 (1); CeCo0.6Fe0.4Ge3 (1)
- measured range: 10-300 K (5th-95th pct of 9 curves)
- papers: https://doi.org/10.1016/j.jallcom.2019.151850 (Comprehensive studies of the transformation between antiferromagnetic ...)

## Ce-Co-Fe-La-Sb
- rank 1160 | 5 samples | 2 papers | 1 compositions
- compositions: LaCeFe3CoSb12 (5)
- measured range: 330-774 K (5th-95th pct of 20 curves)
- papers: https://doi.org/10.1016/j.jallcom.2010.06.040 (Thermoelectric properties of rare earths filled CoSb3 based nanostruct...) | https://doi.org/10.1557/jmr.2012.90 (Effects of disordered structure on thermoelectric properties of LaCeFe...)

## Ce-Cu-In-La
- rank 1161 | 5 samples | 2 papers | 5 compositions
- compositions: (Ce0.5La0.5)Cu5In (1); (Ce0.6La0.4)Cu5In (1); (Ce0.4La0.6)Cu5In (1); Ce0.6La0.4Cu4In (1); Ce0.4La0.6Cu4In (1)
- solid-solution axis: Ce/(Ce+La) spans 0.40-0.60 (median 0.50) over 5 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-314 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.1088/0953-8984/16/12/007 (Specific heat, susceptibility, magnetotransport and thermoelectric pow...) | https://doi.org/10.1016/j.surfin.2019.100413 (Electrical resistivity, magnetic properties and thermoelectric power f...)

## Ce-Fe-Ge
- rank 1162 | 5 samples | 3 papers | 4 compositions
- compositions: CeFeGe3 (2); CeCo0.2Fe0.8Ge3 (1); CeCo0.1Fe0.9Ge3 (1); CeFe2Ge2 (1)
- dopant candidates (<5% at.): Co (2)
- measured range: 10-311 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(FeGe)2 I4/mmm (139) mp-21882 [hull=0.000, icsd=4, PRIMARY]; CeFeGe3 I4mm (107) mp-20722 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.52.10136 (CeFeGe3: A concentrated Kondo compound with a stable valency and high ...) | https://doi.org/10.1016/j.jallcom.2019.151850 (Comprehensive studies of the transformation between antiferromagnetic ...) | https://doi.org/10.1103/physrevb.93.085104 (Anomalous frequency and temperature-dependent scattering and Hund's co...)

## Ce-Ga
- rank 1163 | 5 samples | 3 papers | 2 compositions
- compositions: CeGa2 (4); CePd0.2Ga3.8 (1)
- dopant candidates (<5% at.): Pd (1)
- measured range: 10-293 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeGa2 P6/mmm (191) mp-912227 [hull=0.000, icsd=12, PRIMARY]; CeGa Cmcm (63) mp-1018276 [hull=0.000, icsd=4, PRIMARY]; CeGa6 P4/nbm (125) mp-711 [hull=0.000, icsd=4, PRIMARY]; Ce3Ga Pm-3m (221) mp-19920 [hull=0.000, icsd=3, PRIMARY]; Ce3Ga2 P4_2/mnm (136) mp-1106087 [hull=0.031, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2015.07.007 (Suppression of ferromagnetism in solid solution CePdxGa4−x) | https://doi.org/10.1088/0953-8984/4/20/009 (Thermoelectric power and resistivity studies in the Kondo-lattice syst...) | https://doi.org/10.1016/0921-4526(93)90665-s (Transport properties of RGa2 (R=La, Ce and Sm))

## Ce-Ge-Pt-Sb
- rank 1164 | 5 samples | 1 papers | 5 compositions
- compositions: CePt4Ge10.5Sb1.5 (1); CePt4Ge9Sb3 (1); CePt4Ge11Sb (1); CePt4Ge10Sb2 (1); CePt4Ge9.5Sb2.5 (1)
- measured range: 10-144 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1103/physrevb.90.235104 (Probing strong Kondo disorder with measurements of thermoelectric power)

## Ce-Ge-Ti
- rank 1165 | 5 samples | 2 papers | 4 compositions
- compositions: CeTiGe (2); CeTi1Ge3 (1); CeTi0.9Ni0.1Ge3 (1); CeTi0.8Ni0.2Ge3 (1)
- dopant candidates (<5% at.): Ni (2)
- measured range: 10-299 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeTiGe P4/nmm (129) mp-19860 [hull=0.008, icsd=1, PRIMARY]; CeTiGe3 P6_3/mmc (194) mp-1205531 [hull=0.000, PRIMARY]; CeTiGe I4/mmm (139) mp-1077736 [hull=0.028, icsd=1]
- papers: https://doi.org/10.1088/0953-8984/22/14/146003 (New high temperature modification of CeTiGe: structural characterizati...) | https://doi.org/10.1088/2053-1591/3/10/106101 (Ferromagnetic quantum critical behavior in heavy-fermion compounds CeT...)

## Ce-In-La
- rank 1166 | 5 samples | 2 papers | 5 compositions
- compositions: (Ce0.2La0.8)In3 (1); (Ce0.4La0.6)In3 (1); (Ce0.8La0.2)In3 (1); (Ce0.6La0.4)In3 (1); (Ce0.2La0.8)In2.88 (1)
- solid-solution axis: Ce/(Ce+La) spans 0.20-0.80 (median 0.40) over 5 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 11-291 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaCeIn6 P4/mmm (123) mp-1223179 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(85)90291-4 (Thermoelectric power and electrical resistivity of Ce(In1-xSnx)3 and (...) | https://doi.org/10.1016/0304-8853(87)90671-8 (Thermoelectric power of some Ce compounds of the dilute Kondo type)

## Ce-In-Rh
- rank 1167 | 5 samples | 3 papers | 4 compositions
- compositions: CeRhIn5 (2); CeRhIn (1); CeRh0.9Ge0.1In (1); Ce2Rh2In (1)
- dopant candidates (<5% at.): Ge (1)
- measured range: 10-299 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeIn5Rh P4/mmm (123) mp-20294 [hull=0.000, icsd=5, PRIMARY]; CeInRh P-62m (189) mp-1079553 [hull=0.000, icsd=3, PRIMARY]; Ce2In8Rh P4/mmm (123) mp-1206465 [hull=0.000, PRIMARY]; CeIn2Rh Cmcm (63) mp-1206576 [hull=0.022, PRIMARY]; Ce2InRh2 P4/mbm (127) mp-1205710 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2014.09.001 (Electronic properties of CeRh1−xGexIn; evolution from an intermediate-...) | https://doi.org/10.1103/physrevlett.120.187002 (Tuning the Pairing Interaction in a \nd\n-Wave Superconductor by Param...) | https://doi.org/10.1016/j.ssc.2006.03.016 (Thermoelectric power of Ce-based intermediate valent systems)

## Ce-Pd-Pt
- rank 1168 | 5 samples | 2 papers | 2 compositions
- compositions: CePd2Pt (3); CePd2.5Pt0.5 (2)
- measured range: 82-342 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CePd2Pt P4/mmm (123) mp-1226474 [hull=0.000, PRIMARY]; CePdPt4 P-6m2 (187) mp-1226749 [hull=0.006, PRIMARY]
- papers: https://doi.org/10.1063/1.4751265 (Enhanced thermoelectric properties of CePd3−xPtx) | https://doi.org/10.1007/s11664-012-2328-7 (Structural, Magnetic, and Thermoelectric Properties of Some CePd3-Base...)

## Ce-Pt-Sn
- rank 1169 | 5 samples | 2 papers | 1 compositions
- compositions: CePtSn (5)
- measured range: 10-297 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeSnPt Pnma (62) mp-20834 [hull=0.000, icsd=3, PRIMARY]; Ce(SnPt)2 P4/nmm (129) mp-672267 [hull=0.046, icsd=2, PRIMARY]; Ce4Sn25Pt12 Im-3 (204) mp-640776 [hull=0.018, icsd=1, PRIMARY]; CeSnPt P-62m (189) mp-22763 [hull=0.005, icsd=1]
- papers: https://doi.org/10.1016/0921-4526(94)90919-9 (Thermopower and resistivity of CeRhSb and CePtSn) | https://doi.org/10.1016/s0304-8853(10)80151-9 (Magnetic, transport and specific heat measurements on CeTX (T = Pd and...)

## Ce-Ru-Sb
- rank 1170 | 5 samples | 4 papers | 1 compositions
- compositions: CeRu4Sb12 (5)
- measured range: 11-844 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(Sb3Ru)4 Im-3 (204) mp-1189811 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.7566/jpsj.82.124608 (Influence of Ru Substitution on the Thermoelectric Properties of Ce(Fe...) | https://doi.org/10.1088/0953-8984/14/45/317 (Transport properties in the filled-skutterudite compounds RERu4Sb12 (R...) | https://doi.org/10.1016/j.jssc.2016.05.027 (FP-LAPW calculations of the elastic, electronic and thermoelectric pro...)

## Cl-Pb-S
- rank 1171 | 5 samples | 2 papers | 5 compositions
- compositions: PbS0.9Cl0.1 (1); (Pb0.99Bi0.01S)(Pb0.067Cl0.134) (1); (Pb0.985Bi0.015S)(Pb0.067Cl0.134) (1); (Pb0.995Bi0.005S)(Pb0.067Cl0.134) (1); (PbS)(Pb0.067Cl0.134) (1)
- dopant candidates (<5% at.): Bi (3)
- measured range: 297-824 K (5th-95th pct of 24 curves)
- papers: https://doi.org/10.1016/j.jallcom.2015.10.052 (High performance thermoelectrics from earth-abundant materials: Enhanc...) | https://doi.org/10.1016/j.jallcom.2020.157788 (Enhanced thermoelectric properties of n-type Cl doped PbS-based materi...)

## Co-Cu-O-S-Sr
- rank 1172 | 5 samples | 1 papers | 5 compositions
- compositions: Sr2Cu2CoO2S2 (1); Sr1.7Cu2CoO2S2 (1); Sr1.5Cu2CoO2S2 (1); Sr1.6Ca0.4Cu2CoO2S2 (1); Sr1.9Cu2CoO2S2 (1)
- dopant candidates (<5% at.): Ca (1)
- measured range: 22-296 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1063/1.2173638 (Electronic nature of layered oxysulfide Sr2−xCaxCu2CoO2S2 with CoO2 pl...)

## Co-Fe-Nd-O-Sr
- rank 1173 | 5 samples | 2 papers | 5 compositions
- compositions: Nd0.7Sr0.3Fe0.7Co0.3O3 (1); Nd0.5Sr0.5Fe0.7Co0.3O3 (1); Nd0.3Sr0.7Fe0.7Co0.3O3 (1); Nd0.7Sr0.3Fe0.6Co0.4O3 (1); Nd0.7Sr0.3Fe0.4Co0.6O3 (1)
- measured range: 297-1358 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/j.ssi.2016.08.005 (Crystal structure, oxygen nonstoichiometry, thermal expansion and cond...) | https://doi.org/10.1016/s0921-5107(02)00058-2 (Crystal structure, thermal expansion and electrical conductivity of Nd...)

## Co-Ho
- rank 1174 | 5 samples | 1 papers | 5 compositions
- compositions: Ho(Co0.995Al0.005)2 (1); Ho(Co0.925Al0.075)2 (1); HoCo2 (1); Ho(Co0.975Al0.025)2 (1); Ho(Co0.95Al0.05)2 (1)
- dopant candidates (<5% at.): Al (4)
- measured range: 10-299 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HoCo2 Fd-3m (227) mp-1072130 [hull=0.000, icsd=20, PRIMARY]; HoCo3 R-3m (166) mp-30558 [hull=0.000, icsd=14, PRIMARY]; Ho2Co17 P6_3/mmc (194) mp-1023 [hull=0.000, icsd=7, PRIMARY]; HoCo5 P6/mmm (191) mp-2435 [hull=0.026, icsd=6, PRIMARY]; Ho3Co Pnma (62) mp-622565 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.78.035101 (Effect of static and dynamic disorder on electronic transport inRCo2co...)

## Co-Ho-O
- rank 1175 | 5 samples | 2 papers | 2 compositions
- compositions: Ho0.9Ca0.1CoO3 (4); HoCoO3 (1)
- dopant candidates (<5% at.): Ca (4)
- measured range: 361-1165 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HoCoO3 Pnma (62) mp-24875 [hull=0.012, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/s0167-577x(00)00308-6 (Ca-doped HoCoO3 as p-type oxide thermoelectric material) | https://doi.org/10.1016/s0921-5107(01)00645-6 (Influence of ionic size of rare-earth site on the thermoelectric prope...)

## Co-La-O-Ti
- rank 1176 | 5 samples | 2 papers | 3 compositions
- compositions: LaCo0.5Ti0.5O3 (3); LaCo0.6Ti0.4O3 (1); LaCo0.7Ti0.3O3 (1)
- measured range: 352-1237 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2TiCoO6 Fm-3m (225) mp-1078893 [hull=0.117, icsd=1, PRIMARY]; La2Ti2CoO8 P-4m2 (115) mp-1223127 [hull=0.071, PRIMARY]; La2Ti3CoO10 I-4m2 (119) mp-1223091 [hull=0.114, PRIMARY]; La2TiCoO6 P2_1/c (14) mp-1211314 [hull=0.012]
- papers: https://doi.org/10.1016/j.actamat.2009.09.046 (Crystal structure, morphology and physical properties of LaCo1−xTixO3±...) | https://doi.org/10.1088/1742-6596/549/1/012022 (Neutron structural characterization and transport properties of the ox...)

## Co-Nb-Sb-Sn
- rank 1177 | 5 samples | 3 papers | 5 compositions
- compositions: NbCoSn0.8Sb0.2 (1); NbCoSb0.8Sn0.2 (1); NbCoSb0.75Sn0.25 (1); NbCo1.05Sn0.75Sb0.25 (1); NbCo1.05Sn0.5Sb0.5 (1)
- measured range: 298-974 K (5th-95th pct of 23 curves)
- papers: https://doi.org/10.1063/1.4961215 (Enhancement of thermoelectric properties in the Nb–Co–Sn half-Heusler/...) | https://doi.org/10.1039/c7cp04801g (The effect of Sn doping on thermoelectric performance of n-type half-H...) | https://doi.org/10.1039/c7cp07521a (Impact of Nb vacancies and p-type doping of the NbCoSn–NbCoSb half-Heu...)

## Co-Rh-Sb
- rank 1178 | 5 samples | 2 papers | 5 compositions
- compositions: (Co0.8Rh0.2)4Sb12 (1); Co0.5Rh0.5Sb3 (1); Co0.6Rh0.4Sb3 (1); Co0.73Rh0.27Sb3 (1); Co0.33Rh0.67Sb3 (1)
- solid-solution axis: Co/(Co+Rh) spans 0.33-0.80 (median 0.60) over 5 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 312-759 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CoSbRh2 I4/mmm (139) mp-1206379 [hull=0.083, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2010.09.207 (Effects of Tl-filling into the voids and Rh substitution for Co on the...) | https://doi.org/10.1016/j.jallcom.2006.08.296 (Study of transport properties of the Co1−xRhxSb3)

## Co-Sb-Se
- rank 1179 | 5 samples | 2 papers | 4 compositions
- compositions: CoSb2.7Se0.3 (2); CoSb2.68Se0.32 (1); CoSb2.76Se0.24 (1); CoSb2.8Se0.2 (1)
- measured range: 78-699 K (5th-95th pct of 14 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CoSbSe P2/m (10) mp-1226035 [hull=0.022, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(03)00411-0 (Thermoelectric properties and electronic structure of CoSb3 doped with...) | https://doi.org/10.1016/j.jallcom.2015.05.171 (Structure and thermoelectric properties of Se- and Se/Te-doped CoSb 3 ...)

## Cr-Cu-Fe-O
- rank 1180 | 5 samples | 2 papers | 5 compositions
- compositions: CuFe0.75Cr0.25O2 (1); CuFe0.25Cr0.75O2 (1); CuFe0.5Cr0.5O2 (1); CuCr0.4Fe1.6O4 (1); CuCr0.5Fe1.5O4 (1)
- measured range: 298-762 K (5th-95th pct of 17 curves)
- papers: https://doi.org/10.1088/0022-3727/48/49/495103 (Effects of spin entropy and lattice strain from mixed-trivalent Fe3+/C...) | https://doi.org/10.1016/j.jallcom.2004.12.044 (High temperature thermoelectric power studies of Cu–Cr ferrites)

## Cr-Cu-In-Se
- rank 1181 | 5 samples | 2 papers | 5 compositions
- compositions: CuCr0.75In0.25Se2 (1); CuCr0.5In0.5Se2 (1); CuCr0.25In0.75Se2 (1); (Cu0.46In0.54)Cr2.08Se4 (1); CuCr1.38In0.62Se4 (1)
- measured range: 292-673 K (5th-95th pct of 17 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cr4InCuSe8 F-43m (216) mp-20809 [hull=0.000, icsd=1, PRIMARY]; Cr4In2(CuSe4)3 C2/m (12) mp-1226645 [hull=0.057, PRIMARY]
- papers: https://doi.org/10.1111/jace.13860 (CuCrSe2\n Ternary Chromium Chalcogenide: Facile Fabrication, Doping an...) | https://doi.org/10.1016/j.jallcom.2008.09.180 (Influence of cation substitution on electrical conductivity of the n-t...)

## Cr-Fe-La-O-Sr
- rank 1182 | 5 samples | 3 papers | 4 compositions
- compositions: La0.3Sr0.7Fe0.7Cr0.3O3 (2); La0.6Sr0.4Cr0.5Fe0.5O3 (1); La0.6Sr0.4Cr0.25Fe0.75O3 (1); La0.6Sr0.4Cr0.75Fe0.25O3 (1)
- measured range: 423-1173 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr4LaCrFe4O15 Cm (8) mp-1218634 [hull=0.039, PRIMARY]
- papers: https://doi.org/10.1016/j.materresbull.2018.05.031 (Property optimization for strontium-rich lanthanum chromium ferrite ca...) | https://doi.org/10.1039/d2nj04357b (Enhanced CO<sub>2</sub> electrolysis through modulation of oxygen vaca...) | https://doi.org/10.1016/j.jpowsour.2013.02.024 (Sr-rich chromium ferrites as symmetrical solid oxide fuel cell electrodes)

## Cr-Gd-O-Ru-Sr
- rank 1183 | 5 samples | 1 papers | 5 compositions
- compositions: (SrRuO3)0.5(GdCrO3)0.5 (1); (SrRuO3)0.4(GdCrO3)0.6 (1); (SrRuO3)0.3(GdCrO3)0.7 (1); (SrRuO3)0.7(GdCrO3)0.3 (1); (SrRuO3)0.6(GdCrO3)0.4 (1)
- measured range: 10-300 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1088/1361-648x/aa9728 (Effect of Gd and Cr substitution on the structural, electronic and mag...)

## Cr-O-Pr
- rank 1184 | 5 samples | 1 papers | 5 compositions
- compositions: Pr0.9Ca0.1CrO3 (1); Pr0.95Ca0.05CrO3 (1); Pr0.8Ca0.2CrO3 (1); PrCrO3 (1); Pr0.95Sr0.05CrO3 (1)
- dopant candidates (<5% at.): Ca (3), Sr (1)
- measured range: 51-657 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrCrO3 Pnma (62) mp-1105822 [hull=0.000, icsd=2, PRIMARY]; PrCrO4 I4_1/amd (141) mp-18863 [hull=0.000, icsd=2, PRIMARY]; PrCr2O2 I4_1/amd (141) mp-1211150 [hull=1.113, PRIMARY]; PrCrO3 Pm-3m (221) mp-19353 [hull=0.040, icsd=1]
- papers: https://doi.org/10.1140/epjb/e2006-00349-8 (Transport and magnetic properties of Pr1-xCaxCrO3 (x = 0.0–0.5): effec...)

## Cr-O-Ti
- rank 1185 | 5 samples | 1 papers | 5 compositions
- compositions: Ti0.8Cr0.2O1.6 (1); Ti0.75Cr0.25O1.5 (1); Ti0.7Cr0.3O1.4 (1); Ti0.65Cr0.35O1.3 (1); Ti0.5Cr0.5O (1)
- measured range: 372-973 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti2CrO5 C2/c (15) mp-19369 [hull=0.023, icsd=1, PRIMARY]; Ti2Cr3O12 Pbcn (60) mp-774286 [hull=0.041, PRIMARY]; Ti7Cr12O48 P1 (1) mp-853216 [hull=0.078, PRIMARY]; TiCr2O5 C2/c (15) mp-1208207 [hull=0.058, PRIMARY]; TiCr7O12 P1 (1) mp-765454 [hull=0.028, PRIMARY]
- papers: https://doi.org/10.2320/jinstmet.j2013071 (Fabrication of Ti1^|^minus;xCrxOz and Analysis of Its Microstructure a...)

## Cr-Si-Ti
- rank 1186 | 5 samples | 1 papers | 5 compositions
- compositions: Cr0.6Ti0.4Si2 (1); Cr0.8Ti0.2Si2 (1); Cr0.5Ti0.5Si2 (1); Cr0.4Ti0.6Si2 (1); Cr0.2Ti0.8Si2 (1)
- measured range: 294-1132 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti(CrSi3)2 C222 (21) mp-1217270 [hull=0.051, PRIMARY]; Ti2Cr3Si P6_3/mmc (194) mp-1217151 [hull=0.014, PRIMARY]; Ti2Cr4Si5 Ibam (72) mp-1208248 [hull=0.000, PRIMARY]; Ti2CrSi6 C222 (21) mp-1217112 [hull=0.037, PRIMARY]; Ti3Cr17Si12 Amm2 (38) mp-1217346 [hull=0.128, PRIMARY]
- papers: https://doi.org/10.1007/bf00792195 (Physical properties of Cr1−xTixSiyyyand Cr1−xTaxSi2+y solid solutions)

## Cr-W
- rank 1187 | 5 samples | 1 papers | 2 compositions
- compositions: (W)73.32(Cr)25.92(Hf)0.76 (4); (W)88.76(Cr)9.41(Hf)1.83 (1)
- dopant candidates (<5% at.): Hf (5)
- measured range: 19-1299 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CrW Cmmm (65) mp-1226162 [hull=0.124, PRIMARY]
- papers: https://doi.org/10.1016/j.fusengdes.2018.01.012 (Microstructure and phase stability of W-Cr alloy prepared by spark pla...)

## Cs-Cu-Se
- rank 1188 | 5 samples | 1 papers | 5 compositions
- compositions: CsCu5Se3 (1); Cs(Cu0.99Sb0.01)5Se3 (1); Cs(Cu0.98Sb0.02)5Se3 (1); Cs(Cu0.97Sb0.03)5Se3 (1); Cs(Cu0.96Sb0.04)5Se3 (1)
- dopant candidates (<5% at.): Sb (4)
- measured range: 326-989 K (5th-95th pct of 25 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cs3(Cu4Se3)2 C2/m (12) mp-1188128 [hull=0.005, icsd=2, PRIMARY]; Cs2Cu5Se4 Cmcm (63) mp-28467 [hull=0.000, icsd=1, PRIMARY]; CsCuSe4 P2_12_12_1 (19) mp-17095 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/jacs.0c00062 (α-CsCu5Se3: Discovery of a Low-Cost Bulk Selenide with High Thermoelec...)

## Cu-Fe-Ni-O
- rank 1189 | 5 samples | 2 papers | 4 compositions
- compositions: Ni0.4Cu0.6Fe2O4 (2); Ni0.6Cu0.4 Fe2O4 (1); Ni0.5Cu0.5Fe2O4 (1); Ni0.6Cu0.4Fe2O4 (1)
- measured range: 305-797 K (5th-95th pct of 5 curves; full span incl. outliers 305-895 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe4CuNiO8 C2/m (12) mp-1225235 [hull=0.083, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2015.05.041 (Temperature-dependence thermoelectric power studies of mixed Ni–Cu nan...) | https://doi.org/10.1016/s0925-8388(03)00474-2 (High-temperature thermoelectric power studies of copper substituted ni...)

## Cu-Fe-Se
- rank 1190 | 5 samples | 2 papers | 1 compositions
- compositions: CuFeSe2 (5)
- measured range: 11-658 K (5th-95th pct of 16 curves)
- [ref 1] TEDesignLab / ICSD: FeCuSe2 (112)
- [ref 2] MP, ranked by ICSD evidence: FeCuSe2 P-42m (111) mp-1079566 [hull=0.128, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/j.jmat.2015.03.007 (Thermoelectric properties of n-type cobalt doped chalcopyrite Cu1−xCox...) | https://doi.org/10.3390/nano8010008 (Colloidal Synthesis and Thermoelectric Properties of CuFeSe2 Nanocrystals)

## Cu-Fe-Se-Sn
- rank 1191 | 5 samples | 4 papers | 2 compositions
- compositions: Cu6Fe4Sn12Se32 (4); Cu2FeSnSe4 (1)
- measured range: 10-588 K (5th-95th pct of 13 curves; full span incl. outliers 10-850 K)
- [ref 1] TEDesignLab / ICSD: FeCu2SnSe4 I-42m (121) mp-22612 [hull=0.040, icsd=3, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: CdFe4Cu10(SnSe4)5 I-4 (82) mp-1228572 [hull=0.040, PRIMARY, AMBIGUOUS]; Fe2Cu3(Sn3Se8)2 Pm (6) mp-1225320 [hull=0.036, PRIMARY]; FeCu2SnSe4 R3m (160) mp-1225270 [hull=0.140]; CdFe4Cu10(SnSe4)5 C2 (5) mp-1228871 [hull=0.041]
- papers: https://doi.org/10.1016/j.jallcom.2013.02.032 (Structural and thermoelectric properties of Cu6Fe4Sn12Se32 single crystal) | https://doi.org/10.1007/s11664-011-1842-3 (Thermoelectric Properties of Selenospinel Cu6Fe4Sn12Se32) | https://doi.org/10.1063/1.3569624 (Variable-range-hopping conduction and low thermal conductivity in chal...)

## Cu-La-O-Pr
- rank 1192 | 5 samples | 2 papers | 5 compositions
- compositions: (La0.75Pr0.25)1.8Sr0.2CuO4 (1); La0.9PrSr0.1CuO4 (1); La0.85PrSr0.15CuO4 (1); La0.8PrSr0.2CuO4 (1); La0.7PrSr0.3CuO4 (1)
- dopant candidates (<5% at.): Sr (5)
- solid-solution axis: La/(La+Pr) spans 0.41-0.75 (median 0.46) over 5 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 12-79 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/0022-4596(88)90341-6 (Solid-state chemistry of high-temperature oxide superconductors: The e...) | https://doi.org/10.1016/0921-4534(91)90472-b (Structural and superconducting properties of the system La1−xPrSrxCuO4)

## Cu-Pb-Te
- rank 1193 | 5 samples | 3 papers | 5 compositions
- compositions: PbTe(Cu2Se)0.09 (1); (PbTe)81Sb2Te3Sb0.6(Cu2Te)5 (1); (PbTe)94.68(Cu2Te)5.32 (1); (PbTe)92.89(Cu2Te)7.11 (1); (PbTe)91.63(Cu2Te)8.37 (1)
- dopant candidates (<5% at.): Se (1), Sb (1)
- measured range: 299-874 K (5th-95th pct of 21 curves)
- papers: https://doi.org/10.1088/0022-3727/49/6/065302 (Thermoelectric transport properties of PbTe-based composites incorpora...) | https://doi.org/10.1002/adfm.202007340 (Coherent Sb/CuTe Core/Shell Nanostructure with Large Strain Contrast B...) | https://doi.org/10.1021/jacs.7b11662 (Remarkable Roles of Cu To Synergistically Optimize Phonon and Carrier ...)

## Cu-S-Sb-Te
- rank 1194 | 5 samples | 2 papers | 3 compositions
- compositions: Cu12Sb2.19Te1.81S13 (2); Cu12Sb2.15Te1.85S13 (2); Cu12Sb2.21Te1.79S13 (1)
- measured range: 10-690 K (5th-95th pct of 19 curves)
- papers: https://doi.org/10.1039/c5tc01636c (Crystal structure, electronic band structure and high-temperature ther...) | https://doi.org/10.1021/acs.chemmater.5b03785 (Exsolution Process as a Route toward Extremely Low Thermal Conductivit...)

## Cu-S-Se-Sn
- rank 1195 | 5 samples | 3 papers | 5 compositions
- compositions: Cu2Sn0.925In0.075Se2.1S0.9 (1); Cu4Sn7.5S14Se2 (1); Cu2SnSe2.5S0.5 (1); Cu2SnSe2.6S0.4 (1); Cu2Sn0.97In0.03Se2.7S0.3 (1)
- dopant candidates (<5% at.): In (2)
- solid-solution axis: S/(S+Se) spans 0.10-0.87 (median 0.17) over 5 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 293-894 K (5th-95th pct of 26 curves)
- papers: https://doi.org/10.1007/s11664-012-1969-x (Improved Thermoelectric Performance in Cu-Based Ternary Chalcogenides ...) | https://doi.org/10.1038/s41598-018-26362-z (Improved thermoelectric performance of solid solution Cu4Sn7.5S16 thro...) | https://doi.org/10.1021/acsnano.1c03120 (Boosting Thermoelectric Performance of Cu2SnSe3 via Comprehensive Band...)

## Dy-O-V
- rank 1196 | 5 samples | 1 papers | 5 compositions
- compositions: DyVO3 (1); Dy0.95Ca0.05VO3  (1); Dy0.85Ca0.15VO3 (1); Dy0.8Ca0.2VO3 (1); Dy0.9Ca0.1VO3 (1)
- dopant candidates (<5% at.): Ca (4)
- measured range: 10-338 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DyVO4 I4_1/amd (141) mp-18784 [hull=0.000, icsd=9, PRIMARY]; Dy2V2O7 Fd-3m (227) mp-642823 [hull=0.014, icsd=1, PRIMARY]; Dy2VO5 P2_1/c (14) mp-1200746 [hull=0.043, icsd=1, PRIMARY]; DyVO3 Pnma (62) mp-25144 [hull=0.000, icsd=1, PRIMARY]; DyVO2 I4_1/amd (141) mp-1212946 [hull=0.516, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2013.01.075 (Transport and magnetic properties in the Dy1−xCaxVO3 ceramics)

## Er-Ho-Ni-Sb
- rank 1197 | 5 samples | 1 papers | 5 compositions
- compositions: Er0.7Ho0.3NiSb (1); Er0.3Ho0.7NiSb (1); Er0.8Ho0.2NiSb (1); Er0.5Ho0.5NiSb (1); Er0.2Ho0.8NiSb (1)
- solid-solution axis: Er/(Er+Ho) spans 0.20-0.80 (median 0.50) over 5 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 330-994 K (5th-95th pct of 15 curves)
- papers: https://doi.org/10.1016/j.matpr.2019.02.054 (High-temperature thermoelectric properties of half-Heusler phases Er1-...)

## Er-O-Ru-Sr
- rank 1198 | 5 samples | 2 papers | 4 compositions
- compositions: Sr2ErRuO6 (2); (Sr0.95La0.05)2ErRuO6 (1); (Sr0.8La0.2)2ErRuO6 (1); (Sr0.9La0.1)2ErRuO6 (1)
- dopant candidates (<5% at.): La (3)
- measured range: 118-1250 K (5th-95th pct of 13 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2ErRuO6 P2_1/c (14) mp-6294 [hull=0.000, icsd=3, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2008.09.003 (High-temperature thermoelectric properties of Sr2RuYO6 and Sr2RuErO6 d...) | https://doi.org/10.1063/1.4757632 (High-temperature thermoelectric properties of the double-perovskite ru...)

## Er-O-Sb
- rank 1199 | 5 samples | 2 papers | 1 compositions
- compositions: Er2SbO2 (5)
- measured range: 11-392 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Er2Sb2O7 P3_121 (152) mp-772137 [hull=0.016, PRIMARY]; Er2SbO2 Imm2 (44) mp-1225518 [hull=0.000, PRIMARY]; Er3Sb5O12 I-43m (217) mp-772087 [hull=0.000, PRIMARY]; Er3SbO7 C222_1 (20) mp-1212828 [hull=0.000, PRIMARY]; ErSbO4 P-1 (2) mp-1213308 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1021/ja209652d (Decoupling the Electrical Conductivity and Seebeck Coefficient in theR...) | https://doi.org/10.1021/acs.chemmater.7b03996 (Rare-Earth Pnictide Oxides (RE,Ca)mPnnOm (Pn = Sb, Bi): A Review of Cr...)

## Eu-Mn-O
- rank 1200 | 5 samples | 3 papers | 4 compositions
- compositions: EuMnO3 (2); Eu0.8Sr0.2MnO3 (1); Dy0.2Eu0.8MnO3 (1); Dy0.0Eu1.0MnO3 (1)
- dopant candidates (<5% at.): Sr (1), Dy (1)
- measured range: 12-298 K (5th-95th pct of 5 curves; full span incl. outliers 12-1364 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): EuMnO3 Pnma (62) mp-25667 [hull=0.000, icsd=3, PRIMARY]; EuMn2O5 Pbam (55) mp-622520 [hull=0.000, icsd=2, PRIMARY]; Eu2Mn2O7 Fd-3m (227) mp-769834 [hull=0.000, PRIMARY]; Eu2Mn2O5 Ima2 (46) mp-1099747 [hull=0.000, PRIMARY]; EuMnO3 Pm-3m (221) mp-1099619 [hull=0.046]
- papers: https://doi.org/10.1016/j.jallcom.2016.05.098 (Structural, electrical, magnetic and thermal studies on Eu 1-x Sr x Mn...) | https://doi.org/10.1039/c8ra00224j (Modification of low temperature magnetic interactions in Dy1−xEuxMnO3) | https://doi.org/10.1016/j.jssc.2004.12.006 (Structural, transport, and magnetic properties of RMnO3 perovskites (R...)
