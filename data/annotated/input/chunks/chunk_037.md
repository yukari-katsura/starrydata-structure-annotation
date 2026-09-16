# Host systems -- chunk 037 of 73

Ranks 1801-1850 by sample count. These 50 host systems cover 110 samples (0.21% of the TE set); cumulative through this chunk: 95.53%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## S-Th-U
- rank 1801 | 3 samples | 1 papers | 3 compositions
- compositions: (US)75(ThS)25 (1); (US)50(ThS)50 (1); (US)25(ThS)75 (1)
- measured range: 287-1352 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ThU2S5 Pna2_1 (33) mp-1217436 [hull=0.070, PRIMARY]; ThUS2 R-3m (166) mp-1217311 [hull=0.015, PRIMARY]; ThUS2 P4/mmm (123) mp-1217265 [hull=0.045]
- papers: https://doi.org/10.1063/1.1702883 (Thermoelectric Properties of Uranium Monosulfide, Thorium Monosulfide,...)

## S-Ti-Tl
- rank 1802 | 3 samples | 1 papers | 1 compositions
- compositions: Tl4TiS4 (3)
- sample form: Bulk (3)
- measured range: 313-577 K (5th-95th pct of 3 curves)
- [ref 1] TEDesignLab / ICSD: Ti(TlS)4 (14) [PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ti(TlS2)2 Pbca (61) mp-14441 [hull=0.014, icsd=1, PRIMARY]; Ti5TlS8 C2/m (12) mp-1101049 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1134/s0020168510010036 (Effect of nonstoichiometry on the thermoelectric properties of Tl4TiS4...)

## Sb-Sc-U
- rank 1803 | 3 samples | 1 papers | 1 compositions
- compositions: U3ScSb5 (3)
- measured range: 11-295 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ScU3Sb5 P6_3/mcm (193) mp-13243 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/cm061281y (Anisotropic Transport and Magnetic Properties of Ternary Uranium Antim...)

## Sb-Te-Zn
- rank 1804 | 3 samples | 1 papers | 3 compositions
- compositions: Zn0.25Sb1.75Te3 (1); Zn0.5Sb1.5Te3 (1); Zn0.75Sb1.25Te3 (1)
- sample form: Bulk (3)
- measured range: 300-425 K (5th-95th pct of 12 curves)
- papers: https://doi.org/10.1016/j.jallcom.2021.158621 (Optical and thermoelectric properties of Sb2Te3/ZnTe nanostructured co...)

## Sb-Ti-U
- rank 1805 | 3 samples | 1 papers | 1 compositions
- compositions: U3TiSb5 (3)
- measured range: 10-295 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U3TiSb5 P6_3/mcm (193) mp-21227 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/cm061281y (Anisotropic Transport and Magnetic Properties of Ternary Uranium Antim...)

## Se
- rank 1806 | 3 samples | 1 papers | 3 compositions
- compositions: Se0.9999935In0.0000065 (1); Se0.99935In0.00065 (1); Se0.9667In0.0333 (1)
- dopant candidates (<5% at.): In (3)
- [ref 1] TEDesignLab / ICSD: Se P3_121 (152) mp-14 [hull=0.006, icsd=27, PRIMARY]; Se R-3 (148) mp-147 [hull=0.026, icsd=2]
- [ref 2] MP, ranked by ICSD evidence: Se Pm-3m (221) mp-7755 [hull=0.180, icsd=3]; Se Im-3m (229) mp-119 [hull=0.589, icsd=2]; Se Cmcm (63) mp-1009757 [hull=0.156, icsd=1]; Se Fd-3m (227) mp-12771 [hull=0.509, icsd=1]
- papers: https://doi.org/10.1007/bf00616667 (Electrical conductivity and thermoelectric power of liquid selenium do...)

## Sn-U
- rank 1807 | 3 samples | 2 papers | 2 compositions
- compositions: U3Sn5 (2); USn3 (1)
- measured range: 13-299 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): USn3 Pm-3m (221) mp-20336 [hull=0.000, icsd=9, PRIMARY]; U3Sn7 Cmmm (65) mp-1205645 [hull=0.005, PRIMARY]; U5Sn4 P6_3/mcm (193) mp-1208157 [hull=0.192, PRIMARY]; USn P-6m2 (187) mp-972495 [hull=0.124, PRIMARY]; USn2 Cmmm (65) mp-1207038 [hull=0.024, PRIMARY]
- papers: https://doi.org/10.1016/s0921-4526(90)81072-v (Magnetic and transport properties of new uranium compounds U3Sn5 and U...) | https://doi.org/10.1143/jpsj.59.3687 (Some Characteristics of the Thermoelectric Power in Uranium Intermetal...)

