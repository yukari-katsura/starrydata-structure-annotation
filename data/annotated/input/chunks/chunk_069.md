# Host systems -- chunk 069 of 73

Ranks 3401-3450 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 99.62%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Ir-O-Pb
- rank 3401 | 1 samples | 1 papers | 1 compositions
- compositions: Pb2Ir2O7 (1)
- measured range: 25-288 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ir2Pb2O7 Fd-3m (227) mp-1190246 [hull=0.000, icsd=2, PRIMARY]
- papers: Mixed-valent metallic pyrochlore iridate: A possible route to non-Fermi liquids

## Ir-O-Sm
- rank 3402 | 1 samples | 1 papers | 1 compositions
- compositions: Sm2Ir2O7 (1)
- measured range: 11-317 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sm3IrO7 Cmcm (63) mp-15326 [hull=0.000, icsd=1, PRIMARY]
- papers: Metal–Insulator Transition in Pyrochlore IridatesLn2Ir2O7(Ln= Nd, Sm, and Eu)

## Ir-O-Tl
- rank 3403 | 1 samples | 1 papers | 1 compositions
- compositions: Tl2Ir2O7 (1)
- measured range: 16-299 K (5th-95th pct of 1 curves)
- papers: Tl<sub>2</sub>Ir<sub>2</sub>O<sub>7</sub>: A Pauli Paramagnetic Metal, Proximal to a Metal Insulator Transition

## Ir-Rh-Sb
- rank 3404 | 1 samples | 1 papers | 1 compositions
- compositions: Ir0.5Rh0.5Sb3 (1)
- measured range: 301-815 K (5th-95th pct of 3 curves)
- papers: Some properties of semiconducting IrSb3

## Ir-Sc
- rank 3405 | 1 samples | 1 papers | 1 compositions
- compositions: Sc57Ir13_1_1 (1)
- measured range: 15-299 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ScIr2 Fd-3m (227) mp-2263 [hull=0.005, icsd=4, PRIMARY]; ScIr Pm-3m (221) mp-1129 [hull=0.000, icsd=3, PRIMARY]; Sc11Ir4 Fm-3m (225) mp-12304 [hull=0.000, icsd=2, PRIMARY]; Sc44Ir7 F-43m (216) mp-1200708 [hull=0.000, icsd=2, PRIMARY]; Sc57Ir13 Pm-3 (200) mp-1201561 [hull=0.006, icsd=2, PRIMARY]
- papers: Electrical resistivity of crystal approximants in Sc-based alloys

## Ir-Ta
- rank 3406 | 1 samples | 1 papers | 1 compositions
- compositions: Ir3Ta (1)
- measured range: 298-1091 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TaIr3 Pm-3m (221) mp-265 [hull=0.000, icsd=2, PRIMARY]; Ta3Ir Fm-3m (225) mp-1187196 [hull=0.000, PRIMARY]; TaIr3 P6_3/mmc (194) mp-1187241 [hull=0.018]
- papers: Thermophysical Properties of L1<SUB><B>2</B></SUB> Intermetallic Compounds of Iridium

## Ir-Ti
- rank 3407 | 1 samples | 1 papers | 1 compositions
- compositions: Ir3Ti (1)
- measured range: 299-1095 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti3Ir Pm-3n (223) mp-544 [hull=0.000, icsd=9, PRIMARY]; TiIr P4/mmm (123) mp-1235 [hull=0.000, icsd=6, PRIMARY]; TiIr3 Pm-3m (221) mp-1089 [hull=0.000, icsd=5, PRIMARY]; Ti3Ir2 P4/mmm (123) mp-1217113 [hull=0.056, PRIMARY]; TiIr Pm-3m (221) mp-12594 [hull=0.074, icsd=3]
- papers: Thermophysical Properties of L1<SUB><B>2</B></SUB> Intermetallic Compounds of Iridium

