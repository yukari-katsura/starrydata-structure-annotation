# Host systems -- chunk 021 of 73

Ranks 1001-1050 by sample count. These 50 host systems cover 300 samples (0.58% of the TE set); cumulative through this chunk: 89.66%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Cd-Hg-Te
- rank 1001 | 6 samples | 3 papers | 3 compositions
- compositions: Hg0.79Cd0.21Te (3); Hg0.788Cd0.212Te (2); Hg0.825Cd0.175Te (1)
- measured range: 18-300 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CdHg3Te4 P-43m (215) mp-1120716 [hull=0.008, PRIMARY]; CdHg4Te5 Immm (71) mp-1226794 [hull=0.164, PRIMARY]; CdHgTe2 R3m (160) mp-1226741 [hull=0.010, PRIMARY]
- papers: https://doi.org/10.1007/bf02653090 (Nondestructive characterization of Hg1−xCdxTe layers with n-p structur...) | https://doi.org/10.1063/1.357643 (Transport coefficients and thermoelectric figure of merit ofn‐Hg1−xCdxTe) | https://doi.org/10.1016/0022-0248(90)90804-t (Arsenic ion implantation in Hg1-xCdxTe)

## Cd-O-Re
- rank 1002 | 6 samples | 5 papers | 1 compositions
- compositions: Cd2Re2O7 (6)
- measured range: 11-507 K (5th-95th pct of 6 curves; full span incl. outliers 11-607 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cd2Re2O7 Fd-3m (227) mp-16783 [hull=0.044, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.83.125103 (Structural and electronic properties of pyrochlore-type<mml:math xmlns...) | https://doi.org/10.1103/physrevlett.87.187001 (Superconductivity at 1 K in<mml:math xmlns:mml=\"http://www.w3.org/199...) | https://doi.org/10.1016/s0022-3697(02)00090-2 (Structural phase transition in the superconducting pyrochlore oxide Cd...)

## Cd-Sb-Sr
- rank 1003 | 6 samples | 1 papers | 6 compositions
- compositions: Sr0.9975Na0.0025Cd2Sb2 (1); Sr0.995Na0.005Cd2Sb2 (1); Sr0.98Na0.02Cd2Sb2 (1); SrCd2Sb2 (1); Sr0.999Na0.001Cd2Sb2 (1); Sr0.99Na0.01Cd2Sb2 (1)
- dopant candidates (<5% at.): Na (5)
- measured range: 298-701 K (5th-95th pct of 30 curves)
- [ref 1] TEDesignLab / ICSD: Sr11(CdSb2)6 C2/m (12) mp-3195 [hull=0.000, icsd=2, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Sr(CdSb)2 P-3m1 (164) mp-7432 [hull=0.000, icsd=1, PRIMARY]; Sr2CdSb2 Pm (6) mp-1218871 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.cej.2021.130530 (Manipulation of hole and band for thermoelectric enhancements in SrCd2...)

## Ce-Fe-P
- rank 1004 | 6 samples | 2 papers | 5 compositions
- compositions: CeFe4P12 (2); Ce0.999La0.001Fe4P12 (1); Ce0.99La0.01Fe4P12 (1); Ce0.95La0.05Fe4P12 (1); Ce0.9La0.1Fe4P12 (1)
- dopant candidates (<5% at.): La (4)
- measured range: 10-864 K (5th-95th pct of 13 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(FeP3)4 Im-3 (204) mp-16272 [hull=0.000, icsd=2, PRIMARY]; Ce(FeP)2 I4/mmm (139) mp-6957 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.physb.2006.01.066 (Thermoelectric properties in) | https://doi.org/10.1063/1.1427141 (Preparation and thermoelectric properties of CeFe4As12)

## Ce-In-Ni
- rank 1005 | 6 samples | 4 papers | 3 compositions
- compositions: CeNiIn (4); CeNi4In (1); Ce2Ni2In (1)
- measured range: 10-300 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeInNi P-62m (189) mp-21492 [hull=0.000, icsd=7, PRIMARY]; CeIn2Ni9 P4/mbm (127) mp-1193040 [hull=0.015, icsd=4, PRIMARY]; Ce11In9Ni4 Cmmm (65) mp-1192200 [hull=0.000, icsd=2, PRIMARY]; Ce2InNi2 P4/mbm (127) mp-640108 [hull=0.000, icsd=1, PRIMARY]; Ce(In2Ni)3 Pmmn (59) mp-1189631 [hull=0.014, icsd=1, PRIMARY]
- papers: https://doi.org/10.7567/jjaps.26s3.549 (Magnetic and Transport Properties of New Kondo Compounds CeTIn (T=Ni, ...) | https://doi.org/10.1016/j.jallcom.2009.10.028 (Thermoelectric power in (, Ni; , Ga) compounds) | https://doi.org/10.1103/physrevb.39.6840 (Anisotropic Kondo effect in a valence-fluctuating system: CeNiIn)

## Ce-Ir-Si
- rank 1006 | 6 samples | 1 papers | 1 compositions
- compositions: CeIrSi3 (6)
- measured range: 10-299 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(SiIr)2 I4/mmm (139) mp-4433 [hull=0.012, icsd=4, PRIMARY]; Ce2Si5Ir3 Ibam (72) mp-1105703 [hull=0.000, icsd=1, PRIMARY]; CeSi2Ir Cmcm (63) mp-1079402 [hull=0.000, icsd=1, PRIMARY]; CeSi2Ir3 Imma (74) mp-13475 [hull=0.000, icsd=1, PRIMARY]; CeSi3Ir I4mm (107) mp-1068906 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1143/jpsjs.80sa.sa068 (Thermoelectric Power in a Single-Crystalline CeIrSi3)

## Ce-O-Ti
- rank 1007 | 6 samples | 1 papers | 6 compositions
- compositions: Ce0.9Sr0.1TiO3 (1); CeTiO3 (1); CeTiO2.85 (1); Ce0.99Sr0.01TiO3 (1); Ce0.98Sr0.02TiO3 (1); Ce0.97Sr0.03TiO3 (1)
- dopant candidates (<5% at.): Sr (4)
- measured range: 11-331 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeTi2O6 C2/m (12) mp-1079004 [hull=0.005, icsd=1, PRIMARY]; Ce2Ti2O7 Fd-3m (227) mp-755065 [hull=0.010, PRIMARY]; Ce2TiO5 Pnma (62) mp-768309 [hull=0.000, PRIMARY]; CeTiO3 Pm-3m (221) mp-754524 [hull=0.087, PRIMARY]; CeTi2O6 C2/c (15) mp-1105722 [hull=0.049, icsd=1]
- papers: https://doi.org/10.1088/0953-8984/9/26/010 (Electronic states of perovskite-type and systems with a metal - insula...)

## Ce-Pb-Sn
- rank 1008 | 6 samples | 1 papers | 6 compositions
- compositions: Ce(Pb0.4Sn0.6)3 (1); Ce(Pb0.2Sn0.8)3 (1); Ce(Pb0.7Sn0.3)3 (1); Ce(Pb0.9Sn0.1)3 (1); Ce(Pb0.8Sn0.2)3 (1); Ce(Pb0.6Sn0.4)3 (1)
- solid-solution axis: Pb/(Pb+Sn) spans 0.20-0.90 (median 0.70) over 6 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-297 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.1016/0304-8853(88)90399-x (Thermoelectric power of Ce(Pb1−xSnx)3)

## Cl-Cu-Se
- rank 1009 | 6 samples | 1 papers | 6 compositions
- compositions: (CuCl)0.2(Cu2Se)0.8 (1); (CuCl)0.5(Cu2Se)0.5 (1); (CuCl)0.6(Cu2Se)0.4 (1); (CuCl)0.3(Cu2Se)0.7 (1); (CuCl)0.4(Cu2Se)0.6 (1); (CuCl)0.8(Cu2Se)0.2 (1)
- measured range: 1102-1453 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuSe2Cl P2_1/c (14) mp-31038 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1051/epjconf/20111501003 (Electrical properties of molten CuCl-Cu2Se mixtures)

## Cl-Na-Pb-Te
- rank 1010 | 6 samples | 2 papers | 6 compositions
- compositions: (NaCl)0.18PbTe (1); PbTe(NaCl)0.37 (1); PbTe(NaCl)0.64 (1); PbTe(NaCl)0.12 (1); PbTe(NaCl)0.24 (1); PbTe(NaCl)0.5 (1)
- measured range: 303-774 K (5th-95th pct of 26 curves)
- papers: https://doi.org/10.1155/2015/496739 (Reduction of Lattice Thermal Conductivity in PbTe Induced by Artificia...) | https://doi.org/10.1016/j.mtla.2020.100912 (Enhancement of thermoelectric performance of PbTe by embedding NaCl)

## Co-Cu-S-Sb
- rank 1011 | 6 samples | 4 papers | 5 compositions
- compositions: Cu10Co2Sb4S13 (2); Cu10.5Co1.5Sb4S13 (1); Cu10.0Co2.0Sb4S13 (1); Cu10.49Co1.51Sb4S13 (1); Cu10.3Co1.7Sb4S13 (1)
- measured range: 11-691 K (5th-95th pct of 26 curves)
- papers: https://doi.org/10.1016/j.actamat.2015.08.040 (Thermoelectric properties of Co substituted synthetic tetrahedrite) | https://doi.org/10.1143/apex.5.051201 (Thermoelectric Properties of Mineral Tetrahedrites Cu$_{10}$Tr$_{2}$Sb...) | https://doi.org/10.1021/cm404026k (Enhanced Thermoelectric Performance of Synthetic Tetrahedrites)

## Co-Dy-O-Sr
- rank 1012 | 6 samples | 1 papers | 2 compositions
- compositions: Sr2.4Dy0.6Co2O5.90 (3); Sr2.4Dy0.6Co2O6.67 (3)
- measured range: 315-808 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SrDyCoO4 Cmcm (63) mp-1218284 [hull=0.128, PRIMARY]
- papers: https://doi.org/10.1016/j.ceramint.2020.12.030 (The Sr2.4Dy0.6Co2O7-δ Ruddlesden‒Popper Phase: Structural, thermoelect...)

## Co-Fe-Ni-O
- rank 1013 | 6 samples | 1 papers | 6 compositions
- compositions: (Ni0.4Co0.6)0.9Fe2.1O4 (1); (Ni0.5Co0.5)1.0Fe2.0O4 (1); (Ni0.5Co0.5)1.1Fe1.9O4 (1); (Ni0.5Co0.5)0.9Fe2.1O4 (1); (Ni0.4Co0.6)1.0Fe2.0O4 (1); (Ni0.4Co0.6)1.1Fe1.9O4 (1)
- measured range: 471-974 K (5th-95th pct of 12 curves)
- papers: https://doi.org/10.1109/ict.2006.331228 (P-type thermoelectric properties of sintered (NiyCo1-y)xFe3-xO4 with s...)

## Co-Fe-Ni-Sb
- rank 1014 | 6 samples | 2 papers | 3 compositions
- compositions: Fe0.25Ni0.25Co0.5Sb3 (4); Fe0.33Ni0.33Co0.34Sb3 (1); Fe0.375Ni0.375Co0.25Sb3 (1)
- measured range: 179-726 K (5th-95th pct of 18 curves)
- papers: https://doi.org/10.1016/j.jallcom.2006.11.037 (Thermoelectric properties of skutterudites FexNiyCo1−x−ySb3 (x=y)) | https://doi.org/10.1007/s12598-009-0046-y (Solvothermal synthesis and thermoelectric properties of skutterudite c...)

## Co-Fe-Sb-Te
- rank 1015 | 6 samples | 1 papers | 1 compositions
- compositions: Ce0.09Fe0.67Co3.33Sb12(FeSb2.1Te)4 (6)
- dopant candidates (<5% at.): Ce (6)
- measured range: 310-465 K (5th-95th pct of 18 curves)
- papers: https://doi.org/10.1016/j.tsf.2013.09.068 (Properties of thermoelectric Ce0.09Fe0.67Co3.33Sb12/FeSb2Te multi-laye...)

## Co-Fe-Sn-Ti
- rank 1016 | 6 samples | 2 papers | 6 compositions
- compositions: Fe1.4Co0.6TiSn (1); FeCoTiSn (1); Fe1.8Co0.2TiSn (1); Fe1.6Co0.4TiSn (1); Fe1.2Co0.8TiSn (1); CoFeTiSn (1)
- measured range: 29-559 K (5th-95th pct of 32 curves)
- papers: https://doi.org/10.1007/s11595-021-2436-4 (Thermoelectric Properties of n-type Full-Heusler Fe2−2xCo2xTiSn Prepar...) | https://doi.org/10.1016/j.jmmm.2019.01.100 (Anomalous transport and magnetic behaviours of the quaternary Heusler ...)

## Co-Ge-Sb
- rank 1017 | 6 samples | 2 papers | 4 compositions
- compositions: In0.5Co4Sb11Ge1 (3); Yb0.46Co4Ge0.86Sb11.13 (1); Yb0.49Co4Ge1.00Sb10.92 (1); Yb0.65Co4Ge0.96Sb11.21 (1)
- dopant candidates (<5% at.): Yb (3), In (3)
- measured range: 11-696 K (5th-95th pct of 24 curves)
- papers: https://doi.org/10.1063/1.1927702 (Thermoelectric properties of Yb-filled Ge-compensated CoSb3 skutterudi...) | https://doi.org/10.1016/j.matlet.2011.10.035 (The thermoelectric properties of In0.5Co4Sb12−xGex alloys prepared by ...)

## Co-Hf-Sb-Sn
- rank 1018 | 6 samples | 5 papers | 4 compositions
- compositions: HfCoSb0.8Sn0.2 (3); Ti0.15Hf0.85CoSb0.8Sn0.2 (1); Zr0.10Hf0.90CoSb0.7Sn0.3 (1); Hf0.9Ti0.1CoSb0.8Sn0.2 (1)
- dopant candidates (<5% at.): Ti (2), Zr (1)
- measured range: 16-1125 K (5th-95th pct of 21 curves)
- papers: https://doi.org/10.1039/c5tc01196e (Fine tuning of thermoelectric performance in phase-separated half-Heus...) | https://doi.org/10.1039/c4cp02561j (Enhanced thermoelectric performance in the p-type half-Heusler (Ti/Zr/...) | https://doi.org/10.1063/1.2959103 ((Zr,Hf)Co(Sb,Sn) half-Heusler phases as high-temperature (>700°C) p-ty...)

## Co-Mn-Sb
- rank 1019 | 6 samples | 2 papers | 6 compositions
- compositions: Co3Mn1Sb12 (1); Co3Mn1Sb11.6Sn0.4 (1); Co2.5Mn1.5Sb12 (1); Co3Mn1Sb11.8Sn0.2 (1); Ca0.3Co3MnSb12 (1); Ca0.3Co2.5Mn1.5Sb12 (1)
- dopant candidates (<5% at.): Sn (2), Ca (2)
- measured range: 317-825 K (5th-95th pct of 24 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MnCoSb P4/nmm (129) mp-1018803 [hull=0.061, icsd=4, PRIMARY]; MnCo2Sb Fm-3m (225) mp-5396 [hull=0.004, icsd=2, PRIMARY]; Mn2CoSb F-43m (216) mp-13085 [hull=0.135, icsd=1, PRIMARY]; Mn7CoSb4 P-4m2 (115) mp-1221837 [hull=0.126, PRIMARY]; MnCoSb F-43m (216) mp-5318 [hull=0.009, icsd=3]
- papers: https://doi.org/10.1007/s13391-011-0306-5 (Thermoelectric properties of Co4−xMnxSb12−ySny skutterudites) | https://doi.org/10.1007/s11664-010-1400-4 (Thermoelectric Properties of Ca-Filled CoSb3-Based Skutterudites Synth...)

## Co-Nb-Ni-Sn-Zr
- rank 1020 | 6 samples | 1 papers | 3 compositions
- compositions: Zr0.25Nb0.75Ni0.25Co0.75Sn (2); Zr0.75Nb0.25Ni0.75Co0.25Sn (2); Zr0.5Nb0.5Ni0.5Co0.5Sn (2)
- measured range: 367-1063 K (5th-95th pct of 29 curves)
- papers: https://doi.org/10.2320/jinstmet.jaw201507 (Solid Solution Behavior and Thermoelectric Properties of Half-Heusler ...)

## Co-O-Sb-Zn
- rank 1021 | 6 samples | 3 papers | 6 compositions
- compositions: (ZnO)9.6(In0.2Co4Sb12)5.3 (1); (ZnO)14(In0.2Co4Sb12)5 (1); (CoSb3)68.82(ZnO)31.18 (1); (CoSb3)58.46(ZnO)41.54 (1); (ZnO)0.5CoSb3 (1); (ZnO)0.7CoSb3 (1)
- dopant candidates (<5% at.): In (2)
- measured range: 10-799 K (5th-95th pct of 28 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zn3Co4(SbO6)2 P-1 (2) mp-1216036 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2013.11.204 (Thermoelectric properties of In0.2Co4Sb12 skutterudites with embedded ...) | https://doi.org/10.1007/s11664-011-1866-8 (Influence of ZnO Inclusions on the Low-Temperature Thermoelectric Prop...) | https://doi.org/10.1016/j.jallcom.2012.11.167 (Influence of ZnO nano-inclusions on the transport properties of the Co...)

## Co-Ru-Sb
- rank 1022 | 6 samples | 1 papers | 6 compositions
- compositions: Co0.5Ru0.5Sb2 (1); Co0.4Ru0.6Sb2 (1); Co0.8Ru0.2Sb2 (1); Co0.7Ru0.3Sb2 (1); Co0.6Ru0.4Sb2 (1); Co0.3Ru0.7Sb2 (1)
- measured range: 78-622 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1016/s0925-8388(00)01350-5 (Structural and electrical properties of Co1−xRuxSb2)

## Co-Sn-Ti
- rank 1023 | 6 samples | 6 papers | 3 compositions
- compositions: Co2TiSn (4); CoTiSn (1); TiCo1.5Sn (1)
- measured range: 10-890 K (5th-95th pct of 16 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiCo2Sn Fm-3m (225) mp-21467 [hull=0.000, icsd=9, PRIMARY]; TiCoSn F-43m (216) mp-1216949 [hull=0.068, icsd=2, PRIMARY]; Ti5CoSn3 P6_3/mcm (193) mp-1208283 [hull=0.000, PRIMARY]; Ti2Co3Sn2 R3m (160) mp-1217124 [hull=0.000, PRIMARY]; TiCo2Sn P4/mmm (123) mp-1216996 [hull=0.143]
- papers: https://doi.org/10.1016/j.jallcom.2004.04.095 (High temperature thermoelectric properties of CoNb1−xMxSn half-Heusler...) | https://doi.org/10.1098/rsta.2011.0183 (Anomalous transport properties of the half-metallic ferromagnets Co2Ti...) | https://doi.org/10.1103/physrevb.81.064404 (Itinerant half-metallic ferromagnetsCo2TiZ(Z=Si, Ge, Sn):Ab initiocalc...)

## Cr-Ge-Te
- rank 1024 | 6 samples | 2 papers | 2 compositions
- compositions: Cr2Ge2Te6 (4); Cr1.94Ge2Te6 (2)
- measured range: 12-834 K (5th-95th pct of 21 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CrGeTe3 R-3 (148) mp-1078220 [hull=0.005, icsd=4, PRIMARY]
- papers: https://doi.org/10.1021/acs.chemmater.5b04895 (Cr2Ge2Te6: High Thermoelectric Performance from Layered Structure with...) | https://doi.org/10.48550/ARXIV.2305.13268 (Spin-phonon scattering-induced low thermal conductivity in a van der W...)

## Cu-Mn-N
- rank 1025 | 6 samples | 2 papers | 2 compositions
- compositions: Mn3CuN (4); CuNMn3 (2)
- measured range: 13-347 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn3CuN Pm-3m (221) mp-1070242 [hull=1.908, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.materresbull.2011.03.015 (Structure and properties of ternary manganese nitride Mn3CuNy thin fil...) | https://doi.org/10.1016/s0038-1098(01)00395-7 (Nearly zero temperature coefficient of resistivity in antiperovskite c...)

## Cu-Mn-S-Sb
- rank 1026 | 6 samples | 3 papers | 4 compositions
- compositions: Cu10Mn2Sb4S13 (3); Cu10.5Mn1.5Sb4S13 (1); Cu10.6Mn1.5Sb4S13 (1); Cu10.2Mn1.8Sb4S13 (1)
- measured range: 13-730 K (5th-95th pct of 24 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mn2Cu10Sb4S13 I-42m (121) mp-1222021 [hull=0.032, PRIMARY]
- papers: https://doi.org/10.1143/apex.5.051201 (Thermoelectric Properties of Mineral Tetrahedrites Cu$_{10}$Tr$_{2}$Sb...) | https://doi.org/10.1021/cm404026k (Enhanced Thermoelectric Performance of Synthetic Tetrahedrites) | https://doi.org/10.1039/c4cp04039b (Thermoelectric properties of a Mn substituted synthetic tetrahedrite)

## Cu-Ni-S-Sb
- rank 1027 | 6 samples | 4 papers | 2 compositions
- compositions: Cu10Ni2Sb4S13 (4); Cu10.5Ni1.5Sb4S13 (2)
- measured range: 27-708 K (5th-95th pct of 26 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuNiSbS3 P2_12_12_1 (19) mp-1191203 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1143/apex.5.051201 (Thermoelectric Properties of Mineral Tetrahedrites Cu$_{10}$Tr$_{2}$Sb...) | https://doi.org/10.1021/cm404026k (Enhanced Thermoelectric Performance of Synthetic Tetrahedrites) | https://doi.org/10.1021/cm502570b (Increasing the Thermoelectric Figure of Merit of Tetrahedrites by Co-D...)

## Cu-S-Sb-Zn
- rank 1028 | 6 samples | 5 papers | 2 compositions
- compositions: Cu10Zn2Sb4S13 (4); Cu10.5Zn1.5Sb4S13 (2)
- measured range: 14-670 K (5th-95th pct of 17 curves; full span incl. outliers 14-722 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zn2Cu10Sb4S13 I-42m (121) mp-1215797 [hull=0.042, PRIMARY]
- papers: https://doi.org/10.1002/aenm.201200650 (High Performance Thermoelectricity in Earth-Abundant Compounds Based o...) | https://doi.org/10.1143/apex.5.051201 (Thermoelectric Properties of Mineral Tetrahedrites Cu$_{10}$Tr$_{2}$Sb...) | https://doi.org/10.1021/cm404026k (Enhanced Thermoelectric Performance of Synthetic Tetrahedrites)

## Dy-Gd-Ge-Si
- rank 1029 | 6 samples | 2 papers | 6 compositions
- compositions: DyGd4Si2Ge2 (1); Dy3.5Gd1.5Si2Ge2 (1); Dy4.5Gd0.5Si2Ge2 (1); Dy1.5Gd3.5Si2Ge2 (1); Dy2.5Gd2.5Si2Ge2 (1); Dy3.0Gd2.0Si2Ge2 (1)
- solid-solution axis: Dy/(Dy+Gd) spans 0.20-0.90 (median 0.60) over 6 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 19-299 K (5th-95th pct of 7 curves)
- papers: https://doi.org/10.1016/s0925-8388(01)01243-9 (Magnetism in DyGd4Si2Ge2) | https://doi.org/10.1016/j.jmmm.2006.07.002 (Magnetic and electrical transport properties of DyxGd5−xSi2Ge2 (x=0.0,...)

## Eu-Nb-O
- rank 1030 | 6 samples | 1 papers | 6 compositions
- compositions: Eu0.70NbO3.09 (1); Eu0.76NbO3.03 (1); Eu0.82NbO3.03 (1); Eu0.90NbO3.10 (1); Eu0.68NbO3.05 (1); Eu0.88NbO3.03 (1)
- measured range: 106-373 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): EuNbO3 Imma (74) mp-1078341 [hull=0.000, icsd=2, PRIMARY]; EuNb8O14 Pbam (55) mp-21593 [hull=0.000, icsd=1, PRIMARY]; Eu3NbO6 P2_1/c (14) mp-1188621 [hull=0.000, icsd=1, PRIMARY]; EuNb2O6 P2_1/c (14) mp-1201130 [hull=0.000, icsd=1, PRIMARY]; Eu5Nb4O15 P-3m1 (164) mp-1185383 [hull=0.002, icsd=1, PRIMARY]
- papers: https://doi.org/10.1149/1.2127638 (Electrical Properties of Divalent Europium Niobium Bronzes Eu[sub x]Nb...)

## Eu-O-Pb-Ru
- rank 1031 | 6 samples | 1 papers | 6 compositions
- compositions: Pb0.6Eu1.4Ru2O7 (1); Pb1.4Eu0.6Ru2O7 (1); Pb1.2Eu0.8Ru2O7 (1); Pb1.1Eu0.9Ru2O7 (1); Pb0.8Eu1.2Ru2O7 (1); PbEuRu2O7 (1)
- measured range: 20-248 K (5th-95th pct of 7 curves)
- papers: https://doi.org/10.2497/jjspm.65.249 (Metal-insulator Crossover in Pb-Ru Based Oxides with Pyrochlore-type S...)

## F-Mn-Rb
- rank 1032 | 6 samples | 1 papers | 5 compositions
- compositions: RbMnF3 (2); (RbMnF3)90K10 (1); (RbMnF3)99.69Ni0.31 (1); (RbMnF3)99.82Co0.18 (1); (RbMnF3)99.81Fe0.19 (1)
- dopant candidates (<5% at.): K (1), Ni (1), Co (1), Fe (1)
- measured range: 10-41 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Rb2MnF6 Fm-3m (225) mp-614121 [hull=0.000, icsd=3, PRIMARY]; RbMnF4 P2_1/c (14) mp-616766 [hull=0.000, icsd=2, PRIMARY]; Rb2MnF5 P4/mmm (123) mp-612605 [hull=0.000, PRIMARY]; Rb2MnF4 I4/mmm (139) mp-1206523 [hull=0.000, PRIMARY]; Rb3MnF7 P4/mbm (127) mp-614758 [hull=0.006, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.15.273 (Thermal conductivity of antiferromagnetic RbMnF3)

## F-O-P-U
- rank 1033 | 6 samples | 1 papers | 3 compositions
- compositions: (UO2.02)(FPO2.02) (4); (UO2)(FPO2) (1); (UO2.2)(FPO2.2) (1)
- measured range: 283-2090 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1016/s0022-3115(97)00105-0 (The effects of oxidation on the thermal conductivity of (U, M)O2 pelle...)

## Fe-Gd-O-Sr
- rank 1034 | 6 samples | 3 papers | 6 compositions
- compositions: Gd0.33Sr0.67FeO3 (1); GdSrFeO4 (1); Gd0.9Sr1.1FeO4 (1); Gd0.8Sr1.2FeO4 (1); Gd0.7Sr1.3FeO4 (1); Gd0.5Sr0.5Fe0.8Cu0.2O3 (1)
- dopant candidates (<5% at.): Cu (1)
- measured range: 124-389 K (5th-95th pct of 6 curves; full span incl. outliers 124-1122 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2Gd(FeO3)3 C2/c (15) mp-1218942 [hull=0.011, PRIMARY]; SrGd2(FeO3)3 P-3m1 (164) mp-1218646 [hull=0.121, PRIMARY]
- papers: https://doi.org/10.1016/s0167-577x(02)00856-x (Non-adiabatic small polaron hopping conduction in Gd1/3Sr2/3FeO3) | https://doi.org/10.1016/j.ceramint.2016.11.182 (Effect of increasing Sr content on structural and physical properties ...) | https://doi.org/10.1007/s11581-019-03314-9 (Cobalt-free perovskite Ln0.5Sr0.5Fe0.8Cu0.2O3-δ (Ln = Pr, Nd, Sm, and ...)

## Fe-Ge
- rank 1035 | 6 samples | 2 papers | 5 compositions
- compositions: FeGe1.52 (2); Fe39.81Ge60.19 (1); Fe39.53Ge60.47 (1); Fe39.67Ge60.33 (1); FeGe (1)
- measured range: 13-805 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeGe2 I4/mcm (140) mp-1071018 [hull=0.020, icsd=9, PRIMARY]; FeGe P6/mmm (191) mp-22478 [hull=0.000, icsd=5, PRIMARY]; Fe3Ge P6_3/mmc (194) mp-1079030 [hull=0.006, icsd=4, PRIMARY, AMBIGUOUS]; Fe2Ge P6_3/mmc (194) mp-20432 [hull=0.077, icsd=4, PRIMARY]; Fe6Ge5 C2/m (12) mp-636946 [hull=0.030, icsd=2, PRIMARY]
- papers: https://doi.org/10.1021/acs.chemmater.5b03952 (Glass-like Lattice Thermal Conductivity and Thermoelectric Properties ...) | https://doi.org/10.1103/physrevb.90.024403 (Scattering mechanisms in textured FeGe thin films: Magnetoresistance a...)

## Fe-Ge-Si
- rank 1036 | 6 samples | 1 papers | 1 compositions
- compositions: (Si0.8Ge0.2P0.02)0.9(FeSi2)0.1 (6)
- dopant candidates (<5% at.): P (6)
- measured range: 290-1177 K (5th-95th pct of 18 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeSiGe Cmce (64) mp-640075 [hull=0.149, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/s11664-016-4487-4 (Thermoelectric Properties of n-Type Si0,8Ge0,2-FeSi2 Multiphase Nanost...)

## Fe-O-Sm-Sr
- rank 1037 | 6 samples | 5 papers | 6 compositions
- compositions: La0.05Sm0.45Sr0.32Ba0.18FeO3 (1); Sm0.6Sr0.4Co0.2Fe0.8O3 (1); Sm0.6Sr0.4FeO3 (1); Sm0.5Sr0.5Fe0.8Cu0.2O3 (1); Sm0.5Sr0.5FeO3 (1); Sm0.5Sr0.45K0.05FeO3 (1)
- dopant candidates (<5% at.): Ba (1), La (1), Co (1), Cu (1), K (1)
- measured range: 318-1173 K (5th-95th pct of 6 curves; full span incl. outliers 318-1223 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr3Sm(FeO4)2 Amm2 (38) mp-1218432 [hull=0.018, PRIMARY]
- papers: https://doi.org/10.1016/j.ssi.2011.07.019 (Characterization of Ln0.5M0.5FeO3–δ (Ln=La, Nd, Sm; M=Ba, Sr) perovski...) | https://doi.org/10.1016/j.jallcom.2006.04.005 (Structure, electrical conducting and thermal expansion properties of L...) | https://doi.org/10.1016/j.memsci.2011.12.027 (Design and experimental investigation of oxide ceramic dual-phase memb...)

## Fe-Si-Ti
- rank 1038 | 6 samples | 4 papers | 1 compositions
- compositions: Fe2TiSi (6)
- measured range: 10-380 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiFeSi2 Pbam (55) mp-21662 [hull=0.000, icsd=5, PRIMARY]; TiFeSi Ima2 (46) mp-8648 [hull=0.000, icsd=2, PRIMARY]; TiFe2Si Fm-3m (225) mp-866141 [hull=0.000, PRIMARY]; Ti2FeSi F-43m (216) mp-1094030 [hull=0.295, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.90.085127 (Experimental realization of a semiconducting full-Heusler compound:Fe2...) | https://doi.org/10.1063/1.5141949 (Thermoelectric properties of single-phase full-Heusler alloy Fe2TiSi f...) | https://doi.org/10.1134/s1063782617070363 (Preparation and study of the thermoelectric properties of Fe2TiSn1–x\n...)

## Ga-Ge
- rank 1039 | 6 samples | 1 papers | 1 compositions
- compositions: La2Ga6Ge40 (6)
- dopant candidates (<5% at.): La (6)
- measured range: 301-597 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ga3Ge Pm-3m (221) mp-973875 [hull=0.094, PRIMARY]; GaGe F-43m (216) mp-1224769 [hull=0.162, PRIMARY]; GaGe3 P6_3/mmc (194) mp-1184140 [hull=0.256, PRIMARY, AMBIGUOUS]; Ga3Ge P6_3/mmc (194) mp-1184355 [hull=0.107]; GaGe3 Pm-3m (221) mp-1183975 [hull=0.257]
- papers: https://doi.org/10.1016/j.commatsci.2016.05.013 (Hosting of La 3+  guest ions in type-I Ge clathrates: A first-principl...)

## Ga-Re-Se-Te
- rank 1040 | 6 samples | 1 papers | 6 compositions
- compositions: Re6Ga2Se2.4Te12.6 (1); Re6Ga2Se4.5Te10.5 (1); Re6Ga1.5Se7.5Te7.5 (1); Re6Ga1.5Se2.4Te12.6 (1); Re6Ga1.5Se4.5Te10.5 (1); Re6Ga2Se7.5Te7.5 (1)
- solid-solution axis: Se/(Se+Te) spans 0.16-0.50 (median 0.30) over 6 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 10-323 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1016/j.matchemphys.2009.08.061 (Thermoelectric properties of Re6GaxSeyTe15−y (0≤x≤2; 0≤y≤7.5))

## Gd-Ge
- rank 1041 | 6 samples | 3 papers | 3 compositions
- compositions: Gd5(Si0.1Ge0.9)4 (4); Gd5Ge3 (1); Gd5Ge4 (1)
- dopant candidates (<5% at.): Si (4)
- measured range: 11-897 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd5Ge4 Pnma (62) mp-1198083 [hull=0.000, icsd=8, PRIMARY]; GdGe Cmcm (63) mp-19918 [hull=0.000, icsd=6, PRIMARY]; GdGe2 I4_1/amd (141) mp-1072982 [hull=0.075, icsd=1, PRIMARY]; GdGe2 Imma (74) mp-1212652 [hull=0.638]
- papers: https://doi.org/10.2320/jinstmet.j2014005 (Thermoelectric Properties of RE5X3(RE=Gd, La, X=Si, Ge)) | https://doi.org/10.1063/1.1459612 (Thermopower behavior in the Gd5(Si0.1Ge0.9)4 magnetocaloric compound f...) | https://doi.org/10.1016/j.jmmm.2004.11.331 (Thermopower and electrical resistivity behavior near the martensitic t...)

## Gd-N-U
- rank 1042 | 6 samples | 1 papers | 3 compositions
- compositions: (GdN)14.99(UN)85.01 (2); (GdN)19.97(UN)80.03 (2); (GdN)47.85(UN)52.15 (2)
- measured range: 298-1274 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdUN2 R-3m (166) mp-1224527 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.jnucmat.2021.152785 (Thermal conductivity of gadolinium added uranium mononitride fuel pell...)

## Gd-O-Ti
- rank 1043 | 6 samples | 3 papers | 6 compositions
- compositions: (Gd2O3)50(TiO2)50 (1); (Gd2O3)45.5(TiO2)54.5 (1); (Gd2O3)15.8(TiO2)84.2 (1); GdTiO3 (1); Gd0.960Sr0.040TiO3 (1); Gd0.870Sr0.130TiO3 (1)
- dopant candidates (<5% at.): Sr (2)
- measured range: 105-1271 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd2Ti2O7 Fd-3m (227) mp-5302 [hull=0.008, icsd=7, PRIMARY]; Gd2TiO5 P2_1/c (14) mp-770065 [hull=0.050, PRIMARY, AMBIGUOUS]; Gd7Ti8O26 P1 (1) mp-685713 [hull=0.059, PRIMARY]; Gd2Ti2O7 C2/m (12) mp-686465 [hull=0.037]; Gd2TiO5 Pnma (62) mp-770189 [hull=0.058]
- papers: https://doi.org/10.1016/j.jnucmat.2007.03.266 (Characteristics of GdxMyOz (M=Ti, Zr or Al) as a burnable absorber) | https://doi.org/10.1063/1.4899277 (Structural, magnetic, and electronic properties of GdTiO<sub>3</sub> M...) | https://doi.org/10.1016/j.tsf.2015.03.065 (Metal–insulator transitions in epitaxial Gd1−Sr TiO3 thin films grown ...)

## Ge-Pr-Pt-Sb
- rank 1044 | 6 samples | 1 papers | 6 compositions
- compositions: PrPt4Ge10Sb2 (1); PrPt4Ge8Sb4 (1); PrPt4Ge11Sb (1); PrPt4Ge9Sb3 (1); PrPt4Ge8.5Sb3.5 (1); PrPt4Ge7Sb5 (1)
- measured range: 12-282 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1103/physrevb.93.104507 (Investigation of superconducting and normal-state properties of the fi...)

## H-I
- rank 1045 | 6 samples | 1 papers | 2 compositions
- compositions: IIDT (3); IIDDT (3)
- measured range: 303-353 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): HI C2/c (15) mp-697025 [hull=0.000, PRIMARY]; HI3 P-1 (2) mp-1184859 [hull=0.084, PRIMARY]
- papers: https://doi.org/10.1021/acsnano.5b00589 (Seebeck Effects in N-Type and P-Type Polymers Driven Simultaneously by...)

## H-Ti
- rank 1046 | 6 samples | 2 papers | 6 compositions
- compositions: TiH1.53 (1); TiH1.66 (1); TiH1.75 (1); TiH1.7 (1); TiH2 (1); TiH0.82 (1)
- measured range: 293-768 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiH2 Fm-3m (225) mp-24161 [hull=0.002, icsd=11, PRIMARY]; TiH P4_2/mmc (131) mp-690760 [hull=0.001, icsd=2, PRIMARY]; MgTi7H16 Fm-3m (225) mp-1191885 [hull=0.014, icsd=1, PRIMARY]; Ti2H Pn-3m (224) mp-1077045 [hull=0.046, icsd=1, PRIMARY]; Ti4H3 P-42m (111) mp-1078123 [hull=0.042, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2005.10.032 (Electrical and thermal properties of titanium hydrides) | https://doi.org/10.1007/bf00162965 (Thermal conductivity and heat capacity of titanium hydrides)

## Hf-Ni-Sb-Ti
- rank 1047 | 6 samples | 1 papers | 3 compositions
- compositions: Ti0.4Hf0.6Ni1.005Sb0.975Sn0.025 (2); Ti0.4Hf0.6Ni1.03Sb0.975Sn0.025 (2); Ti0.4Hf0.6Ni1.01Sb0.975Sn0.025 (2)
- dopant candidates (<5% at.): Sn (6)
- measured range: 302-776 K (5th-95th pct of 30 curves)
- papers: https://doi.org/10.1039/c4ta00896k (Nanometer-scale interface engineering boosts the thermoelectric perfor...)

## Hf-Ni-Sb-Zr
- rank 1048 | 6 samples | 2 papers | 5 compositions
- compositions: Hf0.75Zr0.25NiSb0.99Sb0.01 (2); Zr2HfNi2.9Co0.1Sb4 (1); ZrHf2Ni2.9Co0.1Sb4 (1); ZrHf2Ni2.7Cu0.3Sb4 (1); Zr2HfNi2.7Cu0.3Sb4 (1)
- dopant candidates (<5% at.): Co (2), Cu (2)
- solid-solution axis: Hf/(Hf+Zr) spans 0.33-0.75 (median 0.67) over 5 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 326-867 K (5th-95th pct of 22 curves)
- papers: https://doi.org/10.1063/1.4928168 (Thermoelectric properties and electronic transport analysis of Zr3Ni3S...) | https://doi.org/10.1021/acs.chemmater.6b04898 (Thermoelectric Properties of n-type ZrNiPb-Based Half-Heuslers)

## In-O-Sb-Sn
- rank 1049 | 6 samples | 1 papers | 6 compositions
- compositions: In5SnSbO12 (1); In4.95Ga0.05SnSbO12 (1); In4.875Ga0.125SnSbO12 (1); In4.625Ga0.375SnSbO12 (1); In4.75Ga0.25SnSbO12 (1); In4.5Ga0.5SnSbO12 (1)
- dopant candidates (<5% at.): Ga (5)
- measured range: 291-977 K (5th-95th pct of 30 curves)
- papers: https://doi.org/10.1007/s10853-018-2048-3 (Improved densification and thermoelectric performance of In5SnSbO12 vi...)

## La
- rank 1050 | 6 samples | 2 papers | 6 compositions
- compositions: Ce0.005La (1); Ce0.003La (1); Ce0.0003La (1); Ce0.02La (1); Ce0.05La (1); La (1)
- dopant candidates (<5% at.): Ce (5)
- measured range: 11-295 K (5th-95th pct of 5 curves; full span incl. outliers 11-342 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La Fm-3m (225) mp-156 [hull=0.025, icsd=6, PRIMARY]; La P6_3/mmc (194) mp-26 [hull=0.021, icsd=4]; La Im-3m (229) mp-10023 [hull=0.143, icsd=2]
- papers: https://doi.org/10.1063/1.1660291 (Thermopower of Dilute Alloys of Cerium in Lanthanum) | https://doi.org/10.1063/1.325726 (Thermoelectric power of Nd1−xLaxand Ce1−xLaxalloys)
