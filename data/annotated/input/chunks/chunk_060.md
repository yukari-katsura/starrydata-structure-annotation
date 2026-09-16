# Host systems -- chunk 060 of 73

Ranks 2951-3000 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 98.75%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Co-Cu-Fe-Li-O
- rank 2951 | 1 samples | 1 papers | 1 compositions
- compositions: Li0.4Cu0.6Co0.4Fe0.6O3 (1)
- sample form: pellets (1)
- measured range: 623-1023 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li4Fe2Co3Cu3O16 Cm (8) mp-767234 [hull=0.036, PRIMARY]; Li4Fe3Co2Cu3O16 Cm (8) mp-763163 [hull=0.079, PRIMARY]; Li4Fe3Co3(CuO8)2 Cm (8) mp-777062 [hull=0.055, PRIMARY]
- papers: https://doi.org/10.1016/j.ceramint.2020.01.031 (Structural and electrochemical characterization of low-cost LixCu1-xCo...)

## Co-Cu-La-Mn-O-Sr
- rank 2952 | 1 samples | 1 papers | 1 compositions
- compositions: La0.75Sr0.25Cu0.25Co0.25Mn0.5O3 (1)
- measured range: 473-1123 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.electacta.2015.10.166 (Investigations on structures, thermal expansion and electrochemical pr...)

