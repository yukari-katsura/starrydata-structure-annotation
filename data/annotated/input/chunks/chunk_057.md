# Host systems -- chunk 057 of 73

Ranks 2801-2850 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 98.47%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## C-Cl-H-N
- rank 2801 | 1 samples | 1 papers | 1 compositions
- compositions: C6H7NCl (1)
- measured range: 280-320 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeH12C2(NCl2)2 P4_2/ncm (138) mp-1194613 [hull=0.050, icsd=19, PRIMARY]; Sb2H30C9(NCl3)3 Pc (7) mp-709030 [hull=0.065, icsd=4, PRIMARY]; HgH20C6(NCl2)2 P2_1/c (14) mp-1197209 [hull=0.082, icsd=2, PRIMARY]; H24PdC8(NCl2)2 P4_2/mnm (136) mp-707284 [hull=0.095, icsd=2, PRIMARY]; FeH16C4(NCl2)2 P2_1/c (14) mp-709074 [hull=0.060, icsd=2, PRIMARY]
- papers: Investigating thermoelectric properties of doped polyaniline nanowires

## C-Co-Ga
- rank 2802 | 1 samples | 1 papers | 1 compositions
- compositions: GaCCo3 (1)
- measured range: 14-328 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ga2Co6C P4/mmm (123) mp-1224829 [hull=0.039, PRIMARY]
- papers: Good Thermoelectric Performance in Strongly Correlated System SnCCo3with Antiperovskite Structure

## C-Co-Ge
- rank 2803 | 1 samples | 1 papers | 1 compositions
- compositions: GeCCo3 (1)
- measured range: 29-327 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co12Ge4C P4/mmm (123) mp-1226575 [hull=0.068, PRIMARY]
- papers: Good Thermoelectric Performance in Strongly Correlated System SnCCo3with Antiperovskite Structure

## C-Cr-Ge
- rank 2804 | 1 samples | 1 papers | 1 compositions
- compositions: GeCCr3 (1)
- measured range: 12-299 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cr2GeC P6_3/mmc (194) mp-922991 [hull=0.007, icsd=3, PRIMARY]; Cr3GeC Cmcm (63) mp-1079343 [hull=0.031, icsd=2, PRIMARY]
- papers: Synthesis and characterization of Ge–Cr-based intermetallic compounds: GeCr3, GeCCr3, and GeNCr3

## C-Cu-H-O
- rank 2805 | 1 samples | 1 papers | 1 compositions
- compositions: Cu3(CO3)2(OH)2 (1)
- measured range: 12-147 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu3H2(CO4)2 P2_1/c (14) mp-23733 [hull=0.007, icsd=5, PRIMARY]; Cu2H4CO5 P2_1 (4) mp-1192779 [hull=0.170, icsd=1, PRIMARY]; Cu3H10(C4O7)2 P2_1/c (14) mp-1204488 [hull=0.237, icsd=1, PRIMARY]; CuH2(CO2)2 P2_1/c (14) mp-643934 [hull=0.228, icsd=1, PRIMARY]; CuH3C3O4 P2_1/c (14) mp-1194779 [hull=0.193, icsd=1, PRIMARY]
- papers: Thermal Conductivity and Spin State of the Spin Diamond-Chain System Azurite Cu3(CO3)2(OH)2

