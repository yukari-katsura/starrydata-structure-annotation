# Host systems -- chunk 046 of 73

Ranks 2251-2300 by sample count. These 50 host systems cover 100 samples (0.19% of the TE set); cumulative through this chunk: 97.26%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## In-La-Pt
- rank 2251 | 2 samples | 2 papers | 2 compositions
- compositions: LaPtIn (1); La3Pt4In13 (1)
- measured range: 11-307 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaInPt P-62m (189) mp-20451 [hull=0.000, icsd=1, PRIMARY]; LaInPt4 F-43m (216) mp-1077796 [hull=0.000, icsd=1, PRIMARY]
- papers: Magnetic and Transport Properties of New Kondo Compounds CeTIn (T=Ni, Pd and Pt) | Unusual Kondo behavior in the indium-rich heavy-fermion antiferromagnet<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">Ce</mml:mi></mml:mrow><mml:mrow><mml:mn>3</mml:mn></mml:mrow></mml:msub></mml:mrow><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">Pt</mml:mi></mml:mrow><mml:mrow><mml:mn>4</mml:mn></mml:mrow></mml:msub></mml:mrow><mml:mrow><mml:msub><mml:mrow><mml:mi mathvariant=\"normal\">In</mml:mi></mml:mrow><mml:mrow><mml:mn>13</mml:mn></mml:mrow></mml:msub></mml:mrow></mml:math>

## In-Lu
- rank 2252 | 2 samples | 2 papers | 1 compositions
- compositions: LuIn3 (2)
- measured range: 12-292 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LuIn3 Pm-3m (221) mp-977 [hull=0.000, icsd=3, PRIMARY]; Lu2In P6_3/mmc (194) mp-1250 [hull=0.000, icsd=2, PRIMARY]; Lu5In3 P6_3/mcm (193) mp-1188644 [hull=0.016, icsd=1, PRIMARY]; Lu3In5 Pnma (62) mp-1211016 [hull=0.004, PRIMARY]; Lu3In Pm-3m (221) mp-976949 [hull=0.004, PRIMARY]
- papers: Thermoelectric power of the REIn3 single crystals where RE = La, Ce, Pr, Nd, Sm, Gd, Ho, ErIn3, TmandLu | Resistivity and thermopower of monocrystalline TbIn3 and DyIn3

## In-Ni-Sb
- rank 2253 | 2 samples | 2 papers | 2 compositions
- compositions: Ni3InSb (1); (InSb)90(NiSb)10 (1)
- measured range: 71-1056 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): InNi3Sb P-6m2 (187) mp-1223697 [hull=0.060, PRIMARY]
- papers: Synthesis and high-temperature thermoelectric properties of Ni3GaSb and Ni3InSb | Microstructure and thermoelectric properties of InSb compound with nonsoluble NiSb in situ precipitates

## In-Ni-U
- rank 2254 | 2 samples | 1 papers | 2 compositions
- compositions: UNi2In (1); UNi4In (1)
- measured range: 13-297 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UInNi4 F-43m (216) mp-672702 [hull=0.014, icsd=3, PRIMARY]; U2InNi2 P4/mbm (127) mp-647194 [hull=0.118, icsd=2, PRIMARY]; UInNi2 Fm-3m (225) mp-646821 [hull=0.108, icsd=1, PRIMARY]
- papers: Physical and Structural Properties of Ternary Uranium Compounds in the U-Ni-Sn and U-Ni-In Systems

## In-O-Pd
- rank 2255 | 2 samples | 1 papers | 2 compositions
- compositions: Pd0.3In2O3 (1); Pd2In2O3 (1)
- measured range: 400-1293 K (5th-95th pct of 4 curves)
- papers: Thermoelectric power factor of In2O3:Pd nanocomposite films

## In-O-Sn-Zn
- rank 2256 | 2 samples | 1 papers | 2 compositions
- compositions: In1.2Zn0.4Sn0.4O3 (1); In1.4Zn0.3Sn0.3O3 (1)
- measured range: 10-1033 K (5th-95th pct of 4 curves)
- papers: Enhancement of the thermoelectric performances of In2O3 by the coupled substitution of M2+/Sn4+ for In3+

