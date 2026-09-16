# Host systems -- chunk 017 of 73

Ranks 801-850 by sample count. These 50 host systems cover 378 samples (0.73% of the TE set); cumulative through this chunk: 87.17%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Fe-La-Mn-O-Sr
- rank 801 | 8 samples | 4 papers | 6 compositions
- compositions: (La0.7Sr0.3MnO3)(La0.7Sr0.3FeO3) (3); SrLaFeMnO6 (1); Sr1.4La0.6FeMnO6 (1); Sr1.2La0.8FeMnO6 (1); La0.5Sr0.5Mn0.5Fe0.5O3 (1); La0.7Sr0.3Mn0.7Fe0.3O3 (1)
- measured range: 81-1125 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr3La7Mn7(FeO10)3 P1 (1) mp-706341 [hull=0.000, PRIMARY]; Sr3La7Mn8(FeO15)2 P1 (1) mp-705096 [hull=0.000, PRIMARY]; Sr3La7Mn9FeO30 C2 (5) mp-1173239 [hull=0.011, PRIMARY]; SrLaMnFeO6 Pc (7) mp-1218252 [hull=0.000, PRIMARY]; SrLaMnFeO6 P2/c (13) mp-705491 [hull=0.000]
- papers: Thickness dependence of exchange coupling in (111)-oriented perovskite oxide superlattices | Electron doping of Sr<sub>2</sub>FeMoO<sub>6−δ</sub> as high performance anode materials for solid oxide fuel cells | Effect of Fe and Co doping on structural and electrical properties of La0.5Sr1.5MnO4 layered-structure and the corresponding La0.5Sr0.5MnO3 perovskite

## Fe-Li-O
- rank 802 | 8 samples | 8 papers | 8 compositions
- compositions: Li0.45Zn0.1La0.04Fe2.41O4 (1); Li0.4Cd0.2Fe2.4O4 (1); Li0.4Zn0.2Fe2.4O4 (1); Mg0.1Al0.2Li0.45Fe2.25O4 (1); Li0.45Mg0.1Fe2.45O4 (1); Li0.6Ge0.2Fe2.2O4 (1)
- dopant candidates (<5% at.): Zn (2), Mg (2), La (1), Cd (1), Al (1), Ge (1), Cu (1)
- measured range: 197-1121 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiFe5O8 P4_332 (212) mp-31768 [hull=0.040, icsd=13, PRIMARY]; LiFeO2 I4_1/amd (141) mp-18782 [hull=0.018, icsd=4, PRIMARY]; Li5FeO4 Pbca (61) mp-19511 [hull=0.000, icsd=1, PRIMARY]; Li(Fe2O3)4 Cc (9) mp-1178116 [hull=0.048, PRIMARY]; Li11(FeO3)4 Pm (6) mp-849463 [hull=0.125, PRIMARY]
- papers: Correlation of the physico chemical properties of Zn-substituted Li–La ferrite | Electrical conductivity and thermoelectric power of lithium-cadmium ferrites | Electrical Conductivity and Thermoelectric Power of LithiumZinc Ferrites

## Fe-P-S
- rank 803 | 8 samples | 1 papers | 1 compositions
- compositions: FePS3 (8)
- measured range: 12-289 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FePS3 C2/m (12) mp-5864 [hull=0.134, icsd=6, PRIMARY]; FePS P2_1/c (14) mp-1101971 [hull=0.000, icsd=1, PRIMARY]; Fe(PS3)2 C2 (5) mp-753614 [hull=0.123, PRIMARY]
- papers: Metal-insulator transition in Mott-insulator FePS3