## Ir-U
- rank 3408 | 1 samples | 1 papers | 1 compositions
- compositions: UIr3 (1)
- measured range: 15-302 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UIr P2_1/c (14) mp-2236 [hull=0.000, icsd=4, PRIMARY, AMBIGUOUS]; UIr3 Pm-3m (221) mp-1044 [hull=0.000, icsd=3, PRIMARY]; UIr2 Fd-3m (227) mp-1655 [hull=0.027, icsd=2, PRIMARY]; UIr P2_1 (4) mp-1105762 [hull=0.002, icsd=4]; UIr P-1 (2) mp-644899 [hull=0.437, icsd=1]
- papers: Some Characteristics of the Thermoelectric Power in Uranium Intermetallic Compounds

## Ir-V
- rank 3409 | 1 samples | 1 papers | 1 compositions
- compositions: Ir3V (1)
- measured range: 301-1085 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): VIr P4/mmm (123) mp-1281 [hull=0.024, icsd=4, PRIMARY]; V3Ir Pm-3n (223) mp-2006 [hull=0.000, icsd=3, PRIMARY]; VIr3 Pm-3m (221) mp-1082 [hull=0.020, icsd=2, PRIMARY]; V4Ir Fmmm (69) mp-1216454 [hull=0.250, PRIMARY]; VIr Cmmm (65) mp-1079582 [hull=0.014, icsd=3]
- papers: Thermophysical Properties of L1<SUB><B>2</B></SUB> Intermetallic Compounds of Iridium

## Ir-Zr
- rank 3410 | 1 samples | 1 papers | 1 compositions
- compositions: Ir3Zr (1)
- measured range: 302-1091 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZrIr2 Fd-3m (227) mp-715 [hull=0.082, icsd=4, PRIMARY]; ZrIr3 Pm-3m (221) mp-1438 [hull=0.000, icsd=3, PRIMARY]; Zr2Ir I4/mcm (140) mp-1077297 [hull=0.002, icsd=1, PRIMARY]; ZrIr P4/mmm (123) mp-1017541 [hull=0.077, icsd=1, PRIMARY]; Zr3Ir I-42m (121) mp-30748 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermophysical Properties of L1<SUB><B>2</B></SUB> Intermetallic Compounds of Iridium

## K-Mo-Se
- rank 3411 | 1 samples | 1 papers | 1 compositions
- compositions: K2Mo15Se19 (1)
- measured range: 297-791 K (5th-95th pct of 4 curves)
- [ref 1] TEDesignLab / ICSD: K(MoSe)3 P6_3/m (176) mp-1104242 [hull=0.000, icsd=3, PRIMARY]; K2(MoSe6)3 (4) [PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: K2Mo15Se19 R-3c (167) mp-1204618 [hull=0.037, icsd=1, PRIMARY]; K3Mo3Se14 Cmc2_1 (36) mp-651347 [hull=0.023, icsd=1, PRIMARY]; K2InMo15Se19 P2_1/m (11) mp-1226012 [hull=0.031, PRIMARY]; K4Mo6Se25O Cm (8) mp-1224595 [hull=0.310, PRIMARY]
- papers: Unravelling the Beneficial Influence of Ag insertion on the Thermoelectric Properties of the Cluster Compound K2Mo15Se19

## K-O-Ta-W
- rank 3412 | 1 samples | 1 papers | 1 compositions
- compositions: KTaWO6 (1)
- measured range: 372-980 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): KTaW2O9 P1 (1) mp-1223468 [hull=0.004, PRIMARY]; KTaWO6 Ima2 (46) mp-1223039 [hull=0.000, PRIMARY]; KTaWO7 Imma (74) mp-1223034 [hull=0.202, PRIMARY]
- papers: Extremely Low Thermal Conductivity in Oxides with Cage-Like Crystal Structure

## K-Sn-Zn
- rank 3413 | 1 samples | 1 papers | 1 compositions
- compositions: K8Zn4Sn42 (1)
- measured range: 10-358 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): K4Zn2Sn21 Ama2 (40) mp-1224111 [hull=0.005, PRIMARY]
- papers: Synthesis of Large Single Crystals and Thermoelectrical Properties of the Type-I Clathrate K8Zn4Sn42

