# Host systems -- chunk 044 of 73

Ranks 2151-2200 by sample count. These 50 host systems cover 100 samples (0.19% of the TE set); cumulative through this chunk: 96.88%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Cs-O-V
- rank 2151 | 2 samples | 1 papers | 2 compositions
- compositions: (K0.20Cs0.80)VO3 (1); CsVO3 (1)
- dopant candidates (<5% at.): K (1)
- measured range: 498-682 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CsV3O8 P2_1/m (11) mp-651814 [hull=0.000, icsd=2, PRIMARY]; Cs2V4O9 I-42d (122) mp-1193809 [hull=0.001, icsd=1, PRIMARY]; Cs4BaV6O18 R3c (161) mp-1198646 [hull=0.000, icsd=1, PRIMARY]; Cs2V5O13 I4mm (107) mp-617180 [hull=0.000, icsd=1, PRIMARY]; CsV2O5 P6mm (183) mp-1078919 [hull=0.101, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/bf02746039 (Thermoelectric power of ferroelectric potassium vanadate, cesium vanad...)

## Cu-Eu-Nb-O-Sr
- rank 2152 | 2 samples | 1 papers | 2 compositions
- compositions: (Nb0.9Ti0.1)Sr2EuCu2O8 (1); (Nb0.75Cu0.25)Sr2EuCu2O8 (1)
- dopant candidates (<5% at.): Ti (1)
- curator composition details (from the paper): polycrystalline (2)
- measured range: 10-270 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2EuNb(CuO4)2 I4/mcm (140) mp-16786 [hull=0.022, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2015.06.001 (Structure and superconductivity in new Nb-based cuprates (Nb,Ti,Cu)Sr2...)

## Cu-Fe-Gd-O
- rank 2153 | 2 samples | 1 papers | 2 compositions
- compositions: Gd0.8Ba0.2CuFeO5 (1); Gd0.7Ba0.3CuFeO5 (1)
- dopant candidates (<5% at.): Ba (2)
- curator composition details (from the paper): polycrystalline (2)
- measured range: 365-2577 K (5th-95th pct of 2 curves; full span incl. outliers 365-2641 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdFe4(CuO4)3 Im-3 (204) mp-1188097 [hull=0.015, icsd=2, PRIMARY]
- papers: https://doi.org/10.1111/jace.13728 (Electrical and Thermal Conduction Behaviors in La‐Substituted GdBaCuFe...)

## Cu-Fe-La-O-Sr
- rank 2154 | 2 samples | 1 papers | 2 compositions
- compositions: La0.7Sr0.3Cu0.6Fe0.4O3 (1); La0.7Sr0.3Cu0.4Fe0.6O3 (1)
- sample form: rod-shaped (2)
- measured range: 324-1071 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2La2FeCu3O10 Pbam (55) mp-1173276 [hull=0.000, PRIMARY]; Sr2La3Fe4CuO15 R-3m (166) mp-1218789 [hull=0.025, PRIMARY]; Sr2La6FeCu7O20 Pm (6) mp-1173271 [hull=0.003, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2008.07.044 (Electrical conductivity, thermal expansion and electrochemical propert...)

## Cu-Fe-S-Sb
- rank 2155 | 2 samples | 2 papers | 1 compositions
- compositions: Cu10Fe2Sb4S13 (2)
- sample form: Other (1)
- measured range: 38-573 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Fe2Cu10Sb4S13 I-42m (121) mp-1224745 [hull=0.064, PRIMARY]
- papers: https://doi.org/10.1143/apex.5.051201 (Thermoelectric Properties of Mineral Tetrahedrites Cu$_{10}$Tr$_{2}$Sb...) | https://doi.org/10.1021/cm404026k (Enhanced Thermoelectric Performance of Synthetic Tetrahedrites)

## Cu-Ga-S-Sn
- rank 2156 | 2 samples | 1 papers | 2 compositions
- compositions: Cu3Al0.25Ga0.75SnS5 (1); Cu3GaSnS5 (1)
- dopant candidates (<5% at.): Al (1)
- sample form: Bulk (2)
- measured range: 372-665 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.1021/acsaem.0c00730 (Effect of Gallium Substitution in Cu3Al1–xGaxSnS5 Nanobulk Materials o...)

## Cu-Gd
- rank 2157 | 2 samples | 2 papers | 2 compositions
- compositions: GdCu (1); Gd2Cu9 (1)
- sample form: Bulk (1)
- measured range: 11-294 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdCu5 P6/mmm (191) mp-636253 [hull=0.000, icsd=5, PRIMARY]; GdCu Pm-3m (221) mp-614455 [hull=0.000, icsd=4, PRIMARY]; GdCu2 Imma (74) mp-1077933 [hull=0.000, icsd=3, PRIMARY]; GdCu6 Pnma (62) mp-1194708 [hull=0.003, icsd=3, PRIMARY]
- papers: https://doi.org/10.1143/jjap.46.5797 (Magnetic and Transport Properties of GdNi1-xCux) | https://doi.org/10.1016/0375-9601(96)00055-2 (Electrical resistivity and thermopower of Gd2Cu9 and Dy2Cu9)

## Cu-Gd-Sb
- rank 2158 | 2 samples | 2 papers | 1 compositions
- compositions: Gd3Cu3Sb4 (2)
- sample form: Polycrystal (1)
- measured range: 11-398 K (5th-95th pct of 7 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdCuSb2 P4/nmm (129) mp-20502 [hull=0.000, icsd=2, PRIMARY]; Gd3Cu3Sb4 I-43d (220) mp-1189617 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1109/ict.2006.331231 (Galvanomagnetic and Thermoelectric Properties of R3Cu3Sb4 Compounds) | https://doi.org/10.1063/1.367018 (Magnetic and thermoelectric properties of R3Cu3Sb4 (R=La, Ce, Gd, Er))

## Cu-Ge-P
- rank 2159 | 2 samples | 1 papers | 2 compositions
- compositions: CuGe4P3 (1); CuGe2P3 (1)
- sample form: Bulk (2)
- measured range: 11-397 K (5th-95th pct of 8 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuGe2P3 P3m1 (156) mp-1225680 [hull=0.115, PRIMARY, AMBIGUOUS]; CuGe2P3 Cm (8) mp-673663 [hull=0.120]; CuGe2P3 Pmm2 (25) mp-1225735 [hull=0.324]
- papers: https://doi.org/10.1039/b914555a (Composition, structure, bonding and thermoelectric properties of “CuT2...)

## Cu-Ge-S-Zn
- rank 2160 | 2 samples | 2 papers | 2 compositions
- compositions: Cu2ZnGeS4 (1); Cu22Zn4V2Ge6S32 (1)
- dopant candidates (<5% at.): V (1)
- sample form: Bulk (1)
- measured range: 10-675 K (5th-95th pct of 6 curves)
- [ref 1] TEDesignLab / ICSD: ZnCu2GeS4 I-42m (121) mp-6408 [hull=0.000, icsd=4, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Zn4FeCu10(GeS4)5 Pm (6) mp-1217745 [hull=0.012, PRIMARY, AMBIGUOUS]; ZnCu2GeS4 Pmn2_1 (31) mp-1105527 [hull=0.003, icsd=3]; Zn4FeCu10(GeS4)5 C2 (5) mp-1216234 [hull=0.012]
- papers: https://doi.org/10.1021/ja410753k (Effect of Isovalent Substitution on the Thermoelectric Properties of t...) | https://doi.org/10.1063/1.4892593 (Tunable electronic properties and low thermal conductivity in syntheti...)

## Cu-Ge-Sb-Se-Te
- rank 2161 | 2 samples | 1 papers | 2 compositions
- compositions: (GeTe)0.85(CuSbSe2)0.15 (1); (GeTe)0.8(CuSbSe2)0.2 (1)
- sample form: Polycrystal (2)
- measured range: 301-764 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1021/acsaem.1c00632 (Thermoelectric Performance Optimization and Phase Transition of GeTe b...)

## Cu-H-Ni
- rank 2162 | 2 samples | 1 papers | 2 compositions
- compositions: Ni0.4Cu0.6H0.15 (1); Ni0.4Cu0.6H0.08 (1)
- measured range: 82-276 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.jallcom.2004.11.126 (Transport properties of some hydrogenated nickel-based alloys)

## Cu-Hg-O-Sr
- rank 2163 | 2 samples | 1 papers | 1 compositions
- compositions: Hg0.7Cr0.3Sr2CuO4 (2)
- dopant candidates (<5% at.): Cr (2)
- sample form: Bulk (2)
- measured range: 48-301 K (5th-95th pct of 4 curves; full span incl. outliers 48-454 K)
- papers: https://doi.org/10.1016/0921-4526(96)00180-9 (X-ray structure, electrical resistivity, Hall effect and thermoelectri...)

## Cu-In-Lu
- rank 2164 | 2 samples | 2 papers | 2 compositions
- compositions: LuInCu4 (1); LuCuIn (1)
- sample form: Bulk (2)
- measured range: 12-281 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LuInCu2 Fm-3m (225) mp-4972 [hull=0.000, icsd=2, PRIMARY]; Lu2InCu2 P4/mbm (127) mp-1080814 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/0304-8853(94)01472-8 (Transport properties of RInCu4 with C15b-type structure) | https://doi.org/10.1016/j.jpcs.2008.04.031 (Electronic structure and magnetic properties of the compound CeCuIn)

## Cu-In-Pr
- rank 2165 | 2 samples | 2 papers | 1 compositions
- compositions: PrInCu2 (2)
- sample form: Bulk (1)
- measured range: 11-286 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrInCu2 Fm-3m (225) mp-21148 [hull=0.013, icsd=2, PRIMARY]; PrInCu P-62m (189) mp-1080085 [hull=0.000, icsd=1, PRIMARY]; Pr2InCu2 P4/mbm (127) mp-1079498 [hull=0.000, icsd=1, PRIMARY]; Pr(InCu)6 Immm (71) mp-1220006 [hull=0.013, PRIMARY]; Pr2(InCu3)3 Pnnm (58) mp-1221285 [hull=0.023, PRIMARY]
- papers: https://doi.org/10.1016/j.jmmm.2006.10.047 (Non-enhancement of thermoelectric-power coefficient of at low temperat...) | https://doi.org/10.1016/j.physb.2006.01.190 (Non-magnetic-doublet ground state in ; Enhancement of the specific-hea...)

## Cu-K-Te
- rank 2166 | 2 samples | 1 papers | 2 compositions
- compositions: K2.1Ba0.9Cu8Te10 (1); K2BaCu8Te10 (1)
- dopant candidates (<5% at.): Ba (2)
- sample form: Bulk (2)
- measured range: 11-299 K (5th-95th pct of 4 curves)
- [ref 1] TEDesignLab / ICSD: K4Cu8Te11 C2/m (12) mp-28743 [hull=0.005, icsd=1, PRIMARY]; KCuTe P6_3/mmc (194) mp-7436 [hull=0.000, icsd=1, PRIMARY]; KCu3Te2 (12) [PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: K2(CuTe)5 Cmcm (63) mp-28737 [hull=0.000, icsd=1, PRIMARY]; K2Cu2Te5 Cmcm (63) mp-29828 [hull=0.019, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/cm000390o (Thermoelectric Properties and Electronic Structure of the Cage Compoun...)

## Cu-La-O-S-Sr
- rank 2167 | 2 samples | 1 papers | 2 compositions
- compositions: ((La0.8Sr0.2)O)CuS (1); ((La0.7Sr0.3)O)CuS (1)
- measured range: 81-290 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr3La21Cu10(SO24)2 Pm (6) mp-1173252 [hull=0.181, PRIMARY]
- papers: https://doi.org/10.1016/0921-4526(94)00579-k (The new conductive oxysulfides [(La1−Sr )O]CuS containing a Cu-layer)

## Cu-Mg
- rank 2168 | 2 samples | 1 papers | 2 compositions
- compositions: Cu4.58Mg1.70Ga0.1Fe0.1Mn0.1Si0.1V0.1Zn0.1Cr 0.05Sn0.01Ti0.01Ca0.001Ag0.001Zr0.001 (1); Cu4.58Mg1.70Ga0.1Fe0.1Mn0.1Si0.1V0.1Zn0.1Cr0.05Sn0.01Ti0.01Ca0.001Ag0.001Zr 0.001 (1)
- dopant candidates (<5% at.): Ga (2), Fe (2), Mn (2), Si (2), V (2), Zn (2), Cr (2), Sn (2), Ti (2), Ca (2), Ag (2), Zr (2)
- measured range: 11-234 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): MgCu2 Fd-3m (227) mp-1038 [hull=0.000, icsd=14, PRIMARY]; Mg2Cu Fddd (70) mp-2481 [hull=0.000, icsd=8, PRIMARY]; Mg15Cu P-6m2 (187) mp-1023610 [hull=0.045, PRIMARY]; Mg3Cu Imm2 (44) mp-978279 [hull=0.073, PRIMARY]; Mg5Cu P-62m (189) mp-1185803 [hull=0.074, PRIMARY]
- papers: https://doi.org/10.1063/1.1735617 (Low‐Temperature Transport Properties of Commercial Metals and Alloys. ...)

## Cu-Mo-Te
- rank 2169 | 2 samples | 1 papers | 2 compositions
- compositions: CuMo6Te8 (1); Cu2Mo6Te8 (1)
- sample form: Bulk (2)
- measured range: 296-803 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1016/s1003-6326(08)60326-x (Thermoelectric properties of MxMo6Te8 (M=Ag, Cu))

## Cu-N-Pd
- rank 2170 | 2 samples | 1 papers | 1 compositions
- compositions: Cu3PdN (2)
- measured range: 19-294 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu11PdN4 P4/mmm (123) mp-1105864 [hull=0.254, icsd=2, PRIMARY]; Cu12PdN4 P4/mmm (123) mp-1188468 [hull=0.389, icsd=2, PRIMARY]; Cu23PdN8 I4/mmm (139) mp-1225855 [hull=0.219, PRIMARY]; Cu31PdN8 Pmmm (47) mp-1225808 [hull=0.227, PRIMARY]; Cu3PdN Pm-3m (221) mp-1206517 [hull=0.115, PRIMARY]
- papers: https://doi.org/10.1063/1.4992006 (Epitaxial thin films of Dirac semimetal antiperovskite           Cu<su...)

## Cu-Nb-Ni-Sn-Ti
- rank 2171 | 2 samples | 1 papers | 2 compositions
- compositions: Ti24.3Nb5.9Ni27Cu5.7Sn31.6Sb1.5 (1); Ti15.6Nb12.3Ni27.7Cu5.1Sn31.2Sb1.5 (1)
- dopant candidates (<5% at.): Sb (2)
- measured range: 13-884 K (5th-95th pct of 8 curves; full span incl. outliers 13-1024 K)
- papers: https://doi.org/10.1557/opl.2013.217 (Thermoelectric behaviour of p- and n- type Ti-Ni-Sn half Heusler alloy...)

## Cu-Ni-O-Si
- rank 2172 | 2 samples | 1 papers | 2 compositions
- compositions: (Ni0.47Cu0.53)(SiO2)0.11 (1); (Ni0.47Cu0.53)(SiO2)0.08 (1)
- curator composition details (from the paper): 30vol.%SiO2 (1); 20vol.%SiO2 (1)
- measured range: 292-1070 K (5th-95th pct of 8 curves)
- papers: https://doi.org/10.1016/s0925-8388(03)00295-0 (Thermoelectric properties of constantan/spherical SiO2 and Al2O3 parti...)

## Cu-Ni-Sb-Zr
- rank 2173 | 2 samples | 1 papers | 1 compositions
- compositions: Zr3Ni2.5Cu0.5Sb4 (2)
- sample form: Bulk (2)
- measured range: 24-849 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1063/1.4869573 (High thermoelectric performance in the multi-valley electronic system ...)

## Cu-O-Pb-Sr
- rank 2174 | 2 samples | 1 papers | 2 compositions
- compositions: (Pb0.75Cu0.25)Sr2(Ca0.5Y0.5)Cu2O7 (1); (Pb0.75Cu0.25)Sr2(Ca0.5Yb0.5)Cu2O7 (1)
- dopant candidates (<5% at.): Ca (2), Y (1), Yb (1)
- sample form: Bulk (2)
- measured range: 44-298 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr4CaHoCu6(PbO4)4 P-1 (2) mp-1218617 [hull=0.021, PRIMARY]; Sr4CaYCu6(PbO4)4 P-1 (2) mp-1218734 [hull=0.021, PRIMARY, AMBIGUOUS]; Sr8CaY3Cu12(PbO4)8 P-1 (2) mp-1218823 [hull=0.020, PRIMARY]; Sr9Nd3Cu12(PbO4)8 C2/m (12) mp-1218827 [hull=0.022, PRIMARY]; Sr4CaYCu6(PbO4)4 I4/mmm (139) mp-1218685 [hull=0.025]
- papers: https://doi.org/10.1016/0038-1098(93)90531-q (Superconductivity in Pb-based 1212 cuprates; evidence for under-doping...)

## Cu-O-Ru
- rank 2175 | 2 samples | 2 papers | 2 compositions
- compositions: La0.5Ca0.5Cu3Ru4O12 (1); Cu1.82La0.18RuO4 (1)
- dopant candidates (<5% at.): La (2), Ca (1)
- sample form: Bulk (1); SingleCrystal (1)
- measured range: 16-911 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1080/14686996.2021.1951593 (Thermoelectric materials taking advantage of spin entropy: lessons fro...) | https://doi.org/10.1103/physrevresearch.6.023222 (Negatively enhanced thermopower near a Van Hove singularity in electro...)

## Cu-O-Ru-Sr-Y
- rank 2176 | 2 samples | 1 papers | 1 compositions
- compositions: Ru0.9Sr2YCu2.1O7.9 (2)
- measured range: 12-297 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr12Y6CuRu5O36 P-1 (2) mp-1173630 [hull=0.013, PRIMARY]; Sr4CeY3Cu4(RuO10)2 P4mm (99) mp-1218787 [hull=0.055, PRIMARY]
- papers: https://doi.org/10.1007/s10948-010-1071-7 (Magnetic and Thermal Behavior of Ru0.9Sr2YCu2.1O7.9 Magneto-Supercondu...)

## Cu-O-S
- rank 2177 | 2 samples | 1 papers | 1 compositions
- compositions: (Cu1.8S)88.63(SiO2)11.37 (2)
- dopant candidates (<5% at.): Si (2)
- sample form: Bulk (2)
- measured range: 322-623 K (5th-95th pct of 10 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuSO4 Pnma (62) mp-20525 [hull=0.000, icsd=4, PRIMARY]; Cu4SO10 P2_1/c (14) mp-1197335 [hull=0.049, icsd=3, PRIMARY]; Cu2SO5 C2/m (12) mp-4386 [hull=0.011, icsd=3, PRIMARY]; Cu3SO8 Pnma (62) mp-1202614 [hull=0.026, icsd=2, PRIMARY]; Cu2SO4 Fddd (70) mp-28491 [hull=0.020, icsd=1, PRIMARY]
- papers: https://doi.org/10.1002/pssa.201330185 (Size effect of SiO2on enhancing thermoelectric properties of Cu1.8S)

## Cu-O-V-Zn
- rank 2178 | 2 samples | 1 papers | 2 compositions
- compositions: ZnCuV2O7 (1); Zn2CuV2O7 (1)
- sample form: Bulk (2)
- measured range: 375-924 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): V2ZnCuO7 C2 (5) mp-1216520 [hull=0.008, PRIMARY]; V4Zn3Cu3O22 P-1 (2) mp-1217369 [hull=0.352, PRIMARY]; V4ZnCu3O14 P1 (1) mp-1216485 [hull=0.008, PRIMARY]
- papers: https://doi.org/10.2320/matertrans.e-mra2007856 (Thermoelectric Properties and Phase Transition of (Zn<I><SUB>x</SUB></...)

## Cu-Pb-Se
- rank 2179 | 2 samples | 1 papers | 2 compositions
- compositions: (PbSe0.998Br0.002)93.19(Cu2Se)6.81 (1); (PbSe0.998Br0.002)90.54(Cu2Se)9.46 (1)
- dopant candidates (<5% at.): Br (2)
- sample form: Bulk (2)
- measured range: 316-816 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.1021/jacs.8b10448 (High-Performance n-Type PbSe–Cu2Se Thermoelectrics through Conduction ...)

## Cu-Pd-Yb
- rank 2180 | 2 samples | 2 papers | 2 compositions
- compositions: YbCu4Pd (1); YbPdCu4 (1)
- sample form: Polycrystal (1)
- measured range: 11-278 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbCu4Pd F-43m (216) mp-1077750 [hull=0.000, icsd=1, PRIMARY]; Yb2CuPd Fm-3m (225) mp-1187894 [hull=0.020, PRIMARY]; YbCuPd2 Fm-3m (225) mp-1187677 [hull=0.039, PRIMARY]
- papers: https://doi.org/10.1007/bf02570277 (Low temperature hall effect and thermopower of YbCu4Au and YbCu4Pd) | https://doi.org/10.1016/s0304-8853(10)80217-3 (Thermoelectric power of YbMCu4 (M = Ag, Au and Pd) and YbPd2Si2)

## Cu-Rb-Te
- rank 2181 | 2 samples | 1 papers | 1 compositions
- compositions: Rb2BaCu8Te10 (2)
- dopant candidates (<5% at.): Ba (2)
- sample form: Bulk (2)
- measured range: 10-307 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1021/cm000390o (Thermoelectric Properties and Electronic Structure of the Cage Compoun...)

## Cu-Sb-Se-Zn
- rank 2182 | 2 samples | 1 papers | 2 compositions
- compositions: (Cu3SbSe4)0.25Zn4Sb3 (1); (Cu3SbSe4)0.18Zn4Sb3 (1)
- sample form: Bulk (2)
- measured range: 296-649 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.1016/j.jallcom.2013.11.049 (Enhanced thermoelectric performance of β-Zn4Sb3 based composites incor...)

## Cu-Si-Y
- rank 2183 | 2 samples | 1 papers | 2 compositions
- compositions: YCu2.05Si2 (1); Ce0.1Y0.9Cu2.05Si2 (1)
- dopant candidates (<5% at.): Ce (1)
- sample form: Polycrystal (2)
- measured range: 13-293 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y(CuSi)2 I4/mmm (139) mp-3390 [hull=0.000, icsd=3, PRIMARY]; Y3(CuSi)4 Immm (71) mp-1101887 [hull=0.000, icsd=1, PRIMARY]; YCuSi P6_3/mmc (194) mp-8126 [hull=0.000, icsd=1, PRIMARY]; Y2Cu3Si Pmm2 (25) mp-1216078 [hull=0.045, PRIMARY]; Y3Cu11Si4 P6_3/mmc (194) mp-1207856 [hull=0.072, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.64.195107 (Transport properties of<mml:math xmlns:mml=\"http://www.w3.org/1998/Ma...)

## Dy-Er-Pd-Sb
- rank 2184 | 2 samples | 1 papers | 2 compositions
- compositions: Er0.25Dy0.75Pd1.02Sb1.05 (1); Er0.25Dy0.75PdSb1.05 (1)
- measured range: 20-350 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1063/1.123596 (Antimonides with the half-Heusler structure: New thermoelectric materials)

## Dy-Mo-O
- rank 2185 | 2 samples | 2 papers | 1 compositions
- compositions: Dy2Mo2O7 (2)
- sample form: Bulk (1)
- measured range: 12-255 K (5th-95th pct of 2 curves; full span incl. outliers 12-295 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Dy2Mo2O7 Fd-3m (227) mp-1190424 [hull=0.014, icsd=1, PRIMARY]; Dy4Mo4O11 Pbam (55) mp-19669 [hull=0.175, icsd=1, PRIMARY]; Dy5(MoO6)2 C2/m (12) mp-1105361 [hull=0.000, icsd=1, PRIMARY]; Dy2(MoO4)3 Pba2 (32) mp-1213230 [hull=0.000, PRIMARY]; Dy2Mo8O33 P2_1 (4) mp-1198422 [hull=0.280, PRIMARY]
- papers: https://doi.org/10.1016/0022-3697(86)90030-2 (Thermoelectric power of RE2Mo2O7 pyrochlores) | https://doi.org/10.1088/0953-8984/2/15/010 (Electrical conductivity and thermoelectric power of the compounds (Dyx...)

## Dy-Ni-Sb
- rank 2186 | 2 samples | 2 papers | 1 compositions
- compositions: DyNiSb (2)
- measured range: 14-992 K (5th-95th pct of 9 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DyNiSb F-43m (216) mp-4510 [hull=0.000, icsd=2, PRIMARY]; Dy(NiSb)2 P4/nmm (129) mp-1080718 [hull=0.092, icsd=1, PRIMARY]; Dy5Ni2Sb I4/mcm (140) mp-9353 [hull=0.000, icsd=1, PRIMARY]; DyNiSb2 P4/nmm (129) mp-1079636 [hull=0.020, icsd=1, PRIMARY]; Dy2NiSb4 P-4m2 (115) mp-1225313 [hull=0.010, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2019.152596 (High-temperature power factor of half-Heusler phases RENiSb (RE = Sc, ...) | https://doi.org/10.1103/physrevapplied.14.054046 (Thermoelectric Performance of the Half-Heusler Phases \n<mml:math xmln...)

## Er-Mo-O
- rank 2187 | 2 samples | 2 papers | 2 compositions
- compositions: ErMo2O7 (1); Er2Mo2O7 (1)
- sample form: Bulk (1)
- measured range: 13-301 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Er5(MoO6)2 C2/m (12) mp-1105166 [hull=0.025, icsd=1, PRIMARY]; Er2Mo4O15 P2_1/c (14) mp-1212977 [hull=0.000, PRIMARY]; Er6MoO12 P-1 (2) mp-1213660 [hull=0.298, PRIMARY]; ErMoO5 P2_1/c (14) mp-1213170 [hull=0.096, PRIMARY]; KLiEr2(MoO4)4 C2/c (15) mp-1211563 [hull=0.014, PRIMARY]
- papers: https://doi.org/10.1016/0022-3697(86)90030-2 (Thermoelectric power of RE2Mo2O7 pyrochlores) | https://doi.org/10.1016/0025-5408(80)90094-x (Electrical properties of Ln2Mo2O7 pyrochlores (Ln=SmYb,Y))

## Er-N
- rank 2188 | 2 samples | 2 papers | 1 compositions
- compositions: ErN (2)
- measured range: 15-72 K (5th-95th pct of 2 curves; full span incl. outliers 15-255 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ErN Fm-3m (225) mp-19830 [hull=0.000, icsd=27, PRIMARY]; ErN Pm-3m (221) mp-1002229 [hull=0.955, icsd=1]
- papers: https://doi.org/10.1063/1.2158689 (Specific heat and thermal conductivity of HoN and ErN at cryogenic tem...) | https://doi.org/10.1016/j.jmmm.2010.01.016 (Magnetic properties of ErN films)

## Er-Ni-Sb-Sn-Zr
- rank 2189 | 2 samples | 1 papers | 2 compositions
- compositions: (Zr0.25Er0.75)Ni(Sn0.25Sb0.75) (1); (Zr0.75Er0.25)Ni(Sn0.75Sb0.25) (1)
- sample form: Bulk (2)
- measured range: 16-301 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.1557/proc-545-421 (Observed Properties and Electronic Structure of RNiSb Compounds (R = H...)

## Er-Se
- rank 2190 | 2 samples | 1 papers | 2 compositions
- compositions: ErSe (1); Er3Se4 (1)
- sample form: Bulk (1)
- measured range: 298-801 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Er2Se3 Fddd (70) mp-209 [hull=0.000, icsd=6, PRIMARY]; ErSe Fm-3m (225) mp-2491 [hull=0.000, icsd=5, PRIMARY]; ErSe2 P4/nmm (129) mp-9978 [hull=0.039, icsd=2, PRIMARY]; ErSe2 Immm (71) mp-1077779 [hull=0.051, icsd=1]; Er2Se3 P-4m2 (115) mp-1225508 [hull=0.063]
- papers: https://doi.org/10.1063/1.1703024 (Thermoelectric and Electrical Measurements in the Er‐Se System)

## Eu-Ge-Ni
- rank 2191 | 2 samples | 2 papers | 2 compositions
- compositions: EuNi2(Si0.05Ge0.95)2 (1); Eu2Ni3Ge5 (1)
- dopant candidates (<5% at.): Si (1)
- sample form: Bulk (1); SingleCrystal (1)
- measured range: 10-297 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Eu(NiGe)2 I4/mmm (139) mp-3333 [hull=0.000, icsd=3, PRIMARY]; EuNiGe P2_1/c (14) mp-5887 [hull=0.000, icsd=2, PRIMARY]; EuNiGe3 I4mm (107) mp-974769 [hull=0.000, icsd=2, PRIMARY]; EuNiGe2 Cmcm (63) mp-1080556 [hull=0.000, icsd=2, PRIMARY]; EuNi9Ge4 I4/mcm (140) mp-1213407 [hull=0.213, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/s0921-4526(99)00865-0 (Thermoelectric power of EuNi2(Si1−xGex)2) | https://doi.org/10.7566/jpsj.86.034708 (Unique Pressure versus Temperature Phase Diagram for Antiferromagnets ...)

## Eu-Ge-Pt
- rank 2192 | 2 samples | 1 papers | 2 compositions
- compositions: Pr0.1Eu0.9Pt4Ge12 (1); EuPt4Ge12 (1)
- dopant candidates (<5% at.): Pr (1)
- measured range: 24-290 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): EuGe3Pt I4mm (107) mp-19763 [hull=0.000, icsd=2, PRIMARY]; EuGePt P2_13 (198) mp-19798 [hull=0.000, icsd=2, PRIMARY]; Eu(GePt)2 P2_1/m (11) mp-1080180 [hull=0.000, icsd=1, PRIMARY]; Eu(Ge3Pt)4 Im-3 (204) mp-1184807 [hull=0.365, icsd=1, PRIMARY]; Eu(GePt)2 P2_1/c (14) mp-607169 [hull=0.102, icsd=1]
- papers: https://doi.org/10.1103/physrevb.95.134517 (Crossover and coexistence of superconductivity and antiferromagnetism ...)

## Eu-O-V
- rank 2193 | 2 samples | 1 papers | 1 compositions
- compositions: EuVO3 (2)
- measured range: 159-300 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): EuVO4 I4_1/amd (141) mp-1095243 [hull=0.001, icsd=5, PRIMARY]; Eu2VO4 I4/mmm (139) mp-25120 [hull=0.000, icsd=2, PRIMARY]; Eu2V2O5 Ima2 (46) mp-1099750 [hull=0.029, PRIMARY]; Eu3V2O7 I4/mmm (139) mp-1212877 [hull=0.017, PRIMARY]; EuVO2 I4_1/amd (141) mp-1213429 [hull=0.319, PRIMARY]
- papers: https://doi.org/10.1016/j.jcrysgro.2022.126752 (Single-crystal thin film growth of the Mott insulator EuVO3 under biax...)

## F-La
- rank 2194 | 2 samples | 1 papers | 2 compositions
- compositions: LaF3 (1); (LaF3)99.2Eu0.8 (1)
- dopant candidates (<5% at.): Eu (1)
- measured range: 75-298 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaF3 P-3c1 (165) mp-905 [hull=0.000, icsd=21, PRIMARY]; LaF P6_3/mmc (194) mp-1184996 [hull=0.348, PRIMARY]; LaF2 Fm-3m (225) mp-1207087 [hull=0.220, PRIMARY]; SrLa5F17 P1 (1) mp-675492 [hull=0.023, PRIMARY]; LaF3 I4/mmm (139) mp-323 [hull=0.172, icsd=6]
- papers: https://doi.org/10.1007/bf00859487 (Thermal conductivity of rare earth fluoride crystals)

## F-Na-Y
- rank 2195 | 2 samples | 1 papers | 1 compositions
- compositions: NaYF4 (2)
- measured range: 313-399 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Na2YF6 P-62m (189) mp-1210270 [hull=0.000, PRIMARY]; Na3YF6 Fm-3m (225) mp-1114251 [hull=0.169, PRIMARY]; NaY2F7 C2/m (12) mp-675778 [hull=0.033, PRIMARY]; NaY3F10 P4_2/mmc (131) mp-676023 [hull=0.136, PRIMARY]; NaYF4 I4_1/amd (141) mp-34081 [hull=0.000, PRIMARY, AMBIGUOUS]
- papers: https://doi.org/10.1002/crat.2170181134 (Thermoelectric power studies on polycrystalline NaYF4 samples)

## F-O-Sb-Sr-Ti
- rank 2196 | 2 samples | 1 papers | 1 compositions
- compositions: (SrF)2Ti2Sb2O (2)
- measured range: 11-347 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2Ti2Sb2OF2 I4/mmm (139) mp-1079717 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/cm9027258 (Structure and Physical Properties of the Layered Pnictide-Oxides: (SrF...)

## F-O-Sn
- rank 2197 | 2 samples | 2 papers | 2 compositions
- compositions: (SnO2)0.83F0.17 (1); Sn2OF (1)
- measured range: 110-503 K (5th-95th pct of 2 curves; full span incl. outliers 110-663 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sn2OF2 C2/m (12) mp-27480 [hull=0.000, icsd=1, PRIMARY]; Sn2OF5 C2/m (12) mp-29590 [hull=0.000, icsd=1, PRIMARY]; Sn4OF6 P2_12_12_1 (19) mp-28932 [hull=0.001, icsd=1, PRIMARY]; Sn13(O5F3)2 C2/c (15) mp-760170 [hull=0.046, PRIMARY]; Sn3(OF)2 Pnma (62) mp-753246 [hull=0.047, PRIMARY]
- papers: https://doi.org/10.4028/www.scientific.net/msf.725.281 (Electrical Properties of Fluorine Doped Tin Dioxide Film Grown by Spra...) | https://doi.org/10.1007/s10854-018-8795-8 (Optical and electrical properties of fluorine doped tin oxide thin film)

## Fe-Ga-Ti-V
- rank 2198 | 2 samples | 1 papers | 2 compositions
- compositions: Fe2V0.8Ti0.2Ga (1); Fe2V0.75Ti0.25Ga (1)
- sample form: Bulk (2)
- measured range: 297-704 K (5th-95th pct of 10 curves)
- papers: https://doi.org/10.1063/1.4934734 (Thermoelectric properties optimization of Fe2VGa by tuning electronic ...)

## Fe-Gd-O
- rank 2199 | 2 samples | 1 papers | 1 compositions
- compositions: GdFeO (2)
- curator composition details (from the paper): GdFeO a-axis (1); GdFeO c-axis (1)
- sample form: SingleCrystal (2)
- measured range: 12-183 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdFeO3 Pnma (62) mp-600862 [hull=0.000, icsd=16, PRIMARY]; Gd3FeO6 Cmc2_1 (36) mp-1189831 [hull=0.009, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.83.014414 (Magnetic phase transitions and magnetoelectric coupling of GdFeO3singl...)

## Fe-H-La-O-P
- rank 2200 | 2 samples | 1 papers | 2 compositions
- compositions: LaFePO0.75H0.25 (1); LaFePO0.90H0.30 (1)
- measured range: 22-288 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1103/physrevb.95.214515 (Three superconducting phases with different categories of pairing in h...)