## C-Cu-O
- rank 2806 | 1 samples | 1 papers | 1 compositions
- compositions: CuOC0.7 (1)
- measured range: 301-684 K (5th-95th pct of 4 curves; full span incl. outliers 301-775 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu2CO5 P2_1/c (14) mp-1198809 [hull=0.113, icsd=9, PRIMARY]; Cu(CO2)2 P2_1/c (14) mp-1104057 [hull=0.547, icsd=2, PRIMARY]; Cu3(CO4)2 P2_1/c (14) mp-1192764 [hull=0.000, icsd=2, PRIMARY]; Cu(CO3)2 P2_1/c (14) mp-1201134 [hull=0.636, icsd=2, PRIMARY]; Cu(CO2)4 P2_1/c (14) mp-1192806 [hull=0.329, icsd=1, PRIMARY]
- papers: Nanocomposites of CuO/SWCNT: Promising thermoelectric materials for mid-temperature thermoelectric generators

## C-Cu-Se-Sn
- rank 2807 | 1 samples | 1 papers | 1 compositions
- compositions: C0.33Cu2SnSe3 (1)
- measured range: 300-700 K (5th-95th pct of 5 curves)
- papers: Enhanced Thermoelectric Performance of Cu2SnSe3-Based Composites Incorporated with Nano-Fullerene

## C-Eu
- rank 2808 | 1 samples | 1 papers | 1 compositions
- compositions: EuC2 (1)
- measured range: 10-299 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): EuC2 I4/mmm (139) mp-1018177 [hull=0.000, icsd=2, PRIMARY]; EuC6 P6_3/mmc (194) mp-1103990 [hull=0.000, icsd=1, PRIMARY]; EuC10 Im-3 (204) mp-1182736 [hull=0.672, PRIMARY]; EuC2 C2/c (15) mp-1077301 [hull=0.026, icsd=1]
- papers: Structural Phase Transitions in EuC<sub>2</sub>

## C-F-H-S
- rank 2809 | 1 samples | 1 papers | 1 compositions
- compositions: C13H7BF4NS6 (1)
- dopant candidates (<5% at.): B (1), N (1)
- measured range: 10-286 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PH18PtC6S3BrF6 P2_1/c (14) mp-1204443 [hull=0.000, icsd=1, PRIMARY]; PH18PtC6S3ClF6 P2_1/c (14) mp-1202301 [hull=0.001, icsd=1, PRIMARY]
- papers: β”-(CNB-EDT-TTF)4BF4; Anion Disorder Effects in Bilayer Molecular Metals

## C-Fe-Si
- rank 2810 | 1 samples | 1 papers | 1 compositions
- compositions: Fe0.95Co0.05Si2C0.58 (1)
- dopant candidates (<5% at.): Co (1)
- measured range: 573-973 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe5SiC Cmc2_1 (36) mp-1212719 [hull=0.022, PRIMARY]
- papers: Optimization of properties of Fe/sub 1-x/Co/sub x/Si/sub 2+z/ for energy conversion and sensors

## C-H-I-P
- rank 2811 | 1 samples | 1 papers | 1 compositions
- compositions: PCDIPT (1)
- measured range: 293-403 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): P2H19C6I7N P-1 (2) mp-1196394 [hull=0.000, icsd=1, PRIMARY]
- papers: Doping High‐Mobility Donor–Acceptor Copolymer Semiconductors with an Organic Salt for High‐Performance Thermoelectric Materials

## C-H-N-Te
- rank 2812 | 1 samples | 1 papers | 1 compositions
- compositions: (C6H7N)37(Te)63 (1)
- measured range: 313-482 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaTe3H15(CN)3 C2/c (15) mp-1197650 [hull=0.059, icsd=1, PRIMARY]; MnTe2H20(CN)4 C2/c (15) mp-1198837 [hull=0.078, icsd=1, PRIMARY]
- papers: Flexible low-grade energy utilization devices based on high-performance thermoelectric polyaniline/tellurium nanorod hybrid films

## C-H-O-S-Se
- rank 2813 | 1 samples | 1 papers | 1 compositions
- compositions: (C4H2Se)(C6H4O2S) (1)
- measured range: 145-305 K (5th-95th pct of 2 curves)
- papers: Thermoelectric Properties of Poly(selenophene-co-3, 4-ethylenedioxythiophene) via Electropolymerization

