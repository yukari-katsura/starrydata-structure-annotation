# Host systems -- chunk 049 of 73

Ranks 2401-2450 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 97.70%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Ag-Mg-O-Si
- rank 2401 | 1 samples | 1 papers | 1 compositions
- compositions: Mg2SiAg7.5O2.5 (1)
- measured range: 309-861 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/j.intermet.2012.08.026 (Fabrication and thermoelectric properties of Mg2Si-based composites us...)

## Ag-Mn-Te
- rank 2402 | 1 samples | 1 papers | 1 compositions
- compositions: Mn0.90Te0.95(Ag2S)0.05 (1)
- dopant candidates (<5% at.): S (1)
- measured range: 319-871 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1016/j.jmat.2020.11.007 (Enhanced thermoelectric performance in MnTe due to doping and in-situ ...)

## Ag-Na-Sb-Se-Te
- rank 2403 | 1 samples | 1 papers | 1 compositions
- compositions: Ag0.366Sb0.558Te1.005(Na2Se)1.005Ni0.02 (1)
- dopant candidates (<5% at.): Ni (1)
- measured range: 77-629 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1063/1.4916217 (Off-stoichiometric silver antimony telluride: An experimental study of...)

## Ag-O-Pb-V
- rank 2404 | 1 samples | 1 papers | 1 compositions
- compositions: (Ag2O)15(PbO)35(V2O5)50 (1)
- measured range: 300-498 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.physb.2006.02.002 (Anomalous temperature variation of thermoelectric power in CdO and Ag2...)

## Ag-O-Ru
- rank 2405 | 1 samples | 1 papers | 1 compositions
- compositions: AgRuO3 (1)
- measured range: 13-324 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ag3RuO4 C2/c (15) mp-1195464 [hull=0.078, icsd=1, PRIMARY]; AgRuO3 Fd-3m (227) mp-776168 [hull=0.056, PRIMARY]; AgRuO4 I4_1/a (88) mp-761035 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1002/chem.201606057 (AgRuO<sub>3</sub>, a Strongly Exchange-Coupled Honeycomb Compound Lack...)

## Ag-O-Ti
- rank 2406 | 1 samples | 1 papers | 1 compositions
- compositions: Ag0.20TiO2 (1)
- measured range: 64-1042 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiAg2O3 C2/c (15) mp-29160 [hull=0.036, icsd=1, PRIMARY]; Ti4Ag2O9 C2/m (12) mp-1208381 [hull=0.033, PRIMARY]
- papers: https://doi.org/10.1039/c2jm31469j (Bottom-up assembly to Ag nanoparticles embedded Nb-doped TiO2 nanobulk...)

