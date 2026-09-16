# Host systems -- chunk 010 of 73

Ranks 451-500 by sample count. These 50 host systems cover 732 samples (1.41% of the TE set); cumulative through this chunk: 80.50%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Pb-Se-Sn
- rank 451 | 16 samples | 5 papers | 16 compositions
- compositions: Pb0.854Sn0.15Se0.998Cl0.002 (1); Sn0.88Pb0.12Na0.01Se (1); Sn0.84Pb0.16Na0.01Se (1); Sn0.8Pb0.2Na0.01Se (1); Sn0.85Pb0.15Se (1); Sn0.9Pb0.1Se (1)
- dopant candidates (<5% at.): Cl (6), Na (5), Br (2)
- solid-solution axis: Pb/(Pb+Sn) spans 0.10-0.85 (median 0.16) over 16 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 296-925 K (5th-95th pct of 79 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sn2PbSe3 P-3m1 (164) mp-1219016 [hull=0.004, PRIMARY]; SnPb4Se5 R-3m (166) mp-1218958 [hull=0.000, PRIMARY]; SnPbSe2 R-3m (166) mp-1218938 [hull=0.004, PRIMARY]
- papers: https://doi.org/10.1039/c4cp06021k (Electrical and thermal transport properties of Pb1−xSnxSe solid soluti...) | https://doi.org/10.1063/1.4975603 (Thermoelectric transport properties of polycrystalline SnSe alloyed wi...) | https://doi.org/10.1021/jacs.7b05881 (Enhancing p-Type Thermoelectric Performances of Polycrystalline SnSe v...)

## Pd
- rank 452 | 16 samples | 5 papers | 14 compositions
- compositions: Pd (3); Pd0.97Ce0.03 (1); Pd0.97Ce0.03H0.05 (1); Fe0.001Pd (1); Fe0.0004Pd (1); Fe0.0002Pd (1)
- dopant candidates (<5% at.): Fe (4), Ru (4), Rh (3), Ce (2), H (1)
- measured range: 10-297 K (5th-95th pct of 12 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Pd Fm-3m (225) mp-2 [hull=0.000, icsd=20, PRIMARY]; Pd P6_3/mmc (194) mp-1186427 [hull=0.010]
- papers: https://doi.org/10.1016/s0925-8388(00)01507-3 (Thermoelectric power of hydrogenated palladium and some of its dilute ...) | https://doi.org/10.1007/bf00655139 (Thermoelectric power of palladium-iron alloys at Millikelvin temperatures) | https://doi.org/10.1007/bf00661543 (Electron transport properties of palladium-ruthenium alloys from 50 mK...)

## S-Sm
- rank 453 | 16 samples | 3 papers | 10 compositions
- compositions: SmS (7); SmS1.375 (1); SmS1.333 (1); SmS1.501 (1); SmS1.414 (1); SmS1.355 (1)
- seed hypothesis (confirm): rocksalt
- measured range: 11-999 K (5th-95th pct of 22 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SmS Fm-3m (225) mp-1269 [hull=0.000, icsd=21, PRIMARY]; Sm3S4 I-43d (220) mp-2038 [hull=0.042, icsd=7, PRIMARY]; Sm2S3 Pnma (62) mp-1403 [hull=0.000, icsd=4, PRIMARY]; Sm10S19 P4_2/n (86) mp-10534 [hull=0.000, icsd=1, PRIMARY]; Sm39S56 P1 (1) mp-684860 [hull=0.024, PRIMARY]
- papers: https://doi.org/10.1023/b:inma.0000008909.13771.f3 (Thermoelectric Properties of SmSx(x = 0.8–1.5)) | https://doi.org/10.1016/0304-8853(87)90681-0 (Resistivity and thermoelectric power of single crystals of semiconduct...) | https://doi.org/10.1143/jpsjs.80sa.sa077 (Thermoelectric Power Investigation on SmS)

## Ag-Ca-Ce-Sb
- rank 454 | 15 samples | 2 papers | 14 compositions
- compositions: Ca0.84Ce0.16Ag0.85Sb (2); CaCeAgSb (1); Ca0.84Ce0.16Ag0.86Sb (1); Ca0.84Ce0.16Ag0.9Sb (1); Ca0.84Ce0.16Ag0.89Sb (1); Ca0.84Ce0.16Ag0.87Sb (1)
- measured range: 303-1082 K (5th-95th pct of 65 curves)
- papers: https://doi.org/10.1021/ja403653m (Ca1–xRExAg1–ySb (RE = La, Ce, Pr, Nd, Sm; 0 ≤x≤1; 0 ≤y≤1): Interesting...) | https://doi.org/10.1021/acs.chemmater.7b00716 (Defect Chemistry, Phase Transitions, and Thermoelectric Properties of ...)

## Ag-Ga-Te
- rank 455 | 15 samples | 6 papers | 11 compositions
- compositions: AgGaTe2 (4); Ag9GaTe6 (2); Ag0.99GaTe2 (1); Ag0.97GaTe2 (1); Ag0.95GaTe2 (1); AgGa0.95Cu0.05Te2 (1)
- dopant candidates (<5% at.): Cu (2), Zn (1), Mg (1), Cd (1), Nb (1)
- seed hypothesis (confirm): chalcopyrite
- measured range: 300-867 K (5th-95th pct of 65 curves)
- [ref 1] TEDesignLab / ICSD: GaAgTe2 I-42d (122) mp-4899 [hull=0.000, icsd=7, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ga12Ag2Te19 P1 (1) mp-675033 [hull=0.055, PRIMARY]; GaAgTe2 P-4m2 (115) mp-1224790 [hull=0.033]
- papers: https://doi.org/10.1063/1.3617458 (Thermoelectric properties of Ag1−xGaTe2 with chalcopyrite structure) | https://doi.org/10.2497/jjspm.59.206 (Effect of Cu Doping into the Ga Site on the Thermoelectric Properties ...) | https://doi.org/10.7567/jjap.52.081801 (Thermoelectric Properties of Chalcopyrite-Type CuGaTe2with Ag Substitu...)

## Al-In-N
- rank 456 | 15 samples | 5 papers | 12 compositions
- compositions: Al0.35In0.65N (4); Al0.16In0.84N (1); Al0.55In0.45N (1); Al0.28In0.72N (1); Al0.57In0.43N (1); In0.19Al0.81N (1)
- solid-solution axis: Al/(Al+In) spans 0.12-0.83 (median 0.55) over 12 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 200-869 K (5th-95th pct of 27 curves)
- papers: https://doi.org/10.1063/1.1560560 (Thermoelectric properties of Al1−xInxN and Al1−y−zGayInzN prepared by ...) | https://doi.org/10.1063/1.1637156 (Thermal diffusivity and thermoelectric figure of merit of Al1−xInxN pr...) | https://doi.org/10.1063/1.4759287 (Thermoelectric properties of lattice matched InAlN on semi-insulating ...)

## Au
- rank 457 | 15 samples | 4 papers | 11 compositions
- compositions: Au (5); Au96.5Mn3.5 (1); Au96.99Pd3.01 (1); Au96.01Pd3.99 (1); Au98.99Pt1.01 (1); Au97.98Pt2.02 (1)
- dopant candidates (<5% at.): Pd (5), Pt (4), Mn (1)
- seed hypothesis (confirm): solid_solution_alloy
- measured range: 10-972 K (5th-95th pct of 28 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Au Fm-3m (225) mp-81 [hull=0.000, icsd=15, PRIMARY]; Au P6_3/mmc (194) mp-1008634 [hull=0.003, icsd=1]
- papers: https://doi.org/10.1063/1.1722342 (Thermoelectric Power and Electrical Resistivity of Dilute Alloys of Mn...) | https://doi.org/10.1063/1.1729605 (Effects of Transition Metal Solutes on the Thermoelectric Power of Cop...) | https://doi.org/10.1063/1.353016 (Thin gold wires as reference for thermoelectric power measurements of ...)

## B-C-Si
- rank 458 | 15 samples | 4 papers | 10 compositions
- compositions: Si0.37B2.51C (4); B1.9Si0.53C (2); B1.08Si0.73C (2); Si0.76B0.95C (1); (Al2O3)0.02Si0.75B0.92C (1); (Al2O3)0.02Si0.36B2.44C (1)
- dopant candidates (<5% at.): Al (4), O (2)
- solid-solution axis: C/(C+Si) spans 0.50-0.74 (median 0.57) over 10 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 298-1178 K (5th-95th pct of 21 curves)
- papers: https://doi.org/10.1007/s11664-010-1129-0 (Preparation and Thermoelectric Characterization of SiC-B4C Composites) | https://doi.org/10.1016/s0955-2219(03)00213-9 (SiC–B4C composites for synergistic enhancement of thermoelectric property) | https://doi.org/10.2320/matertrans.mra2007232 (Thermoelectric Properties of Silicon Carbide Sintered with Addition of...)

## Ba-Ga-Ge-Zn
- rank 459 | 15 samples | 4 papers | 11 compositions
- compositions: Ba8Ga16Zn3.0Ge27.0 (2); Ba8Ga16Zn2.8Ge27.2 (2); Ba8Ga16Zn3.2Ge26.8 (2); Ba8Zn6Ga4Ge36 (2); Ba8Ga16.1Zn3Ge26.9 (1); Ba8Ga16.4Zn3Ge26.6 (1)
- seed hypothesis (confirm): clathrate_i
- measured range: 296-1042 K (5th-95th pct of 36 curves)
- papers: https://doi.org/10.1063/1.2769781 (Synthesis and thermoelectric properties of p-type Ba8Ga16ZnxGe30−x typ...) | https://doi.org/10.1007/s10853-008-3205-x (Effects of Ga content on thermoelectric properties of P-type Ba8Ga16+x...) | https://doi.org/10.2320/matertrans.e-mra2008846 (Study of Zn-Substituted Germanium Clathrates as High Performance Therm...)

## Ba-Nb-O
- rank 460 | 15 samples | 5 papers | 10 compositions
- compositions: Ba6Ti2Nb8O30 (4); BaNb2O6 (2); ((Nd)0.0099(Ca0.28Ba0.72)0.9901)Nb2O6 (2); BaNb2O6(TiC)0.25 (1); Sr0.25Ba0.75Nb2O6 (1); BaNb2O6(TiC)0.05 (1)
- dopant candidates (<5% at.): Ti (6), Sr (4), C (2), Ca (2), Nd (2)
- measured range: 11-1069 K (5th-95th pct of 37 curves)
- [ref 1] TEDesignLab / ICSD: BaNb2O6 P2_1/c (14) mp-28150 [hull=0.000, icsd=1, PRIMARY]; BaNb2O6 Pmma (51) mp-640553 [hull=0.037, icsd=1]
- [ref 2] MP, ranked by ICSD evidence: Ba2Nb5O9 P4/mmm (123) mp-19796 [hull=0.000, icsd=4, PRIMARY]; Ba2NaNb5O15 P4bm (100) mp-15983 [hull=0.015, icsd=2, PRIMARY]; BaNbO3 Pm-3m (221) mp-3020 [hull=0.000, icsd=2, PRIMARY]; Ba4Nb14O23 Cmmm (65) mp-4564 [hull=0.000, icsd=2, PRIMARY]; Ba5Nb4O15 P-3m1 (164) mp-3563 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1007/s00339-014-8515-z (Semiconducting large bandgap oxides as potential thermoelectric materi...) | https://doi.org/10.1016/j.scriptamat.2015.07.025 (Thermal conductivity and thermoelectric performance of SrxBa1−xNb2O6 c...) | https://doi.org/10.1063/1.5119962 (The structure and thermoelectric properties of tungsten bronze Ba6Ti2N...)

## Bi-I-Te
- rank 461 | 15 samples | 5 papers | 8 compositions
- compositions: BiTeI (4); Bi2(Se0.07Te0.93)3I0.4 (3); (BiTeI)97.62(CuI)2.38 (2); (BiTeI)99.22(BiI3)0.78 (2); (BiTeI)81.85(Bi)18.15 (1); (BiTeI)90.02(Bi)9.98 (1)
- dopant candidates (<5% at.): Se (3), Cu (2), Br (2)
- seed hypothesis (confirm): bitei_polar
- measured range: 15-570 K (5th-95th pct of 66 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BiTeI P3m1 (156) mp-22965 [hull=0.000, icsd=4, PRIMARY]; Bi2TeI R-3m (166) mp-23435 [hull=0.027, icsd=2, PRIMARY]
- papers: https://doi.org/10.1134/s1063782610120031 (Galvanomagnetic and thermoelectric properties of BiTeBr and BiTeI sing...) | https://doi.org/10.1134/s1063782611070128 (Thermoelectric properties of BiTeI with addition of BiI3, CuI, and ove...) | https://doi.org/10.3724/sp.j.1077.2010.00609 (Effects of Preparation Techniques on the Thermoelectric Properties and...)

## Ca-Fe-O-Sr
- rank 462 | 15 samples | 1 papers | 12 compositions
- compositions: Sr1.2Ca2.8Fe6O13 (3); Sr2.4Ca1.6Fe6O13 (2); Sr0.4Ca0.6FeO3 (1); Sr2Ca2Fe6O13 (1); Sr1.6Ca2.4Fe6O13 (1); Sr2.4Ca1.6Fe5.4Co0.6O13 (1)
- dopant candidates (<5% at.): Co (3), Mn (1), Ni (1), Cu (1)
- solid-solution axis: Ca/(Ca+Sr) spans 0.40-0.70 (median 0.60) over 12 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 309-1179 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr3Ca(Fe2O5)2 P1 (1) mp-1076761 [hull=0.005, PRIMARY]; Sr3Ca(FeO3)4 Pm (6) mp-1094055 [hull=0.015, PRIMARY, AMBIGUOUS]; Sr4Ca(FeO2)5 Cmmm (65) mp-1218462 [hull=0.030, PRIMARY]; Sr4Ca(FeO3)5 P4/m (83) mp-1218523 [hull=0.012, PRIMARY]; Sr5Ca3MnFe7O20 P1 (1) mp-1076199 [hull=0.018, PRIMARY]
- papers: https://doi.org/10.1006/jssc.1999.8261 (Synthesis, Crystal Chemistry, and Electrical Properties of the Intergr...)

## Ce-Cu-Ge
- rank 463 | 15 samples | 6 papers | 3 compositions
- compositions: CeCu2Ge2 (13); Ce2CuGe6 (1); Ce(Cu0.9Co0.1)2Ge2 (1)
- dopant candidates (<5% at.): Co (1)
- seed hypothesis (confirm): thcr2si2_122
- measured range: 10-302 K (5th-95th pct of 19 curves; full span incl. outliers 10-350 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeCuGe P6_3/mmc (194) mp-20766 [hull=0.000, icsd=4, PRIMARY]; Ce(CuGe)2 I4/mmm (139) mp-20173 [hull=0.000, icsd=3, PRIMARY]; Ce2CuGe6 Amm2 (38) mp-5684 [hull=0.013, icsd=1, PRIMARY]; Ce3(CuGe)4 Immm (71) mp-22623 [hull=0.000, icsd=1, PRIMARY]; CeCuGe2 Cmcm (63) mp-1080708 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2007.04.286 (Electric transport in R2MGe6 ternary compounds (R=La, Ce, Gd, Tb, Dy, ...) | https://doi.org/10.1016/0304-8853(87)90605-6 (Seebeck coefficient of heavy fermion compounds) | https://doi.org/10.1103/physrevb.98.165136 (Non-Fermi-liquid behavior at the antiferromagnetic quantum critical po...)

## Co-Gd-O
- rank 464 | 15 samples | 4 papers | 4 compositions
- compositions: GdCoO3 (5); Gd0.9Ca0.1CoO3 (5); Gd0.8Ca0.2CoO3 (3); GdCo0.95Ni0.05O3 (2)
- dopant candidates (<5% at.): Ca (8), Ni (2)
- measured range: 92-1169 K (5th-95th pct of 19 curves; full span incl. outliers 92-1231 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GdCoO3 Pm-3m (221) mp-24863 [hull=0.180, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.actamat.2007.05.020 (High-temperature thermoelectric properties of Ln(Co, Ni)O3 (Ln=La, Pr,...) | https://doi.org/10.1007/s11664-010-1214-4 (Synthesis and Characterization of New Ceramic Thermoelectrics Implemen...) | https://doi.org/10.1016/s0921-5107(01)00645-6 (Influence of ionic size of rare-earth site on the thermoelectric prope...)

## Co-Hf-Sb-Ti-Zr
- rank 465 | 15 samples | 6 papers | 14 compositions
- compositions: Ti0.5Zr0.25Hf0.25Co0.95Ni0.05Sb (2); In0.03Ti0.5Zr0.25Hf0.25Co0.95Ni0.05Sb1.03 (1); In0.01Ti0.5Zr0.25Hf0.25Co0.95Ni0.05Sb1.01 (1); In0.07Ti0.5Zr0.25Hf0.25Co0.95Ni0.05Sb1.07 (1); Ti0.5Zr0.25Hf0.25CoSb (1); Ti0.5Zr0.25Hf0.25Co0.99Ni0.01Sb (1)
- dopant candidates (<5% at.): Ni (7), Sn (4), In (3), Pd (1)
- solid-solution axis: Ti/(Ti+Zr) spans 0.31-0.67 (median 0.67) over 14 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 18-985 K (5th-95th pct of 63 curves)
- papers: https://doi.org/10.1016/j.actamat.2010.05.005 (Simultaneously optimizing the independent thermoelectric properties in...) | https://doi.org/10.1063/1.2885113 (The preparation and thermoelectric properties of Ti0.5Zr0.25Hf0.25Co1−...) | https://doi.org/10.1088/0022-3727/42/23/235407 (Synthesis and thermoelectric properties of (Ti,Zr,Hf)(Co,Pd)Sb half-He...)

## Co-Ho-O-Sr
- rank 466 | 15 samples | 3 papers | 6 compositions
- compositions: Ho0.33Sr0.67CoO2.71 (4); Ho0.33Sr0.67CoO2.80 (4); Ho0.33Sr0.67CoO2.67 (4); Sr1.65Ho0.35CoO3 (1); Sr1.6Ho0.4CoO3 (1); Ho0.35Sr0.65CoO3 (1)
- measured range: 10-394 K (5th-95th pct of 15 curves; full span incl. outliers 10-440 K)
- papers: https://doi.org/10.1103/physrevb.76.134407 (Structural, transport, and magnetic properties of the cation-ordered c...) | https://doi.org/10.1063/1.2834238 (Magnetic and transport and structure properties of the room temperatur...) | https://doi.org/10.1134/s1063783411040226 (Effect of the spin and valence states of cobalt ions on the kinetic pr...)

## Co-Sb-Ti-Zr
- rank 467 | 15 samples | 6 papers | 11 compositions
- compositions: Ti0.6Zr0.4CoSb (3); Ti0.8Zr0.2CoSb (2); Ti0.5Zr0.5CoSb (2); Ti0.6Zr0.4Co0.93Ni0.07Sb (1); Ti0.6Zr0.4Co0.97Ni0.03Sb (1); Zr0.5Ti0.5CoSn0.15Sb0.85 (1)
- dopant candidates (<5% at.): Ni (3), Sn (1), Pd (1), Hf (1)
- seed hypothesis (confirm): half_heusler
- solid-solution axis: Ti/(Ti+Zr) spans 0.30-0.80 (median 0.60) over 11 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 13-1000 K (5th-95th pct of 48 curves)
- papers: https://doi.org/10.1063/1.2896591 (Thermoelectric properties of p-type half-Heusler alloys Zr1−xTixCoSnyS...) | https://doi.org/10.1063/1.3238363 (Enhanced thermoelectric performance by the combination of alloying and...) | https://doi.org/10.1088/0022-3727/42/23/235407 (Synthesis and thermoelectric properties of (Ti,Zr,Hf)(Co,Pd)Sb half-He...)

## Cr-O
- rank 468 | 15 samples | 10 papers | 3 compositions
- compositions: CrO2 (12); Cr2O3 (2); (CrO2)0.9(SnO2)0.1 (1)
- dopant candidates (<5% at.): Sn (1)
- measured range: 10-477 K (5th-95th pct of 15 curves; full span incl. outliers 10-1273 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cr2O3 R-3c (167) mp-796301 [hull=0.000, icsd=55, PRIMARY]; CrO2 P4_2/mnm (136) mp-715486 [hull=0.000, icsd=33, PRIMARY]; BaCr10O15 Cmce (64) mp-19500 [hull=0.031, icsd=3, PRIMARY]; CrO Fm-3m (225) mp-19091 [hull=0.335, icsd=2, PRIMARY]; CrO3 Ama2 (40) mp-715566 [hull=0.043, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/j.msea.2004.11.009 (Thermal diffusivity of plasma-sprayed Cr3C2–NiCr coatings) | https://doi.org/10.1103/physrevb.15.4451 (Specific heat ofCr2O3near the Néel temperature) | https://doi.org/10.1103/physrevb.61.9621 (Evidence for two-band magnetotransport in half-metallic chromium dioxide)

## Cu-I
- rank 469 | 15 samples | 3 papers | 13 compositions
- compositions: CuI (3); CuCo0.001I (1); CuGa0.001I (1); CuSn0.001I (1); CuMn0.001I (1); CuTb0.001I (1)
- dopant candidates (<5% at.): Tb (5), Co (1), Ga (1), Sn (1), Mn (1), Fe (1), Zn (1), Mg (1)
- seed hypothesis (confirm): sphalerite
- measured range: 298-446 K (5th-95th pct of 51 curves; full span incl. outliers 293-1156 K)
- [ref 1] TEDesignLab / ICSD: CuI F-43m (216) mp-22895 [hull=0.006, icsd=12, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Cu13I15 Cm (8) mp-684621 [hull=0.013, PRIMARY]; Cu14I19 Cm (8) mp-685100 [hull=0.062, PRIMARY]; Cu16I19 Cm (8) mp-685158 [hull=0.015, PRIMARY]; CuI2 P4/mmm (123) mp-1147667 [hull=0.201, PRIMARY]; CuI4 I-42m (121) mp-33218 [hull=0.193, PRIMARY]
- papers: https://doi.org/10.1063/1.4788729 (Thermoelectric properties of molten Bi2Te3, CuI, and AgI) | https://doi.org/10.1016/j.solener.2020.02.091 (Use of biomass for a development of nanocellulose-based biodegradable ...) | https://doi.org/10.1016/j.ceramint.2020.07.209 (Effective dopants for CuI single nanocrystals as a promising room temp...)

## Cu-La-Ni-O
- rank 470 | 15 samples | 4 papers | 6 compositions
- compositions: (LaNiO3)(La2CuO4) (7); LaNi0.5Cu0.5O3 (2); LaNi0.7Cu0.3O3 (2); LaNi0.6Cu0.4O3 (2); LaNi0.4Cu0.6O3 (1); LaNi0.3Cu0.7O3 (1)
- measured range: 10-980 K (5th-95th pct of 20 curves; full span incl. outliers 10-1123 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La4CuNiO8 C2/m (12) mp-1223008 [hull=0.076, PRIMARY]
- papers: https://doi.org/10.1007/s13391-013-0034-0 (Thermoelectric properties of a doped LaNiO3 perovskite system prepared...) | https://doi.org/10.1021/acsami.8b02153 (High-Temperature Thermoelectricity in LaNiO3–La2CuO4 Heterostructures) | https://doi.org/10.4191/kcers.2015.52.5.344 (Lanthanum Nickelates with a Perovskite Structure as Protective Coating...)

## Eu-O
- rank 471 | 15 samples | 6 papers | 2 compositions
- compositions: EuO (9); Eu0.95Gd0.05O (6)
- dopant candidates (<5% at.): Gd (6)
- seed hypothesis (confirm): rocksalt
- measured range: 10-299 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): EuO Fm-3m (225) mp-21394 [hull=0.000, icsd=5, PRIMARY]; Eu2O3 C2/m (12) mp-647924 [hull=0.024, icsd=4, PRIMARY]; EuO2 P4/nmm (129) mp-1018700 [hull=0.095, icsd=1, PRIMARY]; EuO3 P6_3/m (176) mp-1206483 [hull=0.271, icsd=1, PRIMARY]; Eu3O4 Pnma (62) mp-1193398 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.8.2299 (EuO. I. Resistivity and Hall Effect in Fields up to 150 kOe) | https://doi.org/10.1016/0038-1098(72)90585-6 (Electrical conductivity in EuO films with large excess of europium) | https://doi.org/10.1103/physrevb.93.235201 (Magnetic and transport properties of degenerate ferromagnetic semicond...)

## Fe-La-Sb
- rank 472 | 15 samples | 8 papers | 2 compositions
- compositions: LaFe4Sb12 (14); La1.5Fe4Sb12 (1)
- measured range: 10-824 K (5th-95th pct of 38 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(FeSb3)4 Im-3 (204) mp-30073 [hull=0.000, icsd=2, PRIMARY]; LaFeSb2 P4/nmm (129) mp-1079119 [hull=0.116, icsd=2, PRIMARY]; La2Fe4Sb5 Cm (8) mp-1223457 [hull=0.101, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2006.07.114 (Band energy and thermoelectricity of filled skutterudites LaFe4Sb12 an...) | https://doi.org/10.3938/jkps.64.863 (ThE SYnthesis of R z Fe4−x Co x Sb12 (R: Yb, La, Ce) skutterudites and...) | https://doi.org/10.1016/j.matlet.2005.12.074 (Preparation and thermoelectric properties of La filled skutterudites b...)

## Gd-O-Zr
- rank 473 | 15 samples | 6 papers | 8 compositions
- compositions: Gd2Zr2O7 (8); (Gd2O3)48.5(ZrO2)51.5 (1); (Gd0.96Yb0.04)2Zr2O7 (1); (Gd0.94Yb0.06)2Zr2O7 (1); (Gd0.9Yb0.1)2Zr2O7 (1); (Gd0.98Yb0.02)2Zr2O7 (1)
- dopant candidates (<5% at.): Yb (5)
- seed hypothesis (confirm): pyrochlore
- measured range: 293-1473 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Gd2Zr2O7 Fd-3m (227) mp-757233 [hull=0.007, icsd=1, PRIMARY]; Gd8Zr7O26 C2/m (12) mp-676108 [hull=0.105, PRIMARY]; GdZrO3 Pm-3m (221) mp-1184599 [hull=0.401, PRIMARY]; Gd2Zr2O7 P2_1/c (14) mp-780342 [hull=0.081]; Gd2Zr2O7 Pmna (53) mp-35735 [hull=0.087]
- papers: https://doi.org/10.31349/revmexfis.67.255 (Electrical and thermal conductivities of rare-earth A2Zr2O7 (A = Pr, N...) | https://doi.org/10.1016/j.jnucmat.2007.03.266 (Characteristics of GdxMyOz (M=Ti, Zr or Al) as a burnable absorber) | https://doi.org/10.1016/j.ceramint.2015.06.090 (Structural evolution and thermal conductivities of (Gd1−xYbx)2Zr2O7 (x...)

## Ge-Sb-Se-Te
- rank 474 | 15 samples | 3 papers | 13 compositions
- compositions: Ge0.90Sb0.10Te0.88Se0.12 (3); (GeSe)0.92(Sb2Te3)0.08 (1); (GeSe)0.85(Sb2Te3)0.15 (1); Ge2Sb2Te4.5Se0.5 (1); (GeSe)0.9(Sb2Te3)0.1 (1); Ge2Sb2Te4Se (1)
- solid-solution axis: Se/(Se+Te) spans 0.10-0.79 (median 0.14) over 13 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 297-801 K (5th-95th pct of 64 curves)
- papers: https://doi.org/10.1016/j.jechem.2019.09.021 (Glass-like electronic and thermal transport in crystalline cubic germa...) | https://doi.org/10.1002/andp.201900390 (Effective Mass Enhancement and Thermal Conductivity Reduction for Impr...) | https://doi.org/10.1021/acs.chemmater.6b04066 (Realizing the High Thermoelectric Performance of GeTe by Sb-Doping and...)

## Nd-O-Sb-Zn
- rank 475 | 15 samples | 2 papers | 14 compositions
- compositions: NdOZnSb (2); Nd0.98Sr0.02OZnSb (1); Nd0.92Sr0.08OZnSb (1); Nd0.93Sr0.07OZnSb (1); Nd0.99Sr0.01OZnSb (1); Nd0.97Sr0.03OZnSb (1)
- dopant candidates (<5% at.): Sr (8), Ag (5)
- seed hypothesis (confirm): zrcusias_1111
- measured range: 323-725 K (5th-95th pct of 75 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NdZnSbO P4/nmm (129) mp-12516 [hull=0.000, icsd=2, PRIMARY]; Nd2ZnSb2O P4/mmm (123) mp-1209925 [hull=1.164, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2016.07.197 (Structure and thermoelectric performance of layered compounds Nd 1−x S...) | https://doi.org/10.1016/j.matlet.2016.11.073 (Influence of Ag doping on the thermoelectric properties of layered com...)

## Ni-Te
- rank 476 | 15 samples | 4 papers | 12 compositions
- compositions: Ni0.786Te (4); Ni3Te2 (1); NiTe (1); Ni2Te3 (1); NiTe2 (1); Ni32Te67 (1)
- dopant candidates (<5% at.): Sb (4)
- measured range: 92-601 K (5th-95th pct of 52 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NiTe P6_3/mmc (194) mp-203 [hull=0.004, icsd=8, PRIMARY]; NiTe2 P-3m1 (164) mp-2578 [hull=0.000, icsd=6, PRIMARY]; Ni3Te2 P2_1/m (11) mp-31103 [hull=0.000, icsd=1, PRIMARY]; Ni23Te42 P-1 (2) mp-684997 [hull=0.003, PRIMARY]; Ni3Te P6_3/mmc (194) mp-976953 [hull=0.152, PRIMARY]
- papers: https://doi.org/10.1016/0022-5088(86)90369-3 (The magnetic and thermoelectric properties of single-crystal Ni0.786Te) | https://doi.org/10.1039/c3ta13456c (Understanding of the contact of nanostructured thermoelectric n-type B...) | https://doi.org/10.1007/s11664-020-07956-8 (Effects of Ni Magnetic Nanoparticles on Thermoelectric Properties of n...)

## O-Pb-Ti-Zr
- rank 477 | 15 samples | 2 papers | 9 compositions
- compositions: Pb0.85La0.1(Zr0.65Ti0.35)O3 (2); Pb1.5La0.1(Zr0.65Ti0.35)O3 (2); Pb0.97La0.1(Zr0.65Ti0.35)O3 (2); Pb1.2La0.1(Zr0.65Ti0.35)O3 (2); Pb1.4La0.1(Zr0.65Ti0.35)O3 (2); Pb1.1La0.1(Zr0.65Ti0.35)O3 (2)
- dopant candidates (<5% at.): La (15), Mn (3), Ca (2), Sr (1)
- seed hypothesis (confirm): perovskite
- measured range: 14-373 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZrTi(PbO3)2 P4mm (99) mp-1079056 [hull=0.018, icsd=2, PRIMARY]; BaZr2Ti3Pb4O15 Pm (6) mp-1227980 [hull=0.027, PRIMARY]; Zr2Ti(PbO3)3 Cm (8) mp-1215944 [hull=0.026, PRIMARY, AMBIGUOUS]; Zr3Ti(PbO3)4 Pm (6) mp-1215936 [hull=0.028, PRIMARY, AMBIGUOUS]; Zr2Ti3(PbO3)5 Pmm2 (25) mp-1216039 [hull=0.025, PRIMARY]
- papers: https://doi.org/10.1111/jace.14984 (High electrocaloric effect in hot-pressed Pb<sub>0.85</sub>\nLa<sub>0....) | https://doi.org/10.1063/1.3592660 (Effect of PbZr0.52Ti0.48O3 thin layer on structure, electronic and mag...)

## P-Si-Te
- rank 478 | 15 samples | 3 papers | 13 compositions
- compositions: Si33P13Te8 (2); Si30P16Te8 (2); Si30.3P15.6Te6.6Se1.46 (1); Si132P40Te21.5 (1); Si32P14Te7 (1); Si30.3P15.6Te6.17Se1.88 (1)
- dopant candidates (<5% at.): Se (3), Br (1)
- measured range: 11-1097 K (5th-95th pct of 41 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Si60Te13P32Se3 Pmmm (47) mp-1219353 [hull=0.027, PRIMARY]
- papers: https://doi.org/10.1002/chem.201001990 (Bulk and Surface Structure and High-Temperature Thermoelectric Propert...) | https://doi.org/10.1021/ic3010097 (Homo- and Heterovalent Substitutions in the New Clathrates I Si30P16Te...) | https://doi.org/10.1143/jjap.46.l746 (Synthesis and Thermoelectric Properties of Type-I Clathrate Compounds ...)

## Ru-Si-U
- rank 479 | 15 samples | 7 papers | 2 compositions
- compositions: URu2Si2 (13); U2Ru3Si5 (2)
- seed hypothesis (confirm): thcr2si2_122
- measured range: 10-1084 K (5th-95th pct of 23 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U(SiRu)2 I4/mmm (139) mp-3388 [hull=0.000, icsd=12, PRIMARY]; U2Si5Ru3 C2/c (15) mp-1188211 [hull=0.000, icsd=1, PRIMARY]; USiRu Pnma (62) mp-1102216 [hull=0.000, icsd=1, PRIMARY]; U2Si3Ru P-3m1 (164) mp-1216891 [hull=0.028, PRIMARY]; U2Si7Ru12 Pnma (62) mp-1208764 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/0038-1098(95)00641-9 (Thermoelectric power on single crystals of URu2Si2) | https://doi.org/10.1016/0304-8853(93)90477-j (Transport and magnetic properties of U2M3Si5 silicides (M = Co, Rh, Ru)) | https://doi.org/10.1016/s0022-3115(01)00476-7 (Thermoelectric properties of URu2Si2 and U2Ru3Si5)

## Ag-As-Ce
- rank 480 | 14 samples | 2 papers | 1 compositions
- compositions: CeAgAs2 (14)
- measured range: 10-288 K (5th-95th pct of 14 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CeAgAs2 Pbcm (57) mp-672195 [hull=0.001, icsd=3, PRIMARY]; CeAgAs2 P4/nmm (129) mp-20384 [hull=0.000, icsd=1]; CeAgAs2 Cmce (64) mp-985705 [hull=0.000]
- papers: https://doi.org/10.1016/j.jallcom.2007.04.108 (Intriguing magnetic and electrical transport behavior in novel CeTAs2 ...) | https://doi.org/10.3390/ma13173865 (Antiferromagnetic Ordering and Transport Anomalies in Single-Crystalli...)

## Ag-Bi-Ge-Se-Te
- rank 481 | 14 samples | 1 papers | 14 compositions
- compositions: (GeTe)75(AgBiSe2)25 (1); (GeTe)50(AgBiSe2)50 (1); (GeTe)82.5(AgBiSe2)17.5 (1); (GeTe)65(AgBiSe2)35 (1); (GeTe)60(AgBiSe2)40 (1); (GeTe)50(AgBiSe1.995Cl0.005)50 (1)
- dopant candidates (<5% at.): Cl (1), I (1), Br (1)
- solid-solution axis: Se/(Se+Te) spans 0.21-0.82 (median 0.57) over 14 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 292-745 K (5th-95th pct of 47 curves)
- papers: https://doi.org/10.1021/jacs.9b11405 (Realization of Both n- and p-Type GeTe Thermoelectrics: Electronic Str...)

## Ag-Bi-S-Se
- rank 482 | 14 samples | 3 papers | 13 compositions
- compositions: BiAgSeS0.985Cl0.015 (2); BiAgSeS0.99Cl0.01 (1); BiAgSeS0.98Cl0.02 (1); BiAgSeS0.95Cl0.05 (1); BiAgSeS (1); BiAgSeS0.97Cl0.03 (1)
- dopant candidates (<5% at.): Cl (8)
- solid-solution axis: S/(S+Se) spans 0.10-0.90 (median 0.50) over 13 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 298-824 K (5th-95th pct of 72 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ag2Bi2SeS3 Imm2 (44) mp-1229130 [hull=0.062, PRIMARY]; AgBiSeS P4/mmm (123) mp-1229089 [hull=0.095, PRIMARY]
- papers: https://doi.org/10.1039/c3ee40879e (High thermoelectric performance in n-type BiAgSeS due to intrinsically...) | https://doi.org/10.1002/adfm.201402211 (Significantly Enhanced Thermoelectric Performance in n-type Heterogene...) | https://doi.org/10.1021/acsami.0c19387 (Boosting Thermoelectric Properties of AgBi3(SeyS1–y)5 Solid Solution v...)

## Ag-Cu-Ga-In-Te
- rank 483 | 14 samples | 1 papers | 14 compositions
- compositions: Cu0.8Ag0.2In0.8Ga0.2Te2 (1); Cu0.8Ag0.2In0.6Ga0.4Te2 (1); Cu0.8Ag0.2In0.5Ga0.5Te2 (1); Cu0.8Ag0.2In0.4Ga0.6Te2 (1); Cu0.8Ag0.2In0.3Ga0.7Te2 (1); Cu0.8Ag0.2In0.2Ga0.8Te2 (1)
- solid-solution axis: Ga/(Ga+In) spans 0.20-0.80 (median 0.80) over 14 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 296-853 K (5th-95th pct of 80 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): InGaCuAgTe4 I-4 (82) mp-1224000 [hull=0.012, PRIMARY]
- papers: https://doi.org/10.1021/jacs.1c01801 (Ultralow Thermal Conductivity in Diamondoid Structures and High Thermo...)

## Ag-Ga-Se
- rank 484 | 14 samples | 3 papers | 12 compositions
- compositions: Ag9GaSe6 (2); Ag9GaSe5.98 (2); Ag9Ga(Se0.92Te0.08)6 (1); Ag9Ga(Se0.95Te0.05)6 (1); Ag9Ga(Se0.88Te0.12)6 (1); Ag9Ga(Se0.9Te0.1)6 (1)
- dopant candidates (<5% at.): Te (8)
- measured range: 296-850 K (5th-95th pct of 50 curves)
- [ref 1] TEDesignLab / ICSD: GaAgSe2 I-42d (122) mp-5518 [hull=0.000, icsd=15, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ga(Ag3Se2)3 P2_13 (198) mp-27163 [hull=0.000, icsd=1, PRIMARY]; GaAgSe2 P-4m2 (115) mp-1224792 [hull=0.037]
- papers: https://doi.org/10.1016/j.joule.2017.09.006 (High Thermoelectric Performance of Ag9GaSe6 Enabled by Low Cutoff Freq...) | https://doi.org/10.1039/c7cc05935c (An argyrodite-type Ag9GaSe6 liquid-like material with ultralow thermal...) | https://doi.org/10.1016/j.mtphys.2018.05.001 (Entropy optimized phase transitions and improved thermoelectric perfor...)

## Al
- rank 485 | 14 samples | 9 papers | 2 compositions
- compositions: Al (12); Zr0.08Al99.92 (2)
- dopant candidates (<5% at.): Zr (2)
- seed hypothesis (confirm): solid_solution_alloy
- measured range: 10-923 K (5th-95th pct of 16 curves; full span incl. outliers 10-1072 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Al Fm-3m (225) mp-134 [hull=0.000, icsd=24, PRIMARY]; MnAl24Cr C2/m (12) mp-1221714 [hull=0.000, PRIMARY]; Al Im-3m (229) mp-998860 [hull=0.095, icsd=1]; Al P6_3/mmc (194) mp-1183144 [hull=0.020]
- papers: https://doi.org/10.1063/1.1145257 (Highly sensitive method for simultaneous measurements of thermal condu...) | https://doi.org/10.1063/1.1735617 (Low‐Temperature Transport Properties of Commercial Metals and Alloys. ...) | https://doi.org/10.1016/0011-2275(89)90203-8 (Impact welding: a superior method of producing joints with high therma...)

## Al-Co
- rank 486 | 14 samples | 4 papers | 8 compositions
- compositions: Al13Co4 (3); Al75Co22Ni3 (3); Al76Co22Ni2 (3); Al5(Co0.95Fe0.05)2 (1); Al5Co2 (1); Al5(Co0.99Fe0.01)2 (1)
- dopant candidates (<5% at.): Ni (6), Fe (3)
- measured range: 11-1082 K (5th-95th pct of 36 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): AlCo Pm-3m (221) mp-284 [hull=0.001, icsd=6, PRIMARY]; Al5Co2 P6_3/mmc (194) mp-196 [hull=0.000, icsd=3, PRIMARY]; AlCo3 Pm-3m (221) mp-1018101 [hull=0.122, icsd=2, PRIMARY]; Al13Co4 Pmn2_1 (31) mp-1198336 [hull=0.005, icsd=1, PRIMARY, AMBIGUOUS]; Al9Co2 P2_1/c (14) mp-16488 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1080/14786435.2010.511595 (Anisotropic transport properties of the Al13TM4and T-Al–Mn–Fe complex ...) | https://doi.org/10.2320/jinstmet.j2016053 (Electronic Structure and Thermoelectric Properties of Pseudogap Interm...) | https://doi.org/10.1088/0305-4608/16/9/017 (Structural, electrical and magnetic properties of icosahedral Al-Co al...)

## As-Ba-Fe
- rank 487 | 14 samples | 4 papers | 11 compositions
- compositions: BaFe2As2 (3); Ba(Fe0.9Co0.1)2As2 (2); Ba0.9K0.1Fe2As2 (1); BaFe1.83Co0.17As2 (1); Ba0.8K0.2Fe2As2 (1); BaFe1.84Co0.16As2 (1)
- dopant candidates (<5% at.): Co (9), K (2)
- seed hypothesis (confirm): thcr2si2_122
- measured range: 10-301 K (5th-95th pct of 21 curves; full span incl. outliers 10-360 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba4Na(FeAs)10 I4/m (87) mp-1228543 [hull=0.007, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.81.235107 (Thermoelectric properties of electron- and hole-dopedBaFe2As2) | https://doi.org/10.1209/0295-5075/84/27010 (Transport properties and superconductivity in Ba1-xMxFe2As2(M=La and K...) | https://doi.org/10.1038/s41467-019-08784-z (Giant thermoelectric power factor in ultrathin FeSe superconductor)

## As-Se-U
- rank 488 | 14 samples | 3 papers | 9 compositions
- compositions: UAsSe (2); UAs0.979Se1.021 (2); UAs0.926Se1.074 (2); UAs0.982Se1.018 (2); UAs0.99Se1.01 (2); UAs0.994Se1.006 (1)
- measured range: 10-300 K (5th-95th pct of 14 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): UAsSe P4/nmm (129) mp-22595 [hull=0.000, icsd=4, PRIMARY]; U2As3Se P4mm (99) mp-1216777 [hull=0.006, PRIMARY]; U2AsSe C2/m (12) mp-685138 [hull=0.000, PRIMARY, AMBIGUOUS]; U3As2Se P-3m1 (164) mp-1216733 [hull=0.142, PRIMARY]; U2AsSe I4_1/amd (141) mp-1173089 [hull=0.000]
- papers: https://doi.org/10.1016/s0921-4526(99)01191-6 (Anisotropy of transport properties of novel Kondo ferromagnet UAsSe) | https://doi.org/10.1016/s0921-4526(01)01337-0 (A Kondo-like thermoelectric power behaviour of UAsSe ferromagnet) | https://doi.org/10.1016/j.physb.2006.01.365 (Coherent electronic scattering in orbital-Kondo ferromagnet UAs1−xSe1+x)

## B-O-Sr-Ti
- rank 489 | 14 samples | 3 papers | 6 compositions
- compositions: (TiB2)1.4(Sr0.9Y0.1TiO3)5.4 (3); (TiB2)1.4(SrTiO3)5.5 (3); (TiB2)0.264SrTiO3 (3); (TiB2)0.264Sr0.9Y0.1TiO3 (3); Sr0.9Y0.1Ti1.25O3B0.5 (1); Sr0.95Y0.05Ti1.25O3B0.5 (1)
- dopant candidates (<5% at.): Y (8)
- seed hypothesis (confirm): composite_multiphase
- measured range: 318-1157 K (5th-95th pct of 14 curves)
- papers: https://doi.org/10.2497/jjspm.57.224 (Microstructural Control and Development of Synthesis Route for Enhanci...) | https://doi.org/10.1088/1742-6596/232/1/012005 (Transport properties of thermoelectric SrTiO3synthesized by polymerize...) | https://doi.org/10.4028/www.scientific.net/msf.706-709.1909 (Thermoelectric Properties and Densification Behavior of SrTiO<sub>3</s...)

## B-Sm
- rank 490 | 14 samples | 7 papers | 4 compositions
- compositions: SmB6 (11); Sm0.94B6 (1); Sm0.8B6 (1); Sm0.75B6 (1)
- measured range: 10-299 K (5th-95th pct of 15 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SmB6 Pm-3m (221) mp-6996 [hull=0.000, icsd=30, PRIMARY]; SmB2 P6/mmm (191) mp-10141 [hull=0.126, icsd=2, PRIMARY]; SmB4 P4/mbm (127) mp-8546 [hull=0.000, icsd=2, PRIMARY]; La(SmB8)3 Cmmm (65) mp-1223255 [hull=0.003, PRIMARY]; SmB12 Fm-3m (225) mp-1004525 [hull=0.018, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/28/35/355801 (Thermoelectric signals of state transition in polycrystalline SmB6) | https://doi.org/10.1016/j.jssc.2006.01.030 (An observation of electron phase transition in SmB6 at low temperatures) | https://doi.org/10.1016/j.isci.2020.101632 (Intrinsic Bulk Quantum Oscillations in a Bulk Unconventional Insulator...)

## Ba-Cd-Sb
- rank 491 | 14 samples | 1 papers | 14 compositions
- compositions: Ba0.99Na0.01Cd2Sb2 (1); Ba0.98Na0.02Cd2Sb2 (1); BaCd1.98Ag0.02Sb2 (1); BaCd1.94Ag0.06Sb2 (1); Ba0.7975Yb0.2Na0.0025Cd2Sb2 (1); Ba0.795Yb0.2Na0.005Cd2Sb2 (1)
- dopant candidates (<5% at.): Na (7), Ag (6), Yb (2)
- seed hypothesis (confirm): caal2si2_zintl
- measured range: 300-701 K (5th-95th pct of 17 curves)
- [ref 1] TEDesignLab / ICSD: Ba11(CdSb2)6 (12) [PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Ba2Cd2Sb3 C2/m (12) mp-1104804 [hull=0.000, icsd=1, PRIMARY]; Ba21(Cd2Sb9)2 Cmce (64) mp-684034 [hull=0.000, icsd=1, PRIMARY]; BaCdSb2 I4/mmm (139) mp-30040 [hull=0.005, icsd=1, PRIMARY]; Ba(CdSb)2 P-3m1 (164) mp-8150 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.mtphys.2019.03.002 (Experimental revelation of multiband transport in heavily doped BaCd2S...)

## Ba-Mn-O-Sm
- rank 492 | 14 samples | 4 papers | 4 compositions
- compositions: SmBaMn2O6 (10); SmBaMn2O5 (2); Sm0.9La0.24Ba0.86Mn2O6 (1); Sm0.5Ba0.5MnO3 (1)
- dopant candidates (<5% at.): La (1)
- measured range: 10-398 K (5th-95th pct of 26 curves; full span incl. outliers 10-1172 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ba5Sm8Mn4O21 I4/m (87) mp-19471 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.5096960 (Anomalous thermal conductivity across the structural transition in SmB...) | https://doi.org/10.1063/1.2034078 (1000% colossal magnetoresistance at room temperature in the A-site ord...) | https://doi.org/10.1021/acs.chemmater.9b01012 (High-Performance SmBaMn<sub>2</sub>O<sub>5+δ</sub> Electrode for Symme...)

## Bi-Cu-O-S
- rank 493 | 14 samples | 5 papers | 9 compositions
- compositions: Bi0.98Pb0.01Ca0.01CuSO (4); BiCuOS (2); BiCuSO (2); BiCuSe0.1S0.9O (1); Bi0.975Pb0.025CuOS (1); Bi0.95Pb0.05CuOS (1)
- dopant candidates (<5% at.): Pb (9), Ca (6), Se (1)
- seed hypothesis (confirm): zrcusias_1111
- measured range: 192-773 K (5th-95th pct of 42 curves; full span incl. outliers 13-774 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu2BiSO2 P4/mmm (123) mp-1206303 [hull=0.773, PRIMARY]
- papers: https://doi.org/10.3390/ma8031043 (Structure and Transport Properties of the BiCuSeO-BiCuSO Solid Solution) | https://doi.org/10.1063/1.5102141 (Comparisons of electrical/magneto-transport properties of degenerate s...) | https://doi.org/10.1021/acs.chemmater.7b04989 (Electronic Band Structure Engineering and Enhanced Thermoelectric Tran...)

## Bi-La-O-S
- rank 494 | 14 samples | 5 papers | 7 compositions
- compositions: LaOBiS2 (8); LaO0.95F0.05BiS2 (1); LaOBiS1.8Se0.2 (1); LaO0.93BiS2 (1); LaO0.95BiS2 (1); LaO0.9BiS2 (1)
- dopant candidates (<5% at.): F (1), Se (1)
- measured range: 12-967 K (5th-95th pct of 27 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaBiS2O P4/nmm (129) mp-1078397 [hull=0.005, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.4867186 (High-temperature thermoelectric properties of novel layered bismuth-su...) | https://doi.org/10.1063/1.4900953 (Enhancement of thermoelectric properties by Se substitution in layered...) | https://doi.org/10.1016/j.jallcom.2014.12.003 (Anisotropy and high thermopower of LaOBiS2)

## Ca-Fe-O
- rank 495 | 14 samples | 6 papers | 12 compositions
- compositions: Ca2Fe2O5 (2); CaFeO3 (2); Ca2Zn0.1Fe1.9O5 (1); Ca2Zn0.05Fe1.95O5 (1); Ca0.9Co0.1Fe2O4 (1); Ca0.7Co0.3Fe2O4 (1)
- dopant candidates (<5% at.): Co (3), Zn (2), Sr (2), Pr (2), Ni (2), La (1)
- seed hypothesis (confirm): brownmillerite
- measured range: 312-1173 K (5th-95th pct of 25 curves; full span incl. outliers 310-1223 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ca(FeO2)2 Pnma (62) mp-25690 [hull=0.002, icsd=22, PRIMARY]; Ca2Fe2O5 Pnma (62) mp-25750 [hull=0.010, icsd=20, PRIMARY]; CaFeO3 Pnma (62) mp-19115 [hull=0.000, icsd=18, PRIMARY]; CaFeO2 P-42_1m (113) mp-1079680 [hull=0.036, icsd=2, PRIMARY]; CaFe5O7 P2_1/m (11) mp-1195295 [hull=0.028, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2010.05.016 (p-Type thermoelectric properties of the oxygen-deficient perovskite Ca...) | https://doi.org/10.1016/j.jssc.2011.06.009 (Structural behavior and thermoelectric properties of the brownmillerit...) | https://doi.org/10.1016/j.jallcom.2003.08.073 (Thermoelectric power studies of Ca–Co ferrites)

## Cd-Sb-Zn
- rank 496 | 14 samples | 3 papers | 9 compositions
- compositions: Zn0.2Cd0.8Sb (6); (Zn0.9Cd0.1)13Sb10 (1); (Zn0.8Cd0.2)13Sb10 (1); (Zn0.6Cd0.4)13Sb10 (1); (Zn0.7Cd0.3)13Sb10 (1); (Zn0.9Cd0.1)4Sb3 (1)
- solid-solution axis: Cd/(Cd+Zn) spans 0.10-0.80 (median 0.30) over 9 compositions
     ISOELECTRONIC SERIES: the parent compound depends on the composition, not on this host. Near either end the minor element is a dilute substituent; in the middle it is a genuine alloy. Record the axis, not one parent -- and note the 5% split used the whole formula, not the sublattice, so its cut lands at a different level on each site.
- measured range: 11-342 K (5th-95th pct of 33 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): ZnCdSb2 P2_12_12_1 (19) mp-1215678 [hull=0.035, PRIMARY]
- papers: https://doi.org/10.1016/j.intermet.2011.11.021 (Preparation of the crack-free single phase (Zn1–xCdx)13Sb10 by a gradi...) | https://doi.org/10.1016/j.jallcom.2004.01.054 (Thermoelectric properties of (Zn1−xCdx)4Sb3 below room temperature) | https://doi.org/10.1007/bf01725690 (Electric and thermoelectric effects in a solid solution of ZnxCd1−xSb)

## Ce-Ge-Ru
- rank 497 | 14 samples | 2 papers | 1 compositions
- compositions: CeRu2Ge2 (14)
- seed hypothesis (confirm): thcr2si2_122
- measured range: 10-300 K (5th-95th pct of 17 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce(GeRu)2 I4/mmm (139) mp-22343 [hull=0.000, icsd=5, PRIMARY]; CeGe3Ru Pm-3n (223) mp-1198354 [hull=0.000, icsd=2, PRIMARY]; Ce3Ge13Ru4 Pm-3n (223) mp-1204084 [hull=0.039, icsd=1, PRIMARY]; Ce5Ge2Ru Pnma (62) mp-21651 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/17/11/012 (High-pressure transport properties of CeRu2Ge2) | https://doi.org/10.1103/physrevb.69.214408 (Probing the phase diagram ofCeRu2Ge2by thermopower at high pressure)

## Ce-In-Ir-Rh
- rank 498 | 14 samples | 1 papers | 1 compositions
- compositions: CeRh0.58Ir0.42In5 (14)
- measured range: 10-122 K (5th-95th pct of 14 curves)
- papers: https://doi.org/10.1038/s41535-018-0080-9 (Unconventional and conventional quantum criticalities in CeRh0.58Ir0.4...)

## Ce-Ru-Sn
- rank 499 | 14 samples | 4 papers | 9 compositions
- compositions: CeRuSn3 (4); CeRu4Sn6 (3); CeRuSn2.91 (1); CeRuSn3.03 (1); CeRuSn3.09 (1); CeRuSn2.97 (1)
- measured range: 10-554 K (5th-95th pct of 27 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce3Sn13Ru4 Pm-3n (223) mp-1198582 [hull=0.000, icsd=3, PRIMARY]; CeSnRu C2/m (12) mp-610687 [hull=0.000, icsd=3, PRIMARY]; CeSn3Ru Pm-3n (223) mp-1198476 [hull=0.000, icsd=3, PRIMARY]; Ce(Sn3Ru2)2 I-42m (121) mp-20752 [hull=0.000, icsd=1, PRIMARY]; Ce3Sn6Ru Cmcm (63) mp-1105483 [hull=0.031, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/s11664-014-3139-9 (Anisotropic Thermopower of the Kondo Insulator $$\\hbox {CeRu}_4\\hbox...) | https://doi.org/10.1088/0953-8984/1/40/023 (Electronic and magnetic properties of a new heavy-fermion compound, Ce...) | https://doi.org/10.1088/0953-8984/3/45/014 (Transport and magnetic properties of RERuSn3(RE=La, Ce, Pr, Nd, Sm): a...)

## Cl-Ru
- rank 500 | 14 samples | 2 papers | 1 compositions
- compositions: RuCl3 (14)
- measured range: 10-91 K (5th-95th pct of 14 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): RuCl3 P6_3/mcm (193) mp-22850 [hull=0.002, icsd=5, PRIMARY]; Ru3Cl I4/mmm (139) mp-974467 [hull=1.144, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.102.235155 (High-field thermal transport properties of the Kitaev quantum magnet \...) | https://doi.org/10.48550/ARXIV.2305.13268 (Spin-phonon scattering-induced low thermal conductivity in a van der W...)
