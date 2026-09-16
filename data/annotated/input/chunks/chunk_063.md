# Host systems -- chunk 063 of 73

Ranks 3101-3150 by sample count. These 50 host systems cover 50 samples (0.10% of the TE set); cumulative through this chunk: 99.04%.

Assign each host system a structural prototype from `data/annotated/taxonomy/prototypes_seed_v3.json`, or propose a new one in `taxonomy/prototypes_proposed.jsonl` first. Append results to `data/annotated/annotations/family_assignments.jsonl`.

The hand-entered MaterialFamily labels are deliberately NOT shown here -- they are held out in `df_host_systems.parquet` to validate this classification later. Decide from the compositions.

A "seed hypothesis" line means the taxonomy already names this host under that prototype. Confirm it against the compositions rather than accepting it; two or more listed means the host is mixed and needs splitting per composition.

Evidence follows the project precedence. Your judgement about the thermoelectric chemistry decides the prototype. [ref 1] is TEDesignLab, ICSD-backed and thermoelectric-specific -- prefer it. [ref 2] is Materials Project. Within a formula, polymorphs are ranked by ICSD reference count and the top one is marked PRIMARY -- not by e_above_hull, which is unusable for layered chalcogenides in the 2019 dump (Sb2Te3 R-3m carries 26 ICSD refs at hull 1.02). A primary resting on fewer than 5 ICSD references is flagged weak; the ambient phase may simply be absent from the snapshot, as it is for Bi2Se3.

While you have the host in view, also record what each minor element DOES, in `dopant_roles` -- the role follows from the prototype and cannot be judged without it. A median host has 2 such elements. Not everything listed is a dopant: O, C, N and H are usually milling or pressing residue, and an element just under 5 at.% may be an alloying end member rather than dilute doping. The doping LEVEL is computed later from the parsed fractions -- do not work it out by hand here.

A polymorph list is NOT a thermal sequence. SnSe has three known structures but only Pnma -> Cmcm happens on heating; rocksalt SnSe is metastable (2 icsd refs against 32). Put thermally reached phases in `phases` with their transition temperatures, and everything else in `other_polymorphs` with an occurrence reason. hull and icsd counts are shown to help you tell them apart.

A host may need MORE THAN ONE prototype. Transport is measured across a wide window and many thermoelectrics transform inside it, so where a "MEASUREMENT CROSSES A TRANSITION" line appears, record each phase with its own temperature range in the `phases` field. Transition temperatures shown are approximate and composition-dependent.

Both references describe which phases EXIST in a chemistry, not which phase this paper made. Al-O-Zn is best attested as ZnAl2O4 spinel (227) while almost every sample in it is Al-doped wurtzite ZnO (186). Weigh them against the compositions; do not follow them blindly.

## Cu-La-O-Ru
- rank 3101 | 1 samples | 1 papers | 1 compositions
- compositions: LaCu3Ru4O12 (1)
- sample form: Bulk (1)
- measured range: 14-911 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): LaCu3(RuO3)4 Im-3 (204) mp-680690 [hull=0.035, icsd=2, PRIMARY]
- papers: https://doi.org/10.1080/14686996.2021.1951593 (Thermoelectric materials taking advantage of spin entropy: lessons fro...)

