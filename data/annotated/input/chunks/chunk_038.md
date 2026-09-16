# Host systems -- chunk 038 of 73

Ranks 1851-1900 by sample count. These 50 host systems cover 100 samples (0.19% of the TE set); cumulative through this chunk: 95.72%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Al-Ce-Rh
- rank 1851 | 2 samples | 2 papers | 2 compositions
- compositions: Ce2Rh3Al9 (1); Ce2Rh2Al9 (1)
- measured range: 10-297 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeAlRh Pnma (62) mp-3344 [hull=0.000, icsd=2, PRIMARY]; Ce2(Al3Rh)3 Cmcm (63) mp-1213916 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(98)00408-3 (Transport and magnetic properties of new ternary Ce2T3X9-compounds (T=...) | https://doi.org/10.1016/s0925-8388(97)00174-6 (Crystallographic and physical properties of new ternary R2T3X9 (R=La, ...)

## Al-Co-Cr-Ni-O-Y-Zr
- rank 1852 | 2 samples | 1 papers | 2 compositions
- compositions: (ZrO2)77.66(NiCoCrAlY)22.34 (1); (ZrO2)60.7(NiCoCrAlY)39.3 (1)
- measured range: 302-408 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.2497/jjspm.37.313 (Evaluation on thermomechanical properties of functionally gradient mat...)

## Al-Co-Fe
- rank 1853 | 2 samples | 2 papers | 2 compositions
- compositions: Co2FeAl (1); Fe2CoAl (1)
- measured range: 301-1014 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlFeCo2 Fm-3m (225) mp-10884 [hull=0.000, icsd=1, PRIMARY]; Al2FeCo Fm-3m (225) mp-862691 [hull=0.000, PRIMARY, AMBIGUOUS]; Al2FeCo P4/mmm (123) mp-1228905 [hull=0.000]
- papers: https://doi.org/10.1007/s11664-016-4944-0 (Structural and Thermoelectric Properties of Ternary Full-Heusler Alloys) | https://doi.org/10.1063/1.5029868 (Magnetic and thermoelectric properties of melt-spun ribbons of Fe2XAl ...)

## Al-Co-Pr
- rank 1854 | 2 samples | 1 papers | 2 compositions
- compositions: PrCo2Al8 (1); Pr2Co6Al19 (1)
- measured range: 12-299 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Pr7Al7Co6 P4/mbm (127) mp-5711 [hull=0.044, icsd=2, PRIMARY]; Pr2AlCo2 C2/c (15) mp-11928 [hull=0.032, icsd=1, PRIMARY]; Pr2Al3Co14 R-3m (166) mp-1106291 [hull=0.074, icsd=1, PRIMARY]; Pr2Al2Co15 R-3m (166) mp-1188126 [hull=0.049, icsd=1, PRIMARY]; PrAl4Co Pmma (51) mp-975726 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2005.09.019 (PrCo2Al8 and Pr2Co6Al19: Crystal structure and electronic properties)

## Al-Co-Ru
- rank 1855 | 2 samples | 1 papers | 2 compositions
- compositions: Al65Co22Ru13_IQC (1); Al65Co21Ru14_IQC (1)
- measured range: 13-298 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al2CoRu Fm-3m (225) mp-862695 [hull=0.000, PRIMARY]; Al2CoRu P4/mmm (123) mp-1228908 [hull=0.023]
- papers: https://doi.org/10.1103/physrevb.61.8771 (Modeling the electrical conductivity of icosahedral quasicrystals)

## Al-Cr
- rank 1856 | 2 samples | 2 papers | 2 compositions
- compositions: Al0.062Cr (1); SmCr2Al20 (1)
- dopant candidates (<5% at.): Sm (1)
- measured range: 14-296 K (5th-95th pct of 2 curves; full span incl. outliers 14-692 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(Al10Cr)2 Fd-3m (227) mp-3910 [hull=0.000, icsd=4, PRIMARY]; Gd(Al10Cr)2 Fd-3m (227) mp-658303 [hull=0.001, icsd=3, PRIMARY]; La(Al10Cr)2 Fd-3m (227) mp-1200867 [hull=0.000, icsd=3, PRIMARY]; AlCr2 I4/mmm (139) mp-1699 [hull=0.000, icsd=3, PRIMARY]; Al8Cr5 R3m (160) mp-19954 [hull=0.078, icsd=2, PRIMARY]
- papers: https://doi.org/10.1063/1.1660393 (Antiferromagnetism and Electrical Transport Properties of Chromium‐Alu...) | https://doi.org/10.7566/jpscp.3.011040 (Thermoelectric Property of SmT<sub>2</sub>Al<sub>20</sub> (T = Ti, V, ...)

## Al-Cr-Mn-Si
- rank 1857 | 2 samples | 1 papers | 2 compositions
- compositions: Al32Cr12.5Mn31.5Si34 (1); Al32Cr12Mn32Si34 (1)
- measured range: 12-584 K (5th-95th pct of 7 curves)
- papers: https://doi.org/10.2320/jinstmet.74.605 (Electronic Structure and Thermoelectric Properties of Si2Ti-Type Al-(M...)

## Al-Cr-Ni-Si
- rank 1858 | 2 samples | 1 papers | 1 compositions
- compositions: Ni37.04Cr29.35Al17.14Si16.47 (2)
- measured range: 291-723 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1063/10.0017693 (Fabrication and characterization of NiCr-based films with high resisti...)

## Al-Cu-Fe-O
- rank 1859 | 2 samples | 2 papers | 1 compositions
- compositions: CuAl0.8Fe0.2O2 (2)
- measured range: 290-1141 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1016/j.ceramint.2011.12.079 (Effects of mechanical milling on preparation and properties of CuAl1−x...) | https://doi.org/10.1016/j.jallcom.2006.07.067 (Improvement in thermoelectric properties of CuAlO2 by adding Fe2O3)

## Al-Cu-La
- rank 1860 | 2 samples | 2 papers | 1 compositions
- compositions: LaCu4Al (2)
- measured range: 12-298 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaAl3Cu I4mm (107) mp-1070573 [hull=0.000, icsd=1, PRIMARY]; La2Al3Cu7 P2/m (10) mp-1223301 [hull=0.000, PRIMARY]; La(Al5Cu)2 Fmmm (69) mp-1223260 [hull=0.026, PRIMARY]; La2Al7Cu P4mm (99) mp-1223239 [hull=0.003, PRIMARY]; La5Al15Cu4Au I4mm (107) mp-1223196 [hull=0.005, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2011.08.009 (Thermopower of Ce1−xLaxCu4Al intermetallic compounds) | https://doi.org/10.1063/1.3624748 (Thermopower and thermal conductivity of Kondo lattice CeCu4Al)

## Al-Cu-Ni-O
- rank 1861 | 2 samples | 1 papers | 2 compositions
- compositions: (Ni0.47Cu0.53)(Al2O3)0.038 (1); (Ni0.47Cu0.53)(Al2O3)0.07 (1)
- measured range: 297-1076 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1016/s0925-8388(03)00295-0 (Thermoelectric properties of constantan/spherical SiO2 and Al2O3 parti...)

## Al-Cu-Ru-Si
- rank 1862 | 2 samples | 1 papers | 2 compositions
- compositions: Al64.5Si7.5Cu6Ru22_IAC_1_0 (1); Al62.5Si8.0Cu8.4Ru21.1_IAC_1_0 (1)
- measured range: 300-801 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1103/physrevmaterials.5.125401 (Effects of Cu doping on thermoelectric properties of Al–Si–Ru semicond...)

## Al-Cu-S-Sn
- rank 1863 | 2 samples | 1 papers | 2 compositions
- compositions: Cu3Al0.75Ga0.25SnS5 (1); Cu3AlSnS5 (1)
- dopant candidates (<5% at.): Ga (1)
- measured range: 372-668 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlCuSnS4 Imma (74) mp-1228961 [hull=0.001, PRIMARY]
- papers: https://doi.org/10.1021/acsaem.0c00730 (Effect of Gallium Substitution in Cu3Al1–xGaxSnS5 Nanobulk Materials o...)

## Al-Cu-Yb
- rank 1864 | 2 samples | 2 papers | 1 compositions
- compositions: YbCuAl (2)
- measured range: 10-196 K (5th-95th pct of 2 curves; full span incl. outliers 10-294 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbAlCu P-62m (189) mp-1078543 [hull=0.000, icsd=3, PRIMARY]; Yb(Al2Cu)4 I4/mmm (139) mp-1104848 [hull=0.000, icsd=1, PRIMARY]; YbAl2Cu R-3m (166) mp-977428 [hull=0.000, icsd=1, PRIMARY]; Yb6Al7Cu16 Fm-3m (225) mp-1193533 [hull=0.002, icsd=1, PRIMARY]; Yb(AlCu)6 Immm (71) mp-1215808 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1063/1.335167 (Two-band model and ground state of heavy fermion compounds) | https://doi.org/10.1023/a:1021801903961 (Thermopower of Yb Heavy Fermion Compounds at High Pressure)

## Al-Dy-Si
- rank 1865 | 2 samples | 1 papers | 1 compositions
- compositions: Dy8Al16Si30 (2)
- measured range: 322-675 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Dy2Al3Si2 C2/m (12) mp-3513 [hull=0.000, icsd=2, PRIMARY]; Dy(AlSi)2 P-3m1 (164) mp-7121 [hull=0.010, icsd=1, PRIMARY]; Dy12Al7Si I4/mcm (140) mp-1213130 [hull=0.014, PRIMARY]; DyAlSi Cmcm (63) mp-1206330 [hull=0.000, PRIMARY]; DyAlSi I4_1md (109) mp-1225273 [hull=0.021]
- papers: https://doi.org/10.1007/s10854-016-5113-1 (Thermoelectric properties of rare earth containing type-I Clathrate co...)

## Al-Er-O-Y
- rank 1866 | 2 samples | 1 papers | 2 compositions
- compositions: Y2ErAl5O12 (1); YEr2Al5O12 (1)
- measured range: 298-1074 K (5th-95th pct of 2 curves; full span incl. outliers 298-1273 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y9Er3Al20O48 C2 (5) mp-1216239 [hull=0.001, PRIMARY]; YErAl2O6 Pmc2_1 (26) mp-1215985 [hull=0.020, PRIMARY]
- papers: https://doi.org/10.1002/adem.201100122 (Y3−xErxAl5O12 Aluminate Ceramics: Preparation, Thermal Properties and ...)

## Al-Er-Yb
- rank 1867 | 2 samples | 1 papers | 2 compositions
- compositions: Yb0.5Er0.5Al3 (1); Yb0.75Er0.25Al3 (1)
- measured range: 80-300 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1007/s11664-012-2401-2 (Thermoelectric Properties of Yb1−x (Er,Lu) x Al3 Solid Solutions)

## Al-Eu
- rank 1868 | 2 samples | 1 papers | 1 compositions
- compositions: EuAl4 (2)
- measured range: 10-300 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): EuAl2 Fd-3m (227) mp-917786 [hull=0.000, icsd=5, PRIMARY]; EuAl4 I4/mmm (139) mp-990191 [hull=0.000, icsd=5, PRIMARY]; EuAl Pmmn (59) mp-1189619 [hull=0.011, icsd=1, PRIMARY]; Eu4Al Fd-3m (227) mp-1213330 [hull=0.465, PRIMARY]; EuAl Cmcm (63) mp-1079783 [hull=0.086, icsd=1]
- papers: https://doi.org/10.7566/jpsj.84.124711 (Transport and Magnetic Properties of EuAl4 and EuGa4)

## Al-Fe-Mn-Si
- rank 1869 | 2 samples | 2 papers | 2 compositions
- compositions: Al73Mn5.5Fe12.5Si9 (1); Al73.6Mn11.9Fe5.5Si9 (1)
- measured range: 11-297 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1007/s11664-010-1240-2 (Electronic Structure and Thermoelectric Properties of Al-Mn-Fe-Si Alloys) | https://doi.org/10.1103/physrevb.74.054206 (Extremely small thermal conductivity of the Al-based Mackay-type<mml:m...)

## Al-Fe-O
- rank 1870 | 2 samples | 2 papers | 2 compositions
- compositions: Mg0.3Al0.6Li0.35Fe1.75O4 (1); AlFeO3 (1)
- dopant candidates (<5% at.): Li (1), Mg (1)
- measured range: 200-398 K (5th-95th pct of 2 curves; full span incl. outliers 200-907 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al2FeO4 Fd-3m (227) mp-31801 [hull=0.145, icsd=3, PRIMARY]; AlFeO3 Pna2_1 (33) mp-25693 [hull=0.029, icsd=1, PRIMARY]; Al2(FeO3)3 C2/m (12) mp-1214939 [hull=0.269, PRIMARY]; Al15Fe9O32 C2/m (12) mp-766067 [hull=0.026, PRIMARY]; AlFe3O Pm-3m (221) mp-1206753 [hull=1.453, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2004.09.059 (Thermoelectric power studies of magnesium and aluminium substituted li...) | https://doi.org/10.3390/ma15238369 (Influence of Sb3+ Cations on the Structural, Magnetic and Electrical P...)

## Al-Fe-Sn-V
- rank 1871 | 2 samples | 2 papers | 2 compositions
- compositions: Fe2VAl0.8Sn0.2 (1); FeVAl0.8Sn0.2 (1)
- measured range: 10-298 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1063/1.4710350 (Enhancement in power factor values of Sn substituted Fe2 VAl Heusler a...) | https://doi.org/10.1007/s11664-008-0626-x (High Thermoelectric Power Factor Near Room Temperature in Full-Heusler...)

## Al-Ga-In-N
- rank 1872 | 2 samples | 2 papers | 2 compositions
- compositions: Al0.1In0.1Ga0.8N (1); Al0.26Ga0.44In0.30N (1)
- measured range: 297-1057 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1143/apex.4.051001 (Erbium-Doped AlInGaN Alloys as High-Temperature Thermoelectric Materials) | https://doi.org/10.1063/1.1560560 (Thermoelectric properties of Al1−xInxN and Al1−y−zGayInzN prepared by ...)

## Al-Ga-K-Si
- rank 1873 | 2 samples | 1 papers | 2 compositions
- compositions: K7.5Ga4.8Al3.0Si38.7 (1); K7.6Ga3.1Al4.6Si38.7 (1)
- measured range: 11-703 K (5th-95th pct of 17 curves)
- papers: https://doi.org/10.1016/j.intermet.2016.11.006 (Synthesis and thermoelectric properties of the quaternary type-I Si cl...)

## Al-Gd
- rank 1874 | 2 samples | 2 papers | 1 compositions
- compositions: GdAl2 (2)
- measured range: 11-250 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdAl2 Fd-3m (227) mp-19923 [hull=0.000, icsd=20, PRIMARY]; GdAl Cmcm (63) mp-1078585 [hull=0.000, icsd=1, PRIMARY]; Gd3Al Pm-3m (221) mp-1184417 [hull=0.005, PRIMARY]; GdAl3 P6_3/mmc (194) mp-865411 [hull=0.000, PRIMARY]; GdAl Pm-3m (221) mp-12753 [hull=0.015, icsd=1]
- papers: https://doi.org/10.1016/0304-8853(83)90564-4 (Thermoelectric power of RAl2) | https://doi.org/10.1088/0305-4608/16/4/013 (Thermal conductivity of REAl2compounds (RE=rare earth))

## Al-Gd-O
- rank 1875 | 2 samples | 2 papers | 2 compositions
- compositions: (Gd2O3)52.8(Al2O3)47.2 (1); GdAlO3 (1)
- measured range: 290-1272 K (5th-95th pct of 2 curves; full span incl. outliers 290-1373 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdAlO3 Pnma (62) mp-5223 [hull=0.009, icsd=10, PRIMARY]; Gd3Al5O12 Ia-3d (230) mp-14133 [hull=0.000, icsd=2, PRIMARY]; GdAlO3 Pm-3m (221) mp-1178268 [hull=0.086]
- papers: https://doi.org/10.1016/j.jnucmat.2007.03.266 (Characteristics of GdxMyOz (M=Ti, Zr or Al) as a burnable absorber) | https://doi.org/10.1016/s0022-3115(97)00235-3 (Investigation of the thermal conductivity of selected compounds of gad...)

## Al-Ho
- rank 1876 | 2 samples | 2 papers | 1 compositions
- compositions: HoAl2 (2)
- measured range: 11-250 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HoAl2 Fd-3m (227) mp-391 [hull=0.000, icsd=12, PRIMARY]; HoAl3 R-3m (166) mp-898 [hull=0.000, icsd=7, PRIMARY]; Ho3Al2 P4_2/mnm (136) mp-1106135 [hull=0.013, icsd=3, PRIMARY]; Ho2Al Pnma (62) mp-16502 [hull=0.000, icsd=1, PRIMARY]; Ho4Al Fd-3m (227) mp-1212293 [hull=0.685, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(83)90564-4 (Thermoelectric power of RAl2) | https://doi.org/10.1088/0305-4608/16/4/013 (Thermal conductivity of REAl2compounds (RE=rare earth))

## Al-La-Ni
- rank 1877 | 2 samples | 2 papers | 1 compositions
- compositions: LaNiAl4 (2)
- measured range: 10-292 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaAl5Ni2 Immm (71) mp-1080524 [hull=0.000, icsd=1, PRIMARY]; La2Al7Ni I4_1md (109) mp-1225981 [hull=0.009, PRIMARY]; LaAl3Ni2 Cmcm (63) mp-1211232 [hull=0.000, PRIMARY]; LaAlNi4 Cmmm (65) mp-1222929 [hull=0.000, PRIMARY]; LaAlNi4 P-6m2 (187) mp-1222982 [hull=0.045]
- papers: https://doi.org/10.1016/j.intermet.2013.01.016 (Thermal conductivity of CeNiAl4 Kondo lattice) | https://doi.org/10.1016/j.ssc.2007.08.041 (Electrical resistivity and thermoelectric power of the Kondo lattice C...)

## Al-Nd
- rank 1878 | 2 samples | 2 papers | 1 compositions
- compositions: NdAl2 (2)
- measured range: 11-252 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NdAl2 Fd-3m (227) mp-400 [hull=0.000, icsd=7, PRIMARY]; NdAl4 I4/mmm (139) mp-1834 [hull=0.066, icsd=3, PRIMARY]; Nd3Al11 Immm (71) mp-1104100 [hull=0.011, icsd=3, PRIMARY]; NdAl Pbcm (57) mp-864637 [hull=0.000, icsd=2, PRIMARY]; NdAl3 P6_3/mmc (194) mp-16513 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(83)90564-4 (Thermoelectric power of RAl2) | https://doi.org/10.1088/0305-4608/16/4/013 (Thermal conductivity of REAl2compounds (RE=rare earth))

## Al-Ni
- rank 1879 | 2 samples | 2 papers | 1 compositions
- compositions: Ni3Al (2)
- measured range: 272-1074 K (5th-95th pct of 2 curves; full span incl. outliers 272-1337 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlNi3 Pm-3m (221) mp-991114 [hull=0.000, icsd=15, PRIMARY]; AlNi Pm-3m (221) mp-1487 [hull=0.000, icsd=9, PRIMARY]; Al3Ni2 P-3m1 (164) mp-1057 [hull=0.000, icsd=6, PRIMARY]; Al3Ni5 Cmmm (65) mp-16514 [hull=0.000, icsd=3, PRIMARY]; Al3Ni Pnma (62) mp-622209 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.2497/jjspm.43.278 (Densification and Thermal Properties of TiC-Ni3Al Composites Materials.) | https://doi.org/10.1016/j.intermet.2014.12.006 (Thermal conductivity of Ni3V–Ni3Al pseudo-binary alloys)

## Al-Ni-Zn
- rank 1880 | 2 samples | 1 papers | 1 compositions
- compositions: Zn0.9Al0.05Ni0.05 (2)
- measured range: 12-295 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al3ZnNi12 P4/mmm (123) mp-1229039 [hull=0.007, PRIMARY]; AlZnNi2 Immm (71) mp-1093891 [hull=2.354, PRIMARY]
- papers: https://doi.org/10.1016/j.matchemphys.2010.12.041 (Al and Ni co-doped ZnO films with room temperature ferromagnetism, low...)

## Al-Np-Pd
- rank 1881 | 2 samples | 2 papers | 1 compositions
- compositions: NpPd5Al2 (2)
- measured range: 10-298 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NpAl3Pd2 P6/mmm (191) mp-1206258 [hull=0.104, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.77.212502 (Transport and magnetic properties of the superconductorNpPd5Al2) | https://doi.org/10.1103/physrevb.79.134525 (Kondo behavior in superconductingNpPd5Al2)

## Al-O-Sn
- rank 1882 | 2 samples | 1 papers | 2 compositions
- compositions: (SnO2)0.8527Al0.1473 (1); (SnO2)0.7728Al0.2272 (1)
- measured range: 50-290 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1080/14786435.2014.962641 (Effect of Al doping on structural, optical and electrical properties o...)

## Al-Pr
- rank 1883 | 2 samples | 2 papers | 1 compositions
- compositions: PrAl2 (2)
- measured range: 11-250 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrAl2 Fd-3m (227) mp-1189 [hull=0.000, icsd=15, PRIMARY]; PrAl Pbcm (57) mp-1106232 [hull=0.008, icsd=3, PRIMARY]; Pr3Al P6_3/mmc (194) mp-1079266 [hull=0.030, icsd=2, PRIMARY, AMBIGUOUS]; PrAl4 I4/mmm (139) mp-2336 [hull=0.054, icsd=2, PRIMARY]; PrAl3 P6_3/mmc (194) mp-12553 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(83)90564-4 (Thermoelectric power of RAl2) | https://doi.org/10.1088/0305-4608/16/4/013 (Thermal conductivity of REAl2compounds (RE=rare earth))

## Al-Re
- rank 1884 | 2 samples | 2 papers | 2 compositions
- compositions: Al11Re4 (1); Al12Re_IAC_1_0 (1)
- measured range: 359-863 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al12Re Im-3 (204) mp-1648 [hull=0.000, icsd=2, PRIMARY]; Al5Re24 I-43m (217) mp-1192984 [hull=0.056, icsd=1, PRIMARY]; Al6Re Cmcm (63) mp-16528 [hull=0.000, icsd=1, PRIMARY]; AlRe Pm-3m (221) mp-10908 [hull=0.236, icsd=1, PRIMARY]; AlRe2 I4/mmm (139) mp-10909 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.1486030 (Composition dependence of thermoelectric properties of AlPdRe icosahed...) | https://doi.org/10.1088/1468-6996/15/4/044802 (Metallic–covalent bonding conversion and thermoelectric properties of ...)

## Al-Rh
- rank 1885 | 2 samples | 2 papers | 2 compositions
- compositions: Al73.3Rh26.7_IAC (1); Al73Rh27 (1)
- measured range: 16-845 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlRh Pm-3m (221) mp-364 [hull=0.000, icsd=4, PRIMARY]; Al9Rh2 P2_1/c (14) mp-1645 [hull=0.000, icsd=2, PRIMARY]; Al5Rh2 P6_3/mmc (194) mp-1791 [hull=0.000, icsd=2, PRIMARY]; Al13Rh4 C2/m (12) mp-1203489 [hull=0.021, icsd=1, PRIMARY]; AlRh3 P6_3/mmc (194) mp-1183306 [hull=0.069, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2020.156904 (Band engineering in Al-TM (TM=Rh, Ir) quasicrystalline approximants vi...) | https://doi.org/10.1016/j.jnoncrysol.2003.12.005 (Electrical resistivity of the Al65Rh27Si8 2/1 cubic approximant)

## Al-Ru-Ta
- rank 1886 | 2 samples | 1 papers | 2 compositions
- compositions: Ru2TaAl (1); Ru1.95Ta1.05Al (1)
- measured range: 13-298 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TaAlRu2 Fm-3m (225) mp-862446 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.96.125106 (Semimetallic behavior in Heusler-type \n<mml:math xmlns:mml=\"http://w...)

## Al-Sb-Y-Yb
- rank 1887 | 2 samples | 1 papers | 2 compositions
- compositions: (YbAl3)0.8(Y5Sb3)0.2 (1); (YbAl3)0.9(Y5Sb3)0.1 (1)
- measured range: 299-674 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.1007/s11664-014-2997-5 (Effects of Second Phase Yb5Sb3 on the Thermoelectric Properties of YbAl3)

## Al-Sb-Yb
- rank 1888 | 2 samples | 2 papers | 2 compositions
- compositions: Yb5Al2Sb6 (1); Yb5Al2Sb6Ge0.5 (1)
- dopant candidates (<5% at.): Ge (1)
- measured range: 279-875 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Yb11AlSb9 Iba2 (45) mp-1196426 [hull=0.000, icsd=33, PRIMARY]; Yb14AlSb11 I4_1/acd (142) mp-1196138 [hull=0.000, icsd=32, PRIMARY]
- papers: https://doi.org/10.1039/c4dt03773a (Thermoelectric properties of the Zintl phases Yb5M2Sb6 (M = Al, Ga, In)) | https://doi.org/10.1021/acs.chemmater.6b05281 (Influence of Thermally Activated Solid-State Crystal-to-Crystal Struct...)

## Al-Sm
- rank 1889 | 2 samples | 2 papers | 1 compositions
- compositions: SmAl2 (2)
- measured range: 11-248 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SmAl2 Fd-3m (227) mp-2358 [hull=0.000, icsd=6, PRIMARY]; SmAl4 I4/mmm (139) mp-1891 [hull=0.084, icsd=2, PRIMARY]; SmAl Pbcm (57) mp-978951 [hull=0.000, icsd=2, PRIMARY]; SmAl5 P6_322 (182) mp-1190357 [hull=0.038, icsd=2, PRIMARY]; Sm2Al Pnma (62) mp-1102344 [hull=0.003, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(83)90564-4 (Thermoelectric power of RAl2) | https://doi.org/10.1088/0305-4608/16/4/013 (Thermal conductivity of REAl2compounds (RE=rare earth))

## Al-Tb
- rank 1890 | 2 samples | 2 papers | 1 compositions
- compositions: TbAl2 (2)
- measured range: 11-249 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TbAl2 Fd-3m (227) mp-756 [hull=0.000, icsd=9, PRIMARY]; TbAl3 R-3m (166) mp-369 [hull=0.002, icsd=3, PRIMARY]; TbAl Pbcm (57) mp-11225 [hull=0.000, icsd=2, PRIMARY]; Tb2Al Pnma (62) mp-1103391 [hull=0.000, icsd=1, PRIMARY]; Tb2Al17 P6_3/mmc (194) mp-1202952 [hull=0.067, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(83)90564-4 (Thermoelectric power of RAl2) | https://doi.org/10.1088/0305-4608/16/4/013 (Thermal conductivity of REAl2compounds (RE=rare earth))

## Al-Te-Zn
- rank 1891 | 2 samples | 1 papers | 2 compositions
- compositions: Zn0.9Al0.1Te (1); Zn0.85Al0.15Te (1)
- measured range: 85-651 K (5th-95th pct of 12 curves)
- [ref 1] TEDesignLab / ICSD: Al2ZnTe4 I-4 (82) mp-7908 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.ceramint.2015.09.032 (Low thermal conductivity and enhanced thermoelectric performance of na...)

## As-Bi-Se-Te-Tl
- rank 1892 | 2 samples | 1 papers | 2 compositions
- compositions: As17.65Bi11.76Se8.82Te44.12Tl17.65 (1); As11.11Bi22.22Se5.56Te50Tl11.11 (1)
- measured range: 103-331 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1063/1.1702619 (Thermoelectric Properties of Diphasal Systems Combining As2Te3 and Tl2...)

## As-Ce-Ni
- rank 1893 | 2 samples | 1 papers | 2 compositions
- compositions: CeNi2(As0.9P0.1)2 (1); CeNi2As2 (1)
- dopant candidates (<5% at.): P (1)
- measured range: 11-283 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(NiAs)2 P4/nmm (129) mp-610645 [hull=0.000, icsd=2, PRIMARY]; Ce2Ni12As7 P-6 (174) mp-1191623 [hull=0.000, icsd=1, PRIMARY]; CeNiAs P-6m2 (187) mp-1061766 [hull=0.000, icsd=1, PRIMARY]; Ce6Ni20As13 P-6 (174) mp-1214373 [hull=0.000, PRIMARY]; Ce(NiAs)2 I4/mmm (139) mp-21006 [hull=0.016, icsd=2]
- papers: https://doi.org/10.1038/s41598-019-48662-8 (Heavy fermion quantum criticality at dilute carrier limit in CeNi2−δ(A...)

## As-Ce-Os
- rank 1894 | 2 samples | 1 papers | 2 compositions
- compositions: CeOs4As12  (1); CeOs4As12 (1)
- measured range: 10-287 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(As3Os)4 Im-3 (204) mp-1189855 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1073/pnas.0808991105 (The filled skutterudite CeOs4As12: A hybridization gap semiconductor)

## As-Co-Fe-Sb
- rank 1895 | 2 samples | 1 papers | 2 compositions
- compositions: Yb0.13Co3.0Fe1.0Sb9As2.9 (1); Yb0.23Co2.8Fe1.0Sb9As2.9 (1)
- dopant candidates (<5% at.): Yb (2)
- measured range: 319-816 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1007/s10853-014-8562-z (High-temperature thermoelectric properties of p-type skutterudites Ba0...)

## As-F-O-Sr-Ti
- rank 1896 | 2 samples | 1 papers | 2 compositions
- compositions: (SrF)2Ti2As2O (1); (SrF)2TiAs2O (1)
- measured range: 11-444 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2Ti2As2OF2 I4/mmm (139) mp-1079747 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/cm9027258 (Structure and Physical Properties of the Layered Pnictide-Oxides: (SrF...)

## As-Fe-O-Tb
- rank 1897 | 2 samples | 1 papers | 1 compositions
- compositions: TbFeAsO0.85 (2)
- measured range: 10-299 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TbFeAsO P4/nmm (129) mp-1079887 [hull=0.180, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.3136764 (Crystal structure and electronic and thermal properties of TbFeAsO0.85)

## As-La-Ni-O
- rank 1898 | 2 samples | 1 papers | 1 compositions
- compositions: LaNiAsO (2)
- measured range: 15-300 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaNiAsO P4/nmm (129) mp-1079362 [hull=0.548, icsd=2, PRIMARY]; La2NiAs2O P4/mmm (123) mp-1213453 [hull=1.795, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/22/7/072201 (A comparative study on the thermoelectric effect of parent oxypnictide...)

## As-La-Os
- rank 1899 | 2 samples | 2 papers | 1 compositions
- compositions: LaOs4As12 (2)
- measured range: 11-300 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(As3Os)4 Im-3 (204) mp-1105556 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2007.04.094 (Crystal structure, 139La NMR and transport properties of the As-based ...) | https://doi.org/10.1073/pnas.0808991105 (The filled skutterudite CeOs4As12: A hybridization gap semiconductor)

## As-Mn
- rank 1900 | 2 samples | 2 papers | 1 compositions
- compositions: MnAs (2)
- measured range: 29-325 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnAs P6_3/mmc (194) mp-610 [hull=0.032, icsd=11, PRIMARY]; Mn2As P4/nmm (129) mp-610522 [hull=0.019, icsd=7, PRIMARY]; Mn3As Cmcm (63) mp-2668 [hull=0.000, icsd=4, PRIMARY]; Mn4As3 C2/m (12) mp-9305 [hull=0.055, icsd=1, PRIMARY]; Mn3As2 C2/m (12) mp-28916 [hull=0.060, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.1643774 (Thermal transport properties of magnetic refrigerants La(FexSi1−x)13 a...) | https://doi.org/10.1002/aelm.201700636 (Outstanding Comprehensive Performance of La(Fe, Si)<sub>13</sub>H<sub>...)