## In-P-Sr
- rank 2257 | 2 samples | 1 papers | 1 compositions
- compositions: SrIn2P2 (2)
- measured range: 309-895 K (5th-95th pct of 2 curves)
- [ref 1] TEDesignLab / ICSD: Sr(InP)2 P6_3/mmc (194) mp-1078973 [hull=0.000, icsd=1, PRIMARY]; Sr3(InP2)2 Pnnm (58) mp-28324 [hull=0.000, icsd=1, PRIMARY]; Sr3InP3 Pnma (62) mp-616026 [hull=0.000, icsd=1, PRIMARY]
- papers: Temperature and doping effects on the transport properties of SrIn2P2 Zintl compound

## In-Pb-Te
- rank 2258 | 2 samples | 1 papers | 2 compositions
- compositions: Pb1Te1In0.14 (1); Pb1Te1In0.18 (1)
- measured range: 324-759 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): In6Te10Pb C2 (5) mp-1224649 [hull=0.000, PRIMARY]; InTe5Pb4 R-3m (166) mp-1223713 [hull=0.025, PRIMARY]; InTe5Pb4 I4/mmm (139) mp-1223727 [hull=0.035]
- papers: Thermoelectric Properties of Two-Phase PbTe with Indium Inclusions

## In-Se-Sn
- rank 2259 | 2 samples | 2 papers | 2 compositions
- compositions: In1.0Sn0.2Se (1); Sn0.9In0.1Se (1)
- measured range: 299-823 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): In4SnSe4 Pa-3 (205) mp-628768 [hull=0.002, icsd=1, PRIMARY]; InSn3Se4 Pm (6) mp-1223673 [hull=0.073, PRIMARY]
- papers: Thermoelectric properties of In1.3−xSnxSe prepared by spark plasma sintering method | Indium substitution effect on thermoelectric and optical properties of Sn1−xInxSe compounds

## In-Sn
- rank 2260 | 2 samples | 1 papers | 1 compositions
- compositions: ZnIn18SiSn20 (2)
- dopant candidates (<5% at.): Zn (2), Si (2)
- measured range: 300-724 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): In3Sn C2/m (12) mp-1224025 [hull=0.032, PRIMARY]; InSn3 Pm-3m (221) mp-1184776 [hull=0.040, PRIMARY]; InSn4 Cmmm (65) mp-1223653 [hull=0.046, PRIMARY]; In3Sn Pm-3m (221) mp-1184894 [hull=0.045]; InSn3 P-6m2 (187) mp-1223722 [hull=0.050]
- papers: Effect of Cooling Conditions on the Microstructure and Thermoelectric Properties of Zn/Si-Codoped InSb

## In-Te-Tl
- rank 2261 | 2 samples | 2 papers | 2 compositions
- compositions: TlInTe2 (1); TlIn0.9Ga0.1Te2 (1)
- dopant candidates (<5% at.): Ga (1)
- measured range: 290-873 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TlInTe2 I4/mcm (140) mp-22791 [hull=0.000, icsd=7, PRIMARY]
- papers: Systematic investigation of the thermoelectric properties of TlMTe[sub 2] (M=Ga, In, or Tl) | X-ray diffraction characterization and electrical properties of TlIn1 − x Ga x Te2 crystals

## K-Li-O-V
- rank 2262 | 2 samples | 1 papers | 2 compositions
- compositions: (K0.40Li0.60)VO3 (1); (K0.60Li0.40)VO3 (1)
- measured range: 574-638 K (5th-95th pct of 2 curves)
- papers: Thermoelectric power of ferroelectric potassium vanadate, cesium vanadate, lithium vanadate and their solid solutions

## K-Nb-O-Ta
- rank 2263 | 2 samples | 1 papers | 2 compositions
- compositions: KTa0.63Nb0.37O3 (1); KTa0.67Nb0.33O3 (1)
- measured range: 298-567 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): K2TaNbO6 Fm-3m (225) mp-1207114 [hull=0.007, PRIMARY]; K4Ta3NbO12 R-3m (166) mp-1223769 [hull=0.004, PRIMARY]; K2TaNbO6 P4/mmm (123) mp-1207110 [hull=0.008]
- papers: Thermal properties of cubic KTa1−xNbxO3 crystals

