# Host systems -- chunk 035 of 73

Ranks 1701-1750 by sample count. These 50 host systems cover 150 samples (0.29% of the TE set); cumulative through this chunk: 95.03%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Cu-Sb-Zn
- rank 1701 | 3 samples | 3 papers | 3 compositions
- compositions: Cu0.8Sb0.4Zn2.4Sb1.8 (1); Zn3.6Cu0.4Sb3 (1); ZnSbSn0.02Cu0.15 (1)
- dopant candidates (<5% at.): Sn (1)
- sample form: Bulk (3)
- measured range: 297-721 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1016/j.cap.2008.06.012 (Effects of a Cu-contained compound on the microstructures and thermoel...) | https://doi.org/10.1016/j.matchar.2009.01.013 (Thermoelectric properties of Cu-added Zn–Sb based alloys with multi-ph...) | https://doi.org/10.1134/s1063782614040095 (Thermoelectric efficiency of intermetallic compound ZnSb)

## Cu-Se-Te
- rank 1702 | 3 samples | 1 papers | 3 compositions
- compositions: Cu2Se0.3Te0.7 (1); Cu2Se0.5Te0.5 (1); Cu2Se0.7Te0.3 (1)
- sample form: Bulk (3)
- measured range: 309-500 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuTeSe P2_13 (198) mp-1225744 [hull=0.048, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2020.155188 (Enhanced seebeck coefficient and low thermal conductivity of Cu2SexTe1...)

## Dy-Eu-Mn-O
- rank 1703 | 3 samples | 1 papers | 2 compositions
- compositions: Dy0.5Eu0.5MnO3 (2); Dy0.7Eu0.3MnO3 (1)
- measured range: 182-235 K (5th-95th pct of 2 curves; full span incl. outliers 182-305 K)
- papers: https://doi.org/10.1039/c8ra00224j (Modification of low temperature magnetic interactions in Dy1−xEuxMnO3)

## Dy-Ni-O
- rank 1704 | 3 samples | 1 papers | 1 compositions
- compositions: DyNiO3 (3)
- measured range: 299-483 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DyNiO3 Pnma (62) mp-19265 [hull=0.000, icsd=4, PRIMARY]
- papers: https://doi.org/10.1021/acsami.9b12609 (A d-Band Electron Correlated Thermoelectric Thermistor Established in ...)

## Er-Ni-Pd-Sb
- rank 1705 | 3 samples | 1 papers | 3 compositions
- compositions: ErNi0.75Pd0.25Sb (1); ErNi0.5Pd0.5Sb (1); ErNi0.25Pd0.75Sb (1)
- sample form: Bulk (3)
- measured range: 297-975 K (5th-95th pct of 15 curves)
- papers: https://doi.org/10.1063/1.2956699 (Substitution effect on the thermoelectric properties of p-type half-He...)

## Er-O-Zr
- rank 1706 | 3 samples | 1 papers | 1 compositions
- compositions: Er2Zr2O7 (3)
- measured range: 303-772 K (5th-95th pct of 3 curves; full span incl. outliers 303-873 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Er2Zr2O7 C2/m (12) mp-1178353 [hull=0.082, PRIMARY, AMBIGUOUS]; Er2Zr8O19 P-4m2 (115) mp-675556 [hull=0.093, PRIMARY]; Er4Zr3O12 P-1 (2) mp-675065 [hull=0.000, PRIMARY]; Er2Zr2O7 Fd-3m (227) mp-756545 [hull=0.082]; Er2Zr2O7 Pmma (51) mp-674842 [hull=0.152]
- papers: https://doi.org/10.31349/revmexfis.67.255 (Electrical and thermal conductivities of rare-earth A2Zr2O7 (A = Pr, N...)

## Er-Zr
- rank 1707 | 3 samples | 1 papers | 3 compositions
- compositions: Zr90.9Er9.1 (1); Zr95Er5 (1); Zr85.7Er14.3 (1)
- measured range: 299-673 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ErZr P-6m2 (187) mp-1225381 [hull=0.075, PRIMARY]
- papers: https://doi.org/10.3327/taesj.j14.040 (Phase State and Thermal and Mechanical Properties of Zr-Er Alloys)

## Eu-Ga
- rank 1708 | 3 samples | 1 papers | 1 compositions
- compositions: EuGa4 (3)
- sample form: SingleCrystal (3)
- measured range: 10-299 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): EuGa2 Imma (74) mp-22317 [hull=0.000, icsd=5, PRIMARY]; EuGa4 I4/mmm (139) mp-21884 [hull=0.000, icsd=3, PRIMARY]; Eu3Ga8 Immm (71) mp-1102706 [hull=0.038, icsd=2, PRIMARY]; Eu3Ga2 C2/c (15) mp-672286 [hull=0.000, icsd=1, PRIMARY]; EuGa P-1 (2) mp-1079244 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.7566/jpsj.84.124711 (Transport and Magnetic Properties of EuAl4 and EuGa4)

## Eu-Mn-O-Sr
- rank 1709 | 3 samples | 1 papers | 3 compositions
- compositions: Eu0.7Sr0.3MnO3 (1); Eu0.6Sr0.4MnO3 (1); Eu0.5Sr0.5MnO3 (1)
- sample form: Bulk (3)
- measured range: 12-297 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1016/j.jallcom.2016.05.098 (Structural, electrical, magnetic and thermal studies on Eu 1-x Sr x Mn...)

## Eu-Nd-Ni-O
- rank 1710 | 3 samples | 1 papers | 3 compositions
- compositions: Nd0.70Eu0.30NiO3 (1); Nd0.75Eu0.25NiO3 (1); Nd0.65Eu0.35NiO3 (1)
- sample form: Bulk (3)
- measured range: 11-392 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1063/1.2710738 (Magnetothermopower in Nd1−xEuxNiO3 compounds)

## Eu-Ni-O-Sm
- rank 1711 | 3 samples | 1 papers | 1 compositions
- compositions: Sm0.75Eu0.25NiO3 (3)
- measured range: 299-483 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1021/acsami.9b12609 (A d-Band Electron Correlated Thermoelectric Thermistor Established in ...)

## Eu-O-Ru
- rank 1712 | 3 samples | 1 papers | 3 compositions
- compositions: Pb0.4Eu0.6Ru2O7 (1); Eu2Ru2O7 (1); Pb0.2Eu0.8Ru2O7 (1)
- dopant candidates (<5% at.): Pb (2)
- measured range: 18-246 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Eu2Ru2O7 Fd-3m (227) mp-637431 [hull=0.000, icsd=2, PRIMARY]; Eu3RuO7 Cmcm (63) mp-22365 [hull=0.000, icsd=2, PRIMARY]; EuRuO3 Pm-3m (221) mp-866036 [hull=0.114, PRIMARY]
- papers: https://doi.org/10.2497/jjspm.65.249 (Metal-insulator Crossover in Pb-Ru Based Oxides with Pyrochlore-type S...)

## F-La-Mn-O-Sr
- rank 1713 | 3 samples | 1 papers | 1 compositions
- compositions: La1.4Sr1.6Mn2O7F2 (3)
- measured range: 148-295 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr3La2Mn6(O2F)6 P1 (1) mp-1173236 [hull=0.177, PRIMARY]; Sr5La2Mn8(O3F)6 P1 (1) mp-743681 [hull=0.154, PRIMARY]; Sr5La3Mn8(O2F)8 P1 (1) mp-694947 [hull=0.139, PRIMARY]; Sr5La3Mn8(O5F)4 P1 (1) mp-698712 [hull=0.069, PRIMARY]; SrLaMnO4F P4/nmm (129) mp-1218175 [hull=0.091, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2014.10.099 (Electrical properties of fluorine-intercalated layered manganite: La 1...)

## Fe-Ge-Li-O
- rank 1714 | 3 samples | 1 papers | 3 compositions
- compositions: Li0.7Ge0.4Fe1.9O4 (1); Li0.8Ge0.6Fe1.6O4 (1); Li0.9Ge0.8Fe1.2O4 (1)
- measured range: 310-420 K (5th-95th pct of 3 curves; full span incl. outliers 310-581 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiFe(GeO3)2 P2_1/c (14) mp-645305 [hull=0.000, icsd=11, PRIMARY]; Li2FeGeO4 Pmn2_1 (31) mp-1210923 [hull=0.000, PRIMARY]; Li3Fe2(GeO4)3 Ia-3d (230) mp-1013849 [hull=0.128, PRIMARY]; LiFe(GeO3)2 C2/c (15) mp-24979 [hull=0.007, icsd=4]
- papers: https://doi.org/10.1023/a:1020044430832 ([])

## Fe-I-O
- rank 1715 | 3 samples | 1 papers | 3 compositions
- compositions: (Fe)66.54(I2O3)33.46 (1); (Fe)44.68(I2O3)55.32 (1); (Fe)54.76(I2O3)45.24 (1)
- measured range: 16-159 K (5th-95th pct of 2 curves; full span incl. outliers 16-300 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe(IO3)3 P6_3 (173) mp-24993 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1109/tmag.2011.2158302 (Abnormal Resistance and Magnetoresistance Temperature Dependence in Fe...)

## Fe-In-Mg-O-Yb-Zn
- rank 1716 | 3 samples | 1 papers | 3 compositions
- compositions: In0.4Yb0.6FeZn0.6Mg0.4O4 (1); In0.4Yb0.6FeZn0.5Mg0.5O4 (1); In0.4Yb0.6FeZn0.4Mg0.6O4 (1)
- sample form: Bulk (3)
- measured range: 299-1273 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/j.jallcom.2016.05.064 (Thermal and mechanical properties of Yb&Mg co-doped InFeZnO4)

## Fe-La-Ni-O-Sr
- rank 1717 | 3 samples | 2 papers | 2 compositions
- compositions: La1.5Sr0.5Ni0.5Fe0.5O4 (2); La0.7Sr0.3Ti0.1Fe0.6Ni0.3O3 (1)
- dopant candidates (<5% at.): Ti (1)
- sample form: pellets (1)
- measured range: 383-1073 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.electacta.2016.10.025 (Electrochemical Performance of La 1.5 Sr 0.5 Ni 1-x Fe x O 4+ δ Cathod...) | https://doi.org/10.1016/j.jpowsour.2020.228498 (Performance evaluation of highly active and novel La0.7Sr0.3Ti0.1Fe0.6...)

## Fe-La-Si
- rank 1718 | 3 samples | 2 papers | 3 compositions
- compositions: LaFe11.40Co0.52Si1.09 (1); LaFe11.5Si1.5 (1); La(Fe0.88Si0.12)13 (1)
- dopant candidates (<5% at.): Co (1)
- measured range: 26-343 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(FeSi)2 I4/mmm (139) mp-4088 [hull=0.000, icsd=3, PRIMARY]; LaFe9Si4 I4/mcm (140) mp-662529 [hull=0.014, icsd=2, PRIMARY]; LaFeSi2 Cmcm (63) mp-1080643 [hull=0.000, icsd=1, PRIMARY]; LaFe8Si5 I4/mcm (140) mp-1211378 [hull=0.033, PRIMARY, AMBIGUOUS]; La2FeSi3 P-6m2 (187) mp-1223271 [hull=0.161, PRIMARY]
- papers: https://doi.org/10.1063/1.4801424 (The maximal cooling power of magnetic and thermoelectric refrigerators...) | https://doi.org/10.1063/1.1643774 (Thermal transport properties of magnetic refrigerants La(FexSi1−x)13 a...)

## Fe-Mn
- rank 1719 | 3 samples | 1 papers | 3 compositions
- compositions: Fe0.9Mn0.1 (1); Fe0.8Mn0.2 (1); Fe0.7Mn0.3 (1)
- measured range: 300-300 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn3Fe Pmmm (47) mp-999545 [hull=0.026, icsd=1, PRIMARY]; MnFe P4/mmm (123) mp-1009134 [hull=0.093, icsd=1, PRIMARY]; MnFe3 P4/mmm (123) mp-999542 [hull=0.061, icsd=1, PRIMARY]; Mn7Fe3 P2_1 (4) mp-1221991 [hull=0.057, PRIMARY]; MnFe4 Fmmm (69) mp-1221635 [hull=0.040, PRIMARY]
- papers: https://doi.org/10.2320/jinstmet1952.63.11_1435 (Thermoelectric Properties of Fe-Mn-Si Alloys and Compound Fe3Si doped ...)

## Fe-Mn-Nd-O-Se
- rank 1720 | 3 samples | 1 papers | 3 compositions
- compositions: Nd2(Fe0.625Mn0.375)2Se2O3 (1); Nd2(Fe0.75Mn0.25)2Se2O3 (1); Nd2FeMnSe2O3 (1)
- measured range: 72-324 K (5th-95th pct of 9 curves)
- papers: https://doi.org/10.1016/j.jallcom.2014.08.145 (Synthesis, structure and properties of new layered oxyselenides Nd2(Fe...)

## Fe-Mn-Si-Ti
- rank 1721 | 3 samples | 1 papers | 3 compositions
- compositions: Fe2Ti0.77Mn0.23Si (1); Fe2Ti0.59Mn0.41Si (1); Fe2Ti0.42Mn0.58Si (1)
- measured range: 10-380 K (5th-95th pct of 9 curves)
- papers: https://doi.org/10.1038/s41598-020-76554-9 (Probing local distortion around structural defects in half-Heusler the...)

## Fe-Na-O-Ta
- rank 1722 | 3 samples | 1 papers | 1 compositions
- compositions: (Fe2O3)NaTaO3 (3)
- measured range: 566-1047 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1007/s40243-013-0021-2 (SPS-sintered NaTaO3–Fe2O3 composite exhibits enhanced Seebeck coeffici...)

## Fe-Ni-Sb-Yb
- rank 1723 | 3 samples | 3 papers | 3 compositions
- compositions: Yb0.95Fe3NiSb12 (1); YbFe3NiSb12 (1); Yb0.89Fe2.98Ni1.02Sb12 (1)
- sample form: Powder (1)
- measured range: 11-799 K (5th-95th pct of 11 curves)
- papers: https://doi.org/10.1016/j.actamat.2011.12.022 (Thermoelectric properties of p-type skutterudites YbxFe3.5Ni0.5Sb12 (0...) | https://doi.org/10.1063/1.4800827 (Thermoelectric performance of p-type skutterudites YbxFe4−yPtySb12 (0....) | https://doi.org/10.1016/j.jmst.2014.05.007 (Thermoelectric Transport Properties of RyFe3NiSb12 (R = Ba, Nd and Yb))

## Fe-O-Ti
- rank 1724 | 3 samples | 1 papers | 3 compositions
- compositions: Fe1.5Ti1.5O5 (1); FeTi2O5 (1); Fe2TiO5 (1)
- measured range: 299-801 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiFeO3 R-3 (148) mp-19417 [hull=0.000, icsd=23, PRIMARY]; TiFe2O5 Cmcm (63) mp-24977 [hull=0.022, icsd=2, PRIMARY]; Ti2FeO5 Cmcm (63) mp-31857 [hull=0.000, icsd=1, PRIMARY]; Ti3FeO7 Imm2 (44) mp-1103361 [hull=0.235, icsd=1, PRIMARY]; Ti(FeO2)2 Pmma (51) mp-1193065 [hull=0.149, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jpcs.2020.109802 (Structural, electronic, magnetic and thermoelectric properties of pseu...)

## Fe-Pr-Sb
- rank 1725 | 3 samples | 2 papers | 2 compositions
- compositions: PrFe4Sb12 (2); PrFe3.5Co0.5Sb12 (1)
- dopant candidates (<5% at.): Co (1)
- measured range: 298-824 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Pr6Fe13Sb I4/mcm (140) mp-1197545 [hull=0.017, icsd=2, PRIMARY]; PrFeSb2 P4/nmm (129) mp-1079872 [hull=0.114, icsd=2, PRIMARY]; PrFeSb3 Pbcm (57) mp-1200999 [hull=0.008, icsd=1, PRIMARY]; Pr(FeSb3)5 R-3 (148) mp-685871 [hull=0.000, PRIMARY]; Pr5Fe2Sb I4/mcm (140) mp-1209713 [hull=0.140, PRIMARY]
- papers: https://doi.org/10.3938/jkps.65.2071 (Preparation and thermoelectric properties of p-type Pr z Fe4− x Co x S...) | https://doi.org/10.1063/1.3553842 (High-temperature electrical and thermal transport properties of fully ...)

## Fe-Sb-Sr
- rank 1726 | 3 samples | 2 papers | 1 compositions
- compositions: SrFe4Sb12 (3)
- measured range: 10-800 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr(FeSb3)4 Im-3 (204) mp-1188542 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.physb.2006.03.067 (Roles of spin fluctuations and rattling in magnetic and thermoelectric...) | https://doi.org/10.1063/1.3553842 (High-temperature electrical and thermal transport properties of fully ...)

## Ga-In-N
- rank 1727 | 3 samples | 3 papers | 3 compositions
- compositions: In0.36Ga0.64N (1); In0.17Ga0.83N (1); In0.3Ga0.7N (1)
- sample form: Film (2); EpitaxialFilm (1)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 295-875 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): In3GaN4 P6_3mc (186) mp-1120750 [hull=0.023, PRIMARY]; InGa3N4 P3m1 (156) mp-1223879 [hull=0.060, PRIMARY]; InGaN2 P3m1 (156) mp-1223660 [hull=0.078, PRIMARY]; In3GaN4 P3m1 (156) mp-1224009 [hull=0.057]
- papers: https://doi.org/10.1063/1.2839309 (Thermoelectric properties of InxGa1−xN alloys) | https://doi.org/10.1063/1.3670966 (High temperature thermoelectric properties of optimized InGaN) | https://doi.org/10.1007/s11664-009-0676-8 (Thermoelectric Properties of In0.3Ga0.7N Alloys)

## Ga-In-Te
- rank 1728 | 3 samples | 1 papers | 3 compositions
- compositions: (Ga0.5In0.5)2Te3 (1); (Ga0.25In0.75)2Te3 (1); (Ga0.75In0.25)2Te3 (1)
- sample form: Bulk (3)
- measured range: 300-869 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): InGaTe2 I4/mcm (140) mp-20408 [hull=0.039, icsd=3, PRIMARY]; In3GaTe4 I-42m (121) mp-1223857 [hull=0.028, PRIMARY]
- papers: https://doi.org/10.1007/s11664-008-0654-6 (Thermoelectric Characterization of (Ga,In)2Te3 with Self-Assembled Two...)

## Ga-K-Si
- rank 1729 | 3 samples | 2 papers | 3 compositions
- compositions: K8Ga8Si38 (1); K7.4Ga7.7Si38.9 (1); K7.5Ga5.5Al2.2Si38.8 (1)
- dopant candidates (<5% at.): Al (1)
- measured range: 10-554 K (5th-95th pct of 16 curves)
- papers: https://doi.org/10.1021/cm504436v (Synthesis, Structure, Thermoelectric Properties, and Band Gaps of Alka...) | https://doi.org/10.1016/j.intermet.2016.11.006 (Synthesis and thermoelectric properties of the quaternary type-I Si cl...)

## Ga-O-Sn
- rank 1730 | 3 samples | 1 papers | 3 compositions
- compositions: Ga3InSn4.5Ti0.5O16 (1); Ga3InSn4TiO16 (1); Ga3InSn5O16 (1)
- dopant candidates (<5% at.): In (3), Ti (2)
- sample form: Bulk (3)
- measured range: 772-1273 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GaSnO3 Pm-3m (221) mp-1184243 [hull=0.575, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2012.02.056 (Thermoelectric properties and impedance spectroscopy of polycrystallin...)

## Ga-Sn
- rank 1731 | 3 samples | 1 papers | 3 compositions
- compositions: Ga90.15Sn6.64Zn3.21Na0.32 (1); Ga90.15Sn6.64Zn3.21Na0.16 (1); Ga90.15Sn6.64Zn3.21Na1.57 (1)
- dopant candidates (<5% at.): Zn (3), Na (3)
- measured range: 307-908 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ga3Sn I4/mmm (139) mp-1184031 [hull=0.049, PRIMARY, AMBIGUOUS]; GaSn3 I4/mmm (139) mp-1184266 [hull=0.049, PRIMARY]; Ga3Sn Fm-3m (225) mp-1183986 [hull=0.052]; Ga3Sn Pm-3m (221) mp-1183978 [hull=0.062]; GaSn3 P6_3/mmc (194) mp-1184285 [hull=0.068]
- papers: https://doi.org/10.1016/j.molliq.2019.112024 (Potential cooling agents for fast nuclear reactors: Sodium influence o...)

## Gd
- rank 1732 | 3 samples | 3 papers | 1 compositions
- compositions: Gd (3)
- measured range: 11-320 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd P6_3/mmc (194) mp-155 [hull=0.000, icsd=11, PRIMARY]; Gd R-3m (166) mp-1076915 [hull=0.018, icsd=3]; Gd Fm-3m (225) mp-614502 [hull=0.071, icsd=2]; Gd Im-3m (229) mp-11421 [hull=0.106, icsd=1]
- papers: https://doi.org/10.1109/tasc.2004.831058 (Thermal Property of Magnetic Materials for Hydrogen Magnetic Refrigera...) | https://doi.org/10.1063/1.1643774 (Thermal transport properties of magnetic refrigerants La(FexSi1−x)13 a...) | https://doi.org/10.1002/aelm.201700636 (Outstanding Comprehensive Performance of La(Fe, Si)<sub>13</sub>H<sub>...)

## Gd-S-Sm
- rank 1733 | 3 samples | 1 papers | 3 compositions
- compositions: SmGdS3 (1); SmGd1.02S3 (1); SmGd1.06S3 (1)
- measured range: 294-974 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sm(GdS2)2 I-42d (122) mp-676424 [hull=0.023, PRIMARY]; Sm4GdS5 Immm (71) mp-1219448 [hull=0.040, PRIMARY]; SmGdS2 R-3m (166) mp-1219007 [hull=0.000, PRIMARY]; SmGdS3 Pnma (62) mp-1219055 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1007/s11664-010-1436-5 (Preparation and Thermoelectric Properties of LaGd1+x S3 and SmGd1+x S3)

## Ge-Ir-La-Sb
- rank 1734 | 3 samples | 2 papers | 2 compositions
- compositions: La1Ir4Ge3Sb9 (2); LaIr4Ge3Sb9 (1)
- measured range: 298-951 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.stam.2004.02.006 (Enhancement of high temperature thermoelectric properties of intermeta...) | https://doi.org/10.1007/s11664-004-0117-7 (Effect of partial la filling on high-temperature thermoelectric proper...)

## Ge-La-Pd
- rank 1735 | 3 samples | 2 papers | 3 compositions
- compositions: La2PdGe6 (1); LaPd2Ge (1); LaPdGe3 (1)
- sample form: Bulk (2)
- measured range: 10-299 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(GePd)2 I4/mmm (139) mp-21033 [hull=0.000, icsd=2, PRIMARY]; La3(GePd)4 Immm (71) mp-22729 [hull=0.000, icsd=1, PRIMARY]; LaGePd C2/m (12) mp-1222934 [hull=0.017, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2012.01.036 (Physical properties of polycrystalline Dy2PdGe6 and La2PdGe6) | https://doi.org/10.1016/j.jallcom.2013.07.169 (Crystal structure and physical properties of LaPd2Ge and a novel compo...)

## Ge-Mn-Pb-Te
- rank 1736 | 3 samples | 1 papers | 3 compositions
- compositions: (Ge0.8Pb0.2)0.87Mn0.13Te (1); (Ge0.8Pb0.2)0.82Mn0.18Te (1); (Ge0.8Pb0.2)0.9Mn0.1Te (1)
- sample form: Bulk (3)
- measured range: 297-726 K (5th-95th pct of 15 curves)
- papers: https://doi.org/10.1016/j.jallcom.2014.09.198 (Effects of Mn substitution on the phases and thermoelectric properties...)

## Ge-Mo-Ru
- rank 1737 | 3 samples | 1 papers | 3 compositions
- compositions: Mo0.4Ru0.6Ge1.769 (1); Mo0.8Ru0.2Ge1.769 (1); Mo0.6Ru0.4Ge1.769 (1)
- sample form: Bulk (3)
- measured range: 298-973 K (5th-95th pct of 15 curves)
- papers: https://doi.org/10.1063/1.5065417 (Tuning valence electron concentration in the Mo13Ge23-Ru2Ge3 pseudobin...)

## Ge-P-Se
- rank 1738 | 3 samples | 1 papers | 1 compositions
- compositions: Ge30.6P15.4Se8 (3)
- measured range: 326-662 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1021/ic3011025 (Synthesis, Structure, and Transport Properties of Type-I Derived Clath...)

## H-Ni-P
- rank 1739 | 3 samples | 1 papers | 1 compositions
- compositions: NiTPP (3)
- measured range: 300-380 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1007/s00339-014-8737-0 (Polaron activation energy of nano porphyrin nickel(II) thin films)

## H-P-V
- rank 1740 | 3 samples | 1 papers | 1 compositions
- compositions: PTVT2T (3)
- measured range: 281-380 K (5th-95th pct of 9 curves)
- papers: https://doi.org/10.1039/c5ta07526b (Two soluble polymers with lower ionization potentials: doping and ther...)

## Hf-Ni-Sb
- rank 1741 | 3 samples | 2 papers | 3 compositions
- compositions: Hf3Ni2.9Co0.1Sb4 (1); Hf3Ni2.7Cu0.3Sb4 (1); Hf6NiSb2 (1)
- dopant candidates (<5% at.): Co (1), Cu (1)
- sample form: Other (2); Bulk (1)
- measured range: 10-861 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Hf3NiSb7 Pnma (62) mp-1195404 [hull=0.001, icsd=1, PRIMARY]; HfNi2Sb P6_3/mmc (194) mp-1078574 [hull=0.000, icsd=1, PRIMARY]; Hf6NiSb2 P-62m (189) mp-15297 [hull=0.000, icsd=1, PRIMARY]; Hf10NiSb5 I422 (97) mp-1224579 [hull=0.024, PRIMARY]; HfNiSb Pnma (62) mp-1212231 [hull=0.024, PRIMARY]
- papers: https://doi.org/10.1063/1.4928168 (Thermoelectric properties and electronic transport analysis of Zr3Ni3S...) | https://doi.org/10.1016/s0925-8388(99)00537-x (Thermoelectric properties of ternary transition metal antimonides)

## Hf-O
- rank 1742 | 3 samples | 1 papers | 1 compositions
- compositions: HfO (3)
- measured range: 80-301 K (5th-95th pct of 7 curves)
- [ref 1] TEDesignLab / ICSD: HfO2 P2_1/c (14) mp-352 [hull=0.000, icsd=11, PRIMARY]; HfO2 Pnma (62) mp-741 [hull=0.139, icsd=4]; HfO2 Pbca (61) mp-775757 [hull=0.010, icsd=3]; HfO2 P4_2/nmc (137) mp-1018721 [hull=0.055, icsd=1]; HfO2 (225)
- [ref 2] MP, ranked by ICSD evidence: Hf6PbO18 C2/m (12) mp-675600 [hull=0.408, PRIMARY]; Hf8PbO24 C2/m (12) mp-676713 [hull=0.424, PRIMARY]; HfO2 P4_2/mnm (136) mp-776532 [hull=0.025]; HfO2 Pbcn (60) mp-776097 [hull=0.028]; HfO2 Pca2_1 (29) mp-685097 [hull=0.029]
- papers: https://doi.org/10.1038/ncomms5598 (Thermoelectric Seebeck effect in oxide-based resistive switching memory)

## Ho-Ni-Sb
- rank 1743 | 3 samples | 3 papers | 1 compositions
- compositions: HoNiSb (3)
- sample form: Bulk (1)
- measured range: 11-994 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HoNiSb F-43m (216) mp-4174 [hull=0.000, icsd=3, PRIMARY]; Ho(NiSb)2 P4/nmm (129) mp-1079761 [hull=0.106, icsd=1, PRIMARY]; Ho5NiSb2 Pnma (62) mp-640383 [hull=0.000, icsd=1, PRIMARY]; Ho5Ni2Sb I4/mcm (140) mp-10500 [hull=0.000, icsd=1, PRIMARY]; HoNiSb2 P4/nmm (129) mp-1092222 [hull=0.025, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2019.152596 (High-temperature power factor of half-Heusler phases RENiSb (RE = Sc, ...) | https://doi.org/10.1016/j.matpr.2019.02.054 (High-temperature thermoelectric properties of half-Heusler phases Er1-...) | https://doi.org/10.1557/proc-545-421 (Observed Properties and Electronic Structure of RNiSb Compounds (R = H...)

## In-N-O
- rank 1744 | 3 samples | 2 papers | 2 compositions
- compositions: InO0.82N0.86 (2); Al0.02In0.98O1.14N0.49 (1)
- dopant candidates (<5% at.): Al (1)
- sample form: Film (1)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 299-957 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): In3NO3 R-3m (166) mp-778848 [hull=0.040, PRIMARY]; In3NO3 Ima2 (46) mp-1178163 [hull=0.060]
- papers: https://doi.org/10.1109/ict.2003.1287527 (Thermal and thermoelectric properties of III-nitride and III-oxynitrid...) | https://doi.org/10.1002/pssc.200303303 (Thermoelectric properties of Al1−xInxN and InOsNtprepared by reactive ...)

## In-Sb-Te
- rank 1745 | 3 samples | 3 papers | 3 compositions
- compositions: Sb1.9In0.5Te3 (1); Sb1.6In0.4Te3 (1); Sb1.85In1.5Te3 (1)
- measured range: 15-643 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): In10Sb9Te P-1 (2) mp-37501 [hull=0.187, PRIMARY]; In3SbTe2 Immm (71) mp-1223976 [hull=0.335, PRIMARY]; In3SbTe4 I422 (97) mp-1223951 [hull=0.463, PRIMARY]; In4SbTe3 Cm (8) mp-685941 [hull=0.246, PRIMARY]; In3SbTe2 P-3m1 (164) mp-1224005 [hull=0.350]
- papers: https://doi.org/10.1016/j.actamat.2014.11.023 (Enhanced figure of merit in antimony telluride thermoelectric material...) | https://doi.org/10.1103/physrevb.52.10915 (Valence-band changes inSb2−xInxTe3andSb2Te3−ySeyby transport and Shubn...) | https://doi.org/10.1038/srep23143 (A strategy to optimize the thermoelectric performance in a spark plasm...)

## In-Se-Si
- rank 1746 | 3 samples | 1 papers | 3 compositions
- compositions: In0.9Si0.1Se0.93Te0.07 (1); In0.9Si0.1Se (1); In0.9Si0.1Se0.97Te0.03 (1)
- dopant candidates (<5% at.): Te (2)
- sample form: Bulk (3)
- measured range: 102-690 K (5th-95th pct of 16 curves)
- papers: https://doi.org/10.1007/s13391-021-00278-9 (Thermoelectric Properties of Te-doped In0.9Si0.1Se with Enhanced Effec...)

## In-Se-Zn
- rank 1747 | 3 samples | 1 papers | 1 compositions
- compositions: ZnIn2Se4 (3)
- sample form: Bulk (3)
- measured range: 294-847 K (5th-95th pct of 7 curves)
- [ref 1] TEDesignLab / ICSD: Zn(InSe2)2 I-4 (82) mp-22607 [hull=0.000, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Zn(InSe2)3 R3m (160) mp-1216140 [hull=0.158, PRIMARY]; Zn(InSe2)2 I-42m (121) mp-34169 [hull=0.001]; Zn(InSe2)2 Fd-3m (227) mp-1001017 [hull=0.058]
- papers: https://doi.org/10.1016/j.jallcom.2019.05.238 (Novel n-type thermoelectric material of ZnIn2Se4)

## Ir-La-Mn-O-Sr
- rank 1748 | 3 samples | 1 papers | 1 compositions
- compositions: La0.4Sr0.6Mn0.6Ir0.4O3 (3)
- measured range: 53-300 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr4La2Mn3(IrO6)3 P-3m1 (164) mp-1218666 [hull=0.062, PRIMARY]
- papers: https://doi.org/10.1021/acsami.2c01849 (Emergence of Insulating Ferrimagnetism and Perpendicular Magnetic Anis...)

## Ir-O-Pr
- rank 1749 | 3 samples | 2 papers | 2 compositions
- compositions: Pr2Ir2O7 (2); 	Pr2Ir2O7 (1)
- sample form: Polycrystal (2)
- measured range: 13-292 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Pr3IrO7 Cmcm (63) mp-5322 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1143/jpsj.76.043706 (Metal–Insulator Transition in Pyrochlore IridatesLn2Ir2O7(Ln= Nd, Sm, ...) | https://doi.org/10.1103/physrevb.103.165135 (Unified description of resistivity and thermopower of<mml:math xmlns:m...)

## Ir-Pt
- rank 1750 | 3 samples | 1 papers | 3 compositions
- compositions: Pt94.2Ir5.8 (1); Pt90.2Ir9.8 (1); Pt92.2Ir7.8 (1)
- measured range: 20-118 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): IrPt R-3m (166) mp-1223665 [hull=0.087, PRIMARY]; IrPt3 Pm-3m (221) mp-1184759 [hull=0.080, PRIMARY]
- papers: https://doi.org/10.1007/bf00655330 (Comments upon ?the thermoelectric power of someThCe alloys? and an alt...)