## C-H-O-Se
- rank 2814 | 1 samples | 1 papers | 1 compositions
- compositions: (C4H2Se)2(C6H4O2S) (1)
- dopant candidates (<5% at.): S (1)
- measured range: 145-305 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): H6C2SeO P-1 (2) mp-1189850 [hull=0.258, icsd=1, PRIMARY]; U2H18C4Se3N2O17 P2_12_12_1 (19) mp-1195410 [hull=0.324, icsd=1, PRIMARY]
- papers: Thermoelectric Properties of Poly(selenophene-co-3, 4-ethylenedioxythiophene) via Electropolymerization

## C-H-Sb-Te
- rank 2815 | 1 samples | 1 papers | 1 compositions
- compositions: (HSC6H4OH)39.14(Sb2Te3)60.86 (1)
- dopant candidates (<5% at.): S (1), O (1)
- measured range: 298-499 K (5th-95th pct of 6 curves)
- papers: An Organic–Inorganic Superlattice with Nanocrystal‐Amorphous Composite Nanolayers for Ultrahigh Thermoelectric Performance

## C-Li-Mg-O-Si
- rank 2816 | 1 samples | 1 papers | 1 compositions
- compositions: Mg2SiLi5C2.5O7.5 (1)
- measured range: 305-862 K (5th-95th pct of 4 curves)
- papers: Fabrication and thermoelectric properties of Mg2Si-based composites using reduction reaction with additives

## C-Mn-Sn
- rank 2817 | 1 samples | 1 papers | 1 compositions
- compositions: SnCMn3 (1)
- measured range: 11-330 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn3SnC Pm-3m (221) mp-991257 [hull=0.055, icsd=4, PRIMARY]
- papers: Good Thermoelectric Performance in Strongly Correlated System SnCCo3with Antiperovskite Structure

## C-Ni-Ti
- rank 2818 | 1 samples | 1 papers | 1 compositions
- compositions: (TiC)89.86(Ni3Al)10.14 (1)
- dopant candidates (<5% at.): Al (1)
- measured range: 292-1311 K (5th-95th pct of 1 curves)
- papers: Densification and Thermal Properties of TiC-Ni3Al Composites Materials.

## C-O-S-Ti
- rank 2819 | 1 samples | 1 papers | 1 compositions
- compositions: TiO2SC (1)
- measured range: 1223-1323 K (5th-95th pct of 1 curves)
- papers: Concentration of electrons at grain boundaries in TiO2 (rutile): Impact on charge transport and reactivity

## C-O-Zr
- rank 2820 | 1 samples | 1 papers | 1 compositions
- compositions: Y0.06ZrO2C0.3 (1)
- dopant candidates (<5% at.): Y (1)
- measured range: 302-672 K (5th-95th pct of 5 curves)
- papers: Mechanically reliable thermoelectric (TE) nanocomposites by dispersing and embedding TE-nanostructures inside a tetragonal ZrO2matrix: the concept and experimental demonstration in graphene oxide–3YSZ system

## C-Pu-U
- rank 2821 | 1 samples | 1 papers | 1 compositions
- compositions: (U)81.14(PuC)18.86 (1)
- measured range: 750-1309 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PuU4C5 R-3m (166) mp-1219737 [hull=0.184, PRIMARY]; PuUC2 R-3m (166) mp-1219685 [hull=0.017, PRIMARY]; PuUC3 I2_13 (199) mp-1219701 [hull=0.000, PRIMARY]
- papers: U-PuO2, U-PuC, U-PuN cermet fuel for fast reactor

## C-S-W
- rank 2822 | 1 samples | 1 papers | 1 compositions
- compositions: WS2C0.2 (1)
- measured range: 290-780 K (5th-95th pct of 5 curves)
- papers: Enhanced Thermoelectric Properties of WS2/Single-Walled Carbon Nanohorn Nanocomposites