## Cu-La-O-Se-Sr
- rank 3102 | 1 samples | 1 papers | 1 compositions
- compositions: La0.8Sr0.2CuOSe (1)
- sample form: Bulk (1)
- measured range: 369-665 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1063/1.1646438 (Thermoelectric properties of layered oxyselenides La1−xSrxCuOSe (x=0 t...)

## Cu-La-O-Te
- rank 3103 | 1 samples | 1 papers | 1 compositions
- compositions: (LaO)CuTe (1)
- measured range: 12-293 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La2CuTe2O P4/mmm (123) mp-1211660 [hull=1.342, PRIMARY]; La4Cu3TeO12 Im-3m (229) mp-1147683 [hull=0.199, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2005.04.085 (Preparation and crystal structure analysis and physical properties of ...)

## Cu-La-Sb
- rank 3104 | 1 samples | 1 papers | 1 compositions
- compositions: La3Cu3Sb4 (1)
- sample form: Polycrystal (1)
- measured range: 12-391 K (5th-95th pct of 3 curves; full span incl. outliers 12-468 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La3Cu3Sb4 I-43d (220) mp-1105594 [hull=0.000, icsd=1, PRIMARY]; LaCuSb2 P4/nmm (129) mp-1079103 [hull=0.000, icsd=1, PRIMARY]; La4Cu3Sb8 I-42m (121) mp-1223074 [hull=0.000, PRIMARY]; La4Cu5Sb8 P4mm (99) mp-1223235 [hull=0.025, PRIMARY]; La6CuSb15 Cm (8) mp-1223212 [hull=0.035, PRIMARY]
- papers: https://doi.org/10.1063/1.367018 (Magnetic and thermoelectric properties of R3Cu3Sb4 (R=La, Ce, Gd, Er))

## Cu-La-Sn
- rank 3105 | 1 samples | 1 papers | 1 compositions
- compositions: La5CuSn3 (1)
- sample form: Bulk (1)
- measured range: 11-282 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): La(CuSn)2 P4/nmm (129) mp-636264 [hull=0.000, icsd=4, PRIMARY]; LaCuSn P6_3/mmc (194) mp-20024 [hull=0.000, icsd=1, PRIMARY]; La2CuSn4 Amm2 (38) mp-1223589 [hull=0.000, PRIMARY]; LaCu5Sn Pnma (62) mp-1211431 [hull=0.000, PRIMARY]; LaCu9Sn4 I4/mcm (140) mp-1212245 [hull=0.152, PRIMARY]
- papers: https://doi.org/10.1007/s10582-004-0413-8 (Formation of Heavy-fermion State in Ce5-xLaxCuSn3)

## Cu-Li-O
- rank 3106 | 1 samples | 1 papers | 1 compositions
- compositions: LiCu2O2 (1)
- sample form: SingleCrystal (1)
- measured range: 130-299 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Li2CuO2 Immm (71) mp-4711 [hull=0.000, icsd=9, PRIMARY]; LiCuO I4/mmm (139) mp-5127 [hull=0.000, icsd=4, PRIMARY]; Li(CuO)2 Pnma (62) mp-18162 [hull=0.011, icsd=3, PRIMARY]; LiCuO2 C2/m (12) mp-9158 [hull=0.000, icsd=1, PRIMARY]; Li3CuO3 P4_2/mnm (136) mp-19970 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1023/b:inma.0000012177.38378.10 (Crystal Growth, Thermal Stability, and Electrical Properties of LiCu2O2)

## Cu-Lu-Pd
- rank 3107 | 1 samples | 1 papers | 1 compositions
- compositions: LuCu4Pd (1)
- measured range: 14-286 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Lu2CuPd Fm-3m (225) mp-1185442 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1007/bf02570277 (Low temperature hall effect and thermopower of YbCu4Au and YbCu4Pd)

## Cu-Mg-O-Rh
- rank 3108 | 1 samples | 1 papers | 1 compositions
- compositions: CuRh0.8Mg0.2O2 (1)
- measured range: 13-773 K (5th-95th pct of 2 curves)
- papers: https://doi.org/10.1109/ict.2007.4569441 (Mg substitution effects of new thermoelectric Rh oxides)

## Cu-Mn-O-Pr
- rank 3109 | 1 samples | 1 papers | 1 compositions
- compositions: Pr2CuMnO6 (1)
- measured range: 116-299 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): PrMn4(CuO4)3 Im-3 (204) mp-640853 [hull=0.024, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2021.159123 (Exotic magnetic behavior with intrinsic and extrinsic magnetodielectri...)

## Cu-Mn-O-Sr-Te
- rank 3110 | 1 samples | 1 papers | 1 compositions
- compositions: Sr2MnCu2Te2O2 (1)
- sample form: Bulk (1)
- measured range: 322-762 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1039/c8tc04506b (Synthesis and the physical properties of layered copper oxytellurides ...)

## Cu-Mn-P-Yb
- rank 3111 | 1 samples | 1 papers | 1 compositions
- compositions: YbMnCuP2 (1)
- sample form: Bulk (1)
- measured range: 310-977 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbMnCuP2 P3m1 (156) mp-1215514 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1088/0022-3727/44/15/155406 (High Seebeck coefficientAMXP2(A= Ca and Yb;M,X= Zn, Cu and Mn) Zintl p...)

## Cu-Mn-S-Sn
- rank 3112 | 1 samples | 1 papers | 1 compositions
- compositions: Cu2MnSnS4 (1)
- sample form: Bulk (1)
- measured range: 299-702 K (5th-95th pct of 4 curves)
- [ref 1] TEDesignLab / ICSD: MnCu2SnS4 I-42m (121) mp-19722 [hull=0.000, icsd=6, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: MnCu2Sn3S8 R-3m (166) mp-1221928 [hull=0.005, PRIMARY]
- papers: https://doi.org/10.1039/c3mh00091e (Magnetic ions in wide band gap semiconductor nanocrystals for optimize...)

## Cu-Mn-S-Ti
- rank 3113 | 1 samples | 1 papers | 1 compositions
- compositions: CuMn0.5Ti1.5S4 (1)
- sample form: Bulk (1)
- measured range: 14-326 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Ti3Mn(CuS4)2 R-3m (166) mp-1217139 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1080/14686996.2021.1951593 (Thermoelectric materials taking advantage of spin entropy: lessons fro...)

## Cu-Mn-Se-Sn
- rank 3114 | 1 samples | 1 papers | 1 compositions
- compositions: Cu2MnSnSe4  (1)
- measured range: 297-850 K (5th-95th pct of 1 curves)
- [ref 1] TEDesignLab / ICSD: MnCu2SnSe4 I-42m (121) mp-22400 [hull=0.000, icsd=3, PRIMARY]
- papers: https://doi.org/10.1002/aelm.201600312 (Quaternary Pseudocubic Cu<sub>2</sub>TMSnSe<sub>4</sub> (TM = Mn, Fe, ...)

## Cu-Na-O-Ru
- rank 3115 | 1 samples | 1 papers | 1 compositions
- compositions: NaCu3Ru4O12 (1)
- sample form: Bulk (1)
- measured range: 30-284 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): NaCu3(RuO3)4 Im-3 (204) mp-22305 [hull=0.014, icsd=2, PRIMARY]
- papers: https://doi.org/10.1080/14686996.2021.1951593 (Thermoelectric materials taking advantage of spin entropy: lessons fro...)

## Cu-Na-Se
- rank 3116 | 1 samples | 1 papers | 1 compositions
- compositions: Na0.162Cu2.03Se (1)
- sample form: Bulk (1)
- measured range: 323-673 K (5th-95th pct of 5 curves)
- [ref 1] TEDesignLab / ICSD: NaCuSe P4/nmm (129) mp-7433 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.3390/app8010012 (Na-Doping Effects on Thermoelectric Properties of Cu2−xSe Nanoplates)

## Cu-Nd-P-Zn
- rank 3117 | 1 samples | 1 papers | 1 compositions
- compositions: NdCuZnP2 (1)
- sample form: Bulk (1)
- measured range: 303-792 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1039/d0mh01112f (Experimental validation of high thermoelectric performance in RECuZnP2...)

## Cu-Ni-O
- rank 3118 | 1 samples | 1 papers | 1 compositions
- compositions: (Ni0.47Cu0.53)(SiO2)0.04 (1)
- dopant candidates (<5% at.): Si (1)
- curator composition details (from the paper): 10vol.%SiO2 (1)
- measured range: 304-1073 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu(NiO2)2 Fd-3m (227) mp-769689 [hull=0.004, PRIMARY]; Cu2Ni11O13 Immm (71) mp-761502 [hull=0.020, PRIMARY]; Cu2NiO4 I4_1/a (88) mp-771115 [hull=0.095, PRIMARY]; Cu6NiO6 Fm-3m (225) mp-1147668 [hull=0.237, PRIMARY]; CuNi3O4 Cmmm (65) mp-761415 [hull=0.065, PRIMARY]
- papers: https://doi.org/10.1016/s0925-8388(03)00295-0 (Thermoelectric properties of constantan/spherical SiO2 and Al2O3 parti...)

## Cu-Ni-S
- rank 3119 | 1 samples | 1 papers | 1 compositions
- compositions: Cu10.4Ni4S13 (1)
- sample form: Bulk (1)
- measured range: 301-692 K (5th-95th pct of 5 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuNi3S8 R-3 (148) mp-1225702 [hull=0.012, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2015.02.045 (Structural stability of the synthetic thermoelectric ternary and nicke...)

## Cu-Ni-S-Sn
- rank 3120 | 1 samples | 1 papers | 1 compositions
- compositions: Cu2NiSnS4 (1)
- sample form: Bulk (1)
- measured range: 302-440 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu2NiSn3S8 R-3m (166) mp-1225853 [hull=0.013, PRIMARY]; Cu2NiSnS4 I-4 (82) mp-1225842 [hull=0.027, PRIMARY]; CuNi3(SnS4)2 Imm2 (44) mp-1225814 [hull=0.062, PRIMARY]
- papers: https://doi.org/10.1016/j.matlet.2015.03.083 (Optical and thermoelectric properties of chalcogenide based Cu2NiSnS4 ...)

## Cu-Ni-Sn-Ti
- rank 3121 | 1 samples | 1 papers | 1 compositions
- compositions: TiNiCu0.20Sn (1)
- sample form: Bulk (1)
- measured range: 308-774 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1016/j.scriptamat.2020.09.010 (Fast synthesis of n-type half-heusler TiNiSn thermoelectric material)

## Cu-Ni-Sn-Zr
- rank 3122 | 1 samples | 1 papers | 1 compositions
- compositions: ZrNiCu0.20Sn (1)
- measured range: 305-949 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/j.mtphys.2023.101049 (The role of interstitial Cu on thermoelectric properties of ZrNiSn hal...)

## Cu-O-S-Sc-Sr
- rank 3123 | 1 samples | 1 papers | 1 compositions
- compositions: Sr3Cu2Sc2O5S2 (1)
- curator composition details (from the paper): polycrystalline (1)
- measured range: 149-449 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr3Sc2Cu2S2O5 I4/mmm (139) mp-15900 [hull=0.041, icsd=1, PRIMARY]
- papers: https://doi.org/10.1063/1.2817643 (A promising p-type transparent conducting material: Layered oxysulfide...)

## Cu-O-S-Sr
- rank 3124 | 1 samples | 1 papers | 1 compositions
- compositions: Sr1.8Ca0.2CuO2S2 (1)
- dopant candidates (<5% at.): Ca (1)
- curator composition details (from the paper): polycrystalline (1)
- measured range: 31-296 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sr2Cu3(SO)2 I4/mmm (139) mp-7112 [hull=0.130, icsd=1, PRIMARY]; Sr2CuSO2 P4/mmm (123) mp-1147582 [hull=0.180, PRIMARY]
- papers: https://doi.org/10.1063/1.2173638 (Electronic nature of layered oxysulfide Sr2−xCaxCu2CoO2S2 with CoO2 pl...)

## Cu-O-Sr-Te-Zn
- rank 3125 | 1 samples | 1 papers | 1 compositions
- compositions: Sr2ZnCu2Te2O2 (1)
- sample form: Bulk (1)
- measured range: 326-754 K (5th-95th pct of 3 curves)
- papers: https://doi.org/10.1039/c8tc04506b (Synthesis and the physical properties of layered copper oxytellurides ...)

## Cu-P-Pr-Zn
- rank 3126 | 1 samples | 1 papers | 1 compositions
- compositions: PrCuZnP2 (1)
- sample form: Bulk (1)
- measured range: 303-790 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1039/d0mh01112f (Experimental validation of high thermoelectric performance in RECuZnP2...)

## Cu-P-Si
- rank 3127 | 1 samples | 1 papers | 1 compositions
- compositions: CuSi2P3 (1)
- measured range: 32-394 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Cu4SiP8 I4_1/a (88) mp-28995 [hull=0.000, icsd=1, PRIMARY]; Cu2SiP4 I4_1/a (88) mp-1213539 [hull=0.263, PRIMARY]; CuSi2P3 Cm (8) mp-674984 [hull=0.055, PRIMARY]; CuSi4P3 R3m (160) mp-1225800 [hull=0.175, PRIMARY]; CuSi2P3 P3m1 (156) mp-1225670 [hull=0.107]
- papers: https://doi.org/10.1039/b914555a (Composition, structure, bonding and thermoelectric properties of “CuT2...)

## Cu-P-Yb-Zn
- rank 3128 | 1 samples | 1 papers | 1 compositions
- compositions: YbCuZnP2 (1)
- sample form: Bulk (1)
- measured range: 311-982 K (5th-95th pct of 5 curves; full span incl. outliers 311-1073 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbZnCuP2 P3m1 (156) mp-1215494 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1088/0022-3727/44/15/155406 (High Seebeck coefficientAMXP2(A= Ca and Yb;M,X= Zn, Cu and Mn) Zintl p...)

## Cu-Pb-S-Sb
- rank 3129 | 1 samples | 1 papers | 1 compositions
- compositions: PbCuSbS3 (1)
- measured range: 18-301 K (5th-95th pct of 2 curves; full span incl. outliers 18-607 K)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuSbPbS3 Pmn2_1 (31) mp-649774 [hull=0.004, icsd=4, PRIMARY]
- papers: https://doi.org/10.1002/cphc.201500476 (Bournonite PbCuSbS3: Stereochemically Active Lone-Pair Electrons that ...)

## Cu-Pb-Se-Te
- rank 3130 | 1 samples | 1 papers | 1 compositions
- compositions: PbTe(Cu2Se)0.12 (1)
- sample form: Bulk (1)
- measured range: 304-754 K (5th-95th pct of 5 curves)
- papers: https://doi.org/10.1088/0022-3727/49/6/065302 (Thermoelectric transport properties of PbTe-based composites incorpora...)

## Cu-Ru-Sn
- rank 3131 | 1 samples | 1 papers | 1 compositions
- compositions: CuRu4Sn6 (1)
- sample form: Polycrystal (1)
- measured range: 10-98 K (5th-95th pct of 4 curves; full span incl. outliers 10-265 K)
- papers: https://doi.org/10.1016/j.physb.2005.01.111 (Electronic properties of semiconducting)

## Cu-S-Se-Ti
- rank 3132 | 1 samples | 1 papers | 1 compositions
- compositions: Cu0.25TiSe0.5S1.5 (1)
- measured range: 300-699 K (5th-95th pct of 1 curves)
- papers: https://doi.org/10.1016/j.jallcom.2015.02.021 (Tuned thermoelectric properties of TiS1.5Se0.5 through copper intercal...)

## Cu-S-Sn-Tl
- rank 3133 | 1 samples | 1 papers | 1 compositions
- compositions: Tl2Cu2SnS4 (1)
- measured range: 81-300 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Tl2Cu2SnS4 Ibam (72) mp-18240 [hull=0.027, icsd=1, PRIMARY]
- papers: https://doi.org/10.1021/cm050412c (Exploring Thallium Compounds as Thermoelectric Materials:  Seventeen N...)

## Cu-S-V
- rank 3134 | 1 samples | 1 papers | 1 compositions
- compositions: CuV2S4 (1)
- measured range: 15-298 K (5th-95th pct of 1 curves)
- [ref 1] TEDesignLab / ICSD: VCu3S4 P-43m (215) mp-3762 [hull=0.002, icsd=10, PRIMARY]
- [ref 2] MP, ranked by ICSD evidence: V2CuS4 I-4m2 (119) mp-1104259 [hull=0.059, icsd=7, PRIMARY, AMBIGUOUS]; V4Cu3S8 R3m (160) mp-29211 [hull=0.086, icsd=1, PRIMARY]; V3(CuS2)4 R3m (160) mp-1208142 [hull=0.229, PRIMARY]; V7(CuS6)2 P-1 (2) mp-1216478 [hull=0.054, PRIMARY]; VCuS4 Imma (74) mp-1216385 [hull=0.373, PRIMARY]
- papers: https://doi.org/10.1016/j.physb.2005.01.345 (High-pressure study of the metallic spinel CuV2S4)

## Cu-Sb-Se-Tl
- rank 3135 | 1 samples | 1 papers | 1 compositions
- compositions: Tl11.5Sb11.5Cu8Se27 (1)
- measured range: 81-301 K (5th-95th pct of 2 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Tl14Cu8(SbSe3)9 P2/m (10) mp-1210510 [hull=0.025, PRIMARY]
- papers: https://doi.org/10.1021/cm050412c (Exploring Thallium Compounds as Thermoelectric Materials:  Seventeen N...)

## Cu-Sb-Sr-Zn
- rank 3136 | 1 samples | 1 papers | 1 compositions
- compositions: SrZn0.25Cu0.5Sb (1)
- sample form: Bulk (1)
- measured range: 301-971 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1016/j.jallcom.2019.152508 (Structure transition and thermoelectric properties related to AZn(1-x)...)

## Cu-Sb-Te
- rank 3137 | 1 samples | 1 papers | 1 compositions
- compositions: (Cu4Te3)0.5(Bi0.5Sb1.5Te3)0.5 (1)
- dopant candidates (<5% at.): Bi (1)
- sample form: Bulk (1)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): CuSbTe2 R3m (160) mp-1225707 [hull=1.065, PRIMARY]
- papers: https://doi.org/10.1063/1.2745413 (High thermoelectric properties of p-type pseudobinary (Cu4Te3)x–(Bi0.5...)

## Cu-Sb-U
- rank 3138 | 1 samples | 1 papers | 1 compositions
- compositions: UCu0.9Sb2 (1)
- sample form: SingleCrystal (1)
- measured range: 10-282 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): U3Cu3Sb4 I-43d (220) mp-1188951 [hull=0.135, icsd=2, PRIMARY]; U3Cu2Sb3 P6_3/mmc (194) mp-30070 [hull=0.060, icsd=1, PRIMARY]; UCuSb2 P4/nmm (129) mp-1079070 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2005.05.027 (Single-crystalline study of the ferromagnetic kondo compound UCu0.9Sb2)

## Cu-Sb-Y
- rank 3139 | 1 samples | 1 papers | 1 compositions
- compositions: Y3Cu3Sb4 (1)
- measured range: 11-297 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YCuSb2 P4/nmm (129) mp-19943 [hull=0.000, icsd=2, PRIMARY]; Y3Cu3Sb4 I-43d (220) mp-1106051 [hull=0.000, icsd=1, PRIMARY]
- papers: https://doi.org/10.1109/ict.2006.331231 (Galvanomagnetic and Thermoelectric Properties of R3Cu3Sb4 Compounds)

## Cu-Sb-Yb
- rank 3140 | 1 samples | 1 papers | 1 compositions
- compositions: YbCu0.52Sb (1)
- sample form: SingleCrystal (1)
- measured range: 307-838 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YbCuSb P6_3mc (186) mp-11701 [hull=0.000, icsd=1, PRIMARY, AMBIGUOUS]; YbCuSb2 P4/nmm (129) mp-1078982 [hull=0.035, icsd=1, PRIMARY]; Yb2CuSb3 P4/mmm (123) mp-1206807 [hull=2.805, PRIMARY]; YbCuSb P6_3/mmc (194) mp-9439 [hull=0.001, icsd=1]
- papers: https://doi.org/10.1016/j.jallcom.2020.156551 (YbCu0.52(2)Sb: Mixed-valent compound with a layered structure)

## Cu-Se-Sm
- rank 3141 | 1 samples | 1 papers | 1 compositions
- compositions: Cu5SmSe4 (1)
- sample form: Bulk (1)
- measured range: 91-373 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): SmCuSe2 P2_1/c (14) mp-11793 [hull=0.000, icsd=3, PRIMARY]; Sm31(CuSe16)3 P1 (1) mp-1173540 [hull=0.046, PRIMARY]; Sm3CuSe6 Pca2_1 (29) mp-1219332 [hull=0.026, PRIMARY]; Sm5CuSe8 I-4 (82) mp-38162 [hull=0.076, PRIMARY]
- papers: https://doi.org/10.1134/s0020168513010123 (Transport properties of Cu5SmSe4)

## Cu-Se-Sn-Te-Zn
- rank 3142 | 1 samples | 1 papers | 1 compositions
- compositions: Cu2.2Zn0.8SnSe3.6Te0.4 (1)
- sample form: Bulk (1)
- measured range: 298-697 K (5th-95th pct of 4 curves)
- papers: https://doi.org/10.1039/c5dt00910c (Synthesis, crystal structure, and transport properties of Cu2.2Zn0.8Sn...)

## Cu-Se-V
- rank 3143 | 1 samples | 1 papers | 1 compositions
- compositions: Cu3VSe4 (1)
- sample form: Bulk (1)
- measured range: 324-572 K (5th-95th pct of 5 curves)
- [ref 1] TEDesignLab / ICSD: VCu3Se4 P-43m (215) mp-21855 [hull=0.000, icsd=4, PRIMARY]
- papers: https://doi.org/10.1016/j.jallcom.2021.160387 (Thermoelectric properties of p-Type Cu3VSe4 with high seebeck coeffici...)

## Cu-Sm-Te
- rank 3144 | 1 samples | 1 papers | 1 compositions
- compositions: Cu3SmTe3 (1)
- sample form: Bulk (1)
- measured range: 297-899 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Sm(CuTe)3 R-3 (148) mp-1219189 [hull=0.044, PRIMARY]; Sm2CuTe4 P2_1 (4) mp-1219248 [hull=0.030, PRIMARY]
- papers: https://doi.org/10.1021/acsami.0c09918 (Ternary Compounds Cu3RTe3 (R = Y, Sm, and Dy): A Family of New Thermoe...)

## Cu-Sn-Te-Tl
- rank 3145 | 1 samples | 1 papers | 1 compositions
- compositions: Tl2Cu2SnTe4 (1)
- measured range: 80-299 K (5th-95th pct of 3 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Tl2Cu2SnTe4 Fmm2 (42) mp-1216636 [hull=0.028, PRIMARY]
- papers: https://doi.org/10.1021/cm050412c (Exploring Thallium Compounds as Thermoelectric Materials:  Seventeen N...)

## Cu-Te-Tm
- rank 3146 | 1 samples | 1 papers | 1 compositions
- compositions: TmCuTe2 (1)
- sample form: Bulk (1)
- measured range: 298-872 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Tm(CuTe)3 Pmn2_1 (31) mp-640889 [hull=0.000, icsd=1, PRIMARY]; TmCuTe2 P3m1 (156) mp-1216671 [hull=0.031, PRIMARY]; Tm(CuTe)3 R-3 (148) mp-1216875 [hull=0.054]; TmCuTe2 P-3m1 (164) mp-1206396 [hull=0.099]
- papers: https://doi.org/10.1002/chem.201404453 (Chemical Modification and Energetically Favorable Atomic Disorder of a...)

## Cu-Te-Y
- rank 3147 | 1 samples | 1 papers | 1 compositions
- compositions: Cu3YTe3 (1)
- sample form: Bulk (1)
- measured range: 298-899 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Y(CuTe)3 R-3 (148) mp-1216225 [hull=0.029, PRIMARY]; Y4CuTe8 Pc (7) mp-675009 [hull=0.000, PRIMARY]; YCuTe2 P2/m (10) mp-945184 [hull=0.000, PRIMARY]
- papers: https://doi.org/10.1021/acsami.0c09918 (Ternary Compounds Cu3RTe3 (R = Y, Sm, and Dy): A Family of New Thermoe...)

## Cu-Y
- rank 3148 | 1 samples | 1 papers | 1 compositions
- compositions: YCu2 (1)
- curator composition details (from the paper): annealed in an evacuated quartz tube at 700 "C for one week (1)
- sample form: Polycrystal (1)
- measured range: 12-274 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): YCu Pm-3m (221) mp-712 [hull=0.021, icsd=7, PRIMARY]; YCu2 Imma (74) mp-2698 [hull=0.000, icsd=4, PRIMARY]; YCu5 P6/mmm (191) mp-2797 [hull=0.000, icsd=4, PRIMARY]; Y2Cu3 Cmcm (63) mp-1190402 [hull=0.620, icsd=1, PRIMARY]; Y4Cu19Pb R3m (160) mp-1216359 [hull=0.028, PRIMARY]
- papers: https://doi.org/10.1088/0305-4608/15/9/015 (CeCu2: a new Kondo lattice showing magnetic order)

## Cu-Zn
- rank 3149 | 1 samples | 1 papers | 1 compositions
- compositions: Zn58.71Cu41.29 (1)
- sample form: Bulk (1)
- measured range: 10-338 K (5th-95th pct of 4 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Zn8Cu5 I-43m (217) mp-1368 [hull=0.000, icsd=6, PRIMARY]; ZnCu Pm-3m (221) mp-987 [hull=0.007, icsd=3, PRIMARY]; Zr(Zn10Cu)2 Fd-3m (227) mp-1195710 [hull=0.000, icsd=1, PRIMARY]; Zn3Cu P6_3/mmc (194) mp-972042 [hull=0.001, PRIMARY]; Zn35Cu17 P1 (1) mp-1216020 [hull=0.004, PRIMARY]
- papers: https://doi.org/10.1063/1.3043884 (Correlation between structural and low-temperature thermoelectric prop...)

## Dy
- rank 3150 | 1 samples | 1 papers | 1 compositions
- compositions: Dy (1)
- measured range: 162-200 K (5th-95th pct of 1 curves)
- [ref 2] MP, ranked by ICSD evidence (no TEDesignLab entry): Dy P6_3/mmc (194) mp-1184067 [hull=0.000, icsd=9, PRIMARY]; Dy R-3m (166) mp-10658 [hull=0.000, icsd=3]; Dy Fm-3m (225) mp-10750 [hull=0.015, icsd=2]; Dy Im-3m (229) mp-10751 [hull=0.139, icsd=1]
- papers: https://doi.org/10.1109/tasc.2004.831058 (Thermal Property of Magnetic Materials for Hydrogen Magnetic Refrigera...)