## La-Li-O-Zr
- rank 3414 | 1 samples | 1 papers | 1 compositions
- compositions: Li6.4La3Zr1.4Ta0.6O12 (1)
- dopant candidates (<5% at.): Ta (1)
- measured range: 148-497 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li7La3Zr2O12 I4_1/acd (142) mp-942733 [hull=0.007, icsd=7, PRIMARY]; Li17La12Zr8O48 I-4 (82) mp-1120817 [hull=0.125, PRIMARY]
- papers: Good Solid‐State Electrolytes Have Low, Glass‐Like Thermal Conductivity

## La-Mn-Nd-O-Pb
- rank 3415 | 1 samples | 1 papers | 1 compositions
- compositions: La0.4Nd0.3Pb0.3MnO3 (1)
- measured range: 24-345 K (5th-95th pct of 1 curves)
- papers: Variation of magnetic and transport properties in magnetoresistive oxides La-ln-Pb-Mn-O (Ln=Pr, Nd, Dy, and Y)

## La-Mn-O-Pb-Pr
- rank 3416 | 1 samples | 1 papers | 1 compositions
- compositions: La0.4Pr0.3Pb0.3MnO3 (1)
- measured range: 16-346 K (5th-95th pct of 1 curves)
- papers: Variation of magnetic and transport properties in magnetoresistive oxides La-ln-Pb-Mn-O (Ln=Pr, Nd, Dy, and Y)

## La-Mn-O-Pb-Zr
- rank 3417 | 1 samples | 1 papers | 1 compositions
- compositions: (PbZr0.52Ti0.48O3)2000(La0.65Ca0.35MnO3)2000 (1)
- dopant candidates (<5% at.): Ti (1), Ca (1)
- measured range: 20-300 K (5th-95th pct of 1 curves)
- papers: Effect of PbZr0.52Ti0.48O3 thin layer on structure, electronic and magnetic properties of La0.65Sr0.35 MnO3 and La0.65Ca0.30MnO3 thin-films

## La-Mn-O-Pr-Sr
- rank 3418 | 1 samples | 1 papers | 1 compositions
- compositions: La0.3Pr0.3Sr0.4MnO3 (1)
- measured range: 72-396 K (5th-95th pct of 1 curves)
- papers: The effect of a cation radii on structural, magnetic and electrical properties of doped manganites La0.6−xPrxSr0.4MnO3

## La-Mn-O-Si-Sr
- rank 3419 | 1 samples | 1 papers | 1 compositions
- compositions: La0.6Gd0.1Sr0.3Mn0.75Si0.25O3 (1)
- dopant candidates (<5% at.): Gd (1)
- measured range: 85-290 K (5th-95th pct of 1 curves)
- papers: Electrical conductivity and dielectric behaviour of nanocrystalline La<sub>0.6</sub>Gd<sub>0.1</sub>Sr<sub>0.3</sub>Mn<sub>0.75</sub>Si<sub>0.25</sub>O<sub>3</sub>

## La-Mn-O-Sn
- rank 3420 | 1 samples | 1 papers | 1 compositions
- compositions: La0.7Sn0.3MnO3 (1)
- measured range: 94-434 K (5th-95th pct of 1 curves)
- papers: Structural and magnetic heterogeneities, phase transitions, and magnetoresistance and magnetoresonance properties of the composition ceramic La0.7Pb0.3 − x Sn x MnO3

## La-Mn-O-Sr-Zn
- rank 3421 | 1 samples | 1 papers | 1 compositions
- compositions: La0.6Sr0.4Mn0.7Zn0.3O3 (1)
- measured range: 50-474 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2La2MnZnO8 Amm2 (38) mp-1218782 [hull=0.034, PRIMARY, AMBIGUOUS]; Sr2La2MnZnO8 C2/m (12) mp-1173272 [hull=0.036]; Sr2La2MnZnO8 P4/mmm (123) mp-1218735 [hull=0.082]
- papers: Effects of Zn substitution on the magnetic and transport properties of La0.6Sr0.4Mn1−yZnyO3−δ (0≤y≤0.3)