## Sr
- rank 1808 | 3 samples | 1 papers | 1 compositions
- compositions: Sr (3)
- measured range: 288-899 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr Fm-3m (225) mp-76 [hull=0.000, icsd=5, PRIMARY, AMBIGUOUS]; Sr Im-3m (229) mp-95 [hull=0.009, icsd=4]; Sr P6/mmm (191) mp-19858 [hull=0.225, icsd=4]; Sr P6_3/mmc (194) mp-867202 [hull=0.005, icsd=3]; Sr I4_1/amd (141) mp-10617 [hull=0.262, icsd=2]
- papers: https://doi.org/10.1016/0022-5088(78)90162-5 (The electrical resistivity and thermoelectric power of Ca and Sr above...)

## Ta-Te
- rank 1809 | 3 samples | 1 papers | 3 compositions
- compositions: TaTe2 (1); Ta0.94Nb0.06Te2 (1); Ta0.9Nb0.1Te2 (1)
- dopant candidates (<5% at.): Nb (2)
- sample form: SingleCrystal (3)
- measured range: 12-332 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TaTe2 C2/m (12) mp-1967 [hull=0.000, icsd=5, PRIMARY]; TaTe4 P4/mcc (124) mp-22817 [hull=0.013, icsd=4, PRIMARY]; Ta21Te13 P6mm (183) mp-680343 [hull=0.000, icsd=1, PRIMARY]; TaTe4 P4/ncc (130) mp-202 [hull=0.000, icsd=2]
- papers: https://doi.org/10.1209/0295-5075/109/17003 (Structural, electrical, and thermoelectric properties of distorted 1T-...)

