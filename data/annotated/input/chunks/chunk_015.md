# Host systems -- chunk 015 of 73

Ranks 701-750 by sample count. These 50 host systems cover 450 samples (0.86% of the TE set); cumulative through this chunk: 85.67%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Ba-Fe-Nd-O
- rank 701 | 9 samples | 3 papers | 9 compositions
- compositions: La0.04Nd0.46Sr0.24Ba0.26FeO3 (1); Nd0.4Ba0.6Fe0.9Ni0.1O3 (1); Nd0.6Ba0.4Fe0.9Ni0.1O3 (1); Nd0.4Ba0.6Fe0.9Cu0.1O3 (1); Nd0.6Ba0.4Fe0.9Cu0.1O3 (1); Nd0.5Ba0.5Fe0.9Co0.1O3 (1)
- dopant candidates (<5% at.): Ni (3), Cu (3), Sr (1), La (1), Co (1)
- measured range: 298-1174 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaNdFe2O5 Pmc2_1 (26) mp-1182187 [hull=0.000, icsd=2, PRIMARY]; Ba2Nd2Fe4O11 Cmmm (65) mp-704634 [hull=0.005, icsd=1, PRIMARY]; Ba5SrNd2Fe4O15 Cc (9) mp-698854 [hull=0.000, PRIMARY]; Ba6Nd2Fe4O15 Cc (9) mp-1228695 [hull=0.000, PRIMARY]; BaNd(FeO3)2 Fm-3m (225) mp-1227836 [hull=0.062, PRIMARY]
- papers: Characterization of Ln0.5M0.5FeO3–δ (Ln=La, Nd, Sm; M=Ba, Sr) perovskites as SOFC cathodes | Doped (Nd,Ba)FeO3 oxides as potential electrodes for symmetrically designed protonic ceramic electrochemical cells | Designing a protonic ceramic fuel cell with novel electrochemically active oxygen electrodes based on doped Nd<sub>0.5</sub>Ba<sub>0.5</sub>FeO<sub>3−δ</sub>

## Ba-Ni-Sb-Sn
- rank 702 | 9 samples | 1 papers | 1 compositions
- compositions: Ba0.92Ni4Sb6.7Sn5.3 (9)
- measured range: 13-723 K (5th-95th pct of 16 curves)
- papers: Ba-filled Ni–Sb–Sn based skutterudites with anomalously high lattice thermal conductivity

