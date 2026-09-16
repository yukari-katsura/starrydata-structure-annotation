# Host systems -- chunk 055 of 73

Ranks 2701-2750 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 98.27%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Bi-Br-O
- rank 2701 | 1 samples | 1 papers | 1 compositions
- compositions: BiOBr (1)
- measured range: 11-260 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BiBrO P4/nmm (129) mp-23072 [hull=0.000, icsd=5, PRIMARY]; Bi4Br2O5 P2_1 (4) mp-23544 [hull=0.000, icsd=2, PRIMARY]; Bi3BrO4 Pnna (52) mp-29447 [hull=0.014, icsd=1, PRIMARY]; Bi12Br5O16 C2/m (12) mp-1214265 [hull=0.031, PRIMARY]; Bi2Br2O P4/mmm (123) mp-1206613 [hull=0.637, PRIMARY]
- papers: https://doi.org/10.1063/1.4972047 (Influence of the reduced dimensionality on the thermodynamical and ele...)

## Bi-C-H-O-Te
- rank 2702 | 1 samples | 1 papers | 1 compositions
- compositions: (Bi2Te3)88.56(C14H14O5S2)11.44 (1)
- dopant candidates (<5% at.): S (1)
- measured range: 299-555 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1021/acsami.3c11235 (Selective Charge Carrier Transport and Bipolar Conduction in an Inorga...)

## Bi-Ca-Ce
- rank 2703 | 1 samples | 1 papers | 1 compositions
- compositions: Ca3CeBi3 (1)
- measured range: 300-460 K (5th-95th pct of 2 curves; full span incl. outliers 300-600 K)
- papers: https://doi.org/10.1039/d2dt00412g (Materials design, synthesis, and transport properties of disordered ra...)

## Bi-Ca-Co-I-O
- rank 2704 | 1 samples | 1 papers | 1 compositions
- compositions: Bi2Ca1.99Co1.44Al0.28O7I0.98 (1)
- dopant candidates (<5% at.): Al (1)
- measured range: 20-301 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1109/ict.2005.1519878 (Structural features and transport properties of iodine intercalated mi...)

## Bi-Ca-Co-O-Pb-Sr
- rank 2705 | 1 samples | 1 papers | 1 compositions
- compositions: Bi1.1Pb1.1Sr1.4Ca1.4Co2O9 (1)
- measured range: 302-976 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1109/ict.2003.1287485 (Magneto-thermoelectric effects of the layered cobalt oxides)

## Bi-Ca-Cu-Er-O-Sr
- rank 2706 | 1 samples | 1 papers | 1 compositions
- compositions: Bi2Sr2Ca2Cu2ErO10 (1)
- measured range: 50-270 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/j.jallcom.2004.04.135 (Synthesis and characterization of Er-substituted Bi-2223 H-Tc glass–ce...)

## Bi-Ca-Cu-O-Si-Sr
- rank 2707 | 1 samples | 1 papers | 1 compositions
- compositions: (Bi1.6Pb0.4)Sr2Ca3(Cu0.965Si0.35)4O12 (1)
- dopant candidates (<5% at.): Pb (1)
- measured range: 80-281 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1007/bf02562809 (Thermoelectric power of Si-doped (Bi,Pb)SrCaCuO superconducting system)

## Bi-Ca-Dy-O
- rank 2708 | 1 samples | 1 papers | 1 compositions
- compositions: Ca2Dy7Bi5O5 (1)
- measured range: 10-382 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/j.jssc.2016.04.015 (Investigation of the transport properties and compositions of the Ca2R...)

## Bi-Ca-Er-O
- rank 2709 | 1 samples | 1 papers | 1 compositions
- compositions: Er2O1.4Bi1.3(CaO)0.5 (1)
- measured range: 11-99 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1021/acs.inorgchem.8b01199 (Superconductivity in Anti-ThCr<sub>2</sub>Si<sub>2</sub>-type Er<sub>2...)

## Bi-Ca-Er-Sb
- rank 2710 | 1 samples | 1 papers | 1 compositions
- compositions: Ca3ErBi1.5Sb1.5 (1)
- measured range: 302-600 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1039/d2dt00412g (Materials design, synthesis, and transport properties of disordered ra...)