## La-Mo-Ni-O
- rank 3422 | 1 samples | 1 papers | 1 compositions
- compositions: LaNi0.75Mo0.25O3 (1)
- measured range: 393-1073 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2NiMoO6 Fm-3m (225) mp-1206064 [hull=0.284, PRIMARY]; La4Ni3MoO12 P4/mmm (123) mp-1223026 [hull=0.147, PRIMARY]
- papers: Defective Ni Perovskites as Cathode Materials in Intermediate-Temperature Solid-Oxide Fuel Cells: A Structure−Properties Correlation

## La-Nb-Ni-O
- rank 3423 | 1 samples | 1 papers | 1 compositions
- compositions: La3Ni2NbO9 (1)
- measured range: 376-1124 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2NbNiO6 P2_1/c (14) mp-1211522 [hull=0.202, PRIMARY]
- papers: Synthesis and electrical property study of La3Ni2MO9 (M=Nb and TA)

## La-Ni-O-Os
- rank 3424 | 1 samples | 1 papers | 1 compositions
- compositions: La2Ni1.19Os0.81O6 (1)
- measured range: 104-298 K (5th-95th pct of 1 curves)
- papers: Canted ferrimagnetism and giant coercivity in the nonstoichiometric double perovskite \nLa2Ni1.19Os0.81O6

## La-Ni-O-Os-Sr
- rank 3425 | 1 samples | 1 papers | 1 compositions
- compositions: SrLaNiOsO6 (1)
- measured range: 176-300 K (5th-95th pct of 1 curves)
- papers: Synthesis, crystal structures, and magnetic properties of double perovskites SrLaNiOsO6 and BaLaNiOsO6

## La-Ni-O-Ta
- rank 3426 | 1 samples | 1 papers | 1 compositions
- compositions: La3Ni2TaO9 (1)
- measured range: 301-1126 K (5th-95th pct of 1 curves)
- papers: Synthesis and electrical property study of La3Ni2MO9 (M=Nb and TA)

## La-O-P
- rank 3427 | 1 samples | 1 papers | 1 compositions
- compositions: LaPO4 (1)
- measured range: 301-1268 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaPO4 P2_1/c (14) mp-3962 [hull=0.000, icsd=5, PRIMARY]; La(PO3)3 C222_1 (20) mp-9646 [hull=0.000, icsd=1, PRIMARY]; LaP5O14 Pmna (53) mp-1204624 [hull=0.000, icsd=1, PRIMARY]; La2P4O13 C222_1 (20) mp-771240 [hull=0.003, PRIMARY, AMBIGUOUS]; La3PO7 Cm (8) mp-779590 [hull=0.000, PRIMARY]
- papers: Thermophysical properties of rare earth barium aluminates

## La-O-Pb-Sr
- rank 3428 | 1 samples | 1 papers | 1 compositions
- compositions: Sr0.75La0.25PbO3 (1)
- measured range: 11-277 K (5th-95th pct of 3 curves)
- papers: Oxalate coprecipitation synthesis and transport properties of polycrystalline Sr1−xLaxPbO3−δ solid solutions

## La-O-Sb
- rank 3429 | 1 samples | 1 papers | 1 compositions
- compositions: La2SbO2 (1)
- measured range: 92-392 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La3SbO7 Cmcm (63) mp-1190600 [hull=0.000, icsd=2, PRIMARY]; La(SbO3)3 Cmcm (63) mp-31418 [hull=0.000, icsd=1, PRIMARY]; La14Sb8CO7 P4bm (100) mp-1200169 [hull=0.041, icsd=1, PRIMARY]; La3SbO3 C2/m (12) mp-1104307 [hull=0.000, icsd=1, PRIMARY]; LaSbO4 P2_1/c (14) mp-1190427 [hull=0.000, icsd=1, PRIMARY]
- papers: Decoupling the Electrical Conductivity and Seebeck Coefficient in theRE2SbO2Compounds through Local Structural Perturbations

## La-O-Sb-Zn
- rank 3430 | 1 samples | 1 papers | 1 compositions
- compositions: LaOZnSb (1)
- measured range: 311-664 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaZnSbO P4/nmm (129) mp-12515 [hull=0.000, icsd=3, PRIMARY]
- papers: Chemical bonding and properties of “layered” quaternary antimonide oxide REOZnSb (RE = La, Ce, Pr, Nd)

