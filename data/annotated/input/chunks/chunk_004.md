# Host systems -- chunk 004 of 73

Ranks 151-200 by sample count. These 50 host systems cover 2145 samples (4.12% of the TE set); cumulative through this chunk: 67.91%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Bi-Sb-Se-Te
- rank 151 | 48 samples | 15 papers | 39 compositions
- compositions: Bi0.5Sb1.5Te2.7Se0.3 (5); BiSbTe1.5Se1.5 (3); Bi1.5Sb0.5Te1.7Se1.3 (3); Bi0.4Sb1.6Se0.6Te2.4 (2); Bi1.7Sb0.3Te0.67Se0.33 (1); (Bi0.5Sb0.5)2(Te0.9Se0.1)3  (1)
- dopant candidates (<5% at.): Ag (6), Zn (3), S (1)
- seed hypothesis (confirm): tetradymite
- solid-solution axis: Se/(Se+Te) spans 0.10-0.86 (median 0.33) over 39 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 13-575 K (5th-95th pct of 189 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi2Sb2(TeSe)3 R3m (160) mp-1227440 [hull=0.503, PRIMARY]
- papers: https://doi.org/10.1063/1.4754840 (Thermoelectric properties of p-type Bi0.5Sb1.5Te2.7Se0.3 fabricated by...) | https://doi.org/10.1021/ja909591x (Semiconductor Nanocrystals Functionalized with Antimony Telluride Zint...) | https://doi.org/10.1103/physrevb.75.195203 (Structures and thermoelectric properties of the infinitely adaptive se...)

## Fe-Ni-Sb-Ti
- rank 152 | 48 samples | 8 papers | 37 compositions
- compositions: Ti2FeNiSb2 (3); Fe0.55Ni0.45TiSb (2); Ti2Fe1Ni1Sb2 (2); Ti2FeNiSb1.8Sn0.2 (2); Fe0.5Ni0.5TiSb (2); TiFe0.5Co0.15Ni0.35Sb (2)
- dopant candidates (<5% at.): Sn (5), Co (5), Hf (3), Cu (1)
- seed hypothesis (confirm): quaternary_heusler
- measured range: 294-975 K (5th-95th pct of 205 curves; full span incl. outliers 11-985 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti2FeNiSb2 R3m (160) mp-1217120 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1007/s11664-011-1517-0 (An Alternative Approach to Improve the Thermoelectric Properties of Ha...) | https://doi.org/10.1002/adfm.201905044 (Design of High‐Performance Disordered Half‐Heusler Thermoelectric Mate...) | https://doi.org/10.1016/j.joule.2019.04.003 (Double Half-Heuslers)

## Fe-O-Sm
- rank 153 | 48 samples | 7 papers | 21 compositions
- compositions: Sm0.95Ce0.05FeO3 (7); Sm0.95Ba0.05Fe0.95Ru0.05O3 (4); Sm0.95Ce0.05Fe0.93Ni0.07O3 (3); Sm0.95Ce0.05Fe0.9Ni0.1O3 (3); Sm0.95Ce0.05Fe0.99Ni0.01O3 (3); Sm0.95Ce0.05Fe0.97Ni0.03O3 (2)
- dopant candidates (<5% at.): Ce (42), Ni (13), Co (10), Cr (10), Ba (4), Ru (4), Ca (1)
- measured range: 296-1274 K (5th-95th pct of 48 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SmFeO3 Pnma (62) mp-24989 [hull=0.000, icsd=9, PRIMARY]; Sm3FeO6 Cmc2_1 (36) mp-1105484 [hull=0.000, icsd=1, PRIMARY]; Sm3Fe5O12 Ia-3d (230) mp-19686 [hull=0.004, icsd=1, PRIMARY]; Sm(FeO2)2 R3m (160) mp-793791 [hull=0.059, PRIMARY]; Sm2Fe2O5 Ima2 (46) mp-1076463 [hull=0.117, PRIMARY]
- papers: https://doi.org/10.1039/c6ra02251k (Evaluation of Sm<sub>0.95</sub>Ba<sub>0.05</sub>Fe<sub>0.95</sub>Ru<su...) | https://doi.org/10.1016/j.snb.2010.12.057 (Electrical conductivity dependence of Ni doped Sm0.95Ce0.05FeO3− on su...) | https://doi.org/10.1016/j.ssi.2010.01.017 (Effect of cobalt substitution on thermal stability and electrical cond...)

## C-H-O-S
- rank 154 | 47 samples | 10 papers | 25 compositions
- compositions: C14H14O5S2 (14); (C14H14O5S2)68.3(C2H6SO)31.7 (4); (C14H14O5S2)78.32(C2H6O2)21.68 (4); (C14H14O5S2)81.98(C2H6SO)18.02 (4); (C14H14O5S2)39.81(Ag)60.19 (1); (C14H14O5S2)48.56(Ag)51.44 (1)
- dopant candidates (<5% at.): Ag (7), Bi (6), Te (5), In (4), Se (3), Sb (1), Cu (1), Sn (1)
- seed hypothesis (confirm): organic_polymer
- measured range: 101-399 K (5th-95th pct of 171 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlH20C2S2NO14 Pc (7) mp-708992 [hull=0.056, icsd=4, PRIMARY]; H6C2SO4 C2/c (15) mp-1192689 [hull=0.278, icsd=2, PRIMARY]; BeH24C8S4(ClO2)2 Pbca (61) mp-1199791 [hull=0.137, icsd=1, PRIMARY]; CdH20C4S4(NO6)2 P-1 (2) mp-24273 [hull=0.201, icsd=1, PRIMARY]; BiH25C8(SO2)6 P-1 (2) mp-1200655 [hull=0.213, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/s40843-016-5132-8 (Ultralight conducting PEDOT:PSS/carbon nanotube aerogels doped with si...) | https://doi.org/10.1021/acs.iecr.4c00866 (High Energy Electron Beam as an Effective Method for Molecular Modific...) | https://doi.org/10.1002/eem2.12824 (Nanoscale Electron Beam Patterning of <scp>PEDOT</scp>:<scp>PSS</scp> ...)

## Ba-Co-Nd-O
- rank 155 | 46 samples | 7 papers | 36 compositions
- compositions: NdBa0.94La0.06Co2O5.55 (3); NdBa0.94La0.06Co2O5.48 (3); NdBa0.94La0.06Co2O5.5 (3); NdBaCo2O5.5 (2); NdBaCo2O5.72 (2); NdBaCo2O5.55 (2)
- dopant candidates (<5% at.): Ca (10), La (9)
- seed hypothesis (confirm): layered_double_perovskite
- measured range: 10-399 K (5th-95th pct of 88 curves; full span incl. outliers 10-1125 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaNdCo2O5 Pmmm (47) mp-24853 [hull=0.047, icsd=5, PRIMARY, AMBIGUOUS]; Ba2Nd2Co4O11 Pmmm (47) mp-24879 [hull=0.054, icsd=5, PRIMARY]; BaNd(CoO3)2 P4/mmm (123) mp-1079144 [hull=0.092, icsd=2, PRIMARY]; BaNd2CoO5 Immm (71) mp-19118 [hull=0.035, icsd=1, PRIMARY]; Ba3Nd3(Co3O8)2 C2/m (12) mp-1228415 [hull=0.048, PRIMARY]
- papers: https://doi.org/10.1007/s12034-008-0137-7 (A novel method to control oxygen stoichiometry and thermoelectric prop...) | https://doi.org/10.1016/j.jallcom.2015.04.219 (Impact of charge doping, oxygen disorder and hydrostatic pressure on t...) | https://doi.org/10.1103/physrevb.73.121101 (Origin of the large thermoelectric power in oxygen-variableRBaCo2O5+x(...)

## Bi-Cu-O-Sr
- rank 156 | 46 samples | 14 papers | 26 compositions
- compositions: Bi2Sr2Ca0.5Y0.5Cu2O8 (5); Bi2Sr2Ca0.6Ce0.4Cu2O8 (3); (Bi1.74Pb0.38)Sr1.88CuO6 (3); Bi2Sr2Ca0.6Y0.4Cu2O8 (3); Bi2Sr2CuO5 (3); Bi2Sr2Ca0.7Ce0.3Cu2O8 (2)
- dopant candidates (<5% at.): Ca (17), Y (10), La (8), Pb (6), Ce (5), Cd (2)
- seed hypothesis (confirm): bscco_cuprate
- measured range: 10-742 K (5th-95th pct of 59 curves; full span incl. outliers 10-978 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr10Cu5Bi10O29 P1 (1) mp-667638 [hull=0.068, PRIMARY, AMBIGUOUS]; Sr4Cu2Bi4O13 C2 (5) mp-1218715 [hull=0.121, PRIMARY]; Sr10Cu5Bi10O29 C2 (5) mp-652781 [hull=0.072]
- papers: https://doi.org/10.1088/0953-8984/10/39/019 (Thermoelectric power of the system) | https://doi.org/10.1016/0038-1098(91)90232-k (Thermoelectric study of PbxBi2-xSr2Ca2Cu3Oy superconductors) | https://doi.org/10.1088/0953-8984/9/44/016 (Thermoelectric power of single crystals)

## Co-Nd-O-Sr
- rank 157 | 46 samples | 12 papers | 19 compositions
- compositions: Nd0.75Sr1.25CoO4 (9); Nd0.5Sr0.5CoO3 (4); Nd0.75Sr0.25CoO3 (3); SrNdCoO4 (3); Nd0.6Sr0.4CoO3 (3); Sr1.05Nd0.95CoO4 (3)
- dopant candidates (<5% at.): Cu (4), Fe (2)
- seed hypothesis (confirm): ruddlesden_popper
- measured range: 11-1222 K (5th-95th pct of 46 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr3Nd(CoO4)2 Amm2 (38) mp-1218466 [hull=0.002, PRIMARY]; SrNd(CoO3)2 Imm2 (44) mp-1218211 [hull=0.029, PRIMARY]; SrNdCoO4 I4mm (107) mp-1218151 [hull=0.026, PRIMARY]; SrNdCoO4 Cmcm (63) mp-1218146 [hull=0.043]
- papers: https://doi.org/10.1016/j.jallcom.2003.09.152 (Heat conductivity and thermopower of Nd1−xSrxCoO3 ceramic) | https://doi.org/10.1088/0022-3727/40/17/029 (The magnetic, electrical and thermal transport studies in the layered ...) | https://doi.org/10.1088/0022-3727/41/21/215009 (Structural, magnetic, electrical and thermal transport properties in t...)

## Cu-Ni
- rank 158 | 46 samples | 11 papers | 20 compositions
- compositions: Cu40Ni60 (9); Cu0.25Ni0.75 (9); Cu56Ni42Mn2 (5); Cu56Ni42Mn2Se (4); Cu0.15Ni0.85 (3); Cu0.55Ni0.45 (2)
- dopant candidates (<5% at.): Mn (14), Se (10), C (2), O (1), Al (1), Ti (1), Zn (1)
- seed hypothesis (confirm): solid_solution_alloy
- measured range: 299-1082 K (5th-95th pct of 102 curves; full span incl. outliers 15-1086 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu3Ni Cmmm (65) mp-1225698 [hull=0.051, PRIMARY]; CuNi R-3m (166) mp-1225687 [hull=0.011, PRIMARY]; CuNi3 I4/mmm (139) mp-1184054 [hull=0.031, PRIMARY]; CuNi P-6m2 (187) mp-1184069 [hull=0.028]; CuNi Cmmm (65) mp-1225695 [hull=0.066]
- papers: https://doi.org/10.1016/0013-7480(70)90070-7 (Electrical and thermoelectric properties of some metallic thermoelectr...) | https://doi.org/10.1016/s0925-8388(03)00295-0 (Thermoelectric properties of constantan/spherical SiO2 and Al2O3 parti...) | https://doi.org/10.1063/1.1569432 (Thermoelectric properties of electrodeposited CuNi alloys on Si)

## Hf-Ni-Sn-Ti
- rank 159 | 46 samples | 14 papers | 35 compositions
- compositions: Ti0.5Hf0.5NiSn (5); Ti0.8Hf0.2NiSn (4); Ti0.6Hf0.4NiSn (3); Ti0.7Hf0.3NiSn (2); Ti0.8Hf0.2NiSn0.99Sb0.01 (2); Ti0.8Hf0.2NiSn0.993Sb0.007 (1)
- dopant candidates (<5% at.): Sb (6), Zr (1)
- solid-solution axis: Hf/(Hf+Ti) spans 0.17-0.83 (median 0.50) over 35 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 290-962 K (5th-95th pct of 148 curves; full span incl. outliers 285-1077 K)
- papers: https://doi.org/10.1016/j.intermet.2006.08.008 (High temperature thermoelectric properties of TiNiSn-based half-Heusle...) | https://doi.org/10.1039/c5tc02025e (Compositions and thermoelectric properties of XNiSn (X = Ti, Zr, Hf) h...) | https://doi.org/10.1016/j.stam.2004.02.006 (Enhancement of high temperature thermoelectric properties of intermeta...)

## Mn-O-Pr-Sr
- rank 160 | 46 samples | 13 papers | 16 compositions
- compositions: Pr0.5Sr0.5MnO3 (18); Pr0.6Sr0.4MnO3 (6); Pr0.7Sr0.3MnO3 (3); Pr0.67Sr0.33MnO3 (3); Pr0.45Bi0.15Sr0.4MnO3 (3); Pr0.65Ca0.1Sr0.25MnO3 (2)
- dopant candidates (<5% at.): Bi (5), Ca (4), Ag (1), La (1)
- seed hypothesis (confirm): perovskite
- measured range: 10-875 K (5th-95th pct of 70 curves; full span incl. outliers 10-1296 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2PrMn3O9 C2/c (15) mp-1218779 [hull=0.003, PRIMARY]; Sr3PrMn2O8 Amm2 (38) mp-1218451 [hull=0.000, PRIMARY]; Sr3PrMn4O12 Amm2 (38) mp-1218481 [hull=0.005, PRIMARY, AMBIGUOUS]; Sr4Pr6Mn9BiO30 Pm (6) mp-1173250 [hull=0.028, PRIMARY]; Sr4PrMn5O15 C2/m (12) mp-1218591 [hull=0.023, PRIMARY]
- papers: https://doi.org/10.1063/1.2992521 (Magnetotransport, thermoelectric power, thermal conductivity and speci...) | https://doi.org/10.2320/jinstmet.ja201516 (P-Type Thermoelectric Properties of Pr<sub>1&minus;<i>x</i></sub>Sr<su...) | https://doi.org/10.1016/j.jallcom.2007.11.046 (Electrical resistivity, thermoelectric power and electron spin resonan...)

## Bi-Pb-Te
- rank 161 | 45 samples | 14 papers | 24 compositions
- compositions: PbBi4Te7 (7); PbBi2Te4 (6); PbBi3.94Cd0.06Te7 (4); PbBi6Te10 (3);  PbBi2Te4 (3); Bi0.25Pb0.75Te (3)
- dopant candidates (<5% at.): Cd (7), Cu (4), Ag (2), Sn (2), Se (1)
- seed hypothesis (confirm): homologous_tetradymite
- measured range: 38-800 K (5th-95th pct of 106 curves; full span incl. outliers 28-852 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi4Te7Pb P-3m1 (164) mp-23005 [hull=0.000, icsd=3, PRIMARY]; Bi2Te4Pb R-3m (166) mp-676250 [hull=0.001, icsd=1, PRIMARY]; Bi6Te10Pb R-3m (166) mp-1106025 [hull=0.210, icsd=1, PRIMARY]; Bi3Te5Pb P3m1 (156) mp-1227656 [hull=0.235, PRIMARY]; Bi2Te4Pb R3m (160) mp-1227398 [hull=0.184]
- papers: https://doi.org/10.1023/b:inma.0000027590.43038.a8 (Crystal Structures and Thermoelectric Properties of Layered Compounds ...) | https://doi.org/10.1023/b:inma.0000027591.50936.18 (Thermoelectric Properties of Cation-Substituted Solid Solutions Based ...) | https://doi.org/10.1023/b:inma.0000048211.53027.e7 (Thermoelectric Properties of PbBi4Te7-Based Anion-Substituted Layered ...)

## Ca-O-Ru
- rank 162 | 45 samples | 16 papers | 8 compositions
- compositions: CaRuO3 (16); Ca2RuO4 (13); Ca3(Ru0.995Ti0.005)2O7 (10); CaRu0.8Ga0.2O3 (2); Ca0.8Sr0.2RuO3 (1); Ca1.91Sr0.09RuO4 (1)
- dopant candidates (<5% at.): Ti (10), Sr (4), Ga (2)
- seed hypothesis (confirm): ruddlesden_popper
- measured range: 10-1028 K (5th-95th pct of 73 curves; full span incl. outliers 10-1264 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaRuO3 Pnma (62) mp-20947 [hull=0.000, icsd=20, PRIMARY]; Ca2RuO4 Pbca (61) mp-21466 [hull=0.014, icsd=12, PRIMARY]; Ca3Ru2O7 Cmc2_1 (36) mp-3258 [hull=0.003, icsd=8, PRIMARY]; Ca3(Ru2O7)2 R-3m (166) mp-1227743 [hull=0.096, PRIMARY]; Ca2RuO4 Cmce (64) mp-4208 [hull=0.032, icsd=2]
- papers: https://doi.org/10.1016/j.jallcom.2012.01.150 (Thermoelectric properties of Ca1−xSrxRuO3 compounds prepared by spark ...) | https://doi.org/10.1016/j.mseb.2008.12.026 (Thermoelectric properties of alkaline earth ruthenates prepared by SPS) | https://doi.org/10.2320/matertrans.mra2007055 (Preparations of CaRuO<SUB>3</SUB> Body by Plasma Sintering and Its The...)

## Cu-Gd-O-Ru-Sr
- rank 163 | 45 samples | 8 papers | 22 compositions
- compositions: RuSr2GdCu2O8 (17); RuSr2(Gd1.5Ce0.5)Cu2O10 (3); RuSr2Gd1.4Ce0.6Cu2O10 (2); Ru(Sr0.99La0.01)2GdCu2O8 (2); RuSr2GdCu2O8  (2); Ru(Sr0.95La0.05)2GdCu2O8 (2)
- dopant candidates (<5% at.): La (7), Ce (5), Ti (4), Rh (4), Sn (3), Na (3)
- seed hypothesis (confirm): ruthenocuprate
- measured range: 11-324 K (5th-95th pct of 54 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2GdCu2RuO8 P4/mbm (127) mp-1194240 [hull=0.022, icsd=1, PRIMARY]; Sr2GdCu2RuO8 P4/mmm (123) mp-1104173 [hull=0.050, icsd=1]; Sr2GdCu2RuO8 Amm2 (38) mp-1218868 [hull=0.050]
- papers: https://doi.org/10.1063/1.2784962 (Magnetothermopower and magnetoresistivity of RuSr2Gd2−xCexCu2O10+δ (x=...) | https://doi.org/10.1063/1.2163276 (Transport, thermal, and magnetic properties of RuSr2(Gd1.5Ce0.5)Cu2O10...) | https://doi.org/10.1080/14786435.2010.529091 (Thermoelectric power factor of RuSr2GdCu2O8)

## Fe-Ni-Sb
- rank 164 | 45 samples | 12 papers | 38 compositions
- compositions: Ba0.03Sr0.01(Nd0.9513Pr0.0487)0.10Yb0.02Fe2.4Ni1.6Sb12 (3); Ce0.05Yb0.12Fe2.08Ni1.92Sb12 (2); Pr0.1Fe2Ni2Sb12 (2); Sm0.7Fe2.8Ni1.2Sb12.8 (2); Pr0.21Fe2.5Ni1.5Sb12 (2); (Pr0.0487Nd0.9513)0.46(Fe0.75Ni0.25)4Sb12 (2)
- dopant candidates (<5% at.): Yb (24), Pr (23), Nd (19), Ba (13), Sr (9), Ce (8), Tl (4), Sm (2)
- seed hypothesis (confirm): skutterudite, filled_skutterudite  <-- MIXED, split per composition
- measured range: 13-820 K (5th-95th pct of 138 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe3NiSb8 P2/m (10) mp-1224765 [hull=0.018, PRIMARY]; FeNiSb4 P2/m (10) mp-1224810 [hull=0.021, PRIMARY]; FeNiSb6 C2/m (12) mp-1224908 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2009.06.005 (Thermoelectric properties of novel skutterudites with didymium: DDy(Fe...) | https://doi.org/10.1016/j.jallcom.2012.04.121 (Thermoelectric properties of p-type didymium (DD) based skutterudites ...) | https://doi.org/10.1016/j.jallcom.2013.09.051 (Preparation and thermoelectric properties of p-type filled skutterudit...)

## In-O-Sn
- rank 165 | 45 samples | 4 papers | 19 compositions
- compositions: (SnO2)5(In2O3)3 (7); In4Sn3O12 (6); (In0.975Y0.025)4Sn3O12 (4); In4Sn3.6Ti0.4O12 (3); In3.6Y0.4Sn3O12 (3); In3.95Y0.05Sn3O12 (2)
- dopant candidates (<5% at.): Y (13), Ti (11), Ga (4), Sb (1), Zn (1)
- seed hypothesis (confirm): bixbyite
- measured range: 77-1267 K (5th-95th pct of 65 curves; full span incl. outliers 18-1272 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): In15SnO24 R-3 (148) mp-867998 [hull=0.000, PRIMARY, AMBIGUOUS]; In2Sn2O7 Fd-3m (227) mp-755027 [hull=0.092, PRIMARY]; In4(SnO4)3 P-1 (2) mp-676320 [hull=0.039, PRIMARY, AMBIGUOUS]; In15SnO24 C2 (5) mp-766006 [hull=0.001]; In4(SnO4)3 P1 (1) mp-673669 [hull=0.039]
- papers: https://doi.org/10.1111/j.1551-2916.2011.04650.x (Enhanced Densification and Thermoelectric Performance of In4Sn3O12 by ...) | https://doi.org/10.1006/jssc.2000.8781 (Structure and Thermoelectric Properties of Me-Substituted In4Sn3O12, M...) | https://doi.org/10.14723/tmrsj.41.101 (Substitution effect of tetravalent and pentavalent elements on thermoe...)

## Nb-O
- rank 166 | 45 samples | 14 papers | 21 compositions
- compositions: Nb2O5 (11); Nb12O29 (7); NbO (5); NbO2 (4); NbO0.8 (2); (W1.083O3)0.08(Nb2.1O5)0.92 (1)
- dopant candidates (<5% at.): Ti (5), W (4), C (4), N (1), Si (1), Ag (1), Sm (1), Eu (1), Gd (1), Dy (1), Ho (1), Er (1)
- seed hypothesis (confirm): magneli_phase, block_shear_niobate  <-- MIXED, split per composition
- measured range: 14-1197 K (5th-95th pct of 85 curves; full span incl. outliers 10-1384 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NbO Pm-3m (221) mp-2311 [hull=0.000, icsd=6, PRIMARY]; NbO2 I4_1/a (88) mp-821 [hull=0.005, icsd=6, PRIMARY]; Nb2O5 C2/c (15) mp-604 [hull=0.019, icsd=4, PRIMARY]; Nb12O29 Cmcm (63) mp-1470 [hull=0.000, icsd=2, PRIMARY]; NaNb6O15F Amm2 (38) mp-8084 [hull=0.059, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.4931161 (Single-step preparation and consolidation of reduced early-transition-...) | https://doi.org/10.1007/s00339-014-8515-z (Semiconducting large bandgap oxides as potential thermoelectric materi...) | https://doi.org/10.1088/0953-8984/27/11/115501 (Vacancy filling effect in thermoelectric NbO)

## Ni
- rank 167 | 45 samples | 13 papers | 29 compositions
- compositions: Ni (16); Pt0.05Ni (2); NiCr0.0051 (1); NiFe0.0063 (1); NiFe0.0024 (1); NiCr0.0012 (1)
- dopant candidates (<5% at.): Fe (6), Cr (4), Si (4), Mn (3), Co (3), Pd (2), Ti (2), Pt (2), Cu (1), V (1), K (1)
- seed hypothesis (confirm): solid_solution_alloy
- measured range: 10-834 K (5th-95th pct of 63 curves; full span incl. outliers 10-1271 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ni Fm-3m (225) mp-23 [hull=0.000, icsd=24, PRIMARY]; Ni P6_3/mmc (194) mp-10257 [hull=0.027, icsd=1]; Ni Im-3m (229) mp-1008728 [hull=0.098, icsd=1]; Ni P-3m1 (164) mp-1014111 [hull=0.600]; Ni P6/mmm (191) mp-1094136 [hull=0.796]
- papers: https://doi.org/10.1007/bf03159747 (Thermoelectric power and electrical resistivity of some Ni-Based alloy...) | https://doi.org/10.1088/0022-3719/3/1/016 (The thermoelectric power of nickel and its alloys) | https://doi.org/10.1063/1.3167302 (Size-dependent thermopower in nanocrystalline nickel)

## O-Zr
- rank 168 | 45 samples | 18 papers | 28 compositions
- compositions: ZrO2 (7); (ZrO2)95.47(Y2O3)4.53 (5); Y0.08Zr0.94O2 (3); Y0.09Zr0.93O2 (2); Gd0.09Y0.13Zr0.84O2 (2); (Y2O3)4.2(ZrO2)95.8 (2)
- dopant candidates (<5% at.): Y (35), Gd (4), P (3), Ca (3), Sr (3), Ti (3), Hf (2), Er (2), Sm (1), Eu (1), Tb (1), Dy (1), Lu (1), Nd (1), Ni (1), Co (1), Cr (1), Al (1)
- seed hypothesis (confirm): fluorite_oxide
- measured range: 65-1499 K (5th-95th pct of 53 curves; full span incl. outliers 11-2065 K)
- [ref 1] TEDesignLab / ICSD: ZrO2 P2_1/c (14) mp-2858 [hull=0.000, icsd=46, PRIMARY]; ZrO2 P4_2/nmc (137) mp-2574 [hull=0.037, icsd=48]; ZrO2 Fm-3m (225) mp-1565 [hull=0.070, icsd=17]; ZrO2 Pnma (62) mp-755089 [hull=0.023, icsd=5]; ZrO2 Pbca (61) mp-776404 [hull=0.010, icsd=2]
- [ref 2] MP, ranked by ICSD evidence: Zr3O P6_322 (182) mp-1017 [hull=0.004, icsd=3, PRIMARY]; ZrO Fm-3m (225) mp-10197 [hull=0.347, icsd=1, PRIMARY]; Zr2O Pn-3m (224) mp-10735 [hull=0.227, icsd=1, PRIMARY]; Zr11VO24 P1 (1) mp-861249 [hull=0.022, PRIMARY]; Zr27O49 P3m1 (156) mp-684977 [hull=0.117, PRIMARY]
- papers: https://doi.org/10.1038/srep03449 (Enhanced thermoelectric performance of Nb-doped SrTiO3 by nano-inclusi...) | https://doi.org/10.1016/j.scriptamat.2019.12.006 (Multicomponent high-entropy zirconates with comprehensive properties f...) | https://doi.org/10.1063/1.357390 (Superconducting fast microbolometers operating below their critical te...)

## As-Te
- rank 169 | 44 samples | 7 papers | 12 compositions
- compositions: As2Te3 (24); As1.965Bi0.035Te3 (4); As1.983Bi0.017Te3 (2); As1.976Bi0.024Te3 (2); As1.975Bi0.025Te3 (2); As1.95Sn0.05Te3 (2)
- dopant candidates (<5% at.): Bi (12), Sn (6)
- seed hypothesis (confirm): tetradymite
- measured range: 10-522 K (5th-95th pct of 127 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Te3As2 C2/m (12) mp-484 [hull=0.000, icsd=4, PRIMARY]; TeAs Fm-3m (225) mp-10051 [hull=0.118, icsd=1, PRIMARY]; Te7As6 Cmmm (65) mp-1211390 [hull=1.265, PRIMARY]; TeAs2 I4_1/amd (141) mp-1217320 [hull=0.214, PRIMARY]; Te3As2 R-3m (166) mp-9897 [hull=0.011, icsd=2]
- papers: https://doi.org/10.1039/c3ta11159h (A comprehensive study of the crystallization of Cu–As–Te glasses: micr...) | https://doi.org/10.1063/1.4950947 (High-temperature thermoelectric properties of the β-As2−xBixTe3solid s...) | https://doi.org/10.1007/s11664-015-4063-3 (Thermoelectric Properties of the α-As2Te3 Crystalline Phase)

## Ba-Cu-O-Pr
- rank 170 | 44 samples | 12 papers | 17 compositions
- compositions: PrBa2Cu3O7 (12); Pr2Ba4Cu7O15 (6); (Pr0.7Y0.3)1.06Ba1.94Cu3O7 (5); Pr1.06Ba1.94Cu3O7 (5); PrBa2(Cu0.8Zn0.2)3O7 (2); PrBa2(Cu0.8Ga0.2)3O7 (2)
- dopant candidates (<5% at.): Y (7), Ga (3), Zn (2), Ni (1), Al (1)
- seed hypothesis (confirm): ybco_cuprate
- measured range: 11-1183 K (5th-95th pct of 42 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba2Pr(CuO2)4 Cmmm (65) mp-6779 [hull=0.000, icsd=5, PRIMARY]; Ba2PrCu3O7 Pmmm (47) mp-20936 [hull=0.016, icsd=5, PRIMARY]; BaPr2CuO5 P4/mbm (127) mp-20212 [hull=0.024, icsd=2, PRIMARY]; Ba2PrCu3O8 P4/mmm (123) mp-614964 [hull=0.045, icsd=1, PRIMARY]; Ba10Pr4Y(CuO2)20 Cmmm (65) mp-1229131 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1063/1.112551 (Two‐band hopping conductivity in the nonmetallic barrier material PrBa...) | https://doi.org/10.1016/j.physc.2012.05.008 (Magnetization and transport properties in the superconducting Pr2Ba4Cu...) | https://doi.org/10.1016/s0921-4534(02)02501-7 (Thermal transport of Pr2Ba4Cu7O15−y compound with alternative repetiti...)

## Ba-La-Mn-O
- rank 171 | 44 samples | 16 papers | 21 compositions
- compositions: La0.7Ba0.3MnO3 (16); La0.67Ba0.33MnO3 (4); La0.67Ba0.33Mn0.98Sb0.02O3 (3); La0.67Ba0.33Mn0.97Sb0.03O3 (2); La0.75Ba0.25MnO3 (2); La0.67Ba0.33Mn0.95Sb0.05O3 (2)
- dopant candidates (<5% at.): Sb (8), Al (3), Cr (3), Sm (2), Fe (1), Er (1), Ti (1), Rb (1)
- seed hypothesis (confirm): perovskite
- measured range: 15-460 K (5th-95th pct of 46 curves; full span incl. outliers 11-1215 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaLaMn2O6 P4/mmm (123) mp-19245 [hull=0.010, icsd=8, PRIMARY]; Ba2La2Mn4O11 Cmmm (65) mp-1214651 [hull=0.000, PRIMARY]; Ba2La4Mn5SnO18 P1 (1) mp-743694 [hull=0.035, PRIMARY]; Ba4La8Mn11SnO36 P1 (1) mp-743838 [hull=0.026, PRIMARY]; Ba2LaMn2O7 I4/mmm (139) mp-1228437 [hull=0.006, PRIMARY]
- papers: https://doi.org/10.3740/mrsk.2008.18.4.175 (High-Temperature Electrical Transport and Thermoelectric Properties of...) | https://doi.org/10.1016/j.ssc.2007.09.022 (Magnetotransport and thermoelectric power of La2/3Ba1/3Mn1−xSbxO3 (x=0...) | https://doi.org/10.1016/j.cplett.2019.04.021 (Impact of aluminum on the Seebeck coefficient and magnetic properties ...)

## Bi-Sb-Se
- rank 172 | 44 samples | 9 papers | 26 compositions
- compositions: BiSb(Se0.94Br0.06)3 (9); BiSbSe3 (4); BiSb(Se0.96Br0.04)3 (2); BiSb(Se0.98Br0.02)3 (2); BiSb(Se0.92Br0.08)3 (2); Bi5.6Sb2.4Se7 (2)
- dopant candidates (<5% at.): Br (15), Pb (5), Cl (4)
- seed hypothesis (confirm): stibnite
- solid-solution axis: Bi/(Bi+Sb) spans 0.20-0.90 (median 0.75) over 26 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-801 K (5th-95th pct of 222 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BiSbSe3 Pnma (62) mp-1227508 [hull=0.014, PRIMARY]
- papers: https://doi.org/10.1109/ict.2006.331340 (Electronic Properties of Low-Temperature Thermoelectric Materials: Sel...) | https://doi.org/10.1063/1.1904158 (n-type to p-type crossover in quaternary BixSbyPbzSe3 single crystals) | https://doi.org/10.1007/s11664-013-2496-0 (Effect of Se Substitution on Structural and Electrical Transport Prope...)

## Ce-Cu-Si
- rank 173 | 44 samples | 11 papers | 10 compositions
- compositions: CeCu2Si2 (30); CeCu2.02Si1.98 (3); CeCu2.05Si2 (3); Ce0.8La0.2Cu2.05Si2 (2); Ce0.9La0.1Cu2Si2 (1); Ce(Ni0.12Cu0.88)2Si2 (1)
- dopant candidates (<5% at.): La (6), Ni (1), Y (1)
- seed hypothesis (confirm): thcr2si2_122
- measured range: 10-315 K (5th-95th pct of 40 curves; full span incl. outliers 10-399 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(CuSi)2 I4/mmm (139) mp-5452 [hull=0.000, icsd=21, PRIMARY]; CeCuSi P6_3/mmc (194) mp-22740 [hull=0.000, icsd=6, PRIMARY]; CeCuSi2 Cmcm (63) mp-1080057 [hull=0.031, icsd=1, PRIMARY]; CeCu2Si Cmcm (63) mp-1213794 [hull=0.031, PRIMARY]; Ce2CuSi3 P-6m2 (187) mp-1226885 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2013.06.080 (Competing energy scales in the compounds Ce(Ni1−xCux)2(Si2)) | https://doi.org/10.1007/bf00681517 (Electric and magnetic properties of the Kondo-lattice compound CeCu2Si2) | https://doi.org/10.1016/0304-8853(85)90348-8 (High-pressure transport coefficients of the heavy-fermion superconduct...)

## La-O-Ti
- rank 174 | 44 samples | 9 papers | 19 compositions
- compositions: Sr0.1La0.6TiO3 (8); Sr0.2La0.52Ti0.95Nb0.05O3 (4); LaTiO3 (4); Sr0.2La0.52Ti1O3 (4); La2Ti2O7 (3); Sr0.2La0.52Ti0.85Nb0.15O3 (3)
- dopant candidates (<5% at.): Sr (29), Nb (11), Y (2), Cr (2), Ta (2)
- seed hypothesis (confirm): perovskite
- measured range: 14-1068 K (5th-95th pct of 54 curves; full span incl. outliers 11-1140 K)
- [ref 1] TEDesignLab / ICSD: La2Ti2O7 Fd-3m (227) mp-4423 [hull=0.050, icsd=2, PRIMARY]; La4Ti3O12 R-3 (148) mp-3249 [hull=0.037, icsd=1, PRIMARY]; La2Ti2O7 Cmc2_1 (36) mp-8154 [hull=0.010, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: LaTiO3 Pnma (62) mp-22013 [hull=0.026, icsd=12, PRIMARY]; La2TiO5 Pnma (62) mp-18051 [hull=0.000, icsd=5, PRIMARY]; La5Ti4O15 P-3c1 (165) mp-28801 [hull=0.066, icsd=1, PRIMARY]; La5Ti5O17 Pmn2_1 (31) mp-29045 [hull=0.006, icsd=1, PRIMARY]; LaTiO3 Pm-3m (221) mp-8020 [hull=0.069, icsd=1]
- papers: https://doi.org/10.1039/c4ra13945c (Thermoelectric properties of sol–gel derived lanthanum titanate ceramics) | https://doi.org/10.1021/acs.chemmater.5b04616 (High-Figure-of-Merit Thermoelectric La-Doped A-Site-Deficient SrTiO3Ce...) | https://doi.org/10.1103/physrevb.71.184431 (Evidence for two electronic phases inY1−xLaxTiO3from thermoelectric an...)

## Mn-Te
- rank 175 | 44 samples | 13 papers | 33 compositions
- compositions: MnTe (11); Mn0.92Te0.96(Ag2S)0.04 (2); Mn0.50Te0.50 (1); Mn0.49Te0.51 (1); Mn0.52Te0.48 (1); Mn0.51Te0.49 (1)
- dopant candidates (<5% at.): Ag (10), S (6), Se (4), Sb (4), Sn (4), Cu (3)
- seed hypothesis (confirm): nias
- measured range: 117-873 K (5th-95th pct of 167 curves)
- [ref 1] TEDesignLab / ICSD: MnTe P6_3/mmc (194) mp-404 [hull=0.008, icsd=18, PRIMARY]; MnTe2 Pa-3 (205) mp-21893 [hull=0.000, icsd=4, PRIMARY]; MnTe Pnma (62) mp-1080073 [hull=0.005, icsd=1]; MnTe F-43m (216) mp-1009222 [hull=0.037, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: Mn3Te Fm-3m (225) mp-1185993 [hull=0.306, PRIMARY, AMBIGUOUS]; MnTe Fm-3m (225) mp-1406 [hull=0.054, icsd=2]; MnTe P2_1/m (11) mp-672389 [hull=0.001]; MnTe Imma (74) mp-1172860 [hull=0.605]; Mn3Te P6_3/mmc (194) mp-1185988 [hull=0.312]
- papers: https://doi.org/10.1007/s13391-013-0035-z (Thermoelectric properties of non-stoichiometric MnTe compounds) | https://doi.org/10.1016/j.jallcom.2014.09.198 (Effects of Mn substitution on the phases and thermoelectric properties...) | https://doi.org/10.1063/1.4868584 (Thermoelectric study of crossroads material MnTe via sulfur doping)

## Cd-O-Te
- rank 176 | 43 samples | 1 papers | 11 compositions
- compositions: Cd2.99Bi0.01TeO6 (4); Cd2.98Bi0.02TeO6 (4); Cd2.98La0.02TeO6 (4); Cd2.99In0.01TeO6 (4); Cd2.97In0.03TeO6 (4); Cd2.96In0.04TeO6 (4)
- dopant candidates (<5% at.): In (16), Bi (12), La (12)
- seed hypothesis (confirm): double_perovskite
- measured range: 14-316 K (5th-95th pct of 51 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cd2(TeO3)3 P2_1/c (14) mp-30941 [hull=0.005, icsd=1, PRIMARY]; Cd2Te2O7 P-1 (2) mp-30940 [hull=0.000, icsd=1, PRIMARY]; Cd3TeO6 P2_1/c (14) mp-14243 [hull=0.000, icsd=1, PRIMARY]; CdTeO3 P2_1/c (14) mp-28290 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.ceramint.2004.03.045 (Preparation and thermoelectric properties of Cd3−xAxTeO6 (A = In, La, ...)

## Mn-O-Sr
- rank 177 | 43 samples | 14 papers | 33 compositions
- compositions: Sr0.8La0.2MnO3 (4); Gd0.2Sr0.8MnO3 (3); SrMnO3 (3); Bi0.2Sr0.8MnO3 (3); Sr0.8Ce0.2MnO3 (2); Sr0.95Ti0.05MnO3 (1)
- dopant candidates (<5% at.): Ce (9), La (7), Mo (6), Si (4), Pb (4), Sn (4), Gd (4), Pr (4), Ti (3), Bi (3), V (1), Nd (1), Dy (1), Sm (1), Yb (1)
- seed hypothesis (confirm): perovskite
- measured range: 12-1150 K (5th-95th pct of 75 curves; full span incl. outliers 10-1273 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2Mn2O5 Pbam (55) mp-18798 [hull=0.000, icsd=15, PRIMARY]; SrMnO3 P6_3/mmc (194) mp-19001 [hull=0.008, icsd=3, PRIMARY]; SrMn7O12 R-3 (148) mp-1105126 [hull=0.003, icsd=3, PRIMARY]; Sr3Mn2O7 I4/mmm (139) mp-19070 [hull=0.023, icsd=3, PRIMARY]; Sr2MnO4 I4/mmm (139) mp-18978 [hull=0.005, icsd=3, PRIMARY]
- papers: https://doi.org/10.1007/s13391-014-4237-9 (Structural and thermoelectric properties of n-type Sr1−x Ti x MnO3−δ p...) | https://doi.org/10.1007/s11664-011-1860-1 (Thermoelectric Properties of Electron-Doped SrMnO3 Single Crystals wit...) | https://doi.org/10.1016/j.powtec.2015.02.035 (Fabrication and thermoelectric properties of Sr1−xSixMnO3−δ)

## O-Pb-Sr
- rank 178 | 43 samples | 9 papers | 25 compositions
- compositions: SrPbO3 (10); Sr0.99La0.01PbO3 (4); Sr0.975La0.025PbO3 (3); Sr0.995La0.005PbO3 (3); Sr0.98La0.02PbO3 (2); Sr0.95La0.05PbO3 (2)
- dopant candidates (<5% at.): La (20), K (8), Ba (5), F (4)
- seed hypothesis (confirm): perovskite
- measured range: 12-1077 K (5th-95th pct of 79 curves; full span incl. outliers 10-1120 K)
- [ref 1] TEDesignLab / ICSD: Sr2PbO4 Pbam (55) mp-20944 [hull=0.000, icsd=2, PRIMARY]; SrPbO3 Pnma (62) mp-20489 [hull=0.000, icsd=2, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Sr3PbO Pm-3m (221) mp-19944 [hull=0.000, icsd=1, PRIMARY]; Sr5Zn(PbO4)3 P31m (157) mp-1218569 [hull=0.007, PRIMARY]; Sr8SnPb3O16 P4/mmm (123) mp-1218629 [hull=0.083, PRIMARY]
- papers: https://doi.org/10.2497/jjspm.55.408 (Preparation of Perovskite-Type Sr1-xBaxPbO3 Ceramics by an Oxalate Cop...) | https://doi.org/10.1134/s1087659613040068 (Synthesis and thermoelectric properties of ceramics based on barium-st...) | https://doi.org/10.1088/0953-8984/11/29/304 (Thermoelectric properties of Sr1-xLaxPbO3(xle0.02))

## Ag-Sb-Se
- rank 179 | 42 samples | 9 papers | 23 compositions
- compositions: AgSbSe2 (10); AgSb0.98Bi0.02Se2 (3); AgSb0.98Ba0.02Se2 (3); AgSb0.98Pb0.02Se2 (3); AgSb0.96Ba0.04Se2 (2); AgSb0.98Mg0.02Se2 (2)
- dopant candidates (<5% at.): Pb (7), Ba (6), Mg (5), Bi (4), Na (4), Sn (4), Zn (1), Cd (1)
- seed hypothesis (confirm): rocksalt
- measured range: 294-723 K (5th-95th pct of 164 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AgSbSe2 R-3m (166) mp-1229000 [hull=0.007, PRIMARY]; AgSbSe2 I4_1/amd (141) mp-33683 [hull=0.021]; AgSbSe2 P4/mmm (123) mp-1229008 [hull=0.073]
- papers: https://doi.org/10.1021/acsami.5b06492 (Contrasting the Role of Mg and Ba Doping on the Microstructure and The...) | https://doi.org/10.1039/c4dt03059a (Enhancement of thermoelectric properties by Na doping in Te-free p-typ...) | https://doi.org/10.1016/j.jallcom.2014.11.081 (High thermoelectric properties for Sn-doped AgSbSe2)

## Ba-Cu-Ge
- rank 180 | 42 samples | 11 papers | 17 compositions
- compositions: Ba8Cu4.8Ga1Ge40.2 (9); Ba8Cu6Ge40 (8); Ba8Cu3.5Ge41In1.5 (5); Ba8Cu5.9Ge40.1 (4); Ba8Cu5.1Ge40.2Sn0.7 (3); Ba8Cu5.7Ge40.3 (2)
- dopant candidates (<5% at.): Ga (11), In (5), Sn (3)
- seed hypothesis (confirm): clathrate_i
- measured range: 11-896 K (5th-95th pct of 112 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba4Cu3Ge20 Pm-3n (223) mp-669542 [hull=0.000, icsd=16, PRIMARY]; BaCu9Ge4 I4/mcm (140) mp-11145 [hull=0.000, icsd=2, PRIMARY]; BaCuGe P-6m2 (187) mp-1227964 [hull=0.044, PRIMARY]
- papers: https://doi.org/10.1007/s11664-012-2440-8 (High-Pressure Torsion to Improve Thermoelectric Efficiency of Clathrates?) | https://doi.org/10.1039/c5ta04168f (Structure and thermoelectric properties of the n-type clathrate Ba8Cu5...) | https://doi.org/10.2320/matertrans.46.1485 (Effect of Cu Substitution on Thermoelectric Properties of Ge Clathrates)

## Co-Fe-O
- rank 181 | 42 samples | 9 papers | 29 compositions
- compositions: CoFe2O4 (14); CoCr0.1Fe1.9O4 (1); CoCr0.3Fe1.7O4 (1); Co1.5Fe1.5O4 (1); Co1.2Fe1.8O4 (1); (Ni0.1Co0.9)0.9Fe2.1O4 (1)
- dopant candidates (<5% at.): Ni (9), Ge (3), Gd (3), Cr (2), Nd (2), Sm (2), Cu (1), Sr (1), La (1), Ba (1), Pr (1)
- seed hypothesis (confirm): spinel
- measured range: 303-975 K (5th-95th pct of 84 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe2CoO4 Imma (74) mp-34501 [hull=0.034, icsd=2, PRIMARY]; Fe(CoO3)2 C2/m (12) mp-761530 [hull=0.105, PRIMARY, AMBIGUOUS]; Fe(CoO2)2 Imma (74) mp-767034 [hull=0.030, PRIMARY]; Fe19Co5O32 C2/m (12) mp-762884 [hull=0.024, PRIMARY]; Fe2Co3O10 Pm (6) mp-778217 [hull=0.113, PRIMARY]
- papers: https://doi.org/10.1109/tmag.2013.2245112 (Magnetic and Thermoelectric Properties of Cobalt Ferrite) | https://doi.org/10.1016/j.jallcom.2014.03.097 (Thermoelectric power studies of Co–Cr nano ferrites) | https://doi.org/10.1109/ict.2006.331222 (Thermoelectric Properties of Sintered (MnyCo1-y) Fe2O4)

## Se-Ti
- rank 182 | 42 samples | 11 papers | 29 compositions
- compositions: TiSe2 (6); Cu0.06TiSe2 (2); Cu0.04TiSe2 (2); Cu0.02TiSe2 (2); Cu0.005TiSe2 (2); Cu0.08TiSe2 (2)
- dopant candidates (<5% at.): Cu (15), Pb (5), Ni (5), S (4), Sr (4)
- seed hypothesis (confirm): cdi2_1t
- measured range: 10-673 K (5th-95th pct of 96 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiSe2 P-3m1 (164) mp-2194 [hull=0.000, icsd=12, PRIMARY]; Ti2Se Pnnm (58) mp-620032 [hull=0.000, icsd=3, PRIMARY]; Ti3Se4 C2/m (12) mp-1077978 [hull=0.049, icsd=3, PRIMARY]; Ti45Se16 C2/m (12) mp-1198191 [hull=0.047, icsd=2, PRIMARY]; Ti8Se3 C2/m (12) mp-679962 [hull=0.004, icsd=2, PRIMARY]
- papers: https://doi.org/10.1021/am503477z (Enhanced Thermoelectric Properties of Selenium-Deficient Layered TiSe2...) | https://doi.org/10.1007/s00339-012-7536-8 (Low temperature thermoelectric properties of Cu intercalated TiSe2: a ...) | https://doi.org/10.1016/j.jallcom.2012.01.067 (CdI2 structure type as potential thermoelectric materials: Synthesis a...)

## Ag-Cu-Te
- rank 183 | 41 samples | 7 papers | 23 compositions
- compositions: AgCuTe (9); (AgCu)0.995Te0.9Se0.1 (9); (Ag0.685Cu0.3)2Te (3); (Ag0.785Cu0.2)2Te (1); (Ag0.885Cu0.1)2Te (1); Ag1.8Cu0.2Te (1)
- dopant candidates (<5% at.): Se (13), Ni (4)
- seed hypothesis (confirm): cu2se_superionic
- solid-solution axis: Ag/(Ag+Cu) spans 0.09-0.90 (median 0.50) over 23 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 301-835 K (5th-95th pct of 185 curves; full span incl. outliers 11-901 K)
  !! MEASUREMENT CROSSES A TRANSITION: cu2se_superionic -> cu2se_superionic at ~400 K (Ordered low-T superstructure -> cubic superionic, ~400 K. Cu2S transforms near ~376 K.)
     Record each phase with its own temperature range, not a single prototype.
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuAgTe2 Pmm2 (25) mp-2977 [hull=0.053, icsd=1, PRIMARY]; CuAgTe F-43m (216) mp-1225652 [hull=0.159, PRIMARY]
- papers: https://doi.org/10.1039/c3ta12508d (Thermoelectric properties of Ag-doped Cu2Se and Cu2Te) | https://doi.org/10.1039/c5ta01266j (Enhanced thermoelectric properties of p-type Ag2Te by Cu substitution) | https://doi.org/10.1016/j.jmat.2019.01.008 (Synergistic optimization of thermoelectric performance in p-type Ag2Te...)

## Ba-Ge
- rank 184 | 41 samples | 14 papers | 32 compositions
- compositions: Ba8Ge43 (5); Ba24Ge100 (4); Ba24Ga4Ge96 (3); Ba24Ga4Ag1Ge95 (1); Ba24Ga4Ag2Ge94 (1); Ba24Ga0Ge100 (1)
- dopant candidates (<5% at.): Ni (12), Ga (5), Ag (5), Cu (3), Sn (2), Zn (1), Al (1), In (1), Sb (1)
- seed hypothesis (confirm): clathrate_iii_ix
- measured range: 13-1048 K (5th-95th pct of 147 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaGe2 Pnma (62) mp-2139 [hull=0.000, icsd=5, PRIMARY]; BaGe3 P6_3/mmc (194) mp-1078234 [hull=0.038, icsd=2, PRIMARY]; Ba8Ge43 Ia-3d (230) mp-1199827 [hull=0.032, icsd=2, PRIMARY]; BaGe Cmcm (63) mp-1730 [hull=0.000, icsd=2, PRIMARY]; BaGe5 Imma (74) mp-1095284 [hull=0.077, icsd=2, PRIMARY]
- papers: https://doi.org/10.1021/acsami.5b04910 (Thermoelectric Properties of Ga/Ag Codoped Type-III Ba24Ge100Clathrate...) | https://doi.org/10.1016/j.actamat.2005.12.032 (High thermoelectric performance of type-III clathrate compounds of the...) | https://doi.org/10.1016/j.jallcom.2013.03.074 (Tuning of band gap and thermoelectric properties of type-I clathrate B...)

## Cr-La-O
- rank 185 | 41 samples | 8 papers | 15 compositions
- compositions: LaCrO3 (8); La0.8Sr0.2CrO3 (8); La0.8Ca0.2CrO3 (5); La0.9Sr0.1CrO3 (4); La0.98Ca0.02CrO3 (3); La0.9Ca0.1CrO3 (3)
- dopant candidates (<5% at.): Ca (18), Sr (13), Co (3), Zn (2), Al (1), Cu (1), Fe (1)
- seed hypothesis (confirm): perovskite
- measured range: 298-1925 K (5th-95th pct of 41 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaCrO3 Pnma (62) mp-19281 [hull=0.000, icsd=26, PRIMARY]; LaCrO4 P2_1/c (14) mp-19668 [hull=0.005, icsd=1, PRIMARY]; BaLa4TiCr4O15 P-1 (2) mp-744123 [hull=0.023, PRIMARY]; BaLa5TiCr5O18 P1 (1) mp-694922 [hull=0.021, PRIMARY]; La2Cr3O19 P2_1/c (14) mp-1204810 [hull=0.531, PRIMARY]
- papers: https://doi.org/10.1111/jace.18978 (Sintering temperature–induced structural transition in LaCrO\n        ...) | https://doi.org/10.1016/j.ceramint.2011.02.028 (Electrical conduction behaviors of isovalent and acceptor dopants on B...) | https://doi.org/10.1016/0022-0248(94)90010-8 (Deposition of LaMO3 (M=Co, Cr, Al) films by spray pyrolysis in inducti...)

## Eu-O-Ti
- rank 186 | 41 samples | 10 papers | 10 compositions
- compositions: EuTiO3 (18); Ba0.2Eu0.8TiO3 (5); Ba0.1Eu0.9TiO3 (4); Sr0.03Eu0.97TiO3 (4); EuTi0.98Nb0.02O3 (3); EuTiO3N0.1 (3)
- dopant candidates (<5% at.): Ba (9), Sr (5), Nb (4), N (3), La (3)
- seed hypothesis (confirm): perovskite
- measured range: 12-1288 K (5th-95th pct of 58 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): EuTiO3 Pm-3m (221) mp-22246 [hull=0.001, icsd=20, PRIMARY]; Eu2TiO5 Pnma (62) mp-1195915 [hull=0.000, icsd=1, PRIMARY]; Eu2Ti2O5 P4/mmm (123) mp-1184430 [hull=0.043, PRIMARY]; Eu2TiO4 I4/mmm (139) mp-1025200 [hull=0.000, PRIMARY]; Eu3Ti2O7 I4/mmm (139) mp-1212973 [hull=0.001, PRIMARY]
- papers: https://doi.org/10.1063/1.4737872 (Electronic structure and thermoelectric properties of nanostructured E...) | https://doi.org/10.1063/1.2822142 (The effect of Eu substitution on thermoelectric properties of SrTi0.8N...) | https://doi.org/10.1063/1.4813098 (Structure and thermoelectric properties of EuTi(O,N)3 ± δ)

## Ag-Mg-Sb
- rank 187 | 40 samples | 12 papers | 22 compositions
- compositions: MgAg0.97Sb0.99 (13); MgAg0.97Sb0.995 (5); MgAgSb (3); MgAg0.967Cu0.003Sb0.99 (1); MgAg0.96Cu0.01Sb0.99 (1); MgAg0.963Cu0.007Sb0.99 (1)
- dopant candidates (<5% at.): Li (5), Cu (3), Na (3), Zn (3), O (2), Si (2)
- seed hypothesis (confirm): mgagsb_alpha
- measured range: 296-566 K (5th-95th pct of 214 curves; full span incl. outliers 10-689 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MgAgSb F-43m (216) mp-1008903 [hull=0.000, icsd=1, PRIMARY]; MgAgSb P4/nmm (129) mp-1018797 [hull=0.023, icsd=1]; MgAgSb I-4c2 (120) mp-1191396 [hull=0.050, icsd=1]
- papers: https://doi.org/10.1016/j.actamat.2015.01.018 (Effect of Cu concentration on thermoelectric properties of nanostructu...) | https://doi.org/10.1016/j.nanoen.2014.11.027 (Study on thermoelectric performance by Na doping in nanostructured Mg ...) | https://doi.org/10.1103/physrevb.85.144120 (Abinitiodetermination of crystal structures of the thermoelectric mate...)

## Ag-Te-Tl
- rank 188 | 40 samples | 13 papers | 27 compositions
- compositions: AgTlTe (6); Ag9TlTe5 (2); AgTlTe2 (2); Ag9TlTe5.05 (2); Ag9TlTe5.3 (2); Ag9TlTe5.1 (2)
- dopant candidates (<5% at.): Cu (3), Pd (2)
- measured range: 296-699 K (5th-95th pct of 162 curves; full span incl. outliers 287-828 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TlAg3Te2 Cmmm (65) mp-8925 [hull=0.242, icsd=2, PRIMARY]; TlAgTe Pnma (62) mp-5874 [hull=0.000, icsd=2, PRIMARY]; Tl3AgTe2 P2_1/c (14) mp-650442 [hull=0.000, icsd=1, PRIMARY]; TlAgTe2 I-4m2 (119) mp-10006 [hull=0.122, icsd=1, PRIMARY]; Tl2Ag16Te11 P1 (1) mp-685196 [hull=0.050, PRIMARY]
- papers: https://doi.org/10.1063/1.2009828 (Ag9TlTe5: A high-performance thermoelectric bulk material with extreme...) | https://doi.org/10.1063/1.2756037 (Enhancement of thermoelectric figure of merit of AgTlTe by tuning the ...) | https://doi.org/10.1016/0022-3093(75)90053-8 (Electrical conductivity and thermoelectric power of some molten AIBIII...)

## Au-Ba-Si
- rank 189 | 40 samples | 7 papers | 24 compositions
- compositions: Ba8Au5Si41 (11); Ba8Au4.85Si41.15 (2); Ba8Au5.59Si40.41 (2); Ba8Au5.43Si40.57 (2); Ba8Au5.14Si40.86 (2); Ba8Au6.10Si39.90 (2)
- dopant candidates (<5% at.): Ga (1), Ce (1), La (1)
- seed hypothesis (confirm): clathrate_i
- measured range: 10-762 K (5th-95th pct of 92 curves; full span incl. outliers 10-875 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba4Si20Au3 Pm-3n (223) mp-17815 [hull=0.000, icsd=3, PRIMARY]; Ba2Si3Au P-6m2 (187) mp-1228346 [hull=0.030, PRIMARY]; Ba4Si21Au2 Ama2 (40) mp-1228313 [hull=0.004, PRIMARY]; Ba4Si22Au Ama2 (40) mp-1228316 [hull=0.026, PRIMARY]; Ba8Si43Au3 R32 (155) mp-1228259 [hull=0.014, PRIMARY]
- papers: https://doi.org/10.1063/1.3682585 (High temperature thermoelectric properties of the type-I clathrate Ba8...) | https://doi.org/10.1007/s11664-014-3118-1 (Reinvestigation of Thermoelectric Properties of n- and p-Type Ba8−d Au...) | https://doi.org/10.1103/physrevb.84.195137 (Low-temperature thermoelectric, galvanomagnetic, and thermodynamic pro...)

## Bi-Mn-O-Sr
- rank 190 | 40 samples | 6 papers | 11 compositions
- compositions: Bi0.5Sr0.5MnO3 (8); Bi0.4La0.1Sr0.5MnO3 (5); Bi0.3La0.2Sr0.5MnO3 (5); Bi0.55Sr0.45MnO3 (4); Bi0.45Sr0.55MnO3 (4); Bi0.4Sr0.6MnO3 (4)
- dopant candidates (<5% at.): La (10)
- measured range: 11-797 K (5th-95th pct of 40 curves; full span incl. outliers 11-1012 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr4Mn2Bi4O13 Pna2_1 (33) mp-1205023 [hull=0.000, icsd=1, PRIMARY]; Sr3MnBiO6 P2_1/c (14) mp-1208471 [hull=0.000, PRIMARY]; SrMn2BiO6 I4mm (107) mp-1218247 [hull=0.026, PRIMARY]
- papers: https://doi.org/10.1063/1.2938033 (Magnon drag effect as the dominant contribution to the thermopower in ...) | https://doi.org/10.1088/0953-8984/19/29/296205 (Evidence of the Bi3+ lone-pair effect on the charge-ordering state: re...) | https://doi.org/10.1088/0953-8984/19/47/476203 (The universal relation between thermopower and magnetic susceptibility...)

## Eu-Sb-Zn
- rank 191 | 40 samples | 14 papers | 26 compositions
- compositions: EuZn2Sb2 (14); EuZn1.8Cd0.2Sb2 (2); Eu11Zn6Sb12 (1); Eu1Zn2Sb2 (1); Ca0.1Eu0.9Zn2Sb2 (1); Eu2Zn0.98Sb2 (1)
- dopant candidates (<5% at.): Ag (11), Cd (3), Ca (1), Yb (1)
- seed hypothesis (confirm): caal2si2_zintl
- measured range: 298-825 K (5th-95th pct of 159 curves; full span incl. outliers 10-826 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Eu(ZnSb)2 P-3m1 (164) mp-1069042 [hull=0.000, icsd=2, PRIMARY]; Eu11(ZnSb2)6 C2/m (12) mp-1193786 [hull=0.000, icsd=1, PRIMARY]; Eu2ZnSb2 P-6m2 (187) mp-1225256 [hull=0.015, PRIMARY]
- papers: https://doi.org/10.1021/acs.chemmater.5b01301 (High Temperature Thermoelectric Properties of the Solid-Solution Zintl...) | https://doi.org/10.1039/b914172c (Electronic structure and transport in thermoelectric compounds AZn2Sb2...) | https://doi.org/10.1039/b916346h (Thermoelectric properties of Eu(Zn1−xCdx)2Sb2)

## Fe-O-Sr-Ti
- rank 192 | 40 samples | 13 papers | 27 compositions
- compositions: Sr2TiFeO6 (3); Ba0.15Sr1.85TiFeO6 (3); Ba0.25Sr1.75TiFeO6 (3); Ba0.1Sr1.9TiFeO6 (3); SrTi0.3Fe0.7O3 (3); Sr0.92Y0.08Ti0.5Fe0.5O3 (3)
- dopant candidates (<5% at.): Ba (12), Y (7), Nb (4), Co (4), Mo (1)
- seed hypothesis (confirm): double_perovskite
- measured range: 328-1223 K (5th-95th pct of 40 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2TiFeO6 P4/mmm (123) mp-1218692 [hull=0.006, PRIMARY]; Sr5Ti4FeO15 C2/m (12) mp-1218575 [hull=0.014, PRIMARY]; Sr6Ti3FeO14 P4mm (99) mp-1218493 [hull=0.002, PRIMARY]; Sr2TiFeO6 Fm-3m (225) mp-1094048 [hull=0.022]
- papers: https://doi.org/10.1039/c6ra09629h (Environmentally friendly BaxSr2−xTiFeO6double perovskite with enhanced...) | https://doi.org/10.1016/j.ceramint.2015.06.074 (Evaluation of double perovskite Sr2FeTiO6−δ as potential cathode or an...) | https://doi.org/10.1016/j.materresbull.2015.09.023 (Investigation of cobalt-free perovskite Sr2FeTi0.75Mo0.25O6−δ as new c...)

## Co-Hf-Sb-Sn-Zr
- rank 193 | 39 samples | 13 papers | 24 compositions
- compositions: Zr0.5Hf0.5CoSb0.8Sn0.2 (11); Ti0.12Zr0.44Hf0.44CoSb0.8Sn0.2 (5); Hf0.2Zr0.8CoSb0.8Sn0.2 (2); (Hf0.44Zr0.44Ti0.12)CoSb0.8Sn0.2 (1); Hf0.303Zr0.697CoSn0.3Sb0.7 (1); Hf0.3Zr0.7CoSn0.3Sb0.7 (1)
- dopant candidates (<5% at.): Ti (10)
- seed hypothesis (confirm): half_heusler
- solid-solution axis: Hf/(Hf+Zr) spans 0.20-0.80 (median 0.50) over 24 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 294-1127 K (5th-95th pct of 164 curves; full span incl. outliers 19-1169 K)
- papers: https://doi.org/10.1002/aenm.201200973 (Thermoelectric Property Study of Nanostructured p-Type Half-Heuslers (...) | https://doi.org/10.1007/s11664-013-2863-x (Thermoelectric Modules Based on Half-Heusler Materials Produced in Lar...) | https://doi.org/10.1557/jmr.2011.329 (Half-Heusler phases and nanocomposites as emerging high-ZT thermoelect...)

## Co-O-Pd
- rank 194 | 39 samples | 5 papers | 1 compositions
- compositions: PdCoO2 (39)
- seed hypothesis (confirm): delafossite
- measured range: 10-908 K (5th-95th pct of 39 curves; full span incl. outliers 10-1000 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CoPdO2 R-3m (166) mp-18919 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.91.041113 (Large anisotropic thermal conductivity of the intrinsically two-dimens...) | https://doi.org/10.1016/s0038-1098(01)00484-7 (Thermoelectric power of delafossite-type metallic oxide PdCoO2) | https://doi.org/10.1103/physrevmaterials.3.085403 (Large thermopower anisotropy in \nPdCoO2\n thin films)

## Ge
- rank 195 | 39 samples | 12 papers | 13 compositions
- compositions: Ge (26); Ge0.98Si0.02 (2); Ga0.000002Ge (1); Bi0.00008Ge (1); Ga0.0002Ge (1); Sb0.00008Ge (1)
- dopant candidates (<5% at.): Ga (5), Si (2), Bi (1), Sb (1), P (1), As (1)
- seed hypothesis (confirm): diamond_cubic
- measured range: 53-1075 K (5th-95th pct of 63 curves; full span incl. outliers 42-1296 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ge Fd-3m (227) mp-32 [hull=0.000, icsd=15, PRIMARY]; Ge P4_32_12 (96) mp-137 [hull=0.144, icsd=16]; Ge R-3 (148) mp-128 [hull=0.148, icsd=6]; Ge Cmce (64) mp-1079020 [hull=0.313, icsd=6]; Ge Fmmm (69) mp-148 [hull=0.240, icsd=5]
- papers: https://doi.org/10.1002/adfm.201401201 (Nanograined Half-Heusler Semiconductors as Advanced Thermoelectrics: A...) | https://doi.org/10.1002/pssa.201228392 (Morphology, thermoelectric properties and wet-chemical doping of laser...) | https://doi.org/10.1134/s1063783415030208 (Transport properties of nanocomposite thermoelectric materials based o...)

## La-Mn-O-Pb
- rank 196 | 39 samples | 8 papers | 20 compositions
- compositions: La0.7Pb0.3MnO3 (8); La0.5Pb0.5MnO3 (6); (La0.7Nd0.3)0.7Pb0.3MnO3 (4); La0.6Pb0.4MnO3 (3); La0.6Pb0.4Mn0.95Co0.05O3 (2); La0.6Pb0.4Mn0.975Co0.025O3 (2)
- dopant candidates (<5% at.): Nd (5), Co (4), Dy (4), Y (4), Pr (2), Ca (2), Na (1)
- measured range: 11-400 K (5th-95th pct of 48 curves; full span incl. outliers 10-450 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2Mn3PbO9 P-3c1 (165) mp-690564 [hull=0.028, PRIMARY]; La2MnPbO9 P3m1 (156) mp-1223416 [hull=0.389, PRIMARY]; La4Mn5Co(PbO9)2 P1 (1) mp-743770 [hull=0.043, PRIMARY]; La4TiMn5(PbO9)2 P1 (1) mp-706223 [hull=0.042, PRIMARY]; La5Mn7Co(PbO8)3 P1 (1) mp-705288 [hull=0.046, PRIMARY]
- papers: https://doi.org/10.1063/1.1459618 (Particle size and magnetic field dependent resistivity and thermoelect...) | https://doi.org/10.1063/1.2188029 (Ferro-antiferromagnetic coupling and unusual transport properties of f...) | https://doi.org/10.1016/j.physleta.2005.01.002 (Thermoelectric effect in La0.6Pb0.4Mn1−xCoxO3)

## O-Si
- rank 197 | 39 samples | 17 papers | 10 compositions
- compositions: SiO2 (26); Au0.02SiO2 (4); Si2O (2); (SiO2)90(GeO2)10B0.63 (1); (SiO2)90(GeO2)10B0.15 (1); (SiO2)90(GeO2)10B15 (1)
- dopant candidates (<5% at.): Ge (6), B (4), Au (4), Ti (1)
- measured range: 11-1235 K (5th-95th pct of 49 curves)
- [ref 1] TEDesignLab / ICSD: SiO2 P3_221 (154) mp-6930 [hull=0.011, icsd=99, PRIMARY]; SiO2 P4_2/mnm (136) mp-6947 [hull=0.196, icsd=60]; SiO2 P4_12_12 (92) mp-6945 [hull=0.003, icsd=47]; SiO2 C2/c (15) mp-651707 [hull=0.008, icsd=43]; SiO2 P3_121 (152) mp-7000 [hull=0.011, icsd=37]
- [ref 2] MP, ranked by ICSD evidence: NaLiZr(Si2O5)3 Cmce (64) mp-15543 [hull=0.000, icsd=2, PRIMARY]; Si2O3 C2/c (15) mp-1179195 [hull=0.805, icsd=2, PRIMARY]; Si2O5 Ima2 (46) mp-862998 [hull=0.600, icsd=2, PRIMARY]; NaNd(Si2O5)3 Cmm2 (35) mp-1198222 [hull=0.128, icsd=1, PRIMARY]; Na2CaZr2Si10O27 C2/c (15) mp-1197941 [hull=0.101, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/cm401990c (Silicon-Based Thermoelectrics Made from a Boron-Doped Silicon Dioxide ...) | https://doi.org/10.1140/epjb/e2015-50594-7 (Thermoelectrics from silicon nanoparticles: the influence of native oxide) | https://doi.org/10.1021/nl102931z (Holey Silicon as an Efficient Thermoelectric Material)

## Co-Nd-O
- rank 198 | 38 samples | 14 papers | 20 compositions
- compositions: NdCoO3 (9); Nd0.75Sr0.25CoO4 (3); Nd0.9Ca0.1CoO3 (3); Nd0.995Ca0.005CoO3 (2); Nd0.875Ca0.125CoO3 (2); Nd0.9Ba0.1CoO3 (2)
- dopant candidates (<5% at.): Ca (15), Sr (8), Ba (5), Ni (1)
- measured range: 12-1171 K (5th-95th pct of 57 curves; full span incl. outliers 11-1232 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NdCoO3 Pnma (62) mp-24882 [hull=0.000, icsd=10, PRIMARY]; Nd4Co3O10 P2_1/c (14) mp-1199738 [hull=0.041, icsd=2, PRIMARY]; Nd2CoO4 I4/mmm (139) mp-1206526 [hull=0.123, PRIMARY]; NdCoO3 Pm-3m (221) mp-24851 [hull=0.166, icsd=1]
- papers: https://doi.org/10.1016/j.actamat.2007.05.020 (High-temperature thermoelectric properties of Ln(Co, Ni)O3 (Ln=La, Pr,...) | https://doi.org/10.1016/j.jallcom.2009.04.100 (Influence of ionic sizes of rare earths on thermoelectric properties o...) | https://doi.org/10.1063/1.3671070 (Thermoelectric module made of perovskite cobalt oxides with large ther...)

## Cu-S-Sn-Zn
- rank 199 | 38 samples | 12 papers | 15 compositions
- compositions: Cu2ZnSnS4 (17); Cu2.1Zn0.9SnS4 (6); Cu2.19Zn0.80Sn0.75S3.53 (2); Cu2.125Zn0.875SnS4 (2); Ni0.026Cu2ZnSnS4 (1); Cu22Zn4V2Sn6S32 (1)
- dopant candidates (<5% at.): Ag (2), Ni (1), V (1)
- seed hypothesis (confirm): stannite_kesterite
- measured range: 297-774 K (5th-95th pct of 164 curves; full span incl. outliers 11-992 K)
- [ref 1] TEDesignLab / ICSD: ZnCu2SnS4 I-4 (82) mp-1079541 [hull=0.000, icsd=3, PRIMARY]; ZnCu2SnS4 I-42m (121) mp-1025500 [hull=0.003, icsd=2]
- [ref 2] MP, ranked by ICSD evidence: ZnCu2SnS4 Pmn2_1 (31) mp-1190224 [hull=0.012, icsd=1]
- papers: https://doi.org/10.7567/jjap.54.061801 (High-temperature thermoelectric properties and thermal stability in ai...) | https://doi.org/10.1039/c3mh00091e (Magnetic ions in wide band gap semiconductor nanocrystals for optimize...) | https://doi.org/10.1021/nl201718z (Nontoxic and Abundant Copper Zinc Tin Sulfide Nanocrystals for Potenti...)

## Fe-Mo-O-Sr
- rank 200 | 38 samples | 13 papers | 24 compositions
- compositions: Sr2FeMoO6 (12); SrFe0.75Mo0.25O3 (3); Sr1.8La0.2FeMoO6 (2); Sr2Fe0.87Mo1.13O6 (1); Sr2Fe0.80Mo1.2O6 (1); Sr2FeMo0.8Nb0.2O6 (1)
- dopant candidates (<5% at.): La (5), V (4), Zn (4), Ba (3), Nb (1), Al (1)
- seed hypothesis (confirm): double_perovskite
- measured range: 18-1075 K (5th-95th pct of 60 curves; full span incl. outliers 16-1123 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2FeMoO6 I4/m (87) mp-905403 [hull=0.000, icsd=14, PRIMARY]; Sr10Fe3Co2(MoO6)5 P-1 (2) mp-1218936 [hull=0.004, PRIMARY]; NaSr9Fe5(MoO6)5 C2 (5) mp-706231 [hull=0.018, PRIMARY]; Sr10Fe4Co(MoO6)5 I4/m (87) mp-1218934 [hull=0.032, PRIMARY]; Sr10Fe5Mo4WO30 P-1 (2) mp-1218929 [hull=0.004, PRIMARY]
- papers: https://doi.org/10.1039/c4dt03307h (Antisite-disorder, magnetic and thermoelectric properties of Mo-rich S...) | https://doi.org/10.1002/ecjb.20111 (First-principles simulation of electric and magnetic properties of Sr2...) | https://doi.org/10.2497/jjspm.55.827 (Thermoelectric Property of Nb-doped Sr2FeMoO6 Double Perovskite Oxide)