## Bi-Ca-Fe-O
- rank 2711 | 1 samples | 1 papers | 1 compositions
- compositions: Bi0.7Ca0.3FeO3 (1)
- measured range: 373-1074 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CaFe2BiO6 I4mm (107) mp-1227229 [hull=0.506, PRIMARY]
- papers: https://doi.org/10.1039/d2ra06750a (Effect of calcium doping on the electrocatalytic activity of the Bi<su...)

## Bi-Ca-Gd-O
- rank 2712 | 1 samples | 1 papers | 1 compositions
- compositions: Ca2Gd7Bi5O5 (1)
- measured range: 10-384 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/j.jssc.2016.04.015 (Investigation of the transport properties and compositions of the Ca2R...)

## Bi-Ca-Ho-Sb
- rank 2713 | 1 samples | 1 papers | 1 compositions
- compositions: Ca3HoBi1.5Sb1.5 (1)
- measured range: 301-599 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1039/d2dt00412g (Materials design, synthesis, and transport properties of disordered ra...)

## Bi-Ca-I-O-Sr
- rank 2714 | 1 samples | 1 papers | 1 compositions
- compositions: IBi2Sr2CaO8 (1)
- measured range: 50-288 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/0921-4534(92)90573-u (Structural and superconducting properties of iodine-intercalated Bi2Sr...)

## Bi-Ca-La
- rank 2715 | 1 samples | 1 papers | 1 compositions
- compositions: Ca3LaBi3 (1)
- measured range: 300-460 K (5th-95th pct of 2 curves; full span incl. outliers 300-598 K)
- papers: https://doi.org/10.1039/d2dt00412g (Materials design, synthesis, and transport properties of disordered ra...)

## Bi-Ca-La-Sb
- rank 2716 | 1 samples | 1 papers | 1 compositions
- compositions: Ca3LaBi1.5Sb1.5 (1)
- measured range: 301-598 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1039/d2dt00412g (Materials design, synthesis, and transport properties of disordered ra...)

## Bi-Ca-Lu-Sb
- rank 2717 | 1 samples | 1 papers | 1 compositions
- compositions: Ca3LuBi1.5Sb1.5 (1)
- measured range: 301-599 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1039/d2dt00412g (Materials design, synthesis, and transport properties of disordered ra...)

## Bi-Ca-Nd
- rank 2718 | 1 samples | 1 papers | 1 compositions
- compositions: Ca3NdBi3 (1)
- measured range: 300-460 K (5th-95th pct of 2 curves; full span incl. outliers 300-599 K)
- papers: https://doi.org/10.1039/d2dt00412g (Materials design, synthesis, and transport properties of disordered ra...)

## Bi-Ca-O-Sr
- rank 2719 | 1 samples | 1 papers | 1 compositions
- compositions: Bi2Sr2CaO8 (1)
- measured range: 61-294 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr8Ca3(Bi3O11)2 P2_1/c (14) mp-1208822 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/0921-4534(92)90573-u (Structural and superconducting properties of iodine-intercalated Bi2Sr...)

## Bi-Ca-Pr
- rank 2720 | 1 samples | 1 papers | 1 compositions
- compositions: Ca3PrBi3 (1)
- measured range: 301-450 K (5th-95th pct of 2 curves; full span incl. outliers 301-600 K)
- papers: https://doi.org/10.1039/d2dt00412g (Materials design, synthesis, and transport properties of disordered ra...)

## Bi-Ca-Sm
- rank 2721 | 1 samples | 1 papers | 1 compositions
- compositions: Ca3SmBi3 (1)
- measured range: 300-460 K (5th-95th pct of 2 curves; full span incl. outliers 300-599 K)
- papers: https://doi.org/10.1039/d2dt00412g (Materials design, synthesis, and transport properties of disordered ra...)