## C-Sn
- rank 2823 | 1 samples | 1 papers | 1 compositions
- compositions: CSn3 (1)
- measured range: 11-30 K (5th-95th pct of 2 curves; full span incl. outliers 11-290 K)
- [ref 1] TEDesignLab / ICSD: SnC F-43m (216) mp-1009820 [hull=0.815, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: SnC Fm-3m (225) mp-1009822 [hull=1.293, icsd=1]
- papers: Thermoelectric power of Ce(Pb1−xSnx)3

## C-W
- rank 2824 | 1 samples | 1 papers | 1 compositions
- compositions: C90W10 (1)
- measured range: 307-906 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): WC P-6m2 (187) mp-1894 [hull=0.000, icsd=20, PRIMARY]; W2C Pbcn (60) mp-2034 [hull=0.066, icsd=3, PRIMARY]; W3C I4/mmm (139) mp-979413 [hull=1.341, PRIMARY]; W9C4 R32 (155) mp-684989 [hull=0.074, PRIMARY]; WC Fm-3m (225) mp-13136 [hull=0.451, icsd=4]
- papers: Thermal diffusivity/conductivity of doped graphites

## Ca-Ce-O
- rank 2825 | 1 samples | 1 papers | 1 compositions
- compositions: CaCeO3 (1)
- measured range: 580-1460 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca2CeO4 Pbam (55) mp-755597 [hull=0.021, PRIMARY]; CaCeO3 Pnma (62) mp-756365 [hull=0.059, PRIMARY]; Ca2CeO4 Pbca (61) mp-770977 [hull=0.065]
- papers: Thermophysical properties of BaUO3

## Ca-Ce-Sb
- rank 2826 | 1 samples | 1 papers | 1 compositions
- compositions: Ca3CeSb3 (1)
- measured range: 300-597 K (5th-95th pct of 1 curves)
- papers: Synthesis and Transport Properties of the Family of Zintl Phases Ca<sub>3</sub>RESb<sub>3</sub> (RE = La–Nd, Sm, Gd–Tm, Lu): Exploring the Roles of Crystallographic Disorder and Core 4f Electrons for Enhancing Thermoelectric Performance

## Ca-Co-Fe-O-Sr
- rank 2827 | 1 samples | 1 papers | 1 compositions
- compositions: Sr2.4Ca1.6Fe4.5Co1.5O13 (1)
- measured range: 454-1175 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2Ca2Fe(CoO4)3 Pm (6) mp-1099605 [hull=0.071, PRIMARY]; Sr2Ca2Fe3CoO10 P1 (1) mp-1076147 [hull=0.018, PRIMARY]; Sr2Ca2Fe3CoO12 Pm (6) mp-1075966 [hull=0.048, PRIMARY]; Sr2Ca2FeCo3O10 P1 (1) mp-1099665 [hull=0.024, PRIMARY]; Sr2Ca6Fe3(CoO4)5 P1 (1) mp-1076198 [hull=0.031, PRIMARY]
- papers: Synthesis, Crystal Chemistry, and Electrical Properties of the Intergrowth Oxides Sr4−xCaxFe6−yCoyO13+δ

## Ca-Co-I-O
- rank 2828 | 1 samples | 1 papers | 1 compositions
- compositions: Ca3Co3.9I40.1O9 (1)
- papers: Strengthening of Thermoelectric Performance via Ir Doping in Layered Ca3Co4O9System

## Ca-Co-Mg-O
- rank 2829 | 1 samples | 1 papers | 1 compositions
- compositions: Ca2.2Mg0.8Co4O9 (1)
- measured range: 303-992 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca7Mg(Co2O5)4 P1 (1) mp-1076526 [hull=0.044, PRIMARY]; Ca7Mg(CoO3)8 Pm-3m (221) mp-1076128 [hull=0.209, PRIMARY]; CaMg14CoO16 Pmmm (47) mp-1036443 [hull=0.035, PRIMARY]; CaMg30CoO32 P4/mmm (123) mp-1038117 [hull=0.016, PRIMARY]; CaMg6CoO8 P4/mmm (123) mp-1032957 [hull=0.113, PRIMARY]
- papers: Cation substituted (Ca2CoO3)xCoO2 films and their thermoelectric properties