## K-O-Ru
- rank 2264 | 2 samples | 1 papers | 1 compositions
- compositions: KRu4O8 (2)
- measured range: 26-778 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): K(RuO2)4 I4/m (87) mp-5628 [hull=0.000, icsd=2, PRIMARY]; K2RuO4 Pnma (62) mp-17789 [hull=0.000, icsd=1, PRIMARY]; K2RuO5 P2_12_12_1 (19) mp-1201514 [hull=0.000, icsd=1, PRIMARY]; KRuO4 I4_1/a (88) mp-14005 [hull=0.000, icsd=1, PRIMARY]; KRuO2 I4_1/amd (141) mp-1211539 [hull=0.367, PRIMARY]
- papers: Transport properties of quasi-one-dimensional<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\"><mml:mrow><mml:msub><mml:mrow><mml:mtext>KRu</mml:mtext></mml:mrow><mml:mn>4</mml:mn></mml:msub><mml:msub><mml:mtext>O</mml:mtext><mml:mn>8</mml:mn></mml:msub></mml:mrow></mml:math>

## K-Pb-Sb-Se
- rank 2265 | 2 samples | 1 papers | 2 compositions
- compositions: K1.45Pb3.1Sb7.45Se15 (1); K2.15Pb1.7Sb8.15Se15 (1)
- measured range: 181-300 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): K2Sb9PbSe15 P2_1/m (11) mp-1212430 [hull=0.012, PRIMARY]
- papers: Modular Construction of A1+xM4-2xM‘7+xSe15(A = K, Rb; M = Pb, Sn; M‘ = Bi, Sb):  A New Class of Solid State Quaternary Thermoelectric Compounds

## K-Sb-V
- rank 2266 | 2 samples | 1 papers | 1 compositions
- compositions: KV3Sb5 (2)
- measured range: 12-294 K (5th-95th pct of 2 curves)
- papers: New kagome prototype materials: discovery of \nKV3Sb5,RbV3Sb5\n, and \nCsV3Sb5