## La-O-Ti-Y
- rank 3431 | 1 samples | 1 papers | 1 compositions
- compositions: Y0.3La0.7TiO3 (1)
- measured range: 88-304 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La3YTi4O14 R-3m (166) mp-1223094 [hull=0.041, PRIMARY]; LaY3Ti4O12 Pm (6) mp-1222863 [hull=0.060, PRIMARY]; LaY3Ti4O14 R-3m (166) mp-1222804 [hull=0.021, PRIMARY]; LaYTi2O6 Pmc2_1 (26) mp-1222876 [hull=0.055, PRIMARY]
- papers: Evidence for two electronic phases inY1−xLaxTiO3from thermoelectric and magnetic susceptibility measurements

## La-O-Y-Zr
- rank 3432 | 1 samples | 1 papers | 1 compositions
- compositions: (La0.76Y0.24)2(Zr0.94Y0.06)2O6.94 (1)
- measured range: 455-1242 K (5th-95th pct of 1 curves)
- papers: Glass-like thermal conductivities in (x=x1+x2, 0⩽x⩽1.0) solid solutions

## La-Os-P
- rank 3433 | 1 samples | 1 papers | 1 compositions
- compositions: LaOs4P12 (1)
- measured range: 13-301 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(P3Os)4 Im-3 (204) mp-1021506 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermal Properties of Filled Skutterudite PrOs4P12

## La-Rh
- rank 3434 | 1 samples | 1 papers | 1 compositions
- compositions: La7Rh3 (1)
- measured range: 12-294 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaRh2 Fd-3m (227) mp-1702 [hull=0.000, icsd=6, PRIMARY]; La4Rh3 I-43d (220) mp-626 [hull=0.000, icsd=2, PRIMARY]; La5Rh4 Pnma (62) mp-1197877 [hull=0.014, icsd=2, PRIMARY]; LaRh Cmcm (63) mp-1002107 [hull=0.000, icsd=2, PRIMARY]; LaRh3 P6_3/mmc (194) mp-974030 [hull=0.000, icsd=1, PRIMARY]
- papers: Magnetic and electrical properties of the intermetallic compounds R7Rh3 (R=La, Ce, Pr and Nd)

## La-Rh-Si
- rank 3435 | 1 samples | 1 papers | 1 compositions
- compositions: LaRh2Si2 (1)
- measured range: 17-300 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(SiRh)2 I4/mmm (139) mp-5936 [hull=0.000, icsd=7, PRIMARY]; LaSi2Rh3 P6/mmm (191) mp-29726 [hull=0.000, icsd=1, PRIMARY, AMBIGUOUS]; La2Si3Rh P6_3/mmc (194) mp-1191810 [hull=0.000, icsd=1, PRIMARY]; La2Si5Rh3 Ibam (72) mp-8620 [hull=0.000, icsd=1, PRIMARY]; La3Si2Rh3 Pnma (62) mp-601852 [hull=0.000, icsd=1, PRIMARY]
- papers: Electrical resistivity and thermopower studies of Ce(Rh1−xRux)2Si2 compounds with 0 ⩽ x ⩽ 0.4

## La-Ru
- rank 3436 | 1 samples | 1 papers | 1 compositions
- compositions: LaRu2 (1)
- measured range: 11-280 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaRu2 Fd-3m (227) mp-2019 [hull=0.000, icsd=13, PRIMARY]; La3Ru Pnma (62) mp-1189592 [hull=0.000, icsd=3, PRIMARY]; La5Ru2 C2/c (15) mp-1104417 [hull=0.000, icsd=2, PRIMARY]; La7Ru3 Pnma (62) mp-1202486 [hull=0.000, icsd=1, PRIMARY]; La4Ru Fd-3m (227) mp-1211363 [hull=0.348, PRIMARY]
- papers: Transport properties of (Ce1−xRx)Ru2 (R  La, Nd)

