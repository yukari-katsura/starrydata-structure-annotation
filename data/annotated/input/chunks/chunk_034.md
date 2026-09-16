# Host systems -- chunk 034 of 73

Ranks 1651-1700 by sample count. These 50 host systems cover 150 samples (0.29% of the TE set); cumulative through this chunk: 94.74%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Ce-Ru
- rank 1651 | 3 samples | 1 papers | 3 compositions
- compositions: CeRu2 (1); (Ce0.9Nd0.1)Ru2 (1); (Ce0.9La0.1)Ru2 (1)
- dopant candidates (<5% at.): Nd (1), La (1)
- sample form: Polycrystal (3)
- measured range: 14-294 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeRu2 Fd-3m (227) mp-607 [hull=0.000, icsd=16, PRIMARY]; Ce7Ru3 P6_3mc (186) mp-31164 [hull=0.002, icsd=2, PRIMARY]; Ce3Ru Pnma (62) mp-672261 [hull=0.032, icsd=1, PRIMARY]; Ce4Ru Fd-3m (227) mp-1214027 [hull=0.485, PRIMARY]
- papers: https://doi.org/10.1016/0921-4526(94)00430-4 (Transport properties of (Ce1−xRx)Ru2 (R  La, Nd))

## Ce-Te
- rank 1652 | 3 samples | 1 papers | 3 compositions
- compositions: CeTe2 (1); CeTe1.95Sb0.05 (1); CeTe1.9Sb0.1 (1)
- dopant candidates (<5% at.): Sb (2)
- sample form: SingleCrystal (3)
- measured range: 100-299 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeTe Fm-3m (225) mp-1525 [hull=0.000, icsd=7, PRIMARY]; Ce3Te4 I-43d (220) mp-22422 [hull=0.000, icsd=5, PRIMARY]; Ce10Te19 P4_2/n (86) mp-645273 [hull=0.000, icsd=1, PRIMARY]; Ce2Te5 Cmcm (63) mp-1104233 [hull=0.056, icsd=1, PRIMARY]; Ce2Te3 Pnma (62) mp-1188216 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.4756911 (Dimensional crossover of charge density wave and thermoelectric proper...)

## Co-Cu-Gd
- rank 1653 | 3 samples | 1 papers | 3 compositions
- compositions: Gd(Co0.9Cu0.1)3 (1); Gd(Co0.7Cu0.3)3 (1); Gd(Co0.8Cu0.2)3 (1)
- sample form: Bulk (3)
- measured range: 10-298 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1063/1.3549597 (Thermoelectric power of Gd4(Co1-xCux)3 compounds)

## Co-Cu-Na-O
- rank 1654 | 3 samples | 3 papers | 2 compositions
- compositions: Na(Co0.8Cu0.2)2O4 (2); Na0.6Cu0.4Co2O4 (1)
- sample form: Bulk (2)
- measured range: 573-1074 K (5th-95th pct of 7 curves)
- papers: https://doi.org/10.1016/j.jallcom.2005.08.081 (Influence of partial substitution of Cu for Co on the thermoelectric p...) | https://doi.org/10.1021/cm300159w (Thermoelectric Solid-Oxide Fuel Cells with Extra Power Conversion from...) | https://doi.org/10.1109/ict.2005.1519899 (Microstructure and high-temperature thermoelectric properties of Cu-do...)

## Co-Fe-Ge
- rank 1655 | 3 samples | 1 papers | 3 compositions
- compositions: Co0.7Fe0.3Ge (1); Co0.88Fe0.12Ge (1); Co0.8Fe0.2Ge (1)
- measured range: 12-291 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeCo2Ge Fm-3m (225) mp-22300 [hull=0.000, icsd=2, PRIMARY]; Fe2CoGe Fm-3m (225) mp-30044 [hull=0.115, icsd=1, PRIMARY]; Fe3Co3Ge2 R3m (160) mp-1225391 [hull=0.102, PRIMARY]; FeCoGe P6_3/mmc (194) mp-1025047 [hull=0.044, PRIMARY]
- papers: https://doi.org/10.1063/1.3691260 (Band-filling dependence of thermoelectric properties in B20-type CoGe)

## Co-Fe-In-S-Sn
- rank 1656 | 3 samples | 1 papers | 3 compositions
- compositions: Co2.5Fe0.5Sn1.6In0.4S2 (1); Co2.5Fe0.5Sn1.5In0.5S2 (1); Co2.5Fe0.5Sn1.4In0.6S2 (1)
- sample form: Bulk (3)
- measured range: 297-626 K (5th-95th pct of 15 curves)
- papers: https://doi.org/10.1021/acsaem.9b02272 (Improved Thermoelectric Performance through Double Substitution in Sha...)