## La-Mn-Mo-O-Sr
- rank 2267 | 2 samples | 1 papers | 2 compositions
- compositions: SrLaMnMoO6 (1); Sr1.5La0.5MnMoO6 (1)
- measured range: 304-1042 K (5th-95th pct of 5 curves; full span incl. outliers 304-1096 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrLaMnMoO6 Pc (7) mp-690552 [hull=0.000, PRIMARY]
- papers: La doped effects on structure and thermoelectric properties of Sr2MnMoO6 double-perovskite oxides

## La-Mn-Ni-O
- rank 2268 | 2 samples | 2 papers | 2 compositions
- compositions: ((LaNiO3) 2 (La0.7Sr0.3MnO3 )3 )20 (1); LaNi0.25Mn0.75O3 (1)
- dopant candidates (<5% at.): Sr (1)
- measured range: 10-298 K (5th-95th pct of 2 curves; full span incl. outliers 10-1123 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2MnNiO6 Fm-3m (225) mp-1079517 [hull=0.000, icsd=1, PRIMARY]; La4Mn(NiO4)3 P-1 (2) mp-1223093 [hull=0.001, PRIMARY]; La4Mn3NiO12 P-1 (2) mp-1223131 [hull=0.000, PRIMARY]; La2MnNiO6 R-3 (148) mp-1223253 [hull=0.000]
- papers: Observation of Superconductivity in the LaNiO3/La0.7Sr0.3MnO3 Superlattice | Assessment of LaM0.25Mn0.75O3- (M = Fe, Co, Ni, Cu) as promising cathode materials for intermediate-temperature solid oxide fuel cells

## La-Mn-Pb
- rank 2269 | 2 samples | 1 papers | 1 compositions
- compositions: La0.7Pb0.3Mn0.3 (2)
- measured range: 10-399 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La5MnPb3 P6_3/mcm (193) mp-1106340 [hull=0.127, icsd=1, PRIMARY]
- papers: Thermal conductivity of colossal magnetoresistive manganites (La1−xNdx)0.7Pb0.3MnO3

## La-N-O-W
- rank 2270 | 2 samples | 1 papers | 2 compositions
- compositions: LaWO0.6N2.4 (1); LaWO0.7N2.3 (1)
- measured range: 114-462 K (5th-95th pct of 2 curves)
- papers: On the electrical properties of the perovskites LnWOxN3−x

## La-Nb-O
- rank 2271 | 2 samples | 2 papers | 2 compositions
- compositions: La0.33Li0.08NbO3 (1); LaNb3O9 (1)
- dopant candidates (<5% at.): Li (1)
- measured range: 41-1022 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaNbO4 I4_1/a (88) mp-5295 [hull=0.000, icsd=17, PRIMARY]; La3NbO7 Cmcm (63) mp-12287 [hull=0.006, icsd=1, PRIMARY]; LaNb7O19 P321 (150) mp-28200 [hull=0.017, icsd=1, PRIMARY]; LaNb2O7 P4/mmm (123) mp-1079978 [hull=0.199, icsd=1, PRIMARY]; LaNb7O12 P2_1/c (14) mp-29183 [hull=0.000, icsd=1, PRIMARY]
- papers: Metallization of La1/3NbO3 by lithium incorporation | Prospects for Engineering Thermoelectric Properties in La1/3NbO3Ceramics Revealed via Atomic-Level Characterization and Modeling

## La-Nd
- rank 2272 | 2 samples | 1 papers | 2 compositions
- compositions: Nd0.75La0.25 (1); Nd0.63La0.37 (1)
- measured range: 10-12 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La3Nd I4/mmm (139) mp-1185150 [hull=0.029, PRIMARY]; LaNd3 Pm-3m (221) mp-1185074 [hull=0.017, PRIMARY]; LaNd3 I4/mmm (139) mp-1185124 [hull=0.021]; LaNd3 P6_3/mmc (194) mp-977225 [hull=0.037]
- papers: Thermoelectric power of Nd1−xLaxand Ce1−xLaxalloys

## La-Ni-O-Rh
- rank 2273 | 2 samples | 2 papers | 1 compositions
- compositions: LaRh0.7Ni0.3O3 (2)
- measured range: 11-793 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2NiRhO6 P2_1/c (14) mp-1223214 [hull=0.000, PRIMARY]
- papers: Thermoelectric properties of LaRh1−xNixO3 | Thermoelectric Properties of B-Site Substituted LaRhO3

## La-Ni-O-Ti
- rank 2274 | 2 samples | 1 papers | 2 compositions
- compositions: LaNi0.7Ti0.3O3 (1); LaNi0.5Ti0.5O3 (1)
- measured range: 77-302 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2TiNiO6 Fm-3m (225) mp-1079373 [hull=0.103, icsd=1, PRIMARY]; La2Ti3NiO10 I-4m2 (119) mp-1223170 [hull=0.114, PRIMARY]; LaTiNiO4 P4/nmm (129) mp-1147531 [hull=0.308, PRIMARY]; La2TiNiO6 P2_1/c (14) mp-1211325 [hull=0.012]
- papers: Electrical Transport Properties of LaNi1-xTixO3(x∼0.5) Ceramics

## La-O-Os
- rank 2275 | 2 samples | 1 papers | 2 compositions
- compositions: La3OsO7 (1); La2.8Ca0.2OsO7 (1)
- dopant candidates (<5% at.): Ca (1)
- measured range: 153-298 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La3(OsO5)2 C2/m (12) mp-27330 [hull=0.000, icsd=1, PRIMARY]; La3OsO7 Cmcm (63) mp-31353 [hull=0.000, icsd=1, PRIMARY]; La5MnOs3O16 P-1 (2) mp-644707 [hull=0.005, icsd=1, PRIMARY]
- papers: Magnetic structure of the quasi-one-dimensionalLa3OsO7as determined by neutron powder diffraction

## La-O-Ru-Sr
- rank 2276 | 2 samples | 1 papers | 2 compositions
- compositions: La0.7Sr0.3Mn0.2Ru0.8O3 (1); La0.7Sr0.3Mn0.1Ru0.9O3 (1)
- dopant candidates (<5% at.): Mn (2)
- measured range: 30-494 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr4La2Mg(RuO6)2 I4/mmm (139) mp-1218460 [hull=0.048, PRIMARY]; Sr8La3(RuO7)3 P1 (1) mp-684802 [hull=0.003, PRIMARY]; SrLa(RuO3)2 Pmn2_1 (31) mp-1218253 [hull=0.021, PRIMARY]; Sr4La2Mg(RuO6)2 C2/m (12) mp-1173214 [hull=0.055]
- papers: Effects of Ru substitution for Mn on La0.7Sr0.3MnO3 perovskites

## La-O-Ta
- rank 2277 | 2 samples | 2 papers | 2 compositions
- compositions: LaTa3O9 (1); La3TaO7 (1)
- measured range: 294-1073 K (5th-95th pct of 2 curves; full span incl. outliers 294-1473 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaTaO4 Cmc2_1 (36) mp-3998 [hull=0.009, icsd=6, PRIMARY]; La3TaO7 Cmcm (63) mp-31415 [hull=0.000, icsd=2, PRIMARY]; LaTa3O9 Pnma (62) mp-5308 [hull=0.012, icsd=2, PRIMARY]; La2Ta2O9 C2/m (12) mp-1104362 [hull=0.122, icsd=1, PRIMARY]; LaTa7O19 P-6c2 (188) mp-14485 [hull=0.000, icsd=1, PRIMARY]
- papers: Spontaneously formed nanostructures in double perovskite rare-earth tantalates for thermal barrier coatings | Thermal properties of La3TaO7 and La2AlTaO7 oxides

## La-Pb-Te
- rank 2278 | 2 samples | 2 papers | 2 compositions
- compositions: La3Te3.6Pb0.4 (1); PbTeLa (1)
- measured range: 302-1081 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2Te4Pb I-42d (122) mp-675458 [hull=0.033, PRIMARY]
- papers: Study on the effect of Pb partial substitution for Te on the thermoelectric properties of La3Te4−xPbxmaterials | Synergistically optimizing thermoelectric transport properties of n-type PbTe via Se and Sn co-alloying

## La-Pd-Sb
- rank 2279 | 2 samples | 2 papers | 1 compositions
- compositions: LaPdSb (2)
- measured range: 299-963 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(SbPd)2 P4/nmm (129) mp-1079540 [hull=0.000, icsd=2, PRIMARY]; LaSb2Pd P4/nmm (129) mp-1078519 [hull=0.000, icsd=1, PRIMARY]; LaSbPd P6_3/mmc (194) mp-1018745 [hull=0.003, icsd=1, PRIMARY]; La2(SbPd)3 P4/mmm (123) mp-1206246 [hull=1.217, PRIMARY]; LaSb3Pd Pbcm (57) mp-1211524 [hull=0.000, PRIMARY]
- papers: LnPdSb (Ln=La,Gd): Promising intermetallics with large carrier mobility for high performance p-type thermoelectric materials | High-temperature Hall measurements of lanthanide based ternary intermetallics

## La-Si
- rank 2280 | 2 samples | 2 papers | 1 compositions
- compositions: LaSi (2)
- measured range: 298-959 K (5th-95th pct of 8 curves; full span incl. outliers 298-1166 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaSi2 I4_1/amd (141) mp-2062 [hull=0.000, icsd=8, PRIMARY]; LaSi Pnma (62) mp-1860 [hull=0.013, icsd=6, PRIMARY]; La5Si3 I4/mcm (140) mp-10961 [hull=0.000, icsd=5, PRIMARY]; La5Si4 P4_12_12 (92) mp-18345 [hull=0.000, icsd=4, PRIMARY]; LaSi5 C2/m (12) mp-1101787 [hull=0.165, icsd=2, PRIMARY]
- papers: Thermoelectric properties of BaSi2, SrSi2, and LaSi | Thermoelectric properties of alkaline-earth silicides

## Li-Mg-Si
- rank 2281 | 2 samples | 1 papers | 2 compositions
- compositions: Mg1.7Li0.3Si (1); Mg1.8Li0.2Si (1)
- measured range: 299-733 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li2MgSi P-43m (215) mp-1105932 [hull=0.000, icsd=3, PRIMARY]; Li(Mg2Si)2 P4/mmm (123) mp-1077902 [hull=0.045, icsd=1, PRIMARY]; Li(Mg2Si)4 Pm-3m (221) mp-1104791 [hull=0.045, icsd=1, PRIMARY]; Li12Mg3Si4 I-43d (220) mp-8331 [hull=0.000, icsd=1, PRIMARY]; LiMg2Si Fm-3m (225) mp-1067042 [hull=0.157, icsd=1, PRIMARY]
- papers: Structural and Thermoelectric Properties of Polycrystalline p-Type Mg2−x Li x Si

## Li-Mg-Si-Sn
- rank 2282 | 2 samples | 1 papers | 2 compositions
- compositions: Li0.4Mg2Si0.25Sn0.75 (1); Ag0.005Li0.32Mg2Si0.25Sn0.75 (1)
- dopant candidates (<5% at.): Ag (1)
- measured range: 291-826 K (5th-95th pct of 4 curves)
- papers: Thermoelectric Properties of p-Type Mg2.00Si0.25Sn0.75 with Li and Ag Double Doping

## Li-Ni-O
- rank 2283 | 2 samples | 1 papers | 1 compositions
- compositions: LiNiO2 (2)
- measured range: 150-297 K (5th-95th pct of 2 curves; full span incl. outliers 150-855 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiNiO2 R-3m (166) mp-25592 [hull=0.007, icsd=3, PRIMARY]; Li2NiO2 P-3m1 (164) mp-19308 [hull=0.000, icsd=2, PRIMARY]; Li(NiO2)2 P4_332 (212) mp-774941 [hull=0.000, PRIMARY]; Li(NiO2)3 C2/m (12) mp-1222821 [hull=0.046, PRIMARY]; Li11(NiO2)12 C2/m (12) mp-38676 [hull=0.010, PRIMARY]
- papers: Transport properties of the LiNi1−yCoyO2 system

## Li-O-Rh
- rank 2284 | 2 samples | 2 papers | 2 compositions
- compositions: LiRhO3 (1); LiRh2O4 (1)
- measured range: 89-299 K (5th-95th pct of 3 curves; full span incl. outliers 89-754 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiRhO2 R-3m (166) mp-14115 [hull=0.000, icsd=1, PRIMARY]; Li(RhO2)3 Cmmm (65) mp-1207037 [hull=2.112, PRIMARY]; Li2RhO3 C2/m (12) mp-754870 [hull=0.000, PRIMARY]; LiRhO2 Fd-3m (227) mp-14476 [hull=0.010, icsd=1]
- papers: Spin State Control of the Perovskite Rh/Co Oxides | Band Jahn-Teller Instability and Formation of Valence Bond Solid in a Mixed-Valent Spinel OxideLiRh2O4

## Li-O-Rh-Zn
- rank 2285 | 2 samples | 1 papers | 1 compositions
- compositions: Li0.5Zn0.5Rh2O4 (2)
- measured range: 372-872 K (5th-95th pct of 5 curves)
- papers: Synthesis and thermoelectric properties of the novel A-site deficient Zn0.5Rh2O4 compound

## Li-Sb-Zn
- rank 2286 | 2 samples | 1 papers | 1 compositions
- compositions: LiZnSb (2)
- measured range: 297-530 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LiZnSb P6_3mc (186) mp-9919 [hull=0.000, icsd=2, PRIMARY]; Li2ZnSb F-43m (216) mp-1222606 [hull=0.196, PRIMARY]
- papers: Thermoelectric properties of p-type LiZnSb: Assessment of ab initio calculations

## Lu-O-Rh
- rank 2287 | 2 samples | 2 papers | 1 compositions
- compositions: Lu2Rh2O7 (2)
- measured range: 14-295 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LuRhO3 Pnma (62) mp-1205366 [hull=0.000, icsd=1, PRIMARY]; LuRhO3 Pm-3m (221) mp-973681 [hull=0.721]
- papers: Coexistence of metallic and nonmetallic properties in the pyrochlore Lu2Rh2O7 | Impact of iso-structural template layer on stabilizing pyrochlore Bi2Rh2O7

## Mg-Mn-Sb
- rank 2288 | 2 samples | 1 papers | 2 compositions
- compositions: Mg2.6Mn0.4Sb2 (1); Mg2.7Mn0.3Sb2 (1)
- measured range: 10-597 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg14MnSb Amm2 (38) mp-1028074 [hull=0.078, PRIMARY]; Mg5MnSb4 P3m1 (156) mp-1222105 [hull=0.077, PRIMARY]; Mg6MnSb Amm2 (38) mp-1022926 [hull=0.156, PRIMARY]; Mg14MnSb P-6m2 (187) mp-1028069 [hull=0.082]
- papers: Thermoelectric properties of Mn-doped Mg–Sb single crystals

## Mg-N-O-Ti
- rank 2289 | 2 samples | 1 papers | 2 compositions
- compositions: MgTi2O5(TiN)1.386 (1); MgTi2O5(TiN)0.808 (1)
- measured range: 300-974 K (5th-95th pct of 10 curves)
- papers: Thermoelectric properties of MgTi2O5/TiN conductive composites prepared via reactive spark plasma sintering for high temperature functional applications

## Mg-Na-Sn
- rank 2290 | 2 samples | 1 papers | 2 compositions
- compositions: Na2Mg3Sn2 (1); Na4Mg4Sn3 (1)
- measured range: 301-598 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Na2MgSn P6_3/mmc (194) mp-865625 [hull=0.000, icsd=1, PRIMARY]; NaMg14Sn Amm2 (38) mp-1028273 [hull=0.030, PRIMARY]; NaMg6Sn Amm2 (38) mp-1021414 [hull=0.073, PRIMARY]; NaMg14Sn P-6m2 (187) mp-1028260 [hull=0.048]
- papers: Synthesis of Na2Mg3X2 (X = Sn, Pb) and Na4Mg4Sn3 and their crystal structures and thermoelectric properties

## Mg-O-Rh-Zn
- rank 2291 | 2 samples | 1 papers | 2 compositions
- compositions: ZnRh1.6Mg0.4O4 (1); ZnRh1.4Mg0.6O4 (1)
- measured range: 11-774 K (5th-95th pct of 4 curves)
- papers: Mg substitution effects of new thermoelectric Rh oxides

## Mg-O-V
- rank 2292 | 2 samples | 1 papers | 2 compositions
- compositions: Li0.1Mg0.9V2O4 (1); Li0.3Mg0.7V2O4 (1)
- dopant candidates (<5% at.): Li (2)
- measured range: 63-292 K (5th-95th pct of 2 curves)
- [ref 1] TEDesignLab / ICSD: Mg3V2O8 Cmce (64) mp-19034 [hull=0.000, icsd=2, PRIMARY]; MgV2O5 Cmcm (63) mp-19003 [hull=0.026, icsd=2, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: MgV2O4 Fd-3m (227) mp-18900 [hull=0.090, icsd=3, PRIMARY]; MgV2O6 C2/m (12) mp-1176494 [hull=0.011, icsd=1, PRIMARY]; Mg2V2O7 P-1 (2) mp-32500 [hull=0.000, icsd=1, PRIMARY]; Mg2VO4 Fd-3m (227) mp-32432 [hull=0.099, icsd=1, PRIMARY]; MgV2O6 Pbcn (60) mp-1196870 [hull=0.017, icsd=1]
- papers: Preparation and physical properties of the spinel Ti and V oxides

## Mg-Sb-Si
- rank 2293 | 2 samples | 1 papers | 2 compositions
- compositions: Mg2Si.75Sb0.25 (1); Mg2Si0.97Sb0.33 (1)
- measured range: 254-794 K (5th-95th pct of 2 curves)
- [ref 1] TEDesignLab / ICSD: MgSiSb2 I-42d (122) mp-1078680 [hull=0.115, icsd=2, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Mg14SiSb P-6m2 (187) mp-1026689 [hull=0.079, PRIMARY]; Mg6SiSb Amm2 (38) mp-1017349 [hull=0.151, PRIMARY]; Mg14SiSb Amm2 (38) mp-1026698 [hull=0.086]
- papers: Sb- and Bi-doped Mg2Si: location of the dopants, micro- and nanostructures, electronic structures and thermoelectric properties

## Mg-Sb-Si-Sn
- rank 2294 | 2 samples | 1 papers | 2 compositions
- compositions: Mg2Si0.4Sn0.22Sb0.38 (1); Mg2Si0.4Sn0.33Sb0.27 (1)
- measured range: 289-750 K (5th-95th pct of 8 curves)
- papers: High Performance Mg2(Si,Sn) Solid Solutions: a Point Defect Chemistry Approach to Enhancing Thermoelectric Properties

## Mg-Sb-Yb-Zn
- rank 2295 | 2 samples | 1 papers | 2 compositions
- compositions: Mg1.194Yb0.4Na0.006Zn1.2Sb2 (1); Mg1.394Yb0.4Na0.006Zn1.2Sb2 (1)
- dopant candidates (<5% at.): Na (2)
- measured range: 299-576 K (5th-95th pct of 8 curves)
- papers: Enhanced Thermoelectric Performance of p‐Type Mg<sub>3</sub>Sb<sub>2</sub> for Reliable and Low‐Cost all‐Mg<sub>3</sub>Sb<sub>2</sub>‐Based Thermoelectric Low‐Grade Heat Recovery

## Mn
- rank 2296 | 2 samples | 2 papers | 1 compositions
- compositions: Mn (2)
- measured range: 11-276 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn I-43m (217) mp-35 [hull=0.000, icsd=16, PRIMARY]; BaMn28 I-43m (217) mp-1194459 [hull=0.202, icsd=1, PRIMARY]; CaMn28 I-43m (217) mp-1194089 [hull=0.072, icsd=1, PRIMARY]; YbMn28 I-43m (217) mp-1194487 [hull=0.033, icsd=1, PRIMARY]; Mn Im-3m (229) mp-1055908 [hull=0.147, icsd=3]
- papers: Origin of low thermal conductivity in /spl alpha/-Mn: enhancing the ZT of YbAl/sub 3/ and CoSb/sub 3/ through Mn addition | Thermal Conductivity, Thermoelectric Power, and the Electrical Resistivity of Stoichiometric TiNi in the 3° to 300°K Temperature Range

## Mn-Nd-O-Sm-Sr
- rank 2297 | 2 samples | 1 papers | 1 compositions
- compositions: Nd0.25Sm0.25Sr0.50MnO3 (2)
- measured range: 12-285 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2NdSmMn4O12 Cm (8) mp-1218770 [hull=0.011, PRIMARY]
- papers: Phase separation and stability in Sm0.50Sr0.50MnO3: effects of cation dopants

## Mn-Ni
- rank 2298 | 2 samples | 1 papers | 2 compositions
- compositions: Ni76Mn24 (1); Ni74.5Mn23.5Pd2 (1)
- dopant candidates (<5% at.): Pd (1)
- measured range: 24-274 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnNi P4/mmm (123) mp-1797 [hull=0.037, icsd=2, PRIMARY]; MnNi3 Pm-3m (221) mp-11501 [hull=0.000, icsd=1, PRIMARY]; MnNi Pm-3m (221) mp-11500 [hull=0.039, icsd=1]; MnNi Cmmm (65) mp-1221603 [hull=0.137]; MnNi R-3m (166) mp-1221588 [hull=0.183]
- papers: Effect of exchange bias on the electrical resistivity of Pd doped NiMn thin films: Two-channel Kondo system

## Mn-O-Pb-Ti-Zr
- rank 2299 | 2 samples | 1 papers | 2 compositions
- compositions: (PbZr0.52Ti0.48O3)2000(La0.65Sr0.35MnO3)1000 (1); (PbZr0.52Ti0.48O3)2000(La0.65Sr0.35MnO3)800 (1)
- dopant candidates (<5% at.): La (2), Sr (2)
- measured range: 16-346 K (5th-95th pct of 2 curves)
- papers: Effect of PbZr0.52Ti0.48O3 thin layer on structure, electronic and magnetic properties of La0.65Sr0.35 MnO3 and La0.65Ca0.30MnO3 thin-films

## Mn-O-Pr-W
- rank 2300 | 2 samples | 1 papers | 1 compositions
- compositions: MnPr2W2O10 (2)
- measured range: 297-495 K (5th-95th pct of 2 curves)
- papers: Dielectric and magnetic permittivities of three new ceramic tungstates MPr2W2O10(M = Cd, Co, Mn)