## La-S-Sm
- rank 3437 | 1 samples | 1 papers | 1 compositions
- compositions: La2.3Sm0.7S4 (1)
- measured range: 973-1277 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2SmS4 I-42d (122) mp-37386 [hull=0.036, PRIMARY]; La5SmS8 I-4 (82) mp-36088 [hull=0.032, PRIMARY]; LaSmS2 R-3m (166) mp-1222697 [hull=0.000, PRIMARY]; LaSmS2 F-43m (216) mp-1222688 [hull=1.514]
- papers: Thermal conductivity of La3−xRxS4where R=Sm, Eu, and Yb

## La-S-Ti
- rank 3438 | 1 samples | 1 papers | 1 compositions
- compositions: La2Ti0.6S2.67 (1)
- measured range: 291-952 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaTiS3 Pnma (62) mp-1211414 [hull=0.027, PRIMARY]
- papers: Thermoelectric properties of lanthanum sesquisulfide with Ti additive

## La-S-Yb
- rank 3439 | 1 samples | 1 papers | 1 compositions
- compositions: La2.3Yb0.7S4 (1)
- measured range: 677-1275 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaYbS3 Cmcm (63) mp-8215 [hull=0.230, icsd=2, PRIMARY]; La(YbS2)3 P2_1/m (11) mp-1190422 [hull=0.241, icsd=1, PRIMARY]; La2YbS4 I-42d (122) mp-675767 [hull=0.006, PRIMARY]; La5YbS8 I-4 (82) mp-676443 [hull=0.017, PRIMARY]; LaYbS3 Pna2_1 (33) mp-1188442 [hull=0.277, icsd=2]
- papers: Thermal conductivity of La3−xRxS4where R=Sm, Eu, and Yb

## La-Sb-Yb
- rank 3440 | 1 samples | 1 papers | 1 compositions
- compositions: Yb3.5La0.5Sb3 (1)
- measured range: 292-1268 K (5th-95th pct of 4 curves)
- papers: High-temperature transport properties of complex antimonides with anti-Th3P4structure

## La-Zn
- rank 3441 | 1 samples | 1 papers | 1 compositions
- compositions: LaZn11 (1)
- measured range: 15-298 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaZn Pm-3m (221) mp-2615 [hull=0.000, icsd=4, PRIMARY]; LaZn5 P6/mmm (191) mp-2424 [hull=0.000, icsd=4, PRIMARY]; LaZn13 Fm-3c (226) mp-1193170 [hull=0.000, icsd=2, PRIMARY]; La2Zn17 R-3m (166) mp-30709 [hull=0.000, icsd=2, PRIMARY]; LaZn4 Cmcm (63) mp-861620 [hull=0.000, icsd=1, PRIMARY]
- papers: Anisotropic transport and magnetic properties and magnetic-field tuned states of CeZn<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:msub><mml:mrow/><mml:mn>11</mml:mn></mml:msub></mml:math>single crystals

## Li-Mg-O-V
- rank 3442 | 1 samples | 1 papers | 1 compositions
- compositions: Li0.5Mg0.5V2O4 (1)
- measured range: 40-291 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li3MgV8O16 Cm (8) mp-771733 [hull=0.035, PRIMARY]
- papers: Preparation and physical properties of the spinel Ti and V oxides

## Li-N
- rank 3443 | 1 samples | 1 papers | 1 compositions
- compositions: Li3N (1)
- measured range: 12-144 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li3N P6/mmm (191) mp-2251 [hull=0.000, icsd=20, PRIMARY]; LiN3 C2/m (12) mp-2659 [hull=0.000, icsd=6, PRIMARY]; Li2N Fm-3m (225) mp-1062345 [hull=0.241, icsd=1, PRIMARY]; LiN F-43m (216) mp-1059612 [hull=1.410, icsd=1, PRIMARY]; Li3N2 P-4m2 (115) mp-1222421 [hull=0.755, PRIMARY]
- papers: Low-temperature thermal conductivity of Li3N