## Co-Fe-La-Mn-Ni-O
- rank 1657 | 3 samples | 1 papers | 3 compositions
- compositions: LaCo0.25Fe0.25Ni0.25Mn0.25O3 (1); La0.9Sr0.1Co0.25Fe0.25Ni0.25Mn0.25O3 (1); La0.8Sr0.2Co0.25Fe0.25Ni0.25Mn0.25O3 (1)
- dopant candidates (<5% at.): Sr (2)
- sample form: rod-shaped (3)
- measured range: 923-1073 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/j.ceramint.2023.06.275 (A medium-entropy perovskite oxide La0.7Sr0.3Co0.25Fe0.25Ni0.25Mn0.25O3...)

## Co-Fe-O-Pr
- rank 1658 | 3 samples | 1 papers | 3 compositions
- compositions: Pr1.8Sr0.2CoFeO6 (1); Pr2CoFeO6 (1); Pr1.6Sr0.4CoFeO6 (1)
- dopant candidates (<5% at.): Sr (2)
- sample form: Bulk (3)
- measured range: 301-777 K (5th-95th pct of 15 curves)
- papers: https://doi.org/10.1016/j.cej.2021.130668 (Double perovskite Pr2CoFeO6 thermoelectric oxide: Roles of Sr-doping a...)

## Co-Fe-O-Zn
- rank 1659 | 3 samples | 1 papers | 3 compositions
- compositions: Co0.5Zn0.5Cr0.1Fe1.9O4 (1); Co0.5Zn0.5Cr0.2Fe1.8O4 (1); Co0.5Zn.5Cr0.3Fe1.7O4 (1)
- dopant candidates (<5% at.): Cr (3)
- measured range: 303-479 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zn3Fe12(CoO12)2 Imm2 (44) mp-1216048 [hull=0.072, PRIMARY]; Zn3Fe8CoO16 P-4m2 (115) mp-1215745 [hull=0.001, PRIMARY]; ZnFe4CoO8 F-43m (216) mp-1215623 [hull=0.001, PRIMARY]; ZnFe8Co3O16 P-4m2 (115) mp-1215842 [hull=0.000, PRIMARY]; ZnFe4CoO8 R3m (160) mp-1215658 [hull=0.061]
- papers: https://doi.org/10.1016/j.jmmm.2015.04.104 (Investigation of structural and temperature dependent electromagnetic ...)