## Ba-Sb-Zn
- rank 703 | 9 samples | 2 papers | 6 compositions
- compositions: BaZn2Sb2 (4); Ba(Zn0.998Ag0.002)2Sb2 (1); Ba(Zn0.996Ag0.004)2Sb2 (1); Ba(Zn0.992Ag0.008)2Sb2 (1); Ba(Zn0.994Ag0.006)2Sb2 (1); Ba(Zn0.99Ag0.01)2Sb2 (1)
- dopant candidates (<5% at.): Ag (5)
- measured range: 13-777 K (5th-95th pct of 36 curves)
- [ref 1] TEDesignLab / ICSD: Ba2ZnSb2 Ibam (72) mp-1079149 [hull=0.000, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ba(ZnSb)2 Pnma (62) mp-14207 [hull=0.000, icsd=1, PRIMARY]; BaZnSb2 I4/mmm (139) mp-1205765 [hull=0.010, PRIMARY]; Ba(ZnSb)2 I4mm (107) mp-1228651 [hull=0.209]
- papers: Thermoelectric properties and electronic structure of Zintl compound BaZn2Sb2 | Increasing the thermoelectric power factor via Ag substitution at Zn site in Ba(Zn1-Ag )2Sb2

## Bi-Cu-Te
- rank 704 | 9 samples | 2 papers | 6 compositions
- compositions: Bi0.38Te0.57Cu0.05 (2); Bi0.36Te0.54Cu0.10 (2); Bi0.370Te0.555Cu0.075 (2); Bi2.23Te3Cu0.97 (1); Bi2.28Te3Cu1.17 (1); Bi2.32Te3Cu2.06 (1)
- measured range: 295-514 K (5th-95th pct of 33 curves)
- papers: Investigations on morphology and thermoelectric transport properties of Cu+ ion implanted bismuth telluride thin film | Synthesis of heavily Cu-doped Bi2Te3 nanoparticles and their thermoelectric properties

## Bi-F-Pr-S
- rank 705 | 9 samples | 1 papers | 1 compositions
- compositions: PrO0.1F0.9BiS2 (9)
- dopant candidates (<5% at.): O (9)
- papers: Superconducting and magneto-transport properties of BiS2 based superconductor PrO1-xFxBiS2 (x = 0 to 0.9)

## Bi-Fe-O-Pb-Ti
- rank 706 | 9 samples | 2 papers | 9 compositions
- compositions: (Bi0.8La0.2FeO3)0.57(PbTiO3)0.43 (1); (Bi0.8La0.2FeO3)0.57(PbTiO3)0.43(Fe2O3)0.025 (1); (Bi0.8La0.2FeO3)0.57(PbTiO3)0.43(Fe2O3)0.05 (1); (Bi0.8La0.2FeO3)0.57(PbTiO3)0.43(Fe2O3)0.125 (1); (Bi0.8La0.2FeO3)0.57(PbTiO3)0.43(Fe2O3)0.25 (1); (BiFeO3)0.6(PbTiO3)0.27Ba0.13(Zr0.5Ti0.5)0.13O0.39 (1)
- dopant candidates (<5% at.): La (5), Ba (4), Zr (4)
- measured range: 322-854 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti2Fe3Bi3Pb2O15 Cmm2 (35) mp-1101108 [hull=0.021, PRIMARY]; Ti4FeBiPb4O15 Cmm2 (35) mp-1217456 [hull=0.004, PRIMARY]; TiFe2Bi2PbO9 Cmm2 (35) mp-1216956 [hull=0.022, PRIMARY]; TiFe3Bi3PbO12 P1 (1) mp-1217154 [hull=0.024, PRIMARY]; TiFeBiPbO6 Imm2 (44) mp-1216981 [hull=0.020, PRIMARY]
- papers: Enhanced insulation and piezoelectric properties of 0.57(Bi\n            <sub>0.8</sub>\n            La\n            <sub>0.2</sub>\n            )FeO\n            <sub>3</sub>\n            ‐0.43PbTiO\n            <sub>3</sub>\n            solid solutions with Fe addition | High‐temperature BiFeO\n            <sub>3</sub>\n            –PbTiO\n            <sub>3</sub>\n            ‐Ba(Zr,Ti)O\n            <sub>3</sub>\n            ternary ceramics with excellent piezoelectricity

## Bi-La-O-S-Se
- rank 707 | 9 samples | 3 papers | 4 compositions
- compositions: LaOBiSSe (4); LaOBiS1.4Se0.6 (2); LaOBiS1.2Se0.8 (2); LaOBiS1.6Se0.4 (1)
- solid-solution axis: S/(S+Se) spans 0.50-0.80 (median 0.70) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 296-741 K (5th-95th pct of 34 curves)
- papers: High thermoelectric performance and low thermal conductivity of densified LaOBiSSe | Enhancement of thermoelectric properties by Se substitution in layered bismuth-chalcogenide LaOBiS2-xSex | Electronic Origins of Large Thermoelectric Power Factor of LaOBiS2−xSex

## Bi-O-Rh-Sr
- rank 708 | 9 samples | 5 papers | 4 compositions
- compositions: Bi0.78Sr0.4RhO3 (5); Bi1.8Sr2Rh1.6O8 (2); (Bi0.8Pb0.2)1.8Sr2Rh1.6O8 (1); (Bi0.9Pb0.1)1.8Sr2Rh1.6O8 (1)
- dopant candidates (<5% at.): Pb (2)
- measured range: 10-300 K (5th-95th pct of 22 curves)
- papers: Thermal Conductivity of Thermoelectric Rhodium Oxides Measured by a Modified Harman Method | Enhanced thermoelectric properties in a layered rhodium oxide with a trigonal symmetry | Thermoelectric properties in the misfit-layered-cobalt oxides [Bi<inf>2</inf>A<inf>2</inf>O<inf>4</inf>][CoO<inf>2</inf>]<inf>b1/b2</inf> (A=Ca, Sr, Ba, b<inf>1</inf>/b<inf>2</inf>=1.65, 1.82, 1.98) single crystals

## Bi-O-S
- rank 709 | 9 samples | 1 papers | 1 compositions
- compositions: Bi4O4S3 (9)
- measured range: 10-300 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi2SO7 P2_1/c (14) mp-1201092 [hull=0.132, icsd=2, PRIMARY]; Bi2(SO4)3 C2/c (15) mp-1195213 [hull=0.007, icsd=1, PRIMARY]; Bi2SO2 Pnnm (58) mp-27891 [hull=0.000, icsd=1, PRIMARY]; CoBi6(SO8)2 C2 (5) mp-1190466 [hull=0.000, icsd=1, PRIMARY]; Bi2S2O9 C2/c (15) mp-1197960 [hull=0.000, icsd=1, PRIMARY]
- papers: Superconducting and thermoelectric properties of new layered superconductor Bi4O4S3

## C-N-Zr
- rank 710 | 9 samples | 1 papers | 9 compositions
- compositions: ZrC0.12N0.78 (1); ZrC0.40N0.55 (1); ZrC0.33N0.60 (1); ZrC0.25N0.68 (1); ZrC0.44N0.50 (1); ZrC0.62N0.34 (1)
- measured range: 297-2074 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zr2CN R-3m (166) mp-1215592 [hull=0.000, PRIMARY]; Zr4C3N R-3m (166) mp-1215389 [hull=0.000, PRIMARY]; Zr4CN3 R-3m (166) mp-1215387 [hull=0.002, PRIMARY]
- papers: Processing and properties of ZrC, ZrN and ZrCN ceramics: a review

## C-Pb-Te
- rank 711 | 9 samples | 3 papers | 8 compositions
- compositions: C@PbTe (2); PbTeC0.28 (1); PbTeC1.4 (1); PbTeC0.84 (1); PbTeC2 (1); PbTeC2.8 (1)
- dopant candidates (<5% at.): I (2)
- solid-solution axis: C/(C+Pb) spans 0.10-0.74 (median 0.50) over 8 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 299-824 K (5th-95th pct of 43 curves)
- papers: In situ synthesis and thermoelectric properties of PbTe–graphene nanocomposites by utilizing a facile and novel wet chemical method | Coupled hydrothermal synthesis/hot pressing of PbSe/C@PbTe heterostructured composites with enhanced thermoelectric performance | Enhanced thermoelectric performance of n-type PbTe through the introduction of low-dimensional C60 nanodots

## Ca-Fe-O-Pr
- rank 712 | 9 samples | 4 papers | 8 compositions
- compositions: Pr0.5Ca0.5Fe0.9W0.1O3 (2); Pr0.7Ca0.3Fe0.8Ni0.2O3 (1); Pr0.6Ca0.4Fe0.8Ni0.2O3 (1); Pr0.5Ca0.5Fe0.8Ni0.2O3 (1); Pr0.3Ca0.7Fe0.8Ni0.2O3 (1); Pr0.4Ca0.6Fe0.8Ni0.2O3 (1)
- dopant candidates (<5% at.): Ni (5), W (2), Co (1)
- measured range: 473-1122 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaPr3(FeO3)4 Pm (6) mp-1227161 [hull=0.000, PRIMARY]
- papers: Characterization of Pr<sub>0.5</sub>A<sub>0.5</sub>Fe<sub>0.9</sub>W<sub>0.1</sub>O<sub>3−<i>δ</i></sub> (A = Ca, Sr and Ba) as symmetric electrodes for solid oxide fuel cells | A novel one step synthesized Co-free perovskite/brownmillerite nanocomposite for solid oxide fuel cells | Synthesis and electric properties of perovskite Pr0.6Ca0.4Fe0.8Co0.2O3 for SOFC applications

## Ca-Sb-Yb
- rank 713 | 9 samples | 2 papers | 5 compositions
- compositions: Yb12Ca2MnSb11 (3); Yb10Ca4MnSb11 (3); Yb8Ca6MnSb11 (1); Yb6Ca8MnSb11 (1); Yb14Ca2Sb11 (1)
- dopant candidates (<5% at.): Mn (8)
- measured range: 18-1285 K (5th-95th pct of 14 curves)
- papers: Enhanced High-Temperature Thermoelectric Performance of Yb14–xCaxMnSb11 | Thermoelectric properties and electronic structure calculations of low thermal conductivity Zintl phase series M16X11 (M=Ca and Yb; X=Sb and Bi)

## Cd-Ge-Te
- rank 714 | 9 samples | 1 papers | 8 compositions
- compositions: Ge0.88Cd0.08Cd0.04Te (2); Ge0.90Cd0.10Te (1); Ge0.90Cd0.08Cd0.02Te (1); Ge0.87Cd0.08Cd0.05Te (1); Ge0.865Cd0.08Cd0.055Te (1); Ge0.95Cd0.08Cd0.07Te (1)
- measured range: 300-803 K (5th-95th pct of 43 curves)
- papers: Thermoelectric Transport Properties of CdxBiyGe1–x–yTe Alloys

## Ce-In-Sn
- rank 715 | 9 samples | 1 papers | 9 compositions
- compositions: Ce(In0.9Sn0.1)3 (1); Ce(In0.8Sn0.2)3 (1); Ce(In0.7Sn0.3)3 (1); Ce(In0.6Sn0.4)3 (1); Ce(In0.5Sn0.5)3 (1); Ce(In0.3Sn0.7)3 (1)
- measured range: 10-296 K (5th-95th pct of 13 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce2(InSn)3 Pmmm (47) mp-1227310 [hull=0.000, PRIMARY]
- papers: Thermoelectric power and electrical resistivity of Ce(In1-xSnx)3 and (Ce1-xLaxIn3

## Ce-Nd-Pd
- rank 716 | 9 samples | 1 papers | 9 compositions
- compositions: Nd0.4Ce0.6Pd3 (1); Nd0.6Ce0.4Pd3 (1); Nd0.7Ce0.3Pd3 (1); (Nd0.6Ce0.4)Pd3 (1); Th0.05(Nd0.6Ce0.4)0.95Pd3 (1); Th0.1(Nd0.6Ce0.4)0.9Pd3 (1)
- dopant candidates (<5% at.): Th (4)
- solid-solution axis: Ce/(Ce+Nd) spans 0.30-0.60 (median 0.40) over 9 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 11-300 K (5th-95th pct of 35 curves)
- papers: Modification of the thermoelectric properties of CePd3 by the substitution of neodymium and thorium

## Co-Eu-O-Sr
- rank 717 | 9 samples | 3 papers | 5 compositions
- compositions: SrEuCoO4 (3); Eu2SrCo1.5Fe0.5O7 (3); Eu0.75Sr1.25CoO4 (1); EuSrCoO4 (1); Eu1.25Sr0.75CoO4 (1)
- dopant candidates (<5% at.): Fe (3)
- measured range: 12-1173 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrEu(CoO3)2 P4/mmm (123) mp-1218310 [hull=0.123, PRIMARY]; SrEuCoO4 I4mm (107) mp-1218291 [hull=0.041, PRIMARY]
- papers: Studies of structural, magnetic, electrical and thermal properties in layered perovskite cobaltite SrLnCoO4 (Ln = La, Ce, Pr, Nd, Eu, Gd and Tb) | Dielectric, magnetic, and magnetotransport properties in Sr doped two-dimensional RE2CoO4 (RE=Pr,Eu) compounds | Eu<sub>2</sub>SrCo<sub>1.5</sub>Fe<sub>0.5</sub>O<sub>7</sub> a new promising Ruddlesden–Popper member as a cathode component for intermediate temperature solid oxide fuel cells

## Co-Fe-Ge-Si
- rank 718 | 9 samples | 1 papers | 5 compositions
- compositions: Fe0.241Co0.063Si0.686Ge0.06Cu0.014P0.03 (5); Fe0.241Co0.063Si0.686Ge0.06Cu0.013P0.04 (1); Fe0.241Co0.063Si0.686Ge0.06Cu0.013P0.05 (1); Fe0.241Co0.063Si0.686Ge0.06Cu0.007P0.03Sb0.01 (1); Fe0.241Co0.063Si0.686Ge0.06Cu0.007P0.03Sb0.02 (1)
- dopant candidates (<5% at.): P (9), Cu (9), Sb (2)
- measured range: 303-1073 K (5th-95th pct of 37 curves)
- papers: Improved Thermoelectric Performance of Eco‐Friendly β‐FeSi\n            2\n            –SiGe Nanocomposite via Synergistic Hierarchical Structuring, Phase Percolation, and Selective Doping

## Co-Fe-La-O
- rank 719 | 9 samples | 3 papers | 9 compositions
- compositions: La2CoFeO6 (1); La1.8Sr0.2CoFeO6 (1); La1.6Sr0.4CoFeO6 (1); La0.9Sr0.1Co0.50Fe0.50O3 (1); La0.8Sr0.2Co0.3Fe0.7O3 (1); La0.8Sr0.2Co0.7Fe0.3O3 (1)
- dopant candidates (<5% at.): Sr (8)
- measured range: 322-1279 K (5th-95th pct of 19 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2FeCoO6 P2_1/c (14) mp-1223373 [hull=0.013, PRIMARY]; La4Fe(CoO4)3 P-1 (2) mp-1223109 [hull=0.006, PRIMARY]
- papers: Enhancement of thermoelectric power factor by inducing octahedral ordering in \nLa2−xSrxCoFeO6\n double perovskites | EFFECT OF Sr2+DOPING ON THE STRUCTURAL, THERMAL, DIELECTRIC AND ELECTRICAL PROPERTIES OF La1-xSrxCo0.50Fe0.50 O3 {0.1≤ x≤ 0.4}CATHODE FOR SOFCS | Structure and electrical properties of La1−xSrxCo1−yFeyO3. Part 1. The system La0.8Sr0.2Co1−yFeyO3

## Co-Fe-La-Sb
- rank 720 | 9 samples | 8 papers | 5 compositions
- compositions: LaFe3CoSb12 (3); La0.9Fe3CoSb12 (2); La0.9FeCo3Sb12 (2); Yb0La0.85Fe2.7Co1.3Sb12 (1); La0.9CoFe3Sb12 (1)
- measured range: 15-824 K (5th-95th pct of 38 curves)
- papers: Thermoelectric properties of p-type YbxLayFe2.7Co1.3Sb12 double-filled skutterudites | Thermoelectric properties of La filled skutterudite prepared by mechanical alloying and hot pressing | Preparation and thermoelectric properties of LaxFeCo3Sb12 skutterudites by mechanical alloying and hot pressing

## Co-La-O-Sr-Ti
- rank 721 | 9 samples | 2 papers | 4 compositions
- compositions: La0.3Sr0.7Ti0.4Co0.6O3 (6); Sr1.2La0.8CoTiO6 (1); La0.3Sr0.7Ti0.7Co0.3O3 (1); La0.3Sr0.7Ti0.55Co0.45O3 (1)
- measured range: 300-1173 K (5th-95th pct of 9 curves; full span incl. outliers 300-1241 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrLa3Ti2(CoO6)2 P-4m2 (115) mp-1218234 [hull=0.085, PRIMARY]
- papers: Structural and semiconductor-to-metal transitions of double-perovskite cobalt oxide Sr2−xLaxCoTiO6−δ with enhanced thermoelectric capability | Evaluation of La<sub>0.3</sub>Sr<sub>0.7</sub>Ti<sub>1−x</sub>Co<sub>x</sub>O<sub>3</sub> as a potential cathode material for solid oxide fuel cells

## Co-Ni-Y
- rank 722 | 9 samples | 1 papers | 9 compositions
- compositions: Y(Co0.7Ni0.3)2 (1); Y(Co0.4Ni0.6) (1); Y(Co0.2Ni0.8)2 (1); Y(Co0.9Ni0.1)2 (1); Y(Co0.8Ni0.2)2 (1); Y(Co0.6Ni0.4)2 (1)
- measured range: 12-982 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y2(CoNi)5 Pmmm (47) mp-1216167 [hull=0.080, PRIMARY]; Y2CoNi5 R3m (160) mp-1216367 [hull=0.034, PRIMARY]; Y6CoNi Pmc2_1 (26) mp-1216144 [hull=0.008, PRIMARY]; YCo3Ni2 P6/mmm (191) mp-1215948 [hull=0.044, PRIMARY]; YCoNi Imma (74) mp-1215957 [hull=0.042, PRIMARY]
- papers: Electrical properties and spin fluctuations studies of Y(Co1−xNix)2 compounds

## Co-Sb-Sn-Ti-Zr
- rank 723 | 9 samples | 4 papers | 8 compositions
- compositions: Ti0.5Zr0.5CoSb0.8Sn0.2 (2); Zr0.7Ti0.3CoSn0.3Sb0.7 (1); Zr0.5Ti0.5CoSn0.3Sb0.7 (1); Ti 0.65 Zr0.5 Hf0.15 CoSb0.35 Sn0.65 (1); Ti0.6Zr0.4CoSb0.8Sn0.2 (1); Ti0.4Zr0.6CoSb0.8Sn0.2 (1)
- dopant candidates (<5% at.): Hf (1)
- solid-solution axis: Ti/(Ti+Zr) spans 0.20-0.80 (median 0.50) over 8 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 18-982 K (5th-95th pct of 37 curves)
- papers: Thermoelectric properties of p-type half-Heusler alloys Zr1−xTixCoSnySb1−y (0.0<x<0.5; y=0.15 and 0.3) | Enhanced thermoelectric performance in the p-type half-Heusler (Ti/Zr/Hf)CoSb0.8Sn0.2 system via phase separation | Half-Heusler materials as model systems for phase-separated thermoelectrics

## Cr-Mn-Si
- rank 724 | 9 samples | 5 papers | 9 compositions
- compositions: Mn0.75Cr0.15Ru0.1Si1.74 (1); (Mn0.8Cr0.2)Si1.758 (1); Cr0.6Mn04Si (1); Cr0.4Mn0.6Si (1); Cr0.8Mn0.2Si (1); Cr0.1Mn0.9Si (1)
- dopant candidates (<5% at.): Ru (1)
- measured range: 13-1001 K (5th-95th pct of 24 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn2CrSi Fm-3m (225) mp-1185616 [hull=0.010, PRIMARY]; MnCrSi2 P2_1 (4) mp-1221675 [hull=0.056, PRIMARY]; Mn2CrSi Immm (71) mp-1097306 [hull=2.994]
- papers: The role of simultaneous substitution of Cr and Ru on the thermoelectric properties of defect manganese silicides MnSiδ (1.73<δ<1.75) | Crystal Structure and Thermoelectric Properties of Chimney-Ladder Higher Manganese Silicides | Filling dependence of thermoelectric power in transition-metal monosilicides

## Cr-S-Se
- rank 725 | 9 samples | 3 papers | 9 compositions
- compositions: Cr2S2.4Se0.6 (1); Cr2S0.6Se2.4 (1); Cr2S2.1Se0.9 (1); Cr2S1.5Se1.5 (1); Mn0.04Cr1.96Se2.7S0.3 (1);  Cr3S3.5Se0.5 (1)
- dopant candidates (<5% at.): Mn (1)
- solid-solution axis: S/(S+Se) spans 0.10-0.87 (median 0.62) over 9 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 301-897 K (5th-95th pct of 16 curves; full span incl. outliers 301-938 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cr2SeS P-6m2 (187) mp-1226267 [hull=0.151, PRIMARY]; Cr4(SeS)3 R3 (146) mp-1226292 [hull=0.036, PRIMARY]
- papers: Thermoelectric properties of chromium sulfo-selenides | Enhanced Thermoelectric Properties of Codoped Cr2Se3: The Distinct Roles of Transition Metals and S | About the Impact of Defect Phases on the Thermoelectric Properties of Cr\n            <sub>3</sub>\n            S\n            <sub>\n              4–\n              <i>x</i>\n            </sub>\n            Se\n            <sub>\n              <i>x</i>\n            </sub>

## Cs-Ge-Na
- rank 726 | 9 samples | 4 papers | 3 compositions
- compositions: Cs8Na9.94Tl6.06Ge136 (4); Cs8Na16Ge136 (3); Cs8Na16Cu5Ge131 (2)
- dopant candidates (<5% at.): Tl (4), Cu (2)
- measured range: 11-881 K (5th-95th pct of 18 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CsNa2Ge17 Fd-3m (227) mp-640321 [hull=0.000, icsd=6, PRIMARY]; CsNaGe2 P2_1/c (14) mp-29566 [hull=0.000, icsd=1, PRIMARY]
- papers: Structure and properties of type-II clathrate Cs8Na16−xTlxGe136 | Synthesis and characterization of framework-substituted Cs8Na16Cu5Ge131 | Temperature dependent structural and transport properties of the type II clathrates A8Na16E136 (A=Cs or Rb and E=Ge or Si)

## Cu-S-Ti
- rank 727 | 9 samples | 2 papers | 6 compositions
- compositions: CuTi2S4 (4); Cu0.875Ti2S4 (1); Cu0.625Ti2S4 (1); Cu0.375Ti2.25S4 (1); Cu0.75Ti2S4 (1); Cu0.5Ti2.25S4 (1)
- measured range: 299-674 K (5th-95th pct of 42 curves; full span incl. outliers 14-674 K)
- [ref 1] TEDesignLab / ICSD: Ti(CuS)4 I-42m (121) mp-29091 [hull=0.000, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ti2CuS4 Fd-3m (227) mp-3951 [hull=0.000, icsd=5, PRIMARY]; Ti10Cu7S20 Cm (8) mp-674343 [hull=0.034, PRIMARY]; Ti16CuS32 R3m (160) mp-767157 [hull=0.016, PRIMARY]; Ti3CuS6 P3m1 (156) mp-686094 [hull=0.001, PRIMARY]; Ti4CuS8 F-43m (216) mp-1217123 [hull=0.001, PRIMARY]
- papers: Thermoelectric Properties and Electronic Structures of CuTi2S4 Thiospinel and Its Derivatives: Structural Design for Spinel-Related Thermoelectric Materials | Thermoelectric materials taking advantage of spin entropy: lessons from chalcogenides and oxides

## Er-Ni-Sb
- rank 728 | 9 samples | 5 papers | 4 compositions
- compositions: ErNiSb (5); ErNiSn0.05Sb0.95 (2); ErNiSn0.01Sb0.99 (1); ErNiSn0.03Sb0.97 (1)
- dopant candidates (<5% at.): Sn (4)
- measured range: 11-992 K (5th-95th pct of 38 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ErNiSb F-43m (216) mp-21272 [hull=0.000, icsd=3, PRIMARY]; Er(NiSb)2 P4/nmm (129) mp-1079414 [hull=0.122, icsd=1, PRIMARY]; Er10NiSb5 Pmc2_1 (26) mp-1225477 [hull=0.000, PRIMARY]; Er5Ni2Sb I4/mcm (140) mp-1213207 [hull=0.000, PRIMARY]
- papers: Effect of Sn doping on the thermoelectric properties of ErNiSb-based p-type half-Heusler compound | Thermoelectric properties of p-type half-Heusler compound: Sn-doped ErNiSb | High-temperature power factor of half-Heusler phases RENiSb (RE = Sc, Dy, Ho, Er, Tm, Lu)

## Eu-Ge-Ni-Si
- rank 729 | 9 samples | 2 papers | 6 compositions
- compositions: EuNi(Si0.8Ge0.2)3 (4); EuNi2(Si0.25Ge0.75)2 (1); EuNi2(Si0.5Ge0.5)2 (1); EuNi2(Si0.3Ge0.7)2 (1); EuNi2(Si0.21Ge0.79)2 (1); EuNi2(Si0.18Ge0.82)2 (1)
- solid-solution axis: Ge/(Ge+Si) spans 0.20-0.82 (median 0.75) over 6 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-288 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): EuSiNi2Ge I4mm (107) mp-1225155 [hull=0.001, PRIMARY]
- papers: Thermoelectric power of EuNi2(Si1−xGex)2 | Pressure Effect on Transport Properties of EuNi(Si1-xGex)3 Compounds

## Eu-O-Sr-Ti
- rank 730 | 9 samples | 2 papers | 3 compositions
- compositions: Sr0.25Eu0.75TiO3 (4); Sr0.75Eu0.25TiO3 (4); (Sr0.5Eu0.5)Ti0.8Nb0.2O3 (1)
- dopant candidates (<5% at.): Nb (1)
- measured range: 12-1288 K (5th-95th pct of 11 curves)
- papers: The effect of Eu substitution on thermoelectric properties of SrTi0.8Nb0.2O3 | Influence of the Oxygen Content on the Electronic Transport Properties of SrxEu1–xTiO3-δ

## Fe-N
- rank 731 | 9 samples | 2 papers | 6 compositions
- compositions: Fe4N (3); Fe0.81N0.19 (2); Fe0.86N0.14 (1); Fe0.92N0.08 (1); Fe0.925N0.075 (1); Fe0.93N0.07 (1)
- measured range: 10-303 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe3N P6_322 (182) mp-1804 [hull=0.000, icsd=9, PRIMARY]; Fe8N I4/mmm (139) mp-555 [hull=0.003, icsd=8, PRIMARY]; FeN F-43m (216) mp-6988 [hull=0.000, icsd=4, PRIMARY]; Fe2N P-31m (162) mp-248 [hull=0.057, icsd=3, PRIMARY]; Fe4N Pm-3m (221) mp-535 [hull=0.018, icsd=3, PRIMARY]
- papers: Transport properties of iron nitride films prepared by ion beam assisted deposition | Anomalous Hall effects in pseudo-single-crystal <i>γ</i>′-Fe<sub>4</sub>N thin films

## Fe-Nb-Sb-Ti-V
- rank 732 | 9 samples | 3 papers | 9 compositions
- compositions: Fe(V0.6Nb0.4)0.84Ti0.16Sb (1); Fe(V0.6Nb0.4)0.80Ti0.20Sb (1); Fe(V0.6Nb0.4)0.76Ti0.24Sb (1); Fe(V0.6Nb0.4)0.82Ti0.18Sb (1); (V0.6Nb0.4)0.8Ti0.2FeSb (1); Fe(Nb0.75V0.25)0.8Ti0.2Sb (1)
- solid-solution axis: Nb/(Nb+V) spans 0.30-0.75 (median 0.40) over 9 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-1050 K (5th-95th pct of 29 curves)
- papers: High Band Degeneracy Contributes to High Thermoelectric Performance in p-Type Half-Heusler Compounds | Unique Role of Refractory Ta Alloying in Enhancing the Figure of Merit of NbFeSb Thermoelectric Materials | Are Solid Solutions Better in FeNbSb‐Based Thermoelectrics?

## Ga
- rank 733 | 9 samples | 4 papers | 4 compositions
- compositions: Ga (6); Ga0.999In0.001 (1); Ga0.9995In0.0005 (1); Ga0.9999In0.0001 (1)
- dopant candidates (<5% at.): In (3)
- measured range: 302-773 K (5th-95th pct of 2 curves; full span incl. outliers 302-1053 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ga Cmce (64) mp-142 [hull=0.000, icsd=9, PRIMARY]; Ga Cmcm (63) mp-1067880 [hull=0.010, icsd=2]; Ga I4/mmm (139) mp-140 [hull=0.026, icsd=2]
- papers: Electronic transport properties of liquid Ga–Zn alloys | Thermophysical Properties of the Liquid Ga–In–Sn Eutectic Alloy | Thermoelectric power of pure gallium. I. Temperature dependence

## Ga-Zn
- rank 734 | 9 samples | 1 papers | 9 compositions
- compositions: Ga0.7Zn0.3 (1); Ga0.4Zn0.6 (1); Ga0.9Zn0.1 (1); Ga0.6Zn0.4 (1); Ga0.8Zn0.2 (1); Ga0.2Zn0.8 (1)
- measured range: 561-1077 K (5th-95th pct of 18 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZnGa3 Pm-3m (221) mp-971720 [hull=0.074, PRIMARY]
- papers: Electronic transport properties of liquid Ga–Zn alloys

## Ge-Ir-Lu
- rank 735 | 9 samples | 1 papers | 2 compositions
- compositions: Lu3Ir4Ge13 (8); (Yb0.3Lu0.7)3Ir4Ge13 (1)
- dopant candidates (<5% at.): Yb (1)
- measured range: 11-180 K (5th-95th pct of 2 curves; full span incl. outliers 11-298 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Lu3Ge13Ir4 Pm-3n (223) mp-1197864 [hull=0.005, icsd=1, PRIMARY]; Lu3Ge3Ir2 Cmcm (63) mp-30235 [hull=0.000, icsd=1, PRIMARY]; Lu5(Ge5Ir2)2 P4/mbm (127) mp-1196530 [hull=0.000, icsd=1, PRIMARY]; LuGeIr Pnma (62) mp-10999 [hull=0.000, icsd=1, PRIMARY]
- papers: Low-carrier density and fragile magnetism in a Kondo lattice system

## Hf-Ni-Pd-Sn-Zr
- rank 736 | 9 samples | 3 papers | 5 compositions
- compositions: Zr0.5Hf0.5Ni0.8Pd0.2Sn0.99Sb0.01 (4);  Zr0.5Hf0.5Ni0.8Pd0.2Sn0.99Sb0.01 (2); Zr0.5Hf0.5Ni0.5Pd0.5Sn0.99Sb0.01 (1); (Zr0.5Hf0.5Ni0.8Pd0.2Sn0.99Sb0.01)92.9(HfO2)7.1 (1); (Zr0.5Hf0.5Ni0.8Pd0.2Sn0.99Sb0.01)97.03(HfO2)2.97 (1)
- dopant candidates (<5% at.): Sb (9), O (2)
- measured range: 296-1001 K (5th-95th pct of 42 curves)
- papers: The high temperature thermoelectric performances of Zr0.5Hf0.5Ni0.8Pd0.2Sn0.99Sb0.01 alloy with nanophase inclusions | Effects of partial substitution of Ni by Pd on the thermoelectric properties of ZrNiSn-based half-Heusler compounds | Structure and Thermoelectric Properties Correlation in half-Heusler ZrNiSn- based Bulk Nano-composite Materials by Transmission Electron Microscopy

## Ho-O-Sb
- rank 737 | 9 samples | 3 papers | 4 compositions
- compositions: Ho2SbO2 (6); Ho3SbO3 (1); Ho8Sb3O8 (1); Ho2Sb0.8Bi0.2O3 (1)
- dopant candidates (<5% at.): Bi (1)
- measured range: 11-392 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ho2SbO2 I4/mmm (139) mp-1067935 [hull=0.000, icsd=1, PRIMARY]; Ho3SbO3 C2/m (12) mp-1104812 [hull=0.034, icsd=1, PRIMARY]; Ho2Sb2O7 P3_121 (152) mp-780448 [hull=0.007, PRIMARY]; Ho3Sb5O12 I-43m (217) mp-771762 [hull=0.000, PRIMARY]; Ho3SbO7 C222_1 (20) mp-1212301 [hull=0.000, PRIMARY]
- papers: Synthesis, Crystal and Electronic Structures of New Narrow-Band-Gap Semiconducting Antimonide Oxides RE3SbO3and RE8Sb3−δO8, with RE = La, Sm, Gd, and Ho | Decoupling the Electrical Conductivity and Seebeck Coefficient in theRE2SbO2Compounds through Local Structural Perturbations | Rare-Earth Pnictide Oxides (RE,Ca)mPnnOm (Pn = Sb, Bi): A Review of Crystal Structures, Chemistry, Compositions, and Physical Properties

## Ho-Pd-Sb
- rank 738 | 9 samples | 4 papers | 5 compositions
- compositions: HoPdSb (5); HoPd2Sb (1); HoPd1.02Sb1.05 (1); HoPdSb1.05 (1); HoPd1.02Sb (1)
- measured range: 10-350 K (5th-95th pct of 20 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ho5Sb2Pd Pnma (62) mp-1200650 [hull=0.003, icsd=1, PRIMARY]; Ho5SbPd2 I4/mcm (140) mp-1212203 [hull=0.000, PRIMARY]; HoSbPd2 Fm-3m (225) mp-977574 [hull=0.000, PRIMARY]
- papers: Physical properties of rare-earth-based Heusler phases REPdZ and REPd/sub 2/Z (Z = Sb,Bi) | Magnetic and transport properties of the rare-earth-based Heusler phasesRPdZandRPd2Z(Z=Sb,Bi) | Antimonides with the half-Heusler structure: New thermoelectric materials

## In-Sb-Zn
- rank 739 | 9 samples | 3 papers | 6 compositions
- compositions: Zn5Sb4In1.85 (4); (ZnSb)60(InSb)40 (1); (ZnSb)50(InSb)50 (1); (ZnSb)80(InSb)20 (1); (ZnSb)70(InSb)30 (1); (ZnSb)90(InSb)10 (1)
- measured range: 10-623 K (5th-95th pct of 24 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zn9(InSb3)2 P2_12_12_1 (19) mp-1202823 [hull=0.046, icsd=2, PRIMARY]
- papers: Thermoelectric Properties of (ZnSb)1-x-(MSb)x Binary Systems | Zn5Sb4In2−δ— a Ternary Derivative of Thermoelectric Zinc Antimonides | Thermoelectric properties of Zn5Sb4In2-δ (δ = 0.15)

## Ir-O
- rank 740 | 9 samples | 4 papers | 2 compositions
- compositions: IrO2 (7); Ir0.9Sn0.1O2 (2)
- dopant candidates (<5% at.): Sn (2)
- measured range: 10-899 K (5th-95th pct of 9 curves; full span incl. outliers 10-998 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): IrO2 P4_2/mnm (136) mp-2723 [hull=0.000, icsd=7, PRIMARY]; IrO3 Cmcm (63) mp-1097041 [hull=0.000, PRIMARY]; IrO2 Pa-3 (205) mp-1095353 [hull=0.094, icsd=1]; IrO2 I4_1/amd (141) mp-1014261 [hull=0.258]; IrO3 Amm2 (38) mp-1022963 [hull=0.037]
- papers: Electrical Transport Properties of Ir<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">O</mml:mi></mml:mrow><mml:mrow><mml:mn>2</mml:mn></mml:mrow></mml:msub></mml:mrow></mml:math>and Ru<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">O</mml:mi></mml:mrow><mml:mrow><mml:mn>2</mml:mn></mml:mrow></mml:msub></mml:mrow></mml:math> | Temperature dependence of the resistivity of RuO2 and IrO2 | Enhanced Electron Correlation and Significantly Suppressed Thermal Conductivity in Dirac Nodal‐Line Metal Nanowires by Chemical Doping

## La-O-Sr-V
- rank 741 | 9 samples | 2 papers | 5 compositions
- compositions: La0.74Sr0.26VO3 (2); La0.6Sr0.4VO3 (2); La0.4Sr0.6VO3 (2); La0.7Sr0.3VO3 (2); La0.75Sr0.25VO3 (1)
- measured range: 11-1244 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr3LaV3O12 Cm (8) mp-1218724 [hull=0.039, PRIMARY]; SrLaVO4 I4mm (107) mp-1218139 [hull=0.005, PRIMARY]; SrLaVO4 Cmcm (63) mp-1218174 [hull=0.016]
- papers: Thermoelectric response in the incoherent transport region near Mott transition: The case study of La1−xSrxVO3 | Metal-insulator transition in low dimensional La<sub>0.75</sub>Sr<sub>0.25</sub>VO<sub>3</sub> thin films

## N-Ti
- rank 742 | 9 samples | 5 papers | 4 compositions
- compositions: TiN (6); TiN0.9 (1); TiN0.83 (1); TiN0.72 (1)
- measured range: 17-1299 K (5th-95th pct of 9 curves; full span incl. outliers 17-1471 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiN Fm-3m (225) mp-492 [hull=0.000, icsd=34, PRIMARY]; Ti2N P4_2/mnm (136) mp-8282 [hull=0.000, icsd=1, PRIMARY]; Ti3N I4/mmm (139) mp-980940 [hull=1.339, PRIMARY]; Ti19N25 R-3m (166) mp-32584 [hull=0.371, PRIMARY]; Ti3N2 R-3c (167) mp-1187591 [hull=0.017, PRIMARY]
- papers: Titanium carbonitride-based cermets: processes and properties | Phonon and electron contributions to the thermal conductivity of \nVNx\n epitaxial layers | Thermophysical properties of several nitrides prepared by spark plasma sintering

## Nd-O-Zr
- rank 743 | 9 samples | 5 papers | 4 compositions
- compositions: Nd2Zr2O7 (6); (Nd)2Zr2O7 (1); (Nd0.8Yb0.2)2Zr2O7 (1); (Nd0.8Ce0.2)2Zr2O7.2 (1)
- dopant candidates (<5% at.): Yb (1), Ce (1)
- measured range: 293-1470 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Nd2Zr2O7 Fd-3m (227) mp-5977 [hull=0.000, icsd=8, PRIMARY]; Nd16Zr16O49 P1 (1) mp-675021 [hull=0.071, PRIMARY]; Nd2Zr8O19 Pmm2 (25) mp-675068 [hull=0.117, PRIMARY]; Nd3GdZr4O14 R-3m (166) mp-1220577 [hull=0.364, PRIMARY]; Nd3HoZr4O14 R-3m (166) mp-1220266 [hull=0.034, PRIMARY]
- papers: Electrical and thermal conductivities of rare-earth A2Zr2O7 (A = Pr, Nd, Sm, Gd, and Er) | Effects of Yb3+ doping on phase structure, thermal conductivity and fracture toughness of (Nd1-xYbx)2Zr2O7 | Low-Thermal-Conductivity Rare-Earth Zirconates for Potential Thermal-Barrier-Coating Applications

## Ni-Sn-Zn
- rank 744 | 9 samples | 2 papers | 5 compositions
- compositions: ZnNiSn (5); Zn27.0Ni40.4Sn32.6 (1); Zn29.5Ni38.2Sn32.3 (1); Zn27.7Ni39.1Sn33.2 (1); Zn29.6Ni37.5Sn32.8 (1)
- measured range: 300-1001 K (5th-95th pct of 24 curves)
- papers: Thermoelectric Properties of Amorphous Zr-Ni-Sn Thin Films Deposited by Magnetron Sputtering | Preparation of ZrNiSn half-Heusler compounds with crystalline alignment by unidirectional solidification in short-duration microgravity and their thermoelectric properties

## O-Re
- rank 745 | 9 samples | 2 papers | 1 compositions
- compositions: ReO3 (9)
- measured range: 31-296 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ReO3 Im-3 (204) mp-20741 [hull=0.005, icsd=18, PRIMARY]; ReO2 Pbcn (60) mp-7228 [hull=0.003, icsd=2, PRIMARY]; Re2O9 P2_1/m (11) mp-1179674 [hull=0.336, icsd=2, PRIMARY]; ReO5 I4_1/a (88) mp-1179307 [hull=0.449, icsd=1, PRIMARY]; Re2O7 P2_12_12_1 (19) mp-1016092 [hull=0.000, icsd=1, PRIMARY]
- papers: Preparation of conductive ReO<sub>3</sub>thin films | Interface Conduction between Conductive ReO<sub>3</sub> Thin Film and NdBa<sub>2</sub>Cu<sub>3</sub>O<sub>6</sub> Thin Film

## O-Ru-Tl
- rank 746 | 9 samples | 2 papers | 9 compositions
- compositions: Tl2Mn0.3Ru1.7O7 (1); Tl2Ru2O6.5 (1); Tl1.8Ru2O6.5 (1); Tl1.7Ru2O6.55 (1); Tl1.8Ru2O6.7 (1); Tl1.9Ru2O6.85 (1)
- dopant candidates (<5% at.): Mn (1)
- measured range: 10-290 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Tl2Ru2O7 Fd-3m (227) mp-22094 [hull=0.000, icsd=2, PRIMARY]
- papers: Magnetoresistance in Tl2Mn2O7 pyrochlore: magnetic and charge density effects | High-Pressure Synthesis, Crystal Structure, and Metal–Semiconductor Transitions in the Tl2Ru2O7−δPyrochlore

## O-Ta
- rank 747 | 9 samples | 2 papers | 9 compositions
- compositions: TaO (1); TaO1.3 (1); TaO1.5 (1); Ta0.53O0.47 (1); Ta0.49O0.51 (1); Ta0.47O0.53 (1)
- measured range: 18-349 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TaO Fm-3m (225) mp-1895 [hull=1.105, icsd=5, PRIMARY]; TaO2 P4_2/mnm (136) mp-20994 [hull=0.071, icsd=5, PRIMARY]; Ta2O5 C2/c (15) mp-10390 [hull=0.008, icsd=3, PRIMARY]; Ba2Ta15O32 R-3 (148) mp-28457 [hull=0.000, icsd=1, PRIMARY]; Ta2O I-43m (217) mp-27873 [hull=1.769, icsd=1, PRIMARY]
- papers: Correlation between the transport mechanisms in conductive filaments inside Ta2O5-based resistive switching devices and in substoichiometric TaOx thin films | Tantalum Suboxide Films with Tunable Composition and Electrical Resistivity Deposited by Reactive Magnetron Sputtering

## O-Yb
- rank 748 | 9 samples | 3 papers | 2 compositions
- compositions: Yb2O3 (5); YbO (4)
- measured range: 11-854 K (5th-95th pct of 21 curves; full span incl. outliers 11-1471 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb2O3 Ia-3 (206) mp-2814 [hull=0.199, icsd=26, PRIMARY]; YbO Fm-3m (225) mp-1216 [hull=0.000, icsd=2, PRIMARY]; Yb3O4 Pnma (62) mp-1194318 [hull=0.097, icsd=1, PRIMARY]; YbO2 P-42_1m (113) mp-1178667 [hull=0.327, icsd=1, PRIMARY]; YbO3 P6_3/mmc (194) mp-1206160 [hull=0.397, icsd=1, PRIMARY]
- papers: Creation of Yb2O3 Nanoprecipitates Through an Oxidation Process in Bulk Yb-Filled Skutterudites | Microstructure and Thermomechanical Properties of Atmospheric Plasma-Sprayed Yb2O3 Coating | High electron mobility with significant spin-orbit coupling in rock-salt YbO epitaxial thin film

## Re-Se-Te
- rank 749 | 9 samples | 1 papers | 9 compositions
- compositions: Re6Se2.4Te12.6 (1); Re6Ga0.5Se2.4Te12.6 (1); Re6Ga0.5Se4.5Te10.5 (1); Re6GaSe4.5Te10.5 (1); Re6Se7.5Te7.5 (1); Re6Ga0.5Se7.5Te7.5 (1)
- dopant candidates (<5% at.): Ga (6)
- solid-solution axis: Se/(Se+Te) spans 0.16-0.50 (median 0.30) over 9 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 11-323 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Re6Te7Se8 Pbca (61) mp-667286 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric properties of Re6GaxSeyTe15−y (0≤x≤2; 0≤y≤7.5)

## Sb-Sn-Te-Zn
- rank 750 | 9 samples | 1 papers | 2 compositions
- compositions: (ZnSb)72.7(SnTe)27.3 (5); (ZnSb)66.6(SnTe)33.4 (4)
- measured range: 378-651 K (5th-95th pct of 9 curves)
- papers: High thermoelectric performance in ZnSb-SnTe pseudo-binary materials
