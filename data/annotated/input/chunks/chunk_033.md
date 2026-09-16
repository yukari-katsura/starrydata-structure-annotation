# Host systems -- chunk 033 of 73

Ranks 1601-1650 by sample count. These 50 host systems cover 150 samples (0.29% of the TE set); cumulative through this chunk: 94.45%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Bi-La-Te
- rank 1601 | 3 samples | 2 papers | 3 compositions
- compositions: La22.9Bi34.0Te43.1 (1); La3Te3.20Bi0.80 (1); La3Te3.35Bi0.65 (1)
- measured range: 294-1273 K (5th-95th pct of 11 curves)
- papers: Solvothermal synthesis and thermoelectric properties of lanthanum contained Bi–Te and Bi–Se–Te alloys | Electron and phonon scattering in the high-temperature thermoelectricLa3Te4−zMz(M=Sb,Bi)

## Bi-Mg-Si
- rank 1602 | 3 samples | 1 papers | 3 compositions
- compositions: Mg2Si0.75Bi0.25 (1); Mg2Si0.625Bi0.375 (1); Mg2Si0.5Bi0.5 (1)
- measured range: 95-1207 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg63Si32Bi P-43m (215) mp-1194890 [hull=0.068, icsd=1, PRIMARY]; Mg64Si32Bi Pm-3m (221) mp-1194936 [hull=0.086, icsd=1, PRIMARY]; Mg64Si31Bi Pm-3m (221) mp-1195280 [hull=0.059, icsd=1, PRIMARY]; Mg14SiBi P-6m2 (187) mp-1026682 [hull=0.074, PRIMARY]; Mg6SiBi Amm2 (38) mp-1017330 [hull=0.131, PRIMARY]
- papers: Enhancement of figure of merit (ZT) by doping Bi in Mg2Si for energy harvesting applications

## Bi-Mn-S-Se
- rank 1603 | 3 samples | 1 papers | 3 compositions
- compositions: MnBi4S6.16Se0.70 (1); MnBi4S5.46Se1.40 (1); MnBi4S5.86Se1.00 (1)
- measured range: 317-774 K (5th-95th pct of 11 curves)
- papers: Thermoelectricity of n-type MnBi4S7-7xSe7x solid solution

## Bi-O-Os
- rank 1604 | 3 samples | 1 papers | 1 compositions
- compositions: Bi3Os3O11 (3)
- measured range: 15-395 K (5th-95th pct of 3 curves)
- papers: Transport, thermal and magnetic properties of Bi3Os3O11 and Bi3Ru3O11