## U
- rank 1810 | 3 samples | 2 papers | 1 compositions
- compositions: U (3)
- sample form: Bulk (1)
- measured range: 297-1019 K (5th-95th pct of 4 curves; full span incl. outliers 297-1374 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U Cmcm (63) mp-44 [hull=0.000, icsd=21, PRIMARY]; U Im-3m (229) mp-108 [hull=0.280, icsd=6]; U P4_2nm (102) mp-43 [hull=0.101, icsd=4]; U P4_2/mnm (136) mp-93 [hull=0.111, icsd=4]; U Pmma (51) mp-1197206 [hull=0.370, icsd=2]
- papers: https://doi.org/10.1016/0022-3115(70)90185-6 (Electrical resistivity and thermoelectric power of polycrystalline ura...) | https://doi.org/10.1016/0022-3115(88)90127-4 (Thermophysical properties of uranium-zirconium alloys)

## Ag-Al-Cu-Ni-Zr
- rank 1811 | 2 samples | 1 papers | 1 compositions
- compositions: Zr65Al7.5Ni10Cu7.3Fe0.2Ag10 (2)
- dopant candidates (<5% at.): Fe (2)
- measured range: 11-247 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1088/0953-8984/14/27/312 (M$ouml$ssbauer and transport studies of amorphous and icosahedral Zr-N...)

## Ag-Au
- rank 1812 | 2 samples | 2 papers | 2 compositions
- compositions: Ag0.92Au0.06Pd0.02 (1); Ag0.89Au0.11 (1)
- dopant candidates (<5% at.): Pd (1)
- sample form: Other (1)
- measured range: 24-92 K (5th-95th pct of 2 curves; full span incl. outliers 24-263 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ag3Au I4/mmm (139) mp-1183214 [hull=0.000, PRIMARY, AMBIGUOUS]; AgAu R-3m (166) mp-1229092 [hull=0.000, PRIMARY, AMBIGUOUS]; AgAu3 P6_3/mmc (194) mp-985287 [hull=0.000, PRIMARY, AMBIGUOUS]; Ag3Au Pm-3m (221) mp-1183137 [hull=0.005]; Ag3Au P6_3/mmc (194) mp-1183205 [hull=0.017]
- papers: https://doi.org/10.1109/77.919762 (Characterization of the thermal conductivity and mechanical properties...) | https://doi.org/10.1016/0011-2275(93)90215-a (Thermal and electrical properties of Ag-Au and Ag-Cu alloy tapes for m...)

## Ag-Ba-Eu-Sb
- rank 1813 | 2 samples | 1 papers | 2 compositions
- compositions: Ba0.95Eu0.3AgSb (1); Ba0.96Eu0.2AgSb (1)
- sample form: Bulk (2)
- measured range: 299-778 K (5th-95th pct of 14 curves)
- papers: https://doi.org/10.1007/s40843-020-1640-2 (Point defect approach to enhance the thermoelectric performance of Zin...)

## Ag-Bi-Cs-S
- rank 1814 | 2 samples | 1 papers | 2 compositions
- compositions: Cs1.2Ag0.6Bi3.4S6 (1); Cs0.6Ag0.8Bi2.2S4 (1)
- sample form: Bulk (2)
- measured range: 305-817 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CsAg2BiS3 P2_1/c (14) mp-1193928 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/jacs.7b06373 (Homologous Series of 2D Chalcogenides Cs–Ag–Bi–Q (Q = S, Se) with Ion-...)

## Ag-Bi-Sb
- rank 1815 | 2 samples | 1 papers | 2 compositions
- compositions: Bi85Sb10Ag5 (1); Bi85Sb8Ag7 (1)
- sample form: Bulk (2)
- measured range: 79-300 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1016/j.jpcs.2007.02.047 (Thermoelectric performance of ternary Bi–Sb–Ag alloys prepared by mech...)

## Ag-Bi-Sb-Se
- rank 1816 | 2 samples | 1 papers | 1 compositions
- compositions: AgBi0.5Sb0.5Se2 (2)
- sample form: Bulk (2)
- measured range: 300-551 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ag2BiSbSe4 I-4m2 (119) mp-1229120 [hull=0.046, PRIMARY]
- papers: https://doi.org/10.1021/ja3020204 (Solid-Solutioned Homojunction Nanoplates with Disordered Lattice: A Pr...)

## Ag-Ce-Cu-In
- rank 1817 | 2 samples | 1 papers | 2 compositions
- compositions: CeInCu1.8Ag0.2 (1); CeInCu1.5Ag0.5 (1)
- measured range: 10-293 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeInCuAg F-43m (216) mp-1226682 [hull=0.027, PRIMARY]
- papers: https://doi.org/10.1007/bf00683635 (Thermpower of Ce x Y1?x InCu2 and CeInCu y Ag2?y)

## Ag-Ce-In
- rank 1818 | 2 samples | 1 papers | 1 compositions
- compositions: CeInAg2 (2)
- measured range: 10-295 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeInAg2 Fm-3m (225) mp-672191 [hull=0.000, icsd=1, PRIMARY]; Ce2InAg P4/mmm (123) mp-1227262 [hull=0.054, PRIMARY]
- papers: https://doi.org/10.1007/bf00683635 (Thermpower of Ce x Y1?x InCu2 and CeInCu y Ag2?y)

## Ag-Cl-Se-Te
- rank 1819 | 2 samples | 1 papers | 2 compositions
- compositions: Ag5Te1.4Se0.6Cl (1); Ag5Te1.6Se0.4Cl (1)
- sample form: Bulk (2)
- measured range: 302-482 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.jssc.2011.01.031 (Effects of partial anion substitution on the thermoelectric properties...)

## Ag-Cs-S-Te
- rank 1820 | 2 samples | 1 papers | 1 compositions
- compositions: CsAg5TeS2 (2)
- measured range: 322-803 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1021/acs.chemmater.8b03306 (Two-Dimensional CsAg5Te3–xSx Semiconductors: Multi-anion Chalcogenides...)

## Ag-Cs-Te
- rank 1821 | 2 samples | 1 papers | 1 compositions
- compositions: CsAg5Te3 (2)
- sample form: Bulk (2)
- measured range: 292-761 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CsAg5Te3 P4_2/mnm (136) mp-9206 [hull=0.000, icsd=1, PRIMARY]; CsAg3Te2 C2/m (12) mp-1213692 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1002/anie.201605015 (Concerted Rattling in CsAg5\nTe3\n Leading to Ultralow Thermal Conduct...)

## Ag-Dy-Sb
- rank 1822 | 2 samples | 1 papers | 1 compositions
- compositions: DyAgSb2 (2)
- sample form: SingleCrystal (2)
- measured range: 11-296 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DyAgSb2 P4/nmm (129) mp-10965 [hull=0.000, icsd=1, PRIMARY]; Dy2AgSb3 P4/mmm (123) mp-1206934 [hull=3.071, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/23/47/476001 (Thermoelectric power of RAgSb2(R = Y, La, Ce, and Dy) in zero and appl...)

## Ag-Ga-Se-Te
- rank 1823 | 2 samples | 1 papers | 2 compositions
- compositions: Ag9Ga(Se0.85Te0.15)6 (1); Ag9Ga(Se0.83Te0.17)6 (1)
- measured range: 299-849 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ga2Ag2TeSe3 C2 (5) mp-1224849 [hull=0.010, PRIMARY]; GaAgTeSe I2_12_12_1 (24) mp-1224853 [hull=0.016, PRIMARY]
- papers: https://doi.org/10.1016/j.joule.2017.09.006 (High Thermoelectric Performance of Ag9GaSe6 Enabled by Low Cutoff Freq...)

## Ag-Ge-In-Te
- rank 1824 | 2 samples | 1 papers | 1 compositions
- compositions: (GeTe)5.5AgInTe2 (2)
- sample form: Bulk (2)
- measured range: 10-399 K (5th-95th pct of 9 curves)
- papers: https://doi.org/10.1039/c4ta00072b (TAGS-related indium compounds and their thermoelectric properties – th...)

## Ag-Ge-Yb
- rank 1825 | 2 samples | 1 papers | 1 compositions
- compositions: YbAgGe (2)
- sample form: SingleCrystal (2)
- measured range: 10-347 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbAgGe P-62m (189) mp-9776 [hull=0.000, icsd=2, PRIMARY]; Yb2AgGe Fm-3m (225) mp-865630 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.82.174403 (Thermoelectric power investigations of YbAgGe across the quantum criti...)

## Ag-In-Mo-Se
- rank 1826 | 2 samples | 2 papers | 1 compositions
- compositions: Ag3In2Mo15Se19 (2)
- sample form: Bulk (1)
- measured range: 11-1122 K (5th-95th pct of 7 curves)
- papers: https://doi.org/10.1021/cm3009557 (Synthesis, Crystal and Electronic Structures, and Thermoelectric Prope...) | https://doi.org/10.1021/acs.chemmater.6b04076 (Ultralow Lattice Thermal Conductivity and Enhanced Thermoelectric Perf...)

## Ag-In-Se-Zn
- rank 1827 | 2 samples | 1 papers | 2 compositions
- compositions: AgInZnSe2 (1); Ag0.9In0.9Zn0.2Se2 (1)
- sample form: Bulk (2)
- measured range: 319-816 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1039/c4ra03054k (Site occupations of Zn in AgInSe2-based chalcopyrites responsible for ...)

## Ag-Mn-O-Pr-Sr
- rank 1828 | 2 samples | 1 papers | 2 compositions
- compositions: (Pr0.67Sr0.33MnO3)0.8(Ag2O)0.2 (1); (Pr0.67Sr0.33MnO3)0.7(Ag2O)0.3 (1)
- measured range: 10-312 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.jallcom.2014.08.216 (Near room temperature magneto-transport (TCR &amp; MR) and magnetocalo...)

## Ag-Mo-Se-Tl
- rank 1829 | 2 samples | 2 papers | 2 compositions
- compositions: Ag2Tl2Mo9Se11 (1); Ag3Tl2Mo15Se19 (1)
- sample form: Bulk (2)
- measured range: 11-792 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.1021/ic501939k (X-ray Characterization, Electronic Band Structure, and Thermoelectric ...) | https://doi.org/10.1021/acs.inorgchem.8b03452 (Electronic Band Structure and Transport Properties of the Cluster Comp...)

## Ag-Mo-Te
- rank 1830 | 2 samples | 1 papers | 2 compositions
- compositions: AgMo6Te8 (1); Ag2Mo6Te8 (1)
- sample form: Bulk (2)
- measured range: 300-802 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ag(TeMo)6 C2/m (12) mp-29607 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/s1003-6326(08)60326-x (Thermoelectric properties of MxMo6Te8 (M=Ag, Cu))

## Ag-Nb-O
- rank 1831 | 2 samples | 1 papers | 2 compositions
- compositions: (Nb2O5)67.57Ag32.43 (1); (Nb2O5)63.07Ag36.93 (1)
- measured range: 294-510 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NbAgO3 Pbcm (57) mp-5537 [hull=0.038, icsd=12, PRIMARY]; Nb4Ag2O11 R3c (161) mp-984755 [hull=0.031, icsd=1, PRIMARY]; Nb3AgO8 Ibam (72) mp-16837 [hull=0.038, icsd=1, PRIMARY]; GdNb5Ag2O15 P4/mbm (127) mp-1212605 [hull=0.102, PRIMARY]; Nb14AgO36 Immm (71) mp-1210596 [hull=0.016, PRIMARY]
- papers: https://doi.org/10.1016/j.matlet.2015.04.148 (Niobium(V) oxide with added silver as a thermoelectric material prepar...)

## Ag-Ni-O
- rank 1832 | 2 samples | 1 papers | 1 compositions
- compositions: AgNiO2 (2)
- measured range: 11-294 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ni(AgO)2 R-3m (166) mp-19405 [hull=0.043, icsd=14, PRIMARY]; NiAgO2 P6_3/mmc (194) mp-19284 [hull=0.000, icsd=1, PRIMARY, AMBIGUOUS]; NiAgO2 R-3m (166) mp-19069 [hull=0.001, icsd=1]
- papers: https://doi.org/10.1016/0022-4596(88)90338-6 (On the electrical properties of polycrystalline delafossite-type AgNiO2)

## Ag-Te-Tm
- rank 1833 | 2 samples | 1 papers | 1 compositions
- compositions: TmAgTe2 (2)
- sample form: Bulk (2)
- measured range: 299-873 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TmAgTe2 P-42_1m (113) mp-1078600 [hull=0.000, icsd=1, PRIMARY]; TmAgTe2 P-3m1 (164) mp-12953 [hull=0.015, icsd=1]; TmAgTe2 P3m1 (156) mp-1216570 [hull=0.024]
- papers: https://doi.org/10.1039/c5tc01440a (Computational and experimental investigation of TmAgTe2and XYZ2compoun...)

## Al-B-Ba-K-Li-O
- rank 1834 | 2 samples | 1 papers | 1 compositions
- compositions: K3Ba3Li2Al4B6O20F (2)
- dopant candidates (<5% at.): F (2)
- sample form: SingleCrystal (2)
- measured range: 298-723 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): K3Ba3Li2Al4B6O20F P-62c (190) mp-1195057 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/acs.cgd.8b01054 (Physical Properties of a Promising Nonlinear Optical Crystal K3Ba3Li2A...)

## Al-B-Co-Fe-Nb-O
- rank 1835 | 2 samples | 1 papers | 2 compositions
- compositions: (CoFeB)44(NbAlO3)56 (1); (CoFeB)48(NbAlO3)52 (1)
- measured range: 11-298 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/b978-0-12-813594-5.00013-8 (Magnetic Metal-Nonstoichiometric Oxide Nanocomposites: Structure, Tran...)

## Al-B-Co-Fe-O
- rank 1836 | 2 samples | 1 papers | 2 compositions
- compositions: (CoFeB)49(AlO1.5)51 (1); (CoFeB)53(AlO1.5)47 (1)
- measured range: 12-294 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/b978-0-12-813594-5.00013-8 (Magnetic Metal-Nonstoichiometric Oxide Nanocomposites: Structure, Tran...)

## Al-B-Tm
- rank 1837 | 2 samples | 1 papers | 1 compositions
- compositions: TmAlB4 (2)
- measured range: 300-300 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TmAlB4 Pbam (55) mp-1191390 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.5005869 (Thermal conductivity of PrRh4.8B2, a layered boride compound)

## Al-B-Y
- rank 1838 | 2 samples | 1 papers | 1 compositions
- compositions: YAlB14 (2)
- sample form: Bulk (2)
- measured range: 324-980 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1007/s40243-014-0031-8 (Microstructure and thermoelectric properties of Y x Al y B14 samples f...)

## Al-B-Yb
- rank 1839 | 2 samples | 1 papers | 1 compositions
- compositions: YbAlB4 (2)
- sample form: SingleCrystal (2)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbAlB4 Pbam (55) mp-1191244 [hull=0.049, icsd=4, PRIMARY]; YbAlB14 Imma (74) mp-1198572 [hull=0.004, icsd=2, PRIMARY]; Yb2AlB6 Pbam (55) mp-21102 [hull=0.107, icsd=1, PRIMARY]; YbAlB4 Cmmm (65) mp-1095659 [hull=0.052, icsd=2]; YbAlB4 Pmmm (47) mp-1077729 [hull=0.246, icsd=1]
- papers: https://doi.org/10.1103/physrevlett.109.156405 (Thermoelectric Response Near a Quantum Critical Point ofβ−YbAlB4andYbR...)

## Al-Ba-Dy-O
- rank 1840 | 2 samples | 1 papers | 2 compositions
- compositions: Ba6Dy2Al4O15 (1); Ba2Dy2Al4O15 (1)
- sample form: Bulk (2)
- measured range: 301-1074 K (5th-95th pct of 2 curves; full span incl. outliers 301-1268 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba6Dy2Al4O15 P2/c (13) mp-1214541 [hull=0.000, PRIMARY]; Ba6Dy2Al4O15 Amm2 (38) mp-1228068 [hull=0.034]
- papers: https://doi.org/10.1111/jace.15504 (Thermophysical properties of rare earth barium aluminates)

## Al-Ba-Er-O
- rank 1841 | 2 samples | 1 papers | 2 compositions
- compositions: Ba6Er2Al4O15 (1); Ba2ErAlO5 (1)
- sample form: Bulk (2)
- measured range: 303-1073 K (5th-95th pct of 2 curves; full span incl. outliers 303-1278 K)
- papers: https://doi.org/10.1111/jace.15504 (Thermophysical properties of rare earth barium aluminates)

## Al-Ba-Ga-K-Sn
- rank 1842 | 2 samples | 2 papers | 1 compositions
- compositions: K9Ba15Al31Ga8Sn97 (2)
- measured range: 101-641 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/j.jallcom.2016.09.231 (Preparation and thermoelectric properties of sintered type-II clathrat...) | https://doi.org/10.1021/acs.chemmater.6b05027 (Predicting Ground-State Configurations and Electronic Properties of th...)

## Al-Ba-La-Mn-O
- rank 1843 | 2 samples | 1 papers | 2 compositions
- compositions: (La0.7Ba0.3MnO3)0.875(Al2O3)0.125 (1); (La0.7Ba0.3MnO3)0.85(Al2O3)0.15 (1)
- measured range: 85-286 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.cplett.2019.04.021 (Impact of aluminum on the Seebeck coefficient and magnetic properties ...)

## Al-C-N-Ti
- rank 1844 | 2 samples | 1 papers | 2 compositions
- compositions: Ti2AlC0.5N0.5 (1); Ti3AlCN (1)
- sample form: Bulk (2)
- measured range: 16-292 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti4Al2CN P-3m1 (164) mp-1217141 [hull=0.005, PRIMARY]; Ti8Al4CN3 P-3m1 (164) mp-1217099 [hull=0.004, PRIMARY]
- papers: https://doi.org/10.1063/1.2979326 (Electronic and thermal properties of Ti[sub 3]Al(C[sub 0.5],N[sub 0.5]...)

## Al-C-Si-Zr
- rank 1845 | 2 samples | 1 papers | 2 compositions
- compositions: Zr2(Al3.56Si0.44)4C5 (1); Zr3(Al3.56Si0.44)4C6 (1)
- sample form: Bulk (2)
- measured range: 470-1474 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1111/j.1551-2916.2008.02879.x (Mechanical and Thermophysical Properties of Zr-Al-Si-C Ceramics)

## Al-C-Ti
- rank 1846 | 2 samples | 1 papers | 2 compositions
- compositions: Ti3AlC2 (1); Ti2AlC (1)
- sample form: Bulk (2)
- measured range: 10-288 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti2AlC P6_3/mmc (194) mp-12990 [hull=0.000, icsd=8, PRIMARY]; Ti3AlC Pm-3m (221) mp-3271 [hull=0.000, icsd=8, PRIMARY]; Ti3AlC2 P6_3/mmc (194) mp-3747 [hull=0.000, icsd=4, PRIMARY]; Ti5Al2C3 R-3m (166) mp-1079706 [hull=0.002, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.2979326 (Electronic and thermal properties of Ti[sub 3]Al(C[sub 0.5],N[sub 0.5]...)

## Al-Ca
- rank 1847 | 2 samples | 2 papers | 2 compositions
- compositions: CaAl2 (1); CaAl4 (1)
- sample form: Polycrystal (1); SingleCrystal (1)
- measured range: 14-278 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaAl2 Fd-3m (227) mp-2404 [hull=0.000, icsd=5, PRIMARY]; CaAl4 I4/mmm (139) mp-1749 [hull=0.012, icsd=2, PRIMARY]; Ca13Al14 C2/m (12) mp-1193055 [hull=0.002, icsd=1, PRIMARY]; Ca4Al Fd-3m (227) mp-1214044 [hull=0.464, PRIMARY]; Ca2Al25Cr Fd-3m (227) mp-1215151 [hull=0.501, PRIMARY]
- papers: https://doi.org/10.1063/1.1808248 (Unusual thermoelectric behavior of packed crystalline granular metals) | https://doi.org/10.1016/j.jallcom.2015.08.193 (Characteristic Fermi surfaces and charge density wave in SrAl4 and rel...)

## Al-Ca-In-Sb
- rank 1848 | 2 samples | 1 papers | 2 compositions
- compositions: Ca5AlInSb6 (1); Ca5Al0.95In0.95Zn0.1Sb6 (1)
- dopant candidates (<5% at.): Zn (1)
- measured range: 297-971 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1039/c4dt02206h (Thermoelectric properties of the Ca5Al2−xInxSb6solid solution)

## Al-Ca-Sb-Zn
- rank 1849 | 2 samples | 1 papers | 2 compositions
- compositions: Ca9Zn4.5Al3Sb9 (1); Ca9Zn4Al20.33Sb9 (1)
- measured range: 301-871 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.1021/acs.chemmater.6b02498 (Tuning the Thermoelectric Properties of Ca9Zn4+xSb9by Controlled Dopin...)

## Al-Ce-Ir
- rank 1850 | 2 samples | 2 papers | 1 compositions
- compositions: Ce2Ir3Al9 (2)
- sample form: Polycrystal (2)
- measured range: 10-294 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeAlIr Pnma (62) mp-1102352 [hull=0.000, icsd=2, PRIMARY]; Ce2(Al3Ir)3 Cmcm (63) mp-1213885 [hull=0.000, PRIMARY]; CeAlIr P6_3/mmc (194) mp-1077038 [hull=0.000, icsd=1]
- papers: https://doi.org/10.1016/s0925-8388(98)00408-3 (Transport and magnetic properties of new ternary Ce2T3X9-compounds (T=...) | https://doi.org/10.1016/j.jallcom.2021.160925 (A new look at the ground state properties of Ce2Ir3Al9: Coexistence of...)
