# Host systems -- chunk 006 of 73

Ranks 251-300 by sample count. These 50 host systems cover 1315 samples (2.53% of the TE set); cumulative through this chunk: 73.60%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## La-Ni-O-Sr
- rank 251 | 29 samples | 9 papers | 13 compositions
- compositions: LaSrNiO4 (8); LaSrNi0.8Sc0.2O4.00 (3); LaSrNi0.9Sc0.1O3.99 (3); La1.5Sr0.5NiO4 (3); LaSrNiO3.97 (3); La1.5Sr0.5Ni0.7Fe0.3O4 (2)
- dopant candidates (<5% at.): Sc (6), Fe (2), Mn (2)
- seed hypothesis (confirm): ruddlesden_popper
- measured range: 10-1235 K (5th-95th pct of 28 curves; full span incl. outliers 10-1407 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr4La4Cr(NiO5)3 P2/m (10) mp-1173211 [hull=0.069, PRIMARY]; Sr5La5Cu(NiO5)4 P1 (1) mp-690554 [hull=0.000, PRIMARY]; SrLa3(NiO4)2 Amm2 (38) mp-1218254 [hull=0.008, PRIMARY]; SrLaNiO4 Cmcm (63) mp-1218178 [hull=0.001, PRIMARY]
- papers: Electrical Conductivity and Thermoelectric Power of La | Transport properties of LaSrNi1 − x ScxOy solid solutions | Electrochemical Performance of La 1.5 Sr 0.5 Ni 1-x Fe x O 4+ δ Cathode for IT-SOFCs

## La-O-Rh
- rank 252 | 29 samples | 4 papers | 16 compositions
- compositions: LaRhO3 (7); LaRh0.95Ni0.05O3 (3); LaRh0.9Ni0.1O3 (3); LaRh0.8Ni0.2O3 (2); LaCo0.2Rh0.8O3 (2); LaCo0.1Rh0.9O3 (2)
- dopant candidates (<5% at.): Ni (9), Sr (5), Mg (4), Co (4)
- measured range: 10-808 K (5th-95th pct of 43 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaRhO3 Pnma (62) mp-5163 [hull=0.000, icsd=2, PRIMARY]
- papers: Thermoelectric properties of LaRh1−xNixO3 | Thermoelectric Properties of B-Site Substituted LaRhO3 | Lattice crossover and mixed valency in the LaCo1−xRhxO3 solid solution

## Ni-Sb-Sn
- rank 253 | 29 samples | 2 papers | 11 compositions
- compositions: Ni4Sb8.2Sn3.8 (10); Ba0.42Ni4Sb8.2Sn3.8 (10); Sn0.15Ni4Sb7.6Sn4.4 (1); Sn0.22Ni4Sb7.1Sn4.9 (1); Sn0.21Ni4Sb7.1Sn4.9 (1); Eu0.8Ni4Sb5.8Sn6.2 (1)
- dopant candidates (<5% at.): Ba (10), Eu (1), Yb (1), Co (1)
- measured range: 10-771 K (5th-95th pct of 46 curves; full span incl. outliers 10-820 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ni4(SnSb3)3 Cm (8) mp-1220099 [hull=0.005, PRIMARY]; Ni6SnSb Pmm2 (25) mp-1219799 [hull=0.002, PRIMARY]
- papers: Ba-filled Ni–Sb–Sn based skutterudites with anomalously high lattice thermal conductivity | Crystal structure and thermoelectric properties of novel skutterudites Ep/sub y/Ni/sub 4/Sb/sub 12-x/Sn/sub x/ with Ep=Sn, Eu and Yb

## O-Pr-Sr-Ti
- rank 254 | 29 samples | 3 papers | 4 compositions
- compositions: Sr0.45Pr0.367TiO3 (9); Sr0.30Pr0.467TiO3 (9); Sr0.60Pr0.267TiO3 (9); Sr0.70Pr0.30TiO3 (2)
- measured range: 307-1173 K (5th-95th pct of 35 curves)
- papers: Enhancement of thermoelectric performance in strontium titanate by praseodymium substitution | Effect of A-Site Cation Deficiency on the Thermoelectric Performance of Donor-Substituted Strontium Titanate | Enhancing the thermoelectric properties of Sr\n            \n              1−\n              x\n            \n            Pr\n            \n              2\n              x\n              /3\n            \n            □\n            \n              x\n            \n            /3\n            TiO\n            \n              3±\n              δ\n            \n            through control of crystal structure and microstructure

## B-Fe
- rank 255 | 28 samples | 6 papers | 18 compositions
- compositions: Fe80B20 (6); Fe85B15 (3); Fe83B14Si1.5C1.5 (2); FeB (2); Fe2B (2); (Fe0.98Ni0.02)84B16 (1)
- dopant candidates (<5% at.): Ni (3), Si (2), C (2), Co (2), Ta (1), V (1), Nb (1), Cr (1), Mn (1), Rh (1), Pd (1)
- seed hypothesis (confirm): metallic_glass
- measured range: 13-962 K (5th-95th pct of 32 curves; full span incl. outliers 12-1272 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeB Pnma (62) mp-20787 [hull=0.005, icsd=12, PRIMARY]; Fe2B I4/mcm (140) mp-1915 [hull=0.000, icsd=12, PRIMARY]; Fe2B7 Pbam (55) mp-1194531 [hull=0.009, icsd=11, PRIMARY]; Fe3B Pnma (62) mp-973682 [hull=0.018, icsd=2, PRIMARY]; FeB4 Pnnm (58) mp-1079437 [hull=0.000, icsd=2, PRIMARY]
- papers: Thermoelectric power in some ferromagnetic Fe based amorphous alloys | Influence of small amounts of Co and Ni additives on thermoelectric power in amorphous Fe&lt;inf&gt;84&lt;/inf&gt;B&lt;inf&gt;16&lt;/inf&gt; | Seebeck coefficients of iron group elements borides

## Ba-Ge-Ni
- rank 256 | 28 samples | 10 papers | 13 compositions
- compositions: Ba8Ni2.9Zn1.2Ge41.9 (6); Ba8Ni2.8Zn2.4Ge40.8 (4); Ba8Ni2.8Zn1.5Ge41.7 (4); Ba8Ni3.5Ge42.1 (3); Ba8Ni4Ge42 (2); Ba8Ni5Ge41 (2)
- dopant candidates (<5% at.): Zn (14)
- seed hypothesis (confirm): clathrate_i
- measured range: 10-841 K (5th-95th pct of 54 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2Ni5Ge4 C2/m (12) mp-1095498 [hull=0.000, icsd=1, PRIMARY]; Ba4Ni3Ge20 Pm-3n (223) mp-30169 [hull=0.018, icsd=1, PRIMARY]
- papers: On the Design of High-Efficiency Thermoelectric Clathrates through a Systematic Cross-Substitution of Framework Elements | Atomic ordering and thermoelectric properties of the n-type clathrate Ba8Ni3.5Ge42.1□0.4 | Low-Temperature Physical and Thermoelectric Properties of Ba8Ni5Ge41

## Ba-O-Pb
- rank 257 | 28 samples | 8 papers | 16 compositions
- compositions: BaPbO3 (6); BaPb0.8Bi0.2O3 (3); Ba0.8Sr0.2Pb0.85Bi0.15O3 (2); BaPb0.85Bi0.15O3 (2); Ba0.8Sr0.2Pb0.8Bi0.2O3 (2); Ba0.9Sr0.1Pb0.85Bi0.15O3 (2)
- dopant candidates (<5% at.): Bi (14), Sr (8), Zr (3), Sb (3), La (2)
- seed hypothesis (confirm): perovskite
- measured range: 11-1172 K (5th-95th pct of 29 curves)
- [ref 1] TEDesignLab / ICSD: BaPbO3 C2/m (12) mp-20461 [hull=0.000, icsd=14, PRIMARY]; Ba2PbO4 I4/mmm (139) mp-20098 [hull=0.000, icsd=4, PRIMARY]; BaPbO3 Imma (74) mp-22230 [hull=0.000, icsd=11]; BaPbO3 I4/mcm (140) mp-20991 [hull=0.003, icsd=2]
- [ref 2] MP, ranked by ICSD evidence: Ba3PbO Pm-3m (221) mp-29242 [hull=0.000, icsd=1, PRIMARY]; Ba32Sb7Pb25O96 Cmmm (65) mp-686499 [hull=0.000, PRIMARY]; Ba4Pb3O10 P1 (1) mp-752906 [hull=0.014, PRIMARY]; Ba7Pb17O24 Pm (6) mp-758059 [hull=0.000, PRIMARY]; BaPbO3 Pm-3m (221) mp-21280 [hull=0.026, icsd=5]
- papers: Preparation of dense BaPbO3-based ceramics by a coprecipitation and their thermoelectric properties | Transport studies of perovskite oxide BaPb1-xZrxO3 | Metal–insulator transition and superconductivity in Sr- and La-substituted BaPb1−xBixO3

## Cr-Se
- rank 258 | 28 samples | 5 papers | 26 compositions
- compositions: Cr2Se3 (3); Ba0.5Cr5Se8 (1); Ba0.52Cr5Se8 (1); Ba0.55Cr5Se8 (1); Ba0.51Cr5Se8 (1); Cr1.96Se3 (1)
- dopant candidates (<5% at.): Mn (8), Ba (4), Ni (4), S (4), Nb (4)
- seed hypothesis (confirm): nias
- measured range: 11-873 K (5th-95th pct of 41 curves)
- [ref 1] TEDesignLab / ICSD: CrSe P6_3/mmc (194) mp-2189 [hull=0.128, icsd=6, PRIMARY]; Cr2Se3 R-3 (148) mp-1079651 [hull=0.000, icsd=4, PRIMARY]; CrSe (186)
- [ref 2] MP, ranked by ICSD evidence: Cr3Se4 C2/m (12) mp-27840 [hull=0.000, icsd=4, PRIMARY]; CrSe2 P-3m1 (164) mp-1009581 [hull=0.000, icsd=1, PRIMARY]; Cr7Se8 C2/m (12) mp-696673 [hull=0.056, icsd=1, PRIMARY]; Cr5Se8 C2/m (12) mp-1104327 [hull=0.000, icsd=1, PRIMARY]; Cr2Se3 P-31c (163) mp-1189023 [hull=0.002, icsd=1]
- papers: Thermoelectric properties of chromium sulfo-selenides | Magnetic and thermoelectric properties of the ternary pseudo-hollandite BaxCr5Se8(0.5 < x < 0.55) solid solution | Facile p–n control, and magnetic and thermoelectric properties of chromium selenides Cr2+xSe3

## In-Ru
- rank 259 | 28 samples | 5 papers | 17 compositions
- compositions: RuIn3 (3); RuIn2.99Sn0.01 (2); RuIn2.975Zn0.025 (2); RuIn2.95Zn0.05 (2); RuIn2.9Zn0.1 (2); Ru0.25In0.75 (2)
- dopant candidates (<5% at.): Zn (10), Sn (9), Ir (2), Rh (1), Re (1)
- seed hypothesis (confirm): fega3
- measured range: 10-808 K (5th-95th pct of 94 curves; full span incl. outliers 10-972 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): In3Ru P4_2/mnm (136) mp-607450 [hull=0.000, icsd=2, PRIMARY]; InRu3 P6_3/mmc (194) mp-1095082 [hull=0.357, icsd=1, PRIMARY]; In3Ru P-4n2 (118) mp-672326 [hull=0.000, icsd=1]
- papers: Thermoelectric properties of FeGa3-type narrow-bandgap intermetallic compounds Ru(Ga,In)3: Experimental and calculational studies | Thermoelectric properties of intermetallic semiconducting RuIn3 and metallic IrIn3 | RuIn3-xSnx, RuIn3-xZnx, and Ru1-yIn3—new thermoelectrics based on the semiconductor RuIn3

## Ni-Sb-Zr
- rank 260 | 28 samples | 4 papers | 16 compositions
- compositions: Zr3Ni3Sb4 (4); Zr3Ni2.9Co0.1Sb4 (4); Zr3Ni2.7Cu0.3Sb4 (3); Zr3Ni2.95Co0.05Sb4 (2); Zr3Ni2.8Co0.2Sb4 (2); Zr3Ni2.9Cu0.1Sb4 (2)
- dopant candidates (<5% at.): Co (13), Cu (7), Te (4), Pt (1)
- seed hypothesis (confirm): y3au3sb4
- measured range: 13-872 K (5th-95th pct of 102 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zr3NiSb7 Pnma (62) mp-22174 [hull=0.003, icsd=4, PRIMARY]; ZrNi2Sb P6_3/mmc (194) mp-3469 [hull=0.000, icsd=3, PRIMARY]; Zr3Ni3Sb4 I-43d (220) mp-17926 [hull=0.000, icsd=1, PRIMARY]; Zr5NiSb3 P6_3/mcm (193) mp-1106076 [hull=0.000, icsd=1, PRIMARY]; Zr5NiSb9 P4/n (85) mp-1192450 [hull=0.020, icsd=1, PRIMARY]
- papers: Thermoelectric properties and electronic transport analysis of Zr3Ni3Sb4-based solid solutions | High thermoelectric performance in the multi-valley electronic system Zr3Ni3−xCoxSb4 and the high-mobility Zr3Ni3−xCuxSb4 | Thermoelectric properties of ternary transition metal antimonides

## Ag-Bi-Se
- rank 261 | 27 samples | 6 papers | 20 compositions
- compositions: AgBiSe2 (7); Ag0.985In0.015BiSe2 (2); AgBiSe1.98I0.02 (1); AgBiSe1.98Cl0.02 (1); AgBiSe1.98Br0.02 (1); AgBi0.975Pb0.025Se2 (1)
- dopant candidates (<5% at.): Pb (5), In (5), Nb (2), Cl (1), I (1), Br (1)
- seed hypothesis (confirm): rocksalt
- measured range: 36-810 K (5th-95th pct of 108 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AgBiSe2 R-3m (166) mp-27916 [hull=0.002, icsd=4, PRIMARY]; Ag(BiSe2)3 Cmmm (65) mp-1207284 [hull=1.434, PRIMARY]; Ag3BiSe6 Cmmm (65) mp-1215149 [hull=1.150, PRIMARY]; AgBiSe2 I4_1/amd (141) mp-33618 [hull=0.043]; AgBiSe2 P4/mmm (123) mp-1229087 [hull=0.104]
- papers: Promising thermoelectric performance in n-type AgBiSe2: effect of aliovalent anion doping | Solid-Solutioned Homojunction Nanoplates with Disordered Lattice: A Promising Approach toward “Phonon Glass Electron Crystal” Thermoelectric Materials | High Thermoelectric and Reversiblep-n-pConduction Type Switching Integrated in Dimetal Chalcogenide

## Ag-Cu-Se
- rank 262 | 27 samples | 7 papers | 13 compositions
- compositions: CuAgSe (15); Cu0.99AgSe (1); Cu0.98AgSe (1); CuAg0.99Se (1); Cu1.98Ag0.2Se (1); CuAgSe1.04 (1)
- dopant candidates (<5% at.): Te (3), Ni (1), Co (1), Zn (1)
- seed hypothesis (confirm): cu2se_superionic
- solid-solution axis: Ag/(Ag+Cu) spans 0.09-0.51 (median 0.50) over 13 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 18-775 K (5th-95th pct of 105 curves; full span incl. outliers 10-899 K)
  !! MEASUREMENT CROSSES A TRANSITION: cu2se_superionic -> cu2se_superionic at ~400 K (Ordered low-T superstructure -> cubic superionic, ~400 K. Cu2S transforms near ~376 K.)
     Record each phase with its own temperature range, not a single prototype.
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuAgSe P4/nmm (129) mp-1225840 [hull=0.052, PRIMARY]
- papers: Thermoelectric properties of Ag-doped Cu2Se and Cu2Te | Compound defects and thermoelectric properties in ternary CuAgSe-based materials | Thermoelectric properties of Te-doped ternary CuAgSe compounds

## Ba-Cu-O-Sm
- rank 263 | 27 samples | 6 papers | 19 compositions
- compositions: SmBa2Cu3O7 (6); SmBa2Cu3O6.92 (3); Sm1Ba2Cu3O7 (2); SmBa1.8Sr0.2Cu3O7 (1); SmBa1.6Sr0.4Cu3O7 (1); SmBa2Cu3O6.835 (1)
- dopant candidates (<5% at.): Fe (8), Mn (8), Sr (3), H (3)
- seed hypothesis (confirm): ybco_cuprate
- measured range: 55-311 K (5th-95th pct of 26 curves; full span incl. outliers 52-388 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2SmCu3O7 Pmmm (47) mp-21451 [hull=0.016, icsd=19, PRIMARY]; Ba2Sm(CuO2)3 P4/mmm (123) mp-622576 [hull=0.000, icsd=1, PRIMARY]; Ba4Sm2Cu2O9 P-4n2 (118) mp-636383 [hull=0.015, icsd=1, PRIMARY]; Ba10Sm5(Cu5O11)3 P-1 (2) mp-1229115 [hull=0.017, PRIMARY]; Ba2Sm(CuO2)4 Cmmm (65) mp-1214577 [hull=0.000, PRIMARY]
- papers: Low percolation concentration for zero thermoelectric power in Y1Ba2Cu3O7−x | Normal state transport properties in superconducting oxides RBa2Cu3O7- delta(R=Y, Gd, Sm, Nd, and Dy) | The thermoelectric power of the system SmBa2-xSrxCu3O7-δ

## Bi-Te-Tl
- rank 264 | 27 samples | 8 papers | 17 compositions
- compositions: Tl9BiTe6 (9); TlBiTe2 (3); Tl9Bi0.98Te6 (1); Tl9Bi0.96Te6 (1); Tl9Bi0.97Te6 (1); Tl8.99Bi1.01Te6 (1)
- dopant candidates (<5% at.): Sn (5), Pb (3)
- seed hypothesis (confirm): tl5te3
- measured range: 287-671 K (5th-95th pct of 104 curves; full span incl. outliers 279-763 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TlBiTe2 R-3m (166) mp-27438 [hull=0.000, icsd=2, PRIMARY]; Tl(BiTe2)3 Cmmm (65) mp-1206572 [hull=1.597, PRIMARY]; Tl9BiTe6 I4/m (87) mp-34361 [hull=0.000, PRIMARY]; TlBiTe2 P4/mmm (123) mp-1216532 [hull=0.209]
- papers: Enhanced Thermoelectric Properties of Variants of Tl9SbTe6and Tl9BiTe6 | Thermoelectric properties of TlBiTe2 | Thermoelectric properties of Tl9BiTe6

## Ca-Sb-Zn
- rank 265 | 27 samples | 11 papers | 17 compositions
- compositions: CaZn2Sb2 (9); Ca9Zn4.5Sb9 (2); Ca9Zn4.6Sb9 (2); Eu0.01Ca0.99Zn2Sb2 (1); Ca1Zn2Sb2 (1); Eu0.2Ca0.8Zn2Sb2 (1)
- dopant candidates (<5% at.): Cu (4), Eu (3), Al (1)
- seed hypothesis (confirm): caal2si2_zintl, zintl_9_4_9  <-- MIXED, split per composition
- measured range: 293-874 K (5th-95th pct of 112 curves; full span incl. outliers 16-876 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca(ZnSb)2 P-3m1 (164) mp-7429 [hull=0.000, icsd=1, PRIMARY]; Ca21(Zn2Sb9)2 C2/m (12) mp-1194667 [hull=0.000, icsd=1, PRIMARY]; Ca9Zn4Sb9 Pbam (55) mp-21594 [hull=0.000, icsd=1, PRIMARY]; Ca2ZnSb2 Pm (6) mp-1227973 [hull=0.014, PRIMARY]
- papers: Zintl Phases as Thermoelectric Materials: Tuned Transport Properties of the Compounds CaxYb1-xZn2Sb2 | Enhanced Thermoelectric Properties in Zinc Antimonides | Electronic structure and transport in thermoelectric compounds AZn2Sb2 (A = Sr, Ca, Yb, Eu)

## Co-Fe-Si
- rank 266 | 27 samples | 6 papers | 20 compositions
- compositions: Co2FeSi (5); Fe0.2Co0.8Si (3); Fe0.6Co0.4Si (2); Fe0.1Co0.9Si (1); Co2FeSi  (1); Fe0.8Co0.2Si (1)
- seed hypothesis (confirm): full_heusler, b20_fesi  <-- MIXED, split per composition
- measured range: 10-1015 K (5th-95th pct of 18 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeCo2Si Fm-3m (225) mp-1065751 [hull=0.000, icsd=3, PRIMARY]; FeCoSi Pnma (62) mp-1102660 [hull=0.064, icsd=1, PRIMARY]; Fe2CoSi F-43m (216) mp-1207117 [hull=0.000, PRIMARY]; Fe3Co3Si2 R3m (160) mp-1225227 [hull=0.000, PRIMARY]; FeCoSi2 P2_1 (4) mp-1224983 [hull=0.020, PRIMARY]
- papers: Filling dependence of thermoelectric power in transition-metal monosilicides | Structural and Thermoelectric Properties of Ternary Full-Heusler Alloys | Quantum phase transition and non-Fermi liquid behavior in Fe<sub>1−<i>x</i></sub>Co<sub><i>x</i></sub>Si (<i>x</i>⩾ 0.7)

## Co-Ni-Sb
- rank 267 | 27 samples | 9 papers | 18 compositions
- compositions: Co0.8Sb2.4Ni0.2Sb0.2 (5); Ce0.3Ni1.5Co2.5Sb12 (4); Co0.8Ni0.2Sb3 (2); Co7.3Ni2.7Sb30 (2); Co7.2Ni2.8Sb30 (1); Co0.79Ni0.21Sb2.88Sn0.12 (1)
- dopant candidates (<5% at.): Ce (5), Sn (1)
- seed hypothesis (confirm): skutterudite
- measured range: 26-886 K (5th-95th pct of 83 curves; full span incl. outliers 23-948 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co4NiSb12 Im-3 (204) mp-1106327 [hull=0.159, icsd=1, PRIMARY]; Co3NiSb12 R-3 (148) mp-1226458 [hull=0.004, PRIMARY]; CoNiSb P6_3/mmc (194) mp-1025009 [hull=0.217, PRIMARY]; CoNiSb6 C2/m (12) mp-1226120 [hull=0.009, PRIMARY]; CoNiSb P3m1 (156) mp-1226172 [hull=0.237]
- papers: Enhanced thermoelectric properties of Co1−x−y Ni x+y Sb3−x Sn x materials | Nanostructured Co1−xNixSb3 skutterudites: Synthesis, thermoelectric properties, and theoretical modeling | Effect of NiSb on the thermoelectric properties of skutterudite CoSb3

## Co-Sb-Sn-Zr
- rank 268 | 27 samples | 11 papers | 12 compositions
- compositions: ZrCoSb0.8Sn0.2 (14); ZrCoSb0.7Sn0.3 (3); Zr0.85Ti0.15CoSn0.3Sb0.7 (1); Zr0.95Ti0.05CoSn0.3Sb0.7 (1); Hf0.15Zr0.85CoSb0.8Sn0.2 (1); ZrCo1.03Sb0.8Sn0.2 (1)
- dopant candidates (<5% at.): Ti (2), Hf (1), Pt (1)
- measured range: 38-981 K (5th-95th pct of 101 curves; full span incl. outliers 21-1127 K)
- papers: Thermoelectric properties of p-type half-Heusler alloys Zr1−xTixCoSnySb1−y (0.0<x<0.5; y=0.15 and 0.3) | Enhanced thermoelectric performance in the p-type half-Heusler (Ti/Zr/Hf)CoSb0.8Sn0.2 system via phase separation | Investigating the thermoelectric properties of p-type half-Heusler Hfx(ZrTi)1−xCoSb0.8Sn0.2 by reducing Hf concentration for power generation

## Cr-O-Y
- rank 269 | 27 samples | 5 papers | 12 compositions
- compositions: Y0.8Ca0.2CrO3 (6); Y0.8Ca0.2Cr0.9Co0.1O3 (4); Y0.8Ca0.2Cr0.8Co0.2O3 (2); YCrO3 (2); Y0.8Ca0.2Cr0.85Ni0.15O3 (2); Y0.8Ca0.2Cr0.9Ni0.1O3 (2)
- dopant candidates (<5% at.): Ca (22), Co (6), Ni (4), Mn (3), Cu (2), Fe (2), Sr (2)
- seed hypothesis (confirm): perovskite
- measured range: 25-1663 K (5th-95th pct of 30 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YCrO4 I4_1/amd (141) mp-18825 [hull=0.000, icsd=3, PRIMARY]; YCrO3 Pnma (62) mp-18725 [hull=0.000, icsd=3, PRIMARY]; YCrO5 P2_1/c (14) mp-1204332 [hull=0.087, icsd=1, PRIMARY]; Y3LuCr4O16 P-4m2 (115) mp-1216164 [hull=0.008, PRIMARY]; YCr2O2 I4_1/amd (141) mp-1208171 [hull=1.045, PRIMARY]
- papers: Calcium- and Cobalt-Doped Yttrium Chromites as an Interconnect Material for Solid Oxide Fuel Cells | Electrical conductivity anomaly and X-ray photoelectron spectroscopy investigation of YCr<sub>1−</sub><sub><i>x</i></sub>Mn<sub><i>x</i></sub>O<sub>3</sub> negative temperature coefficient ceramics | Effect of nickel substitution on defect chemistry, electrical properties, and dimensional stability of calcium-doped yttrium chromite

## Fe-Se-Te
- rank 270 | 27 samples | 7 papers | 17 compositions
- compositions: FeSe0.6Te0.4 (5); FeSe0.9Te0.1 (3); FeSe0.8Te0.2 (3); FeSe0.7Te0.3 (3); Fe1.01Te0.62Se0.38 (1); Fe1.14Te0.7Se0.3 (1)
- seed hypothesis (confirm): fese_pbo
- solid-solution axis: Se/(Se+Te) spans 0.11-0.90 (median 0.50) over 17 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-300 K (5th-95th pct of 31 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe2TeSe P4mm (99) mp-1225136 [hull=0.076, PRIMARY]; Fe3Te2Se P4mm (99) mp-1225183 [hull=0.070, PRIMARY]; Fe4Te3Se I4mm (107) mp-1224987 [hull=0.071, PRIMARY, AMBIGUOUS]; Fe4TeSe3 Amm2 (38) mp-1225054 [hull=0.014, PRIMARY]; Fe4Te3Se P4mm (99) mp-1225000 [hull=0.073]
- papers: Magnetothermoelectric effects in <mml:math altimg=\"si8.gif\" overflow=\"scroll\" xmlns:xocs=\"http://www.elsevier.com/xml/xocs/dtd\" xmlns:xs=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns=\"http://www.elsevier.com/xml/ja/dtd\" xmlns:ja=\"http://www.elsevier.com/xml/ja/dtd\" xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" xmlns:tb=\"http://www.elsevier.com/xml/common/table/dtd\" xmlns:sb=\"http://www.elsevier.com/xml/common/struct-bib/dtd\" xmlns:ce=\"http://www.elsevier.com/xml/common/dtd\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" xmlns:cals=\"http://www.elsevier.com/xml/common/cals/dtd\"><mml:mrow><mml:msub><mml:mrow><mml:mtext>Fe</mml:mtext></mml:mrow><mml:mrow><mml:mn>1</mml:mn><mml:mo>+</mml:mo><mml:mi>d</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mrow><mml:mtext>Te</mml:mtext></mml:mrow><mml:mrow><mml:mn>1</mml:mn><mml:mo>-</mml:mo><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mrow><mml:mtext>Se</mml:mtext></mml:mrow><mml:mrow><mml:mi>x</mml:mi></mml:mrow></mml:msub></mml:mrow></mml:math> | Normal state above the upper critical field in \nFe1+yTe1−x(Se,S)x | Magnetotransport properties and Seebeck effect in the superconductor <i>FeSe</i><sub>0.5</sub><i>Te</i><sub>0.5</sub>

## Mo-S
- rank 271 | 27 samples | 8 papers | 7 compositions
- compositions: MoS2 (17); V0.05MoS2 (2); V0.1MoS2 (2); V0.01MoS2 (2); V0.02MoS2 (2); MoS2Cu0.065 (1)
- dopant candidates (<5% at.): V (8), Cu (2)
- seed hypothesis (confirm): mos2_2h
- measured range: 84-1003 K (5th-95th pct of 80 curves; full span incl. outliers 10-1010 K)
- [ref 1] TEDesignLab / ICSD: Mo2S3 P2_1/m (11) mp-1627 [hull=0.094, icsd=7, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: MoS2 P6_3/mmc (194) mp-2815 [hull=0.000, icsd=12, PRIMARY]; Mo3S4 R-3 (148) mp-2164 [hull=0.066, icsd=9, PRIMARY]; Mo15S19 P6_3/m (176) mp-31257 [hull=0.084, icsd=2, PRIMARY]; InMo12PbS16 R-3 (148) mp-1223724 [hull=0.044, PRIMARY]; AgMo12PbS16 R-3 (148) mp-1229112 [hull=0.059, PRIMARY]
- papers: Thermal conductivity of bulk and monolayer MoS2 | A thin film efficient pn-junction thermoelectric device fabricated by self-align shadow mask | Thermoelectric performance of Cu-doped MoS2 layered nanosheets for low grade waste heat recovery

## N-Ta
- rank 272 | 27 samples | 7 papers | 20 compositions
- compositions: TaN (3); TaN1.35 (3); TaN0.89 (3); Ta3N5 (2); Ta0.932Si0.068N0.56 (1); Ta0.955Si0.045N0.56 (1)
- dopant candidates (<5% at.): Si (2), Ag (1), O (1)
- seed hypothesis (confirm): rocksalt_nitride_carbide
- measured range: 10-373 K (5th-95th pct of 24 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TaN Fm-3m (225) mp-251 [hull=0.327, icsd=13, PRIMARY]; Ta5N6 P6_3/mcm (193) mp-1642 [hull=0.000, icsd=4, PRIMARY]; Ta3N5 Cmcm (63) mp-27488 [hull=0.000, icsd=3, PRIMARY]; Ta2N P-31m (162) mp-1079438 [hull=0.000, icsd=2, PRIMARY]; TaN2 P6_3/mmc (194) mp-1019272 [hull=0.438, icsd=1, PRIMARY, AMBIGUOUS]
- papers: Electrical transport properties of polycrystalline TaN1- films | Electrical and optical properties of Ta-Si-N thin films deposited by reactive magnetron sputtering | Mechanism and control of the metal-to-insulator transition in rocksalt tantalum nitride

## Te-Tl
- rank 273 | 27 samples | 10 papers | 22 compositions
- compositions: Tl2Te (4); TlTe (3); Tl9.75Gd0.25Te6 (1); Tl9.32Gd0.68Te6 (1); Tl9.5La0.5Te6 (1); Tl9.25La0.75Te6 (1)
- dopant candidates (<5% at.): Sn (5), Bi (5), Gd (3), La (2)
- seed hypothesis (confirm): tl5te3
- measured range: 295-1066 K (5th-95th pct of 93 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TlTe I4/mcm (140) mp-2081 [hull=0.000, icsd=9, PRIMARY]; Tl5Te3 I4/mcm (140) mp-174 [hull=0.005, icsd=5, PRIMARY]; Tl2Te3 C2/c (15) mp-29711 [hull=0.000, icsd=1, PRIMARY]; Tl5Te3 I-4 (82) mp-1796 [hull=0.140, icsd=3]; Tl2Te3 Cc (9) mp-680731 [hull=0.024, icsd=1]
- papers: Crystal structures and thermoelectric properties of the series Tl10−xLaxTe6with 0.2 ≤ x ≤ 1.15 | Thermoelectric properties of Tl10−xLnxTe6, with Ln=Ce, Pr, Nd, Sm, Gd, Tb, Dy, Ho and Er, and 0.25⩽x⩽1.32 | Thermoelectric Properties of Liquid Semiconductor Solutions of Thallium and Tellurium

## Ag-Cu-In-Te
- rank 274 | 26 samples | 4 papers | 19 compositions
- compositions: Cu0.75Ag0.2InTe2 (3); Cu0.68Ag0.3InTe2 (2); Cu0.4Ag0.6InTe2 (2); Cu0.8Ag0.2InTe2 (2); Cu0.6Ag0.4InTe2 (2); Cu0.2Ag0.8InTe2 (2)
- dopant candidates (<5% at.): Ga (1)
- seed hypothesis (confirm): chalcopyrite
- solid-solution axis: Ag/(Ag+Cu) spans 0.18-0.80 (median 0.20) over 19 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 297-851 K (5th-95th pct of 115 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): In2CuAgTe4 I-4 (82) mp-1224246 [hull=0.010, PRIMARY]; In4Cu3AgTe8 P1 (1) mp-1226859 [hull=0.006, PRIMARY]; In4CuAg3Te8 P-4 (81) mp-1224343 [hull=0.010, PRIMARY]
- papers: High-Performance Pseudocubic Thermoelectric Materials from Non-cubic Chalcopyrite Compounds | Thermoelectric performance of Cu1−x−δAgxInTe2 diamond-like materials with a pseudocubic crystal structure | Ultralow thermal conductivity in diamondoid lattices: high thermoelectric performance in chalcopyrite Cu0.8+yAg0.2In1−yTe2

## B-Mg
- rank 275 | 26 samples | 10 papers | 9 compositions
- compositions: MgB2 (15); (MgB2)1.9Co0.1 (4); Mg7.0B100 (1); Mg7.5B99 (1); Mg6.9B98 (1); Mg7.7B100 (1)
- dopant candidates (<5% at.): Co (4), Ti (1), Si (1), C (1)
- seed hypothesis (confirm): alb2
- measured range: 10-300 K (5th-95th pct of 32 curves; full span incl. outliers 10-876 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MgB2 P6/mmm (191) mp-763 [hull=0.000, icsd=29, PRIMARY]; MgB4 Pnma (62) mp-365 [hull=0.000, icsd=1, PRIMARY]; MgB7 Imma (74) mp-978275 [hull=0.000, icsd=1, PRIMARY]; LiMg9B20 P-1 (2) mp-35040 [hull=0.013, PRIMARY]; Mg7B P-6m2 (187) mp-1016262 [hull=0.384, PRIMARY]
- papers: [] | Co-addition into MgB2: The structural and electronic properties of (MgB2)2−xCox | Studies of transport properties of MgB2 superconductor

## Cu-O-Sr
- rank 276 | 26 samples | 9 papers | 17 compositions
- compositions: Sr0.875Nd0.125CuO2 (4); Sr0.9La0.1CuO2 (4); Sr2CuO3 (4); (In0.2Pb0.55Cu0.25)Sr2(Ca0.5Y0.5)Cu2O7 (1); Sr0.90La0.10CuO2 (1); Sr0.88La0.12CuO2 (1)
- dopant candidates (<5% at.): La (7), Eu (5), Nd (4), Na (3), Pb (1), Ca (1), Y (1), In (1)
- seed hypothesis (confirm): cuprate_chain, infinite_layer_cuprate  <-- MIXED, split per composition
- measured range: 11-304 K (5th-95th pct of 28 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2CuO3 Immm (71) mp-5456 [hull=0.000, icsd=9, PRIMARY]; SrCuO2 Cmcm (63) mp-5787 [hull=0.000, icsd=6, PRIMARY]; SrCu2O3 Cmmm (65) mp-5938 [hull=0.017, icsd=3, PRIMARY]; Sr2Cu2O3 Fmmm (69) mp-8806 [hull=0.549, icsd=2, PRIMARY]; Sr2Cu3O5 Immm (71) mp-5700 [hull=0.059, icsd=2, PRIMARY]
- papers: Superconductivity in Pb-based 1212 cuprates; evidence for under-doping from thermoelectric power | Superconducting Sr0.875Nd0.125CuO2−δthin films | Structural, electrical and magnetic studies of infinite-layered Sr1−xLaxCuO2 superconductor

## Cu-Yb
- rank 277 | 26 samples | 2 papers | 3 compositions
- compositions: YbCu4.5 (24); YbCu5 (1); YbCu4.75Ag0.25 (1)
- dopant candidates (<5% at.): Ag (1)
- seed hypothesis (confirm): cacu5
- measured range: 10-297 K (5th-95th pct of 46 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbCu Pnma (62) mp-1937 [hull=0.000, icsd=3, PRIMARY]; YbCu5 P6/mmm (191) mp-1607 [hull=0.000, icsd=3, PRIMARY]; Yb6Cu23 Fm-3m (225) mp-1193632 [hull=0.041, icsd=1, PRIMARY]; YbCu2 P6_3/mmc (194) mp-1103426 [hull=0.024, icsd=1, PRIMARY]; Yb3Cu Pm-3m (221) mp-1187968 [hull=0.224, PRIMARY]
- papers: Resistivity and thermoelectric power of YbCu4.5 under very high pressure | Thermoelectric power of heavy-fermion system

## Fe-La-Ni-O
- rank 278 | 26 samples | 10 papers | 23 compositions
- compositions: LaNi0.6Fe0.4O3 (4); LaNi0.60Fe0.40O3 (1); LaNi0.40Fe0.60O3 (1); LaFe0.6Ni0.4O3 (1); LaFe0.5Ni0.5O3 (1); LaFe0.4Ni0.6O3 (1)
- dopant candidates (<5% at.): Sr (4), Mn (3), Ga (1), Cr (1)
- measured range: 19-1279 K (5th-95th pct of 31 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2FeNiO6 P2_1/c (14) mp-1223335 [hull=0.000, PRIMARY]; La4Fe(NiO4)3 P-1 (2) mp-1223166 [hull=0.002, PRIMARY]; La4Fe(NiO5)2 I4mm (107) mp-1223077 [hull=0.065, PRIMARY]; La4Fe3NiO12 P-1 (2) mp-1223185 [hull=0.000, PRIMARY]; La5Fe4NiO15 C2/m (12) mp-1223413 [hull=0.007, PRIMARY]
- papers: Electrical, Thermoelectric, and Structural Properties of La(M[sub x]Fe[sub 1−x])O[sub 3] (M=Mn, Ni, Cu) | Power factor of La1−xSrxFeO3 and LaFe1−yNiyO3 | Electrical properties of A∕B-site substituted Ni-deficient La(Ni0.6Fe0.3)O3 perovskites with A=Ag+, Pb2+, Nd3+ and B=Mn3+, Ga3+

## K-O-Rh
- rank 279 | 26 samples | 2 papers | 2 compositions
- compositions: K0.87RhO2 (24); K0.63RhO2 (2)
- seed hypothesis (confirm): naxcoo2_layered
- measured range: 10-376 K (5th-95th pct of 26 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): K2Rh2O5 P4/mmm (123) mp-867920 [hull=0.000, PRIMARY]; KRhO3 Pm-3m (221) mp-975134 [hull=0.050, PRIMARY]
- papers: Structure and physical properties of K0.63RhO2 single crystals | Enhanced thermoelectric performance in K0.87RhO2 thin films induced by changing ambient gases during pulsed laser deposition

## Mg
- rank 280 | 26 samples | 5 papers | 23 compositions
- compositions: Mg (3); Mg97Zn1Gd2 (2); Mg2.10(Si0.3Sn0.7)0.03Ga0.07 (1); Mg2.10(Si0.3Sn0.7)0.08Ga0.02 (1); Mg2.10(Si0.3Sn0.7)0.05Ga0.05 (1); Mg96Zn2Y2 (1)
- dopant candidates (<5% at.): Zn (13), Sn (10), Ga (4), Si (4), Al (3), Y (2), Gd (2)
- seed hypothesis (confirm): solid_solution_alloy
- measured range: 298-801 K (5th-95th pct of 42 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg P6_3/mmc (194) mp-153 [hull=0.010, icsd=19, PRIMARY]; BaMg149 P-6m2 (187) mp-1184337 [hull=0.000, PRIMARY]; AcMg149 P-6m2 (187) mp-1184231 [hull=0.000, PRIMARY]; CaMg149 P-6m2 (187) mp-1184449 [hull=0.000, PRIMARY]; CsMg149 P-6m2 (187) mp-978251 [hull=0.027, PRIMARY]
- papers: Enhanced hole concentration through Ga doping and excess of Mg and thermoelectric properties of p-type Mg2(1+z)(Si0.3Sn0.7)1−yGay | Thermal diffusivity and thermal conductivity of Mg–Zn–rare earth element alloys with long-period stacking ordered phase | Thermal conductivity of as-cast and as-extruded binary Mg–Al alloys

## Ag-Sb-Se-Te
- rank 281 | 25 samples | 5 papers | 21 compositions
- compositions: Cu0.2Ag2.8SbSeTe2 (4); AgSbSe1.25Te0.75 (2); Ag3SbSeTe2 (1); Cu0.1Ag2.9SbSeTe2 (1); AgSbSe1.75Te0.25 (1); AgSbSe1.5Te0.5 (1)
- dopant candidates (<5% at.): Cu (5)
- solid-solution axis: Se/(Se+Te) spans 0.10-0.88 (median 0.33) over 21 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 299-699 K (5th-95th pct of 71 curves; full span incl. outliers 10-702 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AgSbTeSe P4/mmm (123) mp-1229007 [hull=0.470, PRIMARY]
- papers: Influence of Doping on Structural and Thermoelectric Properties of AgSbSe2 | Glassy thermal conductivity in the two-phase CuxAg3−xSbSeTe2alloy and high temperature thermoelectric behavior | Structural and thermoelectric properties ofAgSbTe2-AgSbSe2pseudobinary system

## Ba-Cu-La-O
- rank 282 | 25 samples | 2 papers | 13 compositions
- compositions: Y0.38La0.62(Ba0.88La0.12)2Cu3O7 (3); Y0.38La0.62(Ba0.4La0.6)2Cu3O7 (3); (Ca0.1La0.9)(Ba1.65La0.35)Cu3O7.20 (2); (Ca0.1La0.9)(Ba1.65La0.35)Cu3O7.03 (2); (Ca0.1La0.9)(Ba1.65La0.35)Cu3O7.00 (2); (Ca0.1La0.9)(Ba1.65La0.35)Cu3O7.10 (2)
- dopant candidates (<5% at.): Ca (13), Y (12)
- seed hypothesis (confirm): ybco_cuprate
- measured range: 10-394 K (5th-95th pct of 23 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2LaCu3O7 Pmmm (47) mp-622210 [hull=0.019, icsd=1, PRIMARY]; Ba2La(CuO2)3 P4/mmm (123) mp-1228413 [hull=0.004, PRIMARY]; Ba3La3(Cu3O7)2 Fmm2 (42) mp-1228365 [hull=0.026, PRIMARY]; Ba4La2Cu6O13 Fmmm (69) mp-1228239 [hull=0.007, PRIMARY]; Ba2LaCu3O7 P4mm (99) mp-1228519 [hull=0.068]
- papers: A direct correlation between Tc and EDOS for 1-2-3 type (Ca0.1La0.9)(Ba1.65La0.35)Cu3Oy superconductor | Metallic state in La-doped YBa<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:msub><mml:mrow /><mml:mn>2</mml:mn></mml:msub></mml:math>Cu<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:msub><mml:mrow /><mml:mn>3</mml:mn></mml:msub></mml:math>O<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:msub><mml:mrow /><mml:mi>y</mml:mi></mml:msub></mml:math>thin films with<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mi>n</mml:mi></mml:math>-type charge carriers

## Ba-Cu-Nd-O
- rank 283 | 25 samples | 7 papers | 10 compositions
- compositions: NdBa2Cu3O7 (11); NdBa1.9La0.1Cu3O7 (2); NdBa1.8La0.2Cu3O7 (2); NdBa1.85La0.15Cu3O7 (2); NdBa1.7La0.3Cu3O7 (2); NdBa1.95La0.05Cu3O7 (2)
- dopant candidates (<5% at.): La (10), Pr (3), Y (1)
- seed hypothesis (confirm): ybco_cuprate
- measured range: 17-301 K (5th-95th pct of 27 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaNd2CuO5 P4/mbm (127) mp-6704 [hull=0.024, icsd=6, PRIMARY]; Ba2NdCu3O7 Pmmm (47) mp-22719 [hull=0.015, icsd=2, PRIMARY]; Ba2Nd(CuO2)3 P4/mmm (123) mp-614981 [hull=0.000, icsd=1, PRIMARY]; Ba3Nd3(Cu3O7)2 Fmm2 (42) mp-1228353 [hull=0.046, PRIMARY]; Ba4Nd2Cu6NiO15 Imm2 (44) mp-1228702 [hull=0.057, PRIMARY]
- papers: A study on the thermoelectric power and thermal conductivity properties of the Y1−xNdxBa2Cu3O7−δ system | Normal state transport properties in superconducting oxides RBa2Cu3O7- delta(R=Y, Gd, Sm, Nd, and Dy) | The normal state transport properties of NdBa2−xLaxCu3O7−δ: Evidence of localization hole by La

## Ba-Ga-Si
- rank 284 | 25 samples | 10 papers | 21 compositions
- compositions: Ba8Ga16Si30 (5); Ba7.81Ga15.72Si29.83 (1); Ba8.01Ga16.61Si28.93 (1); Ba7.93Ga17.13Si28.72 (1); Ba8Si30.5Ga15.5 (1); Ba7.75Yb0.25Si31.9Ga14.1 (1)
- dopant candidates (<5% at.): Eu (5), Au (2), Yb (1), Zn (1), Cu (1)
- seed hypothesis (confirm): clathrate_i
- measured range: 14-1000 K (5th-95th pct of 71 curves; full span incl. outliers 12-1271 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba4Ga3Si20 Pm-3n (223) mp-1214507 [hull=0.005, PRIMARY]; BaGaSi P-6m2 (187) mp-1227940 [hull=0.000, PRIMARY]
- papers: Synthesis and high temperature thermoelectric transport properties of Si-based type-I clathrates | Influence of sintering temperature on the thermoelectric properties of Ba8Ga16Si30 clathrate treated by spark plasma sintering | Synthesis and thermoelectric properties of rare earth Yb-doped Ba8−xYbxSi30Ga16 clathrates

## Bi-S-Se
- rank 285 | 25 samples | 7 papers | 22 compositions
- compositions: Bi2SeS2 (3); Bi2SeS2(CuI)0.02 (2); (Bi2S2.25Se0.75)0.995(BiCl3)0.005 (1); Cu0.005Bi2SeS2 (1); Cu0.01Bi2SeS2 (1); (Bi2S2.70Se0.30)0.995(BiCl3)0.005 (1)
- dopant candidates (<5% at.): Cu (11), Cl (6), I (5), Br (2), Ag (2)
- seed hypothesis (confirm): stibnite
- solid-solution axis: S/(S+Se) spans 0.33-0.90 (median 0.67) over 22 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 51-775 K (5th-95th pct of 126 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi2Se2S Pnma (62) mp-1227504 [hull=0.022, PRIMARY]; Bi4(SeS)3 Pmc2_1 (26) mp-1227512 [hull=0.020, PRIMARY]
- papers: Tellurium-Free Thermoelectric: The Anisotropic n-Type Semiconductor Bi2S3 | Thermoelectric property studies on Cu x Bi 2 SeS 2  with nano-scale precipitates Bi 2 S 3 | Fabrication and properties of Bi2S3−xSex thermoelectric polycrystals

## C-Co-Sn
- rank 286 | 25 samples | 3 papers | 19 compositions
- compositions: SnCCo3 (5); Sn0.9Sb0.1CCo3 (2); Sn0.9Co0.1CCo3 (2); Sn0.95Sb0.05CCo3 (1); Sn0.95Co0.05CCo3 (1); Sn0.95Ag0.05CCo3 (1)
- dopant candidates (<5% at.): Ag (4), In (4), Sb (3), Pb (3), Ge (3)
- seed hypothesis (confirm): antiperovskite
- measured range: 10-350 K (5th-95th pct of 79 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co3SnC Pm-3m (221) mp-20679 [hull=0.058, icsd=1, PRIMARY]
- papers: Thermoelectric properties of metallic antiperovskites AXD3 (A=Ge, Sn, Pb, Al, Zn, Ga; X=N, C; D=Ca, Fe, Co) | Good Thermoelectric Performance in Strongly Correlated System SnCCo3with Antiperovskite Structure | Role of chemical doping on the enhancement of thermoelectric performance in metal-based thermoelectric system SnCCo 3

## Co-Hf-Sb-Zr
- rank 287 | 25 samples | 8 papers | 18 compositions
- compositions: Hf0.5Zr0.5CoSb0.85Sn0.15 (4); Zr0.5Hf0.5CoSb0.99Sn0.01 (3); Zr0.5Hf0.5CoSb0.9Sn0.1 (2); Zr0.5Hf0.5Co0.9Ir0.1Sb0.99Sn0.01 (2); Zr0.5Hf0.5Co0.9Rh0.1Sb0.99Sn0.01 (1); Zr0.50Hf0.50CoSb0.9Sn0.1 (1)
- dopant candidates (<5% at.): Sn (19), Nb (5), Ir (2), Rh (1), Mn (1)
- solid-solution axis: Hf/(Hf+Zr) spans 0.20-0.80 (median 0.50) over 18 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 300-1172 K (5th-95th pct of 103 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HfZr(CoSb)2 R3m (160) mp-1224254 [hull=0.660, PRIMARY]
- papers: Effects of Rh on the thermoelectric performance of the p-type Zr0.5Hf0.5Co1−xRhxSb0.99Sn0.01 half-Heusler alloys | (Zr,Hf)Co(Sb,Sn) half-Heusler phases as high-temperature (>700°C) p-type thermoelectric materials | Effects of Ir Substitution and Processing Conditions on Thermoelectric Performance of p-Type Zr0.5Hf0.5Co1−x Ir x Sb0.99Sn0.01 Half-Heusler Alloys

## Co-Sb-V
- rank 288 | 25 samples | 4 papers | 12 compositions
- compositions: CoVSb (8); VCoSb (7); VCoSb0.98Sn0.02 (1); V0.98Ti0.02CoSb (1); V0.95CoSb (1); V0.9CoSb (1)
- dopant candidates (<5% at.): Ti (3), Sn (1)
- seed hypothesis (confirm): half_heusler
- measured range: 12-978 K (5th-95th pct of 94 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): VCoSb F-43m (216) mp-4076 [hull=0.005, icsd=5, PRIMARY]; VCoSb P6_3/mmc (194) mp-1216413 [hull=0.521]
- papers: Synthesis and thermoelectric properties of n-type half-Heusler compound VCoSb with valence electron count of 19 | Improving the Thermoelectric Properties of the Half-Heusler Compound VCoSb by Vanadium Vacancy | Titanium Doping to Enhance Thermoelectric Performance of 19‐Electron VCoSb Half‐Heusler Compounds with Vanadium Vacancies

## Co-Sc-Zr
- rank 289 | 25 samples | 1 papers | 1 compositions
- compositions: ScZrCo (25)
- measured range: 18-298 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZrScCo2 Fm-3m (225) mp-1188031 [hull=0.000, PRIMARY]; ZrScCo2 Immm (71) mp-1097476 [hull=3.087]
- papers: Pressure induced superconductivity in the compound ScZrCo

## Cr-Cu-S
- rank 290 | 25 samples | 6 papers | 8 compositions
- compositions: CuCrS2 (17); Cu0.9CrS2 (2); CuCrS2.00 (1); CuCrS2.01 (1); CuCrS2.02 (1); CuCrS2.10 (1)
- dopant candidates (<5% at.): Sb (2)
- seed hypothesis (confirm): cucrs2_layered
- measured range: 16-915 K (5th-95th pct of 81 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cr2CuS4 Fd-3m (227) mp-22803 [hull=0.000, icsd=16, PRIMARY]; CrCuS2 R3m (160) mp-5862 [hull=0.039, icsd=4, PRIMARY]; Cr8Cu3NiS16 R3m (160) mp-1226091 [hull=0.000, PRIMARY]; CrCuS4 P2_1/c (14) mp-1226309 [hull=0.008, PRIMARY]; MnCr8Cu3S16 R3m (160) mp-1221752 [hull=0.000, PRIMARY, AMBIGUOUS]
- papers: Thermoelectric Properties of Layer-Antiferromagnet CuCrS2 | Ordered-Defect Sulfides as Thermoelectric Materials | Thermoelectric properties of p-type semiconductors copper chromium disulfide CuCrS2+x

## Cr-Sb
- rank 291 | 25 samples | 6 papers | 20 compositions
- compositions: CrSb2 (6); Cr0.97Mn0.03Sb2 (1); Cr0.95Mn0.05Sb2 (1); Cr0.99Mn0.01Sb2 (1); CrSb1.99Sn0.01 (1); CrSb1.97Sn0.03 (1)
- dopant candidates (<5% at.): Te (5), Mn (3), Sn (3), Ti (3), Ni (3), Ru (2)
- seed hypothesis (confirm): marcasite
- measured range: 10-316 K (5th-95th pct of 83 curves; full span incl. outliers 10-629 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CrSb2 Pnnm (58) mp-22498 [hull=0.093, icsd=9, PRIMARY]; CrSb P6_3/mmc (194) mp-1641 [hull=0.094, icsd=9, PRIMARY]; CrSb2 I4/mcm (140) mp-2666 [hull=0.139, icsd=2]
- papers: Transport and thermoelectric properties of Cr1−xMnxSb2 at low temperatures | The effect of Sn substitution for Sb on transport and thermoelectric properties of CrSb2 at low temperatures | The effect of Ti substitution for Cr on transport and thermoelectric properties of CrSb2 at low temperatures

## Ge-Sb-Sn-Te
- rank 292 | 25 samples | 5 papers | 18 compositions
- compositions: (Ge0.5Sn0.5Te)4Sb2Te3 (3); (Ge0.5Sn0.5Te)7Sb2Te3 (3); (Ge0.5Sn0.5Te)12Sb2Te3 (3); Sn0.57Sb0.13Ge0.3Te (2); Ge1.3Sn0.7Sb2Te5 (1); GeSnSb2Te5 (1)
- dopant candidates (<5% at.): Bi (4)
- seed hypothesis (confirm): gst_homologous
- solid-solution axis: Ge/(Ge+Sn) spans 0.13-0.88 (median 0.50) over 18 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 75-810 K (5th-95th pct of 83 curves; full span incl. outliers 19-812 K)
  !! MEASUREMENT CROSSES A TRANSITION: gst_homologous -> rocksalt at ~420 K (Amorphous -> metastable cubic, ~420 K; cubic -> stable layered above ~500 K.)
     Record each phase with its own temperature range, not a single prototype.
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sn2Ge5(SbTe5)2 R3m (160) mp-1219061 [hull=0.297, PRIMARY]; Sn5Ge2(SbTe5)2 R3m (160) mp-1219067 [hull=0.293, PRIMARY]
- papers: Layered germanium tin antimony tellurides: element distribution, nanostructures and thermoelectric properties | Nanostructured rocksalt-type solid solution series (Ge1−xSnxTe)nSb2Te3 (n=4, 7, 12; 0≤x≤1): Thermal behavior and thermoelectric properties | Effects of Sn Substitution on Thermoelectric Properties of Ge4SbTe5

## Hf-Te
- rank 293 | 25 samples | 5 papers | 11 compositions
- compositions: HfTe5 (14); HfTe4.75Se0.25 (2); Hf0.95Ti0.05Te5 (1); Hf0.75Ce0.25Te5 (1); Hf0.75Pr0.25Te5 (1); Hf0.75Nd0.25Te5 (1)
- dopant candidates (<5% at.): Se (2), Ti (1), Ce (1), Pr (1), Nd (1), Gd (1), Sm (1), Tb (1), Dy (1), Ho (1)
- seed hypothesis (confirm): zrte5_hfte5
- measured range: 10-374 K (5th-95th pct of 32 curves)
- [ref 1] TEDesignLab / ICSD: HfTe5 Cmcm (63) mp-1168 [hull=0.000, icsd=5, PRIMARY]; HfTe2 P-3m1 (164) mp-32887 [hull=0.000, icsd=3, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: HfTe3 P2_1/m (11) mp-1025459 [hull=0.015, icsd=2, PRIMARY]; Hf3Te2 I4/mmm (139) mp-28919 [hull=0.000, icsd=1, PRIMARY]; Hf5Te4 I4/m (87) mp-12884 [hull=0.000, icsd=1, PRIMARY]; Hf3TiTe20 Amm2 (38) mp-1224556 [hull=0.000, PRIMARY]
- papers: Effect of Ti substitution on the thermoelectric properties of the pentatelluride materials M1−xTixTe5 (M=Hf, Zr) | Thermoelectric power of HfTe5 and ZrTe5 | Enhancement of the power factor of the transition metal pentatelluride HfTe5 by rare-earth doping

## Nb-Se
- rank 294 | 25 samples | 4 papers | 3 compositions
- compositions: NbSe2 (17); Cr0.0009NbSe2 (7); NbSe3 (1)
- dopant candidates (<5% at.): Cr (7)
- seed hypothesis (confirm): mos2_2h, nbse3_chain  <-- MIXED, split per composition
- measured range: 10-360 K (5th-95th pct of 26 curves)
- [ref 1] TEDesignLab / ICSD: NbSe2 P6_3/mmc (194) mp-1072113 [hull=0.001, icsd=12, PRIMARY]; Nb2Se3 P2_1/m (11) mp-2330 [hull=0.017, icsd=2, PRIMARY]; NbSe2 P-6m2 (187) mp-643063 [hull=0.016, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: NbSe3 P2_1/m (11) mp-525 [hull=0.000, icsd=5, PRIMARY]; Nb3Se4 P6_3/m (176) mp-561 [hull=0.000, icsd=3, PRIMARY]; Nb5Se4 I4/m (87) mp-15837 [hull=0.006, icsd=2, PRIMARY]; Nb2Se C2/m (12) mp-27793 [hull=0.000, icsd=1, PRIMARY]; NbSe2 Fmm2 (42) mp-7007 [hull=0.004, icsd=1]
- papers: Chemically exfoliated transition metal dichalcogenide nanosheet-based wearable thermoelectric generators | Influence of pressure on the transport, magnetic, and structural properties of superconducting Cr0.0009NbSe2 single crystal | Using controlled disorder to probe the interplay between charge order and superconductivity in NbSe2

## O-Sr-Zr
- rank 295 | 25 samples | 6 papers | 6 compositions
- compositions: Sr(Zr0.9Yb0.05Gd0.05)O2.95 (8); Sr(Zr0.85Yb0.075Gd0.075)O2.925 (5); Sr(Zr0.8Yb0.1Gd0.1)O2.9 (5); SrZrO3 (3); SrZr0.8Co0.2O3 (2); SrZr0.85Al0.15O2.925 (2)
- dopant candidates (<5% at.): Yb (18), Gd (18), Co (2), Al (2)
- measured range: 299-1674 K (5th-95th pct of 25 curves)
- [ref 1] TEDesignLab / ICSD: SrZrO3 I4/mcm (140) mp-5076 [hull=0.013, icsd=10, PRIMARY]; SrZrO3 Pm-3m (221) mp-3323 [hull=0.055, icsd=10]; SrZrO3 Pnma (62) mp-4387 [hull=0.000, icsd=6]; SrZrO3 Cmcm (63) mp-3626 [hull=0.008, icsd=2]; Sr3Zr2O7 (47)
- [ref 2] MP, ranked by ICSD evidence: Sr3Zr2O7 I4/mmm (139) mp-27690 [hull=0.039, icsd=1, PRIMARY]; Sr2Zr7O16 R-3 (148) mp-770419 [hull=0.000, PRIMARY]; Sr2ZrO4 I4/mmm (139) mp-1025349 [hull=0.035, PRIMARY]; Sr4Zr3O10 Pbca (61) mp-1208748 [hull=0.003, PRIMARY]; SrZrO3 Imma (74) mp-1080575 [hull=0.006, icsd=1]
- papers: Zirconates as New Materials for Thermal Barrier Coatings | Phase Composition and Thermal Properties of Yb-Gd Co-Doped SrZrO3 Coating Prepared by the Solution Precursor Plasma Spray | Achieving low thermal conductivity in Sr(Zr0.9Yb0.05Gd0.05)O2.95: A suitable material for high temperature applications

## O-Th
- rank 296 | 25 samples | 6 papers | 13 compositions
- compositions: ThO2 (12); (CaO)0.07(ThO2)0.93 (2); Th0.98U0.02O2 (1); Th0.99U0.01O2 (1); Th0.97U0.03O2 (1); Th0.9Y0.1O2 (1)
- dopant candidates (<5% at.): U (8), Ca (2), Pu (2), Y (1)
- seed hypothesis (confirm): fluorite_oxide
- measured range: 290-1270 K (5th-95th pct of 25 curves; full span incl. outliers 285-1374 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ThO2 Fm-3m (225) mp-643 [hull=0.000, icsd=19, PRIMARY]; NdTh9O20 P-1 (2) mp-676564 [hull=0.007, PRIMARY]; CeTh9O20 P-1 (2) mp-760080 [hull=0.002, PRIMARY]; Th3O I4/mmm (139) mp-979038 [hull=1.589, PRIMARY]; Th3O2 R-3c (167) mp-865439 [hull=0.320, PRIMARY]
- papers: Thermoelectric Power in Pure and CaO-Doped ThO[sub 2] Electrolytes | Thermal conductivity of ThO2 and Th0.98U0.02O2 | Critical evaluation of the thermal properties of Th02 and Th1−yUy02 and a survey of the literature data on Th1−yPuy02

## Pb-S-Se-Te
- rank 297 | 25 samples | 7 papers | 18 compositions
- compositions: (PbTe)0.65(PbS)0.25(PbSe)0.1 (5); Pb0.98Na0.02Te0.76Se0.12S0.12 (2); Pb0.98Na0.02Te0.8Se0.1S0.1 (2); PbTe0.1Se0.4S0.5 (2); (PbTe)0.75(PbSe)0.1(PbS)0.15 (1); (PbTe)0.8(PbSe)0.1(PbS)0.1 (1)
- dopant candidates (<5% at.): Na (10), Cd (5), Sb (4)
- seed hypothesis (confirm): rocksalt
- solid-solution axis: Se/(Se+Te) spans 0.11-0.86 (median 0.67) over 18 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 297-901 K (5th-95th pct of 90 curves; full span incl. outliers 100-907 K)
- papers: HighZTin p-Type (PbTe)1–2x(PbSe)x(PbS)xThermoelectric Materials | Electron Doping in Bottom-Up Engineered Thermoelectric Nanomaterials through HCl-Mediated Ligand Displacement | Origin of resistivity anomaly in p-type leads chalcogenide multiphase compounds

## S-Se-Ti
- rank 298 | 25 samples | 4 papers | 22 compositions
- compositions: TiS1.5Se0.5 (2); TiSe1.8S0.2 (2); TiSe1.7S0.3 (2); Cu0.025TiS1.5Se0.5 (1); TiSSe (1); TiS0.5Se1.5 (1)
- dopant candidates (<5% at.): Cu (13)
- seed hypothesis (confirm): cdi2_1t
- solid-solution axis: S/(S+Se) spans 0.10-0.75 (median 0.19) over 22 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-701 K (5th-95th pct of 79 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti3(SeS2)2 P3m1 (156) mp-1217140 [hull=0.004, PRIMARY]; TiSeS P3m1 (156) mp-1216698 [hull=0.000, PRIMARY]
- papers: CdI2 structure type as potential thermoelectric materials: Synthesis and high temperature thermoelectric properties of the solid solution TiSxSe2−x | Tuned thermoelectric properties of TiS1.5Se0.5 through copper intercalation | The low temperature thermoelectric properties of CuxTiSe2−ySy

## Ag
- rank 299 | 24 samples | 4 papers | 19 compositions
- compositions: Ag (5); Ag0.9995Mg0.0005 (2); Ag96.85Mn3.85 (1); Ag98.32Pt1.68 (1); Ag97.75Pt2.25 (1); Ag98.07Mn1.93 (1)
- dopant candidates (<5% at.): Au (5), Pd (4), Mn (3), Pt (3), Mg (3), Cu (2)
- seed hypothesis (confirm): solid_solution_alloy
- measured range: 13-946 K (5th-95th pct of 34 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ag Fm-3m (225) mp-124 [hull=0.000, icsd=22, PRIMARY]; Ag P6_3/mmc (194) mp-8566 [hull=0.006, icsd=1]; Ag R-3m (166) mp-989737 [hull=0.003]
- papers: Thermoelectric Power and Electrical Resistivity of Dilute Alloys of Mn, Pd, and Pt in Cu, Ag, and Au | Nanometrology: Absolute Seebeck coefficient of individual silver nanowires | Characterization of the thermal conductivity and mechanical properties of sheath alloy materials for Bi-2223 superconductor tapes

## B-Zr
- rank 300 | 24 samples | 6 papers | 7 compositions
- compositions: ZrB2 (18); ZrB12 (1); Zr34B66 (1); Zr14B86 (1); Zr11B89 (1); Zr6.7B93.3 (1)
- seed hypothesis (confirm): alb2
- measured range: 54-2274 K (5th-95th pct of 24 curves; full span incl. outliers 54-2425 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZrB2 P6/mmm (191) mp-1472 [hull=0.000, icsd=12, PRIMARY]; ZrB12 Fm-3m (225) mp-1084 [hull=0.017, icsd=7, PRIMARY]; ZrB Fm-3m (225) mp-451 [hull=0.367, icsd=5, PRIMARY]; ZrB6 Pm-3m (221) mp-1001788 [hull=0.408, PRIMARY]; ZrB P-6m2 (187) mp-1014138 [hull=0.335]
- papers: Thermal properties of La2O3-doped ZrB2- and HfB2-based ultra-high temperature ceramics | Thermal and Electrical Transport Properties of Spark Plasma-Sintered HfB2 and ZrB2 Ceramics | Thermal conductivity of metal dodecaborides with a UB12 structure
