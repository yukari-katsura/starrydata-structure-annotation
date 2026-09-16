# Host systems -- chunk 051 of 73

Ranks 2501-2550 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 97.89%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Al-Zr
- rank 2501 | 1 samples | 1 papers | 1 compositions
- compositions: ZrAl3 (1)
- measured range: 323-923 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZrAl3 I4/mmm (139) mp-395 [hull=0.000, icsd=9, PRIMARY]; ZrAl2 P6_3/mmc (194) mp-2772 [hull=0.000, icsd=9, PRIMARY]; Zr2Al P6_3/mmc (194) mp-2557 [hull=0.014, icsd=7, PRIMARY]; Zr5Al3 P6_3/mcm (193) mp-2044 [hull=0.061, icsd=6, PRIMARY]; Zr3Al Pm-3m (221) mp-1471 [hull=0.000, icsd=6, PRIMARY]
- papers: Tailoring Thermal Transport Properties by Inducing Surface Oxidation Reactions in Bulk Metal Composites

## Am-N
- rank 2502 | 1 samples | 1 papers | 1 compositions
- compositions: AmN (1)
- measured range: 216-1468 K (5th-95th pct of 1 curves)
- papers: Thermal diffusivity of Americium mononitride from 373 to 1473K

## As-Au-Ce
- rank 2503 | 1 samples | 1 papers | 1 compositions
- compositions: CeAuAs2 (1)
- measured range: 14-347 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeAs2Au P4/nmm (129) mp-1226657 [hull=0.000, PRIMARY]
- papers: Intriguing magnetic and electrical transport behavior in novel CeTAs2 (T=Cu, Ag, Au) compounds

## As-B-F-H
- rank 2504 | 1 samples | 1 papers | 1 compositions
- compositions: (BTBT)2AsF6 (1)
- measured range: 101-300 K (5th-95th pct of 4 curves)
- papers: Low-temperature properties of thermoelectric generators using molecular conductors