## Bi-Cd-Cs-Se
- rank 2722 | 1 samples | 1 papers | 1 compositions
- compositions: CsCdBi3Se6 (1)
- measured range: 301-701 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1039/b516790f (A new chalcogenide homologous series A2[M5+nSe9+n] (A = Rb, Cs; M = Bi...)

## Bi-Cd-Pb-S
- rank 2723 | 1 samples | 1 papers | 1 compositions
- compositions: CdPb2Bi4S9 (1)
- measured range: 295-813 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1021/acs.chemmater.9b00585 (Six Quaternary Chalcogenides of the Pavonite Homologous Series with Ul...)

## Bi-Cd-Te
- rank 2724 | 1 samples | 1 papers | 1 compositions
- compositions: Cd4Bi2Te7 (1)
- measured range: 201-299 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1039/c0cp00079e (Self-reorganization of CdTe nanoparticles into two-dimensional Bi2Te3/...)

## Bi-Ce-O
- rank 2725 | 1 samples | 1 papers | 1 compositions
- compositions: Ce2O2Bi (1)
- measured range: 12-294 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ce2BiO2 I4/mmm (139) mp-23003 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1063/1.4983280 (Magnetic and magnetotransport properties of ThCr<sub>2</sub>Si<sub>2</...)

## Bi-Ce-Se-Te
- rank 2726 | 1 samples | 1 papers | 1 compositions
- compositions: Ce0.3Bi1.7Se0.3Te2.7 (1)
- measured range: 298-473 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1002/pssa.201228589 (Thermoelectric properties of Ce-doped n-type CexBi2 − xTe2.7Se0.3nanoc...)

## Bi-Ce-Te
- rank 2727 | 1 samples | 1 papers | 1 compositions
- compositions: Ce0.3Bi1.7Te3 (1)
- measured range: 303-533 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1007/s13391-014-4139-x (Preparation and thermoelectric properties of flower-like nanoparticles...)

## Bi-Cl-K-Se
- rank 2728 | 1 samples | 1 papers | 1 compositions
- compositions: (K2Bi8Se13)68.33(BiCl3)31.67 (1)
- measured range: 303-874 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1021/jacs.6b09568 (Multiple Converged Conduction Bands in K2Bi8Se13: A Promising Thermoel...)

## Bi-Cl-O
- rank 2729 | 1 samples | 1 papers | 1 compositions
- compositions: BiOCl (1)
- measured range: 12-296 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BiClO P4/nmm (129) mp-22939 [hull=0.000, icsd=5, PRIMARY]; Bi4Cl2O5 Pnma (62) mp-651836 [hull=0.019, icsd=1, PRIMARY]; Bi3ClO4 C2/c (15) mp-29558 [hull=0.009, icsd=1, PRIMARY]; Bi12Cl5O16 C2/m (12) mp-766035 [hull=0.027, PRIMARY]; Bi2Cl2O P4/mmm (123) mp-1206832 [hull=0.755, PRIMARY]
- papers: https://doi.org/10.1063/1.4972047 (Influence of the reduced dimensionality on the thermodynamical and ele...)

## Bi-Cl-S
- rank 2730 | 1 samples | 1 papers | 1 compositions
- compositions: (Bi2S3)0.99(BiCl3) (1)
- measured range: 299-659 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): BiSCl Pnma (62) mp-23318 [hull=0.000, icsd=2, PRIMARY]; Bi5(S2Cl)3 P1 (1) mp-675345 [hull=0.063, PRIMARY]; Bi7(S3Cl)3 Pm (6) mp-676611 [hull=0.171, PRIMARY]
- papers: https://doi.org/10.1002/aenm.201100775 (Tellurium-Free Thermoelectric: The Anisotropic n-Type Semiconductor Bi2S3)

## Bi-Cl-Te
- rank 2731 | 1 samples | 1 papers | 1 compositions
- compositions: BiTeCl (1)
- measured range: 10-297 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Bi2Te4Cl7 P2_12_12_1 (19) mp-29991 [hull=0.002, icsd=2, PRIMARY]; Bi2Te7Cl8 P-1 (2) mp-30097 [hull=0.000, icsd=1, PRIMARY]; Bi3(TeCl5)2 P-1 (2) mp-623135 [hull=0.008, icsd=1, PRIMARY]; BiTeCl P6_3mc (186) mp-28944 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.scriptamat.2013.12.017 (Enhanced low-temperature thermoelectrical properties of BiTeCl grown b...)