## Bi-O-Y
- rank 1605 | 3 samples | 3 papers | 3 compositions
- compositions: Y2O1.6Bi1.5 (1); Bi0.95Sr0.05YO3 (1); Y2O2Bi (1)
- dopant candidates (<5% at.): Sr (1)
- measured range: 21-298 K (5th-95th pct of 3 curves; full span incl. outliers 21-1012 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y2BiO2 I4/mmm (139) mp-1070510 [hull=0.000, icsd=1, PRIMARY]; Y(Bi5O8)3 Pm (6) mp-860892 [hull=0.051, PRIMARY]; Y(Bi3O5)4 I23 (197) mp-769643 [hull=0.058, PRIMARY]; Y(BiO2)3 R-3 (148) mp-754107 [hull=0.043, PRIMARY]; Y2Bi2O7 P2_1 (4) mp-772305 [hull=0.063, PRIMARY]
- papers: Two-Dimensional Superconductivity Emerged at Monatomic Bi<sup>2–</sup> Square Net in Layered Y<sub>2</sub>O<sub>2</sub>Bi via Oxygen Incorporation | Sr doped BiMO 3 (M = Mn, Fe, Y) perovskites: Structure correlated thermal and electrical properties | Magnetic and magnetotransport properties of ThCr<sub>2</sub>Si<sub>2</sub>-type Ce<sub>2</sub>O<sub>2</sub>Bi composed of conducting Bi<sup>2−</sup> square net and magnetic Ce−O layer

## Bi-Pb-Sb-Te
- rank 1606 | 3 samples | 2 papers | 2 compositions
- compositions: (Bi0.2Sb0.8)2Te3(PbTe)0.3 (2); (Bi0.2Sb0.8)2Te3(Pb0.7Sn0.3Te)0.77 (1)
- dopant candidates (<5% at.): Sn (1)
- measured range: 298-623 K (5th-95th pct of 13 curves)
- papers: Thermoelectric properties and extremely low lattice thermal conductivity in p-type Bismuth Tellurides by Pb-doping and PbTe precipitation | Thermoelectric Characteristics of p-Type (Bi,Sb)2Te3/(Pb,Sn)Te Functional Gradient Materials with Variation of the Segment Ratio

## Br-Na
- rank 1607 | 3 samples | 1 papers | 1 compositions
- compositions: NaBr (3)
- measured range: 12-87 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NaBr Fm-3m (225) mp-22916 [hull=0.000, icsd=7, PRIMARY]
- papers: Tunneling in NaBr:F−: Thermal and Dielectric Properties

## C-Cl-Cu-H-O-S
- rank 1608 | 3 samples | 1 papers | 1 compositions
- compositions: CuCl2.2((CH3)2SO) (3)
- papers: Low-temperature thermal conductivity of antiferromagnetic S = 1/2 chain material CuCl2·2((CH3)2SO)

## C-Cu-Ga-Te
- rank 1609 | 3 samples | 1 papers | 3 compositions
- compositions: CuGaTe2C0.5 (1); CuGaTe2C0.25 (1); CuGaTe2C0.38 (1)
- measured range: 281-876 K (5th-95th pct of 13 curves)
- papers: Enhanced thermoelectric performance of CuGaTe2 based composites incorporated with graphite nanosheets

## C-H-S-Ti
- rank 1610 | 3 samples | 2 papers | 3 compositions
- compositions: TiS2(C6H16N)0.08(H2O)0.22(C2H6SO)0.03 (1); TiS2(C6H16N)0.08(H2O)0.22(C2H6OS)0.03 (1); TiS2((C4H9)4N)0.013(C6H16N)0.019 (1)
- dopant candidates (<5% at.): N (3), O (2)
- measured range: 299-413 K (5th-95th pct of 19 curves)
- papers: Flexible n-type thermoelectric materials by organic intercalation of layered transition metal dichalcogenide TiS2 | Ultrahigh thermoelectric power factor in flexible hybrid inorganic-organic superlattice

## C-Hf
- rank 1611 | 3 samples | 2 papers | 3 compositions
- compositions: HfC0.67 (1); HfC0.98 (1); HfC (1)
- measured range: 296-1095 K (5th-95th pct of 3 curves; full span incl. outliers 296-1274 K)
- [ref 1] TEDesignLab / ICSD: HfC F-43m (216) mp-1002124 [hull=0.642, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: HfC Fm-3m (225) mp-21075 [hull=0.000, icsd=28, PRIMARY]; Hf3C I4/mmm (139) mp-976422 [hull=1.327, PRIMARY]; HfC P-6m2 (187) mp-1008832 [hull=0.764, icsd=1]; HfC Pm-3m (221) mp-1001918 [hull=1.342, icsd=1]; HfC P6_3/mmc (194) mp-1096993 [hull=0.203]
- papers: Mechanical, Thermal, and Oxidation Properties of Refractory Hafnium and zirconium Compounds | Low temperature densification mechanism and properties of Ta1-Hf C solid solutions with decarbonization and phase transition of Cr3C2

## C-Hf-Ta
- rank 1612 | 3 samples | 1 papers | 3 compositions
- compositions: Ta0.8Hf0.2C (1); Ta0.5Hf0.5C (1); Ta0.2Hf0.8C (1)
- measured range: 297-1274 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HfTa3C4 P-3m1 (164) mp-1224369 [hull=0.413, PRIMARY]; HfTaC2 R-3m (166) mp-1224285 [hull=0.000, PRIMARY]
- papers: Low temperature densification mechanism and properties of Ta1-Hf C solid solutions with decarbonization and phase transition of Cr3C2

## C-Mo-Zr
- rank 1613 | 3 samples | 1 papers | 3 compositions
- compositions: (ZrC)70.69(Mo)29.31 (1); (ZrC)58.45(Mo)41.55 (1); (ZrC)47.49(Mo)52.51 (1)
- measured range: 426-1278 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zr4MoC5 R-3m (166) mp-1215358 [hull=0.050, PRIMARY]; ZrMoC2 R-3m (166) mp-1215218 [hull=0.095, PRIMARY]
- papers: Thermal properties and thermal shock resistance of liquid phase sintered ZrC–Mo cermets

## C-Ti-Zr
- rank 1614 | 3 samples | 1 papers | 3 compositions
- compositions: (TiC)49(ZrC)49(Cr3C2)2 (1); (TiC)78.4(ZrC)19.6(Cr3C2)2 (1); (TiC)19.6(ZrC)78.4(Cr3C2)2 (1)
- dopant candidates (<5% at.): Cr (3)
- measured range: 297-1274 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZrTiC2 R-3m (166) mp-1215182 [hull=0.064, PRIMARY]; ZrTiC2 P4/mmm (123) mp-1215174 [hull=0.100]
- papers: Microstructural evolution, mechanical and thermal properties of TiC-ZrC-Cr3C2 composites

## C-U
- rank 1615 | 3 samples | 3 papers | 1 compositions
- compositions: UC (3)
- measured range: 22-2571 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UC Fm-3m (225) mp-2489 [hull=0.000, icsd=23, PRIMARY]; UC2 I4/mmm (139) mp-2486 [hull=0.000, icsd=12, PRIMARY]; U2C3 I-43d (220) mp-2625 [hull=0.000, icsd=9, PRIMARY]; U3C Pm-3m (221) mp-972103 [hull=0.534, PRIMARY]; UC2 Pa-3 (205) mp-1102444 [hull=0.293, icsd=1]
- papers: Thermal Aspects of Uranium Carbide and Uranium Dicarbide Fuels in Supercritical Water-Cooled Nuclear Reactors | Coupled analysis for new fuel design using UN and UC for SCWR | Etude de la structure electronique des carbures de thorium, d'uranium et de plutonium

## Ca-Cd-Sb
- rank 1616 | 3 samples | 2 papers | 3 compositions
- compositions: Ca1Cd2Sb2 (1); Yb0.2Ca0.8Cd2Sb2 (1); CaCd2Sb2 (1)
- dopant candidates (<5% at.): Yb (1)
- measured range: 296-651 K (5th-95th pct of 14 curves)
- [ref 1] TEDesignLab / ICSD: Ca(CdSb)2 P-3m1 (164) mp-7430 [hull=0.000, icsd=1, PRIMARY]; Ca2CdSb2 (62) [PRIMARY]
- papers: Zintl phase Yb1−xCaxCd2Sb2 with tunable thermoelectric properties induced by cation substitution | Synthesis and properties of CaCd2Sb2 and EuCd2Sb2

## Ca-Cd-Sb-Yb
- rank 1617 | 3 samples | 1 papers | 3 compositions
- compositions: Yb0.4Ca0.6Cd2Sb2 (1); Yb0.5Ca0.5Cd2Sb2 (1); Yb0.6Ca0.4Cd2Sb2 (1)
- measured range: 298-652 K (5th-95th pct of 15 curves)
- papers: Zintl phase Yb1−xCaxCd2Sb2 with tunable thermoelectric properties induced by cation substitution

## Ca-Co-Fe-Sb
- rank 1618 | 3 samples | 1 papers | 3 compositions
- compositions: CaFe2Co2Sb12 (1); CaFe2.5Co1.5Sb12 (1); CaFe3Co1Sb12 (1)
- measured range: 11-789 K (5th-95th pct of 19 curves)
- papers: Rare-earth free  p -type filled skutterudites: Mechanisms for low thermal conductivity and effects of Fe/Co ratio on the band structure and charge transport

## Ca-Co-La-Mn-O
- rank 1619 | 3 samples | 2 papers | 2 compositions
- compositions: LaCaMnCoO6 (2); La1.5Ca0.5CoMnO6 (1)
- measured range: 47-296 K (5th-95th pct of 2 curves)
- papers: Magnetic, transport, and magnetocaloric properties of double perovskite oxide LaCaMnCoO6 | Influence of magnetic frustration and structural disorder on magnetocaloric effect and magneto-transport properties in La<sub>1.5</sub>Ca<sub>0.5</sub>CoMnO<sub>6</sub> double perovskite

## Ca-Cr-O
- rank 1620 | 3 samples | 2 papers | 3 compositions
- compositions: Na0.25Ca0.75Cr2O4 (1); CaCr2O4 (1); Ca2CrO4 (1)
- dopant candidates (<5% at.): Na (1)
- measured range: 11-381 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca5Cr3ClO12 P6_3/m (176) mp-1196512 [hull=0.007, icsd=2, PRIMARY]; CaCrO4 I4_1/amd (141) mp-19215 [hull=0.000, icsd=2, PRIMARY]; Ca2CrO8 Cm (8) mp-795621 [hull=0.333, icsd=1, PRIMARY]; Ca5Cr3O12 Pnma (62) mp-1198286 [hull=0.022, icsd=1, PRIMARY]; Ca2Cr2O5 Ima2 (46) mp-1105485 [hull=0.148, icsd=1, PRIMARY]
- papers: Electronic, thermoelectric, and magneto-dielectric properties of Ca1−xNaxCr2O4 | High-pressure and high-temperature synthesis and physical properties of Ca2CrO4 solid

## Ca-Cu-O-Sr
- rank 1621 | 3 samples | 1 papers | 1 compositions
- compositions: (Sr0.7Ca0.3)0.9CuO2 (3)
- measured range: 11-298 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr3Ca(CuO2)4 Pmmm (47) mp-1218445 [hull=0.013, PRIMARY]; Sr3Ca(CuO3)2 Cm (8) mp-1218473 [hull=0.012, PRIMARY]; Sr4Ca2TlCu4PbO14 I4/mmm (139) mp-1173221 [hull=0.025, PRIMARY]; Sr6Ca4Cu17O29 C2/m (12) mp-1218738 [hull=0.026, PRIMARY]; Sr8Ca3NdTl2Cu8(PbO14)2 Fmmm (69) mp-1218785 [hull=0.027, PRIMARY]
- papers: Synthesis of the Carrier Doped Infinite-Layer Films by rf Thermal Plasma Evaporation

## Ca-In-Sb-Sr
- rank 1622 | 3 samples | 1 papers | 3 compositions
- compositions: Ca3.75Sr1.25In2Sb6 (1); Ca1.25Sr3.75In2Sb6 (1); Ca2.5Sr2.5In2Sb6 (1)
- measured range: 291-778 K (5th-95th pct of 8 curves)
- papers: Thermoelectric properties and electronic structure of the Zintl phase Sr5In2Sb6 and the Ca5−xSrxIn2Sb6 solid solution

## Ca-Mn-Nb-O
- rank 1623 | 3 samples | 2 papers | 2 compositions
- compositions: CaMn0.7Nb0.3O3 (2); CaMn0.75Nb0.25O3 (1)
- measured range: 332-1101 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca2MnNbO6 P2_1/c (14) mp-1227519 [hull=0.012, PRIMARY]
- papers: High-temperature transport properties of Nb and Ta substituted CaMnO3 system | High-temperature thermoelectric properties of polycrystalline CaMn1-Nb O3-δ

## Ca-Mn-O-Yb
- rank 1624 | 3 samples | 1 papers | 3 compositions
- compositions: CaMn0.7Yb0.3O3 (1); CaMn0.6Yb0.4O3 (1); CaMn0.5Yb0.5O3 (1)
- measured range: 304-1057 K (5th-95th pct of 4 curves; full span incl. outliers 304-1114 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaYb3Mn4O12 Pm (6) mp-1227162 [hull=0.010, PRIMARY]
- papers: Effect of the Yb substitutions on the thermoelectric properties of CaMnO3

## Ca-Mn-P-Zn
- rank 1625 | 3 samples | 1 papers | 3 compositions
- compositions: CaMnZnP2 (1); CaMnZn0.8Cu0.2P2 (1); CaMnZn0.9Cu0.1P2 (1)
- dopant candidates (<5% at.): Cu (2)
- measured range: 81-976 K (5th-95th pct of 11 curves)
- papers: Thermoelectric Properties of Light-Element-Containing Zintl Compounds CaZn2−x Cu x P2 and CaMnZn1−x Cu x P2 (x = 0.0–0.2)

## Ca-N
- rank 1626 | 3 samples | 1 papers | 2 compositions
- compositions: Ca3N2 (2); Ca2N (1)
- measured range: 17-327 K (5th-95th pct of 3 curves)
- [ref 1] TEDesignLab / ICSD: CaN6 Fddd (70) mp-676 [hull=0.000, icsd=2, PRIMARY]; Ca3N2 R-3c (167) mp-1047 [hull=0.014, icsd=3]; Ca3N2 P6_3/mmc (194) mp-13148 [hull=0.195, icsd=1]; Ca3N2 (12); Ca3N2 (60)
- [ref 2] MP, ranked by ICSD evidence: Ca2N R-3m (166) mp-2686 [hull=0.000, icsd=7, PRIMARY]; Ca3N2 Ia-3 (206) mp-844 [hull=0.000, icsd=5, PRIMARY]; CaN Fm-3m (225) mp-1058549 [hull=0.399, icsd=3, PRIMARY]; CaN2 I4/mmm (139) mp-1009657 [hull=0.000, icsd=1, PRIMARY]; Ca11N8 P4_2/mnm (136) mp-680640 [hull=0.201, icsd=1, PRIMARY]
- papers: β-Ca<sub>3</sub>N<sub>2</sub>, a Metastable Nitride in the System Ca-N

## Ca-O-Pb
- rank 1627 | 3 samples | 1 papers | 3 compositions
- compositions: Ca3PbO (1); Ca3Pb0.9Bi0.1O (1); Ca3Pb0.8Bi0.2O (1)
- dopant candidates (<5% at.): Bi (2)
- measured range: 15-297 K (5th-95th pct of 6 curves)
- [ref 1] TEDesignLab / ICSD: Ca2PbO4 Pbam (55) mp-21137 [hull=0.000, icsd=1, PRIMARY]; CaPbO3 Pnma (62) mp-20079 [hull=0.003, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ca3PbO Pm-3m (221) mp-20273 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric properties of antiperovskite calcium oxides Ca3PbO and Ca3SnO

## Ca-O-S
- rank 1628 | 3 samples | 1 papers | 2 compositions
- compositions: Dy0.002CaSO4 (2); CaSO4 (1)
- dopant candidates (<5% at.): Dy (2)
- measured range: 301-529 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaSO4 Cmcm (63) mp-4406 [hull=0.000, icsd=12, PRIMARY]; CaSO6 C2/c (15) mp-1189751 [hull=0.384, icsd=10, PRIMARY]; Ca2S2O9 C2 (5) mp-1198084 [hull=0.168, icsd=2, PRIMARY]; Ca(SO5)2 P6_4 (172) mp-1182310 [hull=0.523, icsd=1, PRIMARY]; Ca2S2O7 Pbcn (60) mp-1198348 [hull=0.380, icsd=1, PRIMARY]
- papers: Crystal growth and electrical properties of CaSO4:Dy single crystals

## Cd-Co-S
- rank 1629 | 3 samples | 1 papers | 3 compositions
- compositions: Co0.2Cd0.8S (1); Co0.1Cd0.9S (1); Co0.5Cd0.5S (1)
- measured range: 302-437 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cd4CoS5 Cm (8) mp-1226929 [hull=0.114, PRIMARY]
- papers: On the surface morphology and transport properties of chemical bath deposited CoxCd1−xS thin films: A correlation

## Cd-Cr-Se
- rank 1630 | 3 samples | 1 papers | 3 compositions
- compositions: CdCr1.95Sb0.05Se4 (1); CdCr1.94Sb0.06Se4 (1); CdCr1.92Sb0.08Se4 (1)
- dopant candidates (<5% at.): Sb (3)
- measured range: 275-472 K (5th-95th pct of 3 curves)
- [ref 1] TEDesignLab / ICSD: Cr2CdSe4 Fd-3m (227) mp-22605 [hull=0.000, icsd=12, PRIMARY]
- papers: On the n–p phase transition in CdCr2−xSbxSe4

## Cd-Cu-Se-Sn-Zn
- rank 1631 | 3 samples | 1 papers | 3 compositions
- compositions: Cu2Cd0.5Zn0.5SnSe4 (1); Cu2Cd0.4Zn0.6SnSe4 (1); Cu2Cd0.45Zn0.55SnSe4 (1)
- measured range: 298-721 K (5th-95th pct of 15 curves)
- papers: Crystal structure and thermoelectric properties of Cu2Cd1−xZnxSnSe4 solid solutions

## Cd-In-Te
- rank 1632 | 3 samples | 1 papers | 3 compositions
- compositions: Ag0.25Cd0.5In2.25Te4 (1); Ag0.1Cd0.8In2.1Te4 (1); Ag0.2Cd0.75In2.1Te4 (1)
- dopant candidates (<5% at.): Ag (3)
- measured range: 324-675 K (5th-95th pct of 3 curves)
- [ref 1] TEDesignLab / ICSD: Cd(InTe2)2 I-4 (82) mp-21374 [hull=0.000, icsd=2, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Cd3(InTe3)2 C2 (5) mp-1226986 [hull=0.016, PRIMARY]
- papers: Silver Indium Telluride Semiconductors and Their Solid Solutions with Cadmium Indium Telluride: Structure and Physical Properties

## Cd-Mg-Sb-Yb
- rank 1633 | 3 samples | 1 papers | 3 compositions
- compositions: YbCd1.6Mg0.4Sb2 (1); YbCd1.2Mg0.8Sb2 (1); YbCd1.4Mg0.6Sb2 (1)
- measured range: 299-651 K (5th-95th pct of 9 curves)
- papers: Thermoelectric properties of YbCd2Sb2 doped by Mg

## Cd-P
- rank 1634 | 3 samples | 2 papers | 2 compositions
- compositions: Cd3P2 (2); Cd3(P0.9As0.1)2 (1)
- dopant candidates (<5% at.): As (1)
- measured range: 71-526 K (5th-95th pct of 3 curves; full span incl. outliers 71-619 K)
- [ref 1] TEDesignLab / ICSD: CdP2 P4_12_12 (92) mp-12112 [hull=0.000, icsd=3, PRIMARY]; CdP4 P2_1/c (14) mp-7904 [hull=0.009, icsd=2, PRIMARY]; CdP2 Pna2_1 (33) mp-402 [hull=0.001, icsd=3]; CdP2 P4_32_12 (96) mp-913 [hull=0.000, icsd=2]
- [ref 2] MP, ranked by ICSD evidence: Cd3P2 P4_2/nmc (137) mp-2441 [hull=0.022, icsd=7, PRIMARY]; Cd7P10 Fdd2 (43) mp-29576 [hull=0.035, icsd=1, PRIMARY]; Cd3P Pm-3m (221) mp-1183632 [hull=0.270, PRIMARY]; Cd2P Pn-3m (224) mp-1213851 [hull=0.307, PRIMARY]; Cd3P2 Pn-3m (224) mp-21185 [hull=0.214, icsd=2]
- papers: Physical and electronic properties of semiconducting solid solutions of the Cd3 As2Cd3 P2 system | Preparation and Semiconducting Properties of Cd3P2

## Ce
- rank 1635 | 3 samples | 1 papers | 1 compositions
- compositions: Ce (3)
- measured range: 10-294 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce Fm-3m (225) mp-28 [hull=0.000, icsd=17, PRIMARY]; Ce P6_3/mmc (194) mp-20372 [hull=0.041, icsd=4]; Ce Cmcm (63) mp-64 [hull=0.039, icsd=3]; Ce Im-3m (229) mp-10024 [hull=0.231, icsd=1]
- papers: Thermoelectric power of α- and β-cerium

## Ce-Cu-In-Y
- rank 1636 | 3 samples | 1 papers | 3 compositions
- compositions: Ce0.25Y0.75InCu2 (1); Ce0.75Y0.25InCu2 (1); Ce0.5Y0.5InCu2 (1)
- measured range: 10-294 K (5th-95th pct of 6 curves)
- papers: Thermpower of Ce x Y1?x InCu2 and CeInCu y Ag2?y

## Ce-Cu-La
- rank 1637 | 3 samples | 2 papers | 3 compositions
- compositions: Ce0.61La0.39Cu6 (1); Ce0.38La0.62Cu6 (1); Ce0.5La0.5Cu6 (1)
- measured range: 10-277 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaCeCu12 Pmc2_1 (26) mp-1223412 [hull=0.007, PRIMARY]
- papers: Point contact spectra and transport properties of the dense Kondo substance CexLa1-xCu6 | Heavy fermion state in CeCu6

## Ce-Cu-Pd-Si
- rank 1638 | 3 samples | 1 papers | 3 compositions
- compositions: Ce(Pd0.75Cu0.25)2Si2 (1); Ce(Pd0.5Cu0.5)2Si2 (1); Ce(Pd0.15Cu0.85)2Si2 (1)
- measured range: 10-298 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeCuSi2Pd I-4m2 (119) mp-1226625 [hull=0.000, PRIMARY]
- papers: Low Temperature Thermoelectric Power of Ce(Pd $$_{1-x}$$ 1 - x Cu $$_x$$ x ) $$_2$$ 2 Si $$_2$$ 2

## Ce-Cu-Si-Y
- rank 1639 | 3 samples | 1 papers | 3 compositions
- compositions: Ce0.5Y0.5Cu2.05Si2 (1); Ce0.7Y0.3Cu2.05Si2 (1); Ce0.3Y0.7Cu2.05Si2 (1)
- measured range: 10-303 K (5th-95th pct of 3 curves)
- papers: Transport properties of<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">Ce</mml:mi></mml:mrow><mml:mrow><mml:mi>x</mml:mi></mml:mrow></mml:msub></mml:mrow><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">Y</mml:mi></mml:mrow><mml:mrow><mml:mn>1</mml:mn><mml:mi>−</mml:mi><mml:mi>x</mml:mi></mml:mrow></mml:msub></mml:mrow><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">Cu</mml:mi></mml:mrow><mml:mrow><mml:mn>2.05</mml:mn></mml:mrow></mml:msub></mml:mrow><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">Si</mml:mi></mml:mrow><mml:mrow><mml:mn>2</mml:mn></mml:mrow></mml:msub></mml:mrow><mml:mo>:</mml:mo></mml:math>A heavy-fermion alloy system on the border of valence fluctuation

## Ce-Eu-S
- rank 1640 | 3 samples | 1 papers | 3 compositions
- compositions: Ce2.6Eu0.4S4 (1); Ce2.4Eu0.6S4 (1); Ce2.2Eu0.8S4 (1)
- measured range: 298-674 K (5th-95th pct of 6 curves)
- papers: Preparation and thermoelectric properties of ternary rare earth sulfide γ-Ce3–xEuxS4

## Ce-Ga-Rh
- rank 1641 | 3 samples | 3 papers | 3 compositions
- compositions: CeRh2Ga2 (1); Ce2Rh3Ga9 (1); CeRh2Ga (1)
- measured range: 10-309 K (5th-95th pct of 8 curves; full span incl. outliers 10-388 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeGaRh Pnma (62) mp-1102417 [hull=0.000, icsd=1, PRIMARY]; Ce2(Ga3Rh)3 Cmcm (63) mp-1213907 [hull=0.000, PRIMARY]; Ce3(GaRh)2 Pbcm (57) mp-1213977 [hull=0.000, PRIMARY]
- papers: Kondo lattice heavy fermion behavior in CeRh<sub>2</sub>Ga<sub>2</sub> | Transport and magnetic properties of new ternary Ce2T3X9-compounds (T=Rh, Ir, X=Al, Ga) | Non-Fermi-liquid behavior in an undoped single crystal of<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">CeRh</mml:mi></mml:mrow><mml:mrow><mml:mn>2</mml:mn></mml:mrow></mml:msub></mml:mrow><mml:mi mathvariant=\"normal\">Ga</mml:mi></mml:math>

## Ce-Ga-Sn
- rank 1642 | 3 samples | 1 papers | 3 compositions
- compositions: Ce(Ga0.8Sn0.2)2 (1); Ce(Ga0.7Sn0.3)2 (1); Ce(Ga0.9Sn0.1)2 (1)
- measured range: 10-262 K (5th-95th pct of 3 curves)
- papers: Thermoelectric power and resistivity studies in the Kondo-lattice system CeGa2with Sn or Al substitutions and RGa2(R identical to Ho,Dy,Tb) alloys

## Ce-Ge-Pd
- rank 1643 | 3 samples | 3 papers | 1 compositions
- compositions: CePdGe (3)
- measured range: 11-299 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(GePd)2 I4/mmm (139) mp-13467 [hull=0.000, icsd=2, PRIMARY]; Ce3Ge5Pd14 Pnma (62) mp-680221 [hull=0.012, icsd=1, PRIMARY]; Ce3(Ge3Pd10)2 Fm-3m (225) mp-672275 [hull=0.023, icsd=1, PRIMARY]; CeGePd2 Pnma (62) mp-1188948 [hull=0.019, icsd=1, PRIMARY]; CeGePd Pnma (62) mp-21647 [hull=0.000, icsd=1, PRIMARY]
- papers: Thermoelectric power of CeTGe (T: Ni, Pd and Pt) | Electrical and magnetic properties of YbPdGe and YbPtGe | Magnetic, transport and specific heat measurements on CeTX (T = Pd and Pt, X = Ga, Ge and Sn)

## Ce-In
- rank 1644 | 3 samples | 3 papers | 1 compositions
- compositions: CeIn3 (3)
- measured range: 11-295 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeIn3 Pm-3m (221) mp-20369 [hull=0.000, icsd=11, PRIMARY]; Ce3In Pm-3m (221) mp-20984 [hull=0.000, icsd=6, PRIMARY]; Ce2In P6_3/mmc (194) mp-19733 [hull=0.009, icsd=3, PRIMARY]
- papers: Thermoelectric power and electrical resistivity of Ce(In1-xSnx)3 and (Ce1-xLaxIn3 | Thermoelectric power of the REIn3 single crystals where RE = La, Ce, Pr, Nd, Sm, Gd, Ho, ErIn3, TmandLu | Anomalously large thermoelectric cooling figure of merit in the Kondo systems CePd3 and Celn3

## Ce-In-Pd
- rank 1645 | 3 samples | 3 papers | 3 compositions
- compositions: CePdIn (1); Ce2PdIn8 (1); Ce6Pd12In5 (1)
- measured range: 11-299 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeInPd P-62m (189) mp-991729 [hull=0.000, icsd=5, PRIMARY]; Ce(In2Pd)2 Pnma (62) mp-641911 [hull=0.000, icsd=1, PRIMARY]; Ce2In5Pd4 P2_1/m (11) mp-604594 [hull=0.016, icsd=1, PRIMARY]; Ce2In8Pd P4/mmm (123) mp-1102172 [hull=0.000, icsd=1, PRIMARY]; Ce6In5Pd12 P6_3/mcm (193) mp-641689 [hull=0.010, icsd=1, PRIMARY]
- papers: Magnetic and Transport Properties of New Kondo Compounds CeTIn (T=Ni, Pd and Pt) | Quantum criticality in Ce2PdIn8: A thermoelectric study | Detailed investigation of thermal and electron transport properties in strongly correlated compound Ce6Pd12In5 and its nonmagnetic analog La6Pd12In5

## Ce-In-Pt
- rank 1646 | 3 samples | 3 papers | 3 compositions
- compositions: CePtIn (1); Ce3PtIn11 (1); Ce3Pt4In13 (1)
- measured range: 13-308 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeInPt P-62m (189) mp-640922 [hull=0.000, icsd=3, PRIMARY]; CeIn7Pt2 I4/mmm (139) mp-1078439 [hull=0.000, icsd=1, PRIMARY]; Ce12InPt7 I4/mcm (140) mp-637609 [hull=0.000, icsd=1, PRIMARY]; Ce(InPt)2 P2_1/m (11) mp-602328 [hull=0.006, icsd=1, PRIMARY]; Ce2In8Pt P4/mmm (123) mp-1103614 [hull=0.000, icsd=1, PRIMARY]
- papers: Magnetic and Transport Properties of New Kondo Compounds CeTIn (T=Ni, Pd and Pt) | Quantum Critical Behavior and Superconductivity in new multi-site Cerium Heavy Fermion Compound Ce3PtIn11 | Unusual Kondo behavior in the indium-rich heavy-fermion antiferromagnet<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">Ce</mml:mi></mml:mrow><mml:mrow><mml:mn>3</mml:mn></mml:mrow></mml:msub></mml:mrow><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">Pt</mml:mi></mml:mrow><mml:mrow><mml:mn>4</mml:mn></mml:mrow></mml:msub></mml:mrow><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">In</mml:mi></mml:mrow><mml:mrow><mml:mn>13</mml:mn></mml:mrow></mml:msub></mml:mrow></mml:math>

## Ce-La-Pd-Si
- rank 1647 | 3 samples | 1 papers | 3 compositions
- compositions: Ce0.7La0.3Pd2Si2 (1); Ce0.45La0.55Pd2Si2 (1); Ce0.3La0.7Pd2Si2 (1)
- measured range: 10-285 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaCe(SiPd)4 P4/mmm (123) mp-1222952 [hull=0.009, PRIMARY]
- papers: Thermoelectric power on Ce1−xLaxPd2Si2

## Ce-Nd-Ru
- rank 1648 | 3 samples | 1 papers | 3 compositions
- compositions: (Ce0.6Nd0.4)Ru2 (1); (Ce0.4Nd0.6)Ru2 (1); (Ce0.8Nd0.2)Ru2 (1)
- measured range: 10-289 K (5th-95th pct of 4 curves)
- papers: Transport properties of (Ce1−xRx)Ru2 (R  La, Nd)

## Ce-P-Ru
- rank 1649 | 3 samples | 1 papers | 3 compositions
- compositions: CeRu4P12 (1); La0.025Ce0.975Ru4P12 (1); La0.1Ce0.9Ru4P12 (1)
- dopant candidates (<5% at.): La (2)
- measured range: 91-652 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(P3Ru)4 Im-3 (204) mp-10069 [hull=0.000, icsd=2, PRIMARY]; Ce5P12Ru19 P-62m (189) mp-1203369 [hull=0.000, icsd=1, PRIMARY]
- papers: La doping effect in thermoelectric properties of skutterudite compound CeRu/sub 4/P/sub 12/

## Ce-Pd-Sb
- rank 1650 | 3 samples | 2 papers | 1 compositions
- compositions: CePdSb (3)
- measured range: 11-494 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeSb3Pd Pbcm (57) mp-1204615 [hull=0.000, icsd=1, PRIMARY]; Ce2(SbPd3)3 Cmcm (63) mp-18287 [hull=0.002, icsd=1, PRIMARY]; Ce(SbPd)2 P4/nmm (129) mp-1078778 [hull=0.031, icsd=1, PRIMARY]; Ce3Sb5Pd6 Pmmn (59) mp-662558 [hull=0.000, icsd=1, PRIMARY]; Ce8SbPd24 Pm-3m (221) mp-29101 [hull=0.030, icsd=1, PRIMARY]
- papers: Large thermoelectric power in several metallic compounds of cerium and uranium | Thermoelectric power of Ce-based Kondo alloys