## Fe-Sb-Ti
- rank 804 | 8 samples | 3 papers | 6 compositions
- compositions: TiFe1.33Sb (3); Ti0.867Fe1.463Sb (1); Ti1.108Fe1.222Sb (1); TiFe1.0Ni0.1Sb (1); TiFeCu0.10Sb (1); TiFeCu0.15Sb (1)
- dopant candidates (<5% at.): Cu (2), Ni (1)
- measured range: 299-967 K (5th-95th pct of 40 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiFe2Sb Fm-3m (225) mp-998970 [hull=0.030, icsd=1, PRIMARY]; Ti5FeSb2 I4/mcm (140) mp-30326 [hull=0.015, icsd=1, PRIMARY]; TiFeSb F-43m (216) mp-10755 [hull=0.000, icsd=1, PRIMARY]; Ti10FeSb5 I422 (97) mp-1217288 [hull=0.000, PRIMARY]; Ti4(FeSb)5 R3m (160) mp-1217622 [hull=0.412, PRIMARY]
- papers: The half Heusler system Ti<sub>1+x</sub>Fe<sub>1.33−x</sub>Sb–TiCoSb with Sb/Sn substitution: phase relations, crystal structures and thermoelectric properties | Structure and thermoelectric property evolution of TiFe1.1−xNixSb with the filling of Ni | Structure and thermoelectric properties of half-Heusler-like TiFeCu Sb alloys

## Fe-Si-U
- rank 805 | 8 samples | 3 papers | 8 compositions
- compositions: U1.2Fe4Si9.7 (1); U2Fe3Si5 (1); U2FeSi3 (1); U3Fe2Si7 (1); UFe2Si2 (1); UFe5Si3 (1)
- dopant candidates (<5% at.): C (1)
- measured range: 16-309 K (5th-95th pct of 16 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U(FeSi)2 I4/mmm (139) mp-20924 [hull=0.000, icsd=3, PRIMARY]; U2Fe3Si5 C2/c (15) mp-1105639 [hull=0.000, icsd=3, PRIMARY]; U6Fe16Si7C Fm-3m (225) mp-642273 [hull=0.000, icsd=2, PRIMARY]; UFeSi Pnma (62) mp-20121 [hull=0.000, icsd=2, PRIMARY]; U6Fe16Si7 Fm-3m (225) mp-642279 [hull=0.000, icsd=2, PRIMARY]
- papers: Thermoelectric properties of ternary compounds from the U–Fe–Si system | Novel Intermetallic Compound UFe5Si3:  A New Room-Temperature Magnet with an Original Atomic Arrangement | Crystal structure and electronic properties of the new compounds, U6Fe16Si7 and its interstitial carbide U6Fe16Si7C

## Ga-K-Sn
- rank 806 | 8 samples | 5 papers | 3 compositions
- compositions: K8Ga8Sn38 (6); K8Ga6Sn40 (1); K8Ga7Sn39 (1)
- measured range: 10-516 K (5th-95th pct of 17 curves)
- papers: Preparation and thermoelectric properties of sintered type-I clathrates K8GaxSn46−x | Preparation and thermoelectric properties of sinteredn-type K8M8Sn38(M= Al, Ga and In) with the type-I clathrate structure | Interplay between thermoelectric and structural properties of type-I clathrateK8Ga8Sn38single crystals

## Ga-Nb-Ru
- rank 807 | 8 samples | 1 papers | 8 compositions
- compositions: Ru1.90Nb1.10Ga (1); Ru2NbGa0.95In0.05 (1); Ru2NbGa0.90Sn0.10 (1); Ru1.95Nb1.05Ga (1); Ru2NbGa (1); Ru2.05Nb0.95Ga (1)
- dopant candidates (<5% at.): In (2), Sn (1), Ge (1)
- measured range: 10-299 K (5th-95th pct of 40 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NbGaRu2 Fm-3m (225) mp-977401 [hull=0.000, PRIMARY]
- papers: Thermoelectric properties of chemically substituted Heusler-type Ru2-Nb1+Ga and Ru2NbGa1-M  (M = In, Ge, and Sn) alloys

## Gd-Ge-Si
- rank 808 | 8 samples | 5 papers | 5 compositions
- compositions: Gd5Si2Ge2 (4); Gd5Si2.2Ge1.8 (1); Gd5Si1.7Ge2.3 (1); Gd5Si2.3Ge1.7 (1); Gd5(Si0.45Ge0.55)4 (1)
- solid-solution axis: Ge/(Ge+Si) spans 0.42-0.58 (median 0.50) over 5 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 11-321 K (5th-95th pct of 12 curves)
- papers: Magnetic and electrical transport properties of DyxGd5−xSi2Ge2 (x=0.0, 1.5, 2.5, 3.0, 3.5, 4.5 and 5.0) compounds | Effect of Si/Ge ratio on resistivity and thermopower in Gd5SixGe4−x magnetocaloric compounds | Thermopower and electrical resistivity behavior near the martensitic transition in Gd5(SixGe1−x)4 magnetocaloric compounds

## Gd-Mn-O
- rank 809 | 8 samples | 2 papers | 5 compositions
- compositions: Gd0.8Sr0.2MnO3 (2); GdMnO3 (2); GdMn0.9Cr0.1O3 (2); GdMn0.8Cr0.2O3 (1); GdMn0.8Cr.2O3 (1)
- dopant candidates (<5% at.): Cr (4), Sr (2)
- measured range: 12-301 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdMnO3 Pnma (62) mp-1189827 [hull=0.323, icsd=4, PRIMARY]; GdMn2O5 Pbam (55) mp-703682 [hull=0.000, icsd=1, PRIMARY]
- papers: Structural, electrical, magnetic and thermal properties of Gd1–xSrxMnO3 (0.2≤x≤0.5) manganites | Structural, electrical and magnetic phase evolution of Cr substituted GdMn1−Cr O3 (0 ⩽x⩽ 0.2) manganites

## Ge-Pr-Pt
- rank 810 | 8 samples | 4 papers | 5 compositions
- compositions: PrPt4Ge12 (4); Pr3Pt4Ge6 (1); Pr0.9Ce0.1Pt4Ge12 (1); Pr0.9Eu0.1Pt4Ge12 (1); PrPt4Ge11.7Sb0.3 (1)
- dopant candidates (<5% at.): Ce (1), Eu (1), Sb (1)
- measured range: 10-310 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Pr(Ge3Pt)4 Im-3 (204) mp-1105939 [hull=0.022, icsd=1, PRIMARY]; Pr(GePt)2 Pmn2_1 (31) mp-1079841 [hull=0.000, icsd=1, PRIMARY]; Pr3(Ge3Pt2)2 Pnma (62) mp-645543 [hull=0.000, icsd=1, PRIMARY]; Pr3Ge13Pt4 Cc (9) mp-1195347 [hull=0.070, icsd=1, PRIMARY]; PrGe2Pt Immm (71) mp-1106226 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric Properties of Correlated Electron Systems Ln 3Pt4Ge6and LnPt4Ge12(Ln = Ce, Pr) and Non-centrosymmetric X 2 T 12P7(X = Yb, Hf and T = Fe, Co) | Probing the superconductivity ofPrPt4Ge12through Ce substitution | Crossover and coexistence of superconductivity and antiferromagnetism in the filled-skutterudite system \nPr1−xEuxPt4Ge12

## H-P
- rank 811 | 8 samples | 3 papers | 5 compositions
- compositions: PDTPT (3); P3HT  (2);   P3HT (1);  P3HT  (1); PDPP4T  (1)
- measured range: 284-401 K (5th-95th pct of 25 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PH3 P1 (1) mp-696588 [hull=0.052, icsd=1, PRIMARY]; P3H Fm-3m (225) mp-1186360 [hull=0.774, PRIMARY]
- papers: Two soluble polymers with lower ionization potentials: doping and thermoelectric properties | Flexible and printable thermoelectric films based on FeCl3 doped P3HT | Revealing unipolar thermoelectric performance in bipolar polymer

## Ir-Sn-Te
- rank 812 | 8 samples | 2 papers | 7 compositions
- compositions: IrSn1.5Te1.5 (2); Ir(Sn1.475In0.025)Te1.5 (1); Ir(Sn1.45In0.05)Te1.5 (1); (Ir0.975Pd0.025)Sn1.5Te1.5 (1); Ir(Sn1.4In0.1)Te1.5 (1); Ir(Sn1.425In0.075)Te1.5 (1)
- dopant candidates (<5% at.): In (4), Pd (1), Ru (1)
- measured range: 10-992 K (5th-95th pct of 20 curves; full span incl. outliers 10-1053 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sn3Te3Ir2 R-3 (148) mp-5142 [hull=0.000, icsd=2, PRIMARY]
- papers: Electronic structure and thermoelectric properties of pnictogen-substituted ASn1.5Te1.5 (A = Co, Rh, Ir) skutterudites | Synthesis, crystal structure and thermoelectric properties of IrSn1.5Te1.5 -based skutterudites

## K-Mo-O
- rank 813 | 8 samples | 3 papers | 4 compositions
- compositions: K0.3MoO3 (3); K0.24Tl0.06MoO3 (2); K0.3Mo0.96W0.04O3 (2); Tl0.06K0.24MoO3 (1)
- dopant candidates (<5% at.): Tl (3), W (2)
- measured range: 24-299 K (5th-95th pct of 8 curves)
- [ref 1] TEDesignLab / ICSD: K2Mo3O10 (15) [PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: K3(MoO3)10 C2/m (12) mp-615973 [hull=0.026, icsd=3, PRIMARY]; K2MoO4 C2/m (12) mp-18914 [hull=0.000, icsd=2, PRIMARY]; K(MoO3)3 C2/m (12) mp-19607 [hull=0.040, icsd=1, PRIMARY]; K2Mo2O7 P-1 (2) mp-32046 [hull=0.000, icsd=1, PRIMARY]; K10Hf3Mo12PbO48 R-3 (148) mp-1205471 [hull=0.005, icsd=1, PRIMARY]
- papers: Transverse thermoelectric power in the molybdenum blue bronze K0.3MoO3 | Effect of impurities on thermoelectric power in thallium blue bronze Tl0.3MoO3 | Thermopower hysteresis in the charge density wave state of Rb0.3MoO3 and K0.3MoO3

## K-O-Ta
- rank 814 | 8 samples | 4 papers | 6 compositions
- compositions: KTaO3 (3); K0.9995Ba0.0005TaO3 (1); K0.9998Ba0.0002TaO3 (1); K0.9999Ba0.0001TaO3 (1); K0.9997Ba0.003TaO3 (1); K0.998Ba0.02TaO3 (1)
- dopant candidates (<5% at.): Ba (5)
- measured range: 10-374 K (5th-95th pct of 17 curves; full span incl. outliers 10-567 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): KTaO3 Pm-3m (221) mp-3614 [hull=0.000, icsd=7, PRIMARY]; K3TaO8 I-42m (121) mp-4690 [hull=0.015, icsd=2, PRIMARY]; K2LaTa5O15 P4/mbm (127) mp-1204933 [hull=0.000, icsd=1, PRIMARY]; KTa5O13 Pbcm (57) mp-27169 [hull=0.000, icsd=1, PRIMARY]; K2Ta4O11 R-3c (167) mp-1195471 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric Properties of Electron-Doped KTaO3 | Enhanced Thermoelectric Power Factor of NaxCoO2Thin Films by Structural Engineering | Thermal properties of cubic KTa1−xNbxO3 crystals

## La-Mo-O
- rank 815 | 8 samples | 3 papers | 6 compositions
- compositions: La2Mo2O7 (3); La1.85Sm0.15Mo1.85W0.15O9 (1); La1.80Sm0.20Mo1.80W0.20O9 (1); La2Mo2O9 (1); La1.95Sm0.05Mo1.95W0.05O9 (1); La1.90Sm0.10Mo1.90W0.10O9 (1)
- dopant candidates (<5% at.): Sm (4), W (4)
- measured range: 14-1273 K (5th-95th pct of 9 curves)
- [ref 1] TEDesignLab / ICSD: La2MoO6 (121)
- [ref 2] MP, ranked by ICSD evidence: La2MoO6 I4_1/acd (142) mp-19300 [hull=0.000, icsd=3, PRIMARY]; La2MoO5 P4/m (83) mp-1194825 [hull=0.033, icsd=2, PRIMARY]; La7Mo7O30 R-3 (148) mp-19436 [hull=0.009, icsd=2, PRIMARY]; La2Mo2O7 Pnnm (58) mp-32061 [hull=0.099, icsd=1, PRIMARY]; La(Mo4O7)2 Pbcn (60) mp-1199742 [hull=0.191, icsd=1, PRIMARY]
- papers: The temperature dependence of resistivity and thermoelectric power in lanthanum molybdenum oxide crystal | Complex Effect of Sm3+\n/W6+\n Codoping on α-β Phase Transformation and Phonon Scattering of Oxygen-Deficient La2\nMo2\nO9 | Quasi-one-dimensionality in the new bronze-like compound La2Mo2O7

## Li-S-Ti
- rank 816 | 8 samples | 2 papers | 4 compositions
- compositions: Li0.26Ti1.03S2 (2); Li0.61Ti1.03S2 (2); Li0.8Ti1.03S2 (2); Li0.97Ti1.03S2 (2)
- measured range: 239-462 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiTiS2 P-3m1 (164) mp-9615 [hull=0.000, icsd=2, PRIMARY]; Li(TiS2)3 P-3m1 (164) mp-19755 [hull=0.000, icsd=2, PRIMARY]; Li(TiS2)2 C2/m (12) mp-1223278 [hull=0.068, PRIMARY]; Li3TiS3 C2/c (15) mp-753497 [hull=0.084, PRIMARY]; Li2Ti2S5 C2/c (15) mp-753863 [hull=0.064, PRIMARY]
- papers: The thermoelectric power in solid solution electrodes: A disregarded phenomenon? | The thermodynamic and thermoelectric properties of LixTiS2 and LixCoO2

## Mn-Ru-Si
- rank 817 | 8 samples | 2 papers | 8 compositions
- compositions: Ru0.5Mn0.5Si1.650 (1); Ru0.45Mn0.55Si1.660 (1); Ru0.25Mn0.75Si1.710 (1); Ru0.15Mn0.85Si1.725 (1); Ru0.5Mn0.5Si1.5 (1); Ru0.25Mn0.75Si1.5 (1)
- measured range: 293-1064 K (5th-95th pct of 24 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn2SiRu F-43m (216) mp-999576 [hull=0.008, icsd=1, PRIMARY]; MnSiRu2 Fm-3m (225) mp-864966 [hull=0.000, PRIMARY]
- papers: Crystal structure and thermoelectric properties of chimney–ladder compounds in the Ru2Si3–Mn4Si7 pseudobinary system | Structural and Thermoelectric Properties of Chimney–Ladder Compounds in the Ru-Mn-Si System

## Mn-Sb-Yb
- rank 818 | 8 samples | 6 papers | 3 compositions
- compositions: Yb9Mn4.2Sb9 (4); YbMn2Sb2 (3); Yb9Mn1.2ZnSb9 (1)
- dopant candidates (<5% at.): Zn (1)
- measured range: 13-984 K (5th-95th pct of 30 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(MnSb)2 P-3m1 (164) mp-4836 [hull=0.202, icsd=8, PRIMARY]; YbMnSb2 I4/mmm (139) mp-1094016 [hull=0.063, PRIMARY]
- papers: Enhanced Thermoelectric Figure of Merit of Zintl Phase YbCd2-xMnxSb2 by Chemical Substitution | Glass-like lattice thermal conductivity and high thermoelectric efficiency in Yb9Mn4.2Sb9 | Thermoelectric properties of the Yb9Mn4.2−xZnxSb9 solid solutions

## Nd-Ni-O-Sr
- rank 819 | 8 samples | 3 papers | 7 compositions
- compositions: Nd0.7Sr0.3NiO3 (2); Nd1.6Sr1.4Ni0.98Cu0.02O4 (1); Nd1.6Sr1.4NiO4 (1); Nd1.6Sr1.4Ni0.9Cu0.1O4 (1); Nd1.6Sr1.4Ni0.8Cu0.2O4 (1); Nd1.6Sr1.4Ni0.7Cu0.3O4 (1)
- dopant candidates (<5% at.): Cu (4)
- measured range: 10-300 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrNd3(NiO4)2 Amm2 (38) mp-1218171 [hull=0.022, PRIMARY]; SrNdNiO4 I4mm (107) mp-1217981 [hull=0.001, PRIMARY]; SrNdNiO4 Cmcm (63) mp-1218010 [hull=0.015]
- papers: Pressure studies on the electrical properties in R2-xSrxNi1-yCuyO4+δ(R=La, Nd) and La3Ni2O7+δ | Structural, electrical, and magnetic properties of bulk Nd1-Sr NiO3 (x = 0–0.3) | Superconductivity in an infinite-layer nickelate

## Ni-O-Zn
- rank 820 | 8 samples | 2 papers | 8 compositions
- compositions: Zn0.7Ni0.3O (1); Zn0.837Ni0.163O (1); (Ni0.6Zn0.4)O (1); ((Zn0.97Ni0.03)O)0.1((Ni0.6Zn0.4)O)0.9 (1); ((Zn0.97Ni0.03)O)0.2((Ni0.6Zn0.4)O)0.8 (1); ((Zn0.97Ni0.03)O)0.4((Ni0.6Zn0.4)O)0.6 (1)
- measured range: 51-818 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zn(Ni2O5)2 C2/m (12) mp-1215795 [hull=0.201, PRIMARY]; Zn2Ni11O13 Immm (71) mp-1101164 [hull=0.058, PRIMARY]; Zn2Ni3O5 C2/m (12) mp-763705 [hull=0.056, PRIMARY]; Zn2NiO3 Immm (71) mp-1215778 [hull=0.110, PRIMARY]; Zn3Ni7O10 R-3m (166) mp-768016 [hull=0.040, PRIMARY]
- papers: Localized Charge Carrier Transport Properties \nof Zn1−x\n                     Ni\n                x\n              O/NiO Two-Phase Composites | Origin of the Positive Temperature Coefficient of Resistivity Anomaly in the ZnO-NiO System

## Ni-Pb-Sn-Zr
- rank 821 | 8 samples | 2 papers | 7 compositions
- compositions: ZrNiPb0.38Sn0.6Bi0.02 (2); ZrNiPb0.18Sn0.8Bi0.02 (1); ZrNiPb0.78Sn0.2Bi0.02 (1); ZrNiPb0.58Sn0.4Bi0.02 (1); ZrNi1.01Pb0.38Sn0.6Bi0.02 (1); ZrNi1.03Pb0.38Sn0.6Bi0.02 (1)
- dopant candidates (<5% at.): Bi (8)
- solid-solution axis: Pb/(Pb+Sn) spans 0.18-0.80 (median 0.39) over 7 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 301-873 K (5th-95th pct of 40 curves)
- papers: Thermoelectric Properties of n-type ZrNiPb-Based Half-Heuslers | Substantial enhancement in thermoelectric figure-of-merit of half-Heusler ZrNiPb alloys

## O-Pb-Ti
- rank 822 | 8 samples | 1 papers | 4 compositions
- compositions: PbTi0.92Nb0.08O3 (2); PbTi0.96Nb0.04O3 (2); PbTi0.94Nb0.06O3 (2); PbTi0.88Nb0.12O3 (2)
- dopant candidates (<5% at.): Nb (8)
- measured range: 77-423 K (5th-95th pct of 8 curves)
- [ref 1] TEDesignLab / ICSD: TiPbO3 P4mm (99) mp-20459 [hull=0.000, icsd=30, PRIMARY]; Ti3PbO7 (11) [PRIMARY]; TiPbO3 Pm-3m (221) mp-19845 [hull=0.040, icsd=10]; TiPbO3 I4/m (87) mp-1106215 [hull=0.002, icsd=3]; TiPbO3 (47)
- [ref 2] MP, ranked by ICSD evidence: HfTi4(PbO3)5 Cm (8) mp-1224605 [hull=0.013, PRIMARY]; Ti10Bi(Pb3O10)3 P1 (1) mp-677372 [hull=0.021, PRIMARY]; MgTi3Pb5WO15 P4/nmm (129) mp-694933 [hull=0.054, PRIMARY]; Ti3TePb4O13 R3m (160) mp-1217292 [hull=0.001, PRIMARY]; HfTi4(PbO3)5 Pmm2 (25) mp-1224660 [hull=0.014]
- papers: Coexistence of polar distortion and metallicity in \n<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:mrow><mml:msub><mml:mi>PbTi</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mtext>−</mml:mtext><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Nb</mml:mi><mml:mi>x</mml:mi></mml:msub><mml:msub><mml:mi mathvariant=\"normal\">O</mml:mi><mml:mn>3</mml:mn></mml:msub></mml:mrow></mml:math>

## Pb-Sb-Te
- rank 823 | 8 samples | 4 papers | 4 compositions
- compositions: Pb2Sb6Te11 (4); PbSb2Te4.1I0.0006 (2); Pb0.9Sb0.1Te (1); Pb0.6Sb0.8Te1.8 (1)
- dopant candidates (<5% at.): I (2)
- measured range: 85-722 K (5th-95th pct of 30 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sb2Te4Pb R-3m (166) mp-31507 [hull=0.736, icsd=1, PRIMARY]; Sb4Te7Pb P-3m1 (164) mp-1209139 [hull=0.853, PRIMARY]
- papers: Anisotropic thermoelectric properties of the layered compounds PbSb2Te4 and PbBi4Te7 | Effect of annealing on thermoelectric properties of eutectic PbTe–Sb2Te3 composite with self-assembled lamellar structure | Effect of Ag or Sb addition on the thermoelectric properties of PbTe

## Re-Ru-Si
- rank 824 | 8 samples | 1 papers | 8 compositions
- compositions: Ru0.24Re0.73Si1.67 (1); Ru0.27Re0.73Si1.6714 (1); Ru0.64Re0.36Si1.6048 (1); Ru0.47Re0.53Si1.6354 (1); Ru0.4Re0.6Si1.648 (1); Ru0.86Re0.14Si1.5652 (1)
- dopant candidates (<5% at.): Al (1)
- measured range: 171-977 K (5th-95th pct of 24 curves; full span incl. outliers 171-1060 K)
- papers: Thermoelectric properties of ternary and Al-containing quaternary Ru1−xRexSiy chimney–ladder compounds

## Sb-Sm
- rank 825 | 8 samples | 3 papers | 2 compositions
- compositions: SmSb (6); Sm4Sb3 (2)
- measured range: 343-1142 K (5th-95th pct of 2 curves; full span incl. outliers 343-1235 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SmSb Fm-3m (225) mp-2281 [hull=0.000, icsd=10, PRIMARY]; Sm4Sb3 I-43d (220) mp-367 [hull=0.008, icsd=3, PRIMARY]; Sm5Sb3 P6_3/mcm (193) mp-980757 [hull=0.000, icsd=3, PRIMARY]; SmSb2 Cmce (64) mp-29647 [hull=0.000, icsd=3, PRIMARY]; Sm2Sb I4/mmm (139) mp-1077018 [hull=0.023, icsd=2, PRIMARY]
- papers: High-temperature transport properties of complex antimonides with anti-Th3P4structure | High-Temperature Transport Properties of Yb4−x Sm x Sb3 | Anomalous quantum oscillations and evidence for a non-trivial Berry phase in SmSb

## Sb-Sn-Zn
- rank 826 | 8 samples | 2 papers | 4 compositions
- compositions: ZnSnSb2 (5); Zn9Sb3Sn (1); Zn7Sb3Sn (1); Zn11Sb3Sn (1)
- measured range: 88-660 K (5th-95th pct of 15 curves)
- [ref 1] TEDesignLab / ICSD: ZnSnSb2 I-42d (122) mp-4756 [hull=0.000, icsd=3, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: ZnSnSb2 P-4m2 (115) mp-1215452 [hull=0.013]; ZnSnSb2 Cm (8) mp-676663 [hull=0.138]
- papers: Sphalerite−Chalcopyrite Polymorphism in Semimetallic ZnSnSb2 | Electrical Transport Properties of Single-Crystalline β-Zn4Sb3 Prepared Through the Zn-Sn Mixed-Flux Method

## Sb-Ta
- rank 827 | 8 samples | 1 papers | 1 compositions
- compositions: TaSb2 (8)
- measured range: 10-818 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ta3Sb Pm-3n (223) mp-541 [hull=0.000, icsd=2, PRIMARY]; Ta5Sb4 I4/m (87) mp-2598 [hull=0.000, icsd=2, PRIMARY]; TaSb2 C2/m (12) mp-11697 [hull=0.000, icsd=2, PRIMARY]; TaSb3 Fm-3m (225) mp-1187254 [hull=0.635, PRIMARY]
- papers: Constitution of the systems {V,Nb,Ta}-Sb and physical properties of di-antimonides {V,Nb,Ta}Sb2

## Sb-V
- rank 828 | 8 samples | 1 papers | 2 compositions
- compositions: V0.97Sb2 (7); V0.96Sb2 (1)
- measured range: 10-804 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): V3Sb Pm-3n (223) mp-1555 [hull=0.000, icsd=4, PRIMARY]; V5Sb4 I4/m (87) mp-30536 [hull=0.025, icsd=3, PRIMARY]; VSb2 I4/mcm (140) mp-2851 [hull=0.033, icsd=3, PRIMARY]; V3Sb2 R-3m (166) mp-29617 [hull=0.026, icsd=2, PRIMARY]; VSb P6_3/mmc (194) mp-7821 [hull=0.139, icsd=1, PRIMARY]
- papers: Constitution of the systems {V,Nb,Ta}-Sb and physical properties of di-antimonides {V,Nb,Ta}Sb2

## Ag-Bi-Ge-Te
- rank 829 | 7 samples | 1 papers | 7 compositions
- compositions: (GeTe)0.8(AgBiTe2)0.2 (1); (GeTe)0.7(AgBiTe2)0.3 (1); (GeTe)0.65(AgBiTe2)0.35 (1); (GeTe)0.5(AgBiTe2)0.5 (1); (GeTe)0.6(AgBiTe2)0.4 (1); (GeTe)0.55(AgBiTe2)0.45 (1)
- measured range: 296-674 K (5th-95th pct of 35 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AgGeBiTe3 Imm2 (44) mp-1229030 [hull=0.147, PRIMARY]
- papers: Hierarchical Architectural Structures Induce High Performance in n‐Type GeTe‐Based Thermoelectrics

## Ag-Co
- rank 830 | 7 samples | 2 papers | 1 compositions
- compositions: Co20Ag80 (7)
- measured range: 10-293 K (5th-95th pct of 11 curves)
- papers: Thermal and thermoelectric properties of granular Co-Ag solids | Giant magnetothermal conductivity and giant magnetothermopower in granular Co-Ag solids

## Ag-Cr-Se
- rank 831 | 7 samples | 2 papers | 4 compositions
- compositions: AgCrSe2 (4); Ag0.98CrSe2 (1); Ag0.96CrSe2 (1); Ag0.90CrSe2 (1)
- measured range: 11-824 K (5th-95th pct of 28 curves)
- [ref 1] TEDesignLab / ICSD: CrAgSe2 R3m (160) mp-3532 [hull=0.000, icsd=5, PRIMARY]
- papers: Revisiting AgCrSe2as a promising thermoelectric material | Localised Ag+ vibrations at the origin of ultralow thermal conductivity in layered thermoelectric AgCrSe2

## Ag-In-O
- rank 832 | 7 samples | 2 papers | 5 compositions
- compositions: AgIn0.9Sn0.1O2 (2); AgIn0.95Sn0.05O2 (2); AgIn0.93Sn0.07O2 (1); AgIn0.97Sn0.03O2 (1); AgInO2 (1)
- dopant candidates (<5% at.): Sn (6)
- measured range: 301-778 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): InAgO2 P6_3/mmc (194) mp-20329 [hull=0.000, icsd=1, PRIMARY]; InAgO2 R-3m (166) mp-22660 [hull=0.001, icsd=1]; InAgO2 R3m (160) mp-1097001 [hull=0.111]
- papers: Temperature Dependences of Electric Resistivity and Thermoelectric Power on Sn FractionXin Polycrystalline n-AgIn1-XSnXO2Compounds | Thermoelectric properties of delafossite-type layered oxides AgIn1−xSnxO2

## Ag-Sn
- rank 833 | 7 samples | 2 papers | 7 compositions
- compositions: Ag0.2Sn0.8 (1); Ag0.6Sn0.4 (1); Ag0.4Sn0.6 (1); Ag0.3Sn0.7 (1); Ag0.68Sn0.32 (1); Ag0.5Sn0.5 (1)
- measured range: 11-180 K (5th-95th pct of 7 curves; full span incl. outliers 11-302 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ag3Sn Pmmn (59) mp-611 [hull=0.000, icsd=3, PRIMARY]; AgSn3 P6_3/mmc (194) mp-1183248 [hull=0.113, PRIMARY]; Ag3Sn P-6m2 (187) mp-1229107 [hull=0.098]
- papers: Temperature Dependence of the Thermoelectric Powder of Quench Condensed Amorphous AgxSn1-x-Films | THERMAL CONDUCTIVITY MEASUREMENT OF BSCCO TAPES FOR CURRENT LEAD APPLICATIONS

## Al-Ca-Sb-Yb
- rank 834 | 7 samples | 2 papers | 4 compositions
- compositions: Ca1.5Yb3.5Al2Sb6 (3); Ca3.30Yb1.50Sm0.20Al2Sb6 (2); Ca3.20Yb1.65Pr0.15Al2Sb6 (1); Ca3.46Yb1.35Pr0.19Al2Sb6 (1)
- dopant candidates (<5% at.): Pr (2), Sm (2)
- measured range: 302-872 K (5th-95th pct of 31 curves)
- papers: p-Type to n-Type Conversion through the “Bypass” Phase Transition in the Zintl-Phase Thermoelectric Materials | Influence of Thermally Activated Solid-State Crystal-to-Crystal Structural Transformation on the Thermoelectric Properties of the Ca5–xYbxAl2Sb6 (1.0 ≤ x ≤ 5.0) System

## Al-Ce-Ga
- rank 835 | 7 samples | 2 papers | 7 compositions
- compositions: Ce(Ga0.9Al0.1)2 (1); Ce0.9La0.1Al2Ga2 (1); CeAl2Ga2 (1); Ce0.95La0.05Al2Ga2 (1); Ce0.8La0.2Al2Ga2 (1); Ce0.95Y0.05Al2Ga2 (1)
- dopant candidates (<5% at.): La (3), Y (2)
- solid-solution axis: Al/(Al+Ga) spans 0.10-0.50 (median 0.50) over 7 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-291 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(AlGa)2 I4/mmm (139) mp-3303 [hull=0.000, icsd=3, PRIMARY]; CeAlGa P-6m2 (187) mp-1226618 [hull=0.030, PRIMARY]
- papers: Thermoelectric power and resistivity studies in the Kondo-lattice system CeGa2with Sn or Al substitutions and RGa2(R identical to Ho,Dy,Tb) alloys | Antiferromagnetism inCe1−xLaxAl2Ga2andCe1−yYyAl2Ga2Kondo-lattice systems

## Al-Cr-Fe-Ti
- rank 836 | 7 samples | 2 papers | 4 compositions
- compositions: Fe2(Ti0.7Cr0.3)Al (4); Fe2(Ti0.6Cr0.4)Al (1); Fe2(Ti0.5Cr0.5)Al (1); Fe1.99Ti0.66Cr0.45Al0.90 (1)
- measured range: 21-566 K (5th-95th pct of 15 curves)
- papers: Thermoelectric properties of Fe2TiAl Heusler alloys | Crystal growth and flat-band effects on thermoelectric properties of Fe2TiAl-based full-Heusler thin films

## Al-Fe-Ti
- rank 837 | 7 samples | 3 papers | 7 compositions
- compositions: Fe2Ti0.86Ti0.22Al0.92 (1); Fe2.18Ti0.73Al1.09 (1); (Fe0.8Ti0.2)3Al (1); (Fe0.85Ti0.15)3Al (1); (Fe0.75Ti0.25)3Al (1); (Fe0.7Ti0.3)3Al (1)
- measured range: 12-1102 K (5th-95th pct of 11 curves; full span incl. outliers 12-1164 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti2AlFe F-43m (216) mp-999069 [hull=0.178, icsd=2, PRIMARY]; TiAlFe2 Fm-3m (225) mp-31187 [hull=0.000, icsd=1, PRIMARY]; Ti6Al16Fe7 Fm-3m (225) mp-1208277 [hull=0.027, PRIMARY]; TiAlFe Amm2 (38) mp-1217171 [hull=0.070, PRIMARY]; TiAlFe2 P4/mmm (123) mp-1217020 [hull=0.061]
- papers: Effects of off-stoichiometry and Ti doping on thermoelectric performance of Fe2VAl Heusler compound | Crystal growth and flat-band effects on thermoelectric properties of Fe2TiAl-based full-Heusler thin films | Electronic Structure and Transport Properties of Pseudogap System Fe2VAl

## Al-Ga-Ge-Sr
- rank 838 | 7 samples | 1 papers | 6 compositions
- compositions: Sr8Al6.3Ga10.3Ge29.4 (2); Sr8Al6.5Ga10.5Ge29 (1); Sr8Al6Ga10Ge30 (1); Sr8Al8Ga8Ge30 (1); Sr8Al7Ga11Ge28 (1); Sr8Al6.6Ga10.6Ge28.8 (1)
- measured range: 288-994 K (5th-95th pct of 10 curves)
- papers: Synthesis and thermoelectric properties of type-VIII germanium clathrates Sr8AlxGayGe46−x−y

## Al-La-O
- rank 839 | 7 samples | 6 papers | 1 compositions
- compositions: LaAlO3 (7)
- measured range: 10-356 K (5th-95th pct of 8 curves)
- [ref 1] TEDesignLab / ICSD: LaAlO3 Pm-3m (221) mp-5304 [hull=0.007, icsd=69, PRIMARY]; LaAlO3 R-3c (167) mp-2920 [hull=0.000, icsd=33]; LaAlO3 I4/mcm (140) mp-1080080 [hull=0.001, icsd=2]; LaAlO3 Imma (74) mp-1080060 [hull=0.001, icsd=1]; LaAlO3 (15)
- [ref 2] MP, ranked by ICSD evidence: La2Al4O9 Pbam (55) mp-768382 [hull=0.078, PRIMARY]; La3Al5O12 Ia-3d (230) mp-780432 [hull=0.034, PRIMARY]; La3AlO6 Cmc2_1 (36) mp-1178155 [hull=0.020, PRIMARY]; La3AlO Pm-3m (221) mp-1206996 [hull=0.000, PRIMARY]; La4Al6O15 C2/c (15) mp-1024042 [hull=0.071, PRIMARY]
- papers: Enhanced Thermoelectric Power Factor of NaxCoO2Thin Films by Structural Engineering | Strain Effect on Oxygen Evolution Reaction Activity of Epitaxial NdNiO<sub>3</sub> Thin Films | Irradiation induced modification in transport properties of LaNiO<sub>3</sub> thin films: An x-ray absorption study

## Al-Mn-Y
- rank 840 | 7 samples | 1 papers | 7 compositions
- compositions: YMn3Al9 (1); YMn3.5Al7.5 (1); YMn4Al8 (1); YMn5.3Al6.7 (1); YMn6.5Al5.5 (1); YMn2Al10 (1)
- measured range: 10-395 K (5th-95th pct of 21 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y(MnAl2)4 I4/mmm (139) mp-10896 [hull=0.000, icsd=2, PRIMARY]; Y(MnAl)6 Immm (71) mp-1216200 [hull=0.047, PRIMARY]; YMnAl Imma (74) mp-1215934 [hull=0.049, PRIMARY]
- papers: Thermoelectric properties of YMn4+xAl8−x for −2≤x≤2.5

## As-Ce-Ni-P
- rank 841 | 7 samples | 1 papers | 7 compositions
- compositions: CeNi2(As0.7P0.3)2 (1); CeNi2(As0.6P0.4)2 (1); CeNi2(As0.45P0.55)2 (1); CeNi2(As0.2P0.8)2 (1); CeNi2(As0.8P0.2)2 (1); CeNi2(As0.4P0.6)2 (1)
- solid-solution axis: As/(As+P) spans 0.20-0.80 (median 0.45) over 7 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 11-304 K (5th-95th pct of 7 curves)
- papers: Heavy fermion quantum criticality at dilute carrier limit in CeNi2−δ(As1−xPx)2

## As-La-Mn-O
- rank 842 | 7 samples | 2 papers | 7 compositions
- compositions: La0.94Sr0.06MnAsO (1); La0.92Sr0.08MnAsO (1); La1MnAsO (1); La0.98Sr0.02MnAsO (1); La0.96Sr0.04MnAsO (1); La0.9Sr0.1MnAsO (1)
- dopant candidates (<5% at.): Sr (5), Fe (1)
- measured range: 10-297 K (5th-95th pct of 11 curves)
- papers: Insulator-to-metal transition and large thermoelectric effect in La1−xSrxMnAsO | Studies on Effects of Impurity Doping and NMR Measurements of La 1111 and/or Nd 1111 Fe-Pnictide Superconductors

## Au-Ce-Si
- rank 843 | 7 samples | 1 papers | 1 compositions
- compositions: CeAu2Si2 (7)
- measured range: 11-279 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(SiAu)2 I4/mmm (139) mp-5173 [hull=0.000, icsd=5, PRIMARY]; Ce(SiAu2)2 P-4m2 (115) mp-601420 [hull=0.007, icsd=1, PRIMARY]; Ce8Co(Si4Au)3 Pmm2 (25) mp-1228667 [hull=0.000, PRIMARY]
- papers: Scaling behavior of temperature-dependent thermopower in<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:mrow><mml:msub><mml:mi>CeAu</mml:mi><mml:mn>2</mml:mn></mml:msub><mml:msub><mml:mi>Si</mml:mi><mml:mn>2</mml:mn></mml:msub></mml:mrow></mml:math>under pressure

## B-C-Nb-Si
- rank 844 | 7 samples | 1 papers | 7 compositions
- compositions: (NbB2)75(SiC)25 (1); (NbB2)61.84(SiC)27.1(C)11.06 (1); (NbB2)63.63(SiC)36.37 (1); (NbB2)63.37(SiC)35.01(C)1.62 (1); (NbB2)62.85(SiC)32.33(C)4.82 (1); (NbB2)62.34(SiC)29.69(C)7.96 (1)
- measured range: 303-573 K (5th-95th pct of 7 curves)
- papers: Effects ofSiCandSiC-GNP additions on the mechanical properties and oxidation behavior of NbB2

## B-Ca-Cu-O-Sr
- rank 845 | 7 samples | 1 papers | 1 compositions
- compositions: B1.6Pb0.4Sr2Ca2Cu3O10 (7)
- dopant candidates (<5% at.): Pb (7)
- measured range: 52-114 K (5th-95th pct of 14 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2CaCu6(BO3)6 C2 (5) mp-1218946 [hull=0.057, PRIMARY]
- papers: Thermoelectric and thermomagnetic effects of (B1.6Pb0.4) Sr2Ca2Cu3Ox thin films

## B-O
- rank 846 | 7 samples | 4 papers | 4 compositions
- compositions: B2O3 (3); B6O (2); (Li2O)10(B2O3)90 (1); (K2O)10(B2O3)90 (1)
- dopant candidates (<5% at.): Li (1), K (1)
- measured range: 165-1274 K (5th-95th pct of 7 curves; full span incl. outliers 165-1677 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): B2O3 P3_121 (152) mp-306 [hull=0.000, icsd=9, PRIMARY]; B6O R-3m (166) mp-1346 [hull=0.000, icsd=6, PRIMARY]; BaLi(B3O5)3 R3c (161) mp-17672 [hull=0.000, icsd=2, PRIMARY]; B8PbO15 P2_1/c (14) mp-1201012 [hull=0.153, icsd=2, PRIMARY]; Mg(B2O5)3 Pbca (61) mp-868019 [hull=0.714, icsd=2, PRIMARY]
- papers: Thermal Conductivity of Molten B2\nO3\n, B2\nO3\n-SiO2\n, Na2\nO-B2\nO3\n, and Na2\nO-SiO2\n Systems | Thermal conductivity of B2O3 glass under pressure | Thermoelectric Properties of Hot-pressed Boron Suboxide (B<SUB>6</SUB>O)

## B-Ti
- rank 847 | 7 samples | 4 papers | 4 compositions
- compositions: TiB2 (4); (Ti)93.12(TiB2)6.88 (1); (Ti)85.74(TiB2)14.26 (1); (TiB2)88.02(SiC)11.98 (1)
- dopant candidates (<5% at.): Si (1), C (1)
- measured range: 291-1170 K (5th-95th pct of 8 curves; full span incl. outliers 291-1473 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiB2 P6/mmm (191) mp-1145 [hull=0.000, icsd=16, PRIMARY]; TiB Pnma (62) mp-7857 [hull=0.000, icsd=4, PRIMARY]; Ti3B4 Immm (71) mp-1025170 [hull=0.000, icsd=1, PRIMARY]; Ti2B I4/mcm (140) mp-1025149 [hull=0.160, icsd=1, PRIMARY]; TiB F-43m (216) mp-10143 [hull=1.555, icsd=1]
- papers: Fabrication and contact resistivity of W–Si 3 N 4 /TiB 2 –Si 3 N 4 /p–SiGe thermoelectric joints | Thermal conductivities of Ti-SiC and Ti-TiB2 particulate composites | Microstructures and properties of silicon carbide- and graphene nanoplatelet-reinforced titanium diboride composites

## Ba-Bi-O-Rh
- rank 848 | 7 samples | 4 papers | 6 compositions
- compositions: Bi1.8Ba2Rh1.9O8 (2); Bi1.7Ba2(Co0.2Rh0.8)2O8 (1); Bi1.7Ba2Rh2O8 (1); (Bi0.9Pb0.1)1.8Ba2Rh1.9O8 (1); (Bi0.8Pb0.2)1.8Ba2Rh1.9O8 (1); Bi1.8Ba2Rh1.6O8 (1)
- dopant candidates (<5% at.): Pb (2), Co (1)
- measured range: 10-301 K (5th-95th pct of 20 curves)
- papers: Thermoelectric properties of bismuth based cobalt-rhodium oxides with hexagonal (Co,Rh)O2 layers | Transport Properties and Electronic States in the Layered Thermoelectric Rhodate (Bi1-xPbx)1.8Ba2Rh1.9Oy | Thermoelectric properties of cobalt rhodium oxides: [Bi2Ba2O4]p(Co,Rh)O2

## Ba-Ca-Cu-La-O
- rank 849 | 7 samples | 1 papers | 7 compositions
- compositions: CaLaBaCu3O6.71 (1); CaLaBaCu3O6.83 (1); CaLaBaCu3O6.86 (1); CaLaBaCu3O6.89 (1); CaLaBaCu3O6.76 (1); CaLaBaCu3O6.79 (1)
- measured range: 22-350 K (5th-95th pct of 14 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba3CaLa2(Cu3O7)2 Cmm2 (35) mp-1228470 [hull=0.035, PRIMARY]; Ba3CaLa2Cu6O13 Cm (8) mp-1228590 [hull=0.029, PRIMARY]
- papers: Thermoelectric power in CaLaBaCu3Oy (6.71<y<6.89)

## Ba-Co-Lu-O
- rank 850 | 7 samples | 2 papers | 7 compositions
- compositions: BaLuCo4O7 (1); LuBaCo4O7 (1); Lu0.96Pb0.04BaCo4O7 (1); Lu0.9Pb0.1BaCo4O7 (1); Lu0.98Pb0.02BaCo4O7 (1); Lu0.94Pb0.06BaCo4O7 (1)
- dopant candidates (<5% at.): Pb (5)
- measured range: 306-983 K (5th-95th pct of 28 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaLuCo4O7 P6_3mc (186) mp-19624 [hull=0.021, icsd=2, PRIMARY]; BaLu2CoO5 Pnma (62) mp-24891 [hull=0.009, icsd=1, PRIMARY]; BaLuCo4O7 Pna2_1 (33) mp-1200479 [hull=0.003, icsd=1]; BaLuCo4O7 Cc (9) mp-1193997 [hull=0.004, icsd=1]
- papers: Structural and thermoelectric properties of BaRCo4O7 (R = Dy, Ho, Er, Tm, Yb, and Lu) | Enhanced Thermoelectric Properties of Hole-Doped Lu1−x Pb x BaCo4O7 Ceramics