## As-Ba
- rank 2505 | 1 samples | 1 papers | 1 compositions
- compositions: Ba0.85La0.15As2 (1)
- dopant candidates (<5% at.): La (1)
- measured range: 14-269 K (5th-95th pct of 1 curves)
- [ref 1] TEDesignLab / ICSD: BaAs2 Pc (7) mp-31243 [hull=0.000, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ba2As I4/mmm (139) mp-2768 [hull=0.079, icsd=2, PRIMARY]; Ba5As3 P6_3/mcm (193) mp-10045 [hull=0.008, icsd=1, PRIMARY]; Ba3As14 P2_1/c (14) mp-524 [hull=0.000, icsd=1, PRIMARY]; BaAs3 C2/m (12) mp-15325 [hull=0.000, icsd=1, PRIMARY]; Ba20As13 Fdd2 (43) mp-685008 [hull=0.000, PRIMARY]
- papers: Transport properties and superconductivity in Ba1-xMxFe2As2(M=La and K) with double FeAs layers

## As-Ba-Cr-O-Ti
- rank 2506 | 1 samples | 1 papers | 1 compositions
- compositions: Ba2Ti2Cr2As4O (1)
- measured range: 21-384 K (5th-95th pct of 1 curves)
- papers: Synthesis, crystal structure and physical properties of a new oxypnictide Ba2Ti2Cr2As4O containing [Ti2As2O]2− and [Cr2As2]2− layers

## As-Bi-Te-Tl
- rank 2507 | 1 samples | 1 papers | 1 compositions
- compositions: As5.26Bi31.57Se2.63Te55.26Tl5.26 (1)
- dopant candidates (<5% at.): Se (1)
- measured range: 123-310 K (5th-95th pct of 1 curves)
- papers: Thermoelectric Properties of Diphasal Systems Combining As2Te3 and Tl2Se with Sb2Te3, Bi2Te3, or Sb2Se3

## As-Ca-Fe-O-Sc-Ti
- rank 2508 | 1 samples | 1 papers | 1 compositions
- compositions: (Fe2As2)Ca5(Sc0.5Ti0.5)4O11 (1)
- measured range: 12-296 K (5th-95th pct of 4 curves)
- papers: Thermoelectric properties of FeAs based superconductors, with thick perovskite- and Sm-O fluorite-type blocking layers

## As-Cd-Eu-Sb
- rank 2509 | 1 samples | 1 papers | 1 compositions
- compositions: Eu11Cd6Sb10As2 (1)
- measured range: 296-778 K (5th-95th pct of 4 curves)
- papers: High-Temperature Thermoelectric Properties of the Solid–Solution Zintl Phase Eu11Cd6Sb12–xAsx(x< 3)

## As-Cd-Na
- rank 2510 | 1 samples | 1 papers | 1 compositions
- compositions: NaCd4As3 (1)
- measured range: 12-298 K (5th-95th pct of 2 curves; full span incl. outliers 12-351 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NaCdAs Pnma (62) mp-7378 [hull=0.000, icsd=2, PRIMARY]; NaCd4As3 R-3m (166) mp-1078578 [hull=0.000, icsd=1, PRIMARY]
- papers: Eight-Coordinated Arsenic in the Zintl Phases RbCd4As3and RbZn4As3: Synthesis and Structural Characterization

## As-Ce-Co-Fe-O
- rank 2511 | 1 samples | 1 papers | 1 compositions
- compositions: CeFe0.8Co0.2AsO (1)
- measured range: 20-289 K (5th-95th pct of 1 curves)
- papers: Effects of Co doping on the transport properties and superconductivity in CeFe1 −xCoxAsO

## As-Ce-Cu
- rank 2512 | 1 samples | 1 papers | 1 compositions
- compositions: CeCuAs2 (1)
- measured range: 10-287 K (5th-95th pct of 1 curves)
- papers: Intriguing magnetic and electrical transport behavior in novel CeTAs2 (T=Cu, Ag, Au) compounds

## As-Ce-Fe
- rank 2513 | 1 samples | 1 papers | 1 compositions
- compositions: CeFe4As12 (1)
- measured range: 284-875 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(FeAs3)4 Im-3 (204) mp-1021509 [hull=0.000, icsd=1, PRIMARY]
- papers: Preparation and thermoelectric properties of CeFe4As12

## As-Co-Fe-O-Sm
- rank 2514 | 1 samples | 1 papers | 1 compositions
- compositions: SmFe0.7Co0.3AsO (1)
- measured range: 10-296 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sm4Fe3Co(AsO)4 P-4m2 (115) mp-1219165 [hull=0.184, PRIMARY]; Sm4Fe3Co(AsO)4 P-42m (111) mp-1219200 [hull=0.218]
- papers: Effect of Co-doping on the resistivity and thermopower of SmFe1-xCoxAsO (0.0≤x≤0.3)

## As-Co-Gd-O
- rank 2515 | 1 samples | 1 papers | 1 compositions
- compositions: GdCo0.95Fe0.05AsO (1)
- dopant candidates (<5% at.): Fe (1)
- measured range: 11-40 K (5th-95th pct of 1 curves)
- papers: Magnetocrystalline anisotropic effect in<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:mrow><mml:msub><mml:mi>GdCo</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mo>−</mml:mo><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Fe</mml:mi><mml:mi>x</mml:mi></mml:msub><mml:mi>AsO</mml:mi><mml:mspace width=\"0.16em\" /><mml:mrow><mml:mo>(</mml:mo><mml:mi>x</mml:mi><mml:mo>=</mml:mo><mml:mn>0</mml:mn><mml:mo>,</mml:mo><mml:mn>0.05</mml:mn><mml:mo>)</mml:mo></mml:mrow></mml:mrow></mml:math>

## As-Co-O-Sc-Sr
- rank 2516 | 1 samples | 1 papers | 1 compositions
- compositions: Sr4Sc2O6Co2As2 (1)
- measured range: 14-295 K (5th-95th pct of 1 curves)
- papers: Structure and physical properties of the new layered oxypnictides Sr4Sc2O6M2As2(M=Fe and Co)

## As-Cr
- rank 2517 | 1 samples | 1 papers | 1 compositions
- compositions: CrAs (1)
- measured range: 10-349 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CrAs Pnma (62) mp-20717 [hull=0.000, icsd=11, PRIMARY]; Cr2As P4/nmm (129) mp-20552 [hull=0.077, icsd=7, PRIMARY]; CrAs2 C2/m (12) mp-15681 [hull=0.003, icsd=1, PRIMARY]; Cr4As3 C2/m (12) mp-28704 [hull=0.051, icsd=1, PRIMARY]; Cr15As7 Amm2 (38) mp-1227256 [hull=0.157, PRIMARY]
- papers: Giant Negative Thermal Expansion in Antiferromagnetic \n<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\" display=\"inline\" overflow=\"scroll\"><mml:mrow><mml:mi>Cr</mml:mi><mml:mi>As</mml:mi></mml:mrow></mml:math>\n-Based Compounds

## As-Cr-O-Sr
- rank 2518 | 1 samples | 1 papers | 1 compositions
- compositions: Sr2Cr3As2O2 (1)
- measured range: 11-294 K (5th-95th pct of 1 curves)
- papers: Physical properties and electronic structure ofSr2Cr3As2O2containingCrO2andCr2As2square-planar lattices

## As-Cu-Fe-S
- rank 2519 | 1 samples | 1 papers | 1 compositions
- compositions: Cu10.5Fe1.5As3.6Sb0.4S13 (1)
- dopant candidates (<5% at.): Sb (1)
- measured range: 301-667 K (5th-95th pct of 3 curves)
- papers: High Performance Thermoelectricity in Earth-Abundant Compounds Based on Natural Mineral Tetrahedrites

## As-Cu-S
- rank 2520 | 1 samples | 1 papers | 1 compositions
- compositions: Cu9.95Ag0.04Zn1.44Fe0.47Sb0.80As3.23S13.07 (1)
- dopant candidates (<5% at.): Zn (1), Sb (1), Fe (1), Ag (1)
- measured range: 300-719 K (5th-95th pct of 4 curves; full span incl. outliers 300-773 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu3AsS4 Pmn2_1 (31) mp-3345 [hull=0.000, icsd=5, PRIMARY]; CuAsS Pnma (62) mp-5305 [hull=0.000, icsd=3, PRIMARY]; Cu6As4S9 P1 (1) mp-28717 [hull=0.000, icsd=2, PRIMARY]; VCu13As3S16 P-43n (218) mp-1202812 [hull=0.014, icsd=1, PRIMARY]; Cu12As4S13 P1 (1) mp-1225920 [hull=0.002, PRIMARY]
- papers: Electrical, Thermal, and Magnetic Characterization of Natural Tetrahedrites–Tennantites of Different Origin

## As-Cu-S-Sb-Zn
- rank 2521 | 1 samples | 1 papers | 1 compositions
- compositions: Cu9.85Ag0.10Zn1.79Fe0.11Sb1.57As2.48S13.09 (1)
- dopant candidates (<5% at.): Fe (1), Ag (1)
- measured range: 298-716 K (5th-95th pct of 4 curves; full span incl. outliers 298-775 K)
- papers: Electrical, Thermal, and Magnetic Characterization of Natural Tetrahedrites–Tennantites of Different Origin

## As-Er-Ni-Sb
- rank 2522 | 1 samples | 1 papers | 1 compositions
- compositions: ErNiSb0.8As0.2 (1)
- measured range: 47-287 K (5th-95th pct of 1 curves)
- papers: Observed Properties and Electronic Structure of RNiSb Compounds (R = Ho, Er, Tm, Yb and Y). Potential Thermoelectric Materials

## As-Eu-Ni
- rank 2523 | 1 samples | 1 papers | 1 compositions
- compositions: EuNi5As3 (1)
- measured range: 12-295 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Eu(NiAs)2 I4/mmm (139) mp-6992 [hull=0.000, icsd=1, PRIMARY]; EuNi5As3 Cmcm (63) mp-16838 [hull=0.000, icsd=1, PRIMARY]
- papers: Antiferromagnetism with divalent Eu in \n<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:mrow><mml:msub><mml:mi>EuNi</mml:mi><mml:mn>5</mml:mn></mml:msub><mml:msub><mml:mi>As</mml:mi><mml:mn>3</mml:mn></mml:msub></mml:mrow></mml:math>

## As-Eu-Sn
- rank 2524 | 1 samples | 1 papers | 1 compositions
- compositions: Eu5Sn2As6 (1)
- measured range: 294-724 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Eu5(SnAs3)2 Pbam (55) mp-1194194 [hull=0.000, icsd=1, PRIMARY]
- papers: A5Sn2As6(A = Sr, Eu). Synthesis, Crystal and Electronic Structure, and Thermoelectric Properties

## As-F-Fe-O-Sm-Te
- rank 2525 | 1 samples | 1 papers | 1 compositions
- compositions: Sm4Fe2As2Te0.72O3.8F1.2 (1)
- measured range: 11-302 K (5th-95th pct of 1 curves)
- papers: Upper critical field, pressure-dependent superconductivity and electronic anisotropy of Sm<sub>4</sub>Fe<sub>2</sub>As<sub>2</sub>Te<sub>1−<i>x</i></sub>O<sub>4−<i>y</i></sub>F<sub><i>y</i></sub>

## As-Fe-Gd-O
- rank 2526 | 1 samples | 1 papers | 1 compositions
- compositions: GdFeAsO (1)
- measured range: 82-304 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdFeAsO P4/nmm (129) mp-1078679 [hull=0.172, icsd=7, PRIMARY]
- papers: Thermoelectric power of RFeAsO (R=Ce, Pr, Nd, Sm and Gd)

## As-Fe-N-Th
- rank 2527 | 1 samples | 1 papers | 1 compositions
- compositions: ThFeAsN0.92O0.08 (1)
- dopant candidates (<5% at.): O (1)
- measured range: 11-35 K (5th-95th pct of 1 curves)
- papers: Peculiar phase diagram with isolated superconducting regions in ThFeAsN<sub>1−<i>x</i> </sub>O<sub> <i>x</i> </sub>

## As-Fe-Nd-O-Rh
- rank 2528 | 1 samples | 1 papers | 1 compositions
- compositions: NdFe0.8Rh0.2AsO (1)
- measured range: 18-303 K (5th-95th pct of 1 curves)
- papers: Electronic phase diagram ofNdFe1−xRhxAsO

## As-Fe-O-Pr
- rank 2529 | 1 samples | 1 papers | 1 compositions
- compositions: PrFeAsO (1)
- measured range: 78-307 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrFeAsO P4/nmm (129) mp-1079608 [hull=0.134, icsd=8, PRIMARY]; Pr2FeAs2O P4/mmm (123) mp-1209715 [hull=1.545, PRIMARY]
- papers: Thermoelectric power of RFeAsO (R=Ce, Pr, Nd, Sm and Gd)

## As-Fe-O-Pr-Te
- rank 2530 | 1 samples | 1 papers | 1 compositions
- compositions: Pr4Fe2As2TeO4 (1)
- measured range: 25-301 K (5th-95th pct of 1 curves)
- papers: Magnetotransport studies of superconducting<mml:math xmlns:mml=\"http://www.w3.org/1998/Math/MathML\"><mml:mrow><mml:mi mathvariant=\"normal\">P</mml:mi><mml:msub><mml:mi mathvariant=\"normal\">r</mml:mi><mml:mn>4</mml:mn></mml:msub><mml:mi mathvariant=\"normal\">F</mml:mi><mml:msub><mml:mi mathvariant=\"normal\">e</mml:mi><mml:mn>2</mml:mn></mml:msub><mml:mi mathvariant=\"normal\">A</mml:mi><mml:msub><mml:mi mathvariant=\"normal\">s</mml:mi><mml:mn>2</mml:mn></mml:msub><mml:mi mathvariant=\"normal\">T</mml:mi><mml:msub><mml:mi mathvariant=\"normal\">e</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mo>−</mml:mo><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi mathvariant=\"normal\">O</mml:mi><mml:mn>4</mml:mn></mml:msub></mml:mrow></mml:math>

## As-Fe-O-Sc-Sr
- rank 2531 | 1 samples | 1 papers | 1 compositions
- compositions: Sr4Sc2O6Fe2As2 (1)
- measured range: 10-295 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr3Sc2Fe2As2O5 I4/mmm (139) mp-1103895 [hull=0.070, icsd=3, PRIMARY]; Sr2ScFeAsO3 P4/nmm (129) mp-1105960 [hull=0.049, icsd=1, PRIMARY]
- papers: Structure and physical properties of the new layered oxypnictides Sr4Sc2O6M2As2(M=Fe and Co)

## As-Ge-Ni
- rank 2532 | 1 samples | 1 papers | 1 compositions
- compositions: Ni4As9.1Ge2.9 (1)
- measured range: 10-281 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ni4(GeAs3)3 Cm (8) mp-1220089 [hull=0.025, PRIMARY]
- papers: Crystal structure and thermoelectric properties of novel skutterudites Ep/sub y/Ni/sub 4/Sb/sub 12-x/Sn/sub x/ with Ep=Sn, Eu and Yb

## As-Ge-Se
- rank 2533 | 1 samples | 1 papers | 1 compositions
- compositions: As14Ge14Se69Sb3 (1)
- dopant candidates (<5% at.): Sb (1)
- measured range: 401-450 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GeAsSe Pnna (52) mp-29249 [hull=0.000, icsd=1, PRIMARY]
- papers: Semiconducting quaternary chalcogenide glasses as new potential thermoelectric materials: an As–Ge–Se–Sb case

## As-La-Lu
- rank 2534 | 1 samples | 1 papers | 1 compositions
- compositions: La0.15Lu0.85As (1)
- measured range: 21-302 K (5th-95th pct of 1 curves)
- papers: Temperature dependence of the electrical resistivity of La<sub>x</sub>Lu<sub>1-x</sub>As

## As-Mo-Ti
- rank 2535 | 1 samples | 1 papers | 1 compositions
- compositions: Ti0.9Mo1.1As4 (1)
- measured range: 221-296 K (5th-95th pct of 2 curves; full span incl. outliers 221-548 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti3MoAs4 P-3m1 (164) mp-1217100 [hull=0.064, PRIMARY]; TiMoAs2 Pmc2_1 (26) mp-1216734 [hull=0.018, PRIMARY]
- papers: Crystal Structure, Electronic Structure, and Physical Properties of Ti1-δMo1+δAs4and Ti1-δMo1+δSb4

## As-Nb
- rank 2536 | 1 samples | 1 papers | 1 compositions
- compositions: NbAs (1)
- measured range: 14-303 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NbAs I4_1md (109) mp-2059 [hull=0.000, icsd=3, PRIMARY]; Nb5As3 Pnma (62) mp-623038 [hull=0.000, icsd=2, PRIMARY]; NbAs2 C2/m (12) mp-7598 [hull=0.000, icsd=2, PRIMARY]; Nb2As Pmma (51) mp-1200152 [hull=0.000, icsd=1, PRIMARY]; Nb7As4 C2/m (12) mp-1191483 [hull=0.006, icsd=1, PRIMARY]
- papers: Properties of binary transition-metal arsenides (TAs)

## As-Nd-O-Pd
- rank 2537 | 1 samples | 1 papers | 1 compositions
- compositions: Nd10Pd3As8O10 (1)
- measured range: 11-295 K (5th-95th pct of 1 curves)
- papers: Palladium pnictide oxides Nd<sub>10</sub>Pd<sub>3</sub>As<sub>8</sub>O<sub>10</sub>and Sm<sub>10</sub>Pd<sub>3</sub>As<sub>8</sub>O<sub>10</sub>– low temperature structural phase transition and physical properties

## As-Ni
- rank 2538 | 1 samples | 1 papers | 1 compositions
- compositions: NiAs (1)
- measured range: 11-303 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NiAs P6_3/mmc (194) mp-590 [hull=0.004, icsd=11, PRIMARY]; NiAs2 Pnnm (58) mp-19814 [hull=0.000, icsd=7, PRIMARY]; Ni5As2 P6_3cm (185) mp-941 [hull=0.000, icsd=4, PRIMARY]; Ni11As8 P4_12_12 (92) mp-28227 [hull=0.000, icsd=1, PRIMARY]; Ni3As P6_3/mmc (194) mp-976930 [hull=0.077, PRIMARY]
- papers: Properties of binary transition-metal arsenides (TAs)

## As-Os
- rank 2539 | 1 samples | 1 papers | 1 compositions
- compositions: OsAs2 (1)
- measured range: 303-476 K (5th-95th pct of 2 curves; full span incl. outliers 303-695 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): As2Os Pnnm (58) mp-2455 [hull=0.000, icsd=5, PRIMARY]
- papers: Crystal Growth and Characterization of the Narrow-Band-Gap Semiconductors OsPn2(Pn = P, As, Sb)

## As-Os-Pr
- rank 2540 | 1 samples | 1 papers | 1 compositions
- compositions: PrOs4As12 (1)
- measured range: 10-313 K (5th-95th pct of 1 curves)
- papers: Crystal structure, 139La NMR and transport properties of the As-based filled skutterudites LaOs4As12 and PrOs4As12

## As-Rb-Zn
- rank 2541 | 1 samples | 1 papers | 1 compositions
- compositions: RbZn4As3 (1)
- measured range: 97-292 K (5th-95th pct of 2 curves; full span incl. outliers 97-349 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Rb2Zn5As4 Cmcm (63) mp-1192151 [hull=0.000, icsd=1, PRIMARY]; Rb4(ZnAs)7 Cmcm (63) mp-1199025 [hull=0.085, icsd=1, PRIMARY]; RbZn4As3 P4/mmm (123) mp-975144 [hull=0.000, icsd=1, PRIMARY]
- papers: Eight-Coordinated Arsenic in the Zintl Phases RbCd4As3and RbZn4As3: Synthesis and Structural Characterization

## As-Ru
- rank 2542 | 1 samples | 1 papers | 1 compositions
- compositions: RuAs (1)
- measured range: 12-304 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): As2Ru Pnnm (58) mp-766 [hull=0.000, icsd=4, PRIMARY]; AsRu Pnma (62) mp-15650 [hull=0.033, icsd=2, PRIMARY]
- papers: Properties of binary transition-metal arsenides (TAs)

## As-Sb-Te-Tl
- rank 2543 | 1 samples | 1 papers | 1 compositions
- compositions: As5.26Sb31.58Se2.63Te55.26Tl5.26 (1)
- dopant candidates (<5% at.): Se (1)
- measured range: 119-334 K (5th-95th pct of 1 curves)
- papers: Thermoelectric Properties of Diphasal Systems Combining As2Te3 and Tl2Se with Sb2Te3, Bi2Te3, or Sb2Se3

## As-Sc
- rank 2544 | 1 samples | 1 papers | 1 compositions
- compositions: ScAs (1)
- measured range: 10-303 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ScAs Fm-3m (225) mp-2052 [hull=0.000, icsd=5, PRIMARY]; Sc3As2 Pnma (62) mp-1188926 [hull=0.002, icsd=2, PRIMARY]; Sc3As P6_3/mmc (194) mp-1186963 [hull=0.253, PRIMARY]; Sc7As3 I4/mcm (140) mp-1219422 [hull=0.005, PRIMARY]; ScAs Pm-3m (221) mp-12982 [hull=0.483, icsd=2]
- papers: Properties of binary transition-metal arsenides (TAs)

## As-Se-Te-Tl
- rank 2545 | 1 samples | 1 papers | 1 compositions
- compositions: As11.76Se23.53Te17.65Tl47.06 (1)
- measured range: 125-318 K (5th-95th pct of 1 curves)
- papers: Thermoelectric Properties of Diphasal Systems Combining As2Te3 and Tl2Se with Sb2Te3, Bi2Te3, or Sb2Se3

## As-Ta
- rank 2546 | 1 samples | 1 papers | 1 compositions
- compositions: TaAs (1)
- measured range: 14-304 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TaAs I4_1md (109) mp-1936 [hull=0.000, icsd=3, PRIMARY]; Ta2As Pnnm (58) mp-672222 [hull=0.014, icsd=2, PRIMARY]; Ta5As4 I4/m (87) mp-8312 [hull=0.000, icsd=2, PRIMARY]; TaAs2 C2/m (12) mp-12561 [hull=0.000, icsd=2, PRIMARY]; Ta3As C2/c (15) mp-30523 [hull=0.000, icsd=1, PRIMARY, AMBIGUOUS]
- papers: Properties of binary transition-metal arsenides (TAs)

## As-Te-Tl
- rank 2547 | 1 samples | 1 papers | 1 compositions
- compositions: As34.78Se4.35Te52.17Tl8.7 (1)
- dopant candidates (<5% at.): Se (1)
- measured range: 113-327 K (5th-95th pct of 1 curves)
- papers: Thermoelectric Properties of Diphasal Systems Combining As2Te3 and Tl2Se with Sb2Te3, Bi2Te3, or Sb2Se3

## As-Th-U
- rank 2548 | 1 samples | 1 papers | 1 compositions
- compositions: (Th0.85U0.15)3As4 (1)
- measured range: 14-292 K (5th-95th pct of 1 curves)
- papers: Electronic properties of Th3As4U3As4 solid solutions

## As-Ti
- rank 2549 | 1 samples | 1 papers | 1 compositions
- compositions: TiAs (1)
- measured range: 15-304 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TiAs P6_3/mmc (194) mp-1822 [hull=0.000, icsd=4, PRIMARY]; TiAs2 Pnnm (58) mp-604647 [hull=0.000, icsd=2, PRIMARY]; Ti3As Pm-3n (223) mp-12071 [hull=0.026, icsd=1, PRIMARY]; Ti5As3 P6_3/mcm (193) mp-1208252 [hull=0.000, PRIMARY]; TiAs3 P6_3/mmc (194) mp-1187559 [hull=0.430, PRIMARY]
- papers: Properties of binary transition-metal arsenides (TAs)

## As-V
- rank 2550 | 1 samples | 1 papers | 1 compositions
- compositions: VAs (1)
- measured range: 12-306 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): VAs Pnma (62) mp-19940 [hull=0.000, icsd=5, PRIMARY]; V3As Pm-3n (223) mp-292 [hull=0.000, icsd=2, PRIMARY]; V5As3 I4/mcm (140) mp-7022 [hull=0.044, icsd=1, PRIMARY]; V4As3 C2/m (12) mp-2623 [hull=0.020, icsd=1, PRIMARY]; VAs2 C2/m (12) mp-1072660 [hull=0.000, icsd=1, PRIMARY]
- papers: Properties of binary transition-metal arsenides (TAs)