## Ag-Pb-Sb-Sn-Te
- rank 2407 | 1 samples | 1 papers | 1 compositions
- compositions: (AgSbTe2)0.2(Pb0.5Sn0.5Te)0.8 (1)
- measured range: 323-673 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/j.jallcom.2005.08.033 (Thermoelectric properties of p-type (AgSbTe2)x(Pb0.5Sn0.5Te)1−x (x=0.0...)

## Ag-S-Sn
- rank 2408 | 1 samples | 1 papers | 1 compositions
- compositions: Ag8SnS6 (1)
- measured range: 319-651 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ag4Sn3S8 P4_132 (213) mp-1195808 [hull=0.007, icsd=10, PRIMARY]; Ag8SnS6 Pna2_1 (33) mp-15645 [hull=0.000, icsd=1, PRIMARY]; AgSnS2 P4/mmm (123) mp-1229005 [hull=0.081, PRIMARY]
- papers: https://doi.org/10.1039/d0ra10454j (N-type thermoelectric Ag8SnSe6 with extremely low lattice thermal cond...)

## Ag-Se-Sn-Zn
- rank 2409 | 1 samples | 1 papers | 1 compositions
- compositions: Ag2ZnSnSe4 (1)
- measured range: 16-301 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZnAg2SnSe4 I-42m (121) mp-1093995 [hull=0.010, PRIMARY]
- papers: https://doi.org/10.1021/acsami.5b01617 (Synthesis and Characterization of Nanostructured Stannite Cu2ZnSnSe4an...)

## Ag-Si-Te
- rank 2410 | 1 samples | 1 papers | 1 compositions
- compositions: Ag8SiTe6 (1)
- measured range: 301-799 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1143/jjap.48.011603 (Ag8SiTe6: A New Thermoelectric Material with Low Thermal Conductivity)

## Al-Au-Ce
- rank 2411 | 1 samples | 1 papers | 1 compositions
- compositions: CeAuAl (1)
- measured range: 11-201 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeAlAu Pnma (62) mp-1102423 [hull=0.000, icsd=2, PRIMARY]; CeAl3Au I4mm (107) mp-1070063 [hull=0.000, icsd=2, PRIMARY]; Ce(AlAu)2 P4/nmm (129) mp-1078886 [hull=0.000, icsd=1, PRIMARY]; CeAl7Au3 R-3c (167) mp-11031 [hull=0.000, icsd=1, PRIMARY]; CeAlAu P6_3/mmc (194) mp-1077768 [hull=0.001, icsd=1]
- papers: https://doi.org/10.1088/0953-8984/9/22/024 (Magnetism of the Kondo compound CeAuAl)

## Al-Au-Ce-Ge
- rank 2412 | 1 samples | 1 papers | 1 compositions
- compositions: CeAuAl4Ge2 (1)
- measured range: 11-19 K (5th-95th pct of 2 curves; full span incl. outliers 11-305 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeAl4Ge2Au R-3m (166) mp-12017 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevmaterials.1.044404 (Electronic structure and magnetism in the layered triangular lattice c...)

## Al-B-C-Ca
- rank 2413 | 1 samples | 1 papers | 1 compositions
- compositions: Ca0.078Al0.068C0.024B0.027 (1)
- measured range: 295-974 K (5th-95th pct of 4 curves; full span incl. outliers 295-1074 K)
- papers: https://doi.org/10.1016/j.mtcomm.2019.100820 (Positive ionic conduction of mayenite cement Ca12Al14O33/nano-carbon b...)

## Al-B-Mg
- rank 2414 | 1 samples | 1 papers | 1 compositions
- compositions: AlMgB14 (1)
- measured range: 372-1033 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg(AlB14)2 Cm (8) mp-1222257 [hull=0.031, PRIMARY]; Mg14AlB P-6m2 (187) mp-1028227 [hull=0.195, PRIMARY]; Mg4AlB10 P6/mmm (191) mp-1222150 [hull=0.000, PRIMARY]; Mg6AlB Amm2 (38) mp-1023279 [hull=0.398, PRIMARY]; MgAlB4 P6/mmm (191) mp-1207086 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2003.02.005 (Thermoelectric properties of some metal borides)

## Al-Ba
- rank 2415 | 1 samples | 1 papers | 1 compositions
- compositions: BaAl4 (1)
- measured range: 21-292 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BaAl4 I4/mmm (139) mp-1903 [hull=0.000, icsd=3, PRIMARY]; Ba4Al5 P6_3/mmc (194) mp-2631 [hull=0.000, icsd=2, PRIMARY]; Ba3Al5 P6_3/mmc (194) mp-261 [hull=0.004, icsd=2, PRIMARY]; BaAl2 Fd-3m (227) mp-551 [hull=0.038, icsd=2, PRIMARY]; Ba7Al13 P-3m1 (164) mp-1952 [hull=0.021, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2015.08.193 (Characteristic Fermi surfaces and charge density wave in SrAl4 and rel...)

## Al-Ba-Cu-P
- rank 2416 | 1 samples | 1 papers | 1 compositions
- compositions: BaCuAlP2 (1)
- measured range: 12-823 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1039/d4ta01063a (BaCu<i>T</i>P<sub>2</sub> (<i>T</i> = Al, Ga, In): a semiconducting bl...)

## Al-Ba-Fe-O
- rank 2417 | 1 samples | 1 papers | 1 compositions
- compositions: BaFe0.7Al0.3O3 (1)
- measured range: 298-773 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.23939/chcht10.04.387 (Synthesis, Structural and Physicochemical Characterization of BaFe1-xA...)

## Al-Ba-Gd-O
- rank 2418 | 1 samples | 1 papers | 1 compositions
- compositions: Ba6Gd2Al4O15 (1)
- measured range: 316-1069 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba5Gd2ZrAl2O13 P6_3/mmc (194) mp-1214525 [hull=0.018, PRIMARY]; Ba6Gd2Al4O15 P2/c (13) mp-1214682 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1111/jace.15504 (Thermophysical properties of rare earth barium aluminates)

## Al-Ba-Ir-O
- rank 2419 | 1 samples | 1 papers | 1 compositions
- compositions: Ba5AlIr2O11 (1)
- measured range: 79-739 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba5AlIr2O11 Pnma (62) mp-21742 [hull=0.000, icsd=1, PRIMARY]; Ba4Al(IrO5)2 Cmc2_1 (36) mp-1228412 [hull=0.030, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.91.235147 (Coexisting charge and magnetic orders in the dimer-chain iridate<mml:m...)

## Al-Ba-O-Yb
- rank 2420 | 1 samples | 1 papers | 1 compositions
- compositions: Ba6Yb2Al4O15 (1)
- measured range: 301-1073 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba5Yb2ZrAl2O13 P6_3/mmc (194) mp-1214540 [hull=0.054, PRIMARY]
- papers: https://doi.org/10.1111/jace.15504 (Thermophysical properties of rare earth barium aluminates)

## Al-Bi-Br-Cl-Te
- rank 2421 | 1 samples | 1 papers | 1 compositions
- compositions: (Bi4Te4Br2)(Al2Cl5.46Br0.54)Cl2 (1)
- measured range: 301-435 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlBi2Te2BrCl4 C2/c (15) mp-1200931 [hull=0.077, icsd=1, PRIMARY]; Al4Bi8Te8(BrCl3)5 P1 (1) mp-1229275 [hull=0.135, PRIMARY]
- papers: https://doi.org/10.1021/ic400782c (Semiconducting [(Bi4Te4Br2)(Al2Cl6–xBrx)]Cl2and [Bi2Se2Br](AlCl4): Cat...)

## Al-Bi-O-Sb-Te
- rank 2422 | 1 samples | 1 papers | 1 compositions
- compositions: (Al2O3)0.2Bi0.4Sb1.6Te3 (1)
- measured range: 297-474 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.3390/en81112323 (Thermoelectric Properties of Alumina-Doped Bi0.4Sb1.6Te3 Nanocomposite...)

## Al-Bi-Sb-Te
- rank 2423 | 1 samples | 1 papers | 1 compositions
- compositions: (Al2Te3)0.2(Bi0.5Sb1.5Te3)0.8 (1)
- measured range: 319-534 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/j.jallcom.2007.05.063 (Crystal structure analysis and thermoelectric properties of p-type pse...)

## Al-C-Co
- rank 2424 | 1 samples | 1 papers | 1 compositions
- compositions: AlCCo3 (1)
- measured range: 11-330 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlCo3C Pm-3m (221) mp-10037 [hull=0.019, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/ic500026t (Good Thermoelectric Performance in Strongly Correlated System SnCCo3wi...)

## Al-C-Cr
- rank 2425 | 1 samples | 1 papers | 1 compositions
- compositions: Cr2AlC (1)
- measured range: 474-1473 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlCr2C P6_3/mmc (194) mp-9956 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2011.04.134 (Effect of Cr7C3 on the mechanical, thermal, and electrical properties ...)

## Al-C-Fe
- rank 2426 | 1 samples | 1 papers | 1 compositions
- compositions: AlC1.1Fe3 (1)
- measured range: 10-334 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlFe3C Pm-3m (221) mp-22793 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/j.jmmm.2012.05.022 (The structural, magnetic, electrical/thermal transport properties and ...)

## Al-C-Ni
- rank 2427 | 1 samples | 1 papers | 1 compositions
- compositions: AlCNi3 (1)
- measured range: 11-350 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al3Ni9C P4/mmm (123) mp-1229029 [hull=0.045, PRIMARY]; Al4Ni12C P4/mmm (123) mp-1228788 [hull=0.037, PRIMARY]; AlNi3C Pm-3m (221) mp-1207084 [hull=0.168, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.74.224416 (Strong spin fluctuations and possible non-Fermi-liquid behavior in<mml...)

## Al-C-Y
- rank 2428 | 1 samples | 1 papers | 1 compositions
- compositions: YAl3C3 (1)
- measured range: 350-1049 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y3AlC Pm-3m (221) mp-4448 [hull=0.000, icsd=2, PRIMARY]; Y(AlC)3 P6_3/mmc (194) mp-1104050 [hull=0.000, icsd=1, PRIMARY]; Y3AlC3 Pmma (51) mp-1103810 [hull=0.000, icsd=1, PRIMARY]; Y5Al3C4 P4/mbm (127) mp-1190521 [hull=0.025, icsd=1, PRIMARY]
- papers: https://doi.org/10.1111/j.1551-2916.2007.01855.x (Crystal Structure and Thermoelectric Properties of YAl3C3)

## Al-Ca-Cu-O
- rank 2429 | 1 samples | 1 papers | 1 compositions
- compositions: CuAl0.8Ca0.2O2 (1)
- measured range: 540-1141 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/j.mseb.2005.10.035 (Effect of partial substitution of Ca for Al on the microstructure and ...)

## Al-Ca-Na-Sb
- rank 2430 | 1 samples | 1 papers | 1 compositions
- compositions: Ca4NaAl2Sb6 (1)
- measured range: 307-693 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Na3Ca3AlSb4 P6_3mc (186) mp-1190339 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1002/adfm.201000970 (The Zintl Compound Ca5Al2Sb6 for Low-Cost Thermoelectric Power Generation)

## Al-Ce-Fe
- rank 2431 | 1 samples | 1 papers | 1 compositions
- compositions: CeFe1.7Ir0.3Al10 (1)
- dopant candidates (<5% at.): Ir (1)
- measured range: 10-358 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(Al4Fe)2 Pbam (55) mp-607077 [hull=0.000, icsd=4, PRIMARY]; Ce(Al2Fe)4 I4/mmm (139) mp-16486 [hull=0.000, icsd=3, PRIMARY]; Ce(Al5Fe)2 Cmcm (63) mp-1193938 [hull=0.000, icsd=1, PRIMARY]; Ce2Al3Fe R-3m (166) mp-1226882 [hull=0.027, PRIMARY]; Ce2AlFe3 R-3m (166) mp-1226839 [hull=0.015, PRIMARY]
- papers: https://doi.org/10.1016/j.jmmm.2022.169370 (Thermal conductivity, thermoelectric power and Mössbauer investigation...)

## Al-Ce-Ga-La
- rank 2432 | 1 samples | 1 papers | 1 compositions
- compositions: Ce0.5La0.5Al2Ga2 (1)
- measured range: 10-280 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1103/physrevb.43.3204 (Antiferromagnetism inCe1−xLaxAl2Ga2andCe1−yYyAl2Ga2Kondo-lattice systems)

## Al-Ce-Ga-Y
- rank 2433 | 1 samples | 1 papers | 1 compositions
- compositions: Ce0.7Y0.3Al2Ga2 (1)
- measured range: 10-282 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1103/physrevb.43.3204 (Antiferromagnetism inCe1−xLaxAl2Ga2andCe1−yYyAl2Ga2Kondo-lattice systems)

## Al-Ce-La
- rank 2434 | 1 samples | 1 papers | 1 compositions
- compositions: Ce0.5La0.5Al3 (1)
- measured range: 10-169 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaCeAl4 F-43m (216) mp-1222920 [hull=0.015, PRIMARY]
- papers: https://doi.org/10.1016/0378-4363(77)90404-1 (Influence of the crystalline field on the Kondo effect: Cerium and ytt...)

## Al-Ce-Os
- rank 2435 | 1 samples | 1 papers | 1 compositions
- compositions: CeOs2Al10 (1)
- measured range: 10-297 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce3(Al3Os)4 P6_3/mmc (194) mp-1213926 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.85.245116 (Transport, thermoelectric, and thermal expansion investigations of the...)

## Al-Co-Cr
- rank 2436 | 1 samples | 1 papers | 1 compositions
- compositions: Co2CrAl (1)
- measured range: 309-1015 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlCrCo2 Fm-3m (225) mp-10883 [hull=0.071, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/s11664-016-4944-0 (Structural and Thermoelectric Properties of Ternary Full-Heusler Alloys)

## Al-Co-Ho
- rank 2437 | 1 samples | 1 papers | 1 compositions
- compositions: Ho(Co0.9Al0.1)2 (1)
- measured range: 16-297 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ho2Al3Co14 P6_3/mmc (194) mp-1205177 [hull=0.064, icsd=1, PRIMARY]; HoAlCo Amm2 (38) mp-1224090 [hull=0.044, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.78.035101 (Effect of static and dynamic disorder on electronic transport inRCo2co...)

## Al-Co-Ni-Sb-Sn-Ta-Ti
- rank 2438 | 1 samples | 1 papers | 1 compositions
- compositions: Ti0.66Al0.67Ta0.67NiCoSn0.5Sb1.5 (1)
- measured range: 297-825 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1021/acsaem.4c03382 (Entropy Engineering in the Off-Stoichiometric Ti<sub>2</sub>NiCoSn<sub...)

## Al-Co-Ni-Sb-Sn-Ta-Ti-Zr
- rank 2439 | 1 samples | 1 papers | 1 compositions
- compositions: Ti0.5Al0.5Ta0.5Zr0.5NiCoSn0.5Sb1.5 (1)
- measured range: 292-874 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1021/acsaem.4c03382 (Entropy Engineering in the Off-Stoichiometric Ti<sub>2</sub>NiCoSn<sub...)

## Al-Co-Si
- rank 2440 | 1 samples | 1 papers | 1 compositions
- compositions: CoSi0.88Al0.12 (1)
- measured range: 295-973 K (5th-95th pct of 4 curves; full span incl. outliers 295-1015 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al14Co5Si2 Pnma (62) mp-645302 [hull=0.004, icsd=2, PRIMARY]; Al(CoSi)2 P-3m1 (164) mp-10010 [hull=0.000, icsd=1, PRIMARY]; Al3Co3Si4 Im-3m (229) mp-1214851 [hull=0.000, PRIMARY]; AlCo2Si Immm (71) mp-1015831 [hull=1.062, PRIMARY]
- papers: https://doi.org/10.1063/1.2041843 (Effects of Al doping on the thermoelectric performance of CoSi single ...)

## Al-Cr-Cu-U
- rank 2441 | 1 samples | 1 papers | 1 compositions
- compositions: UCu3Cr2Al7 (1)
- measured range: 12-297 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jallcom.2005.12.049 (Low temperature specific heat and thermoelectric power of UCu3M2Al7 al...)

## Al-Cr-Fe
- rank 2442 | 1 samples | 1 papers | 1 compositions
- compositions: Al74.5Cr18.2Fe7.3 (1)
- measured range: 10-289 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlCrFe2 Fm-3m (225) mp-16495 [hull=0.017, icsd=2, PRIMARY]; Al119Cr16Fe13 Cm (8) mp-1215162 [hull=0.087, PRIMARY]; Al2CrFe Immm (71) mp-1096119 [hull=2.674, PRIMARY]; AlCrFe2 P4/mmm (123) mp-1228906 [hull=0.022]; AlCrFe2 Cmm2 (35) mp-1228937 [hull=0.171]
- papers: https://doi.org/10.1016/j.jallcom.2005.06.055 (Magnetic, electrical and thermal transport properties of Al–Cr–Fe appr...)

## Al-Cr-Ge
- rank 2443 | 1 samples | 1 papers | 1 compositions
- compositions: Al60Cr19.9Fe0.1Ge20 (1)
- dopant candidates (<5% at.): Fe (1)
- measured range: 14-300 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlCrGe F222 (22) mp-1228945 [hull=0.024, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/18/35/022 (Physical properties of the icosahedral quasicrystal Al60Cr19.9Fe0.1Ge20)

## Al-Cr-O
- rank 2444 | 1 samples | 1 papers | 1 compositions
- compositions: (Al2O3)90.06(Cr3C2)9.94 (1)
- dopant candidates (<5% at.): C (1)
- measured range: 297-871 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al2Cr4O19 P2/c (13) mp-1205208 [hull=0.324, icsd=1, PRIMARY]; Al19CrO30 P1 (1) mp-761414 [hull=0.004, PRIMARY]; Al2CrO5 C2/c (15) mp-773505 [hull=0.035, PRIMARY, AMBIGUOUS]; Al3CrO6 R3 (146) mp-1228485 [hull=0.013, PRIMARY, AMBIGUOUS]; AlCr2O4 Fd-3m (227) mp-773322 [hull=0.103, PRIMARY]
- papers: https://doi.org/10.1016/0956-7151(94)00303-y (Heat conduction of composites and its dependence on the microstructure...)

## Al-Cr-Si
- rank 2445 | 1 samples | 1 papers | 1 compositions
- compositions: Cr(Si0.92Al0.08)2 (1)
- measured range: 300-700 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al3Cr20Si9 C222 (21) mp-1228632 [hull=0.111, PRIMARY]; Al8Cr4Si3 P-1 (2) mp-1214842 [hull=0.080, PRIMARY]; Al9Cr3Si P6_3/mmc (194) mp-1214838 [hull=0.000, PRIMARY]; AlCr6Si Pm-3 (200) mp-1228922 [hull=0.003, PRIMARY]
- papers: https://doi.org/10.1016/j.scriptamat.2006.09.015 (Effects of Al doping on the transport performances of CrSi2 single cry...)

## Al-Cs-Si
- rank 2446 | 1 samples | 1 papers | 1 compositions
- compositions: Cs7.9Al7.9Si38.1 (1)
- measured range: 10-397 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1002/chem.201403416 (A Combined Metal-Halide/Metal Flux Synthetic Route towards Type-I Clat...)

## Al-Cu-Fe-U
- rank 2447 | 1 samples | 1 papers | 1 compositions
- compositions: UCu3.5Fe1.5Al7 (1)
- measured range: 12-299 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UAl7Fe3Cu2 Cm (8) mp-1216353 [hull=0.043, PRIMARY]; UAl8(FeCu)2 Immm (71) mp-1216340 [hull=0.105, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2005.12.049 (Low temperature specific heat and thermoelectric power of UCu3M2Al7 al...)

## Al-Cu-Ga-S-Sn
- rank 2448 | 1 samples | 1 papers | 1 compositions
- compositions: Cu3Al0.5Ga0.5SnS5 (1)
- measured range: 374-665 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1021/acsaem.0c00730 (Effect of Gallium Substitution in Cu3Al1–xGaxSnS5 Nanobulk Materials o...)

## Al-Cu-Li
- rank 2449 | 1 samples | 1 papers | 1 compositions
- compositions: Al55.0Li35.8Cu9.2 (1)
- measured range: 10-15 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li4(AlCu2)3 P6_3/mmc (194) mp-1211199 [hull=0.010, PRIMARY]; Li6Al13Cu8 P4/mbm (127) mp-1211217 [hull=0.027, PRIMARY]; LiAl2Cu Fm-3m (225) mp-1185307 [hull=0.015, PRIMARY]; LiAlCu2 Fm-3m (225) mp-867272 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1143/jpsj.58.2472 (Electronic Properities of the Single-Grained Icosahedral Phase of Al–L...)

## Al-Cu-Mg
- rank 2450 | 1 samples | 1 papers | 1 compositions
- compositions: Al5Cu6Mg2 (1)
- measured range: 13-381 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MgAl2Cu Cmcm (63) mp-3034 [hull=0.000, icsd=3, PRIMARY]; Mg11(Al2Cu)6 Fd-3m (227) mp-1200279 [hull=0.020, icsd=1, PRIMARY]; Mg2Al5Cu6 Pm-3 (200) mp-30178 [hull=0.000, icsd=1, PRIMARY]; Mg14AlCu Amm2 (38) mp-1028253 [hull=0.054, PRIMARY, AMBIGUOUS]; Mg16Al12Cu R3m (160) mp-1185659 [hull=0.065, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2013.03.012 (Physical properties of the V-Al5Cu6Mg2 complex intermetallic phase)