## Co-Fe-S
- rank 1660 | 3 samples | 1 papers | 3 compositions
- compositions: Fe2.0Co5.0S8 (1); Fe4.2Co2.8S8 (1); Fe2.8Co4.2S8 (1)
- measured range: 322-573 K (5th-95th pct of 14 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe(CoS)8 Fm-3m (225) mp-1188182 [hull=0.002, icsd=1, PRIMARY]; FeCo3S8 R-3 (148) mp-1224978 [hull=0.004, PRIMARY]; FeCoS2 P-3m1 (164) mp-1224971 [hull=0.240, PRIMARY]; FeCoS4 P2_1/c (14) mp-1225004 [hull=0.011, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2019.152999 (Exploring the thermoelectric behavior of spark plasma sintered Fe7-xCo...)

## Co-Fe-Zr
- rank 1661 | 3 samples | 1 papers | 3 compositions
- compositions: Fe44.6Co44.4NbZr7.3B3.7Cu1  (1); Fe44.6Co44.4HfZr7.3B3.7Cu1 (1); Fe44.6Co44.4Zr7.3B3.7Cu1 (1)
- dopant candidates (<5% at.): B (3), Cu (3), Nb (1), Hf (1)
- measured range: 349-1029 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zr2FeCo Immm (71) mp-1096398 [hull=3.410, PRIMARY]; Zr2FeCo3 R-3m (166) mp-1215554 [hull=0.000, PRIMARY]; Zr4FeCo I422 (97) mp-1215368 [hull=0.016, PRIMARY]; ZrFeCo Imma (74) mp-1215271 [hull=0.009, PRIMARY]
- papers: https://doi.org/10.1016/j.jnoncrysol.2008.07.038 (Thermoelectric and electrical resistivity study of Hitperm alloys)

## Co-Ga-La-O
- rank 1662 | 3 samples | 1 papers | 3 compositions
- compositions: LaCo0.7Ga0.3O3 (1); LaCo0.5Ga0.5O3 (1); LaCo0.93Ga0.7O3 (1)
- measured range: 322-1048 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2GaCoO6 R-3 (148) mp-1223269 [hull=0.064, PRIMARY]
- papers: https://doi.org/10.1134/s0020168509090155 (Electrical conductivity and thermoelectric power of LaCo1 − x Ga x O3 ...)

## Co-Ga-Th
- rank 1663 | 3 samples | 1 papers | 1 compositions
- compositions: ThCoGa4 (3)
- sample form: SingleCrystal (3)
- measured range: 10-315 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ThGa4Co Cmcm (63) mp-22767 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/16/30/005 (The crystal structure, transport and thermodynamic properties of ThCoG...)

## Co-Ge-Sb-Te
- rank 1664 | 3 samples | 2 papers | 3 compositions
- compositions: (CoSb2Ge0.5Te0.5)2(GeTe)10.5Sb2Te3 (1); Co4Sb8Ge1.9Te2.1 (1); Co4Sb9Ge1.4Te1.6 (1)
- sample form: Bulk (2); Other (1)
- measured range: 296-776 K (5th-95th pct of 13 curves)
- papers: https://doi.org/10.1039/c5tc01509j (Heterostructures of skutterudites and germanium antimony tellurides – ...) | https://doi.org/10.1007/s11664-010-1457-0 (Effects of Double Substitution with Ge and Te on Thermoelectric Proper...)

## Co-Ge-Ti
- rank 1665 | 3 samples | 3 papers | 1 compositions
- compositions: Co2TiGe (3)
- measured range: 10-885 K (5th-95th pct of 7 curves; full span incl. outliers 10-942 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiCo2Ge Fm-3m (225) mp-4612 [hull=0.000, icsd=5, PRIMARY]; TiCoGe P-62m (189) mp-22769 [hull=0.000, icsd=2, PRIMARY]; Ti4Co7Ge6 Im-3m (229) mp-1188792 [hull=0.000, icsd=2, PRIMARY]; Ti(CoGe)6 P6/mmm (191) mp-1104097 [hull=0.019, icsd=1, PRIMARY]; Ti2CoGe F-43m (216) mp-999067 [hull=0.301, icsd=1, PRIMARY]
- papers: https://doi.org/10.1098/rsta.2011.0183 (Anomalous transport properties of the half-metallic ferromagnets Co2Ti...) | https://doi.org/10.1103/physrevb.81.064404 (Itinerant half-metallic ferromagnetsCo2TiZ(Z=Si, Ge, Sn):Ab initiocalc...) | https://doi.org/10.1002/pssb.202000067 (Anomalous Hall Effect and Magnetoresistance in Sputter‐Deposited Magne...)

## Co-Hf-Rh-Sb-Sn-Zr
- rank 1666 | 3 samples | 1 papers | 3 compositions
- compositions: Zr0.5Hf0.5Co0.4Rh0.6Sb0.6Sn0.4 (1); Zr0.5Hf0.5Co0.4Rh0.6Sb0.8Sn0.2 (1); Zr0.5Hf0.5Co0.4Rh0.6Sb0.75Sn0.25 (1)
- sample form: Bulk (3)
- measured range: 269-775 K (5th-95th pct of 18 curves)
- papers: https://doi.org/10.1016/j.jssc.2013.03.024 (Thermoelectric performance of nanostructured p-type Zr0.5Hf0.5Co0.4Rh0...)

## Co-I-Sb
- rank 1667 | 3 samples | 1 papers | 3 compositions
- compositions: IFe0.3Co3.7Sb12 (1); IFe0.5Co3.5Sb12 (1); IFe0.7Co3.3Sb12 (1)
- dopant candidates (<5% at.): Fe (3)
- sample form: Bulk (3)
- measured range: 296-601 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co5Sb15I C2/m (12) mp-1226477 [hull=0.064, PRIMARY]
- papers: https://doi.org/10.1016/j.matlet.2014.10.072 (Iodine-filled FexCo4−xSb12 polycrystals: Synthesis, structure, and the...)

## Co-Nb-Sb-Sn-Ta-Ti
- rank 1668 | 3 samples | 1 papers | 3 compositions
- compositions: CoTi0.6Nb0.2Ta0.2Sb0.6Sn0.4 (1); CoTi0.4Nb0.3Ta0.3Sb0.4Sn0.6 (1); CoTi0.2Nb0.4Ta0.4Sb0.2Sn0.8 (1)
- measured range: 40-937 K (5th-95th pct of 12 curves)
- papers: https://doi.org/10.1016/j.jallcom.2004.04.096 (High temperature thermoelectric properties of CoTiSb half-Heusler comp...)

## Co-Ni
- rank 1669 | 3 samples | 1 papers | 3 compositions
- compositions: Co39Ni61 (1); Co71Ni29 (1); Co24Ni76 (1)
- sample form: Wire (3)
- measured range: 56-288 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co3Ni Pm-3m (221) mp-1008349 [hull=0.000, icsd=1, PRIMARY]; CoNi Pm-3m (221) mp-1006883 [hull=0.156, icsd=1, PRIMARY]; CoNi3 P6_3/mmc (194) mp-1183785 [hull=0.019, PRIMARY, AMBIGUOUS]; Co3Ni P6_3/mmc (194) mp-1183837 [hull=0.000]; Co3Ni P-6m2 (187) mp-1226559 [hull=0.025]
- papers: https://doi.org/10.1063/1.4819949 (Magneto-thermopower and magnetoresistance of single Co-Ni alloy nanowires)

## Co-O-Sc-Sr
- rank 1670 | 3 samples | 1 papers | 3 compositions
- compositions: SrCo0.6Sc0.4O3 (1); SrCo0.7Sc0.3O3 (1); SrCo0.5Sc0.5O3 (1)
- measured range: 575-1173 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1590/s0104-66322009000300012 (Effects of scandium doping concentration on the properties of strontiu...)

## Co-O-Si
- rank 1671 | 3 samples | 1 papers | 3 compositions
- compositions: (CoSi)0.85(SiO2)0.15 (1); (CoSi)0.9(SiO2)0.1 (1); (CoSi)0.925(SiO2)0.075 (1)
- sample form: Bulk (3)
- measured range: 298-982 K (5th-95th pct of 13 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co2SiO4 Pnma (62) mp-25474 [hull=0.000, icsd=8, PRIMARY]; CoSiO3 Pbca (61) mp-699575 [hull=0.018, icsd=1, PRIMARY]; CoSiO4 Pna2_1 (33) mp-633897 [hull=0.189, PRIMARY]; KNaCaCo5(SiO3)8 P1 (1) mp-1223618 [hull=0.028, PRIMARY]; Co2SiO4 Imma (74) mp-18941 [hull=0.035, icsd=2]
- papers: https://doi.org/10.1007/s11664-014-3213-3 (Structural Characterization and Thermoelectric Properties of Hot-Press...)

## Co-Se
- rank 1672 | 3 samples | 1 papers | 1 compositions
- compositions: CoSe (3)
- measured range: 10-12 K (5th-95th pct of 3 curves)
- [ref 1] TEDesignLab / ICSD: Co9Se8 Fm-3m (225) mp-22745 [hull=0.000, icsd=2, PRIMARY]; Co3Se4 Fd-3m (227) mp-20456 [hull=0.003, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: CoSe2 Pa-3 (205) mp-22309 [hull=0.018, icsd=9, PRIMARY]; CoSe P6_3/mmc (194) mp-426 [hull=0.140, icsd=8, PRIMARY]; Co3Se Pm-3m (221) mp-1183684 [hull=0.409, PRIMARY]; Co17Se20 P-1 (2) mp-685129 [hull=0.063, PRIMARY]; CoSe2 Pnnm (58) mp-20862 [hull=0.000, icsd=1]
- papers: https://doi.org/10.1103/physrevb.97.104408 (Frustrated magnetism in the tetragonal CoSe analog of superconducting ...)

## Co-Se-Sn
- rank 1673 | 3 samples | 1 papers | 3 compositions
- compositions: Co4Sn6Se6 (1); Co3.6Ru0.4Sn6Se6 (1); Co3.8Ni0.2Sn6Se6 (1)
- dopant candidates (<5% at.): Ru (1), Ni (1)
- sample form: Bulk (3)
- measured range: 301-804 K (5th-95th pct of 9 curves)
- papers: https://doi.org/10.1007/s11664-009-1067-x (Thermoelectric Properties of Co4Sn6Se6 Ternary Skutterudites)

## Co-Y
- rank 1674 | 3 samples | 3 papers | 1 compositions
- compositions: YCo2 (3)
- sample form: SingleCrystal (1)
- measured range: 11-496 K (5th-95th pct of 5 curves; full span incl. outliers 11-996 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YCo2 Fd-3m (227) mp-1077486 [hull=0.000, icsd=28, PRIMARY]; YCo3 R-3m (166) mp-2588 [hull=0.000, icsd=27, PRIMARY]; YCo5 P6/mmm (191) mp-1077022 [hull=0.017, icsd=21, PRIMARY]; Y3Co Pnma (62) mp-1105598 [hull=0.000, icsd=6, PRIMARY]; Y2Co17 R-3m (166) mp-1106140 [hull=0.000, icsd=5, PRIMARY]
- papers: https://doi.org/10.1016/s0921-4526(97)00157-9 (Transport phenomena in spin fluctuations systems) | https://doi.org/10.1088/0953-8984/7/33/008 (The transport properties of RCo2compounds) | https://doi.org/10.1016/s0921-4526(96)00583-2 (Transport properties in CeCo2 single crystal)

## Cr-Fe-Mg-O
- rank 1675 | 3 samples | 1 papers | 3 compositions
- compositions: MgFeCrO4 (1); MgFe0.5Cr1.5O4 (1); MgFe1.5Cr0.5O4 (1)
- sample form: Bulk (3)
- measured range: 322-697 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg14CrFeO16 Pmmm (47) mp-1035602 [hull=0.035, PRIMARY]; Mg30CrFeO32 P4/mmm (123) mp-1037531 [hull=0.018, PRIMARY]; Mg3Cr8FeO16 R3m (160) mp-1222216 [hull=0.071, PRIMARY]; Mg6CrFeO8 P4/mmm (123) mp-1032130 [hull=0.121, PRIMARY]; MgCr4FeO8 F-43m (216) mp-1222043 [hull=0.186, PRIMARY]
- papers: https://doi.org/10.1016/j.solidstatesciences.2009.09.005 (Effect of sintering temperature and thermoelectric power studies of th...)

## Cr-Fe-S
- rank 1676 | 3 samples | 2 papers | 3 compositions
- compositions: FeCr2S4 (1); Fe0.86Cu0.14Cr2S4 (1); Fe0.94Cu0.06Cr2S4 (1)
- dopant candidates (<5% at.): Cu (2)
- measured range: 10-494 K (5th-95th pct of 3 curves; full span incl. outliers 10-550 K)
- [ref 1] TEDesignLab / ICSD: Cr2FeS4 Fd-3m (227) mp-21019 [hull=0.096, icsd=16, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Cr12Fe3S20 P-1 (2) mp-1226707 [hull=0.053, PRIMARY]; Cr8Fe2CuNiS16 R3m (160) mp-1226149 [hull=0.068, PRIMARY]; Cr8Fe3NiS16 R3m (160) mp-1226423 [hull=0.067, PRIMARY]; CrFeS2 P-3m1 (164) mp-1226240 [hull=0.262, PRIMARY]; CrFeS4 Imma (74) mp-1226336 [hull=0.304, PRIMARY]
- papers: https://doi.org/10.1143/jjap.17.1745 (Preparation of Some Chalcogenide Spinel Single Crystals and Their Elec...) | https://doi.org/10.1063/1.2163563 (Electrical Transport in FeCr2S4‐CuCr2S4 Spinels)

## Cr-Ge-Si
- rank 1677 | 3 samples | 1 papers | 1 compositions
- compositions: Si0.8Ge0.2B0.016(CrSi2)0.091 (3)
- dopant candidates (<5% at.): B (3)
- sample form: Bulk (3)
- measured range: 293-1142 K (5th-95th pct of 12 curves)
- papers: https://doi.org/10.1063/1.4764919 (Comparison of thermoelectric properties of p-type nanostructured bulk ...)

## Cr-Mo-Si
- rank 1678 | 3 samples | 1 papers | 3 compositions
- compositions: Cr0.8Mo0.2Si2 (1); Cr0.7Mo0.3Si2 (1); Cr0.75Mo0.25Si2 (1)
- measured range: 320-1070 K (5th-95th pct of 11 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cr3Si2Mo3 R32 (155) mp-1226248 [hull=0.046, PRIMARY]; CrSiMo Amm2 (38) mp-1226241 [hull=0.182, PRIMARY]
- papers: https://doi.org/10.1016/j.jpcs.2015.08.017 (Thermoelectric properties of Cr 1−x Mo x Si 2)

## Cs-N-Si
- rank 1679 | 3 samples | 1 papers | 1 compositions
- compositions: Si NCs (3)
- sample form: Bulk (1)
- measured range: 321-449 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1039/c4nr04688a (Pseudo-direct bandgap transitions in silicon nanocrystals: effects on ...)

## Cs-Na-Si
- rank 1680 | 3 samples | 2 papers | 1 compositions
- compositions: Cs8Na16Si136 (3)
- measured range: 10-301 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CsNa2Si17 Fd-3m (227) mp-4877 [hull=0.000, icsd=6, PRIMARY]; Cs7NaSi8 Pa-3 (205) mp-1199908 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1109/ict.2005.1519927 (Synthesis and transport properties of type II clathrates) | https://doi.org/10.1063/1.1471370 (Temperature dependent structural and transport properties of the type ...)

## Cu-Eu-O-Ru-Sr
- rank 1681 | 3 samples | 2 papers | 2 compositions
- compositions: RuSr2EuCu2O8 (2); RuSr2Eu1.5Ce0.5Cu2O10 (1)
- dopant candidates (<5% at.): Ce (1)
- measured range: 11-257 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/j.physc.2006.03.123 (Anomalous lattice expansion of RuSr2Eu1.5Ce0.5Cu2O10−δ (Ru-1222) magne...) | https://doi.org/10.1016/s0921-4534(00)01753-6 (Synthesis and physical properties of superconducting RuSr2EuCu2O8)

## Cu-Eu-O-Sr
- rank 1682 | 3 samples | 2 papers | 3 compositions
- compositions: (Nb0.5Cu0.5)Sr2EuCu2O8 (1); Sr0.78Eu0.22CuO2 (1); Sr0.796Eu0.204CuO2 (1)
- dopant candidates (<5% at.): Nb (1)
- measured range: 11-300 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/j.jallcom.2015.06.001 (Structure and superconductivity in new Nb-based cuprates (Nb,Ti,Cu)Sr2...) | https://doi.org/10.1103/physrevb.106.l100503 (Percolative superconductivity in electron-doped \n<mml:math xmlns:mml=...)

## Cu-Fe-Ge-Se-Zn
- rank 1683 | 3 samples | 1 papers | 3 compositions
- compositions: Cu2Zn0.4Fe0.6GeSe4 (1); Cu2Zn0.6Fe0.4GeSe4 (1); Cu2Zn0.5Fe0.5GeSe4 (1)
- measured range: 299-677 K (5th-95th pct of 9 curves)
- papers: https://doi.org/10.1021/ja308627v (Phonon Scattering through a Local Anisotropic Structural Disorder in t...)

## Cu-Fe-O-Sr
- rank 1684 | 3 samples | 3 papers | 2 compositions
- compositions: SrFe0.7Cu0.3O3 (2); SrFe0.6Cu0.3W0.1O3 (1)
- dopant candidates (<5% at.): W (1)
- measured range: 370-1072 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrFe4(CuO4)3 Im-3 (204) mp-1105138 [hull=0.000, icsd=9, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2021.159127 (Copper doped SrFe0.9-Cu W0.1O3- (x = 0–0.3) perovskites as cathode mat...) | https://doi.org/10.1016/j.electacta.2014.10.137 (Electrochemical performance of novel cobalt-free perovskite SrFe0.7Cu0...) | https://doi.org/10.1016/j.jpowsour.2021.229877 (Insights into the oxygen reduction reaction on Cu-doped SrFeO3- cathod...)

## Cu-Fe-O-Zn
- rank 1685 | 3 samples | 2 papers | 3 compositions
- compositions: Cu0.6Zn0.4Fe2O4 (1); Cu0.4Zn0.6Fe2O4 (1); Cu0.5Zn0.5Fe2O4 (1)
- measured range: 303-483 K (5th-95th pct of 3 curves; full span incl. outliers 303-621 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZnFe4CuO8 R3m (160) mp-1215656 [hull=0.041, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(99)00287-x (Thermoelectric power studies of zinc substituted copper ferrites) | https://doi.org/10.1016/j.jmmm.2015.04.104 (Investigation of structural and temperature dependent electromagnetic ...)

## Cu-Ge-S-Se-Zn
- rank 1686 | 3 samples | 1 papers | 3 compositions
- compositions: Cu2ZnGeSe2S2 (1); Cu2ZnGeSe3S (1); Cu2ZnGeSe1S3 (1)
- sample form: Bulk (3)
- measured range: 298-676 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZnCu2Ge(SeS)2 Pmn2_1 (31) mp-1215417 [hull=0.006, PRIMARY, AMBIGUOUS]; ZnCu2Ge(SeS)2 Fmm2 (42) mp-1215643 [hull=0.015]
- papers: https://doi.org/10.1021/ja410753k (Effect of Isovalent Substitution on the Thermoelectric Properties of t...)

## Cu-Ge-Yb
- rank 1687 | 3 samples | 3 papers | 1 compositions
- compositions: YbCu2Ge2 (3)
- sample form: Other (1); SingleCrystal (1)
- measured range: 16-350 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb(CuGe)2 I4/mmm (139) mp-13401 [hull=0.000, icsd=3, PRIMARY]; YbCuGe P6_3/mmc (194) mp-5111 [hull=0.000, icsd=2, PRIMARY]; Yb3(CuGe)4 Immm (71) mp-1095653 [hull=0.000, icsd=2, PRIMARY]; Yb2CuGe6 C2/m (12) mp-1189806 [hull=0.000, icsd=1, PRIMARY]; YbCuGe F-43m (216) mp-13306 [hull=0.163, icsd=1]
- papers: https://doi.org/10.1063/1.4847455 (Influence of rare earth doping on thermoelectric properties of SrTiO3 ...) | https://doi.org/10.1063/1.4916786 (Interplay of chemical expansion, Yb valence, and low temperature therm...) | https://doi.org/10.1143/jpsj.78.084711 (de Haas–van Alphen Effect and Fermi Surface Properties in High-Quality...)

## Cu-Hg-Se-Sn-Te
- rank 1688 | 3 samples | 1 papers | 3 compositions
- compositions: Cu2HgSnSe0.8Te3.2 (1); Cu2HgSnSe3.2Te0.8 (1); Cu2HgSnSe2Te2 (1)
- sample form: Bulk (3)
- measured range: 295-576 K (5th-95th pct of 14 curves)
- papers: https://doi.org/10.1007/s11664-014-3075-8 (Thermoelectric Properties of Cu2HgSnSe4-Cu2HgSnTe4 Solid Solution)

## Cu-In-U
- rank 1689 | 3 samples | 1 papers | 1 compositions
- compositions: UCu5In (3)
- sample form: SingleCrystal (3)
- measured range: 11-299 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UInCu5 Pnma (62) mp-1208657 [hull=0.029, PRIMARY]
- papers: https://doi.org/10.1016/s0921-4526(01)01322-9 (Single crystal study on a dense Kondo antiferromagnet UCu5In)

## Cu-La-Mn-O
- rank 1690 | 3 samples | 3 papers | 2 compositions
- compositions: La0.8Sr0.2Cu0.3Mn0.7O3 (2); LaCu0.25Mn0.75O3 (1)
- dopant candidates (<5% at.): Sr (2)
- measured range: 323-1428 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaMn4(CuO4)3 Im-3 (204) mp-1211392 [hull=0.024, PRIMARY]
- papers: https://doi.org/10.1016/j.electacta.2015.04.085 (Assessment of LaM0.25Mn0.75O3- (M = Fe, Co, Ni, Cu) as promising catho...) | https://doi.org/10.1149/1.2792193 (Evaluation of La[sub 0.8]Sr[sub 0.2]Cu[sub 1−x]Mn[sub x]O[sub y] Doubl...) | https://doi.org/10.1149/1.2729216 (Evaluation of La0.8Sr0.2Cu1-xMnxOd Double Perovskite for Use in SOFCs)

## Cu-N-Ta
- rank 1691 | 3 samples | 1 papers | 3 compositions
- compositions: Cu0.35(TaN)0.65 (1); Cu0.3(TaN)0.7 (1); Cu0.25(TaN)0.75 (1)
- measured range: 274-373 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TaCuN2 R-3m (166) mp-8927 [hull=0.127, icsd=1, PRIMARY]
- papers: https://doi.org/10.3938/jkps.54.2323 (Electrical Resistivities and TCR Behavior of Co-Sputtered TaN-(Ag, Cu)...)

## Cu-Na-O-Sr
- rank 1692 | 3 samples | 1 papers | 3 compositions
- compositions: Sr1.5Na0.5CuO3 (1); Sr1.3Na0.7CuO3 (1); SrNaCuO3 (1)
- measured range: 36-279 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1002/zaac.19926161033 (Preparation and electrical and magnetic properties of Sr2?xNaxCuO3 (0 ...)

## Cu-Nb-Se-Tl
- rank 1693 | 3 samples | 1 papers | 1 compositions
- compositions: Tl3CuNb2Se12 (3)
- measured range: 80-301 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1021/cm050412c (Exploring Thallium Compounds as Thermoelectric Materials:  Seventeen N...)

## Cu-Nd-Ni-O-Sr
- rank 1694 | 3 samples | 1 papers | 3 compositions
- compositions: Nd1.6Sr1.4Ni0.6Cu0.4O4 (1); Nd1.6Sr1.4Ni0.5Cu0.5O4 (1); Nd1.6Sr1.4Ni0.4Cu0.6O4 (1)
- measured range: 13-296 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr5Nd5Cu(NiO5)4 P1 (1) mp-743818 [hull=0.161, PRIMARY]
- papers: https://doi.org/10.1088/1742-6596/121/5/052013 (Pressure studies on the electrical properties in R2-xSrxNi1-yCuyO4+δ(R...)

## Cu-Ni-Si-Yb
- rank 1695 | 3 samples | 1 papers | 3 compositions
- compositions: Yb(Ni0.125Cu0.875)2Si2 (1); Yb(Ni0.375Cu0.625)2Si2 (1); Yb(Ni0.625Cu0.375)2Si2 (1)
- sample form: Polycrystal (3)
- measured range: 10-298 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1023/a:1021801903961 (Thermopower of Yb Heavy Fermion Compounds at High Pressure)

## Cu-O-Sb-Se-Sr
- rank 1696 | 3 samples | 1 papers | 1 compositions
- compositions: SrOCuSbSe2 (3)
- sample form: Polycrystal (2); SingleCrystal (1)
- measured range: 140-851 K (5th-95th pct of 11 curves)
- papers: https://doi.org/10.1021/acs.chemmater.8b02651 (Observation of High Seebeck Coefficient and Low Thermal Conductivity i...)

## Cu-O-Se
- rank 1697 | 3 samples | 1 papers | 2 compositions
- compositions: (Cu2Se)22.94(Cu2O)77.06 (2); (Cu2Se)31.65(Cu2O)68.35 (1)
- measured range: 309-579 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuSeO3 Pnma (62) mp-22414 [hull=0.033, icsd=3, PRIMARY]; CuSeO5 P2_12_12_1 (19) mp-1194215 [hull=0.206, icsd=2, PRIMARY]; CuSe2O5 C2/c (15) mp-3199 [hull=0.000, icsd=2, PRIMARY]; Cu4Se3O10 P2_1/c (14) mp-1204253 [hull=0.000, icsd=1, PRIMARY]; UCu4(SeO7)2 Pmn2_1 (31) mp-1199963 [hull=0.078, icsd=1, PRIMARY]
- papers: https://doi.org/10.1134/s207511331701018x (The electrical properties of Cu2Se + Cu2O composites)

## Cu-P-Se
- rank 1698 | 3 samples | 2 papers | 1 compositions
- compositions: Cu7PSe6 (3)
- sample form: Bulk (2)
- measured range: 305-575 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu3PSe4 Pmn2_1 (31) mp-5756 [hull=0.000, icsd=3, PRIMARY]; Cu7PSe6 Pna2_1 (33) mp-29823 [hull=0.061, icsd=1, PRIMARY]; CuPSe2 P3m1 (156) mp-1225697 [hull=0.162, PRIMARY]; Cu7PSe6 P2_13 (198) mp-1201955 [hull=0.081, icsd=1]; Cu7PSe6 P1 (1) mp-676863 [hull=0.079]
- papers: https://doi.org/10.1021/ja5056092 (Thermoelectric Transport in Cu7PSe6with High Copper Ionic Mobility) | https://doi.org/10.1021/acs.chemmater.7b00767 (High Electron Mobility and Disorder Induced by Silver Ion Migration Le...)

## Cu-S-Sc-Ti
- rank 1699 | 3 samples | 1 papers | 3 compositions
- compositions: Cu2ScTi3S8 (1); Cu2Sc1.5Ti2.5S8 (1); Cu2Sc2Ti2S8 (1)
- sample form: Bulk (3)
- measured range: 301-752 K (5th-95th pct of 15 curves)
- papers: https://doi.org/10.1016/j.jallcom.2021.159548 (A comparative study of thermoelectric Cu2TrTi3S8 (Tr = Co and Sc) thio...)

## Cu-S-Te
- rank 1700 | 3 samples | 1 papers | 3 compositions
- compositions: Cu2S0.50Te0.50 (1); Cu2S0.52Te0.48 (1); Cu2S0.54Te0.46 (1)
- sample form: Bulk (3)
- measured range: 296-1012 K (5th-95th pct of 15 curves)
- papers: https://doi.org/10.1002/adma.201501030 (Ultrahigh Thermoelectric Performance in Mosaic Crystals)
