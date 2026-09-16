# Host systems -- chunk 027 of 73

Ranks 1301-1350 by sample count. These 50 host systems cover 200 samples (0.38% of the TE set); cumulative through this chunk: 92.42%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## B-Bi-Sb-Te
- rank 1301 | 4 samples | 1 papers | 4 compositions
- compositions: (Bi0.48Sb1.52Te3)72.83B27.17 (1); (Bi0.48Sb1.517In0.003Te3 )72.83B27.17 (1); (Bi0.48Sb1.515In0.005Te3 )72.83B27.17 (1); (Bi0.48Sb1.513In0.007Te3 )72.83B27.17 (1)
- dopant candidates (<5% at.): In (3)
- measured range: 303-497 K (5th-95th pct of 20 curves)
- papers: Synergistic effects of B-In codoping in zone-melted Bi0.48Sb1.52Te3-based thermoelectric

## B-C-Ni-Y
- rank 1302 | 4 samples | 1 papers | 1 compositions
- compositions: YNi2B2C (4)
- measured range: 10-99 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YNi2B2C I4/mmm (139) mp-6576 [hull=0.000, icsd=5, PRIMARY]; YNiBC P4/nmm (129) mp-612670 [hull=0.000, icsd=1, PRIMARY]; TbY3Ni8(B2C)4 P4/mmm (123) mp-1217451 [hull=0.000, PRIMARY]
- papers: Thermal conductivity ofRNi2B2C (R=Y,Ho) single crystals

## B-S
- rank 1303 | 4 samples | 1 papers | 4 compositions
- compositions: B6S0.599 (1); B6S0.609 (1); B6S0.62 (1); B6S0.628 (1)
- measured range: 325-812 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): B2S3 I4_1/a (88) mp-1199451 [hull=0.000, icsd=1, PRIMARY]; BS2 P2_1/c (14) mp-1200183 [hull=0.421, icsd=1, PRIMARY]; B12S R3m (160) mp-1228640 [hull=0.076, PRIMARY]; B2S3 R-3c (167) mp-866066 [hull=0.098]
- papers: An α-rhombohedral boron-related compound with sulfur: Synthesis, structure and thermoelectric properties

## Ba-Bi-Ca-O
- rank 1304 | 4 samples | 1 papers | 4 compositions
- compositions: Ag0.09Bi1.6Pb0.4Ba2Ca2O10 (1); Ag0.15Bi1.6Pb0.4Ba2Ca2O10 (1); Bi1.6Pb0.4Ba2Ca2O10 (1); Ag0.03Bi1.6Pb0.4Ba2Ca2O10 (1)
- dopant candidates (<5% at.): Pb (4), Ag (3)
- measured range: 289-934 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2CaBiO6 Fm-3m (225) mp-1214698 [hull=0.025, PRIMARY]; Ba3CaBi2O9 Immm (71) mp-1228277 [hull=0.000, PRIMARY]; Ba4Ca(BiO4)3 Im-3m (229) mp-1147549 [hull=0.009, PRIMARY]
- papers: Improved thermoelectric performances in textured Bi1.6Pb0.4Ba2Co2Oy/Ag composites

## Ba-Ca-Cu-O-Sr-Tl
- rank 1305 | 4 samples | 1 papers | 2 compositions
- compositions: TlBaSrCaCu2O7 (2); TlBaSrCa2Cu3O9 (2)
- measured range: 29-290 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaSrCa2Tl(CuO3)3 Pm (6) mp-1227794 [hull=0.018, PRIMARY]
- papers: Systematic thermopower measurements of the thallium cuprates Tl(Ba,Sr)2Cam−1CumO2m+3−δ and Tl2Ba2Cam−1CumO2m+4+δ

## Ba-Ce-Co-Fe-Nd-O
- rank 1306 | 4 samples | 1 papers | 4 compositions
- compositions: (NdBaCoFeO5)5.9(Ce0.8Sm0.2O1.9)4.1 (1); (NdBaCoFeO5)2.3(Ce0.8Sm0.2O1.9)2.7 (1); (NdBaCoFeO5)7(Ce0.8Sm0.2O1.9)13 (1); (NdBaCoFeO5)2.7(Ce0.8Sm0.2O1.9)7.3 (1)
- dopant candidates (<5% at.): Sm (4)
- solid-solution axis: Ce/(Ce+Nd) spans 0.36-0.68 (median 0.60) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 522-1123 K (5th-95th pct of 4 curves)
- papers: Improved electrochemical performance and thermal expansion compatibility of LnBaCoFeO5+–Sm0.2Ce0.8O1.9 (Ln Pr and Nd) composite cathodes for IT-SOFCs

## Ba-Ce-Co-Fe-O-Pr
- rank 1307 | 4 samples | 1 papers | 4 compositions
- compositions: (PrBaCoFeO5)5.9(Ce0.8Sm0.2O1.9)4.1 (1); (PrBaCoFeO5)2.7(Ce0.8Sm0.2O1.9)7.3 (1); (PrBaCoFeO5)2.3(Ce0.8Sm0.2O1.9)2.7 (1); (PrBaCoFeO5)7(Ce0.8Sm0.2O1.9)13 (1)
- dopant candidates (<5% at.): Sm (4)
- solid-solution axis: Ce/(Ce+Pr) spans 0.36-0.68 (median 0.60) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 523-1123 K (5th-95th pct of 4 curves)
- papers: Improved electrochemical performance and thermal expansion compatibility of LnBaCoFeO5+–Sm0.2Ce0.8O1.9 (Ln Pr and Nd) composite cathodes for IT-SOFCs

