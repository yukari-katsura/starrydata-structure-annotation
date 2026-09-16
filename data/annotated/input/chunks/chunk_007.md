# Host systems -- chunk 007 of 73

Ranks 301-350 by sample count. These 50 host systems cover 1108 samples (2.13% of the TE set); cumulative through this chunk: 75.73%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Bi-Ca-Mg
- rank 301 | 24 samples | 6 papers | 17 compositions
- compositions: CaMg2Bi1.98 (4); CaMg2Bi2 (3); Ca0.995Na0.005Mg2Bi1.98 (2); CaMg1.9Zn0.1Bi1.98 (2); Ca0.9975Na0.0025Mg2Bi1.98 (1); Ca1Mg2Bi1.98 (1)
- dopant candidates (<5% at.): Zn (11), Na (8), Ba (4), Li (3), Yb (1)
- seed hypothesis (confirm): caal2si2_zintl
- measured range: 51-876 K (5th-95th pct of 125 curves; full span incl. outliers 11-881 K)
- [ref 1] TEDesignLab / ICSD: Ca(MgBi)2 P-3m1 (164) mp-29208 [hull=0.000, icsd=2, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: CaMg14Bi Amm2 (38) mp-1028135 [hull=0.070, PRIMARY]; CaMg6Bi Amm2 (38) mp-1023153 [hull=0.127, PRIMARY]; CaMg14Bi P-6m2 (187) mp-1028126 [hull=0.108]
- papers: Thermoelectric transport properties of CaMg2Bi2, EuMg2Bi2, and YbMg2Bi2 | Thermoelectric properties of Zintl compound Ca1−xNaxMg2Bi1.98 | Thermoelectric properties of Bi-based Zintl compounds Ca1−xYbxMg2Bi2

## Ce-Ni-Sn
- rank 302 | 24 samples | 9 papers | 14 compositions
- compositions: CeNiSn (7); CeNi2Sn2 (5); Ce0.85La0.15NiSn (1); Ce9Ni24Sn49 (1); Ce0.9La0.1NiSn (1); Ce2Ni2Sn (1)
- dopant candidates (<5% at.): La (4), Co (2), Cu (2), Pt (1)
- seed hypothesis (confirm): crb_feb_chain
- measured range: 10-298 K (5th-95th pct of 25 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeNiSn Pnma (62) mp-21119 [hull=0.000, icsd=4, PRIMARY]; Ce(NiSn)2 P4/nmm (129) mp-1078794 [hull=0.000, icsd=2, PRIMARY]; Ce(Ni2Sn)2 I-4c2 (120) mp-30510 [hull=0.306, icsd=2, PRIMARY]; CeNiSn2 Cmcm (63) mp-1025558 [hull=0.009, icsd=2, PRIMARY]; Ce2Ni2Sn Immm (71) mp-22713 [hull=0.000, icsd=1, PRIMARY]
- papers: Magnetic and electrical transport properties of RE9Ni24Sn49 compounds (RE=Y, Ce, Pr, Sm and Tb) | Gap formation in CeNiSn at low temperatures | Transport properties of Ce2Ni2Sn and Ce2Pd2.05Sn0.95 Kondo lattice systems

## Co-O-Sm-Sr
- rank 303 | 24 samples | 9 papers | 13 compositions
- compositions: Sm0.5Sr0.5CoO3 (5); Sm0.7Sr0.3CoO3 (5); Sm0.6Sr0.4CoO3 (2); Sr0.6Sm0.4CoO3 (2); Sm0.3Sr0.7CoO3 (2); Sm0.5Sr0.5Co0.9Ce0.1O3 (1)
- dopant candidates (<5% at.): Ce (4), Fe (1), Cu (1), Mn (1)
- measured range: 297-1268 K (5th-95th pct of 24 curves; full span incl. outliers 295-1317 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr3Sm(CoO4)2 Amm2 (38) mp-1218459 [hull=0.022, PRIMARY]; SrSmCoO4 I4mm (107) mp-1217761 [hull=0.045, PRIMARY]; SrSmCoO4 Cmcm (63) mp-1217772 [hull=0.068]
- papers: Effects of Sm0.5Sr0.5CoO3-based cathode current-collecting element on the performance of intermediate-temperature solid oxide fuel cells | Thermal Expansion and Electrical Conductivity of Perovskite Oxide (Ln1-xSrx)CoO3-.DELTA. (Ln=La, Nd and Sm) | Cobalt-site cerium doped SmxSr1−xCoO3−δ oxides as potential cathode materials for solid-oxide fuel cells

## Cr-Fe
- rank 304 | 24 samples | 5 papers | 23 compositions
- compositions: Fe37Cr63 (2); Cr0.888Fe0.112 (1); Cr0.905Fe0.095 (1); Fe30Cr70 (1); Fe19Cr81 (1); Fe23Cr77 (1)
- dopant candidates (<5% at.): Mo (1), Si (1), V (1), C (1)
- seed hypothesis (confirm): solid_solution_alloy
- measured range: 39-1263 K (5th-95th pct of 47 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cr3Fe Fm-3m (225) mp-1008282 [hull=0.121, icsd=1, PRIMARY]; CrFe3 Pm-3m (221) mp-1018081 [hull=0.046, icsd=1, PRIMARY]; Cr2Fe Fd-3m (227) mp-1077708 [hull=0.279, icsd=1, PRIMARY]; CrFe Cmmm (65) mp-1226211 [hull=0.088, PRIMARY]; CrFe4 Fmmm (69) mp-1226230 [hull=0.021, PRIMARY]
- papers: Thermoelectric power of antiferromagnetic chromium-iron alloys | Thermoelectric Power and Electrical Resistance of Chromium‐Iron Alloys from 125° to 625°K | Thermoelectric Power and Resistivity of Chromium‐Rich CrFe Alloys between 25° and 1000°C

## Cu-Ga-In-Te
- rank 305 | 24 samples | 3 papers | 18 compositions
- compositions: CuIn0.75Ga0.25Te2 (2); CuIn0.5Ga0.5Te2 (2); Cu(In0.5Ga0.5)0.99Zn0.01Te2 (2); CuIn0.65Ga0.35Te2 (2); CuIn0.25Ga0.75Te2 (2); CuIn0.35Ga0.65Te2 (2)
- dopant candidates (<5% at.): Zn (6)
- seed hypothesis (confirm): chalcopyrite
- solid-solution axis: Ga/(Ga+In) spans 0.25-0.75 (median 0.50) over 18 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 72-872 K (5th-95th pct of 57 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): InGa(CuTe2)2 I-4 (82) mp-1224050 [hull=0.011, PRIMARY]
- papers: High-Performance Pseudocubic Thermoelectric Materials from Non-cubic Chalcopyrite Compounds | High thermoelectric performance of solid solutions CuGa1−xInxTe2 (x = 0–1.0) | Influence of doping and solid solution formation on the thermoelectric properties of chalcopyrite semiconductors

## Fe-Mn-Si
- rank 306 | 24 samples | 7 papers | 24 compositions
- compositions: (Mn0.85Fe0.15)Si1.7 (1); (Mn0.80Fe0.20)Si1.7 (1); (Mn0.75Fe0.25)Si1.7 (1); (Mn0.70Fe0.30)Si1.7 (1); (Mn0.65Fe0.35)Si1.7 (1); Mn0.6Fe0.4Si (1)
- dopant candidates (<5% at.): Ti (2), Ga (1), Cu (1), Mg (1), Cr (1), V (1), Zn (1), Bi (1), Pb (1), Zr (1), W (1)
- seed hypothesis (confirm): hms_chimney_ladder
- measured range: 11-855 K (5th-95th pct of 54 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnFe2Si Fm-3m (225) mp-5529 [hull=0.000, icsd=4, PRIMARY]; Mn3Fe3Si2 R3m (160) mp-1221761 [hull=0.064, PRIMARY]; Mn5Fe5Si6 Amm2 (38) mp-1221407 [hull=0.043, PRIMARY]; MnFe3Si8 P4/mmm (123) mp-1221641 [hull=0.066, PRIMARY]; MnFe4Si3 Amm2 (38) mp-1221713 [hull=0.043, PRIMARY]
- papers: Preparation and Thermoelectric Properties of a Chimney-Ladder (Mn1-xFex)Siγ(γ∼1.7) Solid Solution | Filling dependence of thermoelectric power in transition-metal monosilicides | Low‐Temperature Transport Properties of Commercial Metals and Alloys. II. Aluminums

## In-Te
- rank 307 | 24 samples | 10 papers | 12 compositions
- compositions: In4Te3 (4); InTe (4); In2(Te0.94Se0.06)3 (4); In0.995Te (3); In2Te3 (2); In4Se0.2Te2.8 (1)
- dopant candidates (<5% at.): Se (7), Cu (1), Na (1)
- seed hypothesis (confirm): inte_tlse, in4se3  <-- MIXED, split per composition
- measured range: 12-736 K (5th-95th pct of 99 curves; full span incl. outliers 10-776 K)
- [ref 1] TEDesignLab / ICSD: In4Te3 Pnnm (58) mp-617281 [hull=0.000, icsd=9, PRIMARY]; In2Te5 (9)
- [ref 2] MP, ranked by ICSD evidence: InTe Fm-3m (225) mp-2597 [hull=0.008, icsd=10, PRIMARY, AMBIGUOUS]; In2Te3 F-43m (216) mp-622511 [hull=0.038, icsd=2, PRIMARY]; In2Te5 C2/c (15) mp-1197742 [hull=0.006, icsd=1, PRIMARY]; In7Te10 R32 (155) mp-669311 [hull=0.000, icsd=1, PRIMARY]; InTe I4/mcm (140) mp-20320 [hull=0.013, icsd=9]
- papers: Thermoelectric properties of polycrystalline In4Se3 and In4Te3 | Thermoelectric properties of bipolar diffusion effect on In4Se3−xTex compounds | The Origin of Ultralow Thermal Conductivity in InTe: Lone-Pair-Induced Anharmonic Rattling

## Mo-Sb
- rank 308 | 24 samples | 9 papers | 15 compositions
- compositions: Mo3Sb7 (9); Mo2.6Fe0.4Sb7 (2); Mo2.57Fe0.43Sb7 (1); Ni0.2Mo2.8Ni0.2Sb7 (1); Ni0.25Mo2.75Ni0.25Sb7 (1); Mo2.7Ru0.25Sb7 (1)
- dopant candidates (<5% at.): Fe (8), Ni (3), Ru (2), Te (2), I (1)
- seed hypothesis (confirm): ir3ge7
- measured range: 12-993 K (5th-95th pct of 108 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sb7Mo3 Im-3m (229) mp-1521 [hull=0.000, icsd=10, PRIMARY]; Sb3Mo Fm-3m (225) mp-973203 [hull=0.613, PRIMARY]
- papers: High thermoelectric power factor in Fe-substituted Mo3Sb7 | Optimized thermoelectric properties of Mo3Sb7−xTex with significant phonon scattering by electrons | Effect of heavy doping of nickel in compound Mo3Sb7: Structure and thermoelectric properties

## O-Sn-Sr
- rank 309 | 24 samples | 7 papers | 10 compositions
- compositions: Sr0.95La0.05SnO3 (6); Sr0.97La0.03SnO3 (6); Sr0.99La0.01SnO3 (5); (Ba0.2Sr0.8)0.95La0.05SnO3 (1); La0.03Sr0.97SnO3 (1); SrSnO3 (1)
- dopant candidates (<5% at.): La (19), Er (2), Ba (1)
- seed hypothesis (confirm): perovskite
- measured range: 10-1072 K (5th-95th pct of 24 curves)
- [ref 1] TEDesignLab / ICSD: SrSnO3 Pnma (62) mp-2879 [hull=0.000, icsd=14, PRIMARY]; Sr2SnO4 P4_2/ncm (138) mp-4287 [hull=0.000, icsd=7, PRIMARY]; Sr3Sn2O7 Cmcm (63) mp-17743 [hull=0.003, icsd=1, PRIMARY]; Sr2SnO4 I4/mmm (139) mp-3376 [hull=0.013, icsd=6]; Sr2SnO4 Cmce (64) mp-4941 [hull=0.002, icsd=3]
- [ref 2] MP, ranked by ICSD evidence: Sr3SnO Pm-3m (221) mp-7961 [hull=0.000, icsd=2, PRIMARY]
- papers: High-Temperature Thermoelectric Properties of La-Doped Ba1-xSrxSnO3 Ceramics | Thermoelectric properties and figure of merit of perovskite-type Sr1−xLaxSnO3 ceramics | Significant Suppression of Cracks in Freestanding Perovskite Oxide Flexible Sheets Using a Capping Oxide Layer

## Se-Sn-Te
- rank 310 | 24 samples | 7 papers | 18 compositions
- compositions: SnTe0.75Se0.25 (5); SnTe0.90Se0.10 (3); SnSe0.8Te0.2 (1); SnSe0.88Te0.12 (1); Sn0.99Na0.01Se0.84Te0.16 (1); Sn0.99Na0.01Se0.8Te0.2 (1)
- dopant candidates (<5% at.): Cd (5), Ag (4), Na (2), Sb (2), Bi (2)
- seed hypothesis (confirm): rocksalt
- solid-solution axis: Se/(Se+Te) spans 0.10-0.92 (median 0.76) over 18 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 297-826 K (5th-95th pct of 86 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sn3Te2Se P-3m1 (164) mp-1218966 [hull=0.009, PRIMARY]; Sn4Te3Se R3m (160) mp-1219035 [hull=0.130, PRIMARY]; Sn4TeSe3 Pm (6) mp-1219000 [hull=0.022, PRIMARY]
- papers: Thermoelectric transport properties of pristine and Na-doped SnSe1−xTex polycrystals | Facile precipitation of two phase alloys in SnTe0.75Se0.25 with improved power factor | Thermoelectric Performance of Se/Cd Codoped SnTe via Microwave Solvothermal Method

## Al-N
- rank 311 | 23 samples | 7 papers | 8 compositions
- compositions: AlN (15); (TbN)0.5(AlN)99.5 (2); (Y2O3)0.18(AlN)99.82 (1); (AlN)98.53(CaO)1.47 (1); (Y2O3)1.98(AlN)98.02 (1); (Tb)0.5(AlN)99.5 (1)
- dopant candidates (<5% at.): Tb (5), O (3), Y (2), Ca (1)
- seed hypothesis (confirm): wurtzite
- measured range: 11-773 K (5th-95th pct of 23 curves; full span incl. outliers 11-953 K)
- [ref 1] TEDesignLab / ICSD: AlN P6_3mc (186) mp-661 [hull=0.000, icsd=24, PRIMARY]; AlN F-43m (216) mp-1700 [hull=0.021, icsd=8]; AlN Fm-3m (225) mp-1330 [hull=0.172, icsd=6]; AlN P6_3/mmc (194) mp-13178 [hull=0.115, icsd=2]; AlN (63)
- papers: Nonmetallic crystals with high thermal conductivity | Steady-state thermal conductivity measurements of AlN and SiC substrate materials | Effect of CaO on the Thermal Conductivity of Aluminum Nitride

## Bi-O-V
- rank 312 | 23 samples | 3 papers | 13 compositions
- compositions: Bi2V0.95Cr0.05O5.5 (2); Bi2V0.9Cr0.1O5.5 (2); Bi2V0.8Cr0.2O5.5 (2); Bi2V0.9Mo0.1O5.5 (2); Bi2V0.8Mo0.2O5.5 (2); Bi2V0.95W0.05O5.5 (2)
- dopant candidates (<5% at.): Cr (6), Mo (6), W (6)
- seed hypothesis (confirm): v2o5_layered, aurivillius  <-- MIXED, split per composition
- measured range: 40-1002 K (5th-95th pct of 74 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): VBiO4 I4_1/a (88) mp-25122 [hull=0.016, icsd=3, PRIMARY]; V2Bi7O15 C2/c (15) mp-647265 [hull=0.020, icsd=1, PRIMARY]; V(BiO3)2 P2_1/c (14) mp-1204532 [hull=0.101, icsd=1, PRIMARY]; VBi2O5 Pnma (62) mp-1205158 [hull=0.091, icsd=1, PRIMARY]; V(Bi5O8)5 C2 (5) mp-767265 [hull=0.012, PRIMARY]
- papers: Effect of Element Substitution at V site on Thermoelectric Properties of Aurivillius Phase Bi2VO5.5 | Revisiting Hollandites: Channels Filling by Main-Group Elements Together with Transition Metals in Bi2–yVyV8O16 | Metal–insulator transition tuned by magnetic field in Bi1.7V8O16 hollandite

## Co-Hf-Sb-Ti
- rank 313 | 23 samples | 7 papers | 15 compositions
- compositions: Ti0.5Hf0.5CoSb0.85Sn0.15 (6); Hf0.5Ti0.5CoSb0.85Sn0.15 (4); Ti0.6Hf0.4Co0.87Ni0.13Sb (1); Ti0.75(Zr0.25Hf0.75)0.25CoSb (1); Ti0.50(Zr0.25Hf0.75)0.50CoSb (1); Ti0.5Hf0.5Co1.04Sb0.9Sn0.1 (1)
- dopant candidates (<5% at.): Sn (16), Ta (3), Ni (2), Zr (2)
- solid-solution axis: Hf/(Hf+Ti) spans 0.20-0.50 (median 0.50) over 15 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 294-991 K (5th-95th pct of 114 curves; full span incl. outliers 288-1167 K)
- papers: Enhanced thermoelectric performance by the combination of alloying and doping in TiCoSb-based half-Heusler compounds | Thermoelectric and Thermophysical Properties of TiCoSb-ZrCoSb-HfCoSb Pseudo Ternary System Prepared by Spark Plasma Sintering | Short and long range order of Half-Heusler phases in (Ti,Zr,Hf)CoSb thermoelectric compounds

## Co-O-Pr
- rank 314 | 23 samples | 8 papers | 8 compositions
- compositions: Pr0.9Ca0.1CoO3 (6); Pr0.9Sr0.1CoO3 (5); Pr0.9Ba0.1CoO3 (4); PrCoO3 (4); PrCo0.95Ni0.05O3 (1); Pr0.8Sr0.2CoO3 (1)
- dopant candidates (<5% at.): Sr (8), Ca (7), Ba (5), Ni (1), Cu (1)
- measured range: 11-1169 K (5th-95th pct of 29 curves; full span incl. outliers 11-1273 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrCoO3 Pnma (62) mp-24849 [hull=0.000, icsd=7, PRIMARY]; Pr2CoO4 I4/mmm (139) mp-1207107 [hull=0.099, PRIMARY]; PrCoO3 Pm-3m (221) mp-24852 [hull=0.147, icsd=1]
- papers: High-temperature thermoelectric properties of Ln(Co, Ni)O3 (Ln=La, Pr, Nd, Sm, Gd and Dy) compounds | Influence of ionic sizes of rare earths on thermoelectric properties of perovskite-type rare earth cobalt oxides RCoO3 (R=Pr, Nd, Tb, Dy) | Transport and Magnetic Properties of R1-xAxCoO3(R = La, Pr and Nd; A = Ba, Sr and Ca)

## Cu-O-Rh
- rank 315 | 23 samples | 6 papers | 7 compositions
- compositions: CuRhO2 (9); CuRh0.9Mg0.1O2 (7); CuRh0.94Mg0.06O2 (2); CuRh0.97Mg0.03O2 (2); CuRh0.99Mg0.01O2 (1); CuRh0.95Mg0.05O2 (1)
- dopant candidates (<5% at.): Mg (14)
- seed hypothesis (confirm): delafossite
- measured range: 12-1159 K (5th-95th pct of 38 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu(RhO2)2 Fd-3m (227) mp-4409 [hull=0.021, icsd=4, PRIMARY]; CuRhO2 R-3m (166) mp-14116 [hull=0.000, icsd=1, PRIMARY]; Cu(RhO2)2 I4_1/amd (141) mp-1104542 [hull=0.023, icsd=2]
- papers: Electronic structure and thermoelectric properties ofCuRh1−xMgxO2 | High-temperature thermoelectric properties of Delafossite oxide CuRh1-xMgxO2 | Mg substitution effects of new thermoelectric Rh oxides

## Cu-O-V
- rank 316 | 23 samples | 3 papers | 15 compositions
- compositions: Cu2.2V4O11 (9); Cu2V2O7 (1); Zn0.25Cu1.75V2O7 (1); Zn0.2Cu1.8V2O7 (1); Zn0.5Cu1.5V2O7 (1); Cu2.36V4O11 (1)
- dopant candidates (<5% at.): Zn (3)
- seed hypothesis (confirm): vanadium_bronze
- measured range: 14-924 K (5th-95th pct of 42 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): V2Cu2O7 C2/c (15) mp-607934 [hull=0.002, icsd=3, PRIMARY]; VCuO3 Im-3 (204) mp-1105167 [hull=0.124, icsd=2, PRIMARY]; KV3Cu5O13 P-1 (2) mp-699565 [hull=0.050, icsd=1, PRIMARY]; V2CuO6 P-1 (2) mp-741706 [hull=0.010, icsd=1, PRIMARY]; V2(CuO3)3 P2_1/m (11) mp-1194512 [hull=0.090, icsd=1, PRIMARY]
- papers: Thermoelectric Properties and Phase Transition of (Zn<I><SUB>x</SUB></I>Cu<SUB>2&minus;<I>x</I></SUB>)V<SUB>2</SUB>O<SUB>7</SUB> | Multifunctional composite crystalCuxV4O11(x≈2.2) | Polaronic Nonmetal–Correlated Metal Crossover System β′-Cu<i><sub>x</sub></i>V<sub>2</sub>O<sub>5</sub> with Anharmonic Copper Oscillation and Thermoelectric Conversion Performance

## Cu-Te
- rank 317 | 23 samples | 12 papers | 16 compositions
- compositions: Cu2Te (7); Cu1.75Te (2); Cu27.5Ge2.5Te70 (1); CuIn0.09Zn0.01Te2 (1); Cu22.5Ge2.5Te75 (1); Cu1.99Ga0.01Te (1)
- dopant candidates (<5% at.): Fe (5), Ga (3), Ge (2), In (1), Zn (1), Se (1)
- seed hypothesis (confirm): cu2se_superionic
- measured range: 89-743 K (5th-95th pct of 99 curves; full span incl. outliers 10-898 K)
  !! MEASUREMENT CROSSES A TRANSITION: cu2se_superionic -> cu2se_superionic at ~400 K (Ordered low-T superstructure -> cubic superionic, ~400 K. Cu2S transforms near ~376 K.)
     Record each phase with its own temperature range, not a single prototype.
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuTe Pmmn (59) mp-20826 [hull=0.000, icsd=5, PRIMARY]; Cu2Te P6/mmm (191) mp-1861 [hull=0.134, icsd=4, PRIMARY]; Cu7Te4 P3m1 (156) mp-624307 [hull=0.145, icsd=2, PRIMARY]; CuTe2 Pa-3 (205) mp-1103235 [hull=0.039, icsd=1, PRIMARY]; Cu3Te Pm-3m (221) mp-1183984 [hull=0.181, PRIMARY]
- papers: Influence of doping and solid solution formation on the thermoelectric properties of chalcopyrite semiconductors | Conducting glasses as new potential thermoelectric materials: the Cu–Ge–Te case | Thermoelectric properties of Ag-doped Cu2Se and Cu2Te

## Ir-Sb
- rank 318 | 23 samples | 6 papers | 14 compositions
- compositions: IrSb3 (5); La0.1Ir4Ge0.3Sb11.7 (3); La0.3Ir4Sb12 (2); La0.2Ir4Sb12 (2); Ba0.3Ir4Sb12 (2); Ir0.9Co0.1Sb2 (1)
- dopant candidates (<5% at.): La (8), Ge (4), Ba (4), Co (1), Sr (1), K (1), Na (1)
- seed hypothesis (confirm): skutterudite
- measured range: 11-953 K (5th-95th pct of 59 curves; full span incl. outliers 11-1098 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sb2Ir P2_1/c (14) mp-1247 [hull=0.000, icsd=4, PRIMARY]; Sb3Ir Im-3 (204) mp-1239 [hull=0.000, icsd=4, PRIMARY]; SbIr P6_3/mmc (194) mp-10125 [hull=0.086, icsd=1, PRIMARY]
- papers: Thermoelectric properties of CoSb3and related alloys | Preparation and thermoelectric properties of IrxCo1 − xSb2 alloys | Enhancement of high temperature thermoelectric properties of intermetallic compounds based on a Skutterudite IrSb3and a half-Heusler TiNiSb

## N-Zr
- rank 319 | 23 samples | 5 papers | 1 compositions
- compositions: ZrN (23)
- seed hypothesis (confirm): rocksalt_nitride_carbide
- measured range: 294-2311 K (5th-95th pct of 23 curves; full span incl. outliers 105-2408 K)
- [ref 1] TEDesignLab / ICSD: Zr3N4 Pnma (62) mp-277 [hull=0.000, icsd=3, PRIMARY]; Zr3N4 I-43d (220) mp-11661 [hull=0.045, icsd=2]; Zr3N4 (33)
- [ref 2] MP, ranked by ICSD evidence: ZrN Fm-3m (225) mp-1352 [hull=0.000, icsd=37, PRIMARY]; ZrN2 P-3m1 (164) mp-1008600 [hull=1.188, icsd=1, PRIMARY]; Zr2N P4_2/mnm (136) mp-1014265 [hull=0.000, PRIMARY]; Zr3N I4/mmm (139) mp-1188048 [hull=1.543, PRIMARY]; Zr3N2 R-3c (167) mp-866083 [hull=0.016, PRIMARY]
- papers: Phonon and electron contributions to the thermal conductivity of \nVNx\n epitaxial layers | Thermophysical characterization of ZrN and (Zr,Pu)N | Processing and properties of ZrC, ZrN and ZrCN ceramics: a review

## O-Y-Zr
- rank 320 | 23 samples | 9 papers | 13 compositions
- compositions: (ZrO2)0.92(Y2O3)0.08 (10); (Y2O3)0.08(ZrO2)0.92 (2); (Y2O3)0.16(ZrO2)0.84 (1); Zr0.85Y0.15O1.925 (1); (Y2O3)0.12(ZrO2)0.88 (1); (Ta2O5)5.4(Y2O3)9(ZrO2)85.6 (1)
- dopant candidates (<5% at.): Ta (3), Nb (2), La (1)
- seed hypothesis (confirm): fluorite_oxide
- measured range: 292-1998 K (5th-95th pct of 23 curves; full span incl. outliers 115-2000 K)
- [ref 1] TEDesignLab / ICSD: Y2Zr2O7 (227)
- [ref 2] MP, ranked by ICSD evidence: Y2Zr2O7 P2_1 (4) mp-771043 [hull=0.058, PRIMARY]; NdY3Zr4O14 R-3m (166) mp-1220113 [hull=0.337, PRIMARY]; Y2Zr9O22 Pm (6) mp-675231 [hull=0.080, PRIMARY]; Y4Zr3O12 P-1 (2) mp-675802 [hull=0.000, PRIMARY]; YZr4O10 I4/m (87) mp-1215768 [hull=0.143, PRIMARY]
- papers: Thermoelectric power of YSZ | Mechanism of Thermal Transport in Zirconia and Yttria-Stabilized Zirconia by Molecular-Dynamics Simulation | Good Solid‐State Electrolytes Have Low, Glass‐Like Thermal Conductivity

## As-In
- rank 321 | 22 samples | 8 papers | 8 compositions
- compositions: InAs (10); Be0.0002InAs (3); In0.99Ga0.01As (2); In0.96Ga0.04As (2); Be0.00006InAs (2); Be0.001InAs (1)
- dopant candidates (<5% at.): Be (6), Ga (4), P (1), Mn (1)
- seed hypothesis (confirm): sphalerite
- measured range: 14-1068 K (5th-95th pct of 35 curves; full span incl. outliers 11-1172 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): InAs F-43m (216) mp-20305 [hull=0.000, icsd=25, PRIMARY]; In3As Pm-3m (221) mp-973466 [hull=0.189, PRIMARY]; InAs Fm-3m (225) mp-21391 [hull=0.197, icsd=2]; InAs P6_3mc (186) mp-1007652 [hull=0.009, icsd=1]; InAs Pa-3 (205) mp-20412 [hull=0.112, icsd=1]
- papers: Nanograined Half-Heusler Semiconductors as Advanced Thermoelectrics: An Ab Initio High-Throughput Statistical Study | Thermoelectrical properties of In1-xGaxAs and InAs crystals irradiated with fast electrons | Minority carrier barrier heterojunctions for improved thermoelectric efficiency

## B-Ce
- rank 322 | 22 samples | 9 papers | 4 compositions
- compositions: CeB6 (19); Ce0.75La0.25B6 (1); La0.1Ce0.9B6 (1); La0.03Ce0.97B6 (1)
- dopant candidates (<5% at.): La (3)
- seed hypothesis (confirm): cab6_hexaboride
- measured range: 10-303 K (5th-95th pct of 28 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeB6 Pm-3m (221) mp-21343 [hull=0.000, icsd=26, PRIMARY]; CeB4 P4/mbm (127) mp-1974 [hull=0.000, icsd=4, PRIMARY]
- papers: Transport properties of Kondo lattice CeB6 | Anomalous thermopower in heavy-fermion compounds CeB6, CeAl3, and CeCu6 − x Au x | Extended transport measurements on high-purity CeB6

## Ba-Co-Fe-O-Sr
- rank 323 | 22 samples | 8 papers | 9 compositions
- compositions: Ba0.5Sr0.5Co0.6Fe0.4O3 (7); Ba0.5Sr0.5Co0.4Fe0.6O3 (7); Ba0.5Sr0.5Co0.7Fe0.3O3 (2); Ba0.5Sr0.5Co0.7Fe0.28La0.02O3 (1); Ba0.5Sr0.5Co0.7Fe0.28Pr0.02O3 (1); Ba0.5Sr0.5Co0.7Fe0.28Ce0.02O3 (1)
- dopant candidates (<5% at.): La (1), Pr (1), Ce (1), Cu (1), Zn (1)
- measured range: 374-1239 K (5th-95th pct of 22 curves; full span incl. outliers 306-1273 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaSr7Fe6(CoO10)2 P1 (1) mp-1099862 [hull=0.019, PRIMARY]; BaSr7Fe6(CoO12)2 Amm2 (38) mp-1099936 [hull=0.024, PRIMARY]; BaSr7Fe7CoO20 P1 (1) mp-1076892 [hull=0.009, PRIMARY]; BaSr7Fe7CoO24 R3m (160) mp-1075935 [hull=0.024, PRIMARY]
- papers: B-site La, Ce, and Pr-doped Ba0.5Sr0.5Co0.7Fe0.3O3- perovskite cathodes for intermediate-temperature solid oxide fuel cells: Effectively promoted oxygen reduction activity and operating stability | Assessment of Ba0.5Sr0.5Co1−yFeyO3−δ (y=0.0–1.0) for prospective application as cathode for IT-SOFCs or oxygen permeating membrane | Preparation and properties of BaxSr1−xCoyFe1−yO3−δ cathode material for intermediate temperature solid oxide fuel cells

## Ba-Cu-Dy-O
- rank 324 | 22 samples | 3 papers | 6 compositions
- compositions: DyBa2Cu3O7 (7); Dy0.95Pr0.05Ba2(Cu0.98Fe0.02)3O7 (3); Dy0.95Pr0.05Ba2(Cu0.98Ni0.02)3O7 (3); Dy0.95Pr0.05Ba2(Cu0.98Zn0.02)3O7 (3); Dy0.95Pr0.05Ba2Cu3O7 (3); Dy0.95Pr0.05Ba2(Cu0.98Co0.02)3O7 (3)
- dopant candidates (<5% at.): Pr (15), Fe (3), Ni (3), Zn (3), Co (3)
- seed hypothesis (confirm): ybco_cuprate
- measured range: 10-301 K (5th-95th pct of 22 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2Dy(CuO2)4 Cmmm (65) mp-6691 [hull=0.000, icsd=3, PRIMARY]; BaDy2CuO5 Pnma (62) mp-22550 [hull=0.030, icsd=3, PRIMARY]; Ba2DyCu3O7 Pmmm (47) mp-622105 [hull=0.024, icsd=1, PRIMARY]; Ba4Dy(CuO3)3 Pm-3n (223) mp-1214524 [hull=0.000, PRIMARY]; Ba4Dy2Cu6NiO15 Amm2 (38) mp-1228235 [hull=0.024, PRIMARY]
- papers: Normal state transport properties in superconducting oxides RBa2Cu3O7- delta(R=Y, Gd, Sm, Nd, and Dy) | Effective magnetic moment and carrier-phonon coupling constant in RBa2Cu3O7−δ (R = Y, Gd, Sm, Nd and Dy) superconducting oxides at normal state | Electrical and thermal transport properties of Dy0.95Pr0.05Ba2(Cu1−x Mx)3O7−δ with (M=Fe, Co, Ni and Zn) bulk superconductors

## Ba-Cu-Te
- rank 325 | 22 samples | 5 papers | 20 compositions
- compositions: Ba3Cu13.25Te12 (2); BaCu2Te2 (2); Ba3Cu13.5Te12 (1); Ba3Cu13.975Te12 (1); Ba3Cu13.175Te12 (1); Ba3Cu13.325Te12 (1)
- dopant candidates (<5% at.): Ag (5), Se (1)
- measured range: 180-836 K (5th-95th pct of 87 curves; full span incl. outliers 11-850 K)
- [ref 1] TEDesignLab / ICSD: Ba6NaCu3Te14 (193) [PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ba(CuTe)2 Pnma (62) mp-30133 [hull=0.014, icsd=1, PRIMARY]
- papers: Thermoelectric Properties of the New Polytelluride Ba3Cu14-δTe12 | Synthesis, Structure, and Thermoelectric Properties of Barium Copper Polychalcogenides with Chalcogen-Centered Cu Clusters and Te22- Dumbbells | Exploratory synthesis of new heavy main group chalcogenides

## Cd-Hg-Se
- rank 326 | 22 samples | 1 papers | 12 compositions
- compositions: Cr0.003Cd0.21Hg0.79Se (3); Cr0.0003Cd0.21Hg0.79Se (3); Cr0.03Cd0.21Hg0.79Se (3); Co0.003Cd0.24Hg0.76Se (2); Fe0.03Cd0.35Hg0.65Se (2); Co0.03Cd0.24Hg0.76Se (2)
- dopant candidates (<5% at.): Co (10), Cr (9), Fe (3)
- measured range: 90-399 K (5th-95th pct of 22 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cd4HgSe5 P3m1 (156) mp-1226897 [hull=0.007, PRIMARY]; CdHg4Se5 I-4m2 (119) mp-1226731 [hull=0.005, PRIMARY]; CdHgSe2 R3m (160) mp-1226733 [hull=0.005, PRIMARY, AMBIGUOUS]; CdHg4Se5 R-3m (166) mp-1226756 [hull=0.170]; CdHgSe2 P-4m2 (115) mp-1226729 [hull=0.007]
- papers: Effect of Fe, Co, and Cr impurities on the thermoelectric properties of Cd x Hg1−x Se

## Ce-Ni
- rank 327 | 22 samples | 8 papers | 8 compositions
- compositions: CeNi (8); CeNi2 (5); CeNi5 (3); Ce7Ni3 (2); Ce(Ni0.965Ga0.035)5 (1); CeNi15 (1)
- dopant candidates (<5% at.): Ga (1)
- seed hypothesis (confirm): cacu5
- measured range: 11-892 K (5th-95th pct of 42 curves; full span incl. outliers 10-1031 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeNi2 Fd-3m (227) mp-1654 [hull=0.000, icsd=17, PRIMARY]; CeNi5 P6/mmm (191) mp-1910 [hull=0.000, icsd=15, PRIMARY]; CeNi Cmcm (63) mp-21188 [hull=0.000, icsd=5, PRIMARY]; Ce7Ni3 P6_3mc (186) mp-1106354 [hull=0.016, icsd=2, PRIMARY]; Ce4Ni Fd-3m (227) mp-1214244 [hull=0.402, PRIMARY]
- papers: Thermoelectric power of (Ce1−xLax)Ni single crystals | Dependence of the CeNi5 thermoelectric power on strong 4f-electron instability | Thermoelectric power in compounds with an intermediate valence of Ce: phenomenological description

## Fe-Mn-O
- rank 328 | 22 samples | 6 papers | 18 compositions
- compositions: MnFe2O4 (3); Mn0.5Fe2.5O4 (2); FeMn2O4 (2); Mn0.8Fe2.2O4 (1); Mn0.48Zn0.27Nb0.2Fe2.05O4 (1); Mn0.9Fe2.1O4 (1)
- dopant candidates (<5% at.): Zn (12), Nb (6), Sn (6), Cd (1)
- seed hypothesis (confirm): spinel
- measured range: 51-1084 K (5th-95th pct of 27 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn(FeO2)2 Fd-3m (227) mp-18750 [hull=0.015, icsd=2, PRIMARY]; Mn13Fe11O32 P-1 (2) mp-762538 [hull=0.029, PRIMARY]; Mn13Fe3O32 C2/m (12) mp-771188 [hull=0.074, PRIMARY]; Mn19Fe17O48 C2/m (12) mp-706492 [hull=0.042, PRIMARY]; Mn23FeO32 P-1 (2) mp-762043 [hull=0.010, PRIMARY]
- papers: Thermoelectric Properties of Sintered (MnyCo1-y) Fe2O4 | Anomalous electrical properties of MnxFe3−xO4 | []

## Fe-Nb-Sb-V
- rank 329 | 22 samples | 4 papers | 19 compositions
- compositions: Fe0.99Co0.01V0.6Nb0.4Sb (2); Fe0.985Co0.015V0.6Nb0.4Sb (2); FeV0.6Nb0.4Sb (2); Fe(V0.6Nb0.4)0.86Ti0.14Sb (1); Fe(V0.6Nb0.4)0.90Ti0.10Sb (1); Fe(V0.6Nb0.4)0.96Ti0.04Sb (1)
- dopant candidates (<5% at.): Co (6), Ti (4), Zr (4), Hf (4)
- solid-solution axis: Nb/(Nb+V) spans 0.20-0.75 (median 0.40) over 19 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 15-1049 K (5th-95th pct of 75 curves)
- papers: High Band Degeneracy Contributes to High Thermoelectric Performance in p-Type Half-Heusler Compounds | Enhanced phonon scattering by mass and strain field fluctuations in Nb substituted FeVSb half-Heusler thermoelectric materials | Electron and phonon transport in Co-doped FeV0.6Nb0.4Sb half-Heusler thermoelectric materials

## Fe-Sb-Ti-V
- rank 330 | 22 samples | 7 papers | 10 compositions
- compositions: FeV0.8Ti0.4Sb (9); Fe(V0.8Hf0.2)0.6Ti0.4Sb (3); FeV0.8Ti0.2Sb (3); Fe(V0.8Hf0.2)0.4Ti0.6Sb (1); Fe(V0.8Hf0.2)0.5Ti0.5Sb (1); FeV0.6Ti0.4Sb (1)
- dopant candidates (<5% at.): Hf (5), Nb (1)
- seed hypothesis (confirm): half_heusler
- measured range: 24-955 K (5th-95th pct of 95 curves; full span incl. outliers 20-1049 K)
- papers: Thermoelectric properties of fine-grained FeVSb half-Heusler alloys tuned to p-type by substituting vanadium with titanium | Optimizing the thermoelectric performance of FeVSb half-Heusler compound via Hf–Ti double doping | Effects of spark plasma sintering on enhancing the thermoelectric performance of Hf–Ti doped VFeSb half-Heusler alloys

## Ga-In-O-Zn
- rank 331 | 22 samples | 4 papers | 5 compositions
- compositions: InGaZn0.5O4 (12); InGaZnO7 (5); InGaZnO4 (3); InGaO3(ZnO) (1); InGaO3(ZnO)2 (1)
- seed hypothesis (confirm): homologous_inmo3_zno
- measured range: 11-475 K (5th-95th pct of 32 curves)
- [ref 1] TEDesignLab / ICSD: Zn4InGaO7 P6_3/mmc (194) mp-1194209 [hull=0.011, icsd=2, PRIMARY]; Zn2InGaO5 P6_3/mmc (194) mp-1187872 [hull=0.013, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Zn3InGaO6 R3m (160) mp-1215740 [hull=0.012, PRIMARY]; ZnInGaO4 R3m (160) mp-1215688 [hull=0.020, PRIMARY]
- papers: Drastic improvement of oxide thermoelectric performance using thermal and plasma treatments of the InGaZnO thin films grown by sputtering | Analysis of thermoelectric properties of amorphous InGaZnO thin film by controlling carrier concentration | Atomic-level control of the thermoelectric properties in polytypoid nanowires

## Li-O-V
- rank 332 | 22 samples | 7 papers | 12 compositions
- compositions: LiV2O4 (10); LiVO3 (2); (Cr2O3)0.1(LiVO3)99.9 (1); (K0.20Li0.80)VO3 (1); (Cr2O3)3.0(LiVO3)97.0 (1); (Cr2O3)0.025(LiVO3)99.975 (1)
- dopant candidates (<5% at.): Cr (7), Mg (2), K (1)
- seed hypothesis (confirm): vanadium_bronze, spinel  <-- MIXED, split per composition
- measured range: 11-679 K (5th-95th pct of 23 curves; full span incl. outliers 11-730 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiV2O4 Fd-3m (227) mp-19394 [hull=0.035, icsd=15, PRIMARY]; LiV2O5 Pnma (62) mp-777667 [hull=0.000, icsd=4, PRIMARY]; LiVO2 R-3m (166) mp-19340 [hull=0.000, icsd=3, PRIMARY]; Li3VO4 Pmn2_1 (31) mp-19219 [hull=0.000, icsd=3, PRIMARY]; LiVO3 C2/c (15) mp-19440 [hull=0.000, icsd=2, PRIMARY]
- papers: Thermoelectric power of ferroelectric potassium vanadate, cesium vanadate, lithium vanadate and their solid solutions | Thermoelectric power measurement of lithium vanadate ceramics doped with chromium oxide | Transport properties of metallic LiV2O4 single crystals—heavy mass Fermi liquid behavior

## Ni-O
- rank 333 | 22 samples | 6 papers | 14 compositions
- compositions: NiO (9); Ni0.97Li0.03O (1); Ni0.94Li0.06O (1); Ni0.91Li0.09O (1); A0.01NiO (1); Ga0.001NiO (1)
- dopant candidates (<5% at.): Li (4), Ga (3), In (3), Al (2), A0+ (1), Na (1)
- seed hypothesis (confirm): rocksalt_oxide
- measured range: 124-776 K (5th-95th pct of 30 curves; full span incl. outliers 113-1267 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NiO Fm-3m (225) mp-19009 [hull=0.000, icsd=32, PRIMARY]; Mn(Ni9O10)2 I4/mmm (139) mp-763814 [hull=0.000, PRIMARY]; Ni15O16 Im-3m (229) mp-705519 [hull=0.042, PRIMARY, AMBIGUOUS]; Mn3(Ni17O20)2 I4/mmm (139) mp-762377 [hull=0.000, PRIMARY]; Ni2O5 C2/c (15) mp-1094139 [hull=0.517, PRIMARY]
- papers: Synthesis and thermoelectric performance of Li-doped NiO ceramics | Some physico-chemical properties of pure and doped nickel oxide. Electrical conductivity and thermoelectric power measurements | High performance p-type thermoelectric oxide based on NiO

## Si-Ta-Te
- rank 334 | 22 samples | 4 papers | 14 compositions
- compositions: Ta4SiTe4 (6); Ta4Si0.995P0.005Te4 (2); Ta4Si0.98P0.02Te4 (2); Ta4Si0.99P0.01Te4 (2); (Ta0.99Ti0.01)4SiTe4 (1); (Ta0.999Ti0.001)4SiTe4 (1)
- dopant candidates (<5% at.): P (6), Mo (5), Ti (4), Sb (1)
- measured range: 10-346 K (5th-95th pct of 79 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ta4SiTe4 Pbam (55) mp-28509 [hull=0.000, icsd=2, PRIMARY]
- papers: Hole-doped M4SiTe4 (M = Ta, Nb) as an efficient p-type thermoelectric material for low-temperature applications | Thermoelectric properties of phosphorus-doped van der Waals crystal Ta4SiTe4 | Large thermoelectric power factor at low temperatures in one-dimensional telluride Ta4SiTe4

## As-Co-Fe-La-O
- rank 335 | 21 samples | 3 papers | 5 compositions
- compositions: LaFe0.5Co0.5AsO0.89F0.11 (6); LaFe0.6Co0.4AsO0.89F0.11 (6); LaFe0.7Co0.3AsO0.89F0.11 (4); LaFe0.8Co0.2AsO0.89F0.11 (4); LaFe0.75Co0.25AsO0.89F0.11 (1)
- dopant candidates (<5% at.): F (21)
- seed hypothesis (confirm): zrcusias_1111
- measured range: 10-301 K (5th-95th pct of 27 curves)
- papers: Distinct Transport Behaviors of LaFe1-yCoyAsO1-xFx(x=0.11) between the Superconducting and Nonsuperconducting MetallicyRegions Divided byy∼0.05 | Studies on Effects of Impurity Doping and NMR Measurements of La 1111 and/or Nd 1111 Fe-Pnictide Superconductors | Distinct physical behaviors of LaFe1−yCoyAsO0.89F0.11 between the superconducting and nonsuperconducting metallic regions of y divided by y∼0.05

## Au-Ba-Ge
- rank 336 | 21 samples | 6 papers | 12 compositions
- compositions: Ba8Au5.3Ge40.7 (9); Ba8Au6Ge40 (2); Ba8Au5Ga1Ge40 (1); Ba8Au5.33Ge40.67 (1); Ba8Au3Ge43 (1); Ba8Au3.5Ge42.5 (1)
- dopant candidates (<5% at.): Ga (1)
- seed hypothesis (confirm): clathrate_i
- measured range: 16-894 K (5th-95th pct of 41 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba4Ge20Au3 Pm-3n (223) mp-21839 [hull=0.000, icsd=2, PRIMARY]; BaGe2Au5 Pnma (62) mp-1198185 [hull=0.000, icsd=1, PRIMARY]; Ba(GeAu)2 I4/mmm (139) mp-1228646 [hull=0.000, PRIMARY]; BaGeAu3 I4mm (107) mp-1227958 [hull=0.000, PRIMARY]
- papers: Thermoelectric properties of Au-containing type-I clathrates Ba8AuxGa16−3xGe30+2x | Structure and thermoelectric properties of the n-type clathrate Ba8Cu5.1Ge40.2Sn0.7 | Atomic Interactions in the p-Type Clathrate I Ba8Au5.3Ge40.7

## Co-Fe-O-Sr
- rank 337 | 21 samples | 10 papers | 16 compositions
- compositions: SrCo0.25Fe0.75O2.69 (3); SrFe0.475Co0.475Mo0.05O3 (2); SrFe0.475Co0.475Sb0.05O3 (2); SrFe0.5Co0.5O3 (2); SrCo0.6Fe0.4O3 (1); Sr4Fe4.5Co1.5O13 (1)
- dopant candidates (<5% at.): Mo (3), Sb (2), Bi (2), Ca (1), Ti (1), Zr (1), Cu (1), Nb (1), Sn (1), Sc (1)
- seed hypothesis (confirm): brownmillerite
- measured range: 369-1272 K (5th-95th pct of 21 curves; full span incl. outliers 298-1280 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2FeCoO6 P4/mmm (123) mp-1218834 [hull=0.030, PRIMARY, AMBIGUOUS]; Sr5Fe4CoO10 P4/mmm (123) mp-1218452 [hull=0.080, PRIMARY]; Sr8Fe4Co4O23 I4/mmm (139) mp-1218682 [hull=0.028, PRIMARY]; Sr8Fe7CoO20 P1 (1) mp-1076165 [hull=0.004, PRIMARY]; Sr8Fe7CoO24 Pm-3m (221) mp-1077660 [hull=0.011, PRIMARY]
- papers: Synthesis, Crystal Chemistry, and Electrical Properties of the Intergrowth Oxides Sr4−xCaxFe6−yCoyO13+δ | Reducing the Cobalt Content in SrCo<sub>0.95</sub>Ti<sub>0.05</sub>O<sub>3-δ</sub>-Based Perovskites to Produce Cleaner Cathodes for IT-SOFCs | Electrical conductivity and oxygen nonstoichiometry of SrCo0.25Fe0.75O3-δ

## Cu-La-O-Sr
- rank 338 | 21 samples | 7 papers | 12 compositions
- compositions: La2Sr6Cu8O16 (3); La2Sr6Cu8O17.6 (3); La1.60Sr0.40CuO4 (3); La1.50Sr0.50CuO4 (3); La1.61Sr0.39Cu0.94Ti0.06O4 (2); La1.65Sr0.35CuO3.90 (1)
- dopant candidates (<5% at.): Ti (2), Mn (2), Ru (1), Fe (1)
- seed hypothesis (confirm): ruddlesden_popper
- measured range: 10-1072 K (5th-95th pct of 21 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2La6Cu3IrO16 C2/m (12) mp-1218814 [hull=0.070, PRIMARY]; Sr2La6TiCu3O16 Cmmm (65) mp-684769 [hull=0.063, PRIMARY]; Sr3La(CuO2)4 Pmc2_1 (26) mp-1218623 [hull=0.028, PRIMARY]; SrLa2(CuO3)2 I4/mmm (139) mp-1218240 [hull=0.041, PRIMARY]; SrLa3(Cu2O5)2 Pm (6) mp-1218269 [hull=0.027, PRIMARY]
- papers: Transport properties and crystal structures of new conductive copper oxides La2Sr6Cu8O16+δ (δ=0.0 and 1.6) | Thermoelectric power in single-layer copper oxides | Normal state properties of La2−xSrxCuO4 and La2SrCu2Oy

## Fe-Ni-O
- rank 339 | 21 samples | 10 papers | 12 compositions
- compositions: NiFe2O4 (9); Cd0.2Ni0.8Fe2O4 (2); Ni0.8Cu0.2 Fe2O4 (1); Cd0.1Ni0.9Fe2O4 (1); Ni0.8Cu0.2Fe2O4 (1); NiAl0.2Fe1.8O4 (1)
- dopant candidates (<5% at.): Cd (3), B (3), Cu (2), Al (1), Zn (1)
- seed hypothesis (confirm): spinel
- measured range: 299-944 K (5th-95th pct of 21 curves; full span incl. outliers 297-1273 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe2NiO4 Fd-3m (227) mp-24941 [hull=0.281, icsd=4, PRIMARY]; Fe(NiO2)2 Fd-3m (227) mp-640147 [hull=0.013, icsd=1, PRIMARY]; Fe11(NiO3)8 C2/m (12) mp-36806 [hull=0.153, PRIMARY]; Fe14Ni11O32 P1 (1) mp-705749 [hull=0.198, PRIMARY]; Fe13(NiO10)2 Cm (8) mp-1178589 [hull=0.072, PRIMARY]
- papers: Temperature-dependence thermoelectric power studies of mixed Ni–Cu nano ferrites | Tailored conductivity behavior in nanocrystalline nickel ferrite | DC resistivity and thermoelectric power in Ni-Cd ferrites

## Mo-Te
- rank 340 | 21 samples | 7 papers | 15 compositions
- compositions: MoTe2 (4); Mo3Te4 (2); Mo0.95Nb0.05Te2 (2); Mo0.93Nb0.07Te2 (2); Mo1Te2 (1); Mo0.92Nb0.08Te (1)
- dopant candidates (<5% at.): Nb (10), I (4)
- seed hypothesis (confirm): mos2_2h
- measured range: 10-825 K (5th-95th pct of 96 curves; full span incl. outliers 10-1055 K)
- [ref 1] TEDesignLab / ICSD: Te2Mo P6_3/mmc (194) mp-602 [hull=0.000, icsd=4, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Te4Mo3 R-3 (148) mp-8601 [hull=0.000, icsd=2, PRIMARY]; TeMo6 I4/mmm (139) mp-1105049 [hull=0.509, icsd=2, PRIMARY]; TeMo P6_3/mmc (194) mp-1120748 [hull=0.448, PRIMARY]; Te2Mo P2_1/m (11) mp-7459 [hull=0.016, icsd=1]; Te2Mo P-6m2 (187) mp-1025576 [hull=0.002]
- papers: Rich structural phase diagram and thermoelectric properties of layered tellurides Mo1−xNbxTe2 | Thermoelectric properties of perovskite type strontium ruthenium oxide | Thermoelectric properties of Mo3Te4

## Na-O-V
- rank 341 | 21 samples | 1 papers | 14 compositions
- compositions: Na0.83Ca0.17V2O5 (3); NaV2O5 (3); Na0.92V2O5 (2); Na0.96V2O5 (2); Na0.84V2O5 (2); Na0.9Ca0.1V2O5 (1)
- dopant candidates (<5% at.): Ca (7)
- seed hypothesis (confirm): vanadium_bronze
- measured range: 88-309 K (5th-95th pct of 21 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NaV2O5 Pmmn (59) mp-19111 [hull=0.025, icsd=12, PRIMARY]; NaVO3 C2/c (15) mp-19083 [hull=0.000, icsd=5, PRIMARY]; NaVO2 R-3m (166) mp-19391 [hull=0.000, icsd=3, PRIMARY]; NaV2O4 Pmmn (59) mp-783905 [hull=0.019, icsd=2, PRIMARY]; Na2VO4 P-1 (2) mp-1194140 [hull=0.114, icsd=1, PRIMARY, AMBIGUOUS]
- papers: Correlation and disorder effects for the electronic transport in the low-dimensional system NaxCa1−xV2O5and NaxV2O5

## Ni-Ti
- rank 342 | 21 samples | 5 papers | 11 compositions
- compositions: Ti50Ni50 (4); Ti49Ni51 (4); Ni50Ti50 (3); Ti49.3Ni50.7 (2); Ti49.6Ni50.4 (2); Ti48.4Ni51.6 (1)
- dopant candidates (<5% at.): Cu (2)
- seed hypothesis (confirm): b2_cscl
- measured range: 11-396 K (5th-95th pct of 61 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiNi P2_1/m (11) mp-1048 [hull=0.001, icsd=21, PRIMARY]; Ti2Ni Fd-3m (227) mp-1808 [hull=0.000, icsd=7, PRIMARY]; TiNi3 P6_3/mmc (194) mp-1409 [hull=0.000, icsd=7, PRIMARY]; Ti3Ni Pm-3m (221) mp-981209 [hull=0.127, PRIMARY, AMBIGUOUS]; TiNi4 R-3m (166) mp-1216809 [hull=0.380, PRIMARY]
- papers: Cu-substitution effect on thermoelectric properties of the TiNi-based shape memory alloys | Thermal and transport properties of as-grown Ni-rich TiNi shape memory alloys | Internal friction of Ti–Ni alloys

## Pb-S-Se
- rank 343 | 21 samples | 5 papers | 19 compositions
- compositions: Pb1.1234Se1S0.12Cl0.0068 (2); Pb1.1634Se1S0.16Cl0.0068 (2); PbS0.1Se0.9 (1); Pb1.004Se0.88S0.12Cl0.008 (1); Pb1Se0.88S0.12Bi0.003 (1); Pb1.003Se0.84S0.16Cl0.006 (1)
- dopant candidates (<5% at.): Cl (10), Cu (6), Bi (1)
- solid-solution axis: S/(S+Se) spans 0.10-0.60 (median 0.15) over 19 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 296-927 K (5th-95th pct of 77 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Pb2SeS R-3m (166) mp-1219926 [hull=0.004, PRIMARY]; Pb4Se3S P4/mmm (123) mp-1219970 [hull=0.011, PRIMARY]; Pb4SeS3 R-3m (166) mp-1219960 [hull=0.003, PRIMARY]; Pb2SeS P4/mmm (123) mp-1219943 [hull=0.016]
- papers: PbS/PbSe Hollow Spheres: Solvothermal Synthesis, Growth Mechanism, and Thermoelectric Transport Property | Thermoelectrics from Abundant Chemical Elements: High-Performance Nanostructured PbSe–PbS | High thermoelectric performance of n-type PbTe 1−y S y  due to deep lying states induced by indium doping and spinodal decomposition

## Sn-Te-Tl
- rank 344 | 21 samples | 6 papers | 13 compositions
- compositions: Tl4SnTe3 (4); Tl2SnTe3 (3); Tl7.95Sn2.05Te6 (2); Tl2SnTe5 (2); Tl9SnTe6 (2); Tl8.05Sn1.95Te6 (1)
- dopant candidates (<5% at.): Bi (2)
- seed hypothesis (confirm): tl5te3
- measured range: 102-688 K (5th-95th pct of 76 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Tl4SnTe3 I4/mcm (140) mp-3019 [hull=0.005, icsd=5, PRIMARY]; Tl2SnTe3 Pnma (62) mp-28662 [hull=0.000, icsd=1, PRIMARY]; Tl2SnTe5 I4/mcm (140) mp-28843 [hull=0.007, icsd=1, PRIMARY]; Tl9SnTe6 I4/m (87) mp-1216727 [hull=0.000, PRIMARY]
- papers: Improved Bulk Materials with Thermoelectric Figure-of-Merit Greater than 1: Tl10-xSnxTe6and Tl10-xPbxTe6 | Thermoelectric properties of ternary phases of thallium–tin–tellurium system | Thermoelectric properties of Tl–X–Te (X=Ge, Sn, and Pb) compounds with low lattice thermal conductivity

## Al-Ce-Ni
- rank 345 | 20 samples | 11 papers | 9 compositions
- compositions: CeNi2Al3 (5); CeNiAl4 (3); Ce(Ni0.9Cu0.1)2Al3 (3); CeNi2Al5 (3); CeNiAl (2); Ce(Ni1Cu0)2Al3 (1)
- dopant candidates (<5% at.): Cu (3), Co (3)
- measured range: 10-308 K (5th-95th pct of 33 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeAl5Ni2 Immm (71) mp-4817 [hull=0.000, icsd=4, PRIMARY]; CeAlNi P-62m (189) mp-11351 [hull=0.000, icsd=3, PRIMARY]; CeAl4Ni Cmcm (63) mp-30750 [hull=0.000, icsd=2, PRIMARY]; CeAl3Ni2 P6/mmm (191) mp-20338 [hull=0.000, icsd=1, PRIMARY]; CeAl2Ni Cmcm (63) mp-1206482 [hull=0.036, PRIMARY]
- papers: Mangnetoresistance Of Heavy Fermion-like Compound Ce(Ni1-xCux)2Al3 | Thermal conductivity of CeNiAl4 Kondo lattice | Magnetic, Thermal and Transport Properties of Ce(Ni1-xCux)2Al3: The Dominant Role of Electronic Change

## Al-Cu-Ru
- rank 346 | 20 samples | 6 papers | 12 compositions
- compositions: Al64.2Cu19.1Ru16.7_IQC (6); Al65Cu19Ru16_IQC (3); Al65Cu20Ru15 (2); Al64.5Cu20.6Ru14.9_IQC (1); Al64.2Cu19.1Ru16.7_IQC  (1); Al64.5Cu20.6Ru14.9_IQC  (1)
- seed hypothesis (confirm): quasicrystal_approximant
- measured range: 10-305 K (5th-95th pct of 13 curves; full span incl. outliers 10-949 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al7Cu2Ru P4/mnc (128) mp-1214866 [hull=0.000, PRIMARY]
- papers: Complex ɛ-phases in the Al–Pd-transition–metal systems: Towards a combination of an electrical conductor with a thermal insulator | Low Temperature Electronic Transport in Al–Cu–Ru Quasicrystalline Alloys | Modeling the electrical conductivity of icosahedral quasicrystals

## Ca-Co-La-O
- rank 347 | 20 samples | 10 papers | 6 compositions
- compositions: La0.7Ca0.3CoO3 (8); La0.6Ca0.4CoO3 (6); La0.5Ca0.5CoO3 (3); (Ca3Co4O9)32.03(La0.8Sr0.2CoO3)67.97 (1); (LaCo0.8Ni0.1Fe0.1O3)3.3(Ca3Co4O9)0.40 (1); La0.4Ca0.6CoO3 (1)
- dopant candidates (<5% at.): Sr (1), Ni (1), Fe (1)
- measured range: 11-1236 K (5th-95th pct of 30 curves; full span incl. outliers 10-1277 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaLa(CoO3)2 Fm-3m (225) mp-1227082 [hull=0.130, PRIMARY]; CaLa3(CoO4)2 Pm (6) mp-1227143 [hull=0.051, PRIMARY]
- papers: Nanostructured Complex Cobalt Oxides as Potential Materials for Solar Thermoelectric Power Generators | Correlation between the Structural Distortions and Thermoelectric Characteristics in La1−xAxCoO3(A = Ca and Sr) | Development of thermoelectric oxides for renewable energy conversion technologies

## Ce-Ge-Ni
- rank 348 | 20 samples | 9 papers | 10 compositions
- compositions: CeNi2Ge2 (7); CeNiGe2 (5); Ce(Ni0.88Pd0.12)2Ge2 (1); Ce(Ni0.94Pd0.06)2Ge2 (1); Ce2Ni3Ge5 (1); Ce3NiGe2 (1)
- dopant candidates (<5% at.): Pd (2), Si (2)
- seed hypothesis (confirm): thcr2si2_122
- measured range: 10-345 K (5th-95th pct of 33 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeNiGe2 Cmcm (63) mp-3541 [hull=0.000, icsd=5, PRIMARY]; Ce(NiGe)2 I4/mmm (139) mp-3325 [hull=0.000, icsd=4, PRIMARY]; Ce2NiGe3 P6/mmm (191) mp-1102475 [hull=0.007, icsd=2, PRIMARY]; CeNiGe Pnma (62) mp-20616 [hull=0.000, icsd=1, PRIMARY, AMBIGUOUS]; Ce5NiGe2 P4/ncc (130) mp-616173 [hull=0.052, icsd=1, PRIMARY]
- papers: Thermoelectric properties of Ce(Ni, Pd)2Ge2 at low temperatures below 1K | Thermal and electron transport properties of Ce2Ni3Ge5 and Ce3NiGe2: Example of Kondo behavior in the presence of the crystalline field effect | Anisotropic transport and magnetic properties of CeNi2Ge2

## Co-S-Sb
- rank 349 | 20 samples | 4 papers | 15 compositions
- compositions: Co0.92Ni0.08SbS (3); Co0.94Ni0.06SbS (3); CoSbS (2); Co0.98Ni0.02SbS (1); Co0.94Ni0.04SbS (1); Co0.96Ni0.04SbS (1)
- dopant candidates (<5% at.): Ni (11), Se (5), Mo (2)
- seed hypothesis (confirm): cosbs_paracostibite
- measured range: 297-902 K (5th-95th pct of 78 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CoSbS Pbca (61) mp-5881 [hull=0.000, icsd=5, PRIMARY]; CoSbS P2_13 (198) mp-1102443 [hull=0.010, icsd=1]; CoSbS Pmn2_1 (31) mp-4962 [hull=0.010, icsd=1]
- papers: The effect of nickel doping on electron and phonon transport in the n-type nanostructured thermoelectric material CoSbS | Electronic and thermoelectric properties of CoSbS and FeSbS | Modification of the intermediate band and thermoelectric properties in Se-doped CoSbS1−xSex compounds

## Cu-S-Sb-Se
- rank 350 | 20 samples | 5 papers | 12 compositions
- compositions: Cu12Sb3.6Bi0.4S10Se3 (8); Cu3Sb0.94Sn0.06Se3.5S0.5 (2); Cu3Sb0.97Ge0.03Se2.8S1.2 (1); Cu3Sb0.98Ge0.02Se3.2S0.8 (1); Cu3Sb0.98Ge0.02Se2.8S1.2 (1); Cu3Sb0.97Ge0.03Se3.2S0.8 (1)
- dopant candidates (<5% at.): Bi (8), Sn (7), Ge (4)
- seed hypothesis (confirm): tetrahedrite
- solid-solution axis: S/(S+Se) spans 0.12-0.85 (median 0.25) over 12 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 282-708 K (5th-95th pct of 74 curves)
- papers: High thermoelectric figure of merit in the Cu3SbSe4-Cu3SbS4 solid solution | Cu2HgSnSe4 nanoparticles: synthesis and thermoelectric properties | Phase Stability, Crystal Structure, and Thermoelectric Properties of Cu12Sb4S13–xSexSolid Solutions