## Bi-Co-Mg-O
- rank 2732 | 1 samples | 1 papers | 1 compositions
- compositions: Bi2Mg2CoO6 (1)
- measured range: 304-1010 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Mg14CoBiO16 P4/mmm (123) mp-1034825 [hull=0.131, PRIMARY, AMBIGUOUS]; Mg30CoBiO32 P4/mmm (123) mp-1036911 [hull=0.061, PRIMARY]; Mg6CoBiO8 P4/mmm (123) mp-1031710 [hull=0.223, PRIMARY]; Mg14CoBiO16 Pmmm (47) mp-1035048 [hull=0.135]
- papers: https://doi.org/10.1007/s10948-014-2786-7 (Synthesis and Development of Thermoelectric Properties in Layered Bi2A...)

## Bi-Co-O-Pb-Sr
- rank 2733 | 1 samples | 1 papers | 1 compositions
- compositions: Bi1.4Pb0.8Sr2Co2O9 (1)
- measured range: 287-994 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1063/1.1455157 (Thermoelectric properties of Bi2.2−xPbxSr2Co2Oy system)

## Bi-Co-Sb-Sn-Zr
- rank 2734 | 1 samples | 1 papers | 1 compositions
- compositions: ZrCoBi0.60Sb0.20Sn0.20 (1)
- measured range: 302-975 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1038/s41467-018-04958-3 (Discovery of ZrCoBi based half Heuslers with high thermoelectric conve...)