## Ca-Co-O-Pb-Sr
- rank 2830 | 1 samples | 1 papers | 1 compositions
- compositions: Pb0.7SrCaCo0.3O3(CoO2)1.71 (1)
- measured range: 11-341 K (5th-95th pct of 2 curves)
- papers: Thermopower enhancement in misfit cobaltites

## Ca-Co-O-Rh
- rank 2831 | 1 samples | 1 papers | 1 compositions
- compositions: Ca3CoRhO6 (1)
- measured range: 26-1088 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca3CoRhO6 R-3c (167) mp-1191540 [hull=0.051, PRIMARY]; Ca6Co3RhO12 R-3 (148) mp-1227118 [hull=0.042, PRIMARY]
- papers: Magnetic and thermoelectric properties of quasi-one-dimensional oxides An+2CoBnO3n+3 (A=Ca,Sr, B=Co,Rh,Ir; n=1–3)

## Ca-Co-O-Sb
- rank 2832 | 1 samples | 1 papers | 1 compositions
- compositions: Ca2SbCo4O9 (1)
- measured range: 11-297 K (5th-95th pct of 4 curves)
- papers: Low temperature electrical and thermal transport properties of the Ca3−xSbxCo4O9 system

## Ca-Co-O-Sm
- rank 2833 | 1 samples | 1 papers | 1 compositions
- compositions: Sm0.6Ca0.4CoO3 (1)
- measured range: 522-1225 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaSmCoO4 Cmc2_1 (36) mp-1227147 [hull=0.039, PRIMARY]
- papers: Comparative investigation of dual-phase membranes containing cobalt and iron-based mixed conducting perovskite for oxygen permeation

## Ca-Co-O-Y
- rank 2834 | 1 samples | 1 papers | 1 compositions
- compositions: Ca2YCo4O9 (1)
- measured range: 11-295 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca9Y3(CoO6)4 P1 (1) mp-1227804 [hull=0.055, PRIMARY]
- papers: Enhanced thermoelectric properties induced by chemical pressure in Ca3Co4O9

## Ca-Cr-Gd-O
- rank 2835 | 1 samples | 1 papers | 1 compositions
- compositions: Gd0.70Ca0.30CrO3 (1)
- measured range: 63-312 K (5th-95th pct of 2 curves; full span incl. outliers 63-390 K)
- papers: Magnetic and transport properties of Gd1−xCaxCrO3 (x=0.0–0.3): Effect of orbital degeneracy in thermoelectric power

## Ca-Cr-La-O
- rank 2836 | 1 samples | 1 papers | 1 compositions
- compositions: La0.7Ca0.3Cr0.97O3 (1)
- measured range: 773-1123 K (5th-95th pct of 1 curves)
- papers: Evaluation of simple, easily sintered La0.7Ca0.3Cr0.97 O3−δ perovskite oxide as novel interconnect material for solid oxide fuel cells

## Ca-Cr-Na-O
- rank 2837 | 1 samples | 1 papers | 1 compositions
- compositions: Na0.5Ca0.5Cr2O4 (1)
- measured range: 11-370 K (5th-95th pct of 2 curves)
- papers: Electronic, thermoelectric, and magneto-dielectric properties of Ca1−xNaxCr2O4

## Ca-Cu-O-Pd
- rank 2838 | 1 samples | 1 papers | 1 compositions
- compositions: Ca0.7Na0.3Pd2.5Cu0.5O4 (1)
- dopant candidates (<5% at.): Na (1)
- measured range: 202-301 K (5th-95th pct of 1 curves)
- papers: Logarithmic Temperature Dependence of Resistivity for Ca<sub><b>0.7</b></sub>Na<sub><b>0.3</b></sub>Pd<sub><b>3</b></sub>O<sub><b>4</b></sub>Doped with Cu