## Co-Cu-Li-O
- rank 2953 | 1 samples | 1 papers | 1 compositions
- compositions: LiCo0.8Cu0.2O2 (1)
- sample form: Bulk (1)
- measured range: 14-1178 K (5th-95th pct of 6 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li2CoCuO4 Imma (74) mp-767275 [hull=0.047, PRIMARY]; Li3Co(CuO2)4 C2/m (12) mp-770184 [hull=0.043, PRIMARY]; Li3Co2Cu3O10 P-1 (2) mp-764235 [hull=0.068, PRIMARY]; Li3Co2CuO6 C2/m (12) mp-767299 [hull=0.105, PRIMARY]; Li3Co3CuO8 R-3m (166) mp-769624 [hull=0.142, PRIMARY]
- papers: https://doi.org/10.7567/jjap.56.021101 (Thermoelectric properties of LiCo1−xMxO2(M = Cu, Mg, Ni, Zn): Comparis...)

## Co-Cu-O-Sr-Te
- rank 2954 | 1 samples | 1 papers | 1 compositions
- compositions: Sr2CoCu2Te2O2 (1)
- sample form: Bulk (1)
- measured range: 322-768 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1039/c8tc04506b (Synthesis and the physical properties of layered copper oxytellurides ...)

## Co-Cu-S-Sn
- rank 2955 | 1 samples | 1 papers | 1 compositions
- compositions: Cu2CoSnS4 (1)
- sample form: Bulk (1)
- measured range: 298-700 K (5th-95th pct of 3 curves)
- [ref 1] TEDesignLab / ICSD: CoCu2SnS4 I-42m (121) mp-11770 [hull=0.060, icsd=1, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: Co3Cu(SnS4)2 Imm2 (44) mp-1226500 [hull=0.086, PRIMARY]; CoCu2Sn3S8 R-3m (166) mp-1226085 [hull=0.019, PRIMARY]; MnCo4Cu10(SnS4)5 I-4 (82) mp-1222130 [hull=0.046, PRIMARY]
- papers: https://doi.org/10.1039/c3mh00091e (Magnetic ions in wide band gap semiconductor nanocrystals for optimize...)

## Co-Cu-Se
- rank 2956 | 1 samples | 1 papers | 1 compositions
- compositions: Cu3Co0.5Se2 (1)
- measured range: 80-320 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1134/s0020168512080031 (Phase transitions and transport properties of Cu3Co0.5Se2 crystals)

## Co-Cu-Se-Sn
- rank 2957 | 1 samples | 1 papers | 1 compositions
- compositions: Cu2CoSnSe4 (1)
- measured range: 297-850 K (5th-95th pct of 1 curves)
- [ref 1] TEDesignLab / ICSD: CoCu2SnSe4 I-42m (121) mp-1001058 [hull=0.052, icsd=2, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: CoCu2SnSe4 I-4 (82) mp-1226100 [hull=0.062]
- papers: https://doi.org/10.1002/aelm.201600312 (Quaternary Pseudocubic Cu<sub>2</sub>TMSnSe<sub>4</sub> (TM = Mn, Fe, ...)

## Co-Dy-Fe-Sb
- rank 2958 | 1 samples | 1 papers | 1 compositions
- compositions: Dy0.9Co2.5Fe1.5Sb12 (1)
- sample form: Bulk (1)
- measured range: 323-773 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1021/acsaem.0c00794 (p-type High Temperature Thermoelectric Behavior of Dy Filled CoSb3 and...)

## Co-Dy-Mn-O
- rank 2959 | 1 samples | 1 papers | 1 compositions
- compositions: DyMn0.5Co0.5O3 (1)
- measured range: 59-298 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Dy2MnCoO6 P2_1/c (14) mp-1226407 [hull=0.440, PRIMARY]
- papers: https://doi.org/10.1063/1.3672067 (Structural, magnetic, transport and magnetocaloric properties of metam...)

## Co-Dy-Mn-Sn
- rank 2960 | 1 samples | 1 papers | 1 compositions
- compositions: Co2Dy0.5Mn0.5Sn (1)
- sample form: Bulk (1)
- measured range: 10-377 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1002/adfm.201102792 (Thermomagnetic Properties Improved by Self-Organized Flower-Like Phase...)

## Co-Dy-Sn
- rank 2961 | 1 samples | 1 papers | 1 compositions
- compositions: Co8Dy3Sn4 (1)
- sample form: Bulk (1)
- measured range: 19-373 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): DyCoSn Pnma (62) mp-22228 [hull=0.000, icsd=3, PRIMARY]; Dy12Co5Sn Immm (71) mp-1105331 [hull=0.000, icsd=1, PRIMARY]; Dy3Co6Sn5 Immm (71) mp-20703 [hull=0.018, icsd=1, PRIMARY]; DyCoSn2 Cmcm (63) mp-20579 [hull=0.064, icsd=1, PRIMARY]; Dy5(CoSn3)6 I4_1/acd (142) mp-1201480 [hull=0.023, icsd=1, PRIMARY]
- papers: https://doi.org/10.1002/adfm.201102792 (Thermomagnetic Properties Improved by Self-Organized Flower-Like Phase...)

## Co-Er-O-Sr
- rank 2962 | 1 samples | 1 papers | 1 compositions
- compositions: Sr0.7Er0.3CoO3 (1)
- measured range: 299-1123 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1149/2.0031710jes (Design of Sr<sub>0.7</sub>R<sub>0.3</sub>CoO<sub>3-δ</sub>(R = Tb and ...)

## Co-Fe
- rank 2963 | 1 samples | 1 papers | 1 compositions
- compositions: (Fe65Co35)0.67(ZnO)0.33 (1)
- dopant candidates (<5% at.): Zn (1), O (1)
- measured range: 11-292 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): FeCo Pm-3m (221) mp-2090 [hull=0.000, icsd=4, PRIMARY]; Fe11Co5 P4/mmm (123) mp-601848 [hull=0.000, icsd=1, PRIMARY]; Fe13Co3 P4/mmm (123) mp-641526 [hull=0.001, icsd=1, PRIMARY]; Fe15Co Pm-3m (221) mp-18695 [hull=0.006, icsd=1, PRIMARY]; Fe5Co3 Im-3m (229) mp-1084832 [hull=0.533, icsd=1, PRIMARY]
- papers: https://doi.org/10.1007/s11671-010-9609-y (Fabrication and Magnetic Properties of Fe65Co35–ZnO Nano-Granular Films)

## Co-Fe-Ga-V
- rank 2964 | 1 samples | 1 papers | 1 compositions
- compositions: CoFeVGa (1)
- measured range: 12-304 K (5th-95th pct of 2 curves; full span incl. outliers 12-401 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): VGaFeCo F-43m (216) mp-1066581 [hull=0.028, icsd=1, PRIMARY]; VGa2FeCo4 R-3m (166) mp-1216459 [hull=0.008, PRIMARY]
- papers: https://doi.org/10.1016/j.jmmm.2019.01.100 (Anomalous transport and magnetic behaviours of the quaternary Heusler ...)

## Co-Fe-Ge-Sb
- rank 2965 | 1 samples | 1 papers | 1 compositions
- compositions: Nd0.6Fe2Co2Sb11Ge (1)
- dopant candidates (<5% at.): Nd (1)
- measured range: 297-769 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1063/1.4819889 (Intensive suppression of thermal conductivity in Nd0.6Fe2Co2Sb12-xGex ...)

## Co-Fe-In-Sb
- rank 2966 | 1 samples | 1 papers | 1 compositions
- compositions: In0.9Fe0.9Co3.1Sb12 (1)
- measured range: 10-339 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1007/s11664-010-1117-4 (Low-Temperature Transport Properties of In x Fe y Co4−y Sb12)

## Co-Fe-La
- rank 2967 | 1 samples | 1 papers | 1 compositions
- compositions: LaCo8Fe5 (1)
- measured range: 101-337 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1063/1.4801424 (The maximal cooling power of magnetic and thermoelectric refrigerators...)

## Co-Fe-La-Mn-Ni-O-Sr
- rank 2968 | 1 samples | 1 papers | 1 compositions
- compositions: La0.7Sr0.3Co0.25Fe0.25Ni0.25Mn0.25O3 (1)
- sample form: rod-shaped (1)
- measured range: 923-1073 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.ceramint.2023.06.275 (A medium-entropy perovskite oxide La0.7Sr0.3Co0.25Fe0.25Ni0.25Mn0.25O3...)

## Co-Fe-La-Mn-O
- rank 2969 | 1 samples | 1 papers | 1 compositions
- compositions: La2Co0.5Fe0.5MnO6 (1)
- measured range: 151-298 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jallcom.2017.03.331 (Magnetic properties, resistivity and magnetoresistance effects of doub...)

## Co-Fe-Pr-Sb
- rank 2970 | 1 samples | 1 papers | 1 compositions
- compositions: PrFe3CoSb12 (1)
- measured range: 322-824 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.3938/jkps.65.2071 (Preparation and thermoelectric properties of p-type Pr z Fe4− x Co x S...)

## Co-Fe-Sb-Sn-Ti
- rank 2971 | 1 samples | 1 papers | 1 compositions
- compositions: (TiCoSb)0.8(TiFe2Sn)0.2 (1)
- measured range: 311-723 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/j.jssc.2019.04.041 (Phase stability and thermoelectric properties of TiCoSb-TiM2Sn (M = Ni...)

## Co-Ga
- rank 2972 | 1 samples | 1 papers | 1 compositions
- compositions: CoGa3 (1)
- measured range: 10-297 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): GaCo Pm-3m (221) mp-1121 [hull=0.000, icsd=7, PRIMARY]; Ga3Co P4_2/mnm (136) mp-20559 [hull=0.000, icsd=4, PRIMARY]; GaCo3 P6_3/mmc (194) mp-1184009 [hull=0.053, PRIMARY]; GaCo4 R-3m (166) mp-1224812 [hull=0.161, PRIMARY]; GaCo3 I4/mmm (139) mp-1184006 [hull=0.108]
- papers: https://doi.org/10.3762/bjnano.4.54 (Structural and thermoelectric properties of TMGa3(TM = Fe, Co) thin films)

## Co-Ge-La
- rank 2973 | 1 samples | 1 papers | 1 compositions
- compositions: LaCoGe2 (1)
- sample form: Polycrystal (1)
- measured range: 11-299 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(CoGe)2 I4/mmm (139) mp-19939 [hull=0.000, icsd=3, PRIMARY]; LaCoGe3 I4mm (107) mp-19973 [hull=0.000, icsd=3, PRIMARY]; LaCoGe P4/nmm (129) mp-20761 [hull=0.000, icsd=2, PRIMARY]; LaCoGe2 Cmcm (63) mp-1095134 [hull=0.000, icsd=2, PRIMARY]; La5CoGe3 P6_3/mcm (193) mp-1211797 [hull=0.034, PRIMARY]
- papers: https://doi.org/10.1088/0953-8984/26/25/255601 (Electrical and thermal transport properties of intermetallicRCoGe2(R= ...)

## Co-Ge-Sb-Ti
- rank 2974 | 1 samples | 1 papers | 1 compositions
- compositions: TiCoGe0.2Sb0.8 (1)
- measured range: 293-849 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/j.jallcom.2007.12.055 (Effects of Ge doping on the thermoelectric properties of TiCoSb-based ...)

## Co-Ge-Te
- rank 2975 | 1 samples | 1 papers | 1 compositions
- compositions: CoGe1.5Te1.5 (1)
- sample form: Bulk (1)
- measured range: 80-298 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co2(GeTe)3 R-3 (148) mp-2994 [hull=0.000, icsd=2, PRIMARY]; CoGeTe Pbca (61) mp-3715 [hull=0.000, icsd=2, PRIMARY]
- papers: https://doi.org/10.1016/j.jssc.2006.04.004 (Structure and thermoelectric properties of the ordered skutterudite Co...)

## Co-Hf-Mn-Sb-Zr
- rank 2976 | 1 samples | 1 papers | 1 compositions
- compositions: (Hf0.5Zr0.5)0.9Mn0.25Co0.85Sn0.1Sb0.9 (1)
- dopant candidates (<5% at.): Sn (1)
- measured range: 330-949 K (5th-95th pct of 2 curves; full span incl. outliers 330-1062 K)
- papers: https://doi.org/10.1088/0953-8984/20/25/255220 (Electronic structure of transition metal-doped XNiSn and XCoSb (X = Hf...)

## Co-Hf-P
- rank 2977 | 1 samples | 1 papers | 1 compositions
- compositions: Hf2Co12P7 (1)
- measured range: 10-297 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Hf2Co4P3 P-62m (189) mp-18581 [hull=0.000, icsd=1, PRIMARY]; Hf2CoP P2_1/m (11) mp-29154 [hull=0.000, icsd=1, PRIMARY]; HfCoP Pnma (62) mp-1095427 [hull=0.000, icsd=1, PRIMARY]; Hf4CoP P4/mcc (124) mp-1103031 [hull=0.047, icsd=1, PRIMARY]; Hf20Co5P11 Pm (6) mp-1224559 [hull=0.023, PRIMARY]
- papers: https://doi.org/10.1007/978-94-007-4984-9_3 (Thermoelectric Properties of Correlated Electron Systems Ln 3Pt4Ge6and...)

## Co-In-Sm
- rank 2978 | 1 samples | 1 papers | 1 compositions
- compositions: SmCoIn5 (1)
- measured range: 10-21 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sm2In8Co P4/mmm (123) mp-1102596 [hull=0.012, icsd=1, PRIMARY]; SmInCo2 Pmma (51) mp-1079575 [hull=0.022, icsd=1, PRIMARY]; Sm6InCo2 Immm (71) mp-646586 [hull=0.000, icsd=1, PRIMARY]; Sm12InCo6 Im-3 (204) mp-1209691 [hull=0.000, PRIMARY]; Sm2(InCo3)3 Amm2 (38) mp-672646 [hull=0.133, PRIMARY]
- papers: https://doi.org/10.1103/physrevb.97.235149 (Temperature versus Sm concentration phase diagram and quantum critical...)

## Co-Ir-Sb
- rank 2979 | 1 samples | 1 papers | 1 compositions
- compositions: Ir0.8Co0.2Sb2 (1)
- measured range: 332-863 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1016/0022-3697(96)00026-1 (Preparation and thermoelectric properties of IrxCo1 − xSb2 alloys)

## Co-La-Mg-Mn-O
- rank 2980 | 1 samples | 1 papers | 1 compositions
- compositions: La2Co0.5Mg0.5MnO6 (1)
- measured range: 262-348 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1088/2053-1591/aa6920 (Magnetic properties and magnetoresistance effect of La<sub>2</sub>Co<s...)

## Co-Li-O-Zn
- rank 2981 | 1 samples | 1 papers | 1 compositions
- compositions: LiCo0.8Zn0.2O2 (1)
- sample form: Bulk (1)
- measured range: 14-1176 K (5th-95th pct of 6 curves)
- papers: https://doi.org/10.7567/jjap.56.021101 (Thermoelectric properties of LiCo1−xMxO2(M = Cu, Mg, Ni, Zn): Comparis...)

## Co-Mn-Na-O
- rank 2982 | 1 samples | 1 papers | 1 compositions
- compositions: NaCo2.5Mn0.5O4 (1)
- sample form: Bulk (1)
- measured range: 103-600 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/s0025-5408(00)00441-4 (Magnetic and thermoelectric properties of NaCo2−xMxO4 (M = Mn, Ru))

## Co-Mn-O-Pr-Sr
- rank 2983 | 1 samples | 1 papers | 1 compositions
- compositions: PrSrMnCoO6 (1)
- measured range: 56-299 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1063/1.3556716 (Giant magnetoresistance and table-like magnetocaloric effect in double...)

## Co-Mn-O-Sr
- rank 2984 | 1 samples | 1 papers | 1 compositions
- compositions: La0.1Sr0.9Co0.7Mn0.3O3 (1)
- dopant candidates (<5% at.): La (1)
- sample form: rod-shaped (1)
- measured range: 772-1173 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr9Mn5Co2O21 R-3c (167) mp-1197208 [hull=0.036, icsd=3, PRIMARY]; Sr4Mn2CoO9 P321 (150) mp-706805 [hull=0.027, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.ssi.2006.05.023 (Synthesis and characterization of the double-substituted perovskites L...)

## Co-Mn-Sb-Sn
- rank 2985 | 1 samples | 1 papers | 1 compositions
- compositions: Co3Mn1Sb11.2Sn0.8 (1)
- measured range: 318-823 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1007/s13391-011-0306-5 (Thermoelectric properties of Co4−xMnxSb12−ySny skutterudites)

## Co-Na-O-Sr
- rank 2986 | 1 samples | 1 papers | 1 compositions
- compositions: Sr0.32Na0.21CoO2 (1)
- sample form: EpitaxialFilm (1)   <-- film/epitaxial samples present: a metastable polymorph may be reachable here that never forms in bulk
- measured range: 10-291 K (5th-95th pct of 3 curves; full span incl. outliers 10-397 K)
- papers: https://doi.org/10.1063/1.2178768 (Fabrication and thermoelectric properties of layered cobaltite, γ-Sr0....)

## Co-Na-O-Ti
- rank 2987 | 1 samples | 1 papers | 1 compositions
- compositions: Na0.4Co0.2Ti0.8O2 (1)
- measured range: 291-1072 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1016/s0272-8842(02)00050-0 (Thermoelectric characterization of NaxMx/2Ti1−x/2O2 (M=Co, Ni and Fe) ...)

## Co-Nb-Sb-V
- rank 2988 | 1 samples | 1 papers | 1 compositions
- compositions: Ta0.12Nb0.44V0.44CoSb (1)
- dopant candidates (<5% at.): Ta (1)
- measured range: 22-701 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1039/c5ra21404a (Thermal conductivity reduction by isoelectronic elements V and Ta for ...)

## Co-Nb-Sn-Zr
- rank 2989 | 1 samples | 1 papers | 1 compositions
- compositions: Nb0.8Zr0.2CoSn (1)
- measured range: 322-775 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1039/c7cp07521a (Impact of Nb vacancies and p-type doping of the NbCoSn–NbCoSb half-Heu...)

## Co-Ni-Sb-Sn
- rank 2990 | 1 samples | 1 papers | 1 compositions
- compositions: Co0.75Ni0.25Sb2.75Sn0.25 (1)
- sample form: Other (1)
- measured range: 304-772 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1007/s12613-012-0545-y (Enhanced thermoelectric properties of Co1−x−y Ni x+y Sb3−x Sn x materials)

## Co-Ni-Sb-Te
- rank 2991 | 1 samples | 1 papers | 1 compositions
- compositions: Co0.75Ni0.25Sb2.75Te0.25 (1)
- measured range: 202-942 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1063/1.1852072 (Nanostructured Co1−xNix(Sb1−yTey)3 skutterudites: Theoretical modeling...)

## Co-Ni-Si
- rank 2992 | 1 samples | 1 papers | 1 compositions
- compositions: Co0.85Ni0.15Si (1)
- measured range: 17-297 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CoSiNi Pnma (62) mp-1102115 [hull=0.011, icsd=1, PRIMARY]; CoSi4Ni R-3m (166) mp-1226006 [hull=0.000, PRIMARY]; CoSi4Ni3 Pm (6) mp-1226011 [hull=0.011, PRIMARY]
- papers: https://doi.org/10.1109/ict.2007.4569473 (Filling dependence of thermoelectric power in transition-metal monosil...)

## Co-Ni-Sn-Ti-Zr
- rank 2993 | 1 samples | 1 papers | 1 compositions
- compositions: Ti15.6Zr16.8Ni28.8Co6.8Sn30.5 (1)
- measured range: 13-957 K (5th-95th pct of 4 curves; full span incl. outliers 13-1022 K)
- papers: https://doi.org/10.1557/opl.2013.217 (Thermoelectric behaviour of p- and n- type Ti-Ni-Sn half Heusler alloy...)

## Co-O-Pb
- rank 2994 | 1 samples | 1 papers | 1 compositions
- compositions: PbCoO3 (1)
- sample form: Bulk (1)
- measured range: 96-468 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CoPbO3 R-3 (148) mp-1178420 [hull=0.081, PRIMARY]; CoPbO3 Pnma (62) mp-770082 [hull=0.170]; CoPbO3 Pbam (55) mp-770488 [hull=0.184]
- papers: https://doi.org/10.1021/jacs.7b01851 (A-Site and B-Site Charge Orderings in an s–d Level Controlled Perovski...)

## Co-O-Rh-Sr
- rank 2995 | 1 samples | 1 papers | 1 compositions
- compositions: Sr4CoRh2O9 (1)
- measured range: 345-1092 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1063/1.2828575 (Magnetic and thermoelectric properties of quasi-one-dimensional oxides...)

## Co-O-Sn
- rank 2996 | 1 samples | 1 papers | 1 compositions
- compositions: Co0.18Sn0.82O2 (1)
- measured range: 303-498 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Co2SnO4 Imma (74) mp-36028 [hull=0.000, PRIMARY]; Co3SnO8 P6_3mc (186) mp-772446 [hull=0.063, PRIMARY]; Co5SnO12 C2/m (12) mp-853132 [hull=0.138, PRIMARY]; CoSnO3 R-3 (148) mp-761574 [hull=0.036, PRIMARY]; Co2SnO4 P1 (1) mp-706412 [hull=0.018]
- papers: https://doi.org/10.1016/j.physb.2010.06.067 (The electrical, optical, structural and thermoelectrical characterizat...)

## Co-O-Sr-Zn
- rank 2997 | 1 samples | 1 papers | 1 compositions
- compositions: Sr0.7Zn0.3CoO3 (1)
- measured range: 45-376 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr3ZnCoO6 R-3c (167) mp-1191185 [hull=0.000, icsd=1, PRIMARY]; Sr12Zn2Co6O25 C2/m (12) mp-1218902 [hull=0.006, PRIMARY]
- papers: https://doi.org/10.1007/s10948-012-1488-2 (Syntheses and Magnetic-Properties of Zn-Diluted Sr-Based Perovskite Co...)

## Co-O-Tb
- rank 2998 | 1 samples | 1 papers | 1 compositions
- compositions: TbCoO3 (1)
- sample form: Bulk (1)
- measured range: 374-875 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): TbCoO3 Pnma (62) mp-24881 [hull=0.009, icsd=5, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2009.04.100 (Influence of ionic sizes of rare earths on thermoelectric properties o...)

## Co-O-Tl
- rank 2999 | 1 samples | 1 papers | 1 compositions
- compositions: Tl0.28Bi0.14CoO3 (1)
- dopant candidates (<5% at.): Bi (1)
- measured range: 11-288 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Tl3Co3O8 P2_1 (4) mp-772383 [hull=0.091, PRIMARY]; TlCoO3 R-3 (148) mp-770150 [hull=0.091, PRIMARY]; TlCoO3 P-1 (2) mp-770614 [hull=0.105]; TlCoO3 Pnma (62) mp-1101255 [hull=0.119]
- papers: https://doi.org/10.1021/cm0103850 (Large Thermopower in Metallic Misfit Cobaltites)

## Co-Sb-Sc
- rank 3000 | 1 samples | 1 papers | 1 compositions
- compositions: ScCoSb (1)
- sample form: Other (1)
- measured range: 239-380 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sc4Co3Sb4 Pm (6) mp-1219380 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2005.04.012 (Thermoelectric properties of ScCoSb, ScNi0.86Sb and MgNiSb compounds)