## Bi-Cs-Cu-S
- rank 2735 | 1 samples | 1 papers | 1 compositions
- compositions: Cs4Cu3Bi9S17 (1)
- measured range: 297-774 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cs3Cu2(BiS2)5 Pnnm (58) mp-669419 [hull=0.009, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/acs.chemmater.6b05298 (The New Semiconductor Cs4Cu3Bi9S17)

## Bi-Cs-Nb-O
- rank 2736 | 1 samples | 1 papers | 1 compositions
- compositions: CsBiNb2O7 (1)
- measured range: 98-599 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1063/1.3368120 (Low thermal conductivity of CsBiNb2O7 epitaxial layers)

## Bi-Cs-Se
- rank 2737 | 1 samples | 1 papers | 1 compositions
- compositions: CsBi3Se5 (1)
- measured range: 301-700 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cs2Bi8Se13 P2_1/m (11) mp-680317 [hull=0.011, icsd=1, PRIMARY]; Cs3Bi7Se12 Cm (8) mp-650619 [hull=0.000, icsd=1, PRIMARY]; Cs2Bi4Se7 P2_1/m (11) mp-1229208 [hull=0.000, PRIMARY]; Cs3Bi11Se18 Pnma (62) mp-1227437 [hull=0.028, PRIMARY]; CsBi4Se7 C2/m (12) mp-1226121 [hull=0.039, PRIMARY]
- papers: https://doi.org/10.1039/b516790f (A new chalcogenide homologous series A2[M5+nSe9+n] (A = Rb, Cs; M = Bi...)

## Bi-Cs-Se-Te
- rank 2738 | 1 samples | 1 papers | 1 compositions
- compositions: CsBi4Te5.0Se1.0 (1)
- measured range: 11-299 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1021/cm300490v (Sb and Se Substitution in CsBi4Te6: The Semiconductors CsM4Q6(M = Bi, ...)

## Bi-Cu-La-O-Sr
- rank 2739 | 1 samples | 1 papers | 1 compositions
- compositions: Bi2Sr1.4La0.6CuO6 (1)
- measured range: 44-278 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2LaCu2(BiO4)2 Cccm (66) mp-1209034 [hull=0.406, PRIMARY]; Sr3LaCu2(BiO3)4 P1 (1) mp-1173233 [hull=0.000, PRIMARY]; Sr7LaCu4(BiO3)8 P1 (1) mp-686833 [hull=0.331, PRIMARY]
- papers: https://doi.org/10.1016/0921-4534(92)90411-5 (Transport properties of Bi2Sr2-xLaxCuO6+δ)

## Bi-Cu-Mg-O-Se
- rank 2740 | 1 samples | 1 papers | 1 compositions
- compositions: Bi0.8Mg0.2CuSeO (1)
- measured range: 293-923 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1063/1.4799643 (Doping for higher thermoelectric properties in p-type BiCuSeO oxyselenide)

## Bi-Cu-Ni-O-Se
- rank 2741 | 1 samples | 1 papers | 1 compositions
- compositions: Bi0.875Ba0.125Cu0.8Ni0.2SeO (1)
- dopant candidates (<5% at.): Ba (1)
- measured range: 315-918 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1039/c7ta03659k (Enhanced thermoelectric performance of BiCuSeO by increasing Seebeck c...)

## Bi-Cu-O-Se-Yb
- rank 2742 | 1 samples | 1 papers | 1 compositions
- compositions: Bi0.70Yb0.30CuSeO (1)
- measured range: 298-872 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1039/c8tc02700e (Optimizing the thermoelectric transport properties of BiCuSeO via dopi...)

## Bi-Eu-F-O-Ti
- rank 2743 | 1 samples | 1 papers | 1 compositions
- compositions: (EuF)2Ti2Bi2O (1)
- measured range: 14-308 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1021/acs.inorgchem.2c02895 (Structure and Physical Properties of the Layered Titanium-Based Pnicti...)

## Bi-Eu-Mg-Sm
- rank 2744 | 1 samples | 1 papers | 1 compositions
- compositions: Sm0.5Eu0.5Mg2Bi1.99 (1)
- measured range: 299-772 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1039/c9ta13224d (Achieving high-performance p-type SmMg2Bi2 thermoelectric materials th...)

## Bi-Eu-Mn
- rank 2745 | 1 samples | 1 papers | 1 compositions
- compositions: EuMnBi2 (1)
- measured range: 19-340 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): EuMnBi2 I4/mmm (139) mp-1078314 [hull=0.186, icsd=1, PRIMARY]
- papers: https://doi.org/10.1103/physrevlett.122.127207 (Observation of a Magnetopiezoelectric Effect in the Antiferromagnetic ...)

## Bi-Eu-Se
- rank 2746 | 1 samples | 1 papers | 1 compositions
- compositions: EuBiSe3 (1)
- measured range: 80-290 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Eu(BiSe2)2 Pnma (62) mp-1193071 [hull=0.025, icsd=2, PRIMARY]
- papers: https://doi.org/10.1080/15567265.2019.1566937 (Thermoelectric Properties of Single Crystal EuBiSe3 Fiber)

## Bi-Eu-Zn
- rank 2747 | 1 samples | 1 papers | 1 compositions
- compositions: EuZnBi2 (1)
- measured range: 17-304 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Eu2ZnBi2 P-6m2 (187) mp-1225393 [hull=0.090, PRIMARY]
- papers: https://doi.org/10.1103/physrevlett.122.127207 (Observation of a Magnetopiezoelectric Effect in the Antiferromagnetic ...)

## Bi-Fe-La-Mn-O
- rank 2748 | 1 samples | 1 papers | 1 compositions
- compositions: La0.6Bi0.4Mn0.6Fe0.4O3.1 (1)
- measured range: 109-400 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaMnFe3(BiO4)3 Cm (8) mp-1223013 [hull=0.060, PRIMARY]
- papers: https://doi.org/10.1063/1.3646458 (Incoherent effect of Fe and Ni substitutions in the ferromagnetic-insu...)

## Bi-Fe-La-Te
- rank 2749 | 1 samples | 1 papers | 1 compositions
- compositions: La22.3Bi35.3Te37.2Fe5.2 (1)
- measured range: 294-466 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/j.matlet.2004.11.008 (Solvothermal synthesis and thermoelectric properties of lanthanum cont...)

## Bi-Fe-Ni-Si
- rank 2750 | 1 samples | 1 papers | 1 compositions
- compositions: Fe60Ni20Bi10Si10 (1)
- measured range: 315-946 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1109/tmag.1981.1061668 (Thermoelectric power singularities of FeNiBSi amorphous alloys)