## Ca-Cu-Sb-Zn
- rank 2839 | 1 samples | 1 papers | 1 compositions
- compositions: CaZn0.25Cu0.5Sb (1)
- measured range: 301-971 K (5th-95th pct of 4 curves)
- papers: Structure transition and thermoelectric properties related to AZn(1-x)/2CuxSb (A = Ca, Eu, Sr; 0<x<1) Zintl phases

## Ca-Dy-O-Sb
- rank 2840 | 1 samples | 1 papers | 1 compositions
- compositions: Ca2Dy7Sb5O5 (1)
- measured range: 12-369 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca2Dy3Sb3O14 C2/c (15) mp-1227760 [hull=0.010, PRIMARY]
- papers: Investigation of the transport properties and compositions of the Ca2RE7Pn5O5 series (RE=Pr, Sm, Gd, Dy; Pn=Sb, Bi)

## Ca-Fe-La-Ni-O
- rank 2841 | 1 samples | 1 papers | 1 compositions
- compositions: La0.6Ca0.4Fe0.7Ni0.3O3 (1)
- measured range: 773-1073 K (5th-95th pct of 1 curves)
- papers: Synthesis and electrochemical performance of La0.6Ca0.4Fe1−xNixO3 (x=0.1, 0.2, 0.3) material for solid oxide fuel cell cathode

## Ca-Fe-O-Ru
- rank 2842 | 1 samples | 1 papers | 1 compositions
- compositions: Ca2FeRuO6 (1)
- measured range: 110-299 K (5th-95th pct of 1 curves)
- papers: Reentrant magnetism at the borderline between long-range antiferromagnetic order and spin-glass behavior in the \n<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:mi>B</mml:mi></mml:math>\n-site disordered perovskite system \n<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:mrow><mml:mi mathvariant=\"normal\">C</mml:mi><mml:msub><mml:mi mathvariant=\"normal\">a</mml:mi><mml:mrow><mml:mn>2</mml:mn><mml:mo>−</mml:mo><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:mi mathvariant=\"normal\">S</mml:mi><mml:msub><mml:mi mathvariant=\"normal\">r</mml:mi><mml:mi>x</mml:mi></mml:msub><mml:mi>FeRu</mml:mi><mml:msub><mml:mi mathvariant=\"normal\">O</mml:mi><mml:mn>6</mml:mn></mml:msub></mml:mrow></mml:math>

## Ca-Fe-O-Ru-Sr
- rank 2843 | 1 samples | 1 papers | 1 compositions
- compositions: CaSrFeRuO6 (1)
- measured range: 71-298 K (5th-95th pct of 1 curves)
- papers: Reentrant magnetism at the borderline between long-range antiferromagnetic order and spin-glass behavior in the \n<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:mi>B</mml:mi></mml:math>\n-site disordered perovskite system \n<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:mrow><mml:mi mathvariant=\"normal\">C</mml:mi><mml:msub><mml:mi mathvariant=\"normal\">a</mml:mi><mml:mrow><mml:mn>2</mml:mn><mml:mo>−</mml:mo><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:mi mathvariant=\"normal\">S</mml:mi><mml:msub><mml:mi mathvariant=\"normal\">r</mml:mi><mml:mi>x</mml:mi></mml:msub><mml:mi>FeRu</mml:mi><mml:msub><mml:mi mathvariant=\"normal\">O</mml:mi><mml:mn>6</mml:mn></mml:msub></mml:mrow></mml:math>

## Ca-Ga
- rank 2844 | 1 samples | 1 papers | 1 compositions
- compositions: CaGa4 (1)
- measured range: 17-286 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaGa4 I4/mmm (139) mp-1976 [hull=0.000, icsd=4, PRIMARY]; CaGa2 P6_3/mmc (194) mp-11284 [hull=0.000, icsd=4, PRIMARY]; CaGa Cmcm (63) mp-6914 [hull=0.000, icsd=3, PRIMARY]; Ca3Ga8 Immm (71) mp-12611 [hull=0.011, icsd=2, PRIMARY]; Ca11Ga7 Fm-3m (225) mp-30474 [hull=0.000, icsd=1, PRIMARY]
- papers: Characteristic Fermi surfaces and charge density wave in SrAl4 and related compounds with the BaAl4-type tetragonal structure