## Ba-Ce-Fe-O
- rank 1308 | 4 samples | 1 papers | 2 compositions
- compositions: BaCe0.5Fe0.5O3 (2); BaCe0.5Fe0.4Ni0.1O3 (2)
- dopant candidates (<5% at.): Ni (2)
- measured range: 573-973 K (5th-95th pct of 4 curves)
- papers: Novel dual-phase symmetrical electrode materials for protonic ceramic fuel cells

## Ba-Co-Fe-Gd-O
- rank 1309 | 4 samples | 2 papers | 4 compositions
- compositions: GdBaCo1.4Fe0.6O5 (1); GdBaCo1.2Fe0.8O5 (1); GdBaCoFeO5 (1); GdBaFeCoO5 (1)
- measured range: 298-1016 K (5th-95th pct of 5 curves; full span incl. outliers 298-1065 K)
- papers: Thermoelectric properties of GdBaCo2−x Fe x O5+δ ceramics | Synthesis and properties of LnBaFeCoO5 + δ (Ln = Nd, Sm, Gd)

## Ba-Co-Ho-O
- rank 1310 | 4 samples | 3 papers | 3 compositions
- compositions: HoBaCo2O5.5 (2); BaHoCo4O7 (1); HoBaCo4O7 (1)
- measured range: 13-997 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaHoCo4O7 P6_3mc (186) mp-19620 [hull=0.022, icsd=6, PRIMARY]; Ba2Ho2Co4O11 Pmma (51) mp-25731 [hull=0.111, icsd=4, PRIMARY]; BaHo(CoO3)2 Pmmm (47) mp-1105900 [hull=0.158, icsd=1, PRIMARY, AMBIGUOUS]; BaHo(CoO3)2 P4/mmm (123) mp-1079686 [hull=0.159, icsd=1]; Ba2Ho2Co4O11 Pmmm (47) mp-604411 [hull=0.118]
- papers: Structural and thermoelectric properties of BaRCo4O7 (R = Dy, Ho, Er, Tm, Yb, and Lu) | Electronic transport and thermoelectric properties of RBaCo4O7 (R=Dy, Ho, Y, Er) | Thermoelectric Power ofHoBaCo2O5.5: Possible Evidence of the Spin Blockade in Cobaltites

## Ba-Co-O-Sm
- rank 1311 | 4 samples | 2 papers | 4 compositions
- compositions: SmBaCo2O5 (1); SmBa0.75Ca0.25Co2O5 (1); SmBa0.9Sr0.1Co2O5 (1); SmBa0.7Sr0.3Co2O5 (1)
- dopant candidates (<5% at.): Sr (2), Ca (1)
- measured range: 148-1072 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaSm(CoO3)2 Pmmm (47) mp-1188886 [hull=0.098, icsd=1, PRIMARY]; BaSm2(CoO3)2 Pnnm (58) mp-1214473 [hull=0.118, PRIMARY]; BaSm2CoO5 Immm (71) mp-19248 [hull=0.000, PRIMARY]; BaSm(CoO3)2 P4/mmm (123) mp-1205695 [hull=0.106]
- papers: Ca and Fe co-doped SmBaCo2O5 +  layered perovskite as an efficient cathode for intermediate-temperature solid oxide fuel cells | Electrical, thermal and electrochemical properties of SmBa1−xSrxCo2O5+δ cathode materials for intermediate-temperature solid oxide fuel cells

## Ba-Cu-Fe-Gd-O
- rank 1312 | 4 samples | 2 papers | 3 compositions
- compositions: GdBaCuFeO5 (2); Gd0.6Ba0.4CuFeO5 (1); Gd0.5Ba0.5CuFeO5 (1)
- measured range: 293-2578 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaGdFeCuO5 P4mm (99) mp-1206575 [hull=0.710, PRIMARY]
- papers: Thermoelectric properties of layered ferrocuprates LnBaCuFeO5 + δ (Ln= La, Pr, Nd, Sm, Gd-Lu) | Electrical and Thermal Conduction Behaviors in La‐Substituted GdBaCuFeO\n            5+δ\n            Ceramics