## Li-N-Nb-O
- rank 3444 | 1 samples | 1 papers | 1 compositions
- compositions: Li0.88Nb3.0(O0.13N0.87)4 (1)
- measured range: 19-298 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li16Nb2N8O R-3 (148) mp-6031 [hull=0.000, icsd=2, PRIMARY]
- papers: Crystal Structure and Superconducting Properties of Hexagonal Lithium–Niobium Oxynitride

## Li-O-W
- rank 3445 | 1 samples | 1 papers | 1 compositions
- compositions: Li2WO4 (1)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li2WO4 R-3 (148) mp-18902 [hull=0.015, icsd=3, PRIMARY]; Li2W2O7 P-1 (2) mp-706504 [hull=0.050, icsd=1, PRIMARY]; Li14W7O32 P-43m (215) mp-1198827 [hull=0.530, icsd=1, PRIMARY]; Li(WO3)2 Immm (71) mp-774144 [hull=0.042, PRIMARY]; Li11Fe(WO4)7 Cm (8) mp-769470 [hull=0.081, PRIMARY]
- papers: Environmental Friendly Approach for the Development of Ultra-Low-Firing Li2WO4 Ceramic Tapes

## Li-Se-Zr
- rank 3446 | 1 samples | 1 papers | 1 compositions
- compositions: LiZrSe2 (1)
- measured range: 20-298 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiZrSe2 P-3m1 (164) mp-1001615 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric Properties of Li-Intercalated ZrSe2 Single Crystals

## Lu-Ni
- rank 3447 | 1 samples | 1 papers | 1 compositions
- compositions: LuNi2 (1)
- measured range: 53-414 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LuNi2 Fd-3m (227) mp-2130 [hull=0.000, icsd=6, PRIMARY]; Lu2Ni17 P6_3/mmc (194) mp-1202260 [hull=0.007, icsd=1, PRIMARY]; LuNi5 P6/mmm (191) mp-11491 [hull=0.000, icsd=1, PRIMARY]; LuNi Pnma (62) mp-1078899 [hull=0.000, icsd=1, PRIMARY]; Lu4Ni Fd-3m (227) mp-1210828 [hull=0.444, PRIMARY]
- papers: Transport phenomena in spin fluctuations systems

## Lu-Ni-Sb-Sn
- rank 3448 | 1 samples | 1 papers | 1 compositions
- compositions: (LuNiSb)0.5(LuNiSn)0.5 (1)
- measured range: 340-993 K (5th-95th pct of 3 curves)
- papers: Effect of secondary LuNiSn phase on thermoelectric properties of half-Heusler alloy LuNiSb

## Lu-Ni-Sn
- rank 3449 | 1 samples | 1 papers | 1 compositions
- compositions: LuNiSn (1)
- measured range: 326-991 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LuNiSn Pnma (62) mp-977588 [hull=0.000, icsd=3, PRIMARY]; Lu6Ni2Sn Immm (71) mp-30771 [hull=0.000, icsd=2, PRIMARY]; Lu2NiSn6 Cmmm (65) mp-31136 [hull=0.000, icsd=2, PRIMARY]; LuNiSn2 Pnma (62) mp-7736 [hull=0.000, icsd=2, PRIMARY]; LuNi2Sn Fm-3m (225) mp-11492 [hull=0.014, icsd=1, PRIMARY]
- papers: Effect of secondary LuNiSn phase on thermoelectric properties of half-Heusler alloy LuNiSb

## Lu-O-Si
- rank 3450 | 1 samples | 1 papers | 1 compositions
- compositions: Lu2SiO5 (1)
- measured range: 297-1271 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Lu2Si2O7 C2/m (12) mp-7193 [hull=0.000, icsd=1, PRIMARY]; Lu2SiO5 C2/c (15) mp-16969 [hull=0.000, icsd=1, PRIMARY]; LuSiO3 Pm-3m (221) mp-973655 [hull=0.877, PRIMARY]; Lu2Si2O7 P4_12_12 (92) mp-18385 [hull=0.020, icsd=1]; Lu2Si2O7 P4_32_12 (96) mp-1202190 [hull=0.020, icsd=1]
- papers: Theoretical prediction and experimental determination of the low lattice thermal conductivity of Lu2SiO5