## Ca-Gd-O-Sb
- rank 2845 | 1 samples | 1 papers | 1 compositions
- compositions: Ca2Gd7Sb5O5 (1)
- measured range: 11-374 K (5th-95th pct of 3 curves)
- papers: Investigation of the transport properties and compositions of the Ca2RE7Pn5O5 series (RE=Pr, Sm, Gd, Dy; Pn=Sb, Bi)

## Ca-Gd-Sb
- rank 2846 | 1 samples | 1 papers | 1 compositions
- compositions: Ca3GdSb3 (1)
- measured range: 300-597 K (5th-95th pct of 1 curves)
- papers: Synthesis and Transport Properties of the Family of Zintl Phases Ca<sub>3</sub>RESb<sub>3</sub> (RE = La–Nd, Sm, Gd–Tm, Lu): Exploring the Roles of Crystallographic Disorder and Core 4f Electrons for Enhancing Thermoelectric Performance

## Ca-Ge-O
- rank 2847 | 1 samples | 1 papers | 1 compositions
- compositions: Ca3GeO (1)
- measured range: 10-392 K (5th-95th pct of 3 curves)
- [ref 1] TEDesignLab / ICSD: CaGeO3 Pnma (62) mp-8130 [hull=0.108, icsd=19, PRIMARY]; CaGe2O5 C2/c (15) mp-3707 [hull=0.006, icsd=9, PRIMARY]; Ca2GeO4 I4/mmm (139) mp-13650 [hull=0.146, icsd=1, PRIMARY]; Ca2GeO4 P-3m1 (164) mp-1019561 [hull=0.189, icsd=1]; CaGe2O5 (1)
- [ref 2] MP, ranked by ICSD evidence: Ca3GeO Pm-3m (221) mp-9721 [hull=0.001, icsd=2, PRIMARY]; Ca2Ge7O16 P-4b2 (117) mp-29273 [hull=0.000, icsd=2, PRIMARY]; Ca5(GeO5)2 P2_1/c (14) mp-1197278 [hull=0.075, icsd=1, PRIMARY]; CaGe2O5 Pbam (55) mp-4279 [hull=0.005, icsd=2]; CaGeO3 P-1 (2) mp-17761 [hull=0.000, icsd=1]
- papers: Thermoelectric properties of inverse perovskites A3TtO (A = Mg, Ca; Tt = Si, Ge): Computational and experimental investigations

## Ca-Hf-O-Sc
- rank 2848 | 1 samples | 1 papers | 1 compositions
- compositions: CaHf0.7Sc0.3O3 (1)
- measured range: 674-1174 K (5th-95th pct of 1 curves)
- papers: Influence of Sc concentration on transport properties of CaHf1-xScxO3-α

## Ca-K-Mn-O
- rank 2849 | 1 samples | 1 papers | 1 compositions
- compositions: Ca0.9Gd0.1MnO3(K2CO3)0.2 (1)
- dopant candidates (<5% at.): C (1), Gd (1)
- measured range: 328-1069 K (5th-95th pct of 1 curves)
- papers: Improvement of thermoelectric properties of Ca0.9Gd0.1MnO3 by powder engineering through K2CO3 additions

## Ca-La-Sb
- rank 2850 | 1 samples | 1 papers | 1 compositions
- compositions: Ca3LaSb3 (1)
- measured range: 300-589 K (5th-95th pct of 1 curves)
- papers: Synthesis and Transport Properties of the Family of Zintl Phases Ca<sub>3</sub>RESb<sub>3</sub> (RE = La–Nd, Sm, Gd–Tm, Lu): Exploring the Roles of Crystallographic Disorder and Core 4f Electrons for Enhancing Thermoelectric Performance