## Ba-Cu-Ho-O
- rank 1313 | 4 samples | 1 papers | 4 compositions
- compositions: Ba2HoCu2.7Co0.3O6 (1); Ba2HoCu2.5Co0.5O6 (1); Ba2HoCu2.6Co0.4O6 (1); Ba2HoCu2.4Co0.6O6 (1)
- dopant candidates (<5% at.): Co (4)
- measured range: 10-396 K (5th-95th pct of 16 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2Ho(CuO2)4 Cmmm (65) mp-6205 [hull=0.001, icsd=5, PRIMARY]; Ba2HoCu3O7 Pmmm (47) mp-6616 [hull=0.024, icsd=2, PRIMARY]; BaHo2CuO5 Pnma (62) mp-17878 [hull=0.033, icsd=1, PRIMARY]; Ba2Ho(CuO2)3 P4/mmm (123) mp-616166 [hull=0.004, icsd=1, PRIMARY]; Ba10Ho5(Cu5O11)3 P-1 (2) mp-1229045 [hull=0.025, PRIMARY]
- papers: Thermoelectric and structural characterization of Ba2Ho(Cu3−xCox)O6+y

## Ba-Cu-O-Sr-Y
- rank 1314 | 4 samples | 2 papers | 2 compositions
- compositions: Y0.8Ca0.2Sr1Ba1Cu2.7Ga0.3O7 (2); YBa1.2Sr0.8Cu3O6.95 (2)
- dopant candidates (<5% at.): Ga (2), Ca (2)
- measured range: 13-291 K (5th-95th pct of 4 curves; full span incl. outliers 13-346 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2Sr2Y2Cu6O13 Fmm2 (42) mp-1228545 [hull=0.050, PRIMARY]; Ba3SrY8(CuO5)4 Pm (6) mp-1228408 [hull=0.053, PRIMARY]; BaSrY(CuO2)4 Amm2 (38) mp-1227433 [hull=0.018, PRIMARY]; BaSrY4(CuO5)2 Pmc2_1 (26) mp-1227594 [hull=0.065, PRIMARY]
- papers: Comparison of carrier concentration determined by structural and electrical studies of cation substituted YSr2Cu3O7−δ | Strain effect on the thermoelectric power of YBa2−xSrxCu3O7

## Ba-Cu-P
- rank 1315 | 4 samples | 3 papers | 2 compositions
- compositions: Ba8Cu16P30 (3); BaCu2P4 (1)
- measured range: 10-461 K (5th-95th pct of 10 curves; full span incl. outliers 10-888 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba(Cu2P)4 I4/m (87) mp-14785 [hull=0.000, icsd=1, PRIMARY]; Ba(Cu5P2)2 C2/m (12) mp-618788 [hull=0.022, icsd=1, PRIMARY]; Ba2Cu3P4 Ibam (72) mp-28661 [hull=0.000, icsd=1, PRIMARY]; BaCuP P6_3/mmc (194) mp-16254 [hull=0.000, icsd=1, PRIMARY]; Ba4Cu8P15 Pbcn (60) mp-1197658 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric properties of a clathrate compound Ba8Cu16P30 | Twisted Kelvin Cells and Truncated Octahedral Cages in the Crystal Structures of Unconventional Clathrates, AM2P4(A = Sr, Ba; M = Cu, Ni) | Unconventional Clathrates with Transition Metal–Phosphorus Frameworks

## Ba-Fe-In-Sb
- rank 1316 | 4 samples | 1 papers | 4 compositions
- compositions: BaInFe3.7Co0.3Sb13.92 (1); BaInFe3.7Co0.3Sb12.72 (1); BaInFe3.7Co0.3Sb12.96 (1); BaInFe3.7Co0.3Sb13.44 (1)
- dopant candidates (<5% at.): Co (4)
- measured range: 296-805 K (5th-95th pct of 20 curves)
- papers: Effects of Excess Sb on Thermoelectric Properties of Barium and Indium Double-Filled Iron-Based p-Type Skutterudite Materials

## Ba-Ga-Sb
- rank 1317 | 4 samples | 1 papers | 4 compositions
- compositions: BaGa2Sb2 (1); BaGa1.975Zn0.025Sb2 (1); BaGa1.9Zn0.1Sb2 (1); BaGa1.95Zn0.05Sb2 (1)
- dopant candidates (<5% at.): Zn (3)
- measured range: 295-828 K (5th-95th pct of 16 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba(GaSb)2 Pnma (62) mp-29938 [hull=0.000, icsd=1, PRIMARY]; Ba3GaSb3 Pnma (62) mp-28296 [hull=0.000, icsd=1, PRIMARY]; Ba7Ga4Sb9 Pmmn (59) mp-28314 [hull=0.002, icsd=1, PRIMARY]; Ba3Ga4Sb5 Pmn2_1 (31) mp-1228664 [hull=0.050, PRIMARY]
- papers: Thermoelectric Enhancement in BaGa2Sb2by Zn Doping

## Be
- rank 1318 | 4 samples | 2 papers | 3 compositions
- compositions: Be (2); Be98.7(BeO)1.18Al0.044Ni0.014Mn0.009 (1); Be98.7(BeO)1.2Al0.056Si0.035Ni0.016Mn0.010 (1)
- dopant candidates (<5% at.): O (2), Al (2), Ni (2), Mn (2), Si (1)
- measured range: 12-884 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Be P6_3/mmc (194) mp-87 [hull=0.000, icsd=15, PRIMARY]; Be22Mo Fd-3m (227) mp-30440 [hull=0.021, icsd=2, PRIMARY]; Be22W Fd-3m (227) mp-30444 [hull=0.018, icsd=2, PRIMARY]; LaCeBe26 F432 (209) mp-1222939 [hull=0.000, PRIMARY]; ThUBe26 F432 (209) mp-1217315 [hull=0.001, PRIMARY]
- papers: Low‐Temperature Transport Properties of Commercial Metals and Alloys. IV. Reactor Grade Be, Mo, and W | Plasma-sprayed beryllium for ITER

## Be-Cu
- rank 1319 | 4 samples | 1 papers | 1 compositions
- compositions: Be12.01Ni0.19Co0.19Cu87.6 (4)
- dopant candidates (<5% at.): Ni (4), Co (4)
- measured range: 15-255 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BeCu Pm-3m (221) mp-2323 [hull=0.011, icsd=3, PRIMARY]; Be2Cu Fd-3m (227) mp-2031 [hull=0.000, icsd=2, PRIMARY]; Be3Cu R3m (160) mp-1227357 [hull=0.000, PRIMARY]; Be3Cu Fm-3m (225) mp-1183404 [hull=0.061]
- papers: Zirconium Copper — a New Material for Use at Low Temperatures?

## Be-U
- rank 1320 | 4 samples | 4 papers | 1 compositions
- compositions: UBe13 (4)
- measured range: 11-319 K (5th-95th pct of 3 curves; full span incl. outliers 11-360 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UBe13 Fm-3c (226) mp-1163 [hull=0.000, icsd=11, PRIMARY]; U2Be25Cu Fm-3 (202) mp-1216830 [hull=0.001, PRIMARY]; U2Be25Ga Fm-3 (202) mp-1216806 [hull=0.059, PRIMARY]; U4Be51B R-3 (148) mp-1216800 [hull=0.000, PRIMARY]
- papers: Spin gap in heavy fermion compound UBe13 | Thermal conductivity and specific heat measurements on UBe 13 | Specific Heat and Thermal Conductivity of Superconducting UBe13and UPt3at Very Low Temperatures

## Bi-Ho-Pd
- rank 1321 | 4 samples | 3 papers | 2 compositions
- compositions: HoPdBi (3); HoPd2Bi (1)
- measured range: 13-297 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ho5Bi2Pd Pnma (62) mp-1196727 [hull=0.000, icsd=1, PRIMARY]; HoBiPd F-43m (216) mp-1009132 [hull=0.000, icsd=1, PRIMARY]; Ho5BiPd2 I4/mcm (140) mp-1212221 [hull=0.000, PRIMARY]
- papers: Physical properties of rare-earth-based Heusler phases REPdZ and REPd/sub 2/Z (Z = Sb,Bi) | Magnetic and transport properties of the rare-earth-based Heusler phasesRPdZandRPd2Z(Z=Sb,Bi) | Magnetic and transport properties of rare-earth-based half-Heusler phasesRPdBi: Prospective systems for topological quantum phenomena

## Bi-Ir-O-Sr
- rank 1322 | 4 samples | 1 papers | 4 compositions
- compositions: Bi1.4Sr0.6Ir2O7 (1); Bi1.3Sr0.7Ir2O7 (1); Bi1.2Sr0.8Ir2O7 (1); Bi1.1Sr0.9Ir2O7 (1)
- measured range: 20-301 K (5th-95th pct of 4 curves)
- papers: On the electrical properties of the Bi2−Sr Ir2O7 pyrochlore solid solution: Quantum ab initio and classic calculations

## Bi-La-Li-Mn-O
- rank 1323 | 4 samples | 1 papers | 1 compositions
- compositions: La2BiLiMn4O12 (4)
- measured range: 12-301 K (5th-95th pct of 5 curves)
- papers: Effect of bismuth doping on the physical properties of La–Li–Mn–O manganite

## Bi-La-Mn-O-Sr
- rank 1324 | 4 samples | 3 papers | 2 compositions
- compositions: Bi0.25La0.25Sr0.5MnO3 (3); La0.45Bi0.25Sr0.3MnO3 (1)
- measured range: 11-596 K (5th-95th pct of 7 curves)
- papers: Electrical, thermal and magnetic properties of Bi doped La0.7−xBixSr0.3MnO3 manganites | Magnon drag effect as the dominant contribution to the thermopower in Bi0.5−xLaxSr0.5MnO3 (0.1≤x≤0.4) | Evidence of the Bi3+ lone-pair effect on the charge-ordering state: resistivity and thermoelectric power of Bi0.5−yLaySr0.5MnO3 (0.0≤y≤0.4)

## Bi-Li-Se-Te
- rank 1325 | 4 samples | 1 papers | 4 compositions
- compositions: Li0.3Bi2Se0.3Te2.7 (1); Li0.24Bi2Se0.3Te2 (1); Li0.8Bi2Se0.3Te2.7 (1); Li0.74Bi2Se0.3Te2.7 (1)
- measured range: 14-500 K (5th-95th pct of 9 curves)
- papers: Structural modifications and non-monotonic carrier concentration in Bi2Se0.3Te2.7 by reversible electrochemical lithium reactions

## Bi-Ni-O-Sr
- rank 1326 | 4 samples | 1 papers | 1 compositions
- compositions: Sr5BiNi2O9.6 (4)
- measured range: 293-1319 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr5Ni2BiO10 I4/mmm (139) mp-1189753 [hull=0.059, icsd=3, PRIMARY]
- papers: Synthesis, crystal structure and physico-chemical properties of the new quaternary oxide Sr5BiNi2O9.6

## Bi-S-Sb
- rank 1327 | 4 samples | 1 papers | 4 compositions
- compositions: (Bi0.6Sb0.4)2S3 (1); (Bi0.8Sb0.2)2S3 (1); (Bi0.4Sb0.6)2S3 (1); (Bi0.2Sb0.8)2S3 (1)
- solid-solution axis: Bi/(Bi+Sb) spans 0.20-0.80 (median 0.60) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 12-298 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BiSbS3 Pnma (62) mp-1227486 [hull=0.003, PRIMARY]
- papers: Thermoelectric Properties of (Bi1−x Sb x )2S3 with Orthorhombic Structure

## C-Cr-Fe-V
- rank 1328 | 4 samples | 1 papers | 1 compositions
- compositions: Fe0.693C0.0966Si0.0180Mn0.0459Cr0.0776V0.0693 (4)
- dopant candidates (<5% at.): Mn (4), Si (4)
- measured range: 307-1063 K (5th-95th pct of 16 curves)
- papers: Improvement of thermoelectric power of n-type earth-abundant iron rich alloy by microstructure engineering

## C-Cu-Ni
- rank 1329 | 4 samples | 1 papers | 2 compositions
- compositions: Cu55Ni45SeC10.6 (3); Cu55Ni45SeC16 (1)
- dopant candidates (<5% at.): Se (4)
- measured range: 298-875 K (5th-95th pct of 18 curves)
- papers: Enhancing the thermoelectric performance of Cu–Ni alloys by introducing carbon nanotubes

## C-Fe-Zn
- rank 1330 | 4 samples | 1 papers | 4 compositions
- compositions: ZnC1.2Fe3 (1); ZnC1.5Fe3 (1); ZnC1.3Fe3 (1); ZnC1.4Fe3 (1)
- measured range: 11-350 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZnFe3C Pm-3m (221) mp-10266 [hull=0.021, icsd=1, PRIMARY]
- papers: The magnetic, electrical transport and thermal transport properties of Fe-based antipervoskite compounds ZnCxFe3

## C-Ge-Si
- rank 1331 | 4 samples | 1 papers | 3 compositions
- compositions: Si80Ge20C30 (2); Si80Ge20C6 (1); Si80Ge20C15 (1)
- measured range: 300-1088 K (5th-95th pct of 6 curves)
- papers: Transport properties of nanocomposite thermoelectric materials based on Si and Ge

## C-H-Zr
- rank 1332 | 4 samples | 1 papers | 4 compositions
- compositions: (ZrC)0.8(ZrH2)0.2 (1); (ZrC)0.6(ZrH2)0.4 (1); (ZrC)0.7(ZrH2)0.3 (1); (ZrC)0.9(ZrH2)0.1 (1)
- measured range: 304-1273 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zr2HC P3m1 (156) mp-1215471 [hull=0.000, PRIMARY]; Zr3HC2 P-3m1 (164) mp-1215581 [hull=0.026, PRIMARY]
- papers: Densification, mechanical and thermal properties of ZrC1− ceramics fabricated by two-step reactive hot pressing of ZrC and ZrH2 powders

## C-Mg-Sb
- rank 1333 | 4 samples | 1 papers | 4 compositions
- compositions: Mg3Sb2C0.32 (1); Mg3Sb2C0.43 (1); Mg3Sb2C0.66 (1); Mg3Sb1.8Bi0.2C0.3 (1)
- dopant candidates (<5% at.): Bi (1)
- measured range: 317-778 K (5th-95th pct of 20 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg14SbC Amm2 (38) mp-1026465 [hull=0.239, PRIMARY]; Mg6SbC Amm2 (38) mp-1017117 [hull=0.442, PRIMARY]; Mg14SbC P-6m2 (187) mp-1026411 [hull=0.313]
- papers: Graphene boosts thermoelectric performance of a Zintl phase compound

## C-N-Ti
- rank 1334 | 4 samples | 1 papers | 4 compositions
- compositions: TiC0.7N0.3 (1); TiC0.6N0.4 (1); TiC0.4N0.6 (1); TiC0.3N0.7 (1)
- measured range: 308-1025 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti2CN R-3m (166) mp-1217142 [hull=0.000, PRIMARY]; Ti4C3N R-3m (166) mp-1217103 [hull=0.000, PRIMARY]; Ti4CN3 R-3m (166) mp-1217107 [hull=0.001, PRIMARY]; Ti5CN4 R-3m (166) mp-1217133 [hull=0.001, PRIMARY]
- papers: Titanium carbonitride-based cermets: processes and properties

## Ca-Co-Na-O
- rank 1335 | 4 samples | 2 papers | 2 compositions
- compositions: Ca1.55Na0.45Co2O5 (3); (Ca3Co4O9)2.2(Na0.75CoO2)3.2 (1)
- measured range: 301-1052 K (5th-95th pct of 7 curves)
- papers: Preparation and characterization of the new oxides Ca2−xNaxCo2O5 | Improved environmental stability of thermoelectric ceramics based on intergrowths of Ca3Co4O9–Na0.75CoO2

## Ca-Cr-O-Y
- rank 1336 | 4 samples | 1 papers | 4 compositions
- compositions: Y0.7Ca0.3Cr0.95Zn0.05O3 (1); Y0.7Ca0.3Cr0.9Zn0.1O3 (1); Y0.7Ca0.3CrO3 (1); Y0.7Ca0.3Cr0.85Zn0.15O3 (1)
- dopant candidates (<5% at.): Zn (3)
- measured range: 773-1123 K (5th-95th pct of 4 curves)
- papers: Stable, easily sintered Ca–Zn-doped YCrO3 as novel interconnect materials for co-fired yttrium-stabilized zirconia-based solid oxide fuel cells

## Ca-Cu-La-O
- rank 1337 | 4 samples | 1 papers | 2 compositions
- compositions: La1.90Ca1.10Cu2O6 (2); La1.85Ca1.15Cu2O6 (2)
- measured range: 16-300 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca2La2Cu3O8 I4/mmm (139) mp-1214137 [hull=0.138, PRIMARY]; Ca2La3Cu4AgO12 Amm2 (38) mp-1227548 [hull=0.106, PRIMARY]; CaLa2Cu2O7 I4/mmm (139) mp-1213978 [hull=0.098, PRIMARY]
- papers: Evidence for magnetic-field-induced decoupling of superconducting bilayers in \n<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:mrow><mml:msub><mml:mi>La</mml:mi><mml:mrow><mml:mn>2</mml:mn><mml:mo>−</mml:mo><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Ca</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mo>+</mml:mo><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Cu</mml:mi><mml:mn>2</mml:mn></mml:msub><mml:msub><mml:mi mathvariant=\"normal\">O</mml:mi><mml:mn>6</mml:mn></mml:msub></mml:mrow></mml:math>

## Ca-Fe-La-Mo-O
- rank 1338 | 4 samples | 1 papers | 4 compositions
- compositions: Ca1.4La0.6FeMoO6 (1); Ca1.3La0.7FeMoO6 (1); Ca1.2La0.8FeMoO6 (1); Ca1.5La0.5FeMoO6 (1)
- measured range: 25-295 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca3LaFe2(MoO6)2 P1 (1) mp-1228602 [hull=0.184, PRIMARY]
- papers: Disorder induced magnetism and electrical conduction in La doped Ca2FeMoO6 double perovskite

## Ca-Hf-O
- rank 1339 | 4 samples | 1 papers | 4 compositions
- compositions: CaHfO3 (1); CaHf0.9Sc0.1O3 (1); CaHf0.85Sc0.15O3 (1); CaHf0.8Sc0.2O3 (1)
- dopant candidates (<5% at.): Sc (3)
- measured range: 673-1173 K (5th-95th pct of 4 curves)
- [ref 1] TEDesignLab / ICSD: Ca2Hf7O16 R-3 (148) mp-27221 [hull=0.002, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ca2HfO4 Pbam (55) mp-752413 [hull=0.004, PRIMARY]; Ca6HfO8 Fm-3m (225) mp-755421 [hull=0.002, PRIMARY]; CaHfO3 Pnma (62) mp-754853 [hull=0.000, PRIMARY]; Ca2HfO4 Pbca (61) mp-752396 [hull=0.025]; CaHfO3 Pm-3m (221) mp-1016873 [hull=0.154]
- papers: Influence of Sc concentration on transport properties of CaHf1-xScxO3-α

## Ca-La
- rank 1340 | 4 samples | 1 papers | 3 compositions
- compositions: Ca0.78La0.22 (2); Ca0.95La0.05 (1); Ca0.30La0.70 (1)
- measured range: 10-281 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaLa P-6m2 (187) mp-1183602 [hull=0.088, PRIMARY]
- papers: Thermoelectric power of Nd1−xLaxand Ce1−xLaxalloys

## Ca-La-Mn-O-Ti
- rank 1341 | 4 samples | 2 papers | 3 compositions
- compositions: La0.7Ca0.3Ti0.5Mn0.4Ni0.1O3 (2); La0.4Ca0.6Ti0.6Mn0.4O3 (1); La0.4Ca0.6Ti0.4Mn0.6O3 (1)
- dopant candidates (<5% at.): Ni (2)
- measured range: 723-1172 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca9LaTi4Mn6O30 P1 (1) mp-744380 [hull=0.010, PRIMARY]; Ca9LaTi6Mn4O30 P1 (1) mp-706246 [hull=0.008, PRIMARY]; Ca9LaTi8Mn2O30 P1 (1) mp-694916 [hull=0.009, PRIMARY]; Ca9LaTi9MnO30 Pm (6) mp-694954 [hull=0.008, PRIMARY]; CaLaTiMnO6 Pc (7) mp-40866 [hull=0.026, PRIMARY]
- papers: Manganese-doped lanthanum calcium titanate as an interconnect for flat-tubular solid oxide fuel cells | A-site cation influences on performance, structure and conductivity of a lanthanide-based perovskite electrode for symmetrical solid oxide fuel cells

## Ca-La-O-Ti
- rank 1342 | 4 samples | 2 papers | 4 compositions
- compositions: La0.5Ca0.5TiO3 (1); La0.7Ca0.3TiO3 (1); La0.4Ca0.6TiO3 (1); La0.4Ca0.6Ti0.8Mn0.2O3 (1)
- dopant candidates (<5% at.): Mn (1)
- measured range: 300-1172 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca10La6Mg3Ti13O48 P1 (1) mp-695254 [hull=0.015, PRIMARY]; Ca14La6Mg3Ti17O60 P1 (1) mp-695227 [hull=0.012, PRIMARY]; Ca2La4Ti5O18 R-3m (166) mp-1227811 [hull=0.079, PRIMARY]; Ca9LaTi10O30 P1 (1) mp-686651 [hull=0.000, PRIMARY]
- papers: Development of Perovskite-type Cobaltates and Manganates for Thermoelectric Oxide Modules | Manganese-doped lanthanum calcium titanate as an interconnect for flat-tubular solid oxide fuel cells

## Ca-La-Te
- rank 1343 | 4 samples | 1 papers | 4 compositions
- compositions: La2.2Ca0.8Te4 (1); La1.9Ca1.1Te4 (1); La2.5Ca0.5Te4 (1); La0.9Ca2.1Te4 (1)
- measured range: 293-1276 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca(LaTe2)2 I-42d (122) mp-36031 [hull=0.015, PRIMARY]
- papers: Mechanochemical synthesis and high temperature thermoelectric properties of calcium-doped lanthanum telluride La3−xCaxTe4

## Ca-O
- rank 1344 | 4 samples | 2 papers | 3 compositions
- compositions: CaO (2); Ca3O4O9 (1); Ca3O3.9Re0.1O9 (1)
- dopant candidates (<5% at.): Re (1)
- measured range: 300-1274 K (5th-95th pct of 2 curves; full span incl. outliers 300-1412 K)
- [ref 1] TEDesignLab / ICSD: CaO Fm-3m (225) mp-2605 [hull=0.000, icsd=14, PRIMARY]; CaO2 I4/mmm (139) mp-634859 [hull=0.007, icsd=2]; CaO Fd-3m (227) mp-1181903 [hull=2.732]; CaO (186)
- [ref 2] MP, ranked by ICSD evidence: CaO2 P-3m1 (164) mp-1062228 [hull=0.483, icsd=9, PRIMARY]; CaO10 P4/mcc (124) mp-1182382 [hull=0.094, icsd=2, PRIMARY]; Ca3SiCSO24 P2_1 (4) mp-1196628 [hull=0.927, icsd=1, PRIMARY]; Ca2O3 P1 (1) mp-1120811 [hull=0.221, PRIMARY]; Ca3MnCSO25 P6_3 (173) mp-1195426 [hull=0.784, PRIMARY]
- papers: Structure and transport properties in Ca3Co4−xMxO9 (M=Re and Pt) ceramics | Thermal Conductivity of 2CaO·SiO<sub>2</sub> Bearing Solid Solution

## Ca-O-Ru-Sr
- rank 1345 | 4 samples | 2 papers | 4 compositions
- compositions: Ca0.4Sr0.6RuO3 (1); Ca0.6Sr0.4RuO3 (1); Ca0.5Sr0.5RuO3 (1); Ca1.5Sr0.5RuO4 (1)
- solid-solution axis: Ca/(Ca+Sr) spans 0.40-0.75 (median 0.60) over 4 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 12-1167 K (5th-95th pct of 13 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr3Ca3(Ru2O7)2 P1 (1) mp-1218638 [hull=0.010, PRIMARY]; SrCa(RuO3)2 Pmc2_1 (26) mp-1218505 [hull=0.008, PRIMARY]; SrCa3(RuO3)4 Pm (6) mp-1218465 [hull=0.007, PRIMARY]; SrCa3(RuO4)2 Iba2 (45) mp-1218458 [hull=0.033, PRIMARY]
- papers: Thermoelectric properties of Ca1−xSrxRuO3 compounds prepared by spark plasma sintering | Quasi-Two-Dimensional Mott Transition System<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi>Ca</mml:mi></mml:mrow><mml:mrow><mml:mn>2</mml:mn><mml:mo>−</mml:mo><mml:mi mathvariant=\"italic\">x</mml:mi></mml:mrow></mml:msub></mml:mrow><mml:mrow><mml:msub><mml:mrow><mml:mi>Sr</mml:mi></mml:mrow><mml:mrow><mml:mi mathvariant=\"italic\">x</mml:mi></mml:mrow></mml:msub></mml:mrow><mml:mrow><mml:msub><mml:mrow><mml:mi>RuO</mml:mi></mml:mrow><mml:mrow><mml:mn>4</mml:mn></mml:mrow></mml:msub></mml:mrow></mml:math>

## Ca-O-Si
- rank 1346 | 4 samples | 2 papers | 3 compositions
- compositions: (Ca2SiO4)0.86(Ca3P2O8)0.14 (2); (Ca2SiO4)0.84(Ca3P2O8)0.1(Fe2SiO4)0.05 (1); Ca3SiO (1)
- dopant candidates (<5% at.): P (3), Fe (1)
- measured range: 13-1722 K (5th-95th pct of 6 curves)
- [ref 1] TEDesignLab / ICSD: CaSiO3 Pm-3m (221) mp-5893 [hull=0.245, icsd=25, PRIMARY]; Ca2SiO4 P2_1/c (14) mp-4180 [hull=0.035, icsd=19, PRIMARY]; CaSiO3 I4/mcm (140) mp-3387 [hull=0.242, icsd=16]; CaSiO3 Imma (74) mp-5096 [hull=0.242, icsd=15]; Ca2SiO4 Pnma (62) mp-4481 [hull=0.000, icsd=12]
- [ref 2] MP, ranked by ICSD evidence: Ca6Si6O19 P2/c (13) mp-1200566 [hull=0.080, icsd=3, PRIMARY]; Ca3SiO5 P-1 (2) mp-641754 [hull=0.020, icsd=2, PRIMARY]; Ca3Si2O7 P2_1/c (14) mp-3932 [hull=0.009, icsd=2, PRIMARY]; Ca5(SiO5)2 P2_1/c (14) mp-1197843 [hull=0.070, icsd=2, PRIMARY]; CaSiO3 P2_1/c (14) mp-5733 [hull=0.000, icsd=4]
- papers: Thermal Conductivity of 2CaO·SiO<sub>2</sub> Bearing Solid Solution | Thermoelectric properties of inverse perovskites A3TtO (A = Mg, Ca; Tt = Si, Ge): Computational and experimental investigations

## Ca-O-Sr-V
- rank 1347 | 4 samples | 1 papers | 4 compositions
- compositions: Sr0.5Ca0.5VO3.010 (1); Sr0.5Ca0.5VO3.014 (1); Sr0.5Ca0.5VO3.017 (1); Sr0.5Ca0.5VO3.023 (1)
- measured range: 22-296 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr3CaV4O12 Pmmm (47) mp-1218542 [hull=0.071, PRIMARY]; SrCa3V4O12 Pm (6) mp-1218581 [hull=0.017, PRIMARY]; SrCaV2O6 Pmc2_1 (26) mp-1218467 [hull=0.030, PRIMARY]
- papers: Structure and electrical properties of Sr0.5Ca0.5VOy

## Ce-Co-Cu-Ge
- rank 1348 | 4 samples | 1 papers | 3 compositions
- compositions: Ce(Cu0.4Co0.6)2Ge2 (2); Ce(Cu0.8Co0.2)2Ge2 (1); Ce(Cu0.6Co0.4)2Ge2 (1)
- measured range: 11-300 K (5th-95th pct of 4 curves)
- papers: Non-Fermi-liquid behavior at the antiferromagnetic quantum critical point in the heavy-fermion system \n<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:mrow><mml:mi>Ce</mml:mi><mml:msub><mml:mrow><mml:mo>(</mml:mo><mml:msub><mml:mi>Cu</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mo>−</mml:mo><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Co</mml:mi><mml:mi>x</mml:mi></mml:msub><mml:mo>)</mml:mo></mml:mrow><mml:mn>2</mml:mn></mml:msub><mml:msub><mml:mi>Ge</mml:mi><mml:mn>2</mml:mn></mml:msub></mml:mrow></mml:math>

## Ce-Co-Si
- rank 1349 | 4 samples | 4 papers | 3 compositions
- compositions: CeCo2Si2 (2); Ce2Co3Si (1); CeCo0.8Cu0.2Si3 (1)
- dopant candidates (<5% at.): Cu (1)
- measured range: 14-800 K (5th-95th pct of 8 curves; full span incl. outliers 14-896 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(CoSi)2 I4/mmm (139) mp-3437 [hull=0.000, icsd=10, PRIMARY]; CeCoSi2 Cmcm (63) mp-7095 [hull=0.000, icsd=2, PRIMARY]; CeCoSi P4/nmm (129) mp-1018660 [hull=0.000, icsd=2, PRIMARY]; CeCo9Si4 I4/mcm (140) mp-1193469 [hull=0.000, icsd=2, PRIMARY]; Ce3Co8Si P6_3/mmc (194) mp-1214094 [hull=0.024, icsd=1, PRIMARY]
- papers: Thermoelectric properties of the intermediate valent cerium intermetallic Ce2Ni3Si5 doped with Pd, Co, and Cu | Thermoelectric Power and Electron Scattering in Metal Alloys | Peculiarities of the intermediate valence state of Ce in CeM2Si2 (M=Fe, Co, Ni) compounds

## Ce-Cu-Ni-Si
- rank 1350 | 4 samples | 2 papers | 4 compositions
- compositions: Ce2Ni2.5Cu0.5Si (1); Ce(Ni0.4Cu0.6)2Si2 (1); Ce(Ni0.25Cu0.75)2Si2 (1); Ce(Ni0.75Cu0.25)2Si2 (1)
- measured range: 11-399 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeCuSi2Ni I-4m2 (119) mp-1226605 [hull=0.000, PRIMARY]
- papers: Thermoelectric properties of the intermediate valent cerium intermetallic Ce2Ni3Si5 doped with Pd, Co, and Cu | Competing energy scales in the compounds Ce(Ni1−xCux)2(Si2)
